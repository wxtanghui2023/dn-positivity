# V2-19 — **四步追因链 第 1–2 步：$L^{*}$ 对应项 ＋ 承重项**（精确吻合）

> 唐先生 2026-09-16 21:24「继续」；按 REVIEW-V2B 工作单的四步链起手✓
> $$\boxed{\text{最终指数}\to L^{*}\ \text{中对应项}\to\text{(3.1)/(4.4) 输入项}\to\text{具体}\ \mathrm{C\text{-}S／diagonal／Weil／}\delta\text{-split}\ \text{结构}}$$

---

## 1. $L^{*}$ 三个单项式 ↔ 平衡伙伴（**本档逐项验证**）
$$(5.1)\ \text{六项}\：F_1=\tfrac{AM(bN)^{1/2}}{L^{1/2}},\ F_2=\tfrac{AM^2}{bLN},\ F_3=\tfrac{M^2}{L},\ F_4=\tfrac{b^{3/4}AM^{1/2}N^{5/4}}{L^{1/2}},\ F_5=b^{1/2}AL^{3/2}N^{7/4},\ F_6=\tfrac{b^{1/2}A^{1/2}MN}{L}✓$$
$$\text{平衡}：F_5\ \approx\ F_2+F_3+F_6 \Longrightarrow \textbf{三个伙伴各给一个}\ L^{*}\ \text{单项式}：$$
$$\qquad F_5=F_2\Rightarrow L^{5/2}=\frac{M^2}{b^{3/2}N^{11/4}}\Rightarrow \boxed{L_{(2)}=\frac{M^{4/5}}{b^{3/5}N^{11/10}}}✓✓$$
$$\qquad F_5=F_3\Rightarrow L^{5/2}=\frac{M^2}{b^{1/2}AN^{7/4}}\Rightarrow \boxed{L_{(3)}=\frac{M^{4/5}}{b^{1/5}A^{2/5}N^{7/10}}}✓✓$$
$$\qquad F_5=F_6\Rightarrow L^{5/2}=\frac{M}{A^{1/2}N^{3/4}}\Rightarrow \boxed{L_{(6)}=\frac{M^{2/5}}{A^{1/5}N^{3/10}}}✓✓$$
$$\Longrightarrow\ \boxed{L_{(2)}+L_{(3)}+L_{(6)}\ =\ \text{原文}\ L^{*}\ \text{（＋}M^{\varepsilon}\ \text{为平凡加项）}}\ ✓✓\ (\textbf{三项全吻合})✓$$

## 2. ⭐ 哪个单项式**支配**（$M\asymp N,\ A=1,\ b=1$）
$$L_{(2)}=N^{4/5-11/10}=N^{-3/10}✓\quad L_{(3)}=N^{4/5-7/10}=N^{1/10}✓\quad L_{(6)}=N^{2/5-3/10}=N^{1/10}✓$$
$$\Longrightarrow\ \boxed{L^{*}\asymp N^{1/10}=M^{1/10}}✓\quad(\text{由}\ L_{(3)}\ \text{与}\ L_{(6)}\ \text{共同支配}；L_{(2)}\ \text{极小，不参与})✓$$

## 3. ⭐⭐ 代入：**绑定对＝$F_3$ 与 $F_5$**，且与 (1.2) **精确吻合**
$$L=N^{1/10}\ \text{代入六项}（A=1,M=N,b=1）：$$
$$\qquad F_1=N^{3/2-1/20}=N^{29/20}✓\quad F_2=N^{1-1/10}=N^{9/10}✓\quad \boxed{F_3=N^{2-1/10}=N^{19/10}}✓$$
$$\qquad F_4=N^{7/4-1/20}=N^{17/10}✓\quad \boxed{F_5=N^{3/20+7/4}=N^{38/20}=N^{19/10}}✓\quad F_6=N^{1-1/10}=N^{9/10}✓$$
$$\Longrightarrow\ \boxed{\max_j F_j=F_3=F_5=N^{19/10}}✓✓\quad(\textbf{绑定对恰是}\ F_3\ \text{与}\ F_5\ \text{——与平衡条件自洽})✓$$
$$\textbf{取外平方根}（\text{因}\ \mathcal B\ll C_b^{1/2}）\：\ \mathcal B\ll N^{19/20}✓✓$$
$$\textbf{对照 (1.2)}：\ T_1=(AMN)^{7/20}(M+N)^{1/4}\ \xrightarrow{A=1,M=N}\ N^{7/10}\cdot N^{1/4}=\boxed{N^{19/20}}✓✓✓\quad(\textbf{精确吻合})✓✓$$

