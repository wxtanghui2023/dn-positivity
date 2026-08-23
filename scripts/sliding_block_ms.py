#!/usr/bin/env python3
"""关键验证：Σδ=O(1) ⟹ 1+2Σρ = 0 的推导路径
B_L（滑动块和）= O(1) 有界 ⟹ 均方（时间平均）O(1) ⟹ 压缩比 → 0？
验证：(1/N)Σ_k (Σ_{j=k}^{k+L}δ_j)² 的行为——不随 L 增长？
"""
import numpy as np
import gc
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(2000000)
gz = z[:-1]
dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del z, gz, dg, Np
gc.collect()

# 滑动块和 B_{k,L} = Σ_{j=k}^{k+L-1}δ_j——用 cumsum 快速算
Sd = np.cumsum(delta)

print("滑动块和均方（时间平均）——不随 L 增长 = 压缩推导成功：")
print(f"{'L':>8} {'(1/N)Σ B²':>14} {'max|B|':>10} {'压缩比':>10}")
for L in [10, 100, 1000, 10000, 100000]:
    # B_{k,L} = Sd[k+L] - Sd[k]
    if L >= len(Sd) - 1: break
    B = Sd[L:] - Sd[:-L]
    ms = np.mean(B**2)
    var_ind = L * np.var(delta)
    ratio = ms/var_ind
    print(f"{L:8d} {ms:14.6f} {np.max(np.abs(B)):10.3f} {ratio:10.6f}")

# 理论预测：如果 B = O(1) 有界——ms = E[B²] ≤ C²——不随 L 增长
# 独立预测：ms = L·Var(δ)——随 L 增长——压缩 = ms/var_ind → 0
print("\n关键：ms 随 L 增长还是 O(1)？")
L_vals = [10, 100, 1000, 10000, 100000]
ms_vals = []
for L in L_vals:
    B = Sd[L:] - Sd[:-L]
    ms_vals.append(np.mean(B**2))
ms_vals = np.array(ms_vals)
print(f"  ms: {ms_vals}")
print(f"  增长指数（log ms vs log L）：")
import numpy.polynomial.polynomial as P
coef = np.polyfit(np.log(L_vals), np.log(ms_vals), 1)
print(f"  ms ~ L^{coef[0]:.3f}（0 = O(1)——有界——压缩成功；1 = 独立——无压缩）")

del delta, Sd
gc.collect()
print("内存已释放")
