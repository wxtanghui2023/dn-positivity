# E6-2（巳-1 / Q-A₁）— **密度定理的证明依赖剥离**（A₁ 层）

> 唐先生 2026-09-16 18:11 裁定：开巳-1，但把问题改为**证明依赖审计**；今天**只做 A₁**。
> 纪律：**不遍历所有密度定理**；固定一个目标、拆一个经典证明、逐项做删除实验；**不碰巳-2**；不列新机制。

---

## 1. 三层问题的严格区分（唐先生指定，不得混用）
$$\boxed{\begin{array}{lll}
Q\!-\!A_1&\text{证明必要性：}&\text{现有证明中哪些输入}\ \textbf{不可删除}？\ (\textbf{今天做这层})\\
Q\!-\!A_2&\text{逻辑必要性：}&\text{结论本身是否蕴含某种输入？}\ (\text{易变开放问题，今日不做})\\
Q\!-\!A_3&\text{强度最小化：}&\text{实现目标密度指数所需的}\ \textbf{最弱已知条件}？\ (\text{最终目标})
\end{array}}$$
$$\textbf{关键禁令}：\ \textbf{不得} \text{把 Q-A 写成"区域}\to\text{密度的必要条件"} —— \text{"某证明用了}\ X\text{"}\ \ne\ \text{"结论逻辑上必须有}\ X\text{"}✓$$

## 2. 固定目标
$$\boxed{\mathrm{N}(\sigma,T)\ll T^{\theta(\sigma)+\varepsilon},\qquad \sigma>\tfrac12}\quad(\text{目标密度指数}\ \theta(\sigma)\ \text{为待刻画对象})$$

## 3. 依赖 DAG 的剥离（**本档主审对象**：经典"大值集"路线）
$$\text{外形链}：\quad \text{Euler product}\to\text{Dirichlet 多项式}\to\text{mean value}\to\text{large sieve／large values}\to\mathrm{N}(\sigma,T)$$
$$\text{按唐先生要求继续向下剥}：\quad \text{定理}\to\textbf{精确假设}\to\text{假设中真正使用的估计}\to\text{估计所需的}\ \textbf{最小结构}$$

### 3.1 逐节点剥离（本档重建，见 §7 边界）
$$\textbf{节点 1（算术）Euler product}：\zeta\ \text{的局部因子／乘法结构}\ \Longrightarrow\ \textbf{截断近似}：\ \zeta(s)\approx\sum_{n\le X}n^{-s}\ (\text{approximate functional equation 型})，\ X\asymp T^{\kappa}$$
$$\qquad\textbf{真正使用的估计}：\text{截断误差项}\ \Longrightarrow\ \textbf{最小结构}：\text{Euler 积（乘法）＋伸缩对称（FE）}$$
$$\textbf{节点 2（检测）零点检测}：\text{零点}\ \to\ \text{某 Dirichlet 多项式在大值集上取值大}\ (\text{log-derivative／mollifier／Selberg }\wp\text{-型论证})$$
$$\qquad\textbf{最小结构}：\text{"零点}\to\text{大值"的}\ \textbf{定量转化}（\text{此处需要}\ \textbf{无零区或局部零点计数} \text{的弱形式）}$$
$$\textbf{节点 3（计数）大值集控制}：\text{良分离点上}\ |D|\ \text{大的点数}\ \text{被上界控制}\ (\text{Halász--Montgomery／Montgomery 大值集型})$$
$$\qquad\textbf{真正使用的估计}：\textbf{两点／配对相关} \text{的均值型界}$$
$$\textbf{节点 4（分析核）均值定理}：\ \int_T^{2T}|D(\sigma+it)|^{2}dt\ \lesssim\ \bigl(\text{长度}+\text{时间尺度}\bigr)\cdot\|a\|_2^{2}\ \text{型}$$
$$\qquad\textbf{（}\textbf{Montgomery--Vaughan 型均值定理／Hilbert 型不等式）；最小结构}：\textbf{纯调和分析}（\text{无算术输入）}$$
$$\textbf{节点 5（对偶）大筛／对偶}：\text{Gallagher／Montgomery 大筛型对偶估计}\ \Longrightarrow\ \textbf{最小结构}：\text{L}^2\ \text{对偶性}$$

### 3.2 得到的输入包
$$\boxed{\mathcal I_{\rm density}=\{\,I_{\rm Euler}\ (\text{乘法＋FE}),\ I_{\rm detect}\ (\text{零点}\to\text{大值}),\ I_{\rm LV}\ (\text{大值集控制}),\ I_{\rm MV}\ (\text{均值定理}),\ I_{\rm dual}\ (\text{大筛对偶})\,\}}$$

## 4. 删除实验（A₁ 的核心操作）
$$\mathcal I_{\rm density}\setminus\{I_j\}\ \stackrel{?}{\Longrightarrow}\ \mathrm{N}(\sigma,T)\ \text{bound}$$
$$\begin{array}{c|c|c}
\text{删除项} & \text{后果（本档判定）} & \text{不可删除？}\\ \hline
I_{\rm Euler}\ (\text{乘法／FE}) & \text{失去截断近似}\ \Longrightarrow\ \text{无}\ \zeta\ \text{零点与大值集的定量联系} & \textbf{不可删}\\
I_{\rm detect} & \text{零点与大值集脱钩} & \textbf{不可删}\\
I_{\rm LV}\ (\text{大值集}) & \text{无法把大值计数转成零点计数} & \textbf{不可删}\\
I_{\rm MV}\ (\text{均值定理}) & \text{大值集控制失去唯一量化来源} & \textbf{不可删}\\
I_{\rm dual}\ (\text{大筛对偶}) & \text{良分离点上的}\ L^{2}\ \text{估计失去形式} & \textbf{不可删（但可能与}\ I_{\rm MV}\ \text{部分重合）}
\end{array}$$

