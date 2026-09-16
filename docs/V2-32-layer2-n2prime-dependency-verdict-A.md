# V2-32 第二层 — **$\ell$ 可参数化、$n_2'$ 仍是唯一 Weil 变量** ⟹ 判定 **A**

> 唐先生 2026-09-16 21:58 拍板第二层：$\boxed{\text{先判"平方后的}\ \ell\ \text{是否仍可作参数、}\ n_2'\ \text{是否仍可独立吃 Weil"}}$✓
> **两处修正（采纳）**：
> $$\boxed{\text{(i)}\ \text{互反恒等式可处理}\ \not\Rightarrow\ \text{平方后的多变量和可被同一个 Weil 界控制}}✓✓$$
> $$\boxed{\text{(ii)}\ 3\times3=9\ \text{＝naive expansion count，}\textbf{不是} \text{最终复杂度}}✓✓$$

---

## 1. ⭐⭐⭐ 第一步：$n_2'$ 在 (4.19) 中的**出现位置审计**（逐项）
$$(4.19)：\ \vartheta\Bigl(\underbrace{\Delta\frac{\overline{\tilde\ell_2\tilde\ell_2'b\mathfrak p_2\mathfrak q_2n_2'}}{\tilde\ell_1\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1'}}_{\textbf{项 1：含}\ n_2'}-\underbrace{\frac{a_2(d\tilde\ell_1'-d'\tilde\ell_1)}{b\tilde\ell_1\tilde\ell_1'\mathfrak p_1n_1'\mathfrak q_1\mathfrak q_2n_2'}}_{\text{项 2}}-\underbrace{(a_1-a_1')\frac{\overline{c\mathfrak p_1n_1'}}{b\mathfrak p_2}}_{\text{项 3}}+\underbrace{\frac{a_2(d'\tilde\ell_2-d\tilde\ell_2')\overline{\tilde\ell_1\tilde\ell_1'\mathfrak p_1^2\mathfrak q_1n_1'^2}}{b}}_{\text{项 4}}\Bigr)✓$$
$$\boxed{n_2'\ \textbf{只出现在项 1}，\ \text{且仅经}\ \overline{\mathfrak q_2n_2'}\ \text{（模逆元）形式}}✓✓✓$$
$$\qquad\text{项 2：}\ n_2'\ \text{仅作}\ \textbf{分母}（\mathfrak q_2n_2'）\Longrightarrow \textbf{非振荡}✓$$
$$\qquad\text{项 3／项 4：}\ \textbf{不含}\ n_2'✓\qquad\text{且}\ \Delta\ \text{含}\ \tilde\ell,\tilde\ell',a\ \textbf{不含}\ n_2'\Longrightarrow \text{对}\ n_2'\ \textbf{为常数}✓✓$$
$$\Longrightarrow\ \boxed{\text{固定其余变量后，}\ n_2'\ \text{-求和为}\ \textbf{单变量 Kloosterman／互反型}} \Longrightarrow \textbf{Weil 界即施于此}✓✓✓$$
$$\qquad(\text{与 V2-28B 逐字一致：\ "we use Weil's bound on the sum over}\ n_2'\text{"})✓✓$$

## 2. ⭐⭐⭐ 第二步：平方 $\ell_1$ 后的 $n_2'$-依赖
$$\text{平方}\ \ell_1 \Longrightarrow \sum_{\ell_1}\longrightarrow\sum_{\ell_1}\sum_{\ell_1''}\ \text{（两份副本，第二份取共轭}）✓$$
$$\qquad\text{第一份贡献}：\ \Delta\cdot\frac{\overline{\mathfrak q_2n_2'b\mathfrak p_2\tilde\ell_2\tilde\ell_2'}}{\tilde\ell_1\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1'}✓$$
$$\qquad\text{第二份贡献}：\ \Delta''\cdot\frac{\overline{\mathfrak q_2n_2'b\mathfrak p_2\tilde\ell_2''\tilde\ell_2'''}}{\tilde\ell_1''\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1''}（\text{符号相反}）✓$$
$$\Longrightarrow\ \text{两份}\ \textbf{皆仅经}\ \overline{\mathfrak q_2n_2'}\ \text{进入} \Longrightarrow \text{指数}\ \textbf{相加／相减} \Longrightarrow \boxed{\text{合并为}\ \textbf{单个}\ e\bigl(C_{\rm comb}\cdot\overline{\mathfrak q_2n_2'}\bigr)}✓✓✓$$
$$\qquad C_{\rm comb}：＝\frac{\Delta\tilde\ell_2\tilde\ell_2'}{\tilde\ell_1\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1'}-\frac{\Delta''\tilde\ell_2''\tilde\ell_2'''}{\tilde\ell_1''\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1''}✓$$
$$\Longrightarrow\ \boxed{n_2'\ \textbf{仍为唯一振荡变量}，\ \text{Weil 仍可单独施于}\ n_2'✓✓✓}$$

## 3. ⭐⭐ 采纳修正 (ii)：naive 9 项**不是**最终复杂度
$$\text{V2-32 第一层曾写"须两次用 (4.17)}\Rightarrow3\to9\text{"} \Longrightarrow \boxed{\textbf{修正}}：\ \text{9 项}\ \textbf{＝naive expansion count，不是最终复杂度}}✓✓$$
$$\qquad\textbf{本档 §2 显示}：\ \text{两份副本在同}\ \overline{\mathfrak q_2n_2'}\ \text{上}\ \textbf{合并} \Longrightarrow \text{naive 计数}\ \textbf{误导}✓✓$$
$$\qquad(\text{唐先生之修正}\ \textbf{成立}：\ \text{项可合并／共享分母／因同余退化})✓$$

## 4. ⭐⭐⭐ 判定（按唐先生四格表）
$$\boxed{\begin{array}{c|c}
\text{结果}&\text{状态}\\ \hline
\ell\ \text{可参数化，}\ n_2'\ \text{仍是唯一 Weil 变量}&\boxed{\textbf{A 倾向进一步增强}}\\
\ell\ \text{与}\ n_2'\ \text{真正耦合}&—\\
\text{耦合后有新的有效估计}&—\\
\text{无法确定}&—
\end{array}}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{A}}：\ \text{反向 C--S}\ \textbf{不产生} \text{新的估计对象}；\ \ell\ \text{仍为参数，}\ n_2'\ \text{仍单独吃 Weil}✓✓$$
$$\qquad\textbf{但（唐先生指定）}：\ \text{这}\ \textbf{不} \text{意味着能改善}\ L \Longrightarrow \text{须继续算}\ \textbf{额外平方造成的计数／系数损失}✓✓\quad(\text{下一刀})✓$$

## 5. ⚠️ 诚实登记（本档判定的三条前提）
$$\text{(i)}\ \text{"两份副本皆仅经}\ \overline{\mathfrak q_2n_2'}\ \text{进入"}\ \textbf{为依据 (4.19) 结构的推断} \text{——}\ \text{平方后相位}\ \textbf{未显式写出}✓✓\quad(\text{残余 1})✓$$
$$\text{(ii)}\ C_{\rm comb}\ \text{是否}\ \textbf{退化}（\text{为零／非互素／破坏 Kloosterman 形式}）\ \textbf{未核}✓\quad(\text{残余 2})✓$$
$$\text{(iii)}\ \Delta''\ \text{（第二副本的}\ \Delta\text{）对}\ \tilde\ell_1''\ \text{的依赖未核}✓\quad(\text{残余 3})✓$$

## 6. 残余（不得省略）
$$\text{残余 1：平方后相位未显式写出（本档 §2 为结构推断）}✓$$
$$\text{残余 2：}C_{\rm comb}\ \text{退化性未核}✓\quad\text{残余 3：}\Delta''\ \text{依赖未核}✓\quad\text{残余 4：计数／系数损失未算（下一刀）}✓\quad\text{残余 5：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只判"}\ell\ \text{是否参数化、}\ n_2'\ \text{是否独吃 Weil"；}\quad\text{② }\textbf{不算}\ L\ \text{幂次、}\textbf{不做}\ F_5\ \text{envelope}✓$$
$$\text{③ }\textbf{不} \text{宣布 ALIVE／DEAD（除 A 倾向）；}\quad\text{④ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) ⭐⭐⭐ }n_2'\ \textbf{只出现在 (4.19) 项 1}，\ \text{仅经}\ \overline{\mathfrak q_2n_2'}⟹ \text{固定其余变量后}\ n_2'\ \text{求和为}\ \textbf{单变量互反型}⟹\textbf{Weil 施于此}✓✓✓$$
$$\text{(ii) ⭐⭐⭐ 平方}\ \ell_1\ \text{后两份副本}\ \textbf{皆仅经}\ \overline{\mathfrak q_2n_2'}\Rightarrow \text{指数}\textbf{合并} \Rightarrow \boxed{n_2'\ \textbf{仍为唯一振荡变量}}✓✓✓$$
$$\text{(iii) ⭐⭐ 采纳修正 (ii)：naive 9 项}\ \textbf{不是} \text{最终复杂度（本档显示合并）}✓✓$$
$$\text{(iv) ⭐⭐⭐ 判定}\ \boxed{\textbf{A}}\ \text{（A 倾向进一步增强）} \Longrightarrow \text{反向 C--S 不产生新估计对象}✓✓$$
$$\text{(v) ⭐ 但}\ \textbf{不等于} \text{能改善}\ L \Longrightarrow \text{下一刀＝额外平方的}\ \textbf{计数／系数损失}✓✓$$
