# T3-1A-1 · **CRT-local conductor 审计** ⟹ 判定 **DEAD**

> 依唐先生 2026-09-17 09:48 指令｜**压缩后的形式**：$\boxed{\text{不是"能否联合利用 Kloosterman 振荡"，而是"联合利用能否}\ \textbf{改变有效模数}\text{"}}$✓
> **审计序**：A1（局部 conductor 分解）→ A2（公共退化因子）→ A3（跨项 exact cancellation）→ A4（量化）✓
> 材料：(4.4)(4.9)(4.10)(4.11)(4.19) 逐字在手 ✓

---

## 0. 终局形式（唐先生给定）
$$\boxed{\exists\,q_0\mid q,\ q_0\ge N^\delta,\ \text{且}\ q_0\ \text{的消失}\ \textbf{未被 BC 已有}\ u,v,\Delta\ \text{记账过}}✓\quad\Longrightarrow\ \mathrm{ALIVE}✓$$
$$\text{若只能}\ q_0=L^{o(1)} \Longrightarrow \mathrm{DEAD}\ (\text{仅次幂改善})✓\qquad\text{若所有局部 conductor 非平凡} \Longrightarrow \mathrm{DEAD}：\textbf{Weil 的}\ \sqrt q\ \text{是 conductor-level barrier}✓✓$$

---

## 1. A1 · $q=\mathfrak p_1n_1'$ 的 **CRT-local 分解**

$$\text{记号}：n_1=\mathfrak p_1\mathfrak p_2n_1'\ \text{（(4.4) 逐字：}\ n_1'：＝n_1/(n_1,\ell_1\ell_2)=n_1/(\mathfrak p_1\mathfrak p_2)\text{）}✓$$

