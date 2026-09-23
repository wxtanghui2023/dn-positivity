已查地图：本档为**独立问题扫描**（`IP-1`），**不涉 RH/ZF 地图条目** ⟹ 仅按唐先生 2026-09-23 15:04 令执行 ✓
D0: 本档对象 = 独立问题候选池的 `IP-1` 五门筛选（新对象：独立问题候选，非已知 RH 对象重命名）
D1: 0 （`[REVIEW]` 轮次：候选筛选，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`IP-1`：Independent Problem Scan**（6 候选；⛔ 零计算／⛔ 不设计 invariant／⛔ 不连 ZF/RH ✓）

**唐先生令（15:04 ✓✓）**：只做 $$\boxed{\textbf{IP-1：Independent Problem Scan}}$$，限 **5–8** 候选，每个只交卡片（`SOURCE`／`I1`–`I5`／`KNOWN WALL`／`FIRST THEOREM`／`STOP`）✓；
　⛔ **不写 `E-48`**、⛔ **不运行计算**、⛔ **不连接 ZF/RH** ✓；`I3` 最关键，**无 `I3` 直接 `HOLD`** ✓
　⚠️ 本档所有**文献状态**均为**档级／未逐字核** ⚠️（须一手核验后方可升格）✓

---

## CARD 1 · 埃及分数（Erdős–Straus）

```
SOURCE           经典 Diophantine（4/n = 1/a+1/b+1/c，n≥2）
独立数学命题      对一切 n≥2 存在正整数解
I1 不依赖 RH      PASS
I2 弱化/中间命题  PASS（大量：n≡1 (mod 3) 等；Elsholtz–Tao 型上界）
I3 一轮可判子命题 ⚠️ FAIL —— 未找到**未被覆盖**的可封闭子命题；"n≤N₀ 全验证"属纯计算 ✗
I4 首轮独立价值   FAIL（可证的类多为已知）
I5 自然可计算对象 PASS（有理数/单位分数分解）
KNOWN WALL       已有初等估计与计算验证（⚠️ 界待核）
FIRST THEOREM    ——（无）
STOP             若无新子命题 ⟹ CLOSED
```
⟹ **HOLD（退出点 `I3`/`I4`）**

## CARD 2 ★ 覆盖系统（distinct / odd moduli）

```
SOURCE           Erdős 覆盖系统问题族（Moser 奖方向）
独立数学命题      是否存在**互异模数**（或**全奇模数**）的覆盖系统
I1                PASS
I2                PASS（最小模数猜想已由 BBMS+T 解决 ⟹ 余 distinct/odd 方向；已有 2-adic 障碍类结果）⚠️ 状态待核
I3                ✅ PASS —— 具体子命题例：「模数上界 B 下，覆盖系统的 lcm 必须满足显式 2-进/同余约束」，并对 B ≤ B₀ 给 **exact certificate**
I4                ✅ PASS（新的结构性障碍本身即结果）
I5                ✅ PASS（精确有限对象：模数集合、密度、精确有理证书）
KNOWN WALL        2-adic 障碍链（lcm 的 2 幂）＋该领域最小模数/密度结果 ⚠️
FIRST THEOREM     一条**精确有限结构引理**（显式不等式/同余约束）＋可判定的 B₀
STOP             若子命题退化为纯有限验证，或已被 2-adic 障碍蕴含 ⟹ CLOSED
```
⟹ **PASS（`I1`–`I5`）→ 第一轮候选** ✓

## CARD 3 ★ Diophantine m-tuples（`D(n)` 变体）

```
SOURCE           Diophantine m-tuples 族（`D(1)` 五元组 2016 已解决；`D(n)`/`D(4)` 变体多仍开放 ⚠️）
独立数学命题      给定 n，`D(n)`-m 元组的存在性/上界
I1                PASS
I2                PASS（次数界、Gap principle、计算界）
I3                ✅ PASS —— 例：「固定小集合中的 n，`D(n)`-四元组不存在」型（有限结构＋证书）；或三元组的显式上界
I4                ✅ PASS（新有限性/界即独立价值）
I5                PASS（精确整数对象）
KNOWN WALL        Gap principle／Baker 型界已覆盖部分情形；高元组困难 ⚠️
FIRST THEOREM     一条**新的显式有限性/界**，配 exact certificate
STOP             若只能重复已知 Gap principle 推论 ⟹ CLOSED
```
⟹ **PASS → 第一轮候选** ✓

## CARD 4 ★ Brocard–Ramanujan（`n! + 1 = m²`）

```
SOURCE           经典 Diophantine（阶乘与平方）
独立数学命题      方程仅有 n ∈ {4,5,7} 解
I1                PASS
I2                PASS（已知必要条件族 ＋ 计算验证界 ⚠️）
I3                ✅ PASS —— 例：「某同余类中的 n，`n!+1` 不可能为平方」（p-进/Wilson 型论证，**一轮可判** ✓）
I4                ✅ PASS（**新的显式必要条件**即独立结果）
I5                PASS（阶乘/平方，精确可算）
KNOWN WALL        已知必要条件（涉及 `e` 的连分数等 ⚠️）＋计算界
FIRST THEOREM     一条**新的显式必要条件**（同余/进位数/赋值型），或对某类 n 的排除
STOP             若新条件被已知必要条件蕴含 ⟹ CLOSED
```
⟹ **PASS → 第一轮候选** ✓

## CARD 5 · 最小 Riesel 数

```
SOURCE           Sierpiński/Riesel 数族
独立数学命题      509203 是否为最小 Riesel 数
I3                ❌ FAIL —— 须大规模计算＋素数证书，非"一轮可判"
⟹ HOLD（退出点 `I3`）
```

## CARD 6 · Erdős–Turán（AP 猜想，`k≥4` 定量界）

```
SOURCE           加法组合/素数 AP
独立数学命题      `r_k(N) = o(N)`
I2                PASS（Gowers 里程碑等）
I3                ⚠️ 一轮内可证的新界很可能**已被覆盖** ⟹ `I4` FAIL 风险高
⟹ HOLD（退出点 `I4`）
```

---

## 汇总

| # | 候选 | 判定 | 退出点 |
|:--|:--|:--|:--|
| 1 | 埃及分数 | **HOLD** | `I3`/`I4` |
| 2 | **覆盖系统（distinct/odd）** | ✅ **PASS** | — |
| 3 | **Diophantine m-tuples `D(n)`** | ✅ **PASS** | — |
| 4 | **Brocard–Ramanujan** | ✅ **PASS** | — |
| 5 | 最小 Riesel 数 | **HOLD** | `I3` |
| 6 | Erdős–Turán `k≥4` | **HOLD** | `I4` |

```
【本轮产出】 6 候选 → **3 张通过 `I1`–`I5`**（2/3/4）；3 张 `HOLD`（1/5/6，退出点 `I3`/`I3`/`I4`）✓
【⛔ 未做】 未计算／未设计 invariant／未连 ZF／未连 RH／未写 `E-48`／未开案 ✓
【⚠️ 状态标注】 所有"已知/已解决/开放"均标 ⚠️（**档级·未逐字核**）⟹ 下一轮进入前须**一手核验** ✓
【下一步（须授权）】 仅从 2/3/4 中选 **1** 张，写 `FIRST THEOREM` 的**精确陈述**（仍不计算）✓
```
