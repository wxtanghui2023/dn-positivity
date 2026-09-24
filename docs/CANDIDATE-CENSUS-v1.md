已查地图：命中（`RESEARCH-CONSTITUTION` `AMEND-15`）⟹ 本档为其 `S1`（Candidate Factory）第一批，不开新案
D0: 本档对象 = **`Candidate Census v1`**：按 `AMEND-15` 的 `Asset×Object×Quantity×PropType` 矩阵，从 `A/B/D/E/F/G` 出发、跨 **12 个对象族**生成 **100 条具体可证伪候选**，并给 `S2` **初判**（`COVERED/PARTIAL/UNVERIFIED`）
D1: 1（首次大批量候选生成；产出 100 条候选池）
[RESEARCH]

# **`Candidate Census v1`（100 条）**

## §0 口径（照 `AMEND-15`）

```
$$\texttt{S0}\ \text{资产}\to\text{可测量量}\to\text{可变参数}\to\text{候选};\quad \texttt{S1}\ \textbf{故意过生产};\quad \texttt{S2}\ \textbf{仅三态}:\ \texttt{COVERED}/\texttt{PARTIAL}/\texttt{UNVERIFIED}$$ ✓
$$\texttt{C1}\ \text{精确值};\ \texttt{C2}\ \text{极值};\ \texttt{C3}\ \text{唯一/分类};\ \texttt{C4}\ \text{边界};\ \texttt{C5}\ \text{反例};\ \texttt{C6}\ \text{二阶/误差};\ \texttt{C7}\ \text{参数族};\ \texttt{C8}\ \text{结构条件}$$ ✓
$$\boxed{\texttt{PARTIAL}\ \text{不得 }REJECT};\quad \boxed{\texttt{UNVERIFIED}\ \text{不得写作"新"}};\quad \text{本档 }S2\ \text{为\textbf{初判}（未批量核验）}$$ ⚠️
```

## §1 候选矩阵（`Asset×Object×Quantity×PropType`；照 `AMEND-15` §4）

```
$$\begin{array}{c|c|c|c}
\text{Asset}&\text{Object}&\text{Quantity}&\text{典型 }PropType\\
\hline
A&\text{群／图／排列／设计}&\text{计数／轨道／交}&\texttt{C1,C2,C3}\\
B&\text{格／码／有限域}&\text{密度／容量／能量}&\texttt{C1,C2,C4}\\
D&\text{全部}&\text{精确值／证书}&\texttt{C1,C5}\\
E&\text{图／矩阵}&\text{秩／惯性／重数}&\texttt{C1,C2,C3}\\
F&\text{有限域／递推}&\text{阶／周期／可分性}&\texttt{C1,C7}\\
G&\text{组合系统／动力}&\text{最小障碍／周期}&\texttt{C3,C5,C8}\\
\end{array}$$ ✓
```

## §2 100 条候选（按 12 族；`S2` 初判：`U`=未核，`P`=部分，`C`=已覆盖）

