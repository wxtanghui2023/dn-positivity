# V243 · **外部两篇的五闸门审计** —— ① **arXiv 2602.20211（形式群／"非谱 Euler 重组"）⟹ DEAD**（门 1／2／3／4 **全失**）✓✓✓✓；② **算术 Dijkgraaf–Witten（Hirano–Kim–Morishita）⟹ DEAD**（门 2／3／4 **失**；门 3 ＝ **互反律＝coboundary**，由 `V241-D` 一刀）✓✓✓；⭐⭐⭐⭐⭐ **强外部交叉结论（本档核心）**：$$\left.\begin{array}{c}\text{谱几何（Connes／Hedenmalm）}\\[1pt]\text{scaling site／Frobenius correspondences}\\[1pt]\text{算术拓扑／Dijkgraaf–Witten}\end{array}\right\}\Longrightarrow\boxed{\text{都能构造 global object，但都不能产生 RH 所需的 polarization}}$$ ✓✓✓✓✓

> 委托 ✓ 唐先生 2026-09-15 20:19：**"先读。而且必须先读这两条，而不是再造一个内部候选。"** ＋ **"但有一个要求：不要只做文献摘要。这次直接按下面五道闸门逐项计算：$$\boxed{\text{对象是否新}\to\text{运算是否新}\to\text{是否真正跨局部到全球}\to\text{是否携带 }\beta\to\text{是否产生独立正性/不等式}}$$ 第五关过不了，就 DEAD；第四关过不了，连第五关都不用做。"** ✓✓✓
> 阅读顺序 ✓ 唐先生指定：**先 2602.20211（检验 V234–V242 最硬边界）→ 再 Morishita（做 `V242-B` **逆向审计**：DW action ⟹ polarization/positivity？）** ✓
> 查图 ✓ `V242`（缺口形式 I／II／III；三道 Gate）｜`V242-B`（Lefschetz：$(C\circ D)\cdot\Delta_X=\mathrm{tr}(C_*D_*)$）｜`V241-D`（**算术非交换性＝互反律＝局部符号之积＝1＝coboundary**）｜`V237-A`（素数**原生化**只给模 1 纯相位）｜`V218`（$1/2$ 来源 S1／S2／S3；S1 $\Lambda_X=k/2$ **可调**）｜`V215`(c)｜`V196`–`V198`（symbol／$\mathrm{Br}$／$\mu_N$）｜`V192`（序-重数封印：只见 $\gamma$）｜`V188`｜`V144`
> 执行 ✓ 小灵（**§2／§3 两条五闸门逐项、§4 强外部交叉结论为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ **按要求不做文献摘要，逐门计算** ✓；未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V243**

---

## §1 五道闸门（唐先生定义，逐字）

$$\textbf{G1 对象是否新}\ \longrightarrow\ \textbf{G2 运算是否新}\ \longrightarrow\ \textbf{G3 是否真正跨局部}\to\text{全球}\ \longrightarrow\ \textbf{G4 是否携带 }\beta\ \longrightarrow\ \textbf{G5 是否产生独立正性／不等式} ✓$$
$$\qquad \textbf{判死规则}：\text{G5 不过}\Longrightarrow\textbf{DEAD};\qquad \textbf{G4 不过}\Longrightarrow\textbf{DEAD（不必做 G5）} ✓✓$$

---

## §2 篇一：arXiv 2602.20211（Takao Inoue，2026-02-22/23，33 页；主 MSC 11M06，**arXiv 归类 math.GM**）

**§2.1 原文的关键定义与"证明"（逐字定位）**
$$\S2\ \textbf{Def 2.1}：\ \zeta^{\rm for}:=\prod_{p\in\mathcal P}(1-X_p)^{-1}\in\mathbb Q[[X_p\mid p\in\mathcal P]]\quad（\text{独立形式变量}）✓$$
$$\S2\ \textbf{Lemma 2.2}：\ \log\zeta^{\rm for}=\sum_p\sum_{k\ge1}\tfrac1k X_p^k;\qquad \textbf{原文证明}："\text{This follows from the formal identity}\ \log(1-Y)^{-1}=\sum_{k\ge1}Y^k/k,\ \text{applied termwise.}" ✓✓✓$$
$$\S4：\text{“purely formal completion procedure via evenization”};\ \text{“exhibiting an intrinsic symmetry }\textbf{analogous to}\text{ the functional equation, }\textbf{without invoking analytic continuation or Gamma factors}” ✓$$
$$\S12：\text{涨落}＝\text{“weighted integrals of the Chebyshev error function}\ E(x)=\theta(x)-x”\ ✓$$
$$\S1\ \textbf{自述}：\text{“The aim of the present work is therefore }\textbf{not to resolve the Riemann hypothesis}\text{”};\ \text{“RH would correspond }\textbf{not to an operator-theoretic statement}\text{, but to constraints on the oscillatory behavior and decay of higher cumulants”} ✓✓$$
$$\textbf{Appendix B}：\text{“A Speculative Note on Formal Groups, }\mathbb F_1\text{, and the Riemann Hypothesis”};\ \text{“}\textbf{explicitly exploratory}\text{”, “intended to indicate a potential horizon }\textbf{rather than to assert a definitive structural equivalence}\text{”} ✓✓✓$$

