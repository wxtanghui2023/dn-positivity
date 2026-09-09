#!/usr/bin/env python3
"""构造+验证轮3: M 的配对结构——b_k 振荡与交替符号的耦合（detailed balance——）
M = Σ(-1)^k b_k——配对: (-1)^k(b_k - b_{k+1})——若配对和的结构可控——M 有界——
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
areas = []; lens = []; gmid = []
for i in range(len(bounds)-1):
    a, b = bounds[i], bounds[i+1]
    if b - a >= 1:
        areas.append(M_inc[a:b].sum())
        lens.append(b-a)
        gmid.append(z[(a+b)//2])
areas = np.array(areas); lens = np.array(lens); gmid = np.array(gmid)
N = len(areas)
b = np.abs(areas)
sg = np.sign(areas)  # = (-1)^k（平凡——）
alt = np.cumsum(areas)  # M 波包级

print('=== 轮3: M 的配对结构（detailed balance 类比——）===')
# M 的 2 步增量: M_{k+2} - M_k = a_k + a_{k+1} = (-1)^k(b_k - b_{k+1})
# 配对: p_k = (-1)^k(b_k - b_{k+1})
pairs = np.array([(-1)**k * (b[k] - b[k+1]) for k in range(N-1)])
print(f'配对 p_k = (-1)^k(b_k-b_{{k+1}}):')
print(f'  mean={pairs.mean():+.4f}——std={pairs.std():.4f}——max|={np.max(np.abs(pairs)):.4f}')
# 配对累积（= M 的 2 步——）
cum_pairs = np.cumsum(pairs)
print(f'  配对累积 max|={np.max(np.abs(cum_pairs)):.3f}（~ M/2 量级——）')

# 配对的自相关——p_k 的结构
print()
print('p_k 自相关:')
for lag in range(1, 6):
    c = np.corrcoef(pairs[:-lag], pairs[lag:])[0,1]
    print(f'  ρ({lag}) = {c:+.4f}')

# 关键分解: b_k = 包络(长程) + 振荡——包络 ~ 缓慢下降——振荡与交替耦合
# 滑动平均包络
win = 200
env = np.convolve(b, np.ones(win)/win, mode='same')
osc = b - env  # 振荡部分
print()
print(f'分解: b_k = 包络 + 振荡——振荡 std={osc.std():.4f}（b std={b.std():.4f}——）')
# 振荡的配对: 振荡部分与 (-1)^k 的耦合
# Σ(-1)^k·osc_k——如果 osc 与 (-1)^k 反相——抵消
alt_osc = np.cumsum(np.array([(-1)**k * osc[k] for k in range(N)]))
alt_env = np.cumsum(np.array([(-1)**k * env[k] for k in range(N)]))
print(f'振荡部分交替和 max|={np.max(np.abs(alt_osc)):.3f}')
print(f'包络部分交替和 max|={np.max(np.abs(alt_env)):.3f}')

# 包络的导数（长程下降率——）
print()
print('包络的下降（末段 vs 初段——）:')
print(f'  包络: 前={env[100]:.4f}——中={env[N//2]:.4f}——后={env[-100]:.4f}')

# Δb 的配对符号——b_k - b_{k+1} 的符号与 (-1)^k 的关系
db = np.diff(b)
# 如果 db 的符号 ~ (-1)^k 的某种——p_k = (-1)^k(b_k-b_{k+1}) = (-1)^{k+1}db_k 符号正偏
print()
print('Δb_k 符号 vs (-1)^k:')
corr = np.corrcoef(np.sign(db), np.array([(-1)**k for k in range(N-1)]))[0,1]
print(f'  相关 = {corr:+.4f}（~0 = 无关——）')
print(f'  配对 p_k 为正比例: {np.mean(pairs > 0):.4f}')
