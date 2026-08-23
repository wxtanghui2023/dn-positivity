#!/usr/bin/env python3
"""BKT 束缚的量化：δ 的符号翻转间隔（run length）分布
束缚对尺寸有限（短程配对）⟹ 局部抵消 ⟹ Σδ=O(1) 可证
验证：run length 的分布——有界/短尾？
"""
import numpy as np
import math
from math import log, pi
import gc

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)
gz = z[:-1]

dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del dg, Np, gz
gc.collect()

# run length：连续同号 δ 的长度
sign = np.sign(delta)
runs = []
cur = 1
for i in range(1, len(sign)):
    if sign[i] == sign[i-1]:
        cur += 1
    else:
        runs.append(cur)
        cur = 1
runs.append(cur)
runs = np.array(runs)

print(f"δ 的符号 run length 分布（束缚对尺寸）：{len(runs)} 个 run")
print(f"  mean = {np.mean(runs):.3f}  median = {np.median(runs):.1f}  max = {np.max(runs)}")
print(f"  p95 = {np.percentile(runs, 95):.0f}  p99 = {np.percentile(runs, 99):.0f}")

# 分布形状
print("\nrun length 分布：")
for r in [1, 2, 3, 4, 5, 6, 8, 10, 15, 20]:
    cnt = np.sum(runs == r)
    print(f"  len={r:3d}: {cnt:7d}（{cnt/len(runs)*100:.2f}%）")

# 关键：run 的"净贡献"——每个 run 的 δ 和（配对抵消检验）
print("\n每个 run 的净 δ 和（配对抵消——束缚）：")
# 分组：连续同号段的和
group_sums = []
s = 0.0
for i in range(len(delta)):
    s += delta[i]
    if i == len(delta)-1 or sign[i] != sign[i+1]:
        group_sums.append(s)
        s = 0.0
group_sums = np.array(group_sums)
print(f"  mean |run 和| = {np.mean(np.abs(group_sums)):.4f}")
print(f"  max |run 和| = {np.max(np.abs(group_sums)):.4f}")
print(f"  （若小——配对抵消——束缚——Σδ=O(1) 的机制）")

# run 和的分布尾部
print(f"  |run 和| > 0.5: {np.sum(np.abs(group_sums)>0.5)}（{np.sum(np.abs(group_sums)>0.5)/len(group_sums)*100:.2f}%）")
print(f"  |run 和| > 1.0: {np.sum(np.abs(group_sums)>1.0)}")

del delta, sign, runs, group_sums
gc.collect()
print("\n内存已释放")
