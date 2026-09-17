# ⚔️ W6-MAJORANT-1c · **对称化：奇点被消 ＋ 严格带限**（带外＝精确 0）

> 依唐先生 12:28 指令：**直接进入第 5 步，算出最优误差下界** ✓
> 本档先交出前三项（$M_T$ 闭式／带外精确抵消／带内形状），第 4--5 项（extremal 误差下界／代回 $O_1/D$）**另档** ✓

---

## §1 一个**有用的精确关系**（本档第一步）

$$\Phi\ \text{实且偶}（§5.1 逐字）＋\ \mathrm{supp}\,\Phi\subset[-\tfrac L2,\tfrac L2]\ll T \Longrightarrow \alpha_n^\pm\ \text{是半边全变换}✓$$
$$x=-u\ (u\in[0,T])：\ \alpha_n^-=\int_0^{T}\Phi^2(u)e^{-iy_nu}du=\overline{\alpha_n^+}✓✓$$
$$\Longrightarrow\ \boxed{\alpha_n^-=\overline{\alpha_n^+}\quad(\text{记}\ \alpha_n:=\alpha_n^+,\ \ |\alpha_n|\le\pi bL\le\pi L)}✓✓$$

## §2 原式改写
$$\text{Br}:=e^{2iTt}(\alpha_m^++\alpha_n^-)-e^{iTt}(\alpha_n^++\alpha_m^-)\ \xrightarrow{\ \S1\ }\ e^{2iTt}\big(\alpha_m+\overline{\alpha_n}\big)-e^{iTt}\big(\alpha_n+\overline{\alpha_m}\big)✓$$
$$K(n,m)=\frac{\text{Br}}{i(y_n-y_m)},\qquad t:=y_n-y_m✓$$

## §3 ⭐⭐⭐ **对称化：把 $1/(it)$ 换成 $\sin(3Tt/2)/t$**

$$\text{因求和跑在对称集}\ \{(n,m):n\ne m\}\ \text{上，形式值等于用对称化核后的值：}K^{\rm sym}=\tfrac12\big(K(n,m)+K(m,n)\big)✓$$
$$K(m,n)=\frac{1}{it}\Big[e^{-2iTt}\big(\alpha_n+\overline{\alpha_m}\big)-e^{-iTt}\big(\alpha_m+\overline{\alpha_n}\big)\Big]✓$$
$$\Longrightarrow\ K^{\rm sym}=\frac{1}{2it}\Big[\big(\alpha_m+\overline{\alpha_n}\big)\big(e^{2iTt}-e^{-iTt}\big)+\big(\alpha_n+\overline{\alpha_m}\big)\big(e^{-2iTt}-e^{iTt}\big)\Big]✓$$
$$\textbf{关键恒等式}：e^{2iTt}-e^{-iTt}=2i\,e^{iTt/2}\sin\!\big(\tfrac{3Tt}{2}\big),\qquad e^{-2iTt}-e^{iTt}=-2i\,e^{-iTt/2}\sin\!\big(\tfrac{3Tt}{2}\big)✓✓$$
$$\Longrightarrow\ \boxed{K^{\rm sym}(n,m)=\frac{\sin(3Tt/2)}{t}\Big[\big(\alpha_m+\overline{\alpha_n}\big)e^{iTt/2}-\big(\alpha_n+\overline{\alpha_m}\big)e^{-iTt/2}\Big]}✓✓✓$$

## §4 ⭐⭐⭐ 三条结构结论（**直接回答唐先生的问题**）

