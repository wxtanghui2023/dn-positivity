#!/usr/bin/env python3
# b1_dual_representation_defect_scan.py —— B-1 第一刀：离散/解析双表示的结构性缺陷
# 【对象】 zeta 的两种天然表示（同一截断 N）：A(N;s)=sum_{n<=N} n^{-s}；B(N;s)=prod_{p<=N}(1-p^{-s})^{-1}
# 【精确恒等式】 D = A - B = -sum_{n>N, P(n)<=N} n^{-s}   （P(n)=最大质因子）⟹ 这是**精确**差，非离散化误差
# 【记录】 ① 精确消失 ② 整有理结构 ③ 低阶递推 ④ 跨尺度不变量 ⑤ 因子化 ⑥ 奇异阶数转换 ⑦ 是否落入已知账本
# 【对照】 把 Euler 积的截断由 p<=N 改为 p<=N/3 / p<=3N，检验"对角 y=N"是否特殊
import mpmath as mp
from sympy import primerange, factorint
mp.mp.dps = 30

def A(N, s): return mp.nsum(lambda n: mp.mpf(n)**(-s), [1, N])
def B(N, s):
    pr = 1
    for p in primerange(2, N+1): pr *= (1 - mp.mpf(p)**(-s))**(-1)
    return pr

def smooth_above(N, s, count=6):
    """找 n>N 且 P(n)<=N 的最小若干个数（精确恒等式的支配项）"""
    out = []; n = N+1; lim = 40*N+1000
    while len(out) < count and n <= lim:
        if max(factorint(n)) <= N: out.append(n)
        n += 1
    return out

def tail_sum(N, s, terms=4000):
    tot = mp.mpf(0); cnt = 0
    for n in range(N+1, N+terms):
        if max(factorint(n)) <= N:
            tot += mp.mpf(n)**(-s); cnt += 1
    return -tot, cnt

if __name__ == '__main__':
    print("=== B-1 第一刀：双表示结构性缺陷（Dirichlet 截断 vs Euler 积截断，同 N）===")
    for s in (mp.mpf(2), mp.mpf('1.5')):
        print(f"\n### s = {float(s)} ###")
        print("  N | A(N) | B(N) | D=A-B | 恒等式核对 | 最小支配项 n>N | gap | 支配项占比")
        for N in (100, 300, 1000, 3000, 10000):
            a = A(N, s); b = B(N, s); D = a - b
            tl, cnt = tail_sum(N, s, terms=200 if N <= 1000 else 60)
            sm = smooth_above(N, s, count=1)
            n1 = sm[0] if sm else None
            dom = (-mp.mpf(n1)**(-s)) if n1 else mp.mpf(0)
            print(f"  {N} | {float(a):.10f} | {float(b):.10f} | {float(D):.6e} | {float(D-tl):.3e} | {n1} | {n1-N if n1 else '-'} | {float(dom/D) if D!=0 else 0:.4f}")
        # 结构扫描：D 的跨尺度比值
        Ds = []
        for N in (100, 300, 1000, 3000, 10000):
            Ds.append(A(N, s) - B(N, s))
        print("  跨尺度比值 D(N)/D(N_prev): " + " ".join(f"{float(Ds[i+1]/Ds[i]):.6f}" for i in range(len(Ds)-1)))
        print("  D 的符号: " + " ".join(('+' if d > 0 else '-') for d in Ds))
        print("  log|D| 随 log N 的斜率: " + " ".join(f"{float(mp.log(abs(Ds[i+1]/Ds[i]))/mp.log(mp.mpf(3))):.6f}" for i in range(len(Ds)-1)))
    # 对照：非对角截断
    print("\n=== 对照：Euler 积截断改为 p<=N/3 与 p<=3N（检验对角 y=N 是否特殊）===")
    s = mp.mpf(2)
    for N in (300, 1000, 3000):
        d_diag = A(N, s) - B(N, s)
        d_small = A(N, s) - B(N//3, s)
        d_big = A(N, s) - B(3*N, s)
        print(f"  N={N}: D(diag)={float(d_diag):.6e} | D(p<=N/3)={float(d_small):.6e} | D(p<=3N)={float(d_big):.6e}")
