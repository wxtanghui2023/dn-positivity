#!/usr/bin/env python3
"""χ_N(i,j,k) 的 PNT 剥离——商空间 A/Z 测试第一刀
χ_N(i,j,k) = sgn[(log p_j − log p_i)/(log p_k − log p_j) − (j−i)/(k−j)]
——比较真实对数几何与 prime-index 几何的相对失真——
问题：χ 的涨落部分（χ − χ^PNT）∈ Z（零点谱——）吗？
"""
import numpy as np
from math import log

def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return np.array([int(x) for x in np.nonzero(sieve)[0]])

# 素数到 2e6（~15 万个素数——）
N = 2000000
pr = primes_upto(N)
print(f'素数数: {len(pr)}——p_last = {pr[-1]}')

# χ 的核心量 R = (log p_j − log p_i)/(log p_k − log p_j) − (j−i)/(k−j)
# 以及 PNT 主项版本（用 p_j ~ j(log j + log log j − 1)——更好近似——）
def p_pnt(j):
    """PNT 反函数的近似（j 从 1 开始——）"""
    j = float(j)
    logj = log(j)
    # p_j ~ j(log j + log log j − 1)——（更精确——）
    return j*(logj + log(logj) - 1.0) if logj > 1 else j*logj

def R_val(primes, i, j, k):
    """真实——(i,j,k 为 1-based 指标——)"""
    return (log(primes[j-1]) - log(primes[i-1]))/(log(primes[k-1]) - log(primes[j-1])) - (j-i)/(k-j)

def R_pnt(i, j, k):
    """PNT 主项——"""
    return (log(p_pnt(j)) - log(p_pnt(i)))/(log(p_pnt(k)) - log(p_pnt(j))) - (j-i)/(k-j)

# 统计：随机 (i,j,k) 的 χ vs χ^PNT——翻转率
rng = np.random.default_rng(42)
M = len(pr)
print()
print('=== χ vs χ^PNT 比较（随机样本——）===')
for region in [(1000, 5000), (10000, 30000), (50000, 100000)]:
    lo, hi = region
    flips = 0
    total = 0
    for _ in range(3000):
        # 随机 i<j<k in [lo, hi]
        idx = sorted(rng.choice(range(lo, hi+1), 3, replace=False))
        i, j, k = idx[0], idx[1], idx[2]
        r_real = R_val(pr, i, j, k)
        r_pnt = R_pnt(i, j, k)
        chi_real = 1 if r_real > 0 else (-1 if r_real < 0 else 0)
        chi_pnt = 1 if r_pnt > 0 else (-1 if r_pnt < 0 else 0)
        total += 1
        if chi_real != chi_pnt:
            flips += 1
    print(f'  j∈[{lo},{hi}]: 翻转率 = {flips}/{total} = {flips/total:.4f}')

# R 的符号结构——PNT 主项是否主导？
print()
print('=== R 的 PNT 主项大小 vs 涨落 ===')
# 检查 R_real − R_pnt（涨落——）的量级 vs R_pnt
samples = []
for _ in range(2000):
    idx = sorted(rng.choice(range(10000, 60000), 3, replace=False))
    i, j, k = idx[0], idx[1], idx[2]
    r_real = R_val(pr, i, j, k)
    r_pnt = R_pnt(i, j, k)
    samples.append((abs(r_pnt), abs(r_real - r_pnt)))
samples = np.array(samples)
print(f'  |R^PNT| 中位数 = {np.median(samples[:,0]):.6f}——|涨落| 中位数 = {np.median(samples[:,1]):.6f}')
print(f'  |R^PNT| > 10×|涨落| 的比例 = {np.mean(samples[:,0] > 10*samples[:,1]):.3f}')
print(f'  |涨落| > |R^PNT| 的比例（符号可能翻——）= {np.mean(samples[:,1] > samples[:,0]):.3f}')

# 涨落的结构——与 p_j/(j log j) 偏差的关系（显式公式通道——）
print()
print('=== 涨落的来源检查（p_j 的偏差——）===')
# ε_j = log p_j − log(j log j)（PNT 偏差——）——R 的涨落来自 ε 的差——
# 检验：R_real − R_pnt ≈ 线性化（ε 的——）？
# 取 i<j<k 邻近——R 涨落 vs ε_j 的差分
i0, j0, k0 = 50000, 50001, 50002
e = []
for idx in range(49990, 50010):
    j = idx
    e.append(log(pr[j-1]) - log(p_pnt(j)))
print(f'  ε_j（邻近——）= {[f"{x:.6f}" for x in e[:8]]}')
# ε 的相邻差（涨落的驱动——）
de = np.diff(e)
print(f'  Δε（相邻——）std = {np.std(de):.6f}——量级（小——PNT 好近似——）')
