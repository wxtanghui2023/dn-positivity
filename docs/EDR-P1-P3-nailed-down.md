已查地图：命中（`TOOLCHAIN-REAUDIT-independent-theorem-capacity`／`P-a-GATE-VERDICT-CLOSED-and-C-executed`（`r_q`＝rank of apparition 为教科书概念）／`ZF-EDR-2-gapA-dissolved-and-gapB-exact-form`）⟹ 引用，不开新案
D0: 本档对象 = `EDR` 的 `P1`–`P3`：精确定义／最小非平凡实例／所控对象／相邻文献问题／未解余量
D1: 0 （[REVIEW] 轮次：钉死与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`EDR`：`P1`–`P3` 逐项钉死**

## §1 精确定义（钉死）

```
`E/\mathbb Q` 极小 Weierstrass，`P` 非挠，`x(nP)=A_n/B_n^2`（既约），`B_n>0` ⟹ `(B_n)` 为 EDS ✓
$$Z_S(E,P):=\{n\ge1:\ \operatorname{Supp}(B_n)\subseteq S\}$$（`S` 固定有限素数集）✓
**等价刻画（本档补）**：`\operatorname{Supp}(B_n)\subseteq S\iff nP\in E(\mathbb Z_S)` ⟹ $$Z_S(E,P)=\{n:\ nP\in E(\mathbb Z_S)\}$$ ✓✓ —— 即"**`P` 的 `S`-整倍数集**" ✓
【本线结果】 由 `q` 为 `B_n` 的本原素因子 `\iff r_q=n`（`r_q`＝秩出现/rank of apparition）⟹ 固定 `q` 至多对应一个本原指标 ⟹ $$|Z_S(E,P)|\le N_0+|S|$$（`N_0` 来自 Silverman 的本原除子定理）✓
```

## §2 最小非平凡实例（钉死）

```
`E:y^2+y=x^3-x^2-10x-20`（导子 11），`P=(5,5)`，`S=\{2,3\}`：
本线数据 `Z_{\{2,3\}}\cap[1,10]=\{1,2\}` ⟹ **`|Z_S|=2=|S|`（容量项被饱和）** ✓✓ ⟹ 最小非平凡例已**恰好触顶**
```

## §3 它实际控制的数学对象（钉死）

```
$$\#\bigl(E(\mathbb Z_S)\cap\langle P\rangle\bigr)$$ —— 即"`S`-整点群与 `\langle P\rangle` 的交" ✓✓（因 `P` 无限阶、`E(\mathbb Z_S)` 有限 ⟹ 交有限）
【自然的对照上界】 `|Z_S|\le\#E(\mathbb Z_S)`（经典 Siegel）⟹ **我们的 `N_0+|S|` 与之相比是"结构分解式"而非最强界** ✓
```

## §4 相邻文献问题（钉死）

```
**(i)** **Siegel–Mahler 定理**：`\{n:nP\in E(\mathbb Z_S)\}` 有限 ⟹ **我们的 `Z_S` 正是它** ⟹ 本线结果是其**定量细化** ✓
**(ii)** **Silverman 的量化 Siegel 定理**（quantitative version）＋ **有效 Siegel–Mahler**：经**椭圆对数线性型**（Baker 方法系：David／Bugeaud／Hirata-Kohno 线）给**显式但巨大**的界 ⟹ **有效化路径已有** ⚠️
**(iii)** **本原除子理论**：Silverman 1988／Ingram–Silverman 2012／Cheon–Hahn（数域）✓
**(iv)** ⚠️ **`r_q`＝rank of apparition 为教科书概念**（本线 `P-a` 已判定）⟹ **我们那一步是教科书工具**，非新武器 ✓✓
```

## §5 未解决余量（钉死的三处）

```
**【余量 1｜有效化】** `N_0` 来自 Silverman 本原除子定理 ⟹ **非有效** ⟹ 我们的界**继承非有效性** ⟹ ⚠️ **有效化需 abc 型输入**（本线 `P-a` 已 CLOSED）✗
**【余量 2｜容量项锐性（唯一可能真新的一处）】** `|Z_S|` 能否达到 `\omega(D)`？是否存在使 `|Z_S|` 随 `\omega(D)` 增长的族？⟹ **最小实例 `S=\{2,3\}` 恰好触顶** ⟹ **锐性/极值问题是具体的、可攻的** ✓✓
**【余量 3｜数域情形】** Cheon–Hahn 领地 ⟹ 我们未涉 ✓
```

## §6 `P1`–`P3` 判定

```
**`P1`（独立问题？）** ✓ **PASS** —— 明确对象（`Z_S(E,P)=\{n:nP\in E(\mathbb Z_S)\}`）＋明确未知量（`|Z_S|` 的界）＋明确命题（有效化＋锐性）＋**当前未解决**（有效化未决）✓
**`P2`（真正控制量？）** ✓ PASS —— 控制量＝`\#(E(\mathbb Z_S)\cap\langle P\rangle)` 及其"前缀＋容量"分解 ✓
**`P3`（我们的工具是否直接作用于该控制量？）** ⚠️ **PARTIAL** —— `r_q` 记账作用于**容量项**（`|S|`／`\omega(D)`），**不作用于前缀 `N_0`**（那需 abc 型输入）⟹ **工具只覆盖一半** ✓
【判词（照录纪律）】 `EDR` 的**独立问题**成立；但**我们的贡献部分是教科书工具（`r_q`）＋非有效输入** ⟹ 若只到此为止，**应归类为"清晰的计量式叙述"，而非新定理** ✓✓
【唯一可能真新的一处】 **余量 2（容量项锐性/极值）** ✓✓
【边界】 §1 等价刻画、§2 饱和观察、§3 对象、§5 三余量为**本档自行推导**；文献项按档级（未逐字核）；未制造候选／未启动搜索／未碰 RH 总攻。
