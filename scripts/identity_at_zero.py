#!/usr/bin/env python3
# 层间作用：恒等式 ζ'/ζ(s) = χ'/χ(s) - ζ'/ζ(1-s) 在零点附近
import mpmath as mp
mp.mp.dps = 15

def L(s):
    return mp.diff(mp.zeta, s)/mp.zeta(s)

def chi(s):
    return 2**s * mp.pi**(s-1) * mp.sin(mp.pi*s/2) * mp.gamma(1-s)

def Lchi(s):
    h = mp.mpc(1e-7, 0)
    return (chi(s+h) - chi(s-h))/(2*h)/chi(s)

def find_zero(seed):
    z = mp.mpc(0.5, seed)
    for _ in range(20):
        z = z - mp.zeta(z)/mp.diff(mp.zeta, z)
    return z

rho1 = find_zero(14.1347)
print(f"零点 rho1 = {rho1}")
print()
print("=== 恒等式在 rho1+eps 附近 ===")
for eps in [0.1, 0.01, 0.001]:
    s = rho1 + eps
    lhs = L(s)
    rhs = Lchi(s) - L(1-s)
    print(f"eps={eps}: L={complex(lhs).real:+.5f}{complex(lhs).imag:+.4f}i  RHS={complex(rhs).real:+.5f}{complex(rhs).imag:+.4f}i  差={abs(lhs-rhs):.1e}")

print()
print("=== chi'/chi(rho1) 的值 ===")
lc = Lchi(rho1)
print(f"chi'/chi(rho1) = {complex(lc).real:+.6f} {complex(lc).imag:+.6f}i")

print()
print("=== 解析式验证：chi'/chi = log(2pi) + (pi/2)cot(pi s/2) + digamma(1-s) ===")
s = rho1
analytic = mp.log(2*mp.pi) + (mp.pi/2)*mp.cot(mp.pi*s/2) + mp.digamma(1-s)
print(f"解析 = {complex(analytic).real:+.6f} {complex(analytic).imag:+.6f}i（差={abs(analytic-lc):.1e}）")

print()
print("=== 残差分析 ===")
print("恒等式主项：m/(s-rho) = chi'/chi(rho) + m'/(s-rho)——（在 s=rho 附近——）")
print("若 m=m'（rho 和 1-rho 重数相同——）——chi'/chi(rho) 必须 = 0？")
print(f"但 chi'/chi(rho1) = {complex(lc).real:+.6f}（≠0）——检查残差关系——")
for eps in [1e-4, 1e-5]:
    s = rho1 + eps
    lhs = L(s)
    print(f"eps={eps}: eps*L(rho+eps) = {complex(lhs*eps).real:+.5f}（应→残差 m≈1——）")
    # 右边的主项：chi'/chi - L(1-s)——eps*(...)
    rhs_eps = eps*(Lchi(s) - L(1-s))
    print(f"        eps*RHS = {complex(rhs_eps).real:+.5f}")

print()
print("=== 关键检查：恒等式在零点附近的'相容性'——离轴会怎样？===")
print("若零点离轴（sigma0≠1/2——）——rho 和 1-rho 是不同点——")
print("恒等式：m/(s-rho) 项 vs chi'/chi(rho) - m'/(s-rho)——")
print("主项：(m-m')/(s-rho) = chi'/chi(rho)——（若 m=m'——需 chi'/chi(rho)=0——）")
print("→ 检查：对离轴零点——chi'/chi(rho) 是否必须满足某条件（与在线不同——）")
