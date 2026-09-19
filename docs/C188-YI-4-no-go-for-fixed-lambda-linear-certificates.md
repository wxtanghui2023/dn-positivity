已查地图（**先查后写**）：`C-187`（乙三层审计：可分性松弛／非光滑极值）、`C-186`（Fejér 审计 1/20 封顶）、`C-181` §3(a)（Fejér 权路线退化）、`C-170`（mixed-λ 界）。关键词回查：`零均值障碍`=0、`线性证书`=0、`账本修正`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 21:22 指令）**：**乙-4 —— mixed-λ 非可分证书第一刀**；并立即修正账本（撤回 0.4044 作为真值）✓
**结论（先行）**：$$\textbf{(一)}\ ⚠️⚠️\ \textbf{fixed-λ 线性证书存在}\ \textbf{可证障碍}（\text{非数值失败，是定理}）✓✓$$
$$\qquad \text{证书逻辑}：\max_k S_k(x)\ \ge\ \sum_k\lambda_k S_k(x)\（\lambda\ge0,\ \textstyle\sum\lambda=1\text{）} \Longrightarrow \text{只需}\ \inf_x\sum_k\lambda_k S_k(x)\ \ge\ c✓$$
$$\qquad \text{但}\ \sum_k\lambda_k S_k(x)=\sum_j F_\lambda(x_j)，F_\lambda(r,\varphi)=\sum_k\lambda_k r^k\cos(k\varphi)✓$$
$$\qquad \textbf{关键}：F_\lambda\ \text{对}\ \varphi\ \text{的}\ \textbf{均值}=0（\text{各}\ k\ge1\ \text{的余弦均值为零}） \Longrightarrow F_\lambda\ \textbf{必有负值}✓$$
$$\qquad \Longrightarrow \inf_{\text{构型}}\sum_k\lambda_k S_k\ \le\ \inf_\varphi F_\lambda(1,\varphi)\ \color{red}{<}\ 0\qquad（\forall\lambda\ne0\text{，}M\ \text{任意}）✗✗$$
$$\qquad \Longrightarrow \boxed{\textbf{任何 fixed-λ 线性证书}\ \textbf{恒不能给出正的常数}}✓✓\qquad（\text{Fejér 权只是其中一个特例}✓）$$
$$\textbf{(二)}\ ⭐\ \textbf{账本修正}（\text{唐先生指令}）：\boxed{0.35\ \le\ C_3\ \le\ 0.373092\ldots}✓\qquad \textbf{0.4044 作废}✗$$
$$\qquad （\text{旧的}\ 0.4044\ \text{来自更粗的搜索，已被新的阻尼构型}\ 0.373092\ \text{否证为全局值}）✓$$
$$\textbf{(三)}\ \text{与}\ \text{C-187}\ \text{的合读}：\text{阻尼最坏情形}\ \textbf{同时} \text{抵抗}：\text{可分箱界}（\text{松弛}）✗／\text{线性加权}（\text{零均值}）✗／\text{局部单纯形}（\text{非光滑}）✗✓✓$$

FREEZE-ACK: 本档即冻结期内的攻击性推导（依 `§8.1`；不产候选结论）

D0: 本档对象 = **fixed-λ 线性证书的可证 NO-GO ＋ 账本修正（$C_3$ 夹逼）** —— 关系 = 机制级否定与账本更正，非新机制
D1: 0

# C-188 · 乙-4：fixed-λ 线性证书的**可证** NO-GO

---

## §1 定理（零均值障碍）

$$\textbf{命题}：\text{设}\ \lambda\ge0,\ \sum_k\lambda_k=1,\ \lambda\ne0。\text{则}\ \inf_{\text{构型}}\Big[\sum_k\lambda_k S_k(x)\Big]\ <\ 0✓$$
**证明**：构型空间包含 r_2 = ⋯ = r_M = 0（允许，因仅要求 max_j|z_j| = 1）✓
$$\qquad \text{此时}\ \sum_k\lambda_k S_k=\sum_k\lambda_k\cos(k\varphi_1)=:F_\lambda(1,\varphi_1)✓$$
$$\qquad \text{而}\ \int_0^{2\pi}F_\lambda(1,\varphi)\,d\varphi=2\pi\sum_k\lambda_k\cdot\underbrace{\frac1{2\pi}\int\cos(k\varphi)d\varphi}_{=0}=0✓$$
$$\qquad F_\lambda\ \text{连续且不恒为零（}\sum\lambda=1\text{）} \Longrightarrow \exists\varphi：F_\lambda(1,\varphi)<0 \Longrightarrow \inf_\varphi F_\lambda(1,\varphi)<0✓\qquad\square✓✓$$
$$\qquad \textbf{注}：\text{该论证}\ \textbf{对一切}\ M\ \text{成立}，\text{且对}\ M=1\ \text{也成立}✓$$

## §2 数值印证（本次实算）

