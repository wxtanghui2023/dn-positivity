# V2-35 — **(4.4) 全文取到** ⟹ $P,Q$ **不是自由分划参数，而是 $n$ 与 $\ell$ 的 gcd**

> 唐先生 2026-09-16 22:41「继续 V2-35」✓
> 问题：$\boxed{PQ\asymp L\ \text{是否是不可避免的参数分划成本？}\ \text{若改变}\ P,Q\ \text{分划使有效}\ PQ<L^{1-\delta}，\ \text{是否会破坏 (4.29) 的互反／Weil 结构？}}$✓
> 取证：本地 HTML 逐字（外部来源，仅作数据）✓

---

## 1. ⭐⭐⭐ (4.4) 逐字：$P,Q$ 的定义
$$\boxed{n_1'：＝\frac{n_1}{(n_1,\ell_1\ell_2)}=\frac{n_1}{\mathfrak p_1\mathfrak p_2},\qquad \mathfrak p_2=(\ell_2,n_1),\quad \mathfrak p_1=(\ell_1,n_1)}✓✓✓$$
$$\boxed{n_2'：＝\frac{n_2}{(n_2,\ell_1\ell_2)}=\frac{n_2}{\mathfrak q_1\mathfrak q_2},\qquad \mathfrak q_1=(\ell_1,n_2),\quad \mathfrak q_2=(\ell_2,n_2)}✓✓✓$$
$$\qquad\text{原文附注}：\ \text{"and notice that, for square-free integers}\ n_1,n_2\text{, this automatically gives}\ (\ell_1\ell_2,n_1'n_2')=1\text{"}✓$$
$$\Longrightarrow\ \boxed{\mathfrak p_1\mathfrak p_2\,|\,n_1},\quad \boxed{\mathfrak q_1\mathfrak q_2\,|\,n_2} \Longrightarrow \textbf{P,Q 由}\ n_j\ \text{相对于}\ \ell_i\ \text{的因子结构}\ \textbf{完全决定}}✓✓✓$$

## 2. ⭐⭐⭐ 对 V2-35 问题的直接含义
$$\boxed{\text{"分划"}\ \textbf{不是自由参数}，\ \text{而是}\ \textbf{变量替换}}：\ (n_1,n_2)\ \longleftrightarrow\ (n_1',n_2',\mathfrak p_1,\mathfrak p_2,\mathfrak q_1,\mathfrak q_2)✓✓$$
$$\qquad\Longrightarrow\ \text{"改变}\ P,Q\ \text{的分划"}\ \textbf{在变量层面没有对应物}：\ \text{给定}\ n_j\ \text{与}\ \ell_i，\ \text{四个 gcd}\ \textbf{唯一确定}✓✓$$
$$\Longrightarrow\ \boxed{\text{V2-35 的原始问题（作为"自由参数优化"）}\ \textbf{不成立}}✓✓$$
$$\qquad(\text{即：不存在"把}\ PQ\ \text{压小"的操作——你只能改变}\ \textbf{如何命名} \text{这些因子，不能改变它们是什么})✓$$

## 3. ⚠️ 连带修正：$L^5$ 中的"$L_{PQ}$"归属须重定位
$$\text{此前（V2-33 系列）写}\ L^5=L^4_{\ell\text{-count}}\times L_{PQ} \Longrightarrow \textbf{现须修正}：\ \text{既}\ P,Q\ \text{非自由参数}，\ \text{则那个}\ L\ \textbf{不是"分划成本"}✓✓$$
$$\qquad\textbf{真正来源须在 (4.29) 三步中逐项定位}：$$
$$\qquad\text{第 1 式}：\ \frac{A^2\boxed{L}N^{3/2}}{p_1p_2}\operatorname*{\sum\sum\sum\sum}_{\ell_1,\ell_2,\ell_1',\ell_2'}\dots \Longrightarrow \text{含显式}\ L（\text{＋四个}\ \ell\text{-求和）}✓$$
$$\qquad\text{第 2 式}：\ \frac{A^2\boxed{DL^2}N^{3/2}}{(p_1+q_1)p_1q_1p_2^2}\operatorname*{\sum\sum}_{\ell_2,\ell_2'}\frac{\boxed{DL}}{q_1p_2}✓$$
$$\qquad\text{第 3 式}：\ \frac{A^2\boxed{D^2L^5}N^{3/2}}{(p_1+q_1)(p_2+q_2)p_1q_1^2p_2^3q_2}✓$$
$$\Longrightarrow\ \boxed{\text{须重述问题}：\ \text{(4.29) 中}\ L^5\ \text{的每一幂}\ \textbf{哪一来自结构必需，哪一来自可优化选择？}}✓✓$$

## 4. 判定
$$\boxed{\text{V2-35 原始形式（"是否为自由分划成本"）}\ \textbf{已消解}}：\ P,Q\ \textbf{非自由}✓✓$$
$$\boxed{\text{重述后的问题}\ \textbf{OPEN}}：\ \text{(4.29) 的}\ L^5\ \text{逐幂溯源}✓✓$$
$$\qquad\Longrightarrow\ \textbf{不} \text{宣布"不可避免"／"可优化"；}\ \textbf{须} \text{逐项核 (4.26)--(4.29)}✓$$

## 5. 附带取到的高价值原文（(4.1)--(4.2)）
$$(4.1)：\ \mathscr O_b=\mathscr E_{b,1}+\mathscr E^*_{b,1}\quad(\text{按}\ (\ell_1,\ell_2)=1\ \text{与否分})✓$$
$$(4.2)：\ \mathscr E_{b,\eta}：＝\operatorname*{\sum\sum\sum\sum\sum\sum\sum}_{\substack{\ell_1,\ell_2\in\mathcal L,\ m\in\mathcal M,\ n_1,n_2\in\mathcal N,\ a_1,a_2\in\mathcal A\\(mb\vartheta,\ell_1\ell_2n_1n_2)=(m,b)=(\ell_1,\ell_2)=1,\ \eta|m,\\\ell_1n_1\equiv\ell_2n_2\ (\mathrm{mod}\ m),\ \ell_1n_1\ne\ell_2n_2}}\beta_{n_1}\nu_{a_1}\overline{\beta_{n_2}\nu_{a_2}}\operatorname{e}\Bigl(\vartheta\frac{a_1\overline m}{bn_1}-\vartheta\frac{a_2\overline m}{bn_2}\Bigr)✓✓$$
$$\qquad\Longrightarrow\ \text{对角条件}\ \ell_1n_1\equiv\ell_2n_2\ (\mathrm{mod}\ m)\ \text{＋非退化}\ \ell_1n_1\ne\ell_2n_2\ \text{逐字确认}✓✓$$

## 6. 残余（不得省略）
$$\text{残余 1（关键）：}\ L^5\ \text{的逐幂溯源未做（须 (4.26)--(4.29) 逐步核）}✓✓$$
$$\text{残余 2：}\ \mathfrak p,\mathfrak q\ \textbf{在 (4.9) 中被求和}（\text{范围}\ \mathcal L\cup\{1\}\text{）}\ \text{与其"唯一确定"的关系须厘清}（\text{即：为何}\ \textbf{可} \text{对 gcd 求和}）✓✓$$
$$\text{残余 3：}\ \sum_{\mathfrak p,\mathfrak q}\ \text{的计数成本未算（猜想：d(n)$\asymp L^{o(1)}$ 型）}✓\quad\text{残余 4：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只做}\ P,Q\ \text{身份审计；}\quad\text{② }\textbf{不} \text{宣布不可避免／可优化；}\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) ⭐⭐⭐ (4.4) 全文：}\ \mathfrak p_i=(\ell_i,n_1)、\mathfrak q_i=(\ell_i,n_2) \Longrightarrow \boxed{P,Q\ \textbf{是 gcd，非自由分划参数}}✓✓✓$$
$$\text{(ii) ⭐⭐⭐ V2-35 原始问题}\ \textbf{已消解}（\text{"改变分划"无变量层面对应物}）✓✓$$
$$\text{(iii) ⚠️ 连带修正：}\ L^5\ \text{中的"}\ L_{PQ}\text{"归属须重定位；}\ \text{重述为}\ \boxed{\text{(4.29) 的}\ L^5\ \text{逐幂溯源}}✓✓$$
$$\text{(iv) ⭐⭐ 附带取到 (4.1)/(4.2) 逐字（对角条件}\ \ell_1n_1\equiv\ell_2n_2\pmod m\ \text{＋非退化）}✓✓$$
$$\text{(v) 判定：原形式消解；重述形式}\ \textbf{OPEN}✓$$
