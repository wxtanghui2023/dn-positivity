#!/usr/bin/env python3
"""检查干涉峰间隔 ~0.25 的来源——T 依赖（平凡）vs 普适（有趣）
如果间隔随 T（零点数）变化——拍频（N₀' 依赖）——平凡
如果固定 0.25——普适常数——值得深挖
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

def th1(t):
    return np.arctan(1/(2*t))

def lam_n(n, z):
    return 4*np.sum(np.sin(n*th1(z))**2)

def chi12(n, z, w, eps=0.3):
    s1 = np.sin(w*z)
    z_pp = z + 2*eps*s1
    z_mm = z - 2*eps*s1
    return (lam_n(n, z_pp) - 2*lam_n(n, z) + lam_n(n, z_mm))/(4*eps*eps)

# 不同 T（零点数）的干涉光谱——峰间隔
print("峰间隔 vs 零点数（T 依赖检验）：")
for Nz in [100000, 300000, 500000]:
    z = load_zeros(Nz)
    ws_f = np.linspace(0.5, 2.5, 41)
    chis = np.array([chi12(100, z, w) for w in ws_f])
    # 峰位置
    peaks = []
    for i in range(1, len(chis)-1):
        if chis[i] > chis[i-1] and chis[i] > chis[i+1]:
            peaks.append(ws_f[i])
    if len(peaks) > 2:
        gaps = np.diff(peaks[:5])
        print(f"  N={Nz}: 峰 = {[f'{p:.2f}' for p in peaks[:5]]}——间隔 = {[f'{g:.2f}' for g in gaps]}")
    else:
        print(f"  N={Nz}: 峰少（{len(peaks)}）")
    del z
    gc.collect()

# 理论：拍频——sin²(ωγ) 与零点间距的干涉
# 零点间距 ~ 1/N₀'(γ)——sin²(ωγ) 的"采样"——拍频 ~ 2ω 与 N₀' 的共振？
print("\n理论：干涉项 sin²(ωγ_k)——零点处采样——拍频结构")
print(f"  N₀'(T)（不同 N）：")
for Nz in [100000, 300000, 500000]:
    z = load_zeros(Nz)
    Np = log(z[-1]/(2*pi))/(2*pi)
    print(f"    N={Nz}: N₀'(T) = {Np:.4f}  间距 = {1/Np:.4f}")
    del z
    gc.collect()

# 峰间隔 vs 2π/间距（拍频预测）
print("\n拍频预测：2π/间距 vs 观察间隔 0.25：")
for Nz in [300000]:
    z = load_zeros(Nz)
    Np = log(z[-1]/(2*pi))/(2*pi)
    spacing = 1/Np
    print(f"  N={Nz}: 间距 = {spacing:.4f}  2π/间距 = {2*pi/spacing:.3f}  观察间隔 ≈ 0.25")
    print(f"  2π/(间距·25) = {2*pi/(spacing*25):.4f}（25 = 观察间隔的倒数？）")
    del z
    gc.collect()

print("内存已释放")
