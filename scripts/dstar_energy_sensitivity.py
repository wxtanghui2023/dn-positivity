#!/usr/bin/env python3
"""
C 类数值审计：J(t) 能量的 RH 敏感性
J(t) = ΣΛ(n)δ(t−logn) − e^t（素数——）= −Σ_ρ e^{ρt} + arch（零点——）

测试：对实际零点（在线——）vs 模拟离轴——E[J] 是否变化？
候选 E：对测试函数 h——E_h = |∫J(t)h(t)dt|² 类——或——谱能量 Σ|e^{ρt} 投影|²

关键：RH 敏感性（C2——）——如果 E 对离轴敏感——值得追——如果只是重写——死
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 20

def main():
    print("="*60)
    print("C 类审计：J(t) 能量的 RH 敏感性")
    print("="*60)
    
    # 用前 N 个零点——J 的零点表示（截断——）
    # J(t) ≈ −Σ_{|γ|<T} e^{ρt}——在 t 小时（e^{ρt} 衰减控制——）
    # 能量候选：E(t) = |Σ_ρ e^{ρt}|²（瞬时能量——）
    # 在线：ρ = ½+iγ——|Σe^{ρt}|² 的 t-行为
    # 离轴：一个 ρ → ½+δ+iγ——e^{ρt} = e^{(½+δ)t}e^{iγt}——振幅变 e^{δt}
    
    # 数值：取前 50 零点——算 S(t) = Σe^{ρt} 对 t——在线 vs 离轴(δ=0.05)
    from mpmath import zetazero
    N = 50
    gammas = np.array([float(zetazero(k).imag) for k in range(1, N+1)])
    print(f"前 {N} 零点（γ 到 {gammas[-1]:.1f}）")
    
    # 在线配置的 S(t) = Σ e^{(½+iγ)t} = e^{t/2}Σe^{iγt}
    t_vals = np.linspace(0.5, 5.0, 50)
    print("\nS(t) = Σe^{ρt} 的能量 |S(t)|² 的 t-行为：")
    print(f"{'t':>6} {'|S_online|²':>14} {'|S_offline|²':>14} {'比值':>8}")
    # 离线：γ₁ 移到 β=0.55（δ=0.05——）
    for t in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        # S_online = e^{t/2} Σ e^{iγt}
        S_on = np.exp(t/2) * np.sum(np.exp(1j*gammas*t))
        # S_offline：γ₁ 的 ρ → 0.55+iγ₁（β=0.55——）其他在线
        S_off = np.exp(0.55*t)*np.exp(1j*gammas[0]*t) + np.exp(t/2)*np.sum(np.exp(1j*gammas[1:]*t))
        e_on = abs(S_on)**2
        e_off = abs(S_off)**2
        ratio = e_off/e_on if e_on > 1e-10 else float('inf')
        print(f"{t:>6.1f} {e_on:>14.6e} {e_off:>14.6e} {ratio:>8.3f}")
    
    print("""
分析：
- |S(t)|² 含 e^{2βt} 因子（对角——）——离轴（β 增——）→ 能量指数增
- 但——这是"显式公式的直接读出"（已知零点——）——非独立测量
- C2（RH 敏感性）数值上 ✓（能量对离轴敏感——）
- 但 C1（非平凡——非重写——）？？——S(t) 就是显式公式本身——
""")

if __name__ == "__main__":
    main()