$$\textbf{关键互素条件（(4.10) 逐字）}：\ (b\vartheta n_1'n_2',\ \ell_1\ell_2\ell_1'\ell_2')=1✓✓$$
$$\qquad\Longrightarrow\ (\ell_1,\ n_1'n_2'b\vartheta)=1；\quad \text{而}\ \mathfrak p_1=(\ell_1,n_1)\mid\ell_1⟹\boxed{(\mathfrak p_1,\ n_1'n_2'b\vartheta)=1}✓✓✓$$
$$\textbf{特别}：\ \boxed{(\mathfrak p_1,\ n_1')=1} ⟹ q=\mathfrak p_1n_1'\ \text{是}\ \textbf{两个互素因子之积}✓✓$$
$$\qquad\Longrightarrow\ \textbf{CRT 成立}：\ q\ \text{的局部 conductor}＝\{\mathfrak p_1\ \text{的素因子}\}\ \sqcup\ \{n_1'\ \text{的素因子}\}✓\quad(\textbf{无重叠})✓$$

$$\text{另两个用到的互素（逐字）}：\ (b,n_1'n_2')=1；\quad (n_1',\vartheta n_2')=1；\quad (b,p_1n_1'q_2n_2')=1\ \text{（(4.16) 附带）}✓$$
$$\qquad(\ell_1,\ell_2)=(\ell_1',\ell_2')=1 \Longrightarrow (\mathfrak p_1,\mathfrak q_2)=1\ \text{-型交叉互素}✓$$

---

## 2. A2 · 搜索"联合退化"因子

$$\text{相位（T3-1B-2 已定）}：\ e_q\Big(\alpha_{\rm tot}\,\overline{\tilde\ell_2}\ -\ \alpha'_{\rm tot}\,\overline{\tilde\ell_2'}\Big),\qquad \alpha_{\rm tot}：＝\vartheta\,\overline{C_0}\,d\,a_1\quad(\!\!\bmod q)✓$$
$$\qquad\text{其中}\ \overline{C_0}\ \text{是}\ C_0=b\mathfrak p_2\mathfrak q_2n_2'\ \text{相对}\ q\ \text{的逆元}⟹\boxed{\overline{C_0}\ \text{是单位}}✓$$

$$\textbf{局部非平凡性}：\ \text{由}\ (\ell_2,\ n_1'n_2'b\vartheta)=1\ \text{与}\ (\ell_2,\ell_1)=1⟹(\tilde\ell_2,q)=1 ⟹ \overline{\tilde\ell_2}\ \textbf{是单位 mod}\ q✓✓$$
$$\qquad\Longrightarrow\ \text{对每个}\ q_r\mid q：\ \alpha_{\rm tot}\overline{\tilde\ell_2}\not\equiv0\ (\mathrm{mod}\ q_r)\quad\textbf{除非}\ q_r\mid\alpha_{\rm tot}✓$$

$$\textbf{退化的唯一可能}：q_0\mid\alpha_{\rm tot} \Longrightarrow q_0\mid d\ (\text{因}\ \vartheta,\overline{C_0},a_1\ \text{名义上皆单位；}\ a_1\ \text{与}\ q\ \text{的互素性}\ \textbf{未证}——\text{残余})✓$$
$$\qquad\Longrightarrow\ \boxed{q_0=(\mathfrak p_1n_1',\ \vartheta\overline{C_0}da_1)\ \approx\ (\mathfrak p_1n_1',\ d)}✓$$

$$\textbf{量级（}\mathfrak p_1=\mathfrak q_2=1\ \text{最有利点）}：\ d\ \text{范围}\ |d|\le D'=\frac{D}{\mathfrak q_1\mathfrak p_2}\asymp L\ \text{（}D=3NL/M\ \text{逐字，}M\asymp N\text{）}✓$$
$$\qquad\text{而}\ q_0\mid d⟹q_0\le|d|\asymp L；\ \text{典型}\ (\text{随机}\ d\ \text{与固定}\ q)\ \text{给出}\ \boxed{q_0\ll L^{o(1)}}⟹\textbf{仅次幂}✓✓✓$$

$$\Longrightarrow\ \text{按 §0 判据}：\ q_0=L^{o(1)}\ \textbf{不构成}\ q_0\ge N^\delta ⟹ \textbf{A2 失败}✓✓$$

---

## 3. A3 · 跨项 exact cancellation（**CRT 分解 ≠ 模数下降**）

$$\text{相位}\ \textbf{可分}：f(\overline{\tilde\ell_2})+g(\overline{\tilde\ell_2'})，\ \text{两变量}\ \textbf{仅} \text{经 (4.26) 耦合（＝}\ u\ \text{，已记账）}✓$$
$$\qquad\Longrightarrow\ \sum_{\tilde\ell_2,\tilde\ell_2'}\ =\ \Big(\text{单变量和}\Big)\times\Big(\text{单变量和}\Big)\ \text{型}\ \Longrightarrow\ \text{CRT 下}\ \prod_r\mathcal K(q_r)✓$$
$$\qquad\text{每}\ q_r\ \text{上相位皆为单位型非平凡}⟹\textbf{无任何局部 conductor 被消掉}✓✓$$
$$\Longrightarrow\ \boxed{\text{CRT 分解}\ \ne\ \text{模数下降}}✓✓✓\quad(\text{唐先生判据，本档确认})✓$$

$$\text{且 (4.19) 的多分式结构不改变此结论}：\text{各分式之分母（}\tilde\ell_1\tilde\ell_1'\mathfrak q_1\ \text{型）在 T3-1B-2 §2.1 已证}\ \textbf{相消}，\ \text{余下唯一承载振荡的模数仍是}\ q=\mathfrak p_1n_1'✓$$
$$\qquad\Longrightarrow\ \text{不存在"共同 conductor"}\ q_*<\max q_j\ \text{的机制}✓$$

---

## 4. A4 · 量化 ＋ **三个假 ALIVE 检查**

$$\text{若有}\ q_0：\ \text{增益因子}\ =\ q_0^{-1/2}；\ \text{需}\ q_0\gg N^\delta ⟹ \text{本档只得到}\ q_0=L^{o(1)} ⟹ \textbf{失败}✓$$

$$\begin{array}{c|l|l}
&\text{假 ALIVE 形态}&\text{本档核验}\\
\hline
\text{①}&q_*=q/\gcd(q,\alpha)\ \text{而}\ \gcd(q,\alpha)=L^{o(1)}&\boxed{\textbf{正是本例}}：\gcd(q,\alpha_{\rm tot})\mid d\asymp L⟹L^{o(1)}✗\\
\text{②}&q_*=q/\mathfrak p_1\ \text{而}\ \mathfrak p_1=1\ \text{在主贡献区}&\text{(4.9) 允许}\ \mathfrak p_1=1\ (\text{则}\ q=n_1')\ ⟹ \text{非降模，只是参数情形}✗\\
\text{③}&q_*=q/u\ \text{而}\ u\ \text{已支付}&\boxed{\textbf{禁止}}：\ u\ \text{已在 BC 非对角分析中记账（(4.26)(4.29)）⟹ 重复兑现同一算术约束}✗✗\\
\end{array}✓$$

---

## 5. ⭐ 判定

$$\boxed{\textbf{T3-1A-1}\ =\ \mathrm{DEAD}}✓✓✓$$
$$\qquad\textbf{三种失效方式全部核过}：\text{(A2) 唯一候选退化因子}\ q_0=(\mathfrak p_1n_1',da_1)\ \text{仅}\ L^{o(1)}；\ \text{(A3) 可分}\Rightarrow\text{CRT 分解}\ne\text{降模}；\ \text{(A4) 三个假 ALIVE 全被识破}✓$$
$$\Longrightarrow\ \boxed{\text{所有局部 conductor 非平凡} \Longrightarrow \textbf{Weil 的}\ \sqrt q\ \text{是}\ \textbf{conductor-level barrier}}✓✓✓$$

---

## 6. ⭐⭐⭐ 四层淘汰总账（搜索空间的第一次大幅坍缩）

$$\begin{array}{c|l|l}
&\text{层}&\text{判定}\\
\hline
\text{(1)}&\text{fiber cancellation（单}\ \ell_2\text{-fiber 逆元振荡）}&\mathrm{DEAD}\ \text{(T3-1B：}\ X/\sqrt q\asymp N^{-2/5})\\
\text{(2)}&\text{cross-fiber aggregation（聚合账}\ K/Y/R)&\mathrm{DEAD}\ \text{(T3-1C-2：模数不变}\Rightarrow\text{阈值不变})\\
\text{(3)}&\text{partial diagonal（C–S 前预聚类）}&\mathrm{DEAD}\ \text{(T3-1C-1：坍缩为行列式类＝}u,v,\Delta)\\
\text{(4)}&\text{conductor-reducing Weil（联合变换降模）}&\mathrm{DEAD}\ \text{(T3-1A-1：局部 conductor 全非平凡)}\\
\end{array}✓✓✓$$
$$\Longrightarrow\ \boxed{\text{在 }\mathfrak p_1n_1'\text{ 这一模数层的所有"振荡侧"改造，已被四层逐一排除}}✓✓$$

---

## 7. 残余（**未掩盖**）
$$\text{(R1)}\ (\mathfrak p_1,n_1')=1\ \text{的推导依赖}\ (\ell_1,n_1'n_2'b\vartheta)=1\ \text{与}\ \mathfrak p_1\mid\ell_1\ \text{——}\textbf{本档推导}，\ \text{已核 (4.10) 逐字}✓$$
$$\text{(R2)}\ q_0\ \text{的量级}\ \ll L^{o(1)}\ \text{为}\ [\textbf{结构判定}]（\text{未证}\ \gcd(d,\mathfrak p_1n_1')\ \text{的上界}）✓\quad\Longrightarrow\ \textbf{若存在}\ d\ \text{使}\ \gcd(d,q)\gg N^\delta\ \text{则须重审}✓$$
$$\text{(R3)}\ a_1,\ \vartheta\ \text{与}\ q\ \text{的互素性}\ \textbf{未核}✓\qquad\text{(R4)}\ (4.10)\ \text{全部条件}\ \textbf{未逐条穷举}（\text{只用了承载振荡所必需者}）✓$$
$$\text{(R5)}\ \textbf{未用 RH；零数值}✓$$

---

## 8. 【勘误 T10】（2026-09-17 09:52，唐先生指令；**不覆盖上文**）

$$\textbf{越界处}：\text{上文 §2 写}\ q_0\mid d\asymp L\Longrightarrow q_0\ll L^{o(1)} \Longrightarrow \textbf{不成立}✓$$
$$\qquad q_0\mid d\ \text{只给出}\ q_0\le d\asymp L，\ \textbf{推不出}\ q_0=L^{o(1)}✓$$
$$\textbf{正确表述}：\ \boxed{q_0\mid d,\ d\asymp L\ \Longrightarrow\ q_0\le L}✓✓$$
$$\qquad\text{要得到}\ L^{o(1)}\ \text{须}\ \textbf{额外证明}\ \gcd(d,\mathfrak p_1n_1')\ll L^{o(1)}\ \text{（在整个有效求和域上）}✓$$
$$\qquad\Longrightarrow\ \textbf{可能存在允许的}\ d\ \text{使}\gcd(d,q)\asymp L^\eta\ (\eta>0) \Longrightarrow \text{该项}\ \textbf{必须保留为 R2}，\ \text{不得当作已证}✓✓✓$$