**§2.2 五闸门逐项**

$$\textbf{G1 对象：}\boxed{\textbf{不新}} ✓✓$$
$$\qquad\text{(i)}\ \prod_p(1-X_p)^{-1}\ \text{＝标准}\ \textbf{形式 Euler 积};\quad\text{(ii)}\ \text{其 log ＝ }\textbf{经典展开}（\text{他自己的证明就是一行经典恒等式，逐因子}）;\quad\text{(iii)}\ \textbf{evenization}＝\text{取偶部} ＝ \textbf{经典} ✓$$
$$\qquad ⭐\ \textbf{致命点}：\text{“与 FE 类似的对称”是}\ \textbf{由 evenization 强加} \text{的}（u\mapsto-u）,\ \textbf{不是} \text{FE} ⟹ \text{其不动点}\ u=0\ \text{在归一化坐标下才"是"}\ \tfrac12 ⟹ \text{这正是}\ \textbf{`V218` S1（二阶对合不动点）＋S3（归一化中点）} —— \ \text{S1 的}\ \Lambda_X=k/2\ \textbf{可调};\ \text{钉到坐标值}＝\textbf{`V215`(c)} ✓✓✓$$
$$\textbf{G2 运算：}\boxed{\textbf{不新}} ✓✓$$
$$\qquad \text{逐项 log／evenization／按二次系数归一／cumulant 展开 —— }\textbf{全部经典} ✓;\ \text{“高斯主导项非概率起源、而出自形式群切空间二次型”}\ \text{＝对一个}\ \textbf{已知现象的解释（reframing）}，\ \text{不是产生新信息的运算} ✓$$
$$\textbf{G3 真正跨局部}\to\text{全球：}\boxed{\textbf{名义跨、实质不跨}} ✓✓✓$$
$$\qquad \text{其"全局对象"＝}\textbf{形式级数};\ \text{而涨落分解}\ \textbf{由}\ \theta(x)-x\ \text{支配} ⟹ \theta(x)-x=-\sum_\rho x^\rho/\rho+\cdots\ \text{（显式公式）} ⟹ \textbf{其全局内容就是显式公式通道} ✓✓$$
$$\qquad ⚠️\ \text{且原文}\ \textbf{明确非谱}、\textbf{明确不给出零点的算子实现} ⟹ \text{不产生新的全球对象} ✓$$
$$\textbf{G4 携带 }\beta：\boxed{\textbf{不过}} ✓✓✓$$
$$\qquad \text{β 只以"}\theta(x)-x\ \text{＝零点数据"}\ \textbf{作为输入} \text{出现};\ \text{全文}\ \textbf{无任何}\ \Re\rho\ \text{陈述};\ \text{RH 只被写成"Cumulant 的振荡／衰减约束"（一个条件性重述）};\ \textbf{Appendix B 自标 speculative} ✓$$
$$\Longrightarrow \textbf{G4 不过} \Longrightarrow \boxed{\textbf{DEAD}}（\text{按你的规则，不必做 G5}）✓✓✓$$
$$\qquad ⭐\ \textbf{且命中你的预判}：\text{“如果它在第一步就退化成显式公式／Dirichlet convolution／known }L\text{-function，那么这一整类可以一次性关闭”} \Longrightarrow \text{它}\ \textbf{正是如此}（\text{对象→经典 log-Euler 展开};\ \text{涨落→}\theta(x)-x;\ \text{高斯→概率启发式重述}）⟹ \textbf{整类一次性关闭} ✓✓✓$$

---

