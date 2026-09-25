已查地图：已跑 scripts/prework_map_check.sh δ-场 covering excess 子空间计数 Krawtchouk van Wee ⟹ 本档为**新坐标系首次落地**（覆盖 excess / δ-场恒等式），与既有 D4-LANE-A（局部传播，已 CLOSED）明确区分；不开新研究方向，属既有格 `K(10,1)` 的坐标系更换。
D0: 本档对象 = `K(10,1)` 格的**标准守恒量（覆盖 excess δ-场）**（非新对象；为文献标准坐标系）
D1: 0（无新独立自由度；产出为恒等式体系、119 约束束、与自算界的差距量化）

# EXCESS-2026-09-25 · `K(10,1)` 的 δ-场（覆盖 excess）坐标系首次落地

## §1 坐标系更换（唐先生 22:59 定）

```
旧（CLOSED）:  D → A_j, A_k → 局部禁形         （局部约束传播 ✗）
新（本档）:    |C| → δ(x)=|C∩B₁(x)|−1 → 全局守恒 → 关联关系/Krawtchouk → 整数/同余约束 ✓
```

**修正声明**：不把 "LP/SDP" 写成已定主路线；标准坐标系 = **covering-excess / 子空间计数 / 支配构造** ✓

## §2 δ-场恒等式（本项目自算，且在真实 120-码上**逐条校验通过**）

```
$$\delta(x):=|C\cap B_1(x)|-1\ \ge0;\qquad \sum_{x}\delta(x)=11|C|-2^n$$
$$\textbf{关键球交事实（本项目已证）}:\ |B_1(c)\cap B_1(c')|=\begin{cases}11&c=c'\\2&d(c,c')\in\{1,2\}\\0&d(c,c')\ge3\end{cases}$$
$$\Longrightarrow\ \sum_x\binom{m(x)}{2}\ =\ \sum_{\{c,c'\}}|B_1(c)\cap B_1(c')|\ =\ 2(A_1+A_2)\quad(A_i:=\#\text{距离 }i\ \text{的无序码字对})$$
$$\Longleftrightarrow\ \boxed{\sum_x\delta^2+\sum_x\delta\ =\ 4(A_1+A_2)}\qquad(\textbf{二阶恒等式})$$
$$\text{三阶}:\ \sum_x\binom{m(x)}{3}=\sum_{\{c,c',c''\}}|B_1(c)\cap B_1(c')\cap B_1(c'')|\qquad(\text{可直接枚举按下式核验})$$
```

**120-码数值校验（全部 ✓）**

```
c=120: Σδ=296=11·120−1024 ✓｜δ 分布 {0:801,1:172,2:36,3:8,4:7}, max δ=4
A₁=50, A₂=149 ⟹ p₂=199
二阶: ΣC(m,2)=398=2p₂ ✓ ⟺ Σδ²+Σδ=4p₂ ✓
三阶: ΣC(m,3)=138=Σ三重球交（枚举）✓
```

> 注：上述即 Krawtchouk/关联方案展开的**等价形式**（同一双重计数的两种写法）✓

## §3 假设 |C|=119 的约束束（本档核心）

```
$$\textbf{硬约束}:\quad \sum_x\delta(x)=11\cdot119-1024=\boxed{285};\quad \delta(x)\in[0,10];\quad \sum_jN_j=1024,\ \sum_j jN_j=285$$
$$\textbf{二阶}:\quad \sum\delta^2=4(A_1+A_2)-285\ \Longrightarrow\ \sum\delta^2\in[285,\ 2850],\quad A_1+A_2\in[142,\ 783]\ (\text{粗界})$$
$$\textbf{由 }\delta\ge0\ \text{与 }\sum\delta\ \text{固定}:\ \sum\delta^2\ge\sum\delta\ (\text{等号}\iff\delta\in\{0,1\}\ \text{全体}),\ \text{且}\ \sum\delta^2\le10\sum\delta$$
```

**结论（按唐先生 2026-09-25 23:03 修正）**：这些恒等式的**必要条件区间未排除 `119`** ✓；
但**不得**写成"存在满足全部恒等式的 δ-场"✗ —— 目前**未**证整数可行（除非代码级三阶交谱实际给出可行整数解）✓
与"已知下界仅 107"一致：excess 矩族本身不足以排除 119 ✓

