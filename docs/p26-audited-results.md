# P26 审计后正式整理：严格定理链 + 条件性结构 + 研究审计

> 2026-09-01 · 唐先生逐段审计（A6b–A21）后 · 三层归档
> 核心判断：A6b 是核心成果；A7/A9/A10/A11 是可成立局部命题；A12–A21 是结构性解释（非 no-go 定理）

---

## 第一层：已证定理（严格 lemma/theorem chain）

### T1（A6b）Distributional Reflection Rigidity —— 核心定理 ✓
**定理**：设 M_b(s) = Σ_p b_p/(p^s−1)（Re s > 1），|b_p| ≤ C(1+log p)^A。定义临界线边界分布
T_b := w*-lim_{σ↓1/2} M_b(σ+it) ∈ S'(R)（存在——绝对收敛——Schwartz 测试）。
若 T_b(t) = T_b(−t)（S' 恒等式），则 b_p = 0 ∀p。

**证明**：
- 频率集 Λ = {k log p: p 素数, k ≥ 1}——Λ∩[0,R] 有限（局部有限离散频谱）
- |b_p|p^{−k/2} ≪ (1+log p)^A p^{−k/2}——对 Schwartz φ，Σ|b_p|p^{−k/2}|φ̂(k log p)| 绝对收敛
- T_b = Σ b_p p^{−k/2} δ_{−k log p}（S'(R) 中的 tempered distribution——Fourier 支持 ⊂ (−∞, 0)）
- T_b = T_b^∨ ⟹ Fourier 支持同时含正、负频率——但原支持在 (−∞,0)——矛盾
- 选只在 −k₀ log p₀ 附近非零的测试函数——b_{p₀}p₀^{−k₀/2} = 0——b_p = 0 ∎

**不需要**：L²、Parseval、任何 ζ 零点信息。**RH-independent**。

### T2（A7）零点—极点耦合：Res_ρ M_b = −δ_ρ ✓（一阶扰动理论事实）
**定理**：M_b = Ḟ/ζ（合法变形的一阶）。若 ρ 是简单零点，则
Res_{s=ρ} M_b(s) = Ḟ(ρ)/ζ'(ρ) = **−δ_ρ**（零点一阶位移）。
**证明**：0 = F_t(ρ(t)) = tḞ(ρ) + tδ_ρ ζ'(ρ) + O(t²) ⟹ δ_ρ = −Ḟ(ρ)/ζ'(ρ)。∎
**边界**：b ⟶ M_b ⟶ {Res_ρ M_b} ⟷ {δ_ρ} 是由变形诱导的映射——injective/surjective/一一对应**均未证明**（"给定任意 δ_ρ 能否得 Euler 型 b_p"非自动）。

### T3（A9）positive-frequency isolation 被离轴谱数据破坏 ✓（no-go lemma）
**结论**：若存在离轴零点，边界项含光滑项 c_ρ/(½−β+i(t−γ))——Fourier 带 e^{−(½−β)|ξ|} 权重——单频率测试测到"Euler coefficient + off-line zero contribution = 0"——不能单独得到 b_p = 0。
**精确定性**：**positive-frequency isolation is destroyed by off-line spectral data**。
**措辞修正**：不写"因此需要 RH"——写"该证明路线若要排除离轴项，需要一个等价于或至少蕴含 RH 的额外输入"（证明需要 RH ≠ 命题需要 RH）。

### T4（A10，修正 A8）在线零点的一阶横向刚性 ✓（带条件）
**定理**：对**临界线上**的简单零点 ρ = ½+iγ，实系数 + FE 的合法变形：
- FE 和实系数共轭作用在同一 orbit pair（1−ρ = ρ̄）——c_ρ̄ = conj(c_ρ) 且 c_ρ̄ = −c_ρ——合并得 c_ρ = −conj(c_ρ)——**c_ρ ∈ iR——δ_ρ = −c_ρ ∈ iR——Re δ_ρ = 0**
- **"在线零点的一阶实部位移为零"（不是"β 无条件不变"）**
**条件**：零点保持简单；可局部解析追踪；该零点分支保持相应对称性。（"所有阶"非无条件全局命题。）

### T5（A11）orbit-wise first-order balance ✓
**结论**：离轴 orbit {ρ, ρ̄, 1−ρ, 1−ρ̄} 的一阶位移模式 (δ, δ̄, −δ, −δ̄)——**Σ_orbit Re δ = 0**。
**措辞**：称"orbit-wise first-order balance"——不称"β 守恒律"（不意味着存在真正的动力学守恒量）。

### 核心成熟结论（唐先生总判断）
> **在 Euler 型变形中，反射刚性可以在 S' 层面成立（T1）；但一旦合法变形移动 ζ 零点，临界线极点产生的 Sokhotski–Plemelj 跳跃成为 analytic-to-distributional transfer 的不可忽略障碍（T3）；该跳跃的 residue 恰好等于负的零点一阶位移（T2）。因此，试图由 Euler-side reflection rigidity 直接推出 b=0，最终会重新暴露零点位置本身的信息。**

### 逻辑降维（保留）
- **Euler reflection → S'-rigidity**：可以严格完成（T1）
- **analytic deformation → S'-reflection**：被 δ-jump 阻断（δ = −δ_ρ——零点运动本身）
- **最后真正剩下的问题**：如何从 FE + Euler structure + zero dynamics 获得额外的 β-约束？

---

## 第二层：条件性结构

### C1（A6b Transfer）Sokhotski–Plemelj 障碍 ✓/△
- 1/(x±i0) = PV 1/x ∓ iπδ(x)——boundary value 的"平均部分"和"跳跃部分"在反射下行为不同
- **精确表述**：朴素的 analytic reflection ⇒ symmetric boundary distribution transfer 被 δ 跳跃项阻断（**不是**"transfer 不可能"——带跳跃校正的 distributional reflection law 是可能方向——A7 正在探索）

