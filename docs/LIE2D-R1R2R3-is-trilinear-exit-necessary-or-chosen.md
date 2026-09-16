# 猎-2D（N2-续2）— **BCR 的三线性出口：必然出口还是选择性出口？**

> 唐先生 2026-09-16 19:54 拍板 **N2-续2**。
> **前置纠正（唐先生）**：$\boxed{\text{"自由度已定位在约化／架构"}\ \textbf{目前不能作为结果}，\ \text{它是}\ \textbf{待验证的结构假设}}$✓
> 唯一目标：$$\boxed{\mathcal R_{\rm BCR}：\ E_{\rm off}\to S_{A,M,N}\ \text{是}\ \textbf{代数必然物}，\ \text{还是}\ \textbf{可选择归约}？}$$
> **防重复规则**：任何路线若最终仍为 $\text{变换}\to\text{Kloosterman fraction}\to\text{BCR 型三线性界}\to(r,t)\to\theta$，\ \textbf{一律归入 BCR-family，不算新方向}✓

---

## R1：非对角项**为什么**被迫变成三线性和？
$$\text{展开}\ \int|\zeta A|^{2}\ \text{后的非对角项，其核心是}\ \textbf{"探测等式"}\（m=n\ \text{或}\ m\approx n\ \text{的对角条件）}$$
$$\text{经典事实（本档结构重建）}：\ \text{Kloosterman fraction}\ e(a\bar m/n)\ \text{的标准来源}\ =\ \textbf{DFI }\delta\text{-symbol／圆法} \text{型}\ \textbf{探测子}：$$
$$\qquad \delta(m,n)\ \text{由}\ \sum_q\sum_{a\ (q)}\text{型相位}\ \text{表示} \Longrightarrow \textbf{三线性}\ S_{A,M,N}✓$$
$$\Longrightarrow\ \boxed{\text{三线性出口}\ =\ \textbf{探测子的选择} \text{的结果}，\ \textbf{不是} \text{代数必然物}}✓$$
$$\textbf{但须并记一项关键限定}：\text{其他已知探测子（Poisson／Voronoi 型；Mellin／Perron 型；大筛／放大型）}\ \textbf{并非新物}：$$
$$\qquad\text{它们正是}\ \textbf{经典路线} \Longrightarrow \text{BCR 自述}\ \theta<\tfrac12\ \textbf{仅用 diagonal} \text{即指此}⟹ \textbf{已知替代方向存在且}\ \textbf{较弱}✓$$

## R2：哪一步把原始算术结构"丢掉"了？（不可逆损失定位）
$$E_{\rm off}\xrightarrow{\mathcal R_1}X_1\xrightarrow{\mathcal R_2}X_2\xrightarrow{\mathcal R_3}S_{A,M,N}$$
$$\textbf{逐项审计（唐先生列的候选危险步骤）}：$$
$$\qquad\text{(i) }\textbf{Cauchy--Schwarz／绝对值化}：\ \textbf{在精确处理中并非主步}（\text{会杀掉振荡}）\Longrightarrow \textbf{不是} \text{主要不可逆点}✓$$
$$\qquad\text{(ii) }\textbf{dyadic splitting}：\ \text{可逆（}\text{只是分层）}✓$$
$$\qquad\text{(iii) }\textbf{completion／reciprocity／Poisson／Voronoi}：\ \text{在}\ \delta\text{-探测步骤内部，}\ \textbf{改变相位结构}✓$$
$$\Longrightarrow\ \boxed{\text{不可逆损失主要发生在}\ \textbf{探测步骤}（\text{如何编码对角条件}），\ \textbf{而非} \text{最后的 Kloosterman 估计}}✓$$
$$\qquad\textbf{唐先生的判断被确认}：\ \text{"真正危险处可能不是最后的 Kloosterman estimate"}\ ✓$$
$$\qquad\textbf{但附一条重要反向事实}：\ \delta\text{-探测的}\ \textbf{振荡相位被保留}（\text{不取绝对值}）\Longrightarrow \text{可利用相关性}\ \textbf{未被} \text{粗暴杀掉；只是被}\ \textbf{转移} \text{到另一形式}✓$$

