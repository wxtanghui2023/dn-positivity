# A3 — X ≍ T 的三阶矩障碍：文献侦察

**日期** 2026-09-12 · **范围** 只读侦察（不提交、不改他文件）· **工作目录** dn-project
**标签** `[原]` = 已读一手原文（arXiv HTML/abs/PDF）· `[引]` = 转引自原文 · `[未核验]` = 二手/未读到原始出处 · `[未找到]` = 检索未果（空结果）

**侦察对象（已核对原文）** 前沿论文 = **arXiv:2608.13637**《More than two thirds of the zeta zeros are simple and on the critical line》
（v1 2026-08-13，v2 2026-08-19；Ralph Furman 等署名；证明由 Claude/Anthropic 发现、作者验证）。其 §1.1 记 MT 窗 0.6725、
§7.2 记 bandwidth-one 证书类天花板 ≈0.682、§7.2(e) 记「X ≍ T 时无条件更高矩一无所获」。[原]

---

## Q1 — X ≍ T 的 k=3 是否已有无条件结果？

**结论：未找到。**
- 前沿 §7.2(e) 原话：「The prime-side evaluation of tr G̃^k by the diagonal method of Section 5 (multiplicative relations among k prime powers, Montgomery–Vaughan for the rest) is available exactly in the Rudnick–Sarnak range [RS96] X^k ≤ T^{2−ε}; at X ≍ T this allows only k = 1. Thus, unconditionally, higher moments add nothing.」[原]
  - ⟹ k=3 的对角法只覆盖 **X ≤ T^{2/3−ε}**；推到 X ≍ T 需再进 **T^{1/3}**。
- **k=2 是特例**：前沿 item (P) 用 ‖G̃‖²_HS=(R(ψ)+o(1))N，注明即 Montgomery 的**无条件**素数侧二阶矩 [Mon73, Ary22, BGSTB24]。[原]
- k=3 的已知结果全部**依赖 RH**：前沿 §7.3「Under the Riemann hypothesis the third trace tr G̃³ is available [Hej94, RS96]」。[原]
- 三篇引用 2608.13637 的后续工作（arXiv:2609.02882 Lamzouri；arXiv:2609.07918 Biao Wang；arXiv:2608.16034 Hua–Yang）**全部仍停在 k=2 / MT 常数 0.6725**。[原，摘要]
- **给出 X ≍ T 无条件 k=3 的作者/年份/arXiv 号：未找到（无）。**

---

## Q2 — k=2 无条件化的路线，能否推广到 k=3？

**k=2 用了什么：**
- Montgomery 1973：Fejér 核的素数侧二阶矩 ∫_0^T|A₁+A₂+A₃|²dt 可**无条件**求值（对角项 + Montgomery–Vaughan）。[引：BGSTB25 §3 复述该式]
- **Aryan 2022 [Ary22]**：把 Fejér 核二阶矩的这一无条件性**显式化**。[引：2608.13637 §1.3]
- **BGSTB24**（arXiv:2306.04799 = Acta Arith. 214 (2024) 357–376，DOI 10.4064/aa230612-20-3）：把 Montgomery 的 form factor 推广到**对全体复零点求和**。摘要原话：「Here we obtain an unconditional form of Montgomery's theorem…」。注意：**素数侧无条件**，但其**简单零点结论仍设薄盒假设** |β−1/2| < 1/(2log T)（T^{3/8}<γ≤T），得 61.7%；前沿改用 rank–trace 不等式才免去该假设。[原]

**能否推广到 k=3？——未找到任何推广。**
- BGSTB24 全文关键词核验：**"higher moment" 0 次、"higher correlation" 0 次、"triple" 0 次、"n-level" 0 次、"moment" 0 次** ⟹ 其引言**完全未讨论 k=3 或更高阶**。[原，grep]
  （故任务要求"摘 BGSTB24 引言里关于 k=3 的原话"——**原文没有，摘不出**。）
- **BGSTB25**（arXiv:2501.14545，Pair Correlation I）：引言通读，同样**无** "third / higher moment / k=3"。[原，grep]
- 唯一直接谈"下一阶矩"的原话在 **2608.13637 自身**，§7.2(f)：「Conditionally, let HL*(k₀) denote the hypothesis that for all k ≤ k₀, tr G̃^k = d·m_k(1)(1+o(1))… (for k = 4 this encodes a Hardy–Littlewood-type asymptotic for the additive correlations Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), |h| ≤ X²/T).」[原]
  - 同处给出 m_k(1)=1, 4/3, 2, 13/4 (k≤4)、Λ₂(0;1)=5/36、HL*(4) ⟹ lim inf N₀^s/N ≥ **13/18**；HL*(k₀) 对一切 k₀ ⟹ 比例 → 1。[原]
