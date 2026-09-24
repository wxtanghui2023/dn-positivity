已查地图：命中（`ATTACK-A-beta-information-loss-list`／`ASTRA-TRANSFER-three-attacks`／`ZF-GAUSS-LOC-1`（绝对值预算失败）／`META-OBSTRUCTION T3`）⟹ 引用，不开新案
D0: 本档对象 = `EXP-A` 首刀：具体 `M(\beta,\gamma;T,r)` 的定义＋三条检查（基准／`\partial_\beta` 符号／可算性）＋ 首关不等式
D1: 0 （[REVIEW] 轮次：构造与自检，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`EXP-A`：局域 β-排除量 `M` 的首刀构造**

## §1 构造（本档）

取全纯窗 `K`，令 `z:=\rho-\rho_0`（`\rho_0=\beta+i\gamma` 为候选零点），定义**实值、局域、对 `\operatorname{Re}z` 为奇**的权
$$w(z):=\frac{\operatorname{Re}z}{r}\,\exp\!\Bigl(-\frac{|z|^2}{r^2}\Bigr),\qquad M(\beta,\gamma;T,r):=\sum_{|\gamma_\rho|\le T}w(\rho-\rho_0)$$
【为何取奇权】 σ-对称权对 `\delta` 的响应是 `O(\delta^2)`（本线 `T1`）；**奇权给出 `O(\delta)` 一阶响应** ⟹ 正是 `T3` 逃逸条件的**定量实现** ✓

## §2 三条检查

```
【检查 1｜基准】 `\rho_0` 自身零点贡献 `w(0)=0` ✓；镜像零点（`\operatorname{Re}z=-2\delta`）贡献 `\approx-\frac{2\delta}{r}` ✓
【检查 2｜符号】 $$\partial_\beta M\ \approx\ -\frac{2}{r}\ (\text{镜像项主导时})$$ ⟹ **符号确定（负）** ✓✓ —— 这是本线现有量**都没有**的性质（`ATTACK-A` 清单：位置/符号被丢）✓
【检查 3｜可算性】 权 `w` 是 `e^{-|z|^2/r^2}` 型与其导数的组合 ⟹ 属显式公式可容许测试类 ⟹ `M` **可由素数侧＋archimedean 项计算，无需输入零点** ✓✓
```

## §3 ⭐ 首关不等式（本档核心，可算）

$$M\ =\ \underbrace{-\frac{2\delta}{r}+O(\delta^3)}_{\text{信号（离轴对称项）}}\ +\ \underbrace{\mathcal B(\gamma;T,r)}_{\text{背景（其余零点＋素

数侧＋arch）}}$$
$$\boxed{\text{首关：是否存在 }(r,T)\text{ 使 }|\text{信号}|\ >\ |\mathcal B|\ ?}$$
【为何这关是新的】 `ZF-GAUSS-LOC-1` 曾在**正（绝对值）预算**下失败（素数侧 `\lesssim e^{t}` 压过信号 `e^{t\delta^2}`）；本档取**奇投影**，σ-对称背景被**精确抵消**（`T1`/`L2`）⟹ **背景量级可能大幅下降** —— 这是与旧失败**唯一实质差别**，也是本关要测的东西 ✓✓
【判死条件】 若奇投影后 `\mathcal B` 仍 `\gtrsim` 信号（对一切 `(r,T)`）⟹ `EXP-A` CLOSED ✓
【边界】 构造与三条检查、首关不等式为本档自行推导；`GAUSS-LOC-1`／`T1`／`T3` 取自本线既有档（档级）；未制造候选／未启动搜索／未碰 RH 总攻。
