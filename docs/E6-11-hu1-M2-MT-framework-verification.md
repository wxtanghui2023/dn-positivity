# E6-11（虎-1）— **M2 MT-framework verification** ＋ 记号更正

> 唐先生 2026-09-16 18:27 裁定：**虎-1**；不作 GM／REVIEW／新优化。
> 唯一问题：$$\boxed{K_{\rm disc}\ \overset{?}{\longrightarrow}\ K_{\rm meas}\ \text{是否在 MT 的实际证明中以}\ T^{-o(1)}\ \text{的代价实现？}}$$
> **取证**：arXiv HTML（`arxiv.org/html/2403.13157v1`）定向抽取 §1／§2／§10 片段 —— **外部来源，仅作数据**；**片段不完全**（未读全 16 页）。

---

## 0. 记号更正（唐先生指出，立即生效）
$$\textbf{原（E6-10 §M2／M3）写成}\ \ell_{\rm bridge}\le\log T=O(\varepsilon)\ ——\ \textbf{不严谨}：$$
$$\qquad\log T\ \textbf{不是}\ T^{\varepsilon}\ \text{的指数}\ O(\varepsilon)；\ \text{两者是}\ \textbf{不同记号层级}（\varepsilon\ \text{为固定小参数；}o(1)\ \text{为}\ T\to\infty\ \text{的渐近量）$$
$$\textbf{正确写法}：\ \log T=T^{o(1)} \Longrightarrow \text{若}\ r\asymp(\log T)^{-1}，\text{则}\ r^{-1}\asymp\log T=T^{o(1)} \Longrightarrow \boxed{\ell_{\rm bridge}=0\ \text{（幂指数层级）}}\ \text{或}\ \boxed{\ell_{\rm bridge}=o(1)}$$
$$\qquad\textbf{不得} \text{写成}\ O(\varepsilon)✓$$

---

## M2-1：MT 的大值集合定义（**取得**）
$$\text{The 1.2 的集合}：\ \Bigl|\Bigl\{t\in[-T,T]:\ \Bigl|\sum_{M<m\le M'}\frac{1}{m^{1+it}}\Bigr|\ge M^{-\nu}\ \text{对某}\ M\in[T^{\varepsilon},T^{1/2}/2],\ M'\in(M,2M]\Bigr\}\Bigr|$$
$$\text{区间}：[-T,T]；\ D\ \text{为}\ \textbf{二进区间上的}\ \sum 1/m^{1+it}\ (\textbf{未提示平滑／加权})；\ \text{量词：}\ \exists M\ (\text{存在型})$$
$$\text{证明中用到的功能量}：\ R_{\sigma,\eta}(T)：＝\Bigl|\Bigl\{t\in[-T,T]:\max_{\substack{1\le A\le B\le T^{1/2}\\ B\le2A}}\Bigl|\sum_{A<n\le B}\frac{1}{n^{\sigma+it}}\Bigr|\ge T^{\eta}\Bigr\}\Bigr|\quad(\textbf{测度型})✓$$

## M2-2：从离散点到区间的局部稳定性 —— **未在 MT 框架中发现**
$$\text{MT 的}\ \textbf{实际机制（片段证据）}：$$
$$\qquad\textbf{(a) Prop 1.1（正向：零点}\to\text{one-spaced 大值点）}：\text{"refining a standard zero-detecting polynomial"}\ +\ \boxed{\textbf{dyadic splitting}}$$
$$\qquad\qquad\text{原文片段：}\text{"By dyadic splitting, it suffices to show that, for any}\ U\le T/2\text{, we can partition…"}$$
$$\qquad\textbf{(b) The 1.2（反向：density}\to\text{测度）}：\text{经}\ \textbf{Lemma 2.1}（部分求和）＋\textbf{Lemma 2.2／(2.5)}$$
$$\qquad\qquad\text{片段（(2.5)）：}\ R_{\sigma,\eta}(T)\ll_{\varepsilon,\eta}T^{2\varepsilon}\max_{\sigma-\varepsilon\le\alpha\le1}T^{(\alpha-\sigma)/2}\mathrm{N}(\alpha,C\!\cdot\!T)+T^{(1-\sigma)/2+2\varepsilon}$$
$$\Longrightarrow\ \textbf{两个方向各用不同机器}：\text{dyadic splitting}\ \text{vs}\ \text{部分求和＋density 控制的测度界}$$
$$\textbf{未发现} \text{形如"}|D(t_j)|\ge V\Longrightarrow|D(t)|\ge V/2\ \text{for}\ |t-t_j|\le r"\ \text{的}\ \textbf{统一稳定性链}✓$$

## M2-3：桥的方向与损失 —— **不由 MT 决定**
$$\text{所需桥}：K_{\rm disc}(R,V)\Longrightarrow|E(V/2)|\gtrsim rR\Longrightarrow R\lesssim|E(V/2)|/r$$
$$\text{MT 提供的是}\ \textbf{两个独立估计}：\text{正向给}\ \mathrm{N}(1-\nu,T)\ll T^{2\nu+2\varepsilon}+\#\{\text{one-spaced LV}\}；\ \text{反向给}\ R\ \text{的测度界（(2.5)）}$$
$$\qquad\textbf{两者并不经由同一}\ K\text{-坐标复合} \Longrightarrow \text{桥损失}\ \ell_{\rm bridge}\ \textbf{不能由 MT 的指数账本读出}✓$$

## M2-4：⭐ MT 是否实际上**绕开**了该桥 —— **是**
$$\text{MT 的证明结构}：\text{正向＝dyadic splitting＋标准零点检测多项式的精化；反向＝部分求和＋density 控制的测度界}$$
$$\qquad\Longrightarrow\ \textbf{MT 并未使用}\ \boxed{K_{\rm disc}\to K_{\rm meas}}\ \text{这一桥}✓$$
$$\text{唐先生预设的判死标准}：\ \Longrightarrow\ \boxed{\textbf{M2-C}}$$

---

## 判定：**M2-C**
$$\boxed{\text{MT 使用了不同机制，不能把其证明归约成这个 measure}\leftrightarrow\text{one-spaced 桥}}$$
$$\Longrightarrow\ \text{当前的}\ r\asymp1/\log T\ \text{桥}\ \textbf{只能保留为独立结构判定}，\ \textbf{不能进入 MT 的 exponent ledger}✓$$
$$\qquad\textbf{注意}：\text{这}\ \textbf{不是} \text{"桥是错的"}，\ \text{而是}\ \textbf{"MT 的往返不由该桥承载"}\ —— \text{故}\ \text{E6-9 的}\ \Delta\ \text{推法}\ \textbf{仍然不能成立}\ ✓$$

## 由此得到的修正状态
$$\boxed{\begin{aligned}X1&:\ \text{完成（Prop 1.1 推论：}\mathrm{N}(1-\nu,T)\ll T^{2\nu+2\varepsilon}+\#\{\text{one-spaced LV}\}\text{）}\\ X2&:\ \text{完成（The 1.2＋}\mathrm{Lemma\ 2.1/2.2}\text{：density}\to\text{测度型 LV）}\\ X3&:\ \textbf{round-trip loss OPEN}（\text{且}\textbf{不能} \text{由 MT 的机器读出}\\ \mathrm{GM}&:\ \textbf{暂缓}\end{aligned}}$$
$$\textbf{新增事实（本档最有价值）}：\text{MT 的两方向}\ \textbf{各用不同机器}（\text{dyadic splitting／部分求和＋density 控制的测度界）}$$
$$\qquad\Longrightarrow\ \text{"density}\leftrightarrow\text{large-value 是否强度等价"}\ \text{在 MT 的框架内}\ \textbf{根本不是一个可复合的往返问题}✓$$

## 边界（N1/N2 严守）
$$\text{① 证据来源为}\ \textbf{arXiv HTML 的片段}（\text{外部来源，仅作数据）}，\ \textbf{未读全 16 页}；\ \text{§M2-2／M2-4 的判定}\ \textbf{受此限制}；$$
$$\text{② M2-C}\ \text{为}\ \textbf{据现有片段的最佳判定}，\ \text{若后续读到完整证明发现稳定性链}\ \Longrightarrow\ \textbf{须重判}；$$
$$\text{③ 记号更正（}\log T=T^{o(1)}，\ell_{\rm bridge}=0／o(1)\text{）}\ \textbf{立即生效}；\quad\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 净产出
$$\text{(i) 记号更正：}\ell_{\rm bridge}\ \text{须写为}\ 0\ \text{（幂指数层级）或}\ o(1)，\ \textbf{不得} \text{写}\ O(\varepsilon)；$$
$$\text{(ii) M2-1 取得（集合定义／区间／}\exists M\ \text{量词／}R_{\sigma,\eta}\ \text{测度型）；}$$
$$\text{(iii) M2-2／M2-4：MT 未使用统一的}\ r\text{-稳定性链，而用 dyadic splitting 与部分求和＋density 控制的测度界；}$$
$$\text{(iv) 判定}\ \textbf{M2-C}：\text{该桥}\ \textbf{不得} \text{进入 MT 的 exponent ledger；}\ r\asymp1/\log T\ \text{仅保留为独立结构判定；}$$
$$\text{(v) 状态修正＋新事实（MT 两方向各用不同机器 ⟹ 往返复合问题在其框架内不成立）。}$$
