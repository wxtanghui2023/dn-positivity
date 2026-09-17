# ⚔️ **UB-$\theta$-1**：$\mathcal D=0$ 可行域审计 ⟹ **Airy 支线 DEAD（几何＋整数性双重钉死）**

> 依唐先生 15:43「先判 Airy 是否连几何上存在」✓
> **本档结果**：退化必要条件＝$u\in(\tfrac12,\tfrac{\sqrt3}2)$；**C–S 上界再收窄到** $u\in(0.5,\ \mathbf{0.700484})$；而 $\log n$ 的**整数性**使窗口内只剩 $n=2$ ⟹ 只能 $r=1$ ⟹ **无非对角模式** ⟹ **DEAD**✓✓✓

---

## §0 `7fb77dc` 的分层（采纳）
$$\boxed{\text{线性}\ \phi=tu：\text{C2-UB}\ \textbf{视为关闭}（\text{当前模型假设下}）}✓\qquad\boxed{\text{additive}\times\text{multiplicative 接口}\ \textbf{存在但产生压制}}✓✓$$
$$\qquad ⚠️\ \text{C4 的 Abel 界仍}\ \textbf{标度级} \Longrightarrow \textbf{不升级} \text{为整个离散 Poisson 问题的严格定理；}\mathfrak b_i／\text{端点／remainder 保留在边界}✓✓$$

## §1 $\theta$-相位两导数（唐先生给式；**本档数值复核通过**）
$$\phi(u)=-\frac{4nu}{4u^2+1} \Longrightarrow \phi'(u)=\frac{4n(4u^2-1)}{(4u^2+1)^2},\qquad \phi''(u)=\frac{32nu(3-4u^2)}{(4u^2+1)^3}✓✓\quad(\text{数值验证}\ \checkmark)✓$$
$$C=-\frac{\phi'(u)}{2\pi}=-\frac{2n(4u^2-1)}{\pi(4u^2+1)^2}✓\qquad \text{自洽}：u+\frac{\phi'(u)}{2\pi}H_k=0✓$$

## §2 $\mathcal D$ 的化简链（逐字采纳）
$$\mathcal D(u,k)=1+\frac{C\phi''(u)}{2\pi}\sum_ik_i^{-2}；\ \text{用}\ k_i=\frac C{x_i}：\sum k_i^{-2}=\frac1{C^2}\sum x_i^2✓$$
$$2\pi C=-\phi'(u) \Longrightarrow \boxed{\mathcal D=1-\frac{\phi''(u)}{\phi'(u)}S_2},\qquad S_2:=\sum_i x_i^2✓✓$$
$$\Longrightarrow \boxed{\text{Airy}\iff S_2=\frac{\phi'(u)}{\phi''(u)}}✓✓\qquad(\text{且首须}\ \phi''/\phi'>0)✓$$

## §3 退化必要条件
$$\theta\text{-相位}：\frac{\phi''(u)}{\phi'(u)}=\frac{8u(3-4u^2)}{(4u^2+1)(4u^2-1)}✓\qquad \frac{\phi''}{\phi'}>0\iff(4u^2-1)(3-4u^2)>0✓$$
$$\Longrightarrow \boxed{u\in\Big(\tfrac12,\ \tfrac{\sqrt3}2\Big)}✓✓\qquad(\text{唐先生结果，本档确认})✓$$

## §4 ⭐⭐ C–S 约束把窗口再收窄一半
$$x_i>0,\ u=\sum_ix_i \Longrightarrow \boxed{\frac{u^2}{r}\le S_2\le u^2}✓✓\qquad(\text{上界}\ \textbf{硬}；\ \text{下界对}\ r\ \text{大时松})✓$$
$$\text{上界}\ T(u)\le u^2，\ T(u):=\frac{(4u^2+1)(4u^2-1)}{8u(3-4u^2)}；\ \text{令}\ w=4u^2：\boxed{w^2-1\le w^{3/2}(3-w)}✓$$
$$\text{数值求交}：\boxed{w^*=1.962710,\quad u^*=0.700484}✓✓$$
$$\Longrightarrow \boxed{\textbf{Airy 窗口}：u\in(0.5,\ 0.700484)}✓✓✓\qquad(T\le u^2\ \text{在}\ 0.75,0.8\ \text{处已失败})✓$$

## §5 ⭐⭐⭐ 整数性致死（本档的决定性一步）
$$u=\sum_i\log m_i=\log n,\qquad n\in\mathbb Z_{\ge2}\ (\Lambda\ \text{的宗量})✓$$
$$\Longrightarrow \log n\ \text{取值}\ \{0.693,\ 1.099,\ 1.386,\dots\} \Longrightarrow \boxed{\text{窗口内}\ \textbf{唯一}\ n=2\ (\log2=0.693147)}✓✓✓\quad(\text{数值确认})✓$$
$$\text{而}\ m_1\cdots m_r=2：\text{或}\ r=1\（\text{无对角／非对角之分}）\ \text{或某}\ m_i=1 \Longrightarrow x_i=0 \Longrightarrow \textbf{非内部驻点}✓✓$$
$$\Longrightarrow \boxed{r\ge2\ \text{的非对角驻点}\ \textbf{不存在}} \Longrightarrow \boxed{\textbf{Airy 支线 DEAD（几何＋整数性双重）}}✓✓✓$$
$$\qquad 📌\ \text{等价说法}：\text{应用范围内}\ u=\log n\asymp\log X\gg1 \Longrightarrow \textbf{远离窗口} \Longrightarrow \mathcal D\ \textbf{恒不为零}✓✓$$

## §6 判词 ＋ 迁移状态
$$\boxed{\text{① Airy 支线}\ \textbf{DEAD}：$\theta$-型}\ \textbf{无} \text{退化 stationary phase}⟹ \text{三阶项无需算}}✓✓✓$$
$$\boxed{\text{② 故}\ \theta\text{-型}\ \textbf{只剩非退化 stationary phase}；\ \mathcal D\approx1\ \text{级别扰动}⟹ \text{线性相位的压制机制}\ \textbf{大概率迁移}}✓✓$$
$$\qquad ⚠️\ \textbf{待核（下一步）}：\text{非退化情形下的}\ \textbf{扰动稳定性} \text{——局部量}\ 2\pi L^2\gg1\ \text{在}\ \phi''\ne0\ \text{时是否仍}\ \gg1✓✓$$
$$\boxed{\text{③ C 档当前状态}：\text{C2}\ \textbf{在线性相位下关闭}；\ \theta\text{-型的}\ \textbf{唯一潜在复活口（Airy）}\ \textbf{已排除}}✓✓✓$$

## §7 边界
$$\text{(i)}\ §1\ \text{两导数}\ \textbf{数值复核通过}（\text{中心差分}\ \checkmark)✓；\ §2--§4\ \textbf{严格}（\text{初等代数＋C--S}）✓✓；\ §5\ \textbf{严格}（\text{整数性}）✓✓$$
$$\text{(ii)}\ §4\ \text{的}\ u^*\ \text{为数值求根}（\text{至}\ 10^{-6}）✓；\ \text{窗口端点}\ u=0.5\ \text{为开（}\phi''/\phi'\ \text{发散）}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零 numerics 之外无数值}；\ \text{本档}\ \textbf{不声称} \text{C2 已全线完成——}\ \textbf{非退化扰动稳定性待核}✓✓$$
