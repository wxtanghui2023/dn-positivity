# ✅ **A3 完成（第二部分）**：素数侧 (P) 的精确内容 + Bombieri 对齐

**依据**：唐先生 22:45｜**已读原文**：2608.13637v2 §5（素数侧 ✓✓）｜Conrey 调查报告（Bombieri [Bom00] 内容 ✓✓）｜Anthropic PDF 参考文献 ✓

---

## §1 ⭐⭐⭐⭐ **素数侧 (P) 的精确内容（原文 §5 ✓✓）**
```
【核心等式】**‖G̃‖²_HS = (R(ψ) + o(1))N** ✓ —— 其中 **R(ψ) 只依赖窗**（其 Lemma 5.6 ✓）
   · **R(ψ₀) = 4/3**（指示窗 ✓）｜**R(ψ_MT) = c_MT^{−1}**（Montgomery–Taylor ✓）
   · 原文："This is **Montgomery's unconditional prime-side second moment** [Mon73, Ary22, BGSTB24]
     (Theorem 5.7)" ✓✓
【⭐ R(ψ) 的显式公式（原文 ✓）】
   M[μ,μ] + M[P_X,P_X] = (TL³/2π)( **∫ψ² + 2∫₀¹w(ψ*ψ)** ) + O_χ(TL²) = (TL³/2π)·**R(ψ)**·(∫ψ)² + O_χ(TL²) ✓
   且 **2∫₀¹w(ψ*ψ) = ∬|u−v|ψ(u)ψ(v)dudv** ✓（ψ 偶 ✓）
   ⟹ **R(ψ) = [∫ψ² + ∬|u−v|ψψ] / (∫ψ)²** ✓✓（**可优化的显式泛函** ✓）
【λ 参数化（原文 ✓）】取 L = λl（0<λ<1，X = (T/2π)^λ）⟹ 常数变为 **2 − R_λ(ψ)**，
   **R_λ(ψ₀) = 1/λ + λ/3** ⟹ **H(λ) := 2 − 1/λ − λ/3** 取代 2/3 ✓；
   ⭐ "**the log log T may be dropped**" ✓；⭐ "**No λ < 1 improves the constants**" ✓
【误差跟踪（原文 ✓）】N₀^s(T,2T) ≥ (2 − R(ψ) − c_ψ·loglog T/log T)·N(T,2T) ✓
```

## §2 ⭐⭐⭐⭐⭐ **两个重要发现**

### 发现 1：**"高阶矩"探索点【已被前沿回答】** ✓✓✓
```
【原文 §7.2(e) ✓✓✓】"**The prime-side evaluation of tr G̃^k by the diagonal method of Section 5
   (multiplicative relations among k prime powers, Montgomery–Vaughan for the rest) is available
   exactly in the Rudnick–Sarnak range [RS96] X^k ≤ T^{2−ε}; at X ≍ T this allows only k = 1.
   ⭐⭐ Thus, unconditionally, higher moments add nothing.**" ✓✓✓
【条件版本（原文 §7.2(f) ✓）】HL*(k₀)：对 k ≤ k₀，tr G̃^k = d·m_k(1)(1+o(1))（m_k = 极限谱的第 k 阶矩）✓
【⭐ 一般框架（原文 §7.2(d) ✓✓）】若矩已知到 **k ≤ 2m**，则 **n₊(G̃)/d 的尖锐下界 = 1 − Λ_m(0)**，
   **Λ_m = 矩序列在 0 处的 Christoffel 函数** ✓✓✓
⟹ ⭐ **对我们的意义**：
   ① **我们此前的预言（"任何固定有限阶矩都无法强制个体 β"）与前沿结论【一致】** ✓✓
   ② **但前沿的理由是【定量的】**（Rudnick–Sarnak 范围 X^k ≤ T^{2−ε}，X ≍ T 时只允许 k=1 ✓）——
      **这是我们此前没有的精确机制** ✓✓
   ③ **Christoffel 函数框架【正好是我们矩问题工作的对接口】** ✓✓（我们做过 Hankel 行列式/矩确定性 ✓）
```

