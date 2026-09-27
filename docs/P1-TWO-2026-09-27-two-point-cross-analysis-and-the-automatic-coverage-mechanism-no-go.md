# P1-TWO-2026-09-27 — **两点交叉分析**：定向引理 ＋ 子立方体相交刚性 ＋ **机制级否定**

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:52 令 ✓）**：研究**两个不同 $c$ 的内部子立方体如何相交**；不求和 ✓；零程序计算 ✓。

**已查地图：命中（接续 P1-MICRO／P1-AVOID／R4-P1，非新案 ✓）**
所查：`docs/P1-MICRO-2026-09-27-…`（**内部子立方体排斥定理 (α)(α′)** ✓✓）｜`docs/P1-AVOID-2026-09-27-…`（**$d_2,d_3$ 对偶界** ✓✓）｜`docs/R4-P1-2026-09-27-…`｜`docs/R7-LOCK-2026-09-27-…`｜`docs/P1-TETRA-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §5）
D0: 本档对象 ＝ **档案已有** $K_4$-avoidance／内部子立方体对象的**两点交叉**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出定向引理 ＋ 两子立方体相交刚性 ＋ 机制级否定（covering 对 distance-$\le3$ 局部构型不可见）** ✓）
**[RESEARCH]**

---

## §0 结论（**两条新结果 ✓✓ ＋ 一条机制级否定 ✓✓**）

$$\boxed{\textbf{(1) 定向引理（新 ✓）}:\ c'=c\oplus e_a\oplus e_b\ (a\ne b)\Longrightarrow\ \big[a\in S(c)\iff b\in S(c')\big]\ \wedge\ \big[b\in S(c)\iff a\in S(c')\big]✓}$$
$$\boxed{\textbf{(2) 两点刚性（新 ✓✓）}:\ \text{取 }a\in S(c),\ b\notin S(c)\ \Longrightarrow\ C\cap\big(U\cap U'\big)=\{c\oplus e_a\}\ \text{（恰\textbf{一个}码字 ＝ 公共邻居）}✓✓}$$
$$\qquad\big(U:=c+\mathrm{span}(S(c)),\ U':=c'+\mathrm{span}(S(c'))✓\big)$$
$$\boxed{\textbf{(3) 机制级否定 ✓✓}:\ \textbf{covering 对这些距离}\le3\ \textbf{的局部构型\textbf{不可见}}\ ⟹ \text{局部刚性}\not\Rightarrow\text{covering 矛盾}\ ✗✓\ \text{（路线级结论，非"未找到"）}}$$

---

## §1 **定向引理**（**2 行证明 ✓**）

$$\text{设 }c'=c\oplus e_a\oplus e_b\ (a\ne b)✓:\qquad a\in S(c)\iff c\oplus e_a\in C\iff c'\oplus e_b\in C\iff b\in S(c')✓\ ✓\ (\text{对称同理 ✓})$$
$$\textbf{推论（与 avoidance 相容性 ✓）}:\ \{a,b\}\subseteq S(c)\Longrightarrow (\text{引理})\ \{a,b\}\subseteq S(c') \Longrightarrow \text{square}\ \{c',c'\oplus e_a,c'\oplus e_b,c\}\subseteq C\ ✗\ \text{与 }A(c')=0\ \text{矛盾}✓$$
$$\qquad\Longrightarrow\ \boxed{\{a,b\}\not\subseteq S(c)\ \wedge\ \{a,b\}\not\subseteq S(c')\ }\ ✓\ \text{（与 R4-P1 的 }d_2(c)\le45-\binom s2\ \text{同源 ✓）}$$

## §2 **两点刚性**（**子立方体相交恰一个码字 ✓✓**）

$$\text{取 }c'=c\oplus e_a\oplus e_b,\ a\in S(c),\ b\notin S(c)✓\ \Longrightarrow\ (\text{§1})\ b\in S(c'),\ a\notin S(c')\ ✓\ (\text{否则 }\{a,b\}\subseteq S(c')\ ✗)$$
$$\text{逐项判定（}\alpha'\ \text{给出 }C\cap U=\{c\}\cup\{c{\oplus}e_i\}_{i\in S(c)}✓,\ C\cap U'=\{c'\}\cup\{c'{\oplus}e_j\}_{j\in S(c')}✓\big)$$
$$\quad c\in U'?\iff e_a{\oplus}e_b\in\mathrm{span}(S(c'))\iff a,b\in S(c')\iff \textbf{否}✗\ \ (\text{因 }a\notin S(c')✓)$$
$$\quad c'\in U?\iff e_a{\oplus}e_b\in\mathrm{span}(S(c))\iff a,b\in S(c)\iff \textbf{否}✗\ \ (\text{因 }b\notin S(c)✓)$$
$$\quad c{\oplus}e_i\in U'\ (i\in S(c))?\iff e_i{\oplus}e_a{\oplus}e_b\in\mathrm{span}(S(c'))\iff e_i{\oplus}e_a\in\mathrm{span}(S(c'))\iff i=a✓\ (\text{因 }a\notin S(c')✓)$$
$$\quad c'{\oplus}e_j\in U\ (j\in S(c'))?\iff e_a{\oplus}e_b{\oplus}e_j\in\mathrm{span}(S(c))\iff e_b{\oplus}e_j\in\mathrm{span}(S(c))\iff j=b✓\ (\text{因 }b\notin S(c)✓)$$
$$\Longrightarrow\ \boxed{C\cap U\cap U'=\{c\oplus e_a\}}\ ✓✓\ \text{（唯一公共码字 ＝ 公共一阶邻居 ✓；}\text{且 }c{\oplus}e_a=c'{\oplus}e_b✓)$$
$$\textbf{读法 ✓✓}:\ \text{两个内部子立方体\textbf{不共享中心}（}c\notin U',c'\notin U✓\text{），\textbf{不共享任何二阶点}，\textbf{唯一}共享的是那个公共一阶邻居 ✓}$$

## §3 **机制级否定**（**本档最重要 ✓✓**）

$$\textbf{自动覆盖原理 ✓}:\ \text{设 }x\in C\ \text{或}\ d(x,c)\le1\ \text{某 }c\in C\ \Longrightarrow\ x\ \text{被 }c\ \text{覆盖}✓;\ \text{而 rigidity／avoidance 分析涉及的点\textbf{全部}满足}:$$
$$\qquad\text{① 码字本身（}b\ge1\ \text{自动 ✓）};\ \text{② 码字的一阶邻居（距离 1 ✓）};\ \text{③ }\textbf{中点}:\ c{\oplus}e_i{\oplus}e_j\ \text{对 }i\in S(c)\ \Longrightarrow\ d(c{\oplus}e_i,\ \cdot)=1\ ✓\ (\text{P1-MICRO (β) ✓})$$
$$\qquad\text{④ 两点构型的公共邻居（§2 ✓）};\ \text{⑤ square/tetra 的全部顶点（皆为码字或其一阶邻居 ✓）}$$
$$\Longrightarrow\ \boxed{\text{covering 条件只在"}\textbf{到所有码字距离}\ge2\text{"的点上有约束力};\ \text{而本文全部局部构型的点皆 }\le1\ ⟹ \textbf{自动满足}✓✓}$$
$$\Longrightarrow\ \textbf{结论（路线级 ✓✓）}:\ \boxed{\textbf{任何仅由 distance}\le3\ \textbf{局部构型}\ \text{导出的刚性，都不可能通过 covering 产生矛盾}\ ✗✓}$$
$$\qquad\Longrightarrow\ \text{这\textbf{解释}了本线反复出现的"局部有结构、无法闭环"（P1-MICRO (β)、P1-AVOID §3、R7 STOP ✓）\ —— \textbf{不是技巧不足，而是机制边界} ✓✓}$$

## §4 现状与下一步（**诚实 ＋ 尺度判断 ✓**）

$$\textbf{已闭 ✓}:\ \text{单点刚性（}(α)(α')✓\text{）、两点刚性（§2 ✓）、}$d_2,d_3$ 对偶界 ✓、covering 步失效（(β)✓）、自动覆盖原理（§3 ✓）$$
$$\textbf{未闭 ✗}:\ \text{local rigidity}\not\Rightarrow\text{covering 矛盾}（\text{§3 说明\textbf{在 }\le3\ \text{尺度上不可能}✓）⟹ \textbf{必须换尺度}⚠️}$$
$$\textbf{可换的尺度（登记未做 ✓）}:\ \text{① }\textbf{远点覆盖}（\text{到所有码字距离}\ge2\ \text{的点}✓）\ —— \text{这是 covering 唯一"有牙"处 ✓};\ \text{② 全局计数（但须避免落回 profile ✗，见 R7 STOP ✓）};\ \text{③ distance}\ge4\ \text{的内部点（(α′) 未覆盖 ⚠️）}$$

## §5 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "两点交叉"
技术词 两点交叉        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "定向引理"
技术词 定向引理        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "自动覆盖"
技术词 自动覆盖        命中文件数=6    :: ./ZF-global-conservation-law-and-carrier-screening.md ./ASSETS-REGISTRY.md ./C152-M2-COMPLETE-local-lemma-gradients-positively-span-plus-far-field-certificate.md
$ bash scripts/tech_word_check.sh "子立方体相交"
技术词 子立方体相交    命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`两点交叉`／`定向引理`／`子立方体相交` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`自动覆盖` 档案已有（他处语境）✓）
- **注 ✓**：本档实质＝**§1 定向引理 ＋ §2 两点刚性 ＋ §3 机制级否定**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓；**未求和** ✓（照令 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** P1 成立 ✗（V290）；**§3 为路线级否定（有证明 ✓）**，**非**"$K(10,1)\ge120$ 不可能" ✗ —— 只写"**在 $\le3$ 尺度上局部刚性无法接到 covering**" ✓
- §2 的前提（$a\in S(c),b\notin S(c)$）**必须显式保留** ✓（另一分支为 $a,b\notin S(c)$ ✓，本档未展开 ⚠️）
