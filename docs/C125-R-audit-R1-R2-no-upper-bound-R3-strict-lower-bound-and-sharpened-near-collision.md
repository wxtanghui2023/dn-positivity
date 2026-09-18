已查地图（**先查后写**）：`C-121`（三层设计第一行硬检查）、`C-122`（Toeplitz PSD＝K2 判死）、`C-123`（和法则＋近碰撞必要条件，含一次自纠）、`C-124`（刀③：近似→精确的间隙界真空）、`lean-frontier-audit/LawN256.lean`（逐字：`S=(1/256)\sum_c w_c|\hat\mu_c|^2`；`m\in\{1,2\}`；`\sum m=256`；`\tau=3/10^{40}`）。关键词回查：`R-审计`＝0、`Hankel 秩恒等`＝0、`四阶近碰撞`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:28「改成真正的 R-审计（R1–R3）＋不要随机搜索」⟹ **先自纠一处计数，再给三条审计结论** ✓✓：**(甲) ⚠️ 自纠（第 7 次同类）**：`C-124` 刀②的计数阈值应为 `R\le191`（`\Delta^2E_j` 只在 `j=2..254` 上有定义，共 **191** 个），**不是 `R\le253`** ⟹ 阈值**更严**，结论方向不变 ✓✓；**(乙) R1／R2 审计＝\textbf{不给出上界}**：`R` 与 **Hankel 秩精确相等**（相异频率＋非零系数），而"255 个近似值"**信息论上不能约束秩**（计数警告成立）⟹ R1／R2 **不产出** `R\le191` ✗；**(丙) ⭐ R3（正性）给出一条\ \textbf{严格下界}＋一条\ \textbf{加严的近碰撞}**：`R\ge P\ge128`（`\sum m=256,m\le2 \Longrightarrow` 相异位置 `P\ge128`，且差集含 `\{x_a-x_b\}` 固定 `b` ⟹ `R\ge P`）✓✓；且由 **二阶梯度的能量** `\sum_{j=2}^{254}|\Delta^2E_j|^2=O(10^{-76})` 得 **对角项** `\sum_p c_p^2|\zeta_p-1|^4\le1.44\times10^{-78}` ⟹ ⭐ **存在一对极近碰撞** `|\zeta_p-1|\lesssim2.2\times10^{-21}`（`\delta` 与 0 相差 `\lesssim8.8\times10^{-20}\ \mathrm{mod}\ 256`），把 `C-123` 的 `0.6034` **加严约 18 个数量级** ✓✓（⚠️ 该结论受"交叉项不抵消"限制，标**条件性**）；**(丁) 判决**：**`R\le191` 推不出来**，且**即使推出也不能关闭 B2-1**（因刀③已证"近似→精确"真空）⟹ **B2-1 仍 OPEN，R-路线不闭合**；真正缺的是**带相消控制的"低秩且 ε-接近线性 ⟹ 频率聚簇"定理**＝**成对几何** ✓✓

FREEZE-ACK: 本档即冻结期内的 R1–R3 结构审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **R-审计（R1/R2 无上界、R3 严格下界与加严近碰撞）＋一处计数自纠** —— 关系 = 审计与自纠，非新机制
D1: 0

# C-125 · **R-审计（R1–R3）＋ 一处计数自纠**

> **时间**：2026-09-18 23:28 唐先生：**「改成真正的 R-审计」** ✓

---

## §0 结论（先行）

$$\textbf{(甲)}\ ⚠️\ \textbf{自纠}：\text{阈值应为}\ R\le191\ (\text{不是}\ 253)✓✓$$
$$\textbf{(乙)}\ \text{R1／R2}＝\textbf{不给出上界} \Longrightarrow R\le191\ \text{推不出}✓✓$$
$$\textbf{(丙)}\ ⭐\ \text{R3}：R\ge P\ge128\ (\textbf{严格})；\ \text{且}\ \exists\ \text{极近碰撞}\ |\delta|\lesssim8.8\times10^{-20}\ (\textbf{条件性})✓✓$$
$$\textbf{(丁)}\ \textbf{B2-1 仍 OPEN}；\ \text{R-路线不闭合};\ \text{缺的是}\ \textbf{成对几何}✓✓$$

