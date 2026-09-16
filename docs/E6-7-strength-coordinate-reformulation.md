# E6-7（戌-2）— **Strength-coordinate reformulation**（坐标层级纠正）

> 唐先生 2026-09-16 18:20 裁定：**戌-2**；定性为**坐标层级纠正**（\textbf{不是"重写 E6-4/E6-5"}）。
> **暂时不做戌-1**（先钉住坐标关系，再回头算 $V$）。

---

## 0. 四行状态（唐先生指定，正式生效）
$$\boxed{\text{"独立承重核"——}\textbf{撤回}}$$
$$\boxed{\text{"large-value strength 是一个可用强度坐标"——}\textbf{保留}}$$
$$\boxed{\text{"它与 density 的强度域是否等价"——}\textbf{OPEN}}$$
$$\boxed{\text{"reachable-domain boundary 是真正的承重量对象"——}\textbf{作为新的工作定义}}$$

## 1. 坐标层级（承重量的数学对象被替换）
$$\textbf{旧叙事}：\mathcal K\longrightarrow\text{density}\longrightarrow\text{更强估计}\quad(\text{仿佛}\ \mathcal K\ \text{是外部输入，density 是其输出})$$
$$\textbf{新层级}：\quad\boxed{\text{analytic strength space}\ \mathfrak K}\quad\text{其中一点}\ q\ \textbf{不是一个定理}，\text{而是一个}\ \textbf{可达到的估计强度}：$$
$$q=(\kappa,\ \mathfrak b,\ \tau,\ \delta,\dots)：\quad\kappa＝\text{Dirichlet 多项式长度；}\mathfrak b＝\text{large-value／mean-value 界；}\ \tau＝\text{系数类；}\ \delta＝\text{分离／间距 regime}$$
$$\text{定义映射}\quad\boxed{\Theta:\mathfrak K\to\mathfrak S_{\rm density}}\quad(\text{把可用强度点映到它能推出的 density exponent})$$
$$\Longrightarrow\ \textbf{承重量不再是某个输入量，而是}：\quad\boxed{\mathfrak K(\theta_*)=\{q\in\mathfrak K:\Theta(q)\le\theta_*\}}$$
$$\qquad\text{其边界}\quad\boxed{\partial\mathfrak K(\theta_*)}\quad\text{才是}\ \textbf{load-bearing frontier}✓$$

## 2. 酉-1X 的正式等级（措辞必须精确）
$$\text{Matomäki--Teräväinen 型结果证明的是：}\ \text{某类 zero-density information}\Longrightarrow\text{某类 large-value information}$$
$$\qquad\text{（与传统方向}\ \text{large-value}\Longrightarrow\text{zero-density}\ \text{并存；唐先生引文 arXiv:2403.13157，本档未重验）}$$
$$\Longrightarrow\ \text{至少存在}\ \boxed{\mathcal D_{\theta}\ \rightleftarrows\ \mathcal K_{\alpha}}\ \text{形式的}\ \textbf{双向关系}$$
$$\textbf{但不能} \text{由此推出}\ \mathcal D_\theta\iff\mathcal K_\alpha\ \text{在}\ \textbf{精确参数、全部系数类、全部}\ \sigma\ \text{范围} \text{上成立}$$
$$\Longrightarrow\ \textbf{E6-6 的正式等级}：\quad\boxed{\text{酉-1X：独立性假设撤回；定量强度坐标关系}\ \textbf{OPEN}}$$
$$\qquad\textbf{而不是}\ \text{"}\mathcal K\ \text{与 density 已证明等价"}✓$$

## 3. E6-4 查 3 的正式撤销与替换
$$\textbf{原论证（撤销）}：\ \mathcal K\ne\text{density}\ \text{因为}\ \textbf{对象不同}\quad\Longrightarrow\ \textbf{DEAD / REVOKED}\ ✗$$
$$\qquad\text{（"陈述对象不同"}\ \textbf{不能} \text{排除定量强度等价 —— 本档确认 E6-6 §酉-1X 的判断）}$$
$$\textbf{替换为}：\quad\boxed{\mathcal K\ \text{与 density 是}\ \textbf{仅为不同表示}，\text{还是具有}\ \textbf{严格不同的强度域}？}$$

## 4. 四个固定任务（唐先生指定）
$$\boxed{\text{X1}\quad \mathcal K\Rightarrow D}\quad(\text{经典方向，具体参数化})$$
$$\boxed{\text{X2}\quad D\Rightarrow\mathcal K}\quad(\text{以 Matomäki--Teräväinen 为入口重新核验})$$
$$\boxed{\text{X3}\quad \text{比较两方向的 exponent loss}}：\ \theta\ \overset{D\to K}{\longmapsto}\ \alpha(\theta)\ \overset{K\to D}{\longmapsto}\ \theta'$$
$$\qquad\textbf{关键}：\text{不是证明}\ \theta'=\theta，\text{而是先确定}\ \boxed{\theta'-\theta}\ \text{是否为零／正／依赖}\ (\sigma,\kappa,\tau)✓$$
$$\boxed{\text{X4}\quad \text{重新定义}\ \mathfrak K(\theta_*)}\ \Longrightarrow\ \mathfrak R(\theta_*)=\{q:\Theta(q)\le\theta_*\}$$

