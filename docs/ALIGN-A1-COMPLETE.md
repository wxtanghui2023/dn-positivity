# ✅ **A1 方向完成档案**：Li 系数 / 有限高度转换（实读文献后）

**依据**：唐先生 2026-09-11 22:19/22:21（"先做完这个方向"）
**已读原文**：Lagarias 2007（Numdam PDF ✓）｜Palojärvi arXiv:1807.01506v3（HTML ✓）｜**Droll 博士论文 2012（Queen's，PDF excerpt ✓）**
**标注**：【原文 ✓】｜【二手 ⚠️】｜【缺口精确化】

---

## §1 ⭐⭐⭐ **框架（前沿的核心，也是我们此前漏掉的连接）**
```
【Lagarias 2007 原文 ✓】λ_n = **S_∞(n) − S_f(n) + 1**，S_∞/S_f = **阿基米德位 / 有限位**贡献 ✓
   "the dominant contribution … comes from the **archimedean terms**, which correspond to the
    **'trivial zeros'**" ✓ ⟹ **主项来自平凡零点** ✓
【⭐ 关键（原文 ✓）】"**each positivity condition λ_n ⩾ 0 encodes 'Weil positivity' of Weil's quadratic
   functional for a particular test function g_n(x)**" ✓✓✓
   ⟹ **Li 判据 = 一族 Weil 正性命题（每个 n 一个显式 g_n）** ✓✓
   ⟹ **这把 A1 接到 A3（惯性/有限压缩）与 A7（Connes）** ✓✓ —— **我们此前未做此连接** ✓
【经典机制（Wikipedia ✓，且与我们的"恒等式"一致）】φ = 1/(1−z)，z = 1−1/ρ ⟹
   **|1 − 1/ρ| ≥ 1 ⟺ Re(ρ) ≤ 1/2** ✓✓ —— 即 **λ_n = Σ[1−(1−1/ρ)^n]** 的正性判据即源于此 ✓
   ⟹ ⚠️ **我们此前的"初等恒等式 |w|² = 1+(1−2σ)/(σ²+γ²)"是【经典机制】** ✓（非新发现 ✓）—— **对齐结论** ✓
```

## §2 ⭐⭐⭐ **缺口的精确刻画（本方向最重要的产出）**
```
【Brown 2005 JNT 111】Thm 3（Li ⟹ 零自由）**成立 ✓**；Thm 2（零自由 ⟹ Li 非负）**其证明含两处错误** ✗
【Droll 2012 博士论文原文 ✓（决定性）】
   ① **错误 1**：Brown 声称 **f(x) = x^k + x^{−k} 对一切 x>0 递增** ✗ —— **实际只在 x>1 递增** ✓
      ⭐ 原文："**This error is not a significant obstacle, however, and is essentially IRRELEVANT in the
      special case that Brown is addressing**" ✓✓ ⟹ **对经典情形（ζ）此错误【无关紧要】** ✓✓
   ② **错误 2（更严重）**："**The proof of [3, Lemma 5] takes the power series expansion of
      g(x) = (1+x)^k …**" ✓（**具体为何失败，本轮摘录被截断** ✗ —— **待读原文** ✓）
      ⟹ **Droll 不得不引入 Conjecture 3.2.7** ✓ 且**其主定理 3.3.1 至今条件性** ✓✓
      ⭐ 原文："**they seem to invalidate the proof of [3, Theorem 2]**" ✓；"hope to be able to establish
      an **unconditional** generalized result in the future" ✓✓
【Palojärvi 已证的三个定理 ✓】
   · **Thm 2.1**：n ≥ max{e, T₀/(eτ)}，**T(n) := n·e·τ** + 一条**显式不等式** ⟹ n ↔ 高度关系由其决定 ✓
   · **Thm 2.3**：探测方向（某 n 为负 ⟹ 存在零点满足 |ρ/(ρ−τ)| ≥ R ✓）
   · ⭐ **Thm 4.1**：**至多一个离轴零点**的情形 ✓✓ —— **最接近目标的已证结果** ✓
【临近文献（Wikipedia ✓）】Bucur–Ernvall-Hytönen–Odžak–Smajlović：**研究违反 RH 的函数的 Li 系数行为** ✓✓
   ｜Brown–Omar：Epstein zeta 的 Li 判据 ✓ ｜Freitas：Li 型判据 ↔ 零自由半平面 ✓
```