## §1 （甲）计数自纠

$$C\text{-}124\ \text{刀②写}：\Delta^2E_j=0\ \text{for}\ j=1..253 \Longrightarrow R\le253\qquad ⚠️\ \textbf{计数错}✓$$
$$\text{正确}：\Delta^2E_j=E_{j+1}-2E_j+E_{j-1}\ \text{需}\ j-1\ge1\ \text{且}\ j+1\le255 \Longrightarrow j=2..254，\textbf{共 191 个}✓✓$$
$$\Longrightarrow \text{Vandermonde 所需的"连续零点数"为}\ 191 \Longrightarrow \textbf{阈值}\ R\le191✓✓$$
$$\qquad \text{（结论方向不变：}\text{仍是条件性刚性};\ \text{只是条件}\ \textbf{更严}）✓$$

## §2 （乙）R1／R2：**不给出上界**

$$\textbf{恒等式（严格）}：\text{设}\ \nu:=\mu*\tilde\mu=\sum_{a,b}m_am_b\,\delta_{x_a-x_b}，\ \text{则}\ E_j=\hat\nu(j/256)✓$$
$$\qquad \text{且}\ R=\#\mathrm{supp}(\nu)=\textbf{Hankel 矩阵的秩}\ \big((E_{j+k})_{j,k}\big)✓✓$$
$$\qquad \text{（相异频率＋非零系数 ⟹ 秩＝相异指数个数；经典）}✓$$
$$\text{但}：\text{"255 个值}\pm\tau" \text{对秩}\ \textbf{无信息论约束}⟹ \text{计数警告}\ \textbf{成立}✓✓$$
$$\qquad \text{对照：}\text{目标序列}\ j\ \text{的秩＝2（最小递推}\ (X-1)^2，双重根）; \text{而任何构型的递推是}\ \Pi_{\delta\in\mathrm{supp}\nu}(X-\zeta_\delta)\ \text{＝}\ R\ \textbf{个单根}✓✓$$
$$\qquad \Longrightarrow \textbf{张力存在}（\text{双重根 vs 单根}），\text{但}\ \textbf{具现它需要}\ R\le191\ \text{＋精确性}⟹ \text{R1／R2 本身不给上界}✗✗$$

## §3 ⭐（丙）R3：正性给出的**严格下界**与**加严近碰撞**

### 3.1 严格下界（可立即引用）

$$\sum_i m_i=256,\quad m_i\in\{1,2\} \Longrightarrow \#\{\text{相异位置}\}=P\ge128✓✓$$
$$\text{固定}\ b：\{x_a-x_b:a\}\ \text{有}\ P\ \text{个相异值} \Longrightarrow \boxed{R\ge P\ge128}✓✓$$
$$\qquad \text{（}\textbf{严格、仅用整数性与总质量}）⟹ \text{与"需}\ R\le191\text{"}\ \text{并不冲突}（128\le191）✓$$

### 3.2 加严的近碰撞（**条件性**：受交叉项限制）

$$\text{设}\ b_p:=c_p(\zeta_p-1)^2\ (\zeta_p=e^{2\pi i\delta_p/256},\ c_p=m_am_b>0);\quad \Delta^2E_j=\sum_p b_p\zeta_p^{\,j}✓$$
$$\text{对}\ j=2..254：|\Delta^2E_j|\le4\tau=1.2\times10^{-39} \Longrightarrow \sum_{j=2}^{254}|\Delta^2E_j|^2\le191\cdot16\tau^2\approx2.75\times10^{-76}✓✓$$
$$\text{展开}\ \sum_j|\Delta^2E_j|^2=\underbrace{\sum_p|b_p|^2\cdot191}_{\text{对角}}+\underbrace{\sum_{p\ne q}b_p\bar b_q\,G(\theta_p-\theta_q)}_{\text{交叉}},\quad |G|\le\frac{2}{|\sin((\theta_p-\theta_q)/2)|}✓$$
$$\Longrightarrow \text{对角项本身}\ \le2.75\times10^{-76} \Longrightarrow \sum_p c_p^2|\zeta_p-1|^4\le1.44\times10^{-78}✓✓$$
$$\qquad \text{（}c_p\ge1）\Longrightarrow \min_p|\zeta_p-1|\lesssim2.2\times10^{-21} \Longrightarrow \boxed{\exists\ \text{一对：}|\delta|\lesssim8.8\times10^{-20}\ (\mathrm{mod}\ 256)}✓✓$$
$$\qquad \text{⚠️}\ \text{若交叉项不抵消（}\text{或抵消有界}）\text{则此结论成立};\ \text{否则只能得}\ \textbf{"或差异高度聚簇"}✓✓$$
$$\qquad \text{⚠️}\ \text{此条件性}\ \textbf{不得} \text{写成无条件定理}✓$$

## §4 （丁）判决（对照唐先生的判死表）

$$\text{严格推出}\ R\le191：\textbf{未达}（\text{§2}） \Longrightarrow \text{不能关闭 B2-1}✓$$
$$\text{即使推出}：\text{仍需"近似→精确"}\ \textbf{而刀③已证其真空} \Longrightarrow \textbf{双重未达}✓✓$$
$$\text{允许范围}：R\in[P,\#\text{pairs}]=[128,\ 65536] \Longrightarrow \textbf{远大于 191}，\ \text{"}\gg191\text{"}\ \text{允许}✓$$
$$\Longrightarrow \boxed{\textbf{B2-1 仍 OPEN}；\textbf{R-路线不闭合}}✓✓$$
$$\qquad \text{★ 真正缺的}：\textbf{带相消控制的}\ \text{"}\textbf{低秩＋}\varepsilon\text{-接近线性} \Longrightarrow \textbf{频率聚簇}\text{"}\ \text{定理} \Longrightarrow \text{这就是}\ \textbf{成对几何}✓✓$$
$$\qquad \text{（与}\ \text{`C-119`}\ \text{多体线经验一致：只有新的}\ \textbf{联合结构} \text{才有价值}）✓✓$$
$$\text{依唐先生指令}：\textbf{不进入 B2-2};\ \textbf{不做随机搜索}✓$$

## §5 本档净产出（三条，均可引用）

$$\text{(1)}\ \textbf{恒等式}：R=\text{Hankel 秩} \Longrightarrow \text{R-问题＝秩问题}（\text{把几何问题代数化}）✓✓$$
$$\text{(2)}\ \textbf{严格下界}：R\ge P\ge128（\text{纯由整数性＋总质量}）✓✓$$
$$\text{(3)}\ \textbf{条件性加严}：\exists\ \text{近碰撞}\ |\delta|\lesssim8.8\times10^{-20}\ (\text{比}\ \text{`C-123`}\ \text{的}\ 0.6034\ \text{严约 18 个数量级})✓✓$$
$$\qquad \text{（}\text{`C-123`}\ \text{的}\ 0.6034\ \text{来自和法则（一阶量）};\ \text{本档来自二阶能量} \Longrightarrow \text{两法可叠加}）✓$$

## §6 边界与回查

- ⚠️ §1 为**自纠**（计数）；§2 为**经典事实引用＋判断**；§3.1 为**严格**；§3.2 为**条件性**（交叉项未控）✓
- ⚠️ §4 判决**严格**：R-路线不闭合 ⟹ **不声称**能 pin ✓
- ⚠️ **不声称**与 RH 相关；**未用** RH；**未改**前沿档案 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；⚠️ 自纠**先于**落档（未把 253 当既有结论继续用）✓
- ⚠️ 累计自纠（本会话）：**7 次**（`n=2` 引文／`V191` 过强／"机制不可能"过强／`(b)` 伪／"无零信息"未证／和法则整数差／本轮计数）✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:3x）`[纪律]`（先跑后写）

```
技术词 R-审计        命中文件数=0  ⟹ 本档新增
技术词 Hankel 秩恒等   命中文件数=0  ⟹ 本档新增
技术词 四阶近碰撞      命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
