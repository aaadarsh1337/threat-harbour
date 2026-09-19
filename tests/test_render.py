"""Unit tests for scripts/render.py pure functions (no matplotlib needed).

Run: pytest tests/test_render.py
"""

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import render as r


def minimal_payload(**overrides):
    base = {
        "collected_at_utc": "2026-09-19T03:36:26Z",
        "totals": {"total_events": 100, "bad_json_lines": 1},
        "sources": {
            "unique_source_ips": 5,
            "top_source_net16_by_event_volume": [
                {"cidr": "109.160.0.0/16", "events": 60}
            ],
        },
        "sessions": {
            "unique_session_ids": 10,
            "session_connect_events": 10,
            "session_duration_seconds": {
                "n_closed_matched": 10,
                "median": 2.4,
                "max": 100.0,
                "under_10s": 7,
            },
        },
        "protocols": {"ssh": 100},
        "logins": {
            "success_fake": 8,
            "failed": 2,
            "top_usernames": [{"value": "root", "count": 5}],
            "top_passwords": [{"value": "123456", "count": 3}],
        },
        "commands": {
            "input_events": 20,
            "failed_command_events": 1,
            "top_commands": [{"input": "uname -a", "count": 10}],
        },
        "behavioral_command_categories": {"discovery": 18, "other": 2},
        "downloads_uploads": {
            "file_download_events": 2,
            "file_upload_events": 1,
            "top_destfiles": [],
            "top_shasums": [{"value": "a8460f44" + "0" * 56, "count": 2}],
        },
        "event_ids": {"cowrie.session.connect": 10},
        "collection": {
            "files": 2,
            "file_lines": {"cowrie.json": 50, "cowrie.json.2026-09-18": 50},
            "file_open_errors": {},
            "per_day_utc": {"2026-09-18": 50, "2026-09-19": 50},
        },
    }
    base.update(overrides)
    return base


def test_fmt_and_short_date():
    assert r.fmt(357922) == "357,922"
    assert r.short_date("2026-09-06T20:36:00Z") == "2026-09-06"


def test_md_cell_escapes_attacker_input():
    assert r.md_cell("a|b") == "a\\|b"
    assert r.md_cell("a`b") == "a'b"
    assert r.md_cell("a\x00b\x1fc") == "abc"
    assert r.md_cell("") == "?"
    long = "x" * 100
    assert r.md_cell(long).endswith("…")
    assert len(r.md_cell(long)) == 61  # 60 + ellipsis


def test_validate_payload_ok():
    r.validate_payload(minimal_payload())  # must not raise


def test_validate_payload_missing_keys():
    bad = minimal_payload()
    del bad["logins"]
    with pytest.raises(ValueError, match="payload missing keys"):
        r.validate_payload(bad)


def test_validate_payload_bad_date():
    bad = minimal_payload(collected_at_utc="not-a-date")
    with pytest.raises(ValueError):
        r.validate_payload(bad)


def test_missing_days_gap():
    per_day = {"2026-08-27": 10, "2026-08-29": 5}
    assert r.missing_days(per_day, "2026-08-29") == ["2026-08-28"]
    assert r.missing_days(per_day, "2026-08-20") == []  # end < start
    assert r.missing_days(per_day, "bad-date") == []


def test_build_metrics_no_gap_note():
    import datetime
    p = minimal_payload()
    # Fill every day OBS_START..cutoff so missing_days() finds no gap.
    start = datetime.date(2026, 8, 27)
    end = datetime.date(2026, 9, 19)
    d = start
    full = {}
    while d <= end:
        full[d.isoformat()] = 5
        d += datetime.timedelta(days=1)
    p["collection"]["per_day_utc"] = full
    p["collection"]["file_lines"] = {"cowrie.json": sum(full.values())}
    m = r.build_metrics(p)
    assert m["analysis_cutoff_utc"] == "2026-09-19T03:36:26Z"
    assert "no missing days" in m["collection"]["sensor_uptime_note"]
    assert m["stack"]["cowrie"] == "3.0.13"


def test_build_metrics_gap_note():
    p = minimal_payload()
    # OBS_START is 2026-08-27; per_day missing those days -> gap note.
    p["collection"]["per_day_utc"] = {"2026-09-19": 100}
    m = r.build_metrics(p)
    assert "zero events" in m["collection"]["sensor_uptime_note"]


def test_stack_versions_pinned():
    # Single source of truth for published stack; update together with
    # docs/deployment.md + configs/ when upgrading.
    assert r.STACK == {
        "cowrie": "3.0.13",
        "grafana": "10.2.3",
        "loki": "2.9.4",
        "promtail": "2.9.4",
    }


def test_readme_block_contains_key_rows():
    m = r.build_metrics(minimal_payload())
    block = r.readme_block(m)
    assert "109.160.0.0/16" in block
    assert "`root`" in block
    assert "authorized_keys" in block


def test_bucket_weekly_monthly():
    per_day = {"2026-09-01": 10, "2026-09-02": 20, "2026-10-01": 5}
    weeks = r._bucket_weekly(per_day)
    assert sum(c for _, c in weeks) == 35
    months = r._bucket_monthly(per_day)
    assert sum(c for _, c in months) == 35
    assert len(months) == 2  # Sep + Oct
