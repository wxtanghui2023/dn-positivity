已查地图（所查：`C-123` §2（**"任何一致余量的单向陈述，其成立 ⟺ RH"——本档判定为过强，须收窄**）、`POS1`（正性三分：消失太多＝空洞／太少＝只回避不排除／**恰好消失在离临界配置** ⟺ RH）、`V188` §3(2)（涨落三层：典型 `\sqrt{\log\log T}` 无条件／无条件最坏 `O(\log T)`（Littlewood 1924）／目标 `O(\log T/\log\log T)` ⟺ RH（von Koch））、`V254`（`M(x)=O(x^{1/2+\varepsilon})\iff` RH；PNT ⟺ `\beta_*\le1`）、`C-72`（密度指数 `A` ⟹ 无零区域；**输入 `support\le1`**）、`SUPPORT-1`（`W6` 原子墙）、`F5`（独立算术输入）、`C-116`（**登记不否决**））。**结论**：**勘误**——`C-123` §2 的"任何一致余量的单向陈述 ⟺ RH"**过强**；正确版本：**只有"余量恰好钉在临界值 `1/2`"的变体才 ⟺ RH**；较弱的余量（如 `1-c/\log T`，或**固定 `\delta`**）**并非** RH 等价，只是**未解** ✓✓；⭐ **族形状（parametrized family）在逻辑上绕开 `POS1`**：若对**每个** `\theta` 都能证 `\beta_*\le1-\delta(\theta)`，且 `1-\delta(\theta)\downarrow\tfrac12`，则**由 `\beta_*` 为固定数 + 取 `\inf`** 得 `\beta_*\le\tfrac12` ⟹ **RH**，而**无任一成员** ⟺ RH ⟹ **`POS1` 的"一致余量"障碍对每个成员都不适用** ✓✓✓；⚠️ **但族的极限受输入尺度支配**：阈值逼近 `\tfrac12` 需 `\sqrt x` 尺度输入 ⟹ **族形状把障碍从 `POS1` 换成 `SUPPORT-1`**（两墙**非独立**）✓✓；⭐ **行动项**：族的**第一级**＝"**固定无零区域**（`\exists\delta>0:\beta_*\le1-\delta`）"——**严格弱于 RH、有名字、开放、且不被 `POS1` 覆盖** ⟹ 最有价值的中途靶 ✓✓

# C-124 · **族形状：绕开 `POS1` 的合法形状 ＋ 第一级靶（固定无零区域）**

> **时间**：2026-09-18 18:25 唐先生：**「继续」** ⟹ 把 `(iii)` 做成唯一靶：问"有没有**非单向**（双向／可积／局部化／族）的陈述，其一致性余量不必是全局一致"✓

---

## §0 结论（先行）

