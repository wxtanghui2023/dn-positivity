已查地图（**先查后写**）：`C-304`（桥的定性 ＋ ③ 地图预检 ✓）、`C-303`（Hilbert symbol 对照 ✓）、`C-302`（Hecke 关闭 ✓）、`C-286-A`（加法能量族淘汰 ✓）。语境提取：`grep -o` 窗口 ＋ `uniq -c`（✓）。回查见 §5 ✓

D0: 本档对象 = **C-304-A（假阳性清理）＋ C-304-B（四零命中族存在性核验）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① } \text{Schur}=31\ \text{命中}\ \textbf{全部为假阳性}✗✓：\text{均为 Schur 补／Pólya–Schur／Schur 引理／Schur 1911／Schur 圆}✓，\textbf{无一条是 Schur 定理或 Schur 数}✗ \Longrightarrow \textbf{加法组合的 Schur 族＝未覆盖}✓$$
$$\textbf{② } \text{差集}=25\ \text{命中}\ \textbf{全部为假阳性}✗✓：\text{均为档案自有装置（}Delta Lambda = \{\gamma_j - \gamma_k\}✓／\text{指数差集}✓／\text{差分互斥}✓）＋ Barker \text{循环差集}✓ \Longrightarrow \textbf{未覆盖}✓$$
$$\textbf{③ } \text{Kneser}=6\ \textbf{是真实覆盖}⚠️✓：＝\textbf{我们自己的跨素数 Kneser 不等式}✓（E181／E182 ✓）\Longrightarrow \textbf{须引用，不重开}✓$$
$$\textbf{④ 四零命中族核验}✓：\textbf{无一族通过四格}✓ \Longrightarrow \textbf{不升级}✗（\text{但获得一个}\ \textbf{近同构骨架}✓✓，\text{见 §3}✓）$$

---

## §1 C-304-A：Schur 语境清理（✓✓）

| 语境类型 | 是否属"加法禁形" |
|---|---|
| Schur **补**（数值稳定性／Schur balance ✓） | ✗ |
| **Pólya–Schur(–Lax)**（乘子序列／经典理论 ✓） | ✗ |
| **Schur 引理**（`rho(sigma^2) = lambda I` ✓） | ✗ |
| **Schur 1911**（经典 Hilbert 的 `pi` sharp ✓） | ✗ |
| **Schur 圆盘／Schur 界**（`\|c_p\| <= 1` ✓） | ✗ |

$$\Longrightarrow \textbf{Schur 定理／Schur 数族}\ \text{在档案中}\ \textbf{零覆盖}✓（\text{可作候选}✓）$$

## §2 C-304-A：差集语境清理（✓✓）

| 语境类型 | 性质 |
|---|---|
| `Delta Lambda = {gamma_j - gamma_k}`（ζ 零点差集 ✓） | 档案自有装置 ✓ |
| **指数差集**（支撑／带宽论证 ✓） | 档案自有装置 ✓ |
| **差分互斥 ⊗ 平移铺砌** ✓ | 档案自有装置 ✓ |
| **循环差集**（Barker 侧 ✓，C-290 §8／C-300 ✓） | 已登记 ✓ |
| **加性差集**（"档案馆自有装置" ✓ 逐字） | 已登记 ✓ |

$$\Longrightarrow \text{链条}\ \text{局部不可实现} \to \text{两传播} \to \text{非平凡兼容}\ \textbf{未在档案中出现}✓ \Longrightarrow \textbf{不属重包装}✓$$

## §3 C-304-B：四零命中族核验（✓，**四格**✓）

**核验口径** ✓：不是"这领域有什么漂亮定理"✗，而只问四格：**天然 failure ✓／两种现成传播 ✓／非平凡 compatibility ✓**（＋第五格仅记事实 ✓）

| 族 | Failure（文献现成 ✓） | Propagation 1 | Propagation 2 | Compatibility | 判定 |
|---|---|---|---|---|---|
| **sum-free** | ✓ 存在 `x+y=z` 内部解 | **dilation** ✓ 保 sum-free | **translation** ✗ 不保 | **仿射不对称**（缩放保、平移不保 ⚠️） | **不合格** ✗ |
| **van der Waerden** | ✓ 长单色 AP | **dilation** ✓ 保 AP-free | **translation** ✓ 保 AP-free | 未见 FSD 型约束 ⚠️ | **不合格** ✗ |
| **3-term AP / Roth** | ✓ 存在 3-AP | ✓（同上 ✓） | ✓（同上 ✓） | 未见 FSD 型约束 ⚠️ | **不合格** ✗ |
| **Cauchy–Davenport／Kneser** | ✓ 小倍增（`\|A+B\| < min(p, \|A\|+\|B\|-1)`） | **translation** ✓ 保 `\|A+B\|` ✓ | **dilation** ✓ 保 `\|A+B\|` ✓ | ⭐ **Kneser：失败 ⟹ 周期性（stabilizer）⟹ 下降** ✓✓ | **近同构骨架** ⚠️✓ |

- **合格判据** ✓✓：四格全 YES ⟹ 才升级 ✓；本例**无一族**四格全 YES ✗✓
- **诚实标注** ⚠️：上表 propagation／compatibility 列为**我方判读**✓，非逐字核到的文献定理 ✗（`Kneser`／Dyson `e`-变换属标准文献 ✓，但本档未逐字取得原文 ✓）

## §4 ⭐ 近同构骨架（✓✓，**本刀最有价值输出** ✓）

$$\boxed{\text{\textbf{小倍增（failure）}} \Longrightarrow \text{\textbf{周期性／stabilizer（symmetry）}} \Longrightarrow \text{\textbf{按周期下降（descent，Dyson } e\text{-变换）}}✓✓}$$
$$\textbf{与 FSD 的关系}✓：\text{它命中}\ \textbf{FSD 的外骨架}✓（\text{failure} \to \text{symmetry} \to \text{descent}✓）；$$
$$\qquad \textbf{但缺 FSD 的内层}✗✓：\text{两个}\ \textbf{具体 defect}＋\text{其}\ \textbf{commuting compatibility}✗（\text{Liouville 侧的}\ A(x),B(x)\ \text{角色}✓）$$
$$\Longrightarrow \text{登记为}\ \textbf{近同构骨架}✓，\textbf{不得}登记为 FSD 实例 ✗$$

## §5 边界与回查（✓）

- **本阶段未碰 RH** ✓✓：无 RH 映射 ✗、无 defect 设计 ✗、无候选优先级评价 ✗
- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：四族已全部排除 ✗（仅"未通过四格"✓）；Kneser 骨架＝FSD ✗；Schur 族已覆盖 ✗
- **本档新增词**：`假阳性清理`／`近同构骨架`（0 命中 ✓）
