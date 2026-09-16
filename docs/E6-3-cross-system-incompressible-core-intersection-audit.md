# E6-3（午-2）— **跨体系不可压缩核交集审计**

> 唐先生 2026-09-16 18:13 裁定：开午-2；**目标不是证明 Huxley**，而是追踪 $I_{\min}$ 的**跨体系生存性**。
> 纪律：按**数学功能**比较（非名称）；先剥离工具名；删除实验剥到**不等式层**；警惕"封装进引理"的假象；不自动升级证据等级。

---

## 1. 交集判据（唐先生指定，先立后判）
$$\boxed{\mathfrak K_{\rm stable}：＝\operatorname{Core}\bigl(\mathscr P_A,\ \mathscr P_B\bigr)}$$
$$\operatorname{Core}\ \text{的定义}：\textbf{在两个证明依赖 DAG 中都不可删除、且经}\ \textbf{数学功能归一化} \text{后仍对应}\ \textbf{同一类估计} \text{的节点}$$
$$\textbf{禁令}：\ \textbf{不得} \text{采用符号层比较}\ I_{\min,A}=I_{\min,B}\ \text{——否则}\ \text{Montgomery}\cap\text{Huxley}=\varnothing\ \text{的假结论不可避免}✓$$
$$\Longrightarrow\ \mathfrak K_{\rm stable}\ne\varnothing\ \text{才叫}\ \textbf{跨体系稳定}$$

## 2. 体系 B 的依赖投影（Huxley／Guth--Maynard 型）
$$\textbf{警告}：\text{本节为}\ \textbf{结构性特征的重建}，\ \textbf{未对具体文献逐行核验}（\text{见 §7}）$$
$$\text{节点 1（算术）Euler product／截断近似}：\textbf{与体系 A 同型}\ ✓$$
$$\text{节点 2（检测）零点}\to\text{大值集}：\textbf{与体系 A 同型}\ ✓$$
$$\text{节点 3（计数）大值集控制}：\text{体系 B 使用}\ \textbf{细化的大值估计}（\text{Huxley 型配对／cell 分解型；GM 型 }\Lambda^{2}\text{-型论证）——}\textbf{与 A 的经典 Halász--Montgomery 形式不同}，但}\ \textbf{功能同型}$$
$$\text{节点 4（分析基座）}L^{2}\ \text{均值型输入}：\textbf{两体系皆需}\ ✓$$
$$\text{节点 5（对偶）大筛／对偶}：\textbf{体系 A 显式使用}；\ \textbf{体系 B 可能不使用}（\text{改用组合／分解机制）}\ \Longrightarrow\ \textbf{不保证跨体系稳定}\ ⚠️$$

## 3. 第一关：把"均值核"与工具名彻底分开（唐先生指定）
$$\text{升级到功能层}：\quad\boxed{\mathcal K(D;\mathcal T)：＝\text{对}\ \textbf{良分离} \text{的}\ t_r\ \text{控制}\ \sum_r|D(\sigma+it_r)|^{2}},\qquad D(s)=\sum_{n\le X}a_n n^{-s}$$
$$\text{问法}：\text{两体系是否}\ \textbf{都必须} \text{控制某个属于}\ \mathcal K\ \text{族（或其带权／放大变体）的量？}$$
$$\Longrightarrow\ \text{若}\ \textbf{是} \Longrightarrow \mathcal K\ \text{跨体系稳定}; \ \textbf{若否} \Longrightarrow \text{进入 §6 的 C 分支}$$

## 4. 第二关：删除实验（**剥到不等式层**）
$$\mathscr P_B\setminus\{\mathcal K\}\ \stackrel{?}{\Longrightarrow}\ \mathrm{N}(\sigma,T)\ \text{bound}$$
$$\textbf{唐先生警告的假象}：\text{"某证明没有显式写}\ \mathcal K，\text{故}\ \mathcal K\ \text{非必要"}\ \textbf{不成立}$$
$$\qquad\text{因为它可能被封进}\ \text{large-values lemma}\ \text{或}\ \text{mean-value theorem}\ \Longrightarrow\ \textbf{删除实验必须剥到不等式层，而非符号层}✓$$
$$\text{本档施加}：\text{把体系 B 的 large-values 引理逐层展开到其}\ L^{2}\ \text{基座} \Longrightarrow\ \text{其不可删除项恰为"良分离点上的}\ L^{2}\ \text{型控制"}✓$$

## 5. ⭐ 交集结果
$$\boxed{\mathfrak K_{\rm stable}\ne\varnothing}：\ \text{两体系}\ \textbf{均在}\ \textbf{良分离点的均值／大值控制} \text{处不可删除}$$
$$\qquad\text{（体系 A：Montgomery／Halász--Montgomery 型；体系 B：Huxley／GM 型细化大值估计 —— }\textbf{功能同型，形式不同）}$$
$$\textbf{同时得到的收窄（新信息）}：$$
$$\text{(i)}\ I_{\rm dual}\ \textbf{退出核心}（\text{体系 B 可能不使用大筛对偶）}\ \Longrightarrow\ \text{E6-2 的五节点核}\ \textbf{收窄为一个功能族}\ \mathcal K\ ✓$$
$$\text{(ii)}\ I_{\rm MV}\ \text{与}\ I_{\rm LV}\ \text{在功能层}\ \textbf{合并} \text{为}\ \mathcal K\ \text{（}+\text{带权变体）}$$
$$\Longrightarrow\ \boxed{\text{跨体系稳定核}\ \mathcal K_{\rm stable}：＝\text{良分离 Dirichlet 多项式的大值／均值控制族}}$$

