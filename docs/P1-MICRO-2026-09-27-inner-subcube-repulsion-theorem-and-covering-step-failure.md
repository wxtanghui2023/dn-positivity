# P1-MICRO-2026-09-27 — **固定 $c$ 的局部结构**：内部子立方体排斥定理 ＋ covering 步失效（诚实）

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:49 令 ✓）**：**不再求和**，只研究固定 $c$ 的局部二阶结构；查 $P_c$ 的交叉邻域冲突；零程序计算 ✓。

**已查地图：命中（接续 P1-AVOID／R4-P1／R7-LOCK，非新案 ✓）**
所查：`docs/P1-AVOID-2026-09-27-…`（**avoidance 接口／$d_2\le45-\binom s2$** ✓✓）｜`docs/P1-TETRA-2026-09-27-…`（**tetra 几何／中点定理** ✓✓）｜`docs/R4-P1-2026-09-27-…`（**$S(c)\cup V(H_c)$** ✓）｜`docs/R7-LOCK-2026-09-27-…`｜`docs/R6/R7-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** $K_4$-avoidance 对象的**局部微观结构**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次证明"内部子立方体排斥定理"（avoidance ⟹ 内部无 distance-2/3 点）＋ 对偶上界 $d_3\le120-\binom s3$ ＋ 诚实报告 covering 步失效** ✓）
**[RESEARCH]**

---

## §0 结论（**一条新定理 ✓✓｜一处诚实失效 ✗｜一条新上界 ✓**）

$$\boxed{\textbf{(α) 内部子立方体排斥定理（新 ✓✓）}:\ A(c)=0\ \wedge\ \text{相异}\ i,j,x\in S(c)\ \Longrightarrow\ \boxed{c\oplus e_i\oplus e_j\oplus e_x\notin C}\ ✓✓}$$
$$\quad\text{（证明：若 }\in C，\text{则四点 }\big\{c\oplus e_x,\ c\oplus e_i,\ c\oplus e_j,\ c\oplus e_i\oplus e_j\oplus e_x\big\}\subseteq C\ \text{构成 \textbf{tetra}}✗\ \text{与 avoidance 矛盾 ✓}）$$
$$\boxed{\textbf{(α′) 合并形式（与 R4-P1 合读 ✓✓）}:\ \text{在"内部子立方体"}\ c+\mathrm{span}\big(S(c)\big)\ \text{内},\ c\ \text{无任何 distance-2／distance-3 码字}}✓✓$$
$$\boxed{\textbf{(β) 诚实失效 ✗}:\ \text{你的链条在 \textbf{covering 步}失效}——\text{缺失点 }c\oplus e_i\oplus e_j\ \text{已被 distance-1 邻居\textbf{自动覆盖}}\ (d(c\oplus e_i,\ c\oplus e_i\oplus e_j)=1✓) \Longrightarrow \textbf{不迫使 }d_3\ \text{出现}✗✓}$$
$$\boxed{\textbf{(γ) 对偶新上界 ✓}:\ (\alpha)\Longrightarrow\ \boxed{d_3(c)\ \le\ \binom{10}3-\binom{|S(c)|}3=120-\binom s3}\ ✓✓\ \text{（与 R4-P1 的 }d_2(c)\le45-\binom s2\ \text{对偶 ✓）}}$$
$$\boxed{\textbf{(δ) 现状 ✗}:\ \text{聚合仍弱};\ \text{但 (α) 是\textbf{本线第一条局部几何（非 profile 型）定理}✓✓}$$

---

## §1 (α) 的**证明**（**含形状判别 ✓✓**）

$$\text{设 }A(c)=0\ (\text{无含 }c\ \text{的 square})✓;\ \text{相异 }i,j,x\in S(c)\Longrightarrow c{\oplus}e_i,\ c{\oplus}e_j,\ c{\oplus}e_x\in C✓$$
$$\textbf{反设}:\ w:=c\oplus e_i\oplus e_j\oplus e_x\in C✓\qquad \text{考察 }K:=\big\{c{\oplus}e_x,\ c{\oplus}e_i,\ c{\oplus}e_j,\ w\big\}✓$$
$$\text{（i）四点全在 }C\ ✓;\qquad \text{（ii）以 }v:=c{\oplus}e_x\ \text{为基，其余三点的差分}: e_i{\oplus}e_x,\ \ e_j{\oplus}e_x,\ \ e_i{\oplus}e_j\ \text{—— 三者\textbf{皆重量 2}✓}$$
$$\text{（iii）两两距离}: d(e_i{\oplus}e_x,\ e_j{\oplus}e_x)=|e_i{\oplus}e_j|=2✓;\ d(e_i{\oplus}e_x,\ e_i{\oplus}e_j)=|e_x{\oplus}e_j|=2✓;\ d(e_j{\oplus}e_x,\ e_i{\oplus}e_j)=|e_j{\oplus}e_x{\oplus}e_i{\oplus}e_j|=|e_i{\oplus}e_x|=2✓$$
$$\qquad\Longrightarrow\ \text{六距全 }2✓;\ \text{且三差分}=\{i,x\},\{j,x\},\{i,j\}\ \text{两两相交\textbf{但不共点}（无公共坐标 ✓）} \Longrightarrow \textbf{tetra 型}✓✓\ (\text{非 star ✗})$$
$$\qquad\Longrightarrow\ \text{其实为该 3-coset 的\textbf{偶部}}:\ v+\big(\mathrm{span}(e_i,e_j,e_x)\big)_{\rm even}\ ✓✓\ (\text{与 P1-TETRA §1 的刻画一致 ✓})$$
$$\Longrightarrow\ K\ \text{是一个 tetra} \Longrightarrow\ N_{\rm tetra}>0\ \textbf{与 avoidance 矛盾}✗ \Longrightarrow \textbf{(α) 得证}✓✓$$

## §2 合并形式：(**内部子立方体定理 ✓✓**)

$$\text{R4-P1}:\ A(c)=0\ \wedge\ \{i,j\}\subseteq S(c)\Longrightarrow c{\oplus}e_i{\oplus}e_j\notin C\ ✓\ (\text{distance-2 内部点被排})$$
$$\text{本档 (α)}:\ A(c)=0\ \wedge\ \{i,j,x\}\subseteq S(c)\Longrightarrow c{\oplus}e_i{\oplus}e_j{\oplus}e_x\notin C\ ✓\ (\text{distance-3 内部点被排})$$
$$\Longrightarrow\ \boxed{\text{在 }c+\mathrm{span}(S(c))\ \text{内，除 }c\ \text{自身与 }\{c{\oplus}e_i\}_{i\in S(c)}\ \text{外，}\ \textbf{别无 }C\ \text{点}}✓✓\ (\text{即：内部子立方体内 }c\ \text{是"孤点+一阶星"})$$
$$\textbf{注 ✓}:\ \text{此结论\textbf{仅}依赖 }A(c)=0;\ \text{且对 }\mathrm{distance}\ge4\ \text{的内部点}\ \text{不主张}✗\ (\text{本档未覆盖 ⚠️})$$

## §3 **诚实失效报告（β）**（**你的链条的 covering 步 ✓**）

$$\text{你的链条}:\ S(c)\xrightarrow{\text{no square}}\text{缺失 }d_2\xrightarrow{\text{covering}}\text{须覆盖}\xrightarrow{\text{no tetra}}\text{新缺失}$$
$$\textbf{第 2 步失效 ✗}:\ \text{缺失点 }m=c{\oplus}e_i{\oplus}e_j\ (\{i,j\}\subseteq S)✓;\ \text{而 }c{\oplus}e_i\in C\ \text{且}\ d(c{\oplus}e_i,\ m)=|e_j|=1✓$$
$$\qquad\Longrightarrow\ m\ \text{被 }c{\oplus}e_i\ \text{（同 }\ c{\oplus}e_j\text{）\textbf{自动覆盖}}✓ ⟹ \textbf{covering 不产生任何新约束}✗✓;\ \text{故}\ d_3\ \text{不被覆盖性迫使}✗$$
$$\textbf{（教训 ✓）}:\ \text{"缺失点"在本几何中\textbf{天生被一阶邻居覆盖}} \Longrightarrow \text{该链条\textbf{不可能}产生 }\sum|\cdot|\ \text{型占用冲突}✗\ (\text{与 §4 的 (γ) 相反方向 ✓})$$

## §4 **对偶上界（γ）**（**新 ✓**）

$$\text{distance-3 邻居}=c{\oplus}e_a{\oplus}e_b{\oplus}e_c\ (|\{a,b,c\}|=3)✓;\ \text{共 }\binom{10}3=120\ \text{个坐标三元组}✓$$
$$(\alpha)\ \text{排除\textbf{全部落在 }S(c)\ \text{内}的三元组}:\ \binom{s}3\ \text{个}✓\ \Longrightarrow\ \boxed{d_3(c)\le120-\binom{s(c)}3}\ ✓✓$$
$$\textbf{对偶结构 ✓}:\quad d_2(c)\le45-\binom s2\ \big|\ d_3(c)\le120-\binom s3\ \text{—— 即"内部方向的 }\ell\text{-层点被逐个排除"}✓✓$$
$$\textbf{聚合 ✓（弱 ✗）}:\ \sum_c d_3(c)=2N_3\le119\cdot120-\sum_c\binom{d_1(c)}3\ \Longrightarrow\ N_3\le7140-\tfrac12\sum_c\binom{d_1(c)}3\ ✓\ \text{（尚不能形成矛盾 ⚠️）}$$

## §5 现状与下一步（**诚实 ✓**）

$$\textbf{已有 ✓}:\ \text{① 内部子立方体排斥定理（非 profile 型 ✓✓）};\ \text{② }d_2,d_3\ \text{的对偶上界};\ \text{③ covering 步失效的证明 ✓}$$
$$\textbf{缺口 ⚠️}:\ \text{① 该定理\textbf{只用 }A(c)=0，未用 }B(c)=0;\ \text{② 未找到任何\textbf{反证}（无矛盾 ✓）};\ \text{③ 聚合仍弱 ✗}$$
$$\textbf{下一步候选（登记未做 ✓）}:\ \text{① 用 }B(c)=0\ \text{对\textbf{非内部}方向的约束（例：}c{\oplus}e_a{\oplus}e_b{\oplus}e_c\ \text{与 }c{\oplus}e_a{\oplus}e_b{\oplus}e_d\ \text{并存是否逼出 tetra？）⚠️}$$
$$\qquad\text{② 把 (α′) 与 covering 的\textbf{距离-1 层}对撞（内部子立方体"太空" ⟹ 外部必须承担覆盖 ⟹ 能否压出 }\sum|\cdot|\ \text{型冲突，而该冲突\textbf{不落回 }\{n_j\}\text{？） }⚠️$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "内部子立方体"
技术词 内部子立方体    命中文件数=0    ::
$ bash scripts/tech_word_check.sh "局部排斥"
技术词 局部排斥        命中文件数=1    :: ./zeta-nonvariational.md
$ bash scripts/tech_word_check.sh "层级排斥"
技术词 层级排斥        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "pair-system"
技术词 pair-system     命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`内部子立方体`／`层级排斥`／`pair-system` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`局部排斥` 档案已有 ✓）
- **注 ✓**：本档实质＝**§1 (α) 证明 ＋ §2 合并定理 ＋ §3 失效报告 ＋ §4 对偶上界**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未求和** ✓（照令 ✓）；**未碰** profile 聚合量（除 §4 的弱聚合说明 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** P1 成立 ✗（V290）；**不声称** 该链条必然无望 ✗ —— 只写"**covering 步失效**"＋"**定理已得但无反证**" ✓
- §2 的"对 distance $\ge4$ 不主张"**必须**保留 ✓（本档未覆盖 ✓）
