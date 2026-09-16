# E6-5（申-1 / A₃ 第一阶段）— **规范化强度坐标 ＋ 可行域 ＋ 目标函数**

> 唐先生 2026-09-16 18:16 裁定：开申-1；**第一产物不是 $\alpha_{\min}$**，而是 $\mathfrak K$／$\mathcal A(\sigma)$／$F(\sigma;\kappa,\mathbf q)$。
> 工作顺序：**申-1A → 1B → 1C → 1D**；**禁止**引用"经典结果告诉我们指数是多少"代替推导（1C）。

---

## 申-1A：规范化（先固定坐标）
$$D(s)=\sum_{n\le X}a_n n^{-s},\qquad s_r=\sigma+it_r,\qquad |t_r-t_j|\ge\delta\ (\textbf{良分离}),\qquad X=T^{\kappa}$$
$$\textbf{系数归一化}：\ \sum_{n\le X}|a_n|^{2}=1$$
$$\textbf{允许系数类（重要，不得默认）}：\text{核估计的强度}\ \textbf{依赖系数类}（a_n=1\ \text{型／Möbius 型／}\Lambda\text{ 型／}\Lambda^{2}\ \text{型）}\Longrightarrow\ \text{须显式登记所用类}✓$$

## 申-1B：抽取强度指数（取代人为 $\alpha$）
$$\mathcal K[B]:\quad\sum_r|D(s_r)|^{2}\ \le\ B(X,T,\sigma,\mathbf a)$$
$$\text{在归一化}\ \sum|a_n|^{2}=1\ \text{下，写成}\ \textbf{指数坐标}：\quad\boxed{B(X,T)\ \ll\ X^{u}\,T^{v+\varepsilon}}$$
$$\Longrightarrow\ \boxed{\text{强度坐标}\ \mathbf q：＝(u,v)\ (\text{核强度指数})；\ \kappa：＝X\ \text{的指数（截断坐标）}}$$
$$\boxed{\mathfrak K=\{\,(\kappa,u,v,\dots):\ \mathcal K\ \text{成立}\,\}}\quad(\text{强度空间，}\ \textbf{取代}\ \alpha\ \text{这个记号})$$

## 申-1C：可行域与目标函数（骨架；指数推导为待办）
$$\text{链（承接 E6-4）}：\ \text{截断}\to\text{零点检测}\to\text{良分离}\to R\to\mathrm{N}(\sigma,T)$$
$$\text{(a) 大值计数}：\ \#\{r:|D(s_r)|\ge V\}\ \le\ V^{-2}\sum_r|D(s_r)|^{2}\ \le\ V^{-2}B\ \Longrightarrow\ R\ll B/V^{2}$$
$$\text{(b) 检测阈值}：\ \text{零点}\rho=\sigma_1+i\gamma,\ \sigma_1\ge\sigma\ \Longrightarrow\ |D(\gamma)|\gg T^{-c(\sigma)}\ (\text{即}\ V=T^{-c(\sigma)})$$
$$\text{(c) 归并}：\ \mathrm{N}(\sigma,T)\ \ll\ R+\text{（截断／检测误差）} \Longrightarrow\ \theta\ \text{的指数}\ =\ u\kappa+v+2c(\sigma)+\text{（误差指数）}$$
$$\Longrightarrow\ \boxed{\theta_{\mathcal K}(\sigma)=\inf_{(\kappa,u,v)\in\mathcal A(\sigma)}F(\sigma;\kappa,u,v),\qquad F：＝u\kappa+v+2c(\sigma)+\mathrm{err}(\kappa,\sigma)}$$
$$\boxed{\mathcal A(\sigma)=\{(\kappa,u,v):\ \text{截断误差、检测条件、核估计（}\mathcal K\ \text{成立）全部满足}\}}$$
$$\textbf{这是 A}_3\ \text{的第一个真正数学对象}✓\quad\text{（}\textbf{注意}：\text{上式}\ F\ \text{的}\ \textbf{具体指数形式为}\ \textbf{[结构判定]}，\ \textbf{未} \text{从文献逐式导出 —— 见 §残余）}$$

