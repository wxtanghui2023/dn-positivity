# V2-30-RAW — **§4.1.2 原文取证材料**（供逐行审计）

> 唐先生 2026-09-16 21:51「搜索原文」✓
> 来源：arXiv HTML（`ar5iv.labs.arxiv.org/html/1502.00769`）**逐字抽取**；**外部来源，仅作数据**✓
> 本档＝**原始材料归档**，不含判断✓

---

## 1. ⭐⭐ C–S 的**作用集与保留集**（逐字，两处）
$$\textbf{§4.1.2 正文逐字}：\ \text{"Next, we apply the Cauchy--Schwarz inequality with respect to the sums over}\ \boxed{\mathfrak p_1,\mathfrak p_2,\mathfrak q_1,\mathfrak q_2,n_1',n_2',c,a_2}\text{.}\ \text{After squaring out, we get}\dots(4.10)\text{"}✓✓$$
$$\textbf{概要段逐字}：\ \text{"In Section 4.1.2, we apply the Cauchy--Schwarz inequality to the sums over}\ \boxed{n_1,n_2,a_2}\ \text{but}\ \boxed{\textbf{not}}\ \text{to the sums over}\ \boxed{d,a_1,\ell_1,\ell_2}\text{.}\ \text{As a comparison, in [DFI97] the Cauchy--Schwarz inequality is applied to all the sums except those over}\ \boxed{\ell_1\ \text{and}\ \ell_2}\text{"}✓✓✓$$
$$\Longrightarrow\ \textbf{未平方组}＝\{d,a_1,\ell_1,\ell_2\}（\text{BC}）\ \textbf{vs}\ \{\ell_1,\ell_2\}（\text{DFI}）\Longrightarrow \text{BC 额外保留}\ \{d,a_1\}✓✓$$

## 2. ⭐⭐⭐ **决定性的同余条件**（逐字，§4.1.3 开头）
$$\text{原文}：\ \text{"We start the analysis of}\ \mathscr V_{b,\eta}\ \text{by noticing that the conditions}$$
$$\qquad\tilde\ell_1\mathfrak p_1n_1'-\tilde\ell_2\mathfrak q_2n_2'+cd\eta\ \equiv\ 0\quad(\mathrm{mod}\ b\mathfrak q_1\mathfrak p_2|d|\eta)$$
$$\qquad\tilde\ell_1'\mathfrak p_1n_1'-\tilde\ell_2'\mathfrak q_2n_2'+cd'\eta\ \equiv\ 0\quad(\mathrm{mod}\ b\mathfrak q_1\mathfrak p_2|d'|\eta)$$
$$\qquad\textbf{imply the congruence conditions}\dots\text{"}✓✓✓$$
$$\text{且逐字定义}：\ \tilde\ell_1'：＝\ell_1'/\mathfrak q_1,\qquad \tilde\ell_2'：＝\ell_2'/\mathfrak p_2✓$$
$$\Longrightarrow\ \boxed{\text{四个}\ \ell\ \textbf{仅经互补因子}\ \tilde\ell\ \text{（＝商}\ \ell/\mathfrak p\ \text{或}\ \ell/\mathfrak q\text{）}\ \textbf{线性} \text{进入同余条件}}✓✓✓$$
$$\qquad\text{（此事实}\ \textbf{支持} \text{V2-29 的结构观察，但}\ \textbf{不等于} \text{"平方后必成二次型"}——\text{后者}\ \textbf{仍为结构推断}，\text{须 (4.10)/(4.11) 全文核定）}✓$$

## 3. 已取到的分拆式（逐字）
$$(4.12)：\ \mathscr T_{b,\eta}=\mathscr U_{b,\eta}+\mathscr U'_{b,\eta}✓\qquad(4.13)：\ \mathscr U_{b,\eta}=\mathscr V_{b,\eta}+\mathscr V'_{b,\eta}✓$$
$$\qquad\text{其中}\ \mathscr V'_{b,\eta}\ \text{逐字}：\ \text{"the contribution of the terms such that}\ d=d',\ \ell_1=\ell_1',\ \ell_2=\ell_2'\ \text{and}\ a_1\ne a_1'\text{"}✓✓$$

## 4. ⚠️ 仍缺（须补取）
$$\text{(i)}\ (4.10)\ \text{的}\ S^2_{b,M}\ \textbf{完整表达式}（\text{平方后对象的变量集与相位}）✗$$
$$\text{(ii)}\ (4.11)\ \text{的指数相位}\ \textbf{完整表达式}✗$$
$$\text{(iii)}\ (4.14)/(4.15)\ \text{的}\ \mathscr U\ \text{与}\ \mathscr V\ \text{定义式}✗$$
$$\text{(iv)}\ \S4.1.3.1\ \text{的}\ \mathscr V^*\ \text{恢复式}（\text{三阶段：同余／相位／消}\ n_2'）\ \text{已部分见于 V2-9}✓$$
$$\Longrightarrow\ \text{建议补取方式}：\ \text{按 (4.10)/(4.11) 的}\ \textbf{公式标签} \text{定向抽取，或改用}\ \text{arXiv PDF 页 17--22 直接读}✓$$

## 5. 本材料对 V2-30 的用途
$$\text{V2-30 目标（纯审计）}：\ \mathrm{C\!-\!S}\to\text{平方后对象}\to\text{新对角}\to\Delta\to\mathrm{Weil／非Weil}\to\text{幂次账本}✓$$
$$\qquad\text{需 (4.10)/(4.11) 全文方能回答}：\ \text{"若把一个}\ \ell\ \text{移入平方组，新对象中该}\ \ell\ \text{以何形式出现"}✓✓$$
$$\qquad\Longrightarrow\ \text{本档为}\ \textbf{半成品材料}；\ \text{补全 (4.10)/(4.11) 后即可开工}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① 本档仅归档原文片段，}\textbf{不作判断}；\quad\text{② }\textbf{未用 RH}；\ \text{零数值}✓$$
