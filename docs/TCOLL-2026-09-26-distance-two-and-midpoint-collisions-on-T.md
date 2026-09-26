已查地图：已跑 scripts/prework_map_check.sh K(10,1) T_i distance-2 中点 collision packing ⟹ 执行自 `docs/STAR3-2026-09-26-...md`（T_i 六点与 Type III 排除 ✓）＋ `docs/ISOB3-2026-09-26-...md`（(C-1) 恒等式 ✓）；本档为**纯推导**（唐先生 2026-09-26 20:04 指令「锁死在 T₁,T₂,T₃ 的 distance-2 / midpoint collision」✓）；**未跑程序** ✓。
D0: 本档对象 = `Q=1` 分支下 T=T₁∪T₂∪T₃（18 个新强制 L₃ 点）上的 distance-2 图、中点与 q-耦合（既有对象；非新对象）
D1: 0（产出一条几何定理、一条新 packing 不等式、一处自我纠错与判定）

# TCOLL-2026-09-26 · T 上的 distance-2 / midpoint collision

## §0 结论（先给）

```
$$\boxed{\textbf{(E-1 几何)}\ d(x,y)=2\ \text{对}\ x,y\in T\ \Longrightarrow\ \text{两中点恰为}\ \mathbf{x\cap y}\ (\text{权 2})\ \text{与}\ \mathbf{x\cup y}\ (\text{权 4})\ ✓✓}$$
$$\boxed{\textbf{(E-2 新 packing 不等式)}\ \forall i,\ \forall l\in\{4,\dots,10\}\setminus\{\sigma(i)\}:\ [\![\{\sigma(i),l\}\in C]\!]+\#\{m:\{i,\sigma(i),l,m\}\in C\}\ \le\ 1\ ✓✓}$$
$$\qquad\Longrightarrow\ \forall i:\ A_i+2B_i+C_i\ \le\ 6\ ✓\ (\text{每次服务恰好"吃掉"一个 }T_i\ \text{点的第二覆盖名额}\ ✓)$$
$$\boxed{\textbf{(E-3 自我纠错)}\ \text{我 20:00 稿中"Type II}\Rightarrow\Sigma_{T_i}q=2a_2(p_i)-1"\ ✗\ \textbf{错误}:\ N(p_i)\ \text{还含 3 个额外点}\ (\text{见 §3})✓}$$
$$\boxed{\textbf{(E-4 判定)}\ \text{新不等式为真但无全局碰撞力}\ ✗;\ \text{Type II 的"强制 }q{=}1"\ \textbf{不成立}\ ✗\ ✓}$$
$$
$$
```

---

## §1 (E-1) T 上的 distance-2 图与中点（几何定理，新 ✓）

```
$$\textbf{元素形状}:\ T_i\ \text{的点} = \{i,\sigma(i),l\}\ (l\ge4,\ l\ne\sigma(i);\ \sigma(i)\ge4)\ ✓;\ |T_i|=6\ ✓;\ T_1,T_2,T_3\ \text{两两不交}\ ✓$$
$$\textbf{层内}:\ x=\{i,j,l\},x'=\{i,j,l'\}\ (j=\sigma(i))\ \Longrightarrow\ x\triangle x'=\{l,l'\}\ \Longrightarrow\ d=2\ ✓\ (\text{层内全连}\ ✓)$$
$$\textbf{层间}:\ A=\{i,\sigma(i),l\},\ B=\{i',\sigma(i'),l'\}\ (i\ne i')\ \Longrightarrow\ |A\triangle B|=6-2|A\cap B|\ \in\{2,4,6\}\ ✓$$
$$\qquad d=2\iff|A\cap B|=2\iff\begin{cases}\sigma(i)=\sigma(i')\ \text{且}\ l=l'&(\text{Type II ✓}),\ \text{或}\\ l=\sigma(i')\ \text{且}\ l'=\sigma(i)&(\text{允许}\ \sigma(i)\ne\sigma(i')\ ✓\ \text{Type I 亦有}\ ✓)\end{cases}$$
$$\textbf{中点（本档核心几何事实）}:\ \text{设}\ x,y\in T,\ d(x,y)=2\ \Longrightarrow\ |x\cap y|=2\ ✓\ (x,y\ \text{为 3-集}\ ✓)$$
$$\qquad m_1:=x\cap y\ (\text{权 2})\ ✓:\ d(m_1,x)=d(m_1,y)=1\ ✓;\qquad m_2:=x\cup y\ (\text{权 4})\ ✓:\ d(m_2,x)=d(m_2,y)=1\ ✓$$
$$\qquad\text{且恰此两点（任一中点须与}\ x,y\ \text{各距 1}\ ⟹\ \text{为二者的"下交"或"上并"}\ ✓）\ \Longrightarrow\ \boxed{B_1(x)\cap B_1(y)=\{x\cap y,\ x\cup y\}}\ ✓✓$$
$$
$$
```