$$\textbf{(a) 奇点被消}：t\to0\ \text{时括号}\ \to(\alpha_n+\overline{\alpha_n})-(\alpha_n+\overline{\alpha_n})=0 \Longrightarrow K^{\rm sym}\ \textbf{在}\ t=0\ \textbf{正则}✓✓$$
$$\qquad(\text{即：}\ \textbf{离对角核不是 Hilbert 型奇核}，\ \text{而是}\ \textbf{有界带限核})✓✓✓$$
$$\textbf{(b) 严格带限}：\mathrm{FT}\Big[\frac{\sin(3Tt/2)}{t}\Big]\propto\mathbf 1_{[-3T/2,\,3T/2]}(\xi) \Longrightarrow t\text{-侧支撑}\ \boxed{[-3T/2,\,3T/2]}✓✓✓$$
$$\textbf{(c) 带外＝}\textbf{精确 0}：\ \boxed{M_T(\xi)=0\quad\text{for}\ \xi\notin[-3T/2,\,3T/2]}$$
$$\qquad\Longrightarrow\ \textbf{这不是"常数碰巧抵消"，而是}\ \textbf{四项代数组合后}\ \textbf{恒等式级} \text{的带限性}✓✓✓$$
$$\qquad\Longrightarrow\ \textbf{唐先生②的裸 Hilbert 障碍}\ \textbf{在}\ K_T\ \textbf{上彻底不成立}✓✓$$

## §5 带内形状（第 3 项）
$$M_T(\xi)\Big|_{\xi\in[-3T/2,3T/2]}=\text{FT}_{t}\Big[\frac{\sin(3Tt/2)}{t}\Big]\ast_{t}\text{FT}_t\big[\text{括号}\big]✓$$
$$\qquad\text{括号}\ =\big(\alpha_m+\overline{\alpha_n}\big)e^{iTt/2}-\big(\alpha_n+\overline{\alpha_m}\big)e^{-iTt/2}\ \textbf{含}\ n,m\ \textbf{分离的}\ \alpha\ \textbf{权重}$$
$$\qquad\Longrightarrow\ \textbf{诚实修正}：\ \text{因括号含}\ \alpha_n,\alpha_m\ \text{（}\textbf{对角权}），\ M_T\ \textbf{不是单变量乘子}，\ \text{而是}\ \textbf{带限卷积}\times\textbf{对角权} \text{结构}✓✓$$
$$\qquad(\text{即：}\ \text{符号是}\ M_T(\xi,\eta)\ \text{型二变量；}\ \textbf{带限性只在差变量}\ \xi\ \text{上成立}）✓\ \textbf{[T5/D8 标注：不得当单变量乘子用]}✓$$

## §6 第 4--5 项：**定量比较的初步读数**（须复核归一化）
$$\text{无带权版本的双线性范数}\asymp\|\sin(3Tt/2)/t\|_{\rm bilinear}\asymp\boxed{3T/2}\（\text{带质量}）✓$$
$$\text{MV 版本}：|B|\le\frac{\pi}{\delta}\|x\|\|z\|\ \text{＋}\ \delta_n^{-1}\le2n \Longrightarrow \asymp2\pi\,n\ \text{级}✓$$
$$\Longrightarrow\ \text{比值}\ \asymp\frac{2\pi n}{3T/2}\asymp\boxed{\frac{X}{T}}✓✓$$
$$\qquad\text{在}\ X=T^{1+\eta}\ \text{处：}\ \frac{X}{T}=T^{\eta}\ \textbf{——恰为所需量级}✓✓✓\quad(\text{所需补偿}\ \tfrac{T^\eta}{\log T}）✓$$
$$\textbf{⚠️ 但}\ \textbf{不能就此宣布 ALIVE}：\text{括号里的}\ \alpha\ \text{权携带}\ L\ \text{因子}（|\alpha_n|\le\pi L），\ \text{且}\ \ell^2\ \text{归一化须逐项重做}✓✓$$
$$\qquad\Longrightarrow\ \textbf{结论层级}：\textbf{FALSE 路径的理由已被移除}；\ \textbf{出现}\ \textbf{局部 ALIVE 候选}\（\text{量级}\ T^\eta，\text{恰合所需}）\（\text{待归一化复核}）✓✓$$

## §7 边界
$$\text{(i)}\ §1\ \text{用}\ \Phi\ \text{实偶＋}\mathrm{supp}\ll T\ \text{（§5.1 逐字）}✓\quad\text{(ii)}\ §3--§4\ \text{为初等恒等式，可逐行核}✓$$
$$\text{(iii)}\ §5\ \text{的二变量修正是}\ [\textbf{结构}] \text{级（防单变量误用）}✓\quad\text{(iv)}\ §6\ \textbf{未复核归一化}，\ \textbf{未用 RH／HL／pair correlation}，\ \textbf{零数值}✓$$
