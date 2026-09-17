# T3-1C-2 · **C4 聚合账**（$K$／$Y$／$R$）⟹ 判定 **DEAD**

> 依唐先生 2026-09-17 09:39 指令｜**关键逻辑点已采纳**：$\boxed{\text{"聚合更多}\ \ell_2\text{-classes"}\ne\text{"振荡区间自动变长"}}$✓
> 只有聚合后的类能被组织成**同一个有效振荡和**且相位保持可利用相干／正交结构，才算真正增加有效长度 ✓
> 材料：(4.11)(4.19)(4.26) 逐字在手 ✓

---

## 0. 三个量的定义（唐先生给定）

$$K：＝\text{聚合的原始 fiber 数}；\quad Y：＝\text{聚合后}\ \textbf{真正增加的有效相位长度}；\quad R：＝\text{平均 multiplicity／权重成本}✓$$
$$\text{不能简单写}\ Y=KX；\ \text{须证}\ Y\asymp KX\ \text{且}\ R\ll K^{1-\delta}✓$$
$$\textbf{唯一 ALIVE 形态}：\ \frac{Y}{R}\gg\sqrt q\gg X（\text{原来只有}\ X\ll\sqrt q）✓$$

---

## 1. ⭐ 情形 (a)：同一 $\ell_2$ 轴上的聚合 ⟹ **立即 DEAD**

$$X=\frac{L}{\mathfrak p_2\mathfrak q_2}\Longrightarrow K_{\max}\lesssim\frac{L}{X}=\mathfrak p_2\mathfrak q_2✓$$
$$\text{最有利点}\ \mathfrak p_2=\mathfrak q_2=1：K_{\max}=O(1)，\ \text{而所需}\ K\gg N^{2/5}\quad\Longrightarrow\ \boxed{\mathrm{DEAD}}✓✓✓$$
$$\text{（唐先生已算；本档确认）}✓$$

---

## 2. ⭐⭐⭐ 情形 (b)：跨轴聚合（相位格映射）—— C4-1 通过

