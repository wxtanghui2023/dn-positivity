# V2-18-A — **$b$ 的自由度审计** ⟹ 判定 **A（$b$ 非自由变量）**

> 唐先生 2026-09-16 21:17 拍板 **V2-18**，并指定第一刀＝**V2-18-A**（**不**假设 $b=T^\beta$，先判 $b$ 是什么）✓
> **措辞纪律（唐先生）**：$b$ **可以**作为"待审计自由度"，但**不可以**登记为"未被利用的优化自由度" —— "出现在公式里" $\ne$"可以自由优化而不破坏构造"✓
> 判定树：$\mathrm{A}$ 非自由变量 $\Rightarrow$ **DEAD** $\big|\$ $\mathrm{B}$ 可调但二维优化仍给原 envelope $\big|\$ $\mathrm{C}$ 可调且严格改善 $\big|\$ $\mathrm{D}$ 改变 $b$ 会改变 (3.1)/(4.4) 的证明结构✓

---

## 1. ⭐⭐ 决定性逐字取证（BC 原文，**外部来源，仅作数据**）
$$\textbf{(a) §2（}b\ \text{的}\ \textbf{原始用途}）}：\ \text{"We will first give a bound for}\ C_b\ \text{in this case and}\ \boxed{\textbf{in Section 6 we will use the freedom given by the parameter}\ b}\ \text{to obtain a bound for}\ C_1\ \textbf{valid in the general case}\text{"}✓✓✓$$
$$\textbf{(b) §6 开头（}b\ \text{的}\ \textbf{真实身份}）}：\ \text{"We write}\ \boxed{\eta=b\eta_0}\text{, where}\ \eta_0\ \text{is square-free,}\ \boxed{b\ \textbf{is square-full}}\text{, and}\ (b,\eta_0)=1\text{"}$$
$$\qquad\Longrightarrow\ \boxed{b\ ＝\ \eta\ \text{的}\ \textbf{平方全（square-full）核}}✓✓\quad\Longrightarrow\ \text{随后}\ C_1=\sum_{b\le N}\sum_{\eta_0}\dots\Longrightarrow \boxed{b\ \textbf{是被求和的}}✓✓✓$$
$$\textbf{(c) §2（}b\ \text{进入的唯一通道）}：\ \text{"provided that}\ \boxed{L>2\log(b\eta M)}\text{"} \Longrightarrow b\ \textbf{仅经放大器的条件} \text{进入}✓$$

## 2. 三关逐一回答（唐先生指定）
$$\textbf{关 ①}\ b\ \text{的范围是什么？} \Longrightarrow \ \boxed{b\ \text{square-full},\ b\le N,\ (b,\eta)=1}✓\quad(\textbf{非}"b>0"\ \text{式自由}，\ \text{而是}\ \textbf{结构化的离散集})✓$$
$$\qquad\text{且在 §2--§5 的 square-free 情形，}b\ \text{另作}\ \textbf{模数} \text{（}C_b\ \text{的 character 和}）\ \text{并受}\ L>2\log(b\eta M)\ \text{约束}✓$$
$$\textbf{关 ②}\ b\ \text{是否已被前面的变换固定？} \Longrightarrow \ \boxed{\textbf{是}}✓✓\quad(\text{§2 明言其"freedom"}\textbf{被用于}\S6\ \text{的一般情形} \Longrightarrow \text{其自由度被}\textbf{消费} \text{，}\textbf{不是} \text{留给指数优化})✓$$
$$\textbf{关 ③ ⭐ 改变}\ b\ \text{是否改变 (3.1)/(4.4) 本身？} \Longrightarrow \ \boxed{\textbf{是}}✓✓$$
$$\qquad\text{因}\ b\ \text{出现在}\ C_b\ \text{的}\ \textbf{构造前设} \text{（character 模、}\ (m,b)=1\ \text{条件、}\ (mb\eta,\ell_1\ell_2n_1n_2)\ \text{型互素条件}） \Longrightarrow \text{换}\ b\ \textbf{即换对象}✓$$
$$\qquad\textbf{且更根本}：\ \text{在最终定理中}\ b\ \textbf{被求和} \text{（§6）} \Longrightarrow \boxed{b\ \textbf{根本不是} \text{可优化变量}}✓✓✓$$

