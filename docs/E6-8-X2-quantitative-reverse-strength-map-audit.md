# E6-8（亥-2 / X2）— **定量反向 strength map 审计**

> 唐先生 2026-09-16 18:21 裁定：**亥-2：开 X2**，做成**定量反向 strength map 审计**（非泛泛重验 MT）。
> 本轮唯一任务：**把 $\alpha(\theta)$ 真正从文献的蕴含关系中抽出来**；**不优化、不算 $V$、不预设 $\theta'-\theta$ 符号**。

---

## 0. 文献入口的精确陈述（**本轮新取证**）
$$\textbf{来源}：\text{arXiv:2403.13157v1（16 页；2024-03-19；Teräväinen 提交）——}\textbf{外部来源，本档仅作数据引用}✓$$
$$\textbf{摘要原文（关键句）}：\text{"It is well known that estimates of the latter type imply estimates of the former type.}$$
$$\qquad\text{Our goal is to show that there is an implication to the other direction as well, i.e.}\ \textbf{zero density estimates for the Riemann zeta function imply large value estimates for Dirichlet polynomials}\text{."}$$
$$\Longrightarrow\ \textbf{方向确认}：\ \boxed{\text{zero density}\ \Longrightarrow\ \text{large value for Dirichlet polynomials}}\ \text{（与传统方向并存）}✓$$
$$\textbf{同时确认（重要）}：\text{反向映射的}\ \textbf{目标对象类型} \text{恰为}\ \textbf{"Dirichlet 多项式的 large value estimate"}\ ——\ \text{与}\ \mathfrak K\ \text{的}\ \textbf{对象类型相同}✓$$

## 1. 第一关：$\alpha(\theta)$ 的**数据槽**（须逐项取得的清单）
$$\text{要把}\ D(\theta)\Longrightarrow K(\alpha,\tau,\sigma,X,T,\delta)\ \text{真正参数化，须逐式取得以下七项}：$$
$$\begin{array}{ll}(1)&\text{density hypothesis 的}\ \textbf{具体形式}（\text{是否}\ \mathrm{N}(\sigma,T)\ll T^{\theta(1-\sigma)+\varepsilon}\ \text{型）\\(2)&\text{large-value estimate 所控制的}\ \textbf{具体量}（\text{良分离点上的计数？加权计数？}\\(3)&D(s)=\sum a_n n^{-s}\ \text{的}\ \textbf{系数限制}\ (\tau)\\(4)&X\ \text{的}\ \textbf{允许范围}\ (\kappa)\\(5)&V／\text{阈值范围}\\(6)&t_r\ \text{的}\ \textbf{spacing 条件}\ (\delta)\\(7)&\text{最终}\ \theta\to\alpha\ \text{的}\ \textbf{指数变换}\end{array}$$
$$\textbf{本轮状态}：\ \text{摘要层}\ \textbf{已确认方向与对象类型}；\ \textbf{七项定量数据}\ \textbf{均未取得} \Longrightarrow\ \boxed{\alpha(\theta)\ \textbf{本轮未抽出}}$$
$$\qquad\textbf{须取处}：\text{正文 16 页（HTML 版：}\texttt{arxiv.org/html/2403.13157v1}\text{）}\ \Longrightarrow\ \text{下一步的}\ \textbf{精确任务已登记}✓$$

## 2. 第二关：反向映射是否落在**同一个** $\mathfrak K$
$$\text{问题}：K_{\rm MT}\ \text{是否}\ \in\ \mathfrak K=\{(\kappa,\mathfrak b,\tau,\delta,\dots)\}\ \text{（E6-7 定义）}$$
$$\textbf{对象层判定（本轮可得）}：\ \text{摘要明确目标为"large value estimates for Dirichlet polynomials"} \Longrightarrow\ \textbf{对象层同在}\ ✓$$
$$\textbf{参数层判定}：\ \text{若}\ K_{\rm MT}\ \text{使用}\ \textbf{不同系数类／不同}\ X\ \text{范围／不同 spacing／不同权函数} \Longrightarrow \textbf{不能直接记作}\ q(\theta)\in\mathfrak K$$
$$\qquad\Longrightarrow\ \text{X2 的两种可能结果（须在取得七项数据后判定）}：$$
$$\qquad\boxed{\text{(甲) 同一 strength space 内的}\ \textbf{反向坐标}}\qquad\text{或}\qquad\boxed{\text{(乙) 两个不同 strength space 之间的}\ \textbf{映射}}$$
$$\qquad\textbf{唐先生判断（本档采纳）}：\textbf{(乙) 反而更重要}✓$$
$$\textbf{本轮落点}：\text{对象层＝(甲) 倾向；参数层＝}\textbf{OPEN}（\text{七项未取）}$$

## 3. 档案纠正（唐先生指出，立即生效）
$$\textbf{原（E6-7 §6）}：\ \mathcal K_{\rm GM}\mapsto\theta_{\rm GM}=\tfrac{30}{13}(1-\sigma)+o(1)\ \text{易被误读为}\ \mathcal K\ \text{的坐标值}$$
$$\textbf{更正}：\ \boxed{q_{\rm GM}\ \xrightarrow{\ \Theta\ }\ \theta_{\rm GM}(\sigma)=\tfrac{30}{13}(1-\sigma)+o(1)}$$
$$\qquad\textbf{即}：\tfrac{30}{13}(1-\sigma)\ \text{是}\ \textbf{density exponent（}\Theta\ \text{的输出）}，\ \textbf{不得} \text{混入}\ q=(\kappa,\mathfrak b,\tau,\delta,\dots)\ ✓$$
$$\qquad\text{理由}：\text{GM 的贡献是}\ \text{large-value bounds}\to\text{zero-density estimate} \Longrightarrow \text{其输出是}\ \theta，\text{非坐标}$$

## 4. X3 的三种结果（预先登记，**不预设符号**）
$$\text{定义}\ \Delta(\theta,\sigma,\tau,\dots)：＝\theta'-\theta，\ \text{其中}\ \theta\ \xrightarrow{D\to K}\ \alpha(\theta)\ \xrightarrow{K\to D}\ \theta'$$
$$\textbf{A 零损失}\ \theta'=\theta：\text{则在相应参数区域内}\ \boxed{D\sim K}\ \text{为强度坐标等价，}\ \textbf{非独立承重机制} \Longrightarrow \text{E6 的 load-bearing frontier 转为}\ \textbf{reachable-domain geometry}$$
$$\textbf{B 严格正损失}\ \theta'>\theta：\ \textbf{出现真正的不可逆定量损失}；\ \text{此时"承重量"重新获得实质内容，}\ \textbf{但属于映射损失，而非}\ \mathcal K\ \text{本身}$$
$$\textbf{C 参数依赖}\ \Delta=L(\sigma,\kappa,\tau,\delta,\dots)：$$
$$\qquad\textbf{唐先生警告（本档采纳）}：\text{large-value estimates 的强度}\ \textbf{高度依赖长度、阈值与系数结构}；$$
$$\qquad\qquad\text{GM 的改进针对}\ \textbf{特定 large-value regime}（\text{长度}\ N\ \text{与大值规模接近}\ N^{3/4}\ \text{的临界区域）\Longrightarrow\ \textbf{不能} \text{把局部 exponent correspondence 外推成整个}\ \mathfrak K\ \text{的等价}✓$$

## 5. 边界（N1/N2 严守）
$$\text{① 本轮}\ \textbf{仅取得摘要层陈述}（\text{外部来源，仅作数据）；\ \textbf{七项定量数据未取} \Longrightarrow \alpha(\theta)\ \textbf{未抽出}；$$
$$\text{② 本档}\ \textbf{不优化、不算}\ V、\textbf{不预设}\ \Delta\ \text{符号}；\quad\text{③ MT／GM 的}\ \textbf{正文细节未核验}；$$
$$\text{④ 残余 1--4 未消}；\quad\text{⑤ }\textbf{未用 RH}；零数值；\text{未跑 Lean}；\ \text{不引入候选机制}。}$$

## 6. 净产出
$$\text{(i) 文献入口}\ \textbf{精确取证}：\text{方向确认（zero density}\Rightarrow\text{large value for Dirichlet polynomials）＋}\ \textbf{对象类型与}\ \mathfrak K\ \text{相同}；$$
$$\text{(ii) 七项数据槽清单（}\alpha(\theta)\ \text{的抽取规格）＋本轮未抽出的明示；}$$
$$\text{(iii) 第二关落点：对象层倾向(甲)，参数层 OPEN（(乙) 若成立更重要）；}$$
$$\text{(iv) 档案纠正：}q_{\rm GM}\xrightarrow{\Theta}\theta_{\rm GM}(\sigma)\ \text{的写法（坐标与映射输出分离）；}$$
$$\text{(v) X3 三结果预登记＋GM"局部 regime 不可外推"警告。}$$
