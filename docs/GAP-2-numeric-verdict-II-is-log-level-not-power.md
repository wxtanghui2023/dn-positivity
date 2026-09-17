# 🎯 **GAP-② 数值判定**：$|\delta_T|\asymp(\log T)^{1.0}$ —— **(II) 不是幂次级；分辨率地板 ≈0.15**

> 依唐先生 13:18「继续」执行 ②（判定 (II) 的幂次性）✓
> **对象（纯算术，无需 ζ）**：$S_T(s)=\sum_{n\le T}\Lambda(n)n^{-s}$，$s=\tfrac12+it$
> **主项（Abel 恒等式，逐字）**：$S_T(s)=\dfrac{T^{1-s}-s}{1-s}+s\!\int_1^T\!E(u)u^{-s-1}du+E(T)T^{-s}$，$E(u)=\psi(u)-u$
> $$\Longrightarrow\ \delta_T:=\text{deviation}=-\sum_\rho\frac{T^{\rho-s}}{\rho(\rho-s)}+\ldots\asymp T^{\beta_{\max}-\frac12}\quad(\text{(II)}\ \text{的形式})✓$$

---

## §1 【勘误 T10】第一版主项写错（当场自查）
$$\text{首跑用}\ \text{main}=\frac{s}{1-s}(T^{1-s}-1) \Longrightarrow \text{实测}\ |\delta_T|\asymp T^{1/2}\ (\alpha\approx0.50)✓✗$$
$$\text{原因}：\textbf{漏了 Abel 恒等式里的}\ \psi(T)T^{-s}\ \text{项（差}\ -T^{1-s}\asymp T^{1/2}）✓✗$$
$$\text{改正}\ \text{main}=\frac{T^{1-s}-s}{1-s} \Longrightarrow \text{重跑（下表）}✓✓$$

## §2 ⭐⭐⭐ 实测结果（$T=10^5,10^6,10^7$；$t$ 取 5 个零点高度；$\Lambda$ 由筛法到 $10^7$，665{,}134 个素幂项）

| $t$ | $\vert\delta_{10^5}\vert$ | $\vert\delta_{10^6}\vert$ | $\vert\delta_{10^7}\vert$ | 总幂次 $\alpha$ | $(\log T)^c$ 拟合 $c$ |
|:--|:--|:--|:--|:--|:--|
| 14.1347 | 11.9189 | 14.7884 | 16.5065 | 0.1414 | **0.9743** |
| 21.0220 | 12.1117 | 14.2480 | 16.9898 | 0.1470 | **1.0024** |
| 25.0109 | 11.9712 | 14.0651 | 16.7551 | 0.1460 | **0.9957** |
| 30.4249 | 11.6277 | 13.8504 | 16.7151 | 0.1576 | **1.0750** |
| 40.9187 | 12.1807 | 14.7330 | 16.6378 | 0.1354 | **0.9303** |

$$\Longrightarrow\ \boxed{|\delta_T|\ \asymp\ (\log T)^{1.00}\ (\textbf{log 级})},\qquad \text{而非}\ T^{\beta-\frac12}✓✓✓$$
$$\text{与 RH 一致}：\text{RH}\Rightarrow|\psi(T)-T|\ll T^{\frac12}\log^2T \Longrightarrow |\delta_T|\ll\log^2T✓✓$$

## §3 ⭐⭐ 人工 β 对照（定分辨率）
$$v_2(T):=\delta_{\rm real}(T)+A\,T^{\beta-\frac12}\quad(\text{背景取实测}\ t=14.13\ \text{曲线})✓$$

| $\beta$ | 真值 $\beta-\tfrac12$ | 拟合 $\alpha$（$A=1$） | 拟合 $\alpha$（$A=5$） | 可识别？ |
|:--|:--|:--|:--|:--|
| 0.55 | 0.05 | 0.1363 | 0.1242 | ✗（淹没） |
| 0.60 | 0.10 | 0.1544 | 0.1758 | ✗（临界） |
| 0.65 | 0.15 | 0.1988 | 0.2585 | ✓ |
| 0.70 | 0.20 | 0.2785 | 0.3608 | ✓ |
| 0.80 | 0.30 | 0.5146 | 0.5797 | ✓ |

$$\text{背景本身贡献}\ \alpha_{\rm bg}\approx0.146\ \text{（正是}\ \log T\ \text{在}\ 10^5\to10^7\ \text{上的增长率}）✓✓$$
$$\Longrightarrow\ \boxed{\textbf{分辨率地板}：\ \beta-\tfrac12\ \gtrsim\ 0.15\quad(T\le10^7)}✓✓✓$$

## §4 ⭐⭐⭐ 结论（对缺口 $\mathfrak G$ 的直接裁决）
$$\text{(a)}\ \textbf{(II) 不是幂次级}：\text{实测是}\ \log\ \text{级；}\ \text{幂次读数被}\ \log\ \text{背景污染}✓✓$$
$$\text{(b)}\ ⭐\ \textbf{"偏差这么小"本身就是 RH 的数值表现}：\ |\delta_T|\asymp\log T\ \text{（而平凡界}\asymp T^{1/2}）✓✓✓$$
$$\text{(c)}\ \text{要把}\ |\delta_T|\ \text{从}\ \log\ \text{级再压低} \Longrightarrow \text{须}\ |\psi(T)-T|\ll T^{\frac12}(\log T)^{c'}\ \text{型界} \Longrightarrow \textbf{即 RH 强度}✓✓✓$$
$$\Longrightarrow\ \boxed{\mathfrak G\ \textbf{确认为重述（③）}}：\text{偏差小}\iff\mathrm{RH}；\ \text{压制偏差}\iff\mathrm{RH} ⟹ \textbf{夹逼类方案不能产生新杠杆}✓✓✓$$

## §5 副产品（可复用资产）
$$\text{① 一个}\ \textbf{干净、廉价、自足} \text{的数值探针}：\ \delta_T=S_T-\frac{T^{1-s}-s}{1-s}\ \text{（无需 ζ、无延拓）}✓✓$$
$$\text{② 已量化}\ \textbf{分辨率地板}\ \approx0.15\ \text{与}\ \log\ \text{背景}\ \alpha\approx0.146✓✓$$
$$\text{③ 若要真正判定幂次性}：\text{须把}\ T\ \text{推到}\ 10^{10}\ \text{级使}\ \log\ \text{效应变平（否则无法与}\ T^{0.1}\ \text{区分）}✓$$

## §6 边界
$$\text{(i)}\ §1\ \textbf{勘误已标}（首跑主项错，重跑改）✓\quad\text{(ii)}\ §2--§3\ \text{为本档实测（}\Lambda\ \text{由筛法，非外部表）}✓$$
$$\text{(iii)}\ \text{人工}\ \beta\ \text{对照为}\ \textbf{模型层}（\text{把}\ T^{\beta-1/2}\ \text{项加到实测背景上}），\ \textbf{非} \text{真实离轴零点}✓$$
$$\text{(iv)}\ \textbf{未用 RH}；\ \text{全部为有限整数计算}✓$$
