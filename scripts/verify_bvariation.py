#!/usr/bin/env python3
"""构造+验证轮2: b_k=|面积_k| 的变差——Dirichlet/Leibniz 检验（交替级数收敛——）
M(波包级) = Σ(-1)^k b_k——若 b_k 递减→0 或有界变差——M 有界——
"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 400000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

dg = np.diff(z[:K])
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar = kk - (IntN[1:] - IntN[:-1])/dg
M_inc = Sbar * dg

signs = np.sign(Sbar)
flips = np.where(signs[:-1] != signs[1:])[0] + 1
bounds = np.concatenate([[0], flips, [len(Sbar)]])
areas = []; lens = []; gend = []
for i in range(len(bounds)-1):
    a, b = bounds[i], bounds[i+1]
    if b - a >= 1:
        areas.append(M_inc[a:b].sum())
        lens.append(b-a)
        gend.append(z[b-1])
areas = np.array(areas); lens = np.array(lens); gend = np.array(gend)
N = len(areas)
b = np.abs(areas)  # 面积大小

print('=== 轮2: b_k 变差与 Dirichlet 检验 ===')
print(f'b_k: N={N}——mean={b.mean():.4f}——std={b.std():.4f}')

# 1. 递减性检验: b_k 是递减的吗（逐点——）？——块平均（长程——）
print()
print('1. b_k 的块平均（每 2万——）——长程递减?:')
for i in range(0, N, 20000):
    seg = b[i:i+20000]
    print(f'  k={i}-{i+len(seg)}: mean b={seg.mean():.4f}')

# 2. 变差: TV(N) = Σ|b_{k+1} - b_k|——增长?
print()
print('2. 总变差增长（Σ|Δb_k|——Dirichlet 需要 ~O(1) 或 O(log)——）:')
cum_tv = 0
for i in range(0, N-1, 1):
    pass
# 计算分段 TV
for i0 in range(0, N-1, 50000):
    i1 = min(i0+50000, N-1)
    tv = np.sum(np.abs(np.diff(b[i0:i1])))
    cum_tv += tv
    print(f'  段 k={i0}-{i1}: TV={tv:.2f}——累积={cum_tv:.2f}')

# 3. 单调性的'块'结构——b_k 的局部趋势
print()
print('3. b_k 的局部单调（上升/下降段的长度——）:')
db = np.diff(b)
up = db > 0
# 上升/下降游程
runs = []
cur = 1
for i in range(1, len(up)):
    if up[i] == up[i-1]: cur += 1
    else:
        runs.append(cur); cur = 1
runs.append(cur)
print(f'  游程平均长={np.mean(runs):.2f}（1=完全交替升降——）')

# 4. 关键: 相邻 b 的差的相关结构——Δb_k 是否'均值回复'（变差受控——）
print()
print('4. Δb_k 的自相关:')
db2 = db
for lag in range(1, 5):
    c = np.corrcoef(db2[:-lag], db2[lag:])[0,1]
    print(f'  ρ({lag}) = {c:+.4f}')

# 5. M(波包级) vs b 变差的尾部——如果 b_k 不递减——M 靠什么有界?
print()
print('5. M 的波包级交替和 - 泄漏检验:')
# 交替和的增量（每步 b_k——）——如果 b_k 不趋于 0——交替和的'摆动' ~ b_k
alt = np.cumsum(areas)
print(f'  M max={np.max(np.abs(alt)):.3f}——b_k max={b.max():.3f}——b_k 末段 mean={b[-10000:].mean():.4f}')
print(f'  （如果 b_k 不递减——M 的摆动 ~ b_k 的量级——max b={b.max():.3f} vs M max={np.max(np.abs(alt)):.3f}——）')
