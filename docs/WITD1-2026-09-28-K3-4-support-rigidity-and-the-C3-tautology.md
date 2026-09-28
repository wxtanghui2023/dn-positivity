# WITD1-2026-09-28 — **C-523：★★$K_3(4)$ 确认 ＋ 差分支撑结构 $(4,4,2)$ \textbf{恒成立}（640/640）✓✓；✗✓\textbf{末步定义校准}："$C{=}3\Rightarrow\neg1111$"\ \textbf{系定义式同义}（$C(O){=}$ max realizable mask），故末步须重述**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 16:04 §6–§7 令 ✓）**：核 **Lemma D1** 之结构（$K_3(4)$ ＋ 支撑）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-522／C-521／C-503，非新案 ✓）**：`WITGC3-…`／`WITGC2-…`／`WITCAP3-…`
D0: 本档对象 ＝ **档案已有**（$x/y/q$／差分支撑；无新数学对象 ✓）
D1: 1（**首次确认 $\{x_0,x_1,q\}$ 为 $K_3(4)$（640/640）✓✓ ＋ 首次得差分支撑结构 $(4,4,2)$ \textbf{恒成立}✓✓ ＋ 首次给 $y$-三角之两镜像型 ＋ 首次\ \textbf{判定} "C{=}3\Rightarrow\neg1111"\ \textbf{系定义式同义}✗✓**）
**[RESEARCH]**

---

## §0 ★结论（**$K_3(4)$ ＋ 支撑刚性 ✓✓；末步需重述 ✗✓**）

