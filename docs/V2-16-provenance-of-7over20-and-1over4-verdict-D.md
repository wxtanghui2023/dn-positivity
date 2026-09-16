# V2-16 — **$7/20$ 与 $1/4$ 的生成链** ⟹ 判定 **D**

> 唐先生 2026-09-16 21:15 拍板：V2-15 之后**立即 V2-16**；只追 BC 第一项的两个指数生成链✓
> 判定树：$\mathrm{A}$ 可独立改进 $\big|\$ $\mathrm{B}$ 同一核心不等式 $\big|\$ $\mathrm{C}$ 严格 sharp 边界（须**证明**不可突破）$\big|\$ $\boxed{\mathrm{D}}$ 只是参数优化产物✓
> **防误判（唐先生）**：不要只在 $A=1,M=N$ 上追；须追**符号级来源** $A^{7/20}M^{7/20}N^{7/20}(M+N)^{1/4}$✓

---

## 1. 符号级来源链（据已取证原文）
$$\text{BC §5 原文}：\text{"Combining (2.3) with the bounds for the diagonal (3.1) and off-diagonal terms (4.4) we obtain"}\ \Longrightarrow\ (5.1)\ \textbf{六项}✓$$
$$(5.1)：\ \|\beta\|^2\|\nu\|^2M^\varepsilon\Bigl(1+\tfrac{|\vartheta|A}{bNM}\Bigr)^{\frac12}\Bigl[\tfrac{AM(bN)^{1/2}}{L^{1/2}}+\tfrac{AM^2}{bLN}+\tfrac{M^2}{L}+\tfrac{b^{3/4}AM^{1/2}N^{5/4}}{L^{1/2}}+b^{1/2}AL^{3/2}N^{7/4}+\tfrac{b^{1/2}A^{1/2}MN}{L}\Bigr]✓$$
$$\text{原文平衡条件}：\ \boxed{b^{1/2}AL^{3/2}N^{7/4}\ \approx\ \frac{AM^2}{bLN}+\frac{M^2}{L}+\frac{b^{1/2}A^{1/2}MN}{L}}；\ \text{且}\ L^{*}\ \text{＝三项单项式之和}✓✓$$
$$\textbf{关键}：\ (1.2)\ \text{的两项}\ \text{正是}\ \textbf{上述优化（}L^{*}\ \text{代入）的输出} \Longrightarrow \boxed{(7/20,1/4)\ \text{与}\ (3/8,1/8)\ \textbf{共同来自同一个优化步骤}}✓✓$$

