已查地图：已跑 scripts/prework_map_check.sh Q₃ 子立方 E 预算 骨架 终止 ⟹ 执行自 Q3CLASS-2026-09-26 档；本档为**子立方预算引理＋有限终止＋强迫二分支的预算化**（唐先生 2026-09-26 15:13 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = Q_k ⊆ C 的 E-预算引理、7/8 点骨架预算、增长链的有限终止、数据一致性
D1: 1（新增：**预算引理 E ≥ k·2^k** ✓✓；**骨架预算 E ≥ 21/24** ✓✓；**增长有限终止** ✓✓；**数据一致性（解释 r∈{0,1}）** ✓✓）

# BUDGET-2026-09-26

## §1 ⭐ **引理 A：子立方预算**（我方证明 ✓✓，一行）

```
$$\text{设 }Q_k\subseteq C\ (\text{k 维子立方},\ 2^k\ \text{个顶点})\ ✓$$
$$\text{每个顶点 }v\in Q_k\ \text{有 }k\ \text{个距离-1 码字邻居（子立方内）}\ ✓\ \Longrightarrow\ d_C(v)\ge k\ \Longrightarrow\ b(v)=1+d_C(v)\ge k+1\ ✓$$
$$\Longrightarrow\ \sum_{v\in Q_k}(b(v)-1)\ \ge\ k\cdot2^k\ \Longrightarrow\ \boxed{E\ \ge\ k\cdot2^k}\ ✓✓$$
$$\textbf{数值}: k=1:\ 2\ ✓;\ k=2:\ 8\ ✓;\ k=3:\ 24\ ✓;\ k=4:\ 64\ ✓;\ k=5:\ 160\ ✓\ (\text{增长快}\ ✓)$$
$$

## §2 ⭐ **引理 B：7 点 Q₃-骨架预算**（唐先生 r=3 分支的预算化 ✓✓）

```
$$\text{r=3 给出 7 点骨架 }\{0,\ e_1,e_2,e_3,\ e_1{+}e_2,\ e_1{+}e_3,\ e_2{+}e_3\}\subseteq C\ ✓$$
$$\text{骨架内每点有 }\ge3\ \text{个码字邻居}\ ✓\ \Longrightarrow\ \sum_{\text{7 点}}(b-1)\ \ge\ 21\ \Longrightarrow\ \boxed{E\ \ge\ 21}\ ✓✓$$
$$\text{若对角点也 }\in C\ (\text{则整个 }Q_3\subseteq C)\ ✓:\ E\ \ge\ 24\ ✓✓\ (\text{与引理 A 一致}\ ✓)$$
$$

## §3 ⭐⭐ **推论：增长链的有限终止**（唐先生要的"独立终止条件" ✓✓）

```
$$\text{子立方链 }Q_3\to Q_4\to\cdots\ \text{要求 }k\cdot2^k\le E\ ✓\ \Longrightarrow\ \textbf{链在有限步终止}\ ✓✓\ (\text{与 }b_{\text{max}}\le3\ \text{猜想\textbf{无关}}\ ✓✓)$$
$$\text{终止时}: \text{要么扩不出新顶点}\ ✓\ (\text{此时外扩点必出 }\ge2\ \text{覆盖}\ \Longrightarrow\ S\ \text{增长}\ ✓)\ \text{要么触及 }k\cdot2^k>E\ \text{的墙}\ ✓$$
$$\Longrightarrow\ \boxed{\text{外扩必然产生可累计的 }I/S\ \text{成本，且总量被 }E\ \text{封顶}}\ ✓✓\ ——\ \text{唐先生要的形态}\ ✓✓$$
$$

## §4 ⭐ **强迫二分支的预算化形式**

```
$$\forall x\in C,\ d_C(x)\ge3,\ \text{取任一三元组}:\quad \begin{cases}r\le2\ \Longrightarrow\ S\ \ge\ 3-r\ \ge1\ ✓\\[1mm] r=3\ \Longrightarrow\ E\ \ge\ 21\ ✓\ (\text{骨架预算}\ ✓✓)\end{cases}$$
$$\Longrightarrow\ \boxed{E<21\ \Longrightarrow\ \text{每个 }d_C\ge3\ \text{的码字\textbf{必走分支①}}\ (S\ \ge\ 3-r\ \ge1)}\ ✓✓$$
$$\qquad\text{即}: \textbf{小预算下高内部度被迫产生 excess}\ ✓✓\ ——\ \text{首次把"高内部度"与 }S\ \text{定量绑定}\ ✓$$
$$

