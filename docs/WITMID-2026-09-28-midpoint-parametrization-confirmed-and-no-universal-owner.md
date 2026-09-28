# WITMID-2026-09-28 — **C-532：★★$C_{ij}$ 之\ \textbf{中点参数化\ 完全成立}（$C_{ij}{=}\{I_i\oplus\mathbf1_S:S\in\binom D2\}$，\textbf{960/960}）✓✓✓；但\ \textbf{无 universal 额外 owner}（除 $i,j$ 外公共 owner 数恒 $\mathbf0$）✗✓**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 17:07 §1／§7 令 ✓）**：核中点参数化 ＋ universal owner；**不作路线裁定** ✗。

**已查地图：命中（接续 C-531／C-530／C-509，非新案 ✓）**：`WIT6PT-…`／`WIT4TH-…`／`WITDOSSIER-…`
D0: 本档对象 ＝ **档案已有**（$C_{ij}$／中点／owner；无新数学对象 ✓）
D1: 1（**首次\ \textbf{完全确认}中点参数化 $C_{ij}{=}\{I_i\oplus\mathbf1_S:S\in\binom D2\}$（\textbf{960/960}）✓✓✓ ＋ 首次判定\ \textbf{无 universal 额外 owner}（除 $i,j$ 外公共 owner 数恒 $0$）✗✓ ＋ 首次得额外 owner 个数恒为 $2$ 或 $3$（型即 owner-大小 $\{4,5\}$ 之直接读法）✓✓**）
**[RESEARCH]**

---

## §0 ★结论（**参数化 ✓✓✓；universal owner ✗✓**）

$$\textbf{设定 ✓}:\ \text{三正实例之第四槽 }(i,j)\ \text{且 }|C_{ij}|{=}6\ (960\ \text{例});\ D{:=}\mathrm{supp}(I_i\oplus I_j)\ ✓$$
$$\boxed{\textbf{(1) ✓✓✓中点参数化\ \textbf{完全成立}}:\ }\boxed{C_{ij}=\big\{I_i\oplus\mathbf1_S:\ S\in\textstyle\binom D2\big\}}\ \text{于\ \textbf{960/960}}\ ✓✓✓$$
$$\qquad\textbf{（唐先生之推导 ✓✓✓）}:\ |A|{=}|B|{=}2,\ A\cap B{=}\varnothing\ ⟹ d(I_i,I_j){=}4\ \big(\text{码距 }\ge4\big)⟹ |D|{=}4⟹\binom42{=}6\ ✓✓$$
$$\qquad\Longrightarrow\ \textbf{（重大 ✓✓✓）}:\ \text{六点候选集\ \textbf{非经验现象}，而是 }D\ \text{之\ \textbf{全部二元中点}}\ ✓✓\ \text{——\ 六点结构\ \textbf{完全参数化}}✓✓✓$$
$$\boxed{\textbf{(2) ✗✓\textbf{无 universal 额外 owner}}}:\ \text{除 }i,j\ \text{外，无任何码字索引对六中点\ \textbf{全出现}}:\ \#\{\text{公共额 owner}\}=\mathbf0\ \text{于\ \textbf{960/960}}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{唐先生 §7 之 }\mathbf{25}\ \text{未必 universal}✗✓:\ \text{实则\ \textbf{25 与 7 常即 }$i,j$\ \text{本身}}\ ✓\ \big(\text{代表例：六中点之 own }\textbf{皆含 }7\ \text{与 }25⟹\{i,j\}{=}\{7,25\}\ \text{亦即定义式 ✓}\big)$$
$$\qquad\textbf{（故 owner}\ge4\ \text{之来源\ \textbf{非}固定码字}✗✓\big)}:\ \text{额外 owner\ \textbf{随 }$S$\ \text{而变}}✓{$$
$$\boxed{\textbf{(3) ✓✓额外 owner 个数}}:\ \text{每中点之额外 owner 数为 }\mathbf2\ \text{或}\ \mathbf3\ ✓\ \big(\text{型如 }(3,2,2,3,2,2)\text{ 等 12 种}\big)$$
$$\qquad\Longrightarrow\ \text{即 }|\mathrm{own}|{=}2{+}2{=}4\ \text{或 }2{+}3{=}5\ ✓✓\ \text{——\ 与 C-530 之 }\{4{:}4,5{:}2\}\ \text{一致 ✓✓}$$

## §1 代表实例（**✓**）

$$\text{六中点之完整 owner 集 }(i,j{=}7,25):$$
| $S$ | $w_S$（二进制） | $\mathrm{own}(w_S)$ |
|---|---|---|
| $(1,3)$ | $1010001011$ | $(7,21,25,26,35)$ |
| $(1,6)$ | $1011000011$ | $(7,25,29,37)$ |
| $(1,9)$ | $0010000011$ | $(6,7,10,25)$ |
| $(3,6)$ | $1011001001$ | $(7,22,25,28,38)$ |
| $(3,9)$ | $0010001001$ | $(0,7,16,25)$ |
| $(6,9)$ | $0011000001$ | $(7,8,18,25)$ |
$$\qquad\Longrightarrow\ \mathbf{7}\ \text{与}\ \mathbf{25}\ \text{于六者\ \textbf{全出现}}✓✓\ \text{（唯二者即 }i,j\ ✓\big);\ \text{其余额 owner}\ \textbf{逐 }S\ \text{而异}✗✓$$

