已查地图：已跑 scripts/prework_map_check.sh K(10,1) A₂(z) A₃(z) incidence 求和 局部剖面 ⟹ 执行自 `docs/B2QUOTA-2026-09-26-...md`（①′ 的 A₂(z)+3A₃(z)≥21 ✓）＋ `docs/GRAM-LIFT-2026-09-25-...md`（ΣA_aA_b 一般式 ✓）；本档为**纯推导**（唐先生 2026-09-26 19:47 指令「P1 求两 incidence 总和 → P2 代入 → P3 联立 → P4 判弱」✓）；**未跑程序** ✓。
D0: 本档对象 = `Q=1` 分支下局部剖面不等式的**全局求和**（既有对象；非新对象）
D1: 0（产出为两条精确恒等式、一条结构性平凡定理与判弱结论）

# SUM-P1P4-2026-09-26 · Σ_z A₂(z) / Σ_z A₃(z) 与局部剖面的全局命运

## §0 结论（先给）

```
$$\boxed{\textbf{(P1)}\ \sum_zA_2(z)=M\binom{10}{2}=\mathbf{5355}\ ✓;\quad \sum_zA_3(z)=M\binom{10}{3}=\mathbf{14280}\ ✓\quad(\textbf{精确恒等式，与码结构无关})}$$
$$\boxed{\textbf{(P2)}\ \sum_z\bigl(A_2(z)+3A_3(z)\bigr)=5355+42840=\mathbf{48195}}$$
$$\boxed{\textbf{(P3)}\ \text{局部预算要求}\ \ge 21\times1024=\mathbf{21504}\ \Longrightarrow\ \text{实际}\ 48195\ \textbf{满足且松弛}\ \mathbf{26691}\ (\text{松弛率达 2.24 倍})}$$
$$\boxed{\textbf{(P4)}\ \text{按唐先生预设判据（"总 slack 很大 ⟹ 立即判弱"）}\ \Longrightarrow\ \textbf{判弱 ✗}\ ✓✓}$$
$$
$$
```

---

## §1 P1：两条 incidence 求和的精确推导（多重计数 ✓）

```
$$\textbf{定义}:\ A_j(z):=\#\{c\in C:\ d(z,c)=j\}\ ✓\qquad(|C|=M=119,\ n=10)$$
$$\textbf{换序多重计数}:\ \sum_{z}A_j(z)=\sum_{z}\sum_{c\in C}[\![d(z,c)=j]\!]=\sum_{c\in C}\#\{z:\ d(z,c)=j\}=\sum_{c\in C}\binom{10}{j}=M\binom{10}{j}\ ✓✓$$
$$\Longrightarrow\ \boxed{\sum_zA_1(z)=119\times10=\mathbf{1190}},\quad \sum_zA_2(z)=119\times45=\mathbf{5355},\quad \sum_zA_3(z)=119\times120=\mathbf{14280}}\ ✓$$
$$
$$
```

**⚠️ 关键结构性观察（本档核心）**：

```
$$\sum_zA_j(z)=M\binom{n}{j}\ \text{对}\ \textbf{任何}M\ \text{元码成立}\ \Longrightarrow\ \textbf{一切}基于\ A_j(z)\ \text{的\emph{线性}局部泛函, 其全局求和都与码结构无关}\ ✗✗$$
$$\Longrightarrow\ \text{任何"逐点线性不等式}\ \ge K"\ \ \text{求和后只给}\ M\sum_jc_j\binom{n}{j}\ \ge\ 1024K,\ \text{即}\ K\le M\sum_jc_j\binom{n}{j}/1024=\textbf{平均值}\ ✓$$
$$\Longrightarrow\ \textbf{只有局部界超过平均值才有内容}\ ✗\ ——\ \text{而本档要用的局部界是}\ 21,\ \text{平均值是}\ 47.07\ ✗\ ✓✓$$
$$
$$
```

---

## §2 P2–P3：代入联动用（判弱 ✓）

