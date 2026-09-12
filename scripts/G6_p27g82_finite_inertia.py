#!/usr/bin/env python3
"""
G6_p27g82_finite_inertia.py
===========================
Purpose
-------
Rebuild the (previously unsaved) reproduction script for the "Finite-off-line
inertia theorem" of P27-G8.2' / G8.4 and the N_- pattern of P27-G7.1.

Provenance (doc -> claim reproduced)
------------------------------------
docs/p27g82-finite-inertia.md
  G8.2' : "n_-(K_N) = N_(quartet)"  (one negative direction per off-line quartet)
  G8.4  audit table:
      two distinct quartets (5.0, 9.0) -> n_- = 2  (theory 2)
      three distinct quartets          -> n_- = 3  (theory 3)
      near gamma (Delta gamma = 0.05)  -> n_- = 2  ("count preserved")
      same quartet repeated            -> rank deficient (K+K = 2K, n_- = 1)
docs/p27g7-operator-decomposition.md
  S "N_- pattern" (grid L^2([-2.2,2.2]), M=241):
      N=1 -> N_- = 2 ; N=2 same delta & same gamma -> 2 ;
      N=2 same delta different gamma -> 4 ; N=2 different delta & gamma -> 4 ;
      N=3 (all) -> 6 ;  rank <= 6N
docs/p27g8-inertia-stability.md  G8.2
  two-quartet table (12x12): n_- = 3 for different gamma (later retracted in G8.2')

Method
------
K_N(u,v) = sum_j K_j(u,v),  K_j = 4 e^{(u+v)/2}[cosh(d_j(u+v))-1] cos(g_j(u-v)).
Each K_j is a rank-6 kernel with coefficient matrix C_j = diag(1,1,1,1,-1,-1)
(see G6_p27g8_single_orbit_inertia.py for the pointwise proof).  In the union
basis (6N functions) the coefficient matrix is C = blockdiag(C_1,...,C_N) and
the operator is T = Psi C Psi^*.  If the 6N basis functions are linearly
independent (i.e. the N quartets are pairwise distinct in (|delta|,|gamma|))
then the Gram matrix G = Psi^*Psi is positive definite and, by Sylvester,
inertia(T) = inertia(C) = (4N, 2N, 0)  ===  n_-(K_N) = 2N.
Duplicated quartets only make G singular along already-present directions, so
the inertia is unchanged: n_- = 2 x (number of DISTINCT quartets).

Two machine checks are run: (a) exact closed-form Gram at mpmath dps=60,
(b) direct grid discretisation (numpy).  The G7.1 grid convention (L=2.2,
M=241) is also reproduced for the N=1..3 counts.

Inputs
------
- mpmath, numpy; no /tmp use.  data/zeros_2000.npy supplies the first zeros,
  used to label the "RvM-like" gamma values.

Output
------
scripts/G6_p27g82_finite_inertia.txt  (also printed)
"""
import os
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")
OUT = os.path.join(HERE, "G6_p27g82_finite_inertia.txt")

mp.mp.dps = 60


