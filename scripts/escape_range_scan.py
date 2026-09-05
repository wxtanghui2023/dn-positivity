#!/usr/bin/env python3
# 逃逸范围缩小分析: Maier-Rassias 签名 N^{2δ} 的检测阈值
# 逃逸零点 (σ₀=½+δ, γ₀) 的 d_N² 签名 ~ N^{2δ}·A(γ₀)/log²N, A ~ 1/γ₀²
# 检测需要 N^{2δ}/γ₀² ≳ 在线基线 C/log N → N* ~ (γ₀²·C/log N*)^{1/(2δ)}
# 扫描 δ, γ₀ - 确定可检测 vs 不可检测区域
import numpy as np

C_burnol = 2 + 0.5772156649015329 - np.log(4*np.pi)  # ≈ 0.0462 (Burnol 常数)

def detect_threshold(delta, gamma0, C=C_burnol):
    """检测阈值 N*(δ,γ₀): N^{2δ}/γ₀² ~ C/log N 的解
    近似: N* ~ (γ₀²·C)^{1/(2δ)} (忽略 log N 修正 - 粗略)
    更精确: 解 N^{2δ}·log N = C·γ₀²"""
    # 迭代解 N^{2δ} log N = C γ₀²
    target = C * gamma0**2
    # log 形式: 2δ·L - log L = log(C·γ₀²), L = log N
    from scipy.optimize import brentq
    log_target = np.log(target)
    # f(L) = 2δ·L - log L - log_target
    # L 范围: 需要 2δL > log_target → L > log_target/(2δ)
    L_min = max(1.0, log_target/(2*delta) * 0.5)
    L_max = max(L_min*2, log_target/(2*delta) * 1.5, 100.0)
    try:
        # 找 f 的根 (f 在 L 大时 → +∞ 因为 2δL 主导)
        L = brentq(lambda L: 2*delta*L - np.log(L) - log_target, L_min, L_max)
        return np.exp(L)
    except Exception:
        return float('inf')

if __name__ == "__main__":
    print("=== 逃逸范围缩小分析: 检测阈值 N*(δ, γ₀) ===")
    print(f"Burnol 常数 C = {C_burnol:.4f}")
    print("检测条件: N^{2δ}/γ₀² ≳ C/log N (Maier-Rassias 签名 vs 在线基线)")
    print()
    
    deltas = [0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
    gamma0s = [10**3, 10**6, 10**9, 3*10**12]
    
    print(f"{'δ':>7} | " + " | ".join(f"γ₀={g:.0e}" for g in gamma0s))
    print("-" * 80)
    for d in deltas:
        row = []
        for g in gamma0s:
            Nstar = detect_threshold(d, g)
            if Nstar == float('inf'):
                row.append("∞")
            else:
                # 用 log10 显示
                row.append(f"1e{np.log10(Nstar):.1f}")
        print(f"{d:>7.3f} | " + " | ".join(f"{r:>10}" for r in row))
    
    print("\n=== 解读 ===")
    print("N* = 检测该逃逸所需的 Dirichlet 多项式长度 N")
    print("若 N* > 实际可用 (1e6-1e9) → 该 (δ,γ₀) 逃逸实际不可检测")
    print()
    
    print("=== 实际可检测边界 (N_max = 1e6, 1e9, 1e12) ===")
    for Nmax in [10**6, 10**9, 10**12]:
        logN = np.log(Nmax)
        print(f"\nN_max = {Nmax:.0e} (log N = {logN:.1f}):")
        for g in gamma0s:
            # 可检测的 δ: N^{2δ}·log N ≥ C·γ₀² → 2δ ≥ (log(C γ₀²) - log log N)/log N
            log_target = np.log(C_burnol * g**2)
            delta_min = max(0.0, (log_target - np.log(logN)) / (2*logN))
            if delta_min >= 0.5:
                print(f"  γ₀={g:.0e}: 全部不可检测 (需 δ ≥ {delta_min:.3f} > ½)")
            elif delta_min <= 0:
                print(f"  γ₀={g:.0e}: 全部可检测 (δ > 0)")
            else:
                print(f"  γ₀={g:.0e}: 可检测 δ ≥ {delta_min:.4f} — 更小 δ 不可检测")
