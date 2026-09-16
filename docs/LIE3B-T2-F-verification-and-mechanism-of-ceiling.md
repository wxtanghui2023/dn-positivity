# 猎-3B（T2）— $\mathfrak F$ 核验：**通过**，并得到**机制级**收获

> 唐先生 2026-09-16 19:57 拍板 **T2 → T3**（**不开 T1**）。
> 取证：BCR 原文 PDF（`math.mcgill.ca/radziwill/BCR.pdf`，**外部来源，仅作数据**）—— 本档逐条核验三件事。

---

## ① 可达域定义：**是** $\{r,t\ge0\}$，**且存在两处隐藏耦合**（唐先生要找的）
$$\textbf{原文（1.3）}：\ S_{A,M,N}:=\sum_a\sum_{(m,n)=1}\nu_a\alpha_m\beta_n e\!\left(\tfrac{am}{n}\right)\ \ll_\varepsilon\ \|\alpha\|\|\beta\|\|\nu\|(M+N)^{\frac12+r+\varepsilon}A^{t}+\dots$$
$$\qquad\text{其中}\ M\le m<2M,\ N\le n<2N,\ A\le a<2A,\quad \boxed{A\ \ll\ (NM)^{\frac{0.5-r}{1+2t}+\varepsilon}}\ ✓$$
$$\textbf{原文（猜想域）}：\ \text{"We conjecture that (1.3) holds true for}\ \textbf{all}\ r,t\ge0\text{"}\ ✓$$
$$\Longrightarrow\ \textbf{隐藏耦合 1（本档核出，唐先生未列）}：\ (r,t)\ \textbf{不是两个自由参数} \text{——它们}\ \textbf{同时决定}\ A\ \text{的允许范围}$$
$$\qquad\text{且}\ r,t\ \text{减小}\ \Longrightarrow\ \text{指数}\ \tfrac{0.5-r}{1+2t}\ \text{增大}\ \Longrightarrow\ A\ \text{范围}\ \textbf{扩大}✓\quad(\text{攻击相干性})$$
$$\textbf{隐藏耦合 2（本档核出）}：\ \text{定理 2 的误差项含}\ (r,t)：\ O\bigl(\underbrace{T^{\frac12-t+\varepsilon}N^{\frac12+r+2t}}_{\text{主误差}}+\underbrace{T^{\frac13+\varepsilon}}_{\text{次}}\bigr)$$
$$\qquad\Longrightarrow\ \text{渐近式成立}\ \textbf{要求主误差}\ \textbf{次于主项}\ \Longrightarrow\ \text{见 §4（这正是}\ \theta\ \text{-上界公式本身）}✓$$

## ② 端点 $(r,t)\to(0,0)$：**合法**（在猜想集内），且给出 $\theta<1$ **严格**
$$\text{猜想域为}\ r,t\ge0 \Longrightarrow (0,0)\ \textbf{属于}\ \text{同一模板的合法点，}\ \textbf{无需} \text{"形式外推"}✓$$
$$\textbf{定理 2 结论（原文）}：\ \theta<\tfrac12+\frac{0.5-r}{1+2(r+2t)}\ \ (\text{此处}\ N:=T^{\theta})$$
$$\qquad (r,t)=(0,0)\Longrightarrow \text{上界为}\ \theta<1\ \textbf{（严格）}✓ \Longrightarrow \text{原文"asymptotic formula for}\ I\ \text{valid for}\ \textbf{any}\ \theta<1\text{"}\ \textbf{完全一致}✓$$
$$\qquad\Longrightarrow\ \text{唐先生所忧的"}\theta\to1\ \text{可能只是形式外推"}\ \textbf{不成立}✓$$

## ③ Conjecture 1 ⟹ $\theta<1$：**逐字确认**
$$\text{"Using the estimate (1.4) and Theorem 2, we obtain an asymptotic formula for}\ I\ \text{valid for}\ \textbf{any}\ \theta<1\text{, and this implies the Lindelöf hypothesis."}\ ✓$$
$$\text{"Corollary 1. Suppose that Conjecture 1 holds. Then the Lindelöf Hypothesis is true."}\ ✓$$
$$\text{"Conjecture 1 appears to be}\ \textbf{strictly stronger than}\ \text{the Lindelöf Hypothesis."}\ ✓$$
$$\text{且历史点亦逐字确认}：\text{DFI}\to r=\tfrac{23}{48},\ t=\tfrac12；\ \text{Bettin--Chandee}\to r=\tfrac9{20},\ t=\tfrac7{20}\ ✓✓$$

