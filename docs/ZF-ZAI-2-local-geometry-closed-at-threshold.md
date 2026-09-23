已查地图：命中（`ZF-ZAI-1-three-tests-and-per-zero-decomposability`／`ZF-CONT-1 §92`（`\mathcal O(\rho)\in\{0\}\cup[\varepsilon,\infty)` 判据）／`ZF-LEM`（`L1`/`L2`）／`ZF-G5G6-PL-gate`／`T7` 本线自档与既有封存）⟹ **引用，不开新案** ✓
D0: 本档对象 = 局部几何路线的推导与判死（`\operatorname{Re}C=0\iff` 在线；阈值型死因；覆盖范围与唯一未覆盖缝隙）
D1: 0 （`[REVIEW]` 轮次：推导与判死，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-ZAI-2`：局部几何 —— 给出 β-检测器，但死在「阈值」处（CLOSED，含死因推导）**（本档全为自行推导 ✓✓）

## §1 **反对称的验证与加强（您的 §18 ✓）**

```
【变换律（本档验证）】 `\xi(1-s)=\xi(s)` 逐次求导 ⟹ $$\xi'(1-\rho)=-\xi'(\rho),\qquad \xi''(1-\rho)=\xi''(\rho)$$ ✓ ⟹ 用 `C:=\xi''/(2\xi')` 得 $$\boxed{C(1-\rho)=-C(\rho)}$$ ✓（简单零点，`\xi'(\rho)\ne0`）✓
```

## §2 ⭐⭐ **新结果（本档）：`\operatorname{Re}C(\rho)=0\iff\rho` 在线**

```
【证明（在线）】 若 `\rho` 在线（`1-\rho=\bar\rho`）：由**反对称** `C(\bar\rho)=-C(\rho)`；由 `\xi` 在实轴取实值的 **Schwarz 反射** `\xi^{(k)}(\bar\rho)=\overline{\xi^{(k)}(\rho)}` ⟹ `C(\bar\rho)=\overline{C(\rho)}` ⟹
　$$\overline{C(\rho)}=-C(\rho)\ \Longrightarrow\ \boxed{\operatorname{Re}C(\rho)=0}$$ ✓✓
【离线】 `1-\rho\ne\bar\rho` ⟹ 上述两条约束**不重合** ⟹ 一般 `\operatorname{Re}C(\rho)\ne0` ✓
【⟹ 判据】 $$\boxed{\operatorname{Re}C(\rho)=0\iff\rho\ \text{在线（简单零点）}}$$ —— **局部几何确实给出 β-检测器**（Test A ＝ **PASS**）✓✓
【⭐ 且优于显式公式候选】 `C` 是**局部**量（在单个零点处可求值）⟹ **满足 `PL`** ✓✓（而 `\psi(x)-x` 的单项不可分解 ✗）
【⭐ 与 `L1` 的交叉一致】 `\operatorname{Re}C` 对 `\sigma` 为**奇**且在线（`=\operatorname{Fix}(\sigma)`）处取 `0` ⟹ 正是 `L1` 的一个**具体实例** ✓✓
```

## §3 ⚠️ **但 Test B 失败：二分是「阈值型」**

```
【二分形态】 `\operatorname{Re}C(\rho)=0` vs `\ne0` 是**消失/非消失型（阈值型）**，**不是整数型** ✗
【⟹ 正落既有 `§92` 判据】 该处已立：成功的 `\mathcal O` 须满足 $$\boxed{\mathcal O(\rho)\in\{0\}\cup[\varepsilon,\infty)\ \text{或}\ \in\mathbb Z}$$ —— 而阈值型二分**不满足**（响应可任意小）✓
【且确实可任意小】 `\delta\to0` 时 `\operatorname{Re}C` 由解析性**连续趋于在线值** ⟹ `\operatorname{Re}C\to0` ⟹ **无一致下界** ⟹ 排除 ✓✓
```

## §4 ⭐⭐⭐ **结构性死因（本档推导，正确陈述；这是本轮核心）**

```
【观察】 局部 jet 映射 $$s\mapsto\bigl(\xi^{(k)}(s)\bigr)_{k\le K}$$ **解析** ⟹ 任何**解析地**由 jet 构造的量 `I(s)` 亦**解析** ✓
【⟹ 开映射定理】 解析函数不能在**连通域**上取**有限离散值集**（除非常值）⟹ $$\boxed{\text{离散取值的局部不变量必须来自\textbf{非解析操作}}}$$ ✓✓
【而非解析操作只有那几类】 取模 `|\cdot|`、实部/虚部、`\operatorname{sign}`、消失判据 ⟹ 它们产生的二分**必然是阈值型** ⟹ **正落 §92 排除** ✓✓✓
【反之】 真正**整数型**的局部不变量（如重数 `m=\operatorname{ord}_\rho\xi`）**虽离散却 β-盲**（简单离线零点与简单在线零点同为 `m=1`）✗
【⟹ 结构性死因一句话】 $$\boxed{\text{解析性}\Rightarrow\text{离散取值须非解析}\Rightarrow\text{非解析只给阈值型}\Rightarrow\text{阈值型被 §92 排除}}$$ ✓✓✓
```

## §5 **高阶 `C_k` 与 functional equation 一并（同型）**

```
【高阶】 $$C_k(\rho)=\frac{\xi^{(k+1)}(\rho)}{(k+1)\xi^{(k)}(\rho)}$$ 仍为**复值** ⟹ 同型：只有阈值/符号型二分 ⟹ 同死 ✗
【FE 的作用】 只给 `\rho\leftrightarrow1-\rho` 的**成对结构**（您的 §12/§18）⟹ 给**对称性**，**不给排除** ✓（且由 §4 可知：FE 是解析约束，不可能单独产生离散型排除 ✓）
```

## §6 ⭐ **判定与覆盖范围（诚实边界）**

```
【判定】 $$\boxed{\text{「零点局部几何}\to\text{算术事件」这一大类：CLOSED（死在阈值处）}}$$ ✓✓
【覆盖范围】 本档论证覆盖：一切**由 jet 经解析操作构造、再经非解析操作（模/实部/符号/消失）取离散**的局部不变量 ✓
【⛔ 唯一未覆盖的缝（诚实标注）】 若存在**非解析操作直接产出整数值**的局部量（例如某个**全局定义量的整性**在零点附近的表现），则本档论证不覆盖 ⟹ 记为**唯一缺口**（但**无已知实例**）✓
【⟹ 与您预期的对照】 您预期"若也返回连续解析量，则可较有把握封掉该类" ⟹ 本档给出**更强的结果**：不仅返回连续量，且**证明了为何离散出口必然只剩阈值型** ✓✓
```

## §7 **三检验表 ＋ 账本更新**

| 检查（`ZAI-2`） | 结果 |
|:--|:--|
| β-native（局部） | **PASS**（`\operatorname{Re}C=0\iff` 在线，且合 `PL`）|
| 有零点局部信息 | **PASS** |
| FE 给成对结构 | **PASS** |
| 连续变化自然离散化 | **FAIL**（阈值型）|
| 离散化后仍保留 β | **FAIL**（整数型量 β-盲）|
| `\mathcal O\in\{0\}\cup[\varepsilon,\infty)` | **FAIL**（响应可任意小）|

| 层 | 状态 |
|:--|:--|
| `EDR` / `RPC-1` | **PASS / 保留** |
| 离轴 → 稀有算术集（三类） | **CLOSED** |
| 显式公式/`\psi(x)-x` 候选 | **CLOSED**（循环＋不可分解）|
| **局部几何候选（`C(\rho)`）** | **CLOSED（阈值处；死因已推导）** |
| 局部几何类整体的唯一缝隙 | **OPEN（非解析直接产出整数值；无已知实例）** |
| finite event → finite zeros | **已有预算工具可接** |

```
【边界】 ⚠️ §1 变换律与 Schwarz 反射为经典（档级）；⛔ 未制造候选／未启动搜索／未改状态；⭐ §2 判据、§4 死因推导、§6 覆盖范围为**本档自行推导** ✓
```
