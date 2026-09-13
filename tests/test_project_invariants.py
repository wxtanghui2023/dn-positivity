#!/usr/bin/env python3
"""
tests/test_project_invariants.py -- protocol and infrastructure invariants for the dn-project.

WHY
  The project's discipline requires that every verification computation be a committed script, that outputs
  be archived, and that scripts carry provenance headers.  Until now that discipline was enforced by a
  standalone checker run by hand (scripts/check_archive.py).  These tests turn it into an executable
  invariant, and add two more: the Lean tree must compile, and the staged audit data must stay parseable.

WHAT IS TESTED
  * scripts/check_archive.py exits 0 (archive protocol: tracked scripts, no /tmp writes, headers, outputs);
  * data/lawN256_encl_v1.0.json is parseable and carries its provenance fields.

⚠️ DELIBERATELY NOT TESTED HERE: Lean compilation.
  The Lean tree was verified once (2026-09-13: 16 files, all exit 0, no sorries) and that result is on
  record in lean/README.md.  Re-running it on every test pass burns compute for no new information, so
  唐先生's directive of 2026-09-13 11:47 stands: RUN LEAN ONLY WHEN THE PAPERS ARE FINALISED.
  The milestone command is therefore kept in docs/TESTING.md, not in this suite.

PROVENANCE
  Written 2026-09-13 by 小灵 for the E45 continuation (item 6: no test suite).
  Run: python3 -m pytest tests/ -q
"""

import glob
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_archive_protocol_checker_passes():
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "check_archive.py")],
                       capture_output=True, text=True, cwd=ROOT, timeout=300)
    assert r.returncode == 0, r.stdout + r.stderr


@pytest.mark.skip(reason="Lean runs only at paper finalisation (唐先生 2026-09-13 11:47); see docs/TESTING.md")
def test_lean_tree_compiles_DISABLED():
    """REMOVED from routine testing by directive.  Kept as a stub only to document what was verified
    once and where the milestone command lives (docs/TESTING.md).  Do not re-enable in the suite."""
    pass


def test_staged_audit_data_is_intact():
    p = os.path.join(ROOT, "data", "lawN256_encl_v1.0.json")
    with open(p, encoding="utf-8") as fh:
        blob = json.load(fh)
    for key in ("provenance", "N", "K", "tau", "D1_num", "D1_den", "p0_num", "p0_den", "encl"):
        assert key in blob, "missing key %s" % key
    prov = blob["provenance"]
    assert prov["source_sha256"] == "11ae9f7dcc1747f68b51c44f057641ba20bd623b2abea04849b612e716903c6e"
    assert "zeta-23-lean" in prov["source_url"]
