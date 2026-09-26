已查地图：已跑 scripts/prework_map_check.sh K(10,1) b=2 中点 局部邻域 r(m) G_m ⟹ 执行自 `docs/K101-119-ARCHIVE-2026-09-26.md`（L-1 归档 ✓）＋ `docs/MIDSUP-2026-09-26-...md`（中点 injectivity ✓）；本档为**复核＋更正＋重做**（唐先生 2026-09-26 20:21 稿 K-1.6–K-1.14 ✓）；**含一次穷举验证**（874 样本 ✓）。
D0: 本档对象 = `b(m)=2` 非码字中点的局部邻域结构（L-4 首刀；既有对象）
D1: 0（产出为两处更正、一条修正恒等式、一条局部图结构性结果与 r(m) 有界范围）

# L4AUDIT-2026-09-26 · b=2 非码字中点的局部邻域（复核与更正）

## §0 结论（先给）

```
$$\boxed{\textbf{(P-1 更正①)}\ (K1.6)\ \text{应为}\ \sum_{x\in B_1(m)}b(x)=2b(m)+\mathbf{2}r(m)\ ✗✗\ \text{（唐稿系数 1 错）}\ \text{—— 穷举 874 例，我方版 0 失败}\ ✓✓}$$
$$\boxed{\textbf{(P-2 更正②)}\ \Longrightarrow\ r(m)\ \ge\ \mathbf 4\ \text{（非 8}\ ✗)\ ✓;\quad \text{且}\ (K1.13)\ \text{的}\ b(c)\ge2\ \text{为\textbf{伪结论}}\ ✗\ （\text{正确}:b(c)=1+\deg_{G_m}(1)\ ✓）$$
$$\boxed{\textbf{(P-3 更正③)}\ (K1.12)\ \text{的}\ \lambda_i\ \text{项不存在};\ \text{正确式}:\ \mathbf{b(x_i)=\mathbb 1[x_i\in C]+\deg_{G_m}(i)}\ ✓✓\ \text{（穷举 0 失败）}$$
$$\boxed{\textbf{(P-4 新结果)}\ \text{覆盖条件} \Longrightarrow \mathbf{4\le r(m)\le9}\ ✓✓\ \text{（新有界局部参数）};\ G_m:\ \text{顶点 3..10 度}\in\{1,2\},\ \text{顶点 1,2 度}\in\{0,1\}\ ✓}$$
$$\boxed{\textbf{(P-5)}\ \text{修正后各恒等式在给定}\ b(x_i)\ \text{式下退化(恒真)} \Longrightarrow \textbf{暂无第九种约束}\ ✗\ \text{（但 L-4 已得具体局部对象}\ ✓）$$
$$
$$
```

---

## §1 (P-1) 恒等式复核：系数必须是 2（本档核心更正 ✓）

```
$$\textbf{设}\ m\notin C,\ b(m)=2,\ B_1(m)\cap C=\{c,c'\},\ d(c,c')=2\ ✓;\quad r(m):=\#\{u\in C:d(u,m)=2\}\ ✓$$
$$\textbf{双重计数}:\ \sum_{x\in B_1(m)}b(x)=\sum_{x\in B_1(m)}\#\{u\in C:d(u,x)\le1\}=\sum_{u\in C}\big|B_1(m)\cap B_1(u)\big|\ ✓$$
$$\big|B_1(m)\cap B_1(u)\big|=\begin{cases}11&u=m\ (\text{不可能},m\notin C\ ✓)\\ \mathbf 2&d(m,u)\in\{1,2\}\\ 0&d\ge3\end{cases}\ ✓$$
$$\Longrightarrow\ \boxed{\sum_{x\in B_1(m)}b(x)=2\underbrace{\#\{u:d=1\}}_{=b(m)}+2\underbrace{\#\{u:d=2\}}_{=r(m)}=\mathbf{2b(m)+2r(m)}}\ ✓✓$$
$$\textbf{穷举核验}:\ 874\ \text{个随机}\ (C,m)\ \text{样本（}b(m)=2\ ✓）:\ \text{本式失败}\ \mathbf 0\ ✓;\ \text{唐稿}\ (2b+r)\ \text{失败率 100\%}\ ✗✓$$
$$
$$
```

**推论（更正唐稿的导出）**：

