# ⚔️ **UB-3C：线性相位 $\phi=tu$ 精确模型** —— **因子化 ＋ 局部判据** ⟹ **C2 = NO-GO（线性相位）**；**撤销"危险判据"**

> 依唐先生 15:41「先不直接用 $\phi=nu$，先取 $\phi(u)=tu$ 线性相位」＋ 两处修正 ＋ C1–C4 清单 ✓
> **本档结果**：① 采纳两处修正；② $r$ 重和**因子化**；③ **局部相位增量 $\asymp L^2$，与 $t$ 无关** ⟹ **普遍压制**；④ **撤销** $|\phi'|\gg\log X$ 判据 ✓✓✓

---

## §0 采纳两处修正（唐先生）
$$\textbf{(第一处)}\ m_\eta\asymp Q^{r-1}\ \text{只是}\ \textbf{光滑超曲面体积}，\ \textbf{不是} \text{离散 reciprocal-sum level-set 定理}⟹ \text{须}\ \sup_\eta N(\eta,\Delta),\ \sum_\eta N(\eta,\Delta)^2✓✓$$
$$\textbf{(第二处)}\ ⭐\ \text{相位须看}\ \textbf{局部}：C\phi'(CH_k)\,\Delta H_k,\ \textbf{不是} \text{总跨度}\ |\phi'||C|\sum L_i✓✓✓$$
$$\qquad \text{因局部相干簇可与总体振荡}\ \textbf{共存}✓✓$$

## §1 线性相位模型（$\phi''=0$ ⟹ 无 Airy／无退化）
$$\phi(u)=tu \Longrightarrow \phi'(u)=t,\ \phi''(u)=0 \Longrightarrow C=-\frac{t}{2\pi}✓\qquad H=\frac{2\pi}{C}\mathrm{diag}(k_i^2)\ \textbf{对角}✓✓$$
$$\text{驻点自洽}\ u=CH_k\ \text{自动满足}；\ \text{可行盒}\ x_i=\frac C{k_i}\in[L_i,2L_i] \Longleftrightarrow \boxed{k_i\in\Big[\frac{Q_i}{2},Q_i\Big]},\ \ Q_i:=\frac{|C|}{L_i}=\frac{t}{2\pi L_i}✓✓$$

## §2 ⭐⭐⭐ 相位**分离** ⟹ $r$ 重和**因子化**
$$\Phi_k^{\rm stat}=\phi(CH_k)+2\pi rC=tCH_k+2\pi rC=-\frac{t^2}{2\pi}H_k+2\pi rC✓$$
$$\therefore\ \text{权重相位}\ e^{-i\lambda H_k},\qquad \lambda:=\frac{t^2}{2\pi}✓\qquad\Longrightarrow\ H_k=\sum_i\frac1{k_i}\ \textbf{分离}✓✓$$
$$\text{而盒约束}\ k_i\in[Q_i/2,Q_i]\ \textbf{逐变量} \Longrightarrow \boxed{\sum_k\frac{\prod_i\mathfrak b_i(k_i)}{\prod_ik_i^2}e^{-\lambda H_k}\ =\ \prod_{i=1}^r\Big(\sum_{k_i\in[Q_i/2,Q_i]}\frac{\mathfrak b_i(k_i)}{k_i^2}e^{-\lambda/k_i}\Big)}✓✓✓$$
$$\Longrightarrow ⭐\ \boxed{\text{非对角驻点总质量}\ =\ (\textbf{一维 reciprocal 和})^{\,r}}✓✓✓$$

