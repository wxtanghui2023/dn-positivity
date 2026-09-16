# E6-6（酉-1）— **指数账本逐式重建**（酉-1A→1D）＋ **反向蕴含检查**（酉-1X）

> 唐先生 2026-09-16 18:18 裁定：**酉-1**；**不先信 E6-5 的** $F=u\kappa+v+2c(\sigma)+\mathrm{err}$，**须从具体零点检测链逐式重建**。
> 五步未完成前：**不做申-1D 优化**（风险不是算错指数，而是优化了一个尚未证明正确的"承重坐标"）。

---

## 0. 四个可能漏指数的位置（唐先生指定，作为审计清单）
$$\boxed{\begin{array}{ll}
(1)&D\ \text{的实际阈值是否真为}\ V\\
(2)&D\ \text{是否经}\ n^{-\sigma}\ \text{加权，从而改变}\ u\\
(3)&\text{零点检测是否引入额外}\ X,T,\sigma\ \text{因子}\\
(4)&R\to\mathrm{N}(\sigma,T)\ \text{是否一一对应（或有分块／重叠损失）}
\end{array}}$$

## 酉-1A：零点检测（**必须算出 $V$，不得预设 $V=T^{-c(\sigma)}$**）
$$\text{起点}：\rho=\beta+i\gamma,\ \beta\ge\sigma；\ \text{构造}\ D_\rho(s)=\sum_{n\le X}a_n(\rho)n^{-s}$$
$$\text{须严格得到的形状}：\quad|\zeta(\rho)|=0\ \Longrightarrow\ |D_\rho(\rho)|\ \ge\ V(\sigma,T,X)$$
$$\textbf{本档判定}：\ V\ \text{的}\ \textbf{实际指数} \text{必须由}\ \textbf{截断式}\ \text{与}\ \textbf{1/}\zeta\ \text{的近似逆} \text{共同算出}$$
$$\qquad\text{（}\text{经典路线：}\zeta\ \text{的截断展式＋}\ 1/\zeta\ \text{的}\ \mu\text{-型截断；二者在}\ \rho\ \text{处取值的反向估计}）$$
$$\qquad\Longrightarrow\ \textbf{未算出}\ V\ \text{之前，}\ 2c(\sigma)\ \text{这个项}\ \textbf{不得} \text{进入}\ F\ ✗$$
$$\textbf{残余}：V\ \text{的具体指数依赖}\ \textbf{截断式在}\ \sigma\ \text{区的有效范围}\ \text{与}\ \text{近似逆的误差阶} \Longrightarrow\ \textbf{须文献逐式核验}（\text{残余 1）}$$
$$\textbf{对应清单项}：\ (1)\ \text{与}\ (3)\ \textbf{未决}$$

## 酉-1B：良分离与计数损失（**纠正 E6-4 查 4(a) 的粗糙表述**）
$$\text{E6-4 查 4(a) 写的是"零点自动良分离（间隔}\gg1/\log T\text{）"——}\textbf{该表述过强，本档纠正}：$$
$$\qquad\textbf{零点不是一般意义上的简单、均匀间隔点集}；\ \text{零点检测证明通常}\ \textbf{先组织／选择适当的点子集}✓$$
$$\text{须证明的两种可能损失形式}：$$
$$\boxed{\mathrm{N}(\sigma,T)\ \le\ C(\log T)^{A}R\qquad\text{或}\qquad \mathrm{N}(\sigma,T)\ \le\ T^{\eta}R}$$
$$\textbf{对最终}\ F\ \text{的影响}：\text{若损失为}\ (\log T)^{A}\ \text{型} \Longrightarrow \text{只贡献}\ T^{\varepsilon}；\ \text{若为}\ T^{\eta}\ \text{型} \Longrightarrow \text{贡献}\ \textbf{实的幂次}\ \eta\ \text{（改变}\ \theta）$$

## 酉-1C：$\mathcal K$ 插入（**含归一化与系数类的关键修正**）
$$R\,V^{2}\ \le\ \sum_{r=1}^{R}|D(\rho_r)|^{2}\ \le\ B(X,T,\sigma)\ \Longrightarrow\ R\ \le\ B/V^{2}$$
$$\textbf{修正（清单项 (2)）}：D(\rho)=\sum_{n\le X}a_n n^{-\sigma-i\gamma}\ \text{已含}\ n^{-\sigma}\ \text{加权} \Longrightarrow\ \text{估计的}\ (u,v)\ \text{是对}\ \textbf{加权后} \text{多项式而言的}$$
$$\qquad\text{而实际系数带}\ n^{-\sigma},\ \Lambda(n),\ \mu(n),\ \text{平滑权} \Longrightarrow\ \textbf{不能用任意单位}\ \ell^{2}\ \text{系数向量}；$$
$$\qquad\boxed{\text{归一化必须适配加权系数}（\text{如}\ \sum|a_n|^{2}n^{-2\sigma}=1\ \text{或}\ \Lambda^{2}\ \text{型范数）} \Longrightarrow\ (u,v)\ \textbf{依赖系数类}}$$
$$\Longrightarrow\ \text{强度坐标应为}\ \boxed{(\kappa,\ u,\ v,\ \tau)}\quad(\tau：＝\text{系数类})\ \text{——}\ \textbf{E6-5 的}\ (u,v)\ \text{不独立于}\ \tau✓$$

