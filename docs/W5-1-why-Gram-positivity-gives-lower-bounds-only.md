# ⚔️ W5-1 · **审「Gram 正性为什么只能给下界」**

> 依唐先生 12:56「开 W5，不要收工」；第一刀＝**审 Gram 正性为何只给下界** ✓
> **已查地图** ✓（`V186`／`V187`／`V188`／`V113`／`V114`／`E119 §④`／`POS1`／`POS2`／`C-30`）✓

---

## §0 三条硬门槛（**照录唐先生**）
$$\boxed{\text{W5-SOS/Gram}\ \textbf{只允许攻击「上界／负方向」本身}}✓$$
$$\textbf{四禁}：\text{①不把 Weil positivity 换成 Gram 后再证一次 RH}\ \big|\ \text{②不把显式公式重写成 SOS}$$
$$\qquad\text{③不只得到下界／正定性／平均正性}\ \big|\ \text{④不通过选测试函数把}\ \tfrac12\ \text{编进去}✓✓$$
$$\textbf{继承 W6 教训}：\boxed{\text{「带限」本身不能改变离散}\ \log n\ \text{网格的}\ X\ \text{级秩／范数}} \Longrightarrow \text{W5 必须产生}\ \textbf{rank-changing／selection-strength}✓✓$$

## §1 目标结构（照录）
$$0\le Q_T(c)=\sum_{m,n}c_m\overline{c_n}K_T(m,n)\le\mathcal B_T(c),\qquad K_T\succeq0✓$$
$$\exists\rho=\beta+i\gamma,\ \beta>\tfrac12：\ \mathcal B_T(c_\rho)\ll T^{1-\delta}\|c_\rho\|^2\quad\text{而}\quad Q_T(c_\rho)\gg T^{2\beta-1-o(1)}\|c_\rho\|^2✓$$
$$\Longrightarrow\ 2\beta-1>0 \Longrightarrow \textbf{矛盾}✓\qquad\text{否则}：\text{只得}\ Q_T\ge0\ \text{或只得下界而无独立上界} \Longrightarrow \textbf{POS／Gram 重写，停}✓✓$$

## §2 ⭐⭐⭐ 审计结果（本刀核心）：上界只有**两个**原始来源
$$\text{(a)}\ \textbf{正性是一阶锥条件}：K\succeq0\ \text{只给}\ Q\ge0\ \text{——}\textbf{一维信息（符号）}，\ \textbf{不含幅度}✓$$
$$\text{(b)}\ \text{要上界，必须来自}\ \textbf{另一个源}。\ \text{原始可能的来源只有两类}：$$
$$\qquad\text{(i)}\ \textbf{解析／数值侧}：\text{直接用显式公式算}\ Q_T(c)\ \text{的幅度} \Longrightarrow \boxed{\text{这就是值面墙}\ \textbf{W3}}✓✓$$
$$\qquad\text{(ii)}\ \textbf{支配结构}：\text{majorant／dominating kernel} \Longrightarrow \boxed{\text{这就是}\ \textbf{W6}（\text{已封}）}✓✓$$
$$\Longrightarrow\ \boxed{\text{上界请求}\ \textbf{自动落到 W3 或 W6}} ⟹ \text{新攻击面必须来自第三处}✓✓$$

