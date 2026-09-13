#!/usr/bin/env python3
"""
tests/test_e45_exact_ramp.py -- regression tests for the E45 exact near-CUE laws.

WHY
  E45 constructed laws whose grid form factor is EXACTLY the ramp, so the ceiling theorem's numeric
  hypothesis holds with tolerance zero.  These laws are the reason the E44 gap closes on our own instance,
  so their exactness is locked here: any change that breaks the ramp identity, the nonnegativity of the
  weights, or the derived edge bound will fail immediately.

THE LAWS (weights w = u + t*sqrt(D), positions are grid indices m with x = N*m/Q, Q = 2N, unit marks)
  N = 4, Q = 8,  D = 2 : {(0,2,6,7) : 1/2 - 1/4*sqrt2 , (0,3,5,7) : 1/2 + 1/4*sqrt2}
  N = 6, Q = 12, D = 3 : six configurations with weights in Q(sqrt3), all nonnegative
Both give S(j) = j/N exactly for j = 1..N, hence D(1) = 1/(2N) exactly (so d1 = 1/8 and 1/12).

PROVENANCE
  Written 2026-09-13 by 小灵 for the E45 continuation (item 6: no test suite).  Sources:
  docs/E45-ceiling-law-construction.md sections 9-14, scripts/E45_nearcue_exact_attainment.py,
  scripts/E45_nearcue_instance_data.py.  Run: python3 -m pytest tests/ -q
"""

from fractions import Fraction as F

import pytest

# cos(2*pi*r/Q) = a + b*sqrt(D) ; only the two grids used by the laws
COS = {
    8: {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(0), F(0)), 3: (F(0), F(-1, 2)),
        4: (F(-1), F(0)), 5: (F(0), F(-1, 2)), 6: (F(0), F(0)), 7: (F(0), F(1, 2))},
    12: {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(1, 2), F(0)), 3: (F(0), F(0)),
         4: (F(-1, 2), F(0)), 5: (F(0), F(-1, 2)), 6: (F(-1), F(0)), 7: (F(0), F(-1, 2)),
         8: (F(-1, 2), F(0)), 9: (F(0), F(0)), 10: (F(1, 2), F(0)), 11: (F(0), F(1, 2))},
}
D_OF = {8: 2, 12: 3}

LAWS = {
    4: [((0, 2, 6, 7), (F(1, 2), F(-1, 4))),
        ((0, 3, 5, 7), (F(1, 2), F(1, 4)))],
    6: [((0, 2, 5, 7, 9, 10), (F(-11, 30), F(4, 15))),
        ((0, 1, 2, 4, 6, 9), (F(28, 15), F(-14, 15))),
        ((0, 3, 5, 6, 8, 11), (F(-1, 3), F(1, 3))),
        ((2, 3, 4, 8, 10, 11), (F(8, 15), F(-4, 15))),
        ((3, 5, 6, 7, 10, 11), (F(-19, 30), F(2, 5))),
        ((0, 2, 4, 6, 8, 9), (F(-1, 15), F(1, 5)))],
}


def values(N, Q, pos, j):
    """|F(j)|^2 = a + b*sqrt(D) exactly (unit marks)"""
    a = F(0); b = F(0)
    for k1 in range(len(pos)):
        for k2 in range(len(pos)):
            ca, cb = COS[Q][(j * (pos[k1] - pos[k2])) % Q]
            a += ca; b += cb
    return a, b


def nonneg(u, t, D):
    if t == 0:
        return u >= 0
    if t > 0:
        return True if u >= 0 else (D * t * t >= u * u)
    return u >= 0 and u * u >= D * t * t


@pytest.mark.parametrize("N", [4, 6])
def test_weights_are_a_probability_law(N):
    Q, D = 2 * N, D_OF[2 * N]
    law = LAWS[N]
    assert sum(u for _, (u, _) in law) == 1
    assert sum(t for _, (_, t) in law) == 0
    assert all(nonneg(u, t, D) for _, (u, t) in law)


@pytest.mark.parametrize("N", [4, 6])
def test_ramp_holds_exactly_and_through_the_edge(N):
    """sum_c w_c |F_c(j)|^2 = j for j = 1..N  (the edge row included, hence S(j) = j/N for all j)"""
    Q, D = 2 * N, D_OF[2 * N]
    for j in range(1, N + 1):
        s1 = F(0); s2 = F(0)
        for pos, (u, t) in LAWS[N]:
            a, b = values(N, Q, pos, j)
            s1 += u * a + D * t * b
            s2 += u * b + t * a
        assert (s1, s2) == (j, 0), "ramp fails at j=%d" % j


@pytest.mark.parametrize("N,expected_d1", [(4, F(1, 8)), (6, F(1, 12))])
def test_edge_bound_is_one_over_twice_N(N, expected_d1):
    """C(1) = (N+1)/(2N) because S(j) = j/N on every row, hence D(1) = 1/(2N) and d1 = 1/(2N)"""
    C1 = sum(F(j, N * N) for j in range(1, N + 1))
    assert C1 == F(N + 1, 2 * N)
    D1 = C1 - F(1, 2)
    assert D1 == F(1, 2 * N)
    assert D1 == expected_d1
