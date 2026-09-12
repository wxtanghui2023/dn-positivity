# P8 经典原始文献核查（一手阅读）：Li 1997 (A) 与 Bombieri–Lagarias 1999 (B)

**任务**：逐字核对 Li 判据的两篇原始文献，重点回答"是否含显式有限高度范围（如 `n ≤ (T−1)²`）"。
**本文件为唯一新增文件**；未提交；未修改任何其它文件。

证据分层（全文遵守，**不虚构引文**）：`[一手·全文]` 我读到全文｜`[一手·摘要]` 官方摘要原文｜`[二手·逐字转引]` 他人论文逐字引该文｜`[二手·概述]` 转述（不作逐字引用）｜`[OCR]` PDF 渲染后 OCR（数学符号可能有误）｜`[PS]` 作者 PostScript 逐字符解码（符号精度最高，字距信息缺失）。
## 0. 获取情况（一篇拿到、一篇没拿到）

| | (A) Li 1997, JNT **65** 325–333 | (B) Bombieri–Lagarias 1999, JNT **77** 274–287 |
|---|---|---|
| 状态 | **全文未获取** ✗ | **全文已获取** ✓ `[一手·全文]` |
| 途径 | 见下（全部失败） | **作者自存版**：`math.lsa.umich.edu/~lagarias/doc/bombieri.ps`（123,967 B, dvips, 12 页）＋同目录 `bombieri.pdf`（204,958 B）。这是本任务"TRY THIS HARD"的**成功路径** ✓ |
| 版本 | — | 头 `%DVIPSSource: TeX output 1998.08.11` ⇒ **1998-08-11 预印本**；JNT 正式版页码/编号可能不同，内容一致（摘要逐字一致） |

**(A) 获取失败记录**：ScienceDirect 文章页/PDF → `403`（1.2 MB 反爬 HTML）。OpenAlex/Semantic Scholar/Unpaywall **三方一致**指向 `.../S0022314X97921375/pdf`，`oa_status: bronze`（**免费但被反爬封锁**，非付费墙）。**无 arXiv 预印本**（arXiv API `au:"Xian-Jin Li"` 返回其 12 篇，不含此文）。作者 BYU CV 页**只有标题无 PDF**。代理/缓存全败：`r.jina.ai` 超时、`allorigins` 408、`core.ac.uk` 403、`scholar.archive.org` 与 `web.archive.org`/`archive.org` 连接超时（NAS 不可达）。⇒ **(A) 的一切陈述均为二手**，置信度逐条下调。

## 1. 序列 λ_n 的精确公式、下标与归一化

**1.1 (B) `[一手·全文]`（`[PS]` 逐字符校核）** §1 原文：
> 「His criterion can be stated in terms of the Riemann ξ-function
> **ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s)**
> and the sequence **λ_n = 1/(n−1)! · (d^n/ds^n)[ s^{n−1} log ξ(s) ] |_{s=1}**, for n = 1,2,3,…,
> in the form that the Riemann Hypothesis is equivalent to the statement that **λ_n > 0 for every positive integer n**.」

同节给出等价零点表示（`[PS]`：`Σ_ρ = lim_{T→∞} Σ_{|ℑ(ρ)|<T}`）：
> 「The number λ_n can be written in terms of the complex zeros ρ … as **λ_n = Σ_ρ [1 − (1 − 1/ρ)^n]**, where the sum Σ over ρ is understood as Σ_ρ = lim_{T→∞} Σ_{|ℑ(ρ)|<T}.」

- **下标从 n = 1 开始**（无 n=0）；归一化 **1/(n−1)! = 1/Γ(n)**；ξ 用 `½s(s−1)π^{−s/2}Γ(s/2)ζ(s)`（**非** Ξ 归一化）。
- ⚠️ 以上是 **(B) 对 (A) 的转述**。

