#!/usr/bin/env python3
"""波包互补对照实验: 真实 vs 合成——面积互补是真实结构还是锯齿平凡?
合成 A: S 随机游走（ΔS 独立 ±~0.4——）——锯齿的平凡版
合成 B: ΔS 高斯（同 std——）但无记忆
比较面积序列的: ρ(1)/ρ(2)/块压缩——真实 vs 合成
"""
import numpy as np
from math import log, pi

def seg_areas(s):
    """符号段面积——"""
    signs = np.sign(s)
    boundaries = np.where(np.diff(signs) != 0)[0] + 1
    seg_starts = np.concatenate([[0], boundaries])
    seg_ends = np.concatenate([boundaries, [len(s)]])
    areas = []
    for a, b in zip(seg_starts, seg_ends):
        areas.append(np.sum(s[a:b]))
    return np.array(areas)

def stats(areas, name):
    r1 = np.corrcoef(areas[:-1], areas[1:])[0,1]
    r2 = np.corrcoef(areas[:-2], areas[2:])[0,1]
    cum = np.cumsum(areas)
    blk = 100
    n_blk = len(areas)//blk
    blk_sums = np.array([np.sum(areas[i*blk:(i+1)*blk]) for i in range(n_blk)])
    rw = np.sqrt(blk)*areas.std()
    print(f'{name}: ρ(1)={r1:+.4f}——ρ(2)={r2:+.4f}——累积max={np.max(np.abs(cum)):.4f}——块压缩={blk_sums.std()/rw:.4f}')

# 真实
z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = min(len(z), 200000)
z = z[:K]
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z[:-1]])
S_right = np.arange(1, K) - N0v
s_real = S_right - 0.5
stats(seg_areas(s_real), '真实')

# 合成 A: 随机游走（ΔS 独立同分布——std 同真实 ΔS——）
dS_real = np.diff(S_right)
std_dS = dS_real.std()
rng = np.random.default_rng(42)
n_trials = 5
for t in range(n_trials):
    dS_syn = rng.normal(0, std_dS, len(dS_real))
    S_syn = np.cumsum(dS_syn)
    # 去漂移（真实 S 有均值 0.5 的——用去均值版——）
    s_syn = S_syn - S_syn.mean()
    if t == 0:
        stats(seg_areas(s_syn), '合成A(随机游走)')

# 合成 B: 真实 ΔS 的排列（保持分布——打乱顺序——）——破坏时序结构
dS_perm = dS_real.copy()
for t in range(5):
    rng.shuffle(dS_perm)
    S_perm = np.cumsum(dS_perm)
    s_perm = S_perm - S_perm.mean()
    if t == 0:
        stats(seg_areas(s_perm), '合成B(排列)')

# 合成 C: ΔS 的一阶自回归（匹配真实 ρ(ΔS,1)——）
print()
rho_dS1 = np.corrcoef(dS_real[:-1], dS_real[1:])[0,1]
print(f'真实 ΔS 的 ρ(1) = {rho_dS1:+.4f}——std = {std_dS:.4f}')
# AR(1) 合成
for t in range(3):
    dS_ar = np.zeros(len(dS_real))
    dS_ar[0] = rng.normal(0, std_dS)
    for i in range(1, len(dS_ar)):
        dS_ar[i] = rho_dS1*dS_ar[i-1] + rng.normal(0, std_dS*np.sqrt(1-rho_dS1**2))
    S_ar = np.cumsum(dS_ar)
    s_ar = S_ar - S_ar.mean()
    if t == 0:
        stats(seg_areas(s_ar), '合成C(AR1)')
