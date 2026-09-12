# P8-GROUP6 — Voros / Oesterlé / Bucur 三目标原文核验

**任务**：读三份目标文献的**全文**（非摘要）并逐条报告｜**执行**：subagent（P8-GROUP6）｜**日期**：2026-09-12
**结果**：✅ 三个目标**全部找到**；A、B 取得原文/原刊正文，C 取得出版社 OA 全文 PDF。
**引文保真度说明**：A 的引文来自 arXiv:1703.02844 的 ar5iv HTML（由 LaTeX 源渲染，公式经 alttext 逐字核对 ✓）；B 的引文来自 AMS / AGH / Numdam PDF 的文本抽取（上标被压平，已手工还原 ⚠️）；C 的引文来自 Cambridge Core OA PDF 的分块抽取（个别句子在块边界被截断，已标 ⚠️）。**未找到**的项已明示，**未臆测任何标题/编号/引文**。

---

## 目标 A — Voros（约 2020）中引用 Oesterlé 2000 未发表结果的那篇论文

### A.1 书目（两层，均已核验）
**主目标**（"约 2020"）
- A. Voros, *Discretized Keiper/Li Approach to the Riemann Hypothesis*, **Experimental Mathematics 29(4) (2020) 452–469**；DOI 10.1080/10586458.2018.1482480 ✓
- 预印本 **arXiv:1703.02844**（v1 2017-03-08）；arXiv 页面刊载栏原文："Exp. Math. online 17 Jul 2018, print vol. 29(4) (2020) p. 452-469"；报告号 CEA-Saclay IPhT17/030 ✓
- 交叉源：arXiv API（标题/日期 ✓）＋Semantic Scholar（venue=Experimental Mathematics, vol 29, pp. 452-469 ✓）；HAL 版本 cea-01696126（同文，2018 上传）

**次目标**（同一引文的第二处）
- A. Voros, *From asymptotic to closed forms for the Keiper/Li approach to the Riemann Hypothesis*, **arXiv:2204.01036**；RIMS 京都 workshop 报告（Oct. 2021；v2 2022）✓

### A.2 Oesterlé 结果——Voros 的逐字陈述
（arXiv:1703.02844 §1.3.2，**节标题**即 "Oesterlé's argument for the RH true case [26]"）

> "In 2000 Oesterlé **[26, prop. 2]** proved (but left unpublished **[6, § 2.3]**) that"
>
> **[eq. (13)]** "Re ρ = ½ for all zeros with |Im ρ| ≤ T₀  ⟹  λ_n ≥ 0 for all n ≤ T₀²"

LaTeX 原文（ar5iv alttext，逐字保留）：
```
\mathop{\rm Re\,}\nolimits\rho={\textstyle{1\over 2}}\mbox{ for all zeros with }|\mathop{\rm Im\,}\nolimits\rho|\leq T_{0}\ \ \Longrightarrow\ \ \lambda_{n}\geq 0\mbox{ for all }n\leq T_{0}^{\,2}
```

arXiv:2204.01036 §2.2.2（措辞略异：**严格**不等号）：
> "Re ρ = ½ holds up to a height T₀ ⟹ λ_n > 0 as long as **n < T₀²**."
> "This means that low values of n are actually inessential for Li's criterion: we may focus on the asymptotic n → ∞ behavior of λ_n instead."

### A.3 Voros 参考文献条目（逐字）
- [26]（1703）/ [24]（2204）: "J. Oesterlé, *Régions sans zéros de la fonction zêta de Riemann*, typescript (2000, revised 2001, uncirculated)." ✓（两文一致）
- [6]（1703）: "P. Biane, J. Pitman and M. Yor, Probability laws related to the Jacobi theta and Riemann zeta functions, Bull. Amer. Math. Soc. 38 (2001) 435–465." ✓
⟹ Oesterlé 本体**未发表**；Voros 的 "[6, § 2.3]" 指向 **BPY 2001 §2.3** 作为公开出处（→ 目标 B 已核实 ✓）。