## §3 ⭐ **我们的分析方法 vs 前沿方案（结论）**
| 环节 | 前沿 | 我们 | 判断 |
|---|---|---|---|
| 分解 | **λ_n = S_∞ − S_f + δ**（阿基米德 vs 有限位 ✓） | 相位 λ_n = Σ[1−w^n] ✓ | 正确但不同 |
| 主项 | **S_∞（平凡零点 ✓ 显式 ✓）** | **丢弃** ✗（只当在线项 ≥0 用） | ⚠️ 放弃 ~T 倍 |
| 误差 | S_f ← 零自由区 + 显式计数 ✓ | 离轴界 −n·B_T ✓ | ✓ **做对了** |
| **转换视角** | ⭐ **Weil 正性 + 显式测试函数 g_n** ✓✓ | **自制窗口 γ∈[n/2,2n]** ✗ | ⚠️ **装置弱得多** |
| 机制 | **单位圆 ↔ 半平面映射**（经典 ✓） | 同（我们重推了一遍 ✓） | 对齐 ✓（非新 ✓） |
| 显式化 | 全常数 + 机器验证 ✓ | 首项预算 + 数值核验 ✓ | ⚠️ 未完整 |
⟹ **总判断**：**直觉对、装置错；机制是经典的、我们重推了；连接（Weil 正性）我们漏了** ✓✓
```

## §4 ⭐⭐⭐ **建议（A1 的四条，按优先级）**
```
【建议 1·最锐利】**修 Brown 的 Lemma 5（错误 2：幂级数论证）** ✓✓
   · 理由：**错误 1 对经典情形无关紧要** ✓（Droll 原文 ✓）⟹ **只剩错误 2** ✓
   · 奖赏：**Brown Thm 2 = 经典"零自由 ⟹ Li 非负"定理** ✓✓（**正是整个有限高度转换所需的方向** ✓）
   · 状态：**缺口公开、有名字、作者自认"希望将来能给出无条件结果"** ✓✓✓
   · 第一步：**读 Brown Lemma 5 原文 + Droll §3.2**（错误 2 的确切性质，本轮摘录截断 ✗）
【建议 2】**把 Palojärvi Thm 4.1（至多一个离轴零点）推广到有限多个** ✓（有先例 ✓、有界 ✓）
【建议 3·连接**】把"λ_n ≥ 0"当作 **Weil 正性对 g_n 的实例** ✓✓ ⟹ 接通 **A3（惯性）+ A7（Connes）** ✓✓
【建议 4·修正措辞】① "τ 版线性" ⚠️ 过粗（由 Thm 2.1 的不等式决定 ✓）② "我们的恒等式是发现" ⚠️
   —— 实为**经典机制** ✓（对齐后非新 ✓）
```

## §5 **A1 资料补足清单（完成度）**
```
【✅ 已读原文】Lagarias 2007（框架 + Weil 正性连接 ✓）｜Palojärvi v3（Thm 2.1/2.3/4.1 ✓）
   ｜Droll 2012 论文（两处错误 + Conjecture 3.2.7 + Thm 3.3.1 条件性 ✓）
   ｜Wikipedia Li's criterion（经典映射 ✓ + 相关文献线索 ✓）
【✗ 待读】**Brown 2005 Lemma 5 原文**（错误 2 的确切性质 ✗）｜**Droll §3.2 全文**（Conjecture 3.2.7 的形式 ✗）
   ｜Bombieri–Lagarias 1999 Thm 2 原文 ✗｜Voros 2020（Oesterlé 引文）✗
   ｜Bucur–Ernvall-Hytönen–Odžak–Smajlović（违反 RH 的函数 ✓ 值得读 ✗）
【✗ 待补脚本】B–L 分解的**完整预算实现**（horizontals/M₀/H(T)/I_I ✓）
```

## §6 边界
```
【原文级 ✓】§1（Lagarias PDF ✓）｜§2 的三个定理（Palojärvi HTML ✓）｜§2 的错误刻画（Droll PDF ✓✓）
【⚠️ 截断】Droll 关于**错误 2**的完整描述在本轮摘录中被截断 ✗ —— **不得据此断言错误 2 的性质** ✓
【⚠️ 修正】§3/§4 中修正了此前两处过粗表述 ✓
```
## §7 提交链
```
ALIGN-A1（765a5c3）→ 本篇（A1 完成：错误精确化 + 方法对比 + 四条建议 + 补足清单）
```
