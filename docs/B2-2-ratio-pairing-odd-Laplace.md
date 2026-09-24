已查地图：命中（`EXP-A-1-partner-odd-kill`／`EXP-A-1-analytic-odd-carrier-and-B-plan`／`V186`（`E_F=\sum F(\log n/m)`））⟹ 引用，不
开新案
D0: 本档对象 = `B2-2` 首刀：奇 Laplace carrier 的**比值配对**正化组合（含 Gate A–D 判定）
D1: 0 （[REVIEW] 轮次：构造与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`B2-2`：比值配对（把 `e^{-i\gamma\log n}` 变成 `e^{-i\gamma\log(n/m)}`）**

## §1 单和形式的死点（重申）＋修法

单和 `\sum_n A_n(\gamma,r)\sinh((\log n)\delta)` 的一阶 `=\delta\sum_n A_n\log n` 含 `e^{-i\gamma\log n}` ⟹ **无固定符号**（不同 `n` 振荡）✗
**修法**：把相位配对成**比值** —— 双和形式 $$\mathcal S_{r}(\delta,\gamma)=\sum_{n,m}\frac{\Lambda(n)\Lambda(m)}{\sqrt{nm}}\,e^{-\frac{r^2}{4}[(\log n)^2+(\log m)^2]}\,e^{-i\gamma\log(n/m)}\Bigl[\sinh(\delta\log n)-\sinh(\delta\log m)\Bigr]$$
【关键 1】 相位只剩 `e^{-i\gamma\log(n/m)}` ⟹ 求和主要来自 `n/m\approx1` ⟹ **形成 `\gamma`-局部窗口**（Gate C ✓，不退回 pair correlation）✓
【关键 2】 `\sinh` 差：`n>m,\delta>0` 时 `>0` ⟹ **符号确定**（Gate A ✓）✓✓
【关键 3】 一阶系数：$$\delta\sum_{n,m}w(n,m)\log(n/m)\,e^{-i\gamma\log(n/m)}+O(\delta^3)$$ —— 而 `\log(n/m)` 在交换 `n\leftrightarrow m` 下**反号** ⟹ 与对称权组合后**一阶项不抵消**（与 `T1` 的 `\delta^2` 结局不同）✓✓
【关键 4】 全式**仍由素数侧计算**（`\Lambda,\log n` 显式）⟹ 不依赖未知零点 ✓

## §2 Gate A–D 判定

```
**Gate A（同号？）** ✓ 比值配对 + `\sinh` 单调 ⟹ `n>m` 项同号
**Gate B（二次尺度相消？）** ✓ 已由比值配对完成（相位降为 `\log(n/m)`）
**Gate C（`\gamma`-窗？）** ✓ 核在 `\log(n/m)` 上局部 ⟹ Poisson 对偶给 `\gamma`-窗
**Gate D（`\delta\ne0\Rightarrow\mathcal V>0` 可算不等式？）** ⚠️ **未决** —— 下一刀
```

## §3 下一刀（`B2-2` 第二刀）

把 §1 的 `\mathcal S_r` 化为**显式可算形式**（对 `\Lambda` 双和做变量替换 `h=\log(n/m)`，化为 `\int` 型核），判定是否存在权/尺度使 `\mathcal V_r(\delta,\gamma)>0\ (\delta\ne0)` 成为**素数侧可算不等式** ✓
【边界】 §1 构造与四条关键、§2 判定为**本档自行推导**；`EXP-A-1` 判死定理与 `V186` 的 `E_F` 结构取自本线既有档（档级）；未制造候选／未启动搜索／未碰 RH 总攻。
