#!/usr/bin/env python3
"""∫S·d(cos(2nθ₁)) 的分部积分验证——找数值 O(1) 的来源
直接：ΣS_k·Δcos_k vs 分部：边界[M·Δcos] − ΣM·Δ²cos
M_k = ΣS（累积——∫S）
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

z = load_zeros(500000)

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8
def th1(t):
    return np.arctan(1/(2*t))

S_k = np.array([(k+1) - N0(z[k]) for k in range(500000)], dtype=float)
M = np.cumsum(S_k - 0.5)  # ∫S（去均值——累积）

for n in [100, 500]:
    th = th1(z)
    cos_v = np.cos(2*n*th)
    dcos = np.diff(cos_v)
    d2cos = np.diff(dcos)
    
    # 直接：ΣS_k·Δcos_k（S 右极限——对齐）
    S_align = S_k[1:len(dcos)+1]
    direct = np.sum(S_align * dcos)
    
    # 分部：边界 [M·Δcos] − ΣM·Δ²cos
    M_align = M[1:len(dcos)+1]
    M_align2 = M[1:len(d2cos)+1]
    bd = M_align[-1]*dcos[-1] - M[0]*dcos[0]  # 边界（近似——用端点）
    integ = np.sum(M_align2 * d2cos)
    partial = bd - integ
    
    # M 的量级
    print(f"\nn={n}:")
    print(f"  直接 ΣS·Δcos = {direct:+.6f}")
    print(f"  分部 [M·Δcos]−ΣM·Δ²cos = {partial:+.6f}（边界 {bd:+.6f}——积分 {integ:+.6f}）")
    print(f"  差 = {abs(direct-partial):.6f}")
    print(f"  M 端点 = {M[-1]:+.4f}（max|M| = {np.max(np.abs(M)):.4f}）")

# 检查：如果直接用"中点"S（S(γ_k)+S(γ_{k+1}))/2）
print("\n用中点 S 的 Stieltjes：")
for n in [100, 500]:
    th = th1(z)
    cos_v = np.cos(2*n*th)
    dcos = np.diff(cos_v)
    S_mid = 0.5*(S_k[:-1] + S_k[1:])
    direct_mid = np.sum(S_mid * dcos)
    print(f"  n={n}: ΣS_mid·Δcos = {direct_mid:+.6f}（vs 右极限 {np.sum(S_k[1:len(dcos)+1]*dcos):+.6f}）")

del z, S_k, M
gc.collect()
print("内存已释放")
