# V2-20 — **$F_3$／$F_5$ 逐行因果链 ＋ 最小结构图**

> 唐先生 2026-09-16 21:26 拍板 **V2-20**：把 $F_3\leftrightarrow(3.1)$、$F_5\leftrightarrow(4.4)$ 从"溯源判断"升级为**逐行因果链**✓
> 出口：$$\boxed{\text{原始 C--S／diagonal 结构}\to\{F_3,F_5\}\to L^{*}\to N^{19/20}\to 17/33}$$＋检查两输入是否**逻辑独立**✓

---

# A 支路：$F_3=M^2/L$（**完整还原** ✓✓）

## A1. §3 的 diagonal 定义（逐字）
$$\text{(2.3) 定义}：\ D_b：＝\ \text{contribution from the "diagonal terms"}\ \boxed{\ell_1n_1=\ell_2n_2}✓$$
$$\text{§3 原文}：\ \text{"In this section we bound the diagonal terms}\ D_b(M,N,A,L,\eta)\ \text{as the following lemma."}\quad\textbf{Lemma 1}\ (3.1)：D_b\ll\|\alpha\|^2\|\nu\|^2L\bigl[A(bLN)^{\frac12}+\tfrac{AM}{bN}+M\bigr]M^{\varepsilon}✓✓$$

## A2. 推导链（逐字）
$$\textbf{第 1 步（对称＋}2|ab|\le a^2+b^2\text{）}：\ \text{(3.2)}：\ D_b\ll\sum_{\substack{\ell_1,\ell_2\asymp L;\ n_1,n_2\asymp N;\ a_1,a_2\asymp A\\ (b\eta,\ell_1\ell_2n_1n_2)=1;\ \ell_1n_1=\ell_2n_2}}(|n_1a_1|^2+|n_2a_2|^2)\sum_{\substack{m\asymp M\\ (m,b\ell_1\ell_2n_1n_2)=1}}e\bigl(\tfrac{\eta(a_1\ell_1-a_2\ell_2)m}{b\ell_1n_1}\bigr)✓$$
$$\textbf{第 2 步（按}\ a_1\ell_1=a_2\ell_2\ \text{与否二分）}：$$
$$\qquad\boxed{a_1\ell_1\ne a_2\ell_2}\：\ \text{原文"we use the version of}\ \textbf{Weil's bound}\ \text{given in Lemma 3, in the appendix"}\ \Longrightarrow\ \sum_m e(\dots)\ll(bLN)^{\frac12+\varepsilon}+\frac{(a_1\ell_1-a_2\ell_2,bn_1\ell_1)M^{1+\varepsilon}}{bLN}✓✓$$
$$\qquad\qquad\Longrightarrow\ \text{贡献}\ \asymp\ \|\alpha\|^2\|\nu\|^2\Bigl[\frac{A(bLN)^{1/2}}{L}+\frac{M}{bN}\Bigr]L\ \text{型} \Longrightarrow \textbf{Lemma 1 的前两项}\ A(bLN)^{\frac12}+\tfrac{AM}{bN}✓$$
$$\qquad\boxed{a_1\ell_1=a_2\ell_2}\：\ \text{原文"\textbf{The contribution}\dots\textbf{coming from the terms with}\ a_1\ell_1=a_2\ell_2\ \textbf{is trivially}\ O(\|\alpha\|^2\|\nu\|^2LM^{1+\varepsilon})\text{"}\ ✓✓✓$$
$$\qquad\qquad\Longrightarrow\ \text{此处相位}\ e\bigl(\tfrac{\eta\cdot0\cdot m}{b\ell_1n_1}\bigr)=1 \Longrightarrow m\ \text{-求和＝纯计数}\ \asymp M \Longrightarrow \textbf{Lemma 1 的第三项}\ \boxed{M}✓✓✓$$
$$\textbf{第 3 步（}(2.2)\ \text{的因子）}：\ C_b\ \text{由}\ D_b\ \text{经}\ \textbf{因子}\ M/L\ \text{得到（V2-6b 四项验证）} \Longrightarrow \frac ML\cdot M=\boxed{\frac{M^2}{L}=F_3}✓✓✓$$