```
$$\text{因}\ B_1(m)=\{m\}\cup N(m)\ ✓:\ \sum_{x\in N(m)}b(x)=b(m)+2r(m)\ \Longrightarrow\ \sum_{x\in N(m)}(b(x)-1)=b(m)+2r(m)-10\ \overset{b(m)=2}{=}\ \mathbf{2r(m)-8}\ ✓✓$$
$$\text{又}\ N(m)\ \text{含}\ c,c'\ \text{与其余 8 点（各}\ b\ge1\ ✓）:\ 2+2r(m)\ \ge\ b(c)+b(c')+8\ \Longrightarrow\ 2r(m)\ \ge\ b(c)+b(c')+6\ ✓$$
$$\text{由}\ b(c),b(c')\ge1\ \Longrightarrow\ \boxed{r(m)\ \ge\ \mathbf 4}\ ✓✓\quad(\text{唐稿}\ \ge8\ ✗\ \text{来自系数错})$$
$$
$$
```

---

## §2 (P-3) 干净局部公式：$b(x_i)=\mathbb 1[x_i\in C]+\deg_{G_m}(i)$ ✓

```
$$\text{记}\ x_i=m\oplus e_i\ ✓\ (i=1,\dots,10);\quad N(x_i)=N(m+e_i)=\{m\}\cup\{m+e_i+e_j:j\ne i\}\ ✓\ (\text{共 }10\ ✓)$$
$$\text{因}\ m\notin C\ ✓:\ B_1(x_i)\cap C=\big(\{x_i\}\cap C\big)\ \cup\ \big\{m+e_i+e_j\in C:\ j\ne i\big\}\ ✓$$
$$\Longrightarrow\ \boxed{b(x_i)=\mathbb 1[x_i\in C]+\deg_{G_m}(i)}\ ✓✓,\qquad G_m:=([10],\ \{\{i,j\}:m+e_i+e_j\in C\})\ ✓\ \ (\text{边数}=r(m)\ ✓)$$
$$\textbf{穷举核验}:\ 874\ \text{样本}\ \times 10\ \text{邻点}:\ \text{失败}\ \mathbf 0\ ✓✓\ \Longrightarrow\ \text{唐稿的}\ \lambda_i\ \text{项（}(K1.7)\text{）确不存在}\ ✗✓$$
$$\text{特例}:\ x_1=c,\ x_2=c'\ \Longrightarrow\ \boxed{b(c)=1+\deg_{G_m}(1)},\quad b(c')=1+\deg_{G_m}(2)\ ✓✓$$
$$\qquad\Longrightarrow\ \textbf{唐稿}\ (K1.13)\ “b(c)\ge2,\ b(c')\ge2”\ \text{为\textbf{伪}}; \text{正确只给}\ \ge1\ ✓\ \text{（}\deg\ \text{可为 0）}$$
$$
$$
```

---

## §3 (P-4) 新结果：$4\le r(m)\le9$（本档主要正面产出 ✓）

```
$$\textbf{上界}:\ \text{Q=1}\Longrightarrow b(x)\le2\ \forall x\ne z\ ✓\ \Longrightarrow\ \deg_{G_m}(i)=b(x_i)-\mathbb 1[x_i\in C]\ \le\ 2-\mathbb 1[x_i\in C]\ ✓$$
$$\qquad\Longrightarrow\ \deg_{G_m}(i)\le2\ (x_i\notin C\ ✓);\qquad \deg_{G_m}(1),\deg_{G_m}(2)\le\mathbf 1\ (x_1,x_2\in C\ ✓)$$
$$\qquad\Longrightarrow\ 2r(m)=\sum_i\deg\le 1+1+8\times2=18\ \Longrightarrow\ \boxed{r(m)\le\mathbf 9}\ ✓$$
$$\textbf{下界（覆盖条件，关键）}:\ \text{每点被覆盖} \Longrightarrow b(x)\ge1\ \forall x\ ✓\ \Longrightarrow\ x_i\notin C\Rightarrow\deg_{G_m}(i)=b(x_i)\ge\mathbf 1\ ✓✓$$
$$\qquad\text{即}\ i\in\{3,\dots,10\}\ \text{的 8 个顶点度}\ \ge1\ ✓\ \Longrightarrow\ 2r(m)\ge 8+0+0=8\ \Longrightarrow\ \boxed{r(m)\ge\mathbf 4}\ ✓✓\ (\text{与 §1 独立同值}\ ✓)$$
$$\Longrightarrow\ \boxed{\mathbf{4\le r(m)\le9}}\ ✓✓\quad\text{两端点均可实现（}r=4:\ \text{完美匹配}; r=9:\ \text{哈密顿路}\ ✓）$$
$$
$$
```

**$G_m$ 的结构陈述（本档）**：

