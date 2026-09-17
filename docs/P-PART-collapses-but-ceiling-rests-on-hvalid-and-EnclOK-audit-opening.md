# ⚔️ **攻 P-part**：逃逸 (c) **归并**到 (a)/(b) —— 但翻出一个**性质不同**的开口：**天花板的前提是可审的**

> 依唐先生 14:27「继续」；承接 `6395536` §3 逃逸 (c) ✓
> **本档结果**：① (c) **不独立**（归并到矩阶／support）；② ⭐ 但天花板**依赖两个前提** `hvalid`／`EnclOK`，而它**由区间算术＋有限桥支撑** ⟹ **可本地审**✓✓✓

---

## §1 追问：(c) 的"更细结构"到底是什么
$$\text{证书}\ p\ \text{是}\ \textbf{数据的函数}；\ \text{可得数据}\ =\ \{\text{两个矩},\ \text{划分},\ \rho\mapsto1-\bar\rho\ \text{对称性},\ \text{重数整性}\}✓✓$$
$$\text{凡}\ \textbf{由该数据可导出} \text{的，都在天花板范围内}✓$$
$$\Longrightarrow \text{"更细结构"若要}\ \textbf{超出} \text{范围，}\ \text{必须}\ \textbf{知道更多} \text{关于构型的信息}✓✓$$
$$\qquad\Longrightarrow\ \text{更多矩}（\S7.2(e)\ \text{：}\ X\asymp T\ \text{处无条件只允许}\ k=1）✗\quad\big|\quad \text{更大 support}（\Longrightarrow \text{prime pairs}）✗✓$$
$$\Longrightarrow \boxed{\text{(c)}\ \textbf{不独立}：\ \text{归并到 (a)/(b)}}✓✓\qquad[\textbf{结构}]\ ✓$$
$$\qquad ⚠️\ \text{前提}：\text{"the partition"}\ \textbf{须} \text{指}\ \textbf{计数} \text{（非"身份"）——}\ \text{若指身份则天花板定理本身平凡，故必指计数}✓✓$$

## §2 ⭐⭐⭐ 但核验中翻出**另一类**开口（性质不同）
$$\text{天花板的}\ \textbf{前提}（逐字）：\texttt{hvalid}\ \text{（}\ c_0+\sum_{j\le256}(S_j/256)r(j/256)\le p\ \text{对采样形状因子成立）\ ＋\ \texttt{EnclOK}\ \text{（区间算术封闭）}✓✓$$
$$\qquad 📌\ \text{前沿}\ \textbf{自陈}：\text{"the enclosures}\ \texttt{EnclOK}\ \text{are certified by interval arithmetic and are}\ \boxed{\textbf{not checked by the Lean kernel}}"✓✓$$
$$\text{桥}：\text{"the analytic stability inequality with its constant"} \Longrightarrow \text{把}\ \textbf{256 点有限数据} \text{搬到}\ \textbf{全构型类} \text{的上界}✓✓$$
$$\Longrightarrow \boxed{\text{若该桥有缺口（或常数有误）} \Longrightarrow \text{天花板}\ \textbf{不是定理}}✓✓✓$$
$$\qquad ⭐\ \text{这是}\ \textbf{审前沿的证书}，\ \text{而非审计我们自己的墙} —— \text{与今日全部工作}\ \textbf{性质不同}✓✓✓$$

## §3 具体行动（**可本地做**）
$$\text{我们已装}\ \textbf{同版本}：\text{lean4}\ v4.33.0\ ＋\ \textbf{预建 Mathlib}（8311/8311）✓✓$$
$$\text{前沿给出}\ \textbf{Lean 定理名}：\texttt{Zeta23.PairCeiling.ceiling\_law256}\quad\text{与}\ \textbf{文件}：\texttt{Zeta23/PairCeiling/LawN256.lean}✓✓$$
$$\Longrightarrow \text{① 取源码（}\text{GitHub 不通时用}\ \texttt{ghfast.top}\ \text{镜像，档案已验证}\approx2.7\text{MB/s}）✓$$
$$\Longrightarrow \text{② 本地编译}\ \texttt{ceiling\_law256}\ \text{的}\ \textbf{两个假设} \text{逐条审}✓✓$$
$$\Longrightarrow \text{③ 三个具体审计点}：$$
$$\qquad\text{(i)}\ \texttt{EnclOK}\ \text{的区间算术是否正确（}\textbf{未被 kernel 检查} \text{——最大暴露面}）✓✓$$
$$\qquad\text{(ii)}\ \text{采样（}\texttt{LawN256}\text{）是否真能界定}\ \textbf{连续} \text{情形（256 点 }\to\ \text{连续 ⟹ 截断／外插风险}）✓✓$$
$$\qquad\text{(iii)}\ \text{stability 不等式的常数（}\text{前沿逐字列了}\ 0.824|r(1)|+2.55\!\times\!10^{-6}|r'(1)|+\int|r''|）\ \text{是否}\ \textbf{充分}✓✓✓$$

## §4 判词
$$\boxed{\text{P-part}\ \text{逃逸}\ \textbf{不成立}（\text{归并}）；\ \text{但得到}\ \textbf{真开口} = \text{审前沿天花板的前提}}✓✓✓$$
$$\qquad ⚠️\ \text{本档}\ \textbf{不} \text{声称天花板有错；}\ \text{只声称}\ \textbf{它可审}，\ \text{且其最大暴露面已被前沿}\ \textbf{自己点名}✓✓$$

## §5 边界
$$\text{(i)}\ §1\ \text{的归并为}\ [\textbf{结构}]✓\quad\text{(ii)}\ §2--§3\ \text{的引文}\ \textbf{全部逐字}（\texttt{clean.txt}\ L1305--1345）✓✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零计算}；\ \textbf{未取源码}✓\quad\text{(iv)}\ ⚠️\ \text{第三步 (iii) 的"是否充分"须读源码后方能判}✓$$
