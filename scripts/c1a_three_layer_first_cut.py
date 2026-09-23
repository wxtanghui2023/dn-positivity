#!/usr/bin/env python3
# c1a_three_layer_first_cut.py —— C-1a：两侧"各自内部"的精确整数结构扫描（不比较误差）
# 【算术侧】 a_n = Λ(n)（精确整数）；Hankel H_M=(Λ(i+j)) 的精确 rank/det（有理消元）
# 【零点侧】 γ_n（mpmath.zetazero，数值验证）；整数计数 N(k)=#{γ_n<=k}；单位区间计数 c_k=N(k+1)-N(k)
#          ⟹ 对 N(k) 与 c_k 各自的 Hankel 做精确 rank/det（整数矩阵）
# 【记录】 消失阶 / 整数性 / 递推 / 因子化 / 阶数突变（逐项）
import mpmath as mp
from fractions import Fraction as F
from sympy import primerange, factorint
mp.mp.dps = 25

def vonmangoldt(n):
    """Λ(n) 的精确整数编码：Λ(p^k)=log p ⟹ 用 (p,k) 形式；此处为整数化扫描改用 λ/μ（见下）"""
    f = factorint(n)
    if len(f) == 1:
        p = list(f)[0]; return ('log', p)
    return None

def liouville(n):
    """λ(n) = (-1)^{Ω(n)}（完全积性，取值 ±1，精确整数 ✓）"""
    O = sum(factorint(n).values()) if n > 1 else 0
    return (-1)**O

def mobius(n):
    """μ(n) ∈ {0,±1}（精确整数 ✓）"""
    f = factorint(n)
    if any(e > 1 for e in f.values()): return 0
    return (-1)**len(f)

def hankel(vals, M):    # vals[i] = a_{i+1}
    return [[vals[i+j] for j in range(M)] for i in range(M)]

def rank_exact(M):
    A = [[F(x) for x in row] for row in M]; n=len(A); m=len(A[0]); r=0
    for c in range(m):
        piv = next((i for i in range(r,n) if A[i][c]!=0), None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]; pv=A[r][c]
        for i in range(r+1,n):
            if A[i][c]!=0:
                f=A[i][c]/pv
                for j in range(c,m): A[i][j]-=f*A[r][j]
        r+=1
        if r==n: break
    return r

def det_frac(M):
    A=[[F(x) for x in row] for row in M]; n=len(A); d=F(1)
    for c in range(n):
        piv=next((i for i in range(c,n) if A[i][c]!=0), None)
        if piv is None: return F(0)
        if piv!=c: A[c],A[piv]=A[piv],A[c]; d=-d
        d*=A[c][c]; pv=A[c][c]
        for i in range(c+1,n):
            if A[i][c]!=0:
                f=A[i][c]/pv
                for j in range(c,n): A[i][j]-=f*A[c][j]
    return d

if __name__ == '__main__':
    print("=== C-1a 算术侧：Λ 的 Hankel 结构（精确整数/有理）===")
    NMAX = 30
    lam = [F(liouville(n)) for n in range(1, NMAX+1)]
    print("  λ(1..14) =", [str(x) for x in lam[:14]], "  (Liouville，精确整数 ✓)")
    mu = [F(mobius(n)) for n in range(1, NMAX+1)]
    print("  μ(1..14) =", [str(x) for x in mu[:14]], "  (Möbius，精确整数 ✓)")
    prev_r = None
    for name, seq in (('λ', lam), ('μ', mu)):
        print(f"  --- 算术侧 {name} 的 Hankel ---")
        prev_r = None
        for M in range(3, 13):
            H = hankel(seq, M)
            r = rank_exact(H); d = det_frac(H)
            inc = '' if prev_r is None else f"(Δrank={r-prev_r})"
            dv = str(int(d)) if d.denominator == 1 else str(d)
            print(f"    M={M:2d}: rank={r} {inc}  det={dv if len(dv) < 22 else 'HUGE'}")
            prev_r = r
    print("\n=== C-1a 零点侧：整数计数 N(k) 与 c_k 的 Hankel 结构（精确整数）===")
    KMAX = 26
    gammas = [mp.im(mp.zetazero(n)) for n in range(1, 41)]
    print("  γ_1..γ_6 =", [f"{float(g):.6f}" for g in gammas[:6]])
    Nk = [sum(1 for g in gammas if g <= k) for k in range(1, KMAX+1)]
    ck = [Nk[i+1]-Nk[i] for i in range(len(Nk)-1)]
    print("  N(1..26) =", Nk)
    print("  c_k      =", ck)
    for name, seq in (('N(k)', Nk), ('c_k', ck)):
        print(f"  --- {name} ---")
        prev = None
        for M in range(3, min(12, len(seq))):
            H = hankel([F(x) for x in seq], M)
            r = rank_exact(H); d = det_frac(H)
            inc = '' if prev is None else f"(Δrank={r-prev})"
            print(f"    M={M:2d}: rank={r} {inc}  det={d if abs(d) < 10**12 else 'HUGE'}")
            prev = r