## A3. ⭐⭐⭐ A 支路结论（本节最重要发现）
$$\boxed{F_3\ \text{的"承重"不是 Weil，而是}\ \textbf{退化子情形}\ a_1\ell_1=a_2\ell_2\ \text{的}\ \textbf{平凡计数}}✓✓✓$$
$$\qquad\text{因相位}\ e(\eta(a_1\ell_1-a_2\ell_2)m/(b\ell_1n_1))=1 \Longrightarrow m\ \text{-求和退化为}\ \sum_{m\asymp M}1\asymp M✓$$
$$\Longrightarrow\ \boxed{\text{墙的}\ \textbf{diagonal 侧} \text{由}\ \textbf{退化配置的计数} \text{承载，}\ \textbf{而非} \text{深估计}}✓✓✓\quad(\textbf{与 V2-11 容量判据呼应}：\text{退化／碰撞情形是同一现象})✓$$

---

# B 支路：$F_5=b^{1/2}AL^{3/2}N^{7/4}$（**部分还原**）

## B1. 已确证部分
$$\text{(4.21)}：\ \mathscr V_{b,\eta}=\mathscr V^{\delta=0}+\mathscr V^{\delta\ne0}；\ \text{原文"}\boxed{\text{we will use Weil's bound on the sum over}\ n'_2}\ \text{to handle the terms with}\ \delta\ne0\text{"}✓✓$$
$$\delta＝a_2(d\tilde\ell'_1-d'\tilde\ell_1)\tilde\ell_2\tilde\ell'_2p_2(da_1\tilde\ell'_2-d'a'_1\tilde\ell_2)\tilde\ell_1\tilde\ell'_1q_1\quad(\text{V2-11})✓$$
$$\text{§4 后续（原文标题链）}：\ \text{"The terms with}\ \delta\ne0\text{"}\ \text{(line 1429)}\ \Longrightarrow\ \text{其界含}\ \textbf{高}\ L\ \text{-幂}（\text{抽取显示}\ L^{5}\ \text{型组合，如}\ A^2D^2L^5N^3\ \text{型}）✓$$

## B2. 与 $F_5$ 的相容性检查
$$\text{由}\ \S4.1.2\ \text{的外平方根（}\mathcal B\ll C_b^{1/2}\text{）＋}(2.2)\ \text{的}\ M/L：\ \text{若}\ \mathcal V^{\delta\ne0}\ \text{含}\ L^{5}\ \text{型幂} \Longrightarrow \text{开方后}\ L^{5/2}\Longrightarrow \times\frac ML \Longrightarrow L^{3/2}✓$$
$$\qquad\Longrightarrow\ \textbf{与}\ F_5=b^{1/2}AL^{3/2}N^{7/4}\ \text{的}\ L\ \text{-幂}\ \textbf{相容}✓\quad(\textbf{方向一致})✓$$
$$\qquad\textbf{但}：\ \text{精确的}\ L,b,A,N,M\ \text{幂次账本}\ \textbf{未逐行核对} \Longrightarrow \text{B 支路}\ \textbf{未完全闭合}✓$$

---

# 第三层：最小结构图 ＋ 独立性检查

