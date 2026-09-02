# P49-G2.7.4-II-A.2：共同低能有效矩阵——E-map 材料（第一轮）

> 2026-09-02 15:48 · E-map 含算术和 · k_λ 非纯几何 · 两阶段收敛官方化

## 关键定义提取
- **E(f)(u) := u^{1/2}·Σ_{n≥1} f(nu)**（7.2——E-map）
- **h(u) = (π/2)u²(2πu²−3)e^{−πu²}**（7.1——闭式！——h₀/h₄ 组合的显式）
- **k(u) = E(h)(u)**——Ξ = k 的 Fourier（⟨ℝ*₊|ℝ⟩ 对偶）
- h_λ = PW_λ 特征组合（h₀,λ/h₄,λ——Lemma 7.2: h_λ → h 一致 λ⁻²）——k_λ = E(h_λ)

## ⭐ 论文两阶段收敛声明（第 7 节开头——官方化三角桥）
- **Stage 1（fixed λ）**：det_reg(D_{λ,N}−s) →(N→∞) **−iλ^{−iz}ξ̂_λ(z)**（uniform on compact subsets of ℂ——footnote 2）
- **Stage 2（λ→∞）**：ξ̂_λ(z)·suitable constants → **Ξ**（uniform on closed substrips ℑ(z) < ½）
- "det_reg suitably multiplied by e^{a+ibs} converge towards Ξ(s)——This convergence would entail RH using Hurwitz"
- **⟹ 论文自己的两阶段 = 我们的三角桥（det_reg → ξ̂_λ → Ξ）——但——Stage 2 依赖 ξ̂_λ ≈ c·k_λ（missing step 2——未证）——Stage 1 是论文断言（需核验是否有证明——outlook 的 strategy 表述）**

## ⭐ 候选共同结构（II-A.2 核心洞察）
- **E-map 含算术和**：E(f)(u) = u^{1/2}Σ_{n≥1}f(nu)——**k_λ 非"纯几何"——是"调和（h_λ）× 算术和（Σ_n）"**
- **桥不是"纯 prolate vs 算术 Weil"**——是"prolate-调和 × 算术求值（E）vs Weil 二次型（QW）"
- **候选共同主项**：E 的 Σ_{n≥1}f(nu)（所有整数）vs QW 的 Σ_{n≤λ²}Λ(n)T(n)（素数幂）——**两边都含"算术求值算子"（整数/素数点求值）**——可能经 Poisson/显式公式连接
- 这改变 II-A 图景：算术性部分在 E-map 里（非后加）——ξ_λ ≈ k_λ 的桥可能是"两算术求值结构在低能的一致性"

## II-A.2 状态
- E-map/h/k 精确定义到手——论文两阶段收敛声明官方化三角桥
- **候选共同结构定位**（算术求值——E 的 Σ vs QW 的 ΣΛT）——待矩阵级验证（P_V QW P_V vs P_V "prolate×E" P_V）
- ⚠️ Stage 1/2 是论文断言/strategy——需核验证明状态（Stage 1 的 N→∞ fixed λ——footnote 2 说 uniform compact——可能可证——Stage 2 依赖 missing step 2）

## 下一步候选
- (a) II-A.2 矩阵级（V_λ 低-k——P_V QW P_V vs k_λ = E(h_λ) 的低-k 结构——数值比较——算术求值主项检验）
- (b) Stage 1 证明状态核验（det_reg → −iλ^{−iz}ξ̂_λ 的 N→∞——论文是否有证明或只是断言——第 5 节 Theorem 5.10 的延伸）
- (c) 唐先生指示
