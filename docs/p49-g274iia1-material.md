# P49-G2.7.4-II-A.1：Prolate-Weil 材料提取——第一轮

> 2026-09-02 15:44 · 论文精确定义 · 桥方向确认 · ε_λ↔1−χ 性质

## 材料提取（论文第 7-8 节）
- **PW_λ := −∂_x((λ²−x²)∂_x) + (2πλx)²**（prolate wave operator——变形谐振子——7.5）
- h_{n,λ} = PW_λ 特征函数（n 偶 even——n≡0 mod 4 Fourier 不变）
- **h_λ = h₀,λ 与 h₄,λ 唯一 vanish-integral 线性组合**（对应 h = (√3/2^{11/4})h₄ − (3/2^{17/4})h₀——Lemma 7.1）
- **k_λ(u) = E(h_λ)(u)**（∀u ∈ [λ⁻¹,λ]——7.6——educated guess for ξ_λ 的标量倍）
- **Lemma 7.1**：Ξ = k 的 Fourier——k = E(h)——**Ξ 本身 = prolate/调和结构的 Fourier（精确——非逼近）**
- **Lemma 7.2**：‖h_{n,λ} − h_n‖ ≤ cλ⁻²（n = 0,4）——**h_λ → h 一致（λ⁻²）**
- **χ(λ)**：prolate 压缩 Fourier 特征值（1−χ 极快衰减——e^{−4πλ²} 类）
- **Figure 4**：log(ε_λ) 与 log(1−χ(λ)) 作为 μ = λ² 的对数图（indication 2）

## ⭐ 关键确认
1. **论文自列主障碍**："Justifying rigorously this step [k_λ ≈ scalar multiple of ξ_λ] is the main remaining obstacle to our approach to RH"——**桥 = 论文自己的核心未解**
2. **k_λ → Ξ 是纯 prolate 侧定理**（Lemma 7.3——h_λ → h（Lemma 7.2）+ E-map 连续性 + Mellin 估计——**完全绕开 Weil 侧 ξ_λ**）
3. **桥方向 = prolate → Weil**（k_λ 猜 ξ_λ——非 Weil → prolate）——**II-A 的问题 = 为什么 QW_λ（算术）ground 逼近纯 prolate 构造**
4. **ε_λ ↔ 1−χ(λ)**：indication 2——"extremely small numbers ε_λ ... also appear when evaluating the discrepancy for h_λ to belong simultaneously to P_λ and P̂_λ"——**Figure 4 对数同图——两"近零"同尺度——但——indication/heuristic——非定理**——唐先生的 A1-A3 门槛未达（无共同缺陷量 D_λ 的严格定义）
5. **机制线索**：ε_λ ~ h_λ 的时空限制缺陷（P_λ 与 P̂_λ 的同时隶属 discrepancy）——**prolate 的时空限制矛盾与 QW 的极小特征值可能同源**——但需严格化

## II-A 状态
- **II-A：OPEN — Structural Theorem Candidate**（论文自列主障碍——桥方向 prolate→Weil——非整体算子逼近）
- ε_λ ↔ 1−χ(λ)：**heuristic/indication（未达 A1-A3 门槛）**——不可入证明链
- Bridge-III（QW−P → 0）失效——II-A 最自然形式 = 共同低能/近核流形渐近有效理论（待 V_λ 找）

## 下一步候选
- (a) II-A.2（QW_λ 在低-k 子空间的矩阵结构 vs prolate kernel——找共同主项——共同有效矩阵 P_V QW P_V vs P_V P P_V）
- (b) II-A.4（ε_λ 与 1−χ(λ) 的 trace/defect 同源性——Figure 4 的严格化——共同缺陷量 D_λ 的候选）
- (c) 唐先生指示
