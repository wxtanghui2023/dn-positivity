# V318 — **精确算术恒等式搜索**（exact arithmetic identity search）章程 ＋ 第一轮候选审计

> 唐先生 2026-09-16 16:54 指定。
> 动机：V316／V317 构成**双向封口**后，必须向外跨一步，而不是在封口内部继续找门。

---

## 0. 档案状态（本轮起点）
$$\text{V316：variational coordinate system}\ \textbf{closed}；\qquad\text{V316：}C^{\star}\ \text{forcing source}\ \textbf{DEAD（audited）}$$
$$\text{V317：feasible-domain source}\ \textbf{DEAD（audited）}；\qquad\text{V318：}\textbf{search exact arithmetic identities outside the variational coordinates}$$

## 1. 结构性二分（V316＋V317 的共同结论）
$$\boxed{\text{改变 kernel 有效强度}\Rightarrow\lambda>1\ \text{的独立算术来源}}\quad\text{或}\quad\boxed{\text{改变 admissible domain}\Rightarrow\mathcal A_{\text{arith}}\subsetneq\mathcal A}$$
$$\text{V316 封掉第一条的现有来源；V317 封掉第二条的现有自然来源。}\Longrightarrow\ \textbf{第三条拓扑只能是：}$$
$$\boxed{\text{Arithmetic identity}\longrightarrow\text{new invariant}\longrightarrow\text{spectral consequence}}$$
$$\text{其中}\ \textbf{new invariant 必须在 V316 之外先独立存在}。$$

## 2. 第一性对象：**跨尺度 exact identity**（不是算术算子）
$$\text{三层须同时满足：}\quad\text{local arithmetic}\longrightarrow\text{global arithmetic identity}\longrightarrow\text{spectral/variational consequence}$$
$$\textbf{第 1、2 步完全不出现 RH}。$$

## 3. 搜索域定义（第一轮）
$$\boxed{\mathcal D_{\text{new}}=\Big\{\text{exact arithmetic identities}:\ \textbf{additive}\times\textbf{multiplicative},\ X\asymp T,\ \textbf{RH-blind}\Big\}}$$
$$\text{只做三步：}\ \boxed{\text{identity}\to\text{derive exact consequence}\to\text{classify consequence}}$$

## 4. 新增重建准则 **R7**（唐先生 16:54）
$$\text{若机制}\ M\ \text{成立，必须存在自然构造的量}\ A_T\ \text{满足}\ A_T^{\text{local}}\stackrel{\text{exact}}{=}A_T^{\text{global}}，\text{其中：}$$
$$\text{① 两边不是同一对象的重新命名；② 等式在}\ X\asymp T\ \textbf{无条件成立}；③ \text{至少一侧同时含}\textbf{加性与乘性结构}；$$
$$\text{④ 不能通过显式公式把零点直接引入；⑤ 不能依赖 Weil positivity；⑥ 不能是有限阶相关；}$$
$$\text{⑦ 不能只是 support/counting identity；⑧ 必须产生此前没有的}\textbf{定量不等式或刚性条件}。$$
$$\text{最后才检查}\ A_T\Rightarrow\begin{cases}\lambda>1,\\ \text{新的 admissible-domain restriction},\\ \text{直接产生新的 spectral localization}\end{cases}\quad\text{否则 DEAD}。$$

## 5. 与 C1–C8 的本质区别（本轮方法论要点）
$$\text{C1–C8 问的是：}\textbf{"有没有一个结构，可以塞进现有变分框架？"}$$
$$\text{V318 问的是：}\boxed{\textbf{"算术本身有没有一个 exact identity，使 V316 的框架被迫出现，而不是我们主动把算术塞进去？"}}$$

## 6. 后果分类（只有 VI 继续）
$$\mathrm{I}\ \text{旧 explicit-formula/value-surface；}\quad\mathrm{II}\ N(\sigma,T)\text{/density；}\quad\mathrm{III}\ \text{finite-order correlation；}$$
$$\mathrm{IV}\ \text{positivity/repackaged Weil；}\quad\mathrm{V}\ \text{support/counting；}\quad\mathrm{VI}\ \boxed{\text{genuinely new}}$$
$$\textbf{中间任何一步坍缩到 I–V 立即关闭}。\quad\textbf{第一轮甚至不要求碰到}\ \lambda。$$

