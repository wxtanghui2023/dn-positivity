# E27 / A4-5 — The implication "d_N < ε ⟹ a zero-free region", and what the project would need

**Registered item.** E27 (= A4-5 in the merge table): *"d_n < ε ⟹ zero-free region"* (A4↔A1 connection).
Register row records source `[Nik95]` / `[DFMR13]` with **original text not read** ✗.

**Labels.** 核验 = verified here against a script in this repo ｜ 引用 = quoted from a source (wording marked) ｜
推导 = derivation performed in this note ｜ 猜想 = open / unproved.

**Retrieval status (honest).**
· Nikolski 1995 statement: obtained **verbatim as quoted by DFMR** ✗ (not from Nikolski's own paper).
· DFMR: **Theorem 2.1 / Theorem 2.2** retrieved from *Zero-free regions for Dirichlet series (II)* (DFMR II);
**Prop. 7.5 and the explicit distance functional d²_r** retrieved from *Zero-free regions for Dirichlet series* (DFMR I, §7).
· **NOT retrieved**: Nikolski, *Ann. Inst. Fourier (Grenoble)* **45** (1995), no. 1, 143–159 — not found in an open copy.
· Burnol 2002 and [DFMR13] equation numbers below are as recorded in this repo's `DOOR5c/DOOR5e/DOOR5f` archives 核验.

## §1 The precise statement (this is the "conversion theorem")

```
【Nikolski 1995 — as quoted by DFMR, §1】(引用)
  "let r > 0 and λ ∈ ℂ with ℜ(λ) > 0 be fixed parameters and let K̃_r be the subspace of
   L²((0,1), dx/x) spanned by functions E_{α,r} (0 ≤ α ≤ 1) built from fractional parts.
   Then the zero-free regions obtained by Nikolski are domains of the form
     (1.2)   r + { μ ∈ ℂ : |(μ − λ)/(μ + λ̄)|²  <  1 − 2ℜ(λ) d̃_r(λ)² },
   where d̃_r(λ) = dist(x^λ, K̃_r) is the distance in L²((0,1), dx/x) between x^λ and K̃_r."
  (the exact indexing of E_{α,r} was only partially legible on retrieval ⚠️; the region (1.2) is exact) ✓
```
```
【DFMR II, Theorem 2.1】(引用 = 核验 against the authors' own PDF)
  "Let λ ∈ Π_{σ₀}. Then the function L does not vanish on  r − σ₀ + D♯_r(λ)  where
     D♯_r(λ) := { μ ∈ ℂ : |(μ − λ)/(μ + λ − 2σ₀)|  <  √( 1 − 2(ℜ(λ) − σ₀) d♯_r(λ)² ) }."
⟹ 一条【点态】转换：**该点的距离越小 ⟹ 该点周围的无零点区域越大** ✓
   （ζ 时取 L = ζ, σ₀ = σ₁ = 0, φ = χ_{(0,1)}；DFMR I §7.1.1 写成 r + { |(μ−λ)/(μ+λ̄)| < √(1−2ℜ(λ)d_r(λ)²) } ✓）
```
```
【DFMR II, Theorem 2.2（完整判据）】(引用)
  在 φ̂ 于 Π_r 无零点、limsup log|φ̂(x+r−σ₀)|/x = 0、a₁ ≠ 0 之下，四者等价：
  (1) L 在 Π_r 上无零点 (2) ∃λ: d♯_r(λ) = 0 (3) ∀λ: d♯_r(λ) = 0 (4) K♯_r = L²_*((0,1), dt/t^{1−2σ₀})
  ⟹ (4) 即 Beurling–Nyman 型闭包判据 ✓ —— **判据与"d<ε ⟹ 圆盘"是同一对象的两种读数** ✓
```
```
【DFMR I, §7 · 显式距离泛函与平凡界】(引用)
  d²_r = min_{c_j, α_j} ∫₀¹ | t^{1−r} − t^r Σ_j c_j Σ_{n<α_j/t} χ(n) |² dt/t   ✓
  Prop. 7.5:  d²_r < 1/(2 − 2r)  （严格；平凡界 d²_r ≤ 1/(2−2r) 即取全部 c_j = 0）✓
\note: 该泛函是对【一切】有限组合取极小，**没有长度参数 N** ⚠️ —— 与项目的 d_N 不是同一索引对象（见 §4）。
```
```
【DFMR II, Cor. 2.3 · 更可算的形式】(引用)
  L 在圆盘 r − σ₀ + { |(μ−λ)/(μ+λ̄−2σ₀)| < √( 2(ℜ(λ)−σ₀) |d̃_{f_{A,r}}(λ)| / ‖f_{A,r}‖₂ ) } 上无零点 ✓
  ⟹ **半径 ∝ 距离/范数**：可用一个【具体测试函数】的投影残差来下界圆盘 ✓
```

## §2 Quantitative form: how a bound on the distance buys a width

```
【推导】把 (1.2) 区间的几何解出来。令 z = μ,  a = ℜ(λ) > 0,  R² = 1 − 2a d²（d = d_r(λ)）：
   |z − λ|² < R² |z + λ̄|²
   ⟺ |z|² (1−R²) − (zλ̄ + z̄λ)(1+R²) + |λ|²(1−R²) < 0
   ⟺ |z − cλ|² < (c²−1)|λ|² ,   c := (1+R²)/(1−R²) = 1/(a d²) − 1 .
⟹ 无零点区域是【一个圆盘】：
     圆心  cλ ,   半径  rad = |λ| √(1 − 2a d²) / (a d²)  ≈  |λ| / (ℜ(λ) · d²)   （d 小）
⟹ **定量转换律（本项的答案）**：要在点 λ 处得到半径 ρ 的无零点圆盘，需要
     d_r(λ)²  ≲  |λ| / ( ℜ(λ) ρ ) ,    且必须有  d_r(λ)² < 1/(2ℜ(λ))  （否则 R 不实，只剩半平面极限）
  · d → 0 ⟹ R → 1 ⟹ 圆盘 → 半平面 ℜ(μ) > 0（Nyman 的经典情形 ✓）
  · 数值例（推导，仅示意）：ℜ(λ)=1/2, d²=0.68 ⟹ rad ≈ 1.66|λ|（有限圆盘）；
    d²=10⁻³ ⟹ rad ≈ 2·10³|λ|。**宽度对 d² 是 1/d² 的强敏感** ✓
```
⚠️ 注意：这是【点态】转换 —— 得到的是**某个点周围的一个圆盘**，不是一条竖直的零自由带，
   也不是"验证到高度 T ⟹ 某参数范围"的放大器型转换（与 Li/Jensen 的 T² 型相反 ✓ 与 `DOOR5c` §3 的撤回一致）。

## §3 Are the constants explicit?

```
【核验·引用】· Nikolski 的 (1.2) 显式（只依赖 d̃_r(λ)）✓
   · DFMR 自称在【大 ℑ(λ)】处圆盘**大于** Nikolski 的：因 |φ̂(λ+r)| = O(|ℑ(λ)|^{−(1−σ₁)}) ✓
   · 显式应用 DFMR I Cor. 7.4 / (7.6)：取 α = 1/4 给出显式区域 ✓
   · 但 Cor 2.3 / Cor 7.4 的【数值】常数含 ‖f_{A,r}‖₂ 与 φ̂，**需对具体 φ、A 计算** ⚠️
⟹ 结论：**形式显式；数值常数需一次具体投影计算**（这正是项目数值能力可插手的地方）。
【链条（引用）】Nikolski 1995 → Burnol 2002 → de Roton 2006 (Bull. SMF 134) / 2007 (Trans. AMS 359) → DFMR 2013 ✓
   [DFMR13] = C. Delaunay, E. Fricain, E. Mosaki, O. Robert,
              Part I  arXiv:1101.1199 = Trans. AMS 365 (2013) 3227–3253 ;
              Part II arXiv:1112.0166 ("Zero-free regions for Dirichlet series (II)") ✓
```

## §4 What the project would need — and whether it is attainable at present degrees

```
【项目的量】d_N²（Báez-Duarte 形式，长度 N 的 Dirichlet 多项式，临界线上的单一 L² 距离）：
   N=160: d_N² = 0.680283663 ✓ (核验, NB3/NB4)
   d_N²·log N = 3.4526（N=160）；C/log N = 0.00910，C = 2+γ−log4π = 0.046191417932 ✓ (核验, NB1)
【要接入 (1.2) 必须跨过的三道门】
 (G1) 【归一化】项目的 d_N² 与 DFMR 的 d_r(λ)² **不是同一个归一化** ✗ ——
      项目档案已诚实标注："归一化待确认"；且实测 d_N²·logN 从 0.52 升到 3.45（慢于 1/logN）⟹
      当前数值**不能**直接代入 (1.2)。(核验/待定)
 (G2) 【对象不同】DFMR 的 d²_r 是对**无长度限制**的有限组合取极小；项目的 d_N 有长度参数 N ⚠️。
      若长度-N 类 ⊂ DFMR 测试类，则 d_N ≥ d_r，故 d_N ≤ ε 蕴含 d_r ≤ ε（可给出【保守】圆盘）——
      但这一包含关系**未在检索到的原文中确认**（不是"不存在"，是**未找到**）✗。
 (G3) 【截断地板】T = 400 的傅里叶截断、网格 h = 0.05 的固定地板 1/T = 0.0025 不足以解释 0.68，
      但**未排除**；需要 T ≫ N 的扫描（A4-1 §4 已列）✗。
【可达到性判断（诚实）】
   · 在 N=160、T=400、当前归一化下：**不可达** ✗ —— 代入 (1.2) 会给出平庸甚至空区域。
   · 需要的精度：由 §2，得到"半径 ~ 1 的圆盘"只需 d² ≲ 1/(2ℜλ) ~ O(1)（**很弱**）；
      但得到有意义的宽圆盘（rad ≫ 1）需要 d² ≪ 1 ⟹ 归一化必须先修好 ✓。
   · ⟹ 本项的**真正瓶颈不是精度，而是 (G1)+(G2) 的识别**；这是一个可执行的分析任务，不是超算任务 ✓。
【与 A1 的连接】若修好归一化并给出 d_N² < ε ⟹ 圆盘，则与 A1 的"零自由 ⟹ Li 非负"形成互补，
   但与 E30 的对账显示：**该连接是点态型（弱）**，不产生 T² 型放大器 ✓ (引用/推导)
```

## §5 Boundary — what this note does and does not establish

```
【核验】§1 的定理编号与陈述（DFMR I/II 自有 PDF；Nikolski 经 DFMR 引用）；§4 的项目数字（NB1/NB3/NB4）✓
【推导】§2 的 Apollonius 圆盘解与其 1/d² 宽度律；§4 的 (G1)–(G3) 清单
【未做 ✗】未读 Nikolski 原文（**not found** 开放版）；未读 DFMR I 的 §3–§6；未改 L2；未输入 1/2；
   未构造逼近多项式；**未声称任何证明，更未声称本项目证明 RH** ✓
【纪律】本项只登记"机制的精确形式 + 项目接入所需条件"，不给 RH 任何正负判断 ✓
```
