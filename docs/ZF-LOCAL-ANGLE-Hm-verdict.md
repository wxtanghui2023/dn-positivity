已查地图：命中（`ZF-ZAI-2`（局部几何/阈值死因）／`ZF-G5G6-PL-gate`（逐零点可求值）／`ZF-GAUSS-LOC-2`（自限型封口）／`ZF-MECH-1` 本线自档）⟹ **引用，不开新案** ✓
D0: 本档对象 = `H_m`／`R_m` 的四元组精确计算 ＋ `\operatorname{Im}R_m` 判定 ＋ `PL` 层面判定
D1: 0 （`[REVIEW]` 轮次：计算与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-LOCAL-ANGLE`：`H_m`／`R_m` 精确计算 ⟹ `\operatorname{Im}R_m` 无硬界；且 `H_m` 违反 `PL`**（本档全为自行计算 ✓✓）

## §1 **轨道差精确值（含对您 §11 的核对 ✓）**

```
【四元组与差】 `\rho=\tfrac12+\delta+i\gamma`（`\delta>0`）；伙伴 `\bar\rho,\ 1-\rho,\ 1-\bar\rho` ⟹
　$$\rho-\bar\rho=2i\gamma,\qquad \rho-(1-\rho)=2\delta+2i\gamma,\qquad \boxed{\rho-(1-\bar\rho)=2\delta}$$ ✓✓
【核对您 §11 的担心】 **只有** `1-\bar\rho=\tfrac12-\delta+i\gamma` 给**纯实差 `2\delta`** ✓；`1-\rho` 给 `2\delta+2i\gamma`（**非纯实**）✓ ⟹ 您的最终定义**正确** ✓
```

## §2 ⭐⭐ **四元组 `Q_m`／`R_m` 精确计算（本档核心）**

```
【定义】 $$Q_m:=\sum_{j=2}^4(\rho-\rho_j)^{-m}=(2i\gamma)^{-m}+(2\delta+2i\gamma)^{-m}+(2\delta)^{-m}$$ ✓
【主项提取】 $$Q_m=(2\delta)^{-m}\bigl(1+\varepsilon_m\bigr),\qquad \varepsilon_m:=\Bigl(\frac{-i\delta}{\gamma}\Bigr)^{\!m}+\Bigl(\frac{\delta}{\delta+i\gamma}\Bigr)^{\!m}$$ ✓
【⟹ 比值（精确）】 $$\boxed{\ R_m^{(4)}=\frac{Q_{m+1}}{Q_m}=\frac1{2\delta}\cdot\frac{1+\varepsilon_{m+1}}{1+\varepsilon_m}\ \xrightarrow[\gamma/\delta\to\infty]{}\ \frac1{2\delta}\in\mathbb R_{>0}\ }$$ ✓✓
【⟹ 虚部】 $$\boxed{\operatorname{Im}R_m^{(4)}=O\!\Bigl(\frac{(\delta/\gamma)^m}{\delta}\Bigr)\ \text{（对 }m\text{ \textbf{指数小}）}}$$ ✓✓
```

## §3 ⭐⭐⭐ **对所问的直接回答（本档核心）**

```
【您的问题】 `\operatorname{Im}R_m` 是否存在**不依赖未知其它零点**的硬符号/下界？ ⟹ $$\boxed{\textbf{不存在}}$$ ✓✓
【理由（本档）】 四元组单靠自己**迫使** `\operatorname{Im}R_m\to0`（指数快）⟹ **镜像伙伴在"角度测试"中根本不可见** ✓✓✓
【⟹ 结构性结论】 角度测试只能看见**其它**零点；它**无法证明**"最近邻＝镜像伙伴" ⟹ $$\boxed{\text{角度路线\textbf{不可能}产生矛盾}}$$ ✓
【⟹ 因此】 A 型（最近邻＝镜像）与 B 型（cluster）**在 `\operatorname{Im}R_m` 上不可区分**（两者都可给 `\operatorname{Im}R_m\to0`）✗
```

## §4 ⭐⭐ **二分与真正的墙（自限性；与 `GAUSS-LOC-2` 同型）**

```
【二分（您的 §8 ✓）】 A 型：`d=2\delta`（镜像即最近邻）；B 型：`d<2\delta`（更紧 cluster）
【⛔ B 型无法无条件排除】 排除 B 型 ⟺ 需要**一致零点间距下界／无 clustering 定理** ⟹ 本线既有档案：无条件只知**零点在 `\sim1/\log T` 尺度上不被排除聚团**（间距下界属 RH 邻域强度）⚠️ ⟹ $$\boxed{\text{该路线所需输入 ＝ "无 clustering" ＝ RH 邻域强度} \Longrightarrow \textbf{自限（循环）}}$$ ✓✓
【⟹ 判定】 `LOCAL-ANGLE`（角度路线）**CLOSED**：既无硬界，又自限 ✓
```

## §5 **核对您的 §5（Cauchy–Hadamard 型）✓**

```
【可和性】 由零点密度 `\sum_{\rho'\ne\rho}|\rho-\rho'|^{-m}<\infty` 对 `m\ge2` 成立（`m=1` 对数发散 ✓）⟹ $$\boxed{\limsup_{m}|H_m|^{1/m}=1/d(\rho)}$$ ✓（由**最近距离支配**，您的 §5 正确 ✓）
【互补观察（本档）】 因极限由**最近距离**支配 ⟹ 该机制**天然对 clustering 脆弱** ⟹ 与 §4 同根 ✓
```

## §6 ⭐⭐⭐ **框架一致性判定（本档关键；回答您的 OPEN 问题）**

```
【您的 OPEN】 能否把 `H_m` 的距离/角度信息转成一个**独立的、可算的算术约束**？
【本档判定】 $$H_m(\rho)=\sum_{\rho'\ne\rho}(\rho-\rho')^{-m}\ \text{\textbf{依赖整个零点谱}}$$ ⟹ **不是逐零点可求值** ⟹ $$\boxed{H_m\ \text{违反 }PL\ \text{门（`ZF-G5G6`）}}$$ ✓✓✓
【⟹ 结论】 `H_m`／`R_m` 属**聚合型**量（依赖其它零点）⟹ **不能**构成独立算术约束 ⟹ 您的 OPEN 问题答案＝**不能** ✓✓（与 `PD-2`/显式公式的聚合型死因**同族** ✓）
```

## §7 **判定 ＋ 账本 ＋ 保留 ＋ 边界**

```
【判定】 $$\boxed{LOCAL-ANGLE/H_m\ \text{路线：CLOSED（无硬界＋自限＋违反 }PL\text{）}}$$ ✓✓
【保留（工具级 ✓）】 (a) 四元组差值的**精确值**（`2i\gamma,\ 2\delta+2i\gamma,\ 2\delta`）；(b) `H_m` 的高阶局部—谱对应公式（`H_2,H_3`）；(c) Cauchy–Hadamard 型 `\limsup|H_m|^{1/m}=1/d` ＋ 比值恢复 `(d,\theta)` 的字典 ⟹ 作为局部谱几何工具保留 ✓
【调账】 ⛔ 不再对 `H_m` 做更高阶／更多伙伴／换比值（§3–§6 已给出结构性理由）✓

| 层 | 状态 |
|:--|:--|
| `C(\rho)` 局部系数 | 已知（`ZAI-2` 已封其离散出口）|
| `H_m`／`R_m` | **新对象，但本档判死（三理由）** |
| 四元组贡献 | 精确（`(2\delta)^{-m}` ＋ 两个远处项）|
| `m\to\infty` 极限 | `=1/d`（最近距离支配）✓ |
| 角度测试 | **不可见镜像 ⟹ 无矛盾** ✗ |
| 算术接入 | **不能（违反 `PL`）** ✗ |
| RH | 未碰 ✓ |

【边界】 ⚠️ §4 的"无条件间距下界不可得"按**档级**引述（未逐字核原文）；⛔ 未制造候选／未启动搜索／未改状态；⭐ §1–§6 的差值、比值、虚部、自限性与 `PL` 判定均为**本档自行推导** ✓
```