### 发现 2：**Bombieri [Bom00] 中含【我们的 P27 结果】** ✓✓✓
```
【Conrey 调查报告原文 ✓✓✓】"Bombieri considers a general situation where the numbers in Γ are arbitrary
   but have the same symmetries as do zeta-zeros. He shows that **all of the eigenvalues Λ are real**,
   and that **if all of the γ ∈ Γ are real then all of the eigenvalues Λ are positive**.
   In fact, **the number of non-real pairs of conjugate γ is exactly equal to the number of negative
   eigenvalues.**" ✓✓✓
⟹ **= 我们的 P27-G8（n₋(K_ρ)=1 每离轴对）【完全一致】** ✓✓ —— **且是 2000 年的结果** ✗
   ⟹ **我们的 P27 系列必须标为"Bombieri [Bom00] 观察的重现/独立验证"** ✓✓（**已修正** ✓）
【附带】Bombieri 另有：【Bom03】"A variational approach to the explicit formula"（2003 ✓）
   ｜【Bom05】"The Rosetta Stone of L-functions"（2005 ✓）｜并**构造了 Weil 泛函的极值函数** ✓
⟹ ⚠️ **新对齐点**：其**变分方法**可能与我们的**变分定理（在线零点唯一最小化 S_proj）**相关 ✓（**待读 Bom03** ✓）
```

## §3 **参考文献线索（原文 ✓，供后续阅读）**
```
[BGSTB24] Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, **An unconditional Montgomery theorem for
   pair correlation of zeros**, Acta Arith. 214 (2024) 357–376 ✓（**无条件一对相关** ✓）
[BGSTB25] 同上作者, **Pair correlation of zeros of the Riemann zeta function I: proportions of simple
   zeros and critical zeros**, arXiv:2501.14545 ✓✓（**直接的"比例"前驱** ✓ 优先读 ✓）
[BHB13] Bui–Heath-Brown（简单零点 ✓）｜[Bom00]（负指标 ✓）｜[Yos92]（小支集正性 ✓）
[Ary22]（Fejér 核优先权 ✓）｜[CCLM17]（最优窗 ✓）｜[CGdL20]（RH 下 SDP ✓）｜[GS25,GS26] ✓
```

## §4 **A3 完成度：95%**
```
【✅】证明架构 ✓✓｜素数侧 (P) 的精确内容 ✓✓｜R(ψ) 显式 ✓✓｜天花板 ✓✓｜法域归属 ✓✓｜
   与我们工作的深刻呼应 ✓✓｜高阶矩已被回答 ✓✓｜Bombieri 对齐 ✓✓
【✗ 余 5%】**§2 测试族构造**｜**§3 (1.1) 完整证明**｜**§6 链 (1.2)**｜**Lemma 2.1 / (L)**｜
   **§7.2 全文**（天花板的推导 ✓）｜引文 [Bom00] 原文、[BGSTB25]、[BGSTB24]、[Ary22]、[CCLM17] 等 ✗
```

## §5 边界
```
【原文级 ✓】§1（HTML §5 ✓✓）｜§2 发现 1（HTML §7.2(d)(e)(f) ✓✓）｜§2 发现 2（Conrey 调查报告 ✓✓）
   ｜§3 文献（Anthropic PDF ✓）
【⚠️ 二手】Bom00 的内容来自 **Conrey 的调查报告** ⚠️（非原文 ✓）⟹ **须读 Bombieri 原文确认** ✓
【⚠️ 未读】正文 §2/§3/§6、引文 7 篇 ✗
```
## §6 提交链
```
ALIGN-A3-COMPLETE（dac3ecd）→ 本篇（素数侧 + 高阶矩已被回答 + Bombieri 对齐）
```