```
$$\textbf{局部（①′）}:\ \forall z\in\mathbb F_2^{10}:\ A_2(z)+3A_3(z)\ \ge\ 21\ ✓\qquad(\text{来自}\ \delta_2(z)\ge3\ \text{与}\ \delta_2=A_2+3A_3-18\ ✓)$$
$$\textbf{求和}:\ \sum_zA_2(z)+3\sum_zA_3(z)\ \ge\ 21\cdot1024=\mathbf{21504}$$
$$\textbf{实际值}: 5355+3\times14280=5355+42840=\mathbf{48195}\ \Longrightarrow\ \textbf{松弛}=48195-21504=\mathbf{26691}\ ✓$$
$$\textbf{等价}:\ \text{平均}\ \frac{48195}{1024}=47.07\ \text{ vs 界}\ 21\ \Longrightarrow\ \text{界低于平均}\ \mathbf{2.24}\ \text{倍}\ \Longrightarrow\ \text{无法反推}\ A_1+A_2\ \text{的任何上界}\ ✗$$
$$
$$
```

**⚠️ 为什么无法得到"$\Phi(A_1,A_2)<21504$"**：

```
$$\text{唐先生方案要求}:\ \sum_z(A_2+3A_3)\le\Phi(A_1,A_2)<21504\ \Longrightarrow\ \text{矛盾}$$
$$\text{但}:\ \sum_z(A_2+3A_3)=48195\ \text{是\textbf{精确恒等式}（与}\ A_1,A_2\ \text{完全无关）}\ ✗\ \Longrightarrow\ \textbf{不存在这样的上界}\ \Phi\ ✗✓$$
$$\text{根因}:\ \text{被求和的泛函是}\ A_j(z)\ \text{的\textbf{线性}组合；线性组合的求和被}\ M\binom{n}{j}\ \text{完全钉死}\ ✗✓$$
$$
$$
```

---

## §3 P4：slack 结构（按预设判据 ✓）

```
$$r(z):=A_2(z)+3A_3(z)-21\ \ge0\ ✓;\qquad \sum_z r(z)=48195-21504=\mathbf{26691}\ ✓✓$$
$$\text{判据（唐先生 19:47）}: \text{"若总 slack 很大，这条线立即判弱"}\ \Longrightarrow\ \text{slack}=26691\ \text{远超零}\ \Longrightarrow\ \boxed{\textbf{判弱 ✗}}\ ✓✓$$
$$
$$
```

**顺带：$\delta_2$ 的独立交叉核验（与档案层预算一致 ✓）**

```
$$\sum_z\delta_2(z)=\sum_z\sum_{x\in L_2(z)}(b(x)-1)=\sum_x(b(x)-1)\cdot\#\{z:d(z,x)=2\}=\binom{10}{2}\sum_x(b(x)-1)=45E=\mathbf{12825}\ ✓✓$$
$$\qquad(\text{档案层预算}\ \sum_x\delta_i(x)=\binom{10}{i}E\ \text{之}\ i=2\ \text{情形}\ ✓;\ E=285\ ✓)$$
$$\Longrightarrow\ \text{平均}\ \delta_2=12825/1024=\mathbf{12.53}\ \text{ vs 逐点界}\ 3\ \Longrightarrow\ \text{逐点 forcing 比平均弱}\ \mathbf{4.2}\ \text{倍}\ ✗$$
$$
$$
```

---

## §4 ⭐ **本档结构性定理（可复用资产 ✓）**

```
$$\boxed{\textbf{Theorem (incidence-sum triviality).}\ \text{设}\ |C|=M\subseteq\mathbb F_2^n,\ A_j(z)=\#\{c\in C: d(z,c)=j\}\ ✓}$$
$$\qquad\text{则对任意实数}\ c_j:\ \sum_z\sum_{j}c_jA_j(z)=M\sum_jc_j\binom{n}{j}\ \text{——\textbf{与}\ C\ \text{无关}}\ ✓✓$$
$$\textbf{Corollary 1}:\ \text{任何"\emph{线性}局部不等式}\ \sum_jc_jA_j(z)\ge K"\ \text{的求和版只等价于}\ K\le\text{平均值},\ \text{永不含全局信息}\ ✗$$
$$\textbf{Corollary 2}:\ \text{要把局部信息转成全局约束, 泛函必须\emph{至少二次}（}\sum_zA_aA_b\ ✓\ \text{——GRAM-LIFT 族}\ ✓,\ \text{其值含}\ D_r\ ✓）$$
$$\textbf{Corollary 3}:\ \text{但方向是问题}: \text{局部 forcing 给\emph{下界}；而}\ 119\ \text{所需的是}\ A_1+A_2\le143\ \text{的\emph{上界}}\ ✗$$
$$\qquad\Longrightarrow\ \text{"局部 forcing 求和"在\textbf{符号方向}上结构性不可能产出所需上界}\ ✗✓\ (\text{除非找到上界受控的补偿槽, 而}\ 3A_3(z)\ \text{无独立上界}\ ✗)$$
$$
$$
```