## R3：替代出口（三档）
$$\textbf{R3-A}\ \text{三线性归约}\ \textbf{强制} \Longrightarrow \text{路线 B DEAD}\to\text{转 N3}$$
$$\textbf{R3-B}\ \text{非强制，但所有替代归约}\ \textbf{等价} \Longrightarrow \text{架构自由度只是表象}\to\text{关闭}$$
$$\textbf{R3-C}\ \text{存在}\ \textbf{结构上不可等价} \text{的新归约出口} \Longrightarrow \boxed{\text{墙 A 第二方向 ALIVE}}$$
$$\textbf{本档判定（诚实落点）}：\ \textbf{不落 A，也不落 C}：$$
$$\qquad\text{(i) }\text{R1 已示出口是}\ \textbf{选择的} \text{（排除 R3-A）}✓$$
$$\qquad\text{(ii) 已知替代探测子（Poisson／Mellin／大筛）}\ \textbf{均属经典路线且较弱} \Longrightarrow \text{不构成 R3-C}✓$$
$$\qquad\text{(iii) 但}\ \textbf{未证明} \text{所有替代归约等价（R3-B 未证）} \Longrightarrow \boxed{\text{第二方向}\ \textbf{OPEN，且目前无实例}}✓$$
$$\qquad\textbf{故此步判定＝"选择的出口（非必然）＋无已知非等价替代"}\ ——\ \textbf{既不是 A 也不是 C，而是"B 未证"状态}✓$$

## ⭐ 由此对"自由度在约化／架构"假设的处理（唐先生指定）
$$\text{猎-2C 的定位}\ \textbf{降级为待验证假设}：\ \boxed{\text{假设 H-arch}：\text{自由度（若有）在约化／架构}}$$
$$\qquad\text{本档结果}\ \textbf{既不证实也不证伪} \text{H-arch}：\ \text{它}\ \textbf{允许} \text{了 H-arch（出口是选择），}\ \textbf{但未找到} \text{非等价的替代出口}✓$$
$$\qquad\textbf{故当前状态}：\ \text{H-arch}\ =\ \textbf{未验证假设}；\ \text{路线 B}\ =\ \textbf{入口存在但无已知实例}✓$$

## 判定与下一步（干净化）
$$\texttt{如果走 N3（天花板审计）}：\ \text{接受 BCR 架构为给定，审计}\ \tfrac{17}{33}\ \text{的真上限}✓$$
$$\texttt{如果继续路线 B}：\ \text{唯一有意义的搜索目标＝}\ \boxed{\text{寻找}\ \textbf{非 Kloosterman-form} \text{的探测／归约出口}}$$
$$\qquad\text{（按防重复规则：任何最终回到 Kloosterman fraction 的路线}\ \textbf{一律归入 BCR-family}）✓$$
$$\qquad\textbf{但须先接受}：\ \text{这是}\ \textbf{无已知实例的开放搜索} \Longrightarrow \text{成本高、收益不确定}✓$$

## 残余（不得省略）
$$\text{残余 1：R1／R2 为}\ \textbf{结构性重建}，\ \textbf{未逐行核验 BCR 原文} \Longrightarrow \text{须以原文确认"}\delta\text{-探测步骤＝不可逆点"及"出口为选择"}✓$$
$$\text{残余 2：\ H-arch 为}\ \textbf{未验证假设}；\ \text{残余 3：}\ \text{已知替代探测子"较弱"为依据前人自述的}\ \textbf{[结构判定]}，\ \text{未逐篇核验}✓$$

## 边界（N1/N2 严守）
$$\text{① }\textbf{未用} \text{并禁止}\ \text{维数论证（承前纪律）}；\quad\text{② 本档}\ \textbf{不宣告} \text{任何新方向}；$$
$$\text{③ }\textbf{未用 RH}；零数值；\ \text{未跑 Lean}✓$$

## 净产出
$$\text{(i) R1：三线性出口＝}\textbf{探测子的选择}（\text{DFI }\delta\text{-symbol／圆法}），\ \textbf{非代数必然}；但已知替代＝经典且较弱；$$
$$\text{(ii) R2：不可逆点定位在}\ \textbf{探测步骤}（\text{非最后的 Kloosterman 估计；非 Cauchy--Schwarz}）；相位未被粗暴杀掉；}$$
$$\text{(iii) R3：}\ \textbf{非 A、非 C} \Longrightarrow \text{"选择的出口＋无已知非等价替代"}\（\text{R3-B 未证}）⟹\ \text{第二方向 OPEN 无实例}；$$
$$\text{(iv) "自由度在约化／架构"（H-arch）}\ \textbf{退回为待验证假设}（\text{本档既不证实也不证伪}）✓$$
$$\text{(v) 两条干净出路：N3（接受架构审天花板）／路线 B（寻找非 Kloosterman-form 出口，成本高）。}$$
