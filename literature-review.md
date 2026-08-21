# 文献检索报告：望远镜恒等式与框架定位

> 日期：2026-08-21 | 方法：web_search (Tavily) + arXiv 检索

---

## 1. 核心问题：g_n(t) = cos(nθ(t)) − cos((n+1)θ(t)) 是否已知？

**检索关键词**：Riemann zeta cosine telescoping identity；"cos(nθ)" "cos((n+1)θ)"；t sin(nθ) + 0.5cos(nθ)；Gram points positivity

**结果**：**未找到该精确恒等式的文献记载**。相关搜索返回的都是：
- Guinand-Weil 显式公式（一般框架，不含此特定核）
- Gram 点理论（θ(g_n) = nπ 单调性）
- Riemann-Siegel Z 函数（Z(t) = e^{iθ(t)}ζ(1/2+it)）

**初步判断**：望远镜恒等式 g_n = cos(nθ)−cos((n+1)θ)（θ = π−2arctan(2t)）**可能是新的**，但需更彻底检索（arXiv 全文搜索、Google Scholar）确认。

## 2. ★ 关键文献：Murty & Rath (2018) 的惊人相似结构

**Murty, Ram & Rath, "Transcendental sums related to the zeros of zeta functions", Mathematika 64 (2018), arXiv:1807.11201**

### 2.1 结构对比

| | Murty-Rath | 本项目 |
|---|---|---|
| 求和 | Σ_{ν>0} cos(ν log x)/(1/4+ν²) | Σ_γ [t sin(nθ)+0.5cos(nθ)]/(1/4+t²) |
| 分母 | **1/4 + ν²** | **1/4 + t²**（相同！）|
| 相位 | ν log x（对数）| nθ(t)（arctan，θ≈1/t）|
| 零点 | 正虚部 ν | 正虚部 γ |

**分母 1/4+ν² 完全相同**——这暗示 g_n 的分母来自 ζ 显式公式的标准核（可能源自 ξ 函数的部分分式）。

### 2.2 Murty-Rath 的核心公式（RH 下）

Σ_{ν>0} 2cos(ν log x)/(1/4+ν²) = [x − ψ₀(x)]/√x − log 2π/√x − ½√x·log(1−1/x²) + √x(L(x)−log x) + γ/√x − √x/2·log x + 1/(x−1) + 1/√x

其中 ψ₀(x) 是 Chebyshev 函数，L(x) 相关。**通过显式公式把零点求和与素数函数联系**——与本项目 D_n 通过显式公式与 Main 联系的框架同构。

### 2.3 意义

1. "零点余弦和 + 1/(1/4+t²) 核"是**已知研究领域**（Murty-Rath 已研究）
2. 本项目的望远镜恒等式是这一领域的**新工具**（cos 差分使求和可分解）
3. 可引用 Murty-Rath 作为框架定位

## 3. Li 判据：零点和正性 ⟺ RH 的先例

**Li (1997)**：λ_n = Σ_ρ [1 − (1−1/ρ)ⁿ]，**λ_n > 0 对所有 n ⟺ RH**。

- 这是"零点求和的正性"与 RH 等价的经典先例
- 本项目的 D_n > 0 与之同类型（虽然核不同，不直接等价 RH）
- 表明"零点和正性"是有意义的、被认真研究的主题

## 4. 结论与建议

| 项 | 结论 |
|---|---|
| 望远镜恒等式新颖性 | 初步：可能新（需 arXiv 全文确认）|
| 框架定位 | Murty-Rath (2018) 的结构类似物（1/4+t² 核）|
| 正性目标 | Li 判据先例（但本项目不等价 RH）|
| 下一步 | arXiv 全文搜索确认恒等式；写 arXiv 预印本时可引用 Murty-Rath 定位 |

## 5. 参考文献

1. M. R. Murty, P. Rath, "Transcendental sums related to the zeros of zeta functions", Mathematika 64 (2018), arXiv:1807.11201
2. X.-J. Li, "The positivity of a sequence of numbers and the Riemann hypothesis", J. Number Theory 65 (1997), 325–333
3. Guinand-Weil 显式公式（标准参考）
4. Gram 点理论（Titchmarsh, DLMF §25.10）