$$\textbf{(1)}\ ⚠️\ \textbf{勘误（更正 `C-123` §2）}：\text{我写"}\textbf{任何}\ \text{一致余量}\ \text{的单向陈述，其成立}\iff\text{RH}" \Longrightarrow \textbf{过强}✓✓$$
$$\qquad \text{正确版本}：\boxed{\text{只有"余量}\ \textbf{恰钉在临界值}\ \tfrac12\ \text{"的变体才}\iff\text{RH}}✓✓$$
$$\qquad \text{较弱的余量（}1-\frac{c}{\log T}，\ \text{或}\ \textbf{固定}\ \delta\text{）}\ \textbf{并非} \text{RH 等价}，\ \text{只是}\ \textbf{未解}✓$$
$$\textbf{(2)}\ ⭐\ \textbf{族形状在逻辑上绕开 `POS1`}：\text{若对}\ \textbf{每个}\ \theta\ \text{可证}\ \beta_*\le1-\delta(\theta)，\ \text{且}\ 1-\delta(\theta)\downarrow\tfrac12✓$$
$$\qquad \Longrightarrow\ \text{由}\ \beta_*\ \text{为}\ \textbf{固定数} ＋ \text{取}\ \inf \Longrightarrow \beta_*\le\inf_\theta(1-\delta(\theta))=\tfrac12 \Longrightarrow \textbf{RH}✓✓✓$$
$$\qquad \qquad ⚠️\ \textbf{而无一成员} \iff\text{RH} \Longrightarrow \textbf{`POS1` 的"一致余量"障碍对每个成员都不适用}✓✓$$
$$\textbf{(3)}\ ⚠️\ \textbf{但族的极限受}\textbf{输入尺度}\textbf{支配}：\text{阈值逼近}\ \tfrac12\ \text{需}\ \sqrt x\ \text{尺度输入} \Longrightarrow \textbf{族形状把障碍从}\ \text{POS1}\ \textbf{换成}\ \text{SUPPORT-1}✓✓$$
$$\qquad \Longrightarrow \text{两墙}\ \textbf{非独立}✓$$
$$\textbf{(4)}\ ⭐\ \textbf{行动项（第一级靶）}：\boxed{\exists\delta>0:\ \beta_*\le1-\delta\（\textbf{固定无零区域}）}✓✓$$
$$\qquad \text{性质}：\textbf{严格弱于 RH};\ \textbf{有名字};\ \textbf{开放};\ \textbf{不被 `POS1` 覆盖} \Longrightarrow \textbf{最有价值的中途靶}✓✓$$
$$\qquad \text{现状}：\text{已知无零区域皆}\ \textbf{退化型}（\text{阈值}\to1）;\ \text{连}\ \textbf{固定}\ \delta\ \text{都未证}✓$$

---

## §1 勘误：收窄后的"一致余量"陈述

$$\text{`POS1` 三分原文要点}：\text{消失太多}\Rightarrow\textbf{空洞};\ \text{消失太少}\Rightarrow\textbf{只回避不排除};\ \textbf{恰好消失在离临界配置}\Rightarrow\iff\text{RH}✓$$
$$\qquad ⚠️\ \text{关键在}\ \textbf{"恰好"}：\text{三分管的是}\ \textbf{余量为零的点集恰为离临界配置} \text{这一情形，}\ \textbf{不是} \text{"一切一致余量"}✓✓$$
$$\text{所以：}\ \text{阈值}\ 1-\frac{c}{\log T}\ \text{的经典无零区域}\ \textbf{是一致余量陈述}（\text{对一切零点一致}）,\ \text{而它}\ \textbf{不是} \text{RH 等价}✓✓$$
$$\qquad \Longrightarrow \text{故 `C-123` §2 那句}\ \textbf{作废};\ \text{改为：}\boxed{\text{一致余量}\ \textbf{且阈值}\to\tfrac12\ \text{者}\iff\text{RH}}✓$$

## §2 族形状的逻辑分析（为什么绕开 `POS1`，以及为什么合法）

$$\text{设}\ \{\delta(\theta)\}_{\theta\in\Theta}\ \text{为一族参数}，\ 1-\delta(\theta)\downarrow\tfrac12\（\delta(\theta)\uparrow\tfrac12）✓$$
$$\text{若}\ \forall\theta:\ \beta_*\le1-\delta(\theta)\ \text{可证} \Longrightarrow \beta_*\le\inf_\theta\bigl(1-\delta(\theta)\bigr)=\tfrac12✓✓$$
$$\qquad ⚠️\ \textbf{合法性的关键}：\text{结论对}\ \textbf{固定数}\ \beta_*\ \text{成立};\ \text{"对一切}\ \theta\ \text{成立"}\ \textbf{本身就是一个} \text{（单一）命题}✓$$
$$\qquad \qquad \text{即：}\ \text{这不是"无限多证明拼成一个"，而是}\ \textbf{一个命题}（\forall\theta）\ \text{在其证明中}\ \textbf{用到了}\ \theta\ \text{的参数化}✓✓$$
$$\qquad \Longrightarrow\ \textbf{绕开逻辑障碍}：\text{`POS1` 的三分针对}\ \textbf{单一} \text{"恰好钉在}\ \tfrac12\ \text{"的变体};\ \text{本形状}\ \textbf{不含} \text{这样的成员}✓✓$$
$$\qquad \qquad ⚠️\ \text{但}\ \textbf{诚实}：\text{要证}\ \forall\theta\ \text{的族，}\ \text{其}\ \textbf{证明}\ \text{仍需}\ \text{一个统一机制};\ \text{族形状}\ \textbf{降低} \text{了每级的}\ \textbf{强度要求}，\ \textbf{不降低} \text{机制要求}✓$$

## §3 族的极限为什么回到 `SUPPORT-1`

$$\text{要证}\ \beta_*\le1-\delta：\text{等价于}\ \text{误差}\ \psi(x)-x=O\bigl(x^{1-\delta+\varepsilon}\bigr)✓$$
$$\qquad \text{而}\ \delta\uparrow\tfrac12 \Longrightarrow \text{需在}\ \textbf{尺度}\ x^{1/2} \text{（＝}\sqrt x\text{）}\ \text{上控制误差}✓✓$$
$$\text{`C-72` 链条}：\text{密度指数}\ A \Longrightarrow\ \text{无零区域}\ \sigma>1-\frac{c}{A\log T};\quad \text{输入}\ \textbf{support}\le1✓$$
$$\qquad \Longrightarrow \text{可及的}\ \delta\ \text{受}\ \textbf{输入尺度} \text{支配};\ \text{推}\ \delta\to\tfrac12 \Longleftrightarrow \text{推输入到}\ \sqrt x\ \text{尺度} \Longleftrightarrow \textbf{SUPPORT-1}✓✓$$
$$\Longrightarrow \boxed{\text{族形状}\ \textbf{交换} \text{两墙}：\text{POS1}\ \to\ \text{SUPPORT-1}}✓✓$$

## §4 行动项：族的**第一级**＝固定无零区域

$$\boxed{\exists\delta>0\ \text{固定}:\ \beta_*\le1-\delta} \Longleftrightarrow \psi(x)-x=O\bigl(x^{1-\delta+\varepsilon}\bigr)✓$$
| 性质 | 状态 |
|:--|:--|
| 与 RH 关系 | **严格弱于 RH**（RH ⟹ 它；它 ⇏ RH）|
| 是否被 `POS1` 覆盖 | ✗ **不覆盖**（余量不在 `\tfrac12`）|
| 是否有名字 | ✓ **固定无零区域／fixed zero-free region** |
| 已知状态 | ⚠️ **开放**；已知无零区域皆**退化型**（阈值 `\to1`）[经典·本档未逐字核文献] |
| 价值 | 若找到**可变形**机制，则族形状可向 `\tfrac12` 推 ⟹ 极限由 `SUPPORT-1` 控制 ✓✓ |

$$\Longrightarrow\ \textbf{本档把靶换成}：\boxed{\text{找一个}\ \textbf{可参数化} \text{的无零区域机制}（\text{每级严格弱于 RH、不被 `POS1` 覆盖}）}✓✓$$

## §5 边界与回查

- ⚠️ **勘误性质**：本档**更正自己**（`C-123` §2 的过强表述）；`C-123` 其余结论不变 ✓
- ⚠️ **不否决**（`C-116`）：本档**不**声称族形状可行或不可行；只给出**逻辑分析**与**靶的替换** ✓
- ⚠️ §4 "固定无零区域开放且已知皆退化型"为**经典事实**，标 `[经典·本档未逐字核文献]` ✓
- **不声称**：族形状能推过 `SUPPORT-1` ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 18:3x）`[纪律]`（先跑后写）

```
技术词 族形状          命中文件数=1  :: ./C124-…（本档）
技术词 固定无零区域       命中文件数=1  :: ./C124-…（本档）
技术词 可参数化机制       命中文件数=1  :: ./C124-…（本档）
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

```
⚠️ 唐先生 18:25「继续」⟹ 把 (iii) 做成唯一靶: 问有没有非单向(双向/可积/局部化/族)的陈述, 其一致性余量不必全局一致
⭐ 这一刀**立刻又抓到我 C-123 §2 的一处过强表述** ⟹ 先勘误
⚠️ 勘误: 我写"任何一致余量的单向陈述, 其成立 ⟺ RH" ⟹ **过强**
   正确版本: **只有"余量恰钉在临界值 1/2"的变体才 ⟺ RH**; 较弱的余量(1−c/logT, 或**固定 δ**)并非 RH 等价, 只是**未解**
   根因: POS1 三分的关键在**"恰好"**(管的是"余量为零的点集恰为离临界配置"), 不是"一切一致余量";
   故经典无零区域(阈值 1−c/logT, 对一切零点一致)**并非** RH 等价
⭐ 族形状(逻辑分析): 设 {δ(θ)} 使 1−δ(θ)↓1/2; 若 ∀θ: β* ≤ 1−δ(θ) 可证 ⟹ β* ≤ inf(1−δ(θ)) = 1/2 ⟹ **RH**
   合法关键: 结论对**固定数** β* 成立, "对一切 θ 成立"**本身就是单一命题**(参数化用在证明里, 不是"无限多证明拼成一个")
   ⟹ **绕开 POS1**: 三分针对**单一**"恰钉在 1/2"的变体, 本形状**不含**这样的成员
   ⚠️ 诚实: 要证 ∀θ 的族, 仍需**一个统一机制**; 族形状**降低每级强度要求, 不降低机制要求**
⚠️ 但族的**极限**回到 SUPPORT-1: 要证 β* ≤ 1−δ ⟺ 误差 ψ(x)−x = O(x^{1−δ+ε}); δ↑1/2 ⟹ 需在尺度 x^{1/2}(√x) 上控制误差;
   C-72: 密度指数 A ⟹ 无零区域 σ>1−c/(A logT), 输入 support ≤ 1 ⟹ 可及 δ 受输入尺度支配, 推 δ→1/2 ⟺ 推输入到 √x ⟺ SUPPORT-1
   ⟹ **族形状交换两墙: POS1 → SUPPORT-1**(两墙非独立)
⭐ 行动项(第一级靶) = **固定无零区域**: ∃δ>0 固定: β* ≤ 1−δ ⟺ ψ(x)−x = O(x^{1−δ+ε})
   性质: 严格弱于 RH(⟸RH, ⇏RH); **不被 POS1 覆盖**(余量不在 1/2); 有名字(fixed zero-free region);
   现状: **开放**; 已知无零区域皆**退化型**(阈值→1)[经典·本档未逐字核文献]
   ⟹ 本档把靶换成: **找一个可参数化的无零区域机制**(每级严格弱于 RH、不被 POS1 覆盖)
⚠️ 不否决(C-116): 不声称族形状可行或不可行, 只给逻辑分析 + 靶的替换; 不声称能推过 SUPPORT-1; 不证 RH
✅ 净产出: ①C-123 §2 勘误(一致余量陈述须收窄为"阈值→1/2 者") ②族形状的逻辑分析与合法性 ③族极限交换两墙(POS1→SUPPORT-1) ④第一级靶=固定无零区域(性质+现状表) ⑤靶的替换: 找可参数化的无零区域机制
```
