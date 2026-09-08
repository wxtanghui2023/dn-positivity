# M(T)=O(1) 攻坚总结（2026-09-08 全天——γ 层振荡项）

## 目标
证明 M(T) = S₁(T) = ∫_0^T S(t)dt = O(1)（γ 层振荡项——）
- 数值：O(1) 到 2M 零点（max 1.33——8/22——）——200k 验证（max 1.26——）
- 文献：S₁ = O(log T)（Titchmarsh 9.9A——）——S₁ = o(log) ⟹ Lindelöf（13.8——）

## 成果（结构挖掘——）
1. **M_main 展开发散确认**（8/22 路径死——）：
   - Σ_p 1/(p^{1/2}log²p) 发散（~√x/log³x——）
   - M_main 裸级数（先 p 后 k——）发散——非 M(T) 的合法展开

2. **S̄（区间平均 S——）的几乎周期结构**（R² = 0.90-0.93——）：
   - S̄_k ≈ Σ_p a_p sin(γ̄_k log p)——纯 sin——cos 系数 ~0
   - S(mid) 拟合 R²=0.93——残差 27%

3. **S̄ 精确分解**（机器精度——）：
   - S̄_k = S(mid_k) − N0''(γ̄_k)Δγ_k²/24（Euler-Maclaurin——）
   - M(T) = ΣS(mid_k)Δγ_k − Σε_kΔγ_k——ε 项无条件小

4. **求和次序微妙性**：
   - M(T)（先 k——）收敛 O(1) vs M_main（先 p——）发散
   - 非绝对收敛——次序不等价

5. **M 分块累积恒定**（~0.31——不随块长——）——强相消（随机游走预期 60x——）

## 难度定位（诚实——）
- M(T)=O(1) ⟹ Lindelöf（S₁=o(log)⟹Lindelöf——Titchmarsh 13.8——）
- Lindelöf：μ(½) 从 1/4 → 0.155（130 年——Bourgain/Guth-Maynard——）
- M(T)=O(1) 直接给 μ(½)=0——远超任何已知中间结果
- 核心：多频率联合相消（不同素数频率之间——）——不是每频率独立
- 每频率独立界 → 发散（回到 M_main——）——联合相消是 Lindelöf 的心脏

## 结论
- 数值/结构挖掘已到收益递减点
- 剩余 = Lindelöf 级硬核——需要新分析思想（非更多数值——）
- 可沉淀：S̄ 几乎周期分解 + M(T)=O(1) 证据（研究记录——）

## 文件
- scripts/F_T_bounded.py、M_T_bridge.py、M_trajectory.py、e_k_structure.py、Sbar_frequency.py、Sbar_exact.py、decomposition_check.py、inner_riemann_sum.py、M_main_convergence_test.py
- docs/M(T)-attack-state.md、M(T)-lindelof-connection.md、M(T)-hierarchy.md、M(T)-core-object.md、M(T)-phase-results.md
