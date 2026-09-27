# P1-G2-2026-09-27 — **$G_2$／刚性耦合**：勘误（旧结论错 ✗）＋ 见证者分解 ＋ **逃逸定位**（锐化后的单一问题）

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。**范围（照唐先生 23:06 令 ✓）**：固定 $c$、weight-4 block 是否迫使额外 $G_2(C)$ 结构／是否消耗不可重复资源；**纯局部、零计算** ✓。

**已查地图：命中（接续 P1-D4／P1-D3b／P1-MICRO，非新案 ✓）**
`docs/P1-D4-2026-09-27-…`（**球面覆盖恒等式／两类来源排除** ✓✓）｜`docs/P1-D3b-2026-09-27-…`（**共享判据／§2 star 断言** ⚠️）｜`docs/P1-D3-2026-09-27-…`（**被迫高层码字定理** ✓✓）｜`docs/P1-MICRO-2026-09-27-…`（**$(\alpha)(\alpha')$ 排斥定理** ✓✓）｜`docs/R7-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** forced-$d_4$／$G_2$ 结构对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出见证者分解（外见证 1 对 1）＋ 逃逸的精确位置 ＋ 锐化后的单一问题 P1-D4b** ✓）
**[RESEARCH]**

---

## §0 结论（**一处勘误 ✗✓｜一条分解 ✓｜一处逃逸定位 ✓✓｜一个锐问题 ✓✓**）

$$\boxed{\textbf{(1) 勘误（P1-D3b §2 错 ✗✓）}:\ \text{四个 forced 点 }x_T\ (T\subset S,|T|=3)\ \textbf{不是码字}✗\ \big(\text{由 }(\alpha)\ \text{排除 ✓}\big) \Longrightarrow \textbf{不构成 }G_2(C)\ \text{的团、\textbf{不计入} }T_4✗✓}$$
$$\boxed{\textbf{(2) 见证者分解 ✓}:\ \text{每个 forced 三元 }T\subseteq S(c)\ \text{须有见证 }y=c\oplus S\ (T\subset S,|S|=4)\ ✓;\ \text{若 }S\not\subseteq S(c)\ \text{则 }y\ \textbf{恰覆盖 1 个 forced 三元}✓✓}$$
$$\boxed{\textbf{(3) ★逃逸定位（关键 ✓✓）}:\ \text{若 }S\subseteq S(c)\ (\text{即 }e_{(S)}\in\mathrm{span}(S(c)))\ \text{则 }y\ \text{覆盖 }\mathbf 4\ \text{个}; \textbf{而 }(\alpha')\ \text{\textbf{不排除}}这种 }y✗\ \big((\alpha')\ \text{仅覆盖重量 2／3 ✓}\big)}$$
$$\qquad\Longrightarrow\ \textbf{容量界 }d_4(c)\ge\lceil\binom{s(c)}3/4\rceil\ \textbf{存续}✗\ \big(\text{未能升级为 }\binom{s(c)}3\ ✗\big)$$
$$\boxed{\textbf{(4) ★锐化后的单一问题（P1-D4b ✓✓）}:\ \textbf{能否 }c\oplus u\in C\ \text{与 }A(c)=0\ \textbf{共存，其中 }u\subseteq S(c),\ |u|=4\ ?}$$
$$\qquad\textbf{不能} ⟹ d_4(c)\ge\binom{s(c)}3\ \big(\textbf{4 倍增强}✓✓\big);\qquad \textbf{能} ⟹ \text{容量界即最优}✗$$

---

## §1 **勘误**（**P1-D3b §2 的 star 断言错 ✗**）

