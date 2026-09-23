#!/usr/bin/env python3
# c1a_zero_side_window_fix.py —— 修正零点侧窗口（k 从 15 起，覆盖真实零点）＋ 指数阶梯对照
import mpmath as mp
from fractions import Fraction as F
mp.mp.dps = 25
def rank_exact(M):
    A=[[F(x) for x in r] for r in M]; n=len(A); m=len(A[0]); r=0
    for c in range(m):
        piv=next((i for i in range(r,n) if A[i][c]!=0), None)
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
    A=[[F(x) for x in r] for r in M]; n=len(A); d=F(1)
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
def hankel(v,M): return [[v[i+j] for j in range(M)] for i in range(M)]
if __name__=='__main__':
    g=[mp.im(mp.zetazero(n)) for n in range(1,61)]
    print("=== 零点侧（修正窗口）===")
    print("  前 12 个零点:", [f"{float(x):.4f}" for x in g[:12]])
    # 对象 1：单位区间计数 c_k（k=14..50）—— 真实事件的稀疏整数序列
    ks=list(range(14,51))
    ck=[sum(1 for x in g if k < x <= k+1) for k in ks]
    print("  c_k (k=14..50) =", ck)
    # 对象 2：累计计数 N(k)（k=14..50）去掉线性主项后的"波动"（整数）
    Nk=[sum(1 for x in g if x<=k) for k in ks]
    print("  N(k) (k=14..50) =", Nk)
    for nm, seq in (('c_k', ck), ('N(k)', Nk)):
        print(f"  --- {nm} ---")
        prev=None
        for M in range(3, 13):
            H=hankel([F(x) for x in seq], M); r=rank_exact(H); d=det_frac(H)
            inc='' if prev is None else f"(Δrank={r-prev})"
            dv=str(int(d)) if d.denominator==1 else str(d)
            print(f"    M={M:2d}: rank={r} {inc}  det={dv if len(dv)<24 else 'HUGE'}")
            prev=r
    # 对照：理想 GUE 模拟的同类对象（同长度）
    import random
    random.seed(7)
    sim=[F(random.randint(0,1)) for _ in range(len(ck))]
    print("  --- 对照（随机 0/1 同长度）---")
    prev=None
    for M in range(3, 13):
        H=hankel(sim, M); r=rank_exact(H); d=det_frac(H)
        inc='' if prev is None else f"(Δrank={r-prev})"
        print(f"    M={M:2d}: rank={r} {inc}  det={str(int(d)) if d.denominator==1 else d}")
        prev=r
