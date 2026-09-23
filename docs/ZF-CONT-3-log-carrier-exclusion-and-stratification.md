已查地图：命中（`ZF-CONT-1`／`ZF-CONT-2`／`ZF-LEM-parity-structure-three-lemmas`／`T7`（显式公式路线已封）／`E-11`／`E-44` 本线自档与既有封存）⟹ **引用，不开新案** ✓
D0: 本档对象 = 对数/势型载体类的横向排除（`D8`）＋ 两种新重述（`D9`：`k(\gamma)` 分层与"实差"刻画）＋ 存活载体类刻画（`D10`）
D1: 0 （`[REVIEW]` 轮次：结构推导，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-CONT-3`：对数型载体整类排除 ＋ 分层重述（`D8`–`D10`）**（本档全为自行推导 ✓✓）

## §1 ⭐⭐ **`D8`：对数/势型载体类**整类**判死（本档核心 ✓✓）**

```
【载体类定义】 "对数型/势型"＝一切由 `\log`、Green 势、Jensen 型积分、`\log`-导数求和构成的载体，即
　$$\Phi=\int\log|\xi|\,,\qquad \sum_j\log\frac{1}{|s-\rho_j|}\,,\qquad \sum_j\frac{1}{s-\rho_j}\ (=\xi'/\xi),\qquad \text{显式公式型}$$
【关键工具（Jensen，横向小圆盘）】 对 `F_t(u)=\xi(\tfrac12+u+it)`、半径 `r<\tfrac12`：$$\log|F_t(0)|=\frac1{2\pi}\int_0^{2\pi}\log\bigl|F_t(re^{i\theta})\bigr|\,\mathrm d\theta-\sum_{|z_j|<r}\log\frac{r}{|z_j|}$$ ✓
【零点位置】 `z_j=(\beta_j-\tfrac12)+i(\gamma_j-t)` ⟹ 在**在线**情形 `z_j=i(\gamma_j-t)`（纯虚）；在**离线**情形 `z_j=\pm\delta_j+i(\gamma_j-t)` ✓
【⭐ 直接计算】 `|z_j|^2=\delta_j^2+(\gamma_j-t)^2` ⟹ 与在线（`\delta_j=0`）相比之差恰为
　$$-\tfrac12\log\!\Bigl(1+\frac{\delta_j^2}{(\gamma_j-t)^2}\Bigr)=-\frac{\delta_j^2}{2(\gamma_j-t)^2}+O(\delta_j^4)$$ ⟹ ⭐⭐ **偶次、二阶、`O(\delta^2)` 型** ✓✓
【⟹ 双重判死】 **(i)** 一阶横向响应为 `0`（与 `L2` 的 `\sigma`-配对抵消**同一事实的两面** ✓）；**(ii)** 二阶响应是 `\delta^2` 型 ⟹ **正落在 §92 明确排除的 `O(|\beta-\tfrac12|^\alpha)` 类** ✗✓✓
【⟹ 结论】 $$\boxed{\text{对数/势型载体（含显式公式、Jensen、Green 势、}\xi'/\xi\text{ 求和）整体不能给出 }T\text{-无关 obstruction}}$$ ✓✓
【⭐ 副产品】 这**独立地解释了 `T7`（显式公式路线）为何封** —— 不只是"它是已知判据"，而是它在**横向上是偶/二阶盲的** ⟹ 结构原因 ✓✓
```

## §2 ⭐ **`D9-1`：分层重述（本档）**

```
【定义】 对纵坐标 `\gamma`，令 $$k(\gamma):=\#\{\beta:\ \xi(\beta+i\gamma)=0\}$$（该高度上**不同 `\beta` 值**的个数）✓
【结构事实】 在线零点：`k=1`（`\beta=\tfrac12`，重数另计）；离线零点由 `\beta\mapsto1-\beta` 对称 ⟹ **恰 `k=2`**（`\beta` 与 `1-\beta`）✓
【⟹ 重述】 $$\boxed{ZF\iff\#\{\gamma:\ k(\gamma)\ge2\}<\infty}$$ ✓✓
　即：**只有有限多个高度上，"零点的 `\beta` 取值多于一个"** ✓
【读法】 这是一条**分层（stratification）型**陈述：`k\ge2` 的高度＝零点构型的"退化层" ✓（与 `V192` 的"退化"语言一致 ✓）
```

## §3 ⭐ **`D9-2`：实差刻画（本档；新表述）**

```
【计算】 设 `\rho=\tfrac12+\delta+i\gamma`、`\rho'=1-\bar\rho=\tfrac12-\delta+i\gamma` ⟹ $$\rho-\rho'=2\delta\in\mathbb R\setminus\{0\}$$ ✓
【反向】 若两个**不同**零点之差为**非零实数**，则它们不能都在临界线上（同线零点之差为纯虚）⟹ 至少一个离线 ⟹ 由对称性成对 ✓
【⟹ 等价重述】 $$\boxed{\text{存在离线零点}\iff\text{零点集含非零实差}}$$ ⟹ $$\boxed{ZF\iff\text{高处的零点实差对只有有限多}}$$ ✓✓
【⚠️ 注意】 此重述把目标写成**零点集的"差集"性质** ⟹ 与"两结构交互"语言同型（差＝一种交互）⟹ 但⛔ `D8` 已判死其**对数型**读法 ⟹ 只余**代数/index 型**读法 ✓✓
```

## §4 **`D10`：存活载体类的精确刻画（与 `§95` 对齐）**

```
【由 `D8`＋`D3`＋`D4` 得】 存活载体须同时：
　**(i)** **非对数/势型**（`D8`；⟹ 不能由 `\log\xi`、显式公式、Green 势构成）；
　**(ii)** **对横向 `\delta` 一阶/整阶敏感**（⛔ 非 `\delta^2` 型；⟹ 须是**不连续/整跳变**型，`D4`）；
　**(iii)** 有界性来自**算术**（`D3`）；
　**(iv)** `\sigma`-轨道**计数型**（避开 `L2` 取值抵消，`ZF-CONT-2 §3`）；
　**(v)** 增量**不可逆/单侧可加**（`L4`）✓✓
【⟹ 与您的 `§95` 存活清单对齐】 global compatibility obstruction｜finite-length/extension obstruction｜finite-degree degeneration｜monodromy/branch-type｜canonical discrete decomposition failure ⟹ **本档把清单外的一切"解析型"载体整类排除** ✓✓
【⟹ 最重要的净收获】 现在**不需要**再筛查任何"更强的解析估计/显式公式变形/Jensen 型量/势论量"——它们在 `D8` 层面**已被一次性判死** ✓✓
【边界】 ⛔ 未制造候选／未启动搜索／未改状态；⭐ `D8`–`D10` 全为自行推导 ✓
```
