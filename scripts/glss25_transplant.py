#!/usr/bin/env python3
"""GLSS25 工具移植：Σwδ = -Σu_k·ΔS_k → Abel → ΣΔu_k·S_k → mean(S)=½ + Selberg 矩
u_k = w_k/N₀'(γ_k)——w_k = 1-cos(nθ_k)（r(n) 核）
关键：ΣΔu_k·(S_k-½) 是否 O(1)？——S 的加权和（Selberg 矩控制）
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

z = load_zeros(1000000)

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

# S_k = k - N₀(γ_k)（零点处右极限）
S_k = np.array([(k+1) - N0(z[k]) for k in range(len(z))], dtype=float)

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np

print("Σwδ = -Σu_k·ΔS_k 的 Abel 分解验证（GLSS25 工具）：")
for n in [100, 500, 1000]:
    # w_k = 1-cos(nθ_k)——θ_k = 2arctan(2γ)-π
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    u = w / Np  # u_k = w_k/N₀'
    
    # 直接 Σwδ
    S_wd = np.sum(w * delta)
    
    # Abel：-Σu_k·ΔS_k = -[u_N·S_N - ΣΔu_k·S_{k+1}·(修正)]
    # 用：Σwδ = -Σu·ΔS（δ = -ΔS/N₀'——精确——corr 1.0）
    dS = np.diff(S_k)  # ΔS_k = S_{k+1}-S_k
    # 注意：δ_k ≈ -ΔS_k/N₀'(γ_k)——但 ΔS_k 用 S_{k+1}-S_k（右极限）
    pred = -dS[:len(u)] / Np[:len(u)]
    # 对比 delta（之前算的——用 Δγ）
    corr = np.corrcoef(delta[:len(pred)], pred)[0,1]
    
    # Abel：Σu_k·ΔS_k = u_{N-1}·S_N - ΣΔu_k·S_{k+1}
    du = np.diff(u)
    abel = u[-1]*S_k[-1] - np.sum(du * S_k[1:len(u)])
    # 但 ΔS_k = S_{k+1} - S_k——Σu·ΔS = Σu_k·S_{k+1} - Σu_k·S_k
    # = u_{N-1}·S_N - u_0·S_1 - ΣΔu_k·S_{k+1}（部分求和）
    abel2 = u[-1]*S_k[-1] - u[0]*S_k[0] - np.sum(du * S_k[1:len(u)])
    
    # mean(S)=½ 主项：ΣΔu·(S_{k+1}-½) 的"残差"
    resid_sum = np.sum(du * (S_k[1:len(u)] - 0.5))
    
    print(f"\nn={n}: corr(δ, -ΔS/N₀') = {corr:.4f}")
    print(f"  Σwδ（直接）= {S_wd:+.4f}")
    print(f"  -Σu·ΔS（Abel）= {-abel2:+.4f}（差 {abs(S_wd+abel2):.4f}）")
    print(f"  ΣΔu·(S_{'{k+1}'}-½) = {resid_sum:+.4f}（应 O(1)——Selberg 矩控制）")
    print(f"  Σ|Δu| = {np.sum(np.abs(du)):.4f}  max|Δu| = {np.max(np.abs(du)):.6f}")
