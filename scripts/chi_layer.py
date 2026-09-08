#!/usr/bin/env python3
# χ/FE 层分析：ζ'/ζ(s) = χ'/χ(s) - ζ'/ζ(1-s)——素数运动与 χ 的连接
import mpmath as mp
mp.mp.dps = 12

def L(s):
    return mp.diff(mp.zeta, s)/mp.zeta(s)

def chi(s):
    # χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s)
    return 2**s * mp.pi**(s-1) * mp.sin(mp.pi*s/2) * mp.gamma(1-s)

def Lchi(s):
    # χ'/χ = log 2 + log π + (π/2)cot(πs/2) - d/ds[log Γ(1-s)]... 用数值
    h = mp.mpc(1e-6, 0)
    return (chi(s+h) - chi(s-h))/(2*h)/chi(s)

print("=== 验证恒等式：ζ'/ζ(s) = χ'/χ(s) - ζ'/ζ(1-s) ===")
for s in [mp.mpc(0.6, 14.0), mp.mpc(0.7, 8.0), mp.mpc(0.5, 16.0), mp.mpc(0.4, 25.0)]:
    lhs = L(s)
    rhs = Lchi(s) - L(1-s)
    print(f"s={s}: 左={lhs:.4f}  右={rhs:.4f}  差={abs(lhs-rhs):.1e}")

print()
print("=== σ=1/2 线：2Re[ζ'/ζ(1/2+it)] = Re[χ'/χ(1/2+it)]（非零点高度——）===")
print("t        Re[ζ'/ζ]   2Re[ζ'/ζ]   Re[χ'/χ]   差")
for t in [8.0, 12.0, 16.0, 18.0, 23.0, 28.0]:
    try:
        l = L(mp.mpc(0.5, t))
        lc = Lchi(mp.mpc(0.5, t))
        print(f"{t:>5.1f}   {float(l.real):+9.4f}  {float(2*l.real):+9.4f}  {float(lc.real):+9.4f}  {float(abs(2*l.real-lc.real)):.1e}")
    except Exception as e:
        print(f"{t}: 错误 {e}")

print()
print("=== Re[χ'/χ(1/2+it)] 的结构（素数运动在 1/2 线的'力'——由 χ 定——）===")
print("χ'/χ = log 2 + log π + (π/2)cot(πs/2) + Γ'/Γ(1-s)——在 s=1/2+it：")
print("（cot(π(1/2+it)/2) = cot(π/4 + iπt/2)——振荡项——Γ'/Γ(1/2-it)——Stirling——）")
print()
print("=== 关键：Re[χ'/χ] 在 σ=1/2 线——随 t 的行为 ===")
prev = None
for t in mp.arange(5, 40, 2.5):
    lc = Lchi(mp.mpc(0.5, t))
    print(f"t={float(t):>5.1f}: Re[χ'/χ] = {float(lc.real):+10.4f}  Im = {float(lc.imag):+10.4f}")