$$\boxed{\textbf{(1) ✓✓$\{x_0,x_1,q\}$ 之三角形距离恒 }(4,4,4)}\ ✓✓\ \big(640/640✓\big)\ \text{——\ 即\ \textbf{唐先生 §4 之 }$K_3(4)$\ \textbf{断言成立}}✓✓✓$$
$$\boxed{\textbf{(2) ✓✓差分支撑结构恒 }(\lvert e_1\rvert,\lvert e_2\rvert,\lvert e_1\cap e_2\rvert)=(4,4,2)}\ ✓✓\ \big(640/640✓\big),\quad e_1{=}x_0\oplus x_1,\ e_2{=}x_0\oplus q✓$$
$$\qquad\textbf{（读法 ✓✓✓）}:\ \text{两差分向量之支撑各为 4、交为 2 ⟹ 三列式 }\big(\text{每坐标恰落在两个差分中}\big)\ \text{成立 ✓✓\ \big(\text{唐先生 §7 所求之"坐标支撑结构"}\big)✓✓}$$
$$\qquad\Longrightarrow\ \text{这是\ \textbf{真·坐标层}约束（非距离表）✓✓}\ \text{——\ 且\ \textbf{唯一}型（无分支 ✓）}$$
$$\boxed{\textbf{(3) ✓$y$-三角之两镜像型}}:\ (d(y_1,y_2),d(q,y_1),d(q,y_2))=\big((2,2,4)\ / \ (2,4,2)\big)\ \text{各 }320\ ✓\ \big(\text{互为 }y_1\leftrightarrow y_2\ \text{镜像 ✓}\big)$$
$$\boxed{\textbf{(4) ✗✓★末步定义校准（须写入}}）:\ }\text{按 C-503／C-504，}C(O):=\max\{\lvert\mathrm{mask}\rvert:\text{realizable}\}\ ✓{$$
$$\qquad\Longrightarrow\ \boxed{C(O)=3\iff 1111\notin M(O)}\ \text{——\ \textbf{定义式同义} ✗✓\ \big(\text{非新冲突 ✓}\big)}$$
$$\qquad\Longrightarrow\ \textbf{（故末步须\ \textbf{重述} ✓✓）}:\ \text{真正的内容不是"C{=}3 与骨架冲突"，而是}$$
$$\qquad\qquad\boxed{\text{四正}\ \Longrightarrow\ \mathrm{OrbType}\in\{T_1,T_2\}\ \Longrightarrow\ \mathrm{OrbType}\notin\{O_1,\dots,O_6\}}\ ✓✓$$
$$\qquad\qquad\textbf{（此即 C-512 之实测结论 ✓✓；其\ \textbf{结构证明}仍在 Gate A／B／C 之链上 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{（另一等价说法 ✓）}:\ \text{"}C{=}3\Rightarrow\neg1111\text{"}\ \equiv\ \text{"}\forall O\in\{O_1..O_6\}:1111\notin M(O)\text{"}\ \equiv\ \text{B-lemma}\ ✓✓$$

## §1 汇总裁（**✓✓／✗✓**）

| 项 | 值 |
|---|---|
| $\{x_0,x_1,q\}$ | $K_3(4)$ ✓✓（640/640） |
| 差分支撑 | $(4,4,2)$ ✓✓（唯一型） |
| $y$-三角 | $(2,2,4)$／$(2,4,2)$（镜像各 320）✓ |
| $C(O)$ 之定义 | $=\max\lvert\mathrm{mask}\rvert$ ✓ |
| "$C{=}3\Rightarrow\neg1111$" | **定义式同义** ✗✓ |

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §4（}\{x_0,x_1,q\}\text{ 为边长全 4 之 }K_3\big)\ \textbf{完全正确}}✓✓✓\ \big(640/640✓\big){$$
$$\textbf{✓✓✓}:\ \text{其 §7（"}$K_3(4)$\ \text{之坐标支撑＋}(2,2,4)\ \text{三角之支撑"\ 为最有希望之 P1）\ \textbf{方向正确}}✓✓\ \text{——\ 本档已给 }K_3\ \text{侧之\ \textbf{唯一}支撑型}✓✓$$
$$\textbf{✓✓}:\ \text{其 §1（"}$C{=}3\wedge1111\Rightarrow$ 唯一局部构型"\ ）\ \textbf{成立}}✓✓\ \big(\text{C-522 之型数 }1✓\big){$$
$$\textbf{✗✓}:\ \text{其 §6 之 Lemma D1 形（"}$C{=}3$\ \text{之定义性约束下不存在该六点集"\ ）\ ⟹ \textbf{须重述}}✗✓\ \text{——\ 因 }C(O)\ \text{之定义已含 }1111\ \text{是否可实}✗✓\ \text{（同义反复）}$$
$$\textbf{✓✓}:\ \text{其 §9（"无需新分类、无需 owner-capacity"\ ）\ \textbf{同意}}✓✓$$

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓）}:\ \text{把 }K_3(4)\ \text{之支撑型 }(4,4,2)\ \text{与 }y\text{-三角之支撑型\ \textbf{联立}}⟹\ \text{求六点之联合支撑 constraint}\ ✓✓\ \big(\text{纯坐标层；无分类 ✓}\big)$$
$$\textbf{（靶 2 ✓✓✓）}:\ \text{证明"四正}\Rightarrow\mathrm{OrbType}\in\{T_1,T_2\}\text{"（\textbf{结构}）——\ 即 B-lemma 之结构版 ✓✓}$$
$$\textbf{（靶 3 ✓）}:\ \text{把 }C(O)\ \text{之定义重述为"}$\max$ realizable mask"}, \text{并据 C-503 之 }C(O)\ \text{分布 }\{4{:}2,3{:}12,2{:}28,0{:}16,1{:}20\}\ \text{重排台账 ✓}{$$
$$\textbf{（禁止 ✗）}:\ \text{把同义反复当冲突 ✗✓；owner-计数容量 ✗✓}$$

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "坐标支撑结构" "定义式同义" "联合支撑约束"
技术词 坐标支撑结构 命中文件数=1    :: ./WITD1-2026-09-28-K3-4-support-rigidity-and-the-C3-tautology.md
技术词 定义式同义  命中文件数=1    :: ./WITD1-2026-09-28-K3-4-support-rigidity-and-the-C3-tautology.md
技术词 联合支撑约束 命中文件数=1    :: ./WITD1-2026-09-28-K3-4-support-rigidity-and-the-C3-tautology.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 坐标支撑结构 | 0 | 0 | ✓（照唐先生 §7 ✓） |
| 定义式同义 | 0 | 0 | ✓（本档校准 ✓） |
| 联合支撑约束 | 0 | 0 | ✓（本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（640 实例之三角／支撑 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项★确认（$K_3(4)$ ✓✓）** ＋ **一项★刚性（支撑 $(4,4,2)$ ✓✓）** ＋ **一项✗✓校准（末步同义反复）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** $C{=}3$ 冲突已证 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