$$\textbf{C4-1：相位格映射是否存在？}\ \Longrightarrow\ \boxed{\textbf{是}}✓✓$$
$$\text{由 (4.19)/(T3-1B-2)：}(\tilde\ell_2,\tilde\ell_2')\text{-相位}\ =\ -\frac{\vartheta\overline{C_0}}{\mathfrak p_1n_1'}\Big(da_1\overline{\tilde\ell_2}-d'a_1'\overline{\tilde\ell_2'}\Big)✓$$
$$\qquad\Longrightarrow\ \text{它对}\ \textbf{(d,\tilde\ell_2)}\ \text{是}\ \textbf{双线性}：\ \frac{\alpha}{q}\,d\,\overline{\tilde\ell_2}\quad\big(q=\mathfrak p_1n_1'\big)✓✓✓$$
$$\Longrightarrow\ \text{聚合}\ d\ \text{（而非同一}\ \ell_2\ \text{轴）}\ \textbf{即把相位线性化为单一 reciprocal 格}：\ \Phi:(d,\tilde\ell_2)\mapsto x：＝d\,\overline{\tilde\ell_2}✓✓$$

### 2.1 完整双和**恒为零** ⟹ 真实相消存在
$$\sum_{d\bmod q}\sum_{x\bmod q}e(\alpha dx/q)=\sum_x q\,[q\mid\alpha x]=0\quad(\text{因}\ x\ \text{取单位且}\ \alpha\ \text{可逆})✓✓✓$$
$$\Longrightarrow\ \textbf{该双线性和确有大幅相消}（\text{主要项为}\ 0）\Longrightarrow \textbf{C4-1 通过、C3 亦满足}✓✓$$

---

## 3. ⭐⭐⭐ C4-2／C4-3：阈值**不变** ⟹ DEAD

$$\text{范围：}\ |d|\le D'：＝\frac{D}{\mathfrak q_1\mathfrak p_2}\ \text{（(4.26) 使其落在步长}\ u\ \text{的等差列上 —— 见 §3.2）}；\ \#\{\tilde\ell_2\}\asymp X=\frac{L}{\mathfrak p_2\mathfrak q_2}✓$$
$$\text{而}\ D=3NL/M\ \text{（(4.31) 逐字"since}\ D=3NL/M\text{"）}\ \xrightarrow{M\asymp N}\ D\asymp L\ \Longrightarrow\ D'\asymp\frac{L}{\mathfrak q_1}✓$$
$$\Longrightarrow\ \text{最有利点：}\ D'\asymp X\asymp L\quad(\textbf{两轴同尺度})✓✓$$

### 3.1 双线性界的量级（本档推导，$[\textbf{结构判定}]$）
$$\Big|\sum_{|d|\le D'}\sum_{x\le X}e(\alpha d\overline{x}/q)\Big|^2\ \le\ X\sum_{x}|\sum_d e(\alpha\overline{x}d/q)|^2=X\sum_{d,d'\le D'}\sum_{x}e\big(\alpha(d-d')\overline{x}/q\big)✓$$
$$\qquad d=d'：\ \asymp D'\cdot X；\qquad d\ne d'：\ \text{对}\ \overline{x}\text{-集的特征和}\ \ll\sqrt q\log^{O(1)}q✓$$
$$\Longrightarrow\ |T|^2\ll X\big(D'X+D'^2\sqrt q\big)\ \Longrightarrow\ T\ll\sqrt{D'X}\sqrt{X+D'\sqrt q}\ \xrightarrow{D'\asymp X\asymp L}\ L^{3/2}N^{1/4}✓✓$$
$$\text{Trivial：}\ D'X\asymp L^2\ \Longrightarrow\ \boxed{\text{gain}\asymp\frac{L^2}{L^{3/2}N^{1/4}}=L^{1/2}N^{-1/4}}✓✓$$

### 3.2 阈值与 multiplicity
$$\text{gain}\gg1\iff \boxed{L\gg N^{1/2}}\quad\big(\textbf{与 T3-1B 完全同一阈值}\big)✓✓✓$$
$$\text{记账：}\ L=N^{1/10}\Longrightarrow \text{gain}=N^{1/20-1/4}=N^{-1/5}\ll1\ \Longrightarrow\ \boxed{\mathrm{DEAD}}✓✓✓$$
$$\textbf{shortfall}\ =\ \frac{\sqrt N}{L}=N^{1/2-1/10}=\boxed{N^{2/5}}\quad\Longleftarrow\ \textbf{与唐先生算出的缺口逐字一致}✓✓✓$$
$$\text{C4-3：multiplicity——(4.26) 令}\ d\ \text{落在步长}\ u\ \text{的等差列} \Longrightarrow \text{项数按}\ u\ \text{因子}\ \textbf{减少}（\text{是}\ \textbf{增益} \text{而非成本}）✓\quad\text{即}\ R\ \text{吃不掉收益}✓$$
$$\text{故失败点}\ \textbf{不在}\ R，\ \text{而在}\ \sqrt q\ \text{阈值本身}✓$$

---

## 4. ⭐⭐⭐ 结构性结论（**不依赖 §3.1 的精确界**）

$$\text{两轴同尺度}\ D'\asymp X\asymp L\ \text{下，相消尺度}\ \textbf{只能来自} \sqrt q；\ \text{而}\ \boxed{\text{聚合}\ d\ \textbf{不改变模数}\ q=\mathfrak p_1n_1'}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{模数不变} \Longrightarrow \sqrt q\ \textbf{阈值不变} \Longrightarrow \text{聚合不能降低门槛}}✓✓✓$$
$$\qquad(\text{故 §3.1 的具体界只用于}\ \textbf{定量核对}；\ \text{结论}\ \textbf{对任何}\ \text{保持同模数的聚合都成立})✓✓$$

---

## 5. 判定

$$\boxed{\textbf{T3-1C-2}\ (\text{情形 (a)}\ \vee\ \text{情形 (b)})\ =\ \mathrm{DEAD}}✓✓✓$$
$$\begin{array}{c|c|c}
&\text{机制}&\text{死因}\\
\hline
\text{(a)}&\text{同轴聚合}&K_{\max}\lesssim\mathfrak p_2\mathfrak q_2\ \text{不足（最有利点}\ O(1)\ll N^{2/5}）\\
\text{(b)}&\text{跨轴相位格映射}&K\ \text{可任意大，但}\ q\ \text{不变}\Rightarrow\ \text{阈值不变}\Rightarrow\ \text{shortfall}\ N^{2/5}\\
\end{array}✓$$

$$\textbf{与 T3-1B 合看}：\ \text{单 fiber 相消不足（T3-1B）}；\ \text{聚合亦不能补（T3-1C-2）} \Longrightarrow \ell_2\text{-侧振荡路线}\ \textbf{整体 DEAD}✓✓$$

---

## 6. ⭐⭐⭐ T3-1C-2 的**正面产出**：一条新判据

$$\boxed{\text{要降低门槛，必须}\ \textbf{改变相位模数}\ q，\ \text{而不是}\ \textbf{聚合}\ \text{同一模数下的项}}✓✓✓$$
$$\qquad(\text{任何"同模数聚合"——无论跨轴与否——都被}\ \sqrt q\ \text{阈值锁死})✓$$
$$\Longrightarrow\ \textbf{这直接决定 T3-1A 的形式}：\ \text{候选须回答"}\ \textbf{它把模数换成什么}？\text{"}\ ✓✓$$

## 7. 边界与残余
$$\text{(i)}\ \text{§3.1 的界为}\ [\textbf{结构判定}]，\ \textbf{未引经典定理}（\text{残余：}\overline{x}\text{-集上特征和的分布性未核}）✓$$
$$\text{(ii)}\ \text{§4 的结构性结论}\ \textbf{不依赖} \text{§3.1}✓\quad\text{(iii)}\ D=3NL/M\ \text{为 (4.31) 逐字}✓$$
$$\text{(iv)}\ \textbf{未用 RH；零数值}✓\quad\text{(v)}\ \text{情形 (b) 的}\ \Phi\ \text{单射性／像大小未逐项核（残余）}✓$$