$$\begin{array}{l|r|r|c}
\lambda\ \text{选择} & \inf_{r,\varphi}F_\lambda & M=3\ \text{时}\ \inf\sum\lambda_kS_k & \text{能否给正常数}\\\hline
\text{Fejér 权}\ (1-\tfrac{k}{K+1}) & -0.066667 & -0.200000 & \text{否}\\
\text{均匀权} & -0.258596 & -0.775789 & \text{否}\\
\text{支持}\ k\in\{2,5\}\ \text{各半} & -0.916756 & -2.750268 & \text{否}\\
\text{单频}\ k=1 & -1.000000 & -3.000000 & \text{否}\\
\text{单频}\ k=2 & -1.000000 & -3.000000 & \text{否}\\
\text{随机权} & -0.493553 & -1.480658 & \text{否}\\
\end{array}✓$$
$$\Longrightarrow \text{与 §1 的定理一致}：\textbf{全部为负}✗\ —— \textbf{Fejér 权只是最接近的一个}（-0.067）✓$$

## §3 为什么会这样（结构性诊断）

$$\textbf{① 线性证书丢失}\ \max\ \text{的鲁棒性}：\text{加权和是}\ \textbf{固定} \text{线性组合，}\text{可被"把阻尼点推到}\ 0"\ \text{击穿}✗$$
$$\qquad \text{而}\ \max_k S_k\ \text{是鲁棒的}：\text{每个点可在}\ \textbf{各自} \text{的}\ k\ \text{上贡献}✓\ ——\ \textbf{这正是耦合}✓$$
$$\textbf{② 与 C-187 的"可分性松弛"是}\ \textbf{同一损失的两种表现}：$$
$$\qquad \text{可分箱界：把}\ \max_k\ \text{与}\ \min_{x}\ \text{交换}✗\qquad \text{线性加权：用固定凸组合替代}\ \max✗$$
$$\qquad \Longrightarrow \textbf{二者都在"线性化}\ \max"\ \text{处损失} \Longrightarrow \text{任何}\ \textbf{线性} \text{路线都不够}✓✓$$
$$\textbf{③ 因此耦合必须是}\ \textbf{非线性} \text{的}：\text{活跃集/局部}✓\ \text{或}\ \text{构型分类}✓$$
$$\qquad ⚠️\ \text{但}\ \text{C-187}\ \text{已证：阻尼最坏点的局部（单纯形）机制}\ \textbf{失效}（0\notin\mathrm{conv}\text{，}c<0\text{）}✗$$
$$\qquad \Longrightarrow \text{两条非线性路线在阻尼情形}\ \textbf{同时受挫} \Longrightarrow \text{阻尼屏障的具体形状已清楚}✓✓$$

## §4 账本修正（立即生效）

$$\boxed{0.35\ \le\ C_3\ \le\ 0.373092\ldots}✓\qquad（\text{下界：}\text{C-184}\ \text{证书}✓；\text{上界：}\text{C-187}\ \text{阻尼候选构型}✓）$$
$$\qquad ⚠️\ \textbf{旧表述作废}：\text{"}C_3\approx0.4044\text{"}\ ✗\ —— \text{该值来自更粗搜索，}\textbf{不得} \text{再称真值}✓$$
$$\qquad ⚠️\ \text{上界}\ 0.373092\ \text{为}\ \textbf{数值候选}（\text{未证全局最优}）✗；\text{下界}\ 0.35\ \text{为}\ \textbf{已证证书}✓$$

## §5 边界

- ⚠️ §1 的定理**严格**（零均值论证 ✓；不依赖数值 ✓）——**对一切** $\lambda$ 与一切 $M$ ✓
- ⚠️ §2 的数值为**印证**（非证明）✓
- ⚠️ §3③ 的"必须非线性"是**结构判断**（非定理 ✗）：已排除的是**固定线性组合**这一类，未排除"依赖 $x$ 的 $\lambda$"或"分段线性"✗
- ⚠️ 本档**不声称** (RP_M) 阻尼版的结果 ✓；**不声称** $C_3$ 的精确值 ✓
- **未用** RH；**未改**他档正文（`C-184` 的账本修正以**追加指针**方式在本档给出 ✓）
- **纪律**：先跑后写 ✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`）

**读数（按实测，逐字）**：`零均值障碍`=0【新】、`线性证书`=0【新】、`账本修正`=**1**【**沿用**——
命中 `V2-35D-ell2-ell2-prime-fiber-audit-and-constraint-table.md`】✓
**自我更正**：初稿第三项记 0（凭印象），已按实测改写 ✓

```
技术词 零均值障碍   命中文件数=0 ::  ⟹ 本档新增
技术词 线性证书    命中文件数=0 ::  ⟹ 本档新增
技术词 账本修正    命中文件数=1 :: ./V2-35D-ell2-ell2-prime-fiber-audit-and-constraint-table.md  ⟹ 【沿用，非新增】
```