---

## 7. 第一轮候选审计（诚实分类）
$$\textbf{K1 Voronoi／Dirichlet 双曲型精确恒等式（如}\sum_{n\le x}d(n)=2\sum_{n\le\sqrt x}\lfloor x/n\rfloor-\lfloor\sqrt x\rfloor^{2}\text{）}：$$
$$\qquad \text{exact}\ ✓,\ \text{additive}\times\text{multiplicative}\ ✓,\ \text{RH-blind}\ ✓\ \Longrightarrow\ \text{后果为计数型}\ \to\ \textbf{类 V（support/counting）}\ ✗$$
$$\textbf{K2 Theta 变换律（}\theta(1/x)=\sqrt x\,\theta(x)\text{，Poisson＋dilation）}：\text{exact}\ ✓\ \text{additive}\times\text{multiplicative}\ ✓；$$
$$\qquad \text{后果＝FE／archimedean 通道}\ \to\ \textbf{旧语言（A-leak，V172 §5a；V174/V179/V181 已审）}\ ✗$$
$$\textbf{K3 Möbius 卷积恒等式（}\sum_{d\mid n}\mu(d)=\mathbf 1_{n=1}\text{）}：\text{exact}\ ✓\ \text{双结构}\ ✓；\text{后果＝Mertens 型增长界}\ \to\ \textbf{I/V（V287-B、V150 W2）}\ ✗$$
$$\textbf{K4 Gauss 和／CRT 分解型精确恒等式}：\text{exact}\ ✓\ \text{双结构}\ ✓；\text{后果落大筛法／MV 型不等式}\ \to\ \textbf{III/V（MV 本身）}\ ✗$$
$$\textbf{K5 Parseval／群谱恒等式（乘法群上的精确谱分解）}：\text{exact}\ ✓；\text{但其谱}\ \textbf{不是}\ \zeta\ \text{零点谱（对象错配，同 V215 判据）}；\text{后果落}\ L\text{-值}\ \to\ \textbf{I（value face）}\ ✗$$
$$\textbf{K6 Perron＋留数型精确恒等式}：\text{直接含零点}\ \to\ \text{违反 R7④}\ \longrightarrow\ \textbf{I}\ ✗$$
$$\textbf{K7 算术 site／trace-formula 型精确恒等式（Deninger/AOB 线）}：\text{已在 G10／Deninger 6.6 判死}\ \to\ \textbf{I/IV}\ ✗$$

$$\Longrightarrow\ \textbf{第一轮结果：}\mathrm{VI}\ \text{格}\ \textbf{空}（K1–K7 全部坍缩到 I–V）。$$

## 8. 第一轮结论与边界
$$\text{① 第一轮}\ \textbf{未找到}\ \mathrm{VI}\ \text{型恒等式；}\quad\text{② 但这只是}\ \textbf{枚举型}，\textbf{不构成不可能性}（N1/N2）；$$
$$\text{③ }\mathcal D_{\text{new}}\ \text{的定义（additive}\times\text{multiplicative、}X\asymp T、\text{RH-blind）本身是}\textbf{新的工作坐标}，\text{不在 I–V 任何语言内；}$$
$$\text{④ 全档}\ \textbf{未用 RH}；零数值；未跑 Lean。$$

## 9. 下一轮的可操作入口（不回到枚举模式）
$$\text{(a) 把}\ \mathcal D_{\text{new}}\ \text{中"additive}\times\text{multiplicative}"\ \textbf{形式化}：\text{找出所有已知的}\ \textbf{双侧精确恒等式}\ \text{模板}$$
$$\qquad \text{（Voronoi 型、Poisson 型、CRT 型、卷积反演型）并逐一检查其}\ \textbf{后果是否必然坍缩}；$$
$$\text{(b) 反向做法：先固定"希望得到的后果类型"（新刚性条件），再问"什么样的精确恒等式能产生它"——}$$
$$\qquad \textbf{但不允许用目标函数反塑恒等式}（否则违反本轮纪律）；$$
$$\text{(c) 若 (a) 也全坍缩，则}\ \mathcal D_{\text{new}}\ \text{在当前数学工具下}\ \textbf{DEAD}，\text{此时应改变目标（§E.4 第二出口）而非继续找恒等式}。$$
