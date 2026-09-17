# ③-B-2 · **机制搬运到 $\zeta$**：构造 ＋ 精确障碍（**临界指数的来源**）

> 依唐先生 11:21「继续」｜承接 ③-B 第一轮（`docs/P3-B-*`）✓
> 目标：把素数竞赛机制（**调和权重 ＋ 低阶零点共振**）从 $L(s,\chi)$ 搬到 $\zeta$ 自身 ✓
> **门槛（沿用）**：$\Delta_X$ 须 ①算术生成（非误差定义）②局部不可见 ③跨尺度不可积 ✓

---

## 1. 素数竞赛机制的**解剖**（搬什么？）
$$\text{(a)}\ \textbf{分裂}：\text{素数按特征分裂} \Longrightarrow \text{每类自己的}\ L\ \text{函数}✓$$
$$\text{(b)}\ \textbf{调和权重}：\sum_{p\le X}\frac{\chi(p)}{p}\ \text{收敛} \Longrightarrow \text{极限}\ =-\sum_p\log\!\big(1-\tfrac{\chi(p)}p\big)=\log L(1,\chi)✓✓$$
$$\text{(c)}\ \textbf{共振}：\text{偏置方向由}\ L(s,\chi)\ \text{的}\ \textbf{低阶零点} \text{决定（Rubinstein--Sarnak）}⟹ \text{极限涉及}\ \sum_\gamma\frac{1}{1/4+\gamma^2}✓✓$$
$$\Longrightarrow\ \textbf{可搬运的骨架}：\text{分裂}\to\text{调和加权}\to\text{极限存在}\to\text{极限值／逼近率由零点决定}✓$$

## 2. $\zeta$ 侧的类比对象：**能不能造出来？**（答案：能，但不够）
$$\text{阻尼}\ \textbf{二次平滑} \text{的 Chebyshev 对象}：\boxed{\mathcal O_X:=\int_1^X\frac{\psi(t)-t}{t^2}\,dt}✓$$
$$\qquad\text{良定义}：|\psi(t)-t|\ll\sqrt t\Longrightarrow \text{被积}\ll t^{-3/2}\ \text{可积}✓\quad\text{（}\textbf{算术生成}：\text{只用}\ \psi=\sum\Lambda(n)）✓\ \text{①部分满足}✓$$
$$\text{显式公式}：\psi(t)-t=-\sum_\rho\frac{t^\rho}{\rho}+O(\log t) \Longrightarrow \mathcal O_X=\mathcal O_\infty+\sum_\rho\frac{X^{\rho-1}}{\rho(\rho-1)}+\ldots✓$$
$$\qquad\Longrightarrow\ \textbf{极限}\ \mathcal O_\infty=-\sum_\rho\frac{1}{\rho(\rho-1)}\ \text{是}\ \textbf{绝对收敛} \text{的零点（}\sum 1/\gamma^2）✓✓$$
$$\qquad\Longrightarrow\ \textbf{逼近率}：|\mathcal O_\infty-\mathcal O_X|\asymp X^{\beta_{\max}-1}\ \text{（最大}\ \beta\ \text{支配）} \Longrightarrow \textbf{确实读出}\ \beta_{\max}✓✓$$

$$\text{(X)}\ \text{如此则}\ \mathcal O_X\ \text{同时具备}\ \text{①算术生成}\ \text{与}\ \text{零点共振}\ ⟹\ \text{看起来是候选}✓\quad\textbf{但下面三条同时失败}✓✓$$

## 3. ⭐⭐⭐ 三条失败（**本刀的真正结果**）

