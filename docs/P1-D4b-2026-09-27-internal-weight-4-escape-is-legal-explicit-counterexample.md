# P1-D4b-2026-09-27 — **P1-D4b ＝ YES 型（附显式反例）**：内部 weight-4 逃逸合法

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；**不引 RH 链** ✗。
> **⚠️ 词回查分线（照唐先生 23:12 令 ✓）**：本节起，`tech_word_check.sh` 命中**必须按空间分栏** —— 只有 **119 线（空间 B）** 文档计"档案已有（本线）"，**RH 线（空间 A）同名一律标注"空间 A 同名，不计"** ✗（已固化进 `TOOLS.md` ✓）。
> **范围**：做完 P1-D4b（weight-6 层局部检查）；零程序计算 ✓。

**已查地图：命中（接续 P1-G2／P1-D4／P1-MICRO，非新案 ✓）**
`docs/P1-G2-2026-09-27-…`（**见证者分解／逃逸定位／P1-D4b** ✓✓）｜`docs/P1-D3b-2026-09-27-…`（**含勘误横幅** ✓）｜`docs/P1-D3-2026-09-27-…`｜`docs/P1-MICRO-2026-09-27-…`（**$(\alpha)(\alpha')$** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，**已分线**，见 §6）
D0: 本档对象 ＝ **档案已有** P1-D4b 问题（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出内部 weight-4 逃逸的\*\*显式反例\*\* ＋ 其三条推论（局部极限／weight-6 强制不存在／$(\alpha')$ 不可扩）** ✓）
**[RESEARCH]**

---

## §0 结论（**YES 型 ✓✓；附显式反例 ✓✓；三条推论 ✓**）

$$\boxed{\textbf{P1-D4b}:\ \exists\,c\oplus u\in C\ \text{与 }A(c)=0\ \text{共存，}u\subseteq S(c),|u|=4\ ?\qquad\Longrightarrow\ \textbf{YES}\ ✓✓}$$
$$\textbf{显式反例 ✓✓}:\quad \boxed{C_0:=\{0\}\ \cup\ \{e_i:1\le i\le10\}\ \cup\ \{y:=e_1{\oplus}e_2{\oplus}e_3{\oplus}e_4\}}\qquad(12\ \text{点})$$
$$\textbf{逐项核验 ✓}:\quad \textbf{① }\ S(0)=[10]\ \Longrightarrow\ u=\{1,2,3,4\}\subseteq S(0)✓;\quad \textbf{② }\ A(0)=0✓\ (C_0\ \text{无重量 2 点});\quad \textbf{③ }\ (\alpha)\ \text{在 0 成立}✓\ (C_0\ \text{无重量 3 点})$$
$$\qquad\textbf{④ }\ A(y)=0✓\ (S(y)=\varnothing);\quad \textbf{⑤ }\ \textbf{全 avoidance}✓✓:\ N_{\rm square}=N_{\rm tetra}=0\ (\text{逐类排除，见 §1}\ ✓)$$
$$\Longrightarrow\ \boxed{\textbf{内部 weight-4 码字与 }A(c)=0\ \text{可共存}}\ ✓✓\ \Longrightarrow\ \boxed{\textbf{NO 型}\ (d_4(c)\ge\binom{s(c)}3)\ \textbf{不可得}}\ ✗$$
$$\textbf{推论 1 ✓}:\ \text{容量界}\ \lceil\binom{s(c)}3/4\rceil\ \textbf{＝这条局部路线的自然极限}✓\qquad\textbf{推论 2 ✓}:\ \textbf{预期的 weight-6 强制不存在}✓$$
$$\textbf{推论 3 ✓✓}:\ \textbf{$(\alpha')$ 可证不能扩到重量 4}✗\ (\text{由 }C_0\ \text{反例}✓)$$

---

## §1 **显式反例的逐类核验**（**全 avoidance ✓✓**）

$$\textbf{Squares ✓}:\ \text{2-coset}=\{v,v{\oplus}e_a,v{\oplus}e_b,v{\oplus}e_a{\oplus}e_b\}\ (\text{偏移 }0,1,1,2✓)\ \text{—— 需一个重量 2 点}✗;\ C_0\ \text{无重量 2 点} \Longrightarrow \textbf{无 square}✓\ (\text{逐基 0／}e_i／y\ \text{三类皆 ✗}✓)$$
$$\textbf{Tetras ✓}:\ \text{3-coset 偶部}=\{v,v{+}e_a{+}e_b,v{+}e_a{+}e_c,v{+}e_b{+}e_c\}\ (\text{偏移 }0,2,2,2✓)\ \text{—— 需重量 2（基 }0,2\to\text{重量 }1/3;\ \text{基 }y\to\text{重量 }2/6\text{）}✗$$
$$\qquad C_0\ \text{无重量 2／3／5／6 点} \Longrightarrow \textbf{无 tetra}✓✓\ \big(\text{基 }y\ \text{需重量 }2\ \text{或 }6\ ✗✓\big)$$
$$\textbf{K}_4\ \text{型（允许 ✓）}:\ \{e_1,e_2,e_3,e_4\}\ \text{两两距离 2、共享中心 }0 \Longrightarrow \textbf{star（已实现 ✓）}✓;\ \{0,e_i,e_j,e_k\}\ \text{中心 }e_i\in K\Longrightarrow\textbf{claw（已实现 ✓）}✓$$
$$\qquad\Longrightarrow\ \text{二者皆\textbf{非} square／tetra ⟹ \textbf{不被 avoidance 禁止}✓✓\ \text{（与 R7 目录一致 ✓）}$$

## §2 **推论 1：局部极限**（**诚实 ✓**）

$$\text{由 §0}:\ \text{对每个 forced 三元，见证可为\textbf{内见证}（}S\subseteq S(c)\text{，覆盖 4 个 ✓）} \Longrightarrow \text{容量界不可由 avoidance 改进}✗$$
$$\Longrightarrow\ \text{故 P1-D4b 的\textbf{NO 型增强}（}d_4\ge\binom s3\text{）在 avoidance 层面\textbf{不可得}✓;\ \text{容量界 }\lceil\binom s3/4\rceil\ \textbf{＝局部路线的自然极限}✓✓}$$
$$\textbf{（照唐先生 YES 型判据 ✓）}:\ \text{这\textbf{不是"证明失败"}，而是\textbf{明确证明内部块是合法逃逸机制}✓✓}$$

## §3 **推论 2：预期的 weight-6 强制不存在**（**✓**）

$$\text{预测（唐先生 ✓）}:\ A(c)=0\ \wedge\ c\oplus u\in C\ (|u|=4)\Longrightarrow\ \text{某个 weight-6 配置必然出现}$$
$$\textbf{反例检验 ✓}:\ C_0\ \text{含内部 weight-4 码字 }y\ ✓\ \text{且满足全 avoidance ✓};\ \text{而 }C_0\ \textbf{不含任何重量 5／6 点}✓$$
$$\Longrightarrow\ \boxed{\text{局部层面\textbf{不存在}由内部 weight-4 码字强制的 weight-6 配置}}\ ✓✓\ \Longrightarrow\ \text{该接口\textbf{不成立}✗✓}$$
$$\qquad\text{（且 }C_0\ \text{亦无 forced 三元被"重量-6 见证"覆盖的必要 ✓—— 其 forced 三元由 }y\ \text{自身覆盖 ✓）}$$

## §4 **推论 3：$(\alpha')$ 不能扩到重量 4**（**✓✓**）

$$(\alpha')\ \text{（P1-MICRO）}:\ A(c)=0\Longrightarrow C\cap\big(c+\mathrm{span}(S(c))\big)\subseteq\{c\}\cup\{c\oplus e_i\}_{i\in S(c)}✓\ \big(\text{已证部分：重量 }2,3✓\big)$$
$$\textbf{若其扩到重量 4（错 ✗）}:\ C_0\ \text{中 }S(0)=[10]\Longrightarrow\mathrm{span}(S(0))=\mathbb F_2^{10}\Longrightarrow\ \text{断言应为 }C_0\subseteq\{0\}\cup\{e_i\}✗$$
$$\qquad\text{而 }y\in C_0\ (\text{重量 4}\ ✓) \Longrightarrow \ \textbf{矛盾}✗✓\ \Longrightarrow\ \boxed{(\alpha')\ \text{的\textbf{重量 4 扩张被显式反例证否}}\ ✓✓}$$
$$\textbf{意义 ✓}:\ \text{这解释了 C-415 §3 的"逃逸口"为何\textbf{不能被修补}；且与全 avoidance 相容（}C_0\ \text{同时满足 avoidance 与重量-4 内部码字 ✓）}$$

## §5 状态与诚实边界（**✓**）

$$\textbf{已定 ✓}:\ \text{P1-D4b ＝ YES 型}✓✓;\ \text{容量界 ＝ 局部极限}✓;\ \text{weight-6 强制不存在}✓;\ (\alpha')\ \text{重量 4 扩张证否}✓✓$$
$$\textbf{⚠️ 诚实边界（必须写 ✓）}:\ C_0\ \textbf{不是覆盖码}✗\ \big(\text{如 }e_1{\oplus}e_2{\oplus}e_5\ \text{到一切码字距离}\ge2\ ✓\text{，未被覆盖}✓\big)$$
$$\qquad\Longrightarrow\ \textbf{covering 特异性未被本反例触及}⚠️\ \text{—— 反例只证明"avoidance 层面"的逃逸合法 ✓，\textbf{不}证明 119-cover 中存在此构型}✗✓$$
$$\textbf{（与既有结论一致 ✓）}:\ \text{下界侧（容量界）到顶 ✓};\ \text{上界侧被单调性挡住（P1-D4 §4 ✓）} \Longrightarrow\ \text{D3}\to\text{D4 夹逼在\textbf{局部}层面\textbf{关闭}✓;\ 全局层面\textbf{未决}⚠️$$
$$\textbf{C-415 状态 ✓}:\ \textbf{LIVE};\ \text{P1-D4b ＝ \textbf{YES 已决}✓（本档）};\ d_4\ \text{上界仍缺}✗;\ \text{无矛盾}✓$$

## §6 技术词回查（**先跑后写 ＋ 按空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "显式反例"
技术词 显式反例        命中文件数=19
$ bash scripts/tech_word_check.sh "重量6层"
技术词 重量6层         命中文件数=0
$ bash scripts/tech_word_check.sh "局部极限"
技术词 局部极限        命中文件数=0
$ bash scripts/tech_word_check.sh "合法逃逸"
技术词 合法逃逸        命中文件数=0
$ bash scripts/tech_word_check.sh "逃逸口"
技术词 逃逸口          命中文件数=38
```
**分线结果（逐档核对文件属线 ✓）**：

| 词 | 本线命中（空间 B ＝ 119／资产线） | 跨空间同名（空间 A ＝ RH 线，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 显式反例 | **1**（`R6-2026-09-27-…` ✓） | 18 | 0 |
| 逃逸口 | **1**（`P1-G2-2026-09-27-…` ✓） | 37 | 0 |
| 重量6层 | 0 | 0 | 0（本档自造标签 ✓） |
| 局部极限 | 0 | 0 | 0（本档自造标签 ✓） |
| 合法逃逸 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词命中 0，本档自造标签作结构命名，不作新性主张 ✓；`显式反例`／`逃逸口` 的**本线命中**仅为既有 119 线档 ✓）
- **⚠️ 空间纪律 ✓**：`显式反例` 的 18 档、`逃逸口` 的 37 档命中**全部属空间 A（RH 线）**（`V*`／`E*`／`C*`／`W*`／`p5*`／`pillar3*` 等 ✓）⟹ **一律不计** ✗（照唐先生 23:12 令 ✓；已固化 `TOOLS.md` ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§6 已分栏 ✓）
- **不声称** P1 成立 ✗（V290）；**不声称** D3→D4 线已死 ✗ —— 只写"**局部层面闭合**／全局未决" ✓
- **§5 的"$C_0$ 非覆盖码"必须保留** ✓（防把局部反例当 119-cover 结论 ✗）
- **§6 必须按空间分栏** ✓（照唐先生 23:12 令 ✓）