## 酉-1D：真实 $F$（**账本形式，取代预设公式**）
$$\boxed{\theta_{\mathcal K}(\sigma)=\inf_{\mathcal A(\sigma)}\Bigl[\underbrace{\text{核强度指数}}_{\mathcal K}\ +\ \underbrace{\text{检测阈值指数}}_{\text{zero detection}}\ +\ \underbrace{\text{截断／分块损失}}_{\text{error}}\Bigr]}$$
$$\textbf{与 E6-5 的关系}：\text{E6-5 的}\ F=u\kappa+v+2c(\sigma)+\mathrm{err}\ \textbf{恰是本账本在}\ \text{(a)}\ V=T^{-c}\ \text{(b) 损失仅}\ (\log T)^{A}\ \text{(c) 一一对应}\ \text{三项假设下的特例}$$
$$\qquad\Longrightarrow\ \textbf{若逐式核验后确实得到 E6-5 的形状，那才是很强的确认}；\ \textbf{本档不预设}✓$$

## ⭐ 酉-1X：反向蕴含检查（唐先生本轮新增，优先级高于残余 1）
$$\textbf{问题}：\text{是否存在}\quad \text{density}(\theta)\ \Longrightarrow\ \mathcal K_{\alpha(\theta)}\quad\textbf{（反向蕴含）}?$$
$$\textbf{文献依据（唐先生引文，本档未重验）}：\text{已有专门工作研究"zero-density results}\ \textbf{implying}\ \text{large value estimates"（arXiv:2403.13157）}$$
$$\qquad\text{且 Guth--Maynard（Annals 2026）改进的正是"Dirichlet polynomial 在大值附近出现的频率"，从而得到}\ \mathrm{N}(\sigma,T)\le T^{30(1-\sigma)/13+o(1)}$$
$$\Longrightarrow\ \textbf{判定}：\ \text{"density}\leftrightarrow\text{large-value control"}\ \text{在某个强度层面}\ \textbf{可能已形成近似双向对应}$$
$$\qquad\boxed{\text{故 E6-4 查 3 的"}\mathcal K\ \textbf{严格弱于}\ \text{density}"\ \textbf{须重新分级}}：$$
$$\qquad\qquad\text{由"}\textbf{独立承重核}"\ \textbf{降为}\ \textbf{"近等价强度坐标"}（\text{陈述对象不同}\ \textbf{不能} \text{排除定量强度等价）}$$
$$\qquad\textbf{注意}：\ \textbf{不是 DEAD}，\text{但}\ \text{"独立输入"这一层叙事}\ \textbf{必须撤回/降级}}✓$$

## 三结果与纪律
$$\text{ALIVE-strong（}\theta\ \text{可显式计算＋非平凡边界）／WALL（}\inf\theta=\theta_{\rm classical}\ \text{＋优化边界）／COLLAPSE（退化）}$$
$$\textbf{措辞纪律}：\text{若得经典 barrier，只登记"给定}\ \mathcal K\text{-类内的定量墙"，}\ \textbf{绝不} \text{升级为"RH 的普遍墙"}✓$$
$$\textbf{残余}：\text{残余 1（未逐行核验）、残余 2（定义决策）、残余 3（}\textbf{本档已部分处理}：F\ \text{改为账本形式，2c 与}\ \eta\ \text{项待算）、残余 4（余量未量化）}$$
$$\textbf{本档}\ \textbf{未用 RH}；零数值；\text{未跑 Lean}；\ \text{不引入候选机制}。$$

## 净产出
$$\text{(i) 酉-1A：}V\ \text{必须算出，}\ 2c(\sigma)\ \text{不得预设进入}\ F（\text{清单项 1／3 未决）}；$$
$$\text{(ii) 酉-1B：}\textbf{纠正 E6-4 查 4(a)}\（\text{零点非均匀间隔，须先选择子集；损失为}\ (\log T)^{A}\ \text{或}\ T^{\eta}）；$$
$$\text{(iii) 酉-1C：}\textbf{关键修正}——\ \text{归一化须适配加权系数} \Longrightarrow\ \text{强度坐标为}\ (\kappa,u,v,\tau)，\textbf{E6-5 的}\ (u,v)\ \text{不独立于系数类；}$$
$$\text{(iv) 酉-1D：}F\ \text{改写为}\ \textbf{账本形式}；\text{E6-5 形式}\ \textbf{仅为三项假设下的特例}；$$
$$\text{(v) ⭐ 酉-1X：反向蕴含存在（文献依据）}\Longrightarrow \text{E6-4 查 3 的"严格弱于"}\ \textbf{降级} \text{为"近等价强度坐标"。}$$
