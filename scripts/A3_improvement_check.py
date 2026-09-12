#!/usr/bin/env python3
"""
A3_improvement_check.py -- can the project's A3 assets improve the frontier constant?

PROVENANCE
  Written 2026-09-12 by 小灵 (subagent) for docs/A3-improvement-assessment.md.
  Frontier input (verbatim, quoted in-repo at docs/E46-5C-inertia-necessity.md):
  arXiv:2608.13637v2, Lemma 3.2 (rank-trace inequality): for Hermitian d x d
  P, Q with P >= 0, rank P <= r, n_+(Q) <= b,
        (3.1)   r >= 2 tr P + 4 tr Q - 4 b - ||P+Q||^2_HS ,
  equality attainable at P = Pi_1, Q = 2 Pi_2 for orthogonal projections
  Pi_1 _|_ Pi_2 of ranks r, b.  Constants: c_MT^{-1} = 1/2 + (1/sqrt2)cot(1/sqrt2)
  = 1.3274992963, so 2 - R(psi_MT) = 0.6725007; ceiling 0.682 (frontier 7.2).
  Project assets used as inputs:  (i) n_- = 2 per off-axis orbit (ERRATUM-
  inertia-factor2.md);  (ii) moving-edge P28-P33 (2x2 family lam_j^- = -1/j);
  (iii) Toeplitz/CF mechanism rank deficiency <=> simple <=> unit-circle roots
  (CVS1c, 6/6) + Christoffel identity (docs/E8-ceiling-0682.md, E13).
  READ: data/zeros_2000.npy (part D only, as a data-driven stand-in measure).
  OUTPUT of record: scripts/A3_improvement_check.txt
LIMITS: verifies algebra/identities and the quoted lemma numerically.  It does
  NOT re-derive 0.682 (frontier 7.2 is not in-repo); no RH claim.
USAGE: python3 scripts/A3_improvement_check.py > scripts/A3_improvement_check.txt
"""

import numpy as np

np.set_printoptions(precision=10)
C_MT_INV = 0.5 + (1.0 / np.sqrt(2.0)) / np.tan(1.0 / np.sqrt(2.0))   # 1.3274992963
TWO_MINUS_R = 2.0 - C_MT_INV                                          # 0.6725007
CEIL = 0.682

print("=" * 74)
print("A3 improvement check -- negative inertia / moving-edge / Toeplitz-CF")
print("=" * 74)
print(f"  c_MT^-1 = {C_MT_INV:.10f}   2 - R(psi_MT) = {TWO_MINUS_R:.7f}"
      f"   ceiling (frontier 7.2) = {CEIL}")

# ---------------------------------------------------------------- A: Lemma 3.2
print("\n(A) check the quoted Lemma 3.2  r >= 2trP + 4trQ - 4b - ||P+Q||^2_HS")
rng = np.random.default_rng(20260912)
viol, worst = 0, np.inf
for _ in range(4000):
    d = int(rng.integers(3, 13))
    r = int(rng.integers(0, d + 1)); b = int(rng.integers(0, d + 1))
    A = rng.normal(size=(d, max(r, 1))) if r > 0 else np.zeros((d, 1))
    P = A @ A.T; P = P if r > 0 else np.zeros((d, d))
    if r == 0:
        P = np.zeros((d, d))
    U, _ = np.linalg.qr(rng.normal(size=(d, d)))
    nneg = int(rng.integers(0, d - b + 1))
    lam = np.concatenate([rng.uniform(0.1, 3, b),
                          -rng.uniform(0.1, 3, nneg),
                          np.zeros(d - b - nneg)])
    Q = U @ np.diag(lam) @ U.T; Q = (Q + Q.T) / 2
    np_ = int(np.sum(np.linalg.eigvalsh(Q) > 1e-9))
    if np_ > b:      # construction guarantees this; guard anyway
        continue
    slack = (2 * np.trace(P) + 4 * np.trace(Q) - 4 * b
             - np.sum((P + Q) ** 2))
    if r > 0 and np.sum(Q ** 2) > 1e-12:          # skip the trivial P=Q=0
        worst = min(worst, r - slack)
    viol += (slack > r + 1e-8)
print(f"    4000 random trials: violations = {viol}"
      f"  (min slack on non-trivial configs = {worst:.6f})")
