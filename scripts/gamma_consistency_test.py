#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# Γ(X,h) 二维一致性场——跨尺度残差结构测试
# T_h(X) = #{p<=X: p, p+h prime}
# Γ_X(h) = |T_h(X)| / (S(h)·Li₂(X)), S(h)=奇异级数
# 检查: (1) Γ→1? (2) 误差 E_h(X)=Γ-1 的指数 (平方根 -1/2? 或 1/log?)
# (3) 跨尺度残差 D(X,Y;h)=Γ_Y-Γ_X, K=D(Y,Z)/D(X,Y) 是否有稳定非平凡结构
import numpy as np, math, time
from bisect import bisect_right

def sieve(n):
    is_p = np.ones(n+1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(n**0.5)+1):
        if is_p[i]:
            is_p[i*i::i] = False
    return is_p

def twin_const(N=1000000):
    # C₂ = Π_{p>2}(1-1/(p-1)²)
    is_p = sieve(N)
    c = 1.0
    for p in range(3, N+1, 2):
        if is_p[p]:
            c *= (1 - 1.0/((p-1)*(p-1)))
    return c

def singular_series(h, C2, primes_list):
    """S(h) = 2C₂·Π_{p|h, p>2}(p-1)/(p-2)  (h 偶)"""
    s = 2*C2
    m = h
    while m % 2 == 0:
        m //= 2  # 去掉 2 的幂 (2 不贡献, q>2)
    # 只乘奇素因子
    for pr in primes_list:
        if pr <= 2: continue
        if pr*pr > m: break
        if m % pr == 0:
            s *= (pr-1)/(pr-2)
            while m % pr == 0:
                m //= pr
    if m > 1:  # 剩余奇素因子
        s *= (m-1)/(m-2)
    return s

def li2(X, steps=200000):
    """Li₂(X) = ∫₂^X dt/(log t)² 数值积分"""
    if X <= 2: return 0.0
    # 变量替换 t = X^u? 或直接 Simpson (大 X 用渐近更稳)
    # 用分段: 直接数值积分在 log 空间: t=e^v, dt=e^v dv, 积分 v∈[log2,logX] e^v/v² dv
    lo, hi = math.log(2.0), math.log(X)
    n = steps
    h = (hi-lo)/n
    # Simpson
    def f(v):
        return math.exp(v)/(v*v)
    s = f(lo) + f(hi)
    for i in range(1, n):
        v = lo + i*h
        s += (4 if i%2 else 2)*f(v)
    return s*h/3

def main():
    Xmax = 20000000
    t0 = time.time()
    print(f"筛素数到 {Xmax}...")
    is_p = sieve(Xmax)
    P = np.nonzero(is_p)[0].astype(np.int64)
    Pset = set(int(x) for x in P)
    print(f"素数数: {len(P)}, 耗时 {time.time()-t0:.1f}s")
    C2 = twin_const(1000000)
    print(f"孪生常数 C₂ = {C2:.6f}")
    # 素因子列表(用于奇异级数, 到 √Xmax)
    primes_list = [int(x) for x in P if x <= int(Xmax**0.5)+1]
    
    Xs = [10**3, 10**4, 10**5, 10**6, 10**7, 20000000]
    hs = [2, 4, 6, 10, 12, 30, 100]
    print(f"\nΓ_X(h) 表 (T_h/(S(h)·Li₂)):")
    header = f"{'X':>10}" + "".join(f"{'h='+str(h):>12}" for h in hs)
    print(header)
    Gamma = {}
    for X in Xs:
        row = f"{X:>10}"
        for h in hs:
            if h > X: 
                row += f"{'—':>12}"
                continue
            # T_h(X) = #{p<=X: p+h 素}
            Th = 0
            for p in P:
                if p > X: break
                if (p+h) in Pset:
                    Th += 1
            S = singular_series(h, C2, primes_list)
            L2 = li2(X)
            G = Th/(S*L2) if S*L2 > 0 else 0
            Gamma[(X,h)] = G
            row += f"{G:>12.6f}"
        print(row)
    print(f"耗时 {time.time()-t0:.1f}s")
    
    # 误差指数: E_h(X) = Γ-1, log|E|/log X (limsup 近似)
    print(f"\n误差指数 log|Γ-1|/log X (若 ~-1/2 平方根; ~0 则 1/log 类):")
    for h in [2, 4, 6, 12]:
        print(f"  h={h}:")
        prev = None
        for X in Xs:
            if (X,h) not in Gamma: continue
            G = Gamma[(X,h)]
            E = G - 1
            if abs(E) > 1e-12:
                idx = math.log(abs(E))/math.log(X)
            else:
                idx = float('-inf')
            print(f"    X={X:>10}: Γ={G:.6f} E={E:+.6f} log|E|/logX={idx:+.4f}")
    
    # 跨尺度残差 D 与 K
    print(f"\n跨尺度残差 D(X,Y;h)=Γ_Y-Γ_X 与比值 K:")
    for h in [2, 6]:
        print(f"  h={h}:")
        Gs = [(X, Gamma[(X,h)]) for X in Xs if (X,h) in Gamma]
        for i in range(len(Gs)-1):
            X1, G1 = Gs[i]
            X2, G2 = Gs[i+1]
            D = G2-G1
            print(f"    D({X1},{X2})={D:+.6f}", end="")
            if i >= 1:
                X0, G0 = Gs[i-1]
                D0 = G1-G0
                if abs(D0) > 1e-12:
                    print(f"  K=D2/D1={D/D0:+.4f}")
                else:
                    print("  K=—")
            else:
                print()

if __name__ == "__main__":
    main()