$$\text{P1-D3b §2 原文}:\ \text{"四点是 }y\ \text{的四个邻居} \Longrightarrow \text{按 R7 四族目录为 star（已实现）} \Longrightarrow \text{计入 }T_4"\ ✗\textbf{错}$$
$$\textbf{错因 ✓}:\ T_4=\sum_x\binom{b(x)}4\ \text{计数的是\textbf{落在 }C\ \text{中的} 4-子集}✓;\ \text{而 }x_T=c\oplus e_{(T)}\ \text{满足 }T\subseteq S(c)\ \Longrightarrow\ (\alpha)\ x_T\notin C\ ✗✓$$
$$\qquad\Longrightarrow\ \text{四点\textbf{皆非码字}} \Longrightarrow\ \textbf{不构成 }G_2(C)\ \text{的团、不计入 }T_4✓✓\ \text{（此断言须撤回 ✗）}$$
$$\textbf{保留的部分 ✓}:\ \text{"四点两两距离 2、共享 }y\text{、构成 }G_2(Q_{10})\ \text{（\textbf{全图}）的 }K_4\ \text{（star 型）}"\ \text{仍成立}✓\ \text{—— \textbf{但那是全图结构，与 }C\ \text{无关}✗✓}$$

## §2 **见证者分解**（**新 ✓**）

$$\text{forced 情形 ✓}:\ T\subseteq S(c),\ |T|=3\ \Longrightarrow\ x_T=c\oplus e_{(T)}\notin C\ ((\alpha)✓);\ \text{其三个 weight-2 邻居 }c\oplus e_{(T\setminus i)}\notin C\ (A(c)=0✓)✓$$
$$\qquad\Longrightarrow\ x_T\ \text{必须由 weight-4 见证覆盖}:\ y=c\oplus S\in C,\ T\subset S,\ |S|=4✓$$
$$\textbf{（情形 A：外见证 ✓）}:\ S\not\subseteq S(c)\ \Longrightarrow\ S=T\cup\{i\},\ i\notin S(c)✓;\ \text{其四个三元}:\ S\setminus\{j\}=\begin{cases}T&(j=i)✓\ \text{含于 }S(c)✓\\ (T\setminus j)\cup\{i\}&\text{含 }i\notin S(c)\ ⟹ \textbf{非} forced✓\end{cases}$$
$$\qquad\Longrightarrow\ \boxed{\text{外见证恰覆盖 }\mathbf 1\ \text{个 forced 三元}}\ ✓✓\ \text{（＝唐先生所求"消耗不可重复资源"的\textbf{下界侧}形态 ✓）}$$
$$\textbf{（情形 B：内见证 ✓）}:\ S\subseteq S(c)\ \Longrightarrow\ y\ \text{的四个三元}\ S\setminus\{j\}\ \text{皆}\subseteq S(c)\ \Longrightarrow\ \textbf{恰覆盖 }\mathbf 4\ \text{个 forced 三元}✓$$
$$\Longrightarrow\ \text{总需求}:\ \binom{s(c)}3\ \le\ \#\text{外见证}\cdot1+\#\text{内见证}\cdot4\ \le\ 4d_4(c)\ \Longrightarrow\ \textbf{容量界存续}✓\ \text{（无增强 ✗）}$$

## §3 **逃逸定位**（**本档核心 ✓✓**）

$$(\alpha')\ \text{（P1-MICRO ✓）}:\ A(c)=0\Longrightarrow C\cap\big(c+\mathrm{span}(S(c))\big)\subseteq\{c\}\cup\{c\oplus e_i\}_{i\in S(c)}✓$$
$$\qquad\textbf{但该定理的证明只覆盖重量 2（}A(c)=0✓\big)\ \text{与重量 3（}(\alpha)✓\big)\ ✗✓\ \text{—— \textbf{重量}\ge4\ \textbf{未证}⚠️}$$
$$\Longrightarrow\ \text{情形 B（}S\subseteq S(c)✓\text{）\textbf{未被任何已证命题排除}✗✓\ \text{—— \textbf{它就是逃逸口}✓✓}$$
$$\textbf{与既有逃逸的同型性 ✓✓}:\ \text{① P1-D3b 的 }j=3\ \text{混合块（3 内＋1 外）✓};\ \text{② }C(s,4,3)\ \text{不作下界的原因 ✓};\ \text{③ 本档情形 B ✓}$$
$$\qquad\Longrightarrow\ \textbf{三者同一形态}:\ \text{"\textbf{溢出／内部}块\textbf{打散计数}"}✓✓\ \text{—— 本线反复的真正障碍 ✓}$$

## §4 **锐化后的单一问题（P1-D4b ✓✓）**

$$\boxed{\textbf{P1-D4b}:\ \text{是否存在 }c\oplus u\in C\ \text{与 }A(c)=0\ \text{共存，其中 }u\subseteq S(c),\ |u|=4\ ?}$$
$$\textbf{两个出口 ✓}:\quad\textbf{不能} \Longrightarrow (\alpha')\ \text{可扩到重量 4} \Longrightarrow \text{情形 B 消失} \Longrightarrow \boxed{d_4(c)\ \ge\ \binom{s(c)}3}\ \big(\textbf{较容量界强 4 倍}✓✓\big)$$
$$\qquad\qquad\textbf{能} \Longrightarrow \text{给出显式构造} \Longrightarrow \text{容量界即最优}✗\ \text{（\textbf{亦是明确结论} ✓）}$$
$$\textbf{为何已证部分不覆盖它 ✓}:\ u\subseteq S(c)\ \text{时，含 }c\oplus u\ \text{的 square 的其余顶点为重量 2／3（皆被排除 ✓）};\ \text{含 }c\oplus u\ \text{的 tetra 其余顶点为重量 2／6（重量 2 被排除 ✓，\textbf{重量 6 未被排除}✗）}$$
$$\qquad\Longrightarrow\ \text{需\textbf{新的}局部论证（重量 6 层的耦合）}\ ⚠️\ \text{—— 这是下一步唯一该做的局部检查 ✓}$$

## §5 现状（**诚实 ✓**）

$$\textbf{C-414 状态 ✓}:\ \textbf{LIVE}✓;\ \text{第三类来源（图结构／刚性耦合）\textbf{确实咬合}✓ —— 但其咬合\textbf{被重量 4／6 逃逸口门控}⚠️}$$
$$\textbf{已确立 ✓}:\ \text{① 外见证 1 对 1 ✓};\ \text{② 容量界存续（无增强 ✗）};\ \text{③ 逃逸口精确位置 ✓✓};\ \text{④ 同一形态的三处逃逸 ✓}$$
$$\textbf{未确立 ✗}:\ d_4\ \text{上界（仍缺 ✓）};\ \text{P1-D4b（未决 ⚠️）};\ \text{无矛盾 ✓}$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "见证者"
技术词 见证者          命中文件数=2    :: ./B1b-owner-structure-engine-and-results-d1-d4.md ./E188-low-point-hypergraph-transversal-bounded.md
$ bash scripts/tech_word_check.sh "内部逃逸"
技术词 内部逃逸        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "重量4逃逸"
技术词 重量4逃逸       命中文件数=0    ::
$ bash scripts/tech_word_check.sh "一一对应"
技术词 一一对应        命中文件数=17   :: ./KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md ./D1CLUSTER-2026-09-26-new-lower-bound-and-odd-n-target.md ./R7-LOCK-2026-09-27-status-lock-and-the-K4-deficit-interface-identity.md
```
- **本档新增**：**0** 个术语 ✓（`内部逃逸`／`重量4逃逸` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`见证者`／`一一对应` 档案已有 ✓）
- **注 ✓**：本档实质＝**§1 勘误 ＋ §2 分解 ＋ §3 逃逸定位 ＋ §4 锐问题**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **C-414 保持 LIVE** ✓；**不声称** P1 成立 ✗（V290）；**不声称** D3→D4 线已死 ✗
- **§1 为勘误，必须与 P1-D3b 并列引用** ✓（防误传 star 入 $T_4$ ✗）
- **§3 的"$(\alpha')$ 仅覆盖重量 2／3"必须保留** ✓（防把情形 B 当已排除 ✗）
