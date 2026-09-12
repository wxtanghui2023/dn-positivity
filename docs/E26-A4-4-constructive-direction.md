# E26 / A4-4 — The constructive direction, written up as a scoped opportunity

**Registered item.** E26 (= A4-4 in the merge table): *"A4 是【构造型】方向（缺口全在【上界】一侧）"*.
Register note: *"与 A1/A3 的刚性墙【性质相反】⟹ 我方广度 + 数值最可能在此出成果"* — flagged as 候选主攻 (candidate
main attack). Register records the Balazard–de Roton source as **not read** ✗ (now partly closed: see `A4-3-E31`).
**This note is a scoping document, not a result.** Whether to invest here is 唐先生's decision.

**Labels.** 核验 = verified here against a script in this repo ｜ 引用 = quoted from a source ｜ 推导 = derived here ｜ 猜想 = open.

## §1 Why this direction differs in kind from the others

```
【A1/A3 的难度 = 刚性】符号不可得、惯性不可传递、聚合不足 ⟹ 项目已建 NO-GO 地图（引用，A1/A3 对齐档案）✗
【A4 的难度 = 构造性】下界已达最优常数（Burnol ✓）**缺口全在"构造出更好的逼近多项式"** ✓
   · 目标明确：把 d_N² 从 (loglog N)^{5/2}/√(log N) 推到 C/log N ✓ (引用, A4-3/E31)
   · 工具明确：Hilbert 空间投影 + 显式最优多项式 V_N(s) = Σ_{n≤N}(1−log n/log N)μ(n)n^{−s} ✓ (引用, BCF Thm 1)
   · 且最优系数的形状**已知** ✓（项目 NB5 已数值确认 x = N、r = +0.8525 ✓ 核验）
⟹ 难度类型不同 ⟹ **项目的 NO-GO 教训在此【不适用】**（既不远不适用，也不保证可用 —— 见 §5）✓
```

## §2 What would count as progress — three levels, each with a success criterion

```
【L1 · 归一化（最廉价，最该先做）】把项目算的 d_N² 与文献对象**对上一个明确的因子**：
    成功判据：存在显式 k_N 使 d_N²(项目) = k_N · d_N²(文献)，且 k_N → 1（或 k_N 恒为已知常数）✓
【L2 · 数值复现渐近（中等）】在同一归一化下**数值看到** d_N² ~ C/log N：
    成功判据：d_N²·log N 随 N 单调下降并趋近 0.0462（当前相反：0.52 → 3.45 ✗ 核验）✓
【L3 · 真正的结果（最难）】给出一条**上界**（无条件或"RH + 温和矩假设"）⟹ 与 Burnol 下界相遇：
    成功判据：一个可陈述的定理，或把 (loglog N)^{5/2} 的指数**严格改小**（在 RH 下）✓
【⟹ 依 E30-2 的两轴判据】任何"进步"必须同时报告 ① 探针指数 h(n) ② 输入的**无条件性**——
   "为更大范围而放弃无条件性"不是进步，只是换了交易条件 ✓（引用, E30-2 §2）
```

## §3 The specific missing quantities

```
(M1) 【归一化因子 k_N】**完全缺失** ✗ —— 项目档案 `A4-1` §4 / `A4-2` §3 均诚实标注"归一化待确认"。
     可能来源：测度（dt/|s|² 与 dt/(1/4+t²) 的常数）、目标函数（1 还是 1/s）、T 截断地板、网格步长。
     → 这是本方向**唯一**的"已定位但未解"的技术缺口 ✓
(M2) 【显式上界的证明结构】BCF Thm 1 的两层条件：**RH** + **Σ_{|ℑρ|≤T} 1/|ζ′(ρ)|² ≪ T^{3/2−δ}** ✓ (引用)
     —— 第二层即使 RH 之下也**未证** ⚠️（Gonek/HKO 猜想 Σ 1/|ζ′(ρ)|² ~ (6/π³)T 使 (2) 宽裕，但那是猜想 ✓）
     ⟹ 上界侧的"完全无条件化"不是一个引理，而是**判据本身**（见 §5）
(M3) 【点态转换的显式常数】DFMR Cor 2.3 / Cor 7.4 的数值常数含 ‖f_{A,r}‖₂ 与 φ̂ ⟹ 需一次具体投影计算 ✓
     （见 `E27-A4-5` §3；这把 A4 与本项目熟悉的"有限维二次型 + 投影"范式接上 ✓ 引用）
```

## §4 What the project's existing machinery can already test

```
【核验·可复跑】· NB1：常数 C = 2+γ−log4π = 0.046191417932，用 200 万零点独立复现（差 3.68e−6，尾部解析吻合）✓
   · NB3：傅里叶核单次扫描算 d_N²（K(m,n) = g(log(n/m)) 平移不变；求解 K a = l，d_N² = 1 − lᵀa）✓
     已知答案校验：**符号跟随 μ(n)：N=160 时 95/98 个无平方因子指数一致** ✓（实现可信的关键 ✓）
   · NB4：N-趋势表（d_N²、d_N²·logN、μ 一致率）✓ ；NB5：最优系数形状（x = N 精确、r = +0.8525）✓
   · 缓存 data/nb3_grid_H0.050_T400.npz（8001 点）⟹ 重跑秒级 ✓
【⟹ 已有的、可立即用于"构造侧"测试的三件套】
   ① 一个**可信的 d_N² 计算器**（带 known-answer 校验）✓
   ② 一个**显式候选多项式** V_N（BCF）—— 项目还从未把它单独喂进核里 ✗（§6(A) 就是这件事）
   ③ 一张 **2M 零点表** —— 可用于把 C 从系数侧（Möbius 自相关）**反向**校验 ✓
```

