已查地图：命中（`B2-CLOSED-three-condition-intersection-empty`／`EXP-A-1-partner-odd-kill`／`B2-GPT-vs-mine-comparison`）⟹ 引用，不开新案
D0: 本档对象 = `O-TILT` 首刀：`D_{\delta,\eta}` 对一个假设离轴零点的**逐项展开**（自身/镜像/共轭/在线项/边界项）＋ `T1`–`T4` 判定
D1: 0 （[REVIEW] 轮次：展开与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`O-TILT` 首刀：`D_{\delta,\eta}` 的逐项展开 ＋ 四测试**

## §1 逐项展开（本档核心计算）

```
$$D_{\delta,\eta}(\rho_0)=\sum_\rho \mathbf 1_{|\Re\rho-\beta_0|<\delta}\,\mathbf 1_{|\Im\rho-\gamma_0|<\eta}\,\operatorname{sgn}(\Re\rho-\tfrac12)$$
取假设离轴零点 `\rho_1=\frac12+\varepsilon+i\gamma_0`（`\varepsilon>0`），目标 `\beta_0=\frac12+\varepsilon`；其完整轨道四项：
　`\rho_1=\frac12+\varepsilon+i\gamma_0`（`\Re-\beta_0=0`，`\Im-\gamma_0=0`）⟹ **含入，`\operatorname{sgn}=+1` ⟹ 贡献 `+1`** ✓
　`\rho_2=\frac12-\varepsilon+i\gamma_0`（镜像；`|\Re-\beta_0|=2\varepsilon`，`\Im-\gamma_0=0`）⟹ 含入 iff `2\varepsilon<\delta`，贡献 `-1` ✓
　`\rho_3,\rho_4=\frac12\pm\varepsilon-i\gamma_0`（共轭对；`|\Im-\gamma_0|=2\gamma_0`）⟹ 含入 iff `\eta>2\gamma_0` ⟹ **在真正的 `\gamma`-局部窗（`\eta<2\gamma_0`）内被排除** ✓✓
　**在线零点**：`\Re=\frac12` ⟹ `\operatorname{sgn}=0` ⟹ **贡献恒为 `0`** ⟹ $$\boxed{\text{在线零点对 }D\text{ 完全不可见}}$$ ✓✓
【⟹ 局部窗内的取值】 `\delta<2\varepsilon` 时 $$D=+1$$；`\delta>2\varepsilon` 时 $$D=+1-1=0$$ ✓
【⟹ 左侧离轴】 `\beta_0=\frac12-\varepsilon` ⟹ `D=-1` ⟹ **`D` 直接记录取向** ✓
【边界项】 `|\Re-\beta_0|=\delta` 或 `|\Im-\gamma_0|=\eta` 上的零点：取半开窗即可消歧（一般位置测度零）✓
```

## §2 四个硬测试判定

```
**`T1`（绕开镜像对消？）** ✓ **是** —— 取向因子 `\operatorname{sgn}` 反镜像，而窗口不反镜像 ⟹ `f(\rho^\ast)\ne-f(\rho)` ⟹ **不在判死定理适用域** ✓✓
**`T2`（整数型非零证书？）** ✓ **是，但有代价** —— `D\in\mathbb Z`；`\delta<2\varepsilon` ⟹ `D=+1` ⟹ 整数证书 ✓ ；⚠️ **代价**：须选 `\delta<2\varepsilon`，即**须先知道 `\varepsilon` 不小** ⟹ `\varepsilon\to0` 时任何固定 `\delta` 失效 ⟹ **同一 `\delta\to0` 墙的新形态** ✓
**`T3`（存在不含 β 先验的独立入口？）** ⛔ **失败（生死线）** —— 计算 `D` 需 (i) 窗中心 `\beta_0`（未知）与 (ii) `\operatorname{sgn}(\Re\rho-\frac12)`（正是待证者）⟹ **`D` 的计算预设结论** ✓✓
　**更强的形式化**：零点**多重集**只决定 `\{\beta,1-\beta\}`（无序），**不决定符号** ⟹ `D` 不是多重集的函数，而是**带取向标签的构型**的函数 ⟹ **ζ 自身数据只给到多重集** ⟹ $$\boxed{\text{取向输入不可由任何可获得的数据提供}}$$ ✓✓✓
**`T4`（强行连 `\Lambda` 是否回落到显式公式/Weil？）** ✓ **是** —— 显式公式给的是**多重集的泛函**（故对镜像对**对称**）⟹ 任何算术侧可得量**镜像对称** ⟹ 无法输出符号 ⟹ **回落 `B2` 结构** ✓✓
```

## §3 结论（照录您预判的形态）

```
【判定】 `T1` ✓／`T2` ✓（带 `\delta<2\varepsilon` 代价）／`T3` ⛔／`T4` ✓（回落）✓
【新结论（不是旧 β-blind 的重述）】 $$\boxed{\text{取向敏感性确实能突破镜像消去；但一旦要求取向具有\textbf{独立可计算来源}，就必须支付一个新的\textbf{"取向输入"代价}}}$$ ✓✓ —— 即：**取向是自由参数，不是可测项**；所有镜像对称数据源（含全部算术侧）都不供给它 ✓
【与 `B2` 的关系】 `B2` 的失败机制＝解析化 ⟹ 镜像消灭；本档机制＝**非解析化 ⟹ 镜像不消灭，但取向无独立来源** ⟹ **两个不同的封口** ✓✓
【边界】 §1 逐项展开、§2 判定、§3 形式化为**本档自行推导**；未制造候选／未启动搜索／未碰 RH 总攻。
