# WITONER-2026-09-28 — **C-514：★★P1-A′ 引理\ \textbf{成立且机制找到} —— 对角候选点之 owner 数\ \textbf{恒 $\ge4$}（$0$ 反例）✓✓✓；共端点候选恰含 $\mathbf{640}$ 个 owner-size-3 点（＝四正 ✓✓）⟹ 对角禁交有\ \textbf{机制}**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 15:42 令 §9-P1-A′ ✓）**：核单点引理 $w\in W_{\rm diag}\Rightarrow|\mathrm{own}(w)|\ge4$；**不作路线裁定** ✗。

**已查地图：命中（接续 C-513／C-512／C-511，非新案 ✓）**：`WITDIAG-…`／`WITTYPE-…`／`WITLAM-…`
D0: 本档对象 ＝ **档案已有**（own/$N_2$/$W$；无新数学对象 ✓）
D1: 1（**首次\ \textbf{确立单点引理}}$w\in W_{\rm diag}\Rightarrow|\mathrm{own}(w)|\ge4$（\textbf{0 反例} ✓✓✓）＋ 首次给出\ \textbf{机制}（owner-计数 ✓）＋ 首次得共端点候选恰含 640 个 own-3 点（＝四正 ✓✓）** ✓）
**[RESEARCH]**

---

## §0 结论（**★引理成立 ＋ 机制到位 ✓✓✓**）

$$\textbf{设定 ✓}:\ \text{对角候选 }\ D_1{:=}N_2(I_a)\cap N_2(I_u)\cap N_2(I_b)\cap N_2(I_v)\ ✓;\ D_2{:=}N_2(I_a)\cap N_2(I_v)\cap N_2(I_b)\cap N_2(I_u)✓$$
$$\qquad\text{（即 }W_{11}\cap W_{22}\ \text{与}\ W_{12}\cap W_{21}\ \text{之候选集，\ \textbf{不限}于 }\mathcal S✓\big)$$
$$\boxed{\textbf{(1) ✓✓✓单点引理成立（唐先生 §3／§9 之猜想）}:\ }\forall w\in D_1\cup D_2:\ |\mathrm{own}(w)|\ge\mathbf4\ ✓✓✓\ \big(\textbf{0 反例}✓✓✓\big)$$
$$\qquad\textbf{（实测 ✓✓）}:\ D\ \text{元素之 }|\mathrm{own}|\ \text{分布}=\big\{\mathbf4{:}640,\ \mathbf5{:}960\big\}\ \text{——\ }\textbf{绝无 }3\ ✗✓\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{D_1,D_2\ \text{与}\ \mathcal S\ \textbf{不相交}}\ ⟹\ W_{11}\cap W_{22}=W_{12}\cap W_{21}=\varnothing\ ✓✓✓\ \big(\text{C-513 之事实\ \textbf{获得机制}}✓✓\big)$$
$$\qquad\textbf{（候选集结构 ✓）}:\ |D_1|,|D_2|\in\{0,1\}\ ✓\ \big(\text{分布 }\{0{:}22400,\ 1{:}800\}\ ✓\big)\ \text{——\ \textbf{至多一个}候选点 ✓✓}$$
$$\boxed{\textbf{(2) ✓✓★对照（共端点）}:\ }\text{共端点候选 }E{:=}N_2(I_a)\cap N_2(I_u)\cap N_2(I_v)\ ✓\ \big(\text{即 }W_{11}\cap W_{12}\ \text{之候选 ✓}\big)$$
| 量 | 值 |
|---|---|
| $\lvert E\rvert$ | $\{1{:}7680,\ 0{:}15520\}$ ✓ |
| $E$ 元素之 $\lvert\mathrm{own}\rvert$ | $\big\{4{:}3520,\ 5{:}3520,\ \mathbf3{:}\mathbf{640}\big\}$ ✓✓ |
$$\qquad\Longrightarrow\ \boxed{\text{共端点候选\ \textbf{恰含 640 个 own-3 点}}＝\text{四正实例数}\ ✓✓✓}$$
$$\qquad\textbf{（读法 ✓✓✓）}:\ \text{唯一能实现重叠的 }w^\ast\ \text{正是那 640 个 own-size-3 点 ✓✓\ \big(\text{＝}\mathcal S\ \text{元素 ✓}\big)\ \text{——\ 与 C-513 之对当式\ \textbf{完全一致}}✓✓✓}$$
$$\qquad\Longrightarrow\ \textbf{（机制 ✓✓✓）}:\ \text{重叠之存在性\ \textbf{完全由}\ owner-计数\ \text{决定}:\ 对角 ⟹ own}\ge4\ \text{（出局 ✓）;\ 共端点 ⟹ 可 own}{=}3\ ✓✓$$

## §1 机制之两句话总结（**★P1-A 由 census 事实升级为机制 ✓✓✓**）

