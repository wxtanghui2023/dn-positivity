# T3-1B-2 · **R1→R5 硬审计**（逐式归一化）⟹ 判定 **DEAD**

> 依唐先生 2026-09-17 09:30 指令：**不得从化简相位反推模数**；须回 (4.10)(4.11)(4.26)(4.29) 原始定义逐行核 ✓
> **原文**：本地已有 `external_refs/bettin_chandee_trilinear_kloosterman_1502.00769.pdf`（476 KB）＋ `docs/ref-bc-ar5iv-plaintext.txt`（112 KB）✓ **无需上传**✓
> 依据行：plaintext L364–L400（(4.15)–(4.21) 逐字）＋ L281（(4.11)）＋ L467–L497（(4.26)–(4.29)）✓

---

## 1. ⭐ 原始定义（逐字，本轮新读）

$$\text{由 (4.9) 内层：}\ \operatornamewithlimits{\sum\nolimits^{*}}_{c\ (\mathrm{mod}\ b\mathfrak q_1\mathfrak p_2)}\ \text{带两条同余}：$$
$$\qquad\tilde\ell_1\mathfrak p_1n_1'\equiv\tilde\ell_2\mathfrak q_2n_2'-cd\eta\ \mathopen{}\mathclose{{\left(\textnormal{mod}\penalty\ b\mathfrak q_1\mathfrak p_2|d|\eta}}\right),\quad \tilde\ell_1'\mathfrak p_1n_1'\equiv\tilde\ell_2'\mathfrak q_2n_2'-cd'\eta\ (\ldots|d'|\eta)✓$$
$$\Longrightarrow\ \text{导出}\ (4.15)：(\tilde\ell_2'\tilde\ell_1-\tilde\ell_2\tilde\ell_1')\mathfrak p_1n_1'+(\tilde\ell_2'd-\tilde\ell_2d')c\eta\equiv0\ \mathopen{}\mathclose{{\left(\textnormal{mod}\penalty\ b\mathfrak q_1\mathfrak p_2\eta}}\right)✓$$
$$\qquad\qquad (4.16)：\ (d'\tilde\ell_1-d\tilde\ell_1')\overline{\mathfrak q_2n_2'}\equiv(d'\tilde\ell_2-d\tilde\ell_2')\overline{\mathfrak p_1n_1'}\ \mathopen{}\mathclose{{\left(\textnormal{mod}\penalty\ b}}\right)，\ \text{因}\ (b,\mathfrak p_1n_1'\mathfrak q_2n_2')=1✓$$
$$\qquad\qquad (4.17)：\ \frac{\overline{\alpha\gamma}}{\beta}+\frac{\overline{\beta\gamma}}{\alpha}+\frac{\overline{\alpha\beta}}{\gamma}\equiv\frac1{\alpha\beta\gamma}\ (\mathrm{mod}\ 1)\quad(\alpha,\beta,\gamma\ \text{两两互素})✓$$
$$\qquad\qquad (4.18)：\ \text{把}\ -\frac{a_2(d\tilde\ell_1'-d'\tilde\ell_1)\overline{\tilde\ell_1\tilde\ell_1'\mathfrak p_1n_1'b\mathfrak q_1}}{\mathfrak q_2n_2'}\ \text{改写为三项（逐字）}✓$$
$$\qquad\qquad (4.19)：\ \text{相位四式；}\ \Delta：＝a_2(d\tilde\ell_1'-d'\tilde\ell_1)\tilde\ell_2\tilde\ell_2'\mathfrak p_2-(da_1\tilde\ell_2'-d'a_1'\tilde\ell_2)\tilde\ell_1\tilde\ell_1'\mathfrak q_1✓$$

$$\Longrightarrow\ \textbf{关键读数}：\text{(4.19) 是}\ \textbf{模 1 的有理数}，\ \text{四个分母}\ \textbf{显式}：$$
$$\qquad \tilde\ell_1\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1'\quad\big|\quad b\tilde\ell_1\tilde\ell_1'\mathfrak p_1n_1'\mathfrak q_1\mathfrak q_2n_2'\quad\big|\quad b\mathfrak p_2\quad\big|\quad b$$
$$\qquad\Longrightarrow\ \textbf{不存在单一固定模数}；\ \text{其中}\ \tilde\ell_1\tilde\ell_1'\mathfrak q_1\ \textbf{是变量}✓✓\quad(\text{故直觉上的"模数}q\text{"须}\ \textbf{导出而非假设}）✓$$

---

## 2. ⭐⭐⭐ R1：相位模数 $q$ **精确确定**

