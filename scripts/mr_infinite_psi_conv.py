#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 任务4(a): 无限离轴 ψ 贡献收敛性诊断
# ψ_off(x) ~ Σ_j x^{δ_j}cos(γ_j log x)/γ_j (近线离轴 σ_j = ½+δ_j, δ_j→0)
# 测不同 γ_j 分布的收敛/发散
import numpy as np

def partial_sum(x, gammas, deltas, T_cut):
    """Σ_{γ_j≤T_cut} x^{δ_j}cos(γ_j log x)/γ_j"""
    s = 0.0
    for g, d in zip(gammas, deltas):
        if g > T_cut:
            break
        s += x**d * np.cos(g*np.log(x)) / g
    return s

if __name__ == "__main__":
    print("=== 无限离轴 ψ 贡献: 部分和 Σ x^{δ_j}cos(γ_j log x)/γ_j ===")
    print("测试不同 γ_j 分布 (δ_j → 0)\n")
    
    x = 1000.0
    logx = np.log(x)
    
    # 模型 1: 稀疏离轴 (γ_j ~ j² - 快速增长 - Σ1/γ收敛)
    # 模型 2: 正密度准均匀 (γ_j ~ 在线零点子集 - 每 k₀ 个取一个)
    # 模型 3: 正密度均匀 mod 2π/logx (无偏)
    # 模型 4: 共振 (γ_j ~ 2πk/logx + 常数 - cos 不抵消)
    
    # 模型 1: γ_j = j² (稀疏)
    g1 = np.array([j**2 for j in range(1, 2000)])
    d1 = 0.5/np.log(g1+1)  # δ → 0 (慢)
    # 模型 2: γ_j ~ 2πk/log(2πk) 类 (零点型 - 每 3 个取 1 - 正密度 33%)
    k = np.arange(10, 60000)
    g2_all = 2*np.pi*k/np.log(2*np.pi*k)  # 近似零点
    g2 = g2_all[::3]  # 每 3 取 1 (33% 离轴)
    d2 = 0.2/np.log(g2+1)  # δ→0
    # 模型 3: 均匀 mod 2π/logx (相位随机)
    np.random.seed(42)
    g3 = np.sort(np.random.uniform(50, 5e5, 3000))  # 随机高度 (均匀分布)
    d3 = 0.5/np.log(g3+1)
    # 模型 4: 共振 (γ_j ≈ 2π·j/logx + offset - cos 恒正)
    g4 = 2*np.pi*np.arange(100, 6000)/logx + 0.001
    d4 = 0.5/np.log(g4+1)
    
    models = [("稀疏 (γ~j²)", g1, d1), ("正密度33% (零点型)", g2, d2),
              ("均匀随机高度", g3, d3), ("共振 (γ~2πk/logx)", g4, d4)]
    
    for name, g, d in models:
        print(f"--- {name} ---")
        print(f"  零点数: {len(g)}  γ范围: [{g[0]:.1f}, {g[-1]:.0f}]")
        cuts = [g[-1]/100, g[-1]/10, g[-1]/3, g[-1]]
        vals = []
        for Tc in cuts:
            s = partial_sum(x, g, d, Tc)
            vals.append(s)
        print(f"  部分和 @T_cut: " + "  ".join(f"{v:+.4f}" for v in vals))
        # 无 cos 的 Σ1/γ (参考 - 发散?)
        s_noCos = sum(1.0/gg for gg in g if gg <= g[-1])
        print(f"  参考 Σ1/γ (无cos): {s_noCos:.2f}")
        print()
    
    print("=== 解读 ===")
    print("若部分和随 T_cut 增长 (发散) → 离轴 ψ 贡献发散 → 矛盾")
    print("若部分和振荡/有界 (收敛) → 不矛盾")
