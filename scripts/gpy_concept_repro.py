#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# GPY/Maynard 概念复现 (小规模)
# 关键比率: R(F) = k·J(F)/I(F)  (经典 BV 情形 - c1=c2=0)
# I(F) = ∫_{Δ_k} F², Δ_k = {t_i≥0, Σt_i≤1}
# J(F) = ∫_{Δ'_k} (∫_0^{1-Σt_i} F(t_1..t_{k-1},t_k)dt_k)² dt_1..dt_{k-1}
#   (Maynard 的 J 定义 - 对 k-1 变量区域 Σt_i≤1 的平方积分)
# 若 sup R(F) > 1 → H_1 有界 (存在无限 2-素数簇)
# Maynard: 需要 k 足够大 (约 105) - 小 k 应该 < 1 (验证实现)
import numpy as np

def I_integral(F, k, N=200000, seed=42):
    """∫_{Δ_k} F² dt - 蒙特卡洛 (Δ_k 体积 = 1/k!)"""
    rng = np.random.default_rng(seed)
    # 在 Δ_k 采样 (Dirichlet(1,1,...,1))
    samples = rng.dirichlet(np.ones(k+1), N)  # k+1 个分量, 和=1
    t = samples[:, :k]  # 取前 k 个 (第 k+1 个 = 1-Σt_i ≥ 0)
    vals = F(t) ** 2
    vol = 1.0 / np.math.factorial(k)
    return vol * np.mean(vals)

def J_integral(F, k, N=200000, seed=43):
    """J(F) = ∫_{Δ_{k-1}} (∫_0^{1-Σt_i} F(t,t_k)dt_k)² dt_1..dt_{k-1}
    外层 k-1 变量在 Δ_{k-1} (Σt_i ≤ 1)"""
    rng = np.random.default_rng(seed)
    if k == 1:
        return 0.0
    # 外层采样: k-1 个变量在单纯形 Σt_i ≤ 1 → Dirichlet(1,...,1,1) k 个分量
    samples = rng.dirichlet(np.ones(k), N)
    t_outer = samples[:, :k-1]  # k-1 个变量
    s = np.sum(t_outer, axis=1)  # Σt_i ≤ 1
    # 内层积分: ∫_0^{1-s} F(t_outer, t_k) dt_k (数值 - 对每个样本)
    inner = np.zeros(N)
    M_inner = 40
    for i in range(N):
        s_i = s[i]
        if s_i >= 1: 
            continue
        # 在 [0, 1-s_i] 采样 t_k (均匀)
        tk_pts = np.linspace(0, 1-s_i, M_inner)
        to = np.tile(t_outer[i], (M_inner, 1))
        t_full = np.hstack([to, tk_pts.reshape(-1, 1)])
        fvals = F(t_full)
        inner[i] = np.trapz(fvals, tk_pts)
    vol_outer = 1.0 / np.math.factorial(k-1)
    return vol_outer * np.mean(inner**2)

def make_F_const(k):
    return lambda t: np.ones(t.shape[0])

def make_F_linear(k):
    """F(t) = 1 - Σt_i (在 Δ_k 上 - 支撑自然)"""
    def F(t):
        s = np.sum(t, axis=1)
        return np.maximum(0, 1 - s)
    return F

def make_F_power(k, b):
    """F(t) = (1-Σt_i)^b"""
    def F(t):
        s = np.sum(t, axis=1)
        return np.maximum(0, 1-s)**b
    return F

if __name__ == "__main__":
    print("=== GPY/Maynard 概念复现: R(F) = k·J(F)/I(F) ===")
    print("若 sup R > 1 → H_1 有界 (Maynard 需 k~105)")
    print()
    
    for k in [2, 3, 5, 8, 10, 15, 20]:
        for name, F in [("const", make_F_const(k)), ("linear", make_F_linear(k)),
                        ("power b=2", make_F_power(k, 2)), ("power b=4", make_F_power(k, 4))]:
            I = I_integral(F, k, N=50000, seed=42)
            J = J_integral(F, k, N=50000, seed=43)
            R = k * J / I if I > 0 else 0
            flag = " *** >1!***" if R > 1 else ""
            print(f"k={k:>3} {name:>10}: I={I:.4e} J={J:.4e} R=kJ/I={R:.4f}{flag}")
        print()
