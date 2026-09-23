已查地图：命中（`WHY-CANNOT-CREATE-TOOLS-bohr-and-tao`／`ALMOST-PERIODIC-where-is-the-period`／`META-OBSTRUCTION T1/T2`／`D1=0`（算术无内生动力学）／`CROSS-0`（加乘交叉不变量已封）／`I-DH-PARITY-GATE`（痕迹1））⟹ **引用，不开新案** ✓
D0: 本档对象 = prime-power phase flow 第一轮（仅问"能否造出新的算术 invariant/monotone 量"）⟹ 分类判死 ＋ 结构性理由
D1: 0 （`[REVIEW]` 轮次：分类与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **prime-power phase flow 第一轮：没有发动机（分类判死）**

## §0 **任务（照录）＋ 四门**

```
先**不谈 RH**，只问：$$z_{p,m}(t)=e^{-imt\log p}$$ 这个系统能否自然产生**此前未用过**的算术 invariant／单调量？✓
四门：**G1** 非平凡（非 `\Re\log\zeta`／`|\zeta|`／`\zeta'/\zeta` 换记号）｜**G2** 算术可读（见 `p,p^m,m,\log p` 结构）｜**G3** 动力学真产生新信息（`\frac{d}{dt}\mathcal E` 或差分给新符号/不等式）｜**G4** 零点端可读（`\beta\ne\tfrac12` ⟹ 明确违反）✓
```

## §1 **系统精确化（本档）**

```
$$\dot z_{p,m}=-im\log p\,z_{p,m},\qquad A_\sigma(t)=\sum_{p}\sum_{m\ge1}\frac{p^{-m\sigma}}{m}z_{p,m}(t)=\log\zeta(\sigma+it)\quad(\sigma>1)$$ ✓
【频率集】 `\{m\log p\}` 在 `\mathbb Q` 上**线性无关**（唯一分解：`\sum a_{p,m}m\log p=0\Rightarrow a=0`）✓
【⚠️ 注意】 `z_{p,m}=z_{p,1}^{\,m}` ⟹ **`p^m` 模态不是独立生成元**，而是基频 `\{\log p\}` 的幂 ✓（故信息量 ≤ 基频集）✓
```

## §2 ⭐⭐⭐ **结构性理由（本档核心）：该流**极小且唯一遍历** ⟹ 无守恒量**

```
【事实（⚠️ 档级：Kronecker/Bohr 标准理论）】 该流是**紧 Abel 群上的平移（Kronecker 流）** ⟹ 在 Bohr 紧化上**极小（minimal）且唯一遍历（uniquely ergodic）** ✓✓
【⟹ 后果 1：无非平凡守恒量】 极小性 ⟹ **不存在非平凡的连续不变量**（任何连续不变函数必常值）⟹ $$\boxed{\text{无 "}\frac{d}{dt}\mathcal E=0\text{" 型守恒量}}$$ ✗✓✓
【⟹ 后果 2：单调量亦不可能**由流本身**给出】 唯一遍历 ⟹ 时间平均 ＝ 空间平均（Haar）⟹ 一切沿轨平均量**退化为测度论量** ✓
【⟹ ⟹ 结论】 $$\boxed{\text{该流的自然不变量}\ \textbf{只能是测度论（统计）量}}$$ ✓✓✓ —— 这直接判死 `G3` ✓
```

## §3 **不变量的完整分类与逐项判死（本档主表）**

| 不变量类型 | 具体形态 | 死因 |
|:--|:--|:--|
| **(a) Bohr–Fourier 谱** | 系数 `p^{-m\sigma}/m` 于频率 `m\log p` | ＝**重读 Euler 系数** ⟹ `G1` FAIL ✓ |
| **(b) 一阶均值** | `\overline{A_\sigma}=0` | 平凡 ✗ |
| **(c) 二阶相关/矩** | `\sum_{p,m}p^{-2m\sigma}/m^2`、`\sum_{m,n}` 型 | 可表为 `\zeta(2\sigma)` 及其导数 ⟹ `G1` FAIL ✓ |
| **(d) 熵/回复密度** | `\mathcal T_\varepsilon` 密度 `\asymp(\varepsilon/2)^n` | **统计**；且随频率数**指数退化** ⟹ `G3/G4` FAIL ✓（承 `ALMOST-PERIODIC`）|
| **(e) 乘法半群矩** | `n\mapsto n^{-it}` 完全乘性 ⟹ `\sum_{n\le N}n^{-it}` ≈ 线上 `\zeta` 截断 | ＝**线上矩/Lindelöf 墙**（已认定）⟹ 统计，`G4` FAIL ✓ |
| **(f) 加乘交叉不变量** | — | **`CROSS-0` 已封**（Gauss 和/Jacobi 和/Hasse–Davenport 已占）✗ ✓ |
| **(g) Validity 型（值分布）** | Bohr–Jessen 极限分布 | **1930 年代经典** ⟹ 不新；且统计 ⟹ `G4` FAIL ✓ |
【⟹ 主表结论】 $$\boxed{\text{七类全部 FAIL；无第八类（由 §2 极小性可知不存在守恒/单调型）}}$$ ✓✓✓
```

