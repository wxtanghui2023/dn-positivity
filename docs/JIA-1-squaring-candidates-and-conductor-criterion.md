# （甲）-1 · **C–S 可平方对象枚举 ＋ conductor 判据**（第一刀）

> 依冻结基线 `docs/BASELINE-FREEZE-20260917-BC-internal-space.md` 起手 ✓ **不回溯 T1/T2/T3** ✓
> **第一刀目标（锐化）**：$\boxed{\text{是否存在一种平方组织，使}\ \textbf{diagonal constraint 本身改变 phase conductor}？}$✓
> **防漂移**：不要把"新的平方对象"本身当成进展 ✓｜**若没有 → 迅速判死** ✓

---

## 1. ⭐⭐⭐ **conductor 的精确表达式**（本档新得）

$$\text{由基线}：q=\mathfrak p_1n_1'，\ \text{而}\ n_1=\mathfrak p_1\mathfrak p_2n_1' \Longrightarrow \boxed{q=\frac{\mathfrak p_1n_1}{\mathfrak p_1\mathfrak p_2}=\frac{n_1}{\mathfrak p_2}}✓✓✓$$
$$\text{而}\ \mathfrak p_2=(\ell_2,n_1) \Longrightarrow \boxed{q\ =\ \frac{n_1}{(\ell_2,\ n_1)}}✓✓✓$$

$$\textbf{结构规则（由 BC 单实例导出，标}\ [\textbf{结构判定}]\text{）}：\quad \boxed{q\ =\ \frac{\text{modulus}}{\big(\textbf{被求逆变量},\ \text{modulus}\big)}}✓$$
$$\qquad\text{当前：modulus}\ =\ n_1；\ \textbf{被求逆变量}\ =\ \tilde\ell_2\ (\text{即}\ \ell_2\ \text{尺度})✓$$

$$\Longrightarrow\ \boxed{\textbf{降 conductor}\iff\textbf{让"被求逆变量"与 modulus}\ (n_1)\ \textbf{共享更多}}✓✓✓$$
$$\text{（}\textbf{这正是唐先生问的}\ "diagonal 组织是否改变 conductor"\ \text{的精确形式}：\ \text{diagonal 决定谁被求逆}）✓$$

---

## 2. 候选枚举（**C–S 可平方对象**）

$$\textbf{变量清单}：n_1,\ n_2,\ a_2,\ \ell_1,\ \ell_2,\ m\ \big(＋\text{派生}\ d,a_1,p_i,q_i,c\big)✓$$
$$\textbf{可能阶段}：\text{(i) 第一 C--S（over } m\text{）；(ii) 第二 C--S（§4.1.2）；(iii) 额外 C--S；}\text{(iv) diagonal specialization 本身}✓$$

| # | 平方组织 | 重复集 $\mathcal S_j$ | diagonal | 被求逆变量 | $q(\mathcal S_j)$ | 三判据 |
|:--|:--|:--|:--|:--|:--|:--|
| **C0** | BC 原（§4.1.2） | $\{d,a_1,\ell_1,\ell_2\}$ | $x=x'$ | $\tilde\ell_2$（$\ell$-尺度） | $\dfrac{n_1}{(\ell_2,n_1)}=\mathfrak p_1n_1'$ | **基准** |
| **C1** | 第二 C–S 换一个变量进出 | $\pi(\mathcal S_0)$ 型 | 同型 | 同型 | 同型 | **✗ reparameterization**（V2-7--V2-11 已审） |
| **C2** | **加第三 C–S**（§4.1.3 之后） | 新增一对 | 新 | 仍是 $\tilde\ell_2$ | $n_1/(\cdot,n_1)$ | **✗** 不增 $(\cdot,n_1)$ ⟹ 不变 |
| **C3** | **改第一 C–S**（over $m$） | 变化 | 变化 | $\tilde\ell_2$ 或 $m$ | 见 §3 | **② 候选（GAP）** |
| **C4** | **改 diagonal specialization**（不消 $m$） | — | — | $\boxed{m}$（$M$-尺度！） | $\dfrac{n}{(m,n)}$ | **⭐ 唯一真正候选（GAP）** |

---

## 3. ⭐⭐⭐ 定量筛选：**可用降幅被"被求逆变量"的尺度锁死**

$$\text{要求（由 T3-1B 的缺口反推）}：\frac{L\sqrt{q_0}}{\sqrt N}\gg1 \iff \boxed{\sqrt{q_0}\gg\frac{\sqrt N}{L}=N^{2/5}} \iff \boxed{q_0\gg N^{4/5}}✓✓$$
$$\qquad(\text{即需要把 conductor 降掉}\ \textbf{几乎整个}\ n_1\ \text{的}\ N^{4/5}\ \text{部分})✓$$

