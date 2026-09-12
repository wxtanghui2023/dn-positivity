# A3 · 越过 0.682 · 第 3 次尝试（分块版）

> 状态：进行中（边做边写）。规则：每回合一个动作，逐步追加。
> 任务：第一优先子问题 = 无条件配对相关的最大 Fourier 支撑（无条件 vs 条件），逐条给作者·年份·编号+定理原文+[原]/[引]。
> 子问：支撑 1→1+δ 时用 Christoffel/SDP（复用 E8 `1−Λ₁`、`m₁²/m₂`）给 δ→比例曲线，及达到 0.69/0.70 所需最小 δ。

## 进度日志

### [1] 读 A3-third-moment-barrier.md（grep §7.2）
关键结论（均标注 [原]）：
- §7.2 = bandwidth-one 证书类天花板 ≈0.682。
- §7.2(e) 原话：prime-side evaluation of tr G̃^k by diagonal method 仅在 Rudnick–Sarnak 范围 X^k ≤ T^{2−ε} 可用；X≍T 时只允许 k=1。⟹ 无条件更高矩"一无所获"。[原]
- §7.2(f) 原话：Conditionally, HL*(k₀) hypothesis：对所有 k≤k₀，tr G̃^k = d·m_k(1)(1+o(1))；k=4 编码 Hardy–Littlewood 型渐近。 [原]
- §1.4 原话：improving on 2/3 by this route would require **pair-correlation information beyond Fourier support 1**. [原]
- §7.2 原话：if Montgomery's form factor were known on support (−λ₀, λ₀) for all λ₀, the method would certify 100% simple zeros on the line. [原]
- 三重相关无条件结果：未找到。n=2 Montgomery 1973；n=3 Hejhal 1994 (IMRN no.7, 293–302)；n>3 Rudnick–Sarnak 1996 (Duke Math. J. 81(2), 269–322)，支撑 |ξ₁|+⋯+|ξ_n| < 2。[原：Lagarias–Rodgers arXiv:1905.12123v3 转述]
- Lagarias–Rodgers Theorem 2.4 (Band-limited correlations) 明文「Assume RH」⟹ Hejhal(n=3) 与 RS(n>3) 均在 RH 条件下。[原]
- 近 5 年集中 k=2（Aryan 22、BGSTB24/25、GS25 arXiv:2511.20059、GS26、GLSS25、Lamzouri 2609.02882）；n=3 无条件化未找到。[未找到]


### [2] 读 A3-improvement-assessment.md（grep 支撑/support）与 E8-ceiling-0682.md
- Christoffel 两矩尖锐界：`1 − Λ₁(0) = m₁²/m₂ = (Σλ)²/(d·Σλ²)`（Cauchy–Schwarz，E8 §3 [核验]）。
- 数值表（A3-improvement-assessment §(b)）：Montgomery 归一化 0.6725；ceiling data 0.682；三原子/经验零点更差 0.538/0.623/0.649。[核验]
- 0.6725→0.682 的 0.01 = 同一泛函 + 同一两矩输入，用 Christoffel 而非单一标量 R(ψ)。越 0.682 需无条件三阶矩（X≍T）。[推导/引]
- 前沿 §7.2(d) 一般框架：矩已知到 k≤2m ⟹ n₊(G̃)/d 尖锐下界 = 1 − Λ_m(0)。[原]
- 前沿 §7.2(f)：m_k(1)=1, 4/3, 2, 13/4 (k≤4)、Λ₂(0;1)=5/36、HL*(4)⟹ 比例≥13/18≈0.7222。[原]

### [3] 关键引用（repo 内已存）
- [BGSTB24] Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, "An unconditional Montgomery theorem for pair correlation of zeros", arXiv:2306.04799 = Acta Arith. 214 (2024) 357–376, DOI 10.4064/aa230612-20-3。[原，摘要]
- [BGSTB25] 同上, "Pair correlation of zeros of the Riemann zeta function I: proportions of simple zeros and critical zeros", arXiv:2501.14545。[原]
- [Ary22] Aryan 2022（Fejér 核无条件性显式化）。[引]
- [CCLM17] Carneiro–Chandee–Littmann–Milinovich（Montgomery–Taylor 窗最优，Cor.14）。[引]
- [CGdL20]（RH 下 SDP，0.6792，用 form factor [−1,1] 外正性）。[引]
- [BHB13] Bui–Heath-Brown（19/27≈0.703，RH 下）。[引]
- 前沿 arXiv:2608.13637v2（bandwidth-one 证书类天花板 ≈0.682）。[原]

### [4] 已核验的 Christoffel 恒等式（复用 E8 脚本）
- m₁=1, m₂=4/3 ⟹ 1−Λ₁(0)=m₁²/m₂=3/4=0.75；Λ₂(0;1)=detH₂/detB₂=5/36=0.1389（与前沿一致 ✓）。
- 注意：13/18≈0.7222（HL*(4)）≠ 1−Λ₂(0)=31/36≈0.8611 ⟹ 前沿"比例"与 Christoffel 值有独立词典（§7.2 未读，不重建）。

