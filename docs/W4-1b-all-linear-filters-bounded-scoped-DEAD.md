# ⚔️ W4-1b · **全部线性滤波受同一上界**（$y$-卷积限制**不需要**）⟹ W4 限定关闭

> 依唐先生 13:08 选 1（穷尽非 $y$-卷积型滤波）✓
> **本刀结果**：W4-1a 的保留口**闭合**；$\mathcal R\lesssim X^{\beta-1/2}$ 对**全部线性滤波**成立；**W4 = DEAD（限定）** ✓✓

---

## §1 待补口（W4-1a §6 保留项）
$$\text{非}\ y\text{-卷积型}：\text{①}y\text{-非平稳滤波}\ \big|\ \text{②与}\ \log n\ \text{网格直接耦合}\ \big|\ \text{③整数变量上的差分}\ \Delta_h^{\rm int}\ \big|\ \text{④乘性／Dirichlet 卷积型}✓$$

## §2 ⭐⭐⭐ 本刀核心：**限制条件其实不需要**
$$\text{关键结构}：\ \boxed{m_\beta(n)=w(n)\cdot m_0(n)},\qquad w(n):=n^{\beta-\frac12}>0\ \textbf{光滑且乘性}✓✓$$
$$\text{即：}\textbf{离轴模态＝在线模态}\ \times\ \text{光滑正权}。\ \text{于是对}\ \textbf{任意线性泛函}\ \mathcal F：$$
$$\mathcal F[m_\beta]=\mathcal F[w\cdot m_0] \Longrightarrow \frac{\big|\mathcal F[w\,m_0]\big|}{\big|\mathcal F[m_0]\big|}\ \text{由}\ w\ \text{在}\ \mathcal F\ \text{有效支撑上的}\ \textbf{变差} \text{控制}✓✓$$
$$\Longrightarrow\ \boxed{\mathcal R(\mathcal F)\ \lesssim\ \frac{\sup_{\rm supp}w}{\inf_{\rm supp}w}\asymp e^{(\beta-\frac12)\Delta y}\ \le\ X^{\beta-\frac12}}✓✓✓$$
$$\text{其中}\ \Delta y\ \text{为}\ \mathcal F\ \text{的有效支撑长度}；\ \text{而}\ \Delta y\le L\ (\text{总范围})✓$$

### §2.1 四个保留类逐项对照
$$\text{①}y\text{-非平稳}：\text{仍线性} \Longrightarrow \text{受 §2 支配}✓\qquad\text{②网格直接耦合}：\Delta y\le L \Longrightarrow \text{同界}✓$$
$$\text{③整数差分}\ \Delta_h^{\rm int}：\text{相位因子}\ (e^{i\gamma h/n}-1)\ \textbf{在两模态中相同} \Longrightarrow \textbf{比值中抵消} \Longrightarrow \mathcal R\asymp n^{\beta-1/2}✓✗$$
$$\qquad(\text{即：W4-1a 的否决在整数差分层}\ \textbf{逐字重演})✓✓$$
$$\text{④乘性／Dirichlet 卷积}：w\ \text{乘性}\Longrightarrow\ \text{卷积型} \mathcal F\ \text{对}\ w\cdot m_0\ \text{的响应}\ \text{仍由}\ w\ \text{变差控制}✓✗$$

$$\Longrightarrow\ \boxed{\text{四个保留类}\ \textbf{全部} \text{落入 §2 的同一上界}} ⟹ \textbf{W4-1a 的保留口闭合}✓✓✓$$

## §3 非线性滤波：判据退化（不是新出口）
$$\text{取}\ \mathcal F[m]=\big|\sum_nc_nm(n)\big|^2：\ \mathcal F[m_\beta]=\big|\sum_nc_nw_nm_0(n)\big|^2✓$$
$$\text{若}\ \mathcal F[m_0]\ \textbf{因相消而小}，\ \text{而}\ \mathcal F[m_\beta]\ \text{为"一般大小"} \Longrightarrow \text{比值可任意大}✓✗✓$$
$$\qquad\Longrightarrow\ \textbf{这是"与偶然相消之比"，不是选择} \Longrightarrow \text{须与}\ \textbf{算术基线} \text{比较} \Longrightarrow \text{即须}\ \textbf{独立算术上界}✓✓$$
$$\Longrightarrow\ \text{与}\ \text{W5-DEAD §6 的}\ \textbf{要求 (D)} \text{同一缺口；与 W4-1a §4 同一"比值≠选择"}✓✓$$

## §4 判定
$$\boxed{\textbf{W4 = DEAD（限定）}}：\text{算术线性滤波}\ \textbf{不可能} \text{超过}\ X^{\beta-1/2} \Longrightarrow \text{无幂次级选择力}✓✓$$
$$\qquad \text{非线性滤波} \Longrightarrow \text{须 (D) 独立算术上界} \Longrightarrow \text{同一缺口}✓✓$$
$$\qquad ⚠️\ \text{限定范围}：\text{"线性泛函}\ +\ \text{模态=光滑正权}\times\text{在线模态"}\ \text{这一结构内}；\ \textbf{未} \text{断言任意算术机制不存在}✓$$

## §5 三墙汇合（今日结论）
$$\boxed{\textbf{W6}（\text{majorant}）：\text{缺独立幅度控制}\ \big|\ \textbf{W5}（\text{Gram／SOS}）：\text{缺 (D) 独立算术上界}\ \big|\ \textbf{W4}（\text{离散滤波}）：\text{缺同一上界}}✓✓$$
$$\Longrightarrow\ \text{三墙}\ \textbf{独立收敛到同一缺口}；\ \text{与}\ \text{W1-战术B}\ \text{同形}\ (\text{增长敏感响应}\ +\ \text{独立算术上界})✓✓$$
$$\qquad \text{对台账"三面一墙"栏}：\ \textbf{结构性经验支持}（\text{仍非定理}）✓$$

## §6 边界
$$\text{(i)}\ §2\ \text{为}\ [\textbf{结构}] \text{级（以线性性与}\ w\ \text{光滑正为前提）}✓\quad\text{(ii)}\ §2.1\ \text{四类逐项为初等核验}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零数值}✓$$
