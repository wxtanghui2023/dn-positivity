# 🔍 **E39 审计 v2（完整读 PDF 后）**：arXiv:2411.16777

**依据**：唐先生 22:58（"PDF 需要仔细，完整阅读"）｜**已读**：Definition 1 + Theorem 1–5 及其证明关键段落 ✓✓
**标注**：【原文 ✓】＝直接引自 PDF 文本；【审计】＝我方推理

---

## §1 **该文的五条定理（原文 ✓）**
```
【Definition 1】M_{FI+SGI}^{2D}：一个晶向**铁磁**，另一晶向**随机竞争性（铁磁/反铁磁）** ✓
【Theorem 1（Equivalence Theorem）】"**The zero distribution of the partition function of the 2D Ising
   model M_{FI+SGI}^{2D} is equivalent to the zero distribution of the Dirichlet function L(s,χ_k)
   (including ζ(s))**" ✓✓ —— ⭐ **承重定理**
【Theorem 2（Real Eigenvalues）】全部本征值**实**，且"**randomly distributed as** the Dirichlet function
   L(s,χ_k) and ζ(s)" ⚠️（表述不精确 ✗）
【Theorem 3（Hilbert–Pólya Space）】本征矢由 1D Ising 本征矢 + 与 ζ 相关相位构造 ✓
【Theorem 4（Unit Circle–Critical Line）】配分函数零点全在**复温度平面单位圆**上，可映射到临界线 ✓
【Theorem 5】非平凡零点是算子 **R = ½I + iH**（H 自伴，取为 2D Ising 的哈密顿量）的谱 ✓
```

## §2 ⭐⭐⭐ **关键机制：映射 u = s/(1−s)（原文 ✓，且我方熟悉 ✓✓）**
```
【原文 ✓】"The unit circle |u| = 1 can be mapped into the critical line ½ + it = s via the transformation
   **u = s/(1−s) = (½+it)/(½−it) → s**" ✓✓
【审计 ✓】这是**经典的【临界线 ⟷ 单位圆】对应** ✓ —— 且 **与我方 A1 的"初等恒等式"同一机制** ✓✓：
   |u| = |ρ/(1−ρ)| = 1/|1 − 1/ρ| ⟹ **|u| = 1 ⟺ |1 − 1/ρ| = 1 ⟺ Re ρ = ½** ✓✓✓（**完全相同** ✓）
⟹ ⭐ **该文的映射不是新机制** ✓ —— **等于 Li 判据/Lagarias 框架里那个经典单位圆映射** ✓
```

## §3 ⭐⭐⭐⭐ **审计：四个问题（按严重度，均有原文依据 ✓）**

### ★★★★★ **问题 1（决定性·循环论证）—— Theorem 5 的证明**
```
【原文（Theorem 5 的 proof ✓✓）】
   "…the unit circle … also assures the existence of only a critical line… Moreover, **it is verified that
    no nontrivial zeros lie off the critical line.** **However, this ensures only the imaginary part of R,
    while the real part needs to be fixed.** … Hardy proved that infinitely many zeros lie on the critical
    line. Up to date, 100 billions nontrivial zeros have been found to lie on the critical line. **The
    Hardy's result and the computation … fixes already the real part of R.** If our critical line is located
    at σ = 1/2, it will be consistent with the Hardy's proof and the computation …, else it will be
    contradictory with them. **This excludes the possibility that the critical line is off σ = 1/2.**" ✓
【审计 ✗✓】
   ① 文中"**it is verified that no nontrivial zeros lie off the critical line**" ——
      **这【就是】Riemann 假设本身** ✓✓ ⟹ **该句为【断言】，非结论** ✗
   ② 文中**自认**："this ensures only the **imaginary part** of R, while the **real part** needs to be
      fixed" ✓ —— 而 **实部 = ½ 正是 RH 的内容** ✓✓
   ③ **Hardy 定理**给**无穷多个**零点在线 ✓（**非全部** ✗）；
      **数值**只覆盖**前 10¹¹–10¹² 个** ✓（**非全部高度** ✗）
   ⟹ ⭐ **"与 Hardy + 数值不矛盾"【不能排除】临界线偏离 σ=½** ✓✓✓
   ⟹ **该论证【以待证结论为前提】** ✓✓ —— **决定性缺陷** ✓
```