### [5] 外部核验：BGSTB24 的支撑（arXiv 摘要/HTML + CIRM 摘要）
- BGSTB24 原文（arXiv:2306.04799v1 HTML）："…an unconditional version of Montgomery's result on evaluating sums over pairs of zeros for **even kernels with Fourier transforms supported in [−1,1]**. If we assume RH this agrees with the earlier version in [Mon73]." [原]
- CIRM 摘要（Suriajaya）："Montgomery's theorem states an asymptotic behavior of a function F(α) which captures the pair correlation … **in the interval [−1,1]** and he gave the now famous 'pair correlation conjecture' predicting the behavior of F(α) **beyond this interval**." [原]
- BGSTB24 Theorem 2：薄盒假设下 ≥60.8%；用 Montgomery–Taylor 核 j_M(α)（K̂(0)=j_M(0)=1.0061271908…）改进到 **61.7%**。 [原]
- 前沿 2608.13637 用 rank–trace 不等式免去薄盒假设，把无条件比例推到 0.6725/0.682。 [引]
- GLSS25（Goldston–Lee–Schettler–Suriajaya, "Pair Correlation Conjecture for zeros I: simple and critical zeros"）：配对相关猜想本身 ⟹ 渐近 **100%** 零点简单且在线上。 [原，ProofAtlas 转述]

## 【第一优先子问题 · 答案】无条件配对相关的最大 Fourier 支撑

### 结论（一句话）
**配对相关（2 点，Montgomery form factor）可证的最大 Fourier 支撑 = 1（|α|≤1 / 核 Fourier 支撑 [−1,1]），无条件（BGSTB24）与 RH 条件（Montgomery 1973）相同；支撑 >1 即"配对相关猜想"，即使在 RH 下也未证。**

### 逐条（作者·年份·编号 + 陈述 + [原]/[引]）
| # | 作者·年份 | 编号/出处 | 支撑 | 条件 | 标注 |
|---|---|---|---|---|---|
| 1 | Montgomery 1973 | Proc. Symp. Pure Math. **24**, 181–193 | F(α)=α+o(1), 0≤α≤1 ⟺ 核支撑 [−1,1] | RH | [引，多源一致；CIRM 摘要复述 [原]] |
| 2 | Hejhal 1994 | IMRN no. 7, 293–302 (n=3) | Σ\|ξⱼ\|<2 | RH | [原：Lagarias–Rodgers 1905.12123 转述] |
| 3 | Rudnick–Sarnak 1996 | Duke Math. J. **81**(2), 269–322 (n>3) | Σ\|ξⱼ\|<2 | RH | [原：Lagarias–Rodgers 转述] |
| 4 | BGSTB24 2024 | arXiv:2306.04799 = Acta Arith. **214**, 357–376 | 核 Fourier 支撑 [−1,1]（与 Mont 同） | **无条件**（对全体复零点求和） | [原，HTML] |
| 5 | BGSTB25 2025 | arXiv:2501.14545 | 同上框架 → 简单零点比例 | 无条件（弱于 RH 的薄盒） | [引] |
| 6 | GLSS25 2025 | Goldston–Lee–Schettler–Suriajaya | 配对相关猜想 ⟹ 100% | 猜想 | [原，转述] |
| 7 | Dirichlet L 族（平均 over q） | Carneiro–Chirre–Milanez 等 Fourier 优化 | \|α\|<2（额外平均） | 无条件（平均） | [引，NSF 摘要] |

**归一化注意（防混淆）**：Montgomery/BGSTB/前沿用「核 Fourier 支撑 [−1,1]」（bandwidth one），Rudnick–Sarnak n-level 用「Σ\|ξⱼ\|<2」。两者差一个因子 2（对称双侧 vs 单侧归一化），是同一件事。本文统一按前沿的「支撑 1」口径。 [推导]

**核心判读**：
- 2 点 form factor f(t)=min(\|t\|,1) 在 \|t\|≤1 完全确定（RH 下 Montgomery；无条件 BGSTB24 对全体零点求和）；\|t\|≥1 处 f≡1 平凡。⟹ **对"配对相关"而言支撑 >1 没有新的 2 点信息**；"支撑 1+δ" 的真实含义是**更高阶相关（n≥3 点相关 = 三阶及以上矩）**。
- 前沿 §1.4 原话 "beyond Fourier support 1"、§7.2 "form factor on (−λ₀,λ₀) for all λ₀ ⟹ 100%" 与此一致：越 0.682 = 需要支撑 >1 的信息 = 无条件三阶矩/三重点相关。 [原]

## 【子问 · δ→比例曲线】（复用 E8 Christoffel 框架）

**框架（E8/前沿 §7.2(d)）**：矩已知到 k≤2m ⟹ 尖锐下界 = 1 − Λ_m(0)，其中 1 − Λ₁(0)=m₁²/m₂。 [原]
**前沿矩数据** m_k(1)=1, 4/3, 2, 13/4。 [原]

