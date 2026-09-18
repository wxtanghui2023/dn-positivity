已查地图（**先查后写**，唐先生 21:25「印象中这个也分析过，你先搜索」⟹ **先搜，命中**）：`acpc-minimal-test.md`（2026-09-03 10:55：加性卷积 A / 乘性卷积 M / 逐点积 C 的最小模型）、**`acpc-loop-death.md`（2026-09-03 11:05：ACPC A×M×A 闭环 κ 连通量测试 —— 链退化，判死）**、`euclid-k2-death.md`（Σ Λ(n)Λ(m)F_s(nm)：只依赖 nm ⟹ Mellin 化 ⟹ 旧机制换坐标 ⟹ 判死；DS ＝ (ζ'/ζ)² ⟹ Euler 结构完全塌缩）、`iib-boundary-probe.md`（乘性卷积的 Mellin 表示天然在 Re＝½ 轮廓；风险＝轮廓移动＋留数 ⟹ 靠近显式公式死线）、`B-candidate-space-analysis.md`（~40+ 路线死亡原因反推）、`C76`／`C83`（筛权重判据：换权重不够）、`V254`（典范带符号加权阈值＝β_*）。**结论**：⭐ **候选 E（Dirichlet 卷积变形）不是新路——它是两条已判死的旧路** ✓✓：(甲) **乘性卷积**（Λ*Λ 等）⟹ DS ＝ (ζ'/ζ)^k ⟹ **Euler 结构塌缩**（`euclid-k2-death`）；(乙) **ACPC 线**（加性卷积 A×乘性卷积 M×逐点积 C）⟹ 已被 **`acpc-loop-death` 判死**，死因是 **链退化（κ_k ≈ log(1+L1·t) 的平凡系数；L2/L1² 从 4e-6 降到 1.9e-7）**，且**不是退化成欧拉积，而是退化成"单块配分"** ✓✓；**关键**：ACPC 死的**正是本会话新立的第 (iii) 条**（极限恢复零结构）⟹ **第 (iii) 条现有两个独立见证（ACPC 链退化 ＋ 候选 C 截断）** ✓✓

FREEZE-ACK: 本档即冻结期内的查图与判词登记（依 `§8.1`；不产候选结论）

D0: 本档对象 = 候选 E 的**已在档死亡记录**（ACPC 线 ＋ 乘性卷积线）—— 关系 = **查重命中已判死路线**，非新机制
D1: 0

# CREATE-SPEC-3 · **候选 E 的讣告：ACPC 线已判死，且死于本会话新立的第 (iii) 条**

> **时间**：2026-09-18 21:25 唐先生：**「印象中这个也分析过，你先搜索」** ⟹ **先搜，命中** ✓

---

## §0 结论（先行）

