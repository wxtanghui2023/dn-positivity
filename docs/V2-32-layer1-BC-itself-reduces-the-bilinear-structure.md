# V2-32 — **第一层：(4.15)–(4.19) 全文** ⟹ **BC 自己就用互反恒等式处理 $\tilde\ell\tilde\ell'$ 双线性结构**

> 唐先生 2026-09-16 21:56 拍板 **V2-32：先 (4.16)–(4.19)，再做可逆还原测试**✓
> 取证：本地 `/tmp/bc_html.txt` **逐字**✓（外部来源，仅作数据）

---

## 1. ⭐⭐⭐ BC 用的**互反恒等式**（(4.17) 逐字）
$$\boxed{\frac{\overline{\alpha\gamma}}{\beta}+\frac{\overline{\beta\gamma}}{\alpha}+\frac{\overline{\alpha\beta}}{\gamma}\ \equiv\ \frac{1}{\alpha\beta\gamma}\quad(\mathrm{mod}\ 1)},\qquad \alpha,\beta,\gamma\ \textbf{两两互素}✓✓✓$$
$$\qquad(\text{原文："we use the congruence relation}\dots\text{which holds for}\ \alpha,\beta,\gamma\ \text{pairwise coprime"})✓$$

## 2. ⭐⭐⭐ BC **自己**改写含 $\overline{\tilde\ell_1\tilde\ell_1'}$ 的项（(4.18) 逐字）
$$\text{原文}：\ \text{"to rewrite}\ -\frac{a_2(d\tilde\ell_1'-d'\tilde\ell_1)\overline{\tilde\ell_1\tilde\ell_1'\mathfrak p_1n_1'b\mathfrak q_1}}{\mathfrak q_2n_2'}\ \text{(modulo 1) as"}$$
$$\qquad\frac{a_2(d\tilde\ell_1'-d'\tilde\ell_1)\overline{\mathfrak q_2n_2'b}}{\boxed{\tilde\ell_1\tilde\ell_1'}\mathfrak p_1\mathfrak q_1n_1'}+\frac{a_2(d'\tilde\ell_2-d\tilde\ell_2')\overline{\tilde\ell_1\tilde\ell_1'\mathfrak p_1^2\mathfrak q_1n_1'n_1'^2}}{b}-\frac{a_2(d\tilde\ell_1'-d'\tilde\ell_1)}{b\tilde\ell_1\tilde\ell_1'\mathfrak p_1n_1'\mathfrak q_1\mathfrak q_2n_2'}\tag{4.18}✓✓$$
$$\qquad\textbf{by (4.16)}✓\quad(\text{(4.16)：}(d'\tilde\ell_1-d\tilde\ell_1')\overline{\mathfrak q_2n_2'}\equiv(d'\tilde\ell_2-d\tilde\ell_2')\overline{\mathfrak p_1n_1'}\ (\mathrm{mod}\ b)✓）$$
$$\Longrightarrow\ \boxed{\textbf{BC 自己用 (4.17) 把"}\tilde\ell\tilde\ell'\ \text{的模逆元"改写为"}\tilde\ell\tilde\ell'\ \textbf{作分母}" \text{的项}}✓✓✓$$

## 3. ⭐⭐ 改写后的最终相位（(4.19) 逐字）
$$\vartheta\Bigl(\underbrace{\Delta\frac{\overline{\tilde\ell_2\tilde\ell_2'b\mathfrak p_2\mathfrak q_2n_2'}}{\tilde\ell_1\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1'}}_{\textbf{Kloosterman／互反型：}\Delta\times\text{模逆元}}-\underbrace{\frac{a_2(d\tilde\ell_1'-d'\tilde\ell_1)}{b\tilde\ell_1\tilde\ell_1'\mathfrak p_1n_1'\mathfrak q_1\mathfrak q_2n_2'}}_{\text{分母型（非振荡）}}+\underbrace{(a_1-a_1')\frac{\overline{c\mathfrak p_1n_1'}}{b\mathfrak p_2}}_{\text{不含}\ \ell}-\underbrace{\frac{a_2(d'\tilde\ell_2-d\tilde\ell_2')\overline{\tilde\ell_1\tilde\ell_1'\mathfrak p_1^2\mathfrak q_1n_1'^2}}{b}}_{\text{模逆元型}}\Bigr)\tag{4.19}✓✓$$
$$\qquad\text{其中}\ \Delta：＝a_2(d\tilde\ell_1'-d'\tilde\ell_1)\tilde\ell_2\tilde\ell_2'\mathfrak p_2-(da_1\tilde\ell_2'-d'a_1'\tilde\ell_2)\tilde\ell_1\tilde\ell_1'\mathfrak q_1✓$$

## 4. ⭐⭐⭐ 第一层结论（**decisive**）
$$\boxed{\text{BC}\ \textbf{自己就用 (4.17) 处理}\ \tilde\ell\tilde\ell'\ \text{的双线性结构} \Longrightarrow \text{该结构}\ \textbf{并非"genuinely new"}}✓✓✓$$
$$\qquad\text{处理链}：\ \textbf{同余条件 (4.15)/(4.16)} \longrightarrow \textbf{互反恒等式 (4.17)} \longrightarrow \text{分母型／模逆元型相位} \longrightarrow \textbf{Weil 界（施于}\ n_2'\text{）}✓✓$$
$$\qquad\Longrightarrow\ \text{所以 V2-31 观察到的"相位双线性"}\ \textbf{已在 BC 现有机制之内}✓✓$$

## 5. ⭐⭐⭐ 对反向 C--S 的**精确含义**
$$\text{平方}\ \ell_1 \Longrightarrow \text{相位同时含}\ \overline{\tilde\ell_1\tilde\ell_1'}\ \text{与}\ \overline{\tilde\ell_1''\tilde\ell_1'} \Longrightarrow \textbf{两个共享}\ \tilde\ell_1'\ \text{的乘积逆元}✓✓$$
$$\qquad\Longrightarrow\ \text{须}\ \textbf{两次} \text{应用 (4.17)} \Longrightarrow \text{项数从 3 变}\ 3\times3=9✓✓\quad(\textbf{形式仍在同族},\ \text{但代价增大})✓$$
$$\Longrightarrow\ \boxed{\text{反向 C--S 的对象}\ \textbf{形式上仍属互反／Kloosterman 族}，\ \text{但项数与代价增大}}✓✓$$
$$\qquad\Longrightarrow\ \text{按唐先生三叉}：\ \text{"可逆还原到 Weil／BC"}\ \textbf{倾向成立} \Longrightarrow \boxed{\text{A 倾向}\ \textbf{削弱}}；\ \text{同时项数增长}\Rightarrow \textbf{C 倾向}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{两者皆}\ \textbf{非-ALIVE}}\ ⟹ \text{本档判定}\ \boxed{\textbf{A/C 倾向，仍 OPEN}} \text{（第二层未做）}✓✓$$

## 6. 第二层（可逆还原测试）—— **未做**
$$\text{按唐先生五判据}：\ \text{(1) 变量数是否下降；(2) 模数是否可控；(3) 映射是否可逆／有限对一；(4) 是否产生新系数损失；(5) 最终是否留下 Weil 型估计}✓$$
$$\qquad\textbf{本档未做} \Longrightarrow \text{残余 1}✓\quad(\text{需显式构造}\ (\ell_1,\ell_1'',\ell_1')\leftrightarrow(x,y,\text{params})\ \text{映射})✓$$

## 7. 残余（不得省略）
$$\text{残余 1（关键）：第二层可逆还原测试未做（五判据）}✓$$
$$\text{残余 2：}\ \Delta\ \text{在平方后的定义变化未核}✓\quad\text{残余 3：}\ \text{项数增长的定量估计未做（9 项是否可压缩）}✓\quad\text{残余 4：A--D 不变}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 只做第一层（读 (4.16)--(4.19)）；}\quad\text{② }\textbf{不} \text{宣布 ALIVE／DEAD；}\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 9. 净产出
$$\text{(i) ⭐⭐⭐ (4.17) 互反恒等式逐字（三变量、两两互素）}✓✓✓$$
$$\text{(ii) ⭐⭐⭐ (4.18) 逐字：}\ \textbf{BC 自己} \text{用 (4.17) 把}\ \tilde\ell\tilde\ell'\ \text{的模逆元改写为分母型}✓✓✓$$
$$\text{(iii) ⭐⭐ (4.19) 最终相位（含}\ \Delta\times\text{模逆元（Kloosterman 型）四项）}✓✓$$
$$\text{(iv) ⭐⭐⭐ 结论：双线性结构}\ \textbf{已在 BC 机制内} \Longrightarrow \text{非"genuinely new"}✓✓$$
$$\text{(v) ⭐⭐⭐ 反向 C--S 含义：须两次用 (4.17)}\Rightarrow \text{项数}\ 3\to9 \Longrightarrow \textbf{A/C 倾向，仍 OPEN}✓✓$$