### A.4 Voros 自己证明的 vs 归给 Oesterlé 的
| 内容 | 归属 | 证据 |
|---|---|---|
| λ_n ≥ 0 for n ≤ T₀²（RH 验证至 T₀） | **Oesterlé 2000**（Voros 明示；§1.3.2 标题即 "Oesterlé's argument"，且括注 "(reworded by us)"）| ✓ |
| RH ⟺ λ_n > 0 ∀n（Li 判据）| X.-J. Li 1997（Voros 引 [20]）| ✓ |
| λ_n 的 n→∞ 渐近：RH 真 ⟹ λ_n ∼ n(A log n + B) | **Voros 本人**（arXiv:math/0506326）| ⚠️ 仅得摘要片段："…if (and only if) the Hypothesis is true, λ_n ∼ n(A log n + B) (with A > 0 and B …"（截断）|
| RH 假 ⟹ λ_n < 0 在 n→∞ 渐近区**必出现** | Voros 本人（由 eq. (18) 的 Darboux 展开）| 2204 §2.2.2 逐字："If RH is false, the last sentence about (18) implies that λ_n < 0 will occur in the asymptotic regime n → ∞." ✓ |
| 离轴零点 ⟹ 指数增长振荡项 | Voros 本人 | 2204 eq. (18)：λ_n^L = −Σ_{|z_ρ′|<1} z_ρ′^{−n} + o(r^{−n})；"If and only if RH is false, the sum in (18) is nonempty and then, ordered according to nondecreasing |z_ρ′| it forms an asymptotic expansion in exponentially growing oscillations about 0." ✓ |

### A.5 阈值的形式：验证高度 / 首个零点界 / 二者？
**二者其实是同一量。** Voros 写的是 "Re ρ = ½ **holds up to a height T₀**"，即"已被证明在临界线上"的最高高度：RH 若真，T₀ = 数值验证高度；RH 若假，T₀ = 首个离线零点的纵坐标（此时才叫 first-zero bound）。**数值上**，2204 §2.1.2 逐字给出当前值：
> "since 2004, up to the 10¹³-th zero ρ; that sets the largest ordinate T₀ up to which RH is verified to a current value ≈ **2.4·10¹²**."
⚠️ **结论：阈值不是 (T−1)²，也不是 (T₀−1)²，而是 T₀²。** "…(T₀−1)²…" 的说法在 Voros 原文中**未出现**（已全文检索 `Oesterl` 的全部命中位置，共 10 处，无一含 "(T₀−1)"）✗

---

## 目标 B — 同一结果在别处的独立陈述

### B.1 已发表源头（一手，最高价值）★★
**P. Biane, J. Pitman, M. Yor**, *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*, **Bull. Amer. Math. Soc. (N.S.) 38 (2001), no. 4, 435–465**；DOI 10.1090/S0273-0979-01-00912-0；预印 arXiv:math/9912170（1999）

**§2.3 "Li's criterion for the Riemann Hypothesis"，p. 441** 逐字：
> "We learned from J. Oesterlé (private communication) that **λ_n ≥ 0 if every zero ρ of ξ with |ℑρ| < √n has ℜρ = ½**. This is known to be true for **n ≤ 2.975 … × 10¹⁷**."
（PDF 把上标压平为 "1017"，原文即 2.975…×10¹⁷；算术自洽：2.975×10¹⁷ ≈ (5.454×10⁸)²，对应 van de Lune–te Riele–Winter 1986 年验证高度 ✓）

⟹ **与 Voros 的 (T₀²) 形式完全等价**：令 T₀ = √n，"|Im ρ| < √n 全在线上" ⟺ "RH 已验证至 T₀" ⟹ λ_n ≥ 0 for n ≤ T₀²。
⟹ 这是 Oesterlé 结果的**首次公开发表**处（正是 Voros 所引 "[6, §2.3]"）✓✓

### B.2 二手陈述（与 B.1 一致 / 需注意措辞差）
**K. Maślanka**, *Li's criterion for the Riemann hypothesis — numerical approach*, **Opuscula Math. 24 (2004), no. 1, 103–114**（Opuscula AGH OA PDF，已读）
> "In fact, Oesterlé observed recently (in an unpublished note, ⟨ref⟩) that **if the first n complex zeros of zeta are located on the critical line, then the Li positivity criterion should hold for about the first n² Li coefficients** (see ⟨ref⟩, p. 441). Therefore, direct numerical search for a possible counterexample to RH using Li's criterion is rather a hopeless task."
- ⟨ref⟩ = 抽取时丢失的文献编号，**未敢补全** ⚠️；但 "(see …, **p. 441**)" 与 BPY 的 p. 441 完全吻合 ⟹ 几乎确定即 BPY ✓（强证据，非直接证据 ⚠️）
- **措辞差**：BPY 用 "|Im ρ| < √n"；Maślanka 用"头 n 个零点在线上 ⟹ 头 n² 个 λ"，此处 **n 的含义不同**（零点个数 vs 高度），且带 "about" ⟹ 量级表述 ⚠️。二者**量级一致**（N(T) ≈ (T/2π)log T ⟹ 头 n² 个 λ 需 T ≈ n，与 √(n²)=n 吻合 ✓）

