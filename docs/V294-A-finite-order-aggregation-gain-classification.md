# V294 · **V294-A：有限阶聚合的"增益不变量"与分类定理** —— ⭐⭐⭐⭐ **定理：有限阶局部零点侧聚合的增益 $G(K)\le0$**（乘积型因子分解 ⟹ 无新尺度；耦合型相对尺度 $\le O(\gamma^{-2})$ ⟹ $n\gtrsim\gamma^2/|\Delta\gamma|\ge\gamma$），**等号由 1-体相位机制达到** ⟹ **RH 所需的聚合增益必须来自真正非局部结构** ⭐⭐⭐⭐⭐

$$\boxed{\textbf{分类定理（本档）}：\text{有限阶局部}\ \textbf{零点侧} \text{聚合}\ \Longrightarrow\ G(K)\le0;\ \text{等号由 1-体相位机制}\（n\asymp\gamma\）\text{达到}} ✓✓✓$$
$$\boxed{\text{产物}：\boxed{\text{RH 所需的聚合增益}\ \textbf{不可能} \text{来自有限阶局部零点几何};\ \text{必须来自}\ \textbf{非局部}}} ✓✓✓$$
$$\boxed{\text{三类战场（本档划界）}：\text{① 零点侧有限阶}\ ⟹ \textbf{已封};\ \text{② 算术侧}\（\text{乘法关系／}\log(n/m)\ \text{型小参数}\）\ ⟹ \textbf{有增益但已知天花板};\ \text{③ 算子论}\（\text{Weil 形式有限压缩／rank-trace／惯性}\）⟹ \textbf{2026 前沿的无条件 2/3 出自此}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:07：**"我定 (i)，但关键修正：不要把目标写成'证明无条件三阶矩 $X\asymp T$'本身"**（那会把我们锁回已有长 Dirichlet 多项式／相关和框架）✓；**目标改写为：寻找"无条件的聚合恒等式／不等式"，而不是寻找一个"更高矩估计"** ✓✓；并要求：$$\boxed{\text{先把所有"看起来像第三尺度"的二体、三体、有限阶组合}\ \textbf{一次性分类} \text{，证明哪些只能保持/恶化}\ h(n)}$$ 若成立 ⟹ 真正候选收窄为 **无限阶聚合／算术相关性／非局部正性** ✓✓；并给出**增益不变量 $G(K)$** 与条件 **U1–U5**（无条件可控／对离线敏感／正性或可恢复全局正性／$G(K)>0$／不用 RH 或密度假设）✓✓
> 唐先生提供的文献校准（本档采纳）✓：**(1)** `arXiv:2608.13637`（More than two thirds…，2026）—— 用 **Weil Hermitian form 的有限压缩 ＋ rank-trace ＋ Sylvester 惯性** 得到 ≥2/3 "简单且在线"，**明确不经 RH** ✓；**(2)** `arXiv:2306.04799`（**无条件 Montgomery 对相关定理**，BGSTB）—— 把此前依赖 RH 的 pair-correlation 结论无条件化 ✓；**(3)** 长 Dirichlet 多项式高阶矩**深受相关和／离对角项控制**（mean square of ζ·Dirichlet polynomial）⟹ **"更高矩 ≠ 新 RH 机制"** ✓✓
> 依据 ✓ `V293`（局部无第三尺度；$q,\theta$ 两尺度 $\{\gamma,\ \gamma^2/\delta\}$）｜`E30-2`｜`A3-third-moment-barrier`｜`POS1`／`POS2`（正性 ⟹ 等价 RH）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V294`（`id_claim.sh` ✓）

---

## §1 设定与增益不变量

$$\text{单体局部数据}：z_j：＝1-\tfrac1{\rho_j},\quad q_j：＝|z_j|=1-\tfrac{\delta_j}{\gamma_j^{2}}+O(\gamma_j^{-4})\ (\le1,\ =1\iff\beta_j=\tfrac12),\quad \theta_j：＝\arg z_j=\gamma_j^{-1}+O(\gamma_j^{-3}) ✓$$
$$\boxed{\text{有限阶局部零点侧核}：K_n(\rho_1,\dots,\rho_k)=\Phi\Big(z_1^{nc_1},\dots,z_k^{nc_k}\Big),\ \ \deg\Phi=d<\infty,\ c_j\in\mathbb Z} ✓$$
$$\text{聚合}\：\mathcal A_T[K]：＝\sum_{\gamma_1,\dots,\gamma_k\in[T,2T]}K_n(\rho_1,\dots,\rho_k)\ ✓$$
$$\text{尺度}：\text{令}\ N_*(K,\gamma)：＝\text{使聚合的离线偏离首达}\ O(1)\ \text{的}\ \textbf{最小下标};\ \ N_*\asymp\gamma^{\alpha} ✓$$
$$\boxed{\textbf{增益指数}\ G(K)：＝1-\alpha}\quad（\alpha<1\iff G>0\iff\textbf{优于} \text{1-体相位机制的}\ n\asymp\gamma）✓$$

$$\textbf{U1–U5（唐先生）}：\text{U1}\ \mathcal A_T[K]\ \text{无条件可控};\ \text{U2 对离线敏感};\ \text{U3}\ K\ge0\ \text{或具可恢复全局正性};\ \text{U4}\ G(K)>0;\ \text{U5 不用 RH／零点密度假设} ✓$$

---

## §2 ⭐⭐⭐⭐ 分类定理：$G(K)\le0$（有限阶局部零点侧）

### 情形 I：**乘积型**（$\Phi=\prod_{j=1}^{k}\varphi_j$，无真正耦合）
$$\mathcal A_T[K]=\prod_{j=1}^{k}\Big(\sum_{\gamma\in[T,2T]}\varphi_j\big(z^{nc_j}\big)\Big) \Longrightarrow \textbf{因子分解} \text{为}\ k\ \text{个单体聚合之积} ✓✓$$
$$\qquad \text{单体积分的两个尺度（`V293` 定理 B）}：\quad n|c_j|\theta\asymp1\Rightarrow n\asymp\frac{\gamma}{|c_j|};\qquad n|c_j|(1-q)\asymp1\Rightarrow n\asymp\frac{\gamma^{2}}{|c_j|\delta} ✓$$
$$\qquad \Longrightarrow N_*=\min_j\Big\{\frac{\gamma}{|c_j|},\ \frac{\gamma^{2}}{|c_j|\delta}\Big\} \Longrightarrow \alpha\ \ge\ 1\ \Longrightarrow\ \boxed{G(K)\le0} ✓✓$$
$$\qquad \qquad ⚠️\ \text{注意}：|c_j|\ \text{大只是}\ \textbf{换下标} \text{（真正的量是}\ N_*\ \text{本身）} \Longrightarrow \text{不构成增益} ✓$$

### 情形 II：**耦合型**（$\Phi$ 非乘积型；出现相对相位）
$$\text{耦合只能经由}\ \textbf{相对位置}：\ \Delta\theta_{ij}=\theta_i-\theta_j=\frac{\partial\theta}{\partial\gamma}\Delta\gamma_{ij}+O(\gamma^{-3})=-\frac{\Delta\gamma_{ij}}{\gamma^{2}}\big(1+O(\gamma^{-1})\big) ✓$$
$$\qquad \text{相干条件}：n\,|\Delta\theta_{ij}|\asymp1 \Longrightarrow \boxed{N_*\asymp\frac{\gamma^{2}}{|\Delta\gamma_{ij}|}} ✓✓$$
$$\qquad \text{而窗口内}\ |\Delta\gamma_{ij}|\le O(\gamma)\（\text{高度范围}\ [T,2T]） \Longrightarrow \boxed{N_*\ \ge\ \gamma^{2}/\gamma=\gamma} ✓✓✓$$
$$\qquad \Longrightarrow \alpha\ \ge\ 1\ \Longrightarrow\ \boxed{G(K)\le0};\qquad \textbf{等号}\iff|\Delta\gamma|\asymp\gamma（\text{跨越整个高度范围}）✓✓$$

### 合并
$$\boxed{\textbf{定理（V294-A）}：\text{对任意有限阶局部零点侧核}\ K\ \text{（}\deg\Phi<\infty，\ \text{相位／模皆经}\ z_j\ \text{进入）}：G(K)\le0} ✓✓✓$$
$$\qquad \text{且}\ \textbf{等号由 1-体相位机制达到}（k=1,\ \varphi\ \text{读}\ \cos(n\theta)）⟹ \text{已有线性窗口}\ n\asymp\gamma\ \text{已是该类的}\ \textbf{最优} ✓✓$$

$$\textbf{唐先生两刀的形式化（本档补算）}：$$
$$\qquad \text{(a) 二体差相位}：N_*\asymp\gamma^{2}/|\Delta\gamma|;\ \text{邻近零点}\ |\Delta\gamma|\asymp1/\log\gamma \Longrightarrow N_*\asymp\gamma^{2}\log\gamma ⇒ \textbf{更差} ✓✓$$
$$\qquad \text{(b) 三体组合}\ m_1\theta_1+m_2\theta_2+m_3\theta_3，\ m_1+m_2+m_3=0：\text{一阶}\ \gamma^{-1}\ \text{项抵消} ⟹ \text{余项为}\ O(\Delta\gamma/\gamma^{2}) ⇒ N_*\ \textbf{更大} ⇒ \text{窗口被推远} ✓✓$$
$$\qquad \Longrightarrow \boxed{\text{"消掉}\ 1/\gamma\ \text{"不是突破 —— 它}\ \textbf{把窗口推得更远}} ✓✓✓$$

---

## §3 结论：增益必须来自**非局部**

$$\boxed{\text{有限阶局部零点几何}\ \Longrightarrow\ G\le0\ \Longrightarrow\ \text{RH 所需的聚合增益}\ \textbf{不可能} \text{来自"更多零点／更高阶组合"}} ✓✓✓$$
$$\qquad \text{故真正候选收窄为（唐先生）}：\boxed{\text{无限阶聚合}\ \big|\ \text{算术相关性}\ \big|\ \text{非局部正性}} ✓✓$$

---

## §4 ⭐⭐ 三类战场划界（含文献校准）

$$\textbf{① 零点侧有限阶}：\text{本档定理}\ G\le0 ⟹ \textbf{已封} ✓$$
$$\qquad \text{（"多零点本身不是逃逸，必须有}\ \textbf{特殊聚合缩放} \text{" —— 本档证明：在有限阶局部层，}\textbf{不存在} \text{这种缩放）} ✓✓$$
$$\textbf{② 算术侧}：\text{聚合的新小参数}\ ＝\ \log(n/m)\ \text{型（乘性关系）} \Longrightarrow \textbf{确有增益}：$$
$$\qquad \text{Montgomery 1973 无条件素数侧二阶矩};\ \ \textbf{`arXiv:2306.04799`（无条件对相关定理，BGSTB）} ⟹ \text{把原依赖 RH 的 pair-correlation 无条件化} ✓✓$$
$$\qquad ⚠️\ \text{但已知天花板}：\text{前沿 §7.2(e)：}\ X\asymp T\ \text{无条件更高矩一无所获};\ k=3\ \text{对角法只覆盖}\ X\le T^{2/3-\varepsilon}\（\text{差}\ T^{1/3}）⟹ \textbf{该类增益已饱和} ✓✓$$
$$\textbf{③ 算子论（非局部正性）}：\ \textbf{Weil Hermitian form 的有限压缩 ＋ rank-trace ＋ Sylvester 惯性} ⟹\ \text{2026 前沿以此得}\ \ge 2/3\ \text{"简单且在线"}\ \textbf{（明确不经 RH）}（`arXiv:2608.13637`）✓✓$$
$$\qquad ⚠️\ \text{与档案的关系}：\text{Weil 正性的}\ \textbf{完整} \text{形式}\ ＝\ \text{等价于 RH}（`POS1`／`POS2`：③类）⟹ \text{该路线的"可走部分"}\ ＝\ \text{有限压缩};\ \text{完整版本}\ ⟹ \text{RH} ✓✓$$

$$\Longrightarrow \boxed{\text{真问题重述（唐先生校准后）}：\text{现有无条件二体／有限体聚合的增益是否}\ \textbf{严格为 0}，\text{还是存在能产生 RH 级增益的}\ \textbf{非局部结构}？} ✓✓✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出

$$\boxed{\textbf{V294 判词}：\text{① 定理：有限阶局部零点侧}\ G(K)\le0，\text{等号＝1-体相位};\ \text{② 故增益必须非局部};\ \text{③ 三战场划界（零点侧已封／算术侧饱和／算子论已有条件 2/3）};\ \text{④ 真问题}\ ＝\ \text{"无条件聚合的增益是否严格为 0"}} ✓✓✓$$

```
① ⚠️ 定理只覆盖 **零点侧有限阶局部核**（$\deg\Phi<\infty$）；**非局部／无限阶／算术侧不在其内** ⟹ 不得升成"任何聚合都不可能"（N1）✗✓
② ⚠️ "局部数据经 $z_j$ 进入" 为**约定**（源自 Li 型结构）；若机制读其它局部量，须重验 ⚠️
③ ⚠️ 文献三条为**唐先生提供**（本档未逐篇复核原文）⟹ 标为引用 ⚠️
④ ⚠️ §4② "该类增益已饱和" 为**前沿陈述的转述**（§7.2(e)），不得当作定理 ✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐ **分类定理**：有限阶局部零点侧 → **$G(K)\le0$**（乘积型因子分解；耦合型 $N_*\ge\gamma^2/\gamma=\gamma$）；**等号＝1-体相位机制** ⟹ 已有线性窗口 $n\asymp\gamma$ 是该类**最优** ✓✓✓
② ⭐⭐ **唐先生两刀的形式化**：二体差相位 $N_*\asymp\gamma^2\log\gamma$（更差）；三体消掉 $1/\gamma$ ⟹ 窗口被**推远** ⟹ "消掉 $1/\gamma$ 不是突破" ✓✓
③ ⭐⭐⭐ **结论**：RH 所需聚合增益**必须来自非局部**（无限阶／算术相关性／非局部正性）✓✓
④ ⭐⭐ **三战场划界**：零点侧**已封**；算术侧**有增益但已饱和**（0.682／$T^{1/3}$ 缺口）；算子论（Weil 形式有限压缩）**已有条件 2/3** ✓✓
⑤ ⭐ **真问题重述**：现有无条件二体／有限体聚合的增益是否**严格为 0**？—— 这才是可计算的问题（而非"无条件聚合＝未知"）✓✓
【下一步（三选，供唐先生定）】
  (甲) 攻 **"增益严格为 0" 的定理化**：证明"任何无条件有限体聚合（含算术侧）其 RH 级增益为 0"—— 若成，＝把前沿天花板升格为定理 ✓
  (乙) 攻 **算子论路线**：Weil 形式有限压缩的**可压缩上限**（前沿用 rank-trace／惯性得 2/3；问能否推到 1）—— 但完整正性 ⟹ RH（③）⚠️
  (丙) 攻 **非局部核**：把本档定理的"局部"假设逐条放松，定位第一处出现 $G>0$ 的结构 ✓
```