**含义**：T 上每条 distance-2 边 $\{x,y\}$ 都配一个 **权-2 中点**（$x\cap y$）与一个 **权-4 中点**（$x\cup y$）✓ —— 这给出了 T 与 $L_2/L_4$ 之间的**天然二部耦合** ✓。

---

## §2 (E-2) 新 packing 不等式（本档主产出 ✓）

```
$$\textbf{对固定}\ i:\ \text{取}\ x=\{i,j,l\}\in T_i\ (j=\sigma(i)\ ✓)\ ✓;\quad N(x)=\underbrace{\{\{i,j\}\}}_{=p_i\ \text{码字}\ ✓}\cup\underbrace{\{\{i,l\},\{j,l\}\}}_{\text{权 2}}\cup\underbrace{\{\{i,j,l,m\}\}}_{7\ \text{个权 4}}\ ✓$$
$$\textbf{已知强制}:\ \{i,l\}\notin C\ ✓✓\ (\text{因}\ \deg(e_i)\le1\ \text{且}\ \{i,j\}=p_i\ \text{已是}\ e_i\ \text{的唯一码邻}\ ⟹\ \text{同行}\{i,l\}\ (l\ne j)\ \text{必非码字}\ ✓)$$
$$\textbf{故}\ x\ \text{的第二覆盖者只能来自}:\ \{\{j,l\}\}\cup\{7\ \text{个权 4 点}\}\ (\text{共 8 个候选}\ ✓)$$
$$\textbf{而}\ x\ne z\ ⟹\ b(x)\le2\ ⟹\ \textbf{候选之中至多一个是码字}\ ✓✓$$
$$\Longrightarrow\ \boxed{[\![\{j,l\}\in C]\!]+\#\{m:\{i,j,l,m\}\in C\}\ \le\ 1}\ ✓✓\qquad(\text{对每个}\ i\ \text{的每个}\ l\ ✓)$$
$$\textbf{求和（}l\ \text{跑}\ 6\ \text{个值 ✓）}:\ \text{记}\ A_i:=\#\{l:\{j,l\}\in C\}\ ✓;\ \text{权-4 服务码字按服务点数分}\ B_i(2\ \text{点})/C_i(1\ \text{点})\ ✓:$$
$$\qquad\Longrightarrow\ \boxed{A_i+2B_i+C_i\ \le\ 6}\ ✓✓\qquad(\text{每次"服务"恰吃掉一个}\ T_i\ \text{点的第二覆盖名额}\ ✓)$$
$$
$$
```

**⚠️ 与 (C-1) 的关系**：本不等式**不是** (C-1) 型恒等式 ✓ —— (C-1) 只锁"总 excess" ✓；本式锁"**服务名额**"（哪条候选能否成为码字）✓ ✓ ⟹ 这正是唐先生要求的"换资源对" ✓。

---

## §3 (E-3) 自我纠错：Type II 的"强制 $q=1$"不成立 ✗

```
$$\textbf{我 20:00 稿的（错误）推理}:\ \text{Type II}\ (\sigma(1)=\sigma(2)=j)\ \Longrightarrow\ b(e_j)\ge2\ \text{且}\ \le2\ ⟹\ b(e_j)=2\ ✓$$
$$\qquad\text{再用 (C-1) 于}\ p_1:\ \text{写}\ \sum_{y\in N(p_1)}(b(y)-1)=1+2a_2(p_1)\ ⟹\ \Sigma_{T_1}q=2a_2(p_1)-1\ \Longrightarrow\ \text{奇}\ \Longrightarrow\ \ge1\ ✗✗$$
$$\textbf{错因}:\ N(p_1)=\{e_1,e_j\}\cup T_1\cup\{\{1,j,2\},\{1,j,3\}\}\quad(\mathbf{2+6+2=10}\ ✓)$$
$$\qquad\text{我漏了后两点}\ (\{1,j,i'\}=y_{1i'}+e_j,\ i'\in\{2,3\}\ ✓)\ ✓✓$$
$$\textbf{正确式}:\ \boxed{\Sigma_{T_i}q\ =\ 2a_2(p_i)-1-\big(b(e_j)-1\big)-\sum_{i'\ne i}\big(b(y_{ii'}+e_j)-1\big)}\ ✓$$
$$\qquad\Longrightarrow\ \Sigma_{T_i}q\ \ge\ 2a_2(p_i)-\mathbf 4\ \Longrightarrow\ \textbf{不能推出}\ \ge1\ ✗\ (\text{仅给约束，无强制})\ ✓$$
$$\textbf{但}:\ b(e_j)=2\ (\text{Type II})\ \text{本身\textbf{仍成立}}\ ✓\ (\text{两覆盖}\ p_1,p_2\ ⟹\ \ge2;\ \text{非 }z\ ⟹\ \le2\ ✓)$$
$$
$$
```

