# ⚔️ **C2-W6-UB-4**：严格离散 Abel 界尝试 ⟹ **scaling 级压制成立；严格级未建立，缺口具名＝共振/对齐**

> 依唐先生 15:56「把 UB-3C 从 scaling-level 提升为严格离散 Abel 界」＋ 措辞收紧（差变量）✓
> **本档结果**：① 因子化**严格**；② 二阶导检验**严格但不够**（$t\gg L$ 时劣于平凡界）；③ ⚠️ **UB-3C 的压制仍是 scaling 级**；④ ⭐ **精确缺口＝相位对齐（Diophantine）＝共振**✓✓✓

---

## §0 采纳措辞收紧（唐先生）
$$\boxed{y_n=\log n,\qquad \Phi_{n,m}(T)=T\,(y_n-y_m)}✓✓\qquad(\text{W6 的实际对象是}\ \textbf{差变量}\ y_n-y_m=\log(n/m))✓$$
$$\text{HB 多变量后}\ U=\sum_i\log m_i；\ \textbf{真正的识别}\ y_n-y_m\ \longrightarrow\ U\ \text{发生在}\ \textbf{multilinear／Poisson 化步骤}✓✓$$
$$\qquad ⇒ \text{不影响结论}：\textbf{两者同属线性 log-phase geometry}✓✓$$

## §1 严格起点：因子化（**严格**）
$$S:=\sum_{k\in\mathcal K}\mathcal B(k)e^{i\Psi(k)},\quad \mathcal B(k)=\prod_i\frac{\mathfrak b_i(k_i)}{k_i^2},\quad \Psi(k)=-\lambda H_k+2\pi rC,\ \lambda=\frac{t^2}{2\pi}✓$$
$$\text{盒}\ k_i\in[Q_i/2,Q_i]\ \textbf{逐变量} \Longrightarrow \boxed{S=\prod_{i=1}^r\Sigma_i},\qquad \Sigma_i:=\sum_{Q_i/2<k\le Q_i}\frac{\mathfrak b_i(k)}{k^2}e^{-\lambda/k}✓✓$$
$$\Longrightarrow \text{严格任务}\ \textbf{归结为一维}：\text{给}\ \Sigma\ \text{一个}\ \textbf{低于绝对质量} \text{的显式界}✓✓$$

## §2 一维和的两种**严格**界
$$\textbf{绝对（平凡）}：|\Sigma|\le\sum_{Q/2<k\le Q}\frac{|\mathfrak b|}{k^2}\asymp\frac1Q=\frac{2\pi L}{t}\quad(\mathfrak b\ \text{有界时})✓✓$$
$$\textbf{二阶导检验（vdC，严格）}：|f''|=\frac{2\lambda}{k^3}\asymp\frac{2\lambda}{Q^3}=:\rho_2 \Longrightarrow \Big|\sum_{k\le N}e(f(k))\Big|\ll N\sqrt{\rho_2}+\rho_2^{-1/2}✓✓$$
$$\text{代入}\ N\asymp Q,\ \lambda/Q=tL：N\sqrt{\rho_2}\asymp\sqrt{2\lambda/Q}=\boxed{\sqrt{2tL}},\qquad \rho_2^{-1/2}\asymp\frac{Q^{3/2}}{\sqrt{2\lambda}}=\frac{\sqrt t}{2\pi L^{3/2}}✓✓$$
$$\Longrightarrow |\Sigma_{\rm vdC}|\ll\sqrt{tL}+\frac{\sqrt t}{L^{3/2}}✓$$

## §3 ⚠️ 比较：**vdC 不够用**
$$\text{vdC 优于平凡}\iff\sqrt{tL}\ll\frac Lt\iff t^{3/2}\ll L^{1/2} \iff t\ll L^{1/3}✗✗$$
$$\Longrightarrow \boxed{\text{在}\ t\gg L\ \text{（W6/HB 实际参数区）vdC}\ \textbf{劣于平凡界}}⟹ \textbf{不足以给出压制}✗✗✓$$