## §4 本项目自算的子空间计数界（诚实结果）

```
方法（自推）: 对每个 m-面（Q_m 的嵌入），其 2^m 顶点需被半径-1 球覆盖，最少需 τ(m) 个球
              求和得 |C|·K_m ≥ τ(m)·(面数)  ⟹ |C| ≥ τ(m)·C(n,m)2^{n−m}/K_m
结果（n=10, 自算）:
  m=2: τ=2, 面数 11520, K=405  ⟹ c ≥ 57
  m=3: τ=2, 面数 15360, K=960  ⟹ c ≥ 32
  m=4: τ=4, 面数 13440, K=1470 ⟹ c ≥ 37
⟹ **本项目自算的 m-面计数界远弱于平凡球覆盖 ⌈1024/11⌉=94，更弱于文献 107** ✗
```

**正式封口（Layer 1 CLOSED）**：由唐先生给出闭式 `K_m = C(10,m)(11−m)`、`N_m = C(10,m)2^{10−m}` ⟹
`|C| ≥ K(m,1)·2^{10−m}/(11−m)`，代 `K(m,1)` 值后**最强仅 m=0 给 ⌈93.09⌉ = 94**，即**不超过平凡球覆盖** ⟹ 该线正式关闭 ✓

**诚实诊断**：单靠"每个 m-面需 τ(m) 球"再求和，损失过大 ✗；真正达到 107 的机制是
**更精细的 excess/密度 + 子空间计数耦合（van Wee / Haas 型）**，本档**未能**自行复现该强度 ✓（不夸大）。

## §5 差距量化（回答"具体卡在哪里"）

```
现状梯度:  本项目 m-面计数 57–37  <  平凡球覆盖 94  <  文献下界 107  <  排除 119 需 ≥120  <  排除 120 需 ≥121
──────────── 我们在这里 ↑                                  文献在这里 ↑              目标在这里 ↑
```

⟹ **要么**取得 van Wee/Haas 型不等式的**准确形式**（需原文；按惯例请唐先生提供 PDF/地址 ✓），**要么**走**构造路线**（不需要下界机制 ✓）。

## §6 边界（诚实标注）

- 恒等式为**本项目自算并在真实码上校验** ✓；120-码数据来自 Kamenetsky 公开构造（本地已存 ✓）
- **未**复现 107 的强度；**不**主张本项目已具备产生新下界的能力 ✓
- τ(m) 为在"该面一邻域内"取中心的精确最小（m≤4 穷举 ✓）；若允许更远中心，界只会更弱（不改善结论）✓
- 不混同 `138/138`（紧型经验）与 `2307/9576`（一般反例）（§38F 纪律）✓

---

## 【技术词回查】（写于本档定稿前，`scripts/tech_word_check.sh` 逐字输出）

```
技术词 δ-场           命中文件数=1    :: ./EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md
技术词 covering excess  命中文件数=1    :: ./EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md
技术词 子空间计数  命中文件数=1    :: ./EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md
技术词 Krawtchouk       命中文件数=1    :: ./EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md
技术词 van Wee          命中文件数=5    :: ./EXCESS-...md ./MAPPING-2026-09-25-...md ./X1-AMEND-20-21-22-verdict-CLOSED.md
技术词 覆盖 excess    命中文件数=1    :: ./EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md
技术词 球交           命中文件数=3    :: ./EXCESS-...md ./B1b-owner-structure-engine-and-results-d1-d4.md ./C229-errata-B5-center-and-orbit-cardinality-and-second-sliver.md
```

**三分类标注**

- **本档新增**（首次使用，回查仅自命中）：`δ-场`、`covering excess`、`覆盖 excess`、`子空间计数`、`Krawtchouk`
- **档案已有（引用，不列为提出）**：`van Wee`（5 档，含 `X1-AMEND-20-21-22-verdict-CLOSED.md`）、`球交`（3 档，含 `B1b-...-d1-d4.md`）
- **通用词（不计）**：—
- **说明**：本档**不**主张任一技术词为本项目首创；`δ-场`等仅为本档内部对该坐标系的命名 ✓

---