$$\text{可用降幅}：q_0\ \text{是被求逆变量与}\ n_1\ \text{的 gcd} \Longrightarrow \boxed{q_0\le|\text{被求逆变量}|}✓$$
$$\qquad\text{在 C0--C2 中，被求逆变量是}\ \tilde\ell_2\ (\le L) \Longrightarrow q_0\le L=N^{1/10}✓$$
$$\Longrightarrow\ \frac{N^{4/5}}{N^{1/10}}=N^{7/10}\qquad\Longrightarrow\ \boxed{\text{shortfall}\ =\ N^{7/10}}✓✓✓$$

$$\Longrightarrow\ \textbf{C0--C2 全部}\ \boxed{\mathrm{DEAD}}：\ \text{任何"第二／第三 C--S"级调整都}\ \textbf{不改变被求逆变量的尺度}（都留在\ \ell\text{-尺度}）✓✓$$
$$\qquad\text{故 C0--C2 的 conductor 恒为同量级} \Longrightarrow \textbf{diagonal 组织在这些候选下}\ \textbf{不改} \text{conductor 的量级}✓✓$$

---

## 4. ⭐⭐⭐ 唯一逃逸候选：**改变被求逆变量本身**（C3／C4）

$$\textbf{关键}：\text{当前架构中，被求逆变量从原始}\ m\ \textbf{降格} \text{为}\ \tilde\ell_2\ \text{——因为用了}\ \textbf{diagonal specialization}\ \ell_1n_1=\ell_2n_2\ \text{来消去}\ m✓$$
$$\qquad\Longrightarrow\ \textbf{若改用另一种 specialization（不消}\ m\text{），被求逆变量可保持}\ m\text{-尺度}\ (M)，\ \text{则}\ q_0\le M✓✓$$
$$\qquad\Longrightarrow\ \text{此时}\ q_0\ \text{可能}\ \gg N^{4/5}\ \text{——}\textbf{唯一可能逃出 §3 的路径}✓✓✓$$

$$\textbf{但这一候选是}\ \mathrm{GAP}，\ \text{理由}：$$
$$\qquad\text{(i)}\ (m,n_1)\ \text{的}\ \textbf{下界} \text{需要}\ m\ \text{的算术结构（现无）；}\ \text{而}\ (m,n_1)=M^{o(1)}\ \text{是}\ \text{典型情形}✓$$
$$\qquad\text{(ii)}\ \text{diagonal specialization 是 §3 amplification 的}\ \textbf{结构支柱}；\ \text{替换它}\ \textbf{改变整个 §3--§4 组织}，\ \text{不是"换一种 C--S"}✓$$
$$\qquad\Longrightarrow\ \text{须单独立项（登记为}\ \textbf{（甲）-2 候选}），\ \text{不得在本刀内宣称}✓$$

---

## 5. ⭐ 判定

$$\boxed{\textbf{（甲）-1}\ (\text{C--S 平方组织层面})\ =\ \mathrm{DEAD}}✓✓$$
$$\qquad\textbf{理由（定量且不含长估计）}：\text{第二／第三 C--S 级调整全部把被求逆变量留在}\ \ell\text{-尺度}\ (\le L=N^{1/10})；$$
$$\qquad\text{故}\ q_0\le N^{1/10}\ \textbf{而需求}\ q_0\gg N^{4/5} \Longrightarrow \textbf{shortfall}\ N^{7/10}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{diagonal 组织在"C--S 平方"层面}\ \textbf{不能} \text{改变 conductor 的量级}}✓✓$$
$$\qquad(\textbf{与 T3-1A-1 一致}：\text{那里用的是"局部 conductor 非平凡"}，\ \text{这里用的是}\ \textbf{尺度上界}，\ \text{两条独立论证同向})✓✓$$

$$\textbf{唯一逃逸}：\ \text{改变}\ \textbf{被求逆变量}（\text{C4：不消}\ m\text{）} \Longrightarrow \mathrm{GAP}，\ \text{登记为}\ \textbf{（甲）-2 候选}✓$$

## 6. 边界与残余
$$\text{(R-a)}\ \text{§1 的"规则"由 BC 单实例导出，}\ \text{推广到所有组织为}\ [\textbf{结构判定}]，\ \textbf{未逐候选推导}✓$$
$$\text{(R-b)}\ q_0\le|\text{被求逆变量}|\ \text{是 gcd 的}\ \textbf{平凡上界}，\ \text{已足够用于判死}✓$$
$$\text{(R-c)}\ \text{C4 的}\ M\ \text{尺度}\ (M\asymp LN\ \text{在 diagonal 上})\ \textbf{未界定} \ \Longrightarrow\ \text{正因如此才登记为 GAP}✓$$
$$\text{(R-d)}\ \textbf{未用 RH；零数值}✓$$