## C1. 最小结构图
$$\boxed{\text{原始 C--S／diagonal 结构}\ \longrightarrow\ \begin{cases}F_3=\tfrac{M^2}{L}\（\Longleftarrow\ \S3\ \text{diagonal 的退化子情形}）\\[1mm]F_5=b^{1/2}AL^{3/2}N^{7/4}\（\Longleftarrow\ \S4\ \delta\ne0\ \text{支的}\ n'_2\text{-Weil}）\end{cases}\ \longrightarrow\ L^{*}\ \longrightarrow\ N^{19/20}\ \longrightarrow\ 17/33}✓✓$$

## C2. ⭐ 独立性检查（唐先生指定）
$$\boxed{F_3\ \text{侧输入} ＝\ \textbf{计数型}（a_1\ell_1=a_2\ell_2\ \text{退化配置的个数}）}✓$$
$$\boxed{F_5\ \text{侧输入} ＝\ \textbf{解析型}（\delta\ne0\ \text{支中}\ n'_2\ \text{-求和的 Weil 估计}）}✓$$
$$\Longrightarrow\ \text{两者是}\ \textbf{不同模块}（\text{计数 vs 解析}） \Longrightarrow \textbf{逻辑上可分离}✓$$
$$\qquad\textbf{但}：\ \text{二者}\ \textbf{通过}\ L^{*}\ \textbf{耦合} \text{（平衡条件把它们打成平手）} \Longrightarrow \text{单独改一个}\ \textbf{会把瓶颈转移} \text{到另一个}✓✓$$
$$\qquad\textbf{且更深一层}：\ \text{两者都}\ \textbf{源自同一}\ \S4.1.2\ \text{C--S 分解}；\ \text{改}\ F_3\ \text{侧（退化条件）会改变}\ \delta\ \text{的结构}\（\text{因}\ \delta\ \text{含}\ d\tilde\ell'_1-d'\tilde\ell_1\ \text{型碰撞条件}）✓✓$$
$$\Longrightarrow\ \boxed{\text{结论}：\ \text{两输入}\ \textbf{模块独立、结构耦合}}✓✓$$

## C3. 由此得到的**攻击层**陈述（本档出口）
$$\boxed{\text{改变}\ 17/33\ \text{必须改变}\ (F_3,F_5)\ \text{的}\ \textbf{平衡}}✓$$
$$\qquad\textbf{A 侧最干净的杠杆（新）}：\ \text{使}\ F_3\ \text{的}\ \textbf{退化计数更小} \text{——即}\ \textbf{限制}\ a_1\ell_1=a_2\ell_2\ \text{这一退化子情形}✓✓$$
$$\qquad\qquad(\text{注意：}\ \text{BC 的"longer diagonal"}\ \text{恰是通过}\ \textbf{扩大} \text{diagonal 关系}\ (\ell_1n_1=\ell_2n_2)\ \text{换取的；}\ \text{而它的副产品就是}\ a_1\ell_1=a_2\ell_2\ \text{这类退化子情形})✓$$
$$\qquad\textbf{B 侧杠杆}：\ \text{改善}\ \delta\ne0\ \text{支中}\ n'_2\ \text{-Weil 的强度（}\text{＝回到估计层}）✓$$

## D. 残余（不得省略）
$$\text{残余 1：B 支路的}\ L,b,A,N,M\ \text{幂次账本}\ \textbf{未逐行核对}（\text{A 支路已完整）}✓$$
$$\text{残余 2：}\ \mathcal V^{\delta\ne0}\ \text{的完整界式}\ \textbf{未取全}（\text{抽取噪声}）✓$$
$$\text{残余 3：A--D 不变}✓$$

## E. 边界（N1/N2 严守）
$$\text{① 不做指数代数（承唐先生）；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## F. 净产出
$$\text{(i) ⭐⭐⭐ A 支路}\ \textbf{完整还原}：F_3\ \Longleftarrow\ \S3\ \text{diagonal 中}\ \textbf{退化子情形}\ a_1\ell_1=a_2\ell_2\ \text{的}\ \textbf{平凡计数} \text{（相位＝1，}m\ \text{-和}\asymp M\text{）}✓✓✓$$
$$\qquad(\text{Weil 界只管}\ a_1\ell_1\ne a_2\ell_2\ \text{那一半} \Longrightarrow \text{产生}\ F_1,F_2）✓$$
$$\text{(ii) B 支路}\ \textbf{部分还原}：\delta\ne0\Rightarrow n'_2\text{-Weil}\Rightarrow\ \text{高}\ L\ \text{-幂}\Rightarrow\ \text{开方＋}M/L\Rightarrow L^{3/2}\（\textbf{与}\ F_5\ \text{相容}），\ \text{但账本未闭合}✓$$
$$\text{(iii) ⭐ 三结构图成立；独立性：}\ \textbf{模块独立（计数／解析）、结构耦合（同源 C--S，经}\ L^{*}\ \text{打平）}✓✓$$
$$\text{(iv) ⭐ 攻击层新陈述：}\ \text{A 侧杠杆＝}\textbf{限制退化子情形}\ a_1\ell_1=a_2\ell_2\ \text{以压低}\ F_3✓✓\（\text{BC 的 longer diagonal 恰以扩大 diagonal 换取，副产品即该退化子情形}）$$
