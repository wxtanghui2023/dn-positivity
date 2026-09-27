已查地图：已跑 scripts/prework_map_check.sh 三元组 W(x0) 星型 中点强制 ⟹ 读 `SCOL-2026-09-26-...`（F-1..F-5 ✓）、`FAILSET-2026-09-26-...`（§1–§3 ✓）、`PROPAGATION-2026-09-26-...`；本档 = **(119-甲) 三元组结构：支撑型强制 ✓ ＋ 全局退化为 δ-型 ⟹ STOP（第 13 次同向收敛 ✓）**。
D0: 本档对象 = 一个三重覆盖点 x₀ 所强制的带身份（坐标级）结构
D1: 2（**星型约束 ＋ 无共享强制 ✓**；**全局累加退化为 δ-型 ⟹ STOP ✓**）

# (119-甲) 三元组结构（2026-09-27）

## §0 原档逐字（唐先生要求 ✓，供逐行对照）

```
$$\textbf{SCOL-2026-09-26 关键式（逐字 ✓）}:\quad \text{(F-1)}\ e_l\ (l\ge4)\ \text{被 2 码字覆盖} \Longrightarrow b(e_l)=2\Longrightarrow \textbf{行}\ l\ \text{关闭}:\ \forall m:\{l,m\}\notin C\ ✓$$
$$\quad\text{(F-2)}\ \sigma(1){=}\sigma(2){=}j\Longrightarrow \{j,m\}\ (m\ge4,m\ne j,\ 6\ \text{点})\cup\{\{3,j\}\}\ \text{全非码字}\ (+7)\ ✓;\quad \text{(F-4)}\ A_2(z)+3A_3(z)\ge24\ ✓$$
$$\textbf{FAILSET-2026-09-26 关键式（逐字 ✓）}:\quad W(x)=\{c\in C:x\in B_1(c)\};\ \mathrm{holes}(S)=\{x:\varnothing\ne W(x)\subseteq S\}\ ✓$$
$$\quad \mathrm{holes}(\{c,c'\})=p(c)+p(c')+e(c,c'),\ e(c,c')=\#\{x:W(x)=\{c,c'\}\}\in\{0,1,2\}\ ✓;\quad \sum_{\{c,c'\}}e(c,c')=N_2\ ✓$$
$$\quad \Longrightarrow\ \boxed{\sum_{\{c,c'\}}|\mathrm{holes}(\{c,c'\})|=(M-1)N_1+N_2}\ ✓\ \text{（数值验证 }: (4,4)40 ✓,\ (5,7)150 ✓,\ (9,64)28224 ✓\text{）—— 注：该式\textbf{定义性}（}\sum_c p(c)=N_1\ \text{直接给出 ✓），\textbf{不含新信息} ✗}$$
$$
$$
```

---

## §1 三元组结构（**✓ 本档新，规范化无关**）

```
$$\text{设 }x_0\ \text{满足 }b(x_0)\ge3,\ \text{取 }c_1,c_2,c_3\in W(x_0)\ \text{互异 ✓};\ \text{平移令 }x_0=0\ ✓ \Longrightarrow \text{每个 }c_i\in B_1(0)=\{0\}\cup\{e_j\}_{j=1}^{10}\ ✓✓$$
$$\boxed{\textbf{(FA-1 ⭐星型约束)}\ \text{三个覆盖者\textbf{必同处一星}}:\ c_i\in\{0,e_j\}\ ✓ \Longrightarrow\ d(c_i,c_j)\in\{1,2\}\ \text{且}\ \text{型}=\begin{cases}(1,1,2)&\text{若 }x_0\in C\\ (2,2,2)&\text{若 }x_0\notin C\end{cases}\ ✓✓}$$
$$\qquad\text{（解释 }(119\text{-甲}) \text{要求的 "三中心距离型" ✓：}\textbf{不可能出现其它型} ✓）$$
$$\boxed{\textbf{(FB-1 ⭐⭐无共享强制)}\ \text{记 }x_0\notin C\ \text{情形}:W(x_0)\cap\{e_j\}=J\ (\ |J|=b(x_0)\ge3\ ✓);\ \text{对每对 }i<j\in J\ \text{记其\textbf{第二公共邻 }}z_{ij}=e_i{+}e_j\ ✓}$$
$$\qquad\Longrightarrow\ z_{ij}\ \text{两两\textbf{互异}} ✓\ (\text{因 }e_i{+}e_j\ \text{唯一决定 }\{i,j\}\ ✓),\ z_{ij}\notin\{0\}\cup\{e_l\}\ ✓;\ \text{且 }c_i,c_j\in W(z_{ij}) \Longrightarrow \boxed{b(z_{ij})\ge2}\ ✓✓$$
$$\qquad\Longrightarrow\ \textbf{本星内强制量}:\underbrace{\delta(x_0)\ge2}_{b\ge3}\ +\ \underbrace{\binom b2}_{\text{互异点、各 }\delta\ge1}\ ✓✓\ \text{（}b{=}3:\ \ge2{+}3{=}\mathbf 5\ ✓\text{）}$$
$$\qquad\textbf{含 }x_0\in C\ \text{情形}:x_0\ \text{与邻居对 }\ (0,e_i)\ \text{的公共邻只是二者本身 ⟹ 不产生新点 ✓};\ \text{邻居两两给 }\binom{|J|}{2}\ \text{个互异点 ✓ ⟹ 强制 }\ge2+\binom{|J|}{2}\ ✓$$
$$
$$
```

