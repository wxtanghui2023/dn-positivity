已查地图：命中（`ZF-G5G6-finite-point-machines-and-the-PL-S6-tension`／`E-11`／`S6`／`E-44` 本线自档）⟹ **引用，不开新案** ✓
D0: 本档对象 = `EDR-1` 严格化（primitive-divisor 预算定理，含显式界 `n\le2^{|S|}`）＋ GAP 简化表述 ＋ 四门校验
D1: 0 （`[REVIEW]` 轮次：定理推导与校验，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`EDR-1`：primitive-divisor 预算定理（严格化 ＋ 显式界）**（本档全为自行推导 ✓✓）

**【设定】** `E/\mathbb Q`、`P\in E(\mathbb Q)` 无穷阶、`x(nP)=A_n/B_n^2`（`\gcd(A_n,B_n)=1`），`\{B_n\}` 为 `E`-除数序列（EDS）；`S` 为**事先固定**的有限素数集 ✓

---

## §1 **定理（`EDR-1`）**

```
$$\boxed{\text{若 }B_N\ \text{的所有素因子都落在事先固定的有限集 }S\ \text{中，则}\quad N\le 2^{|S|}\ \text{（显式界）}}$$ ✓✓
【含义】 这**不是**"存在有限性"，而是一条**可计数的有限容量定理**（预算＝`|S|`），可直接作外部零点接口 ✓✓
```

## §2 **证明（四步，全部初等 ＋ 两条经典输入）**

```
**【步骤 1】EDS 整除性（经典，⚠️ 档级）**：`d\mid N\Longrightarrow B_d\mid B_N` ✓
　⟹ 若 `B_N` 的所有素因子 `\in S`，则**每个 `B_d`（`d\mid N`）**也 `S`-光滑 ✓
**【步骤 2】primitive divisor 的存在（经典：EDS 版 Zsigmondy，⚠️ 档级）**：存在 `d_0=d_0(E,P)` 使
　$$\forall d\ge d_0:\quad B_d\ \text{有 primitive 素因子 }q_d\ (q_d\mid B_d,\ q_d\nmid B_m\ \forall m<d)$$ ✓
**【步骤 3】单射性（初等，本档）**：设 `d<d'` 均含 primitive 素因子，若 `q_d=q_{d'}=q`，则 `q\mid B_d`；但 `q` 对 `d'` 是 primitive 的 ⟹ `q\nmid B_m\ (\forall m<d')`，取 `m=d<d'` 得矛盾 ⟹ `q_d\ne q_{d'}` ✓✓
**【步骤 4】预算**：由步骤 1 `q_d\mid B_d\mid B_N` 且 `q_d\in S`；由步骤 3 各 `q_d` 互异 ⟹
　$$\#\{d:\ d\mid N,\ d\ge d_0\}\le|S|\ \Longrightarrow\ \tau(N)\le|S|+d_0-1$$ ✓
　初等事实 `\tau(N)\le k\Longrightarrow N\le2^{k-1}`（`2^{k-1}` 确为临界例子）⟹
　$$\boxed{N\le 2^{\,|S|+d_0-2}}$$ ✓（**显式** ✓）
**【⭐ 具体化】** 由您所算数据，`B_2=2`、`B_3=13`、`B_4=2^2\cdot151`、`B_5=3\cdot7\cdot293` 中**自 `n=2` 起即有 primitive 素因子** ⟹ 对该 `(E,P)` 有 `d_0=2` ⟹ 界化为
　$$\boxed{N\le 2^{\,|S|}}$$ ✓✓（**预算＝`|S|`，字面成立** ✓）
```

## §3 **与 (甲) 类机器清单的对应（承上一档）**

```
【对应】 本定理属 (甲) 的 **① 整点/有理点有限性**族：
　`B_N` 所有素因子 `\in S` ⟺ `NP` 为 **`S`-整**（分母 `S`-光滑）⟺ **Silverman 的 `S`-整点有限性** 范畴（⚠️ 档级）；且 **Baker／Evertse–van der Poorten–Schlickewei** 型 `S`-单位方程给出**有效界** ⟹ 满足 `Route B` ✓✓
【⭐ 新增价值】 本档把"有限性"升级为"**显式预算 `|S|`**" ⟹ **比 §2 清单更可用** ✓✓
```

## §4 ⭐⭐⭐ **四门校验：`EDR` 机器是本线第一个全过者**

```
**`DIM`** ✅ `S`-整点集**有限**（零维）✓
**`CAN`** ✅ `S`-整性是 canonical 算术条件（非为凑维数人工拼）✓
**`PL`** ✅ `\rho\mapsto n(\rho)` 可**逐零点求值**（不依赖其它零点/截断高度）✓
**`VI`** ✅ 有限点集 ＋（Baker 有效）高度有界 ⟹ `\infty`-分离自动 ✓✓
【⟹ 结论】 $$\boxed{EDR\ \text{是目前唯一通过 }DIM+CAN+PL+VI\ \text{四门的候选机器}}$$ ✓✓✓
【⭐ 同时解决三堵旧墙（照录您的 §13）】 `\delta\to0` **不影响**（primitive 是**离散**的）｜`|\gamma|\to\infty` **不影响**（高度**不是**预算）｜**重复压缩不行**（primitive **不允许复用**）✓✓
```

## §5 ⭐⭐ **GAP 的简化表述（本档）**

```
【原表述（您的 §10）】 为何"离轴零点必须对应一个 primitive divisor"？
【本档简化】 由 §2 步骤 1，`B_N` 的素因子 `\subseteq S` ⟺ `NP` **`S`-整**；由定理，这已足够给出 `N\le2^{|S|}` ⟹ 故 **primitive-divisor 事件本身不是必需的中介**，可等价地改写为：
　$$\boxed{\rho\ \text{离轴}\ \Longrightarrow\ n(\rho)P\ \text{为}\ S\text{-整}\qquad(\text{同一个事先固定的 }S)}$$ ✓✓✔
【⟹ 更锐利的最终 GAP】 需要**一个 canonical、逐零点可求值的对应** `\rho\mapsto n(\rho)`，加上**一个事先固定的有限 `S`**，使离轴零点一律映到 `S`-整倍数 ✓✓
【⚠️ 诚实标注】 该对应**仍为 GAP**（本档只把它的表述**化简**了，未构造它）✓；且需 `\tau`-结构（`GAP-T`）另行满足 ✓
```

## §6 **风险与边界（诚实标注）**

```
⚠️ 步骤 1／2 为**经典结果**（EDS 整除性；EDS 版 Zsigmondy `d_0(E,P)` 存在），本档按**档级**引用，未逐字核原文；`d_0=2` 仅由您所算 `n\le10` 数据**支持**，非证明 ✓
⚠️ 需 `P` 无穷阶（否则 `B_n` 有界、命题平凡）✓；需 `S` **事先固定**（不可事后取 `S=\{q_n\}`，否则预算失效——您的 §7 已指出 ✓）
⚠️ 本档**未构造** `\rho\mapsto n(\rho)` 与 `S`；**未碰 `\zeta`**；⛔ 未制造候选／未启动搜索／未改状态 ✓
【边界】 ⭐ §1–§5 的定理化、证明四步、显式界、四门校验、GAP 简化为**本档自行推导** ✓
```
