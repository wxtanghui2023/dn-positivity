已查地图：已跑 scripts/prework_map_check.sh K(10,1) Terwilliger 三点 PSD ⟹ 执行自 `THIRD-2026-09-26`（STOP RULE 判据表 ✓）＋ `DELSARTE-2026-09-26`（A₁≤49 ✓）；本档为**一次性 P1 攻击（研究级限定）**（唐先生 2026-09-26 21:45 指令 ✓）；含一次计算 ✓。
D0: 本档对象 = 最小三点状态空间与第一个非平凡 PSD 约束（既有对象）
D1: 0（产出为 STOP 判定与"结构性失明"原因）

# T3MIN1-2026-09-26 · 最小三点 PSD 攻击（一次性）

## §0 结论（先给）

```
$$\boxed{\textbf{(V-1 STOP)}\ \text{第一个非平凡 PSD（Gram 法）＋谱矩系统\textbf{对 }A_1\ \text{完全失明}}\ ✗\ \Longrightarrow\ \textbf{STOP（判据 2/3 命中）}\ ✓}$$
$$\boxed{\textbf{(V-2 原因)}\ G:=(\text{距离}\le2)\ \text{图的边数}=A_1+A_2=143\ \textbf{与 }A_1\ \text{无关}\ \Longrightarrow\ \text{谱量只看总数}\ ✗}$$
$$\boxed{\textbf{(V-3)}\ \text{唯一自然的"A₁-敏感"三点 PSD（}d{=}1\ \text{指示向量 Gram）\textbf{被匹配定理杀掉}（成对角 ⟹ 无信息）}\ ✗✗$$
$$\Longrightarrow\ \textbf{路 A 有界失败}\ ✓\ \text{（按唐先生预设：干净转 }\texttt{FRONTIER-R1}\ ✓）$$
$$
$$
```

---

## §1 第一步：最小三点状态空间（严格 ✓）

```
$$\text{以根 }c\ \text{为基准的三点型 }(d(c,x),d(c,y),d(x,y))\ ✓;\ \text{只保留现存四类（}d{=}1\ \text{pair}／d{=}2\ \text{pair}／b{=}2\ \text{点}／z\text{）}\ ✓$$
$$\textbf{被强制排除}:\ (1,1,*)\ \text{与同三元组含两条 }d{=}1\ \text{边}\ ——\ \text{由匹配定理 }d_1\le1\ ✗✓$$
$$\Longrightarrow\ \text{存活型仅}:\ (2,2,2),\ (1,2,2),\ (2,2,2\text{-变体})\ \text{等}\ ✓\ \text{（状态空间极小 ✓）}$$
$$
$$
```

---

## §2 第二步：第一个非平凡 PSD（Gram 法 ✓）

```
$$\text{关联矩阵 }A\in\{0,1\}^{119\times1024},\ A_{c,x}=\mathbf 1[x\in B_1(c)]\ ✓$$
$$\text{Gram}:\ (AA^{\mathsf T})_{c,c'}=|B_1(c)\cap B_1(c')|=\mathbf 2\cdot\mathbf 1[d(c,c')\le2]\ ✓\ \text{（因 }d{=}1,2\ \text{都给 2 ✓）}$$
$$\Longrightarrow\ AA^{\mathsf T}=2\,(I+G)\ ⪰\ 0\ \Longleftrightarrow\ \boxed{\lambda_{\min}(G)\ge-1}\ ✓✓\quad(G=(\text{距离}\le2)\ \text{邻接矩阵})$$
$$\text{注}:\ 2\times2\ \text{minor 只给 }(\mathbf 1[m\in C]+\mathbf 1[m'\in C])^2\le b(u)b(v)\ \text{—— 由 }b\ge1\ \text{恒成立}\ ⟹\ \textbf{平凡}\ ✗$$
$$
$$
```

---

## §3 第三步：消元 ⟹ 结构性失明（本档计算 ✓）