## §3 ⭐⭐⭐ 更深一层：**inertia／det 三面性**（我方档案逐字）
$$V187\ \text{逐字}：\text{离轴对}\ \{\rho,1-\bar\rho\}\ \text{对不同不变量表现}\ \textbf{完全不同}：$$
$$\qquad\text{signature}\ n_+-n_-\ \text{贡献}\ \mathbf 0（\textbf{盲}）\ \big|\ \textbf{inertia}\ n_-\ \text{贡献}\ +1（\textbf{可见，但需}\ n_-=0）\ \big|\ \operatorname{tr}\ \text{中性}\ \big|\ \operatorname{tr}(G^2)\ \text{可见}\ \big|\ \det G\ \text{可见}✓✓$$
$$\Longrightarrow\ \text{任何}\ \textbf{index／signature／Euler 型} \text{全局不变量}\ \textbf{对离轴零点结构盲}✓✓$$
$$\qquad\Longrightarrow\ \text{能"看见"离轴的只有}\ \textbf{count／inertia 型}（\text{而}\ n_-=0\ \text{＝Weil 正性}\iff\mathrm{RH}）\ \text{或}\ \det\ \text{型}（\text{Deninger，缺 canonical polarization}）✓✓$$
$$\Longrightarrow\ \boxed{\text{上界＝"数出负方向个数"＝}\textbf{覆盖秩问题}；\ \text{而}\ n_-=0\ \text{本身}\ =\ \mathrm{RH} ⟹ \textbf{循环}}✓✓✓$$

## §4 唯一逃逸口（我方已有登记，与唐先生门槛③同向）
$$V187\ \text{唯一逃生口}：\textbf{第四类不变量}（\text{非线性／范数型／多层}）；\ \text{状态}\ =\ \boxed{\textbf{形式存在、实质封闭}}✓✓$$
$$V188／K2\text{-E}''：\ \text{线性通道}\ \textbf{饱和} ⟹ \textbf{Input strength}\ne\textbf{selection strength}✓✓$$
$$\text{与唐先生门槛"要 rank-changing"}\ \textbf{逐字一致}✓✓$$

## §5 ⚠️ 定量校准（对目标结构本身）
$$\text{若上界只到}\ \mathcal B_T\ll T^{1-\delta}\|c\|^2，\ \text{与}\ Q_T\gg T^{2\beta-1}\ \text{冲突需}\ 2\beta-1>1-\delta \iff \boxed{\beta>1-\tfrac\delta2}✓$$
$$\Longrightarrow\ \text{该夹逼}\ \textbf{只抓近线零点}（\beta\ \text{接近}\ 1），\ \textbf{抓不到}\ \beta\in(\tfrac12,\ 1-\tfrac\delta2)✓✗$$
$$\qquad\text{要抓全场}\ \beta>\tfrac12 \Longrightarrow \text{须}\ \boxed{\mathcal B_T\ll T^{o(1)}}\（\text{近乎}\ T^0\ \text{级上界}）✓✓$$
$$\qquad ⚠️\ \text{现有机器最好水平是 MV 型}\ L^2X\ \textbf{（远超}\ T^1\text{）} ⟹ \text{差距是}\ \textbf{幂次级}✓✓$$

## §6 判定
$$\boxed{\text{W5-1}\ =\ \textbf{C（工具失效）}}：\text{Gram 正性只给下界——因上界所需互补信息}\ =\ \textbf{inertia／count 型}，\ \text{而}\ n_-=0\ \text{即 RH} ⟹ \textbf{循环}✓✓$$
$$\qquad\text{且上界的}\ \textbf{两个已知来源}\ \textbf{分别就是}\ W3（\text{值面}）\ \text{与}\ W6（\text{已封}）✓✓$$
$$\Longrightarrow\ \boxed{\text{新攻击面只可能来自}\ \textbf{第四类不变量}（\text{非线性／范数型／多层}）}✓✓$$
$$\text{下一刀判据}：\text{能否给出}\ \textbf{第四类不变量的具体候选}？\ \text{能} \Longrightarrow \text{继续 W5}；\ \text{不能} \Longrightarrow \text{W5 亦为 POS 重写}✓✓$$

## §7 边界
$$\text{(i)}\ §0／§1\ \text{照录唐先生 12:56}✓\quad\text{(ii)}\ §3\ \text{引}\ V186／V187\ \text{逐字（我方档案）}✓$$
$$\text{(iii)}\ §5\ \text{为本档定量校准}✓\quad\text{(iv)}\ \textbf{未用 RH}；\ \textbf{零数值}✓$$