$$\boxed{\textbf{候选 E 不是新路，是两条已判死的旧路}}✓✓$$
$$\qquad \text{(甲)}\ \textbf{乘性卷积}（\Lambda*\Lambda\ \text{等}） \Longrightarrow \text{DS}＝(\zeta'/\zeta)^k \Longrightarrow \textbf{Euler 结构塌缩}（\text{`euclid-k2-death`}）✗$$
$$\qquad \text{(乙)}\ \textbf{ACPC 线}（\text{加性卷积} A\times\text{乘性卷积} M\times\text{逐点积} C） \Longrightarrow \textbf{已判死}（\text{`acpc-loop-death`},\ 2026\text{-09-03}）✗$$
$$\Longrightarrow ⭐\ \textbf{ACPC 死的正是本会话新立的第 (iii) 条}（\text{极限恢复零结构}） \Longrightarrow \textbf{第 (iii) 条现两个独立见证}✓✓$$

---

## §1 `acpc-loop-death` 的逐字判词（决定性）

$$\text{定义（唐先生固定方案）}：A(n)=\sum_{a+b=n}\Lambda(a)\Lambda(b);\quad L_1=\sum_{qm\le X}\Lambda(q)\Lambda(m)A(qm)A(m);\ \dots$$
$$\qquad \kappa_1=L_1,\quad \kappa_2=L_2-\tfrac12L_1^2,\quad \kappa_3=L_3-L_1L_2+\tfrac13L_1^3✓$$

$$\text{数值（}X=10^4,3\times10^4,10^5,3\times10^5\text{）}：\kappa_2/L_2\ \text{增长到}\ -5.3\times10^6;\quad L_2/L_1^2:\ 4\times10^{-6}\to1.9\times10^{-7}\ \textbf{持续下降}\to0✓$$

$$\textbf{判死逐字}：\qquad \text{"**}\kappa_k\approx\log(1+L_1t)\ \text{的平凡展开系数}\text{"};\qquad \text{"}\textbf{连通化无多体结构}\text{"}✓✓$$
$$\qquad \text{"}\textbf{ACPC 闭环（链部分）判死}：\text{不是退化为 Euler 积}——\text{是退化为"}\textbf{单块配分}\text{"（}L_1\text{）}——\text{链不可达}——\kappa\ \text{平凡}\text{"}✓✓$$
$$\qquad \text{机制}：\text{"A}\times\text{M}\times\text{A 链极稀疏（}\text{k 链需 k+1 个素幂乘积}\le X——\text{指数稀）"}\ \Longrightarrow \text{闭环从不共享中间}\ m✓$$

## §2 ⭐ 与四条款规格的对位（关键）

| 条款 | ACPC／候选 E 的满足情况 |
|:--|:--|
| **(i)** 算术的（非坐标）| ✓（A、M 皆算术卷积）|
| **(ii)** 无欧拉积仍可定义 | ⭐ ✓✓（**A 的 DS 无 Euler 积** —— a+b=n 约束不可因子化）|
| **(iii)** 极限恢复零结构（钉点）| ✗✗ **死在此**（κ 平凡、链退化 ⟹ **极限不恢复任何零点信息**）|
| **(iv)** 作用于有零点的因子 | ⚠️ 部分（M 的 DS＝(ζ'/ζ)² 有谱；但 A 侧无零点结构）|

$$\Longrightarrow \textbf{ACPC 是迄今}\ \textbf{唯一在 (i)(ii) 上真通过的候选} \Longrightarrow \text{却}\ \textbf{恰好死在 (iii)}✓✓$$
$$\qquad (\text{候选 C 亦死 (iii)}：\text{部分和零点不收敛}) \Longrightarrow \textbf{(iii) 为最硬条款，两见证}✓✓$$

## §3 附加死线（同族，已在档）

$$\text{`euclid-k2-death`}\ \textbf{逐字}：\text{"}W_s(n,m)\ \text{只依赖}\ nm \Longrightarrow \text{按唐先生判据 B（依赖}\ nm\ \text{可 Mellin／Fourier 化——旧机制换坐标——）}\textbf{判死}\text{"}✓✓$$
$$\qquad \text{"}\Sigma_{n,m}\Lambda(n)\Lambda(m)F_s(nm)=\Sigma_PF_s(P)(\Lambda*\Lambda)(P)——\text{乘性卷积}——\text{DS}=(\zeta'/\zeta)^2——\textbf{Euler 结构——完全塌缩}\text{"}✓✓$$
$$\text{`iib-boundary-probe`}\ \textbf{逐字}：\text{"乘性卷积的 Mellin 表示天然在}\operatorname{Re}=\tfrac12\ \text{轮廓（Parseval）；}\ \textbf{风险：轮廓移动＋留数＝Mellin 变换技巧——靠近显式公式（死线）}\text{"}✓$$

## §4 本会话的第三次"已提出已在档"（诚实登记）

$$\text{第一次}：\text{M1 hereditary} \Longrightarrow \text{与 N46 对齐审计（后发现为正交，但先被要求查）}$$
$$\text{第二次}：\text{free-probability（FZ-2 未测项）} \Longrightarrow \text{实为 FZ-2 表中已列}$$
$$\text{第三次}：\text{候选 E（卷积变形）} \Longrightarrow \textbf{ACPC／乘性卷积两条已判死路线}$$
$$\Longrightarrow ⚠️\ \textbf{模式}：\text{我的"构造"}\ \textbf{反复落在已登记材料上} \Longrightarrow \text{这是"构造空间确已被扫过"的}\ \textbf{证据}（\text{非证明}）✓✓$$
$$\qquad \text{教训（已在 TOOLS.md 立规）：}\textbf{提任何"新"构造前，先把定义译成档案最可能用的词再搜}✓✓$$

## §5 边界与回查

- ⚠️ 本档**只做查图与判词登记**；**不产候选**、**不改任何判词** ✓
- ⚠️ §2 的对位表为**本档做法**（把 ACPC 对到四条款上），**非原文主张** ✓
- ⚠️ `acpc-loop-death` 的剩余记录（逐字）："L1（单闭环量）本身未判——但它只是'单块和'……唐先生方案的核心（链→log→κ）已死（链退化）" ⟹ **L1 未判** 为**已登记的开口**✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 21:2x）`[纪律]`（先跑后写）

```
技术词 链退化           命中文件数=2  :: ./acpc-loop-death.md（**已有**）
技术词 单块配分          命中文件数=2  :: ./acpc-loop-death.md（**已有**）
技术词 构造空间已扫       命中文件数=1  :: ./CREATE-SPEC-3-…（本档）
```
**读数（按实测）**：⚠️ `链退化`／`单块配分`＝**2 档**（`acpc-loop-death` **已有**）⟹ 本档为**沿用**（且正因如此，本档所引判词为**原档术语**）；`构造空间已扫`＝**1 档（仅本档）⟹ 本档新增** ✓
