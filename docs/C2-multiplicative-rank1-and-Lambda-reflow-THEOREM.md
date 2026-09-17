# ⚔️ **C2 执行**：**乘法 rank-1 定理**（严格）＋**旧对象回流定理**（$\Lambda$ 出现 $r$ 次）

> 依唐先生 15:31「开 C2」＋**先纠正 C1 越权** ✓
> **本档结果**：C2-a **已证**（rank ≤1）；**C2-1 检查升级为定理**（$a_r=d_r*\Lambda^{*r}$）；C2-b **仅第一刀**（依嘱**不判死**）✓✓✓

---

## §0 🔧 纠正 C1 的越权（逐字采纳）
$$\text{我在}\ \texttt{75af581}\ \text{写：}\text{"把}\ \mu\ \text{归一侧后长侧}\Rightarrow\text{必须化双线性"}\ \Longrightarrow \boxed{\textbf{不能作为结论}}✗$$
$$\text{正确}：\text{那正是}\ \textbf{C2 最值得打的一刀}；\ \log\ \text{的}\ \textbf{无符号＋光滑} \text{提供了一条}\ \textbf{与 parity 不同的潜在通道}✓✓$$
$$\qquad \Longrightarrow \text{若该通道成立，}\ \textbf{才是真正的新机制}；\ \text{故 C1 的判词降级为}\ \textbf{"待 C2 判定"}✓✓$$

## §1 ⭐⭐⭐ C2-a 执行：**乘法 rank-1 定理**（严格、初等）
$$\text{设纯乘法相位}\ \Phi(m_1,\dots,m_r)=f(m_1\cdots m_r)；\ \text{取}\ x_i=\log m_i,\ u:=x_1+\cdots+x_r,\ \phi(u):=f(e^u)✓$$
$$\Longrightarrow \Phi=\phi(u) \Longrightarrow \partial_{x_i}\Phi=\phi'(u),\qquad \boxed{\partial_{x_i}\partial_{x_j}\Phi=\phi''(u)\ \ \forall i,j}✓$$
$$\Longrightarrow H_\Phi=\phi''(u)\,\mathbf 1\mathbf 1^{\!\top}✓\qquad\big(\mathbf 1\mathbf 1^{\!\top}\ \text{特征值}\ r,\ \underbrace{0,\dots,0}_{r-1}\big)✓✓$$
$$\Longrightarrow \boxed{\operatorname{rank}H_\Phi\le1}\quad(\text{且}\ =\mathbf 1\iff\phi''(u)\ne0)✓✓✓$$
$$\Longrightarrow \text{flat 方向}\ v\perp(1,\dots,1)：D_v\Phi=0,\ D_v^2\Phi=0 \Longrightarrow \textbf{vdC／Poisson 在这些方向无相位增益}✓✓$$
$$\qquad 📌\ \text{故唐先生预期成立}：\boxed{\text{多变量表面复杂度}=r\quad\text{而}\quad\textbf{真正振荡维数}=1}✓✓✓$$
$$\qquad \Longrightarrow \boxed{\text{高阶分裂}\ \textbf{不增加振荡维数}}；\ \text{额外}\ r-1\ \text{维}\ \textbf{坍缩进系数}✓✓$$

## §2 坍缩的精确形式：就是那个卷积
$$\sum_{m_1,\dots,m_r}\Big(\prod\log m_i\Big)F(m_1\cdots m_r)=\sum_n a_r(n)F(n),\qquad a_r(n):=\!\!\sum_{m_1\cdots m_r=n}\!\!\prod_i\log m_i✓$$
$$\text{Dirichlet 级数}：\sum_n\frac{\log n}{n^s}=-\zeta'(s) \Longrightarrow \boxed{\sum_n\frac{a_r(n)}{n^s}=\big(-\zeta'(s)\big)^r}\quad\Longleftrightarrow\quad a_r=\underbrace{\log*\cdots*\log}_{r}✓✓$$