---

## §5 联立结果（P3 收口，诚实 ✓）

```
$$\textbf{Q=1 主线当前参数状态}:\ A_1+A_2=143,\ 3\le A_2\le143,\ A_1\le140\ ✓$$
$$\textbf{本档贡献}:\ \text{证明"用}\ A_2(z)+3A_3(z)\ge21\ \text{求和来压}\ A_1+A_2"\ \textbf{不可能}\ ✗✓\ (\S 4\ \text{Cor.1/3})$$
$$\textbf{未闭合}\ ✓;\ \text{但排除了一条看似很有希望的路线（省下后续无效工作量）}\ ✓✓$$
$$
$$
```

---

## §7 ⭐ **定量判据（本档给出的可复用门槛 ✓）**

```
$$	ext{设局部界为}\ f(z)\ \ge\ K\ orall z,\ 	ext{且}\ \sum_z f(z)=F\ (	ext{常为恒等式}\ ✓)\ \Longrightarrow\ 	ext{求和版只给}\ 1024K\le F$$
$$	extbf{门槛}:\ oxed{K\ \le\ ar f:=F/1024\ 	ext{时，该局部界	extbf{无全局内容}}}\ ✓✓\quad(	ext{严格}: 	ext{求和版恒成立, 不约束任何全局参数})$$
$$	extbf{本档实例}:\ f=\delta_2,\ K=3,\ F=12825\ \Longrightarrow\ ar f=12.53\ \Longrightarrow\ K=3<ar f=12.53\ \Longrightarrow\ 	extbf{无内容}\ ✗✓$$
$$\Longrightarrow\ 	extbf{若要使本路线有内容, 必须把逐点界提升到}\ K>ar f\ 	ext{即}\ \delta_2(z)\ge\mathbf{13}\ orall z\ 	ext{——	extbf{这是一个强得多的命题}}\ ⚠️$$
$$\qquad(	ext{现有 forcing 只给}\ 3;\ 	ext{量级差}\ 4.2\ 	ext{倍}; 	ext{而}\ \max_z\delta_2(z)\ 	ext{尚无上界估计}\ ✗)$$
$$
$$
```

**⟹ 路线判定（本档最终）**：

```
$$oxed{	ext{用局部剖面}\ A_2(z)+3A_3(z)\ge21\ 	ext{的	extbf{求和版}压}\ A_1+A_2:\ 	extbf{结构性不可能}\ ✗✓\ (\S 4\ 	ext{Cor.1} + \S 7\ 	ext{门槛})}$$
$$oxed{	ext{唯一可能的复活路径}:\ 	ext{把逐点界从}\ 3\ 	ext{提升到}\ \ge13\ 	ext{（或对非线性泛函找到\emph{上}界槽）——\ 二者当前都无入口}\ ✗}$$
$$
$$

## §6 边界（诚实标注）

- §1 换序多重计数为**严格**（无需程序 ✓）；两值与 $M\binom{n}{j}$ 的对应可手算核对 ✓
- §2–§3 为**代入与判据应用** ✓；slack 26691 为精确值 ✓
- §3 的 $\sum_z\delta_2(z)=45E$ 为**独立重推**，与档案层预算逐字一致 ✓
- §4 的平凡性定理为**本档新陈述**（内容为标准换序，但"对候选路线的封锁意义"为本档给出 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 incidence 求和平凡性 命中文件数=1    :: ./SUM-P1P4-2026-09-26-incidence-sums-and-the-triviality-of-local-profile-sums.md 
技术词 符号方向封锁 命中文件数=1    :: ./SUM-P1P4-2026-09-26-incidence-sums-and-the-triviality-of-local-profile-sums.md 
技术词 松弛率判据  命中文件数=1    :: ./SUM-P1P4-2026-09-26-incidence-sums-and-the-triviality-of-local-profile-sums.md 
技术词 逐点-平均门槛 命中文件数=0    ::
```
- **本档新增**：incidence 求和平凡性、符号方向封锁、松弛率判据、逐点-平均门槛（见上方命中数）
- **档案已有（引用，不列为提出）**：$\delta_k$ 层预算、$A_j(z)$、GRAM-LIFT 二次族
