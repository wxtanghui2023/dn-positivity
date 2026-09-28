# WITLAM-2026-09-28 — **C-511：四正（mask=1111）实例\ \textbf{确实存在}（640 个）且\ \textbf{极刚性}：$\Sigma\lambda{\equiv}\mathbf7$ ✓✓、四槽 λ-多重集恒为 $(1,2,2,2)$ ✓✓、$\lambda(ab){=}\lambda(uv){=}\mathbf1$ ✓✓、$|W_{ij}|{=}\lambda_{ij}$、$\mu(w)\le\mathbf2$ ✓✓（\textbf{唐先生 §6 之 }$\mu\le2$\textbf{ 证实}）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §5）**。
> **范围（照唐先生 2026-09-28 15:35 令 ✓）**：在**四正反设**下算 $\mu$／R-型聚合；**不作路线裁定** ✗。

**已查地图：命中（接续 C-510／C-509／C-508，非新案 ✓）**：`WITFAM-…`／`WITWIT-…`／`WITK4-…`
D0: 本档对象 ＝ **档案已有**（$W_{ij}$/$\lambda$/incidence；无新数学对象 ✓）
D1: 1（**首次证实四正实例存在（640）＋ 首次得 $\Sigma\lambda{\equiv}7$、四槽 λ-多重集恒 $(1,2,2,2)$、$\lambda(ab){=}\lambda(uv){=}1$ ＋ 首次得 $\mu(w)\le2$（恰一个 $\mu{=}2$、五个 $\mu{=}1$）＋ 首次\ \textbf{更正}唐先生之 $\Sigma|W|{=}8$（实为 $7$ ✗✓）** ✓）
**[RESEARCH]**

---

## §0 结论（**四正可实现 ✓✗ ＋ 四项刚性 ✓✓**）

$$\textbf{（先纠一处理论前提 ✓✗）}:\ W_{ij}\subseteq\mathcal S\ \text{（}|\mathrm{own}|{=}3✓\big);\ \text{而 }B\ \text{之点 }|\mathrm{own}|\ge4\ ⟹ \boxed{W\cap B=\varnothing}\ ✓✓\ \text{——\ 故 incidence }\mu\ \text{须在 }\bigcup W_{ij}\ \text{上算（非在 }B\ \text{上 ✗✓}\big)$$
$$\boxed{\textbf{(1) ✓四正（mask }{=}1111\textbf{）实例\ \textbf{确实存在}}:\ }\text{全量 }\mathbf{640}\ \text{个}\ ✓\ \big(\lambda(ab){=}\lambda(uv){=}1\ \text{且四槽全正 ✓}\big)\ \text{——\ 即四正\ \textbf{并非不可能}}✓✗$$
$$\qquad\Longrightarrow\ \text{唐先生 §2 之判断\ \textbf{成立}}✓✓:\ \text{不能再拿六族作 case split；四正型须\ \textbf{另立} ✓}$$
$$\boxed{\textbf{(2) ✓✓四项刚性（四正情形下）}:\ }$$
| 量 | 值 | 备注 |
|---|---|---|
| $\Sigma_{ij}\lambda_{ij}$ | $\mathbf7$ ✓✓（640/640） | **刚性**（唐先生 §5 猜 8 ⟹ **实为 7** ✗✓） |
| 四槽 λ-多重集 | 恒 $\{1,2,2,2\}$ ✓✓（分布 $(2,1,2,2){:}162$、$(2,2,2,1){:}158$、$(1,2,2,2){:}158$、$(2,2,1,2){:}162$ ✓） | 恰一个 $1$、三个 $2$ |
| $\lambda(ab)$、$\lambda(uv)$ | $\mathbf1$、$\mathbf1$ ✓✓（640/640） | 与 $K_4$ 之 $(1,1,1,2,2,2)$ 相容 ⟹ 三个 $1$ ＝ $ab,uv$ ＋ 一个 cross ✓✓ |
| $\lvert W_{ij}\rvert$ | $=\lambda_{ij}$ ✓（$(1,2,2,2)$ ✓） | 与 C-510 一致 ✓ |
$$\boxed{\textbf{(3) ✓✓\mu(w)\le\mathbf2（唐先生 §6 之猜想\ \textbf{证实}}）}:\ \mu(w){:=}\#\{ij:w\in W_{ij}\}\ \text{之分布 }=\big\{\mathbf2{:}640,\ 1{:}3200\big\}\ ✓✓\ \big(\text{最大 }\mu{=}\mathbf2✓\big)$$
$$\qquad\Longrightarrow\ \textbf{（刚性 incidence ✓✓）}:\ \text{每实例 }\lvert\bigcup W_{ij}\rvert{=}\mathbf6\ \text{（非 7 ✗）}\ ⟹ \text{恰\ \textbf{一个} }w\ \text{之 }\mu{=}2\ \text{、五个 }\mu{=}1\ ✓✓\ \big(\Sigma\mu{=}7{=}\Sigma\lambda✓✓\big)$$
$$\qquad\textbf{（读法 ✓✓）}:\ \text{四正型之 witness\ \textbf{几乎两两不交}（仅一对重合）——\ 一个非常刚性的 incidence 结构 ✓✓}$$

