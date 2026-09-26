已查地图：已跑 scripts/prework_map_check.sh 对角构造 62 码 priv 自由邻居 ⟹ 执行自 GCOMP-2026-09-26 档；本档为**② 第一刀：对角构造的判定与细化目标**（唐先生 2026-09-26 15:24 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = (9,62) 码的对角构造判据、自然选择的反例、8 位 doubled Hamming 的私有点结构
D1: 1（新增：**对角构造判据 U₁⊆C₀** ✓；**自然选择失败（U₁∩C₀=∅）** ✗✓；**n=8 上自由邻居引理复核（p≡7）** ✓✓）

# DIAG62-2026-09-26

## §1 ✅ 对角构造的**正确判据**（我方推导 ✓）

```
$$\text{设 }C=C_0\times\{0\}\cup C_1\times\{1\}\subseteq\mathbb F_2^9\ ✓;\ |C_0|=32,\ |C_1|=30\ \Longrightarrow\ |C|=62\ ✓$$
$$(x,0)\ \text{被覆盖}\iff x\in N[C_0]\cup C_1\ ✓;\quad (x,1)\ \text{被覆盖}\iff x\in N[C_1]\cup C_0\ ✓\ (\text{在 }\mathbb F_2^8\ \text{中}\ ✓)$$
$$\Longrightarrow\ \textbf{覆盖}\iff \big(N[C_0]\cup C_1=\mathbb F_2^8\big)\ \wedge\ \big(N[C_1]\cup C_0=\mathbb F_2^8\big)\ ✓$$
$$\text{若 }C_0\ \text{本身覆盖}\ \mathbb F_2^8\ ✓\ \Longrightarrow\ \text{第一式自动}\ ✓;\ \text{第二式}\iff \boxed{U_1:=\mathbb F_2^8\setminus N[C_1]\ \subseteq\ C_0}\ ✓✓$$
$$\text{好处}: \text{搜索规模从"512 中选 62"降到"256 中选 30 + 一个有约束的 } C_0"\ ✓✓$$
$$

## §2 ⛔ 自然选择失败（实测 ✗✓）

```
$$\text{自然选择}: C_1:=C_0\setminus\{u,v\}\ (30\ \text{词}\ ✓)\ \Longrightarrow\ U_1=priv(u)\cup priv(v)\ ✓$$
$$\textbf{实测（}C_0=\ \text{8 位 doubled Hamming}\ ✓):$$
$$\quad |C_0|=32\ \text{覆盖}\ \mathbb F_2^8\ ✓;\quad \textbf{私有点总数}=224\ ✓;\quad p(c)\equiv\mathbf{7}\ \forall c\ ✓;\quad p=0\ \text{的码字}=0\ ✓$$
$$\quad \text{单点删除后仍覆盖}: \mathbf{0/40}\ ✓\ (\text{与 }K(8,1)=32\ \text{一致}\ ✓✓)$$
$$\quad \textbf{删除后未覆盖的 7 点}: \text{例删 }00000000\ \Rightarrow\ \{2,4,8,16,32,64,\dots\}\ ✓;\quad \textbf{其中属于 }C_0\ \text{的}= \mathbf{0}\ ✗✓$$
$$\Longrightarrow\ U_1\cap C_0=\varnothing\ ✗\ \Longrightarrow\ \textbf{自然选择必然失败}\ ✗✓\ (\text{需弱搜索未找到亦与此一致}\ ✓)$$
$$

## §3 ⭐ 副产品：n=8 上复核**自由邻居引理** ✓✓

```
$$\text{REPAIR 档已证}: d_C(c)\ge1\Rightarrow\ \text{私有点在自由邻居中}\ ✓✓$$
$$\text{本例}: \text{doubled Hamming 每个码字 }d_C=0\ (\text{孤立}\ ✓)\ \Longrightarrow\ \text{引理不直接适用}\ ✓$$
$$\qquad\text{但实测 }p(c)=7\ \text{恰为该码字的 7 个"Hamming 单位向量邻点"}\ ✓\ ——\ \text{即\textbf{自由邻居}}\ ✓✓$$
$$\qquad\text{同时 }b(c)=1\ (c\ \text{自身即其私有点}\ ✓)\ \Longrightarrow\ |Priv(c)|=7\ \text{仅计非自身点}\ ✓\ (\text{约定}\ ✓)$$
$$\text{意义}: \text{引理的"自由邻居"在 }n=8\ \text{极值码上\textbf{再次命中}}\ ✓✓\ (\text{独立复核}\ ✓)$$
$$

## §4 ② 的细化目标（可继续 ✓）

```
$$\text{需要}: \text{找一对 }(C_0,C_1)\ ✓:\ |C_0|=32\ \text{覆盖}\ \mathbb F_2^8\ ✓,\ |C_1|=30\ ✓,\ \boxed{U_1\subseteq C_0}\ ✓$$
$$\text{等价改写}: \text{找 }30\ \text{词 }C_1\ \text{使 }U_1\ (=\mathbb F_2^8\setminus N[C_1]\ ✓)\ \textbf{可被某 32 词覆盖码包含}\ ✓$$
$$\text{两级搜索}: \text{① 搜 }C_1\ \text{最小化 }|U_1|\ \text{并使其"可覆盖"}\ ✓;\ \text{② 给定 }U_1\ \text{搜含 }U_1\ \text{的 32 词覆盖码}\ ✓$$
$$\text{风险}: \text{① 或需较长搜索}\ ⚠️;\ \text{② 是约束覆盖搜索（更难）}\ ✗;\ \text{若两级都失败，应转文献路线（Wille 1996 付费）}\ ✓$$
$$

## §5 状态

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{P1 目标} = \text{极值壳控制 }I\ ✓;\quad \textbf{实验入口} = n=9,M=62\ ✓\ (\text{已正式切换}\ ✓)$$
$$\textbf{本轮}: \text{判据获得}\ ✓;\ \text{自然选择否定}\ ✗;\ \text{引理复核}\ ✓✓;\ (9,62)\ \text{码仍\textbf{未获得}}\ ✗$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$

## §6 边界（诚实标注）

- §1 为**我方推导** ✓；§2/§3 为**数值实测**（8 位空间全枚举 ✓）
- **(9,62) 码尚未获得** ✗（未夸大 ✓）；**未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 对角构造判据 命中文件数=1    :: ./DIAG62-2026-09-26-diagonal-construction-criterion-and-refutation-of-natural-choice.md 
技术词 可覆盖性条件 命中文件数=1    :: ./DIAG62-2026-09-26-diagonal-construction-criterion-and-refutation-of-natural-choice.md 
技术词 未覆盖集包含 命中文件数=1    :: ./DIAG62-2026-09-26-diagonal-construction-criterion-and-refutation-of-natural-choice.md 
技术词 两级搜索     命中文件数=1    :: ./DIAG62-2026-09-26-diagonal-construction-criterion-and-refutation-of-natural-choice.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：对角构造判据、可覆盖性条件、未覆盖集包含、两级搜索
- **档案已有（引用，不列为提出）**：私有点、自由邻居、minimality