脚本 `scripts/A3break_christoffel_hierarchy.py`（provenance 头✓，读数据✓，输出 .txt✓）计算得：
```
m=1: Λ₁(0)=1/4=0.25      ⟹ 1−Λ₁(0)=3/4=0.75  (=m₁²/m₂ ✓ Cauchy–Schwarz)
m=2: Λ₂(0)=5/36≈0.1389   ⟹ 1−Λ₂(0)=31/36≈0.8611  (=5/36 与前沿一致 ✓)
```
**锚点（[原]/[核验]）**：
- 支撑 1（仅 m₁,m₂，2 点相关）：bandwidth-one 天花板 **0.682**（1−Λ₁(0) 的最优两矩字典值）；MT 窗 0.6725。 [核验]
- HL*(4)（m₁..m₄，4 点相关）：比例 ≥ **13/18 ≈ 0.7222**。 [原]
- HL*(∞)（全相关）：比例 → **1**。 [原]

**δ→比例的定性曲线**（离散于矩阶 m，非连续 δ）：
```
δ=0  (2 点相关, k=2)  → 0.682      [天花板，尖锐]
     (三阶矩 k=3)     → [未在 repo，§7.2 未读]   ← 0.69/0.70 落于此
     (四阶矩 k=4)     → 0.7222 (=13/18)
δ→∞ (全相关)         → 1.0
```

**达到 0.69/0.70 所需最小 δ 的诚实回答**：
- 0.69 与 0.70 均 **严格大于 0.682**（bandwidth-one 天花板），故二者都要求 **越过支撑 1**，即需要 **无条件三阶矩（k=3，X≍T）**。
- 精确的"最小连续 δ"无法从 repo 内材料重建：E8 明言 "The dictionary turning Λ₁(0) into 0.682 is not reconstructible from in-repo material (frontier §7.2 unread)"。[原，E8 §5]
- 因此 δ→比例 的**连续数值曲线**给出方式应为：δ 的"阶"对应矩阶，0.69/0.70 的最小要求 = **k=3 一阶**（即从 2 点相关跨到 3 点相关），而非某个小数 δ；具体小数 δ 依赖未读的 §7.2 词典。`[未核验：连续 δ 词典]`

## 收工结论（达到结束条件①：查清支撑上限 + 给出曲线结构）

**支撑上限已查清**：无条件 = 1（BGSTB24），RH = 1（Montgomery），>1 为配对相关猜想（RH 下亦未证）。

**要越过 0.682 必须新证的一句话命题**：
> **必须无条件地证明三阶矩——即在 X ≍ T 处（超出 Rudnick–Sarnak 范围 X³ ≤ T^{2−ε}）无条件求值 tr G̃³ 的素数侧对角和（等价地，无条件化 Hejhal 1994 / Rudnick–Sarnak 1996 的三点相关，即把 Montgomery 型 form factor 从 Fourier 支撑 1 无条件推到支撑 >1）；否则 0.682 即为 bandwidth-one 证书类在无条件矩输入下的尖锐天花板。**

（这句话同时覆盖两个等价缺口：无条件三阶矩 ⇔ 支撑 >1 的配对/三点相关信息。）

---

## 父方核验注记（2026-09-12 23:55）✓

```
【通过 ✓】① 支撑上限 = 1 的结论 ✓（与 `A3-third-moment-barrier.md` §7.2(e) 一致 ✓）
        ② Christoffel 数字：1−Λ₁(0) = 0.75 = m₁²/m₂ ✓；1−Λ₂(0) = 31/36 = 0.8611 ✓（与前沿 Λ₂(0)=5/36 ✓ 吻合）
        ③ 锚点 13/18 = 0.7222 ✓（前沿 HL*(4) ✓）；0.69 / 0.70 均 > 0.682 ⟹ 确需无条件三阶矩 ✓
        ④ 产物齐全 ✓：本档 + `scripts/A3break_christoffel_hierarchy.py/.txt` ✓
【⚠️ 一处标注存疑（待定 ✓）】本档 §表格 **第 1 行把 Montgomery 1973 标为「RH」** ✗，与三处证据不符：
   · 本档自己引的 BGSTB24 摘要原话：「an **unconditional version** of Montgomery's result … for even kernels
     with Fourier transforms supported in [−1,1]. **If we assume RH** this agrees with the earlier version in [Mon73]」
     ⟹ "unconditional" 应指**对全体复零点求和** ✓；RH 的作用是"RH 下全体零点 = 线上零点，两版一致" ✓
   · 前沿原文亦称 Montgomery 的**素数侧二阶矩无条件** ✓（[Mon73, Ary22, BGSTB24] ✓）
   · 我方 `A3-third-moment-barrier.md` §2 同判 ✓（"Montgomery 1973：Fejér 核的素数侧二阶矩可**无条件**求值" ✓）
   ⟹ **建议改为**：「Montgomery 1973：F(α) = α（|α| ≤ 1）**无条件**（就 σ=1/2 上的零点而言）；
      RH 仅用于"全体零点 = 线上零点"的对照」✓ —— 但**结论不变** ✓
【结论不受影响 ✓】越 0.682 仍需：无条件三阶矩（X≍T）**或**支撑 >1 的高阶相关（猜想级）✓
【诚实标注 ✓】本注记本身为**父方判断** ✓（未逐字取得 Montgomery 1973 原文 ✗，标 `[未核验]` ✓）