## §3 ⭐⭐⭐ 局部相位增量（唐先生第二处的**正确形式**）
$$\partial_{k_i}\Phi_k^{\rm stat}=\phi'(CH_k)\cdot C\cdot\Big(-\frac1{k_i^2}\Big) \Longrightarrow \Big|\frac{\partial\Phi}{\partial k_i}\Big|=t\cdot\frac{t}{2\pi}\cdot\frac1{k_i^2}\asymp\frac{t^2}{2\pi Q_i^2}✓✓$$
$$\text{代入}\ Q_i=\frac{t}{2\pi L_i}：\qquad \frac{t^2}{2\pi}\cdot\frac{4\pi^2L_i^2}{t^2}=2\pi L_i^2 \Longrightarrow \boxed{\Delta_{\rm loc}\Phi\asymp 2\pi L_i^2\ \ \textbf{与}\ t\ \textbf{无关}}✓✓✓$$
$$\Longrightarrow ⭐\ L_i=\log M_i\ge1 \Longrightarrow \Delta_{\rm loc}\Phi\gg1 \ \textbf{恒成立} \Longrightarrow \boxed{\textbf{局部强振荡（普遍）}}✓✓✓$$
$$\qquad 📌\ \text{故}\ \texttt{913f47d}\ \text{的}\ \boxed{|\phi'|\gg\log X}\ \textbf{判据撤销}：\text{它是}\ \textbf{总跨度} \text{的误判；}\ \text{正确的局部量}\ =2\pi L^2✓✓✓$$

## §4 C1–C4 逐项（唐先生清单）
$$\textbf{C1 level-set density}：\text{因子化后}\ \textbf{无需} \sup_\eta N\ \text{估计}；\ \text{逐变量}\ k_i\in[Q_i/2,Q_i]✓✓$$
$$\textbf{C2 相邻}\ \eta\ \text{间距}：\Delta H_k\asymp\frac1{k_i^2}\asymp\frac1{Q_i^2}✓✓\quad(\text{已钉死})✓$$
$$\textbf{C3 相干簇}：\text{相位}\ \lambda H_k\ \textbf{分离} \Longrightarrow \textbf{无跨变量簇积累}✓✓$$
$$\textbf{C4 真实上界}：\text{一维因子}\ \sum_{k\asymp Q}\frac{e^{-\lambda/k}}{k^2}：\ |f'|=\frac{\lambda}{k^2}\asymp L_i^2\gg1\ \text{且}\ f'\ \text{不变号}$$
$$\qquad \xrightarrow{\text{一阶导检验＋Abel}} \Big|\sum\Big|\ll\frac{1}{Q^2L^2}\quad\text{vs}\ \textbf{绝对}\ \asymp\frac1Q \Longrightarrow \boxed{\text{单变量增益}\asymp\frac{Q}{t^2}\cdot\ldots\asymp(Lt)^{-1}}✓✓$$
$$\qquad \Longrightarrow \boxed{r\ \text{重总质量}\ \ll\ \textbf{绝对}\times(Lt)^{-r}}✓✓✓$$

## §5 判词（**含一条撤销**）
$$\boxed{\text{① C2 = NO-GO（线性相位模型）：非对角驻点总质量被}\ \textbf{普遍压制}✓✓✓}$$
$$\boxed{\text{② 撤销}\ \texttt{913f47d}\ \text{的"危险判据"}\ |\phi'|\gg\log X（\text{总跨度误判}）⟹ \text{代之以}\ \textbf{局部量}\ 2\pi L^2\gg1✓✓✓}$$
$$\boxed{\text{③ 线性相位的净效果}：t\ \text{只影响}\ \textbf{绝对大小}（C^{r/2}）\ \text{与}\ \textbf{可行盒}，\ \textbf{不影响} \text{压制质量}✓✓}$$
$$\text{故}\ \text{乙}\ \textbf{在线性相位模型下关闭}；\ \text{迁移到}\ \theta\text{-型（}\phi''\ne0）\ \text{时须重核}\ §3\ \text{的局部量（多出}\ \phi''\ \text{项}）✓✓$$

## §6 ⭐⭐ 你预言的"二级结构"——**出现了，但方向相反**
$$\text{你预言：若压制}\ \textbf{来自} \text{reciprocal-sum level set 自身} \Longrightarrow \text{得到}\ \textbf{additive}\times\textbf{multiplicative 接口}✓✓$$
$$\text{本档确认}\ \boxed{\text{该接口}\ \textbf{存在且运作}}（H_k\ \text{的加性 reciprocal 结构}\times k\ \text{的乘性格点}）✓✓✓$$
$$\qquad ⚠️\ \text{但其}\ \textbf{方向是压制}（\text{杀死非对角 Poisson 质量}），\ \textbf{不是增益}✓✓✓$$
$$\Longrightarrow \boxed{\text{这正是你清单里"漂亮的 C2 NO-GO"那一支}}✓✓$$

## §7 边界
$$\text{(i)}\ §1--§3\ \textbf{严格}（\text{初等求导}＋\text{盒等价}）✓✓；\ §4\ \textbf{C4}\ \text{为一阶导检验＋Abel 的}\ \textbf{标度级}（\text{未含}\ \mathfrak b_i\ \text{显式}）✓$$
$$\text{(ii)}\ \textbf{未做}：\theta\text{-型迁移、Airy 支线、}\mathfrak b_i\ \text{的显式 Fourier 衰减}✓；\ \textbf{未用 RH}；\ \textbf{零数值}✓$$
$$\text{(iii)}\ ⚠️\ \text{因子化依赖}\ \textbf{逐变量盒}（\text{若实际约束含}\ \prod m_i\asymp X\ \text{的耦合，须单独核非对角余项——但该余项已在 UB-2 处理}）✓✓$$
