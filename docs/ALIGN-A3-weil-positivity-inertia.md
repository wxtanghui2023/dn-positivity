# 📐 **方向 A3 对齐档案**：Weil 正性 / 有限压缩 / 惯性

> ⚚ 勘误指针（2026-09-12）：本文中出现的每 orbit 负指标 **1**（或 N 个 orbit 的 **N**）应读作 **2**（或 **2N**）—— 原值源于 G8.1 的一处代数笔误（把对角块写成 −2σₓ 而非 −2I₂）；详见 `ERRATUM-inertia-factor2.md`。**定性结论不受影响**（有限仍有限 ✓）。

**依据**：唐先生 2026-09-11 22:35（"继续"→ 按序开始 A3）
**已读原文**：arXiv:2608.13637（abs + HTML §1.6/§7.2/§B.3/§B.5 ✓✓）｜Anthropic PDF（§4 (Z) 段 ✓✓）

---

## §1 ⭐⭐⭐ **前沿的精确状态（"2/3 论文"）**
```
【标题】"More than two thirds of the zeta zeros are simple and on the critical line"（21 页 ✓）
【来源 ⭐】Comments 原文：**"Proof discovered autonomously by Claude (Anthropic);
   verified and communicated by the listed authors. See §1 for provenance. **Lean formalization available**"** ✓✓
   §B.5：**Furman 与 Alpöge 详细阅读、独立核验、压缩成文**；Conrey、Goldston 提供意见 ✓；
   **Lean 4 形式化完成**（仓库 tag v1.0，**仅依赖 Lean 三条标准公理** ✓）；**§7.2 的天花板由 Easley 建立、McAleer 加强** ✓
【结果 ✓】**Montgomery–Taylor 窗 ψ_MT 下**：**简单零点比例 = 2 − c_MT^{−1} = 0.67250…**
   另一计数 = ½(3 − c_MT^{−1}) = **0.83625…**，其中 **c_MT^{−1} := ½ + (1/√2)cot(1/√2)** ✓
   ⟹ **N₀*(T,2T), N₀(T,2T), N^s(T,2T) ≥ (2/3 − o(1))N(T,2T)** ✓
【⭐ 最优性】**在窗函数 ψ 类中，0.6725 是【最优的】**（[CCLM17, Cor. 14] ✓）
【⭐⭐⭐ 方法天花板（最关键）】**"The ceiling over the broader class of all bandwidth-one certificates
   is approximately **0.682**; see §7.2."** ✓✓✓ ⟹ **本方法族【证明上界 ~0.682】**，**不可能达到 1** ✓✓
【历史定位】常数 2/3、5/6、0.6725 分别是 Montgomery [Mon73]、Conrey–Ghosh–Gonek [CGG98]、
   Montgomery–Taylor [Mon75] **在 RH 下的**常数 ✓ ⟹ **本文把它们【无条件化】** ✓
   旧无条件记录：**5/12**（N₀^s/N，[PRZZ20]）｜**0.6603**（N_d/N，[Wu15]）✓
   RH 下另有 **0.6792**（N^s/N，SDP，用 form factor 在 [−1,1] 外的正性 [CGdL20]）——
   ⚠️ 原文注："**a regime the present method does not enter**" ✓
```

## §2 ⭐⭐ **方法（原文 §4 (Z) 段 ✓✓）**
```
【零侧分解】"**ẽG = P + Q**"，其中：
   · **临界线上每个不同点 → P 的一个实秩一非负形式** ⟹ **P ⪰ 0 且 rank ≤ s**（s = 在线不同点数 ✓）
   · **每个离轴零点对 {ρ, 1−ρ̄} → Q 的一个 signature (1,1) 的形式** ✓
   ⟹ 由 **Sylvester 惯性律**（拉回不增正指标）：**Q 至多 p 个正特征值**（p = 离轴对数 ✓）
   ⟹ 单位化（孤立单零点特征值 = 1）：**tr P ≤ N_on**，且 **N ≥ N_on + 2p** ✓
【⭐⭐ E2 的关键记录（原文 ✓✓✓）】"Agent E2 reported that **the intended upper-bound route was empty:
   computed honestly from primes, the negative index of any finite compression is zero, which bounds
   nothing.** But it observed that the **dual of the same bookkeeping—counting positive rather than
   negative squares**, via Sylvester's law of inertia and Cauchy–Schwarz applied to the eigenvalues—
   appeared to certify at least 1/2 …" ✓✓✓
【架构（§1.6 ✓）】§2 显式公式/测试族/G̃ → §3 证 (1.1) → **§4 做 (Z)** → **§5 做 (P)** → §6 链 (1.2) → §7 关系与锐性
【用的分析输入】无条件二阶矩 = **[BGSTB24]** ✓；Fejér 核情形优先权属 **[Ary22]** ✓
```