$$\boxed{\text{（m1）一个点若同时实现\ \textbf{两组端点不相交}之 cross-pair ⟹ 其 owner 数}\ \ge4\ ⟹\ \text{不属}\ \mathcal S\ ⟹\ \text{对角交为空}}✓✓✓$$
$$\boxed{\text{（m2）一个点若同时实现\ \textbf{两槽共一码字}之 cross-pair ⟹ owner 数可为 3 ⟹ 可属}\ \mathcal S\ ✓✓}$$
$$\qquad\Longrightarrow\ \text{此即 C-513 之}\ W_{ij}\cap W_{kl}\ne\varnothing\Rightarrow\{ij,kl\}\ \text{共端点}\ \text{的\ \textbf{结构性原因}}✓✓✓$$

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §3（"一个 }w\ \text{能否同时满足两组 }N_2\ \text{约束 ⟹ 支撑计数矛盾"\ ）\ \textbf{完全命中}}✓✓✓\ \text{——\ 本档证实：}\textbf{owner 计数即该矛盾}✓✓$$
$$\textbf{✓✓✓}:\ \text{其 §9-P1-A′ 之目标形 }w\in W_{\rm diag}\Rightarrow|\mathrm{own}(w)|\ge4\ \textbf{成立}}✓✓✓\ \text{（0 反例 ✓）——\ 且其\ \textbf{单行 P1} 之愿望达成 ✓✓$$
$$\textbf{✓✓✓}:\ \text{其 §4 之"λ-free interface"（四正 \iff 共端点重叠）\ \textbf{成立}}✓✓\ \big(\text{C-513 ✓ ＋ 本档 (2) 之 640 对当 ✓✓}\big)$$
$$\textbf{✓✓}:\ \text{其 §5–§6（}W_{11}{=}\{w^\ast\}\ \text{等规范化）\ \textbf{成立}}✓✓\ \text{（}|\lambda{=}1\Rightarrow|W|{=}1✓\ \text{，C-510 ✓）}$$
$$\textbf{✓✓}:\ \text{其 §7–§8（跨层禁配候选 C{=}3\Rightarrow\mathrm{mask}\ne1111）\ \textbf{方向正确}}✓✓\ \text{（本档之机制为其提供 owner-计数支点 ✓✓）}$$

## §3 汇总裁（**✓✓✓**）

| 项 | 值 |
|---|---|
| $D$ 元素之 $\lvert\mathrm{own}\rvert$ | $\{4{:}640,5{:}960\}$（**无 3**）✓✓✓ |
| 反例数 | $\mathbf0$ ✓✓✓ |
| $\lvert D\rvert$ | $\le1$ ✓ |
| $E$ 元素之 $\lvert\mathrm{own}\rvert$ | 含 $\mathbf{640}$ 个 own-3 ✓✓ |
| 机制 | 对角 ⟹ own$\ge4$；共端点 ⟹ own${=}3$ 可 ✓✓ |

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "owner计数支点" "对角候选集" "跨层禁配定理"
技术词 owner计数支点 命中文件数=1    :: ./WITONER-2026-09-28-diagonal-overlap-forces-owner-size-four.md
技术词 对角候选集  命中文件数=1    :: ./WITONER-2026-09-28-diagonal-overlap-forces-owner-size-four.md
技术词 跨层禁配定理 命中文件数=1    :: ./WITONER-2026-09-28-diagonal-overlap-forces-owner-size-four.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| owner计数支点 | 0 | 0 | ✓（本档新命名 ✓） |
| 对角候选集 | 0 | 0 | ✓（本档新命名 ✓） |
| 跨层禁配定理 | 0 | 0 | ✓（照唐先生 §8 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 下一靶（**照唐先生 §9 之序 ✓**）

$$\textbf{（P1-B ✓✓）}:\ \text{四正 ＋ }w^\ast\in W_{11}\cap W_{12}⟹R(w^\ast)\in\{(4,2,2,2),(2,4,2,4),(2,4,4,2)\}\ ——\ \text{由 }\lvert T_{w^\ast}\rvert{=}3\ \text{＋ }d(ab){=}d(uv){=}4\ \text{逐加排除 ✓✓}$$
$$\textbf{（P1-C ✓✓✓）}:\ \text{直攻层数}:\ w^\ast\ \text{重叠}\Rightarrow\exists\ \text{必要点 }|\mathrm{own}|\ge4\ ⟹\ C\ge4\ ——\ \text{若成则\ \textbf{取代} }T_1/T_2\ \text{completion}✓✓$$
$$\textbf{（P2 ✓备用）}:\ \text{common-endpoint profile}\to\text{private witnesses}\to T_1,T_2\ ✓$$
$$\textbf{（禁止 ✗）}:\ \text{再扩 census ✗（照唐先生 ✓）；把机制之实证当\ \textit{证明}\ ✗✓}$$

## §6 边界（硬 ✓）

- **有限穷举** ✓（候选集 $D_1,D_2,E$ 全量 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项★引理（0 反例 ✓✓✓）** ＋ **一项机制（owner-计数 ✓✓✓）** ＋ **一项对当（640 ✓✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** 单点引理已有\ *书面证明* ✗（现为\n 全量实证 ✓）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
