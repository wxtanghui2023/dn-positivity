# T3-1B · **$(\ell_2,\ell_2')$-fiber 的振荡结构**（第一刀）

> 依唐先生 2026-09-17 09:27 指令｜**优先 T3-1B**（唯一不与 T2-1 矛盾、又可能直接吃掉 $L^2$ 的入口）✓
> 判定档：$\mathrm{ALIVE}\ /\ \mathrm{GAP}\ /\ \mathrm{DEAD}$；**ALIVE 须有可写成公式的新信息流**✓
> 材料：`docs/ref-bc-ar5iv-plaintext.txt`（BC 逐字）✓

---

## 1. ⭐⭐⭐ (4.11) 相位（逐字，L281）

$$\vartheta\Bigg(\overline{c}(a_1-a_1')\frac{\overline{\mathfrak p_1n_1'}}{b\mathfrak p_2}-\underbrace{\frac{(da_1\tilde\ell_2'-d'a_1'\tilde\ell_2)\overline{\tilde\ell_2\tilde\ell_2'b\mathfrak p_2\mathfrak q_2n_2'}}{\mathfrak p_1n_1'}}_{\textbf{项 2：}(\ell_2,\ell_2')\ \text{在此}}+\ldots\Bigg)✓$$
$$\text{项 2 的}\ (\tilde\ell_2,\tilde\ell_2')\text{-依赖}：\ \textbf{线性}（da_1\tilde\ell_2'-d'a_1'\tilde\ell_2）\ \times\ \textbf{乘积之逆}（\overline{\tilde\ell_2\tilde\ell_2'C_0}），\ C_0：＝b\mathfrak p_2\mathfrak q_2n_2'✓✓$$

$$\Longrightarrow\ \text{链对}\ \sum_{\ell_2,\ell_2'}\ \text{用的是}\ \textbf{trivial count}（\text{Line3/4 的}\ \sum\sum_{\ell_2,\ell_2'}\ \text{无显式 summand 依赖}）\ \Longrightarrow\ \textbf{振荡被整段丢弃}✓✓$$

---

## 2. ⭐⭐⭐ **NEW：展开后相位**可分****（逆元素的乘法性）

$$\text{关键：}\ \overline{xy}\equiv\overline{x}\,\overline{y}\ \text{（乘法性，在}\ (xy,\text{modulus})=1\ \text{时）}✓$$
$$\qquad\text{(4.10) 自带}\ (\ell_2',b\mathfrak q_1\mathfrak p_2)=1\ \text{与}\ (b\vartheta n_1'n_2',\ell_1\ell_2\ell_1'\ell_2')=1 \Longrightarrow \textbf{互素条件满足}✓✓$$

$$\text{故}\quad \tilde\ell_2'\cdot\overline{\tilde\ell_2\tilde\ell_2'C_0}=\overline{C_0}\cdot\tilde\ell_2'\overline{\tilde\ell_2}\overline{\tilde\ell_2'}=\overline{C_0}\,\overline{\tilde\ell_2}\quad(\text{因}\ \tilde\ell_2'\overline{\tilde\ell_2'}\equiv1)✓✓$$
$$\qquad\quad \tilde\ell_2\cdot\overline{\tilde\ell_2\tilde\ell_2'C_0}=\overline{C_0}\,\overline{\tilde\ell_2'}✓✓$$

$$\boxed{\text{项 2}\ \stackrel{\text{展开}}{=}\ -\frac{\vartheta\overline{C_0}}{\mathfrak p_1n_1'}\Big(\underbrace{da_1\,\overline{\tilde\ell_2}}_{\text{只含}\tilde\ell_2}\ -\ \underbrace{d'a_1'\,\overline{\tilde\ell_2'}}_{\text{只含}\tilde\ell_2'}\Big)}✓✓✓$$
$$\Longrightarrow\ \boxed{\textbf{相位可分}：\ \text{项 2}\ =\ f(\overline{\tilde\ell_2})+g(\overline{\tilde\ell_2'})}✓✓✓$$

---

## 3. ⭐⭐ 唯一的耦合：**线性同余 (4.26)**

$$\text{除可分相位外，}\tilde\ell_2\ \text{与}\ \tilde\ell_2'\ \text{之间}\ \textbf{只} \text{通过下列条件耦合}：$$
$$\qquad\text{(i)}\ \text{(4.26)}：\ \tilde\ell_2'd\equiv\tilde\ell_2d'\ \mathopen{}\mathclose{{\left(\textnormal{mod}\penalty\ u}}\right)\quad(\textbf{线性}！)✓✓$$
$$\qquad\text{(ii)}\ \text{整除}：\ \mathfrak p_2,\mathfrak q_2\mid(\ell_2,\ell_2')\ \text{（各自独立）}✓$$
$$\qquad\text{(iii)}\ (\ell_2',b\mathfrak q_1\mathfrak p_2)=1,\ (\ell_2,\ell_2')=1\ \text{型互素}✓$$

$$\Longrightarrow\ \text{对象形状}：\ \boxed{\sum_{\tilde\ell_2}e\big(f(\overline{\tilde\ell_2})\big)\cdot G_u(\tilde\ell_2\bmod u)}✓✓$$
$$\qquad\text{（}G_u\ \text{为只依赖}\ \tilde\ell_2\bmod u\ \text{的周期函数，(4.26) 的产物）}✓$$

---

## 4. ⭐⭐⭐ 判定：**ALIVE（有条件）**

$$\text{单变量因子的完整和是}\ \textbf{Ramanujan 和}：\ \sum_{x\bmod q,(x,q)=1}e(a\overline{x}/q)=c_q(a)\ \text{（代}\ y=\overline{x}\text{）}✓✓$$
$$\qquad\Longrightarrow\ \text{短区间（}\textbf{不完全}）版本经补全：\ \sum_{x\le X}e(\alpha\overline{x}/q)\ll\sqrt{q}\,\log^{O(1)}q✓✓$$
$$\Longrightarrow\ \textbf{每因子增益}\ \asymp\ \frac{X}{\sqrt q}\quad\big(X：＝\frac{L}{\mathfrak p_2\mathfrak q_2}\ \text{（}\tilde\ell_2\ \text{的区间长）}，\ q\ \text{为相位振动的模数}\big)✓✓$$

$$\boxed{\text{ALIVE 的条件}：\ X\gg\sqrt q\quad(\text{区间长超过模数的平方根}）⟹ \text{真正幂次增益}}✓✓$$
$$\qquad\text{反例边界}：X\lesssim\sqrt q\ \text{时}\ \textbf{trivial count}\ \text{已最优} \Longrightarrow \text{该支在该区间}\ \textbf{不退化为新架构}✓$$

$$\textbf{ALIVE 所要求的"可写成公式的新信息流"}：$$
$$\boxed{\sum_{\tilde\ell_2,\tilde\ell_2'}^{\text{(4.26)}}e\Big(-\tfrac{\vartheta\overline{C_0}}{\mathfrak p_1n_1'}\big(da_1\overline{\tilde\ell_2}-d'a_1'\overline{\tilde\ell_2'}\big)\Big)\ \asymp\ \Big(\sum_{\tilde\ell_2}e(\alpha\overline{\tilde\ell_2})G_u\Big)\ \textbf{（不完全线性逆和 × 模}\ u\ \text{周期权重）}}✓✓✓$$
$$\qquad\text{它与链的}\ \#\{\ell_2\}\#\{\ell_2'\}\max|\cdot|\ \textbf{是两种不同的信息流}✓✓$$

---

## 5. 对 T2-1 的关系（唐先生指定的要点）

$$\textbf{T2-1 给出}\ \#\{(\ell_2,\ell_2')\}=L^{2+o(1)}（\textbf{点数饱和}）；\ \text{本节给出的是}\ \textbf{指标和} \text{（振荡和）}✓$$
$$\qquad\Longrightarrow\ \boxed{\text{点数饱和}\ \ne\ \text{振荡和饱和}；\ \textbf{T2-1 不杀掉 cancellation architecture}}✓✓✓$$
$$\qquad\text{本支}\ \textbf{绕开} \text{T2-1（不否定它）}：\ \text{把}\ L^2\ \text{从"自由变量数"改成"振荡和的量级"}✓$$

---

## 6. 残余（**登记，不掩盖**）

$$\textbf{R1}：\ \text{相位模数}\ q\ \text{的精确值（是}\ \mathfrak p_1n_1'？\ b\mathfrak p_2\mathfrak q_2n_2'？\ \text{其组合？）}\ \textbf{未定} ⟹ \text{增益量级}\ X/\sqrt q\ \text{是}\ [\textbf{结构判定}]✓$$
$$\textbf{R2}：\ \text{不完全和的补全型界（}\ll\sqrt q\log^{O(1)}q\text{）}\ \textbf{未逐字核} \text{（属经典方法，但本档未引原文）}✓$$
$$\textbf{R3}：\ G_u\ \text{的显式形式（周期权重）}\ \textbf{未写出}✓$$
$$\textbf{R4}：\ \text{与 (4.11) 项 1／项 3 的相互作用（项 3 含}\ \tilde\ell_1,\tilde\ell_1'\ \text{，已被 (4.27) 消去）}\ \textbf{未核}✓$$
$$\textbf{R5}：\ \text{该区间条件}\ X\gg\sqrt q\ \text{在 BC 应用参数（}\theta<17/33\text{）下}\ \textbf{是否成立}\ \textbf{未核}✓✓\quad(\textbf{这一项决定 ALIVE 是否可用})✓$$

$$\Longrightarrow\ \textbf{下一刀（T3-1B-2）}：\ \text{定}\ q\ \text{与}\ X\ \text{的精确值} \to \text{判定}\ X\gg\sqrt q\ \text{是否在应用参数下成立}✓$$

## 7. 边界

$$\text{(i)}\ \text{本节结论}\ \textbf{限定 BC §4.1.2--§4.1.3 的已读范围}✓\quad\text{(ii)}\ \text{可分性与耦合结构}\ \textbf{为本档推导}（\text{逆元素乘法性，初等}）✓$$
$$\text{(iii)}\ \text{增益量级}\ X/\sqrt q\ \text{为}\ [\textbf{结构判定}]，\ \textbf{非定理}✓\quad\text{(iv)}\ \text{未用 RH；零数值}✓$$