### ★★★★ **问题 2（承重定理未证）—— Theorem 1**
```
【原文（Theorem 1 的 proof）虽给出 Hamiltonian 与配分函数的具体形式 ✓，但**"零点分布等价"**这一步
   本质上就是**该路径的全部困难** ✓✓】
【⭐ 作者自己承认（结论段 ✓✓）】"**The main obstacle of the path is to find an appropriate model to
   satisfy the condition that the zero distribution of the partition function is equivalent to the
   distribution of the nontrivial zeros of the Riemann zeta function**" ✓✓✓
⟹ **即：承重定理（等价性）是路径的【障碍】，而文中把它当作【已证】** ✗✓
```

### ★★★ **问题 3（单位圆缺正性前提）—— Theorem 4**
```
【原文】其证明由（40）式（含 2cosh/2sinh 的乘积表示）⟹ "Z = ∏ Z̄_α ⟹ **all the zeros of Z lie on a
   unit circle**" ✓ —— ⚠️ **该步未给证明** ✗
【审计 ✓】Lee–Yang/Fisher 的**单位圆结论依赖铁磁/正性（Markov 性）** ✓；
   该模型**含随机反铁磁耦合** ⟹ **前提不成立** ✗✓
【我方资产 ✓✓】我们的 **TP₅ 失败**（7 个负子式，120 位稳定 ✓ + Gaussian 对照 ✓）
   ⟹ **正是检验此类亚正性主张的标准工具** ✓✓ —— **说明：验单位圆结论须先验正性** ✓
```

### ★★ **问题 4（表述不精确）**
```
【Theorem 2】"randomly distributed **as** the Dirichlet function L(s,χ_k) and ζ(s)" ⚠️
   —— **未指明是何种统计量**（分布？谱？相关？）✗
【"100 billions" 数值】⚠️ 稍旧（现为 Platt–Trudgian **3.0×10¹²** ✓）
```

## §4 ⭐⭐⭐⭐ **审计判决 + 与我们的三重呼应**
```
【判决】**该文未能建立其主张（RH / Hilbert–Pólya）** ✗✓ ——
   ① **Theorem 5 的证明循环**（"no zeros off" = RH 本身 ✓；Hardy/数值不能定实部 ✓）
   ② **Theorem 1（等价性）未证**，而作者自认它才是障碍 ✓
   ③ **Theorem 4 的单位圆缺正性前提** ✓
【⭐ 三重呼应（与我们此前的工作）】
   ① **机制相同**：其 u = s/(1−s) 映射 = **我方 A1 的经典恒等式**（|1−1/ρ|=1 ⟺ Reρ=½ ✓）✓✓
   ② **主题相同**：其缺口正在"**等价性/转换**" ⟹ **又一次印证我方中心命题
      "转换才是全部内容"** ✓✓✓（**Burnol 的"无信息"自述是第一次 ✓，本篇是第二次** ✓✓）
   ③ **工具对口**：其单位圆结论需要**正性**，而**我方 TP/正性工具**正是检验手段 ✓✓
【对外部的价值】⭐ **可作为"物理路线等价性主张的审计准则"的示范案例**（E39c ✓）
```

## §5 边界
```
【原文级 ✓✓】Definition 1｜Theorem 1–5 的陈述及其证明的关键段落（含 §3.1/§3.4 与结论段引文 ✓）
   —— **承重段落（Thm 1 的 Hamiltonian、Thm 4 的 (40) 式、Thm 5 的收尾论证）均已读到** ✓
【未读 ✗】中间推导细节（Eq. 34 的定义、(40) 的完整来源、附录 ✓）
【⚠️ 公平】作者明确指出该路径的障碍（"main obstacle" ✓），且承认 GM 进展"still far from
   the desired solution" ✓ —— **本审计针对的是【已发表的推理链】，非作者的诚实度** ✓
```

## §6 提交链
```
E39 初版（3e6b070）→ **本篇（完整读 PDF 后：循环论证定位 + 三重呼应）**
```
