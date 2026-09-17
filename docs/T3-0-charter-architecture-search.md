# T3-0 · **Architecture Search 宪章**

> 唐先生 2026-09-17 09:27 指令｜**前置**：T1（取证＋(r,t)模板＋无谱）＋ T2（fiber 饱和＋除因子对齐）已完成 ⟹ BC 支线封存 ✓
> **纪律**：T3 第一阶段 **不发明新估计**；先找**可能改变信息流的架构**，再估计 ✓✓

---

## 1. 为什么是"架构搜索"而非"更强估计"

$$\text{T1＋T2 的真正价值}\ \textbf{不是} \text{"BC 很难"}，\ \text{而是把搜索空间从}\ \underbrace{\text{无穷多个估计技巧}}_{\text{不可枚举}}\ \text{压缩成：}$$
$$\boxed{\text{必须改变}\ \textbf{Weil ／}\ \ell_2\text{-fiber ／ diagonal ／ C--S}\ \text{四者至少一个的}\ \textbf{信息流}}✓✓✓$$

$$\textbf{禁止的循环}：\ \text{换变量}\to\text{换 C--S}\to\text{重新计数}\to L^5\quad(\text{即 V2-7--V2-11 重演})✗$$

---

## 2. 旧架构的四个**操作**（待搜索其不可交换性）

$$\boxed{\mathsf C\to\mathsf W\to\mathsf E\to\mathsf K}$$
$$\mathsf C：\text{Cauchy--Schwarz}（\text{§4.1.2：施于}\{n_1,n_2,a_2\}\ \text{等，不施于}\{d,a_1,\ell_1,\ell_2\}）✓$$
$$\mathsf W：\text{Weil（附录 A，不完全 Kloosterman 和）}✓$$
$$\mathsf E：\text{执行}\ \ell\text{-变量（(4.27) 消去}\ \tilde\ell_1；\ \text{余下}\ \ell_2,\ell_2'\ \text{计数）}✓$$
$$\mathsf K：\text{gcd／除子分类（}\mathfrak p_i,\mathfrak q_i,u,\Delta=0/\!\ne0\text{）}✓$$

$$\textbf{核心待搜问题}：\ \boxed{\text{是否存在一种}\ \textbf{次序}，\text{使一个现在被当作"独立长度}\ L\text{"的变量，在进入 Weil 或 C--S}\ \textbf{之前} \text{已被另一个算术约束压缩？}}✓✓$$

---

## 3. T3 的核心判据（**新架构的硬条件**）

$$\text{设原损耗}\ L^5=L_{\rm W}L_{\ell_1}L_{\ell_2}L_u。\ \text{产生真正新架构，至少须出现一种：}$$
$$\boxed{L_iL_j\ \longrightarrow\ \text{一个}\ \textbf{联合算术对象}}✓✓\qquad(\text{而不是分别估计}\ L_i\cdot L_j)✓$$
$$\textbf{理由（由 T2 提供）}：\ \text{只要仍逐层绝对值化}\ \sum_{\ell_2,\ell_2'}|\cdots|\le\#\{\ell_2\}\#\{\ell_2'\}\max|\cdots|，\ \text{而}\ \#\{\ell_2,\ell_2'\}=L^{2+o(1)} \Longrightarrow \textbf{不可能凭空制造固定幂次}✓✓$$

---

## 4. ⭐⭐ 关键区分：**点数饱和 ≠ 振荡和饱和**

$$\text{T2-1 证明的是}\ \boxed{N_2=\#\{(\ell_2,\ell_2')\}=L^{2+o(1)}}\ \text{（}\textbf{点数} \text{饱和）}✓$$
$$\qquad\text{但原架构支付的}\ L^2\ \text{来自}\ \textbf{"自由变量数量"}；\ \text{若这}\ L^2\ \text{个点之间存在}\ \textbf{真正的二次／双线性 cancellation}：$$
$$\qquad\qquad\left|\sum_{\ell_2,\ell_2'}K(\ell_2,\ell_2')\right|\ll L^{2-\delta}\ \Longrightarrow\ \text{它}\ \textbf{绕开} \text{T2 的 saturation，而}\ \textbf{不是否定} \text{T2}✓✓✓$$
$$\Longrightarrow\ \boxed{\textbf{T2-1 不杀掉 cancellation architecture}}✓✓✓$$

---

## 5. T3-1 第一轮（**三支，先做 architecture test，不做 20 页推导**）

$$\boxed{\begin{array}{ll}
\textbf{T3-1A}&\text{Weil}\ \textbf{之前} \text{能否对多个 Kloosterman 相位做}\ \textbf{联合求和}？\（\text{若不能且文献表明 Weil 已是最自然逐项入口}\Rightarrow \text{DEAD}）\\
\textbf{T3-1B}&(\ell_2,\ell_2')\ \text{的}\ L^2\ \textbf{饱和之后是否仍存在结构性（二次／双线性）cancellation}？\\
\textbf{T3-1C}&\text{是否存在}\ \textbf{真正不同于 BC 的 diagonal-preserving C--S 架构}？（\text{BC 自身的关键增益＝"longer diagonal"；须更深一级}）
\end{array}}✓$$

$$\textbf{判定（仅三档）}：\ \boxed{\mathrm{ALIVE}\ /\ \mathrm{GAP}\ /\ \mathrm{DEAD}}✓$$
$$\textbf{ALIVE 的硬标准}：\ \text{必须存在一个}\ \textbf{明确的、可写成数学公式} \text{的新信息流}✓\quad(\text{"理论上也许有 cancellation"}\ \textbf{不算} \text{ALIVE})✗$$

## 6. 执行顺序（唐先生指定）
$$\boxed{\textbf{优先 T3-1B}}✓\quad\text{理由}：\ \text{它是}\ \textbf{唯一不与 T2-1 矛盾、又可能直接吃掉}\ L^2\ \text{的入口}✓✓$$