```
**【F1 有限群】（A,D,E）**
G01 阶 n≤512 中**非超可解**精确个数与最小反例序列 — U
G02 固定 n≤2000 下**自同构群阶**的精确分布 — U
G03 小阶 n≤1000 下**极大子群指数**缺失值完整清单 — U
G04 S_n (n≤12) 中指定型子群（A₅, S₄…）的**共轭类个数** — U
G05 小群中 |H ∩ gKg⁻¹| 的**精确分布** — U
G06 n≤256 阶群的**生成元对数最小值**与达到者分类 — U
G07 阶 ≤3⁷ 的 p-群中 **Frattini 指数**分布 — U
G08 小阶群**特征标表**上独立量的极值 — U

**【F2 图】（A,E,D）**
Gr01 n=8 图的 **inertia 集完备表** — U/P（已解阶阈值待核）
Gr02 n=9 图的**最小秩**精确分布 — U
Gr03 n=11 下**最大特征值重数**极值图分类 — U
Gr04 三次图 n≤12 的 **zero forcing number** 精确极值 — U
Gr05 n=9 下**同谱类大小**精确分布 — U
Gr06 n=9 下给定 inertia 三元组 (p,q,z) 的**存在性完整表** — U
Gr07 小阶 **rank defect** 极值与达到者 — U
Gr08 n≤10 下 **slope（正则化 Laplacian）**取值集合 — U
Gr09 小阶**图能量**（等数值不变量）极值与唯一性 — U
Gr10 n≤10 下**给定惯性且极小秩**的图的计数 — U

**【F3 排列】（A,D）**
P01 长度 5 的 Wilf 类在 n=12 的**精确计数** — U
P02 长度 4 模式的（弱）**Wilf 等价类完整分类证书** — U/P
P03 递降集给定时的 **involutions 计数**精确公式之反例搜索 — U
P04 **循环递降最大值**的排列个数 — U
P05 n≤13 下 avoiding **两模式**的计数（未列表格） — U
P06 **完美洗牌分解**最短长度极值 — U
P07 n≤12 下置换 Cayley 图**直径**精确值（特定生成集） — U
P08 n≤11 下 **LIS 分布**的精确尾部 — U

**【F4 格与球堆积】（B,D,E）**
L01 维 9–11 **特定格族**堆积密度精确值/最优性 — U/P（8,24 维已解）
L02 给定指数下**极小行列式子格**的分类与计数 — U
L03 维 10–11 **kissing 数**可达上界改进 — U/P
L04 **BW/Leach 覆盖半径**精确值 — U
L05 小指数子格**最短向量个数**精确统计 — U
L06 维 ≤12 下 **unimodular 格**不变量极值 — U
L07 给定 minimum 下 **theta 级数系数**极值 — U
L08 维 ≤10 下**格自同构群阶**极值与分类 — U

**【F5 编码】（A,B,D）**
C01 覆盖码 K_q(n,R) 若干**未收割单元**的界改进（先筛格） — U
C02 ℓ₂(n,2) 在 n∈{39,…,44} 的精确/改进界 — U
C03 小参数 **A(n,d)** 未列表格的精确值 — U
C04 特定 BCH 码**覆盖半径**精确值 — U
C05 小码 **list-decoding radius** 精确值 — U
C06 固定 n 下**最优码非同构个数** — U
C07 q-ary 小参数 **covering radius** 表缺口 — U
C08 给定参数下 **weight distribution 唯一性** — U
C09 小 n 下**最小距离的谱**（达到者分类） — U

**【F6 多项式与根】（D,F,A）**
Po01 三项式 xⁿ±xᵐ±1 的**整数根型完整分类**（n≤40） — U
Po02 xⁿ−1 在 F₂ 上按次数分解的**精确计数**（n≤100） — U/P
Po03 给定 trace 的**不可约多项式计数**（小 q,n） — U
Po04 次数 ≤30 三项式的 **Galois 群分布** — U
Po05 多项式理想中**最小 Hamming 重量** — U
Po06 有限重**单位根消去和**极小重量分类 — U/P
Po07 小 n 下**不可约二项式**存在性完整表 — U
Po08 给定判别式的**整系数多项式计数**（小范围） — U

**【F7 有限域】（F,B,A）**
FF01 指数 m∉{2,3,4} 的**精确 λ（Q1''）** — U（无经典闭式区）
FF02 q=2^k 的**五次分圆数**精确值 — U/P
FF03 给定 trace 的**本原元计数**（小 q） — U
FF04 **最小本原根**分布极值（小范围） — U
FF05 受限特征和**取值集合**（小参数） — U
FF06 小 q 下**子群∩平移**完整表（基准） — P（经典理论仅渐近）
FF07 小 q 下**乘法子群作为 cap** 的完整分类 — U/P
FF08 给定 n 下**不可约多项式最小 weight**谱 — U
FF09 小 q 下**指数 m 子群的加法能量**精确值 — U

**【F8 递推与序列】（F,D）**
R01 EDS 指数集 |T(S)|>|S| 的**小范围完整分类** — U
R02 线性递推 mod m **周期精确分布**（小 m） — U
R03 Fibonacci mod m **Pisano 周期**计数表缺口 — U/P
R04 给定周期的 m 的**精确计数** — U
R05 递推中**零和模式**极值 — U
R06 小范围下**整除猜想的极小反例** — U
R07 **rank of apparition** 分布精确统计 — U
R08 给定参数 **k-正则序列**分类小例 — U

**【F9 设计/配置】（A,D）**
D01 覆盖设计 C(v,k,t) 未收割单元精确值 — U
D02 小 (v,k) 下 **Steiner 系统存在性**表缺口 — U/P
D03 给定参数**非同构设计个数** — U
D04 2-(v,k,λ) **packing 数**表缺口 — U
D05 小 v **正交阵列**存在性表 — U/P
D06 给定参数**差集**存在性小例分类 — U
D07 **Turán 型小超图极值数**未收割格 — U
D08 **AG(7,3) 最大 cap** 精确值（T-2 遗留） — U/P

**【F10 矩阵与谱】（E,D）**
M01 特定结构矩阵族 n≤30 **秩亏精确值** — U
M02 参数化族 **PSD 阈值**精确刻画 — U
M03 n=5 **SNIEP 整谱可实现性**完整表 — U
M04 小尺寸 (0,±1)-矩阵 **rank 分布** — U
M05 小尺寸 **sign-rank vs rank** 极值差 — U
M06 给定惯性**最小秩矩阵计数** — U
M07 小尺寸 **totally positive 矩阵**计数极值 — U
M08 特定族**特征值重数**极值与唯一性 — U

**【F11 拟阵/偏序/组合系统】（A,G）**
Mt01 n≤9 元素**非同构拟阵个数**表缺口 — U
Mt02 给定参数**不可表示拟阵**最小例 — U/P
Mt03 特定有限偏序族**最大反链** — U
Mt04 小阶**格的表示数**极值 — U
Mt05 给定 hypergraph **minimal obstruction** 尺寸分类 — U
Mt06 小阶 STS 相关系统**自同构群阶分布** — U
Mt07 **Ramsey 型小参数**未收割格 — U
Mt08 小阶**拟阵 Tutte 多项式**唯一性/反例 — U

**【F12 自动机与离散动力】（G,D）**
Au01 小自动机 **Černý 型最短同步字**精确值 — U/P
Au02 宽度 n≤20 特定 CA 规则**周期分布** — U
Au03 n=5 布尔函数**吸引子计数**分布 — U
Au04 小布尔网络**暂态长度**极值 — U
Au05 小正则网络**极限环**极值 — U
Au06 特定类 **Collatz 型停时记录**（有界域） — P
Au07 小自动机**最小 DFA 计数**（给定语言类） — U
Au08 给定规则**可逆性阈值**精确刻画 — U
```

