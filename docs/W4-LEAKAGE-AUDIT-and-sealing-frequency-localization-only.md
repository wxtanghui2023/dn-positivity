# ⚔️ **W4 Leakage/Error-Budget Audit**（纯数学）⟹ **W4 正式封存为"仅频率定位机制"**

> 依唐先生 13:33：**在烧}\ 10^{11\!-\!12}\ \text{算力之前，先做纯数学审计**：频率投影后的增长估计器，**理论上是否有比 GAP-② 更低的分辨率地板**？✓
> **本档结果**：① 背景泄漏**可**压制（但非瓶颈）；② 真正的瓶颈＝**频带混合**（相邻零点），**频率投影不能压制它**；③ 即使做成也只是**重测显式公式已知项** ⟹ **不值得烧算力** ⟹ **W4 封存** ✓✓✓

---

## §1 误差预算（三个来源，逐项估）

### (i) 背景（$\nu\approx0$）泄漏 → **可忽略** ✓
$$\text{背景振幅}\ A_{\rm bg}\approx1.688\ (\nu=0)；\ \text{Hann 旁瓣衰减}\ \asymp(\Delta\nu)^{-3}\ \text{型}✓$$
$$\text{在}\ \nu_j\approx30\!-\!90\ \text{的带内}：\ \text{泄漏}\ \asymp A_{\rm bg}\cdot(\nu_j)^{-3}\approx1.688\times(30)^{-3}\approx6\times10^{-5} \Longrightarrow \textbf{可忽略}✓✓$$
$$\Longrightarrow\ ⭐\ \textbf{结论 (i)}：\ \boxed{\text{频率投影}\ \textbf{能} \text{系统压制背景}}✓✓\quad\text{—— 这正是频率坐标成功的原因}✓$$

### (ii) **相邻零点频带混合** → **主导项，且不可被投影压制** ✗✗
$$\text{当前全窗分辨率}\ \Delta\nu=2\pi/U=0.455；\ \textbf{三窗}\ \Delta\nu_{\rm sub}=2\pi/L=1.37\ (L=4.6)✓$$
$$\text{零点间距}\ \Delta\gamma\ \asymp\ 2.5\!-\!5 \Longrightarrow \boxed{\Delta\nu_{\rm sub}\ \textbf{与}\ \Delta\gamma\ \textbf{同阶}}✓✗✓$$
$$\Longrightarrow\ \text{每个频带}\ \textbf{不是单零点带}，\ \text{而是}\ \textbf{若干零点贡献之和，相对相位随窗口漂移}✓✓$$
$$\Longrightarrow\ \hat\eta_j\ =\ \text{各贡献者}\ \eta\ \text{的}\ \textbf{权重漂移混合} \Longrightarrow \textbf{η 随窗口漂移}✓✓✓\quad(\text{与实测}\ \pm0.08\ \text{漂移}\ \textbf{逐字吻合})✓✓$$
$$\Longrightarrow\ ⭐\ \textbf{结论 (ii)}：\ \boxed{\text{频率投影}\ \textbf{不能} \text{压制频带混合；它由}\ 2\pi/L\ \text{决定，}\ \textbf{只能靠加长}\ U\ \text{改善}}✗✗✗$$

### (iii) 离散化／有限点数 → 小
$$\text{增加}\ T\ \text{点数只压低 (iii)，}\ \textbf{不碰}\ (ii)✓✗\qquad(\text{故"把同一仪器做大"}\ \textbf{无效})✓✓$$

## §2 ⭐⭐ 要"频带单零点"，需要多大的 $U$？
$$\text{要求 Hann 主瓣宽}\ 2\pi/L\ \lesssim\ \Delta\gamma/3\ (\Delta\gamma\approx2.5) \Longrightarrow L\gtrsim7.5✓$$
$$\text{三窗方案}：U=3L\gtrsim23 \Longrightarrow \frac{T_{\max}}{T_{\min}}\gtrsim e^{23}\approx10^{10}✓$$
$$\text{取}\ T_{\min}=10^3 \Longrightarrow \boxed{T_{\max}\sim10^{13}} \Longrightarrow \textbf{贵}✗✗\qquad(\text{与唐先生"须}\ 10^{11\!-\!12}"\ \text{估计一致})✓$$

## §3 ⭐⭐⭐ 即使做成，也只是**重测显式公式的已知项**
$$\text{每个}\ \gamma\ \text{带的增长率}\ \textbf{按定义} \text{就是该零点的}\ \beta\ (\text{显式公式})\ \Longrightarrow \text{测出来的}\ \eta_j\ \textbf{不含新信息}✓✗✓$$
$$\Longrightarrow\ \boxed{\text{成功测量}\ \equiv\ \text{对显式公式的数值确认}，\ \textbf{不是新的 RH 机制}}✓✓✓$$
$$\qquad(\text{与}\ \text{唐先生 13:33 的警惕}\ \textbf{逐字一致}：\text{"更高精度测量显式公式中的已知零点项"})✓✓$$

## §4 判词
$$\boxed{\textbf{W4}\ \text{正式封存}：\ \ = \ \textbf{frequency-localization mechanism only}}✓✓✓$$
$$\text{理由（三条全闭合）}：\text{① 背景可压制（非瓶颈）\ ② 瓶颈＝频带混合，投影不能压制，须}\ U\gtrsim23\Rightarrow T_{\max}\sim10^{13}\ \text{（贵）\ ③ 即便做成＝重测已知项}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{不投入}\ 10^{11\!-\!12}\ \text{算力}}✓✓$$

## §5 保留资产（本线真正的正产出）
$$\boxed{\text{prime arithmetic}\ \longrightarrow\ \textbf{blind frequency localization}\ \longrightarrow\ \gamma\text{-indexed spectral peaks}}✓✓✓$$
$$\qquad\text{两条坐标}：\boxed{\nu=\gamma\ (\text{已实验拿到，blind-success})\qquad\big|\qquad \eta=\beta-\tfrac12\ (\text{未获分辨能力})}✓✓$$
$$\qquad \text{地位}：\ \text{W4}\ \text{证明了}\ \textbf{频率轴真实可观测}；\ \textbf{尚未证明} \text{增长轴可观测}✓✓$$
$$\qquad \text{与}\ A\text{-}1\ (\text{Guinand 相位锁定})\ \textbf{同族}✓$$

## §6 边界
$$\text{(i)}\ §1\ \text{的旁瓣估计为}\ [\textbf{结构}]（\text{Hann 衰减率与常数未逐位核}）✓\quad\text{(ii)}\ §2\ \text{为量级估算}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \text{本轮}\ \textbf{零计算}✓$$
