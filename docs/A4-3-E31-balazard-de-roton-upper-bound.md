# A4-3 / E31 — The upper-bound side: Balazard–de Roton, and what the gap means for the criterion

**Registered item.** E31 (= A4-3 in the merge table): *"A4 补上界（Balazard–de Roton）"*.
Register note: *"我方 A4 唯一缺口"* — the **only** gap in the project's A4 alignment is the upper bound.
Register records original text **not read** ✗.

**Labels.** 核验 = verified here against a script in this repo ｜ 引用 = quoted from a source ｜ 推导 = derived here ｜ 猜想 = open.

**Retrieval status (honest).**
· The Balazard–de Roton **paper itself was NOT retrieved** ✗: *Sur un critère de Báez-Duarte pour l'hypothèse de
Riemann*, Int. J. Number Theory **6** (2010), no. 4, 883–903 (preprint HAL:hal-00345313, 2008); no open copy found
(HAL bot-blocked; no arXiv version located). **This is "not found", not "does not exist".**
· The **statement** below is quoted from a published source that states it explicitly and attributes it:
S. Bettin, J. B. Conrey, D. W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion*,
arXiv:1211.5191 (Sovrem. Probl. Mat. **16** (2012), 38–44). **This is the paper this repo abbreviates as "AIM《Optimal
Choice of Dirichlet Polynomials》"** — so the repo's existing A4 entry was already one step from the primary ✓ 核验.

## §1 The upper bound (exact statement as published)

```
【BCF, §1（引用）】"An open question is to determine what the rate of convergence of d_n to zero is, assuming the
   Riemann hypothesis. **Balazard and de Roton showed that, if the Riemann hypothesis is true, then**
        d_N²  ≪  (log log N)^{5/2 + ε} / √(log N)      for all ε > 0 ."
⟹ 上界是【条件性】的：**假设 RH**（不是无条件）✓
⟹ 而且它与下界不同**数量级**：下界 ~ 1/log N，上界 ~ (loglog N)^{5/2}/√(log N) —— 两者【不相遇】✓
【d_N 的定义（BCF, §1，与本项目 NB3 完全一致 ✓）】
   d_N² = inf_{A_N} (1/2π) ∫_{-∞}^{∞} |1 − ζ A_N(1/2+it)|² dt/(1/4+t²) ,
   inf 取遍长度 N 的 Dirichlet 多项式 A_N(s) = Σ_{n≤N} a_n n^{−s} ；RH ⟺ lim_N d_N² = 0 ✓
```

## §2 The proved lower bound that carries the constant (for comparison)

```
【BBLS 2000/2005（无条件，引用）】lim inf_{N→∞} d_N² log N  ≥  Σ_{ℜ(ρ)=1/2} 1/|ρ|²
   （和取【互异】的临界线零点）✓
【Burnol 2002（无条件，引用；Adv. Math. 170(1) 56–70）】
   lim inf_{N→∞} d_N² log N  ≥  Σ_{ℜ(ρ)=1/2} m(ρ)² / |ρ|² ,  m(ρ) = 零点重数 ✓✓
   —— 这是本项目 A4 的"已证下界 + 常数"（`A4-1`/`A4-NUMERIC` 已核验）✓
【猜想（BBLS/BCF，引用）】d_N² ~ (1/log N) Σ_{ℜ(ρ)=1/2} m(ρ)²/|ρ|² ；
   RH 之下 Σ m(ρ)/|ρ|² = 2+γ−log 4π = 0.046191417932… ；
   **若全部零点单重**则退化为 d_N² ~ (2+γ−log4π)/log N ✓
【⚠️ 一处必须写清的差别（推导）】Burnol 的下界带 **m(ρ)²**，故 RH 之下它 ≥ 2+γ−log4π；
   本项目 NB1 核验的 0.046191417932 是【单重/互异】情形（Σ 2/(1/4+γ_k²) → 0.0461877353，差 3.68e−6）✓。
   两者在"全部简单"假设下重合；一般情形下 Burnol 的界【更强】✓
【对照（推导）】平凡上界：取 A_N = 0 得 (1/2π)∫dt/(1/4+t²) = 1 ⟹ **d_N² ≤ 1 无条件** ✓
   （本项目实测 0.680 ≤ 1 ✓ 核验）——即**无条件侧只有 O(1)，没有任何衰减** ✗
   （注：DFMR I Prop. 7.5 在自己归一化下另有 d²_r < 1/(2−2r)，那是另一个测度，不可与本条混用 ⚠️）
```

## §3 The gap, and what it means for the criterion

