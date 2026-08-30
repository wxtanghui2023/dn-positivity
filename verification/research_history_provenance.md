# Research History & Provenance（内部研究史——不随投稿）

> 目的：保存"失败如何迫使结构改变"的完整记录——证明最终结构
> 不是"挑了一个正的表达式"——而是被独立重建反复摧毁后，
> 由函数方程轨道结构重新涌现的。
> 状态：内部文档——不随 manuscript 提交。

---

## 三个层次

### 1. 数学内容层
C1–C5 / O1–O5 均有正式推导（从原始定义——非数值实验）。
交付物：`independent_core_note.md`。

### 2. 失败 provenance 层（本文件）
以下失败**不是被外部发现的**——而是零背景重建（从 Hadamard 第一性
原理独立推导）主动摧毁的：

| # | 失败 | 发现方式 | 迫使的结构改变 |
|---|------|----------|----------------|
| 1 | 冻结 K_δ = 2(x²−δ²)/(x²+δ²)² 是自然核的 −2 倍（归一化+符号错） | Test 1 从 Hadamard 重推 S | 采用 K^nat := L''（S 的单项） |
| 2 | 冻结 H_0 第二项符号错（−1/(2π(1+t²)) vs 正确 +） | Chain III 独立算 Ĥ_0 = ŵ/K̂ | 采用 H_0^correct（ŵ/K̂ 构造） |
| 3 | |δ| 偷换实际 δ（w_H 用 |δ|——无独立推导支持） | D1 独立配对 | 采用实际 δ（a = 1+δ）——非 |δ| |
| 4 | 逐点正性 Δ_H(γ,δ) > 0 失效（δ<0 时负——成对和也负） | v2.15.2 D3 | 放弃逐点正性——寻找成对结构 |
| 5 | 整体分布配对 ⟨log|ξ|,H_0''⟩ 发散（O(t log t)·1/t² = log t/t 不可积） | C3 严格化 | Q 逐项定义（Parseval 乘积 L¹——绝对可和） |

**关键点**：最终结构（成对正性 P_γ = δ²M₂/(2U²D₊D₋)——正系数
多项式）**不是人为设计以产生正性**——而是在独立重建摧毁逐点正性
之后，由函数方程轨道结构（ρ ~ 1−ρ̄——同 γ 反 δ）重新涌现的。
这是可追溯的数学来源。

### 3. 学术边界层（永久）
> **Formally reconstructed criterion equivalent to the Riemann
> Hypothesis under the stated distributional framework, pending
> independent external verification.**

严格不等于："RH 已证明"。三永久边界：
1. "equivalent to RH" = 当前目标与内部重建结论；
2. "under the stated distributional framework" = 适用范围限定；
3. "pending independent external verification" = 内部完成 ≠ 学界确认。

---

## O5 永久警惕点（最值得外部攻击）

"C1–C5 全部成立"不自动产生数学界意义上的 RH 等价判据。
真正的核心是 O5：

- Q 与 Q'_RH 是否**从原始对象合法定义**（Q'_RH 定义阶段无 RH——
  投影谱 Π({ρ}) 通过同一 w_H 泛函——非从 ΣP 反向定义）；
- Q = Q'_RH ⟺ RH 的方向是否**没有把 RH 信息偷偷编码进定义**。

这是陌生专家从零攻击的首选位置。

## 建议的外部验证实验（INVALID-first）

给一个没看过历史的分析数论专家：只提供 theorem-level exposition +
assumptions + C1–C5——**要求他尝试证明 INVALID（而非 VALID）**。
- 攻击失败 → 证据等级明显提升；
- 攻击成功 → 精确定位最后一个缺口。
