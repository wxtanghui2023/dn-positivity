已查地图（**先查后写**）：`C-143`（第一刀：二阶矩余量≈`M` 倍；更正 `ENGINE-5`；分离二分作为下一步）、`E4-ENGINE-4`（卡点逐字）、`E4-ENGINE-2`（引理 C：`\max_{1\le k\le5}\cos k\theta\ge\tfrac12`）、`E4-ENGINE-5`（二阶矩族）。关键词回查：`偶数对齐`=0、`共振角`=0、`Case A 引理`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:22「选一个入门档目标，完整做完，写成短文投出去；不要再做元层面比较」）**：**锁定 `(RP_M), M\le11`；本刀＝分离二分的 `Case A`（已完成严格证明）**
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{目标锁定}：(\text{RP}_M):\ |z_j|=1\Longrightarrow\exists k\le5M:\ \sum_j\mathrm{Re}\,z_j^k\ \ge\ \tfrac12；\ \text{产出}＝\text{一篇短文}✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{Case A 引理（本档，}\textbf{已严格证明}）✓✓$$
$$\qquad \text{设}\ \delta\le\pi/6,\ m:=\#\{j:\ \mathrm{dist}(\theta_j,\pi\mathbb Z)\le\delta\};\ \text{若}\ m\ \ge\ \tfrac{2M}{3}+\tfrac13 \Longrightarrow \text{取}\ k=2：\ f(2)\ge\tfrac32m-M\ge\tfrac12✓✓$$
$$\qquad \text{机制}：\cos(2(\pi+x))=\cos(2x)\ \text{（周期}\ \pi\ \text{在}\ k=2\ \text{时）} \Longrightarrow \textbf{0 与}\ \pi\ \textbf{附近的点同时贡献}\ \approx+1✓✓$$
$$\textbf{(三)}\ ⚠️\ \textbf{Case B 是硬核}：\text{数值极值配置（}M=2:\ (60^\circ,90^\circ)）\ \text{属}\ \textbf{Case B}✓✓$$
$$\textbf{(四)}\ \text{故}\ (\text{RP}_M)\ \text{已归结为}\ \textbf{Case B}：\text{少点近}\ 0\bmod\pi\ \text{的配置}✓✓$$

FREEZE-ACK: 本档即冻结期内的目标锁定与 Case A 证明（依 `§8.1`；不产候选结论）

D0: 本档对象 = **目标锁定（`(RP_M), M\le11` 短文）＋ Case A 引理的严格证明 ＋ Case B 的精确表述** —— 关系 = 证明推进，非新机制
D1: 0

# C-144 · **(RP_M) Case A 已证：偶数 `k` 对齐引理；Case B 是硬核**

> **唐先生 2026-09-19 12:22**：选定一个目标、完整做完、写成短文；**不再做元层面比较** ✓

---

## §1 目标（锁定，不再改）

$$\boxed{(\text{RP}_M):\quad |z_j|=1\ (j\le M)\ \Longrightarrow\ \exists k\in[1,5M]:\ \sum_{j=1}^{M}\mathrm{Re}\,z_j^{\,k}\ \ge\ \tfrac12}✓✓$$
$$\text{记}\ \theta_j：z_j=e^{i\theta_j},\quad f(k):=\sum_j\cos(k\theta_j)✓$$
$$\text{已知}：M=1\ \text{已证（引理 C，初等覆盖）};\ M=2\ \text{数值饱和}\approx0.506;\ M\ge3\ \text{数值}\ \textbf{增长}✓$$

## §2 ⭐ Case A 引理（**已严格证明**）

$$\textbf{引理（Case A）}：\text{设}\ \delta\le\pi/6，\ m:=\#\{j:\mathrm{dist}(\theta_j,\pi\mathbb Z)\le\delta\}.\ \text{若}\ m\ge\frac{2M}{3}+\frac13，\ \text{则}\ f(2)\ge\frac12✓✓$$

**证明**（三行）
$$①\ \text{对}\ j\in A：\theta_j=\pi n_j+x_j,\ |x_j|\le\delta \Longrightarrow \cos(2\theta_j)=\cos(2x_j)\ge\cos(2\delta)\ge\cos\frac\pi3=\tfrac12✓$$
$$\qquad (\text{用}\ \cos(2(\pi+x))=\cos(2x)\ \text{，即}\ k=2\ \text{下}\ \theta\ \text{与}\ \theta+\pi\ \textbf{同相}✓✓)$$
$$②\ \text{对}\ j\notin A：\cos(2\theta_j)\ge-1✓$$
$$③\ \text{故}\ f(2)\ \ge\ m\cdot\tfrac12+(M-m)\cdot(-1)=\tfrac32m-M\ \ge\ \tfrac32\Big(\tfrac{2M}{3}+\tfrac13\Big)-M=\tfrac12✓✓$$

