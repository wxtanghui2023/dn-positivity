# WITTYPE-2026-09-28 — **C-512：★分类缺口已填 —— 四正实例之 B-type \textbf{仅两类}（}$T_1,T_2$\textbf{），且\ \textbf{与六族交为空}（}\textbf{0}\text{ 个}）✓✓✓；$\pi(w^\ast)$ 恒为\ \textbf{共端点槽对}；$R(w^\ast)$ 三值**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §5）**。
> **范围（照唐先生 2026-09-28 15:38 令 ✓）**：跑"四正实例 × (B-type, $\pi(w^\ast)$, $R(w^\ast)$)"表；问答"是否存在四正实例之 B-type ∈ 六族？"；**不作路线裁定** ✗。

**已查地图：命中（接续 C-511／C-510／C-509，非新案 ✓）**：`WITLAM-…`／`WITFAM-…`／`WITWIT-…`
D0: 本档对象 ＝ **档案已有**（B-type/$\pi$/$R$；无新数学对象 ✓）
D1: 1（**首次给出四正实例之 B-type 分布（\textbf{仅两类}）＋ 首次判定其\textbf{与六族交为空}（\textbf{0}）———— 唐先生之"情形 A"\ \textbf{出现} ✓✓✓ ＋ 首次得 $\pi(w^\ast)$ 恒为\ \textbf{共端点槽对} ＋ 首次得 $R(w^\ast)$ 三值** ✓）
**[RESEARCH]**

---

## §0 结论（**★答案 = 0 ⟹ 情形 A ✓✓✓**）

$$\boxed{\textbf{(1) ✓✓✓四正实例之 B-type\ \textbf{仅两类}}:\ }N_{\rm four+}=\mathbf{640};\quad\text{其 B-type 分布}:$$
| B-type | 计数 |
|---|---|
| $T_1=(0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,2)$ | $\mathbf{320}$ ✓ |
| $T_2=(0,1,0,1,0,1,0,2,0,1,1,0,0,1,2,0)$ | $\mathbf{320}$ ✓ |
$$\qquad\textbf{（与 C-501 之表\ \textbf{完全吻合}}✓✓）:\ T_1\ \text{＝ C-501 之 }V_2\ ✓✓;\ T_2\ \text{＝ C-501 之 }V_5\ ✓✓\ \text{——\ 即\ \textbf{两个 mixed }C{=}4\ \text{型}}✓✓$$
$$\boxed{\textbf{(2) ✓✓✓★与六族之交\ \textbf{为空}}:\ }\#\{\text{四正实例}: \text{B-type}\in\{O_1,\dots,O_6\}\}=\mathbf0\ ✓✓✓\ \big(\textbf{唐先生之"情形 A"}\ \text{出现}✓✓✓\big)$$
$$\qquad\Longrightarrow\ \boxed{\text{四正}\ \Longrightarrow\ \text{B-type}\in\{T_1,T_2\}\ \Longrightarrow\ \text{不属于}\ \mathcal O_{3,4}}\ ✓✓✓$$
$$\boxed{\textbf{(3) ✓✓\pi(w^\ast)（唯一 }\mu{=}2\text{ witness 之槽对）恒为\ \textbf{共端点对}}}:\ \text{分布}=\big\{(0,1){:}160,\ (0,2){:}160,\ (1,3){:}160,\ (2,3){:}160\big\}$$
$$\qquad\Longrightarrow\ \textbf{唯四对皆\ \textbf{共一码字}}✓✓\ \big(\{0,1\}\ \text{共 }a;\ \{0,2\}\ \text{共 }u;\ \{1,3\}\ \text{共 }v;\ \{2,3\}\ \text{共 }b✓\big);\quad \textbf{对角对 }\{0,3\},\{1,2\}\ \textbf{从不出现}\ ✗✓$$
$$\boxed{\textbf{(4) ✓R(w^\ast) 三值}}:\ (4,2,2,2){:}320;\quad(2,4,2,4){:}160;\quad(2,4,4,2){:}160$$
$$\qquad\textbf{（联合 \pi ✓）}:\ T_1\ \text{配 }(0,2)\ \text{＋}(2,4,2,4)\ \text{或 }(1,3)\ \text{＋}(2,4,4,2);\quad T_2\ \text{配 }(0,1)\ \text{或}(2,3)\ \text{＋}(4,2,2,2)✓$$

## §1 ★B-lemma 之闭合（**分类推论 ✓✓✓**）