## 5. 墙的定义随之改变（本档核心）
$$\textbf{此前}：\text{"}\mathcal K\ \text{不够强"}\quad\textbf{现在}：\boxed{\text{当前 strength space 的 reachable domain 无法越过某个 density boundary}}$$
$$\text{即}\quad\Theta(\mathfrak K)\subsetneq\mathfrak S_{\rm density}^{\rm target}\quad\Longrightarrow\ \text{墙}\ =\ \boxed{\partial\Theta(\mathfrak K)}$$
$$\qquad\textbf{而不是} \text{某个具体}\ u=u_*,\ v=v_*,\ \lambda=\lambda_*✓$$
$$\Longrightarrow\ \text{与 E5／E6"承重量不是一个 scalar"的判断一致，但}\ \textbf{给出了更严格的数学版本}✓$$

## 6. 校准点登记（A₃ 的起点，**登记为计划，非结果**）
$$\text{Guth--Maynard 提供一个新的前沿点}：\quad\boxed{\mathcal K_{\rm GM}\ \longmapsto\ \theta_{\rm GM}=\tfrac{30}{13}(1-\sigma)+o(1)}$$
$$\qquad\text{（论文将 large-value estimate 与 zero-density estimate 放在同一结果链；唐先生引文 Annals 2026，本档未重验）}$$
$$\text{未来 A}_3\ \textbf{不应} \text{从抽象的}\ (u,v)\ \text{开始}，\text{而应把}\ \textbf{至少三个已知点} \text{放进同一 ledger}：$$
$$\begin{array}{c}\text{classical large-value input}\ \downarrow\ \text{Huxley-type density}\end{array};\quad\begin{array}{c}\text{modern large-value input}\ \downarrow\ \text{Guth--Maynard density}\end{array};\quad\begin{array}{c}\text{known density}\ \downarrow\ \text{large-value estimate}\end{array}$$
$$\text{然后问}：\boxed{\text{这些点是否落在同一个 strength-equivalence class？}}$$
$$\qquad\text{若是} \Longrightarrow \mathcal K\ \text{确实只是 density 的一个}\ \textbf{坐标化表示}；\ \text{若否} \Longrightarrow \textbf{不可逆损失在哪里}？$$

## 7. 为什么现在不做戌-1（唐先生指定）
$$\text{若现在直接算}\ V\ \text{并优化}\ \inf_{\mathcal K}F，\text{则默认了}\ \mathcal K\ \text{是}\ \textbf{独立坐标}；$$
$$\qquad\text{而酉-1X 已表明}\ \mathcal K\leftrightarrow D\ \text{可能存在}\ \textbf{反向转换} \Longrightarrow \text{更正确的是先钉住}\ \mathfrak K\xrightarrow{\Theta}\mathfrak R_{\rm density}，\text{再找}\ \partial\mathfrak R_{\rm density}$$
$$\Longrightarrow\ \text{只有确定该映射的性质后，才有意义讨论}\ V,\kappa,u,v,\eta\ \text{究竟是}\ \textbf{哪一个方向} \text{上的真正限制}✓$$

## 8. 边界与残余
$$\text{① 本档为}\ \textbf{坐标层级纠正}，\ \textbf{不是新定理}；\quad\text{② MT／GM 引文}\ \textbf{未逐行重验}；$$
$$\text{③ }q\ \text{的分量选取（}\kappa,\mathfrak b,\tau,\delta\text{）为}\ \textbf{定义决策}（\text{可修订}）；\quad\text{④ 残余 1--4 未消}；$$
$$\text{⑤ }\textbf{未用 RH}；零数值；\text{未跑 Lean}；\ \text{不引入候选机制}。}$$

## 9. 净产出
$$\text{(i) 承重量对象替换：}\mathfrak K\to\mathfrak R_{\rm density}\ \text{的}\ \textbf{可达域}\ \partial\mathfrak K(\theta_*)；$$
$$\text{(ii) 酉-1X 正式等级：独立性假设}\ \textbf{撤回}；定量强度坐标关系}\ \textbf{OPEN}（\textbf{不得} \text{写成"已证等价"}）；$$
$$\text{(iii) E6-4 查 3 的"对象不同"论证}\ \textbf{正式撤销}；$$
$$\text{(iv) X1--X4 四任务固定（X3 的关键量＝}\theta'-\theta\ \text{的符号／依赖性）；}$$
$$\text{(v) 墙的定义改为}\ \partial\Theta(\mathfrak K)；\ \text{＋校准点 ledger 计划（Huxley／GM／反向）。}$$

---

## 【勘误 T10】（2026-09-16 18:21，唐先生指出；正文不修改，勘误留档）
$$\textbf{原（§6）}：\ \mathcal K_{\rm GM}\ \longmapsto\ \theta_{\rm GM}=\tfrac{30}{13}(1-\sigma)+o(1)\ \text{易被误读为}\ \mathcal K\ \text{自身的坐标值}$$
$$\textbf{更正}：\boxed{q_{\rm GM}\ \xrightarrow{\ \Theta\ }\ \theta_{\rm GM}(\sigma)=\tfrac{30}{13}(1-\sigma)+o(1)}$$
$$\qquad\tfrac{30}{13}(1-\sigma)\ \text{是}\ \textbf{density exponent（}\Theta\ \text{的输出）}，\ \textbf{不得} \text{混入}\ q=(\kappa,\mathfrak b,\tau,\delta,\dots)；$$
$$\qquad\text{理由：GM 的贡献为 large-value bounds}\to\text{zero-density estimate} \Longrightarrow \text{其输出是}\ \theta\ \text{而非坐标。}$$
$$\textbf{详据}：\text{E6-8（X2 定量反向 strength map 审计）§3。}$$
