#!/usr/bin/env python3
"""突破口：r(n) = 零点采样的 Weyl 误差——Erdős-Turán 路径
r(n) = Σ_γ f_n(γ) − ∫ f_n N₀'——"采样 vs 积分"——Weyl 差
Erdős-Turán：|(1/N)Σ e^{2πi·k·x_j} − ∫e^{2πikx}dx| ≤ 界（discrepancy）
验证：f_n 核的"采样 − 积分"——是否 = Weyl 误差——Erdős-Turán 界的量级
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

z = load_zeros(1000000)
gz = z[:-1]

# f_n 核：f_n(t) = 4sin²(nθ₁(t))——θ₁ = arctan(1/2t)
def f_n(t, n):
    th1 = np.arctan(1/(2*t))
    return 4*np.sin(n*th1)**2

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

# r(n) 的"采样 − 积分"分解
print("r(n) = 采样 − 积分（Weyl 差——f_n 核）：")
print(f"{'n':>6} {'采样 Σf_n':>12} {'integral':>14} {'weyl diff':>12}")
for n in [50, 100, 200, 500, 1000]:
    # 采样（零点处）
    fn_g = f_n(gz, n)
    sample = np.sum(fn_g)
    # 积分（∫f_n·N₀'——数值）
    from scipy.integrate import quad
    integ, _ = quad(lambda t: f_n(np.array([t]), n)[0]*N0p(t), z[0], gz[-1], limit=2000)
    diff = sample - integ
    print(f"{n:6d} {sample:12.4f} {integ:14.4f} {diff:+12.4f}")

# 关键：f_n 的 Weyl 结构——f_n = 4sin²(nθ₁) = 2 − 2cos(2nθ₁)
# cos(2nθ₁) 是"振荡项"——采样和 = 主项（2−2·振荡积分）+ Weyl 误差
print("\nWeyl 结构：f_n = 2 − 2cos(2nθ₁)——cos 项的采样 vs 积分：")
for n in [100, 500]:
    th1 = np.arctan(1/(2*gz))
    cos_fn = np.cos(2*n*th1)
    sample_cos = np.sum(cos_fn)
    integ_cos, _ = quad(lambda t: np.cos(2*n*np.arctan(1/(2*t)))*N0p(t), z[0], gz[-1], limit=2000)
    print(f"  n={n}: Σcos(2nθ₁) = {sample_cos:+.4f}  ∫cos(2nθ₁)N₀' = {integ_cos:+.4f}  Weyl 差 = {sample_cos-integ_cos:+.4f}")

# Erdős-Turán 视角：Σe^{i·2nθ₁(γ_k)} 的 Weyl 和——相位 {nθ₁/π} 的均匀性
print("\n相位 {n·θ₁(γ_k)/π} 的均匀性（Weyl——Erdős-Turán）：")
for n in [100, 500, 1000]:
    th1 = np.arctan(1/(2*gz))
    phase = np.mod(n*th1/pi, 1.0)  # 模 1
    disc = np.max(np.abs(np.sort(phase) - np.arange(len(phase))/len(phase)))
    print(f"  n={n}: discrepancy D* = {disc:.4f}（0 = 完全均匀）")

del z, gz
gc.collect()
print("内存已释放")
