#!/usr/bin/env python3
"""
tests/test_e44_enclosure.py -- regression tests for the E44 audit of the frontier's ceiling enclosure.

WHY
  The project has no executable test suite (see docs/TESTING.md): the many files named `*_test.py` under
  scripts/ are exploration scripts, not tests, and pytest collects nothing from them.  These tests lock
  in the numbers that E44 verified, so that a future edit to the audit script or to the staged data is
  caught immediately instead of silently changing a published result.

WHAT IS LOCKED
  * K = 2^140 and the 256 enclosure pairs of data/lawN256_encl_v1.0.json, each of width 1, each bracketing
    j*2^132 at an endpoint (so the 255 row inequalities at tolerance 3e-40 follow);
  * the exact rational D(1) computed from the table lies below the recorded bound 82395317/10^8 with the
    recorded margin, and is positive;
  * the ceiling constant p0 is exactly the recorded fraction, is <= 0.6818287, and its denominator
    factors as 2^43 * 5^39;
  * the theorem's constant step 1/(6*256^2) + (3e-40)/512 <= 2.5431316e-6.

PROVENANCE
  Written 2026-09-13 by 小灵 for the E45 continuation (item 6: no test suite).  Sources: docs/E44-ceiling-
  encl-audit.md, scripts/E44_ceiling_encl_audit.py, data/lawN256_encl_v1.0.json.
  Run: python3 -m pytest tests/ -q
"""

import json
import os
from fractions import Fraction as F

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "lawN256_encl_v1.0.json")


@pytest.fixture(scope="module")
def blob():
    with open(DATA, encoding="utf-8") as fh:
        return json.load(fh)


def test_scale_is_a_power_of_two(blob):
    assert blob["N"] == 256
    assert blob["K"] == 2 ** 140


def test_enclosure_table_shape(blob):
    en = blob["encl"]
    assert len(en) == 256
    assert all(hi - lo == 1 for lo, hi in en)


def test_rows_bracket_the_ramp(blob):
    """the 255 near-CUE rows: each interval brackets j*2^132 at an endpoint"""
    K = blob["K"]
    tau = F(blob["tau"][0], blob["tau"][1])
    worst = F(0)
    for j, (lo, hi) in enumerate(blob["encl"][:255], start=1):
        target = j * 2 ** 132
        assert lo <= target <= hi, "row %d does not bracket the ramp" % j
        worst = max(worst, abs(256 * F(lo, K) - j), abs(256 * F(hi, K) - j))
    assert worst == F(256, K)                    # exactly 2^-132
    assert worst <= tau                          # the recorded tolerance holds
    assert tau / worst == F(3, 10 ** 40) * F(K, 256) or float(tau / worst) > 1.6


def test_edge_bound_reproduces(blob):
    """D(1) = C(1) - 1/2 from the table lies below the recorded bound, with the recorded margin"""
    N, K = blob["N"], blob["K"]
    loN, hiN = blob["encl"][N - 1]
    sum_j = sum(range(1, N))
    lo = (F(sum_j * 2 ** 132 - (N - 1), K) + F(loN, K)) / N - F(1, 2)
    hi = (F(sum_j * 2 ** 132, K) + F(hiN, K)) / N - F(1, 2)
    bound = F(blob["D1_num"], blob["D1_den"])
    assert lo > 0                                 # the recorded sign
    assert hi <= bound                            # the recorded bound holds
    margin = bound - hi
    assert 9e-9 < float(margin) < 1e-8            # margin of record is 9.287e-9


def test_ceiling_constant(blob):
    p0 = F(blob["p0_num"], blob["p0_den"])
    assert p0 == F(10909258999421303588095230195816054408197,
                   16000000000000000000000000000000000000000)
    assert p0 <= F(6818287, 10 ** 7)
    assert blob["p0_den"] == 2 ** 43 * 5 ** 39
    assert float(p0) == pytest.approx(0.6818286874638315, abs=1e-15)


def test_theorem_constant_step(blob):
    N = blob["N"]
    tau = F(blob["tau"][0], blob["tau"][1])
    c = F(1, 6 * N * N) + tau / (2 * N)
    assert c <= F(25431316, 10 ** 13)
    assert float(c) == pytest.approx(2.5431315104166666e-06, rel=1e-9)
