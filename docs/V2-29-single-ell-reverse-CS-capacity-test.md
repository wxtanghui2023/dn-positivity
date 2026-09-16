# V2-29 — **REVERSE-C--S CAPACITY AUDIT**：单个 $\ell$ 的最小扰动测试

> 唐先生 2026-09-16 21:48 拍板 **V2-29 ＝ 单个 $\ell$ 的反向 C--S 容量测试**✓
> ⚠️ **收紧（采纳）**：$\boxed{L^5=L^4\times L\ \not\Rightarrow\ \text{"把更多}\ \ell\ \text{放进 C--S 即可减少}\ L\text{"}}$ —— 那是**候选机制，不是单调关系**✓✓
> 理由（唐先生）：C–S 同时改变对角条件、平方后变量数、后续 Weil 对象；BC 的 longer-diagonal 正是该 trade-off 的产物✓

---

## 1. 测试设定（最小扰动）
$$\mathcal L_{\rm free}=\{\ell_1,\ell_2,\ell_1',\ell_2'\}\quad(\text{BC 保留在}\ \textbf{未平方组})\Longrightarrow \text{贡献}\ L^4✓$$
$$\textbf{最小扰动}：\ \text{只把一个}\ \ell\ \text{移入平方组} \Longrightarrow \text{计数预期}\ L^4\to L^3✓$$
$$\text{五问（唐先生指定）}：\text{(1) 计数收益；(2) 对角条件；(3) 新平方和可否控制；(4) longer-diagonal 收益损失；(5) 回到}\ (F_3,F_5)\ \text{envelope}✓$$

## 2. ⭐⭐ 关键结构事实：四个 $\ell$ **不是自由求和**（本档核心观察）
$$\text{由 §4.1.3.2 的}\ (\mathfrak p,\mathfrak q)\ \text{分解（逐字）}：\ \mathfrak p_1,\mathfrak q_1|(\ell_1,\ell_1'),\quad \mathfrak p_2,\mathfrak q_2|(\ell_2,\ell_2')✓$$
$$\qquad\Longrightarrow\ \boxed{\text{四个}\ \ell\ \text{通过}\ (\mathfrak p,\mathfrak q)\ \text{分解与}\ \textbf{互补因子}\ \tilde\ell_1,\tilde\ell_2\ \text{结构绑定}}✓✓$$
$$\text{且}\ \Delta\ \text{逐字（(4.19) 后）}：\Delta：＝a_2(d\tilde\ell_1'-d'\tilde\ell_1)\tilde\ell_2\tilde\ell_2'\mathfrak p_2-(da_1\tilde\ell_2'-d'a_1'\tilde\ell_2)\tilde\ell_1\tilde\ell_1'\mathfrak q_1✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{四个}\ \tilde\ell\ \text{以}\ \textbf{线性} \text{方式进入}\ \Delta\ \text{（}\Delta=0/\ne0\ \text{分裂即建立于此）}}✓✓$$
$$\text{再者（§2 设定）}：\ \text{对角条件}\ \boxed{\ell_1n_1=\ell_2n_2}\ \text{——}\ \textbf{线性} \text{于}\ \ell✓✓$$

## 3. ⭐⭐⭐ 五问逐一（结构性回答）
$$\textbf{(1) 计数收益}：\ \text{平方一个}\ \ell\Longrightarrow \text{若其余结构不变，则}\ L^4\to L^3 \Longrightarrow \mathcal V\ \text{级}\ L^5\to L^4 \xrightarrow{\text{开方}} L^{5/2}\to L^{2}\Longrightarrow \boxed{F_5\ \text{的}\ L^{3/2}\to L^{1}}✓$$
$$\qquad\textbf{但}：\ \text{此收益}\ \textbf{以"其余结构不变"为条件} \Longrightarrow \text{恰是待验之处}✓$$
$$\textbf{(2) 对角条件}：\ \text{平方}\ \ell_1\ \text{后，}\ \ell_1\ \text{的求和变为}\ |\sum_{\ell_1}|^2 \Longrightarrow \text{出现新副本}\ \ell_1'' \Longrightarrow \text{新对角条件形如}\ \ell_1''n_1''=\dots$$
$$\qquad\Longrightarrow\ \boxed{\text{原}\ \textbf{线性} \text{对角}\ \ell_1n_1=\ell_2n_2\ \text{被}\ \textbf{破坏}}✓✓\quad(\text{因平方后}\ \ell_1\ \text{不再线性出现})✓$$
$$\textbf{(3) 新平方和可否控制（最关键）}：\ \text{平方}\ \ell_1\Longrightarrow\ \tilde\ell_1\ \text{的线性结构受损} \Longrightarrow \Delta\ \text{中}\ \tilde\ell_1\ \text{项变为}\ \textbf{二次型}✓✓$$
$$\qquad\Longrightarrow\ \text{平方后的对象}\ \textbf{不再是线性 Kloosterman／Weil 型} \Longrightarrow \boxed{\text{需要}\ \textbf{新估计}}✓✓\quad(\text{＝唐先生情形 C："成本搬家"})✓$$
$$\textbf{(4) longer-diagonal 收益损失}：\ \text{BC 相对 DFI 的收益（}\tfrac1{48}\to\tfrac1{20}\text{）}\ \textbf{恰来自} \text{对}\ \ell\ \text{的}\ \textbf{不平方}✓✓$$
$$\qquad\Longrightarrow\ \text{平方任一}\ \ell \Longrightarrow \text{该收益}\ \textbf{消失（回到 DFI 型）} \Longrightarrow \boxed{\text{唐先生情形 A}}✓✓$$
$$\textbf{(5) envelope}：\ \text{按唐先生纪律，本档}\ \textbf{不} \text{做 envelope 重优化（需先有净幂次收益）}✓$$

