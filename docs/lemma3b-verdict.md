# Lemma 3 弱版 B 判定：无条件可行性分析（最终）

> 2026-09-01 · 唐先生指令 · 输出两种之一：B 成立 或 B 不能由现有无条件工具推出

## B 的陈述
**β > ½ ⟹ V(T) ≠ O(T^{−1+ε})**（弱下界——只需证明临界指数不能成立——不需要精确主导指数）

## 关键区分（部分相消 vs 完全相消）
- **B 的反例需要"完全相消"**：V(T) ≪ T^{2β−2}——降到 T^{−1+ε}——所有 T
- **部分相消（V ~ 0.2·T^{2β−2}）不够**：β=0.6——2β−2 = −0.8——0.2·T^{−0.8} 仍 ≫ T^{−1+ε}——不推翻 B

## 最小反例测试结果（抽象指数和 F(u) = Σa_j e^{(β+iγ_j)u}）
| 配置 | V_full/对角 | 结论 |
|------|------|------|
| 规则排列（最小间距） | 0.21-13.1（随 T 振荡） | 部分相消可构造——相位分布自由 |
| 随机排列 | ~0.3-1（对角主导） | 相位随机→平均正交 |
| 准简并（成对极近） | 5-10（增强） | 交叉项增强（非相消） |

**数值关键**：规则排列可构造**部分相消**（比值低至 0.06-0.2）——但**未观察到完全相消**（a_j = 1/ρ_j 固定——频率排列只给部分相消）

## dyadic 形式（唐先生——证明 B 需要什么）
```
分块：2^kT < |γ_j| ≤ 2^{k+1}T——D_k（对角）vs X_k（交叉）
需要：|X_k| ≤ (1−η)D_k（η>0 与 T 无关——coercivity）
若只能 |X_k| = O(D_k)——不够（允许 X_k = −D_k——完全相消）
"≤ (1−η)D_k"排除完全相消（保留 η 份额）——coercivity 的精确形态
```
**|X_k| ≤ (1−η)D_k 需要 phase-correlation control——Ingham（计数）+ 间距 + 重数不提供**

## ⭐ 最终判定：B 悬置（neither proven nor disproven）——obstruction 定位
**① B 不能由 Ingham+spacing+multiplicity 无条件推出**：
- 这些工具控制"计数/间距"——不控制"相位相关性"——**density control ⇏ phase-correlation control**
- 抽象配置（规则排列）可构造部分相消（比值 0.06）——破坏"对角主导"的干净论证

**② 但——B 的反例（完全相消）未构造成功**：
- a_j = 1/ρ_j 固定（相位 ~ −π/2——无符号自由度）——频率排列只给部分相消
- "平均 = 0"（完全相消）需要极强的频率/系数共振设计——在 a_j 固定 + 间距约束下不可行（数值未观察到）

**③ 所以——B 的状态**：
- 证明需要 **coercivity**（|X_k| ≤ (1−η)D_k——phase decorrelation）——现有无条件工具不提供——未发现独立来源
- 反例也未构造（完全相消不可行）
- **B 悬置——obstruction 精确定位："缺少把离轴零点贡献转化为 coercive L² 下界的独立刚性"——与 Rigidity Gap 完全闭合**

## 临界尾部路线（C2 ⟹ RH）的最终状态
- **RH ⟹ C2**：严格（pointwise 直接积分——无 Lemma 3）
- **C2 ⟹ RH**：受阻（需要 B——需要 coercivity——缺失）
- **C2 ⟺ RH：未完成——obstruction 在 coercivity（lower-bound/cancellation step）**

## 论文影响
1. **C2 ⟺ RH 不能宣称"双向严格"**——只能宣称：
   - RH ⟹ C2（严格）
   - C2 ⟹ RH（**条件于 coercivity 假设**——或——标注"未完成——obstruction 在 L² 下界的相位相关性控制"）
2. **Lemma 3 的状态**：NOT ESTABLISHED——**"Lemma 3 audit: lower-bound mechanism and cross-term control"**——不能升级为 theorem
3. **这是 Rigidity Gap 的一个具体实例**：临界尾部方法需要"把离轴零点贡献转化为 coercive L² 下界"的独立刚性——**缺失**——与整篇论文的主轴（检测 ≠ 排除）完全闭合

## 判定输出（唐先生要求的两种之一）
**Lemma 3（弱版 B）——不能由现有无条件工具（Ingham + 间距 + 重数）推出**——因为——这些工具提供 density control 但不提供 phase-correlation control——**coercivity（|X_k| ≤ (1−η)D_k）是缺失的独立刚性——这正是 Rigidity Gap**。