## 申-1D（待办）：求边界
$$\text{最后才做}：\inf\theta_{\mathcal K}，\text{并判定}\ \boxed{\text{内部最优}\quad\text{还是}\quad\text{可行域边界最优}}$$
$$\text{若最优点要求某参数取端点（如}\ \kappa=\kappa_{\max}\text{）且}\ \nabla F\ \text{在}\ \mathcal A(\sigma)\ \text{内无下降方向}$$
$$\qquad\Longrightarrow\ \boxed{\text{density improvement}\ =\ \text{必须把}\ \mathfrak K\ \text{的可行域}\ \textbf{向外扩张}}$$
$$\qquad\text{这比"需要更强的大值估计"}\ \textbf{精确很多}✓$$

## 边界对象（承重量的真正形态）
$$\text{不定义}\ \alpha_{\min}；\text{而定义（承接 E6-3 的}\ \mathfrak S_{\rm density}\text{）}：$$
$$\boxed{\mathfrak K(\theta_*)=\{\mathcal K:\ \theta_{\mathcal K}(\sigma)\le\theta_*(\sigma)\};\qquad \text{承重量墙}\ =\ \partial\mathfrak K(\theta_*)}$$
$$\Longrightarrow\ \text{"核强度}\to\text{density exponent"}\ \textbf{不是单变量函数}，\text{而天然是}\ \textbf{偏序可达域}✓$$

## 三种最终结果（唐先生指定，预先登记）
$$\textbf{ALIVE-strong}：\mathfrak K\to\theta\ \text{可显式计算，且存在非平凡边界} \Longrightarrow \text{正式的}\ \textbf{定量承重量}$$
$$\textbf{WALL}：\inf_{\mathcal K\in\mathfrak K}\theta_{\mathcal K}=\theta_{\rm classical}\ \text{且能证明优化边界} \Longrightarrow \textbf{非常有价值的负结果}$$
$$\textbf{COLLAPSE}：\text{若}\ \theta_{\mathcal K}\ \text{只依赖已知 density estimate 本身，或强度参数可任意重参数化} \Longrightarrow \text{A}_3\ \text{承重量定义}\ \textbf{退化}\Longrightarrow \textbf{关闭}$$

## ⚠️ 措辞纪律（唐先生特别强调）
$$\text{若最终得到经典 barrier，登记的应是}\boxed{\text{给定}\ \mathcal K\text{-类内的定量墙}}，\ \textbf{绝不能} \text{升级成"RH 的普遍墙"}✓$$

## 残余（承接 E6-4，未消）
$$\text{残余 1：体系 B 依赖未逐行核验；残余 2："功能同型／}\operatorname{Core}$"为定义决策；}$$
$$\text{残余 3：}\mathbf{F}\ \text{的具体指数形式为}\ \textbf{[结构判定]}，\ \textbf{未从文献逐式导出}（\text{申-1C 的待办核心）；\ \text{残余 4：余量为史实未量化}$$
$$\text{本档}\ \textbf{不引入候选机制}；\ \textbf{未用 RH}；零数值；\text{未跑 Lean}。$$

## 净产出
$$\text{(i) 申-1A 规范化（}D,t_r,\delta,X=T^\kappa,\ \text{系数归一化与}\ \textbf{系数类登记}）；$$
$$\text{(ii) 申-1B 强度坐标}\ (u,v)\ \text{取代人为}\ \alpha：\mathfrak K=\{(\kappa,u,v)\}\ (\mathcal K\ \text{成立})；$$
$$\text{(iii) 申-1C 骨架：}\theta_{\mathcal K}(\sigma)=\inf_{(\kappa,u,v)\in\mathcal A(\sigma)}F,\ F=u\kappa+v+2c(\sigma)+\mathrm{err}；$$
$$\text{(iv) 申-1D 待办：边界最优判定}\Longrightarrow\text{"可行域向外扩张"的精确表述；}$$
$$\text{(v) 承重量墙}\ =\partial\mathfrak K(\theta_*)\ \text{（偏序可达域）＋三结果登记＋措辞纪律。}$$