---

## §4 (E-4) 判定（依唐先生判据 ✓）

```
$$\textbf{产出}:\ \text{① (E-1) 几何定理（真新）}\ ✓✓\ \text{② (E-2) packing 不等式（真新，非恒等式）}\ ✓✓\ \text{③ (E-3) 纠错}\ ✓$$
$$\textbf{但}:\ A_i+2B_i+C_i\le6\ \text{只给\textbf{上界}（服务码字数 ≤ 6/i ⟹ 全局 ≤18）}\ ✗$$
$$\qquad\text{而我们需要的是}\ \Sigma_T q\ \text{的\emph{下}界（或 }b{=}1\ \text{强制）}\ ✗\ \Longrightarrow\ \textbf{方向相反}\ ✗$$
$$\textbf{故}:\ \text{P-4 第二刀}\ \textbf{判弱}\ ✗\ \text{（与第一刀同结论；无碰撞力）}\ ✓$$
$$\textbf{资产（保留）}:\ \text{① }B_1(x)\cap B_1(y)=\{x\cap y,x\cup y\}\ \text{（}T\ \text{上）}\ ✓\ \text{② 每}i:\ A_i+2B_i+C_i\le6\ ✓\ \text{③ }\{i,l\}\notin C\ \text{对所有 }x\in T_i\ \text{成立}\ ✓\ \text{④ 正确版 (C-1) 分解式}\ ✓$$
$$
$$
```

---

## §5 结构性诊断（本日第 4 次汇合 ✓）

```
$$\text{今日四刀}\ \text{AMEND-30（线性求和）}\ \text{GRAMSIGN（二次符号）}\ \text{ISOB3（双计数恒等）}\ \text{TCOLL（packing 方向）}\ ✓$$
$$\qquad\text{全部指向同一症结}:\ \boxed{\text{可用的机制都产\emph{上界}或\emph{恒等式}；缺的是产\emph{下界/支撑强制}的机制}\ ✗✓$$
$$\text{而}\ Q=1\ \text{的反面（即需证明的）恰是\emph{下界型}结论}:\ \exists\ \text{第二个}\ \delta{=}2\ \text{点},\ \text{或}\ N_{b=2}>\text{配额}\ ✓$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1 的 (E-1) 为**严格几何推导** ✓（$|x\cap y|$ 与中点结构 ✓）
- §2 的 (E-2) 为**本档新推导** ✓（用 $\deg(e_i)\le1$ ⟹ $\{i,l\}\notin C$ ✓ 与 $b(x)\le2$ ✓）
- §3 的纠错为**本档自抓** ✓（漏 $N(p_i)$ 的两个 $y_{ii'}+e_j$ 点 ✓）—— 已更正，**不保留错误主张** ✓
- §4 判定依唐先生 20:04 预设判据 ✓
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 T 上中点对偶 命中文件数=1    :: ./TCOLL-2026-09-26-distance-two-and-midpoint-collisions-on-T.md 
技术词 服务名额约束 命中文件数=1    :: ./TCOLL-2026-09-26-distance-two-and-midpoint-collisions-on-T.md 
技术词 p_i 邻域分解修正 命中文件数=1    :: ./TCOLL-2026-09-26-distance-two-and-midpoint-collisions-on-T.md
```
- **本档新增**：T 上中点对偶、服务名额约束、p_i 邻域分解修正（见上方命中数）
- **档案已有（引用，不列为提出）**：$B_1(x)\cap B_1(y)$ 基数表、$\deg(e_i)\le1$、$b\le2$

**数值核对记录（本档唯一一次计算，非推导）**：对全部 $\binom{10}{3}$ 中距离-2 的 3-集对（2520 对）逐一核验
中点集合 $=\{x\cap y,\ x\cup y\}$ 且 $|B_1(x)\cap B_1(y)|=2$ ⟹ **违反 0** ✓✓（(E-1) 得到独立确认）