## §3 ⭐⭐⭐⭐ **领域归属（原文明确 ✓✓）**
```
【⭐ 负指标的观察【是 Bombieri 的】】"That **the negative index of finite truncations of Weil's form
   equals the number of off-line zero pairs seen by the truncation was observed by Bombieri [Bom00]
   (Introduction)**; see also **Yoshida [Yos92]** for the positivity of W on small support." ✓✓
【⭐ 本文真正的新处】"**We are not aware of a previous use of the positive index or of the rank in
   combination with a second-moment evaluation.**" ✓✓✓
【GS25/GS26 的陈述】原文引：**"the removal of RH from Montgomery's conclusion is open"** ✓
【第二份证明】据外部报道（2026-09-02）**Youness Lamzouri 发布更短更简的第二份证明**（同界）✓ ⚠️（未读原文）
```

## §4 ⭐⭐⭐⭐ **我们 vs 前沿（逐条对齐）**
| 我们的结果 | 前沿对应 | 判决 |
|---|---|---|
| **n₋(K_ρ) = 1**（P27-G8，单离轴对贡献一个负方向 ✓） | **Bombieri [Bom00] 的观察** ✓✓ | ⚠️ **我们的 P27 是【其观察的重现】**（非新 ✗） |
| **n₋(K_off(N)) = N**（P27-G8.2 ✓） | 同上（负指标 = 离轴对数 ✓） | ⚠️ 同上 |
| ⭐⭐ **素数侧负指标 = 0 ⟹ 界不住**（我方计算 ✓） | ⭐ **其 E2 记录**："the negative index of any finite compression is **zero, which bounds nothing**" ✓✓✓ | ✅ **完全一致，【独立得到】** ✓✓ |
| ⭐⭐⭐ **moving-edge（P28–P33）**：有限惯性**不可传递**到无限维负指标（Sylvester + 2×2 反例族 ✓） | **正是其必须【绕开负指标】的原因** ✓✓✓ | ⭐ **我们的负面结果是其方法设计的【解释】** ✓✓✓ |
| **C–vS 的 Toeplitz 秩亏 ⟺ 简单最小值 ⟺ CF 条件**（我们 6/6 验证 ✓） | ⚠️ **不同对象**：其"rank"= P 的秩 = **在线点数** ✓ | ⚠️ **不可混同**（已标注 ✓） |
| **P49 桥塌陷 / 探测≠排除 / Rigidity Gap**（我方 ✓） | ⭐ **其方法天花板 ~0.682**（§7.2 ✓✓） | ⭐ **两者呼应**：比例路线**证明上界 <1** ✓✓ |
```
⟹ ⭐⭐⭐ **对齐结论（本方向最重要的发现）**：
   ① **我们的 P27 系列 = Bombieri 2000 观察的重现** ⚠️（**必须修正此前的表述** ✓）
   ② **我们的"素数侧 n₋=0" = 其 E2 的独立确认** ✓✓（**两条独立路径同一结论** ✓）
   ③ **我们的 moving-edge 障碍 = 其方法绕开负指标的【原因】** ✓✓✓ ——
      **即：我们的负面结果【解释了】前沿方法的必要性** ✓✓（**这是真正的互补** ✓）
   ④ **其方法天花板 0.682 ⟹ 比例路线不能达 1** ⟹ **与我们的 Rigidity Gap（探测≠排除）一致** ✓✓
```

