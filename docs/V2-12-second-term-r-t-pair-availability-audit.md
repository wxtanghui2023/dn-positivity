# V2-12 — **BC 第二项的 $(r,t)$ 与应用域相容性审计**（下一入口登记）

> 唐先生 2026-09-16 21:06：本段收口，但 **"我们的破墙还得继续"** ✓
> 本条严格按 REVIEW-V2 §5 登记的问题：$$\boxed{\text{有没有一种新的 uniform estimate}\ (r,t)\in\mathfrak F\ \text{使}\ 17r+t<8\ ?}$$
> **且不再从** $a_2$／变量释放／C–S 划分继续挖 ✓

---

## 1. ⭐ 新的观察：BC (1.2) 有**两项**，而 BCR 只用了第一项的指数
$$\text{(1.2)}：\ \mathcal B\ll\|\alpha\|\|\beta\|\|\nu\|\Bigl(1+\tfrac{|\vartheta|A}{MN}\Bigr)^{\frac12}\Bigl[\underbrace{(AMN)^{\frac7{20}+\varepsilon}(M+N)^{\frac14}}_{T_1}+\underbrace{(AMN)^{\frac38+\varepsilon}(AM+AN)^{\frac18}}_{T_2}\Bigr]✓$$
$$\text{BCR 的}\ (r,t)=(\tfrac9{20},\tfrac7{20})\ \text{对应}\ T_1\（\text{见 V2-1／V2-3}）✓$$
$$\textbf{本档新算}：\ \text{把}\ T_2\ \text{写进模板}\ (M+N)^{\frac12+r}A^{t}\ \text{的形式（}M\asymp N）\：$$
$$\qquad T_2=(AN^2)^{\frac38}(2AN)^{\frac18}\asymp A^{\frac38+\frac18}N^{\frac34+\frac18}=A^{\frac12}N^{\frac78} \Longrightarrow \boxed{(r,t)=\Bigl(\tfrac38,\tfrac12\Bigr)}✓✓$$
$$\Longrightarrow\ \boxed{L=17\cdot\tfrac38+\tfrac12=\tfrac{51}{8}+\tfrac12=\tfrac{55}{8}=\mathbf{6.875}\ <\ \mathbf{8}}✓✓✓$$

## 2. ⭐ 支配性交叉（本档计算）
$$\frac{T_2}{T_1}\asymp A^{\frac12-\frac7{20}}N^{\frac78-\frac{19}{20}}=A^{\frac3{20}}N^{-\frac3{40}}\ \Longrightarrow\ T_2\ge T_1\iff A\ \ge\ N^{\frac12}✓✓$$
$$\Longrightarrow\ \boxed{\text{当}\ A\gtrsim N^{1/2}\ \text{时，第二项支配，其指数对}\ (\tfrac38,\tfrac12)\ \text{给出}\ L=6.875<8}✓✓$$

## 3. ⚠️ 但 BCR 用的是**第一对** —— 这正是决定性的问题
$$\text{若}\ (\tfrac38,\tfrac12)\ \text{在应用域可用，BCR 应当会用它（}\theta\ \text{会更好）} \Longrightarrow \text{BCR 未用} \Longrightarrow \text{猜测其}\ \textbf{不可用}✓$$
$$\textbf{最可能的不可用原因（须核）}：\ \text{模板的}\ A\ \text{范围条件}\ A\ll(NM)^{\frac{0.5-r}{1+2t}}\：$$
$$\qquad(\tfrac38,\tfrac12)\Longrightarrow \frac{0.5-\frac38}{1+2\cdot\frac12}=\frac18\cdot\frac12=\frac1{16} \Longrightarrow \boxed{A\ll(NM)^{\frac1{16}}}（\textbf{极小的}\ A\ \text{范围}）✓$$
$$\qquad\text{而 BCR 应用需}\ A=\frac{N_1N_2}{d}T^{\frac12-\varepsilon}\ \text{型（}\textbf{大}\ A）\Longrightarrow \textbf{范围不相容}✓✓$$
$$\Longrightarrow\ \text{这与}\ \textbf{Q1／Q1b}\ \text{的"统一化"结论}\ \textbf{同源}：\ \text{指数对必须对}\ \textbf{整个出现的配置族} \text{成立，}\ \text{故}\ T_2\ \text{的支配区（大}\ A）\ \text{可能落在其模板有效区（小}\ A）\ \textbf{之外}✓✓$$

## 4. 审计目标（下一刀，可判定）
$$\boxed{\text{在 BCR 的}\ \textbf{完整参数化} \text{中判定：}T_2\ \text{能否提供可用（uniform）的}\ (r,t)=(\tfrac38,\tfrac12)\ ?}$$
$$\qquad\textbf{结果二分}：$$
$$\qquad\text{(一) 不可用（预期）}\ \Longrightarrow \text{则须}\ \textbf{定位不可用的确切原因} \text{（}A\ \text{范围？互反律？}\delta\text{-split？）} \Longrightarrow \text{得到}\ \textbf{墙的机制}✓✓$$
$$\qquad\text{(二) 可用}\ \Longrightarrow L=6.875<8 \Longrightarrow \textbf{实质破墙入口}✓✓✓$$
$$\Longrightarrow\ \text{无论哪种结果都}\ \textbf{有信息量}：\ \text{这是罕见的}\ \textbf{"两边都有产出"} \text{的审计}✓$$

## 5. 与既有登记的衔接
$$\text{本条}\ \textbf{不违反} \text{冻结禁令}：\ \text{不挖}\ a_2／\text{变量释放／C--S 划分；}\ \text{而是沿 REVIEW-V2 §5 的}\ \textbf{纯问题} \text{（新 uniform estimate）}✓$$
$$\qquad\text{且直接使用已建立的工具}：\ \mathfrak F\ \text{的定义（猎-4／5）}＋\theta(r,t)\ \text{公式（猎-3B）}＋L=17r+t✓$$

## 6. 残余（不得省略）
$$\text{残余 1：}T_2\ \text{的}\ (r,t)\ \text{对应为}\ \textbf{本档计算} \text{（}\text{BCR 未在其论文中列出该对应）}✓$$
$$\text{残余 2：}\ T_2\ \text{在其模板下的}\ A\ \text{范围公式与}\ T_1\ \text{处同形（}\textbf{待核} \text{是否另有条件）}✓$$
$$\text{残余 3：残余 A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 不挖已冻结方向；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值（仅分数与量级演算）}✓$$

## 8. 净产出
$$\text{(i) ⭐ 新算：}T_2\ \text{对应}\ (r,t)=(\tfrac38,\tfrac12)\Longrightarrow \boxed{L=\tfrac{55}{8}=6.875<8}✓✓$$
$$\text{(ii) 支配交叉：}T_2\ge T_1\iff A\ge N^{1/2} \Longrightarrow \text{大}\ A\ \text{区由第二项支配}✓$$
$$\text{(iii) ⚠️ 预期不可用原因：}(\tfrac38,\tfrac12)\ \text{的模板}\ A\ \text{范围为}\ (NM)^{1/16}\（\text{极小}），\ \text{与 BCR 所需大}\ A\ \textbf{不相容} \Longrightarrow \text{与 Q1／Q1b 的统一化结论同源}✓✓$$
$$\text{(iv) 下一刀目标：在 BCR 完整参数化中判定}\ T_2\ \text{是否可用；}\ \textbf{两种结果都有信息量}✓$$
