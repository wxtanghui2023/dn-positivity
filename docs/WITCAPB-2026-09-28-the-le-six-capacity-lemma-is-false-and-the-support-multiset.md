# WITCAPB-2026-09-28 — **C-515：✗✓\textbf{更正} —— "全 owner-3 ⟹ $\Sigma|W|\le6$"\ \textbf{不成立}（实为 7，全由 owner-3 实现）；\textbf{新刚性事实}：槽支撑结构恒 $(1^5,2^1)$ ✓✓；并指出"$\exists$ owner$\ge4$"\ \textbf{于一切实例\ \textbf{平凡真}} ⟹ 不能作判别量 ✗✓**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 15:44 令 ✓）**：核 P1-C 之容量论证；**不作路线裁定** ✗。

**已查地图：命中（接续 C-514／C-513／C-512，非新案 ✓）**：`WITONER-…`／`WITDIAG-…`／`WITTYPE-…`
D0: 本档对象 ＝ **档案已有**（$W$/own/支撑；无新数学对象 ✓）
D1: 1（**首次判定"全 owner-3 ⟹ $\Sigma|W|\le6$"\ \textbf{为假}（实为 7，全由 owner-3 实现 ✗✓）＋ 首次得\ \textbf{槽支撑结构恒 }$(1^5,2^1)$\ ✓✓ ＋ 首次指出"$\exists$ owner$\ge4$"\ \textbf{平凡真} ⟹ 不可作判别量 ✗✓**）
**[RESEARCH]**

---

## §0 结论（**✗✓一项更正 ＋ ✓✓一项新事实 ＋ ✗✓一项平凡性**）

$$\textbf{设定 ✓}:\ \text{四正实例 }640;\quad \Sigma_{ij}|W_{ij}|,\ \lvert\bigcup W_{ij}\rvert,\ W\ \text{元素之 }|\mathrm{own}|\ ✓$$
$$\boxed{\textbf{(1) ✗✓"全 owner-3 ⟹ }\Sigma|W|\le6\textbf{"\ \textbf{不成立}}}:\ \text{实测 }\Sigma|W|=\mathbf7\ \big(640/640✓\big);\ \lvert\bigcup W\rvert=\mathbf6\ ✓$$
$$\qquad\textbf{且 ✓}:\ W\ \text{元素之 }|\mathrm{own}|\ \text{分布}=\big\{\mathbf3{:}4480\big\}\ \text{——\ }\textbf{全为 3}✓✓\ \big(\text{因 }W_{ij}\subseteq\mathcal S\ \text{按定义 ✓}\big)$$
$$\qquad\Longrightarrow\ \boxed{\Sigma|W|{=}7\ \text{完全在 owner-3 世界内实现};\ \text{多出之 }1\ \text{来自\ \textbf{重叠}}（\text{非来自 owner}\ge4\ \text{之点 ✗✓}\big)}$$
$$\qquad\Longrightarrow\ \textbf{（故 P1-C 之容量链\ \textbf{断裂} ✗✓）}:\ \text{"}7>6\Rightarrow\exists\ \text{owner}\ge4\text{"}\ \textbf{不成立} ✗✓\ \text{——\ 该 }+1\ \text{由共端点重叠承担 ✓}$$
$$\boxed{\textbf{(2) ✓✓★新刚性事实（槽支撑结构）}:\ }\text{定义槽支撑 }E(w){:=}\{ij:w\in W_{ij}\}\ ✓;\ \text{则各实例之 }|E(w)|\ \text{多重集\ \textbf{恒为}}$$
$$\qquad\boxed{\big(1^5,\ 2^1\big)}\ ✓✓\ \big(640/640\ ✓\big)\ \text{——\ \textbf{恰一个 }双支撑 witness（即重叠点 }\omega^\ast\big)、\text{五个单支撑}✓✓$$
$$\qquad\Longrightarrow\ \text{与 P1-A 完全相容 ✓✓（}|E(w)|\le2\ ✓;\ \text{双支撑者必为共端点对 ✓）}$$
$$\boxed{\textbf{(3) ✗✓"\exists w:|\mathrm{own}(w)|\ge4"\ \textbf{于一切实例平凡真}}:\ }\text{任何实例之}\ B=N_2(x)\cap N_2(p)\cap N_2(q)\ \text{之点\ \textbf{皆 }owner\ 4\text{–}5\ ✓\ \big(\text{C-509 ✓}\big)}$$
$$\qquad\Longrightarrow\ \textbf{（故不可作判别量 ✗✓）}:\ \text{唐先生 §7–§8 之目标"四正}\Rightarrow\exists\ \text{owner}\ge4"\ \textbf{平凡真} ⟹\ \text{不能区分 }C{=}3\ \text{与 }C{=}4\ ✗✓$$
$$\qquad\textbf{（须\textbf{锐化}）}✓:\ \text{只能形如\ \textbf{某个指定的点被迫}\ \mathrm{owner}\ge4\ ✓\ \text{或\ \textbf{witness 被迫非-owner-3}（但 }W\subseteq\mathcal S\text{，⟹ 不可能 ✗✓}\big)}$$

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生之 P1-A 形式化（}E(w)\subseteq\text{一条 }C_4\ \text{边；}|E(w)|\le2\big)\ \textbf{成立}✓✓\ \text{——\ 本档实测 }(1^5,2^1)\ \text{为其\ \textbf{精确强化}}✓✓$$
$$\textbf{✗✓}:\ \text{其 "若所有 witness 皆 owner-3，则 }\Sigma|W|\le6"\ ⟹ \textbf{为假} ✗✓\ \big(\text{实为 7 ✓}\big)\ \text{——\ 因 }W\subseteq\mathcal S\ \text{恒真 ⟹ "全 owner-3"\ 不是限制 ✗✓}$$
$$\textbf{✗✓}:\ \text{其 §7–§8（四正}\Rightarrow\exists\ \text{owner}\ge4\big)\ ⟹ \textbf{平凡真} ✗✓\ \big(\text{}B\ \text{之点恒 owner }4\text{–}5✓\big)$$
$$\textbf{✓✓}:\ \text{其 §"P1-B 压缩成 3-owner profile lemma"\ \textbf{方向仍有效}}✓✓\ \text{——\ 本档未涉 P1-B ✓，其局部几何允许型之论证\ \textbf{不受本更正影响}✓✓}$$
$$\textbf{✓✓}:\ \text{其 §"P1-C 当作备用"\ 与"先打容量矛盾"\ 之\ \textbf{判断需修正}}✗✓:\ \text{容量矛盾\ \textbf{不存在}}✗✓\ \text{（唯一 +1 由重叠承担 ✓）}$$

