# THH/TP 方向审计：拓扑 Hochschild/循环同调与 zeta

> 2026-09-01 · 唐先生指示继续探索 · "别人没发现"候选的文献深挖

## Hesselholt（2016/2018）——F_q 情形（已实现 Deninger 框架）
**定理 A（arXiv:1602.01980）**：对有限域上光滑簇 X：
```
ζ(X, s) = det∞(δ(s·id − Θ) | TP_od(X)⊗C) / det∞(δ(s·id − Θ) | TP_ev(X)⊗C)
```
- **Θ = 最一般的解 q^Θ = Fr*_q**（Frobenius 的无穷小生成元——Deninger 哲学的 TP 实现）
- TP_od/TP_ev = 周期拓扑循环同调的奇/偶部分
- **zeta 零点 = Θ 的谱**——F_q 情形——Fr 的代数性质（Weil——|α|=√q）约束特征值——零点在线

**关键**：F_q 情形——Θ 由 Fr 定义（**独立于零点**）——TP 提供宿主——完整 zeta 实现——**但——F_q 的 Weil 已知（Deligne）——THH 是另一种上同调实现——不是 RH**

## Morin（Duke Math J 173(13), 2024）——Spec ℤ 情形（但只到特殊值）
**主结果**：对正则连通概形 X（维数 d——proper over Spec(Z)——**含 Spec ℤ**）：
- 定义 THH 及 TP, TC⁻ 上的滤过（Antieau + Bhatt-Morrow-Scholze）
- 分次片 = Hodge 完备的导出 de Rham 上同调（相对 ℤ）
- **特殊值公式：±ζ*(X_R, n)（n ∈ ℤ 整数点）**——用 Bloch conductor + RΓ(X_R,W,Z(n)) + LΩ 的行列式
- "This formula is a shadow of the functional equation"——**n ↔ d−n 对称（特殊值形式的函数方程）**

**关键区分**：
- **Morin 处理"zeta 特殊值"（ζ(n)——整数点）——不是"零点位置"（ζ(s)=0——s=½+it 非整数点）**
- "函数方程阴影" = 特殊值公式的 n↔d−n 对称——**不约束零点位置**（函数方程本身只给配对——不给 β=½——已审计）

## Spec ℤ 的"零点 = Θ 谱"——仍未实现
- Spec ℤ 是特征零——**无 Frobenius Fr*_q——Θ 不能由 q^Θ=Fr 定义**
- Morin 的框架处理特殊值——**不提供"零点 = 谱"的机制**
- **Spec ℤ 的 Θ（或等价物）——仍未构造——与 Deninger 的 elusive 是同一障碍**

## 诚实结论
**THH/TP 方向——实质进展——但核心缺失未解决**：
| 层面 | 状态 |
|------|------|
| F_q（Hesselholt） | 完整 zeta = det∞(s−Θ)——但 F_q 的 Weil 已知——不是 RH |
| Spec ℤ（Morin） | 特殊值公式（整数点）——不到零点位置 |
| Spec ℤ 零点 = Θ 谱 | 仍需 Θ（无 Fr——未构造）——THH 换宿主不换约束 |

**这是"算术-解析断裂"的同伦论表述**：
> THH/TP 提供"上同调宿主"（Deninger 想要的空间——F_q 已实现）——但——"谱实/模约束"需要 Fr（特征零无）或 Θ（未构造）——**断裂依然存在——THH 不跨越它**。

**战略意义**：
- THH/TP 值得记录为"动机上同调的现代候选宿主"（比 Deninger 的叶状空间更接近实现）
- 但——RH 的核心缺失（Spec ℤ 的谱实约束来源）——THH 未解决
- 特征零的"几何刚性来源"——仍是开放问题（F_q 的 Fr 模约束不适用）