## 2. 逐问回答（唐先生五问）
$$\textbf{问 1：}7/20\ \text{是哪个核心估计产生的？} \Longrightarrow \ \text{它}\ \textbf{不是单个估计的指数}，\ \text{而是}\ \textbf{平衡优化} \text{的输出}\（\text{输入＝}(5.1)\ \text{的六项）✓$$
$$\textbf{问 2：}1/4\ \text{来自哪一步？} \Longrightarrow\ (M+N)^{1/4}\ \text{同样来自}\ \textbf{同一优化} \text{（其输入是}\ \S3\ \text{diagonal＋}\S4\ \text{off-diagonal 的项）✓$$
$$\textbf{问 3：两者是否由同一不可替代步骤共同锁定？} \Longrightarrow \ \boxed{\textbf{是}}✓✓\quad(\text{同一}\ L\ \text{-平衡})✓$$
$$\textbf{问 4：改进一个是否使另一个自动恶化？} \Longrightarrow\ \text{在}\ \textbf{同一优化内} \text{，两者由}\ \textbf{同一组输入} \text{决定} \Longrightarrow \text{不能独立改进}✓$$
$$\textbf{问 5：能否得到}\ 17r+t<8？\ \Longrightarrow\ \text{只能通过}\ \textbf{改进}\ (5.1)\ \text{的输入项}✓$$

## 3. 判定：**D**（参数优化产物）
$$\boxed{\textbf{D}}：\ (7/20,1/4)\ \text{是}\ \S5\ \textbf{单参数}\ L\ \text{-优化（＝平衡）的}\ \textbf{envelope 输出}，\ \textbf{不是} \text{单个核心估计的指数}✓✓$$
$$\qquad\text{且}\ \text{V2-4 已证}\ \mathrm{E1}：L^{*}\ \text{为}\ \textbf{内部临界点} \text{（唯一约束}\ L\ge2\log(b\vartheta M)\ \text{松弛）} \Longrightarrow \text{确认其为}\ \textbf{真优化} \text{而非边界钉住}✓✓$$
$$\qquad\Longrightarrow\ \textbf{不落 A（不可独立改进）、不落 B（非同一核心不等式，而是同一}\ \textbf{优化}）、\ \text{不落 C（未证 sharp）}✓$$
$$\textbf{但须精确}：\ \text{优化}\ \textbf{输入} \text{是}\ (5.1)\ \text{六项，}\ \textbf{异质} \text{（}\text{V2-6：}\text{含}\ b\ \text{型／对角型／谱型）} \Longrightarrow \text{故}\ \textbf{模块级可改进} \text{，但}\ \textbf{指数级不可独立改进}✓✓$$

## 4. ⭐ 由 D 打开的新入口（唐先生指明）
$$\boxed{\text{改变 BC 的}\ \textbf{证明架构} \text{，而不是寻找第二项}}✓✓$$
$$\textbf{具体化（本档）}：\ \text{既然}\ (7/20,1/4)\ \text{来自}\ L\ \text{-平衡，}\ \text{则改进入口有三}：$$
$$\qquad\text{(i) 替换}\ (5.1)\ \text{六项中的}\ \textbf{某一项} \text{为更强估计} \Longrightarrow \text{平衡改变} \Longrightarrow \text{指数改变}✓$$
$$\qquad\text{(ii) 改变}\ \textbf{平衡方式} \text{（例如引入第二个可优化参数，或改变参与平衡的项集）}✓$$
$$\qquad\text{(iii) 改变}\ \textbf{产生该六项的结构} \text{（}\S3\ \text{diagonal 的 Weil 用法／}\S4\ \text{的}\ \delta\text{-split}）✓$$
$$\qquad\Longrightarrow\ \text{三者都}\ \textbf{不需要} \text{"找一个更强的一般估计"}✓✓\quad(\text{这与 V2-7 的"优化 C--S 后变量维度"是}\ \textbf{不同} \text{的入口})✓$$

## 5. 残余（不得省略）
$$\text{残余 1：}\ (5.1)\ \text{六项}\to(1.2)\ \text{两项的}\ \textbf{代入细节未逐行核}（\text{承 V2-6b／V2-3 残余}）✓$$
$$\text{残余 2：本档断"两指数由同一优化共同锁定"为}\ \textbf{[结构判定]}，}\ \textbf{未} \text{逐项证明哪几个}\ (5.1)\ \text{项决定}\ 7/20\ \text{与哪几个决定}\ 1/4✓$$
$$\text{残余 3：残余 A--D 不变}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① 只追两个指数的生成链；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 7. 净产出
$$\text{(i) 符号级链：}\ (5.1)\ \text{六项}\to L\text{-平衡}\to L^{*}\to(1.2)\ \text{两项} \Longrightarrow (7/20,1/4)\ \textbf{与}\ (3/8,1/8)\ \textbf{同源于一个优化}✓✓$$
$$\text{(ii) 五问全答：7/20 非单估计指数；1/4 同源；}\textbf{共同锁定}；\ \text{不可独立改进；只能改输入}✓$$
$$\text{(iii) 判定}\ \boxed{\textbf{D}}（\text{参数优化产物}）\ \text{＋ V2-4 的 E1 支撑（内部最优）}✓✓$$
$$\text{(iv) ⭐ 由 D 打开的三条架构级入口（替换某项／改变平衡方式／改变生成结构）}✓✓$$
$$\text{(v) 精确限定：优化输入}\ (5.1)\ \text{六项}\textbf{异质} \Longrightarrow \textbf{模块级可改进，指数级不可独立改进}✓$$
