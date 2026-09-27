# P1-D3-2026-09-27 — **$d=3$ 最小检查**：核验通过 ✓ ＋ **被迫高层码字定理** ＋ C-411 NO-GO 的作用域修正

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:56 令 ✓）**：核验 $d=3$ 最小检查；做"两／三个 weight-3 点共存"的第一步；零程序计算 ✓。

**已查地图：命中（接续 P1-TWO／P1-MICRO／P1-AVOID，非新案 ✓）**
所查：`docs/P1-TWO-2026-09-27-…`（**自动覆盖 NO-GO** ✓✓）｜`docs/P1-MICRO-2026-09-27-…`（**(α)(α′)(β)** ✓✓）｜`docs/P1-AVOID-2026-09-27-…`｜`docs/R4-P1-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** $K_4$-avoidance 对象的 $d=3$ 层（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出"被迫高层码字定理"（$\{a,b,c\}\subseteq S(c)\Rightarrow$ 存在 distance-4 码字）＋ $d_4$ 计数下界 ＋ NO-GO 作用域修正** ✓）
**[RESEARCH]**

---

## §0 结论（**核验通过 ✓✓｜一处精化 ✓｜一条被迫高层定理 ✓✓｜一处作用域修正 ✓**）

$$\boxed{\textbf{(1) 最小检查核验通过 ✓✓}:\ d(c,x)=3\ (x=c{\oplus}e_a{\oplus}e_b{\oplus}e_c)\ \Longrightarrow\ B_1(c)\cap B_1(x)=\varnothing\ ✓✓\ (\text{与 }d=2\ \text{情形的 }|B\cap B|=2\ \text{本质不同 ✓})}$$
$$\boxed{\textbf{(2) 精化（本档 ✓）}:\ A(c)=0\ \text{只排除\textbf{支撑含于 }S(c)\ \text{者};\ 故"推入高层"须\textbf{全条件 }\{a,b,c\}\subseteq S(c)}✓✓\ (\text{非自动 ✓})}$$
$$\boxed{\textbf{(3) ★被迫高层码字定理（新 ✓✓）}:\ \{a,b,c\}\subseteq S(c)\ \Longrightarrow\ \boxed{\exists\,i\notin\{a,b,c\}:\ c{\oplus}e_a{\oplus}e_b{\oplus}e_c{\oplus}e_i\in C}\ ✓✓}$$
$$\boxed{\textbf{(4) $d_4$ 计数下界（新 ✓）}:\ \boxed{d_4(c)\ \ge\ \Big\lceil\tbinom{s(c)}3/4\Big\rceil}\ ✓\ \（\text{本线\textbf{第一个下界}（此前皆为上界）✓）}}$$
$$\boxed{\textbf{(5) 作用域修正（诚实 ✓）}:\ C-411\ \text{的自动覆盖 NO-GO 只对\textbf{已研究的构型类}成立};\ d=3\ \text{点覆盖\textbf{不在其内}}✓✓}$$

---

## §1 最小检查的**核验**（**逐层算 ✓✓**）

$$c=0,\ x=e_a{\oplus}e_b{\oplus}e_c\ (d=3)✓;\qquad B_1(x)=\{x\}\cup\{x{\oplus}e_i\}_{i=1}^{10}✓$$
$$\quad i\in\{a,b,c\}:\ x{\oplus}e_i\ \text{为\textbf{重量 2}}（如 }x{\oplus}e_a=e_b{\oplus}e_c✓）\ \text{—— 3 个 ✓};\quad i\notin\{a,b,c\}:\ x{\oplus}e_i\ \text{为\textbf{重量 4} —— 7 个 ✓}$$
$$\Longrightarrow\ B_1(x)=\{\text{3 个 weight-2}\}\cup\{x\}\cup\{\text{7 个 weight-4}\}\ ✓✓\ \text{（照唐先生 ✓）}$$
$$\text{交集 ✓}:\ 0\in B_1(x)?\ d(0,x)=3\ ✗;\quad e_i\in B_1(x)?\ d(e_i,x)=|x{\oplus}e_i|=2\ (i\in\{a,b,c\})\ \text{或}\ 4\ (i\notin)\ \Longrightarrow\ \text{皆}>1\ ✗$$
$$\Longrightarrow\ \boxed{B_1(c)\cap B_1(x)=\varnothing}\ ✓✓\ \text{—— 故 }x\ \text{及其 1-邻域的覆盖\textbf{不能}由 }c\ \text{的 radius-1 邻域自动补掉 ✓✓}$$
$$\textbf{对照 ✓}:\ d(c,y)=2\ (y=e_i{\oplus}e_j)\ \Longrightarrow\ |B_1(c)\cap B_1(y)|=2✓\ \text{—— 这正是 P1-MICRO (β) 的自消解来源 ✓};\ d=3\ \text{无此重叠 ✓✓}$$

## §2 精化：**"推入高层"的精确条件**（**本档 ✓**）

$$\text{覆盖 }x\ \text{者必在 }C\cap B_1(x)\subseteq\{\text{3 个 weight-2}\}\cup\{x\}\cup\{\text{7 个 weight-4}\}✓\ \text{—— 对这三类逐个设限}:$$
$$\textbf{① weight-2 类}:\ x{\oplus}e_i\ (i\in\{a,b,c\})=e_{\{a,b,c\}\setminus i}\ \text{—— 它们是 }c\ \text{的 distance-2 点，\textbf{被 }A(c)=0\ \text{排除的充要条件是其支撑含于 }S(c)✓✓}$$
$$\qquad\Longrightarrow\ \text{仅当 }\{a,b\}\subseteq S(c)\ \text{时 }e_a{\oplus}e_b\notin C✓;\ \text{故三类\textbf{全被排除}须 }\{a,b\}\cup\{a,c\}\cup\{b,c\}\subseteq S(c)\iff\{a,b,c\}\subseteq S(c)✓✓$$
$$\textbf{② }x\ \text{自身}:\ \{a,b,c\}\subseteq S(c)\Longrightarrow(\alpha)\ x\notin C\ ✓✓\ \text{（P1-MICRO 内部子立方体排斥定理 ✓）}$$
$$\Longrightarrow\ \boxed{\text{故在 }\textbf{全条件}\ \{a,b,c\}\subseteq S(c)\ \text{下},\ C\cap B_1(x)\ \text{只能落在 7 个 weight-4 点中}✓✓}$$

## §3 **被迫高层码字定理**（**新 ✓✓；本线第一个"强制"**）

$$\text{由 §2}:\ x\ \text{必须被覆盖且 }C\cap B_1(x)\cap\{\text{weight-2}\cup\{x\}\}=\varnothing\ \Longrightarrow\ \exists\,w\in C\cap B_1(x)\ \text{为 weight-4}✓$$
$$\qquad w=x{\oplus}e_i=c{\oplus}e_a{\oplus}e_b{\oplus}e_c{\oplus}e_i\ \ (i\notin\{a,b,c\})✓$$
$$\Longrightarrow\ \boxed{\textbf{被迫高层码字定理}:\ \{a,b,c\}\subseteq S(c)\ \Longrightarrow\ \exists i\notin\{a,b,c\}:\ c{\oplus}e_a{\oplus}e_b{\oplus}e_c{\oplus}e_i\in C}\ ✓✓$$
$$\textbf{性质 ✓}:\ \text{这是本线\textbf{第一个\textbf{正强制}（存在性）};\ 此前全部为\textbf{界}——既有上界（}d_2,d_3,d_4\ \text{类）也有下界（新的 §4 ✓）✓}$$

## §4 **$d_4$ 计数下界**（**新 ✓；本线第一个下界**）

$$\text{一个 weight-4 码字 }w=c{\oplus}S\ (\text{weight 4},\ |S|=4)\ \text{能覆盖哪些"待覆盖的 }d=3\ \text{点"？}$$
$$\qquad x_T=c{\oplus}e_{(T)}\ (|T|=3)\ \text{与 }w\ \text{距离 1}\iff|e_{(T)}{\oplus}e_{(S)}|=1\iff T\subset S,\ |S\setminus T|=1\iff T\ \text{为 }S\ \text{的 3-子集}✓$$
$$\Longrightarrow\ \text{每个 }w\ \text{至多覆盖 }\binom43=\mathbf 4\ \text{个待覆盖 }T✓;\ \text{而 }\binom{s(c)}3\ \text{个 }T\ \text{各需一个见证 }✓$$
$$\Longrightarrow\ \boxed{d_4(c)\ \ge\ \Big\lceil\tfrac14\tbinom{s(c)}3\Big\rceil}\ ✓✓;\qquad \text{聚合}:\ 2N_4=\sum_cd_4(c)\ \ge\ \tfrac14\sum_c\tbinom{d_1(c)}3✓$$
$$\textbf{类型 ✓}:\ \text{与 P1-AVOID／P1-MICRO 的 }d_2,d_3\ \textbf{上界}相反，本节给出 }d_4\ \textbf{下界} ⟹ \text{方向可用 ✓（若另有 }d_4\ \text{上界即可夹逼 ✓）}$$

## §5 **C-411 NO-GO 的作用域修正**（**诚实 ✓✓**）

$$C-411\ §3\ \text{原文}:\ \text{"本文全部局部构型的点皆 }\le1\text{"} ⟹ \text{covering 无牙 ✓}$$
$$\textbf{修正 ✓}:\ \text{该断言\textbf{只对该档研究的构型类}（square／tetra／中点／公共邻居 —— 其点皆为码字或其 1-邻居 ✓）成立 ✓;$$
$$\qquad\textbf{而 }d=3\ \text{点 }x\ \text{（及其 1-邻域）与 }B_1(c)\ \text{不相交 ⟹ 覆盖责任\textbf{真实存在}✓✓ —— 不在 NO-GO 作用域内 ✓}$$
$$\Longrightarrow\ \boxed{\text{故 }d=3\ \text{路线\textbf{不是} C-410 的重复};\ \text{唐先生的判定\textbf{正确} ✓✓}\ \big(\text{"自动覆盖"检查 \textbf{PASS}，未关闭 ✓}\big)}$$
$$\textbf{（NO-GO 的正确表述 ✓）}:\ \text{covering 只在\textbf{到所有码字距离}\ge2\ \text{的点}上有约束力};\ \text{而 }d=3\ \text{点满足"到 }c\ \text{距离 3"\ ✓} ⟹ \text{它\textbf{可能}远离一切码字 ⟹ 约束真实 ✓}$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "覆盖责任"
技术词 覆盖责任        命中文件数=1    :: ./E184-T2c-vacuous-and-covering-locality.md
$ bash scripts/tech_word_check.sh "被迫高层码字"
技术词 被迫高层码字    命中文件数=0    ::
$ bash scripts/tech_word_check.sh "下降层"
技术词 下降层          命中文件数=0    ::
$ bash scripts/tech_word_check.sh "高层强制"
技术词 高层强制        命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`被迫高层码字`／`下降层`／`高层强制` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`覆盖责任` 档案已有（他处 ✓））
- **注 ✓**：本档实质＝**§1 核验 ＋ §2 精化 ＋ §3 被迫定理 ＋ §4 下界 ＋ §5 作用域修正**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未进入 tetra 共存分析** ✓（照唐先生"先把最小检查做掉" ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** 已产生矛盾 ✗（照唐先生 ✓："没有自动覆盖" $\ne$ "已产生矛盾" ✓）；**不声称** P1 成立 ✗（V290 ✓）
- §3 的被迫定理**前提**（$\{a,b,c\}\subseteq S(c)$）**必须显式保留** ✓；§4 的 $d_4$ 下界**为下界**（若无上界则不能夹逼 ✓）
- 与 C-411 的关系已显式修正 ✓（防把 NO-GO 误扩到 $d=3$ ✓）
