# T2-1 ＋ T2-2 · **fiber 饱和 ＋ 除因子对齐**（BC 架构闭合两刀）

> 依唐先生 2026-09-17 09:23 指令（T2 只做两刀；目标＝把「sharp within BC architecture」做成可审计闭环）✓
> 材料：`docs/ref-bc-ar5iv-plaintext.txt`（BC 全文，逐字）✓｜**纪律**：不用 "u<L ⟹ 同余有解" 型跳步 ✓

---

## 0. ⭐⭐⭐ 关键定义（逐字，L216／L279 —— 本轮新增）

$$\boxed{\tilde\ell_1:=\frac{\ell_1}{\mathfrak q_1},\quad\tilde\ell_2:=\frac{\ell_2}{\mathfrak p_2}}；\qquad \tilde\ell_1':=\frac{\ell_1'}{\mathfrak q_1},\quad\tilde\ell_2':=\frac{\ell_2'}{\mathfrak p_2}✓✓✓$$
$$\text{配合 (4.9) 的参数约束}：\mathfrak p_1,\mathfrak q_1\mid(\ell_1,\ell_1'),\quad \mathfrak p_2,\mathfrak q_2\mid(\ell_2,\ell_2')✓$$
$$\qquad\text{且（}p_i\ne q_i\Rightarrow1\in\{p_i,q_i\}\text{）}\Longrightarrow \text{若}\ \mathfrak p_2,\mathfrak q_2>1\ \text{则}\ \mathfrak p_2=\mathfrak q_2✓$$

---

# T2-1 · **fiber-surjectivity ⟹ 饱和（已证）**

## 1. 逐步归位：两条同余各确定**哪个变量**