## 4. ⭐⭐⭐ 判定
$$\boxed{\text{倾向 A／C，}\ \textbf{非净收益}}✓✓\quad(\text{即}\ L\ \text{收益是"成本搬家"或"失去 longer-diagonal 的价格"})✓$$
$$\qquad\textbf{机制（三条，全部结构性）}：\ \text{(i) 四个}\ \ell\ \text{经}\ (\mathfrak p,\mathfrak q)\ \text{与互补因子}\ \tilde\ell\ \text{绑定，}\ \textbf{非自由求和}✓$$
$$\qquad\qquad\text{(ii) 对角}\ \ell_1n_1=\ell_2n_2\ \text{与}\ \Delta\ \text{皆}\ \textbf{线性} \text{于}\ \ell/\tilde\ell \Longrightarrow \text{平方破坏线性性}✓✓$$
$$\qquad\qquad\text{(iii) BC 的 longer-diagonal 收益}\ \textbf{正以 $\ell$ 不平方为代价换来}✓✓$$
$$\textbf{但}：\ \boxed{\text{未证}} \text{——需}\ \textbf{逐行重建} \ \mathrm{C\!-\!S}\to\text{diagonal}\to\Delta\to\text{Weil}\ \text{账本}✓\quad(\text{唐先生情形 A/B/C 均未被证明})✓$$
$$\qquad\Longrightarrow\ \text{记}\ \boxed{\mathrm{A\text{-}倾向／OPEN}}✓\quad(\textbf{不} \text{宣布 DEAD；}\textbf{不} \text{宣布 ALIVE})✓$$

## 5. ALIVE 判定线（唐先生指定，预登记）
$$\text{若单个}\ \ell\ \text{的平方给出}\ \boxed{L^4\to L^{3+\varepsilon}}\ \text{且}\ \textbf{longer-diagonal 仍存在} \Longrightarrow \boxed{\textbf{本弧线第一个 ALIVE 候选}}✓✓$$
$$\text{若一个}\ \ell\ \text{都不能平方而得净收益} \Longrightarrow \text{对"四个一起改"路线形成}\ \textbf{很强的结构性证据}✓✓$$

## 6. 残余（不得省略）
$$\text{残余 1（关键）：}\ \text{五问中 (2)(3)(4) 的}\ \textbf{逐行重建} \text{未做——本档为结构性判定，非逐行账本}✓✓$$
$$\text{残余 2：}\ \text{平方后的新对象}\ \textbf{具体形式} \text{未写出}（\text{需 §4.1.2--§4.1.3.3 逐行}）✓$$
$$\text{残余 3：}\ \text{唐先生情形 A/B/C}\ \textbf{均未被证明}✓\quad\text{残余 4：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只做单个}\ \ell\ \text{的最小扰动；}\quad\text{② }\textbf{不碰} \ F_5\ \text{整体优化、}\textbf{不找新论文}；\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) ⚠️ 收紧采纳：}\ L^5=L^4\times L\ \textbf{不} \text{蕴含单调关系}✓✓$$
$$\text{(ii) ⭐⭐ 结构事实：四个}\ \ell\ \textbf{非自由求和}（\text{经}\ (\mathfrak p,\mathfrak q)\ \text{与}\ \tilde\ell\ \text{绑定}）；\ \text{对角与}\ \Delta\ \textbf{皆线性} \text{于}\ \ell/\tilde\ell✓✓$$
$$\text{(iii) ⭐⭐⭐ 五问结构判定：}\ \text{(1) 计数可降}\ L^{1/2}；\ \text{(2) 线性对角被破坏；\ (3) 平方后}\ \textbf{非线性 Kloosterman 型} \Longrightarrow \text{需新估计；\ (4) longer-diagonal 收益消失}✓✓$$
$$\text{(iv) 判定}\ \boxed{\mathrm{A\text{-}倾向／OPEN}} \text{（未证；需逐行重建）}✓✓$$
$$\text{(v) ALIVE 判定线预登记：}\ \text{若}\ L^4\to L^{3+\varepsilon}\ \text{且 longer-diagonal 仍在} \Longrightarrow \text{首个 ALIVE 候选}✓$$