## ④ ⭐⭐ 机制级收获：**$\theta$-上界公式就是"误差项次于主项"条件**
$$\text{误差项条件}：\ T^{\frac12-t+\varepsilon}N^{\frac12+r+2t}\ll T^{1}\ (\text{主项量级})，\ N=T^{\theta}$$
$$\qquad\Longrightarrow\ \tfrac12-t+\theta\bigl(\tfrac12+r+2t\bigr)<1\Longrightarrow \theta<\frac{\frac12+t}{\frac12+r+2t}=\frac{1+2t}{1+2r+4t}$$
$$\textbf{与定理 2 公式对照（本档计算）}：\quad \tfrac12+\frac{0.5-r}{1+2(r+2t)}=\frac{\tfrac{1+2r+4t}{2}+0.5-r}{1+2r+4t}=\frac{1+2t}{1+2r+4t}\ ✓✓\ \textbf{恒等}$$
$$\Longrightarrow\ \boxed{\text{定理 2 的}\ \theta\ \text{-上界}\ =\ \textbf{误差项次于主项条件}}\quad(\textbf{机制级识别})✓$$
$$\textbf{由此}：\ \theta>\tfrac{17}{33}\iff 17r+t<8\iff \text{主误差项次于主项}\ \Longrightarrow \textbf{17/33 不是架构天花板}\ \text{现在有}\ \textbf{机制级证明}，\ \textbf{而非} \text{仅依赖猜想自述}✓✓$$
$$\qquad\text{（且}\ T^{\frac13+\varepsilon}\ \text{次项}\ \textbf{不构成阻碍}：\ \tfrac13<1✓）$$

## ⑤ ⚠️ 立即降级（唐先生指定，本档执行）
$$\text{猎-3A 的}\ \text{"}t\ \text{方向比}\ r\ \text{方向高效 17 倍"}\ \Longrightarrow\ \boxed{\text{应改为：}\textbf{坐标灵敏度}}$$
$$\qquad\boxed{\text{在固定}\ \theta(r,t)\ \text{公式下，单位参数变化对越过}\ 17/33\ \text{边界的权重为}\ 17:1}✓$$
$$\qquad\textbf{不得} \text{解释为"研究难度上}\ t\ \text{比}\ r\ \text{容易/有效 17 倍"}\quad(\textbf{"坐标灵敏度"}\ne\textbf{"数学可推进性"})✓$$
$$\textbf{且证据支持此降级（本档据原文）}：\ \text{(1.3) 中}\ \textbf{t 是}\ A\ \text{的指数}，\ \textbf{r 是}\ (M+N)\ \text{的指数} \Longrightarrow \text{两侧算术难度是}\ \textbf{不同问题}✓$$

## T2 判定
$$\boxed{\text{T2}\ \textbf{通过}（三项全部确认）} \Longrightarrow \textbf{N3-C 升级为干净结构结论}：$$
$$\qquad\boxed{17/33\ \textbf{不是 BCR 架构天花板}，\ \text{只是当前已知}\ (r,t)\ \text{输入产生的}\ \textbf{历史最佳点}}✓$$
$$\qquad\text{且}\ \text{"真正攻击对象＝BCR 可达域"}\ \text{获}\ \textbf{机制级支撑} \text{（§4）}✓$$

## 残余（不得省略）
$$\text{残余 1：§4 的"\theta-上界＝误差项条件"为本档计算，}\textbf{未} \text{逐行核验定理 2 的完整证明（含}\ T^{1/3}\ \text{项的来源）}；$$
$$\text{残余 2：隐藏耦合 1 的}\ A\ \text{-范围公式为原文引用，}\ \textbf{未验} \text{其推导；}$$
$$\text{残余 3：}\ \mathfrak F\ \text{的}\ \textbf{完整形态}（\text{含}\ A\ \text{-范围耦合与误差条件的交集）}\ \textbf{未} \text{完整写出}✓$$

## 边界（N1/N2 严守）
$$\text{① 取证为 BCR 原文 PDF（外部来源，仅作数据），关键语句}\ \textbf{逐字引用}✓；$$
$$\text{② 已执行降级（坐标灵敏度}\ne\text{可推进性}）；\quad\text{③ }\textbf{未用 RH}；零数值（\text{仅代数恒等式）}；\ \text{未跑 Lean}✓$$