**1.2 (A) Li 1997（全文未获取）** Maślanka (2004, Opuscula Math. 24, 103–114) 逐字重述 Li 的定义，并**标明 (5) 出自 Li 原文的 formula 1.4** `[二手·逐字转引]`：
> 「Theorem 1. RH is true if and only if all coefficients **λ_n := 1/Γ(n) · d^n/ds^n [ s^{n−1} ln ξ(s) ]|_{s=1}** (3) are non-negative, where **ξ(s) = 2(s−1) π^{−s/2} Γ(1 + s/2) ζ(s)** (4). An equivalent definition of λ_n is (see [Li], **formula 1.4**): **λ_n = Σ_ρ (1 − (1 − 1/ρ)^n)** (5), where the sum runs over all (paired) complex zeros of the Riemann zeta-function.」

- `1/Γ(n) = 1/(n−1)!` ✓ 与 (B) 一致；Maślanka 的 ξ 与 (B) 的 ξ **为同一函数**（`s·Γ(s/2)/2 = Γ(1+s/2)`），其 "2" 系数疑为抄录噪声。
- ⇒ **Li 原文确有编号 (1.4)** 给出 `λ_n = Σ_ρ[1−(1−1/ρ)^n]`；但我**未见到 (1.4) 原文图像**。(B) 亦佐证 Li 的编号体系：BL 引 **"[3, formulae (1.6) and (3.5)]"**（Li 证明中 a_ν、b_ν 的取法）`[一手·全文]`。

## 2. 主定理（Li 判据）逐字陈述

