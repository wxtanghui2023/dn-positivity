已查地图：已跑 scripts/prework_map_check.sh K(10,1) Q=1 packing 匹配 负系数 ⟹ 执行自 `docs/GRAMSIGN-2026-09-26-...md`（上界方向不可能 ✓）＋ `docs/B2QUOTA-2026-09-26-...md`（b=2 名额 ✓）＋ `docs/F14-DEDUP-2026-09-26-...md`（F 表 ✓）；本档为**纯推导**（唐先生 2026-09-26 19:51 指令「开 口 B，攻 N₂≥2」✓）；**未跑程序** ✓。
D0: 本档对象 = `Q=1` 分支的 packing/匹配结构（既有对象；非新对象）
D1: 0（产出为一条匹配定理、两条强参数界与问题归约）

# PACKB-2026-09-26 · 口 B 第一刀：匹配定理与强参数界

## §0 结论（先给）

```
$$\boxed{\textbf{(B-1 匹配定理)}\ Q=1\ \Longrightarrow\ \text{距离-1 图}\ G_1(C)\ \text{是\textbf{匹配}}\ \Longrightarrow\ d_1(c)\le1\ \forall c\in C\ (\text{分支 A})\ ✓✓}$$
$$\boxed{\textbf{(B-2 强界)}\ \Longrightarrow\ \mathbf{A_1\le59}\ (\text{分支 A})\ /\ \mathbf{A_1\le60}\ (\text{分支 B})\ ✓✓\quad(\text{档案原为}\ A_1\le142\ ✗)}$$
$$\boxed{\textbf{(B-3 推论)}\ A_1+A_2=143\ \Longrightarrow\ \mathbf{A_2\ge84}\ (A)\ /\ \mathbf{A_2\ge83}\ (B)\ ✓✓\quad(\text{原为}\ \ge3\ ✗)}$$
$$\boxed{\textbf{(B-4 结构)}\ \text{距离-2 对的\textbf{码字中点}必为}\ b\ge3\ \text{点}\ \Longrightarrow\ Q=1\ \text{下至多一个（即}\ z\text{）}\ ✓}$$
$$\boxed{\textbf{(B-5 判定)}\ \text{仍未获矛盾}\ ✗\ ——\ \text{但参数区间被\textbf{大幅收紧}，且首次出现\textbf{真正的 packing 型}约束}\ ✓✓}$$
$$
$$
```

---

## §1 (B-1)(B-2) 匹配定理与强界的推导（本档核心 ✓）

```
$$\textbf{关键观察}:\ c\in C\ \Longrightarrow\ b(c)=|C\cap B_1(c)|=1+d_1(c)\ \Longrightarrow\ \delta(c)=b(c)-1=\mathbf{d_1(c)}\ ✓✓$$
$$\qquad(\text{因}\ B_1(c)\ \text{含的码字} = c\ \text{自身}\ +\ \text{距离-1 的码字邻}\ ✓)$$
$$\textbf{Q=1 的含义}:\ Q=\sum_x\binom{\delta(x)}2=1\ \Longrightarrow\ \text{恰一点}\ \delta=2,\ \text{其余}\ \delta\le1\ ✓\ (\delta\ge3\ \text{会给}\ \binom32=3>1\ ✗)$$
$$\textbf{分支 A}（z\notin C）:\ \text{唯一的}\ \delta=2\ \text{点是}\ z\ (\text{非码字}\ ✓)\ \Longrightarrow\ \forall c\in C:\ d_1(c)=\delta(c)\le1\ ✓✓$$
$$\qquad\Longrightarrow\ 2A_1=\sum_{c\in C}d_1(c)\ \le\ |C|=\mathbf{119}\ \Longrightarrow\ \boxed{\mathbf{A_1\le59}}\ ✓✓\quad(\text{匹配最多}\ \lfloor119/2\rfloor=59\ \text{条边}\ ✓)$$
$$\textbf{分支 B}（z\in C,\ d_1(z)=\delta(z)=2）:\ \text{其余码字}\ d_1\le1\ \Longrightarrow\ 2A_1\le2+118=\mathbf{120}\ \Longrightarrow\ \boxed{\mathbf{A_1\le60}}\ ✓$$
$$\qquad\text{结构:}\ \text{分支 A 全匹配; 分支 B = 一个}\ \text{V}\ \text{（}z\ \text{度为 2}）\cup\ \text{匹配}\ ✓$$
$$\textbf{结合恒等式}\ A_1+A_2=143\ ✗\ (\text{见 B2QUOTA}\ ✓)\ \Longrightarrow\ \boxed{A_2\ge84\ (A)/\ge83\ (B)}\ ✓✓$$
$$
$$
```