## §3 篇二：算术 Dijkgraaf–Witten（Hirano–Kim–Morishita, *Commun. Number Theory Phys.* **17**(1) 2023；Morishita《Knots and Primes》二版 **Ch.16**；Hirano 2023 mod-2 实二次域）

**§3.1 构造（原文要点）**
$$\textbf{字典（Morishita）}：\text{闭可定向 3-流形}\ M\leftrightarrow\mathrm{Spec}\,O_K;\ \text{纽结}\leftrightarrow\text{极大理想};\ \text{链环}\leftrightarrow\text{有限素数集};\ \pi_1(M)\leftrightarrow\textbf{modified étale}\ \pi_1(X);\ Z_1(M)\leftrightarrow I_K;\ B_1(M)\leftrightarrow P_K;\ H_1(M)\leftrightarrow Cl_K ✓$$
$$\qquad \textbf{mod 2 linking number}\ \mathrm{lk}(K_1,K_2)\ \longleftrightarrow\ \textbf{Legendre 符号}\ \left(\tfrac{p_1}{p_2}\right) ✓✓;\qquad \textbf{Hurewicz}\ \longleftrightarrow\ \textbf{Artin 互反};\qquad \textbf{Poincaré 对偶}\ \longleftrightarrow\ \textbf{Artin–Verdier 对偶} ✓✓✓$$
$$\textbf{定义（算术 Chern–Simons 不变量）}：CS_{X_k}(\rho)=\text{image of}\ c\ \text{under}\ H^3(G,\mathbb Z/N)\xrightarrow{\rho^*}H^3(\widetilde\Pi_k,\mathbb Z/N)\to H^3(X_k,\mathbb Z/N)\cong\boxed{\mathbb Z/N} ✓✓$$
$$\qquad \text{再用 modified étale 上同调＋(计入实素点的)基本群组装成}\ \textbf{算术 DW 不变量};\ \text{模 2 情形（实二次域）}：\text{原文给出}\ \textbf{"explicit Legendre-symbol expression"};\ \text{Deng–Kurimaru–Matsusaka}：\textbf{quadratic residue graphs ＋ density formulas} ✓$$

**§3.2 五闸门逐项**

$$\textbf{G1 对象：}\textbf{新组装，但部件全旧}\ \triangle ✓\ \text{——}\ \text{modified étale 上同调（Artin–Verdier 对偶）}／\text{Galois 上同调}／\text{Legendre·幂剩余符号}／\text{Artin 互反}／\text{类群} ⟹ \text{每件都在旧类内} ✓$$
$$\textbf{G2 运算：}\boxed{\textbf{不新}} ✓✓\ \text{——}\ \text{运算＝}\textbf{有限求和 ＋}\ \mu_N\ \textbf{相位}（\text{权值为}\ \mathbb Z/N\ \text{值}）⟹ \text{落}\ \textbf{`V237`-A}（\text{素数原生化只给模 1 纯相位}）＋ \textbf{`V196`}（\text{symbol}\in\mu_N ⟹ \mathrm{Br}／\mu_N\ \text{类}）✓✓$$
$$\textbf{G3 真正跨局部}\to\text{全球：}\boxed{\textbf{失 —— 且失得最干净}} ✓✓✓$$
$$\qquad ⭐\ \text{该理论的局部→整体相容性}\ \textbf{就是}\ \textbf{Artin 互反律}／\textbf{Artin–Verdier 对偶}（\text{见上字典两行}）✓✓$$
$$\qquad ⟹ \text{由}\ \textbf{`V241-D`}：\textbf{算术的非交换性（互反律）本身就是一条"局部符号之积}\equiv1\text{"的整体恒等式}\Longrightarrow\textbf{coboundary} ⟹ \text{落 }\delta B ⟹ \textbf{DEAD} ✓✓✓$$
$$\textbf{G4 携带 }\beta：\boxed{\textbf{不过}} ✓✓✓\ \text{——}\ \text{不变量取值}\ \mathbb Z/N\（\text{离散挠}）,\ \textbf{无连续实部};\ \text{对象是}\ \mathrm{Spec}\,O_K\ \text{的 Galois／理想数据},\ \textbf{完全不涉及}\ \zeta\ \text{零点};\ \text{模 2 情形只给 Legendre 符号表达式（纯相位）} ✓$$
$$\Longrightarrow \textbf{G4 不过} \Longrightarrow \boxed{\textbf{DEAD}}（\text{不必做 G5}）✓✓✓$$