### 3.1 失败一（②局部不可见）⟹ **不成立**
$$\text{逼近率}\ |\mathcal O_\infty-\mathcal O_X|\asymp X^{\beta-1}\ \text{在}\ \textbf{有限层就是可测量的}（\text{这正是 G4 做过的事}）$$
$$\Longrightarrow\ \textbf{没有局部盲性}：\text{偏差}\ \textbf{直接可见} \text{——它不是"局部看不见、全局才显影"，而是"}\ \textbf{局部就是误差项本身}✓✓$$

### 3.2 失败二（①非插入）⟹ **阈值靠归一化塞入**
$$\text{要得到}\ \beta\le\tfrac12，\text{必须把}\ |R(X)|\ \text{与}\ X^{-1/2}\ \text{比较} \Longrightarrow \textbf{指数}\ \tfrac12\ \text{是}\ \textbf{手写} \text{进去的}✓$$
$$\qquad(\text{单位量纲检验}：\text{对象本身}\ \mathcal O_X\ \text{只给"逼近率"，}\ \text{它}\ \textbf{不知道自己该跟谁比})✓✓$$
$$\qquad\Longrightarrow\ \text{与 S1 同病}：\text{三分性由归一化产生，}\ \textbf{非算术产生} \Longrightarrow \textbf{①失败}✓✓$$

### 3.3 ⭐⭐⭐ 失败三（**临界指数的来源**）—— 本刀核心
$$\text{问：}\ \text{阈值指数}\ \tfrac12\ \text{能从哪里}\ \textbf{合法} \text{地来？三个可能来源全部被堵}：$$
$$\begin{array}{ll}
\text{(A)}&\textbf{归一化}（\text{把}\ R\ \text{除以}\ X^{-1/2}）\Longrightarrow \textbf{插入}，\text{禁止}✗\\
\text{(B)}&\textbf{函数方程对称轴}\ \mathrm{Re}\,s=\tfrac12 \Longrightarrow \text{合法算术}，\text{但}\ \text{我方档案已判为"completion $\equiv$ 同一堵墙"}（\text{E4-1 S1}）✗\\
\text{(C)}&\textbf{显式公式本身} \Longrightarrow \text{退化为}\ \textbf{已知 RH 判据} \Longrightarrow \text{rule 6 判死}✗\\
\end{array}$$
$$\Longrightarrow\ \boxed{\text{临界指数}\ \tfrac12\ \text{的算术来源}\ \textbf{恰好就是那些已知／已封闭的来源}}✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{这就是 ③-B 的真正障碍}：\text{缺陷机制需要临界指数，}\ \text{而}\ 1/2\ \text{无处合法可得}}✓✓$$

## 4. 判定
$$\text{构造（X）}\ =\ \text{②}\ \mathrm{FALSE}\quad(\text{三条同时失败：②无盲性；①阈值靠插入；③指数来源已封闭})✓✓$$
$$\boxed{③\text{-B-2}\ =\ \text{②}\ \mathrm{FALSE}\quad(\text{搬运被}\ \textbf{"临界指数来源"} \text{精确阻断})}✓✓$$
$$\qquad\textbf{诚实}：\text{这不是"我们没做出来"，而是}\ \boxed{\text{障碍被定位到一个}\ \textbf{单点}：\text{指数}\ 1/2\ \text{的合法来源}}✓✓$$

## 5. ⭐⭐⭐ 由此得到的**新规格**（直接指向 P2）

$$\text{要么}\ 1/2\ \text{来自}\ \textbf{归一化}（\text{禁止}）／\textbf{对称}（\text{已封闭}）／\textbf{显式公式}（\text{已知判据}），\ \text{要么}：$$
$$\boxed{\text{指数}\ \tfrac12\ \text{必须}\ \textbf{动态地} \text{产生——作为某个}\ \textbf{自洽方程／流的临界指数}}✓✓✓$$
$$\qquad(\text{关键区别}：\text{临界指数作为}\ \textbf{不动点线性化本征值} \text{出现时，它是}\ \textbf{导出的}，\text{不是插入的}✓✓)$$
$$\Longrightarrow\ \boxed{③\text{-B-2 的失败}\ \textbf{精确指向 P2}：\text{物理机制搬运（尺度演化}\to\text{不动点}\to\text{谱约束}）}}✓✓✓$$

$$\textbf{P2 的硬要求（由本刀反推）}：\text{(i) 流}\ \textbf{必须是算术的}（\text{整数性／乘法结构}）；\ \text{(ii) 不动点}\ \textbf{必须被强制}（\text{不能假设}）；$$
$$\qquad\text{(iii) 临界指数}\ \textbf{必须等同于}\ \beta_{\max}-\tfrac12\ \textbf{而不靠任何显式公式}✓✓$$

## 6. 边界
$$\text{(i)}\ \text{零数值；未用 RH}✓\quad\text{(ii)}\ §2\ \text{的显式公式步骤为}\ [\textbf{结构判定}]（\text{未逐行核}）✓$$
$$\text{(iii)}\ \text{(B) 的引用来自我方档案}\ \text{E4-1 S1}\ \text{的既有判定}✓\quad\text{(iv)}\ \textbf{本轮}\ \textbf{未} \text{造出合格对象}✓$$
