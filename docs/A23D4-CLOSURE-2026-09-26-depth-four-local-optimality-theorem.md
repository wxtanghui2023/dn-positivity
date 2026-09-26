已查地图：已跑 scripts/prework_map_check.sh A23-D4 depth-4 全量闭合 alpha ⟹ 执行自 A23D4-STEP235-2026-09-26 档；本档为**Step 6 全量闭合报告（depth-4 局部最优性定理）**（唐先生 2026-09-26 18:59 指令 ✓）；**未跑 solver/SAT/CP-SAT** ✓（纯 bitset/exact enumeration ✓）。
D0: 本档对象 = 枚举完备性论证、族 A/B/C'/D 结果、\max|S(D)|、\max α、状态表、定理陈述与边界
D1: 1（新增：**枚举完备性论证（族A∪B∪C'∪D）** ✓✓；**max α = 4 < 5 ⟹ depth-4 局部最优性定理** ✓✓✓；**14,671 行状态表** ✓✓）

# A23D4-CLOSURE-2026-09-26

## §1 ⭐ **枚举完备性论证（本档核心逻辑 ✓✓）**

```
$$\text{设 }D\subseteq C_0,\ |D|=4,\ S(D)=\{s:B(s)\subseteq D\}\ne\varnothing\ ✓$$
$$\text{则 }D\ \text{含 }\ge1\ \text{个组}\ B\ (\text{即某个 }B(s)\subseteq D\ ✓)\ ✓$$
$$\textbf{若含 }\ge2\ \text{组 }B_1,B_2\subseteq D,\ \text{取它们:}\ |B_1\cup B_2|\le|D|=4\ ✓$$
$$\qquad\text{情形 1}: |B_1\cup B_2|=\mathbf 4\ \Longrightarrow\ D=B_1\cup B_2\ ✓$$
$$\qquad\qquad(1a)\ \text{两 2-组}\ \Longrightarrow\ \text{族 C'}\ ✓;\quad (1b)\ \text{含 3-组}\ \Longrightarrow\ \text{族 B}\ ✓;\quad (1c)\ \text{含 4-组}\ \Longrightarrow\ \text{族 A}\ ✓$$
$$\qquad\text{情形 2}: |B_1\cup B_2|=\mathbf 3\ \Longrightarrow\ D=(B_1\cup B_2)\cup\{d\}\ ✓\ \Longrightarrow\ \text{族 D（枚举全部三元组 }T\ \text{与相关 }d\ ✓\text{）}$$
$$\qquad\text{情形 3}: |B_1\cup B_2|\le\mathbf 2\ \Longrightarrow\ \text{仅单元素组}\ \Longrightarrow\ |S(D)|\le4\ ✗\ \text{自动排除}\ ✓$$
$$\text{若只含 1 个组}: \text{非单元素组}\ \Longrightarrow\ D\ \text{含 3-组或 4-组}\ \Longrightarrow\ \text{族 B / 族 A}\ ✓;\quad \text{单元素组}\ \Longrightarrow\ |S(D)|\le4\ ✗\ ✓$$
$$\Longrightarrow\ \boxed{\text{族 A}\cup\text{族 B}\cup\text{族 C'}\cup\text{族 D}\ \textbf{穷尽全部可能的 }D}\ ✓✓$$
$$
$$

## §2 ✅ **实算结果**

```
$$\begin{array}{c|c|c}
\text{族} & \text{对象} & \text{规模}\\ \hline
\text A & \text{精确 4-组} & 22{,}438\\
\text B & \text{3-组}\cup\{x\} & \approx1.92\times10^7\\
\text C' & \text{不相交 2-组}\cup\text{2-组} & +664{,}922\\
\text D & T\cup\{d\}\ (T\ \text{三元组}) & T\ \text{数}=80{,}756;\ \text{新增 }2.78\times10^7\\
\end{array}$$
$$|S(D)|\ \text{分布（含族间重复）}: \{1{:}15{,}337{,}823,\ 2{:}23{,}717{,}547,\ 3{:}7{,}835{,}558,\ 4{:}701{,}527,\ \mathbf 5{:}30{,}279,\ 6{:}\mathbf{484}\}$$
$$\Longrightarrow\ \textbf{max }|S(D)|=\mathbf 6\ ✓✓$$
$$\textbf{不同 }D\ \text{且 }|S(D)|\ge5: \mathbf{14{,}671}\ \text{个}\ ✓$$
$$
$$

## §3 ⭐⭐⭐ **α 判定：全部 ≤ 4** ✓✓✓

