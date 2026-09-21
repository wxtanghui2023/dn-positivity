已查地图（**先查后写**）：`C-324`（封口 ＋ 转向决策 ✓）、`C-310`（Barker 四格：**缺失型 failure** ＋ 结构等价链 ≠ 传播兼容 ✓，**本轮不改** ✓）、`C-292`（Barker 深审回执：页码勘误 ＋ 层级纪律 ＋ Turyn 1965／548,964,900 层级 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-325（＝唐先生编号 C-324）：Barker 跨对象机制本体审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（三条 ✓✓）

$$\textbf{① 出口}✓：\boxed{\textbf{NO SUCH COMPATIBILITY FOUND}}✓（\text{就}\ \textbf{两个独立操作／传播} \text{而言}✓，\text{与}\ C\text{-310 一致}✓）$$
$$\textbf{② 但获一项}\ \textbf{真实资产}✓✓：\text{跨对象链}\ \textbf{确有恒等式级联合约束}✓✓（\text{见 §4}✓）\ —— \textbf{这恰是 Mahler 侧所缺的那一层}✓✓$$
$$\textbf{③ 纪律}✓✓：\textbf{恒等式级} \ne \textbf{操作级}✗✓ \Longrightarrow \textbf{不}\ \text{升格为兼容律}✗；\textbf{不}\ \text{宣称}\ RH\ \text{bridge}✗$$

## §1 ① 精确定义对象（✓）

| 对象 | 定义 | 适用条件 |
|---|---|---|
| **Barker 序列** ✓ | `\pm1` 序列 `a_1..a_n`，非周期自相关 `C_k = sum_{i} a_i a_{i+k}` 满足 `\|C_k\| <= 1`（`k >= 1`）✓ | 现代定义 ✓；Barker 1953 原式更严（`C_k \in \{0,-1\}` ✓，8 个已知中仅长度 `3,7,11` 满足 ✓） |
| **循环（周期）自相关** ✓ | `C_per(u) = sum_i a_i a_{i+u}`（循环求和 ✓） | 任意长 ✓ |
| **循环差集** ✓ | `D \subset Z_v`，每个非零差恰出现 `lambda` 次 ✓ | **奇长度** Barker ⟺ 循环 `(v,k,lambda)` 差集 ✓（`v = n` ✓） |
| **perfect binary sequence（PBS）** ✓ | `\pm1` 序列使全部非零移位循环自相关为零 ✓ | ⟺ **循环 Hadamard** 差集 ✓ |
| **circulant Hadamard 矩阵** ✓ | 循环 `\pm1` 矩阵 `H` 满足 `H H^t = v I` ✓ | ⟺ PBS ✓（Mark 1965 ✓） |

## §2 ② 已有关系的性质（✓✓，逐项分层 ✓）

| 关系 | 性质 |
|---|---|
| 奇长度 Barker ⟺ 循环差集 ✓ | **定理／等价** ✓ |
| **偶长度 Barker（>13）⟹ PBS** ✓ | **结构性蕴含（单向）** ✓✓；**反向等价在文献中明确标为未证** ✓✓（`[待核]`⚠️） |
| `C_per(u) = C_aper(u) + C_aper(u-n)` ✓ | **恒等式** ✓（非传播 ✗✓） |
| 奇长度 `n <= 13`（Turyn–Storer 1961 ✓） | **定理**（原证明有缺陷 ✓：Willms 2014 ✓；**Schmidt–Willms 2016 给可用新证明** ✓✓） |
| `PBS(s) > 4 ⟹ s = 4S^2`，`S` 奇、`S >= 55`、非素数幂（Turyn 1965 ✓） | **定理（形状必要条件）** ✓ |
| `4 < n < 548,964,900` 无偶长度 Barker ✓ | **有限计算排除** ✓✓（Leung–Schmidt 2005 ✓；经 PBS／circulant Hadamard 侧 ✓） |
| Barker 猜想 ✓／Ryser 猜想 ✓ | **猜想** ✓ |

$$\textbf{防误写}✓✓：\textbf{等价问题} \ne \textbf{动态传播}✗✓（\text{唐先生指定}✓）$$

## §3 ③ 真正的跨对象操作（✓）

$$\textbf{现成者}✓：\text{① 循环移位／乘子作用}✓（\text{差集自同构}✓，文献标准 ✓）；\text{② 补集}✓（`D -> Z_v \\ D`✓）；\text{③ 差集} \to \textbf{循环关联矩阵}✓；\text{④ Hadamard 类} \to \textbf{circulant 子类}✓（\text{限制／嵌入}✓）；\text{⑤ Turyn 型延长构造}✓（\text{构造}✗）$$
$$\textbf{排除}✗✓：\text{「同一对象换语言」}\ \textbf{不计}✗（\text{如非周期／周期两种自相关的}\ \textbf{记法} \text{互换}✗）$$

## §4 ④ ⭐ compatibility 审查：**恒等式级联合约束存在**（✓✓，本档核心发现 ✓）

$$\textbf{所求形式}✓：\text{两个}\ \textbf{独立结构} \text{的作用受}\ \textbf{共同限制}✓；\text{即}\ \mathcal C(F_X, F_Y) = 0✓$$
$$\textbf{发现}✓✓：\boxed{C_{per}(u) = C_{aper}(u) + C_{aper}(u-n)}✓ \Longrightarrow \text{非周期侧的约束}\ \textbf{强制传播} \text{到周期侧}✓✓$$
$$\qquad \text{例}✓：\text{若}\ |C_{aper}| \le 1✓ \Longrightarrow C_{per} \in \{-2,\dots,2\}✓；\text{偶数长度 Barker}\ \Longrightarrow C_{per} \text{ 受限}✓ \Longrightarrow \text{与}\ PBS\ \text{的必要条件}\ \textbf{共同作用}✓✓$$
$$\qquad \textbf{文献已用}✓✓：\text{Turyn 桥（偶长度} \to PBS✓）\ \textbf{正是靠这条恒等式}✓✓$$
$$\textbf{但}✓✗：\text{它是}\ \textbf{恒等式级}✓（\text{由两个自相关定义直接推出}✓），\textbf{不是}\ \textbf{操作级兼容}✗✓ \Longrightarrow \textbf{不}\ \text{计为兼容律}✗✓$$

## §5 出口与纪律（✓✓）

$$\boxed{\textbf{NO SUCH COMPATIBILITY FOUND}}✓（\text{就操作级／两传播而言}✓）$$
$$\textbf{资产登记}✓✓：\text{Barker 内部跨对象资产}＝\text{恒等式级联合约束}✓（\texttt{C\_per} = \texttt{C\_aper(u)} + \texttt{C\_aper(u-n)}✓）\ —— \textbf{不}\ \text{自动升级为}\ RH\ \text{bridge}✗✓$$
$$\textbf{不改} C\text{-310}✗✓：\text{缺失型 failure ＋ 结构等价链仍}\ \ne \text{传播兼容}✓（\text{保持}✓）$$
$$\textbf{下一步}✓（\text{唐先生定}✓）：\text{Barker 暂停}✓ \to \text{Littlewood 或 Lonely Runner}✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 跨对象机制审计 命中文件数=1    :: ./C324-C323-closure-Mahler-chain-archived-pivot-to-next-external-problem.md 
技术词 恒等式级联合约束 命中文件数=0    :: 
技术词 操作级兼容  命中文件数=0    :: 
```
- 本档新增 ✓：`恒等式级联合约束`／`操作级兼容`（依上表判 ✓）
- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：Barker 已找到兼容律 ✗；恒等式级＝操作级 ✗；Barker 可升格为 RH bridge ✗