---

## §2 🔴 全局累加：退化为 δ-型 ⟹ **STOP**（按唐先生判据 ✓）

```
$$\text{把 }\mathrm{(FB\text{-}1)}\ \text{对全部 }b(x)\ge3\ \text{点求和}:\ \text{得 }\ \boxed{A:=\sum_{x:b(x)\ge3}\binom{b(x)}2\ \le\ \sum_{z:b(z)\ge2}\binom{b(z)}2}\ ✓\ \text{（因每个 }z\ \text{至多为 }\binom{b(z)}2\ \text{对服务 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{两端都是 }\delta\text{-型泛函} ✗ \Longrightarrow \text{被 profile 恒等式钉死（`SUM-P1P4`／`AMEND-30`／`GAPTHEORY` 十类 ✓）} \Longrightarrow \boxed{\textbf{δ-type convergence ⟹ STOP}}\ ✓✓$$
$$\qquad\textbf{为何 sharing 不可免（诚实 ✓）}:\ \text{不同 }x_0\ \text{的星可强制\textbf{同一个 }z} ✓ \Longrightarrow \text{只能得不等式（上式 ✓）、不能得等式/计数 ✓};\ \text{而该不等式对 }M{=}119\ \text{的 profile 只是相容 ✓ 无矛盾 ✗}$$
$$\qquad\Longrightarrow\ \textbf{第 13 次同向收敛 ✓}（新对象最后落回已知恒等式 ✓）；\text{与 }PROPAGATION\ \text{的 }"\text{不聚合}"\text{同根 ✓（sharing ✓）}$$
$$
$$
```

---

## §3 唯一未退化的残件（**✓ 值得记下**）

```
$$\textbf{残件 ✓}:\ \text{(FB-1) 的}\textbf{"无共享"}\ \text{是\textbf{星内}成立、且强制点由}\textbf{坐标对 }\{i,j\}\ \text{唯一决定 ✓} \Longrightarrow \text{这是\textbf{坐标级身份数据} ✓}$$
$$\qquad\text{若再叠加 }SCOL\ \text{(F-1) 的}\textbf{行闭合机制}（\text{某点的覆盖者集 = 某"行"的码字 ⟹ 饱和即关闭整行 ✓）\ \text{—— 该机制为\textbf{支撑型} ✓、且天然带坐标身份 ✓}$$
$$\qquad\Longrightarrow\ \textbf{可容许的下一形状}:\ \text{"若 }x_0\ \text{的星含 }J\ (|J|\ge3\ ✓)\ \text{且某行因饱和被关闭 ⟹ 该 }\binom{|J|}2\ \text{个强制点所在的坐标对全部被封 ⟹ 与 }z_{ij}\ \text{需被\textbf{二次覆盖}矛盾"}\ ⚠️\ \text{—— 尚未证，且须先核 }SCOL\ \text{的规范化是否可脱离 }Q{=}1\ \text{分支 ✓}$$
$$
$$
```

---

## §4 状态（**✓ 纪律**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{本档\textbf{未}产生新障碍 ✗};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：星型约束（$W(x_0)\subseteq\{0\}\cup\{e_j\}$）、无共享强制（星内 $\binom b2$ 个互异点各 $\delta\ge1$）、δ-型退化与 STOP 判定
- **档案已有（引用，不列为提出）**：SCOL-2026-09-26（F-1/F-2/F-4）、FAILSET-2026-09-26（§1–§3，定义性）、PROPAGATION-2026-09-26、SUM-P1P4、AMEND-30、GAPTHEOREM


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 星型约束     命中文件数=1    :: ./TRIPLE-119-2026-09-27-star-confinement-and-the-delta-type-stop.md 
技术词 无共享强制  命中文件数=1    :: ./TRIPLE-119-2026-09-27-star-confinement-and-the-delta-type-stop.md
```
- **本档新增**：星型约束（$W(x_0)\subseteq\{0\}\cup\{e_j\}$）、无共享强制（星内 $\binom b2$ 个互异点各 $\delta\ge1$）、$\delta$-型退化与 STOP 判定（见上方命中数；0 命中者为自造语／内部标签 ✓）
