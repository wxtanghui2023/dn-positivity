# （甲)-2 · **specialization existence audit**（只审存在性，**不做估计**）

> 起手：冻结基线 + （甲)-1（`docs/JIA-1-*`）✓ **不回溯 T1/T2/T3** ✓
> **第一刀目标（唐先生）**：$\boxed{\text{是否存在合法的、不消 }m\text{ 的 diagonal/equality specialization？}}$✓
> **审计序**：① §3 原始关系 → ② 为何 $\ell_1n_1=\ell_2n_2$ 能消 $m$（完整逆推）→ ③ 枚举不消 $m$ 的 specialization → ④ 直接算相位 → ⑤ $m$ 是否真成被求逆变量 → ⑥ 能否强迫 $(m,n)\gg N^{4/5}$ ✓

---

## 1. §2--§3 的**原始关系**（逐字）

$$\text{(2.1)}\ \mathcal B\ll\|\alpha\|\,\mathcal C_1^{\frac12},\qquad \mathcal C_b:=\sum_{\substack{m\in\mathcal M\\(m,b)=1}}\Big|\sum_{a\in\mathcal A}\sum_{\substack{n\in\mathcal N\\(m,n)=1}}\beta_n\nu_a\,e\Big(\vartheta\frac{a\overline m}{bn}\Big)\Big|^2✓$$
$$\text{(2.2)}\ \text{放大器（}\chi\ \text{和}）：\mathcal D_b\ \text{含}\ \frac{1}{\varphi(m)}\sum_{\chi(m)}\big|\sum_{\ell\in\mathcal L,(\ell,\vartheta b)=1}\chi(\ell)\big|^2\ \text{与}\ \big|\sum\sum_{n,a}\chi(n)\beta_n\nu_a e(\ldots)\big|^2✓$$
$$\qquad\Longrightarrow\ \mathcal C_b\ll ML^{-2+\varepsilon}\mathcal D_b\quad(\text{素数}\ \ell\ \text{给}\ \gg L/\log L\ \text{质量})✓$$
$$\text{(2.3)}\ \mathcal D_b=\sum\sum\sum\sum\sum\sum\sum_{\substack{m\in\mathcal M,\ n_1,n_2\in\mathcal N,\ a_1,a_2\in\mathcal A,\ \ell_1,\ell_2\in\mathcal L\\ (mb\vartheta,\ell_1\ell_2n_1n_2)=(m,b)=1,\ \boxed{\ell_1n_1\equiv\ell_2n_2\ (\mathrm{mod}\ m)}}}\beta_{n_1}\nu_{a_1}\overline{\beta_{n_2}\nu_{a_2}}\,e\Big(\vartheta\frac{a_1\overline m}{bn_1}-\vartheta\frac{a_2\overline m}{bn_2}\Big)✓✓$$
$$\qquad=\mathscr D_b+\mathscr O_b\ \big(\text{diagonal}\ \ell_1n_1=\ell_2n_2\ \big|\ \text{off-diagonal}\ \ell_1n_1\ne\ell_2n_2\big)✓$$

$$\textbf{§4 做法（BC §2 逐字 bullets）}：$$
$$\qquad\text{"In Section 4.1.1, we switch to the}\ \textbf{complementary divisor}\ d\ \text{of the congruence relation}\ \ell_1n_1\equiv\ell_2n_2\ (\mathrm{mod}\ m)\text{,}\ \boxed{\textbf{eliminating the variable}\ m}✓✓\quad\text{This also requires that we first}\ \textbf{split the sum over}\ m\ \text{into certain congruence classes}\text{"}✓✓✓$$
$$\qquad\text{"In Section 4.1.3.2, we apply the elementary reciprocity law … which roughly allows one to change}\ \frac{\overline\alpha}{\beta}\ \text{into}\ -\frac{\overline\beta}{\alpha}\ \text{modulo 1"}✓$$