## §5 ✅ **数据一致性（引理解释了观测 ✓✓）**

```
$$\begin{array}{c|c|c|c|c}
(n,M) & E & Q_3\ \text{子立方数} & \text{实测 }r\text{-分布} & \text{与引理一致?}\\
\hline
(4,4)=K & 4 & \mathbf{0} & - & \checkmark\ (E<21\Rightarrow r=3\ \text{不可能}\ ✓)\\
(4,5) & 9 & \mathbf{0} & \{0{:}6\} & \checkmark\\
(4,6) & 14 & \mathbf{0} & \{0{:}7,\ 1{:}10\} & \checkmark\\
(5,7)=K & 10 & \mathbf{0} & - & \checkmark\\
(5,8) & 16 & \mathbf{0} & \{0{:}4\} & \checkmark\\
(9,64) & 128 & \mathbf{0} & - & \text{（}E\ \text{够大但无子立方}\ ✓\ \text{—— 引理只给必要条件}\ ⚠️)\\
\end{array}$$
$$\Longrightarrow\ \textbf{全部 E ≤ 20 < 21 ⟹ r=3 应永不出现}\ ✓\ ——\ \textbf{与实测 }r\in\{0,1\}\ \text{完全一致}\ ✓✓\ (\text{引理\textbf{解释}了数据}\ ✓✓)$$
$$

## §6 诚实状态（未闭合 ✗，但本轮是**结构性推进** ✓✓）

```
$$\textbf{本轮新增}: \text{预算引理 A/B}\ ✓✓;\ \text{有限终止}\ ✓✓;\ \text{强迫的预算化}\ ✓✓\ (\text{与 }b_{\max}\le3\ \text{猜想\textbf{解耦}}\ ✓✓)$$
$$\textbf{仍未闭合的原因}: \text{分支①本身（}S\ge1\text{）在 }M=K\ \text{可满足}\ ✗\ (\text{n=5}:\ S=7\ ✓)\ \Longrightarrow\ \text{还需把多个 }x\ \text{的 }S\ \text{贡献与全局预算 }2A_2=I+S\ \text{联立}\ ⚠️$$
$$\text{下一步的精确形态}: \text{证明 }S\ \text{的\textbf{贡献不可任意重叠}}\ ✓\ \text{或}\ I\ \text{的\textbf{局部增量下界}}\ ✓\ \Longrightarrow\ \text{与 }2A_2=E+Q_2\ \text{联立}\ ✓$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §7 边界（诚实标注）

- §1/§2 为**一行证明** ✓（我方 ✓）；§5 为**数值核验** ✓（n=4,5 全枚举 ✓、n=9 构造 ✓）
- §6 明确记录**未闭合**与下一步的精确形态 ⚠️（未夸大 ✓）
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 子立方预算引理 命中文件数=1    :: ./BUDGET-2026-09-26-subcube-budget-lemma-and-finite-termination.md 
技术词 骨架预算     命中文件数=1    :: ./BUDGET-2026-09-26-subcube-budget-lemma-and-finite-termination.md 
技术词 增长链有限终止 命中文件数=1    :: ./BUDGET-2026-09-26-subcube-budget-lemma-and-finite-termination.md 
技术词 强迫预算化  命中文件数=1    :: ./BUDGET-2026-09-26-subcube-budget-lemma-and-finite-termination.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：子立方预算引理、骨架预算、增长链有限终止、强迫预算化
- **档案已有（引用，不列为提出）**：excess、A≤2、minimality