**⚠️ 与档案的关系（诚实标注）**：档案此前有 $A_1\le142$ ✓（来自 $\sum_{x\notin C}(b-1)=E-2A_1\ge0$ ✓）。
本档的 $A_1\le59/60$ **严格更强** ✓✓ —— 机制完全不同（档案用**全局计数**；本档用**逐码字度上界** ✓）。
⟹ **这是本日 119 线最实质的参数收紧** ✓✓

---

## §2 (B-4) 中点结构定理（本档新 ✓）

```
$$\textbf{定义}:\ \text{称}\ m\ \text{为距离-2 对}\ \{c,c'\}\ \text{的\textbf{中点}\ ⟺\ d(m,c)=d(m,c')=1}\ ✓$$
$$\textbf{定理}:\ m\in C\ \text{且}\ m\ \text{是某距离-2 对的中点}\ \Longrightarrow\ c,c'\in N(m)\ \Longrightarrow\ d_1(m)\ge2\ \Longrightarrow\ b(m)=1+d_1(m)\ \ge3\ ✓✓$$
$$\qquad(\text{无条件成立}\ ✓;\ \text{不依赖}\ Q=1)$$
$$\textbf{推论}:\ Q=1\ \text{下全部}\ b\ge3\ \text{点只有}\ z\ \Longrightarrow\ \text{至多一个码字可作为距离-2 对的中点}\ ✓$$
$$\qquad\text{分支 A}: z\notin C\ \Longrightarrow\ \boxed{\text{没有任何码字是距离-2 对的中点}}\ ✓✓$$
$$\qquad\text{分支 B}: z\in C\ \Longrightarrow\ \text{唯一可能是}\ z\ (\text{对}\ \{u,v\}\ ✓)$$
$$
$$
```

---

## §3 中点的**注入计数**（与档案恒等式一致，无新矛盾 ✗）

```
$$\textbf{(B-4) 的直接后果（分支 A）}:\ \text{所有距离-2 对的中点都是非码字}\ ✓;\ \text{且其}\ b\le2\ (\text{非}\ z\ ✓)\ \Longrightarrow\ b=2\ \text{恰等}\ ✓$$
$$\textbf{注入性}:\ \text{任一}\ b=2\ \text{的非码字}\ m:\ \binom{b(m)}2=1\ \Longrightarrow\ m\ \text{恰是一个距离-2 对的中点}\ ✓✓$$
$$\textbf{双重计数}:\ \sum_{\text{距离-2 对}}2\ =\ 2A_2\ =\ \sum_m\binom{b(m)}2\ (\text{仅中点})\ =\ \underbrace{3}_{z\ \text{的}\ \binom32}+\ \#\{x\notin C:b(x)=2\}\ ✓$$
$$\qquad\Longrightarrow\ 2A_2=3+(283-2A_1)\ \Longrightarrow\ \boxed{A_1+A_2=143}\ ✓\ （\text{与 B2QUOTA 恒等式同一}\ ✗\ \text{无新信息})$$
$$
$$
```

**⟹ 至此本档仍未产生矛盾 ✗** —— 计数层与恒等式层再次闭合 ✓（与 `GRAMSIGN` / `SUM-P1P4` 一致 ✓：**矩/计数层已饱和** ✓）。

---

## §4 问题归约（本档给出的最有用形式 ✓）

```
$$\textbf{目标}:\ N_2\ \ge\ 2\ (\Longleftrightarrow A_1+A_2\ge144\ \Longleftrightarrow Q\ge3)\ ✓$$
$$\textbf{归约（分支 A）}:\ N_2\ \text{中除}\ z\ \text{外的第二点只可能是}\ \begin{cases}\text{另一非码字}\ b=3,\ \text{或}\ \text{某码字}\ b=3\end{cases}$$
$$\qquad\text{而码字}\ b=3\ \Longleftrightarrow\ d_1(c)=2\ \Longleftrightarrow\ c\ \text{是某距离-2 对的中点（B-4）}\ ✓$$
$$\Longrightarrow\ \boxed{\text{分支 A 下}:\ N_2\ge2\ \Longleftrightarrow\ \exists\ \text{码字}\ c\ \text{带}\ d_1(c)\ge2\ \Longleftrightarrow\ \text{距离-1 图\textbf{不是}匹配}}\ ✓✓$$
$$\qquad\text{但 (B-1) 已证 Q=1}\ \Longrightarrow\ \text{距离-1 图是匹配}\ ✓\ \Longrightarrow\ \text{此路\textbf{自动关闭}}\ ✗\ ✓$$
$$\Longrightarrow\ \textbf{结论}:\ \text{在分支 A 内，"找第二个 }\delta{=}2\ \text{点"不能靠码字侧，只能靠}\ \textbf{非码字}\ b=3\ ✓$$
$$
$$
```

