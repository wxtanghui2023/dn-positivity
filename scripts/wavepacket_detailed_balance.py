#!/usr/bin/env python3
"""追波包详细平衡机制（NS 式——构造+验证——）
问题: 为什么 b_k（波包面积幅度）振荡与 (−1)^k 精确配对?
b_k 的 ρ(2) = −0.64——高-低-高-低模式——
假设候选:
H1: b_k 振荡 = 波包内部形状（双峰——）的守恒（相邻波包互补——）
H2: b_k 振荡 = Δγ（间距——）相关的（面积 ~ 符号段长度 × S̄——）
H3: b_k 振荡与交替配对 = 面积序列的自相似（无标度——）
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
K = min(len(z), 200000)
z = z[:K]

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z[:-1]])
S_right = np.arange(1, K) - N0v  # S(γ_k+)（零点处右极限——）
dS = np.diff(S_right)

# 波包 = S̄ 符号段——但 S̄（区间平均——）~ S(mid)——用 S_right 近似（符号段——）
# 波包: S 的符号段（正/负——）——面积 = Σ S(γ_k)（段内——）？——用 S_right−½ 的符号段
s = S_right - 0.5  # 去均值（mean 0.5——）
# 符号段（波包——）
signs = np.sign(s)
boundaries = np.where(np.diff(signs) != 0)[0] + 1
seg_starts = np.concatenate([[0], boundaries])
seg_ends = np.concatenate([boundaries, [len(s)]])
areas = []
lengths = []
for a, b in zip(seg_starts, seg_ends):
    areas.append(np.sum(s[a:b]))
    lengths.append(b - a)
areas = np.array(areas)
lengths = np.array(lengths)
b_k = np.abs(areas)

print(f'波包数: {len(areas)}——平均长 {lengths.mean():.2f}——面积 mean {areas.mean():+.4f} std {areas.std():.4f}')
print(f'b_k = |面积|: mean {b_k.mean():.4f}——std {b_k.std():.4f}')

# 交替和有界性（详细平衡——）
alt_sum = np.cumsum(areas)  # 面积累积（= M?——）
print(f'面积累积 max|={np.max(np.abs(alt_sum)):.4f}')

# H1: 波包内部形状——相邻波包的形状互补?
print()
print('=== H1: 相邻波包面积的关系 ===')
r1 = np.corrcoef(areas[:-1], areas[1:])[0,1]
r2 = np.corrcoef(areas[:-2], areas[2:])[0,1]
print(f'ρ(面积, 相邻) = {r1:+.4f}——ρ(隔一) = {r2:+.4f}')
# 面积符号（应该交替——）与幅度
print(f'正面积比例: {(areas>0).mean():.4f}——符号交替（相邻异号比例）: {(np.sign(areas[:-1])!=np.sign(areas[1:])).mean():.4f}')

# 面积 vs 长度的关系
print()
print('=== 面积 vs 长度（H2 的——）===')
print(f'corr(面积, 长度) = {np.corrcoef(areas, lengths)[0,1]:+.4f}')
# 长度序列的相关
rl1 = np.corrcoef(lengths[:-1], lengths[1:])[0,1]
print(f'长度 ρ(1) = {rl1:+.4f}')

# H3: 面积的无标度/自相似——块平均的方差
print()
print('=== H3: 面积序列的块结构 ===')
for blk in [10, 100]:
    n_blk = len(areas)//blk
    blk_sums = np.array([np.sum(areas[i*blk:(i+1)*blk]) for i in range(n_blk)])
    print(f'块长 {blk}: 块和 std={blk_sums.std():.4f}——随机游走预期={np.sqrt(blk)*areas.std():.4f}——压缩比={blk_sums.std()/(np.sqrt(blk)*areas.std()):.4f}')

# 关键: 面积序列的"配对结构"——(+,−) 对的净面积
print()
print('=== (+,-) 对的结构 ===')
pairs = areas.reshape(len(areas)//2, 2)
pair_net = pairs[:,0] + pairs[:,1]
pair_net_abs = np.abs(pairs[:,0]) + np.abs(pairs[:,1])
print(f'对净面积: mean {pair_net.mean():+.4f}——std {pair_net.std():.4f}')
print(f'|+面积| vs |-面积| 相关: {np.corrcoef(pairs[:,0], pairs[:,1])[0,1]:+.4f}')
print(f'|+面积|/|-面积| 比: mean {np.abs(pairs[:,0]).mean()/np.abs(pairs[:,1]).mean():.4f}')
