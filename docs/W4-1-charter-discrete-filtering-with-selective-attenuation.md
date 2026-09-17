# ⚔️ **W4-1 宪章** · 离散滤波 ＋ **对 off-axis 模态的选择性衰减**

> 依唐先生 12:59：**关 W5，直接开 W4**；门槛继承 W5／W6 ✓
> **已查地图** ✓（`V172 §5a`／`E119`（窗口不能平均相位）／`C-29`／`C-30`／`W5-DEAD`）✓

---

## §0 **继承门槛（硬）**
$$\boxed{\textbf{不得} \text{再寻找一个"更强的正性泛函"}}✓✓$$
$$\text{W4 必须寻找的是}：\boxed{\text{一个}\ \textbf{算术上的离散滤波机制}}✓$$
$$\qquad \text{使某个 off-axis 模态}\ \boxed{n^{\beta-\frac12}e^{i\gamma\log n}}\ \text{在离散}\ \log n\ \text{网格上受到}\ \textbf{选择性衰减}$$
$$\qquad \text{而临界线模态}\ \boxed{n^{i\gamma}}\ \textbf{不被同样衰减}✓✓$$
$$\text{这符合继承的}\ \textbf{rank-changing／selection-strength} \text{门槛，\textbf{而非}再加一个 quadratic／nonlinear observable}✓✓$$

## §1 唐先生原 W4 战术（照录）
$$\text{找离散差分算子}\ \Delta_hA(X)=A(X+h)-A(X)\ \text{使}\ \Delta_h^kA_{\rm ar}(X)\ \textbf{快衰} \text{而有限素数部分不衰}$$
$$\Longrightarrow\ \Delta_h^kA=\textbf{pure finite-arithmetic signal}+o(1) \Longrightarrow \text{把 Archimedean leakage}\ \textbf{从结构上滤掉}✓$$
$$\qquad \text{用}\ \textbf{有限差分／小波／vanishing moments}\ \text{直接打，不再做 Mellin 分解}✓✓$$

## §2 ⭐ 为什么 W4 天然避开 W6 的两个死因
$$\text{W6 的死因①：}\textbf{带限不降离散范数}（\text{采样密度}\asymp X）。\ \text{W4 不用带宽，用}\ \textbf{网格上的差分算子}✓✓$$
$$\text{W6 的死因②：}\textbf{任何有限阶 smoothness 只给 log-saving}。\ \text{W4 的机制是}\ \textbf{模态选择}（\text{modulation-selective}），\ \text{不是平滑度}✓✓$$
$$\qquad \text{关键区别}：n^{\beta-\frac12+i\gamma}\ \text{与}\ n^{i\gamma}\ \text{在}\ y=\log n\ \text{上的差别是}\ \textbf{指数增长率}\ \left(\beta-\tfrac12\right)y，\ \text{而差分算子对该增长率的响应}\ \text{可以}\ \textbf{非平凡}✓✓$$
$$\qquad ⚠️\ \text{但}\ \text{既有}\ \textbf{负向警示}（E119）：\text{窗口}\ \textbf{不能} \text{平均相位}（\text{相位跨窗变化}\ O(1)） \Longrightarrow \text{局部}\ L^2\ \text{不能绕开点态墙}✓✓$$

## §3 第一刀设计（W4-1a）
$$\text{① 定义离散滤波族}：\ \mathcal F:=\big\{\Delta_h^k\ (h\ \text{与网格匹配}),\ \text{小波基},\ \text{vanishing-moment 核}\big\}✓$$
$$\text{② 算}\ \textbf{响应比}：\ \boxed{\mathcal R(\mathcal F;T,\gamma,\beta):=\frac{\big|\mathcal F\big[n^{\beta-\frac12}e^{i\gamma\log n}\big]\big|}{\big|\mathcal F\big[n^{i\gamma}\big]\big|}}✓✓$$
$$\qquad\text{目标}：\ \exists\mathcal F\in\mathcal F\ \text{使}\ \mathcal R\gg1\ \textbf{且算术可实现}；\ \text{理想}\ \mathcal R\asymp T^{\eta}\ \text{级}✓✓$$
$$\text{③ 判据}：\ \mathcal R\gg1\ \Longrightarrow \textbf{ALIVE}；\ \text{所有算术可实现}\ \mathcal F\ \text{对两模态}\ \mathcal R\asymp1 \Longrightarrow \textbf{FALSE}✓✓$$
$$\qquad ⚠️\ \text{须同时验证}\ \mathcal F\ \text{不引入 RH／不依赖}\ \beta✓$$

## §4 四结果（TACTICAL ATTACK）
$$A\ \text{穿透}\ \big|\ B\ \text{局部穿透}\ \big|\ C\ \text{工具失效（精确到不等式）}\ \big|\ D\ \text{反例封死}；\ \textbf{禁止第五种}✓$$

## §5 边界
$$\text{(i)}\ §0／§1\ \text{照录唐先生 12:56／12:59}✓\quad\text{(ii)}\ §2\ \text{的 E119 引为既有判定}✓$$
$$\text{(iii)}\ \textbf{本轮未跑计算}；\ \textbf{未用 RH}；\ \textbf{零数值}✓$$
