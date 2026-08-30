# Draft v2.4 Reference Map（文献引用映射）

> 日期：2026-08-30 20:16
> 目的：文献接口落笔——外部定理接口写法（引用经典 → 验证假设 → 代入——不套用类似版本）
> 状态：Draft v2.4 文献接口阶段——🟡 文献编号整理/参考文献表/最终独立复核

---

## 一、Proposition B（外部定理接口写法）

> **Proposition B（Tempered Weil Compatibility）**：
> We invoke a tempered-distribution form of Weil's explicit formula. For test functions belonging to the admissible Weil space W, the distribution associated with ∂_t²log|ξ(½+it)| admits the decomposition
> $$\langle S,H\rangle = M(H) + P(H) + Z(H).$$
> **The present work does not reprove the explicit formula; it verifies that the constructed kernel-inverse test function H_0 satisfies the required hypotheses.**

定位：Weil 公式 = 外部经典结果——H_0 ∈ W = 本文证明。

## 二、引用层级（Reference Map）

| 证明位置 | 需要引用 | 用途 |
|----------|----------|------|
| **Weil 显式公式**（⟨S,H⟩ = M+P+Z） | A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, 1952 | 零点项/素数项/Gamma 项结构（——正文引用——不重述证明——） |
| **测试空间扩展**（更宽测试函数类——H_0 ∈ C^∞∩S′——tempered 框架） | K. Barner, *On A. Weil's explicit formula*, J. Reine Angew. Math. 323 (1981), 139–152 | Weil-Barner 公式——更宽测试函数类 |
| **Tempered distribution 基础**（S ∈ S′——F: S′→S′） | Schwartz distribution theory——Hörmander, *The Analysis of Linear Partial Differential Operators I* | 分布框架（——不混入 Weil 定理——） |
| **Fourier convention**（tempered 归一化） | 标准 Fourier 分布框架（DLMF 1.16 等） | Ĥ(u) = ∫H(t)e^{−2πiut}dt |

## 三、Appendix C：Convention（固定格式）

**Fourier**（冻结）：Ĥ(u) = ∫_ℝ H(t)e^{−2πiut}dt——注明：*All Fourier transforms are taken under this normalization.*

**ξ**（冻结）：ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)

**零点计数**：ρ = ½+δ_ρ+iγ_ρ——重零点按 multiplicity 计——求和采用对称极限或绝对收敛后的普通求和。

**素数项**：P(H) 中的符号与 Fourier convention 一致（——附录写死——否则不同 Weil 文献之间容易差一个负号——）。

## 四、参考文献表（初稿——落笔时核对页码/版本）

1. A. Weil, Sur les "formules explicites" de la théorie des nombres premiers, Comm. Sém. Math. Lund (1952), 252–265.
2. K. Barner, On A. Weil's explicit formula, J. Reine Angew. Math. 323 (1981), 139–152.
3. L. Schwartz, Théorie des distributions, Hermann, Paris.
4. L. Hörmander, The Analysis of Linear Partial Differential Operators I, Springer.
5. (Fourier convention 来源——按选定的分布理论教材)

## 五、状态

> **Draft v2.4 文献接口阶段**：
> ✅ 已冻结：主恒等式 Q−Q'_RH = ΣΔ_H——正性 Δ_H = δ²c_H（c_H>0）——Weil 输入 H_0 ∈ W
> 🟡 待完成：文献编号整理——参考文献表完善——最终独立复核
>
> ⚠️ 提醒：文献化和审稿仍不能等同于"RH 已被数学界接受为已证明"——最终仍需独立专家验证每个核心引理和外部定理接口。

---

## 六、参考文献表（完善版——Draft v2.5）

**[1] Weil, A.** — Sur les "formules explicites" de la théorie des nombres premiers. *Comm. Sém. Math. Univ. Lund [Medd. Lunds Univ. Mat. Sem.]* Tome Supplémentaire (1952), 252–265.
——用于：Weil explicit formula——零点项/素数项/Gamma 项结构。

**[2] Barner, K.** — On A. Weil's explicit formula. *Journal für die reine und angewandte Mathematik* 323 (1981), 139–152.
——用于：tempered Weil framework——非 Schwartz 测试函数许可。

**[3] Schwartz, L.** — Théorie des distributions. Hermann, Paris, 1950–1951.
——用于：S′——tempered distributions——Fourier transform on distributions。

**[4] Hörmander, L.** — The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis. Springer-Verlag.
——用于：Fourier transform on S′——distributional pairing——延拓唯一性背景（可选加强）。

## 七、正文引用位置（冻结）

- **Proposition B** 第一次出现：*We use the tempered form of Weil's explicit formula [1,2].*——避免"Weil theorem proves our identity"——避免"new Weil formula"——**明确：本文只验证 H_0 ∈ W**。
- **Appendix B（Distribution）**：S = ∂_t²log|ξ(½+it)| ∈ S′——引用 [3,4]。
- **Appendix C（Convention）**：声明 Ĥ(u) = ∫_ℝH(t)e^{−2πiut}dt——*All formulas below follow this normalization.*

## 八、Final Audit（独立复核版——四轮）

**Audit A（外部定理接口）**：Weil 引用版本是否覆盖 W——H_0 条件逐条对应。

**Audit B（内部核心引理）**：Lemma A3（交换）——Lemma C（Δ_H 正性）——H_0 构造唯一性——逐项。

**Audit C（符号一致性）**：Q = −⟨S,H_0⟩——Δ_H = w_H(γ,δ) − w_H(γ,0)——**禁止回写 δ²w_H**。

**Audit D（论文措辞）**：避免"RH is proved"——改"We establish a criterion equivalent to RH under the stated lemmas/assumptions."——直到独立验证完成。

## 九、状态

> **Draft v2.4：文献接口冻结。Draft v2.5：参考文献表 + 最终独立复核阶段启动。**
> 推荐路径：Reference Map → Reference List → Final Audit → v2.5 定稿候选
> ⚠️ 措辞红线：直到独立验证完成——不写"RH is proved"
