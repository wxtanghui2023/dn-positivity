#!/usr/bin/env python3
"""算术运输曲率 v1：最小模型审计
状态 S=(a,b,c), a+b=c
A-运输：T_A(a,b,c) = (b, c, b+c)            （Euclid/Fibonacci 加法移位，保关系）
M-运输：T_M(S) = u(S)·S,  u(S) = rad(c)      （状态依赖标量，保关系）
曲率  ：Ω(S) = log[ W(T_MT_A S)·W(S) / ( W(T_A S)·W(T_M S) ) ]
两个权：W1 = rad(abc)/(abc)   [形状不变 → 预测 Ω≡0]
        W2 = rad(abc)         [尺度敏感 → 预测 Ω≠0 且为 rad 比]
"""
import mpmath as mp
from math import gcd
mp.mp.dps = 30

def rad(n):
    n = abs(int(n))
    if n == 0: return 0
    r = 1; d = 2
    while d*d <= n:
        if n % d == 0:
            r *= d
            while n % d == 0: n //= d
        d += 1
    if n > 1: r *= n
    return r

def TA(S):
    a,b,c = S
    return (b, c, b+c)

def TM(S):
    a,b,c = S
    u = rad(c)
    return (u*a, u*b, u*c)

def W1(S):
    a,b,c = S
    return mp.mpf(rad(a)*rad(b)*rad(c))/mp.mpf(a*b*c)

def W2(S):
    a,b,c = S
    return mp.mpf(rad(a)*rad(b)*rad(c))

def Omega(S, W):
    SA = TA(S); SM = TM(S)
    SAM = TM(SA)          # A 然后 M
    return mp.log(W(SAM)*W(S)/(W(SA)*W(SM)))

N = 2000
print(f'=== v1 曲率扫描（a+b=c, c ≤ {N}）===')
for name, W in [('W1=rad/(abc) 形状不变', W1), ('W2=rad(abc) 尺度敏感', W2)]:
    nz = 0; tot = 0; vals = []
    for a in range(1, N):
        for b in range(a, N-a+1):
            c = a+b
            S = (a,b,c)
            tot += 1
            v = Omega(S, W)
            if abs(v) > mp.mpf('1e-20'):
                nz += 1
                vals.append((c, float(v)))
    fr = nz/tot if tot else 0
    print(f'  {name}: 非零 {nz}/{tot} = {fr:.6f}')
    if vals:
        mn = min(v for _,v in vals); mx = max(v for _,v in vals)
        print(f'      范围 [{mn:.6f}, {mx:.6f}]')

print()
print('=== 尺度敏感情形的还原测试：Ω(W2) ?= log[u(T_A S)/u(S)] 的线性组合 ===')
# 对尺度敏感权：W2(S_AM)W2(S)/(W2(S_A)W2(S_M))
# 由于 S_AM = u(S_A)·S_A 且 S_M = u(S)·S，可解析化；检验与 log(u(SA)/u(S)) 的关系
import statistics
data = []
for a in range(1, 400):
    for b in range(a, 400-a+1):
        S = (a,b,a+b)
        SA = TA(S)
        om = float(Omega(S, W2))
        r = float(mp.log(mp.mpf(rad(SA[2]))/mp.mpf(rad(S[2]))))   # log(u(SA)/u(S))
        data.append((om, r))
if data:
    xs = [r for _,r in data]; ys = [om for om,_ in data]
    mx = statistics.mean(xs); my = statistics.mean(ys)
    cov = sum((x-mx)*(y-my) for x,y in data)/len(data)
    vx = sum((x-mx)**2 for x in xs)/len(data); vy = sum((y-my)**2 for y in ys)/len(data)
    cc = cov/(vx*vy)**0.5 if vx>0 and vy>0 else float('nan')
    slope = cov/vx if vx>0 else float('nan')
    print(f'  n={len(data)}  相关系数 corr(Ω, log(u(SA)/u(S))) = {cc:.6f}')
    print(f'  线性拟合斜率 = {slope:.6f}')
    res = [y-(my+slope*(x-mx)) for x,y in data]
    print(f'  残差标准差 = {statistics.pstdev(res):.6f}   （≈0 ⟹ Ω 完全由 rad 比解释）')

print()
print('=== 尺度分层（W2 情形，按 c 分桶看分布是否稳定）===')
for lo, hi in [(1,300),(300,600),(600,1000),(1000,1500),(1500,2000)]:
    vals = []
    for a in range(1, hi):
        for b in range(a, hi-a+1):
            c = a+b
            if lo <= c < hi:
                vals.append(float(Omega((a,b,c), W2)))
    if vals:
        print(f'  c∈[{lo},{hi}): n={len(vals):>6}  均值={statistics.mean(vals):>10.6f}  '
              f'标准差={statistics.pstdev(vals):>10.6f}')

print()
print('=== 非交换性检验（两条路径端点是否同射线）===')
same_ray = 0; tot2 = 0
for a in range(1, 300):
    for b in range(a, 300-a+1):
        S = (a,b,a+b)
        SAM = TM(TA(S)); SMA = TA(TM(S))
        tot2 += 1
        # 同射线 ⟺ 分量比相等
        if (SAM[0]*SMA[1] == SMA[0]*SAM[1]) and (SAM[1]*SMA[2] == SMA[1]*SAM[2]):
            same_ray += 1
print(f'  同射线比例 = {same_ray}/{tot2} = {same_ray/tot2:.6f}')
print('  ⟹ 1.0 表示 M 运输只是状态依赖标量缩放（保关系空间的必然结果）')