```
                      下界（无条件，已证）        上界（仅 RH 下）
  量级                 C/log N                    (loglog N)^{5/2+ε}/√(log N)
  比值 上界/下界       ≈ (loglog N)^{5/2} · √(log N) / C      ⟹ **趋于 ∞** ✓
【推导】⟹ **两条界之间仍差一个无界的因子**；判据的"闭合"（两端相遇）**尚未达到** ✗
【关键含义（推导）】上界**不可能**是无条件的：
   d_N² → 0 本身【等价于 RH】⟹ 任何无条件给出 d_N² → 0 的证明【就是】RH 的证明 ✓✓
   ⟹ "上界衰减到零"这一侧**必然**是条件性的 —— 这不是技术懒惰，而是逻辑必然 ✓
   ⟹ 因此 A4 的缺口**不是可随手补上的引理**：它以 RH 为前提，或等价于 RH ✓
【本项目已覆盖的一侧（核验）】
   · 【下界侧】已覆盖 ✓：NB3 算出 d_N² = +0.6803（N=160）> 0，且 > C/log N = 0.00910 ⟹ Burnol 不等式成立 ✓；
     NB1 用 200 万零点独立复现常数 C ✓（`A4-NUMERIC`）。
   · 【上界侧】**未覆盖** ✗：项目从未构造上界；且其自身的 d_N²·log N 由 0.52 升到 3.45（N=2→160），
     **慢于 1/log N** ⟹ 连"数值上看到 C/log N"都没有做到 ✗（`A4-1` §3 已诚实标注）。
```

## §4 State of the art on closing it (why the upper side is a construction problem, not a wall)

```
【BCF, Theorem 1（引用·原文级）】若 RH 成立，且
      Σ_{|ℑ(ρ)|≤T} 1/|ζ′(ρ)|²  ≪ T^{3/2 − δ}   （某个 δ > 0）    (2)
   则（用**显式多项式** V_N(s) = Σ_{n≤N} (1 − log n/log N) μ(n) n^{−s}）
      (1/2π) ∫ |1 − ζ V_N(1/2+it)|² dt/(1/4+t²)  ~  (2 + γ − log 4π)/log N  ✓✓
⟹ **上界侧的当前最优 = RH + 一条"温和"矩假设**（Gonek / HKO 猜想 Σ_{|ρ|≤T} 1/|ζ′(ρ)|² ~ (6/π³)T
   使 (2) 显然宽裕）✓ —— 即：**两端在"RH + 矩假设"下已相遇于常数 C** ✓
【与项目 A4-2 的对账（核验）】V_N 的系数 (1 − log n/log N)μ(n) **正是** 项目 NB5 检验的形状：
   最优截断 **x = N（精确）**、a_n/μ(n) 与 (1−log n/log N) 相关 **r = +0.8525** ✓✓
   ⟹ 项目的数值发现与 BCF 的**显式最优多项式**吻合；差的只是【归一化】与【上界证明】✗（见 E26/A4-4）
【Grenander–Rosenblatt 类比（引用）】多项式 P：lim_N N δ_N² = Σ_{|ρ|=1} m(ρ)² ⟺ 零点在单位圆上/外 ✓
   —— BCF 指出其 Thm 1 的证明与多项式情形"very similar"，差别只在 ζ 有无穷多零点（正是 (2) 的来源）✓
```

## §5 Which side the project can now claim

```
【可以声称 ✓】· 下界侧（无条件）：项目数值满足 Burnol 下界，且独立复现常数 C ✓
             · 判据形式与"最优系数形状"与文献一致 ✓（NB5 对 BCF 的 V_N）
【不可以声称 ✗】· 任何上界（无条件或条件）—— 项目**没有**上界结果 ✗
             · 任何"项目数值支持 RH"的推论 —— d_N² 的绝对值仍高于渐近值约 75 倍，**归一化未定** ✗
【A4-3 处理完毕的判据】上界原文 not found；以**出版二级源**（BCF）的逐字陈述补齐，标注为 引用；
   原始推导（Balazard–de Roton 2010）**待取** ⚠️（HAL 被反爬；建议走图书馆/作者主页取 PDF）
```

## §6 Boundary

```
【核验】§1–§2 的 BCF 陈述与其对 BDR/BBLS/Burnol 的转述（arXiv:1211.5191 全文命中 ✓）；
   §3 的项目数字（NB1/NB3/NB4）；§4 与 NB5 的对账 ✓
【推导】§2 的平凡上界 d_N² ≤ 1；§3 的"上界必为条件性"论断与比值分析；§4 的"两端在 RH+矩假设下相遇"
【未做 ✗】未取得 Balazard–de Roton 原文；未取得 de Roton 2006/2007 原文；未改 L2；未输入 1/2；
   **未声称任何证明，更未声称本项目证明 RH** ✓
```
