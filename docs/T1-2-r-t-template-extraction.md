# T1-2 · **$(r,t)$ 模板抽取**（BCR (1.3) 的双参数结构）

> 依 `docs/TACTICAL-PLAN.md`｜**执行日**：2026-09-17｜材料：`external_refs/bettin_chandee_radziwill_1411.7764.txt`（本地 grep）✓
> **纪律**：只抽取结构，不做数学判断 ✓

---

## 1. ⭐⭐⭐ (1.3) 的**完整陈述**（逐字）

$$S_{A,M,N}：＝\sum_a\sum\sum_{(m,n)=1}\nu_a\alpha_m\beta_n\,e\Bigl(\frac{a\overline m}{n}\Bigr)✓$$
$$\ll_\varepsilon\underbrace{\|\alpha\|\|\beta\|\|\nu\|(M+N)^{\frac12+r+\varepsilon}A^t}_{\textbf{项 1（}L^2\text{ 型，}(r,t)\text{ 在此）}}+\underbrace{\|\nu\|A^{\frac12}\Bigl(\|\alpha\|_\infty\|\beta\|N^{\frac12+\varepsilon}+\|\alpha\|\|\beta\|_\infty M^{\frac12+\varepsilon}\Bigr)}_{\text{项 2（}L^\infty\text{ 型）}}\tag{1.3}✓✓$$
$$\text{条件}：M\le m<2M,\quad N\le n<2N,\quad A\le a<2A,\quad \boxed{A\ll(NM)^{\frac{0.5-r}{1+2t}+\varepsilon}}✓✓✓$$

$$\Longrightarrow\ \boxed{(r,t)\ \textbf{同时控制两件事}：\text{(i) 项 1 的节省率；\ (ii) }A\ \text{的可达范围}}✓✓$$

---

## 2. ⭐⭐ Theorem 2（$\theta$ 与 $(r,t)$ 的精确关系）

$$\text{若 (1.3) 对某}\ r,t\ge0\ \text{成立}，\ \text{则}\ I=\text{(主项)}+O\Bigl(T^{\frac12-t+\varepsilon}N^{\frac12+r+2t}+T^{\frac13+\varepsilon}\Bigr)✓$$
$$\text{对}\quad\boxed{\theta<\frac12+\frac{0.5-r}{1+2(r+2t)}},\qquad N：＝T^\theta✓✓$$

$$\textbf{历史归属（逐字）}：\text{DFI}\ \Longrightarrow\ (r,t)=(\tfrac{23}{48},\tfrac12)\ (\delta=\tfrac1{190}\approx0.00526)✓\qquad \text{BC}\ \Longrightarrow\ (r,t)=(\tfrac9{20},\tfrac7{20})\ (\theta<\tfrac{17}{33})✓✓$$
$$\text{"We conjecture that (1.3) holds true for all}\ r,t\ge0\text{"}✓$$

---

## 3. ⭐⭐⭐ **Conjecture 1（端点）＋ Proposition 4（匹配下界）** —— 决定性