## §2 汇总裁（**✗✓／✓✓**）

| 项 | 值 |
|---|---|
| $\Sigma\lvert W\rvert$ | $7$（640/640）✗✓ |
| $\lvert\bigcup W\rvert$ | $6$ ✓ |
| $W$ 元素之 $\lvert\mathrm{own}\rvert$ | **全 3** ✓✓ |
| 槽支撑多重集 | $\big(1^5,2^1\big)$ ✓✓（刚性） |
| "$\le6$" 引理 | **假** ✗✓ |
| "$\exists$ owner$\ge4$" | **平凡真** ✗✓ |

## §3 后续（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓）}:\ \text{唯一仍可行之路线}:\ \textbf{类型级有限命题}（\text{C-512}:\ \text{四正}\Rightarrow\text{type}\in\{T_1,T_2\}\big)\ ✓\ \text{——\ 其结构证明须用 16-向量等式型，非 owner-计数 ✗✓}$$
$$\textbf{（靶 2 ✓✓备用）}:\ \text{P1-B（3-owner profile lemma）\ 仍独立有效 ✓（本档未涉及 ✓）}$$
$$\textbf{（靶 3 ✓本档新增）}:\ \text{槽支撑 }(1^5,2^1)\ \text{之\ \textbf{机制}（为何恰一个双支撑 ✓）——\ 一个有希望的\ \textbf{可证}小命题 ✓✓}$$
$$\textbf{（禁止 ✗）}:\ \text{再走 owner-计数容量矛盾 ✗✓；把"C=3}\Rightarrow C\ge4"\ \text{当已证 ✗}$$

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "支撑多重集" "容量引理失效" "平凡真判别量"
技术词 支撑多重集  命中文件数=1    :: ./WITCAPB-2026-09-28-the-le-six-capacity-lemma-is-false-and-the-support-multiset.md
技术词 容量引理失效 命中文件数=1    :: ./WITCAPB-2026-09-28-the-le-six-capacity-lemma-is-false-and-the-support-multiset.md
技术词 平凡真判别量 命中文件数=1    :: ./WITCAPB-2026-09-28-the-le-six-capacity-lemma-is-false-and-the-support-multiset.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 支撑多重集 | 0 | 0 | ✓（本档新命名 ✓） |
| 容量引理失效 | 0 | 0 | ✓（本档更正 ✓） |
| 平凡真判别量 | 0 | 0 | ✓（本档更正 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（640 四正实例之 $\Sigma|W|$／$\bigcup$／own／支撑 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项更正（"$\le6$" 为假 ✗✓）** ＋ **一项新刚性事实（$(1^5,2^1)$ ✓✓）** ＋ **一项平凡性（✗✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** $C{=}3\Rightarrow C\ge4$ 已证 ✗（本档证其**不可由容量route得到 ✗✓**）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
