已查地图：命中（`TOOLCHAIN-REAUDIT-independent-theorem-capacity`（`Lemma R` 列为候选 2）／`EDR-P1-P3-nailed-down`）⟹ 引用，不开新案
D0: 本档对象 = `Lemma R` 的 `P1`：von Neumann 迹不等式等号分类（`P1-A` 简单谱 ＋ `P1-B` 重根/零块）＋ prior-art 标注
D1: 0 （[REVIEW] 轮次：推导与标注，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`Lemma R` / `P1`：von Neumann 迹不等式等号分类**

## §1 精确表示（推导起点，本档）

```
`A=U_A\Sigma_A V_A^T`、`B=U_B\Sigma_B V_B^T`；令 `X:=U_A^TU_B`、`Z:=V_A^TV_B`（均正交）⟹
$$\operatorname{tr}(A^TB)=\sum_{i,j}\sigma_i(A)\sigma_j(B)\,X_{ij}Z_{ij}=\sum_{i,j}\sigma_i(A)\sigma_j(B)\,P_{ij},\qquad P_{ij}:=X_{ij}Z_{ij}$$ ✓
【关键性质】**`P` 是"次随机"的**：由 Cauchy–Schwarz $$\sum_j|P_{ij}|\le\sqrt{\sum_jX_{ij}^2}\sqrt{\sum_jZ_{ij}^2}=1$$ ⟹ 行/列绝对和 `\le1` ✓✓
```

## §2 `P1-A`：简单谱（**等号 ⟺ `|P|=I`**）

```
【推导】 `\operatorname{tr}\le\sum_{i,j}\sigma_i(A)\sigma_j(B)|P_{ij}|`（取绝对值）＋ 次随机矩阵的**重排引理** ⟹ `\le\sum_i\sigma_i(A)\sigma_i(B)` ✓
【等号条件】 若 `\sigma_i(A),\sigma_j(B)` 均**严格递减且为正** ⟹ 唯一达到最优的支撑是 `|P|=I` ⟹ $$|X_{ij}Z_{ij}|=\delta_{ij}$$ ⟹ **奇异向量逐对对齐** ✓✓
【⟹ 命题（`P1-A`）】 等号 `\iff` 存在公共正交对 `(U,V)`：$$A=U\Sigma_A V^T,\quad B=U\Sigma_B V^T$$ ✓（充分性显然）
```

## §3 ⭐⭐ `P1-B`：重根 ＋ 零奇异值块（本档主结果）

```
【把重根写成块】 `\sigma(A)` 按**相异值**分成递降块 `J^A_1,J^A_2,\dots`（同块内值相等）；`\sigma(B)` 同理 `J^B_1,\dots` ✓
【等号条件（精确形式）】 由赋值问题 `\max\sum c_{ij}q_{ij}`（`c_{ij}=\sigma_i(A)\sigma_j(B)`，超模成本）**最优面＝单调（NW）结构** ⟹ 等号 `\iff`
　**(a)** `|P|` 的支撑落在 `\bigcup_k\bigl(J^A_k\times J^B_k\bigr)`（**同层块矩形**）之内 ✓
　**(b)** 在每个矩形内 `|P|` 的行和与列和**均恰为 1**（即块内为双随机），且块间无质量 ✓
【零奇异值块（特例）】 `\sigma_i(A)=0` 的指标：`c_{ij}=0` 对一切 `j` ⟹ **零块可与任意块自由混合**，不影响等号 ✓✓（即 `\operatorname{rank}` 亏缺部分的奇异向量完全自由）
【⟹ 一句话定理】 $$\boxed{\text{等号}\iff |P|\ \text{在"同值块矩形"上双随机、块外为零；零块自由}}$$ ✓✓ —— 等价的几何说法：**等号 ⟺ 两个矩阵的奇异子空间在"同值层"上可以同时对齐**（层内可任意旋转，跨层不可混合）✓
```

## §4 ⚠️ prior-art 标注（必须先过 gate，再谈独立命题）

```
【风险】 von Neumann 迹不等式的**等号条件**是矩阵分析的**经典题目**（Bhatia《Matrix Analysis》系与量子信息文献常用）⟹ **§2/§3 很可能已知** ⚠️⚠️
【⟹ 处置】**先做 30 分钟文献核查**（"equality case von Neumann trace inequality singular value alignment"）⟹ 若已知 ⟹ `P1` **记为 CLOSED（已知）**，不主张新性 ✓；若只到简单谱、未含**块/零块精确形式** ⟹ 只看"块版"是否构成**新内容**再议 ✓
【⚠️ 对比前车】 本线已因 prior-art 撞车关掉 `I`（DH parity）与 `B-1` ⟹ **不重蹈"先做后查"** ✓✓
【边界】 §1 表示与 `P` 的次随机性、§2 推导、§3 块/零块定理为**本档自行推导**（初等，可手核）；§4 风险标注为**本档判断**；未制造候选／未启动搜索／未碰 RH。
