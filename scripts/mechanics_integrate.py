#!/usr/bin/env python3
# 力学分析：用合规力（自洽方程——）从初始积分零点轨迹——算终点（决定论实现——）
# dρ/dX = F(ρ,X) = -(∂ζ_X/∂X)/ζ_X'(ρ)——从 X0 积分到 X_large——看 ρ(X)
import numpy as np

def zeta_X(s, X, nmax_factor=15):
    nmax = max(int(nmax_factor*X), 300)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def force(rho, X):
    """合规力 F = -(∂ζ_X/∂X)/ζ_X'(ρ)——∂ζ_X/∂X = (1/X²)Σ n^{1-ρ} e^{-n/X}"""
    h = 1e-6 + 1e-6j
    zXp = (zeta_X(rho+h, X) - zeta_X(rho-h, X))/(2*h)
    nmax = max(int(15*X), 300)
    n = np.arange(1, nmax+1, dtype=np.float64)
    dX = (1/X**2) * np.sum(n**(1-complex(rho)) * np.exp(-n/X))
    return -dX / zXp

def integrate_trajectory(rho0, X0, X_end, steps=400):
    """从 (X0, rho0) 出发——用 RK4 积分 dρ/dX = F——到 X_end"""
    X = X0
    rho = rho0
    traj = [(X, rho.real, rho.imag)]
    # 对数步长（X 从 X0 到 X_end——指数间隔——因为 1/X 运动——）
    logX0, logXe = np.log(X0), np.log(X_end)
    logXs = np.linspace(logX0, logXe, steps)
    for i in range(len(logXs)-1):
        lx1, lx2 = logXs[i], logXs[i+1]
        X1 = np.exp(lx1)
        h = np.exp(lx2) - X1  # 步长（X 空间——）
        # RK4
        k1 = force(rho, X1)
        k2 = force(rho + h/2*k1, X1 + h/2)
        k3 = force(rho + h/2*k2, X1 + h/2)
        k4 = force(rho + h*k3, X1 + h)
        rho = rho + h/6*(k1 + 2*k2 + 2*k3 + k4)
        X = np.exp(lx2)
        traj.append((X, rho.real, rho.imag))
    return traj

gamma1 = 14.1347
print("=== 力学积分：从不同初始 X0——积分零点轨迹——终点（决定论——）===")
for X0 in [20, 50]:
    # 初始位置：ζ_X0 的零点（γ1 附近——）
    z = complex(0.4, gamma1)
    for it in range(60):
        f = zeta_X(z, X0)
        h = 1e-6+1e-6j
        fp = (zeta_X(z+h, X0)-zeta_X(z-h, X0))/(2*h)
        step = f/fp
        z = z - step
        if abs(step) < 1e-12: break
    print(f"\n从 X0={X0} 出发——初始 ρ = {z.real:.5f}+{z.imag:.5f}i——积分到 X=2000：")
    traj = integrate_trajectory(z, X0, 2000)
    for X, b, g in traj[::80] + [traj[-1]]:
        print(f"  X={X:>6.1f}: β = {b:.6f}  γ = {g:.4f}")