**J. C. Lagarias**, *Li coefficients for automorphic L-functions*, **Ann. Inst. Fourier 57 (2007), no. 5, 1689–1740**（Numdam OA PDF，已读）
> "Since the non-trivial zeros of ζ(s) are known to lie on the critical line up to height T ≈ 10⁹ we may **expect** the first 10¹⁶ Li coefficients will also exhibit similar asymptotic behavior, i.e. the term |S_f(n)| will remain small over this range."
⚠️ 是 **"expect"（期待）而非定理**，且 T≈10⁹ ⟹ T²≈10¹⁸ 与 10¹⁶ **不自洽**（疑笔误或不同约定）⟹ 仅作旁证，**低置信度** ⚠️
同文另一处（有用）："There is a probabilistic interpretation of some Li coefficients given in Biane, Pitman and Yor **[2, Sec. 2.3]**." ✓ 再次定位 BPY §2.3

### B.3 未找到
- **Oesterlé 2000 typescript 本体**（*Régions sans zéros de la fonction zêta de Riemann*）：**未找到** ✗（"uncirculated"，未发表）。已检索：arXiv API(全库标题/摘要/作者)、HAL、CEA-Saclay/IPhT、Google、Semantic Scholar、OpenAlex、Numdam。无任何电子文本 ✗
- 项目内二手来源 **D-037**（T = √n+1）：本轮**未核验** ✗；其形式与 BPY 的 √n 一致，疑即源自 Oesterlé/BPY ⚠️

---

## 目标 C — Bucur–Ernvall-Hytönen–Odžak–Smajlović：RH **失效**时的 Li 系数

### C.1 书目
- A. Bucur, A.-M. Ernvall-Hytönen, A. Odžak, L. Smajlović, ***On a Li-type criterion for zero-free regions of certain Dirichlet series with real coefficients***, **LMS J. Comput. Math. 19 (2016), no. 1, 259–280**；DOI 10.1112/S1461157016000115；OpenAlex oa_status = bronze；**出版社 OA 全文 PDF 已读** ✓
- 同组相邻（登记，未逐一通读）：*On τ-Li Coefficients for Rankin–Selberg L-Functions*（2015）；arXiv:1410.4384 *On generalized Li criterion for a certain class of L-functions*（2014）
- **未找到**这四位作者另有题为 "…Li coefficients…functions violating RH / few zeros" 的论文 ✗（已检索 arXiv API by author、Semantic Scholar by DOI/author、OpenAlex、Google）——本目标即上述 LMS JCM 2016 一篇 ✓

### C.2 摘要（逐字）
> "The Li coefficients λ_F(n) of a zeta or L-function F provide an equivalent criterion for the (generalized) Riemann hypothesis. In this paper we define these coefficients, and their generalizations, the τ-Li coefficients, for a subclass of the extended Selberg class which is known to contain functions violating the Riemann hypothesis such as the **Davenport–Heilbronn** zeta function. The behavior of the τ-Li coefficients varies depending on whether the function in question has any zeros in the half-plane Re(z) > τ/2. We investigate analytically and numerically the behavior of these coefficients for such functions in both the n and τ aspects."

### C.3 主要定理（逐字）
**Theorem 3.3**（Li 型判据 / 无零点区域）
> "Theorem 3.3. Let F ∈ S^]_R and let τ ∈ [1,∞) be such that 0, τ ∉ Z(F). Then the following statements are equivalent.
> (i) ξ_F possesses no zeros in the half-plane Re(s) > τ/2.
> (ii) λ_F(n,τ) > 0 for all n > 1.
> (iii) For every fixed δ > 0, there exists a constant c(δ) such that λ_F(n,τ) > −c(δ) exp(δn).
> (iv) lim sup_{n→∞} |λ_F(n+1,τ)|^{1/n} ≤ 1."

