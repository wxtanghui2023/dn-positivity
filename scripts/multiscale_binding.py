#!/usr/bin/env python3
"""BKT 多尺度束缚（RG 图像）：run 和的符号是否也交替（二级配对）？
如果 run 和也强交替（p_run > 0.5）——自相似配对——Σδ=O(1) 的机制
—— 多尺度（δ 配对 → run 和配对 → ...）——可能推广到 f_n 核
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

z = load_zeros(1000000)
gz = z[:-1]
dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del z, gz, dg, Np
gc.collect()

# 1. run 和（连续同号 δ 的和）
sign = np.sign(delta)
run_sums = []
s = 0.0
for i in range(len(delta)):
    s += delta[i]
    if i == len(delta)-1 or sign[i] != sign[i+1]:
        run_sums.append(s)
        s = 0.0
run_sums = np.array(run_sums)
del delta, sign
gc.collect()

# 2. run 和的符号翻转概率（二级配对）
rsign = np.sign(run_sums)
p_run = np.mean(rsign[:-1] != rsign[1:])
print(f"run 和的数量：{len(run_sums)}")
print(f"run 和的符号翻转概率 p_run = {p_run:.6f}（δ 的 p = 0.618）")
print(f"  （>0.5 = 二级配对——多尺度束缚——BKT RG）")

# 3. run 和的大小分布
print(f"\nrun 和的统计：mean|·| = {np.mean(np.abs(run_sums)):.4f}  max|·| = {np.max(np.abs(run_sums)):.4f}")

# 4. 三级：run 和的 run（团）
print("\n三级配对（run 和的 run——团）：")
rsign2 = np.sign(run_sums)
runs2 = []
cur = 1
for i in range(1, len(rsign2)):
    if rsign2[i] == rsign2[i-1]:
        cur += 1
    else:
        runs2.append(cur)
        cur = 1
runs2.append(cur)
runs2 = np.array(runs2)
print(f"  团长度分布：mean = {np.mean(runs2):.3f}  1: {np.sum(runs2==1)/len(runs2)*100:.1f}%  2: {np.sum(runs2==2)/len(runs2)*100:.1f}%  3: {np.sum(runs2==3)/len(runs2)*100:.1f}%")

# 5. 团和（三级 run 和）——是否也有界
print("\n团和（run 和的连续同号和）：")
rs2 = []
s2 = 0.0
for i in range(len(run_sums)):
    s2 += run_sums[i]
    if i == len(run_sums)-1 or rsign2[i] != rsign2[i+1]:
        rs2.append(s2)
        s2 = 0.0
rs2 = np.array(rs2)
print(f"  团和：mean|·| = {np.mean(np.abs(rs2)):.4f}  max|·| = {np.max(np.abs(rs2)):.4f}")

# 6. 多尺度累积（δ → run 和 → 团和——每级都配对？）
print("\n多尺度累积（BKT RG——每级配对）：")
print(f"  Σδ（全）= {np.sum(delta) if 'delta' in dir() else '已删'}")
# 重新算 Σδ
print(f"  Σ run 和 = {np.sum(run_sums):.4f}（应 = Σδ）")
print(f"  Σ 团和 = {np.sum(rs2):.4f}（应 = Σδ）")

del run_sums, rsign, rsign2, runs2, rs2
gc.collect()
print("内存已释放")
