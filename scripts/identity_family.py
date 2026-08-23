#!/usr/bin/env python3
"""抵消恒等式家族：∫S·d(cos(2nθ₁)) 是否无条件 → 0？
Σcos(2nθ₁(γ_k)) = ∫cos·N₀' + ∫cos·dS（Stieltjes——N = N₀ + S）
∫cos·dS = [cos·S] − ∫S·d(cos)——S 的加权积分
分部积分两次：∫S·d(cos) = [M·d(cos)] − ∫M·d²(cos)——M=∫S=O(logT)——d²(cos)~n²/t⁴
验证：∫S·d(cos(2nθ₁)) 的量级——是否 → 0？
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

# S(t) 在零点间（线性插值近似——S(γ_k) 处精确）
S_k = np.array([(k+1) - N0(z[k]) for k in range(500000)], dtype=float)

# ∫S·d(cos(2nθ₁)) = Σ_k S_k·(cos(2nθ₁(γ_{k+1})) − cos(2nθ₁(γ_k)))（Stieltjes——分段）
def th1(t):
    return np.arctan(1/(2*t))

print("∫S·d(cos(2nθ₁)) 的量级（Stieltjes——S 的加权积分）：")
print(f"{'n':>6} {'ΣS·Δcos':>14} {'边界[cos·S]':>14} {'−∫S·dcos':>14}")
for n in [50, 100, 200, 500, 1000]:
    th = th1(z[:-1])
    cos_val = np.cos(2*n*th)
    dcos = np.diff(cos_val)  # 长度 499998
    # ΣS·Δcos（Stieltjes——Δcos_k = cos_{k+1}−cos_k——S 取中值）
    S_st = 0.5*(S_k[:-1] + S_k[1:])  # 长度 499999——不对齐——改用 S_k[1:] 与 dcos 对齐
    S_align = S_k[1:len(dcos)+1]
    int_S_dcos = np.sum(S_align * dcos)
    # 边界 [cos·S]
    bd = cos_val[-1]*S_k[-1] - cos_val[0]*S_k[0]
    print(f"{n:6d} {int_S_dcos:+14.4f} {bd:+14.4f} {bd - int_S_dcos:+14.4f}")

# 分部积分两次验证：∫S·d(cos) = [M·d(cos)] − ∫M·d²(cos)
print("\n分部积分两次（M = ∫S——Littlewood O(logT)）：")
M = np.cumsum(S_k - 0.5)  # ∫S（去均值——均值 ½）
for n in [100, 500]:
    th = th1(z[:-1])
    cos_val = np.cos(2*n*th)
    dcos = np.diff(cos_val)
    d2cos = np.diff(dcos)
    # [M·d(cos)]——边界
    bd2 = M[-2]*dcos[-1] - M[0]*dcos[0]
    # ∫M·d²cos（分段）
    int_M_d2 = np.sum(M[:-1] * d2cos)
    print(f"  n={n}: [M·Δcos] = {bd2:+.4f}  ∫M·Δ²cos = {int_M_d2:+.4f}  ΣS·Δcos（直接）= {np.sum(S_st*np.diff(np.cos(2*n*th))):+.4f}")

# 量级分析：∫M·d²(cos) ~ ∫O(logT)·O(n²/t⁴)dt——应该很小
print("\n理论量级：d²(cos) ~ (2nθ₁')² + 2nθ₁''——θ₁'~1/t²——d²cos ~ 4n²/t⁴：")
T = z[-1]
for n in [100, 1000]:
    est = 4*n*n*log(T)/(3*T**3)  # ∫4n²/t⁴·log t dt ~ 4n²logT/(3T³)
    print(f"  n={n}: ∫M·d²cos 估计 ~ {est:.6f}（→ 0——T 大）")
    print(f"  边界 [M·dcos] ~ M·2n/T² ~ {np.max(np.abs(M)):.1f}·2·{n}/{T**2:.0f} = {np.max(np.abs(M))*2*n/T**2:.6f}")

del z, S_k, M
gc.collect()
print("内存已释放")