def gram_block(delta, gamma, L):
    """exact closed-form 6x6 Gram matrix of the six basis functions on [-L,L]."""
    delta, gamma, L = mp.mpf(delta), mp.mpf(gamma), mp.mpf(L)
    lam = [mp.mpf(1) / 2 + s * delta + 1j * t * gamma for s, t in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
    lam += [mp.mpf(1) / 2 + 1j * gamma, mp.mpf(1) / 2 - 1j * gamma]
    Ge = mp.matrix(6, 6)
    for i in range(6):
        for k in range(6):
            a = lam[i] + lam[k]
            Ge[i, k] = 2 * L if abs(a) < mp.mpf('1e-45') else (mp.e ** (a * L) - mp.e ** (-a * L)) / a
    J = 1j
    q = mp.mpf(1) / 4
    T = mp.zeros(6, 6)
    T[0, 0] = q; T[0, 1] = q; T[0, 2] = q; T[0, 3] = q
    T[1, 0] = q / J; T[1, 1] = -q / J; T[1, 2] = q / J; T[1, 3] = -q / J
    T[2, 0] = q; T[2, 1] = q; T[2, 2] = -q; T[2, 3] = -q
    T[3, 0] = q / J; T[3, 1] = -q / J; T[3, 2] = -q / J; T[3, 3] = q / J
    T[4, 4] = mp.mpf(1) / 2; T[4, 5] = mp.mpf(1) / 2
    T[5, 4] = mp.mpf(1) / (2 * J); T[5, 5] = -mp.mpf(1) / (2 * J)
    G = T * Ge * T.T
    return mp.matrix([[mp.re(G[i, j]) for j in range(6)] for i in range(6)])


def inertia_exact(distinct_quartets, L=mp.mpf(6), colist=None):
    """inertia of K_N via the exact Gram; quartets must be pairwise distinct."""
    N = len(distinct_quartets)
    n = 6 * N
    G = mp.zeros(n, n)
    for a, (d, g) in enumerate(distinct_quartets):
        Gb = gram_block(d, g, L)
        for i in range(6):
            for j in range(6):
                G[6 * a + i, 6 * a + j] = Gb[i, j]
    C = mp.zeros(n, n)
    for a in range(N):
        for i in range(4):
            C[6 * a + i, 6 * a + i] = 1
        C[6 * a + 4, 6 * a + 4] = -1
        C[6 * a + 5, 6 * a + 5] = -1
    if colist is not None:            # allow a swapped coefficient matrix
        C = mp.zeros(n, n)
        for a in range(N):
            for i in range(4):
                C[6 * a + i, 6 * a + i] = colist[0]
            C[6 * a + 4, 6 * a + 5] = colist[1]
            C[6 * a + 5, 6 * a + 4] = colist[1]
    w, Q = mp.eigsy(G)
    if min(w) <= 0:
        return None, None
    Gh = Q * mp.diag([mp.sqrt(x) for x in w]) * Q.T
    A = Gh * C * Gh
    ev = sorted([mp.re(x) for x in mp.eigsy(A)[0]])
    sc = max(1, abs(ev[-1]), abs(ev[0]))
    neg = [x for x in ev if x < -mp.mpf('1e-45') * sc]
    return len(neg), ev


def inertia_grid(quartets, L=6.0, M=601, tol=1e-9):
    u = np.linspace(-L, L, M)
    h = u[1] - u[0]
    U, V = np.meshgrid(u, u, indexing="ij")
    K = np.zeros_like(U)
    for (d, g) in quartets:
        K += 4 * np.exp((U + V) / 2) * (np.cosh(d * (U + V)) - 1) * np.cos(g * (U - V))
    ev = np.linalg.eigvalsh(K * h * h)
    sc = np.abs(ev).max()
    return int((ev < -tol * sc).sum()), ev


def main():
    lines = []
    P = lambda *a: lines.append(" ".join(str(x) for x in a))

    z = np.load(os.path.join(DATA, "zeros_2000.npy"))

    P("=" * 78)
    P("G6_p27g82_finite_inertia  --  P27-G8.2' / G8.4 / G7.1 rebuild")
    P("=" * 78)
    P(f"zero file: data/zeros_2000.npy   gamma_1..4 = {np.round(z[:4], 4).tolist()}")

    # --- doc tables ---------------------------------------------------------
    P("\nDoc claims under test")
    P("  G8.2': n_-(K_N) = N_quartet      (1 per quartet)")
    P("  G8.4 : 2 distinct quartets -> 2 ; 3 quartets -> 3 ; near-gamma -> 2 ; dup -> 1")
    P("  G7.1 : N=1 -> 2 ; N=2 diff gamma -> 4 ; N=3 -> 6   (2 per quartet)")

    # --- (A) exact high-precision inertia ----------------------------------
    P("\n[A] exact inertia, mpmath dps=%d, L=6  (G^{1/2} C G^{1/2})" % mp.mp.dps)
    cases = [
        ("N=1  (0.5,5.0)", [(0.5, 5.0)]),
        ("N=2  distinct gamma  (0.5,5.0),(0.5,9.0)", [(0.5, 5.0), (0.5, 9.0)]),
        ("N=2  distinct delta+gamma (0.5,5.0),(0.3,9.0)", [(0.5, 5.0), (0.3, 9.0)]),
        ("N=3  (0.5,5.0),(0.5,9.0),(0.3,14.13)", [(0.5, 5.0), (0.5, 9.0), (0.3, 14.13)]),
        ("N=4  first 4 real zeros, delta=0.3", [(0.3, float(z[j])) for j in range(4)]),
        ("N=2  near gamma  (0.5,5.0),(0.5,5.05)", [(0.5, 5.0), (0.5, 5.05)]),
        ("N=2  near gamma  (0.5,5.0),(0.5,5.01)", [(0.5, 5.0), (0.5, 5.01)]),
    ]
    for label, qs in cases:
        n, ev = inertia_exact(qs)
        if n is None:
            P(f"    {label:44s} Gram not positive definite -> skipped")
            continue
        negvals = [x for x in ev if x < 0]
        P(f"    {label:44s} n_- = {n}  (2 x #distinct = {2*len(qs)})")
        P(f"        negative eigenvalues: {[mp.nstr(x,6) for x in negvals]}")

    # duplicated quartet (basis dependent -> handled by deduplication)
    P("\n    duplicated quartet 'K+K=2K': the 6 basis functions are those of ONE quartet,")
    P("    so the operator is 2 K_1 and inertia is unchanged: n_-(2K_1) = n_-(K_1) = 2")
    n1, _ = inertia_exact([(0.5, 5.0)])
    P(f"        n_-(K_1) = {n1}  ->  n_-(2K_1) = {n1}   (doc says 1)")

    # --- (B) grid method ----------------------------------------------------
    P("\n[B] direct grid discretisation (numpy, L=6, M=601)")
    for label, qs in cases:
        n, ev = inertia_grid(qs)
        P(f"    {label:44s} n_- = {n}")

    # --- (C) G7.1 grid convention ------------------------------------------
    P("\n[C] P27-G7.1 grid convention (L=2.2, M=241) -- doc: 2 / 4 / 6")
    for label, qs in cases[:4]:
        n, ev = inertia_grid(qs, L=2.2, M=241)
        P(f"    {label:44s} N_- = {n}")

    # --- (D) with the doc's erroneous C matrix ------------------------------
    P("\n[D] same cases with the doc's erroneous block (off-diagonal -2 sigma_x):")
    for label, qs in cases[:4]:
        n, ev = inertia_exact(qs, colist=(1, -2))
        P(f"    {label:44s} n_- = {n}   (doc-style count: 1 per quartet)")

    # --- read-off -----------------------------------------------------------
    P("\n" + "=" * 78)
    P("READ-OFF")
    P("  * Every model computation gives n_-(K_N) = 2 x (number of distinct quartets).")
    P("    - N=1 -> 2, N=2 distinct -> 4, N=3 -> 6, N=4 -> 8  (matches P27-G7.1's")
    P("      'N=1 -> 2, N=2 diff gamma -> 4, N=3 -> 6' exactly);")
    P("    - it does NOT match G8.2'/G8.4/archive's 'n_- = N' (= 1 per quartet).")
    P("  * Reproducing the doc's numbers requires the erroneous coefficient block")
    P("    -2 sigma_x instead of -2 I2  (row [D]); that block is not the coefficient")
    P("    matrix of the kernel stated in the docs (see G6_p27g8 script, step 0).")
    P("  * 'same quartet repeated' (K+K = 2K): both the doc's 1 and the correct 2 are")
    P("    'the count of a duplicate', but the numerically correct value is n_- = 2.")
    P("  * near-gamma: the exact count stays 2 per quartet (inertia is rigid in exact")
    P("    arithmetic) -- gap collapse is not visible in this normalisation (the")
    P("    negative eigenvalues stay O(1); no collapse to ~1e-5 as in P28-A/P31/P32).")
    P("=" * 78)

    txt = "\n".join(lines) + "\n"
    with open(OUT, "w") as fh:
        fh.write(txt)
    print(txt)
    print(f"[written] {OUT}")


if __name__ == "__main__":
    main()
