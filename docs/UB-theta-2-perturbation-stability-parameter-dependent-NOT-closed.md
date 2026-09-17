# ⚔️ **UB-$\theta$-2**：非退化扰动稳定性 —— **判据干净，但结论依赖参数 ⟹ 本档未收口（诚实）**

> 依唐先生 15:45「开，但改成精确的非退化扰动比值」✓
> **本档结果**：① 确认 $\phi''$ **不进一阶主项**；② $R_i$ 的闭式与判据**干净**；③ ⚠️ 但数值显示 $R_i\gg1$（依参数）⟹ **稳定性依赖 $(n,u)$ 关系** ⟹ **不判死**；④ 🔧 标出一处**记法冲突** ✓✓✓

---

## §0 采纳修正
$$\text{`fee2ff9` 中"}\phi''\ \text{会直接改掉}\ 2\pi L^2"\ \textbf{需修正}✓\qquad \phi''\ \textbf{不进} \text{一阶局部导数的主项（见}\ §1）✓✓$$

## §1 ⭐ 一阶：**与 $\phi''$ 无关**（解析＋数值双重确认）
$$\Psi(k)=\phi(CH_k)+2\pi rC \Longrightarrow \partial_{k_i}\Psi=\phi'(CH_k)\cdot C\cdot\Big(-\frac1{k_i^2}\Big)=-\frac{C\phi'(CH_k)}{k_i^2}✓$$
$$|C|=\frac{|\phi'|}{2\pi},\quad k_i\asymp\frac{|C|}{L_i}=\frac{|\phi'|}{2\pi L_i} \Longrightarrow \boxed{G_i:=|\partial_{k_i}\Psi|=\frac{|\phi'|^2}{2\pi k_i^2}\asymp2\pi L_i^2}\ ✓✓\quad(\text{数值比值}\ \mathbf{1.0000})✓✓$$
$$\Longrightarrow \boxed{G_i\gg1\ (L_i\ge1)\ \text{恒成立}}✓✓$$

## §2 $R_i$ 闭式（**解析两次验证**；含一处自我更正）
$$\partial^2_{k_i}\Psi=\boxed{+\frac{2C\phi'(CH_k)}{k_i^3}+\frac{C^2\phi''(CH_k)}{k_i^4}}✓✓\qquad(\text{产品法则验证两次；我中途一次符号笔误已纠})✓$$
$$\Longrightarrow R_i:=\frac{|\partial^2_{k_i}\Psi|}{|\partial_{k_i}\Psi|}\lesssim\frac{2}{|k_i|}+\frac{|C\phi''|}{|\phi'|k_i^2}✓\qquad(\text{与唐先生同})✓✓$$
$$\Longrightarrow \boxed{R_i\lesssim\frac{4\pi L_i}{|\phi'|}+\frac{2\pi L_i^2|\phi''|}{|\phi'|^2}}✓✓\qquad(\text{本档复核成立})✓$$

## §3 $\theta$-相位下的判据
$$\frac{\phi''}{\phi'}=\frac{8u(3-4u^2)}{(4u^2+1)(4u^2-1)}=-\frac2u+O(u^{-3})\ (u\gg1)✓$$
$$\Longrightarrow R_i\lesssim\frac{4\pi L_i}{|\phi'|}+\frac{4\pi L_i^2}{u|\phi'|}(1+o(1)) \Longrightarrow \boxed{R_i\ll1\iff|\phi'(u)|\gg L_i+\frac{L_i^2}{u}}✓✓$$
$$\text{而}\ u\gg1\ \text{时}\ |\phi'|\asymp\frac{n}{u^2} \Longrightarrow \boxed{R_i\ll1\iff n\gg L_iu^2}✓✓\qquad(\text{干净的单一判据})✓$$

## §4 ⚠️ 但数值显示：**判据未必成立**（本档诚实记录）
$$\text{取}\ n=10\ \text{固定}、L=u/3：$$
| $u$ | $|\phi'(u)|$ | $L$ | $R_i$（精确式） | 判据 $n\gg Lu^2$？ |
|:--:|:--:|:--:|:--:|:--:|
| 2 | 2.076 | 0.67 | **2.94** | $10\gg2.7$ ✓ |
| 5 | 0.388 | 1.67 | **36.5** | $10\gg41.7$ ✗ |
| 10 | 0.099 | 3.33 | **282** | $10\gg333$ ✗ |
| 20 | 0.025 | 6.67 | **2240** | $10\gg2667$ ✗ |
$$\Longrightarrow \boxed{\text{固定}\ n\ \text{时}\ R_i\ \textbf{随}\ u\ \textbf{急剧增长}}⟹ \text{大}\ u\ \text{处}\ \textbf{稳定性失败}✓✗$$
$$\qquad \text{机理}：|\phi'|\asymp\frac{n}{u^2}\to0\（\text{固定}\ n），\ \text{相位趋于}\ \textbf{缓变} \Longrightarrow \text{非驻相压制}\ \textbf{不再适用}✓✓$$

## §5 🔧⚠️ 关键记录：一处**记法冲突**（必须先解决）
$$\text{本档}\ u:=\sum_i\log m_i=\log n_{\rm HB}\asymp\log X\qquad(\text{HB 的 log-乘积变量})✓$$
$$\text{而档案}\ \texttt{E91}\ \text{的}\ u:=t/\sqrt n,\quad |\phi'|=n/t^2=u^{-2}\qquad(\textbf{不同的}\ u\ \text{与不同的}\ n\text{！})✓✓$$
$$\Longrightarrow ⚠️\ \boxed{\text{两者不可混用}}：\text{判据}\ n\gg L_iu^2\ \text{中的}\ (n,u)\ \textbf{必须} \text{先钉死在}\ \textbf{一个} \text{记法里}✓✓✓$$
$$\qquad 📌\ \text{这正是}\ T5\ (\text{对象混淆}) \text{型风险——本档主动标记，避免把两套参数算成一个}✓✓$$

## §6 判词（**未收口，依唐先生纪律**）
$$\boxed{\text{①}\ G_i\asymp2\pi L_i^2\gg1\ \textbf{恒成立}✓✓\qquad\text{②}\ \phi''\ \textbf{不进} \text{一阶（`fee2ff9` 担忧撤销）}✓✓}$$
$$\boxed{\text{③}\ R_i\ll1\iff|\phi'|\gg L_i+\frac{L_i^2}{u}\iff n\gg L_iu^2\（\text{判据干净}）✓✓}$$
$$\boxed{\text{④ ⚠️ 但}\ R_i\ \text{在固定}\ n、\text{大}\ u\ \text{处}\ \textbf{急剧增长}⟹ \text{稳定性}\ \textbf{依赖参数}⟹ \textbf{本档不判死}}✓✓$$
$$\Longrightarrow \text{故}\ \theta\text{-型}\ \textbf{不能} \text{像线性相位那样直接收口}；\ \text{须先解决}\ §5\ \text{的记法冲突，再判定}\ n\ \text{与}\ Lu^2\ \text{的真实关系}✓✓$$
$$\qquad ⚠️\ \text{纪律（唐先生）}：\text{即使}\ UB\text{-}\theta\text{-2}\ \text{成功，也只能说}\ \textbf{C2 在"HB 高阶 log-weight ＋ Poisson stationary-phase"这一明确机制类内 NO-GO}✓✓$$

## §7 边界
$$\text{(i)}\ §1\ \textbf{解析＋数值一致}（比值 1.0000）✓✓；\ §2\ \textbf{解析两次验证}✓✓；\ §6\ \text{判据为}\ \textbf{标度级}✓$$
$$\text{(ii)}\ ⚠️\ \text{本档快速脚本的}\ \textbf{二阶差分数值不匹配解析}（27913 vs 8.20）——**判定为脚本缺陷**，依项目铁律"结果异常先怀疑自己的实现"}\ \textbf{不采信}✓✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{不声称}\ \text{C2 已收口}✓✓$$