## 3. 判定：**A**
$$\boxed{\textbf{A}：\ b\ \textbf{非自由变量}}\ ✓✓\quad(\text{按唐先生判定树}\Longrightarrow \textbf{该线干净关闭})✓$$
$$\textbf{机制（两步，皆为确证）}：$$
$$\qquad\text{(i) §2 的"freedom given by}\ b\text{"}\ \textbf{已被明确指定} \text{用于"}\textbf{removing the square-free condition}\text{"（§6），}\ \textbf{而非} \text{指数优化}✓✓$$
$$\qquad\text{(ii) §6 中}\ b\ ＝\ \eta\ \text{的 square-full 核，}\ \textbf{被求和} \text{（}b\le N\text{）} \Longrightarrow \text{无连续／独立的指数自由度}✓✓$$

## 4. 与唐先生预判的对照（诚实记录）
$$\text{唐先生预判}：\ \text{"}b\ \text{已经被 BC 的六项竞争自动钉死"（}\mathrm{B}\ \text{型结论}）✓$$
$$\text{实际取证}：\ \text{理由}\ \textbf{更根本} \text{——}\ b\ \textbf{不是被六项钉死}，\ \text{而是}\ \textbf{其自由度本就被 §6 的求和与放大器的约束占用} \Longrightarrow \textbf{A 型}✓✓$$
$$\Longrightarrow\ \text{故 V2-18-B 的二维 envelope（}\inf_{\beta,\ell}\max_j E_j\text{）}\ \textbf{不成立} \text{（缺前提）}✓\quad(\text{唐先生："若 NO，就把这条线干净关闭"})✓$$

## 5. 残余（不得省略）
$$\text{残余 1：§6 的}\ b\ \text{-求和}\ \textbf{完整形式} \text{（含}\ b\ \text{的 dyadic 分块与各项}\ b\ \text{-幂次如何求和）}\ \textbf{未逐行取全}✓$$
$$\text{残余 2：}\ b\ \text{在 §2--§5（square-free 情形）作为模数时，}\textbf{是否} \text{存在"}\ C_b\ \text{内部"的}\ b\ \text{-自由} \text{——}\ \text{但最终定理需}\ C_1，\ \text{故其自由度}\ \textbf{被消费}✓$$
$$\text{残余 3：残余 A--D 不变}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① 只判"}\ b\ \text{是否具有可独立选择的指数自由度"；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 7. 净产出
$$\text{(i) ⭐⭐ 逐字：}\ b\ ＝\ \eta\ \text{的}\ \textbf{square-full 核} \text{（§6），}\ \textbf{被求和} \text{（}b\le N\text{）}✓✓$$
$$\text{(ii) ⭐⭐ 逐字：§2 的"freedom given by}\ b\text{"}\ \textbf{被指定} \text{用于}\ \textbf{removing the square-free condition}，\ \textbf{非} \text{指数优化}✓✓$$
$$\text{(iii) 三关：范围结构化；已被前设占用；改变}\ b\ \text{即改变对象（且}\ b\ \text{被求和）}✓✓$$
$$\text{(iv) 判定}\ \boxed{\textbf{A}}：\ b\ \textbf{非自由变量} \Longrightarrow \textbf{该线干净关闭}；\ \text{V2-18-B 的二维 envelope 不成立（缺前提）}✓✓$$
$$\text{(v) 措辞纪律遵守：}\ b\ \text{仅登记为"待审计自由度"，}\textbf{未} \text{登记为"未被利用的优化自由度"}✓$$
