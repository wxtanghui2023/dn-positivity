已查地图：命中（`LEMMA-R-P1-CLOSED-prior-art-and-three-gate-correction`（其 §4 即 R2 硬门）／`TOOLCHAIN-REAUDIT-independent-theorem-capacity`）⟹ 引用，不开新案
D0: 本档对象 = `R2` 判定 **CLOSED / PRIOR ART**（硬门触发）＋ 登记新筛选门 **E-gate** ＋ 三线收口表 ＋ 提高筛选门槛
D1: 0 （[REVIEW] 轮次：判定与登记，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`R2` CLOSED（prior art）＋ 新硬门 `E-gate`**

## §1 ⭐ `R2` 判定：CLOSED / PRIOR ART（硬门触发）

```
【问题】 `R2`：对给定奇异值谱，**等号面的几何结构/维数**是否有新的、可独立验证的分类？✓
【核查结果】 **(i)** Frobenius 形式等号条件＝**存在共同 `U,V`**：$$\|X-Y\|_F=\|\Sigma(X)-\Sigma(Y)\|_F\iff X=U\Sigma(X)V^*,\ Y=U\Sigma(Y)V^*$$（Horn–Johnson／MathOverflow 整理）✓；**(ii)** **Carlsson 2021** 核心即证"等号必共享 joint singular vectors"（Lund 条目）✓；**(iii)** 后续文献 corrigendum 直接引 **Theobald 的 equality-case 结果**为现成工具 ✓✓
【⟹ 维数层面也无缺口】 固定谱后共同 SVD 的自由度本质上是 $$(U,V)\sim(UG_L,VG_R)$$ 其中 `G_L,G_R` 仅在**共同奇异子空间内**作正交变换、并保对角块 ⟹ 所谓"等号面维数"＝ **(1)** 各重根子空间的 `O(m)` 自由度＋**(2)** 商去同一 SVD 表示的稳定子群＋**(3)** 零奇异子空间的额外自由度 ＝ **群作用/商空间计数问题** ✓✓
【⟹ 硬门触发】 依我方自查硬门："只得到**正交群商空间维数** ⟹ CLOSED" ⟹ $$\boxed{R2=\text{CLOSED / PRIOR ART}}$$ ✓✓ **不得包装为 OPEN** ✓
```

## §2 ⭐⭐ **新硬门 `E-gate`（照录，本档登记）**

```
$$\boxed{\text{若新量只描述\textbf{已知等号面的参数化/维数}\ \Longrightarrow\ CLOSED}}$$ ✓✓
【适用形态（高危信号）】 目标量为：**equality set**／**equality manifold dimension**／**multiplicity-block freedom**／**stabilizer‑quotient dimension** ⟹ **极大概率只是经典等号定理的几何展开** ✓
【放宽条件（只有满足其一才继续）】 **(a)** 新量是**此前不存在的可计算不变量**；**(b)** 能产生**新的独立极值问题** ✓
【配套门槛提高（照录）】 **不得从"某个经典不等式的 equality case"出发** —— 该类问题易得到"漂亮、完整、可证、但无新性"的结果 ✓✓
```

## §3 三线收口表

| 方向 | 状态 | 留存资产 |
|:--|:--|:--|
| **`EDS/CAP`** | **CLOSED** | 最小反例 `B_5=2,\ B_{10}=4`（`S=\{2\}`，`T=\{5,10\}`）；**`(A1)+(A2)` 不可推出成链引理的抽象模型** |
| **`Lemma R / P1`** | **CLOSED / PRIOR ART** | `P=X\odot Z` 次随机坐标；**`G1/G2/G3` 等号审计** |
| **`Lemma R / R2`** | **CLOSED / PRIOR ART** | 等号面＝共同 SVD 的重根自由度/商空间参数化 |

```
【⟹ 处置】 **不在 `Lemma R` 上投入第二轮** ✓；下一步遵守 $$\boxed{\text{独立问题}>\text{邻近资产}>\text{RH 相关性}}$$ 且**先用 `E-gate` 过筛** ✓✓
【边界】 §1 三条 anchors 为档级（未逐字核原文）；§1 维数论证、§2 `E-gate`、§3 表为**照录您的裁示/本档登记**；未制造候选／未启动搜索／未碰 RH。