**Corollary 3.4**（同一清单的"条带"写法，逐字）
> "(i) All the non-trivial zeros of the function F lie in the strip 1 − τ/2 ≤ Re(s) ≤ τ/2. (ii) The τ-Li coefficients λ_F(n,τ) > 0 for all n > 1. (iii) … (iv) …"

### C.4 ★ RH 失效时 λ_n 的行为（本任务的关键）
**(a) 解析公式** —— eq. (3.9) 逐字：
> "λ_F(n,τ) = 2k − 2(1+m)^n ∑_{j=1}^{k} cos(nφ_j) − l(1+m)^n + O(n²τ²) + O(n²(1+m−ε)^n)."

紧接（逐字）：
> "Applying Dirichlet's theorem on simultaneous Diophantine approximations, we can make the sum ∑_{j=1}^{k} cos(nφ_j) arbitrarily close to k. Since k and l cannot both be equal to zero, this shows that **the value of λ_F(n,τ) can be infinitely many times negative and exponentially large in amplitude**, which contradicts (iii)."

p. 279（逐字）：
> "the leading term of the asymptotic behavior of the τ-Li coefficient λ_F(n,τ), as n → ∞, is −2(1+m)^n ∑_{j=1}^{k} cos(nφ_j) − l(1+m)^n for some m > 0. The sum of cosines can be made arbitrarily close to both k and −k (by Diophantine approximations) and hence this **oscillates with amplitude close to k(1+m)^n (which grows exponentially)**. We surmise that no other behavior is possible for the τ-Li coefficients of a Dirichlet series with real coefficients."

**(b) 对提问的正面回答**
- **λ_n 确实变负** ✓；出现在**无穷多个 n** 上——**不是** "λ_n < 0 for some n ≤ N" 这种显式阈值定理 ✗
- **幅度随 n 指数增长**（≈ k(1+m)^n, m>0）⟹ 一旦振荡开始就愈发不可逆 ✓
- 逻辑链：Theorem 3.3 (i)⟺(ii)（无 Re>τ/2 零点 ⟺ 全正）⟹ **只要存在一个离线零点，必存在 n 使 λ<0** ✓；而 (iii) 的存在性形式（λ > −c(δ)e^{δn}）恰是"指数振荡"的反命题 ⟹ 用 Dirichlet 逼近证伪它 ✓
- **阈值**：**无定理级阈值** ✗；全文唯带具体 n 的负面数据是**数值**（见 (c)）⚠️

**(c) 数值证据（逐字，个别句在块边界截断 ⚠️）**
- Davenport–Heilbronn："We have concentrated on the function L_DH(s, ξ⁻) and have numerically computed τ-Li coefficients for τ between 2 and 5 with step 0.5 and for n from 1 to 500 with step 5, with accuracy of 10⁻³⁵. … The negative values of …"（截断 ⚠️）
- L₇ 例："In the case τ = 2.2, negative values of the coefficients are obtained, so we may conclude that L₇(s, 2, −3.2469796) possesses a zero in the half-plane Re(s) > 1.1."；"negative values are obtained for values of **n close to 5000** as shown in Figure 8. (That is, **λ_{L₇}(4801, 3) < [0]** …)"（后半截断 ⚠️）
  ⟹ **唯一显式的"负面首现点"：n = 4801, τ = 3**（对 L₇；数值非定理）⚠️
- L₃₅："In [2], it is proved that L₃₅(s) has no zeros in the half-plane Re(s) > σ₃₅ ≈ 2.339463. This means that we should expect the τ-Li coefficients to exhibit oscillations of growing amplitude and eventually take negative values for τ < 2σ₃₅ and monotonically increase for τ > 2σ₃₅." ✓
- （对照）Dirichlet L-函数例：系数非负且无振荡 ⟹ 支持 GRH ✓（"evidence in support of the generalized Riemann hypothesis"）

### C.5 相邻文献（登记；**未读全文** ✗）
- N. Palojärvi, *Explicit zero-free regions and a τ-Li-type criterion*, **arXiv:1807.01506**（作者经 arXiv API 核实 ✓）。二手摘要（search snippet ⚠️）："The first main result gives explicit numbers N₁ and N₂ such that if all real parts of the τ-Li coefficients are non-negative for all indices between N₁ and N₂, then the function has non zeros outside a certain region." → **与本项目"显式范围"路线最接近的一篇**，建议 P9 精读。
- E. Bombieri, J. C. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, J. Number Theory 77 (1999) 274–287。摘要（Nokia-Bell-Labs 页，二手 ⚠️）：Li 判据对任意复零点多重集成立，"not specific to zeta functions"。**未发现** "RH 假 ⟹ λ_n < 0 且 n ≤ …" 形式的阈值定理 ✗（仅摘要级核验 ⚠️）。

