# V316-C 第一层（差值恒等式）前置缺口分析 —— ⚠️ **不是重设泛函，而是三件尚不存在的东西**

## 一、当前实际 statement（原样取出，**不猜**）

$$\texttt{Q\_pos\_alg}：\forall\{N\ B\ \lambda\},\ 0<\lambda\to\lambda\le1\to0\le N\to|B|\le\tfrac12N\ \Longrightarrow\ \tfrac12N\le N+\lambda^{2}B$$
$$\texttt{Q\_pos}：\text{取}\ N：＝\int_{-\frac12}^{\frac12}v^{2},\quad B：＝\int p,\ |p.1-p.2|\,v\,p.1\,v\,p.2\ \partial(\texttt{Irest.prod Irest})$$
$$\qquad \text{且}\ \textbf{把}\ |B|\le\tfrac12N\ \textbf{当作假设}（\textbf{未}在 Q\_pos 内由 kernel\_bound 导出）$$
$$\texttt{vStar\_EL}：\textbf{逐点 in}\ s：\ \cos(\sqrt2\lambda s)+\lambda^{2}\int_t|s-t|\cos(\sqrt2\lambda t)dt=D_\lambda$$
$$\texttt{KvStar\_affine}：\int_t|s-t|\cos(\sqrt2\lambda t)dt=C_\lambda-\lambda^{-2}\cos(\sqrt2\lambda s)$$

## 二、⚠️ 缺口：文件里**没有** `Q_λ(u)` 泛函、**没有** `B(u,v)` 双线性形式

$$\text{现有对象全是}\ \textbf{二次型的具体积分式}（\text{核}\ |s-t|\ \text{对称}），\text{而不是}\ \text{functional}\ Q_\lambda(u)\ \text{＋双线性}\ B(u,v)$$
$$\Longrightarrow \text{差值恒等式}\ Q_\lambda(u)-Q_\lambda(v)=2D_\lambda\Big(\int u-\int v\Big)+Q_\lambda(u-v)\ \textbf{需要三件新东西}：$$

$$\textbf{(1) 定义}\ \texttt{Qfun}\ \lambda\ u：＝\int_s u^2+\lambda^{2}\iint|s-t|u(s)u(t)\quad（\text{平凡，纯 def}）✓$$
$$\textbf{(2) 极化／展开恒等式}：\iint K(u,u)=\iint K(v,v)+2\iint K(v,u-v)+\iint K(u-v,u-v)$$
$$\qquad \text{证法：点态代数}\ +\ \text{积分线性；需可积性假设。}\ \textbf{中等工作量} ✓$$
$$\textbf{(3) ⭐ 弱（积分）形式的 E–L}：\int_s v_\lambda(s)h(s)\cdot\text{?}\ \text{——即把逐点}\ \texttt{vStar\_EL}\ \text{乘}\ h(s)\ \text{后积分}：$$
$$\qquad \int_s\Big[\cos(\sqrt2\lambda s)+\lambda^{2}\int_t|s-t|\cos(\sqrt2\lambda t)dt\Big]h(s)ds=D_\lambda\int_s h(s)ds$$
$$\qquad \text{并须把}\ \lambda^{2}\int_s\big(\int_t|s-t|v_\lambda(t)dt\big)h(s)ds\ \text{换成}\ \lambda^{2}\iint|s-t|v_\lambda(s)h(t)$$
$$\qquad ⟹ \textbf{需 Tonelli ＋ 对称换序（同 kernel\_sq\_swap 的手法）} ⟹ \textbf{本层真正的硬点} ⚠️$$

## 三、另一处**接线缺口**（易修，但须先做）

$$\texttt{kernel\_bound}\ \text{是}\ \textbf{带 7 条可积性假设的独立定理};\quad \texttt{Q\_pos}\ \text{把}\ |B|\le\tfrac12N\ \text{当}\ \textbf{假设}$$
$$\Longrightarrow \text{链}\ \texttt{kernel\_bound}\to\texttt{Q\_pos}\ \textbf{尚未在文件内接上}$$
$$\qquad \text{接线法（平凡）：}\texttt{have hb := kernel\_bound hmain habs h2 hA hB hF hG};\ \text{再}\ \texttt{exact Q\_pos h0 h1 hN hb} ✓$$
$$\qquad \text{建议先做这一步 —— 它把 V316-A 的自洽闭合补齐（不需新数学）}$$

## 四、建议的第一层最小命题（**待唐先生确认后再落 Lean**）

$$\texttt{Qfun\_diff}：\text{在}\ \text{可积性}\ +\ \int u=\int v_\lambda\ \text{＋ 弱 E–L 的前提下：}$$
$$\qquad Q_\lambda(u)-Q_\lambda(v_\lambda)=Q_\lambda(u-v_\lambda)$$
$$\qquad \Longrightarrow\ \text{第二层：}\ \ge\tfrac12\lVert u-v_\lambda\rVert_2^{2}\ \（\text{直接调已 CLOSED 的}\ \texttt{Q\_pos}）$$
$$\qquad \Longrightarrow\ \text{第三层：}\ Q_\lambda(u)\le Q_\lambda(v_\lambda)\Rightarrow u=v_\lambda\ \text{a.e.}$$

## 五、纪律建议（避免又一次 A4 式错位）
$$\text{① 先做}\ \textbf{接线}（kernel\_bound → Q\_pos），不引入新数学；$$
$$\text{② 三层新东西按 (1)(2)(3) 逐步落，}\textbf{每件单独 EXIT=0}；$$
$$\text{③ (3) 若卡住，}\textbf{停在 Tonelli／换序 API}，不要回头改已 CLOSED 的}\ \texttt{KvStar\_affine／vStar\_EL}$$
$$\text{④ 全流程不重设泛函（沿用现有积分式），不引入 Hilbert 空间抽象}$$
