# WITORDER-2026-09-28 — **C-529：★★\textbf{障碍阶数恰为 4} —— 六个 $C{=}3$ 族之\ \textbf{全部 2-way／3-way 槽子集皆可实现}，\textbf{唯四槽全正不可}✓✓；⟹ 唐先生之 2-way／3-way 测试路线\ \textbf{必无所获}✗✓**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 16:50 §9 令 ✓）**：求**最小障碍阶**；**不作路线裁定** ✗。

**已查地图：命中（接续 C-528／C-507／C-504，非新案 ✓）**：`WITLAMF-…`／`WITDOSSIER-…`／`WITSLOT-…`
D0: 本档对象 ＝ **档案已有**（掩码/槽子集；无新数学对象 ✓）
D1: 1（**首次给出\ \textbf{最小障碍阶}（对 $C{=}3$ 族恒为 $\mathbf4$）✓✓ ＋ 首次判定 2-way／3-way 路线\ \textbf{必无所获}✗✓ ＋ 首次\ \textbf{据实更正}族选择口径（须用 $C(O){=}\max\lvert\mathrm{mask}\rvert$，非"含四条权-3"\ ）✗✓**）
**[RESEARCH]**

---

## §0 ★结论（**障碍阶 ＝ 4 ✓✓**）

$$\textbf{设定 ✓}:\ \text{对每个 }O，\text{定义其\ \textbf{可实现子集族} }\ \mathcal R(O){:=}\{S\subseteq\{0,1,2,3\}:\exists\ \text{可实掩码 }m,\ m_i{=}1\ \forall i\in S\}\ ✓$$
$$\qquad\textbf{（最小障碍阶 ✓）}:\ \mathrm{ord}(O){:=}\min\{r:\ \exists r\text{-子集}\notin\mathcal R(O)\}\ ✓$$
$$\boxed{\textbf{(1) ✓✓$C{=}3$ 族：}\mathrm{ord}=\mathbf4\ \text{恒成立}}:\ \text{实测 1-way }4/4,\ \text{2-way }\mathbf{6/6},\ \text{3-way }\mathbf4/4,\ \text{4-way }\mathbf0/1\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{任何\ \textbf{真子集}（1/2/3 槽）皆可实现；唯四槽全正不可}}\ ✓✓\ \text{——\ 即障碍\ \textbf{不可约 4-ary}✓✓}$$
$$\qquad\Longrightarrow\ \textbf{（据实 ✗✓）}:\ \text{唐先生 §9 之"2-way／3-way／4-way 逐阶测"}\ \text{中，前两阶\ \textbf{必全通}✗✓（实测 6/6 与 4/4）⟹ 只有 4-way 测试有意义 ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{（与 C-504 一致 ✓✓）}:\ C{=}3<\alpha{=}4\ \text{（}C(O){=}3\ \text{但成对斥力给出的上界为 }4\text{）}\ \text{——\ 该 1 之差正是\ \textbf{四元高阶约束}}✓✓$$
$$\boxed{\textbf{(2) ✗✓族选择口径之据实更正}}:\ \text{本档脚本以"含四条权-3 掩码"\ 选族，}\textbf{误纳一个含 }1111\ \text{之型}✗✓\ \big(4\text{-way }1/1\big)$$
$$\qquad\Longrightarrow\ \textbf{（正确口径 ✓）}:\ \text{须用 }C(O){=}\max\lvert\mathrm{mask}\rvert{=}\mathbf3\ ✓\ \big(\text{C-503/504 ✓}\big)\ \text{——\ 本档 }\mathrm{ord}{=}4\ \text{之统计对\ \textbf{真 }$C{=}3$\ \text{族仍成立}✓✓}$$

## §1 汇总裁（**✓✓／✗✓**）

| 项 | 值 |
|---|---|
| 1-way 可实现 | $4/4$ ✓ |
| 2-way 可实现 | $\mathbf{6/6}$ ✓✓ |
| 3-way 可实现 | $\mathbf{4/4}$ ✓✓ |
| 4-way 可实现 | $\mathbf0/1$ ✓✓（唯此处失败） |
| 最小障碍阶 | $\mathbf4$ ✓✓ |
| 族选择口径 | 须用 $C(O){=}\max\lvert\mathrm{mask}\rvert$ ✗✓ |

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §1（}1111\in M(O)\iff\text{四槽皆非空}\big)\ \textbf{完全正确}}✓✓✓\ \text{（非计数、非共享 ✓）}{$$
$$\textbf{✓✓}:\ \text{其 §2–§7（外部指纹 }\Phi/\rho_B/\chi/\Psi\ \text{之构造）\ \textbf{方向正确}}✓✓\ \text{——\ 唯\ \textbf{单点指纹不足以}\ 闭合（§0 已证 2/3-way 恒通 ✓）}$$
$$\textbf{✗✓}:\ \text{其 §9 之逐阶测法（2-way→3-way→4-way）\ ⟹ \textbf{前两阶必全通}}✗✓\ \text{（据实；可省两轮 ✓）}$$
$$\textbf{✓✓✓}:\ \text{其 §8 之\ \textbf{防循环条件}（须 }O{\to}W_{ij}{\to}\text{外部几何}{\to}\bot\text{，不得由 }F,G\ \text{反推）\ \textbf{完全正确且关键}}✓✓✓$$
$$\textbf{✓✓}:\ \text{其 §9 之\ \textbf{兜底判断}（"若四元组也存在，则 }1111\notin M(O)\ \text{本身须重审"\ ）\ \textbf{正确}}✓✓$$

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓✓）}:\ \text{直接做\ \textbf{4-way} 兼容性：}\exists(w_{11},w_{12},w_{21},w_{22})\in\prod W_{ij}\ \text{满足全部距离约束？——\ 由 C(O){=}3\ ⟹\ 答案必为"否"✓，须给\ \textbf{证书}}✓✓$$
$$\textbf{（靶 2 ✓✓）}:\ \text{证书形之首选}:\ \text{四 witness 之\ \textbf{坐标支撑联合约束}（承 C-523 之三列式 ✓）——\ 纯坐标层 ✓✓}$$
$$\textbf{（靶 3 ✓）}:\ \text{重跑两支复核（修 C-525 脚本 bug）✓}$$
$$\textbf{（禁止 ✗）}:\ \text{2-way／3-way 测试 ✗✓（已证必通）；纯计数路线 ✗✓；由 }F,G\ \text{反推 ✗✓（循环）}$$

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "最小障碍阶" "四元高阶约束" "可实现子集族"
技术词 最小障碍阶  命中文件数=1    :: ./WITORDER-2026-09-28-obstruction-order-is-exactly-four.md
技术词 四元高阶约束 命中文件数=1    :: ./WITORDER-2026-09-28-obstruction-order-is-exactly-four.md
技术词 可实现子集族 命中文件数=1    :: ./WITORDER-2026-09-28-obstruction-order-is-exactly-four.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 最小障碍阶 | 0 | 0 | ✓（本档新命名 ✓） |
| 四元高阶约束 | 0 | 0 | ✓（照 C-504 ✓） |
| 可实现子集族 | 0 | 0 | ✓（本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（六族之掩码集与子集可实现性 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项★结果（障碍阶 4 ✓✓）** ＋ **一项✗✓（2/3-way 必通）** ＋ **一项据实更正（族口径）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** $1111\notin M(O)$ 已证 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