---

## 未找到清单（明确）
| 目标 | 状态 | 已检索范围 |
|---|---|---|
| Oesterlé 2000 typescript 原文 | **未找到** ✗（未发表、uncirculated）| arXiv / HAL / CEA-IPhT / Google / Semantic Scholar / OpenAlex / Numdam |
| "λ_n < 0 for some n ≤ N" 形式的**显式阈值定理** | **未找到** ✗（Bucur et al. 只有渐近＋数值）| 目标 C 全文；Bombieri–Lagarias 摘要 |
| Bucur 等四人另作（题目含 violating RH/few zeros）| **不存在（未检出）** ✗ | arXiv API / S2 / OpenAlex |

---

## 对本项目的意义

1. **(T₀)² 型范围是**前人结果 **，必须引用、不得据为己有**：Oesterlé 2000（typescript, prop. 2，未发表）→ **BPY 2001 §2.3, p. 441 首次公开发表** → Voros *Exp. Math.* **29(4) (2020) 452–469**, eq. (13) → Voros arXiv:2204.01036 §2.2.2。本项目 `RETRACTION-A1-li-range-2026-09-11.md` 的判断**本轮由原刊/原文证实** ✓（此前仅为二手 ⚠️）。
2. **精确形式**：不是 (T−1)²、(T₀−1)²，而是 **n ≤ T₀²**（T₀ = "Re ρ = ½ 成立的最高高度"）；等价写法为 BPY 的 "|Im ρ| < √n 全在线上" ⟹ D-037 的 √n 形式即源于此。
3. **⚠️ 范围强弱（最要紧）**：取 T₀ = 3.000175×10¹²（Platt–Trudgian）⟹ Oesterlé/Voros 窗口 **n ≤ T₀² ≈ 9×10²⁴**；本项目 A1 窗口 **n ≤ 2T − O(1) ≈ 6.0×10¹²**。**已知结果比我们大约 12 个数量级** ⚠️⚠️。
4. ⟹ 就 ζ 而言，我们的线性窗口**严格弱于 25 年前的已知结果**；A1 短稿**不能**以"首次给出显式范围"立论。尚可立论者仅剩：**方法全初等**（Oesterlé/Voros 用鞍点-Darboux 渐近）＋**显式常数**（Trudgian 计数界、O(1) 端点）。**是否降级/改定位，请唐先生拍板**（我不做方向性决策）。
5. **文献空白所在**：目标 C 显示 **"λ_n < 0 的显式阈值定理"是空白**（Bucur 等只有渐近＋数值 n=4801，无定理级 n ≤ N）。若欲守住"窗口"叙事，把目标从"正性范围"转向"**负性首现的显式上界**"，是更可能站得住的路线（仅供参考，需唐先生决定）。
6. **建议引用清单**：Oesterlé 2000（typescript，未发表，转引）；**Biane–Pitman–Yor 2001 §2.3 p. 441（一手公开出处）**；Voros *Exp. Math.* 29(4) (2020) 452–469 eq. (13)；Voros arXiv:2204.01036 §2.2.2；Maślanka, Opuscula Math. 24 (2004) 103–114（二手，n² 措辞）；Lagarias ANIT 57 (2007)（"expect"，旁证）。

---

# 附：**独立核验**（助理亲自做 ✓，2026-09-12 19:50）

> 目的 ✓：本文件的结论**决定论文 A 的命运** ✗ ⟹ 按纪律**不轻信子代理** ✓，亲自复取原文 ✓

## 核验 1：BPY 2001 的那句话 ✓ **确证** ✓✓

