已查地图：命中（`ZF-G5G6-DIM-screen-and-height-collapse`／`ZF-G5G6-PL-gate-and-reverse-scan`／`ZF-LEM-parity-structure-three-lemmas`／`E-11` 本线自档）⟹ **引用，不开新案** ✓
D0: 本档对象 = 实现层结构引理 `R1`（`\sigma`-等变 ⟹ 在线自动入 `\operatorname{Fix}(\tau)`）＋ 第二次自我更正 ＋ `VI` 的归约与精确陈述
D1: 0 （`[REVIEW]` 轮次：结构推导与更正，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-G5G6` 续二：实现层结构引理 `R1` ＋ `VI` 归约**（本档全为自行推导 ✓✓）

## §1 ⭐⭐ **`R1`：`\sigma`-等变 ⟹ 在线自动入 `\operatorname{Fix}(\tau)`（本档）**

```
【设定】 `\sigma(s)=1-\bar s`（功能方程反射，`\sigma^2=\mathrm{id}`，`\operatorname{Fix}(\sigma)=\{\Re s=\tfrac12\}`）；设实现 `\Phi:Z(\zeta)\to\mathcal M` 与某某对合 `\tau:\mathcal M\to\mathcal M`（`\tau^2=\mathrm{id}`）**等变**：
　$$\boxed{\Phi\circ\sigma=\tau\circ\Phi}$$ ✓
【断言（在线）】 若 `\Re\rho=\tfrac12`（`\sigma\rho=\rho`）⟹ $$\Phi(\rho)=\Phi(\sigma\rho)=\tau\Phi(\rho)\ \Longrightarrow\ \boxed{\Phi(\rho)\in\operatorname{Fix}(\tau)}$$ —— **自动成立，不需任何额外独立输入** ✓✓
【断言（离线）】 若 `\sigma\rho\ne\rho` ⟹ $$\Phi(\sigma\rho)=\tau\Phi(\rho)$$ ⟹ 若又有 `\Phi(\rho)\in\operatorname{Fix}(\tau)`，则 `\Phi(\rho)=\tau\Phi(\rho)=\Phi(\sigma\rho)` ⟹ **`\Phi` 把 `\sigma`-对塌成一点** ⟹ 与"分离"矛盾 ✓✓
【⟹ 可检验设计条件】 $$\boxed{\Phi\ \text{须\textbf{分离 }\sigma\text{-对}：}\ \sigma\rho\ne\rho\ \Longrightarrow\ \Phi(\sigma\rho)\ne\Phi(\rho)}$$ ✓✓
【⟹ 由此得天然设计】 取 `\mathcal D:=\mathcal M\setminus\operatorname{Fix}(\tau)` ⟹ 则
　在线：`\Phi(\rho)\in\operatorname{Fix}(\tau)` ⟹ `\notin\mathcal D` ✓；离线：`\Phi(\rho)\notin\operatorname{Fix}(\tau)`（由分离性）⟹ `\in\mathcal D` ✓✓
　**正是您 §87/§113 想要的"fixed vs non-fixed 扇区"结构**，且**在线那一半是白送的** ✓✓
```

## §2 ⚠️ **自我更正（第二次）：上一档 `HG` 的"塌缩"方向反了**

```
【上一档说法】 "`\Phi` 须**压掉高度方向**（高度摧毁型）" ✗
【更正】 本轮 `R1` 显示：`\sigma`-对分离性要求 `\Phi` **不要塌缩**（至少不能把 `\rho` 与 `\sigma\rho` 映到同一点）⟹ **正确方向是"分离"，不是"塌缩"** ✓✓
【保留者】 `PL`（禁**聚合**：不得依赖其它零点或截断高度）**仍成立且不受影响** ✓；上一档"本仓工具全为聚合型故失败"的诊断**仍有效** ✓（那是 `PL`，非 `HG`）
【⟹ 更正后：本档对上一档的两次更正汇总】 ① `HG` 非必要门（`Route A` 不需要）；② `HG` 的**方向亦错**（应分离而非塌缩）⟹ `HG` **整体作废**，**不再出现在门集内** ✓
```

## §3 ⭐⭐ **`VI` 的归约：负担全部落到母问题侧（本档）**

```
【由 `R1`】 `§113` 的 **II（transverse rigidity）** 的"**critical-neutral 一半自动成立**" ✓ ⟹ 剩下全部负担＝
　$$\boxed{\text{母问题须给出 canonical }\mathcal D\subset\mathcal M\setminus\operatorname{Fix}(\tau)\ \text{且有限容量（零维）}}$$ ✓✓
【由 `DIM`】 `\mathcal M\setminus\operatorname{Fix}(\tau)` 维数为 `d`（大）⟹ 单靠"非固定"**远不足**（`DIM` 会判正维）⟹ 须**附加 canonical 条件**把它切成**零维** ⟹
　$$\boxed{\text{要找的正是：canonical 多兼容条件，把\textbf{非固定轨迹}切成零维}}$$ ✓✓✓
【⟹ `VI` 与 `DIM` 在此**精确会合**】 `VI` 不再是"另加一层困难"，而是"`DIM` 须在**非固定扇区内部**成立" ✓
```

## §4 **`R4`：对 `\Phi` 的四条可检验设计要求（本档汇总）**

```
**(a)** **逐零点可求值**（`PL`）：不得依赖其它零点或截断高度 ✓
**(b)** **`\sigma`-等变**：`\Phi\circ\sigma=\tau\circ\Phi`（`\tau` 须先在母问题中存在，⛔ 不得定义为 `s\mapsto1-\bar s`，遵 `L3` 与您的 §11）✓
**(c)** **分离 `\sigma`-对**：`\sigma\rho\ne\rho\Rightarrow\Phi(\sigma\rho)\ne\Phi(\rho)` ✓
**(d)** ⛔ **不得"选代表"**：若定义 `\Phi(\rho):=\rho`（当 `\Re\rho\ge\tfrac12`）否则 `\sigma\rho` ⟹ 则全部零点满足 `\Re\Phi\ge\tfrac12`，而"区分 `=\tfrac12` 与 `>\tfrac12`"**就是原目标本身** ⟹ `CAN` FAIL（定义式/循环）✓✓
```

## §5 ⭐ **与 `L1` 的交叉一致性（框架自洽性证据 ✓）**

```
`R1`(i)（`\sigma`-等变 ⟹ 在线 ⟹ `\operatorname{Fix}(\tau)` ⟹ 中性）与 `ZF-LEM` 的 `L1`（不变量**奇数性** ⟹ 固定扇区取值 `0`）是**同一条结构事实在两层语言中的表述**（实现层／不变量层）✓✓ ⟹ 两档独立推导得到同一结论 ⟹ 框架自洽 ✓
```

## §6 **`VI` 的最终精确陈述（the GAP 重述，本档）**

```
$$\boxed{\text{须存在 }(\mathcal M,\overline{\mathcal M},\tau,\mathcal D,F)\ \text{canonical};\ \mathcal D\subset\mathcal M\setminus\operatorname{Fix}(\tau)\ \text{且}\ \dim_{\rm top}\mathcal D=0\ \text{（含 }\infty\text{-分离）};\ \text{并存在 }\Phi\ \text{满足 §4 的 (a)–(d)};\ \text{使 }\rho_{\rm off}\Rightarrow\Phi(\rho)\in\mathcal D}$$ ✓✓
【⛔ 仍为 GAP 的部分】 尚无已知的这样的 `(\mathcal M,\tau,\mathcal D,F,\Phi)` ⟹ 但**结构已完全具体**：只需在**非固定扇区内**找 canonical 的零维异常层 ＋ 一个 `\sigma`-等变、分离对的逐零点实现 ✓
【边界】 ⛔ 未制造候选／未启动搜索／未改状态；⭐ §1/§3/§4/§5 与两次更正均**本档自行推导** ✓
```