$$(1.4)：\ \text{取}\ A\ll(NM)^{\frac12+\varepsilon}\ \text{时}\ S_{A,M,N}\ll\|\alpha\|\|\beta\|\|\nu\|(M+N)^{\frac12+\varepsilon}+\|\nu\|A^{\frac12}\bigl(\|\alpha\|_\infty\|\beta\|N^{\frac12+\varepsilon}+\|\alpha\|\|\beta\|_\infty M^{\frac12+\varepsilon}\bigr)✓✓$$
$$\textbf{BCR 自述}：\text{"essentially states that we expect}\ \textbf{square-root cancellation in the shortest two sums},$$
$$\qquad\text{as long as the total saving does not exceed}\ M\ \text{or}\ N.\ \textbf{In the Appendix we show that this is best possible, up to}\ \varepsilon\text{-powers}\text{"}✓✓✓$$

$$\textbf{Appendix A · Proposition 4（逐字）}：\text{Let}\ A,M,N\ge1\ \text{and}\ A\ll(MN)^{\frac12+\varepsilon}.\ \text{Then}$$
$$\boxed{\max_{\alpha,\beta,\nu}|S_{A,M,N}|\ \gg\ (AMN)^{\frac12-\varepsilon}(M+N)^{\frac12}+A(M+N)^{1-\varepsilon}}✓✓✓$$
$$\qquad\text{（}\max\ \text{取遍}\ \alpha_m,\beta_n,\nu_a\ll1\text{）}✓$$

$$\Longrightarrow\ \boxed{\textbf{目标形态已被 BCR 自己证明为最优（匹配下界）}} \Longrightarrow \text{全部难度在于}\ \boxed{\text{从}\ (\tfrac9{20},\tfrac7{20})\ \textbf{走到}\ (0,0)}✓✓✓$$

---

## 4. ⭐⭐ Proposition 4 的**证明方法**（可复用技术）

$$\text{关键工具 1}：\textbf{互反关系}\ \frac mn\equiv-\frac nm+\frac1{mn}\ (\mathrm{mod}\ 1)\ \Longrightarrow \text{可设}\ M\ge N✓✓$$
$$\text{关键工具 2}：\text{取极值系数}\ \alpha_m=f(m)\ \text{（光滑，}\int f=KM\text{）}；\ \beta_n=-\gamma_n\ \text{（素数}\equiv1\bmod4\ \text{的指示函数）}；\ \nu_a\ \text{（素数}\equiv3\bmod4\text{）}✓✓$$
$$\text{关键工具 3}：\textbf{Poisson 求和} \Longrightarrow \sum_m f(m)e\bigl(\frac{am}{n}\bigr)=\frac{KM}{N}\bigl(c_n(a)+O(M^{-100})\bigr)✓✓$$
$$\qquad\qquad\textbf{Ramanujan 和}：c_n(a)=\sum_{\substack{b=1\\(b,n)=1}}^n e\bigl(\tfrac{ba}{n}\bigr)=\mu\Bigl(\frac n{(n,a)}\Bigr)\frac{\phi(n)}{\phi(n/(n,a))}✓✓$$
$$\Longrightarrow\ \text{极值} \gg (MA)^{1-\varepsilon}；\ \text{且}\ \max\gg M(AN)^{\frac12-\varepsilon}✓✓$$

$$\textbf{资产价值}：\ \text{这是}\ \textbf{"饱和 witness"方法的一个成熟实例}（\text{与我们 E-7 纪律同构}）⟹ \text{可复用}✓✓$$

---

## 5. ⭐ 附带发现（直接影响 T3）

$$\textbf{Corollary 2（逐字）}：\ \int_T^{2T}\bigl|\zeta(\tfrac12+it)\bigr|^3dt\ \ll\ T(\log T)^{9/4}✓✓$$
$$\qquad\text{（"the correct order of magnitude for the third moment"；"Previously Corollary 2 was known}\ \textbf{only on the assumption of the Riemann Hypothesis}\text{"}）✓✓$$
$$\qquad\Longrightarrow\ \textbf{三阶矩的正确上界已无条件成立} \Longrightarrow \textbf{T3 的目标须重新定位}✓✓$$
$$\text{且逐字}：\ \text{"We further indicate in Section 6.1 how to refine this result to obtain correct upper bounds for the}\ 2k\text{-th moment, when}\ k\ \text{has the form}\ k=1+1/n\text{"}✓$$

---

## 6. ⭐⭐ 对 T1 的**直接含义**

$$\text{(i)}\ \text{目标形态}\ \textbf{不需要改进}（\text{Proposition 4 已证最优）}✓✓$$
$$\text{(ii)}\ \text{因此 T1 的}\ \textbf{唯一问题}：\ \text{如何把}\ (r,t)\ \text{从}\ (\tfrac9{20},\tfrac7{20})\ \text{推到}\ (0,0)✓✓$$
$$\text{(iii)}\ \text{而}\ (r,t)\ \text{住在}\ \textbf{项 1}（L^2\ \text{型}）⟹ \text{须改进的是}\ \|\alpha\|\|\beta\|\|\nu\|\ \text{型的}\ L^2\ \text{估计}✓$$
$$\text{(iv)}\ \text{同时}\ A\ll(NM)^{\frac{0.5-r}{1+2t}}\ \text{须一起改善（}\textbf{昨日 Q1 已证 uniformization 必然}）✓$$

$$\textbf{T1-3 的精确化}：\ \boxed{\text{(1.3) 项 1 的}\ L^2\ \text{估计中，哪一处谱输入（Kuznetsov／DI／Weil 单点）在束缚}\ (r,t)？}}✓✓$$

## 7. 残余与下一步

$$\text{残余 1：}\ \text{BC 的两项界 (1.2) 如何}\ \textbf{逐项} \text{转成}\ (\tfrac9{20},\tfrac7{20})\ \text{未逐行核}✓\quad(\text{昨日给出框架：项 1 主导})✓$$
$$\text{残余 2：BC §6.1（}2k\ \text{矩，}k=1+1/n\text{）未读}✓$$
$$\textbf{下一步 T1-3}：\ \text{读 BC §2 outline ＋ §4（已有逐字）}⟹ \text{定位项 1 的谱输入}✓$$
