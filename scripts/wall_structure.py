#!/usr/bin/env python3
""""墙"视角：ζ 零点 = 凸势 ψ 的墙（尖峰）——墙之间的行为
ψ(t) = Σlog(1/|t−γ|) − θ(t)——零点处 +∞（墙）
墙之间（零点之间）：ψ 凸——最小值（谷底）——谷底位置与零点间距的关系
"""
import numpy as np
import math
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(10000)

# 墙之间：ψ 的谷底（最小值）——在 [γ_k, γ_{k+1}] 内
# ψ' = Σ1/(γ−t) − θ' = 0 的根（谷底——凸最小）
def psi_prime(t, z, W=2000):
    idx = np.searchsorted(z, t)
    lo = max(0, idx-W); hi = min(len(z), idx+W)
    s = 0.0
    for j in range(lo, hi):
        d = t - z[j]
        if abs(d) > 0.5:
            s += 1.0/d
    return -s - 0.5*log(t/(2*pi))  # ψ' = −Σ1/(t−γ) − θ'（检查符号）

# 谷底位置：ψ' = 0 在区间内
print("墙之间（零点之间）的谷底位置：")
print(f"{'区间':>8} {'γ_k':>10} {'γ_{k+1}':>10} {'谷底 t*':>10} {'(t*−γ_k)/(γ_{k+1}−γ_k)':>20}")
for k in [100, 500, 1000, 2000, 5000]:
    a, b = z[k-1], z[k]
    # 谷底（ψ' 过零）——扫描
    ts = np.linspace(a+0.5, b-0.5, 20)
    pps = [psi_prime(t, z) for t in ts]
    # 找 ψ' 过零（符号变化）
    t_star = None
    for i in range(len(ts)-1):
        if pps[i]*pps[i+1] < 0:
            t_star = 0.5*(ts[i]+ts[i+1])
            break
    frac = (t_star-a)/(b-a) if t_star else float('nan')
    print(f"k={k:6d} {a:10.3f} {b:10.3f} {t_star if t_star else float('nan'):10.3f} {frac:20.3f}")

# 谷底位置 vs 均匀（1/2 处）——零点在墙之间的"重心"
print("\n谷底分数位置（应 ≈ 0.5 如果对称）：")
fracs = []
for k in range(100, 9000, 50):
    a, b = z[k-1], z[k]
    ts = np.linspace(a+0.5, b-0.5, 10)
    pps = [psi_prime(t, z, 500) for t in ts]
    for i in range(len(ts)-1):
        if pps[i]*pps[i+1] < 0:
            t_star = 0.5*(ts[i]+ts[i+1])
            fracs.append((t_star-a)/(b-a))
            break
fracs = np.array(fracs)
print(f"  平均 = {np.mean(fracs):.4f}  std = {np.std(fracs):.4f}（≈0.5 = 对称——谷底在中间）")