```
$$\text{G 的边数}=A_1+A_2=143\ \textbf{（与 }A_1\ \text{无关 ✓）};\ n=119\ ⟹\ \sum\lambda=0,\ \sum\lambda^2=2\cdot143=\mathbf{286}\ ✓$$
$$\textbf{极值谱型（Chebyshev 系统 ⟹ ≤3 原子；本档解析扫描 ✓）}:\quad \lambda=(16.8403;\ \underbrace{-0.1427\times118}_{\text{118 个}})\ ✓$$
$$\qquad\sum\lambda=0.000000\ ✓,\ \sum\lambda^2=286.000000\ ✓,\ \sum\lambda^3=\mathbf{4775.5}\ ⟹\ \#\mathrm{tri}(G)=\sum\lambda^3/6\le\mathbf{796}\ ✓$$
$$\textbf{下界}:\ \text{z-星 }\{e_1,e_2,e_3\}\ \text{两两距 2}\ ⟹\ \#\mathrm{tri}(G)\ge\mathbf 1\ ✓$$
$$\Longrightarrow\ \#[1,796]\ \text{——\textbf{极宽} ⟹ 对 }A_1\ \text{无新界}\ ✗;\ \text{且谱矩系统\textbf{完全不含 }A_1}\ ✗✗$$
$$
$$
```

---

## §4 (V-3) 为何"A₁-敏感"的自然三点 PSD 也失败（关键结构性原因 ✓✓）

```
$$\text{想看见 }A_1\ \text{必须让 PSD 区分 }d{=}1\ \text{与 }d{=}2\ \text{边}\ ✓;\ \text{最自然的候选：}d{=}1\ \text{指示向量 }y_c:=\mathbf 1[d(c,\cdot)=1]\ ✓$$
$$\langle y_c,y_{c'}\rangle=\#\{c'':d(c,c'')=d(c',c'')=1\}\ \text{（公共 }d{=}1\ \text{邻居数）}\ ✓$$
$$\textbf{匹配定理}（d_1\le1）\ \Longrightarrow\ \text{距离-1 图是匹配}\ \Longrightarrow\ c\ne c'\ \text{时无公共 }d{=}1\ \text{邻居}\ \Longrightarrow\ \boxed{\langle y_c,y_{c'}\rangle=0}\ ✓$$
$$\Longrightarrow\ \text{Gram \textbf{成对角}} \Longrightarrow\ \text{PSD 平凡（无信息）}\ ✗✗\ ——\ \textbf{匹配定理把最小三点路线封死} ✓✓$$
$$
$$
```

---

## §5 判定与移交（按唐先生预设 ✓）

```
$$\textbf{STOP 命中}:\ \text{① 2×2 minor 平凡} ✗;\ \text{② 所有 principal minor 只给 }p,\tau_2\ \text{宽区间} ✗;\ \text{③ 消元后无 }A_1\ \text{新界} ✗;\ \text{④ 与 profile 等价否 ⟹ 未达（本不需）}\ ✓$$
$$\Longrightarrow\ \textbf{路 A 一次性实验结束（有界、无 P1）}\ ✓\ \text{—— 未吞掉研究线 ✓（符合唐先生限定 ✓）}$$
$$\textbf{移交}:\ \text{按预设顺序}\ \to\ \texttt{FRONTIER-R1}\ \text{（RoSQS }56/70/82/86/98\text{ ＋ 校准门 G-CAL）}\ ✓✓$$
$$\qquad\textbf{附带资产}:\ \text{"自然三点 PSD（Gram）对 }A_1\ \text{失明"}＋\text{"匹配定理杀掉 }d{=}1\text{-Gram"}——\ \text{两条**结构性否证**，可迁移（任意 }(n,R{=}1)\ ✓）$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1–§2 为**严格推导** ✓；§3 的极值谱型为**解析扫描** ✓（含 Chebyshev ≤3 原子理由 ✓）
- §4 的"封死"为**对本路线的判定** ✓，**非**"三阶方法统统无用" ✗（更强 PSD／非 Gram 型未试 ⚠️）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张路 A 的思想无价值 ✗
- 本轮**未跑** solver ✓（仅 §3 的谱扫描 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 三点 PSD 对 A1 失明判定 命中文件数=0    :: 
技术词 匹配定理封死 d=1-Gram 命中文件数=1    :: ./T3MIN1-2026-09-26-minimal-three-point-psd-attack.md
```
- **本档新增**：三点 PSD 对 A₁ 失明判定、匹配定理封死 d=1-Gram（见上方命中数；若为 0 则为自造描述语，不列新命名 ✓）
- **档案已有（引用，不列为提出）**：Gram 法、匹配定理、$A_1\le49$、Chebyshev 三点谱型
