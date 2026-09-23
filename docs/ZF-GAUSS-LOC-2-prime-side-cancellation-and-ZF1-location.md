已查地图：命中（`ZF-GAUSS-LOC-1`（高度定位 Gaussian）／`ZF-1`（近 `1/2` 无一致幂次节省）／`T7`／`E-44`／`ZF-MECH-1`（`P/Q` 二分） 本线自档与既有封存）⟹ **引用，不开新案** ✓
D0: 本档对象 = `GAUSS-LOC-1` 唯一剩余不等式（`c<\delta^2`）的无条件判定＋失败原因精确定位（归至 `ZF-1` GAP）
D1: 0 （`[REVIEW]` 轮次：计算与定位，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-GAUSS-LOC-2`：prime-side cancellation 判定 ⟹ `c=1/4` 天花板 ⟹ 失败归至 `ZF-1`**（本档全为自行计算 ✓✓）

## §1 **核对连续模型（照录您的 §5–§7 ✓）**

```
【振荡版（本档复算）】 $$\int_0^\infty e^{u/2-u^2/(4t)}e^{iau}\,du=2\sqrt{\pi t}\,e^{\,t(1/4-a^2)}e^{iat}$$ ✓（配方：`u/2-u^2/(4t)+iau=t/4-ta^2+iat-(u-t-2iat)^2/(4t)` ✓）
【⟹ 两支】 振荡版 `\asymp e^{t(1/4-a^2)}`（`a>1/2` 时**指数衰减** ✓）；绝对值 majorant（丢 `\cos` 给 `\asymp e^{t}` ✗）✓ 与您一致 ✓
```

## §2 ⭐ **显式公式把 prime side 换成 zero side（本档；⚠️ 归一化按档级）**

```
【结构】 以高斯核平滑的显式公式给出 $$\underbrace{\sum_n\Lambda(n)n^{-1/2+ia}e^{-(\log n)^2/(4t)}}_{S(a,t)\ \text{侧}}\ \longleftrightarrow\ \underbrace{\sum_\rho e^{\,t\left((\rho-w)^2\right)}}_{w:=\frac12-ia}\ \times\sqrt{4\pi t}\ +\ \text{pole}\ +\ \Gamma/\text{trivial}$$ ✓
【三类项的具体形态（本档）】 目标离线零点（`\rho=\tfrac12+\delta+i\gamma`）：$$\bigl|e^{t(\rho-w)^2}\bigr|=e^{\,t(\delta^2-(\gamma+a)^2)}\ \xrightarrow{\gamma\approx-a}\ e^{\,t\delta^2}$$ ✓（**与您 §3 完全一致** ✓）；在线零点：$$e^{-t(\gamma+a)^2}$$ ✓；pole 项：$$e^{\,t(1/4-a^2)}$$ ✓（＝§1 的连续模型项 ✓）
【⟹ 机制确认】 高斯＝**高度定位核**，把 zero side 局限到 `|\gamma+a|\lesssim\sqrt t` ✓✓
```

## §3 ⭐⭐ **无条件上界（本档核心计算）**

```
【逐项估计】 对任意零点 `\rho`（仅用平凡无零点区 `\beta\in(0,1)`）：$$Re\bigl((\rho-w)^2\bigr)=(\beta-\tfrac12)^2-(\gamma+a)^2\le\tfrac14-(\gamma+a)^2$$ ⟹ $$\bigl|e^{t(\rho-w)^2}\bigr|\le e^{\,t/4}\cdot e^{-t(\gamma+a)^2}$$ ✓
【求和】 窗口内零点计数 `\ll\sqrt t\,\log t`（由 `|\gamma+a|\lesssim\sqrt t` 局部化） ⟹
　$$\boxed{\ \bigl|S(a,t)\bigr|\lesssim e^{\,t/4+o(t)}\ }$$ ✓✓ —— 即 **`c=1/4` 是无条件天花板**（pole 项 `e^{t(1/4-a^2)}` 在 `a\ge14` 时可忽略 ✓）
```

## §4 **生死判据的答案（照您 §11）**

```
【比较】 `\delta^2<\tfrac14` ⟹ $$e^{\,t\delta^2}\ \ll\ e^{\,t/4}$$ ⟹ **预算恒输** ⟹ $$\boxed{c<\tfrac14\ \text{无条件不可达}}$$ ✓✓
【⟹ 判定】 `GAUSS-LOC-1` 家族在**绝对值与无条件**层面**失败**；且失败是**指数率级**（非常数级）✓
```

## §5 ⭐⭐⭐ **等价性/自限（本档关键）**

```
【反推】 欲得 `c<1/4`，须对窗口内零点排除 `(\beta-\tfrac12)^2>c` ⟹ 即须在**近 `1/2` 处**给出改进的零点排除 ⟹ 这**正是**本线 `ZF-1` 的 GAP：$$\boxed{\text{近 }\tfrac12\text{ 无一致幂次节省}}$$ ✓✓
【⟹ ⟹ 结论】 $$\boxed{\text{该不等式} \equiv \text{部分 RH 型陈述（窗口内的近临界无零点）}\ \Longrightarrow\ \textbf{自限/循环}}$$ ✓✓（与 `T7` 型封口同构，但**本档给出精确指数** `1/4` 与**精确可达性判据** `c<\delta^2` ✓）
```

## §6 **失败原因的精确位置（照您"如果不能…" ✓）**

```
**(i) `c=1/4` 天花板的来源**：只用 `\beta\in(0,1)`（平凡无零点区）⟹ 改进须要**更强的 `\beta` 上界** ✓
**(ii) 改进所需的输入**：窗口内零点密度／无零点区 ⟹ ＝ `ZF-1` GAP（近 `1/2` 无一致幂次节省）✓ ⟹ **非新墙，与既有档案吻合** ✓✓
**(iii) 另一点（承您 §12）**：`\delta\to0` 时目标增长率 `e^{t\delta^2}\to1` 而 ceiling 仍 `e^{t/4}` ⟹ 故**完整 RH 级结论**绝无可能由该家族给出 ✓
```

## §7 **判定 ＋ 账本 ＋ 边界**

```
【判定】 $$\boxed{GAUSS-LOC-1:\ \text{高度定位机制成立（工具级）};\ \text{但其prime-side 不等式 CLOSED —— 无条件 }c=1/4\text{ 天花板 ⟹ 自限}}$$ ✓✓
【保留（工具级 ✓）】 高度定位高斯 `H_{a,t}` 的**零点定位能力**（`e^{-t(\gamma+a)^2}` 窗口）＋ pole 项 `e^{t(1/4-a^2)}` 的**精确形态** ⟹ 以后若有新输入可直接取用 ✓
【不做】 ⛔ 不再调 `t`／换核／加阶 ⟹ 因为 §5 已证**自限性**（任何改进都等价于 `ZF-1` 型输入）✓✓
【边界】 ⚠️ §2 归一化与 $\Gamma$/trivial 项按**档级**处理（未逐字核）；⛔ 未制造候选／未启动搜索／未改状态；⭐ §1–§6 的复算、天花板、等价性、定位均为**本档自行推导** ✓
```