$$\textbf{§3 的对照（关键）}：\ \text{diagonal 情形下，}$m$-和被}\ \textbf{直接} \text{用 Weil 界，模数}\ b\ell_1n_1：$$
$$\qquad\Big|\sum_{\substack{m\in\mathcal M\\(m,b\ell_1\ell_2n_1n_2)=1}}e\Big(\vartheta\frac{(a_1\ell_1-a_2\ell_2)\overline m}{b\ell_1n_1}\Big)\Big|\ll(bLN)^{\frac12+\varepsilon}+(a_1\ell_1-a_2\ell_2,bn_1\ell_1)\frac{M^{1+\varepsilon}}{bLN}✓✓$$

---

## 2. ⭐ **为何能消 $m$**（完整逆推）

$$\text{由 (2.3) 的同余}\ m\mid\ell_1n_1-\ell_2n_2 \Longrightarrow \boxed{d\ :=\ \frac{\ell_1n_1-\ell_2n_2}{m}}\ \text{是整数（互补除子）}✓✓$$
$$\qquad\Longrightarrow\ \textbf{把}\ \sum_m\ \text{换成}\ \sum_d\ \text{——}\textbf{除子对换}，\ \text{范围}\ |d|\le D\ \text{（基线：}D=3NL/M\text{）}✓✓$$
$$\qquad\Longrightarrow\ \text{相位中的}\ \overline m\ \text{用}\ m=(\ell_1n_1-\ell_2n_2)/d\ \text{改写，再经 reciprocity (4.17)}\Longrightarrow\text{被求逆变量}\ \textbf{降格} \text{为}\ \tilde\ell_2\ (\ell\text{-尺度})✓✓$$
$$\Longrightarrow\ \boxed{\text{消 }m\ \text{的机制}＝\textbf{除子对换}\ +\ \textbf{reciprocity}}✓✓\quad(\text{故"保留 }m"\ \text{意味着}\ \textbf{放弃这两步})✓$$

---

## 3. 候选 specialization 表（五段管线）

| # | specialization | 保留 $m$？ | 被求逆变量 | $q_{\rm new}$ | gcd 可达尺度 | 状态 |
|:--|:--|:--:|:--|:--|:--|:--|
| **$S_0$** | BC：除子对换＋reciprocity | ✗ | $\tilde\ell_2$ | $\mathfrak p_1n_1'=\dfrac{n_1}{(\ell_2,n_1)}\asymp N$ | $(\ell_2,n_1)\le L$ | **基准** |
| **$S_1$** | **保留 $m$**，直接 Weil on $m$ | ✓ | $m$（$M$-尺度） | $\dfrac{bn_1n_2}{(m,bn_1n_2)}\ \ge\ \dfrac{n_1n_2}{M}\asymp\dfrac{N^2}{M}$ | $(m,bn_1n_2)\le M$ | 见 §5 |
| **$S_2$** | 保留 $m$ ＋ **gcd 精化** | ✓ | $m$ | $\dfrac{n_1n_2}{(a_1n_2-a_2n_1,\ bn_1n_2)}$ | $\le A\max(n_1,n_2)\asymp AN$ | 见 §5 |
| **$S_3$** | 去掉 mod-$m$ 同余（换 amplifier） | — | — | — | — | **越界**：改 §2 放大器，不属本刀 ✗ |

$$\text{(相位统一式：}e\Big(\vartheta\overline m\Big(\tfrac{a_1}{bn_1}-\tfrac{a_2}{bn_2}\Big)\Big)=e\Big(\tfrac{\vartheta\overline m(a_1n_2-a_2n_1)}{bn_1n_2}\Big)\ \Longrightarrow\ \text{模数}\ bn_1n_2)✓$$

---

## 4. 判据（由（甲)-1 与 T3-1B 反推）

$$\text{需 conductor 被降}\ q_0\gg N^{4/5} \iff \boxed{q_{\rm new}\ll N^{1/5}}✓✓\quad(\text{因最终须}\ \sqrt{q_0}\gg\tfrac{\sqrt N}{L}=N^{2/5})✓$$

---

## 5. ⭐⭐⭐ 判定

$$\textbf{$S_1$}\ \Longrightarrow\ \boxed{\mathrm{DEAD}}✓✓$$
$$\qquad q_{\rm new}\ge\frac{n_1n_2}{M}\asymp\frac{N^2}{M}\ \text{须}\ \ll N^{1/5} \iff \boxed{M\gg N^{9/5}}✓$$
$$\qquad\textbf{应用区间（BCR §3.4）}：M\ll T^{1/2+\varepsilon}\sqrt{N_2/N_1}，\ N\asymp T^\theta\ (\theta<17/33\approx0.5152)✓$$
$$\qquad\Longrightarrow\ \frac MN\lesssim T^{1/2-17/33}=T^{-1/66}\ll1 \Longrightarrow \boxed{M\ll N} \Longrightarrow \frac{N^2}{M}\ggg N^{1/5} \Longrightarrow \textbf{DEAD}✓✓✓$$

$$\textbf{$S_2$}\ \Longrightarrow\ \boxed{\mathrm{GAP}}✓\quad(\text{唯一未死候选})✓$$
$$\qquad q_{\rm new}\gtrsim\frac{n_1n_2}{AN}\asymp\frac{N}{A}\ \text{须}\ \ll N^{1/5} \iff \boxed{A\gg N^{4/5}}✓✓$$
$$\qquad\text{且须}\ \textbf{典型性}：\text{不是"存在配置使}\ \gcd\ \text{大"，而是}\ \textbf{求和意义上}\ \text{大 gcd 的贡献占主导}✓$$
$$\qquad ⚠️\ \text{且大 gcd}\ \Leftrightarrow\ a_1n_2-a_2n_1\ \text{与}\ bn_1n_2\ \text{共因子大} \Longrightarrow\ \text{相位}\ \textbf{振荡弱} ⟹ \textbf{净增益未定}✓✓$$

---

## 6. ⭐⭐⭐ 结构性收获（**反直觉，但重要**）

$$\boxed{\text{消去 }m\ \textbf{本身} \text{就是 conductor 降阶机制}：\ \text{模数}\ bn_1n_2\ (N^2)\ \longrightarrow\ \mathfrak p_1n_1'\ (N)}✓✓✓$$
$$\qquad\Longrightarrow\ \text{（甲)-1 提出的"保留 }m\ \text{以取得 }M\text{-尺度被求逆变量"}\ \textbf{自相矛盾}：\ \text{保留 }m\ \text{会把模数从}\ N\ \text{抬到}\ N^2✓$$
$$\qquad\Longrightarrow\ \text{只有在}\ \boxed{M\gg N^{9/5}}\ (\text{不平衡}) \ \text{或}\ \boxed{A\gg N^{4/5}}\ (\text{gcd 精化}) \ \text{时，"保留 }m"\ \text{才可能翻盘}✓✓$$

$$\textbf{故（甲)-2 第一刀的真正结论}：\ \text{不存在}\ \textbf{无条件合法} \text{的"不消 }m"\ \text{specialization}；\ \text{两个候选各带一个}\ \textbf{硬条件}（M\gg N^{9/5}\ \text{或}\ A\gg N^{4/5}），\ \text{而}\ S_1\ \text{的条件在应用区间}\ \textbf{反向}✓✓$$

---

## 7. 边界与残余
$$\text{(R-1)}\ S_2\ \text{的}\boxed{A\gg N^{4/5}}\ \text{是否在应用区间成立}\ \textbf{未核}（\text{BC Remark：}A\ll M^C，\text{无固定幂约束}）✓\quad\Longrightarrow\ \textbf{下一刀}✓$$
$$\text{(R-2)}\ S_2\ \text{的"大 gcd ⟹ 弱振荡"是否使净增益归零}\ \textbf{未核}✓$$
$$\text{(R-3)}\ \text{§2 放大器的结构约束未穷举（}S_3\ \text{属越界，未展开）}✓$$
$$\text{(R-4)}\ q_{\rm new}\ \text{的表达式为}\ [\textbf{结构判定}]（\text{由相位模数直接读出，未逐项归一化}）✓$$
$$\text{(R-5)}\ \textbf{未用 RH；零数值}✓$$