## §5 The honest counter-argument (why this may still be as hard as RH)

```
【逻辑必然（推导）】d_N² → 0 ⟺ RH ⟹ **任何无条件证明 d_N² → 0 的"构造"就是 RH 的证明** ✓
   故上界侧若要做到【完全无条件】，它与猜想**同难**——这不是技术悲观，而是等价性本身 ✓
【文献自己的承认（引用）】Burnol 原文自述："**It is a disappointing fact that this theorem can be proven
   without leading to any new information whatsoever on the zeros lying on the critical line**" ✓✓
   —— 判据的**定性**版本不含零点信息；**只有定量版本（常数/速率）才带信息** ✓
【即便在 RH 之下（推导）】BCF 仍需一条未经证明的矩假设 (2)；该假设是 Gonek 型猜想的下游 ⟹
   上界侧实际有**两层条件性**：RH + 矩假设 ⚠️
【转换类型偏弱（引用）】DFMR/Nikolski 的 d<ε ⟹ 圆盘是【点态】型，不是 Li/Jensen 的 T² 型放大器 ⟹
   A4 与 A1 的连接是**弱连接**（`E27-A4-5` §4；`DOOR5c` §3 已撤回早期的 T² 普遍性主张）✓
⟹ **诚实结论**：值得投入的是 L1/L2（归一化 + 数值复现渐近）与 M3（显式常数），
   而 L3 的"无条件化"应当**明确放弃**、只做"RH 下的定量改进" ✓
```

## §6 The two or three most concrete next computations

```
(A) 【归一化对账 —— 最高优先，决定其余一切】
    量：I(V_N) := (1/2π)∫_{-∞}^{∞} |1 − ζ(1/2+it) V_N(1/2+it)|² dt/(1/4+t²)，
        V_N(s) = Σ_{n≤N}(1 − log n/log N) μ(n) n^{−s}（BCF 的显式多项式），
        与 NB3 的最优值 d_N² 之比 R(N) := I(V_N)/d_N²(N)，对 N = 20,40,80,160（复用缓存）✓
    成功判据：R(N) 稳定（散度收敛到一个可解释的常数；理想为 1）。若 R(N) 漂移 ⟹ 归一化因子 k_N 被暴露，
        可据其 N-依赖解析定位（测度常数 / T 地板 / 目标函数）✓
    工具：直接用 NB3 的核（V_N 只是 a_n 的一个具体选择，无需新的求积）⟹ **不写新脚本也能做**，或最小改动 ✓
(B) 【截断地板与 N-趋势 —— 检验 L2】
    量：d_N²(N,T) 表，T ∈ {400, 2000, 8000}（T ≫ N），N ≤ 400；报 d_N²·log N
    成功判据：d_N²·log N 随 N **单调下降**并进入 [C, 3C] = [0.046, 0.14] 区间（当前 3.45 且上升 ✗）。
    若仍上升 ⟹ 归一化错误（回到 (A)）或 h(n) 机制不同（须记录为负结果）✓
(C) 【点态转换的显式常数 —— 把 A4 接到 E27】
    量：在 λ = r + i·(所选高度)（如 r = 1/2, |ℑλ| = 10³, 10⁵）处，用 DFMR I Prop. 7.5 的单/少项上界
        估 d_r(λ)²，再按 `E27-A4-5` §2 的公式算无零点圆盘半径 rad = |λ|√(1−2ℜλ d²)/(ℜλ d²)
    成功判据：圆盘非空且与已验证零自由区域（Platt–Trudgian 区域 ✓ 引用）**不冲突**；
        并记录 rad 对 d² 的 1/d² 敏感度 ✓（这是可用初等计算完成、且第一次把 A4 与 E27 数值接上的步骤）
【排序理由】A 决定 B 与 C 是否有意义；C 只用初等公式、风险最低、可与 A 并行 ✓
```

## §7 Boundary

```
【核验】§4 的全部脚本与其输出（NB1/NB3/NB4/NB5，含 95/98 的 Möbius 校验）✓
【引用】BCF Thm 1 与 V_N（arXiv:1211.5191 全文命中 ✓）；Burnol 自述（经 `DOOR5f` 存档 ✓）；
   DFMR Thm 2.2 / Prop 7.5（经 DFMR 自有 PDF ✓）；E30-2 两轴判据（项目内部 ✓）
【推导】§2 的 L1/L2/L3 分层与判据；§5 的"无条件化 = RH"论证；§6(A)(B)(C) 的设计
【未做 ✗】未写新脚本（A/B/C 均复用既有核与缓存；若将来需要新脚本，按仓库约定放入 scripts/ 并附出处 docstring、
   输出 scripts/<name>.txt）；未改任何既有文件；未提交 git；未改 L2；未输入 1/2；
   **未声称任何证明，更未声称本项目证明 RH** ✓
【给唐先生的选项（不做方向性决策）】建议按 A → C → B 顺序投入；A 的产出（归一化因子）无论正负都有登记价值 ✓
```