```
【我找到的独立镜像 ✓】empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/biane-pitman-yor.pdf
（AM 官网 PDF 链接 404 ✗ —— 但 Watkins 镜像有全文 ✓）
【逐字原文 ✓】"We learned from J. Oesterlé (private communication) that λn ≥ 0 if every zero ρ
   of ξ with |ℑρ| < √n has ℜρ = 1/2. This is known to be true for n ≤ 2.975 . . . × 10^17."
【书目 ✓】BULLETIN (New Series) OF THE AMS, Volume 38, Number 4, Pages 435–465,
    S 0273-0979(01)00912-0, Article electronically published on June 12, 2001
    —— **页码与卷期与子代理所报一致** ✓
【数值自洽检验 ✓】(5.454×10⁸)² = 2.975×10¹⁷ ✓ —— 1986 van de Lune–te Riele–Winter 高度 ✓
⟹ **子代理的核心发现【成立】** ✓✓
```

## 核验 2：对论文 A 的**直接后果** ✗（这是必须正视的 ✓）

```
【论文 A 的主张 ✓】"λ_n ≥ 0 for every 2 ≤ n ≤ 2T − O(1)"（T = 已验证高度 ✓）
   其摘要的对照句 ✓："about 6×10⁷ times the range reached by **direct computation of λ_n**
   in the literature"（n ≤ 10⁵ ✓，Palojärvi/Coffey ✓）
【问题 ✗】**这个对照选错了** ✗ ——
   · "直接计算 λ_n" 的 n ≤ 10⁵ ✓ 只是**计算能力**的限制 ✗，**不是**已知的数学范围 ✓
   · **已知的数学范围是 Oesterlé 的 n ≤ T₀²** ✓（已发表 ✓ BPY 2001 §2.3 ✓ 经 Voros 2020 eq.(13) ✓）
【数量级对比 ✓（同取 T₀ = 3.000175×10¹² ✓）】
   · Oesterlé/BPY/Voros：n ≤ **T₀² ≈ 9.0×10²⁴** ✓
   · 论文 A：n ≤ 2T ≈ **6.0×10¹²** ✗
   ⟹ **论文 A 的范围小约 1.5×10¹² 倍** ✗✗（线性 vs 二次 ✓）
⟹ **论文 A 的"范围"卖点不成立** ✗；其摘要的对照句**必须改** ✗✗
```

## 核验 3：论文 A **还剩什么** ✓（诚实评估 ✓）

```
【仍成立 ✓】① 定理本身为真 ✓（"若零到 T 在线上 ⟹ λ_n ≥ 0 对 n ≤ 2T − O(1)" ✓）
            ② **完全初等** ✓（相位窗口 1−cos(nθ_γ) ✓ + Riemann–von Mangoldt ✓ + 离轴项 ✓）
            ③ **显式常数** ✓（C₁(n) = 1−cos(1/2−1/(96n²)) = 0.12241744 ✓；B_T ≤ 2.85×10⁻¹² ✓）
【已失去 ✗】④ "范围更大" ✗ —— **被 Oesterlé（2000/2001）完全覆盖且更弱** ✗✗
            ⑤ "首次显式范围" ✗ —— **BPY 2001 已给出 n ≤ 2.975×10¹⁷** ✗
【待定 ⚠️】⑥ 方法是否与 Oesterlé 的论证不同 ⟹ 需读 Oesterlé 的论证（Voros 说 "(reworded by us)" ✓，
               且其原文 **uncirculated** ✗ —— 可能**无法对比** ✗）
⟹ ⚠️ **必须由唐先生决定** ✓：**改写（降级为"初等/显式常数"说明 ✓）还是撤回** ✗
   —— 按纪律 ✓：**我不做方向性决策** ✗
```

## 核验 4：Bucur et al 的一条 ✓（科学上最相关 ✓）

```
【子代理所报 ✓】LMS J. Comput. Math. 19(1) (2016) 259–280 ✓｜RH 失效 ⟹ λ_n
   **无穷多次为负**、**振幅指数增长** ✓（经 Dirichlet 同时逼近 ✓）✓
   ＋ **无**"n ≤ N 阈值"型定理 ✗；具体负例仅数值：λ_{L₇}(4801, 3) < 0 ✓
【对我们的意义 ✓】**反向（探测）方向的文献缺口是真实的** ✓✓ ——
   即："若存在 |Im ρ| ≤ T 的离轴零点，则 λ_n < 0 对某个 **n ≤ N(T)**"
   —— **这种显式阈值的探测定理【尚无人给出】** ✓✓
   ⟹ 与我方 E4（Palojärvi Thm 4.1 推广 ✓，条件于 m 的先验界 ✓）**同向** ✓
   ⟹ ⭐ **这可能是 A1 方向真正还剩下的、未被先行者占据的空间** ✓
```