$$\text{（}\delta\le\pi/6\ \text{的用处}：\text{保证}\ |2x_j|\le\pi/3 \Longrightarrow \cos\ge\tfrac12；\ \text{若}\ \delta\ \text{更大可改取别的偶}\ k\ \text{或}\ \text{用}\ \cos\ \text{的连续性}✓）$$

## §3 ⚠️ Case B 是硬核（本档定位）

$$\textbf{Case B}：\ m<\tfrac{2M}{3}+\tfrac13 \quad(\text{即}\ \textbf{少点}\ \text{近}\ 0\bmod\pi)✓✓$$
$$\text{数值事实}：M=2\ \text{的极值配置}\ (60^\circ,90^\circ)：\mathrm{dist}(60^\circ,\pi\mathbb Z)=60^\circ,\ \mathrm{dist}(90^\circ,\pi\mathbb Z)=90^\circ \Longrightarrow \textbf{属 Case B}✓✓$$
$$\qquad \text{且该配置}\ \max_k f(k)=\tfrac12\ \textbf{恰饱和} \Longrightarrow \text{目标常数}\ \tfrac12\ \text{是}\ \textbf{紧} \text{的}✓✓$$
$$\Longrightarrow\ \text{任何}\ (\text{RP}_M)\ \text{的证明必须在 Case B 上}\ \textbf{锋利} \text{（不能有损失）}✓✓$$

## §4 两条路线的 Case B 现状（诚实）

$$\text{路线①（计数／鸽笼）}：\text{已证}\ \textbf{不足}：\text{粗界}\ f(k)\ge\tfrac32n_k-M\ \text{需}\ n_k\ge\tfrac{2M}{3}+\tfrac13；\ \text{鸽笼仅给}\ M/5✓$$
$$\qquad \text{本档补充}：\text{按}\ k\ \text{平均}：\overline{n_k}\approx M/3 \Longrightarrow \text{计数路线}\ \textbf{对大}\ M\ \text{结构性失败}✓✓$$
$$\text{路线②（二阶矩）}：\text{数值余量}\approx M\ \text{倍}（\text{`C-143`}）；\ \text{但}\ \textbf{可证} \text{版本需}\ \delta\text{-控制}✓$$
$$\qquad \text{即}：\text{Case B 中}\ \text{cross 项}\ D_K(\theta_j\mp\theta_l)\ \text{需在}\ \theta_j\approx\pm\theta_l\ \text{时被控}✓✓$$

## §5 下一步（**Case B**，不再规划）

$$\text{①}\ \text{把 Case B 再二分}：\text{B1（近反相）}\ \exists j\ne l:\theta_j+\theta_l\approx0；\ \text{B2（一般位置）}✓$$
$$\qquad \text{B1 的机制}：z_j\approx\overline{z_l}\Longrightarrow \mathrm{Re}(z_j^k+z_l^k)\approx2\cos(k\theta_j)\ \text{（}\textbf{同相相加}）\ \text{——}\ \text{可用引理 C 直接逼近}✓✓$$
$$\text{②}\ \text{B2 用二阶矩＋分离控制，目标是}\ \sum_kf(k)^2>K/4✓$$
$$\text{③}\ \text{数值先行}：\text{对}\ M\le11\ \text{逐}\ M\ \text{验证}\ \min Q>K/4\ \text{的}\ \textbf{可证下界} \text{（用区间算术，非启发式搜索）}✓$$

## §6 边界与回查

- ⚠️ §2 为**本档严格证明**（三行可逐行核；`\delta\le\pi/6` 的常数可调）✓
- ⚠️ §4 的"计数路线对大 `M` 结构性失败"为**本档分析**（`\overline{n_k}\approx M/3` 为渐近密度）✓
- ⚠️ **未证** Case B；**不声称** `(RP_M)` 已成 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:2x）`[纪律]`（先跑后写）

```
技术词 偶数对齐   命中文件数=0 ::  ⟹ 本档新增
技术词 共振角    命中文件数=0 ::  ⟹ 本档新增
技术词 Case A 引理 命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
