#!/usr/bin/env python3
"""验证 Σ_k sin(γ_k log p) = O(1)？—— 相位均匀性检查
关键问题：零点指数和 Σ_{k≤K} e^{iγ_k log p} 的有界性
数值显示 ±4（K 到 2e5）—— 但要验证更大 K 和不同 p
"""
import numpy as np
import sys, time

# 读取零点（zeros6 前 N 个）
def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 2000000
print(f"loading {K} zeros...", flush=True)
t0 = time.time()
z = load_zeros(K)
print(f"loaded in {time.time()-t0:.1f}s, γ range: [{z[0]:.3f}, {z[-1]:.3f}]")

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 也测非素数 x（e^x 非整数）对照
xs = [np.log(p) for p in primes] + [0.5, 1.0, 2.0, 3.0]

print(f"\n{'x':>8} {'p=e^x':>10} | {'K=1e4':>10} {'K=1e5':>10} {'K=5e5':>10} {'K=1e6':>10} {'K=2e6':>10} | {'max|S|':>10}")
for x in xs:
    vals = []
    for Kk in [10000, 100000, 500000, 1000000, 2000000]:
        s = np.sum(np.sin(z[:Kk] * x))
        vals.append(s)
    # 全范围 max 部分和
    S = np.cumsum(np.sin(z * x))
    mx = np.max(np.abs(S))
    pe = np.exp(x)
    plab = f"{pe:.2f}" if pe < 1000 else f"{pe:.0e}"
    print(f"{x:8.4f} {plab:>10} | " + " ".join(f"{v:10.3f}" for v in vals) + f" | {mx:10.2f}")
