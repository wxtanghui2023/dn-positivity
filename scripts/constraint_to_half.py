#!/usr/bin/env python3
# 攻：约束（Σ v_n = 0——零点——）⟹ σ=1/2
# 思路：约束 + 运动方程（v_n 如何随 σ 变化）——看能否推出 σ=1/2
# 约束：1 + Σ_{n≥2} n^{-ρ} = 0（ρ = σ+it——零点——）
# 运动方程：∂v_n/∂σ = -log n · v_n——∂v_n/∂t = -i log n · v_n

import numpy as np
import mpmath as mp
mp.mp.dps = 12

# 用平滑（ζ_X——X 大——）处理条件收敛
def zeta_smooth(s, X):
    nmax = max(int(15*X), 300)
    n = np.arange(1, nmax+1)
    return np.sum(n**(-s) * np.exp(-n/X))

# 关键探索：约束（ζ=0）的解——沿"零点轨迹"（γ 固定——σ 扫描——）
# ζ(σ+it) 的实部 u(σ)——在零点高度——u 沿 σ 的行为
# 零点处 u=0——"停"在 σ 意味着——u 沿 σ 的"穿过"（符号变化——）
# Re ζ'(ρ) > 0 ⟹ u 从负到正穿过（σ 增大方向——）

# 检查：u(σ, t) 沿 σ——对"非零点高度"（t 远离零点——）的符号结构
# 如果 u(σ,t) 在 σ<1/2 与 σ>1/2 有"系统性符号"（——）——零点只能穿过 1/2——

print("=== 约束解（零点）的 σ 位置：u=Re ζ 沿 σ 的符号结构 ===")
# 在零点高度 γ1——u(σ) 沿 σ（从 0.3 到 0.7——）——零点在 σ=1/2（u 穿过 0——）
gamma1 = 14.1347
X = 5000
print(f"γ1 高度（零点在 σ=1/2——）：u(σ) 沿 σ：")
for sg in [0.3, 0.4, 0.45, 0.48, 0.5, 0.52, 0.55, 0.6, 0.7]:
    u = zeta_smooth(complex(sg, gamma1), X).real
    print(f"  σ={sg:.2f}: u = {u:+.4f}")

print()
print("=== 非零点高度（t=16——远离零点——）：u 沿 σ 的符号 ===")
for sg in [0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7]:
    u = zeta_smooth(complex(sg, 16.0), X).real
    print(f"  σ={sg:.2f}: u = {u:+.4f}")

print()
print("=== 关键问题：u(σ,t) 沿 σ 的'穿过结构'——零点只穿过 σ=1/2？===")
print("（若 u(σ,t)=0 与 v(σ,t)=0 的交点（零点——）只在 σ=1/2——RH——）")
print("（这 = 0-1/2 压缩——等价 RH——）")
print()
print("=== 运动方程视角：约束 Σv_n=0 对 σ 的依赖 ===")
print("约束：1 + Σ_{n≥2} n^{-σ}e^{-it log n} = 0——取实部：")
print("  1 + Σ n^{-σ}cos(t log n) = 0（平滑——）")
print("  ⟹ Σ n^{-σ}cos(t log n) = -1（n≥2——）——'抵消 n=1 的 +1'")
print("  左边是 σ 的单调函数吗？——检查——")
print()
# 检查 G(σ) = Σ_{n≥2} n^{-σ}cos(γ1 log n)（平滑——）随 σ——单调？
print("G(σ) = Σ_{n≥2} n^{-σ}cos(γ1 log n)（平滑 X=5000——）：")
prev = None
for sg in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]:
    G = 0.0
    nmax = int(5*X)
    n = np.arange(2, nmax)
    G = np.sum(n**(-sg) * np.cos(gamma1*np.log(n)) * np.exp(-n/X))
    print(f"  σ={sg:.2f}: G = {G:+.4f}")