**判读：** k=2 的无条件化本质是"二阶（Fejér）矩存在额外可算结构"（相当于**二元加性除子型**输入已解），k=3 未见类比机制；前沿自己把下一步编码为**猜想级的 HL***。[推导；"二元/三元除子"措辞与文献的严格对应 `[未核验]`——未逐篇核对]

---

## Q3 — 无条件高阶矩的已知最好结果（整线矩 vs 素数侧短和）

**整线矩 I_k(T) := ∫_0^T |ζ(1/2+it)|^{2k} dt：**
- **无条件上界（正确阶 T(log T)^{k²}）**：仅 **0 ≤ k ≤ 2**。来路：Heath-Brown 1981（分数矩，J. LMS (2) **24**, 65–78）→ Bettin–Chandee–Radziwiłł 2017（k=1+1/n）→ **Heap–Radziwiłł–Soundararajan 2019**（QJM **70**(4), 1387–1396，覆盖全部 0≤k≤2）。[引：Florea 综述 arXiv:2509.20335 §3.2]
- **k > 2 的上界须 RH**：Soundararajan 2009 `I_k ≪ T(log T)^{k²+ε}`；Harper 2013（arXiv:1305.4618）RH 下尖锐。[引]
  ⟹ **k=3（六阶矩）的正确阶无条件上界/渐近：未找到**（六阶矩渐近无条件开放）。[引 + 未找到]
- **无条件下界（正确阶）**：Heath-Brown 1981（有理 k≥0）；**Radziwiłł–Soundararajan 2013**（Mathematika **59**, 119–128；arXiv:1202.1351）「for all k > 1」。[引]
  六阶矩显式常数由 **Page**（Manchester 学位论文，research.manchester.ac.uk；**年份未核验**）从 20.26·c₃ 提高到 29.54·c₃〔**c₃ 归一化未核验**〕。[引]

**与本题所需"素数侧短和"的关系：**
- 本题需要的是 **tr G̃^k**（G̃ = Weil 形式在 d∼N 维压缩下的 Gram 型矩阵），其对角法障碍是 **Σ_{p₁⋯p_k=q₁⋯q_k} 的乘性关系**（前沿 §7.2(e) 原话）。[原]
- I_k(T) 与 tr G̃^k **同源不同物**：二者同由"乘性/加性除子关系"主宰，但 I_k 是 |ζ|^{2k} 的**整线均值**，tr G̃^k 是**长度 X≍T 的短和 k 阶矩**。
  ⟹ **I_k 的无条件下界并不给出 tr G̃³**（未找到任何把前者转成后者的定理）。[推导 / 未找到]

---

## Q4 — CFKRS 对三阶矩的预测，是否已被无条件逼近？

- **预测**：Conrey–Ghosh 1998（IMRN no.15, 775–780；arXiv:math/9807187）：
  `∫_0^T |ζ(1/2+it)|^6 dt ∼ (42/9!)·a₃·T(log T)^9`，`a₃ = ∏_p (1−1/p)^4 (1+4/p+1/p²)`。
  **CFKRS 2005**（Conrey–Farmer–Keating–Rubinstein–Snaith，Proc. LMS (3) **91**, 33–104；arXiv:math/0206018）给出全体矩的完整渐近（含低阶项）。[引，多源一致]
- **是否被无条件逼近**：只有"正确阶的**下界**"（Radziwiłł–Soundararajan 2013；常数改进见 Page）；**正确阶无条件上界/渐近：未找到**。[引 + 未找到]
- 注意：本题真正需要的**不是 I₃**，而是前沿 §7.2(f) 的 **HL*(k₀)**（tr G̃^k 的 Hardy–Littlewood 型渐近）——比整线矩更细、更接近加性相关猜想。[原]

---

## Q5 — 零点三重相关（triple correlation）的无条件结果？

**未找到无条件结果。**
- **n=2 Montgomery 1973；n=3 Hejhal 1994（IMRN no.7, 293–302）；n>3 Rudnick–Sarnak 1996（Duke Math. J. 81(2), 269–322）。** 支撑区域：|ξ₁|+⋯+|ξ_n| < 2。[原：Lagarias–Rodgers arXiv:1905.12123v3 转述]
- **关键**：Lagarias–Rodgers 的 Theorem 2.4（Band-limited correlations）**明文写「Assume the Riemann Hypothesis」** ⟹ Hejhal(n=3) 与 RS(n>3) 均为 **RH 条件下**。[原]
- Lagarias–Rodgers（arXiv:1905.12123）另证：Montgomery–Hejhal–Rudnick-Sarnak 的**全部已知 band-limited 信息与 Alternative Hypothesis 相容**（构造反例点过程）——现有高阶相关信息连"替代假设"都排除不了。[原，摘要+正文]
- 近 5 年进展集中于 **k=2**（Aryan 22、BGSTB24/25、GS25 arXiv:2511.20059、GS26、GLSS25、Lamzouri 2609.02882）；**n=3 的无条件化：未找到**。[未找到]

