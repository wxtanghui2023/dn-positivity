# P36.3：Arithmetic Gram-Rigidity Test——第一轮（可行性审计）

> 2026-09-02 10:35 · 唐先生 P36.3 指令 · 矩阵/Gram rigidity · 算术 null direction

## 框架（唐先生）
- **不再找 A ≥ P 标量 domination**（那是把 RH 压缩进精确素数估计）——**寻找结构性约束**：arithmetic structure ⟹ forbidden off-line geometry cannot occur——scalar inequality → operator/order rigidity
- **Hankel 矩阵**：H_N = (M_{i+j})——v^T H_N v = Σw_ρ|P_v(δ_ρ)|² ≥ 0——RH ⟹ H_N=0——离轴 ⟹ H_N≠0——**离轴配置形成有限秩正测度问题**——算术结构是否迫使 rank/kernel/determinant/trace identity（r_arith 不从零点计算）
- **算术 null direction**：找算术定义的非零 v——Σ_ρ|P_v(δ_ρ)|² = 0——P_v 零点只含 0 ⟹ β_ρ=½——v 必须来自算术结构（Euler 系数/Hecke/自伴 resolvent/正定核）
- **catastrophic cancellation 解读**：A ≃ P 不是坏消息——标量显式公式是"差分坐标"——在差分坐标找正性不自然
- **新目标**：A(f) − P(f) = ||T_arith f||²——或——W(f) = ⟨f, K_arith f⟩——K_arith ⪰ 0——核空间独立刻画

## ① Hankel 矩阵结构（数值——确认）
- 在线（δ=0）：M_n = 0——H_N = 0——rank 0
- 离轴：rank(H_N) = **不同 δ 轨道数**（单 δ: rank 1——三 δ: rank 3——同 δ 重复: rank 1 合并）✓——**"离轴配置 = 有限秩正测度"（唐先生表述——数值确认）**

## ② rank/kernel 算术刻画——无（循环）
- M_n = Σ(β−½)^{2n}——"零点实部偶矩"——**无已知算术公式**：
  - (β−½)^{2n} = (Re(ρ−½))^{2n}——在线恒 0——离线需 δ——循环
  - Σ1/ρ^n（复幂）有公式——但——(Re z)^{2n} = ((z+z̄)/2)^{2n}——展开含 z^k z̄^m 混合——Σρ^kρ̄^m——**无独立公式**
- **⟹ M_n 无算术公式——rank(H_N) 无算术刻画——r_arith 无从计算——循环**

## ③ 算术 null direction——无来源（死——预判确认）
- Σ_ρ|P_v(δ_ρ)|² 的算术值——β 矩二次型——无公式
- 候选 v 来源（Euler 系数/Hecke/自伴 resolvent/正定核）——与 β 矩的连接均不存在
- **⟹ "Σ|P_v(δ_ρ)|² = 0"的算术来源——不存在**

## ④ "W = ⟨f, K_arith f⟩"重构——不可行（已知）
- 标准 Weil：W(f) = ΣF_f(ρ)——线性（不是二次型）
- 二次型版本：W(f·g)（P27-G 离轴缺陷 Gram——n₋=N_quartet——已审计）——或——Σ|F_f(ρ)|²（P5.9 K_T——coercivity 缺——已审计）
- **⟹ "K_arith 核空间独立刻画"需"非显式公式的 W"——不存在（已知）——显式公式自适应**

## ⭐ P36.3 第一轮判定
- **Hankel 结构清晰**（有限秩正测度——数值确认）——但——**rank/kernel 的算术刻画无来源**（M_n 无公式——循环）
- **算术 null direction 无来源**（Σ|P_v(δ)|² 无算术值）
- **"W = ⟨f, K_arith f⟩"重构需非显式公式 W——不存在**
- **预判确认：P36.3 撞同一堵墙（Gram 的算术侧 = 显式公式——自适应——rank/kernel 无法独立刻画）**
- **⚠️ 未完全死**：(Re z)^{2n} 的展开（z^k z̄^m 混合——配对轨道求和）——可能给"检测基线"（在线 0——离轴偏差——δ 检测——但——检测≠排除）

## 下一步候选
- (a) ②深化：z^k z̄^m 配对轨道求和——"检测基线"（新检测工具——但——检测≠排除）
- (b) 唐先生指示
