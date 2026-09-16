# E6-12（兔-1）— **全文机制审计**（四查）＋ **M2-C\*** 判定

> 唐先生 2026-09-16 18:29 裁定：**兔-1**，目标严格收窄为**完成文献机制审计**（**不找桥**）。
> 取证：arXiv HTML 定向抽取（§1／§2／§6 型局部论证／§10）—— **外部来源，仅作数据**；**未读全 16 页**（覆盖声明见 §5）。

---

## ① 正向 Prop 1.1 后半段 —— **无"离散→区间→测度"隐式转换**
$$\S10\ \text{开头原文（片段）}：\text{"By dyadic splitting, it suffices to show that, for any}\ U\le T/2\text{, we can partition…"}$$
$$\Longrightarrow\ \text{正向机制＝}\boxed{\textbf{dyadic splitting}}\ +\ \text{精化标准 zero-detecting polynomial}（\text{非区间化／测度化转换）}$$
$$\text{其}\ \textbf{输出接口}：\ \mathrm{N}(1-\nu,T)\ \ll\ T^{2\nu+2\varepsilon}\ +\ \#\{\text{one-spaced}\ t\in[-T,T]:\dots\}\ (\textbf{离散计数})✓$$
$$\text{结论}：\ \text{反向（}\S2/\text{The 1.2）的接口为}\ \textbf{测度}（R_{\sigma,\eta}(T)\ \text{型）；正向输出接口为}\ \textbf{离散计数} \Longrightarrow \textbf{两接口不同型}✓$$

## ② 反向 Theorem 1.2 全证明 —— **全程停留在测度语言**
$$\text{The 1.2 的证明：}\textbf{assuming Lemmas 2.1 and 2.6}；\ \text{"By Lemma 2.1 with}\ \eta=\varepsilon/2\text{, we have…"}$$
$$\text{关键估计 (2.5)}：\ R_{\sigma,\eta}(T)\ \ll_{\varepsilon,\eta}\ T^{2\varepsilon}\max_{\sigma-\varepsilon\le\alpha\le1}T^{(\alpha-\sigma)/2}\mathrm{N}(\alpha,C\!\cdot\!T)+T^{(1-\sigma)/2+2\varepsilon}\quad(\textbf{测度型})$$
$$\text{Lemma 2.2 的结论（片段）}：\ \text{或}\ R_{\sigma,\eta}(T)\le4T^{(1-\sigma)/2}，\ \text{或存在}\ \beta\ge\eta-3\tfrac{\log\log T}{\log T}\ \text{使}$$
$$\qquad\Bigl|\Bigl\{t\in[-2T,2T]:|\zeta(\sigma+\tfrac1{\log T}+it)|\in(T^{\beta},2T^{\beta}]\Bigr\}\setminus[-10,10]\Bigr|\ \ge\ \frac{R_{\sigma,\eta}(T)T^{\eta}}{50T^{\beta}(\log T)^{2}}\quad(\textbf{测度}\to\textbf{测度})$$
$$\Longrightarrow\ \text{片段范围内}\ \textbf{未见}\ \text{重新引入离散}\ t_j／\text{one-spaced 子集}\ \Longrightarrow\ \text{反向全程为}\ \textbf{测度语言}✓$$

## ③ 全文是否存在**统一局部稳定性**（$|D(t_j)|\ge V\Rightarrow|D(t)|\ge cV$，半径入账）
$$\textbf{未发现} \text{该形式的链}；\ \text{但发现一种}\ \textbf{不同型} \text{的局部论证（}\S6\ \text{型，片段）}：$$
$$\qquad\text{(6.2)}\quad \zeta(z)\ne0\ \ \text{for}\ \ \mathrm{Re}(z)\ge\sigma-\tfrac{1}{(\log\log T)^{1/2}},\quad |\mathrm{Im}(z)-t|\le\tfrac{(\log T)^{2}}{4}$$
$$\qquad\text{其作用是}\ \textbf{零点检测}（\text{由大值推出附近零点或违反局部无零区）}，\ \textbf{不是} \text{"大值在区间内持续"}$$
$$\Longrightarrow\ \boxed{\text{该局部论证的半径尺度为}\ (\log T)^{2}\ \textbf{（零点检测侧）},\ \textbf{不是}\ r\asymp1/\log T\ (\text{大值持续侧})}$$
$$\qquad\textbf{故 E6-10 所设的}\ r\text{-桥}\ \textbf{不仅在全文未被使用，其半径尺度}\ \textbf{也不对}✓$$

