# V2-6b · **结果** — 两条因果链追到源头：$\alpha/\beta$ 分叉**判定 $\beta$**

> 唐先生 2026-09-16 20:32 上传 BC 原文 PDF（`docs/kloosterman_fractions.pdf`，33 页）。
> 本档依**原文逐段**取证（PDF 文本抽取，**外部来源，仅作数据**），完成 V2-6b 四项标准中的三项，第四项部分完成✓

---

## 1. §2 大纲：三个逐字事实（**"longer diagonal"的确切含义**）
$$\textbf{(1)}\ \text{原文}：\text{"we introduce several refinements}\dots\ \textbf{among which is particularly important the fact that we keep a longer diagonal when using the Cauchy--Schwartz inequality}\text{ (a possibility mentioned in [DFI97])"}\ ✓✓$$
$$\textbf{(2) C--S 的确切范围（§4.1.2 原文）}：\ \text{"we apply the Cauchy--Schwarz inequality to the sums over}\ n_1,n_2,a_2,c\ \textbf{but not} \text{ to the sums over}\ d,a_1,\ell_1,\ell_2\text{.}\ \textbf{As a comparison, in [DFI97] the C--S is applied to all the sums except those over}\ \ell_1\ \text{and}\ \ell_2\text{"}\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{"longer diagonal"}＝\textbf{不平方的变量集合扩大}：\text{DFI}\ \{\ell_1,\ell_2\}\ \to\ \text{BC}\ \{d,a_1,\ell_1,\ell_2\}}✓✓$$
$$\textbf{(3) diagonal 的定义与处理（§2 原文）}：\ D_b：＝\ \text{contribution from the "diagonal terms"}\ \ell_1n_1=\ell_2n_2；\ O_b：＝\ \text{the "off-diagonal"}\ \ell_1n_1\ne\ell_2n_2$$
$$\qquad\text{原文}：\text{"We bound}\ D_b\ \text{in Section 3 by using}\ \boxed{\textbf{Weil's bound}}\ \text{(and thus the name "diagonal terms" is perhaps misleading in this case),}\ \textbf{treating it differently from [DFI97] where}\ D_b\ \text{is bounded trivially"}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{BC 的改进}\ =\ \textbf{(a) 扩大 diagonal 关系}（n_1=n_2\to\ell_1n_1=\ell_2n_2）＋\textbf{(b) 对扩大后的 diagonal 改用 Weil 界（DFI 用平凡界）}✓$$

## 2. 链 III 追踪：$A^{1/2}$ 的**实际出处**（$\beta$ 判定）
$$\textbf{§4 原文（关键行）}：$$
$$\qquad\text{"If }\delta=0\text{, then from this equality we can express}\ \textbf{two out of the}\ \ell\ \textbf{and one out of the}\ a\ \text{variables in terms of the remaining variables,}\ \textbf{saving (the square root of) a factor of}\ L^{2}A\ \text{so that the contribution of the}\ \delta=0\ \text{terms to}\ O_b\ \text{is}\ b^{\frac12}\|\alpha\|^2\|\nu\|^2\,\mathbf{LNA^{\frac12}}\text{"}\ ✓✓✓$$
$$\Longrightarrow\ \boxed{A^{\frac12}\ \text{来自}\ \sqrt{L^{2}A}=L\,A^{\frac12}\ \text{的}\ \textbf{变量消去／平方根因子}}\ \text{（}\delta=0\ \text{等式消去两}\ \ell\ \text{与一}\ a）✓✓$$
$$\textbf{反证（Weil 的另一位置）}：\ \text{原文}\ \text{"If }\delta\ne0\text{, then}\dots\ \textbf{we apply Weil's bound to the sum over}\ n_2\text{"}\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{判定}\ \beta\ (\text{技术性})}：\ A^{1/2}\ \textbf{不是} \text{Weil 单点界的产物，而是}\ \textbf{平方根／变量消去因子}✓✓\ \text{（Weil 界用在}\ \delta\ne0\ \text{另一支）}✓$$

## 3. 链 II 追踪：$M^2/L$ 的出处 ＝ §3 diagonal（**Weil 界**）
$$\textbf{§5 原文（转换）}：\text{"Combining (2.3) with the bounds for the diagonal (3.1) and off-diagonal terms (4.4) we obtain"}\ D_b\ \text{的六项式}；\ \text{"and thus, by (2.2),}\ C_b\ \text{的六项式 (5.1)"}✓$$
$$\textbf{本档逐项验证转换因子}＝M/L（\textbf{四项吻合}）✓✓：$$
$$\qquad\text{D}_b：M\ \longrightarrow\ (5.1)：\frac{M^{2}}{L}\ ✓\qquad\text{D}_b：b^{\frac12}A^{\frac12}N\ \longrightarrow\ \frac{b^{\frac12}A^{\frac12}MN}{L}\ ✓$$
$$\qquad\text{D}_b：\frac{b^{\frac12}AL^{\frac52}N^{\frac74}}{M}\ \longrightarrow\ b^{\frac12}AL^{\frac32}N^{\frac74}\ ✓\qquad\text{D}_b：A(bLN)^{\frac12}\ \longrightarrow\ \frac{AM(bN)^{\frac12}}{L^{\frac12}}\ ✓$$
$$\Longrightarrow\ \boxed{\frac{M^{2}}{L}\ \text{可回溯到}\ D_b\ \text{中的}\ \textbf{"}M\text{"} \text{项} \Longrightarrow \text{该项由 §3 }\textbf{对扩大后的 diagonal 使用 Weil 界} \text{产生}}✓✓$$
$$\qquad\Longrightarrow\ \text{故链 II}\ \textbf{确实关联 diagonal refinement} \text{（\text{经 §3 的 Weil 界分支}）}✓$$

