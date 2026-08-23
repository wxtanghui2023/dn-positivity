#!/usr/bin/env python3
"""扫描 max|Σsin(γ_k x)| 对连续 x 的行为——O(1) 的一致性检查
x 从 0.3 到 6，密集采样——每个 x 算部分和的最大绝对值
如果 max|Σsin| 随 x 增长 → 不是一致 O(1)；如果平坦 → O(1) 对连续 x 成立
"""
import numpy as np

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(2000000)
print(f"K={len(z)}")

# 采样部分和（每 1000 个零点取一个检查点，减少计算）
checkpoints = np.arange(1000, len(z)+1, 1000)
xs = np.arange(0.3, 6.01, 0.05)
print(f"\n{'x':>6} | max|Σsin| | Σsin(K) | max|Σcos| | Σcos(K)")
results = []
for x in xs:
    # 快速：用分块 cumsum 太大——直接每 1000 块
    # 先算全量 cumsum（2M float——OK）
    S = np.cumsum(np.sin(z*x))
    Sc = np.cumsum(np.cos(z*x))
    mx = np.max(np.abs(S[checkpoints-1]))
    mxc = np.max(np.abs(Sc[checkpoints-1]))
    results.append((x, mx, S[-1], mxc, Sc[-1]))

for x, mx, sf, mxc, scf in results:
    print(f"{x:6.2f} | {mx:9.2f} | {sf:8.3f} | {mxc:9.2f} | {scf:9.1f}")