## §3 ⭐⭐⭐ C2-1 检查（唐先生预警）⟹ **升级为定理：旧对象回流**
$$-\zeta'=\zeta\cdot\Big(-\frac{\zeta'}{\zeta}\Big)，\quad \zeta\leftrightarrow 1\ (\text{即}\ d_1)，\quad -\frac{\zeta'}{\zeta}\leftrightarrow\Lambda✓$$
$$\Longrightarrow \big(-\zeta'\big)^r=\zeta^{\,r}\Big(-\frac{\zeta'}{\zeta}\Big)^{r} \Longrightarrow \boxed{a_r=d_r*\underbrace{\Lambda*\cdots*\Lambda}_{r\ \text{次}}}✓✓✓$$
$$\qquad(d_r:=1^{*r}=\text{除数函数}\；\text{校验}\ r=1：1*\Lambda=\log n\ ✓)✓$$
$$\Longrightarrow \boxed{\text{Heath--Brown 高阶分裂}\ \textbf{不能移除}\ \Lambda，\ \text{而是}\ \textbf{把它乘以}\ r\ \text{份}}✓✓✓$$
$$\qquad 📌\ \text{"长侧"}\ \textbf{等价于}\ r\ \text{阶}\ \Lambda\text{-卷积}；\ \text{而每个}\ \Lambda\ \text{都被 parity 挡} \Longrightarrow \textbf{分裂不产生新通道}✓✓$$
$$\qquad ⚠️\ \text{但依唐先生：}\textbf{尚不能判死} \text{——见 §4 的剩余缝}✓✓$$

## §4 ⭐⭐ C2-b 第一刀：$\log$ 权重的光滑性能否独立产生 cancellation
$$\text{权重}\ W=\prod_i\log m_i=\prod_i x_i\ \text{在}\ (u,v)\ \text{坐标下}：\text{关于}\ v\ \textbf{是多项式}✓$$
$$\textbf{flat 方向}：\text{无相位} \Longrightarrow \text{求和＝}\textbf{格点计数/Euler--Maclaurin} \Longrightarrow \boxed{\textbf{无 cancellation}}✗\quad(\text{只给计数})✓$$
$$\textbf{振荡（}u\text{）方向}：\text{光滑加权} \Longrightarrow \textbf{partial summation} \Longrightarrow \text{按唐先生判据}\ \boxed{\textbf{不算新机制}}✗✓$$
$$\Longrightarrow \text{C2-b}\ \textbf{第一刀}：\text{光滑性只在}\ u\ \text{方向起作用、且在 flat 方向退化为计数} \Longrightarrow \textbf{未发现独立通道}✗✓$$
$$\qquad ⚠️\ ⭐\ \textbf{唯一未审处（精确缝）}：\text{权重与相位的}\ \textbf{高阶交互} \text{——}\ W\ \text{的导数进入}\ \textbf{稳定相/分部积分高阶项}，\ \text{可能产生}\ \textbf{非 partial-summation 型} \text{的额外抵消}$$
$$\qquad\qquad \text{即}：\text{须核}\ \int W\,\phi^{(m)}\ \text{型项的}\ \textbf{符号/量级结构}；\ \text{此为}\ \textbf{C2-b 未完部分}✓✓$$

## §5 C2 状态表（依嘱不判死）
| 审计 | 状态 | 结果 |
|:--|:--|:--|
| **C2-a** 乘法坐标 Hessian rank | **已完成（严格）** | $\operatorname{rank}\le1$ ⟹ **无新振荡维数** ✓✓ |
| **C2-1** 旧对象回流检查 | **升级为定理** | $a_r=d_r*\Lambda^{*r}$ ⟹ $\Lambda$ 出现 $r$ 次 ✓✓✓ |
| **C2-b** 权重独立 cancellation | **仅第一刀** | flat 方向＝计数；$u$ 方向＝partial summation ⟹ 未发现 ✗（**唯一缝＝权重×相位高阶交互**）|
| **C2-c** 复合指数 $\delta_r$ | 未做 | — |

## §6 边界
$$\text{(i)}\ §1\ \textbf{严格}（\text{初等链式法则}）✓✓；\ §2--§3\ \textbf{严格}（\text{Dirichlet 级数恒等式}）✓✓；\ §4\ \text{为}\ [\textbf{结构}] \text{级第一刀}✓$$
$$\text{(ii)}\ \textbf{依唐先生：C2-b 完成前}\ \textbf{不判死}；\ \log\ \text{权重是唯一真正未审的缝}✓✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零数值}✓$$
