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

**结论：矩条件（一/二/三阶）在 `|C|=119` 下不产生障碍** ✗ —— 存在满足全部恒等式的 δ-场 ✓（与"已知下界仅 107"一致：excess 矩族不足以排除 119 ✓）

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