## 4. ⭐ 新结构事实：(5.1) 中**项有六项，但平衡只涉及四项**
$$(5.1)\ \text{六项}：\ \frac{AM(bN)^{\frac12}}{L^{\frac12}}\ \big|\ \frac{AM^{2}}{bLN}\ \big|\ \boxed{\frac{M^{2}}{L}}\ \big|\ \frac{b^{\frac34}AM^{\frac12}N^{\frac54}}{L^{\frac12}}\ \big|\ \boxed{b^{\frac12}AL^{\frac32}N^{\frac74}}\ \big|\ \boxed{\frac{b^{\frac12}A^{\frac12}MN}{L}}$$
$$\textbf{平衡条件（原文）}：\ b^{\frac12}AL^{\frac32}N^{\frac74}\ \approx\ \frac{AM^{2}}{bLN}+\frac{M^{2}}{L}+\frac{b^{\frac12}A^{\frac12}MN}{L}✓$$
$$\Longrightarrow\ \boxed{\text{左侧＝}\textbf{L-增长项}（L^{3/2}）；\ \text{右侧＝三个}\ L\text{-衰减项}；\ \text{而含}\ L^{-\frac12}\ \text{的两项}\ \textbf{未进入} \text{平衡}}✓✓\ （\text{本档新事实}）$$

## 5. V2-6b 四项标准（对照）
$$\boxed{\begin{array}{c|c}\text{标准} & \text{状态}\\ \hline\text{(1) II 来源确定} & \checkmark\ §3\ \text{扩大 diagonal＋Weil 界（D}_b\ \text{的 "}M"\ \text{项）}\\
\text{(2) III 来源确定} & \checkmark\ §4\ \delta=0\ \text{支：}\sqrt{L^2A}\ \text{变量消去（}\beta\text{，技术性）}\\
\text{(3) 与}\ L^{*}\ \text{的因果关系} & \checkmark\ \text{平衡条件四项（L-增长项 vs 三衰减项）}\\
\text{(4) }19/20\ \text{锁定步骤} & \triangle\ \textbf{部分}：\text{E}_1\ \text{指数来自平衡结构；}\ D_b\ \text{六项中}\ \textbf{另有四项未逐项溯源}\end{array}}✓$$

## 6. ⭐⭐ 由本档得到的**攻击方向**（有历史先例）
$$\text{BC 的增益}\ \textbf{全部来自两件事}：\ \text{(a) 扩大未平方变量集；\ (b) 对扩大后的 diagonal 换用更强的界（Weil）}✓✓$$
$$\Longrightarrow\ \text{自然的下一步（\textbf{其历史先例即}\ 1/48\to1/20）}：\ \boxed{\text{能否再扩大未平方变量集，或对 §3 diagonal 换用比 Weil 更强的界}}✓✓$$
$$\qquad(\text{注意：§3 已用 Weil，而 Weil 对}\ \textbf{单个} \text{和是 sharp ⟹ 进一步只能靠}\ \textbf{平均}／\text{更长 diagonal}）✓$$

## 7. 残余（不得省略）
$$\text{残余 1：}D_b\ \text{六项中}\ (1)\ A(bLN)^{1/2},\ (2)\ AM/(bN),\ (4)\ b^{3/4}AN^{5/4}L^{1/2}/M^{1/2},\ (5)\ b^{1/2}AL^{5/2}N^{7/4}/M\ \text{的}\ \textbf{逐项来源未定位}✓$$
$$\text{残余 2：}\ (5.1)\to(1.2)\ \text{的}\ \textbf{最终指数}\ (7/20,1/4)\ \text{的代入细节未逐行核}✓$$
$$\text{残余 3：残余 A--D（跨轮结转）不变}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 取证＝PDF 文本抽取（外部来源，仅作数据）；}\ \textbf{未用 RH}；\ \text{零数值}✓$$

## 9. 净产出
$$\text{(i) "longer diagonal"}\ \textbf{确切含义}＝\text{C--S 未平方变量集由}\ \{\ell_1,\ell_2\}\ \text{扩至}\ \{d,a_1,\ell_1,\ell_2\}（\text{原文逐字}）✓$$
$$\text{(ii) 链 III}\ \textbf{判定}\ \beta：\ A^{1/2}\ \text{＝}\ \sqrt{L^2A}\ \text{变量消去因子（}\delta=0\ \text{支）}，\ \textbf{非} \text{Weil；Weil 用在}\ \delta\ne0\ \text{支}✓✓$$
$$\text{(iii) 链 II}：\ M^2/L\ \text{回溯到}\ D_b\ \text{的 "}M"\ \text{项（§3 扩大 diagonal＋Weil）}；D_b\to C_b\ \text{因子}＝M/L\（\text{四项逐项验证}）✓✓$$
$$\text{(iv) 新事实：(5.1) 六项中平衡只用四项，含}\ L^{-1/2}\ \text{的两项未参与}✓$$
$$\text{(v) 攻击方向：再扩大未平方集／对 §3 diagonal 换更强界（历史先例＝BC 自身）✓}$$