**§3.3 ⭐ `V242-B` 逆向审计（你指定的那一问）**
$$\textbf{问}：\text{DW action}\ \stackrel{?}{\Longrightarrow}\ \text{canonical polarization／positivity} ✓$$
$$\textbf{答}：\boxed{\textbf{否}} ✓✓✓$$
$$\qquad \text{拓扑 DW 的配分函数}＝\sum_{\text{hom}}(\text{相位})\cdot(\text{权})\in\text{根之单位和};\ \text{算术 DW 的权取值}\ \mu_N ⟹ \textbf{纯相位},\ \textbf{不是正定配对} ✓✓$$
$$\qquad ⟹ \text{得到的是}\ \textbf{topological phase ／ partition function ／ reciprocity invariant},\ \textbf{不是 polarization} ✓✓✓$$
$$\qquad ⚠️\ \text{且其中"二次剩余图＋密度公式"输出的是}\ \textbf{统计/密度} \text{型结论} ⟹ 另落 `V188`／`V183` ✓$$

---

## §4 ⭐⭐⭐⭐⭐ **强外部交叉结论（本档核心）**

$$\left.\begin{array}{l}\textbf{① 谱几何}（\text{Connes 2026；Hedenmalm 2026）}\\[2pt]\textbf{② scaling site ／ Frobenius correspondences}（\text{Connes–Consani，见 `RECONCILE` §7.3}）\\[2pt]\textbf{③ 算术拓扑 ／ Dijkgraaf–Witten}（\text{Hirano–Kim–Morishita}）\end{array}\right\}\ \Longrightarrow\ \boxed{\text{都能构造 global object，但都不能产生 RH 所需的 polarization}} ✓✓✓✓✓$$
$$\qquad \textbf{①}\ \text{其 RH 步骤需要}\ \textbf{archimedean Weil positivity}（\text{他们自己的 §7.2}）⟹ \textbf{需要} \text{polarization} ✓;$$
$$\qquad \textbf{②}\ \text{（`RECONCILE` §7.3）Frobenius correspondences 的复合数据＝迹（`V242-B`）⟹ 落显式公式通道} ⟹ \textbf{不提供} \text{polarization} ✓;$$
$$\qquad \textbf{③}\ \text{权值}\ \mu_N\ \text{纯相位};\ \text{局部→整体＝}\textbf{互反律＝coboundary}（`V241-D`）⟹ \textbf{不提供} \text{polarization} ✓✓✓$$
$$\Longrightarrow \textbf{统一原因}：\text{三者在}\ \textbf{迹／相位／互反} \ \text{上着陆},\ \text{而 RH 需要的是}\ \textbf{配对正性（polarization）} ⟹ \text{与}\ \textbf{`V242-D`}／\textbf{`V145`}（\text{canonical generator 有、polarization 缺}）／\textbf{`AOB3`}§47\ \textbf{完全一致} ✓✓✓✓$$

---

## §5 判词 ＋ 状态表