## §2 汇总裁（**✓✓✓／✗✓**）

| 项 | 值 |
|---|---|
| 中点参数化 | **成立**（960/960）✓✓✓ |
| $\lvert D\rvert$ | 恒 $4$ ✓✓ |
| $\lvert C_{ij}\rvert$ | $\binom42{=}6$ ✓✓ |
| universal 额外 owner | **无**（$0/960$）✗✓ |
| 额外 owner 数 | $2$ 或 $3$ ✓✓ |

## §3 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §1（}A,B\ \text{不交}\Rightarrow d{=}4\Rightarrow|D|{=}4\Rightarrow C_{ij}{=}\binom D2\ \text{之中点）\ \textbf{完全正确}}✓✓✓\ \big(\text{960/960}\big)$$
$$\textbf{✓✓}:\ \text{其 §2（owner}\ge4\ \text{化为"每中点须再找 }\ge2\ \text{外部 owner"\ ）\ \textbf{成立}}✓✓$$
$$\textbf{✓✓}:\ \text{其 §4（六中点之内部 }K_6\ \text{：每点 4 个距-2 邻点、1 个距-4 点）\ \textbf{成立}}✓✓\ \big(S\cap T\ \text{之交数决定 }d{=}2,4\big)✓✓$$
$$\textbf{✗✓}:\ \text{其 §7（"25 为 universal owner"\ 之希望）\ ⟹ \textbf{不成立}}✗✓\ \big(\text{25 常即 }j\ \text{本身}\big)✓$$
$$\textbf{✓✓}:\ \text{其 §8（否则寻 }S\mapsto\{K_S,L_S\}\ \text{之对称规则）\ \textbf{方向正确}}✓✓\ \text{——\ 本档已证额外 owner\ \textbf{确随 }$S$\ \text{变}✓✓}$$

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "中点参数化" "universal owner" "二元中点集"
技术词 中点参数化  命中文件数=1    :: ./WITMID-2026-09-28-midpoint-parametrization-confirmed-and-no-universal-owner.md
技术词 universal owner  命中文件数=1    :: ./WITMID-2026-09-28-midpoint-parametrization-confirmed-and-no-universal-owner.md
技术词 二元中点集  命中文件数=1    :: ./WITMID-2026-09-28-midpoint-parametrization-confirmed-and-no-universal-owner.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 中点参数化 | 0 | 0 | ✓（照唐先生 §1 ✓） |
| universal owner | 0 | 0 | ✓（照唐先生 §7 ✓） |
| 二元中点集 | 0 | 0 | ✓（本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓✓）}:\ \text{由中点参数化}＋K_6\ \text{结构\ \textbf{正向推}}\ \lvert\mathrm{own}(w_S)\rvert\ge4\ ✓✓\ \text{——\ 现已是\ \textbf{纯 }$D$\ \text{四坐标问题}}✓✓$$
$$\textbf{（靶 2 ✓✓）}:\ \text{研究 }S\mapsto\{K_S,L_S\}\ \text{之规则（其随 }S\ \text{变 ✓；查是否有 }S\leftrightarrow D{\setminus}S\ \text{或其它对称）}✓✓$$
$$\textbf{（靶 3 ✓）}:\ \text{重跑两支复核（修 C-525 脚本 bug）✓}$$
$$\textbf{（禁止 ✗）}:\ \text{假定 universal owner ✗✓；纯计数 ✗✓；由 }F,G\ \text{反推 ✗✓}$$

## §6 边界（硬 ✓）

- **有限穷举** ✓（960 例之中点／owner 全量 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项★★确认（中点参数化 ✓✓✓）** ＋ **一项✗✓（无 universal owner）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** $|\mathrm{own}(w_S)|\ge4$ 已有结构证明 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