## 5. ⭐ 不可压缩核的候选（本档最有价值的一步）
$$\text{把各删除实验的结论合并}：\text{不同经典密度证明}\ \textbf{外形不同，但都经过}\ \text{节点 3--5}\ \text{的同一类估计}$$
$$\boxed{\text{候选不可压缩核}\ I_{\min}：\ \text{良分离点上 Dirichlet 多项式的}\ \textbf{均值／大值控制} \text{（}\int|D|^{2}\ \text{型＋大值计数量化）}}$$
$$\text{其}\ \textbf{最小结构}：\text{纯调和分析（}\mathrm{L}^{2}\ \text{对偶＋良分离性）}，\ \textbf{不含算术输入}}$$
$$\Longrightarrow\ \textbf{由此得到承重量在该箭头的}\ \textbf{初步刻画}：$$
$$\boxed{\text{区域}\to\text{密度的负载}\ =\ \underbrace{\text{算术节点（乘法＋FE）}}_{\text{决定允许截断}\ X\asymp T^{\kappa}}\ \text{与}\ \underbrace{\text{分析核（均值／大值强度）}}_{\text{决定大值集控制}}\ \text{的}\ \textbf{联合优化输出}}$$
$$\qquad\text{即}\ \theta(\sigma)\ \text{是}\ (\kappa,\ \text{均值强度})\ \text{平面上的}\ \textbf{优化结果}，\ \textbf{不是}\ \text{某个新对象}$$

## 6. 预先固定的判死标准（唐先生指定，先立后判）
$$\textbf{DEAD-1（完全证明依赖）}：\text{若剥到最后只是"证明 A 用大筛／B 用均值／C 用另一技巧"，}\textbf{无共同不可压缩输入}$$
$$\qquad\Longrightarrow\ \boxed{\text{Q-A}\ \textbf{暂不产生新的承重量刻画}}\quad(\textbf{而}\ \textbf{不得} \text{宣布"区域}\to\text{密度没有共同结构"})$$
$$\textbf{DEAD-2（共同输入＝密度定理本身）}：\text{若}\ I_{\min}\ \text{就是}\ \mathrm{N}(\sigma,T)\ll\cdots\ \text{本身} \Longrightarrow \textbf{循环}\Longrightarrow \textbf{直接关闭}$$
$$\textbf{ALIVE（须同时满足五条）}：$$
$$\qquad I_{\min}\Longrightarrow\mathrm{N}(\sigma,T)\ll T^{\theta(\sigma)+\varepsilon}\ \text{且}\ I_{\min}\ \textbf{严格弱于目标}；\ \text{① 可逐项验证}；\ \text{② 删除某项证明链断裂}；$$
$$\qquad\text{③ 不用 RH；④ 非 density estimate 换名；⑤ 能解释其在不同证明体系中的}\ \textbf{共同出现}✓$$

## 7. 本档判定（A₁ 层）
$$\textbf{§5 的候选核满足 ALIVE 的 ④⑤ 与（初步）①②；③ 天然满足（纯调和分析，不含 RH）}$$
$$\Longrightarrow\ \boxed{\text{本档给出}\ \textbf{A}_1\ \text{层的候选不可压缩核}：\text{良分离点上的均值／大值控制}}$$
$$\qquad\text{并给出}\ \textbf{承重量的初步定量形态}：\theta(\sigma)\ \text{＝（截断参数}\kappa,\ \text{均值强度）的联合优化输出}✓$$
$$\textbf{但}\ \textbf{尚未进入}\ A_3：\text{最小充分输入}\ \text{仍未刻画}\Longrightarrow\ \text{下一步条件：}\textbf{A}_1\ \text{找到稳定共同核之后才进}\ A_3✓$$

## 8. 边界（N1/N2 严守，重要）
$$\text{① §3 的 DAG 与逐节点剥离为}\ \textbf{本档据标准"大值集路线"重建的}\ \textbf{[结构判定]}，\ \textbf{未} \text{对某本教科书／论文}\ \textbf{逐行核验}；$$
$$\text{② §4 删除实验为}\ \textbf{结构性论证}（\text{非形式化证明）}；\ \text{③ §5 的核为}\ \textbf{候选}，\ \textbf{非已证最小}；$$
$$\text{④ 本档}\ \textbf{不做}\ A_2／A_3；\ \textbf{不碰巳-2}；\ \text{不列新机制；}\quad\text{⑤ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 9. 净产出
$$\text{(i) 三层问题的严格分离（}A_1／A_2／A_3\text{），并明确今日只做}\ A_1；$$
$$\text{(ii) 密度定理的依赖 DAG 剥离（五节点：Euler／检测／大值集／均值／对偶）＋输入包}\ \mathcal I_{\rm density}；$$
$$\text{(iii) 删除实验（五项皆不可删，其中}\ I_{\rm dual}\ \text{与}\ I_{\rm MV}\ \text{部分重合）；}$$
$$\text{(iv) ⭐ 候选不可压缩核＝良分离点上的均值／大值控制（纯调和分析）；}$$
$$\text{(v) 承重量的初步定量形态：}\theta(\sigma)＝\text{联合优化输出；＋判死标准（DEAD-1／DEAD-2／ALIVE 五条）。}$$