## 4. ⭐⭐⭐ 第 1–2 步的结论
$$\boxed{\text{第 1 步（最终指数}\to L^{*}\ \text{对应项）}\ = \ \boxed{L_{(3)}=\frac{M^{4/5}}{b^{1/5}A^{2/5}N^{7/10}}}✓✓\quad(\text{由}\ F_5\approx F_3\ \text{给出})}✓$$
$$\boxed{\text{第 2 步（}\to\text{(3.1)/(4.4) 输入项）}：\ \textbf{两个承重项}\ F_3\ \text{与}\ F_5}✓✓：$$
$$\qquad F_3=\frac{M^2}{L}\ \Longleftarrow\ D_b\ \text{的}\ \textbf{"}M\text{"}\ \text{项}\times\frac ML \Longrightarrow \boxed{\text{§3 diagonal（(3.1)，用}\ \textbf{Weil 界}\text{）}}✓✓\quad(\text{承 V2-9 溯源})$$
$$\qquad F_5=b^{1/2}AL^{3/2}N^{7/4}\ \Longleftarrow\ D_b\ \text{的}\ \frac{b^{1/2}AL^{5/2}N^{7/4}}{M}\ \text{项}\times\frac ML \Longrightarrow \boxed{\text{§4 off-diagonal（(4.4)）}}✓✓$$
$$\Longrightarrow\ \boxed{\text{即}\ 17/33\ \text{的第一项指数由}\ \textbf{§3 diagonal 与 §4 off-diagonal 的竞争} \text{承载}}✓✓✓$$

## 5. 下一步（第 3 步，下会话/本轮续）
$$\boxed{\text{第 3 步}：\ F_3\ \text{与}\ F_5\ \text{各自具体由}\ (3.1)\ /\ (4.4)\ \text{的}\ \textbf{哪一个推导步骤} \text{产生}}$$
$$\qquad F_3\ \text{侧：}\ (3.1)\ \text{（}\S3\ \text{diagonal 的界）中哪一步产生}\ \textbf{"}M\text{"}\ \text{量级项}\（\text{疑为 Weil 界在扩大 diagonal 上的应用}）✓$$
$$\qquad F_5\ \text{侧：}\ (4.4)\ \text{中哪一步产生}\ \textbf{最高}\ L\ \text{-幂}\ \text{的项}\（L^{5/2}）\（\text{疑为}\ \delta\ne0\ \text{支的}\ n'_2\text{-Weil 应用，承 V2-11}）✓$$

## 6. 残余（不得省略）
$$\text{残余 1：}\ F_3/F_5\ \text{与}\ (3.1)/(4.4)\ \text{的对应}\ \textbf{依据 V2-6b／V2-9 的溯源}（D_b\to C_b\ \text{因子}=M/L\ \text{四项验证）}，}\ \textbf{未} \text{逐行核 (3.1)/(4.4) 全文}✓$$
$$\text{残余 2：本档取}\ b=1\ \text{作指数核算（}b\ \text{为结构变量，}\text{V2-18-A}）✓\quad\text{残余 3：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只做四步链第 1--2 步；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值（仅指数量级与恒等式）}✓$$

## 8. 净产出
$$\text{(i) ⭐ }L^{*}\ \text{三单项式 ↔ 平衡三伙伴}\ \textbf{逐项吻合（本档计算）}✓✓$$
$$\text{(ii) ⭐ 支配项：}M\asymp N,A=1,b=1\Longrightarrow L^{*}\asymp N^{1/10}\ \text{（由}\ L_{(3)},L_{(6)}\ \text{支配；}L_{(2)}\ \text{极小）}✓$$
$$\text{(iii) ⭐⭐ 绑定对：}\ \max_jF_j=F_3=F_5=N^{19/10}\Longrightarrow \mathcal B\ll N^{19/20}\ \text{＝(1.2) 的}\ T_1\ \textbf{精确吻合}✓✓✓$$
$$\text{(iv) ⭐⭐⭐ 第 1 步结论：}\ L^{*}\ \text{对应项＝}\ L_{(3)}=M^{4/5}/(b^{1/5}A^{2/5}N^{7/10})✓✓$$
$$\text{(v) ⭐⭐⭐ 第 2 步结论：两承重项}\ F_3=\frac{M^2}{L}\ \text{（§3 diagonal，(3.1)，Weil）与}\ F_5=b^{1/2}AL^{3/2}N^{7/4}\ \text{（§4 off-diagonal，(4.4)）}✓✓$$
$$\qquad\Longrightarrow \boxed{17/33\ \text{的第一项指数由}\ \textbf{§3 diagonal 与 §4 off-diagonal 的竞争} \text{承载}}✓✓$$
