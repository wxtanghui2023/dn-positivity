#!/usr/bin/env python3
"""干涉测量：两个相位扰动的交叉响应 χ₁₂(ω)——光谱学
γ → γ + ε₁·sin(ωγ) + ε₂·sin(ωγ)（同频——干涉）
χ₁₂ = ∂²λ/∂ε₁∂ε₂——交叉项——选择频率 ω 提取 cos(2nθ₁) 的分量
如果相位均匀性有频率指纹（素数 log p）——χ₁₂ 在特殊 ω 处异常
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

z = load_zeros(300000)

def th1(t):
    return np.arctan(1/(2*t))

def lam_n(n, z):
    return 4*np.sum(np.sin(n*th1(z))**2)

# 交叉响应：χ₁₂(ω) = [λ(+ε,+ε) − λ(+ε,−ε) − λ(−ε,+ε) + λ(−ε,−ε)]/(4ε²)
def chi12(n, z, w, eps=0.3):
    s1 = np.sin(w*z)
    z_pp = z + eps*s1 + eps*s1
    z_pm = z + eps*s1 - eps*s1
    z_mp = z - eps*s1 + eps*s1
    z_mm = z - eps*s1 - eps*s1
    return (lam_n(n, z_pp) - lam_n(n, z_pm) - lam_n(n, z_mp) + lam_n(n, z_mm))/(4*eps*eps)

# 干涉光谱（n=100 固定——扫 ω）
print("干涉光谱 χ₁₂(ω)（n=100——两个同频扰动）：")
print(f"{'ω':>8} {'χ₁₂':>12} {'注':>20}")
ws = [0.1, 0.3, 0.5, 0.69, 0.9, 1.1, 1.3, 1.6, 1.9, 2.4, 3.0, 3.5, 4.6, 5.5, 7.0]
for w in ws:
    chi = chi12(100, z, w)
    note = ""
    for p in [2, 3, 5, 7, 11, 101]:
        if abs(w - log(p)) < 0.2:
            note = f"≈log{p}"
    print(f"{w:8.3f} {chi:+12.4f} {note}")

# 精细扫描（找峰）
print("\n精细扫描（ω ∈ [0.5, 2.5]）：")
ws_f = np.linspace(0.5, 2.5, 41)
chis = np.array([chi12(100, z, w) for w in ws_f])
for i in range(1, len(chis)-1):
    if chis[i] > chis[i-1] and chis[i] > chis[i+1]:
        print(f"  峰 ω={ws_f[i]:.3f}: χ₁₂ = {chis[i]:+.4f}")
    if chis[i] < chis[i-1] and chis[i] < chis[i+1]:
        print(f"  谷 ω={ws_f[i]:.3f}: χ₁₂ = {chis[i]:+.4f}")
print(f"  log2={log(2):.3f} log3={log(3):.3f} log5={log(5):.3f} log7={log(7):.3f} log11={log(11):.3f}")

# 不同 n 的干涉光谱（一致性——指纹检验）
print("\n不同 n 的干涉光谱（指纹一致性）：")
for n in [50, 200, 500]:
    chis_n = np.array([chi12(n, z, w) for w in ws_f])
    # 归一化（n 依赖的幅度）
    chis_norm = chis_n/np.std(chis_n)
    # 关键位置
    print(f"  n={n}: 归一化 χ₁₂ @ log2={chis_norm[8]:+.3f}, log3={chis_norm[16]:+.3f}, log5={chis_norm[25]:+.3f}")

del z
gc.collect()
print("内存已释放")