## §4 ⚠️ 因此：UB-3C 的压制**仍是 scaling 级**（与唐先生判断一致）
$$\text{UB-3C 用的"}\ll\frac1{Q^2L^2}"\ \text{来自}\ \textbf{一阶导检验}：\Big|\sum_{k\le x}e(f(k))\Big|\ll\frac1{\min|f'|}\asymp\frac1{L^2}✓$$
$$\qquad ⚠️\ \text{但该检验的}\ \textbf{假设}\（\text{排除相位}\ \textbf{对齐}）\ \text{本档}\ \textbf{未验证}✗ \Longrightarrow \text{不能作为严格界}✓✓$$
$$\Longrightarrow \boxed{\text{撤销}\ \text{UB-3C 的压制为"scaling 级"}}\ \text{（之前已标注，本档给出}\ \textbf{原因})✓✓$$

## §5 ⭐⭐⭐ 精确缺口：**相位对齐＝Diophantine 条件＝共振**
$$\text{一阶导检验失败的唯一情形}：\Big\|\frac{\lambda}{k^2}\Big\|\ \text{小}\（\text{即}\ e^{-\lambda/k}\ \text{在相邻}\ k\ \text{间几乎同相}）✓✓$$
$$\Longrightarrow \boxed{\text{严格压制}\iff\forall k\in[Q/2,Q]:\ \Big\|\frac{t^2}{2\pi k^2}\Big\|\gg\frac{1}{\#}\ \text{-型一致下界}}✓✓✓$$
$$\qquad 📌\ \text{这}\ \textbf{正是}\ \text{Diophantine（对齐）条件}，\ \textbf{与}\ t\ \text{的算术性质有关}；\ \text{即}\ \textbf{共振}✓✓✓$$
$$\Longrightarrow \text{与档案}\ \textbf{同址}：\text{Soundararajan}\ \textbf{共振法}（\text{造大值}）｜\texttt{E91}\ \text{的"素数侧}\ u\text{-频率}=k\log p\cdot t^2/n\ \text{不共振"}✓✓$$
$$\qquad ⇒ \boxed{\text{故 C2 线性支路的}\ \textbf{严格}\ \text{步＝统一排除相位对齐}\ \text{——}\ \textbf{具名缺口}}✓✓✓$$

## §6 判词
$$\boxed{\text{① 因子化：}\textbf{严格}✓✓\qquad\text{② 绝对界：}\textbf{严格}✓✓\qquad\text{③ 二阶导检验：}\textbf{严格但不够}（t\gg L）✓✓}$$
$$\boxed{\text{④ UB-3C 压制＝}\textbf{scaling 级}（\text{撤销"严格"}）⟹ \textbf{本档}\ \textbf{不判 DEAD}}✓✓$$
$$\boxed{\text{⑤ 缺口}\ \textbf{具名}：\text{相位对齐（Diophantine）条件的一致排除}\ =\ \text{共振问题}}✓✓✓$$
$$\Longrightarrow \text{C2 双轨账本（更新）}：$$
| 支路 | 实际相位 | 状态 |
|:--|:--|:--|
| **W6/HB 线性** | $TU$ | **scaling 级压制成立**；严格级缺口＝共振/对齐（**本档钉死**）|
| E91 | $n_\theta\theta(t)$ | 独立坐标系；$|\phi'|\in[1,11]$ 有界；已被 E91/E79′ 判为循环 |

## §7 边界
$$\text{(i)}\ §1\ \textbf{严格}（\text{盒逐变量}）✓✓；\ §2\ \textbf{严格}（\text{vdC 为经典定理}）✓✓；\ §3\ \textbf{严格}（\text{初等比较}）✓✓$$
$$\text{(ii)}\ §4--§5\ \text{为}\ [\textbf{结构}] \text{级判断；}\ \text{一阶导检验的合法形式}\ \textbf{未逐字核文献}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零数值}；\ \text{本档}\ \textbf{不声称}\ \text{C2 已 DEAD}✓✓$$