$$\textbf{约定}：\ \overline{x}\ \text{表}\ x\ \text{相对}\ \textbf{该分式之分母} \text{的逆元}✓$$
$$\text{(4.11) 项 2 之逆元}\ \overline{\tilde\ell_2\tilde\ell_2'b\mathfrak p_2\mathfrak q_2n_2'}\ \text{相对分母}\ \mathfrak p_1n_1' ⟹ \boxed{q=\mathfrak p_1n_1'}✓✓✓$$
$$\qquad\text{（一致性：BC 对}\ n_2'\ \text{用 Weil，其逆元}\ \overline{\mathfrak p_1n_1'}\ \text{同样相对}\ b\ \text{——见 (4.16)）}✓$$

### 2.1 展开：变量分母**相消**（本档推导，初等）
$$\overline{\tilde\ell_2\tilde\ell_2'C_0}=\overline{\tilde\ell_2}\,\overline{\tilde\ell_2'}\,\overline{C_0}\quad(C_0：＝b\mathfrak p_2\mathfrak q_2n_2')✓$$
$$\text{(i)}\ \textbf{Δ 的}\ \tilde\ell_2\tilde\ell_2'\ \text{部分}：\ \tilde\ell_2\tilde\ell_2'\overline{\tilde\ell_2}\overline{\tilde\ell_2'}\overline{C_0}\equiv\overline{C_0}\ (\mathrm{mod}\ C_0)\ \Longrightarrow \textbf{无振荡，退化为常数}✓✓$$
$$\text{(ii)}\ \textbf{Δ 的}\ (da_1\tilde\ell_2'-d'a_1'\tilde\ell_2)\tilde\ell_1\tilde\ell_1'\mathfrak q_1\ \text{部分}：\ \text{乘逆元后}\ =\ \overline{C_0}\,\tilde\ell_1\tilde\ell_1'\mathfrak q_1\big(da_1\overline{\tilde\ell_2}-d'a_1'\overline{\tilde\ell_2'}\big)✓$$
$$\text{再除以}\ (4.19)\ \text{项 1 之分母}\ \tilde\ell_1\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1' \Longrightarrow \textbf{变量因子}\ \tilde\ell_1\tilde\ell_1'\mathfrak q_1\ \textbf{恰相消}✓✓✓$$
$$\Longrightarrow\ \boxed{\text{项 1 的}\ (\tilde\ell_2,\tilde\ell_2')\text{-相位}\ =\ -\frac{\vartheta\overline{C_0}}{\mathfrak p_1n_1'}\Big(da_1\overline{\tilde\ell_2}-d'a_1'\overline{\tilde\ell_2'}\Big)，\ \textbf{分母固定为}\ \mathfrak p_1n_1'}✓✓✓$$

$$\text{(iii)}\ \text{互素保证逆元存在}：(\ell_1,\ell_2)=1\Rightarrow(\mathfrak p_1,\tilde\ell_2)=1；\ (\ell_2',b\mathfrak q_1\mathfrak p_2)=1\Rightarrow(\tilde\ell_2',b\mathfrak q_1\mathfrak p_2)=1✓$$

---

## 3. R2：单变量和的性质

$$\text{完整和（代}\ y=\overline{\tilde\ell_2}\text{）}：\ \sum_{x\ (\mathrm{mod}\ \mathfrak p_1n_1')^{*}}e\big(\alpha\overline{x}/(\mathfrak p_1n_1')\big)=c_{\mathfrak p_1n_1'}(\alpha)\quad(\textbf{Ramanujan 和})✓✓$$
$$\text{短区间（}\textbf{不完全}）版本：\ \ll\sqrt{\mathfrak p_1n_1'}\,\log^{O(1)}(\mathfrak p_1n_1')✓\quad[\text{经典补全法，本档未引原文}——\text{残余 R2 保留}]✓$$

---

## 4. ⭐⭐⭐ R3／R4 前置：有效区间长度 $X$ **精确确定**

$$\ell_2=\mathfrak p_2\tilde\ell_2，\ \mathfrak q_2\mid\ell_2 \Longrightarrow \mathfrak p_2\mathfrak q_2\mid\ell_2 \Longrightarrow \tilde\ell_2\ \text{取值数}\ \asymp\frac{L}{\mathfrak p_2\mathfrak q_2}✓✓$$
$$\qquad\Longrightarrow\ \boxed{X\asymp\frac{L}{\mathfrak p_2\mathfrak q_2}}\quad(\textbf{与符号量级一致，但此处由整除结构}\ \textbf{确定}）✓✓$$

---

## 5. ⭐⭐⭐ R5：比值 $\dfrac{X}{\sqrt q}$ 与应用区间

$$\frac{X}{\sqrt q}\ \asymp\ \frac{L/(\mathfrak p_2\mathfrak q_2)}{\sqrt{\mathfrak p_1n_1'}}\qquad\text{而}\ \mathfrak p_1\mathfrak p_2n_1'\in\mathcal N\Longrightarrow\mathfrak p_1n_1'\asymp\frac{N}{\mathfrak p_2}✓$$
$$\Longrightarrow\ \frac{X}{\sqrt q}\asymp\frac{L}{\mathfrak q_2\sqrt{\mathfrak p_2N}}\qquad\Longrightarrow\ \textbf{最优情形}\ (\mathfrak p_2=\mathfrak q_2=1)：\ \text{需}\ \boxed{L\gg\sqrt N}✓✓✓$$

### 5.1 代入平衡最优 $L^*$（(4.29) 的平衡条件）
$$L^*=\frac{M^{4/5}}{b^{1/5}A^{2/5}N^{7/10}}\quad(\text{＝V2-19 已定位的第三单项式}）✓$$
$$\textbf{平衡区}\ M\asymp N：\ L^*\asymp\frac{N^{1/10}}{b^{1/5}A^{2/5}}✓$$
$$\Longrightarrow\ \frac{X}{\sqrt q}\ \asymp\ \frac{N^{1/10}}{\sqrt N}=N^{-2/5}\ \ll\ 1✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{X\ll q^{1/2}\ \Longrightarrow\ \textbf{DEAD（应用区间内无幂次收益）}}✓✓✓$$

$$\textbf{定量理由}：\text{平衡最优把}\ L\ \text{压到}\ \asymp N^{1/10}，\ \text{远低于}\ \sqrt N；\ \text{即}\ \textbf{ℓ-变量区间太短}，\ \text{逆元型振荡}\ \textbf{无法} \text{胜过 trivial count}✓✓$$

---

## 6. ⭐ 判定（三档制）

$$\boxed{\textbf{T3-1B-2}\ =\ \mathrm{DEAD}\quad(X\ll q^{1/2}\ \text{在应用区间成立})}✓✓✓$$
$$\qquad\text{（}\textbf{不是} \text{"无 cancellation"；\ 而是}\ \textbf{"cancellation 存在但尺度不够"}——\text{这正是唐先生要的判别力入口}）✓✓$$

$$\text{且因 R5 已判 DEAD，}\ \textbf{R3／R4 无需再解} \text{（登记为未决）}✓$$
$$\text{R3：}\ G_u\ \text{周期结构}\ \textbf{未写}✓\qquad\text{R4：}\ \text{项 1／2／3 相互作用}\ \textbf{未核}✓$$

---

## 7. 残余（**未掩盖**）

$$\textbf{R5-残余 1}：\ \text{不平衡区}\ M\gg N^{3/2}\ \text{时}\ L^*\gg\sqrt N\ \textbf{可能成立}（\text{由}\ L^*\asymp M^{4/5}/(\ldots N^{7/10})\gg\sqrt N\iff M\gg N^{3/2}）✓\quad\textbf{未核}✓$$
$$\textbf{R5-残余 2}：\ \text{"}\mathfrak p_1\mathfrak p_2n_1'\in\mathcal N\Rightarrow\mathfrak p_1n_1'\asymp N/\mathfrak p_2\text{"}\ \text{属}\ [\textbf{结构判定}]（\text{未逐字核}\ \mathfrak p_2\ \text{与}\ n_1'\ \text{的相对大小}）✓$$
$$\textbf{R2}：\ \text{补全型界}\ \ll\sqrt q\log^{O(1)}q\ \textbf{未引原文}✓\qquad\textbf{R1-残余}：\ \text{若}\ \overline{x}\ \text{的模数惯例与本节假设不同，结论须重核}✓$$

---

## 8. 【勘误 T10】（对 T3-1B 本档）

$$\text{T3-1B 曾把}\ \text{(4.19)}\ \text{的变量分母}\ \tilde\ell_1\tilde\ell_1'\mathfrak q_1\ \text{视为"固定模数的一部分"} \Longrightarrow \textbf{过急}✓$$
$$\qquad\text{正确：}\ \text{固定分母}\ \mathfrak p_1n_1'\ \text{是}\ \textbf{展开后相消的结果}（\text{§2.1}\），\ \text{须}\ \textbf{逐式导出} \text{而非假设}✓✓$$
$$\qquad\Longrightarrow\ \text{T3-1B 的 ALIVE（有条件）}\ \textbf{已被本档降为 DEAD}；\ \text{其"条件}\ X\gg\sqrt q\text{"保留}\ \textbf{未变}，\ \text{只是}\ \textbf{不成立}✓✓$$

## 9. 边界
$$\text{(i)}\ \text{本档结论}\ \textbf{限定 BC §4 的已读范围}✓\quad\text{(ii)}\ \text{§2.1 相消为}\ \textbf{本档推导}（\text{初等}）✓\quad\text{(iii)}\ \text{§5.1 用}\ L^*\ \text{属（V2-19）已定位结果}✓$$
$$\text{(iv)}\ \textbf{未用 RH；零数值}✓$$
