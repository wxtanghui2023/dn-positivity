# WITGA2-2026-09-28 — **C-518：★★Gate A（2B）\ \textbf{成立}：4 正槽 $\Longrightarrow$ 必有重叠（640/640，excess 恒 $=1$）✓✓✓；\textbf{新刚性} excess $\le1$ 于全量 23200 ✓✓；✗✓\textbf{更正} C-513 之"$\iff$"过强（2／3 正槽亦有重叠）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 15:51 §12 令 ✓）**：攻 **A**（"7 个完全私有 owner-3 witness 不可能"）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-517／C-516／C-515，非新案 ✓）**：`WITGA-…`／`WITGATE-…`／`WITCAPB-…`
D0: 本档对象 ＝ **档案已有**（$W$／excess／$\lambda$；无新数学对象 ✓）
D1: 1（**首次判定 Gate A（2B）成立：4 正槽 ⟹ excess$=1$（640/640，\textbf{0 反例}）✓✓✓ ＋ 首次得\textbf{新刚性} excess$\le1$ 于全量 23200 ✓✓ ＋ 首次\ \textbf{更正} C-513 之"重叠 $\iff$ 四正"为仅单向 ✗✓**）
**[RESEARCH]**

---

## §0 ★结论（**Gate A 成立 ✓✓✓ ＋ 两项更动 ✓✓／✗✓**）

$$\textbf{设定 ✓}:\ \text{实例 }23200;\quad \mathrm{excess}{:=}\Sigma_{ij}|W_{ij}|-\big|\bigcup_{ij}W_{ij}\big|\ ✓\ \big(\text{重叠计数 ✓}\big)$$
$$\boxed{\textbf{(1) ✓✓✓Gate A（2B）成立}:\ }\text{4 正槽}\ \Longrightarrow\ \mathrm{excess}=\mathbf1\ \text{（640/640，\textbf{0 反例}）}\ ✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{四正}\Rightarrow\exists\,\text{overlap}}\ ✓✓✓\ \text{——\ 即\ \textbf{7 个完全私有 owner-3 witness 不可能}✓✓✓（唐先生 §12 之目标 ✓）}$$
$$\qquad\textbf{（读法 ✓✓）}:\ \text{4 正槽之 }\Sigma|W|{=}7\ \text{而}\ \big|\bigcup W\big|{=}\mathbf6\ \text{恒成立 ✓✓\ \big(\text{即 }\lambda\text{-多重集}\{1,2,2,2\}\text{之 }7\ \text{个 incidence}\ \textbf{必有一处重合}}✓✓\big)$$
$$\boxed{\textbf{(2) ✓✓★新刚性（全量）}:\ }\mathrm{excess}\le\mathbf1\ \text{于\ \textbf{全部} 23200 实例}\ ✓✓\ \text{——\ \textbf{至多一处重叠}}\ ✓✓\ \big(\text{无任何实例 excess}\ge2✓✓\big)$$
$$\qquad\textbf{（强约束 ✓✓）}:\ \text{四槽之 }W\text{-集\ \textbf{不可能有两对以上相重}}\ ⟹\ \bigcup W\ \text{之结构极刚 ✓✓}$$
$$\boxed{\textbf{(3) ✗✓更正 C-513 之"}\iff\textbf{"过强}:\ }\text{实测重叠亦见于\ \textbf{2 正槽}（640）与\ \textbf{3 正槽}（1280）实例}\ ✗✓$$
$$\qquad\Longrightarrow\ \textbf{正确形式（单向 ✓✓）}:\ \boxed{\text{四正}\Rightarrow\text{重叠}}\ ✓✓\ \text{（反向}\ \textbf{不成立} ✗✓\big)$$
$$\qquad\textbf{（C-513 之数字巧合 ✓）}:\ \text{每对共端点槽之非空计数恰 }640\ ⟹\ 4{\times}640{=}2560\ \text{对-实例}\ =\ 640{\,}(2\text{正}){+}1280{\,}(3\text{正}){+}640{\,}(4\text{正})✓\ \text{——\ 前此误读为"全属四正" ✗✓}$$

## §1 分组表（**✓✓**）

