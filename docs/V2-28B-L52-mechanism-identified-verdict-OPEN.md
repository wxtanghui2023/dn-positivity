# V2-28B — **$L^{5/2}$ 的产生机制已定** ⟹ 判定 **OPEN**（五情形中的 (iii)+(v)）

> 唐先生 2026-09-16 21:48「继续」✓
> 唯一问题：$\boxed{L^{5/2}\ \text{是由哪个}\ \textbf{具体不等式} \text{产生的}？}$
> 五情形：(i) Weil 的 $\sqrt q$ sharpness；(ii) C--S 平方根损失；(iii) 纯计数；(iv) 绝对值化；(v) dyadic／参数分解重复计数✓
> 取证：arXiv HTML（ar5iv），**逐字**✓（外部来源，仅作数据）

---

## 1. ⭐⭐⭐ 逐字链：$L^5$ 如何生成（(4.29) 三个中间式）
$$\text{第 1 式}：\ \|\nu\|^2\frac{A^2LN^{\frac32}M^\varepsilon}{\mathfrak p_1\mathfrak p_2}\underbrace{\operatorname{\sum\sum\sum\sum}_{\ell_1,\ell_2,\ell_1',\ell_2'\in\mathcal L}}_{\textbf{四个}\ \ell\ \text{-求和}}\ \dots✓$$
$$\text{第 2 式}：\ \ll\ \|\nu\|^2\frac{A^2\,\boxed{D L^{2}}N^{\frac32}M^\varepsilon}{(\mathfrak p_1+\mathfrak q_1)\mathfrak p_1\mathfrak q_1\mathfrak p_2^2}\operatorname{\sum\sum}_{\ell_2,\ell_2'\in\mathcal L}\frac{\boxed{DL}}{\mathfrak q_1\mathfrak p_2}\Bigl(1+\tfrac{|\vartheta|AD}{bLN^2}\Bigr)✓$$
$$\text{第 3 式}：\ \ll\ \frac{\|\nu\|^2A^2\,\boxed{D^2L^5}N^{\frac32}M^\varepsilon}{(\mathfrak p_1+\mathfrak q_1)(\mathfrak p_2+\mathfrak q_2)\mathfrak p_1\mathfrak q_1^2\mathfrak p_2^3\mathfrak q_2}\Bigl(1+\tfrac{|\vartheta|AD}{bLN^2}\Bigr)\tag{4.29}✓✓$$
$$\Longrightarrow\ \boxed{L^5\ =\ \underbrace{L^4}_{\textbf{四个}\ \ell\ \text{-变量的计数}}\ \times\ \underbrace{L^1}_{(\mathfrak p,\mathfrak q)\ \text{分解}\ PQ\asymp L}}✓✓✓$$

## 2. ⭐⭐⭐ 原文的**关键附注**（直接针对"绝对值化损失"）
$$\text{逐字}：\ \text{"The extra sum over the congruence classes modulo}\ (\ell_1\ell_1',\ell_2\ell_2')\ \text{has the effect of making us lose a factor of}\ (\ell_1\ell_1',\ell_2\ell_2')\ \text{in the}\ \Delta\ne0\ \text{terms,}\ \boxed{\textbf{but this loss is recovered by the extra condition between the}\ \ell_1,\ell_1',\ell_2,\ell_2'}\text{"}✓✓✓$$
$$\qquad\qquad\text{且原文续：\ "In fact, one can obtain a bound }\textbf{stronger than}\ (4.30)\text{"}✓✓$$
$$\Longrightarrow\ \text{即：}\ \textbf{绝对值化损失（情形 iv）}\ \text{已被作者}\ \textbf{显式识别并补偿} \Longrightarrow \boxed{\text{情形 (iv)}\ \textbf{不成立}}✓✓$$
$$\qquad(\text{"bound trivially the sum over}\ c\ \text{using (4.28)" 是那一步绝对值化；其损失被}\ \ell\ \text{间额外条件回收})✓$$

## 3. ⭐⭐ Weil 的位置（**与 $L$ 无关**）
$$\text{(4.20) 逐字}：\ \mathscr V_{b,\eta}=\mathscr V^{\Delta=0}+\mathscr V^{\Delta\ne0}；\ \text{"We shall give a}\ \textbf{trivial bound}\ \text{for the terms with}\ \Delta=0\text{, whereas we will}\ \boxed{\textbf{use Weil's bound on the sum over}\ n_2'}\ \text{to handle the terms with}\ \Delta\ne0\text{"}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{Weil 作用于}\ n'_2\text{-求和}} \Longrightarrow \text{它贡献}\ A,b,N\ \text{侧结构，}\ \textbf{不产生}\ L\ \text{-幂}}✓✓$$
$$\qquad\text{本档已定}\ (\mathrm{V2\text{-}27})：F_5\ \text{的}\ A,b,N^{3/4}\ \text{来自}\ (4.33)\ \text{的}\ n'_2\text{-Weil 输出＋前因子}✓$$

## 4. ⭐⭐⭐ 五情形逐一判定
$$\text{(i) Weil 的}\ \sqrt q\ \text{sharpness} \Longrightarrow \boxed{\textbf{否}}\quad(\text{Weil 在}\ n'_2\ \text{上，不产生}\ L\ \text{-幂})✓$$
$$\text{(ii) C--S 平方根损失} \Longrightarrow \boxed{\textbf{是（一半）}}\quad(L^5\to L^{5/2}\ \text{由}\ \S4.1.2\ \text{的开方给出})✓$$
$$\text{(iii) 纯计数} \Longrightarrow \boxed{\textbf{是（主）}}\quad(L^4\ \text{＝四个}\ \ell\ \text{-变量的朴素计数})✓✓$$
$$\text{(iv) 绝对值化损失} \Longrightarrow \boxed{\textbf{否}}\quad(\text{原文显式识别并回收})✓✓$$
$$\text{(v) dyadic／参数分解重复计数} \Longrightarrow \boxed{\textbf{是（一部分）}}\quad(\text{额外}\ L^1\ \text{来自}\ PQ\asymp L\ \text{的分划})✓$$
$$\Longrightarrow\ \boxed{L^{5/2}\ \text{的产生机制}\ =\ \underbrace{\text{四个未平方}\ \ell\ \text{-变量的计数}}_{\text{(iii)}}\ \times\ \underbrace{PQ\asymp L\ \text{分划}}_{\text{(v)}}\ \xrightarrow{\ \text{C--S 开方}\ }\ L^{5/2}}✓✓✓$$

## 5. 判定：**OPEN**（按唐先生三分支）
$$\text{分支 A（可平均化的绝对值损失}\Rightarrow\mathrm{ALIVE}）\Longrightarrow \boxed{\textbf{不成立}}\quad(\text{情形 (iv) 已被原文回收})✓$$
$$\text{分支 B（可达的 Weil sharp witness}\Rightarrow F_5\ \text{封}）\Longrightarrow \boxed{\textbf{不成立}}\quad(L\ \text{-幂不来自 Weil})✓$$
$$\Longrightarrow\ \boxed{\textbf{OPEN}}✓✓\quad(\textbf{不硬宣布墙})✓$$
$$\text{且}\ \text{OPEN 的}\ \textbf{具体形态已确定}：\ L^{5/2}\ \text{＝}\ \textbf{未平方}\ \ell\ \text{-变量的计数输出} \Longrightarrow \text{压低它需要}\ \textbf{把更多}\ \ell\ \text{-变量平方}✓✓$$

## 6. ⭐ 由此得到的**精确下一问**（含 V2-11 的教训）
$$\boxed{\text{能否把更多}\ \ell\ \text{-变量放进 C--S 的平方组（减少未平方计数），而不破坏后续结构？}}✓✓$$
$$\qquad\textbf{注意方向}：\ \text{这与}\ \mathrm{V2\text{-}7/11}\ \text{研究的}\ \textbf{相反}：\ \text{那里问"能否}\ \textbf{释放} \text{更多变量（少平方）} \Longrightarrow \mathrm{DEAD}✓$$
$$\qquad\qquad\text{本档问"能否}\ \textbf{平方} \text{更多} \Longrightarrow \text{即}\ \text{回到 DFI 型做法} \Longrightarrow \text{疑会}\ \textbf{失去 BC 的 longer-diagonal 收益}✓（\text{未证}）✓$$
$$\qquad\Longrightarrow\ \text{这是}\ \textbf{反向容量问题}，\ \text{且已有}\ \mathrm{V2\text{-}11}\ \text{的}\ \textbf{同族教训}（\text{容量判据}）\ \text{可复用}✓$$

## 7. 残余（不得省略）
$$\text{残余 1：}\ L^5\to L^{5/2}\ \text{的开方具体位置（}\S4.1.2\ \text{的 C--S）}\ \textbf{未逐行核}（\text{但 (4.29)}\to\text{(4.31) 的幂次减半已见}）✓$$
$$\text{残余 2：}\ \text{反向容量问题（§6）未审计}✓\quad\text{残余 3：}\ \mathscr V'_{b,\eta}\ \text{界式仍未读}✓\quad\text{残余 4：A--D 不变}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 只审计}\ L^{5/2}\ \text{的产生机制；}\quad\text{② }\textbf{不} \text{宣布}\ F_5\ \text{的 sharpness／不宣布墙}；\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 9. 净产出
$$\text{(i) ⭐⭐⭐ 机制已定：}\ L^5=L^4（\text{四个}\ \ell\ \text{-变量计数}）\times L^1（PQ\asymp L\ \text{分划）} \xrightarrow{\text{C--S 开方}} L^{5/2}✓✓✓$$
$$\text{(ii) ⭐⭐⭐ 原文附注：}\ \text{绝对值化损失}\ \textbf{已被显式回收} \Longrightarrow \text{情形 (iv)}\ \textbf{排除}✓✓$$
$$\text{(iii) ⭐⭐ Weil 在}\ n'_2\ \text{上，}\ \textbf{不产生}\ L\ \text{-幂} \Longrightarrow \text{情形 (i)}\ \textbf{排除}✓✓$$
$$\text{(iv) ⭐⭐⭐ 判定}\ \boxed{\textbf{OPEN}}：\ \text{非 ALIVE 入口（(iv) 已回收）、非 Weil sharp；}\ \text{具体形态＝}\textbf{未平方}\ \ell\ \text{的计数输出}✓✓$$
$$\text{(v) ⭐ 下一问（反向容量）：}\ \text{能否把更多}\ \ell\ \text{-变量平方？}\（\text{与 V2-11 的释放方向相反，可复用其容量判据}）✓✓$$