## §7 ⭐ **Haas 2013 层式恒等式：校准通过 ＋ LP 结果（Layer 2 首测）**（2026-09-25 23:0x）

### §7.1 层式恒等式（唐先生给出，本档在真实 120-码上校验）

```
$$A_j(x):=|\{c\in C:d(c,x)=j\}|;\qquad \boxed{\delta_i(x)=(11-i)A_{i-1}(x)+A_i(x)+(i+1)A_{i+1}(x)-\binom{10}{i}}$$
$$\textbf{我方可独立推出该式}:\ \sum_{y\in L_i(x)}m(y)=\sum_{c\in C}|B_1(c)\cap L_i(x)|=A_i+(11-i)A_{i-1}+(i+1)A_{i+1}\ ✓\ (\text{与 }A_{-1}=A_{11}=0\text{ 约定一致})$$
```

### §7.2 ⭐⭐ **局部守恒律（本档新发现，已在 120-码上验证）**

```
$$\boxed{\sum_{i=0}^{10}\delta_i(x)\ =\ 11|C|-2^n\ =\ E\quad\textbf{对每一个中心 }x\ \textbf{都成立}}$$
$$120\text{-码}: E=296;\ \text{实测}\ \sum_i\delta_i(x)=296\ \textbf{对全部 }1024\ \text{个 }x\ ✓✓\ (\text{与 }x\ \text{无关！})$$
$$\text{且}\ \boxed{\delta_i(x)\ge0\ \text{对一切 }(x,i)}\ ✓\ (0\ \text{违例})\ \Longleftrightarrow\ \text{层式不等式族}\ (11-i)A_{i-1}+A_i+(i+1)A_{i+1}\ge\binom{10}{i}\ \text{在真实码上成立}$$
$$\text{层紧度}:\ \delta_i=0\ \text{的 }x\ \text{数}=\{i{=}0{:}801,\ i{=}1{:}6,\ i{=}9{:}6,\ i{=}10{:}801\}\ (\text{紧层在两端})$$
$$

### §7.3 **LP 首测：该族强度 = 平凡球覆盖** ✗

```
$$\text{变量 }z_c\in[0,1];\quad \text{目标 }\min\sum z_c;\quad \text{约束}:\ \text{全部 }(x,i)\ \text{的层式不等式}\ (11264\ \text{条})$$
$$\textbf{LP 最优值}=\mathbf{93.0909}=\frac{1024}{11}\ \Longrightarrow\ \textbf{该族给出的界 = 平凡球覆盖}\ \lceil94\rceil\ ✗\ (\text{远低于 107})$$
$$120\text{-码代入}:\ \min(\text{LHS}-\text{RHS})=0.000000\ \Longrightarrow\ \textbf{可行且处处紧}\ ✓\ (\text{族正确})$$
$$\textbf{全部 }1024\ \text{个变量分数}\ \Longrightarrow\ \text{LP 松弛极弱};\ \text{整数版（ILP）须另解}$$
$$

### §7.4 **校准门纪律（唐先生 23:03 定，本档采纳）**

```
$$\boxed{\text{模型必须先精确复现真实 120-码（}|C|{=}120,\ E{=}296,\ \delta\ \text{分布},\ 一/二/三阶恒等式},\ \text{子空间 incidence}\text{）才允许代 }c=119}$$
$$\text{本档达成}:\ \text{层式族已复现（}\delta_i\ge0\ \text{且}\ \sum_i\delta_i\equiv E\ ✓\text{）};\ \text{但\bf{强度不足}} ✗\ (\text{LP}=93.09)$$
$$\Longrightarrow\ \textbf{Layer 2 首测结论}:\ \text{单靠层式族不够};\ \text{必须引入\bf{子空间耦合变量}}\ (N_S(t)\ \text{与跨维 incidence})\ ✓$$
```

### §7.5 状态表（本格）

```
Layer 0  球总量 11|C|≥2^n                       ⟹ |C|≥94            （太弱）
Layer 1  m-面未加权计数                          ⟹ 最强仍 94          **CLOSED** ✓
Layer 2  层式不等式族（Haas 2013 局部形式）        ⟹ LP=93.09           **不足** ✗（校准✓）
Layer 2+ 子空间耦合变量 + incidence + 整数可行     ⟹ 未做                **下一步** ✓
```
