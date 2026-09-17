# ⚔️ W6-MAJORANT-1d · **归一化更正（T10 勘误）＋ $\alpha_n$ 的精确衰减律**

> 依唐先生 12:32 指令：先接受归一化更正，再把 $\alpha_n$ **代回四项求 Gram 最大特征值** ✓
> 本档完成**勘误＋$\alpha_n$ 精确律**；$\lambda_{\max}$ 下界**另档** ✓

---

## §0 【勘误 T10】（对 `W6-MAJORANT-1c §6`，**不覆盖上文**）

$$\text{1c 写"无带权版本双线性范数}\asymp3T/2"\ \textbf{错}✓✗$$
$$\textbf{正确}：S_B(t)=\frac{\sin Bt}{t}\ (B=\tfrac{3T}{2})\Longrightarrow\widehat{S_B}(\xi)=\pi\mathbf 1_{[-B,B]}(\xi) \Longrightarrow \boxed{\|S_B*\|_{L^2\to L^2}=\pi}\ （\textbf{不是}\ B）✓✓$$
$$\textbf{更关键（唐先生）}：\text{我们的对象}\ \textbf{不是连续卷积，而是}\ y_n=\log n\ \text{的}\ \textbf{离散网格}✓✓$$
$$\qquad \Delta y\asymp X^{-1}\ (n\asymp X) \Longrightarrow \sum_mS_B(y_n-y_m)f(y_m)\approx X\!\int\!S_B(y_n-y)f(y)\,dy \Longrightarrow \boxed{\|S_B(y_n-y_m)\|_{\ell^2\to\ell^2}\asymp X}✓✓$$
$$\qquad\Longrightarrow\ \textbf{MV 中的}\ \delta_n^{-1}\asymp n\ \text{正是}"\log n\ \text{网格在}\ n\sim X\ \text{的高采样密度}"，\ \textbf{不能靠带限自动消掉}✓✓$$
$$\textbf{反证（唐先生，照录）}：\text{取}\ f(y)=e^{i\xi_0y}\psi(y),\ |\xi_0|<B \Longrightarrow \langle Sf,f\rangle/\|f\|_2^2\asymp\pi X \Longrightarrow \|S_B\|\gtrsim X✓✓$$

### §0.1 命题 A／B 拆分（照录唐先生，本档采纳）
$$\textbf{命题 A}（\text{核是否具 Hilbert 奇核障碍？}）：\ \boxed{\textbf{否}}——K^{\rm sym}(t)=O(T) ⟹ \textbf{ALIVE 的真实进展}✓✓$$
$$\qquad(\text{小修正}：(\alpha_m+\bar\alpha_n)-(\alpha_n+\bar\alpha_m)=2i(\Im\alpha_m-\Im\alpha_n)\ \textbf{不一定为 0}；\ \text{但}\ \frac{\sin Bt}{t}\to B\ ⟹\ \text{有界性不受影响})✓$$
$$\textbf{命题 B}（\text{带限是否把离散范数从}\ X\ \text{降到}\ T？）：\ \boxed{\textbf{不能}}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{"bandlimit alone"}\ =\ \textbf{FALSE}}（\text{不是 W6 整体 FALSE，而是机制精准化}）✓✓$$

---

## §1 ⭐⭐⭐ 本档新增：$\alpha_n$ 的**精确衰减律**（唐先生 §9 唯一入口）

$$\alpha_n=\alpha_n^+=\int_0^T\Phi^2(x)e^{iy_nx}dx=\widehat{\Phi^2}(-y_n),\qquad y_n=\log n✓$$
$$\text{§5.2 逐字}：\mathbf 1_{[-L/2+w,\,L/2-w]}\le\phi^2\le\phi\le\mathbf 1_{[-L/2,\,L/2]} \Longrightarrow \Phi^2\approx c^2\mathbf 1_{[-L/2,\,L/2]}✓$$
$$\Longrightarrow\ \widehat{\Phi^2}(y)\approx c^2\!\int_{-L/2}^{L/2}\!e^{iyx}dx=\frac{2c^2\sin(Ly/2)}{y}\qquad[\textbf{结构}]✓$$
$$\Longrightarrow\ \boxed{|\alpha_n|\ \asymp\ \frac{c^2\,\big|\sin\big(\tfrac L2\log n\big)\big|}{\log n}}\qquad(n\ge2)✓✓✓$$

### §1.1 两点后果
$$\textbf{(i)}\ \text{一致界}\ |\alpha_n|\le\pi bL\le\pi L\ \textbf{比真值松}：\text{真的一致界是}\ |\alpha_n|\lesssim c^2\ (\textbf{不是}\ L)✓✓$$
$$\qquad(\text{因}\ 1/\log n\le1/\log2,\ |\sin|\le1) \Longrightarrow \textbf{diag 权范数}\ \|D_\alpha\|\lesssim c^2\ \textbf{而非}\ \pi L✓✓$$
$$\qquad\Longrightarrow\ \text{唐先生 §5 的}\ \|K\|\lesssim LX\ \textbf{中那个}\ L\ \textbf{可去掉} ⟹ \|K\|\lesssim X✓✓$$
$$\textbf{(ii)}\ \alpha_n\ \text{沿}\ y=\log n\ \textbf{以周期}\ 2\pi/L\ \textbf{振荡} ⟹ \textbf{测试向量的相干性被破坏}✓✓$$
$$\qquad\Longrightarrow\ \textbf{这正是唐先生 §9 猜的"特殊}\ \alpha_n\ \text{结构可能杀掉测试向量"}\ \textbf{方向成立}✓✓✓$$

---

## §2 判定与下一步
$$\text{本档}：\textbf{归一化错误已更正}；\text{命题 A＝ALIVE}／\text{命题 B＝不能}／\text{"bandlimit alone"＝FALSE}✓✓$$
$$\text{新增（实质）}：\alpha_n\ \text{有}\ \textbf{精确律}\ |\alpha_n|\asymp\frac{|\sin(L\log n/2)|}{\log n} ⟹ \textbf{去掉一个}\ L；\ \textbf{且自带相干性破坏}✓✓✓$$
$$\textbf{下一步（唐先生指定）}：\text{把}\ \alpha_n\ \text{代回四项，求真实 Gram 的}\ \lambda_{\max}✓$$
$$\qquad \lambda_{\max}\gtrsim X \Longrightarrow \textbf{FALSE}（\text{带限不能改变}\ X\ \text{级离散范数}）✓$$
$$\qquad \lambda_{\max}=o(X)\ \text{甚至}\ \lesssim T \Longrightarrow \textbf{ALIVE} \Longrightarrow \textbf{实质新现象}✓✓$$
$$\qquad ⚠️\ \textbf{本档未算}\ \lambda_{\max}✓$$

## §3 边界
$$\text{(i)}\ §0\ \text{照录唐先生 12:32；§0.1 小修正照录唐先生}✓\quad\text{(ii)}\ §1\ \text{的}\ \widehat{\Phi^2}\ \text{渐近标}\ [\textbf{结构}]（\text{未逐位核}\ c^2\ \text{与边缘修正}）✓$$
$$\text{(iii)}\ \textbf{未用 RH／HL／pair correlation}；\ \textbf{零数值}✓$$
