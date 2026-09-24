已查地图：命中（`TARGET-L9-five-items-answered`）⟹ 引用，不开新案
D0: 本档对象 = `q11` 目录探测（入口 A 第一步的取源进展）：已定位族实例文件；族定义/17 类尚未取
D1: 0 （[REVIEW] 轮次：取源，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`q11` 目录探测（入口 A 第一步 · 部分完成）**

## §1 已确认（GitHub API 实测）

```
【路径】**`problems/covering/compute/q11/`** ✓（目录存在）
【已见文件（按名排列，列表被截断）】**`H_r10_n54_fibered.txt`**（size 1305）、**`H_r11_n86_fibered.txt`** … ⟹ **族实例＝`H_r{X}_n{Y}_fibered.txt` 命名** ✓✓
【⟹ 推论】 该族实例**以显式 `H` 文件形式存放** ⟹ **入口 A 的"显式有限规格"有实体可依** ✓
【API 取限】 `contents` 端点可用但**每次只回约 2000–2500 字符** ⟹ **须分页/多次取**（本档只取到前 2 项）✓
```

## §2 尚未取到（下一轮唯一任务）

```
**(i)** `q11` 目录**完整清单**（定位族定义脚本／README／17 类相关文件）✓
**(ii)** **族定义**：`H=H(Q,K,\mathcal L)` 中 quotient／kernel／每非零点 column／kernel block 参数的**精确定义** ✓
**(iii)** `R=2` 条件化成 **`PG` 上 line-colouring** 的**等价表述** ✓
**(iv)** **17 个 kernel-block classes** 的参数、等价关系、族内穷尽性论证 ✓
**(v)** **"14 missing incidences"** 的**精确对象**（非 annealing 数值）✓
**(vi)** 汇总为 `\mathcal F^{(9,38)}=\bigcup_{i=1}^{17}\mathcal F_i` 的 **SAT/exact 规格**（变量/约束/对称商）✓
【⛔ 本轮不碰（照录）】 `r=10,n=49`｜`r=11` 的 order `11/17/23`｜`q10` 的 order-7 自同构｜族外搜索｜SAT 求解 ✓
【边界】 §1 为 **GitHub API 一手**（2026-09-24）；§2 为**待办清单**（未完成）；未制造候选／未启动搜索／未碰 RH。