$$(4.26)\quad \tilde\ell_2'd\equiv\tilde\ell_2d'\ \mathopen{}\mathclose{{\left(\textnormal{mod}\penalty\ u}}\right)$$
$$\qquad\text{左端含}\ \tilde\ell_2',d；\text{右端含}\ \tilde\ell_2,d' ⟹ \textbf{给定}\ (\tilde\ell_2,\tilde\ell_2')\ \text{时它确定}\ d\ \text{mod}\ u ⟹ \textbf{约束的是}\ (d,d')\ \textbf{而非}\ \ell✓✓$$
$$\qquad\text{（BC 自己这样用：Line3 的}\ \frac{D}{u\mathfrak q_1\mathfrak p_2}+1\ \text{正是}\ (d,d')\ \text{的对数}✓）$$

$$(4.27)\quad \mathfrak p_1\tilde\ell_1\equiv\mathfrak p_1\overline{\tilde\ell_2'}\tilde\ell_2\tilde\ell_1'\ \mathopen{}\mathclose{{\left(\textnormal{mod}\penalty\ u}}\right)$$
$$\qquad\text{LHS 只含}\ \tilde\ell_1；\text{RHS 含}\ \tilde\ell_2',\tilde\ell_2,\tilde\ell_1' ⟹ \boxed{\tilde\ell_1\ \textbf{是未知量}}✓✓✓$$
$$\qquad\Longrightarrow\ \text{给定}\ (\tilde\ell_2',\tilde\ell_2,\tilde\ell_1')\ \text{时，(4.27)}\ \textbf{确定}\ \tilde\ell_1\ \text{mod}\ u'：＝u/(\mathfrak p_1,u)✓✓$$
$$\qquad\Longrightarrow\ \textbf{可解性自动}：\text{需求解的是}\ \mathfrak p_1 X\equiv \mathfrak p_1 Y\ \text{型，其可解条件}\ (\mathfrak p_1,u)\mid\mathfrak p_1(Y-Y)=0\ \textbf{恒成立}✓✓✓$$

## 2. ⭐⭐⭐ 结论：$(\ell_2,\ell_2')$ **不承担同余约束**

$$\boxed{\text{(4.26) 约束}\ (d,d')；\ \text{(4.27) 被用于}\ \textbf{消去}\ \tilde\ell_1 \Longrightarrow (\ell_2,\ell_2')\ \text{只剩整除约束}}✓✓✓$$
$$\Longrightarrow\ \#\{(\ell_2,\ell_2')\in\mathcal L^2:\ \mathfrak p_2,\mathfrak q_2\mid(\ell_2,\ell_2')\}=\frac{L^2}{(\mathfrak p_2+\mathfrak q_2)\mathfrak q_2}\ \text{（BC 自己用的形式；}\textbf{逐情形即为精确阶}）✓✓$$

$$\text{三情形核对（}\mathfrak p_2,\mathfrak q_2\ \text{的允许组合）}：$$
$$\begin{array}{c|c|c}
&\text{实际计数}&\text{BC 形式}\ \frac{L^2}{(\mathfrak p_2+\mathfrak q_2)\mathfrak q_2}\\ \hline
\mathfrak p_2=\mathfrak q_2=m>1 & \asymp(L/m)^2 & =L^2/(2m^2)\ \iff\ \text{同阶}✓\\
\mathfrak p_2=1,\ \mathfrak q_2=m>1 & \asymp(L/m)^2 & \approx L^2/m^2\ \iff\ \text{同阶}✓\\
\mathfrak p_2=m>1,\ \mathfrak q_2=1 & \asymp(L/m)^2 & \approx L^2/m\ \gg\ \text{实际}\ \Longrightarrow \textbf{保守（安全）}✓✓
\end{array}$$

$$\Longrightarrow\ \textbf{T2-1 判定}：\ \boxed{\textbf{饱和}\ (N_2\ \text{与"仅整除"计数同阶，}\ L^{o(1)}\ \text{内})}✓✓✓$$
$$\qquad\text{（}\textbf{不是} \text{"同余有解"的充分性跳步，而是}\textbf{变量识别}\text{：同余被用于消去}\ \tilde\ell_1）✓✓$$

## 3. ⭐ 与 (4.29) 链的一致性（B 独立印证）

$$\text{Line1：4 个}\ \ell\text{-sum}\ (\ell_1,\ell_2,\ell_1',\ell_2')\quad\longrightarrow\quad\text{Line3/4：只剩}\ \sum\sum_{\ell_2,\ell_2'}✓✓$$
$$\qquad\Longrightarrow\ \text{被消去者}\ =\ \tilde\ell_1\ \text{（(4.27)）}\ \text{与}\ \tilde\ell_1'\ \text{（Line1→2 的计数）}⟹ \textbf{与 §2 的变量识别逐条吻合}✓✓$$
$$\qquad\text{且 Line3 的}\ (\frac Lu+1)\ \text{正是}\ \tilde\ell_1\ \text{被消去后的残存计数}\ \asymp L/u'\ \text{（而非}\ (\ell_2,\ell_2')\ \text{的约束）}✓✓✓$$

---

# T2-2 · **除因子对齐 ⟹ 关闭（无幂次 saving）**

## 4. 记账户（$\mathfrak p_2,\mathfrak q_2$ 逐处）

| 位置 | 出现 | 来源 |
|:--|:--|:--|
| Line1 | $\frac{1}{\mathfrak p_1\mathfrak p_2}$ | 求和/消去产生的分母 |
| Line3 | $\frac{1}{(\mathfrak p_1+\mathfrak q_1)\mathfrak p_1\mathfrak q_1\mathfrak p_2^2}$ | 同上＋$\mathfrak q_1$ 处理 |
| **Line4＝(4.29)** | $\frac{1}{(\mathfrak p_1+\mathfrak q_1)(\mathfrak p_2+\mathfrak q_2)\mathfrak p_1\mathfrak q_1^2\mathfrak p_2^3\mathfrak q_2}$ | ＋计数行 $\frac{L^2}{(\mathfrak p_2+\mathfrak q_2)\mathfrak q_2}$ |

$$\textbf{Line3}\to\textbf{Line4 的实际运算}：\ \text{乘} \begin{cases}\text{summand}\ \frac{DL}{\mathfrak q_1\mathfrak p_2}\\ \text{计数}\ \frac{L^2}{(\mathfrak p_2+\mathfrak q_2)\mathfrak q_2}\end{cases}✓\ \Longrightarrow\ \text{系数}\ \frac{A^2D^2L^5N^{3/2}}{\ldots\mathfrak p_2^3\mathfrak q_2}✓$$

## 5. ⭐⭐⭐ 判定：**无幂次 saving**

$$\text{(i)}\ \textbf{计数增益 vs 分母}：\text{计数给出}\ \asymp(\mathfrak p_2\mathfrak q_2)^{-2}\ (\text{或}\ \mathfrak p_2^{-2})；\ \text{分母给出}\ \mathfrak p_2^{-3}\mathfrak q_2^{-1}✓$$
$$\qquad\Longrightarrow\ \text{差异仅为}\ \mathfrak p_2^{\pm1},\mathfrak q_2^{\pm1}\ \text{型（单幂次）}✓$$
$$\qquad\Longrightarrow\ \sum_{\mathfrak p_2\le L}\mathfrak p_2^{\pm1}\ \text{型求和}\ \asymp\log^{O(1)}L=L^{o(1)}✓✓✓$$
$$\text{(ii)}\ \textbf{$\mathfrak q_2=1$ 情形下链的计数是保守的}：\text{链给}\ L^2/\mathfrak p_2\ \textbf{大于} \text{实际}\ L^2/\mathfrak p_2^2 ⟹ \textbf{不存在"已入分母却又被重复兑现"的因子}✓✓✓$$
$$\text{(iii)}\ \textbf{§4.1.4 逐字自证}：\ \text{"if}\ (\ell_1\ell_1',\ell_2\ell_2')>1\ \text{then}\ (\ell_2,\ell_2')=(\ell_1,\ell_1')=1\dots\ \text{and so}\ \mathfrak p_1=\mathfrak q_1=\mathfrak p_2=\mathfrak q_2=1\text{"}✓✓$$
$$\qquad\Longrightarrow\ \textbf{非平凡除因子只出现在}\ (\ell_1\ell_1',\ell_2\ell_2')=1\ \text{的情形} ⟹ \text{除因子系统在该情形}\ \textbf{自动坍缩}✓✓$$
$$\text{(iv)}\ \text{BC 自己的记账（§4.1.4）}：\text{"lose a factor of}\ (\ell_1\ell_1',\ell_2\ell_2')\ \text{in the}\ \Delta\ne0\ \text{terms, but this loss is}\ \textbf{recovered by the extra condition}\ \text{between the}\ \ell_1,\ell_1',\ell_2,\ell_2'\text{"}✓✓$$

$$\Longrightarrow\ \textbf{T2-2 判定}：\ \boxed{\text{divisor alignment}\ \textbf{无幂次 saving}}✓✓✓\quad(\text{只余}\ \tau(m),\log^C L,\mathfrak p_2^{\pm1},\mathfrak q_2^{\pm1})✓$$

---

# T2 最终判据（两刀完成）

$$\boxed{\text{(甲)}\ N_2=L^{2+o(1)}\ \textbf{（T2-1 饱和，已证）}}✓\qquad\boxed{\text{(乙)}\ \text{divisor alignment 无幂次 saving（T2-2 关闭）}}✓✓$$

$$\Longrightarrow\ \boxed{L^5=L^{5+o(1)}\ \text{是当前 BC 架构的}\textbf{结构性成本}}✓✓✓$$

## 架构级 closure 合成（T1 ＋ T2）

$$\boxed{\begin{array}{ll}
\text{(1)}&\text{BCR Appendix A · Proposition 4：目标形态}\ \textbf{已证最优（匹配下界）}✓\\
\text{(2)}&\text{BC 全无谱机器} \Longrightarrow \textbf{无谱升级}✓\\
\text{(3)}&F_3\ \textbf{SHARP}（V2-28A 构造性 witness）✓\\
\text{(4)}&L^5\ \textbf{四源审计}（L_{\rm Weil}·L_{\rm transition}·L_{\ell_2,\ell_2'}·L_u，全部锁定）✓\\
\text{(5)}&N_2\ \textbf{饱和}（T2-1，变量识别）✓\\
\text{(6)}&\text{divisor alignment}\ \textbf{无幂次 saving}（T2-2）✓
\end{array}}$$
$$\Longrightarrow\ \boxed{\textbf{BC 路线在已审范围内形成干净的架构级 closure}}✓✓✓\quad(\text{17/33 与}\ L^5\ \text{是该架构的}\textbf{结构性成本，非粗估})✓$$

## 边界（N1/N2 纪律）

$$\text{(i)}\ \text{本闭合}\ \textbf{限定于已审范围}，\ \text{不等于"17/33 不可突破"}✓$$
$$\text{(ii)}\ \text{唯一剩余入口仍是}\ \textbf{改变 §4 的 C--S／对角架构}（\text{T1-4 已登记}）✓$$
$$\text{(iii)}\ \text{T3（Architecture Search）首条纪律：新架构须在写第一条估计}\ \textbf{之前} \text{证明它不退化为 V2-7--V2-11／DFI／BC／现有 C--S 变量选择}✓✓$$