**2.1 (B) 的 Li 判据 = Corollary 1** `[一手·全文]`（`[PS]`+`[OCR]` 双读一致）：
> 「**Corollary 1. (Li's Criterion)** Let R be a multiset of complex numbers ρ such that
> (i) 0, 1 ∉ R; (ii) if ρ ∈ R then 1 − ρ and ρ̄ are in R, with the same multiplicity as ρ;
> (iii) Σ_ρ (1 + |ℜ(ρ)|)/(1 + |ρ|)² < +∞.
> Then the following conditions are equivalent:
> (a) ℜ(ρ) = 1/2 for every ρ;
> (b) **λ_n = Σ_ρ [1 − (1 − 1/ρ)^n] ≥ 0 for n = 1,2,3,…**;
> (c) for every fixed ε > 0 there is a constant c(ε) such that **Σ_ρ [1 − (1 − 1/ρ)^n] ≥ −c(ε)e^{εn}, n = 1,2,3,…**.」

`[一手·摘要]`（Elsevier/Nokia Bell Labs 官方摘要，与预印本一致）：**"has λ_n > 0 for n = 1,2,3,…"**（摘要用严格 >0，推论用 ≥0）。

**2.2 (B) 更一般的 Theorem 1（半平面版）** `[一手·全文]`：
> 「**Theorem 1.** Let R be a multiset of complex numbers ρ such that (i) 1 ∉ R; (ii) Σ_ρ (1 + |ℜ(ρ)|)/(1 + |ρ|)² < +∞.
> Then the following conditions are equivalent:
> (a) **ℜ(ρ) ≤ 1/2 for every ρ**;
> (b) **Σ_ρ ℜ[1 − (1 − 1/ρ)^{−n}] ≥ 0 for n = 1,2,3,…**;
> (c) … **Σ_ρ ℜ[1 − (1 − 1/ρ)^{−n}] ≥ −c(ε)e^{εn}**, n = 1,2,3,….」

⚠️ **两处指数符号不同，且原文如此（两次独立读取一致）**：Theorem 1 用 `(1−1/ρ)^{−n}`（`[PS]`=`«k»\x00«o»n`="−n"），Corollary 1 用 `(1−1/ρ)^{n}`。"−n" 版与证明用的枢纽恒等式 `|1 − 1/ρ|^{−2} = 1 + (2β−1)/|1−ρ|²` 配套。

**2.3 (A) Li 1997 主定理（全文未获取）**
- `[一手·摘要]`（唯一直接来自该文者）：「In this note, we prove that the Riemann hypothesis for the **Dedekind zeta function** is equivalent to the nonnegativity of a sequence of real numbers.」
- (B) §1 转述 `[一手·全文]`：RH ⟺ `λ_n > 0 ∀n`，且 Li **亦证明了 Dedekind ζ 的同一结论**。
- ⇒ (A) 主定理可安全认定为 **"RH ⟺ λ_n > 0 (∀n ≥ 1)，且对 Dedekind ζ 成立"**；**逐字原文无法提供**。

## 3. 逆方向（converse）

**(B)：给出，且是双向完整证明** `[一手·全文]`（Corollary 1 的 (a)⇔(b)⇔(c) 为全套等价）。逆方向论证末句 `[OCR]`：
> 「Hence the sum over |ρ| > n is O(n²) … while the remaining elements ρ_k contribute K − (1+t)^n Σ_{k=1}^K cos(nθ_k). … **By Dirichlet's theorem on simultaneous Diophantine approximation we can make the sum of cosines arbitrarily close to K, making it plain that Σ_ρ ℜ[1−(1−1/ρ)^{−n}] is infinitely often negative and exponentially large in absolute value as n tends to ∞. Thus the negation of (a) implies the negation of (c), hence (c) implies (a), concluding the proof.**」

即 **"RH 失效 ⇒ λ_n 无穷多次指数级为负"是 (B) 的原创严格结果**，机制是 **Dirichlet 联立丢番图逼近**。另：
> 「We show that **Li's criterion follows as a consequence** of a general set of inequalities for an arbitrary multiset of complex numbers ρ and therefore is not specific to zeta functions.」

**(A)**：Li 1997 亦证明双向（摘要 "is equivalent to"）`[一手·摘要]`；**其证明细节我未见**。

## 4. ⭐ 关键问题：两篇是否含任何"显式有限高度范围/阈值"？

### 结论：**(A) 与 (B) 都不含**。两篇中**都不存在**形如「if RH is verified up to height T then λ_n ≥ 0 for all n ≤ f(T)」**的任何语句**。

**证据 (B)（一手全文）**：对 12 页全文（`[OCR]` 17.8 KB + `[PS]` 全文）穷举检索 `height` / `verified` / `numerical` / `known zeros` / `up to` / `first n` / `T₀` —— **仅 1 处无关命中**（"which may be verified as follows"，指某初等积分恒等式的验证）。判据始终写作 **"for n = 1,2,3,…"**（全 n），**无任何有限高度截断**。
- BL 中**唯一定量陈述**是：(i) 指数下界 `≥ −c(ε)e^{εn}`；(ii) 逆方向"**无穷多次**指数级为负"；(iii) §2 Remark 把 (a) 等价于生成函数在单位圆盘的全纯性/增长条件（**非**高度截断）。
- **(B) 全文不含 `Oesterlé/Oesterle/Voros` 字样**，也不含任何"已验证到某高度"的提法。

**(A)**：全文未获取，故**不能给出"原文确无"的严格断言**。但 ①摘要只说等价性；②(B)（同年、直接继之并系统推广 Li 判据）**未提任何高度范围**；③**没有任何二手文献把"有限高度范围"归给 Li 1997**（该说法一律归于 **Oesterlé 未刊稿**）。

### 4.1 "(T₀−1)²" 类说法的真正出处（**不在 (A)(B) 中**）
1. **Oesterlé 未刊稿** `[二手·逐字转引]`（Voros 2022, HAL `cea-03673957` 参考文献）：
   > 「[24] J. Oesterlé, **Régions sans zéros de la fonction zêta de Riemann**, typescript (2000, revised 2001, **uncirculated**).」
2. **Voros 2022 逐字的范围式命题** `[二手·逐字转引]`（同文件 §2.2.2）：
   > 「However: **[24]** **ℜρ ≡ 1/2 holds up to a height T₀  ⟹  λ_n > 0 as long as n < T₀².** [原文排版即 `n < T 2 0`]
   > This means that low values of n are actually inessential for Li's criterion: we may focus on the asymptotic n → ∞ behavior of λ_n instead.」
   同文件式 (23) 给出机制：`a term z_{ρ′}^{−n} from (21) will compete in size with (22) if **n ≳ T²/t** (for ρ′ = 1/2 + t ± iT, t > 0) … the **uncertainty principle for the Fourier-conjugate variables θ and n**`。
3. **Maślanka 2004** 更早转述同一观察 `[二手·逐字转引]`：
   > 「In fact, **Oesterlé observed recently (in an unpublished note, ⟨ref⟩) that if the first n complex zeros of zeta are located on the critical line, then the Li positivity criterion should hold for about the first n² Li coefficients** (see ⟨ref⟩, **p. 441**). Therefore, direct numerical search for a possible counterexample to RH using Li's criterion is rather a hopeless task.」
   ⚠️ 该 PDF 的 ⟨ref⟩ 为超链接，**在可得文本中被剥离**，故 **"p. 441" 指向哪篇我未能确定**。注意措辞差异：Maślanka 是「**前 n 个零点 ⇒ 约前 n² 个系数**」（n = 零点数），Voros 是「**高度 T₀ ⇒ n < T₀²**」（T₀ = 高度）。
4. **反面对照**：Voros 自己的 *A sharpening of Li's criterion*（arXiv `math/0404213v2`, 2004）检索**无** Oesterlé、**无** height、**无** T₀²；*Sharpenings of Li's criterion*（arXiv `math/0506326v2`）只说 **"Oesterlé had a proof of the statement [RH true] ⇒ (17)"**（(17) 即渐近式 `λ_n ∼ ½n(log n − 1 + γ − log 2π)`），**不是**有限高度范围；另有可探测性估计 `S_n` 只能可靠显示至高度 `|ℑρ| ≲ √(n/2)`。
   ⇒ **"T₀²" 命题只在 Voros 2022 以 "However: [24]" 出现，来源为 Oesterlé 未刊 typescript；Voros 2004/2006 两篇正文都把 Oesterlé 的贡献记为"渐近式的证明"。**

## 5. 证明架构（(B)，一手全文）

**§2（纯复分析/任意多重集）**：
- **Lemma 1**（绝对收敛）：分支约定（ρ=0 时 `(1−1/ρ)^{−n}` 对正整数 n 视为 0、负整数视为 ∞）+ `Σ_R (1+|ℜρ|)/(1+|ρ|)² < ∞`（式 2.1）⇒ 对一切整数 n 绝对收敛；若 `Σ 1/ρ` 为 ∗-收敛则 λ_n 亦然。
- **Theorem 1**：(a)⇔(b)⇔(c)。
  - **(a)⇒(b)** 初等：`|1−1/ρ|^{−2} = 1 + (2β−1)/|1−ρ|²`（**全文枢纽恒等式**）⇒ ℜρ ≤ ½ ⇒ `|1−1/ρ|^{−1} ≤ 1` ⇒ 每项实部 ≥ 0。
  - **(b)⇒(c)** 平凡。
  - **¬(a)⇒¬(c)**：分离 |1−1/ρ|^{−1} 的**最大值**（有限个 ρ_k，值 `1+t`）；其余项 `O(n²(1+t−δ)^n)`；余下 K 项给 `K − (1+t)^n Σ_k cos(nθ_k)`；再用 **Dirichlet 联立丢番图逼近**使 cos 和任意接近 K。**唯一非平凡步骤，也是逆方向的全部难度。**
- **Corollary 1**：对 R **与 1−R** 各用一次 Theorem 1（条件 (ii) 保证 λ_n 为实且 `λ_n = λ_{−n}`）。Remark：条件 (iii) 可放宽为 `Σ 1/(1+|ρ|)² < ∞`。

**§3（算术解释）**：陈述 Weil[4]/Guinand[2] 的 **Explicit Formula**（Mellin 形式），把 Li 判据解释为该公式上一族**具体检验函数**的正定性 → **Lemma 2** → **Theorem 2**（λ_n 的算术公式）。证明中**唯一用到零点分布知识处是 de la Vallée-Poussin 无零点区域**（**不用任何高度范围内的 RH 验证**）。
**§4**：Weil 正定性与 Li 判据；λ_n 与 Stieltjes 常数 γ_n 的关系。

## 6. (B) 与 Weil 显式公式/Weil 正定性；检验函数；阿基米德位 vs 有限位

**6.1 检验函数（核心；注意：文中并未出现 "Laguerre"）**
**全文穷举确认：(B) 中 "Laguerre" 出现次数 = 0。** 该命名是任务方（及部分二手文献）的印象，(B) 原文未如此称呼。**Lemma 2 逐字**（`[PS]` 校核）：
> 「**Lemma 2.** For n = 1,2,3,… the inverse Mellin transform of **1 − (1 − 1/s)^n** is
> **g_n(x) = P_n(log x) if 0 < x < 1;  n/2 if x = 1;  0 if x > 1**,
> where P_n(x) is the polynomial **P_n(x) = Σ_{j=1}^{n} C(n,j) x^{j−1} / (j−1)!**.」

`[二手·逐字转引]`（Conrey 调查, aimath.org）引法一致：`P_n(x) = Σ_{j=1}^n (n j) x^{j−1}/(j−1)!`。
**客观评述（我的推导，非引文）**：`P_n(x) = Σ_{k=0}^{n−1} C(n,k+1) x^k/k! = L_{n−1}^{(1)}(−x)`，**确为广义 Laguerre 多项式**；但 **(B) 既未用其名、也未引 Laguerre**。若我方要写"Laguerre 多项式"，须注明"等价改写，原文未如此称呼"。该多项式是把"零点求和 `Σ_ρ[1−(1−1/ρ)^n]`"翻译成"(0,1) 上显式测试函数"的桥梁。

**6.2 与 Weil 正定性（§4 逐字，`[一手·全文]` `[OCR]`）**
> 「The multiplicative convolution of f(x) and g(x) is given by (f ∗ g)(x) = ∫ f(x/y) g(y) dy/y.
> The Mellin transform of f ∗ g is f̂(s) ĝ(s), whence, denoting by f̄ the complex conjugate of f, **the Mellin transform of f̄ ∗ f is f̄(s) f(1−s), which is real and positive on the critical line ℜ(s) = ½**. Thus **the positivity of the Explicit Formula on functions of the type f̄ ∗ f is a necessary condition for the validity of the Riemann Hypothesis. As shown by Weil, this is also a sufficient condition.**
> Li's criterion can be interpreted quite easily in this light. Let g_n(x) be the function defined in the preceding section. We have the identity
> **[1 − (1 − 1/s)^n] + [1 − (1 − 1/(1−s))^n] = [1 − (1 − 1/s)^n] · [1 − (1 − 1/(1−s))^n]**
> and taking the inverse Mellin transform we find **g_n(x) + ⟨reflect⟩ g_n(x) = (g_n ∗ ⟨reflect⟩ g_n)(x)**.
> Since the right-hand side of the Explicit Formula is invariant by changing f(x) into f̄(x), **the positivity in Li's criterion has the same meaning as in Weil's criterion. The interesting point is that Li's criterion requires an explicit and rather simple set of test functions for its verification.**」

- 该**代数恒等式我已独立验证为真**：`(1−1/s)(1−1/(1−s)) = 1`，令 A=(1−1/s)^n, B=(1−1/(1−s))^n 则 AB=1，故 (1−A)+(1−B)=2−A−B=1−A−B+AB=(1−A)(1−B)。✓
- ⚠️ 逆 Mellin 那一行的"反射"记号：`[PS]` 显示 `«m»e g_n(x)`，`«m»e` 是**重音符号**（同 §4 的 f̄）；OCR 给 "Gn(2)" 之类噪声。**是复共轭 f̄ 还是 §3 定义的对合 f̃(x)=(1/x)f(1/x)，我无法最终判定**（如实标注）。**恒等式本身（上一行）确定。**

**6.3 Explicit Formula 的阿基米德位 vs 有限位分项**（`[PS]` 解码）：
> `Σ_ρ f̂(ρ) = ∫_0^∞ f(x)dx + ∫_0^∞ f̃(x)dx`  [= f̂(1)+f̂(0)，**阿基米德/极点项**]
> ` − Σ_{n≥1} Λ(n) n^{−1/2}{ f(n) + f̃(n) }`  [**有限位（素数）项**]
> ` − (log π + γ) f(1)`  [**阿基米德常数项**]
> ` − ∫_1^∞ { f(x) + f̃(x) − 2x²f(1)? } x dx/(x²−1)`  [**阿基米德积分项，需正则化**]
- f̃(x)=(1/x)f(1/x)（§3 的对合），保证 `∫_0^∞ f̃ = f̂(0)`。
- ⚠️ 末项中被减常数的**精确写法**（是否含 x² 因子）与常数是 `log π` 还是 `log 4π`，`[PS]`/`[OCR]` 不一致，**我对该项的逐字复述保留不确定性**。可确证：显式公式常数项 `[PS]` 显示 `−(log π + γ)f(1)`，而 §3 的 n=1 Remark 用 **`log 4π`**（"Σ_ρ 1/ρ = 1 + γ/2 − ½ log 4π = 0.0230957…"，`[PS]` 明确含 "4"）。
- (B) 述史时强调 Guinand[2]（1948）"*under the assumption of the Riemann Hypothesis*"，并引 Guinand 原话——**再次说明 (B) 关心测试函数类，而非数值高度。**

**6.4 Theorem 2（算术公式；`[PS]`+`[OCR]`，含不确定性）** 可确证骨架：
> `λ_n = − Σ_{j=1}^{n} (−1)^j C(n,j)/(j−1)! · lim_{ε→0+}[ Σ_{m ≤ 1/ε} Λ(m)(log m)^{j−1} m^{−1} − (log 1/ε)^j / j ] + ½(log 4π + γ)·n − Σ_{j=2}^{n} (−1)^j C(n,j)(1 − 2^{−j}) ζ(j)`

**独立交叉印证** `[二手·逐字转引]`（Voros 2022）：`Theorem 2 in [1] evaluates the differences (λ_n − S_n) where S_n = −Σ_{j=1}^n C(n,j) η_{j−1} = Σ_{j=1}^n (−1)^{j−1}/(j−1)! C(n,j) g^c_j`，且 `Our g^c_n corresponds to (−1)^n (n−1)! η_{n−1} in [1]`。
§4 逐字：式 **(4.1) η_n = (−1)^{n−1}/n! · lim_{x→∞}[ Σ_{m≤x} Λ(m)(log m)^n/m − (log x)^{n+1}/(n+1) ]** 与 **Stieltjes 常数 (4.2) γ_n = (−1)^n/n! · lim_{x→∞}[ Σ_{m≤x} (log m)^n/m − (log x)^{n+1}/(n+1) ]** 类比。

## 7. λ_n 的阶、以及 RH 失效时的 λ_n

**(B) 内（一手）**
- **指数下界**：Theorem 1(c)/Corollary 1(c)：`Σ_ρ ℜ[1−(1−1/ρ)^{−n}] ≥ −c(ε)e^{εn}`（对任意 ε>0，即增长至多亚指数）。
- **RH 失效时的形态**：`[OCR]`「…is **infinitely often negative and exponentially large in absolute value** as n tends to ∞」。
- §2 的**函数论等价**：生成函数 `f(z)=Π_ρ(1−z/ρ)` 下，(a) 等价于 `d/dz log f(1/(1−z))` 在单位圆盘全纯 ⟺ 某 `lim sup` 增长条件（`[OCR]` 显示形如 `limsup|λ_n − 1|^{1/n} ≤ 1`，**下标/常数受 OCR 干扰，不作逐字引用**）；(b)(c) 表明该双侧条件可被**单侧实部条件**取代。
- **(B) 全文不含 λ_n 的渐近主项**（如 `½n log n`）——那是 Keiper/Voros 的工作。

**(B) 之外（二手，仅供对照）** `[二手·逐字转引]` Voros 2022：RH 真则 `λ_n ∼ ½n[log n + (γ − log 2π − 1)]`；RH 假则指数增长振荡，且 `n ≳ T²/t` 时偏离项才与主项竞争（`ρ′=½+t±iT`）。

## 8. 为什么 RH ⟹ 对所有 n 非负（(B) 给出的机制）

1. **逐项非负（局部机制，全 n 的来源）**：枢纽恒等式 `|1−1/ρ|^{−2} = 1 + (2ℜ(ρ)−1)/|1−ρ|²` ⇒ ℜρ ≤ ½ ⟺ `|1−1/ρ|^{−1} ≤ 1` ⇒ 对**每个 ρ、每个 n** 有 `ℜ[1−(1−1/ρ)^{−n}] ≥ 0`。**无需任何渐近输入。**
2. **共轭/函数方程对合**：Corollary 1 条件 (ii)（ρ、1−ρ、ρ̄ 同重数）使 λ_n 为**实**，把"半平面"升级为"临界直线"。
3. **逆方向的量化代价**：若 (a) 失效，失败**只能在无穷多个 n 上**表现为指数级负值；而要"看见"它需 n 足够大 —— 即 §4.1 的 `n ≳ T²/t`（不确定性原理/Fourier 对偶）。⇒ **低 n 的非负性对判据本质无贡献**（Voros: "low values of n are actually inessential"）。
4. **(B) 自身不讨论 (3)**；(B) 只断言"无穷多次指数级为负"。**把 (3) 量化为 `n < T₀²` 的是 Oesterlé/Voros，不是 (A)(B)。**

## 9. ⭐ 对本项目具体问题的直接回答

**问**：我们的 `λ_n ≥ 0 for 2 ≤ n ≤ 2T − O(1)`（T = 已验证零点高度）与文献 `n ≤ (T₀−1)²`（Oesterlé 2000 未刊，经 Voros 转引）——**这两篇经典里是否有任何显式有限高度范围？**

1. **(B) Bombieri–Lagarias 1999：没有。** 一手全文 12 页穷举检索：判据一律 **"n = 1,2,3,…"**；无 height、无 "verified up to"、无任何 `f(T)` 形式上界；唯一定界是**指数型** `−c(ε)e^{εn}`。**置信度：高（一手全文）。**
2. **(A) Li 1997：全文未获取，无法穷举断言。** 可得材料（官方摘要 + 两处二手逐字重述）**均无**任何高度范围；且 (B) 在完整重述并推广 Li 判据时亦未提。**置信度：中高（因未读原文而保留）。**
3. **"(T₀−1)²" 确实存在，但不在这两篇里。** 文本出处：**Voros 2022 逐字「ℜρ ≡ 1/2 holds up to a height T₀ ⟹ λ_n > 0 as long as n < T₀²」**，标注来源 **[24] Oesterlé, typescript (2000, revised 2001, uncirculated)**；更早 **Maślanka 2004 逐字「if the first n complex zeros … are located on the critical line, then the Li positivity criterion should hold for about the first n² Li coefficients」**（注 "unpublished note", "p. 441"）。
   ⚠️ **两处范围形式不同**：Voros 是 **高度 T₀ → n < T₀²**；Maślanka 是 **零点数 n → 约 n² 个系数**。本项目若用 `(T₀−1)²`，**须明确 T₀ 的定义（高度 or 零点个数），并注明是"经 Voros 转引的 Oesterlé 未刊结果"**，**不可引作 Li 1997 或 BL 1999 的结论**。
4. **与我们 `2T − O(1)` 的关系**：若两者 T 同为"已验证高度"，则 **`n < T₀²` 比 `n ≤ 2T − O(1)` 强一个量级（宽约 T/2 倍）**——文献已给出远强于我们"相窗"论证的先验对照。反之，Voros 的机制写作 **`n ≳ T²/t`**（t = 违反零点实部偏离量），**是量级式/启发式**，且 Oesterlé 原件 "uncirculated"、**无公开严格证明**——**这可能是我们仍可贡献"严格化/常数化"的缝隙。（此条为我的分析判断，非引文。）**

## 附录 A：一手材料清单（可复现）
- `math.lsa.umich.edu/~lagarias/doc/bombieri.ps`（123,967 B, dvips；`TeX output 1998.08.11`）与同目录 `bombieri.pdf`（204,958 B，Type-3 位图字体，**直接抽文本为乱码**，故用 400 dpi 渲染 + tesseract OCR）
- Voros: `arXiv:math/0404213v2`、`arXiv:math/0506326v2`、HAL `cea-03673957`（2022）
- Conrey, *Riemann's Hypothesis*（aimath.org/~kaur/publications/90.pdf）；Maślanka, Opuscula Math. 24 (2004) 103–114
- 本项目既有 `external_refs/conrey-li-positivity.pdf`（Conrey–Li 2000, IMRN 18）

## 附录 B：遗留缺口（如实登记）
1. **(A) Li 1997 全文**仍缺；唯一可行下一步是人工经机构/图书馆访问 ScienceDirect（bronze OA，文章页明写 "Open archive / Under an Elsevier user license"）或索取扫描。
2. Maślanka **"p. 441"** 的指向未解（超链接编号被剥离）。
3. (B) §4 逆 Mellin 行重音符号（复共轭 f̄ vs 对合 f̃）未判。
4. (B) Explicit Formula 末项的精确写法、`log π` vs `log 4π`：`[PS]`/`[OCR]` 不一致，未判。
5. (B) §2 Remark 的 `lim sup` 表达式 OCR 不可靠，未作逐字引用。

## 对本项目的意义

1. **一句话结论**：`λ_n ≥ 0 for 2 ≤ n ≤ 2T − O(1)` 这类**有限高度窗口**结果，在 **Li 1997 与 Bombieri–Lagarias 1999 中【完全不存在】**。两篇经典只讲"**全 n**"的等价性（BL 更给出一般多重集的半平面判据）。故我们的窗口结果既非"被经典做过"，也非"被经典反驳"——是**新的一类陈述**，但**没有先例为我们的常数/形状背书**。

2. **真正要对齐的先验是 Oesterlé/Voros，而非 Li/BL。** 文献窗口式命题是 Voros 2022 逐字 **`ℜρ≡1/2 up to height T₀ ⟹ λ_n > 0 as long as n < T₀²`**（源于 Oesterlé 2000/2001 未刊 typescript），另有 Maślanka 2004「前 n 个零点 ⇒ 约前 n² 个系数为正」。**若 T 同义，`n<T₀²` 比我们的 `2T−O(1)` 强约 T/2 倍**——必须写进 related work，不能装看不见。

3. **可能的真缝隙**：Voros 机制写作 `n ≳ T²/t`，是**量级式/启发式**，Oesterlé 原件 uncirculated、**无公开严格证明**。若我们的相窗论证能给出**带一致常数、对 t 一致**的严格窗口（哪怕弱于 T²），那是**可发表的真贡献**；若只是把 Oesterlé 量级重推一遍，则**不新**。

4. **BL 的两个可复用资产**（此前可能低估）：①枢纽恒等式 `|1−1/ρ|^{−2}=1+(2β−1)/|1−ρ|²` + Dirichlet 联立逼近给出的**逆方向"无穷多次指数级为负"**；②`P_n(x)=Σ_{j=1}^n C(n,j)x^{j−1}/(j−1)!`（`=L_{n−1}^{(1)}(−x)`）这族**显式测试函数**，以及 §4 恒等式把 Li 正定性与 **Weil 正定性**接上——**这是把"λ_n 窗口"翻译成"Weil 二次型窗口"的现成桥梁**。

5. **引文纪律修正**：①"Laguerre 多项式"**不是 BL 用语**（全文 0 次），若用须写"等价改写为 `L_{n−1}^{(1)}(−x)`，原文未如此称呼"；②`(T₀−1)²` **不得引作 Li 1997 或 BL 1999 的结论**，只能引作"Oesterlé 未刊稿，经 Voros 2022 / Maślanka 2004 转引"；③注意两者范围形式不同（高度 T₀² vs 零点数 n²），别混引。

6. **未获取项**：Li 1997 全文仍未到手（bronze OA 但被反爬封锁），其"逐字定理"目前只能以官方摘要 + 二手转引支撑；报告已逐条标注置信度。建议论文中凡引 Li 1997 处**只引其摘要可证之内容**（等价性 + Dedekind 版本），细节引 BL 或 Conrey–Li。