### C2（A8/A10 扩展）"所有阶"的限定
- 需要：零点保持简单 + 局部解析追踪 + 对称性保持——否则"所有阶"不是无条件全局命题

---

## 第三层：启发式元结论 / 研究审计（降级措辞）

### H1（A12）Euler flow 与 heat flow 的结构差异（描述性）
- 算术流（Euler 变形）：在线稳定——离轴自由——已研究方向未见恢复力
- 热流（de Bruijn–Newman）：δ→0（吸引）——但 Λ=0 ⟺ RH（循环）
- **降级**："目前未发现"（不是"不存在"）

### H2（A13/A14）恢复力与混合流（△/✗——最需降级）
- **"Euler 流没有恢复力"** → 改为：**目前没有发现** Euler deformation 中显式依赖 β−½ 的局部恢复项（no mechanism found ≠ no mechanism exists）
- **技术修正（A14 关键错误）**：Euler deformation 的生成数据在 prime/Euler-factor 层局部（b_p ⟷ p），但零点响应通过全局函数 M_b(ρ) = Σ b_p/(p^ρ−1)（**明确依赖 ρ**）产生——**不是"零点完全无耦合"**——正确说法：**缺少目前已识别的、显式依赖 β−½ 的局部恢复项**（与"没有恢复力"是两回事）
- **"混合流不存在"不能作为定理**：最多"目前没有找到保持 Euler 与 de Bruijn–Newman 双方核心结构的自然流"——∂_t F = A[F] + λH[F] 可人为定义——需逐项检查（FE/Euler/meromorphic/arithmetic/zero flow）
- "可逆 + 耗散矛盾"是动力系统一般提醒——不能推出所有可能的 RH-flow 都不可能

### H3（A15–A18）物理模型（启发式）
- log-gas 适合 γ_j−γ_k 方向长程相互作用；但把 β_j 引入二维 Coulomb gas 后，**必须先证明 ζ 的零点是该能量泛函的平衡点**（V(β)=V(1−β)+凸性只说明模型的平衡在 ½——不说明 ζ 的零点就是这个平衡配置）
- "变分原理缺失"——判断准确
- **"算术结构天然不含 β 约束"** → 改为：**现有 Euler-product 结构本身没有提供一个已知的、直接控制零点实部 β 的正定泛函**（"没有已知机制"比"天然不存在"严格）

### H4（A19–A21）对称性与重数强制（概念修正）
- **对称性（共轭+FE）不强制零点退化**（在线和离轴都满足——Wigner 只给轨道）✓
- **"F_q 的重数强制是因为有限维特征多项式"不完整**：Weil 的核心是 αᾱ=q^w 绝对值约束 + Frobenius + Poincaré duality + Galois structure 共同作用——有限维 Frobenius representation 提供了线性代数宿主（Galois、duality、Frobenius eigenvalues 同时编码——模约束转化为谱约束）
- **Spec Z 的困难**：尚没有一个公认的、满足相应性质的 cohomological/Frobenius spectral object——**不是"无限维所以没有重数机制"**（无限维 Hilbert 空间可以有严格的谱和重数理论——self-adjoint 离散谱/Fredholm determinant/trace formula 都存在）
- **真正缺的是：合适的谱对象 + 对称性 + arithmetic realization**
- **"Θ 是唯一编码合并的对象"** → 降级为：**最直接候选之一**——可能存在非自伴算子/transfer operator/dynamical zeta/derived cohomological object/determinant line/categorical trace 等以完全不同的方式编码零点

---

## 完整逻辑地图（唐先生表）

| 层级 | 结论 | 状态 |
|---|---|---|
| A3 | ℓ¹ 反射刚性 | ✓ |
| A5 | ℓ²(p^{−1}) + B² 反射刚性 | ✓ |
| A6b | tempered coefficients + S' reflection ⟹ b=0 | ✓ 核心定理 |
| A6b Transfer | 无极点可传；极点产生 δ obstruction | ✓/△ |
| A7 | residue = −δ_ρ | ✓ 一阶扰动事实 |
| A8/A10 | 临界线零点一阶 Re δ_ρ = 0 | ✓（需简单零点/局部追踪） |
| A9 | 离轴零点产生光滑 correction | ✓ |
| A11 | 四元 orbit 的一阶零和 | ✓ |
| A12 | Euler flow 与 heat flow 的结构差异 | ✓（描述性） |
| A13 | "算术没有恢复力" | △ 只能说目前未发现 |
| A14 | "混合流不存在" | ✗ 尚未证明 |
| A15–18 | 物理模型提供候选结构但缺 variational identification | △/启发式 |
| A19 | 对称性本身不强制零点退化 | ✓ |
| A20 | 缺乏类似 Frobenius 的谱宿主 | ✓（作为现状判断） |
| A21 | "没有自然的合并编码候选" | △；"唯一"不成立 |

---

## 最终定位
- **P26-A6b–A11**：严格可审计成果（定理链 + counter-obstruction）
- **P26-A12–A21**：结构性解释与候选模型审计（非已证明的 no-go theorem）
- **不写**"P26 已完整证明为什么 RH 难：Euler 结构天然没有 β 恢复力"
- **写**：Euler reflection → S'-rigidity 可严格完成；analytic deformation → S'-reflection 被 δ-jump（= −δ_ρ——零点运动本身）阻断；A9 说明单纯 boundary reflection 不够，A19–21 说明单纯 symmetry/degeneracy 也不够——**失败被定位到具体接口："零点位置的信息如何被一个独立于 RH 的正定/谱/变分结构约束"**
