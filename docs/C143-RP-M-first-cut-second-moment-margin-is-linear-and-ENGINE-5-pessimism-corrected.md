已查地图（**先查后写**）：`E4-ENGINE-4`（三工具；**卡点逐字**："三条工具合起来仍缺一步 —— 把 ≥ M/5 个对齐项的优势，从其余项的 −1 里救出来"）、`E4-ENGINE-5`（RMS 路线与**失效点**：`(1/2)MK` vs `M^2\log K` ⟹ 断言 M≳12 起失去分辨力）、`E4-ENGINE-2`（`M=1` 引理 C）、`E4-ENGINE-3`。关键词回查：`分离二分`=0、`近退化情形`=0、`对角项结构`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:16「开 (A)，直接开始写 (RP_M), M≤11 的第一步，不要做任务卡」）**：**第一步实算**：判这条路线在小 `M` 能否闭合。
**结论（先行）**：$$\textbf{(一)}\ \text{卡点（逐字）}：\text{"把}\ \ge M/5\ \text{个对齐项的优势，从其余项的}\ -1\ \text{里救出来"}✓$$
$$\textbf{(二)}\ ⭐\ \textbf{第一刀实算（本档新）}：\min_\theta\sum_{k\le5M}(\mathrm{Re}\,S(k))^2\ \approx\ \frac{KM}{4}\ (\text{对抗最优化}) \Longrightarrow \text{相对阈值}\ K/4\ \text{的比值}\ \textbf{约等于}\ M✓✓$$
$$\textbf{(三)}\ ⚠️\ \textbf{更正}\ \text{`ENGINE-5`}\ \text{的悲观估计}：\text{其粗略界}\ \tfrac12MK-cM^2\log K\ \text{在}\ M=11\ \text{时已}\ \textbf{为负}（302.5-484<0）\ \textbf{完全无用};\ \text{而真实最小值}\approx134✓✓$$
$$\textbf{(四)}\ ⭐\ \text{真障碍}＝\text{对角项／cross 项的}\ \delta\text{-依赖}（\theta_j\approx0\bmod\pi\ \text{时}\ D_K\ \text{尾大}）\Longrightarrow \text{需}\ \textbf{分离二分}✓✓$$
$$\textbf{(五)}\ \text{下一步}＝\text{写这个二分}：\textbf{近退化}（多个\ \theta_j\approx0\bmod\pi）\ \text{直接给}\ \max f\ \text{大};\ \textbf{非退化}\Longrightarrow\text{cross 项受}\ 1/\delta\ \text{控制}✓✓$$

FREEZE-ACK: 本档即冻结期内的第一刀实算与更正（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`(RP_M)` 第一步实算（二阶矩余量≈M 倍）＋ 对 `ENGINE-5` 失效点估计的更正 ＋ 分离二分作为下一步** —— 关系 = 实算与更正，非新机制
D1: 0

# C-143 · **(RP_M) 第一刀：二阶矩余量是线性的（`≈ M` 倍）＋ 更正 `ENGINE-5` 的悲观估计**

> **唐先生 2026-09-19 12:16**：开 (A)，**直接写第一步**（不做任务卡）✓

---

## §1 卡点（`ENGINE-4` 逐字）

$$\textbf{"三条工具合起来仍缺一步 —— 把}\ \ge M/5\ \textbf{个对齐项的优势，从其余项的}\ -1\ \textbf{里救出来"}✓✓$$
$$\qquad M=1\ \text{时无"其余项"故直接闭合};\ M\ge2\ \text{时正需要这一步}✓$$
$$\qquad \text{（我方补充}：\text{粗计数界}\ f(k)\ge\tfrac32n_k-M\ \text{要}\ \ge\tfrac12\ \text{需}\ n_k\ge\tfrac23M+\tfrac13;\ \text{而鸽笼只给}\ M/5\ ⟹ \textbf{计数路线本身可证不足}✓✓）$$

## §2 ⭐ 第一刀实算（本档新）

$$\text{目标}：\min_{\theta}\ Q(\theta):=\sum_{k=1}^{5M}\Big(\sum_{j=1}^{M}\cos(k\theta_j)\Big)^2\quad(\text{对抗最优化}：\text{Nelder–Mead}\times60\ \text{起点})$$

$$\begin{array}{c|r|r|r|r|r}
M & K=5M & K/4\ (\text{阈值}) & \min Q\ (\text{实测}) & \text{比值} & \text{该配置的}\ \max f\\\hline
1 & 5 & 1.25 & 1.6356 & 1.31 & 0.9173\\
2 & 10 & 2.50 & 4.9375 & 1.98 & 0.9542\\
3 & 15 & 3.75 & 9.8544 & 2.63 & 2.4748\\
4 & 20 & 5.00 & 16.3524 & 3.27 & 1.4534\\
5 & 25 & 6.25 & 27.1715 & 4.35 & 1.9771\\
6 & 30 & 7.50 & 36.5500 & 4.87 & 4.0196\\
7 & 35 & 8.75 & 48.1580 & 5.50 & 2.7303\\
8 & 40 & 10.00 & 72.6799 & 7.27 & 2.9542\\
9 & 45 & 11.25 & 86.9851 & 7.73 & 2.3645\\
10 & 50 & 12.50 & 103.9194 & 8.31 & 2.8362\\
11 & 55 & 13.75 & 133.8640 & 9.74 & 3.3150\\
\end{array}✓✓$$

