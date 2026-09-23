#!/usr/bin/env python3
# run2_card4_hecke_common_annihilator.py —— RUN-2（预注册、单轮、不可漂移）
# 冻结范围：forms Φ12,Φ16,Φ18,Φ20,Φ22；10 对全检；W: p<=1e4 前605素数；W': 1e4<p<=2e4 前605素数；
#          h=0..600；J=1..4；判定 ∃c∈Z^{J+1}: Mc=0, c_J=1；M1–M5 固定；∪ker H_x 仅诊断
import numpy as np, itertools, time
from sympy import primerange, Matrix, symbols, linsolve, nextprime

N = 20000
t0 = time.time()
print("=== RUN-2 :: 卡 4（跨形式×两窗口 共同湮灭判定）===")
print("[1] σ1,σ3,σ5,σ7,σ9 筛（精确）...")
sig = {1: [0]*(N+1), 3: [0]*(N+1), 5: [0]*(N+1), 7: [0]*(N+1), 9: [0]*(N+1)}
for d in range(1, N+1):
    for k in (1,3,5,7,9):
        v = d**k
        for m in range(d, N+1, d): sig[k][m] += v
print("    σk(n) 完成，用时 %.1fs" % (time.time()-t0))

print("[2] τ(n) mod 3 素 + CRT（精确）...")
MODS = [int(nextprime(2**31 + 1000)), int(nextprime(2**31 + 100000)), int(nextprime(2**31 + 500000))]
print('    模数（sympy nextprime 生成，保证素数且互不相同）:', MODS)
def tau_mod(P):
    s1 = np.array(sig[1], dtype=np.int64) % P
    t = np.zeros(N+1, dtype=np.int64); t[1] = 1
    for n in range(2, N+1):
        m = np.arange(1, n)
        prod = (t[1:n] * (((P - 24) * s1[n-m]) % P)) % P
        t[n] = (int(prod.sum() % P) * pow(n-1, -1, P)) % P
    return t
ts = [tau_mod(P) for P in MODS]
def crt(vals1, vals2, vals3):
    m1, m2, m3 = MODS
    M12 = m1*m2; inv1 = pow(m1, -1, m2); inv12 = pow(M12 % m3, -1, m3)   # t1 = (a2-a1)*m1^{-1} mod m2
    out = [0]*(N+1)
    for n in range(1, N+1):
        x = (int(vals1[n]) + m1*(((int(vals2[n])-int(vals1[n]))*inv1) % m2)) % M12
        v = (x + M12*(((int(vals3[n])-x) % m3)*inv12 % m3))
        M3 = m1*m2*m3
        out[n] = v - M3 if v > M3//2 else v     # 映射到有符号代表（|τ(n)| < M/2 ✓）
    return out
tau = crt(ts[0], ts[1], ts[2])
known = {2:-24, 3:252, 4:-1472, 5:4830, 6:-6048, 7:-16744}
got = {n: tau[n] for n in known}
ok = all(got[n] == known[n] for n in known)
print("    自检 τ(2..7) =", [got[n] for n in sorted(known)])
print("    期望        =", [known[n] for n in sorted(known)], " ⟹", "ALL OK ✓" if ok else "❌ 不符，终止")
if not ok:
    raise SystemExit("τ 自检失败：后续判定不可信，终止（不产出任何结论）")
print("    用时 %.1fs" % (time.time()-t0))

print("[3] 五个形式在素数处的系数 a_p（Φ12=Δ；Φk=Δ·E_{k-12}，E 系数显式）...")
EIS = {16: (4,  240), 18: (6, -504), 20: (8, 480), 22: (10, -264)}   # k -> (k-12, Eisenstein coeff)
primes = list(primerange(2, N+1))
def ap_of(k, p):
    if k == 12: return tau[p]
    kk, c = EIS[k]
    s = tau[p]                      # a=p, b=0
    sk = kk - 1                     # σ_{k-13}
    for a in range(1, p):
        s += tau[a] * (c * sig[sk][p-a])
    return s
ap = {k: {p: ap_of(k, p) for p in primes} for k in (12,16,18,20,22)}
def series_coeff(k, n):
    """[q^n](Δ·E_{k-12}) 直接卷积（小 n 用）"""
    if k == 12: return tau[n]
    kk, c = EIS[k]; sk = kk-1
    return sum((tau[a] if a >= 1 else 0) * (c*sig[sk][n-a] if n-a >= 1 else 1) for a in range(1, n+1))
print("    自检：形式须满足 Hecke 递推 a_{p^2} = a_p^2 - p^{k-1}（对小 n 直接用级数系数）:")
for k in (12,16,18,20,22):
    for p in (2,3):
        lhs = series_coeff(k, p*p); rhs = ap[k][p]**2 - p**(k-1)
        print(f"      Φ{k} p={p}: 级数 a_{p*p}={lhs}  vs  a_p^2-p^(k-1)={rhs}  {'OK' if lhs==rhs else 'MISMATCH'}")
print("    用时 %.1fs" % (time.time()-t0))

W  = [p for p in primes if p <= 10000][:605]
W2 = [p for p in primes if 10000 < p <= 20000][:605]
print(f"[4] 窗口: W={len(W)} 素数（{W[0]}..{W[-1]}）；W'={len(W2)} 素数（{W2[0]}..{W2[-1]}）")
HROW = 600
def rank_Q(rows, ncols):
    A = [[int(x) for x in r] for r in rows]; r = 0
    piv_cols = []
    for c in range(ncols):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(r+1, len(A)):
            if A[i][c] != 0:
                a, b = A[i][c], A[r][c]
                A[i] = [A[i][j]*b - a*A[r][j] for j in range(ncols)]   # 精确整数消元
        r += 1
        piv_cols.append(c)
        if r == ncols: break
    return r
def rowsof(seq_pairs, J, off):
    return [[seq_pairs[off + h + j] for j in range(J+1)] for h in range(HROW+1)]

print("[5] 10 对 × J=1..4：精确判定 ∃c∈Z^{J+1}: Mc=0, c_J=1 ...")
hits = []; diag = []
for (ka, kb) in itertools.combinations((12,16,18,20,22), 2):
    for J in range(1, 5):
        blocks = []
        for k, Wn in ((ka, W), (ka, W2), (kb, W), (kb, W2)):
            seq = [ap[k][p] for p in Wn]
            blocks += rowsof(seq, J, 0)
        M = blocks
        r = rank_Q(M, J+1)
        nz = (r < J+1)
        verdict = "否"
        cvec = None
        if nz:
            A = Matrix([[int(x) for x in row] for row in M])
            sol = list(linsolve((A, Matrix([0]*len(M))), symbols(f'c0:{J+1}')))
            if sol:
                s = sol[0]
                free = any(v.free_symbols for v in s)
                if not free and all(v.q == 1 for v in s):
                    if s[J] == 1: verdict = "是"; cvec = [int(v) for v in s]
        print(f"  pair(Φ{ka},Φ{kb}) J={J}: rank_Q={r}/{J+1}  ∃c={verdict}" + (f"  c={cvec}" if cvec else ""))
        if verdict == "是": hits.append((ka, kb, J, cvec))
        # 诊断：命中 c 是否落在预注册旧序列核内（仅报告）
        if cvec:
            for nm, seq in (("常1",[1]*(HROW+1+J)), ("h",[float('nan')]*0), ):
                pass
print(f"[6] 命中数 = {len(hits)}")
print("总用时 %.1fs" % (time.time()-t0))
