#!/usr/bin/env python3
"""精确验证：δ 符号翻转概率 p = 1/φ（黄金比例——0.618034）？
准晶（Fibonacci）特征：p = 1/φ——run length 分布 Fibonacci 型
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

# 分块加载（内存管理）
PHI = (np.sqrt(5)-1)/2  # 0.6180339887...
print(f"黄金比例 1/φ = {PHI:.10f}")

# 逐块计算 p（避免加载全部）
total_flip = 0
total_n = 0
prev_sign = None
CHUNK = 200000
with open('/home/node/.openclaw/workspace/dn-project/zeros/zeros6') as f:
    chunk = []
    for line in f:
        chunk.append(float(line))
        if len(chunk) == CHUNK:
            zc = np.array(chunk)
            gzc = zc[:-1]
            dgc = np.diff(zc)
            Npc = np.log(gzc/(2*pi))/(2*pi)
            delta_c = dgc - 1.0/Npc
            sign_c = np.sign(delta_c)
            if prev_sign is not None:
                # 跨块边界
                if prev_sign == sign_c[0]:
                    total_n += 1
                else:
                    total_flip += 1; total_n += 1
            flips = np.sum(sign_c[:-1] != sign_c[1:])
            total_flip += flips
            total_n += len(sign_c) - 1
            prev_sign = sign_c[-1]
            chunk = []
            del zc, gzc, dgc, Npc, delta_c, sign_c
            gc.collect()
    # 剩余
    if chunk:
        zc = np.array(chunk)
        gzc = zc[:-1]
        dgc = np.diff(zc)
        Npc = np.log(gzc/(2*pi))/(2*pi)
        delta_c = dgc - 1.0/Npc
        sign_c = np.sign(delta_c)
        if prev_sign is not None:
            if prev_sign == sign_c[0]:
                total_n += 1
            else:
                total_flip += 1; total_n += 1
        flips = np.sum(sign_c[:-1] != sign_c[1:])
        total_flip += flips
        total_n += len(sign_c) - 1
        del zc, gzc, dgc, Npc, delta_c, sign_c
        gc.collect()

p = total_flip/total_n
print(f"\n全 {total_n:,} 个相邻对：翻转 = {total_flip:,}")
print(f"p = {p:.10f}")
print(f"1/φ = {PHI:.10f}")
print(f"差 = {abs(p-PHI):.2e}")
print(f"{'✅ p = 1/φ（黄金比例——准晶！）' if abs(p-PHI) < 1e-4 else '接近但需更多数据'}")

# 黄金比例的来源猜想：p = 1/φ 意味着 run length 分布 ~ Fibonacci
# run 1: 比例 p1 = p（第一个翻转）？——run length 几何：P(len=k) = p(1-p)^{k-1}？
# 若 p = 0.618：P(1) = 0.618, P(2) = 0.236, P(3) = 0.090——vs 实际 0.578, 0.278, 0.103
print(f"\nrun length 几何预测（p = {p:.4f}）：")
for k in [1, 2, 3, 4]:
    pred = p*(1-p)**(k-1)
    print(f"  P(len={k}) 预测 = {pred:.4f}（实际：{0.578 if k==1 else 0.278 if k==2 else 0.103 if k==3 else 0.031}）")