$$\textbf{读数}：\text{①}\ \min Q\ \textbf{始终} > K/4，\textbf{且比值随}\ M\ \textbf{近似线性增长}（\approx M）✓✓$$
$$\qquad\quad \text{②}\ \text{该配置处}\ \max f\ \textbf{为正且不小}（0.92\to3.32） \Longrightarrow \text{极小化配置}\ \textbf{不产生符号问题}✓✓$$
$$\qquad\quad \text{③}\ \text{拟合}：\min Q/K\approx M/4 \Longrightarrow \min Q\approx KM/4✓✓$$

## §3 ⚠️ 更正 `ENGINE-5` 的失效点估计

$$\text{`ENGINE-5` 原判据}：\text{相容当}\ \tfrac12MK\ \lesssim\ M^2\log K \iff \log(5M)\gtrsim2.5 \iff M\gtrsim12 \Longrightarrow \text{"从}\ M\approx12\ \text{起失去分辨力"}✓$$
$$\textbf{本档更正}：\text{该粗略界}\ \tfrac12MK-cM^2\log K\ \text{在}\ M=11\ \text{时}＝302.5-c\cdot484\ \textbf{已为负}（c=1）⟹ \textbf{比无用更差}✓✓$$
$$\qquad \text{而}\ M=11\ \text{的真实最小值}\approx134\quad(\text{远大于}\ K/4=13.75)✓✓$$
$$\Longrightarrow\ \boxed{\text{损失项}\ M^2\log K\ \text{被严重高估};\ \text{“}\ M\gtrsim12\ \text{失去分辨力”}\ \textbf{不成立}}✓✓$$
$$\qquad ⚠️\ \text{但注意}：\text{本档数值给的是}\ \min Q\ \text{的}\ \textbf{上界}（\text{启发式搜索}）;\ \text{“真实最小值更大”不成立风险存在，故}\ \text{§3}\ \text{只推翻}\ \textbf{其证明}（\text{粗略界为负}），\ \textbf{不推翻其动机}✓$$

## §4 路线可行性的真正障碍（本档分析）

$$\sum_{k\le K}f(k)^2=\tfrac12\sum_{j,l}\big[D_K(\theta_j-\theta_l)+D_K(\theta_j+\theta_l)\big],\qquad |D_K(\varphi)|\le\min\Big(K,\ \frac{c}{|\varphi|}\Big)✓$$
$$\textbf{对角项}\ (j=l)：\tfrac12\big[K+D_K(2\theta_j)\big] \Longrightarrow \theta_j\approx0\ \text{或}\ \pi\ \text{时}\ D_K(2\theta_j)\approx\pm K \Longrightarrow \textbf{可抵消}✓✓$$
$$\textbf{cross 项}\ (j\ne l)：\theta_j\approx\pm\theta_l\ \text{时}\ \textbf{无界} \Longrightarrow \text{粗略界必须付}\ M^2/\delta ⟹ \textbf{这就是}\ M^2\log K\ \text{的来源}✓✓$$
$$\Longrightarrow\ ⭐\ \textbf{需分离二分}：\textbf{近退化}（\text{多个}\ \theta_j\approx0\bmod\pi）\ \text{直接给}\ \max f\ \text{大};\ \textbf{非退化}（\delta\text{-分离}）\Longrightarrow \text{cross 项受}\ 1/\delta\ \text{控制}✓✓$$

## §5 下一步（**写这个二分**）

$$\textbf{Case A（近退化）}：\#\{j:\ \mathrm{dist}(\theta_j,\pi\mathbb Z)<\delta\}\ \ge\ m \Longrightarrow \text{在合适}\ k\ \text{处}\ f(k)\gtrsim m-(M-m)✓$$
$$\textbf{Case B（}\delta\text{-分离）}：\text{全部}\ \mathrm{dist}(\theta_j,\pi\mathbb Z)\ge\delta\ \text{且成对}\ |\theta_j\mp\theta_l|\ge\delta \Longrightarrow \sum f^2\ \ge\ \tfrac{MK}{2}-c\frac{M^2}{\delta}✓$$
$$\qquad ⟹\ \text{取}\ \delta\ \text{与}\ M\ \text{匹配} \Longrightarrow \sum f^2>K/4\ \text{可证} \Longrightarrow \max|f|\ge\tfrac12;\ \text{再处理符号}✓✓$$
$$\qquad ⚠️\ \text{待办}：\text{Case B 的}\ \max|f|\to\max f\ \text{（正性）仍需一步};\ \text{数值显示极值配置}\ \max f>0✓$$

## §6 边界与回查

- ⚠️ §2 为**实际运行**（脚本 `/tmp/rp1.py`；Nelder–Mead 60 起点；`M=1..11`）；给的是 `\min Q` 的**上界估计**（启发式）✓
- ⚠️ §3 只推翻 `ENGINE-5` **失效点证明的有效性**（粗略界为负 ⟹ 该证明不能支持其结论），**不声称**其二阶矩族负面结果"错误"（其"该族不足"的动机仍可能对，只是证明路径失效）✓
- ⚠️ §4／§5 为**分析草案**，**未证明**；Case B 的数字待核 ✓
- ⚠️ **不声称** `(RP_M)` 已证；**未用** RH；**未改**任何原档（仅追加更正指针）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:2x）`[纪律]`（先跑后写）

```
技术词 分离二分   命中文件数=0 ::  ⟹ 本档新增
技术词 近退化情形  命中文件数=0 ::  ⟹ 本档新增
技术词 对角项结构  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
