# 📐 **方向 A4 对齐档案**：Nyman–Beurling / Báez–Duarte 判据

**依据**：唐先生 22:48（"继续"→ 开始 A4）
**已读原文**：Beurling 1955（EuDML 摘要 ✓）｜Báez-Duarte 2003（EuDML 摘要 ✓✓）｜Burnol 2002（经 [BS04]/AIM 转述 ✓✓）｜AIM《Optimal Choice of Dirichlet Polynomials》（✓✓）｜arXiv:1805.06733v4（✓✓）｜MathOverflow 81308（✓✓）

---

## §1 ⭐ **判据（三个版本）**
```
【Nyman 1950 / Beurling 1955 ✓】RH ⟺ **1 ∈ closure(span{f_θ : θ ∈ (0,1)})^L²**，
   f_θ(x) = {θ/x} ✓；等价地：**区间 (0,1] 的特征函数 χ 可用 {1/(ax)} 的线性组合均方逼近**（a > 1 ✓）
【⭐ Báez-Duarte 2003 的强化 ✓✓】原文摘要："According to the well-known Nyman-Beurling criterion the
   Riemann hypothesis is equivalent to the possibility of approximating the characteristic function of
   the interval (0,1] in mean square norm by linear combinations of the dilations of the fractional
   parts {1/ax} for real a > 1. **It was conjectured and established here that the statement remains
   true if the dilations are restricted to those where the a's are POSITIVE INTEGERS.**" ✓✓✓
   ⟹ **只需可数族 ρ_k(x) = {1/(kx)}，k ∈ ℕ** ✓（**可计算化** ✓）
【定量对象 ✓✓】d_n := ‖χ − χ_n‖_H，χ_n = χ 在 H_n = span(ρ_k)_{1≤k≤n} 上的正交投影 ✓
   **RH ⟺ lim_{n→∞} d_n = 0** ✓；且等价于 χ_n 系数的特定渐近（[W07] ✓）
【等价】d_N² = inf_{A_N}(1/2π)∫_{-∞}^{∞}|1 − ζA_N(1/2+it)|² dt/(1/4+t²)（A_N 为长度 N 的 Dirichlet 多项式 ✓）
```

## §2 ⭐⭐⭐⭐ **定量结构（前沿的精确状态 ✓✓）**
```
【⭐ 猜想（BBLS [BS04] ✓）】**d_n² ~ C/log n，其中 C = 2 + γ − log(4π) ≈ 0.0462** ✓✓
   （更精确：d_N² ~ (1/log N)·Σ_{Reρ=1/2} **m(ρ)²/|ρ|²** ✓——该和 = 2+γ−log4π ✓）
【⭐ 已证下界（Burnol 2002 ✓✓）】**d_n² ≥ (C + o(1))/log n ——【同一个常数 C】** ✓✓
   前身（BBLS）：lim inf d_N² log N ≥ Σ_{Reρ=1/2} 1/|ρ|²（不同零点 ✓）；**Burnol 改进为含重数 m(ρ)²** ✓✓
   ⭐ AIM 论文原文："**This lower bound is believed to be optimal** and one expects that
      d_N² ~ (1/log N)Σ m(ρ)²/|ρ|²" ✓✓
【⭐⭐ 上界（条件性，Balazard–de Roton ✓）】若 RH 成立，则 **d_N² ≪ (log log N)^{5/2+ε}/√(log N)** ✓✓
⟹ ⭐⭐⭐ **【整个缺口都在【上界】一侧】**：
   · 下界：**~C/log N（已证，且被认为最优 ✓）**
   · 上界：**~(loglog N)^{5/2}/√(log N)（仅 RH 下 ✓）**
   · ⟹ **差距 ≈ √(log N)/(loglog N)^{5/2}** —— **相当大** ✓✓
```

## §3 ⭐⭐⭐⭐⭐ **A4 的难度【性质】与我们此前所有方向都不同**
```
【A1/A3 的难度】**刚性/不可能性**（符号不可得、惯性不可传递、聚合不足 ✓）⟹ 我们的 NO-GO 地图适用 ✓
【A4 的难度】⭐ **构造性** —— 下界已达最优常数 ✓，**缺口全在"构造出更好的逼近多项式"** ✓✓
⟹ ⭐⭐⭐⭐⭐ **即：A4 是一个【正向、可推进】的方向**：
   · 目标明确（把 d_N² 从 (loglog N)^{5/2}/√log N 推到 C/log N ✓）
   · 工具明确（Hilbert 空间投影 + **Burnol 投影公式** ✓ + 最优 Dirichlet 多项式 ✓）
   · **且已知最优系数的形状** ✓✓（见 §4）
   ⟹ **这是"我们的广度（数值 + 构造经验）"最可能发挥作用的类型** ✓✓✓
```

## §4 ⭐⭐ **已知的最优多项式形状（MathOverflow 81308 的答复 ✓✓）**
```
原文："…the optimal Dirichlet polynomial (the one that solves the optimization problem on the nose) has
   rather complicated arithmetic coefficients. However **when you take the length of the Dirichlet
   polynomial to go to infinity, each coefficient tends to (1 − log n / log x)**. One can then note that
   **the polynomial with those coefficients is also a minimizing polynomial**" ✓✓✓
⟹ ⭐ **最优系数渐近 = 1 − log n/log x** ✓ —— **具体、可用、可数值检验** ✓✓
```

