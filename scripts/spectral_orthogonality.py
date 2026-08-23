#!/usr/bin/env python3
"""频谱正交：A_k（Σδ 部分和——低频压制）vs Δw（f_n 核——高频）
ΣΔw·A_k = 频谱重叠积分——如果频段分离——O(1) 可证
物理：不同频率的功率谱正交
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
del dg, Np
gc.collect()

Sd = np.cumsum(delta)
A_inf = Sd[-1]
A = Sd - A_inf  # A_k（零均值化）

# A 的功率谱（FFT——低频压制检验）
def power_spectrum(x):
    n = len(x)
    X = np.fft.rfft(x - np.mean(x))
    return np.abs(X)**2/n

PS_A = power_spectrum(A[:200000])
freqs = np.fft.rfftfreq(200000, d=1.0)
print("A_k 的功率谱（低频压制——守恒 ⟹ f→0 处 → 0？）：")
for f in [1, 5, 10, 50, 100, 500]:
    idx = int(f)
    if idx < len(PS_A):
        print(f"  频率 f={f}: PS_A = {PS_A[idx]:.6f}")

# Δw 的功率谱（f_n 核——n=100）
print("\nΔw（f_n 核 n=100）的功率谱（高频）：")
th = 2*np.arctan(2*z[:-1]) - pi
w = 1 - np.cos(100*th)
dw = np.diff(w)
PS_dw = power_spectrum(dw[:200000])
# Δw 的主要频率——θ₁' ~ 1/t²——sin(2nθ₁) 频率 ~ 2n·|θ₁'| ~ 200/t²
print(f"  理论频率范围：~200/t²（t=14: ~1.0——t=1000: ~0.0002）")
for f in [1, 5, 10, 50, 100, 500, 1000]:
    idx = int(f)
    if idx < len(PS_dw):
        print(f"  频率 f={f}: PS_dw = {PS_dw[idx]:.6f}")

# 关键：频谱重叠——ΣΔw·A_k = ∫S_Δw(f)·S_A(f)·cos(相位)df
# 简化：检查 A 的低频 vs Δw 的频率分布——是否分离
print("\n频谱重叠检验（A 低频 vs Δw 频率分布）：")
cum_A = np.cumsum(PS_A) / np.sum(PS_A)
cum_dw = np.cumsum(PS_dw) / np.sum(PS_dw)
for pct in [0.5, 0.9, 0.99]:
    fA = np.searchsorted(cum_A, pct)
    fdw = np.searchsorted(cum_dw, pct)
    print(f"  {pct*100:.0f}% 能量：A ≤ f={fA}——Δw ≤ f={fdw}")

# 直接：ΣΔw·A_k 的数值（已知 O(1)——验证）
n = 100
w2 = 1 - np.cos(n*th)
dw2 = np.diff(w2)
S_wa = np.sum(dw2 * A[:len(dw2)])
print(f"\nΣΔw·A_k（n=100）= {S_wa:+.4f}（O(1)——目标）")

del z, gz, delta, Sd, A, w, dw, th
gc.collect()
print("内存已释放")