## §3 初判计数（诚实标注）

```
$$\textbf{总数}=100;\qquad \text{对象族}=12;\qquad \text{资产覆盖}=A(31),D(\ge60),E(14),B(12),F(15),G(12)\ (\text{可重叠})$$ ✓
$$\textbf{S2 初判}:\ \boxed{U=90},\quad \boxed{P=10},\quad \boxed{C=0}\ (\text{本批}\textbf{不含}已覆盖者;\ \text{已覆盖两例——Sylvester 惯性／指数3分圆数——已在 }AMEND\text{-}14\ \text{回归中拦下，未入池})$$ ✓✓
$$\text{注意}:\ \textbf{全部 }100\ \text{条的 }S2\ \text{均为初判};\ \text{正式核验在第二批（逐条逐字覆盖声明）}$$ ⚠️
```

## §4 下一步（`S2` 批量核验优先级）

```
$$\textbf{先核 30 条}:\ \text{取 }P\ \text{标记者 10 条 ＋ 各族 }U\ \text{中"最可能已有文献"者 20 条};\ \text{核验输出须含：theorem／原文／假设／参数范围／结论／逐项对应}$$ ✓
$$\text{若某条被判 }\texttt{COVERED}\ \Longrightarrow\ \text{移出池};\ \text{若 }\texttt{PARTIAL}\ \Longrightarrow\ \text{保留并记录部分覆盖};$$
$$\text{若 }\texttt{UNVERIFIED}\ \Longrightarrow\ \text{进入 }\texttt{S3}\ (\texttt{A1/A2/A3})$$ ✓✓
$$\textbf{目标}:\ \text{非 }\texttt{COVERED/DUPLICATE}\ \text{者}\ \ge20\ \text{条达 }\texttt{ACTIVE-CANDIDATE}/\texttt{PENDING}$$ ✓
【⛔ 纪律】 本档为**生成＋初判**（零数学计算、零文献批量核验）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §2 的 100 条为**自适应生成**（未清洗）；`Gr01/C01/C02/FF06` 等标 `P` 者依**早期档级信息**，尚未逐字核 ✓

## §附 【技术词回查】（补录）
```
技术词 candidate        命中文件数=125  :: ./candidate-proof-v1.md ./E-38-PRECEDENCE-CHAIN-and-NEXT-ROUND-DISCIPLINE.md ./RIGORIZATION-candidate-proof-v1-D0-implies-RH.md 
技术词 census           命中文件数=17   :: ./C264-beta-sensitive-channel-census-three-gates-zero-candidates-and-the-location-vs-counting-criterion.md ./C3844-level3-entrance-audit.md ./C225-DAp-convergence-audit-six-branch-structure-resolved.md 
```

---

## §5 `S2-30 Final` 状态（2026-09-25，锁档 `docs/S2-30-FINAL-LOCK.md`）

```
C=4 (Gr05, Mt01, R03, Po02)  |  P=17  |  U=9  |  N=30
Direct-cover rate=4/30=13.33%  |  survival=26/30=86.67%
Po02 移出池; Po06 = U + SPEC-REQUIRED; Gr03 = P1(守)
剩余 70 条 S2: 待跑 (iii 阶段); S3 冻结
```

---

## §6 `S2` 批次进度（逐批独立统计；`SPEC` 单列）

```
S2-30  Final : C=4  P=17  U=9   N=30   (锁定)