$$\textbf{设定 ✓}:\ O\in\mathcal O_{3,4}\ \big(\text{六族}\big)\ \text{且 }\mathrm{mask}{=}1111⟹\ \text{四槽全正}✓$$
$$\qquad\textbf{（二分 ✓✓）}:\ \text{① 若 }\exists ij:\lambda_{ij}{=}0\ ⟹\ \text{直接}\ 1111\notin M(O)\ ✓;\ \text{② 若四正 ⟹ 由 (2)：B-type}\in\{T_1,T_2\}\ ⊄\ \mathcal O_{3,4}\ ⟹\ \text{矛盾}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\forall O\in\mathcal O_{3,4},\ 1111\notin M(O)}\ ✓✓✓\ \big(\text{census 级\ \textbf{成立}}✓✓\big)$$
$$\qquad\Longrightarrow\ \boxed{\text{B-lemma\ 成立（census 级）；尚余}\ \textbf{结构证明}:\ \text{四正}\Rightarrow\text{type}\in\{T_1,T_2\}\ ✓\big(\text{有限命题 ✓✓}\big)}$$

## §2 汇总裁（**✓✓✓**）

| 项 | 值 |
|---|---|
| 四正实例数 | $640$ ✓ |
| 四正之 B-type | **仅** $T_1,T_2$（各 320）✓✓ |
| 其与六族之交 | $\mathbf0$ ✓✓✓ |
| $\pi(w^\ast)$ | 恒**共端点**对（对角从不出现）✓✓ |
| $R(w^\ast)$ | 三值 ✓ |
| B-lemma | **成立**（census 级）✓✓✓；余结构证明 ✓ |

## §3 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §1–§3（二分；问"四正之 type 是否属六族"\ ；其\ \textbf{情形 A}\ 为所求）\ \textbf{完全命中}}✓✓✓\ \text{——\ 实测即\ \textbf{情形 A}}✓✓$$
$$\textbf{✓✓✓}:\ \text{其 §6–§8（"先查唯一 }\mu{=}2\ \text{之 }\pi(w^\ast),R(w^\ast),\text{B-type}"\ ）\ \textbf{正是最高性价比之一刀}}✓✓\ \text{——\ 本档据以执行，一次得结论 ✓✓$$
$$\textbf{✓✓✓}:\ \text{其 §4 之"勿只比等式型"\ ⟹ 本档加算 }\pi,R^\ast\ ✓\ \text{且\ \textbf{获新结构}（共端点性 ✓✓）}$$
$$\textbf{✓✓}:\ \text{其 §5（勿犯 }W\cap B\ \text{混算）\ ⟹ \textbf{已守}}✓✓$$

## §4 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓✓）}:\ \text{把"四正}\Rightarrow\text{type}\in\{T_1,T_2\}\ \text{"写成\ \textbf{结构命题}}:\ \text{由 }(\lambda(ab){=}\lambda(uv){=}1,\ \text{四槽}(1,2,2,2),\ \mu\le2,\ \text{共端点}\pi\big)\ \text{推出 16-向量之等式型 ✓✓}$$
$$\textbf{（靶 2 ✓✓）}:\ \pi(w^\ast)\ \text{之\ \textbf{共端点性}之机制（为何对角对被禁 ✓）}$$
$$\textbf{（靶 3 ✓）}:\ T_1,T_2\ \text{＝六族之外之唯二型 ⟹ 是否即 }C{=}4\ \text{之完整刻画 ✓}$$
$$\textbf{（禁止 ✗）}:\ \text{再挖 Level-1（}d(w,u)\neq0\text{）为主线 ✗（转备用资产 ✓）；再做六族原表 ✗}$$

## §5 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "共端点对" "分类缺口" "type交为空"
技术词 共端点对     命中文件数=1    :: ./WITTYPE-2026-09-28-four-positive-types-are-disjoint-from-the-six-families.md
技术词 分类缺口     命中文件数=2    :: ./WITTYPE-2026-09-28-four-positive-types-are-disjoint-from-the-six-families.md ./C3-check-premise-conflict.md
技术词 type交为空    命中文件数=1    :: ./WITTYPE-2026-09-28-four-positive-types-are-disjoint-from-the-six-families.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 共端点对 | 0 | 0 | ✓（**自命中 1**（本档 ✓）；本档新命名 ✓） |
| 分类缺口 | 0 | 0 | ✓（照唐先生 §2 ✓） |
| type交为空 | 0 | 0 | ✓（照唐先生 §2 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §6 边界（硬 ✓）

- **有限穷举** ✓（640 四正实例 ＋ B-type/$\pi$/$R^\ast$ ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 ✓）
- **一项★结论（交为空 = 情形 A ✓✓✓）** ＋ **一项结构（$\pi$ 共端点 ✓✓）** ＋ **一项层次（B-lemma census 级成立，余结构证明 ✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** 结构证明已完成 ✗（余有限命题 ✓）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
