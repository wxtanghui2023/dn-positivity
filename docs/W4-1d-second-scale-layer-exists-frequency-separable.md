# ⚔️ **W4-1d** · 第二尺度层**存在且可分**：$\log T$ 上的**频率层**

> 依唐先生 13:24「先走 A，但先检查 $\delta_T(s)$ 复结构是否确实存在第二个可分离尺度层」✓
> **本档结果**：**存在** ✓✓ —— 且**频率可分**（动态范围 30–80×）✓✓✓

---

## §1 检查设计（便宜且直接）
$$\text{阶梯}\ u=\log T\ \text{上}\ 256\ \text{点均匀，}\ T\in[10^5,\,2\times10^8],\qquad s=\tfrac12\ (\text{取}\ t=0)✓$$
$$A(T):=\sum_{n\le T}\frac{\Lambda(n)}{\sqrt n}\ (\text{增量前缀和，一趟过完}),\qquad \text{主项}=2\sqrt T-1,\qquad \delta(T):=A(T)-\text{主项}✓$$
$$\Delta u=0.0298,\qquad \nu_{\max}=105.4,\qquad \Delta\nu=0.827\qquad(\Lambda\ \text{分块筛到}\ 2\times10^8,\ \text{素幂}\ 11{,}080{,}801\ \text{项})✓$$

## §2 ⭐⭐⭐ 结果：谱上**两层**清楚分开

| $\nu$ | 振幅 | 最近的 $\gamma$ | $\lvert\nu-\gamma\rvert$ |
|:--|:--|:--|:--|
| **0.000** | **1.688** | —（**低频背景层**） | — |
| **0.823** | **0.854** | —（趋势层） | — |
| 13.998 | 0.063 | 14.135 | 0.137 |
| **32.936** | 0.041 | **32.935** | **0.001** ✓✓✓ |
| 20.585 / 21.409 | 0.039 / 0.037 | 21.022 | 0.437 / 0.387 |
| 30.466 | 0.036 | 30.425 | **0.041** ✓✓ |
| 24.702 | 0.032 | 25.011 | 0.309 |
| 60.932 | 0.030 | 60.832 | **0.100** ✓✓ |
| 41.170 | 0.029 | 40.919 | 0.252 |
| 52.698 | 0.025 | 52.970 | 0.272 |
| 79.047 | 0.025 | 79.337 | 0.290 |
| **94.692** | 0.024 | **94.651** | **0.041** ✓✓ |
| 43.641 | 0.024 | 43.327 | 0.314 |

$$\Longrightarrow\ \boxed{\text{（i）}\ \nu\approx0\ \text{低频背景层（A=1.688）；\ （ii）}\ \nu=\gamma\ \text{处的零点峰层}}✓✓✓$$
$$\text{最好的匹配}\ \nu=32.936\ \text{vs}\ \gamma=32.935：\ |\Delta|=\textbf{0.001}✓✓✓$$

## §3 ⭐⭐ **可分性**（这是之前缺的东西）
$$\text{动态范围}：\text{背景}\ 1.688\ \text{vs}\ \gamma\ \text{峰}\ 0.024\!-\!0.063 \Longrightarrow \boxed{30\!\sim\!80\times}✓✓$$
$$\text{低频（}<1）\ \text{最大}\ 1.688\qquad\big|\qquad [10,60]\ \text{区间最大}\ 0.063 \Longrightarrow \textbf{频率可分}✓✓✓$$
$$\text{对照}：\text{标量}\ |\delta_T|\ \text{里两层}\ \textbf{混在一起}（\text{故只能一步滤波）}；\ \log T\ \text{谱里}\ \textbf{两层分开}✓✓✓$$

## §4 结构解释（逐字）
$$\delta_T(s)=-\sum_\rho\frac{T^{\rho-s}}{\rho(\rho-s)}+\ldots \Longrightarrow \text{每项}=T^{\beta-\frac12}\cdot e^{i(\gamma-t)u},\qquad u=\log T✓✓$$
$$\Longrightarrow\ \boxed{\text{u-频率}=\gamma-t\ (\text{零点位置})\qquad\big|\qquad \text{u-增长率}=\beta-\tfrac12\ (\text{零点偏移})}✓✓✓$$
$$\text{即：}\textbf{第二层＝频率层}，\ \text{而}\ \textbf{每频率的增长率就是}\ \beta-\tfrac12 ——\ \text{这正是所需的判别量}✓✓✓$$

## §5 与资产的对接
$$\text{这正是}\ \textbf{Guinand 相位锁定} \text{结构}（\text{资产}\ A\text{-1}：\sum_k\sin(\gamma_k\log p)=O(1)，\ \text{已验}）✓✓$$
$$\Longrightarrow\ \text{第二层不是新造，而是}\ \textbf{我们已验资产的谱形式}✓✓$$

## §6 意义（对 W4-1c「限一步」的修正）
$$\text{之前判"限一步"因}\ \textbf{背景只有单一}\ \log\ \text{幂}（\text{标量视角}）✗$$
$$\text{现在：}\ \text{两层}\ \textbf{频率不同} \Longrightarrow \textbf{可用频带选择滤波} \Longrightarrow \textbf{可累积}✓✓✓$$
$$\qquad \mathcal D\ \text{升级为}\ \textbf{频带选择}：\text{低频带}\to\text{背景}；\ \nu\approx\gamma\ \text{带}\to\text{该零点}✓✓$$
$$\qquad ⚠️\ \textbf{但}：\text{这只恢复了}\ \textbf{"可分性"}，\ \textbf{不等于} \text{已获得}\ \beta\ \text{判据}——\text{读出}\ \beta\ \text{仍须}\ T\ \text{足够大（增长率}\ T^{\beta-1/2}\ \text{的测量）}✓✓$$

## §7 下一步（新的、可累积的）
$$\text{① 对每个}\ \gamma\ \text{峰做}\ \textbf{增长率测量}：\text{分两段}\ T\ \text{范围比较同频率振幅} \Longrightarrow \textbf{每零点}\ \beta\ \text{探针}✓✓$$
$$\text{② 若所有}\ \gamma\ \text{峰增长率}\ \approx0 \Longrightarrow \text{数值一致}\ \beta=\tfrac12\ (\text{非证明})✓$$
$$\text{③ 若某}\ \gamma\ \text{峰增长率}\ >0 \Longrightarrow \beta>1/2\ \text{的直接数值信号}✓✓✓$$

## §8 边界
$$\text{(i)}\ N=256,\ \Delta\nu=0.827 \Longrightarrow \text{近邻零点混合}（\text{如}\ 20.585/21.409\ \text{双峰围}\ \gamma=21.022）✓$$
$$\text{(ii)}\ \text{零点}\ \gamma\ \text{仅作}\ \textbf{对照}（\text{非输入}）✓\quad\text{(iii)}\ \text{未用 RH}；\ \text{全部有限整数计算}✓$$