## §1 汇总裁（**✓✓／✗**）

| 项 | 值 |
|---|---|
| 四正实例数 | $640$ ✓ |
| $\Sigma\lambda$ | $7$ ✓✓ |
| 四槽 λ-多重集 | $\{1,2,2,2\}$ ✓✓ |
| $\lambda(ab),\lambda(uv)$ | $1,1$ ✓✓ |
| $\lvert\bigcup W\rvert$ | $6$ ✓✓ |
| $\mu$ 分布 | $\{2{:}640,1{:}3200\}$ ✓✓ |
| $\mu\le2$ | **真** ✓✓ |
| $W\cap B$ | $\varnothing$ ✓✗（纠前提 ✓） |

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生 §1–§2（四正 ⟹ }K_4\ \text{＋ λ-多重集 }(1,1,1,2,2,2)\ \text{＋ 须另立潜在型）\ \textbf{成立}}✓✓\ \text{——\ 且本档证四正\ \textbf{可实现}（}640✓\big)⟹ \text{其"不拿六族作 split"\ 之判断\ \textbf{正确}}✓✓$$
$$\textbf{✗✓}:\ \text{其 §5 之 }\Sigma\lvert W_{ij}\rvert{=}8\ ⟹ \textbf{实为 7} ✗✓\ \big(\text{因 }\lambda(ab){=}\lambda(uv){=}1\ \text{吃掉一个 }2✓\big)$$
$$\textbf{✓✓✓}:\ \text{其 §6–§7（}\mu(w)\le2\ \text{之猜想；}\bar\mu{=}2\big)\ ⟹ \textbf{实测 }\mu\le2\ \textbf{成立}✓✓\ \text{（但 }\bar\mu\ \text{为 }7/6\ \text{非 }2\ ✗✓\big)$$
$$\textbf{✓✓}:\ \text{其 §3–§4（}\epsilon{=}\lambda{-}1\ \text{之二值化；找行列约束）\ \textbf{方向正确}}✓✓\ \text{——\ 且本档已给出\ \textbf{行和级}之刚性（}\Sigma\lambda{\equiv}7\ ✓✓\big)$$
$$\textbf{✓✓}:\ \text{其 §9 之最终证书形态}\ \textbf{仍适用}✓✓\ \text{——\ 唯层次为\ \textbf{四正型 ∩ 六族}\ ✗（两者\ \textbf{互斥} ✓✓，故 B-lemma 实为：六族之 }\lambda\text{-型\ \textbf{必含零}}✓✓\big)$$

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓✓）}:\ \text{B-lemma 之\ \textbf{最终形式}}:\ \boxed{\forall O\in\mathcal O_{3,4},\ \exists ij:\lambda_{ij}{=}0}\ ✓✓\ \text{——\ 现有之\ \textbf{两面证据}}:\ \text{① 六族 λ-型恒含零（C-510 ✓✓）};\ \text{② 四正型之刚性（本档：}\Sigma{=}7,\ {1,2,2,2},\ \mu\le2✓✓\big)\ ⟹\ \text{若能证}\ \textbf{六族之 16-向量等式型与四正型之刚性不相容} ⟹\ \text{闭合 ✓✓}$$
$$\textbf{（靶 2 ✓✓）}:\ \text{四正型之 }\Sigma\lambda{\equiv}7\ \text{与 }\lambda(ab){=}\lambda(uv){=}1\ \text{之\ \textbf{机制解释}}（可否由 }W\ \text{之 incidence 直接推出 ✓）$$
$$\textbf{（靶 3 ✓）}:\ \text{R-型聚合（本档已算：每实例 6 点，R-型分布每实例不同 ✗，未见}\ \text{统一聚合}✗\big)$$
$$\textbf{（禁止 ✗）}:\ \text{再做六族完整原表 ✗};\ \text{把 }W\ \text{与 }B\ \text{混算 ✗✓}$$

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "四正型" "incidence守恒" "λ层刚性"
技术词 四正型        命中文件数=1    :: ./WITLAM-2026-09-28-four-positive-rigidity-and-the-mu-le-two-fact.md
技术词 incidence守恒  命中文件数=1    :: ./WITLAM-2026-09-28-four-positive-rigidity-and-the-mu-le-two-fact.md
技术词 λ层刚性      命中文件数=1    :: ./WITLAM-2026-09-28-four-positive-rigidity-and-the-mu-le-two-fact.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 四正型 | 0 | 0 | ✓（**自命中 1**（本档 ✓）；本档新命名 ✓） |
| incidence守恒 | 0 | 0 | ✓（照唐先生 §5–§6 ✓） |
| λ层刚性 | 0 | 0 | ✓（本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（四正实例 640 ＋ $W$/$\mu$ 全量 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项前提纠正（$W\cap B{=}\varnothing$ ✓✗）** ＋ **四项刚性（$\Sigma\lambda{=}7$／$\{1,2,2,2\}$／$\lambda(ab){=}\lambda(uv){=}1$／$\mu\le2$ ✓✓）** ＋ **一项更正（$\Sigma|W|$：$8\to7$ ✗✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** B-lemma 已证 ✗；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
