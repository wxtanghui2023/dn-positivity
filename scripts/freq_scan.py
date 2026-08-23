#!/usr/bin/env python3
"""频率扫描实验（外力 = 单一频率扰动——找共振）
γ_k → γ_k + ε·sin(ω·γ_k)——频率 ω 扫描
响应 Δλ_n(ω)——共振峰 = 零点结构的本征频率
关键：ω = log p（素数——相位均匀性的频率）处是否特殊？
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

# 频率扫描（n=100 固定——扫 ω）
print("频率扫描：外力 γ → γ + ε·sin(ωγ)——响应 Δλ_n(ω)（n=100, ε=0.5）：")
base = lam_n(100, z)
omegas = [0.01, 0.03, 0.1, 0.3, 0.5, 0.69, 1.0, 1.1, 1.6, 2.4, 3.0, 4.6, 5.0, 7.0, 10.0]
# 素数 log p：log2=0.69, log3=1.10, log5=1.61, log11=2.40, log101=4.62
print(f"{'ω':>8} {'Δλ(ω)':>12} {'注':>20}")
for w in omegas:
    z_p = z + 0.5*np.sin(w*z)
    dl = lam_n(100, z_p) - base
    note = ""
    for p in [2, 3, 5, 11, 101]:
        if abs(w - log(p)) < 0.15:
            note = f"≈log{p}（素数！）"
    print(f"{w:8.3f} {dl:+12.4f} {note}")

# 更精细的扫描（ω 附近——找峰）
print("\n精细扫描（ω ∈ [0.5, 2.5]——素数 log 附近）：")
ws = np.linspace(0.5, 2.5, 41)
responses = []
for w in ws:
    z_p = z + 0.5*np.sin(w*z)
    responses.append(lam_n(100, z_p) - base)
responses = np.array(responses)

# 峰值检测
for i in range(1, len(responses)-1):
    if responses[i] > responses[i-1] and responses[i] > responses[i+1]:
        print(f"  峰在 ω={ws[i]:.3f}（Δλ={responses[i]:+.4f}）")
    if responses[i] < responses[i-1] and responses[i] < responses[i+1]:
        print(f"  谷在 ω={ws[i]:.3f}（Δλ={responses[i]:+.4f}）")

# 关键位置标记
print(f"\n关键频率：log2={log(2):.3f} log3={log(3):.3f} log5={log(5):.3f} log7={log(7):.3f} log11={log(11):.3f} log13={log(13):.3f}")
print(f"平均间距倒数：1/⟨Δγ⟩ = N₀'(T) = {log(z[-1]/(2*pi))/(2*pi):.4f}")

del z
gc.collect()
print("内存已释放")
