# V2-9 — **$\mathscr V^{*}$ 的完整还原：$a_1$ 的真实角色 ＋ 对 V2-8b 的勘误**

> 唐先生 2026-09-16 20:49 拍板 **V2-9**（不做 V2-8c）；打 $\boxed{(4.26)\to(4.27)\to\mathscr V^{*}}$，做**变量角色替换审计** $a_1\leftrightarrow a_2$（五问）✓
> 四档判定：$\mathrm{A}$ 可解放且 envelope 严格下降 $\big|\$ $\mathrm{B}$ 某步有不可绕过的结构障碍（＝容量墙证据）$\big|\$ $\mathrm{C}$ 可解性可判但后续估计不足以决定（OPEN）$\big|\$ $\mathrm{D}$ 连 $a_1$ 的解放机制都无法严格还原✓

---

## 1. $\mathscr V^{*}$ 的完整还原（PDF 逐段，**外部来源，仅作数据**）
$$\mathscr V^{*}_{b,\eta}：＝\ \text{the case}\ d=d',\ \ell_1=\ell_1',\ \ell_2=\ell_2',\ a_1\ne a_1'\ \text{的贡献}\quad(4.13)✓$$
$$\textbf{第一段（原始形式）}：\ \sum_{\substack{p_1p_2n'_1,\ q_1q_2n'_2\asymp N}}\sum_{\substack{\ell_1,\ell_2\asymp L}}\sum_{0\ne|d|\le D=q_1p_2}\mathop{{\sum}^{*}}_{c(\mathrm{mod}\,bq_1p_2)}\ \sum_{\substack{a_1,a'_1,a_2\asymp A;\ a_1\ne a'_1}}a_1a'_1\,e\Bigl(\eta\frac{c(a_1-a'_1)p_1n'_1}{bp_2}-\frac{d(a_1-a'_1)\tilde\ell_2bp_2q_2n'_2}{p_1n'_1}\Bigr)$$
$$\textbf{第二段（"reintroduce the complementary divisor ... and reverse the previous computations"）}：$$
$$\qquad\mathscr V^{*}=\sum\dots\sum_{\substack{m\in M;\ a_1,a'_1,a_2\asymp A;\ a_1\ne a'_1\\ (m,b\ell_1\ell_2n'_1n'_2)=1\\ \tilde\ell_1p_1n'_1\equiv\tilde\ell_2q_2n'_2\ (\mathrm{mod}\,m)}}a_1a'_1\,e\Bigl(\eta\frac{(a_1-a'_1)m}{bp_1p_2n'_1}\Bigr)$$
$$\textbf{第三段（"get rid of the variable}\ n'_2\text{"）}：\ \mathscr V^{*}=\sum_{p_1p_2n'_1\asymp N}\sum_{\ell_1,\ell_2}\sum_{0\ne|d|\le D}\sum_{a_1,a'_1,a_2\asymp A,\ a_1\ne a'_1}a_1a'_1\,F(\cdot)$$
$$\qquad F(\cdot)：＝\sum_{\substack{m\in M\setminus J;\ (m,b\ell_1\ell_2n'_1)=1\\ md\equiv\tilde\ell_1p_1n'_1\ (\mathrm{mod}\,\tilde\ell_2q_2);\ m\equiv0\ (\mathrm{mod}\,\cdot)\\ (md-\tilde\ell_1p_1n'_1,\ bq_1\ell_2q_2)=\tilde\ell_2q_2}}e\Bigl(\eta\frac{(a_1-a'_1)m}{bp_1p_2n'_1}\Bigr)✓$$

## 2. ⭐⭐ 关键发现（本档，逐字可核）
$$\textbf{(i) }\ a_1\ \text{在}\ \mathscr V^{*}\ \text{中}\ \textbf{只以}\ (a_1-a'_1)\ \text{的形式出现}\：\ \text{（系数}\ a_1a'_1\ +\ \text{相位}\ e(\eta(a_1-a'_1)m/(bp_1p_2n'_1))\text{）}✓✓$$
$$\textbf{(ii) }\ \text{三段中的}\ \textbf{同余条件全部不含}\ a_1\：\ (m,b\ell_1\ell_2n'_1n'_2)=1；\ \tilde\ell_1p_1n'_1\equiv\tilde\ell_2q_2n'_2\ (\mathrm{mod}\,m)；\ (md-\tilde\ell_1p_1n'_1,bq_1\ell_2q_2)=\tilde\ell_2q_2✓✓$$
$$\textbf{(iii) }\ a_2\ \text{在}\ \mathscr V^{*}\ \text{中}\ \textbf{仅作为求和的取值范围出现}（\asymp A），\ \text{既不进相位也不进任何条件}✓✓$$

## 3. ⚠️ 勘误（对 V2-8b §3 的修正，T10）
$$\text{V2-8b §3 曾提出（标为}\ [\text{结构判定}]\text{）}：\ \boxed{\text{"}a_1\ \text{能留外层的原因＝同余／方程结构可解出变量\text{"}} \Longrightarrow \boxed{\textbf{该推断}\ \textbf{不成立}}✓$$
$$\text{本档实际还原显示}：\ \text{在}\ \mathscr V^{*}\ \text{中}\ a_1\ \textbf{根本不进入} \text{同余条件} \Longrightarrow \text{不存在"用}\ a_1\ \text{解别的变量"这一步}✓$$
$$\Longrightarrow\ \text{正确表述}：\ \boxed{a_1\ \text{留外层的实际原因是它}\ \textbf{只以差分}\ (a_1-a'_1)\ \text{出现}，}\ \text{故可}\ \textbf{直接对差分作估计} \text{（无需解方程）}}✓✓$$
$$\Longrightarrow\ \text{"同余可解性"}\ \textbf{不是} \text{a}_1\ \text{的解放机制} \Longrightarrow \text{V2-9 的第一问／第二问}\ \textbf{依此改写}✓$$

## 4. 变量角色替换审计（$a_1\leftrightarrow a_2$，五问）
$$\text{(1) }a_1\ \text{进入哪个同余关系}？\ \Longrightarrow\ \textbf{不进入任何同余关系}（\text{仅相位差分}）✓$$
$$\text{(2) 求解}\ d',\ell'_2\ \text{等时是否用}\ a_1\ \text{的互素性／范围／固定性／单射性}？\ \Longrightarrow\ \textbf{未使用}✓$$
$$\text{(3) }a_2\ \text{是否具备相同性质}？\ \Longrightarrow\ \text{在}\ \mathscr V^{*}\ \text{中}\ a_2\ \textbf{更弱}（\text{纯自由求和}）✓✓$$
$$\text{(4) 把}\ a_2\ \text{留外层是否仍得有限重数解}？\ \Longrightarrow\ \text{就}\ \mathscr V^{*}\ \textbf{而言}\ a_2\ \textbf{本就不参与} \text{约束，故此项}\ \textbf{不构成障碍}✓$$
$$\text{(5) ⭐ 即便可解，释放}\ a_2\ \text{后的平方和／Weil 对象是否仍可控}？\ \Longrightarrow\ \textbf{本档无法判定}（\text{须看}\ a_2\ \text{在}\ \textbf{§4.1.3.2} \text{的相位角色}）✓$$

## 5. 判定：**C**
$$\boxed{\textbf{C}}：\ \text{同余可解性}\ \textbf{可判} \text{（且结论是"}\ a_1\ \text{不参与约束"），}\ \text{但}\ \textbf{后续估计不足以决定}✓$$
$$\text{不落 A：}\ \text{未完成 envelope 重优化}✓\qquad\text{不落 B：}\ \textbf{未找到} \text{明确不可绕过的结构障碍}✓$$
$$\text{不落 D：}\ a_1\ \text{的角色}\ \textbf{已被严格还原} \text{（虽与先前推断不同）}✓$$

## 6. 由此得到的下一刀（精确化）
$$\text{§4.1.3.1（}\mathscr V^{*}\text{）中}\ a_2\ \text{是自由变量；}\ \text{而}\ a_2\ \text{的}\ \textbf{相位角色} \text{出现在 (4.12) 与}\ \textbf{§4.1.3.2}\（\text{the case}\ (d,\ell_1,\ell_2)\ne(d',\ell'_1,\ell'_2)\text{）}✓$$
$$\Longrightarrow\ \boxed{\text{下一刀：读 §4.1.3.2，定位}\ a_2\ \text{在相位／条件中的位置}} \Longrightarrow \text{五问中的 (5) 才可判}✓✓$$

## 7. 残余（不得省略）
$$\text{残余 1：}\ \mathscr V\ (\text{而非}\ \mathscr V^{*})\ \text{的对应结构未读}✓$$
$$\text{残余 2：}F(\cdot)\ \text{中}\ n'_2\ \text{被"get rid of"的具体代换未取全}✓$$
$$\text{残余 3：}D_b\ \text{六项中另四项仍未逐项溯源；残余 A--D 不变}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 不假设释放成功；}\ \text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 9. 净产出
$$\text{(i) }\mathscr V^{*}\ \text{三段式完整还原（PDF 逐字）}✓$$
$$\text{(ii) ⭐⭐ }a_1\ \textbf{仅以差分}\ (a_1-a'_1)\ \text{出现，}\ \textbf{不进入任何同余条件}✓✓$$
$$\text{(iii) ⭐ }a_2\ \text{在}\ \mathscr V^{*}\ \text{中}\ \textbf{仅为自由求和范围}✓✓$$
$$\text{(iv) ⚠️ 勘误 T10：V2-8b 的"同余可解性解放机制"}\ \textbf{不成立} \text{，正确表述＝"}$a_1$\ 只以差分出现"✓$$
$$\text{(v) 判定}\ \textbf{C}；\ \text{下一刀＝§4.1.3.2 定位}\ a_2\ \text{的相位角色}✓$$