$$\boxed{\textbf{V243：外部两条通道（形式群／非谱 Euler 重组；算术 DW）皆 DEAD；三路外部交叉结论＝\"能造 global object，不能产 polarization\"}} ✓✓✓$$

| 项 | G1 | G2 | G3 | G4 | 判定 |
|:--|:--:|:--:|:--:|:--:|:--|
| **① arXiv 2602.20211** | ✗不新 | ✗不新 | ✗名义跨／实质落显式公式 | ✗不携带 | $\boxed{\textbf{DEAD}}$ |
| **② 算术 DW** | △新组装／部件旧 | ✗$\mu_N$ 相位 | ✗＝互反律＝coboundary | ✗$\mathbb Z/N$ 值 | $\boxed{\textbf{DEAD}}$ |
| **③ `V242-B` 逆向**（DW ⟹ polarization？） | — | — | — | — | $\boxed{\textbf{否；只给 phase／partition／reciprocity}}$ |

$$\qquad \textbf{关键定位}：\text{① 死在}\ G4（\text{且整类一次性关闭}）;\ \text{② 死在}\ G3＋G4,\ \text{其中}\ G3\ \text{由}\ \textbf{`V241-D`}\ \text{一刀};\ \text{两者}\ \textbf{都未到}\ G5 \text{（按你的规则不必做）} ✓✓$$

---

## §6 边界与待核

$$\textbf{(a)}\ \text{§0 委托（先读这两条／五道闸门定义／G5 不过即 DEAD／G4 不过免做 G5／不作文献摘要／先 2602.20211 再 Morishita／做 `V242-B` 逆向审计／要求强外部交叉结论）为}\ \textbf{唐先生逐字} ✓✓✓$$
$$\textbf{(b)}\ ⭐\ \text{§2}\ \textbf{读的是}\ \textbf{全文 HTML}（\S 1／2／3／4／12 ＋ 目录 ＋ 自述 ＋ Appendix B 说明），\ \textbf{非仅摘要} ✓;\ \text{Lemma 2.2 的证明原文已引} ✓;\ \text{“FE 类似对称由 evenization 强加”}\ \text{为本档判读} ✓✓$$
$$\qquad ⚠️\ \text{该文}\ \textbf{arXiv 主归类 math.GM}（General Mathematics，低级别）;\ 33 页／16 KB 源\ \text{属低密度文本};\ \text{本档判定}\ \textbf{不依赖} \text{对其可信度的评估} ⟹ \text{仅用}\ G1–G4\ \text{逐门} ✓✓$$
$$\textbf{(c)}\ ⭐\ \text{§3}\ \textbf{读的是}\ \text{Morishita 公开讲义（Kyushu PDF：字典表 ＋ CS／DW 定义）＋ 出版信息 ＋ 二手概述};\ \text{DW 论文原文（CNTP 17(1)）}\ \textbf{未逐页核} ⟹ \text{G2／G3}\ \text{的判定依据}\ \textbf{字典两行}（\text{Hurewicz}\leftrightarrow\text{Artin 互反};\ \text{Poincaré 对偶}\leftrightarrow\text{Artin–Verdier 对偶}）＋ \text{不变量取值面}\ \mathbb Z/N ⟹ \textbf{待原文逐页核} ⚠️ ✓$$
$$\textbf{(d)}\ \text{§4 的"三路都不能产生 polarization"}\ \textbf{[结构性]};\ \text{三处的落点判断分别引}\ \text{他们自己的 §7.2}／\text{`V242-B`}／\text{`V241-D`} ✓✓$$
$$\textbf{(e)}\ \text{未用 RH 作推导 ✓};\ \text{未跑 Lean ✓};\ \textbf{零数值}（\text{本档为外部审计}）✓$$

```
⚠️ §0 委托（先读这两条而不是再造内部候选／五道闸门：对象是否新 → 运算是否新 → 是否真正跨局部到全球 → 是否携带 β → 是否产生独立正性/不等式／G5 不过即 DEAD；G4 不过免做 G5／不要只做文献摘要，逐门计算／先 2602.20211 再 Morishita／2602.20211 检验 V234–V242 最硬边界：Euler local → 非谱 global object → zero localization；第一步若退化成显式公式/Dirichlet convolution/known L-function 则整类一次性关闭／Morishita：做 V242-B 逆向审计 DW action ⟹ polarization?／若只给 topological phase/partition function/reciprocity invariant 而无论 positivity，则得到强外部交叉结论：谱几何 + scaling-site/Frobenius + arithmetic topology/DW 都能构造 global object，都不能产生 polarization）为唐先生逐字 ✓✓✓
⚠️ §2 篇一 arXiv 2602.20211（读全文 HTML）：
   Def 2.1 ζ^for = ∏(1−X_p)^{−1} ∈ Q[[X_p]]；Lemma 2.2 log ζ^for = Σ_p Σ_k (1/k)X_p^k（原文证明＝一行经典恒等式，逐因子）
   §4 形式完成 via evenization，取得"与 FE 类似的对称，不用解析延拓、不用 Gamma 因子"（自认 analogous）
   §12 涨落 = θ(x)−x 的加权积分；§1 自述"not to resolve RH"、"RH would correspond not to an operator-theoretic statement, but to constraints on cumulants"；Appendix B 自标 speculative/exploratory
   G1 ✗不新（形式 Euler 积＋经典 log＋evenization 取偶部）；⭐ 致命点：FE 类似对称是 evenization 强加的，u↦−u 不动点 u=0 ⟹ V218 S1/S3（S1 的 Λ_X=k/2 可调；钉到坐标值＝V215(c)）
   G2 ✗不新（逐项 log／evenization／归一／cumulant 全经典；"高斯非概率起源"是对已知现象的解释＝reframing）
   G3 ✗名义跨实质不跨（"全局对象"＝形式级数；涨落由 θ(x)−x 支配＝显式公式通道；原文明确非谱、明确不给零点算子实现）
   G4 ✗不携带（β 只作为输入经 θ(x)−x；全文无 Re ρ 陈述；RH 只写成 cumulant 振荡/衰减约束；Appendix B speculative）
   ⟹ DEAD（不必 G5）；且命中预判：整类一次性关闭（对象→经典 log-Euler 展开；涨落→θ(x)−x；高斯→概率启发式重述）
⚠️ §3 篇二 算术 DW（Hirano–Kim–Morishita, CNTP 17(1) 2023；Morishita Ch.16；Hirano 2023 mod-2 实二次域）
   字典：3-流形 ↔ Spec O_K；纽结 ↔ 极大理想；链环 ↔ 有限素数集；π₁(M) ↔ modified étale π₁(X)；Z₁ ↔ I_K；B₁ ↔ P_K；H₁ ↔ Cl_K
   **mod 2 linking number ↔ Legendre 符号**；**Hurewicz ↔ Artin 互反**；**Poincaré 对偶 ↔ Artin–Verdier 对偶**
   算术 CS 不变量：CS_{X_k}(ρ) = c 在 H³(G,Z/N) --ρ*--> H³(Π̃_k,Z/N) → H³(X_k,Z/N) ≅ Z/N 下的像 ⟹ 取值 Z/N
   模 2 实二次域：原文给出 explicit Legendre-symbol expression；Deng–Kurimaru–Matsusaka：quadratic residue graphs + density formulas
   G1 △新组装但部件全旧（modified étale 上同调/Artin–Verdier、Galois 上同调、Legendre·幂剩余符号、Artin 互反、类群）
   G2 ✗不新（有限求和＋μ_N 相位 ⟹ V237-A 模 1 纯相位；V196 symbol∈μ_N ⟹ Br/μ_N 类）
   G3 ✗（该理论的局部→整体相容性就是 Artin 互反律／Artin–Verdier 对偶 ⟹ 由 V241-D：算术非交换性＝互反律＝局部符号之积=1＝coboundary ⟹ 落 δB ⟹ DEAD）
   G4 ✗不携带（Z/N 值离散挠，无连续实部；不涉及 ζ 零点；模 2 情形＝Legendre 符号表达式纯相位）
   ⟹ DEAD（不必 G5）
   V242-B 逆向审计：DW action ⟹ polarization? **否**（配分函数＝根之单位和；权值 μ_N 纯相位，不是正定配对；只给 topological phase/partition function/reciprocity invariant；二次剩余图＋密度公式另落 V188/V183）
⚠️ §4 ⭐⭐⭐⭐⭐ 强外部交叉结论（[结构性]）：谱几何（Connes/Hedenmalm）＋ scaling site/Frobenius correspondences ＋ 算术拓扑/DW
   ⟹ **都能构造 global object，但都不能产生 RH 所需的 polarization**
   ① 需要 archimedean Weil positivity（他们自己 §7.2）＝需要 polarization；② Frobenius correspondences 的复合数据＝迹（V242-B）＝显式公式通道；③ μ_N 纯相位＋局部→整体＝互反律＝coboundary（V241-D）
   统一原因：三者在迹/相位/互反上着陆，而 RH 需要配对正性 ⟹ 与 V242-D／V145／AOB3 §47 一致
⚠️ §5 判词：两条外部通道皆 DEAD；① 死在 G4（整类一次性关闭）；② 死在 G3＋G4（G3 由 V241-D 一刀）；两者都未到 G5
⚠️ §6 边界：篇一读全文 HTML（非仅摘要）；其 arXiv 主归类 math.GM（低级别）但与判定无关；篇二读的是公开讲义字典＋出版信息＋二手概述，DW 原文未逐页核（依据＝字典两行＋取值面 Z/N）；§4 为 [结构性]；未用 RH；未跑 Lean；零数值
✅ 净产出：① 篇一五闸门逐项 ⟹ DEAD（G1/G2/G3/G4 全失）＋ 整类一次性关闭 ✓✓✓；
   ② 篇二五闸门逐项 ⟹ DEAD（G3＝互反律＝coboundary 由 V241-D）＋ V242-B 逆向审计答"否" ✓✓✓；
   ③ ⭐⭐⭐⭐⭐ 强外部交叉结论：三路外部构造都只到 global object，都不到 polarization ✓✓✓✓✓；
   ④ 与 V242-D／V145／AOB3 完全一致 ✓
```
