已查地图：命中（`LEMMA-R-P1-equality-classification`（本档更正其"一句话定理"）／`TOOLCHAIN-REAUDIT-independent-theorem-capacity`）⟹ 引用，不开新案
D0: 本档对象 = `P1` 判定 **CLOSED / PRIOR ART**（锚 `Carlsson 2021`）＋ 技术更正（**三道 gate**）＋ 保留 `proof-technology` 资产 ＋ 登记 `R2` 及硬门
D1: 0 （[REVIEW] 轮次：判定与更正，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`Lemma R / P1`：CLOSED / PRIOR ART（附技术更正）**

## §0 ⚠️ 更正我前档的"一句话定理"（本档）

```
【我前档写的】 "等号 `\iff|P|` 在同值块矩形上双随机、块外为零；零块自由" ⟹ **不充分** ✗
【原因（照录您的修正）】 我定义 `P=X_{ij}Z_{ij}`，但赋值问题用的是 `|P_{ij}|`；而 `\sum_j|X_{ij}Z_{ij}|\le1` 的**等号本身还含 Cauchy–Schwarz 等号条件** ⟹ $$\boxed{\text{assignment equality}\ \ne\ \text{full matrix equality}}$$ 中间还有一道 **CS 饱和 gate** ✓✓
```

## §1 ⭐ **正确的三道 gate（本档定稿）**

```
$$\text{trace equality}\ \Longrightarrow\ \begin{cases}\textbf{G1 符号/绝对值饱和} & P_{ij}\ge0\ \text{于 }\sigma_i\sigma_j>0\text{ 的支撑上}\\\textbf{G2 CS 饱和} & |X_{ij}|\propto|Z_{ij}|\ \text{（行/列）且行范数饱和}\\\textbf{G3 赋值饱和} & |P|\ \text{集中在同值块矩形、块内行/列和}=1\end{cases}$$
**三者合起来才推出公共左右奇异向量** ✓✓（我前档只做到 G3，缺 G1/G2 ⟹ 结论形式过强）✓
```

## §2 正式判定：`P1` = CLOSED / PRIOR ART

```
【定理（已证，非我方新）】 `\operatorname{tr}(A^TB)=\sum_i\sigma_i(A)\sigma_i(B)` `\iff` 存在正交 `U,V` 使 $$A=U\Sigma_A V^T,\qquad B=U\Sigma_B V^T$$（谱按同向递减）✓
【prior-art 锚】 **Carlsson 2021, "von Neumann's trace inequality for Hilbert–Schmidt operators"**（Lund University 记录）：**专门把"等号必共享 joint singular vectors"作为核心证明** ✓✓
【其余对照】 MathOverflow 相关条目；Frobenius/Mirsky 等价形式 `X=U\Sigma(X)V^*,\ Y=U\Sigma(Y)V^*` ✓
【⟹ 我方贡献性质】**不是新等号现象**，而是该经典结论的一种**显式次随机矩阵坐标**（`P=X\odot Z`）与**三 gate 分解** ✓
【判定】 $$\boxed{P1=\text{CLOSED / PRIOR ART}}$$ —— **不得把"块版"升格为 OPEN** ✓✓
```

## §3 保留资产：`proof-technology`（可复用，但非定理）

```
$$\langle A,B\rangle_F=\langle a,(X\odot Z)b\rangle,\qquad \|P_{i,:}\|_1\le1,\ \|P_{:,j}\|_1\le1\ \ (P=X\odot Z)$$
⟹ 迹不等式被压缩为**次随机约束下的最优赋值**；**等号审计＝G1/G2/G3** ✓
【用途】 遇到**非标准 trace inequality**（把 `X_{ij}Z_{ij}` 换成别的耦合量）时，可作**筛选模板** ✓；**对 `Lemma R` 本身不是新结果** ✓
```

## §4 登记 `R2` 及其硬门（不经硬门不得开）

```
$$\boxed{R2:\ \text{对给定奇异值谱，等号面的几何结构/维数是否有新的、可独立验证的分类？}}$$
【硬门（照录）】 若 `R2` 最终只归结为"**等号面维数 ＝ 若干正交群商空间维数**"（即经典 equality theorem 的直接推论）⟹ **立即 CLOSED** ✓✓
【只有出现经典等号定理未给出的、可独立验证的量，才继续** ✓
【边界】 §0 更正、§1 三 gate、§4 硬门为**照录您的修正/裁示**；§2 判定为**本档登记**；未制造候选／未启动搜索／未碰 RH。
