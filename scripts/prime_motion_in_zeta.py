#!/usr/bin/env python3
# 在 ζ 里找素数的运动/力：ζ'/ζ（von Mangoldt——素数结构——）的动力学
import mpmath as mp
mp.mp.dps = 12

gamma1 = 14.1347

# ζ'/ζ 沿 σ（在 γ1 高度——）——从 σ=2（von Mangoldt 收敛）到 σ=0.5（零点——极点）
print("=== ζ'/ζ（素数运动——von Mangoldt——）沿 σ（γ1 高度——）===")
print("（ζ'/ζ = -Σ Λ(n)n^{-s}——素数的加权运动——）")
print("σ        Re[ζ'/ζ]      Im[ζ'/ζ]      |ζ'/ζ|")
for sg in [2.0, 1.5, 1.2, 1.0, 0.8, 0.7, 0.6, 0.55, 0.52, 0.5]:
    try:
        v = mp.zeta(complex(sg, gamma1), 1)/mp.zeta(complex(sg, gamma1))
        # 注意：mp.zeta(s, 1) 是 Hurwitz——不是导数！用 diff
        v = mp.diff(mp.zeta, complex(sg, gamma1))/mp.zeta(complex(sg, gamma1))
        print(f"{sg:.2f}   {float(v.real):+10.4f}   {float(v.imag):+10.4f}   {float(abs(v)):10.4f}")
    except Exception as e:
        print(f"{sg:.2f}   错误：{e}")

print()
print("=== 关键：Re ζ'/ζ 沿 σ——素数运动的'径向'——零点（1/2）处 ===")
print("（Re ζ'/ζ 在 σ=1/2（零点）处有极点——+∞ 还是 -∞？——）")
# 靠近零点（σ=0.5+ε——）
for eps in [0.1, 0.05, 0.02, 0.01, 0.005, 0.001]:
    sg = 0.5 + eps
    try:
        v = mp.diff(mp.zeta, complex(sg, gamma1))/mp.zeta(complex(sg, gamma1))
        print(f"σ=0.5+{eps}: Re[ζ'/ζ] = {float(v.real):+12.4f}")
    except Exception as e:
        print(f"σ=0.5+{eps}: 错误")

print()
print("=== ζ'/ζ 的零点-极点结构（素数运动的谱——）===")
print("ζ'/ζ 的极点 = ζ 的零点——素数的加权运动（von Mangoldt）在零点共振——")
print("ζ'/ζ 的零点 = ζ'/ζ=0 处（素数运动'平衡'——）")
print("——素数运动（ζ'/ζ）的'谱'（极点——零点——）——")
