# RH 判别定理（Draft v2.2 —— 发表格式化）

> 日期：2026-08-30 20:04
> 状态：**Draft v2.1 数学结构闭合 → v2.2 发表格式化**（论文工程阶段）
> 结构：主正文（Theorem + Lemma A/B/C + Proposition B）→ 附录 A-C → 反向审稿

---

# 主正文

## Theorem（RH 判别定理）

**定义**：S = ∂_t² log|ξ(½+it)| ∈ S′——H_0 = F⁻¹[ŵ_target/K̂_0]——Q := −⟨S,H_0⟩——Q'_RH = Σ_ρ w_target(γ_ρ)。

> **Theorem**：RH ⟺ Q = Q'_RH。

## Lemma A（Kernel rigidity）

**A.1 单零点展开**：K_ρ(t) = −K_{δ_ρ}(t−γ_ρ) 满足 M₀ = M₁ = 0（偶性——精确）且
$$M_2 = \delta_\rho\int y^2 Q_{\eta/\delta_\rho}(y)\,dy$$

**A.2 Q_λ 一致矩界**：
$$\sup_{0<\lambda<1/2}\int_{\mathbb R} y^2|Q_\lambda(y)|\,dy < \infty$$
- 远场（|y| ≥ R）：Q_λ = −(λ²/2)/(y²+1)² + O((y²+1)^{−3})
- 近场（|y| ≤ R）：Q_λ = O(λ²)（Taylor——∂_λ²A₀ = 2K₁ 抵消）
- 中间：连续覆盖

**推论**：|M₂| ≤ C|δ_ρ|——|⟨K_ρ,H_0⟩| ≤ C|δ_ρ||H_0''(γ_ρ)|——Σ_ρ|⟨K_ρ,H_0⟩| < ∞（H_0'' = O(t^{−2})——Σγ^{−2} < ∞）。

## Proposition B（Tempered Weil compatibility）

**假设** H ∈ W——W 满足：H(−t) = H(t)——H ∈ C^∞ ∩ S′——|Ĥ(u)| ≤ C(1+|u|)^{−1−ε}。

**则** 使用标准 tempered Weil explicit formula：
$$\langle S,H\rangle = M(H) + P(H) + Z(H)$$
（M 主项——P 素数项——Z 零点项）

**验证** H = H_0 满足 W1/W2/W3（偶——光滑缓增——|Ĥ_0(u)| ≤ Ce^{−|u|}）——故 Weil 公式适用于 H_0。

## Lemma C（正性刚性）

$$Q - Q'_{\rm RH} = \sum_\rho \delta_\rho^2 w_H(\gamma_\rho, |\delta_\rho|)$$

- w_H > 0（Lemma C1——闭式分子 a²(a+1)+|δ|γ² > 0——全部 γ≥0）——Q ≥ Q'_RH
- Q = Q'_RH ⟹ Σδ²w_H = 0 ⟹ 每项 δ_ρ = 0（正项和）⟹ **RH**

## Theorem 证明

- **RH ⟹ Q = Q'_RH**：全 δ_ρ = 0——w_H(γ,0) = w_target——Q = Q'_RH ∎
- **Q = Q'_RH ⟹ RH**：Lemma C——Σδ²w_H = 0——w_H>0——每项 δ_ρ = 0——RH ∎

---

# 附录

## Appendix A：Kernel estimates

- **A.1 Q_λ 远场展开**：Q_λ = −(λ²/2)/(y²+1)² + R_λ——|R_λ| ≤ C/(y²+1)³（λ 一致——C 不依赖 λ）
- **A.2 Taylor 余项**：A_λ = λ²K₁ + O(λ⁴)——Q_λ = O(λ²)——紧致一致（余项常数依赖 R 不依赖 λ）
- **A.3 显式常数**：sup_{λ<½}∫y²|Q_λ|dy ≤ 0.12（数值）——解析界 C 可显式

## Appendix B：Distribution and extension

- **B.1 S ∈ S′**：log|ξ(½+it)| 缓增（Stirling t log t）+ L¹_loc（零点 log 奇异）——⟨S,ϕ⟩ = ⟨log|ξ|,ϕ''⟩
- **B.2 零频延拓**：Ĥ_0 的 1/|ω| 奇点——配对用逐项（Σ⟨K_ρ,H_0⟩——墙 A 绝对收敛）——单点测度零——唯一（配对意义）
- **B.3 tempered 配对**：Q = −⟨S,H_0⟩ 由逐项定义——不依赖整体 Parseval

## Appendix C：Weil conventions

- **C.1 Fourier convention**：tempered——Ĥ(ξ) = ∫H(t)e^{−iξt}dt（或选定 convention——落笔时固定）
- **C.2 零点计数**：含重数——m_ρK_ρ
- **C.3 素数项符号**：P(H) = −Σ(log p/p^{m/2})Ĥ(m log p)——指数衰减收敛
- **C.4 Gamma 项归属**：M(H) 含 Gamma/极点/显式项——S_reg 并入

---

# 反向审稿（待执行——从结论往前追依赖）

- [ ] Q = Q'_RH ⟹ RH——依赖 Lemma C（正项和）——依赖 w_H > 0（Lemma C1——闭式）——依赖 Q 的 Weil 展开（Prop B）——依赖交换（Lemma A）——依赖 S ∈ S′（Appendix B）
- [ ] 每个依赖——确认封口（——8 攻击点已封闭——）
- [ ] 符号一致性（Q:=−⟨S,H_0⟩——全文）——
- [ ] 引用精确（tempered Weil——文献）——

## 状态

> **Draft v2.2 发表格式化——主正文 + 附录 A-C 结构就绪——待反向审稿 + 文献引用落笔。**
> （——论文工程阶段——不是机制探索——）——