---

## Q6 — 能否绕过矩方法？

**(i) 框架内只有两条路，前沿已点明。**
- §1.4 原话：「Given only tr G̃, ‖G̃‖²_HS and the block structure, the inequality (1.1) is sharp (§7.2); improving on 2/3 by this route would require **pair-correlation information beyond Fourier support 1**.」[原]
- §7.2 原话：「More generally, if Montgomery's form factor were known on support (−λ₀, λ₀) for all λ₀, the method would certify 100% simple zeros on the line.」
  ⟹ **支撑 >1 的配对相关**（Montgomery 配对相关猜想档位）是一条**非矩**的路，但属**猜想级**。[原]
**(ii) 换方法类？** 0.682 是 **bandwidth-one 证书类**的天花板，不是"一切方法"的天花板：
- 无条件：Levinson 型 mollifier 至今停在 **5/12 = 0.4167**（PRZZ20）[引：2608.13637 §1.1]；未见无条件方法 > 0.6725。
- **RH 条件下**可越 0.682：BHB13 的 **19/27 = 0.703**；CGdL20 的 **0.6792**（SDP，用 form factor 在 [−1,1] **外**的正性）。[引：2608.13637 §1.1]
  ⟹ **无条件越 0.682：未找到**；必须要么无条件 k=3 矩，要么 support>1 配对相关（猜想），要么新方法类。[原 + 未找到]
**(iii) 后续工作**：引用 2608.13637 的三篇（2609.02882 / 2609.07918 / 2608.16034）**无一越过 k=2**；其中 Lamzouri 2609.02882 用 Hilbert 空间不等式替代矩阵框架，常数仍是 **0.6725 / 0.8362**。[原，摘要]
**(iv) 该文自身保留**：0.682 的 Lean 定理 `Zeta23.PairCeiling.ceiling_law256` 依赖 `EnclOK`，其区间算术包络**不经 Lean 内核检验**（论文自述这是全文唯一引入数值认证之处），给出 p₀ ≤ **0.6818287**。[原]

---

## 对本项目的意义

**(a) k=3 已被无条件解决？——没有。** 已核验：前沿 §7.2(e) 明言 X≍T 时对角法只允许 k=1；k=3 的已知结果（Hejhal 1994 / Rudnick–Sarnak 1996）**明文 Assume RH**；三篇后续工作仍停在 k=2。「未找到」任何 X≍T 的无条件三阶矩结果。
**(b) 现有技术离它有多远？——不是 ε 级，而是"整阶"。** 量级上，k=3 的对角法只到 **X ≤ T^{2/3−ε}**，到 X≍T 差 **T^{1/3}**（k=2 靠一个二阶矩专属结构才多拿了 T^{1/2}）；更根本的是 k=2 依赖**专属于二阶矩的可算结构**（Fejér/Montgomery 无条件二阶矩；等价于二元加性除子型输入已解），k=3 未见类比机制，且前沿自己把下一步编码为**猜想级 HL***（§7.2(f)）。这是"从已证二阶矩跳到猜想级高阶加性相关"的**质变**，而非参数微调。
**(c) 本项目能否攻？——不宜攻，宜等前沿。** 我方资产是**惯性/负指标（n₋）与配置侧变分**；前沿 §7.2 表明天花板是**矩可得性**问题，且其极值构型取在 **n₋(Q)=0** 处，与负指标路线**无交集**（见 `A3-improvement-assessment.md` Q1–Q3、`E8-ceiling-0682.md` §6–§7）。故 A3 的正确定位仍是**"机制澄清 + 必要性说明"**（0.6725→0.682 的 0.01 来自 Christoffel/矩输入而非窗口；越 0.682 需无条件三阶矩），**不是**进攻 0.682 之上的数值。若前沿未来出现"无条件 k=3/k=4"，我方贡献点也只应是**独立复核**，不是主攻。
**可留意但不宜投入**：support>1 配对相关（§1.4/§7.2 的另一条路）与 GLSS25 的配对相关猜想路线——二者均为猜想级，观察即可。
**诚实缺口**：Page 论文的年份与常数归一化 `[未核验]`；前沿 §7.2 的 Lean 天花板依赖未被内核检验的数值包络 `[原，已注明]`。
