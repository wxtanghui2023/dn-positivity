#!/usr/bin/env python3
"""决定性检验：Σsin(γ_k x) 对 x 的敏感性
x = 3.85 vs x = log 47 = 3.850147...—— 微小差异是否导致巨大行为变化？
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
K = len(z)

import math
xs = [3.85, math.log(47), 3.8501, 3.850147, 3.8501477, 3.850147701]
print(f"log(47) = {math.log(47):.10f}")
for x in xs:
    S = np.cumsum(np.sin(z*x))
    Sc = np.cumsum(np.cos(z*x))
    print(f"x={x:.10f}: max|Σsin|={np.max(np.abs(S)):10.2f}  Σsin(K)={S[-1]:+10.3f}  max|Σcos|={np.max(np.abs(Sc)):10.2f}  Σcos(K)={Sc[-1]:+10.3f}")
