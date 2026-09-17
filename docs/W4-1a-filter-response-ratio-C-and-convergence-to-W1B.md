# ⚔️ W4-1a · **滤波响应比：平移不变性否决 ＋ 判别力上界 ＋ 与 W1-B 收敛**

> 依唐先生 12:59（开 W4）＋ W4-1 宪章 §3 第一刀 ✓
> **本刀结果**：**C（工具失效）**，卡点＝**同一缺口（独立算术上界）**；⭐**结构性发现：W4 与 W1-战术B 收敛** ✓✓

---

## §1 对象与判据（宪章 §3）
$$\text{两模态}：\ \text{在线}\ m_0(n):=n^{i\gamma}=e^{i\gamma y_n}\qquad\big|\qquad \text{离轴}\ m_\beta(n):=n^{\beta-\frac12}e^{i\gamma y_n}=e^{(\beta-\frac12)y_n}e^{i\gamma y_n}✓$$
$$\text{滤波族}\ \mathcal F：\text{差分}\ \Delta_h^k、\ \text{小波基、vanishing-moment 核}✓$$
$$\boxed{\mathcal R(\mathcal F;T,\gamma,\beta):=\frac{\big|\mathcal F[m_\beta]\big|}{\big|\mathcal F[m_0]\big|}}✓\qquad\text{目标}\ \exists\mathcal F\in\mathcal F:\ \mathcal R\gg1\ \text{且算术可实现}✓$$

## §2 ⭐⭐ 否决一：**$y$-卷积型滤波一律无效**（平移不变性）
$$\text{若}\ \mathcal F\ \text{是}\ y\ \text{上的卷积（即在}\ \gamma\ \text{上的 Fourier 乘子）}，\ \text{其响应只依赖}\ m\ \text{在}\ y\ \text{上的局部形状}✓$$
$$\qquad \text{两模态的振荡部分}\ \textbf{完全相同}（\text{均为}\ e^{i\gamma y}），\ \text{差别只在}\ \textbf{包络}\ e^{(\beta-\frac12)y}✓✓$$
$$\qquad \text{而}\ \gamma\gg1\ \text{时包络在滤波支撑上}\ \textbf{近似常数} \Longrightarrow \boxed{\mathcal R\to1\ (\gamma\to\infty)}✓✗✓$$
$$\Longrightarrow\ \text{要看见包络增长，滤波支撑须}\ \boxed{\Delta y\gtrsim\frac1{\beta-\frac12}}✓✓$$
$$\qquad\Longrightarrow\ \text{而可用范围只有}\ y\in[0,\log X]\sim L \Longrightarrow \textbf{可探测阈值}\ \boxed{\beta-\tfrac12\gtrsim\frac1{\log X}}✓✓$$

## §3 ⭐⭐ 判别力的**上界**（本刀量化）
$$\text{最优}\ \Delta y\asymp L \Longrightarrow \boxed{\mathcal R\lesssim e^{(\beta-\frac12)L}\asymp X^{\beta-\frac12}}✓✓$$
$$\qquad\text{在}\ X=T^{1+\eta}：\ \boxed{\mathcal R\lesssim T^{(1+\eta)(\beta-\frac12)}}\ ——\ \textbf{幂次级}✓✓$$
$$\text{即：}\ \text{滤波的判别力}\ \textbf{是}\ \text{包络增长}\ \text{的直接读数}，\ \text{不是新的谱机制}✓✗✓$$

## §4 ⭐⭐⭐ **但比值 ≠ 选择**（本刀关键，也是卡点）
$$\text{比值大}\ \textbf{可以} \text{完全来自模态自身的增长}（m_\beta\ \text{本身}\ \asymp n^{\beta-\frac12}），\ \text{而非滤波"制造"了选择}✓$$
$$\qquad\Longrightarrow\ \text{要与"任意其它贡献"比较，须有}\ \textbf{同一量的独立算术上界}——\ \text{否则比值无判别意义}✓✓$$
$$\text{这恰好就是}\ \text{W5-DEAD §6 的}\ \textbf{要求 (D)}：\mathcal I_T\ \text{须有}\ \textbf{独立的算术上界／递推／压缩律}✓✓$$
$$\qquad\Longrightarrow\ \text{而 (D) 的缺失就是}\ \textbf{W3（值面）／W6（支配）}\ \text{同一缺口}✓✓$$

## §5 ⭐⭐⭐ 结构性发现：**W4 与 W1-战术B 收敛**
$$\text{W1-战术B（唐先生 11:57）}：\text{找整数序列}\ A_{n+1}=F(A_n,\text{prime data})\ \text{使}$$
$$\qquad \text{纯算术上界}\ A_n\le Cn^\alpha\qquad\text{与}\qquad \text{离线零点下界}\ A_n\ge cn^{\alpha+\delta(\beta)} \Longrightarrow \text{矛盾}✓$$
$$\text{本刀的}\ \mathcal R\ \text{正是同一形状}：\ \boxed{\text{一个量同时需要}\ \textbf{增长敏感响应}\ ＋\ \textbf{独立算术上界}}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{W4 ⟶ W1-B 收敛}}（\text{两者}\ \textbf{缺的是同一个东西}）✓✓✓$$
$$\qquad \text{优点（W4 优于 W1 之处）}：\text{W4 的响应量}\ \textbf{可显式写、可算}（\mathcal R\ \text{的幂次}\ X^{\beta-\frac12}\ \text{已定}）✓✓$$

## §6 判定（TACTICAL ATTACK）
$$\boxed{\text{W4-1a}\ =\ \textbf{C（工具失效）}}✓$$
$$\qquad \text{卡点（精确到不等式）}：\ \boxed{\text{判别力}\ \mathcal R\ \text{与}\ \text{独立算术上界}\ \text{不能同时获得}——\ \text{前者来自包络增长，后者正是缺失输入}}✓✓$$
$$\qquad \text{已确立的正成果}：\ \text{①}\ y\text{-卷积型滤波}\ \textbf{一律无效}（\mathcal R\to1）；\ \text{②}\ \text{支撑下界}\ \Delta y\gtrsim\frac1{\beta-1/2}；\ \text{③}\ \mathcal R\lesssim X^{\beta-1/2}\ \text{幂次级}✓✓$$
$$\qquad ⚠️\ \text{保留}：\text{非}\ y\text{-卷积型（如}\ y\text{-非平稳、与}\ \log n\ \text{网格直接耦合的滤波）}\ \textbf{未穷尽}✓$$

## §7 边界
$$\text{(i)}\ §2\ \text{的平移不变性论证为}\ [\textbf{结构}]（\text{以}\ \gamma\gg1\ \text{及滤波}\ O(1)\ \text{尺度为前提}）✓$$
$$\text{(ii)}\ §3\ \text{为本档推导（初等指数比较）}✓\quad\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零数值}✓$$