---

## §5 诚实判定（按唐先生 B6 三步协议 ✓）

```
$$\textbf{Step 1（固定唯一 }u\in S_2\text{）}:\ u=z\ ✓;\ \text{两分支已分类}\ ✓$$
$$\textbf{Step 2（列 forced witness）}:\ \text{分支 A:}\ y_{12},y_{13},y_{23}\ (b=2\ ✓);\ \text{分支 B:}\ w\ (b=2\ ✓)$$
$$\textbf{Step 3（能否共用 }u\text{）}:\ \text{这些 witness 是}\ b=2\ \text{点，\textbf{不是}}\ \delta{=}2\ \text{点}\ ✗\ \Longrightarrow\ \text{它们的存在与}\ N_2=1\ \textbf{不矛盾}\ ✗$$
$$\qquad\Longrightarrow\ \text{F 表（①）给出的 forced 点全部落在 }\ b=2\ \text{层，无法直接产出第二个 }\delta{=}2\ \text{点}\ ✗$$
$$\textbf{判定}:\ \text{口 B 第一刀\textbf{未闭合}\ ✗;\ 但产出两条硬结果（匹配定理 ＋ A_1\le59/60 强界）}\ ✓✓$$
$$
$$
```

---

## §6 下一步候选（本档列出，未执行 ✓）

```
$$\textbf{口 B-2（本档定位的主攻方向）}:\ \text{在分支 A 中寻找被强迫的}\ \textbf{非码字}\ b{=}3\ \text{点}\ ✓$$
$$\qquad\text{已知}:\ \text{① 的 22 个 forced }L_3\ \text{非码字全部被钉在}\ b\le2\ ✗;\ \text{需新的 forcing 机制}\ ⚠️$$
$$\textbf{口 B-3（新出现的可能口）}:\ \text{匹配结构 ＋ 覆盖条件联立}:\ 2A_1\ \text{个码字成对，其余孤立}\ ✓$$
$$\qquad\text{问}:\ \text{孤立码字（}\ d_1=0,\ b=1\ \text{即\textbf{私有点}}\ ✓\text{）在 119-码中的数目是否被上下夹住？}\ ⚠️$$
$$\qquad\qquad\text{若孤立码字数}\ =\ 119-2A_1\ \text{有独立上界，可反推}\ A_1\ \text{的下界}\ \Longrightarrow\ \text{与}\ A_1\le59\ \text{碰撞}\ ✓$$
$$\textbf{口 B-4}:\ \text{把 (B-2) 的}\ A_1\le59/60\ \text{与档案的}\ E-2A_1\ \text{型全局计数联立，重算全部既有界}\ ✓$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1 的 $\delta(c)=d_1(c)$ 为**恒等式** ✓；$Q=1\Rightarrow\delta\le2$ 且恰一点 $\delta=2$ ✓ 为定义性推理 ✓；$\Rightarrow A_1\le59/60$ 为**本档新推导** ✓✓
- §2 的 (B-4) 定理为**无条件成立** ✓（不依赖 $Q=1$）；其 $Q=1$ 推论为直接应用 ✓
- §3 的注入计数**未产生新信息** ✓（回到同一恒等式）—— 与 `GRAMSIGN`／`SUM-P1P4` 的"矩层饱和"结论一致 ✓
- §4 的归约为**本档给出**（分支 A：$N_2\ge2\iff$ 距离-1 图非匹配 ✓）；随后被 (B-1) 自动关闭 ✓（**这是一个真实的负面结果** ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 匹配定理     命中文件数=3    :: ./LJCR-B1-batch-E4-audit-and-cell243-RESOLVED.md ./RESEARCH-CONSTITUTION.md ./PACKB-2026-09-26-matching-theorem-and-strong-parameter-bounds.md 
技术词 中点结构定理 命中文件数=1    :: ./PACKB-2026-09-26-matching-theorem-and-strong-parameter-bounds.md 
技术词 非码字归约  命中文件数=1    :: ./PACKB-2026-09-26-matching-theorem-and-strong-parameter-bounds.md
```
- **本档新增**（扣自引后）：中点结构定理、非码字归约（各 1 文件 ✓）
- **档案已有（不得列为新命名）**：`匹配定理`（命中 3 档：LJCR-B1-batch-E4…／RESEARCH-CONSTITUTION／本档）⟹ 术语已存在，本档只是**在该语义下**给出 $Q=1$ 处的新结论 ✓
- **档案已有（引用，不列为提出）**：$A_1+A_2=143$、$E-2A_1$、$\delta(c)=d_1(c)$