## §4 **四门判定**

```
**G1 非平凡** ✗（(a)(c) 均为 Euler 系数重读）｜**G2 算术可读** ⚠️（可读，但读出的就是 Euler 系数 ⟹ 与 G1 同死）｜**G3 动力学真产生新信息** ✗（§2 极小 ⟹ 无守恒量；统计量属经典）｜**G4 零点端可读** ✗（统计量不能定位，承 `T1/T2`）⟹ $$\boxed{\text{四门全 FAIL}}$$ ✓✓
```

## §5 ⚠️ **且 novelty 侧已先撞（登记）**

```
【承上一轮痕迹 1】 "**prime-power-support equivalence for the log-derivative coefficients**" ＋ "**support and sign, invisible to magnitude**" 已公开 ✓ ⟹ 即使我们造出 **support 型** invariant，也**不新** ✗✓ —— 与本档 §3(a)(c) 的死因**双重** ✓
```

## §6 **判定（照您给的判准）**

```
【您的判准（照录）】 "如果第一轮计算连这个都造不出来，就应该彻底承认：**动力学这条创造工具的路，在我们当前掌握的资产里也没有真正的发动机**" ✓
【本档判定】 $$\boxed{\text{prime-power phase flow 第一轮：造不出} \Longrightarrow \textbf{动力学路无发动机（承认）}}$$ ✓✓
【一致性】 与 `D1=0`（**算术侧无内生动力学**）**完全一致** ✓✓；也解释了为何 `S(t)` 侧只能得到**丰度/统计**（承 `ALMOST-PERIODIC`）✓
```

## §7 **保留（工具级）＋ 边界**

```
【保留 ✓】 **(i)** §2 的**极小性论证**：一个**干净、可复用**的结构性理由 —— **任何 Kronecker 型流都不给守恒量**（可用于将来快速判死同类提案）✓；**(ii)** §3 的**七类分类表**（哪类不变量必死 + 死因）✓
【边界】 ⚠️ §2 的极小/唯一遍历为**标准事实**（档级，未逐字核）；§3 各死因为**本档逐项推导** ✓；⛔ 未制造候选／未启动搜索／未改状态／未碰 RH ✓
```

## §8 【技术词回查】（逐字粘贴 ✓）

```
技术词 phase flow       命中文件数=1    :: ./PHASE-FLOW-round1-no-engine.md 
技术词 极小性        命中文件数=11   :: ./V167-five-device-audit-double-obligation-structure.md ./C226-DB-B1B4-pass-11x11-Krawczyk-damped-M3.md ./C218-m3-at-least-0.764081100745-gap-8.5e-13-BB-phase-complete.md 
技术词 唯一遍历     命中文件数=1    :: ./PHASE-FLOW-round1-no-engine.md 
```
【三分类】 **本档新增**：§2 极小性论证（无守恒量）、§3 七类分类表 ⟹ 本档推导 ✓；**档案已有（引用）**：`phase flow`／`极小性`／`唯一遍历`（见上逐字）；**通用词（不计）**：`发动机`（比喻）✓