## §5 ⭐⭐⭐ **与【我们的工作】的对齐（关键）**
```
【我方 A4 资产（据 REACH-TABLE）】**阈值测量：γ₀ ≲ N^δ** ✓ —— 即"d_N 变小所需的 N 与首个零点 γ₀ 的关系" ✓
【前沿的对应机制 ✓✓】"**The inequality d_n < ε provides zero-free regions for ζ**, see [Nik95] …
   and [DFMR13] for more general results on Dirichlet series." ✓✓
⟹ ⭐ **我们的阈值测量 = 该机制的【数值探针】** ✓（**方向一致** ✓）
【对齐结论】
   ① 我们的测量对象与前沿**同一** ✓；前沿有**显式下界（最优常数 ✓）**与**条件上界** ✓ —— 可逐项对照 ✓
   ② ⭐ **难度类型不同**：A1/A3 撞的是刚性墙 ✗；A4 是构造问题 ✓ ⟹ **我们的 NO-GO 教训在此【不适用】** ✓✓
   ③ **可执行任务**：用**数值**计算 d_N（中等的 N）+ 与 Burnol 下界对照 + 检验系数形状 (1−log n/log x) ✓✓
```

## §6 **方法对比**
| 环节 | 前沿 | 我们 |
|---|---|---|
| 对象 | Hilbert 空间投影距离 d_n ✓ | 同（阈值探针 ✓） |
| 工具 | **Burnol 投影公式（显式乘积公式 ✓）** + 最优 Dirichlet 多项式 ✓ | 数值测量 ✓ |
| 下界 | **C/log n（最优常数 ✓✓）** | 未做解析下界 ✗ |
| 上界 | **RH 下 (loglog N)^{5/2}/√log N** ✗ | 未涉 ✓ |
| 难度类型 | ⭐ **构造性** ✓✓ | 我们习惯处理**刚性** ✗ |
| 副产品 | **d_n < ε ⟹ 零自由区** ✓✓ | 与 A1 相关 ✓ |
⟹ **判断**：**我们的数值能力可立即用于【检验/探索最优多项式】** ✓；**但解析推进需学其投影工具** ✓
```

## §7 ⭐⭐⭐ **建议（A4）**
```
【建议 1·可执行（高优先）】**数值计算 d_N**（用 BD 形式或投影形式 ✓）：
   ① 与 Burnol 下界 C/log N 对照（看差多少 ✓）；② 检验最优系数 ~(1 − log n/log x) ✓
   —— 我方资产：**零点表（2M）+ 高效数值** ✓✓
【建议 2·解析工具】学 **Burnol 的投影公式**（[Bur02] + "Entrelacement de co-Poisson" [Bur07] ✓）
   —— 这是**显式的乘积公式**，与我方"从素数侧算零侧量"的关切**同型** ✓✓
【建议 3·战略定位】⭐ **A4 是【构造型】方向** ⟹ **与 A1/A3 的刚性墙相反** ⟹
   **"我们的广度 + 数值"最可能在此出成果** ✓✓（**建议列为候选主攻之一** ✓）
【建议 4·连接 A1】d_n < ε ⟹ 零自由区 ✓✓ ⟹ 与 A1 的"零自由 ⟹ Li 非负"**可能互补** ✓
```

## §8 **资料补足清单**
```
【✅ 已读】Beurling 1955（摘要 ✓）｜Báez-Duarte 2003（摘要 ✓✓）｜Burnol 2002（经转述 ✓✓）
   ｜AIM《Optimal Choice…》（✓✓）｜arXiv:1805.06733v4（✓✓）｜MathOverflow 81308（✓✓）
【✗ 高优先待读】**Balazard–de Roton**（条件上界的原始推导 ✓✓）｜**Burnol 2002 原文**（投影公式 ✓）
   ｜**[BBLS] 2000/2005**（Notes sur la fonction ζ III / 自相关研究 ✓）
   ｜**最新（2025-2026）**："The Báez-Duarte constant … under a weakened moment hypothesis on ζ'" ✓
   ｜"Spectral and Analytic Structure of the Nyman–Beurling–Báez–Duarte Approximation"（preprints 202506.0772 ✓）
【✗ 中优先】[Nik95]（d_n<ε ⟹ 零自由区 ✓ 我方连接的关键 ✓）｜[DFMR13]｜[W07]｜Bagchi 2006
   ｜Darses–Hillion（Vasyunin 公式 ✓）｜Bober ✓
【✗ 待对接】我方"阈值测量 γ₀ ≲ N^δ"的存档 → 与 Burnol 下界**逐项对照** ✓
```

## §9 边界
```
【原文级 ✓】§1 的 BD 判据陈述（其 EuDML 摘要 ✓✓）｜§2 的常数/下界/上界（AIM 论文 + arXiv:1805.06733 ✓✓）
   ｜§4 的系数形状（MathOverflow 答复 ✓✓）
【⚠️ 二手】Beurling 1955 与 Burnol 2002 **未见原文** ⚠️（经转述 ✓）
【⚠️ 未读】Balazard–de Roton、BBLS、Nik95、最新预印本 ✗
【⚠️ 我方定位】**我们的 A4 存档细节本轮未调取** ✗（"阈值测量"来自 REACH-TABLE 记录 ⚠️）⟹ 下一步应先调档 ✓
```
## §10 提交链
```
A1 收尾（1564bb6）→ 本篇（A4 对齐：判据 + 最优常数下界 + 构造型难度 + 数值可执行建议）
```