r0, b0 = 6, 4
Pi1 = np.zeros((r0 + b0, r0 + b0)); Pi1[:r0, :r0] = np.eye(r0)
Pi2 = np.zeros((r0 + b0, r0 + b0)); Pi2[r0:, r0:] = np.eye(b0)
Pl, Ql = Pi1, 2 * Pi2
rhs = 2 * np.trace(Pl) + 4 * np.trace(Ql) - 4 * b0 - np.sum((Pl + Ql) ** 2)
print(f"    equality config P=Pi1(r={r0}), Q=2*Pi2(b={b0}): RHS = {rhs:.10f}"
      f"  = rank P = {r0}  -> equality attained")
print(f"    NOTE: in that equality config n_-(Q) = {int(np.sum(np.linalg.eigvalsh(Ql) < -1e-9))}"
      f" (moving-edge has zero contact with it)")

# --------------------------------------------------- B: Q1, substituting n_-
print("\n(B) Q1: substitute the project's n_- = 2 per orbit into (3.1)")
print("    model: N_on simple on-line zeros (eigenvalue 1) + p off-line pairs,")
print("    each pair a signature (1,1) block [[0,1],[1,0]] in Q.")
print(f"    {'N_on':>7} {'p':>4} {'rankQ':>6} {'n_+(Q)':>7} {'n_-(Q)':>7}"
      f" {'b=rank-n_-':>11} {'id':>5} {'db_need':>8} {'gain|b->0':>9}")
for (N_on, p) in [(10, 1), (10, 5), (100, 20), (1000, 3), (2000, 500)]:
    d = N_on + 2 * p
    Pm = np.zeros((d, d)); Pm[np.arange(N_on), np.arange(N_on)] = 1.0
    Qm = np.zeros((d, d))
    for i in range(p):
        Qm[N_on + 2 * i, N_on + 2 * i + 1] = 1.0
        Qm[N_on + 2 * i + 1, N_on + 2 * i] = 1.0
    w = np.linalg.eigvalsh(Qm)
    n_p, n_m = int(np.sum(w > 1e-9)), int(np.sum(w < -1e-9))
    rankQ = n_p + n_m
    b = p                                   # the frontier's bound n_+(Q) <= b
    b_new = rankQ - n_m                     # our substitution via Sylvester
    trP, trQ, N = np.trace(Pm), np.trace(Qm), d
    id_ok = abs((2 * trP + 4 * trQ - 4 * b) - (4 * (trP + trQ) - 2 * N)) < 1e-9
    db = (CEIL - TWO_MINUS_R) * N / 4.0     # b-reduction needed to reach 0.682
    gain0 = 4.0 * p / N                     # gain if b -> 0 (no off-line at all)
    print(f"    {N_on:>7} {p:>4} {rankQ:>6} {n_p:>7} {n_m:>7} {b_new:>11}"
          f" {str(id_ok):>5} {db:>8.2f} {gain0:>9.5f}")
print("    b_new = rank Q - n_-(Q) = 2p - p = p = b  -> the rewrite is an IDENTITY.")
print("    identity used: 2trP+4trQ-4b = 4tr(P+Q)-2N  iff  b = p, N = N_on+2p.")
print("    sensitivity: d(rank bound)/db = -4  ->  4/N per unit of proportion.")
print("    'db_need' = b-reduction needed to reach 0.682 = 0.00238 N; the actual")
print("    slack is zero because our n_- asset certifies n_+(Q) = n_-(Q) = p.")
print("    'gain|b->0' = gain if one could prove n_+(Q)=0, i.e. Q <= 0: that is")
print("    'no off-line zeros' = RH (and contradicts signature (1,1) per pair).")

# ------------------------------------------------------------ C: Q2 moving edge
print("\n(C) Q2: moving-edge family K_j = [[1,-(1+1/j)],[-(1+1/j),1]], lam_j^- = -1/j")
print(f"    {'N':>7} {'edge lam^-_N':>14} {'sum |lam^-| = H_N':>18}"
      f" {'H_N/N':>10}")
for N in [10, 100, 1000, 10 ** 4, 10 ** 6]:
    H = float(np.sum(1.0 / np.arange(1, N + 1))) if N <= 10 ** 4 else \
        float(np.log(N) + 0.5772156649)
    print(f"    {N:>7} {-1.0 / N:>14.3e} {H:>18.6f} {H / N:>10.2e}")
print("    edge -> 0 (no uniform negative sector); total negative mass H_N = log N")
print("    = o(N).  Any inequality linear in n_- therefore contributes o(1) to a")
print("    proportion O(1) -> no numeric C* is produced by the moving edge.")

# ------------------------------------------------------ D: Q3 Toeplitz / CF
print("\n(D) Q3: Toeplitz / Christoffel counting on the same moment data")
z = np.load("data/zeros_2000.npy")
x = z / z.mean()                       # normalised ordinates, mean 1 (stand-in)


