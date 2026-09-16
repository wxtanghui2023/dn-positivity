# V316-C ④ 弱 E–L —— 最小假设钉死（④-0 / ④-1），**先数学后 Lean**

## ④-0 目标（唐先生固定）
$$h：＝u-v_\lambda,\qquad \int_I h=0\ (\text{约束})\ \Longrightarrow\ \int_I h\,v_\lambda+\lambda^{2}\,\texttt{Bfun}(v_\lambda,h)=0$$
其中点态 E–L 已 CLOSED：$v_\lambda(s)+\lambda^{2}\int_I|s-t|v_\lambda(t)dt=D_\lambda$（逐点 in $s$）✓

## ④-1 ⭐ **核心问题**：$F(s,t)：＝|s-t|h(s)v_\lambda(t)$ 是否 $\in L^{1}(I\times I)$？

### ⭐ 结论（好消息）：**可以榨出来，不需要造黑箱**
$$\text{链条：}\ \textbf{可容许类自带的连续性}\ \Longrightarrow\ L^{1}\ \Longrightarrow\ \text{product}\ L^{1}$$

**依据（框架内已有的）**：§4 `WindowProfile` 含 $\texttt{contDiff}\ \mathbb R\ 3\ v$ ✓（$\Rightarrow$ 连续 $\Rightarrow$ 紧区间上有界）
$$\Longrightarrow\ v_\lambda\ \text{（即}\ v_\star\ \text{型窗口）连续}\ ✓;\qquad h=u-v_\lambda,\ u\ \text{同类}\ \Longrightarrow\ h\ \text{连续}\ ✓$$

### 推导链（每步都是标准事实，**不是新公理**）
$$\text{(1)}\ |s-t|\le1\ \text{on}\ I\times I\ \Longrightarrow\ |F(s,t)|\le|h(s)|\,|v_\lambda(t)|$$
$$\text{(2)}\ \text{Tonelli（非负）}：\ \iint|h(s)||v_\lambda(t)|=\Big(\int_I|h|\Big)\Big(\int_I|v_\lambda|\Big)$$
$$\text{(3)}\ \text{连续＋紧区间有界＋}\ \mu(I)<\infty\ \Longrightarrow\ h,v_\lambda\in L^{1}(I)\ \Longrightarrow\ \text{(2)}<\infty$$
$$\text{(4)}\ \Longrightarrow\ F\in L^{1}(I\times I)\ ✓\qquad\textbf{（Fubini 可用 ⟹ 不必用 Tonelli ⟹ } h\ \textbf{可变号无妨}\ ✓）$$

## ④-2 Lean 映射（API 名**待核验**，下一轮逐条 grep 确认）
```
①  h 连续 ⟹ AEStronglyMeasurable            ： Continuous.aestronglyMeasurable
②  紧区间上连续 ⟹ 有界                        ： IsCompact.exists_bound_of_continuousOn（待核验名）
③  有限测度                                    ： volume I < ∞（μ := volume.restrict Icc'）
④  ⟹ Integrable h μ / Integrable v μ          ： Integrable.of_bound（AEStronglyMeasurable + 界 + μ univ < ∞）
⑤  product 可积                                 ： Integrable.mul_prod（待核验名）
⑥  核有界支配 ⟹ F 可积                          ： Integrable.mono'＋(1)
⑦  Fubini：nested = 双积分                       ： MeasureTheory.integral_prod / integral_integral（已核验 Prod.lean:444/472）
⑧  交换 s,t                                      ： 已 CLOSED 的 Bfun_symm 手法（product-measure swap）
```

## ④-3 ⚠️ 判死标准（唐先生设定）
$$\textbf{若仅凭已建立的条件推不出}\ F\in L^{1} \Longrightarrow \textbf{不得偷偷补}\ \texttt{Integrable}\ \text{然后继续，}$$
$$\qquad \text{必须追溯到}\ h\in L^{2},\ v_\lambda\in L^{2},\ |s-t|\le1\ \text{是否足以推出 product}\ L^{1}$$

**本档的回答**：$\textbf{足以}$ ✓ —— 而且用的不是 $L^{2}\subset L^{1}$，是更强的 **连续 ⟹ 有界 ⟹ $L^{1}$**（紧区间）；
$$\text{故}\ F\in L^{1}(I\times I)\ \textbf{可由框架内条件推出} \Longrightarrow\ \textbf{④ 不需要暴露新的前提缺口}\ ✓$$

## ④-4 需要新增的**最小**假设清单（供下一轮 Lean 直接落）
$$\textbf{(A)}\ \texttt{ContinuousOn}\ h\ I\quad\text{（或整条直线}\ \texttt{Continuous}\ h\text{）}\qquad\textbf{(B)}\ \texttt{ContinuousOn}\ v_\lambda\ I$$
$$\text{（二者均可由 §4 WindowProfile 的可容许性给出，}\textbf{非}额外数学假设 ✓）$$
$$\textbf{(C)}\ \text{约束}\ \int_I h=0\qquad\textbf{(D)}\ \text{外层可积}\ \texttt{Integrable}\ (s\mapsto h(s)\cdot\int_I|s-t|v_\lambda(t)dt)\ \mu\ \text{（由 (A)(B)+Fubini 可得 ✓）}$$

## ④-5 分步执行顺序（下一轮）
```
④-0 精确列出 h / vλ 的 integrability        ← 本档完成（数学层）
④-1 prove product Integrable（从连续+有界榨出）← 第一刀
④-2 nested = double integral [Fubini]
④-3 double integral = Bfun(v,h) [symmetry]
④-4 weak E–L（配 ∫h=0）
⑤  constraint gap → ⑥ unique minimizer
```
**不要先写 ④-4**；先落 ④-1 的 `Integrable` —— 它决定 V316 弱 E–L 是真正闭合，还是暴露新缺口。

## 边界（诚实标注）
$$\text{① 本档是}\ \textbf{数学层假设清单}，\text{未写 Lean（唐先生要求先钉数学）✓}$$
$$\text{② API 名带"待核验"标记，下一轮逐条 grep 确认后再写代码 ✓}$$
$$\text{③ "可容许 ⟹ 连续" 依据 §4 WindowProfile 的}\ \texttt{contDiff ℝ 3}\ \text{字段（已读，V310/V311 存档）✓}$$
$$\text{④ 未用 RH；零数值 ✓}$$