| 正槽数 | 实例 | excess$=0$ | excess$=1$ | 完全私有比例 |
|---|---|---|---|---|
| $0$ | $4480$ | $4480$ | $0$ | $100\%$ ✓ |
| $1$ | $6400$ | $6400$ | $0$ | $100\%$ ✓ |
| $2$ | $8480$ | $7840$ | $640$ | $92.5\%$ |
| $3$ | $3200$ | $1920$ | $1280$ | $60\%$ |
| $4$ | $640$ | $\mathbf0$ | $640$ | $\mathbf0\%$ ✓✓✓ |
$$\qquad\Longrightarrow\ \textbf{（对当 ✓✓）}:\ \text{正槽越多，越\ \textbf{必须}重叠};\ \text{唯\ \textbf{4 正槽}\ 为\ \textbf{100\% 必重叠}}\ ✓✓✓$$

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §12（"假设四正 ＋ 全 disjoint ⟹ 矛盾"\ ）\ \textbf{方向完全正确}}✓✓✓\ \text{——\ 本档实测：该反设\ \textbf{0/640} 实例 ✗✓（即\ \textbf{不可能}}✓✓\big)$$
$$\textbf{✓✓}:\ \text{其 §4（"2B 只需证至少一个 overlap，不需证 }|\bigcup W|{=}6\text{"）\ \textbf{正确}}✓✓\ \text{——\ 且本档给更强：excess 恒恰 1 ✓✓}$$
$$\textbf{✓✓}:\ \text{其 §5（完全私有之反证对象形）\ \textbf{正确}}✓✓\ \text{——\ 本档确证其\ \textbf{不可实现}}✓✓✓$$
$$\textbf{✗✓}:\ \text{其 §3 与 C-513 之"四正}\iff\text{共端点 overlap"\ ⟹ \textbf{过强} ✗✓\ \text{（重叠亦见于 2／3 正槽 ✓）}}$$
$$\textbf{✓✓}:\ \text{其 §9（勿把 }T_1,T_2\ \text{当 }C{=}4\ \text{之证明）\ \textbf{完全正确且重要}}✓✓✓\ \text{——\ 须"}C{=}3\ \text{之允许型集}\cap\{T_1,T_2\}{=}\varnothing\text{"或直接禁配 ✓}$$

## §3 汇总裁（**✓✓✓／✗✓**）

| 项 | 值 |
|---|---|
| 4 正槽之 excess | 恒 $1$（640/640）✓✓✓ |
| 全量 excess 上界 | $\le1$ ✓✓（新刚性） |
| "7 完全私有 witness" | **不可能** ✓✓✓ |
| 四正 $\Rightarrow$ overlap | **成立** ✓✓✓ |
| 反向（overlap $\Rightarrow$ 四正） | **不成立** ✗✓ |

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "excess上界" "完全私有不可能" "正槽分组对当"
技术词 excess上界     命中文件数=1    :: ./WITGA2-2026-09-28-gate-A-verified-and-the-excess-one-rigidity.md
技术词 完全私有不可能 命中文件数=1    :: ./WITGA2-2026-09-28-gate-A-verified-and-the-excess-one-rigidity.md
技术词 正槽分组对当 命中文件数=1    :: ./WITGA2-2026-09-28-gate-A-verified-and-the-excess-one-rigidity.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| excess上界 | 0 | 0 | ✓（本档新命名 ✓） |
| 完全私有不可能 | 0 | 0 | ✓（照唐先生 §12 ✓） |
| 正槽分组对当 | 0 | 0 | ✓（本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 下一靶（**照唐先生 §11 ✓**）

$$\textbf{（A ✓✓✓已实证）}:\ \text{4 正}\Rightarrow\text{overlap}\ \text{（0 反例）}\ \text{——\ 余\ \textbf{结构证明}（\textbf{唯一}反设：7 点全 disjoint）✓}$$
$$\textbf{（C ✓下一刀）}:\ w^\ast\ \text{之 }R\text{-型三型完备性（局部有限距离引理 ✓✓）}$$
$$\textbf{（D ✓）}:\ \text{四正 incidence ＋ }w^\ast\ \text{profile}\Rightarrow T_1,T_2\ ✓$$
$$\textbf{（B ✓）}:\ \text{overlap}\Rightarrow1111\ \text{（反向）——\ 本档证其\ \textbf{为假} ✗✓\ ⟹ 须\ \textbf{删除}}✗✓$$
$$\textbf{（禁止 ✗）}:\ \text{owner-计数容量 ✗✓；把 }T_1,T_2\ \text{当 }C{=}4\ \text{之证 ✗✓}$$

## §6 边界（硬 ✓）

- **有限穷举** ✓（23200 实例分组 ＋ excess ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项★Gate A 成立（0 反例 ✓✓✓）** ＋ **一项新刚性（excess ≤1 ✓✓）** ＋ **一项更正（C-513 之 $\iff$ 过强 ✗✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** Gate A 之结构证明已完成 ✗（现为全量实证 ✓）；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