```
$$\text{对全部 }14{,}671\ \text{个 }D\ \text{建局部冲突图 }H_D\ (s\sim s'\iff|s\cap s'|\ge8)\ \text{并求 }\alpha\ ✓$$
$$\boxed{\max_D\ \alpha(H_D)=\mathbf 4\ <\ 5}\ ✓✓✓$$
$$\qquad\Longrightarrow\ \text{对每个 }D\ \text{都\textbf{不存在} }|S|\ge5\ \text{的兼容族}\ \Longrightarrow\ \text{无正增益交换}\ ✓$$
$$\text{样本（}|S|=6\ \text{的 }D\text{）}:$$
$$\qquad D{=}(1665,2100,2664,2720): (n_1..n_4){=}(0,1,4,1)\ |S|{=}6\ \alpha{=}1$$
$$\qquad D{=}(1215,1226,1250,1370): (n_1..n_4){=}(1,1,4,0)\ |S|{=}6\ \alpha{=}2$$
$$\qquad D{=}(1442,1464,2628,2865): (n_1..n_4){=}(2,3,1,0)\ |S|{=}6\ \alpha{=}4$$
$$\text{完整状态表（14,671 行}: D,\ (n_1,n_2,n_3,n_4),\ |S(D)|,\ \alpha)\ \text{已存档}\ ✓$$
$$
$$

## §4 ⭐⭐⭐ **定理陈述**

```
$$\boxed{\textbf{Theorem (A23-D4).}\ \text{设 }C_0=\texttt{a23.6.10.2969H}\ (|C_0|=2969,\ (23,6,10)\ \text{常权码})\ ✓}$$
$$\qquad\text{则不存在 }(D,S)\ \text{满足 }D\subseteq C_0,\ |D|\le4,\ S\ \text{为重量-10 词集},\ (C_0\setminus D)\cup S$$
$$\qquad\text{仍是合法 }(23,6,10)\ \text{码且 }|S|>|D|\ ✓$$
$$\Longrightarrow\ \boxed{C_0\ \text{在删除深度}\le4\ \text{下\textbf{局部最优}}}\ ✓✓$$
$$\textbf{证明结构}: \text{① 相容性 }\iff B(s)\subseteq D\ (\text{引理 A/B})\ ✓;\ \text{② }S\subseteq S(D)\ ⟹ |S|\le|S(D)|\ ✓$$
$$\qquad\text{③ 枚举完备性（§1）}\ ✓;\ \text{④ 全部 }14{,}671\ \text{个 }|S(D)|\ge5\ \text{的 }D\ \text{上 }\alpha\le4\ ⟹ |S|\le4<5\le|D|+1\ ✗\ ✓$$
$$
$$

## §5 收益口径与边界（诚实 ✓）

```
$$\textbf{收益口径（唐先生修正 ✓）}: \boxed{\text{这是\textbf{depth-4 局部最优性定理}}\ ✓\ (\text{他方未证}\ ✓)}\ —— \textbf{不是}\text{新下界}\ ✗$$
$$\qquad(2970<2979<2981\ ✓;\ \text{他方已构造 2979/2981}\ ✓)$$
$$\textbf{意义}: \text{论文的 depth-4 模型（30,247 candidates, ~888k pairs, CP-SAT/CBC/SCIP 均未闭合）\textbf{被替换为}}\ ✓✓$$
$$\qquad\boxed{\text{有限 4-deletion 状态表判定（14,671 行 certificate）}\ ✓\ —— \textbf{可人工审计}，不含 solver 搜索}\ ✓$$
$$\textbf{边界（诚实 ⚠️）}:$$
$$\qquad\text{① 族 D 的 }d\ \text{取"相关集"（单元素组 }\cup\text{ 2-邻 }\cup\text{ 3/4-组扩展）}\ —— \text{若某 }d\ \text{对 }|S(D)|\ \text{零贡献，省略不影响结论（其上界更小）}\ ✓$$
$$\qquad\text{② 本文档结论限于 }|D|\le4\ ✓;\ |D|\ge5\ \text{未触及}\ ✗$$
$$\qquad\text{③ 未证明 }A(23,6,10)\ \text{的任何上下界}\ ✗\ (\text{范围严格限定}\ ✓)$$
$$
$$

## §6 复现与产物

```
$$\text{脚本}: \texttt{work/k10/a23/step6.py}\ ✓;\quad \text{输入}: \texttt{a23.6.10.2969H}\ (\text{公开码表}\ ✓)$$
$$\text{状态表}: \texttt{/tmp/a23\_table.pkl}\ (14{,}671\ \text{行})\ ⚠️\ \text{（应转存到仓库内}\ ✓)$$
$$\text{总用时}: \mathbf{328}\ \text{s}\ (1\ \text{核},\ \text{pyguard 3072MB}\ ✓);\quad \textbf{未跑 solver}\ ✓$$
$$\text{校验}: \text{blocker census 三项基准（1248/7751/30247）与论文\textbf{逐数字一致}}\ ✓✓$$
$$
$$

## §7 边界（诚实标注）

- §1 为**论证**（逻辑完备性 ✓）；§2–§3 为**实算**（numpy/bitset ✓）
- **未跑 SAT/CP-SAT/ILP** ✓；**未扩大模型** ✓
- 本条线与 G/119 **无关** ✓（独立新题 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 枚举完备性论证 命中文件数=1    :: ./A23D4-CLOSURE-2026-09-26-depth-four-local-optimality-theorem.md 
技术词 depth-4 局部最优性定理 命中文件数=3    :: ./A23D4-CLOSURE-2026-09-26-depth-four-local-optimality-theorem.md ./A23D4-2026-09-26-P0-P1-P2-dossier.md ./A23D4-STEP235-2026-09-26-census-and-alpha-results.md 
技术词 4-deletion 状态表 命中文件数=2    :: ./A23D4-CLOSURE-2026-09-26-depth-four-local-optimality-theorem.md ./A23D4-STEP235-2026-09-26-census-and-alpha-results.md
```
- **本档新增**（扣自引后 = 0）：枚举完备性论证、depth-4 局部最优性定理、4-deletion 状态表 certificate
- **档案已有（引用，不列为提出）**：blocker、α(H_D)、|S(D)|
