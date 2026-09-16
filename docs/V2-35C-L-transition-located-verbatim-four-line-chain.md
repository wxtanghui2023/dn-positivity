# V2-35-C — **$L_{\rm transition}$ 已精确落位**：(4.29) 是**四行链**，逐字证实 $L^5=L^2\cdot L^2\cdot L$

> 唐先生 2026-09-16 22:46 逐行重算 → $L^5=L^1_{\rm Weil}\cdot L^1_{\rm transition}\cdot L^2_{\ell_2,\ell_2'}\cdot L^1_u$ ✓
> 本档：本地 HTML **逐字取证** (4.26)--(4.29)，落位 $L_{\rm transition}$✓

---

## 1. ⭐⭐⭐ (4.29) 的**四行链**（逐字）
$$\textbf{第 1 行}：\ \ll\|\nu\|^2\frac{A^2\,\boxed{L^1}\,N^{3/2}M^\varepsilon}{\mathfrak p_1\mathfrak p_2}\operatorname*{\sum\sum\sum\sum}_{\substack{\ell_1,\ell_2,\ell_1',\ell_2'\in\mathcal L\\\mathfrak p_1,\mathfrak q_1|(\ell_1,\ell_1'),\ \mathfrak p_2,\mathfrak q_2|(\ell_2,\ell_2')\\(\ell_2',b\mathfrak q_1\mathfrak p_2)=1}}\sum_{\substack{u|b\mathfrak q_1\mathfrak p_2,\ u\le\frac{10DL}{\mathfrak q_1\mathfrak p_2}\\\mathfrak p_1\tilde\ell_1\equiv\mathfrak p_1\overline{\tilde\ell_2'}\tilde\ell_2\tilde\ell_1'\ (\mathrm{mod}\ u)}}\operatorname*{\sum\sum}_{\substack{|d|,|d'|\le D/\mathfrak q_1\mathfrak p_2\\ d\equiv\overline{\tilde\ell_2'}\tilde\ell_2d'\ (\mathrm{mod}\ u)}}u\Bigl(1+\tfrac{|\vartheta|AD}{bLN^2}\Bigr)✓$$
$$\textbf{第 2 行}：\ \ll\|\nu\|^2\frac{A^2\,\boxed{D^1L^2}\,N^{3/2}M^\varepsilon}{(\mathfrak p_1+\mathfrak q_1)\mathfrak p_1\mathfrak q_1\mathfrak p_2^2}\operatorname*{\sum\sum}_{\ell_2,\ell_2'\in\mathcal L,\ \mathfrak p_2,\mathfrak q_2|(\ell_2,\ell_2')}\sum_{\substack{u|b\mathfrak q_1\mathfrak p_2\\u\le\frac{10DL}{\mathfrak q_1\mathfrak p_2}}}u\Bigl(\frac Lu+1\Bigr)\Bigl(\frac{D}{u\mathfrak q_1\mathfrak p_2}+1\Bigr)\Bigl(1+\tfrac{|\vartheta|AD}{bLN^2}\Bigr)✓✓$$
$$\textbf{第 3 行}：\ \ll\|\nu\|^2\frac{A^2D^1L^2N^{3/2}M^\varepsilon}{(\mathfrak p_1+\mathfrak q_1)\mathfrak p_1\mathfrak q_1\mathfrak p_2^2}\operatorname*{\sum\sum}_{\ell_2,\ell_2'}\boxed{\frac{DL}{\mathfrak q_1\mathfrak p_2}}\Bigl(1+\tfrac{|\vartheta|AD}{bLN^2}\Bigr)✓✓$$
$$\textbf{第 4 行}：\ \ll\frac{\|\nu\|^2A^2\,\boxed{D^2L^5}\,N^{3/2}M^\varepsilon}{(\mathfrak p_1+\mathfrak q_1)(\mathfrak p_2+\mathfrak q_2)\mathfrak p_1\mathfrak q_1^2\mathfrak p_2^3\mathfrak q_2}\Bigl(1+\tfrac{|\vartheta|AD}{bLN^2}\Bigr)\tag{4.29}✓✓✓$$

## 2. ⭐⭐⭐ $L_{\rm transition}$ 落位（第 1→2 行）
$$\text{第 1 行}\to\text{第 2 行}\ \textbf{发生了什么}：\ \operatorname*{\sum\sum\sum\sum}_{\ell_1,\ell_2,\ell_1',\ell_2'}\ \longrightarrow\ \operatorname*{\sum\sum}_{\ell_2,\ell_2'} \Longrightarrow \boxed{\ell_1,\ell_1'\ \textbf{两个求和被执行掉}}✓✓$$
$$\qquad\text{收益}：\ L^1\to\boxed{DL^2} \Longrightarrow \text{新增}\ \boxed{DL^1}；\ \text{且分母变为}\ (\mathfrak p_1+\mathfrak q_1)\mathfrak p_1\mathfrak q_1\mathfrak p_2^2✓✓$$
$$\Longrightarrow\ \boxed{L_{\rm transition}\ =\ \#\{(\ell_1,\ell_1')\ \text{admissible}\}\ \asymp\ L^1}✓✓✓$$
$$\qquad(\text{且}\ D^1\ \text{来自}\ |d|,|d'|\le D/(\mathfrak q_1\mathfrak p_2)\ \text{的区间})✓✓$$

## 3. ⭐⭐ 第 2→3 行与第 3→4 行
$$\text{第 2}\to\text{3}：\ \text{对}\ c\ \text{用 (4.29)/丢条件后，}\ u\text{-计数}\ \sum_{u\mid b\mathfrak q_1\mathfrak p_2}u\bigl(\tfrac Lu+1\bigr)\bigl(\tfrac{D}{u\mathfrak q_1\mathfrak p_2}+1\bigr)\ \longrightarrow\ \boxed{\frac{DL}{\mathfrak q_1\mathfrak p_2}}✓✓$$
$$\qquad\Longrightarrow\ \boxed{L_u\asymp L^1}（\text{来自}\ u\cdot\tfrac Lu\ \text{的显式}\ L；\ \text{除以}\ \mathfrak q_1\mathfrak p_2\ \text{的除因子）}✓✓$$
$$\text{第 3}\to\text{4}：\ \operatorname*{\sum\sum}_{\ell_2,\ell_2'}\ \text{求值} \Longrightarrow \boxed{L^2}（\text{配除因子}\ (\mathfrak p_2+\mathfrak q_2)\mathfrak q_2）✓✓$$

## 4. ⭐⭐⭐ 精确账本（与唐先生结论逐字吻合，并含一处机制细化）
$$\boxed{L^5\ =\ \underbrace{L^2}_{\textbf{外层：}\ell_1,\ell_1'\ \text{对}}\times\underbrace{L^2}_{\ell_2,\ell_2'\ \text{对}}\times\underbrace{L^1}_{u\text{-计数}}}✓✓✓\qquad 2+2+1=5✓$$
$$\textbf{机制细化}：\ \text{外层}\ L^2\ \text{的两个}\ L\ \textbf{各有出处}：$$
$$\qquad\text{(a)}\ \boxed{L^1}\ \text{来自}\ \textbf{Lemma 1（Weil）的开方}：\ \text{逐字}\ (\mathfrak p_1,\mathfrak q_1)\Bigl(\frac{N\tilde\ell_1\tilde\ell_1'}{(\mathfrak p_1,\mathfrak q_1)\mathfrak p_2}\Bigr)^{1/2}\Longrightarrow \ \sqrt{\tilde\ell_1\tilde\ell_1'}\approx L✓✓✓$$
$$\qquad\qquad(\textbf{故}\ L_{\rm Weil}\ \text{的}\ L\ \textbf{实为}\ \ell_1,\ell_1'\ \text{的互补因子经 Weil 开方所得}——\textbf{不是} \text{纯模数尺度})✓✓$$
$$\qquad\text{(b)}\ \boxed{L^1}\ \text{来自}\ \ell_1,\ell_1'\ \text{的}\ \textbf{计数}（=L_{\rm transition},\ \text{见 §2}）✓✓$$
$$\Longrightarrow\ \boxed{\text{四个}\ \ell\ \textbf{各贡献}\ L^1\ \Longrightarrow\ L^4；\quad \text{第五个}\ L\ \text{来自}\ u\text{-计数}}✓✓✓$$
$$\qquad(\text{其中}\ \ell_1,\ell_1'\ \text{的}\ L^1\ \text{以"Weil 开方＋计数"两种方式各出一半})✓$$

## 5. ⭐ 两个攻击点的精确形式
$$\textbf{攻击点 A（}L_{\rm transition}\text{）}：\ \boxed{\#\{(\ell_1,\ell_1')\}\asymp L\ \text{是真自由度还是粗估？}}✓✓$$
$$\qquad\text{且注意}\ \textbf{不对称}：\ \ell_1,\ell_1'\Rightarrow L^1\ \text{而}\ \ell_2,\ell_2'\Rightarrow L^2✓✓$$
$$\qquad\qquad\text{原因（结构）}：\ (\ell_1,\ell_1')\ \text{受}\ (4.27)\ \text{的}\ \textbf{同余}\ \mathfrak p_1\tilde\ell_1\equiv\mathfrak p_1\overline{\tilde\ell_2'}\tilde\ell_2\tilde\ell_1'\ (\mathrm{mod}\ u)\ \text{约束}；\ (\ell_2,\ell_2')\ \text{只有整除条件}✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{\ell_2,\ell_2'\ \text{的}\ L^2\ \text{是四个}\ \ell\ \text{中最"自由"的一层}}⇒\textbf{新的候选攻击点}✓✓$$
$$\textbf{攻击点 B（}L_u\text{）}：\ \boxed{u=(\tilde\ell_2'd-\tilde\ell_2d',b\mathfrak q_1\mathfrak p_2)\ \text{是 gcd 诱导参数}，\textbf{非} \text{自由变量}}✓✓$$
$$\qquad\text{且}\ u\le\frac{10DL}{\mathfrak q_1\mathfrak p_2}\ \text{的截断}\ \textbf{已用非对角条件}（\text{逐字}：\text{若}\ u>\dots\Rightarrow\tilde\ell_2'd=\tilde\ell_2d'\Rightarrow u=b\mathfrak q_1\mathfrak p_2,\ d=d',\ \ell_2=\ell_2'\Rightarrow(d,\ell_1,\ell_2)=(d',\ell_1',\ell_2')\ \text{已被排除}）✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{L_u\ \text{已部分吸收非退化结构} \Longrightarrow \text{从}\ u\text{-计数直接取}\ L^{-\delta}\ \text{难度高于普通粗计数优化}}✓✓$$

## 6. 判定
$$\boxed{L^5\ \textbf{已不是一个模糊的"分划成本"}}：\ \text{它}\ \textbf{具体分解为}\ L^1_{\rm Weil}\cdot L^1_{\rm transition}\cdot L^2_{\ell_2,\ell_2'}\cdot L^1_u✓✓$$
$$\qquad\textbf{但}：\ \textbf{不} \text{宣布不可避免／可优化} \Longrightarrow \text{记}\ \mathrm{OPEN}（\text{两个攻击点已具体化}）✓✓$$
$$\qquad\text{三种结果仍适用}：\ \mathrm A\ \text{可优化幂次}\Rightarrow\text{F5 新入口}；\ \mathrm B\ \text{独立结构来源}\Rightarrow\text{局部机制锁定}；\ \mathrm C\ \text{耦合}\Rightarrow\mathrm{OPEN}✓$$

## 7. 附带逐字取到（(4.26)--(4.28)）
$$u：＝(\tilde\ell_2'd-\tilde\ell_2d',\ b\mathfrak q_1\mathfrak p_2),\qquad v：＝(\tilde\ell_2'd-\tilde\ell_2d')/u\quad(\text{故}\ (v,b\mathfrak q_1\mathfrak p_2/u)=1)✓✓$$
$$(4.26)：\ \tilde\ell_2'd\equiv\tilde\ell_2d'\ (\mathrm{mod}\ u)✓\qquad(4.27)：\ \mathfrak p_1\tilde\ell_1\equiv\mathfrak p_1\overline{\tilde\ell_2'}\tilde\ell_2\tilde\ell_1'\ (\mathrm{mod}\ u)✓✓$$
$$(4.28)：\ c\equiv-\overline{v\eta}\frac{(\tilde\ell_2'\tilde\ell_1-\tilde\ell_2\tilde\ell_1')\mathfrak p_1n_1'}{u}\ \Bigl(\mathrm{mod}\ \frac{b\mathfrak q_1\mathfrak p_2}{u}\Bigr)✓✓$$
$$\text{Lemma 1 输出逐字}：\ G(\cdots)\ll M^\varepsilon\Bigl((\mathfrak p_1,\mathfrak q_1)\bigl(\tfrac{N\tilde\ell_1\tilde\ell_1'}{(\mathfrak p_1,\mathfrak q_1)\mathfrak p_2}\bigr)^{1/2}+\tfrac{(\vartheta\Delta,\gamma_1)}{\gamma_1}\tfrac{N}{b\eta\mathfrak q_1^2\mathfrak q_2\mathfrak p_2[d,d']}\Bigr)\ll M^\varepsilon\bigl(LN^{1/2}+\dots\bigr)✓✓✓$$
$$\text{且}\ n_2'\ \text{的区间}：\ \text{"a finite union of intervals of length at most}\ O(N/\mathfrak q_1\mathfrak q_2)\text{"}\ \text{＋同余}\ (\mathrm{mod}\ b\mathfrak q_1\mathfrak p_2[d,d']\eta)✓$$

## 8. 残余（不得省略）
$$\text{残余 1：}L_{\rm transition}\ \text{的}\ \#\{(\ell_1,\ell_1')\}\ \textbf{计数方式未逐行核}（\text{是否含粗估}）✓✓$$
$$\text{残余 2：}\ \ell_2,\ell_2'\ \text{的}\ L^2\ \text{是否可再压（只受整除条件＋}\mathfrak p_2,\mathfrak q_2\ \text{除因子）}✓✓$$
$$\text{残余 3：}L_u\ \text{的}\ \tfrac{DL}{\mathfrak q_1\mathfrak p_2}\ \text{是否已最优（截断已用非对角条件）}✓\quad\text{残余 4：A--D 不变}✓$$

## 9. 边界（N1/N2 严守）
$$\text{① 只做}\ L^5\ \text{逐幂溯源；}\quad\text{② }\textbf{不碰} \ F_5\ \text{envelope}；\quad\text{③ }\textbf{不} \text{宣布 A/B/C}；\quad\text{④ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 10. 净产出
$$\text{(i) ⭐⭐⭐ (4.29) 四行链逐字取出} \Longrightarrow \boxed{L_{\rm transition}\ \text{＝第 1}\to\text{2 行的}\ \ell_1,\ell_1'\ \text{计数}\asymp L^1}✓✓✓$$
$$\text{(ii) ⭐⭐⭐ 精确账本：}\ L^5=L^2_{(\ell_1,\ell_1')}\cdot L^2_{(\ell_2,\ell_2')}\cdot L^1_{u}\ \text{（与唐先生结论吻合）}✓✓✓$$
$$\text{(iii) ⭐⭐⭐ 机制细化：外层}\ L^2\ \text{＝Weil 开方}\ \sqrt{\tilde\ell_1\tilde\ell_1'}\approx L\ \textbf{＋}\ \ell_1,\ell_1'\ \text{计数}\approx L✓✓$$
$$\text{(iv) ⭐⭐ 不对称发现：}\ \ell_1,\ell_1'\Rightarrow L^1\ \text{（受 (4.27) 同余约束）}，\ \ell_2,\ell_2'\Rightarrow L^2 \Longrightarrow \boxed{\ell_2,\ell_2'\ \text{最自由}}✓✓$$
$$\text{(v) ⭐⭐ }L_u\ \text{的截断已用非对角条件（逐字）}\Longrightarrow \text{取}\ L^{-\delta}\ \text{难度高于粗计数优化}✓✓$$
