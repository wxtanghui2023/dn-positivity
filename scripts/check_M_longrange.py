#!/usr/bin/env python3
"""关键检验: M(T) 长程行为（O(1) vs O(log)——）用 2M 零点
9/8 封存: M ~ O(log)（系数 0.04-0.06）——今天模型: 几乎周期积分 → O(1)
"""
import numpy as np
from math import log, pi

# 加载 2M 零点
try:
    z = np.load('/tmp/zeros_odlyzko_2M.npy')
    print(f'2M 零点: {len(z)}——γ到 {z[-1]:.0f}')
except:
    print('无 2M 数据——用 200k')
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    K = 200000
    z = np.zeros(K)
    with open(path) as f:
        for i in range(K):
            z[i] = float(f.readline())
    print(f'200k 零点: γ到 {z[-1]:.0f}')

K = len(z)
dg = np.diff(z)
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
# 分块计算 Sbar（内存——）
IntN = np.array([IntN0(t) for t in z[::100]])  # 采样
# 直接算 M 的分块累积（每 50000 零点一块——）
print()
print('M(T) 分块（每 5 万零点——max|M| 和 分段增量——）:')
cumM = 0.0
block_max = 0.0
block_start_M = 0.0
N_block = 50000
M_blocks = []
for b in range(0, K-1, N_block):
    b1 = min(b+N_block, K-1)
    zg = z[b:b1]
    dgg = dg[b:b1]
    kk_g = np.arange(b+1, b1+1)
    # Sbar 在块内
    IntN_g = np.array([IntN0(t) for t in zg])
    IntN_g2 = np.array([IntN0(t) for t in z[b+1:b1+1]])
    Sbar_b = kk_g - (IntN_g2 - IntN_g)/dgg
    M_inc = Sbar_b * dgg
    # 块内累积
    local = np.cumsum(M_inc)
    block_max = max(block_max, np.max(np.abs(cumM + local)))
    cumM += local[-1]
    M_blocks.append(cumM)
    if len(M_blocks) <= 12:
        print(f'  到零点{b1}: M={cumM:+.3f}——块内max|M|={np.max(np.abs(cumM+local)):.3f}')

print()
print(f'最终: M({K})={cumM:+.3f}——max|M|（全程——）≈{block_max:.3f}')
print(f'log(γ_max) = {log(z[-1]):.2f}——如果 O(log): 系数 ~ {block_max/log(z[-1]):.4f}')
print(f'如果 O(1): max|M| 应稳定（~1.3-1.9——）——')