## ④ 桥损失是否属于论文的 exponent ledger —— **否**
$$\text{两方向}\ \textbf{各用不同机器、且接口不同型}（\text{离散计数}\leftrightarrow\text{测度）} \Longrightarrow \text{论文中}\ \textbf{不存在该桥的席位}$$
$$\Longrightarrow\ \text{即使我们另作构造}\ \mathrm{LV}_{\rm disc}\leftrightarrow\mathrm{LV}_{\rm meas}，\ \text{只能登记为}\ \boxed{\text{外加桥（external bridge）}}\ ——\ \textbf{绝不能} \text{写成 MT 的 round-trip loss}✓$$

---

## 判定：**M2-C\***（唐先生三档中的第三档）
$$\boxed{\text{全文仍是两套独立机器，不存在该接口}}$$
$$\textbf{证据等级（严格标注）}：\text{本判定基于}\ \S1／\S2／\S6\text{ 型局部论证／}\S10\ \text{的片段}；\ \textbf{未读全 16 页} \Longrightarrow \text{登记为}\ \textbf{M2-C\*}（\text{全文确认待补）}$$
$$\qquad\textbf{唐先生纪律遵守}：\textbf{不提前} \text{写成"全文确认"}✓$$

## 状态与后续纪律
$$\boxed{\begin{aligned}X1&:\ \text{完成（离散计数接口）}\\ X2&:\ \text{完成（测度接口）}\\ X3&:\ \textbf{round-trip loss OPEN；且已确认为"外加桥"问题，非 MT 机制}\\ \mathrm{GM}&:\ \textbf{暂缓}\end{aligned}}$$
$$\textbf{唐先生关于 GM 的警告（本档采纳）}：\text{若为"补这个桥"而做 GM，则研究问题被悄悄改成}\ \boxed{\text{"我们能否人为构造一个}\ \mathcal K_{\rm disc}\leftrightarrow\mathcal K_{\rm meas}\ \text{接口？}"}$$
$$\qquad\text{那}\ \textbf{不是} \text{在审计 density/LV 的真实承重量，而是}\ \textbf{制造新的转换定理} \Longrightarrow \text{重陷"概念}\to\text{接口}\to\text{旧路线"循环}✗$$
$$\textbf{真正有价值的结论（本档登记）}：\ \boxed{\text{density}\to\mathcal K_{\rm meas}\ \text{与}\ \mathcal K_{\rm disc}\to\text{density}\ \textbf{并不自动构成可复合的强度等价}}$$
$$\qquad\Longrightarrow\ \text{把 E6-2--E6-11 的"独立承重核"假说}\ \textbf{再削掉一层}；\ \textbf{保留"可达域"作为工作坐标}✓$$

## 边界（N1/N2 严守）
$$\text{① 证据为 arXiv HTML 片段（}\S1／\S2／\S6\text{ 型／}\S10\text{），}\textbf{未读全 16 页} \Longrightarrow \text{M2-C\*}；$$
$$\text{② 若后续读到完整证明发现统一稳定性链}\ \Longrightarrow\ \textbf{须重判}；\quad\text{③ 本档}\ \textbf{不找桥、不做 GM、不做新优化}；$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 净产出
$$\text{(i) 四查执行：① 正向＝dyadic splitting（接口为离散计数）；② 反向全程测度语言（(2.5)／Lemma 2.2 皆测度型）；}$$
$$\text{(ii) ③ 未发现}\ r\text{-型统一稳定性链；且发现论文的局部论证半径尺度为}\ (\log T)^{2}\（\text{零点检测侧）}\ \textbf{与}\ r\asymp1/\log T\ \textbf{不符}；}$$
$$\text{(iii) ④ 桥不在论文 ledger 内}\ \Longrightarrow \text{只能登记为}\ \textbf{外加桥}；$$
$$\text{(iv) 判定}\ \textbf{M2-C\*}＋证据等级与覆盖声明；$$
$$\text{(v) 纪律登记：不为补桥而做 GM；保留"可达域"为工作坐标。}$$