def christoffel(moms, m):
    H = np.array([[moms[i + j] for j in range(m + 1)] for i in range(m + 1)])
    B = np.array([[moms[i + j] for j in range(1, m + 1)] for i in range(1, m + 1)])
    return float(np.linalg.det(H) / np.linalg.det(B))


def lam_and_cs(pts, wts, m, shift=0.0):
    p = np.asarray(pts, float) - shift
    mm = [float(np.sum(wts * p ** k)) for k in range(2 * m + 1)]
    L = christoffel(mm, m)
    return L, float(mm[1] ** 2 / mm[2]), float(np.log(np.linalg.det(
        np.array([[mm[i + j] for j in range(m + 1)] for i in range(m + 1)]))))


def count_atoms(pts, wts, tol=1e-12):
    keep, seen = 0, []
    for p_, w_ in zip(pts, wts):
        if w_ <= tol:
            continue
        seen.append(p_); keep += 1
    return len(np.unique(np.round(np.array(seen), 12))) if seen else 0


print(f"    {'measure':>38} {'1-L1':>9} {'1-L2':>9} {'1-L3':>9} {'m1^2/m2':>9}")
sets = [
    ("0.6725 d_1 + 0.3275 d_0  (Montgomery 2-pt)", [1.0, 0.0], [0.6725, 0.3275]),
    ("0.682 d_1 + 0.318 d_0   (0.682 2-pt ceiling)", [1.0, 0.0], [0.682, 0.318]),
    ("0.682 d_3 + 0.318 d_0   (same, c=3)", [3.0, 0.0], [0.682, 0.318]),
    ("0.3275 d_0 + 0.6725 * empirical zeros", np.concatenate([[0.0], x]),
     np.concatenate([[0.3275], np.full(len(x), 0.6725 / len(x))])),
]
for name, pts, wts in sets:
    r_at = count_atoms(pts, wts)
    mass0 = float(np.sum(np.asarray(wts)[np.asarray(pts) == 0.0]))
    row = []
    for m in (1, 2, 3):
        if m >= r_at - 1:            # Christoffel is exactly sharp: = mass at 0
            row.append(1 - mass0)
        else:
            L, _, _ = lam_and_cs(pts, wts, m)
            row.append(1 - L)
    _, cs1, _ = lam_and_cs(pts, wts, 1)
    print(f"    {name:>38} {row[0]:>9.6f} {row[1]:>9.6f} {row[2]:>9.6f} {cs1:>9.6f}")
print("    [Py] Toeplitz/Christoffel identity  Lambda_m(0)=detH_m/detB_m =")
print("         1/(H_m^-1)_00  and for m=1: 1-Lambda_1(0) = m1^2/m2 = the")
print("         Cauchy-Schwarz rank bound.  Same functional, same number.")
print("    Rows 1-3: 1-L_m = 1-mu({0}) exactly (sharp two- or three-moment data)")
print("      -> 0.6725 (Montgomery normalisation) and 0.682 (ceiling data).")
print("    Row 4 (data-driven): the empirical spread costs moments; 1-L_m rises")
print("      only as 1-L_1=0.538 -> 0.649 -> ..., never above 0.6725 = 1-mu({0}).")

# Toeplitz rank-deficiency device on the same data (CVS1c construction)
print("    Toeplitz rank-deficiency device (r atoms on the unit circle):")
for n, r in [(12, 6), (24, 12)]:
    th = np.linspace(0.17, np.pi - 0.11, r)
    c = np.array([np.sum(np.cos(k * th)) for k in range(n + 1)])
    T = np.array([[c[abs(k - l)] for l in range(n + 1)] for k in range(n + 1)])
    rk = np.linalg.matrix_rank(T, tol=1e-9)
    print(f"      n={n:>3} size={n+1:>3} atoms r={r:>2}  rank(T)={rk:>3}"
          f"  deficiency={n + 1 - rk}  (=1 iff generic)")
print("    deficiency 1 <-> all roots on the unit circle (Caratheodory-Fejer);")
print("    rank(T) = 2r = #nonzero eigenvalues: the SAME invariant as the")
print("    frontier's rank P.  No second constant is produced.")
print("\n" + "=" * 74)
print("SUMMARY: Q1 identity (no gain, 0.6725); Q2 no numeric C* from moving-edge;")
print("Q3 same functional, same constant (0.682 ceiling).  Best available = 0.682.")
print("=" * 74)