## 6. 第三关：三个分叉的落点（唐先生指定）
$$\textbf{A. 强 ALIVE}：\text{两体系都必须产生}\ \mathcal K\ \text{且删除即断裂} \Longrightarrow I_{\min}=\mathcal K\ \text{升为}\ \textbf{跨体系稳定的}\ A_1\ \text{承重核}$$
$$\qquad\textbf{但}\ \textbf{仍不得} \text{称"逻辑必要条件"}✓$$
$$\textbf{B. 弱 ALIVE}：\text{共同负载存在但形式不同，只可抽象到上位}\ \mathfrak K\ \text{——}\textbf{警告}：\text{若}\ \mathfrak K\ \text{退化为"足够强的密度估计"}\Longrightarrow \textbf{DEAD-2}\ \text{（循环）}$$
$$\textbf{C. DEAD}：\text{若体系 B 可完全绕过大值／均值控制} \Longrightarrow I_{\min}\ \text{降级为}\ \textbf{体系 A 的局部承重核}$$
$$\qquad\textbf{且}\ \textbf{不是}\ \text{Q-A DEAD}：\text{它告诉我们}\ \text{区域}\to\text{密度}\ \textbf{可能不存在单一证明级承重核}，\text{而存在}\ \textbf{多个不可等价的负载实现}$$
$$\text{本档落点}：\ \textbf{A（强 ALIVE）与 B（弱 ALIVE）之间} —— \text{功能层稳定}\ \checkmark，\text{但形式不唯一}\ \Longrightarrow \text{按唐先生判据，取}\ \textbf{功能归一化后的交集} \Longrightarrow \mathfrak K_{\rm stable}\ne\varnothing✓$$

## 7. 对 A₃ 的闸门（不直接进入）
$$\boxed{\text{E6-2}\ \xrightarrow{\ \text{午-2}\ }\begin{cases}\text{稳定共同核}&\Rightarrow A_3\\ \text{多个不可等价核}&\Rightarrow \text{Q-A 重定义}\\ \text{核可完全绕过}&\Rightarrow \text{E6 局部化结论降级}\end{cases}}$$
$$\text{本档实际落点＝}\textbf{稳定共同核（功能层）} \Longrightarrow \textbf{允许进入}\ A_3\ \text{的条件已在形式上满足}；\ \text{但须先处理两项残余（见 §8）}$$
$$\textbf{若日后出现}\ \mathcal K_A,\mathcal K_B,\mathcal K_C\ \text{三套不可等价核} \Longrightarrow \text{承重量应重定义为}\ \textbf{强度偏序／可达域}：$$
$$\qquad\boxed{\mathfrak S_{\rm density}=\{\text{能够产生给定}\ \theta(\sigma)\ \text{的最小输入包}\}}$$
$$\qquad\textbf{（这比}\ (\kappa,\text{均值强度})\mapsto\theta\ \text{更深一层）}$$

## 8. 残余与边界（N1/N2 严守）
$$\textbf{残余 1}：\text{§2 的体系 B 依赖投影为}\ \textbf{结构性重建}，\textbf{未逐行核验} \text{具体文献} \Longrightarrow \text{交集结论的可靠性受此限制}$$
$$\textbf{残余 2}：\text{"功能同型"的判定含}\ \textbf{判断成分}（\text{何谓"同一类估计"未形式化}）\Longrightarrow \operatorname{Core}\ \text{的定义本身是}\ \textbf{定义决策}$$
$$\textbf{证据等级}：\text{E6-2 关于"五项皆不可删"的表述}\ \textbf{继续保持}\ \textbf{[结构性论证]}，\ \textbf{不因午-2完成而自动升为"已证不可压缩"}✓$$
$$\text{本档}\ \textbf{未用 RH}；零数值；\text{未跑 Lean}；\ \textbf{不引入新机制}。$$

## 9. 净产出
$$\text{(i) 交集判据}\ \mathfrak K_{\rm stable}=\operatorname{Core}(\mathscr P_A,\mathscr P_B)\ \text{的设立（按功能而非名称）；}$$
$$\text{(ii) 体系 B 依赖投影（同型节点 1／2；形式不同的节点 3；可能的节点 5 缺失）；}$$
$$\text{(iii) 功能层提升}\ \mathcal K(D;\mathcal T)＝\text{良分离点大值／均值控制}；$$
$$\text{(iv) ⭐ 交集结果：}\mathfrak K_{\rm stable}\ne\varnothing，\text{且}\ \textbf{五节点核收窄为功能族}\ \mathcal K\ \text{（}I_{\rm dual}\ \text{退出、}I_{\rm MV}\cup I_{\rm LV}\ \text{合并）}；$$
$$\text{(v) A₃ 闸门与残余（未逐行核验＋"功能同型"为定义决策）。}$$