Batch-1 (F1+F2+F3, 19条): C=0  P1=0  P2=2  P3=3  P4=3  U=11  SPEC=1
             核对 0+2+3+3+11 = 19 OK;  本批无 COVERED
             P2={Gr09,P03}  P3={G03,P02,P07}  P4={G07,P01,P05}  SPEC={P02}

Batch-2 (F4+F5+F6, 18条): C=3  P1=0  P2=3  P3=1  P4=3  U=8  SPEC=6
             核对 3+0+3+1+3+8 = 18 OK
             C={L04,Po03,Po07}  P2={L07,C08,Po04}  P3={L08}  P4={C06,C07,C09}
             U={L02,L05,L06,C04,C05,Po01,Po05,Po08}  SPEC={L02,L06,C04,C05,Po05,Po08}
Batch-3 (F7+F8+F9, 15条): C=0  P1=0  P2=6  P3=0  P4=6  U=3  SPEC=2
             核对 0+6+6+3 = 15 OK;  本批 C=0
             P2={FF04,FF05,FF08,FF09,R01,R05}  P4={R04,R07,D03,D04,D06,D07}
             U={FF01,R06,R08}  SPEC={R06,R08}
Batch-4 (F10+F11+F12, 18条): 待跑

口径（AMEND-17）:
  (1) P4 须为「已覆盖目标对象一部分」的枚举/数据库结果；
      仅存在通用数据库、或我们自己拿数据库跑计算  ⟹ 不构成 P4
  (2) 多标签行最终归入唯一 P 类：取「证据最直接指向目标命题」者
  (3) SPEC-REQUIRED 与 C/P/U 正交，统计单列，不得混入
  (4) S3 冻结
```