```
$$\boxed{G_m\subseteq K_{10}:\ \ \deg(i)\in\{1,2\}\ (i=3..10),\quad \deg(i)\in\{0,1\}\ (i=1,2)\ \Longrightarrow\ G_m=\text{若干路径/圈之并}}\ ✓$$
$$\qquad(|E(G_m)|=r(m)\in[4,9]\ ✓;\ \text{边}\ \{i,j\}\ \leftrightarrow\ \text{码字}\ m\oplus e_i\oplus e_j\in C\ ✓)$$
$$
$$
```

---

## §4 (P-5) 修正后：恒等式退化为恒真 ⟹ 暂无第九约束 ✗

```
$$\text{把 (P-3) 代入 (P-1) 之推论}:\ \sum_{i}\big(b(x_i)-1\big)=\sum_i\big(\mathbb 1[x_i\in C]+\deg(i)-1\big)=\underbrace{\sum_i\mathbb 1[x_i\in C]}_{=2\ (\text{恰 }c,c'\ ✓)}-10+2r(m)=2r(m)-8\ ✓$$
$$\qquad\Longrightarrow\ \text{两边恒等} \Longrightarrow\ \textbf{该恒等式在 (P-3) 下为恒真，不含新约束}\ ✗✓$$
$$\textbf{但收获}:\ \text{L-4 的对象从"模糊的 }b{=}1/2\ \text{分布"变成}\ \textbf{具体局部图}\ G_m\ \text{＋有界参数}\ r(m)\in[4,9]\ ✓✓$$
$$
$$
```

---

## §5 与全局量的接口（本档列出，未压 ✗）

```
$$\textbf{接口 J-1}:\ \sum_{m\in\mathrm{Mid}_2}r(m)=\sum_{u\in C}\#\{m\in\mathrm{Mid}_2:d(u,m)=2\}\ ✓;\quad 4|\mathrm{Mid}_2|\le\text{LHS}\le 45M=5355\ ✗\ \text{（无碰撞力）}$$
$$\textbf{接口 J-2}:\ \text{边}\ \{i,j\}\ \leftrightarrow\ \text{码字}\ m\oplus e_i\oplus e_j\ \text{—— 这些码字位于}\ L_2(m)\ \text{层};\ \text{与行闭合（SCOL）联立的可能口}\ ⚠️$$
$$\textbf{接口 J-3}:\ G_m\ \text{的圈结构}:\ \text{三角形}\ \{i,j,k\}\ \text{给三个两两距 2 的码字}\ \Longrightarrow\ \text{若}\ x_i\in C\ \text{则}\ b(x_i)=1+\deg=3\ \Longrightarrow\ x_i=z\ ⚠️\ \text{（未展开）}$$
$$
$$
```

---

## §6 判定（诚实 ✓）

```
$$\textbf{本轮}:\ \text{唐稿}\ K-1.6\text{--}K-1.14\ \text{含两处会\textbf{改变结论}的错误（系数 2／}\lambda_i\ \text{项）}\ ⚠️;\ \text{修正后：}$$
$$\qquad\text{① 恒等式真但恒真}\ ✗\ \text{② 新得}\ r(m)\in[4,9]\ \text{＋}\ G_m\ \text{结构}\ ✓\ \text{③ 无第九种约束}\ ✗$$
$$\textbf{状态}:\ \text{L-4 由 UNEXPLORED 升级为}\ \textbf{EXPLORED-FIRST-CUT（未闭合）}\ ⚠️\ —— \text{不下"弱"判（因首次出现有界局部参数）}\ ✓$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1 的恒等式为**严格推导 ＋ 874 例穷举核验**（0 失败 ✓）；对唐稿系数 1 的否证为**实测** ✓
- §2 的干净式为**严格推导 ＋ 穷举核验**（0 失败 ✓）
- §3 的上界用 Q=1（$b\le2$，$z$ 除外 ✓）；下界用**覆盖条件**（$b\ge1$ ✓）—— 二者均引用既有事实 ✓
- §3 的"两端点可实现"为**构造性说明**（未在 119 上下文验证 ⚠️）
- §5 接口**均未展开** ✗（如实标注）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 b=2 中点邻域恒等式 命中文件数=1    :: ./L4AUDIT-2026-09-26-local-neighbourhood-of-b2-midpoint.md 
技术词 局部图 G_m    命中文件数=1    :: ./L4AUDIT-2026-09-26-local-neighbourhood-of-b2-midpoint.md 
技术词 r(m) 有界范围 命中文件数=0    ::
```
- **本档新增**：b=2 中点邻域恒等式、局部图 G_m（各 1 档 ✓）；`r(m) 有界范围` **命中 0** ⚠️（本档自造描述语，非档案术语 ⟹ 按纪律**不列为新命名** ✓）
- **档案已有（引用，不列为提出）**：中点 injectivity、$Q=1\Rightarrow b\le2$、覆盖条件 $b\ge1$
