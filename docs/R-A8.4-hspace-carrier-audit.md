# R8.4 审计记录：h-space Independent Carrier Audit（小灵执行）

**日期**：2026-09-10 13:51+ ｜ 预算：纸面，无代码 ｜ 提案：唐先生（选 ②）
**核心问题（唯一）**：
$$\boxed{\text{是否存在一种已知的、不经 }F(\alpha)\text{、不经 HL、不经 AP/族平均，}\\
\text{却能直接给出 }\sum_{h\le H}w_H(h)\sum_n\Lambda(n)\Lambda(n+h)\sim HX\log(X/H)\text{ 的 char-0 机制？}}$$

---

## 0. 伪绕开清单（严格不接受）
```
固定 h（⟹ HL）｜AP 平均（AOC* 不合格）｜族平均（排除）｜zero statistics（目标另一侧）
｜仅上界/均方 bound（非 S2-c）｜显式公式改写为零点和（N1）｜仅 Fourier mean-square（须回到 h-空间主项）
```

## 1. 按"产生 cancellation 的变量"分类（唐先生的表 + 核查）
| 机制 | 真正平均变量 | R8 资格 | 核查结论 |
|---|---|---|---|
| HL（个体或平均） | h / prime pair | **排除** | 个体 h = twin-prime 强度；平均化版本亦以 HL 主项为输出 |
| Hooley/Montgomery（AP） | $(q,a)$ | **AOC\* 不匹配** | 其 h 仅为 AP 误差项区间长度 |
| 族平均 / 迹公式（L-function 族） | family parameter | **排除** | R6 已确立族结构不匹配 ζ |
| zero statistics | $(\gamma,\gamma')$ | **目标侧** | 即 $F(\alpha)$ 本身 |
| Fourier mean-square（Lavrik 型） | $\alpha$ | **需回到 h** | 只给频率侧；回 h-空间主项仍需算术输入（= 本问题） |
| 纯筛法 | — | **奇偶性障碍** | 只给上界，不给二元素数关联主项 |
| 大筛 / zero-density | — | **S2-b 级** | 非 uniform 主项 |
| Bombieri–Vinogradov 型 | modulus | **AOC\* 不匹配** | 同 AP |
| almost-all 一阶结果 | — | **非二阶** | 一阶 ⇏ S2-c（S4 教训） |
| **未知第三机制** | **h 本身** | **唯一活口** | 本轮**未发现** |

## 2. ⭐ 本轮结构性发现：唯一走出"平均二元关联"的先例，其引擎是【离散（自伴）谱侧】

**既有先例**：加法除数问题（$\sum_n d(n)d(n+h)$）在 **h-平均**下**可无条件求解**
（Motohashi / Deshouillers–Iwaniec 一线），机制 = **谱方法（Kuznetsov 公式）**。

**关键拆解**：
```
· Kuznetsov 的谱侧 = 离散谱（Maass 尖点形式）+ 连续谱（Eisenstein/ζ 相关项）
· 对除数函数：离散谱贡献【无条件可得】（自伴谱侧 ⟹ 谱参数实 ⟹ 门⑲的"RH 自动"侧）
· 对素数 Λ：对应的"谱输入"正是 ζ 的零点/配对相关 F(α) ⟹ **落在条件侧/目标侧**
```
$$\boxed{\text{除数情形之所以能无条件走出 h-平均，是因为其谱引擎坐在【离散·自伴】侧；}\\
\text{而 Λ 情形的同一引擎坐在【零点·散射】侧}}$$
**⟹ 与门⑲/⑳的结构完全同型**（"锁管离散侧；ζ 住在散射侧"）✓✓
**这是本项目内部的一条强交叉一致性检验**（两条独立路线指向同一不对称）。

## 3. 输出判定

$$\boxed{\textbf{R8.4-B}:\ \text{所有看似独立的候选机制，最后都退化为 HL / zero statistics / AP-族机器}}$$
**⚠️ 严格限定**：这是"**已枚举机制**"的归约，**仍不是必然性定理**；但本轮给出了**结构性理由**（§2）。

**R8-C\* 相应锐化**（@唐先生）：
$$\boxed{\textbf{R8-C}^{*}:\ \text{任何 canonical}、\text{zero-blind}、\text{非-HL}、\text{h-space cancellation}}\\
\text{若给出 S2-c，则必产生一个等价于 }F(\alpha)\ (\alpha>1)\ \text{的量}}$$
**等价表述（由 §2 得到的更强形式）**：
$$\boxed{\text{h-space cancellation 必须供给一个【谱输入】；而 Λ-关联可用的谱输入只有 zero-side 一种（"谱输入二分"）}}$$
——这正是门⑲/⑳"离散 vs 散射"的不对称在 R8 世界的重现。

## 4. 保留任务 ①（收口用，非当前决定性）
```
严格化 A2：完整扣除 Λ(n)² diagonal / 主项 H² 及交叉项 / x-积分边界 O(H²) 与 endpoint
⟹ 把"结构性可逆"升级为"严格可逆"，并形式化链条
   S2-c → V(X,H) → Σ_h(H−|h|)C_X(h) → F(α)
```

## 5. 诚实边界
```
· §2 的"Motohashi 一线经 Kuznetsov/谱方法"、"离散谱贡献无条件可得"标【文献级/待核实】
  （须核 Motohashi《Spectral theory of the Riemann zeta-function》原书与 DI 原文）
· §2 的"Λ 情形的谱输入 = 零点侧"为结构性论证（非定理）
· §3 是"已枚举机制范围内"的归约；R8-C* 仍为**待证靶点**
· 本轮未新增文献检索（除既有登记材料）；未写代码、未做数值
```

## 6. 提交链
```
c3cc749 R_conv 解出 → 本篇（R8.4 执行）
```