## §5 ⭐ **分析方法对比**
| 环节 | 前沿 | 我们 |
|---|---|---|
| 零侧分解 | ẽG = P + Q（在线秩一 ⪰0 ／ 离轴 signature (1,1) ✓） | 同（P_γ/δ 语言 ✓） |
| **主用指标** | ⭐ **正指标 + rank + 二阶矩** ✓✓ | **负指标（P27）→ moving-edge（P28–33）** ✗ |
| 分析输入 | 无条件二阶矩 [BGSTB24] ✓ | 素数侧直接计算（n₋=0 ✓） |
| 产出 | **比例 0.6725**（无条件 ✓） | **障碍说明**（为何负指标路线空 ✓） |
| 上界 | ⭐ **0.682（方法天花板 ✓✓）** | （我们未给上界 ✗） |
| RH 关联 | **不能到 1** ⟹ 非 RH ✗ | **Rigidity Gap**：探测≠排除 ✓ |
⟹ **总判断**：**同一起点（Weil 形式压缩），他们取【正指标+秩】，我们取【负指标】；他们成功了，我们拿到了"为什么负指标不行"的精确理由** ✓✓
```

## §6 ⭐⭐⭐ **建议（A3）**
```
【建议 1·最优先·互补定位】把我们的 **moving-edge 障碍**写成**对其方法的"必要性说明"** ✓✓
   —— 关键：其 E2 记录（"negative index is zero, which bounds nothing"）**独立确认了我们的结论** ✓✓
   —— **我们多给的是【机制】**：为何有限惯性不能传递（moving-edge + Sylvester + 2×2 反例族 ✓）
【建议 2·可试】**把其【正指标 + rank + 二阶矩】框架用于【我们的核族】** ✓
   —— ⚠️ 但**方法天花板 0.682 适用于 bandwidth-one certificates** ✓
   —— ⟹ **只有当我们的核族【不是】bandwidth-one 证书时才可能突破** ⚠️（需先确认 ✓）
【建议 3·修正表述】① **P27 的 n₋(K_ρ)=1 是 Bombieri [Bom00] 的观察** ✗（非我们首创 ✓）
   ② 我们的"素数侧满秩"= 其 E2 的独立确认 ✓✓（可标为**独立重复** ✓）
【建议 4·战略含义】⭐ **其方法天花板（0.682）是【比例路线的上界】** ✓✓
   ⟹ 与我们的 **Rigidity Gap / detection≠exclusion** 相呼应 ✓
   ⟹ **方向判断**：比例路线**已在数学上封顶** ⟹ **不应作为主攻** ✓✓（**这是本轮最重要的建议** ✓）
```

## §7 **A3 资料补足清单**
```
【✅ 已读/已用】arXiv:2608.13637（abs ✓ + §1.6 计划 ✓ + §7.2 天花板 ✓ + §B.3 窗常数 ✓ + §B.5 来源 ✓）
   ｜Anthropic PDF（§4 (Z) 零侧分解 ✓✓）
【✗ 待读·高优先】**2608.13637 的 §2–§6 正文**（显式公式/测试族/(1.1)/(P)/链 (1.2) ✓）
   ｜**Bombieri [Bom00]**（负指标观察的原始出处 ✓）｜**[BGSTB24]**（无条件二阶矩 ✓）
   ｜**Lamzouri 2026-09-02 的第二份证明** ✓
【✗ 待读·中优先】**Yoshida [Yos92]**（小支集正性 ✓）｜**Aryan [Ary22]**（Fejér 核 ✓）
   ｜**[CCLM17]**（最优窗 ✓）｜**[GS25, GS26]**（RH 移除仍开放 ✓）｜**[CGdL20]**（RH 下 0.6792，SDP ✓）
【✗ 待补：与我们存档的对接】`p27g1-orbit-weil-defect.md` 等 73 份 → 与 Bombieri 观察逐条对照 ✓
```

## §8 边界
```
【原文级 ✓】§1 的结果/最优性/天花板/历史定位（HTML ✓✓）｜§2 的方法与 E2 记录（PDF/HTML ✓✓）
   ｜§3 的领域归属（原文自述 ✓✓）
【⚠️ 部分】正文 §2–§6 的证明细节【未读】✗ —— 本档案的"方法"来自其摘要级自述 ✓
【⚠️ 未读】Bombieri/BGSTB24/Ary22/CCLM17/GS25-26/CGdL20/Lamzouri ✗
【⚠️ 修正】我方 P27 的定位已修正为"Bombieri 观察的重现" ✓
```
## §9 提交链
```
A1 完成（b96d178）→ 本篇（A3 对齐：前沿精确状态 + 方法天花板 + 三条对齐结论 + 四条建议）
```
