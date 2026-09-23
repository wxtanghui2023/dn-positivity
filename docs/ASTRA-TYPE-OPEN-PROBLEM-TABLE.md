已查地图：命中（`ENGINE-X-PROBLEM-pilot-v2-no-RH-ancestry`／`EXTERNAL-DEMAND-SCAN-cross-domain`／`CORRECTION-idea-first-not-capacity`）⟹ **引用，不开新案** ✓
D0: 本档对象 = `ASTRA-TYPE` 开放问题表（11 字段 × 6 候选）＋ 两条**新查出的关键事实**
D1: 0 （`[REVIEW]` 轮次：需求扫描，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ASTRA-TYPE OPEN PROBLEM TABLE`**

## §0 ⚠️ **两条决定性新事实（本档核心，逐字）**

```
【事实 1 —— `668` 已被吃掉】 MathWorld 逐字："**Epoch AI (2026) reported that L. Alpöge, P. Voinov, and S. Reynolds-Haertle had announced constructions obtained with Claude for the twelve previously unresolved orders below 2000: 668, 716, 892, 1132, …**" ⟹ **2026-08，AI 团队把该格全部关掉** ✓✓
【事实 2 —— Ramsey 上界正被算力推进】 逐字："**Angeltveit–McKay … We prove that the Ramsey number R(5,5) is less than or equal to 46. The proof uses a combination of linear programming and checking a large number of cases by computer.**"（JGT 2026）✓✓；同线 `R(3,10)\le42`（2017，计算）✓
【⟹ 含义（最重要）】 `Astra-type` 形态**是真的**，但其**开采方式在当前是"算力密集"**：**LP ＋ 巨量情况枚举**；而**算力富集的 AI 团队正在快速收割**"有明显数字缺口"的格 ✓✓
```

## §1 **表（11 字段压缩；6 候选 × 四个优先类）**

| 问题 | 当前最佳 | 缺口 | 为何仍 OPEN | 可验证输出 | 我们能做什么 | 新机制？ | 规模 | Prior art | 48h 第一刀 | Go/No-Go |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| **Hadamard `n=668`**（编码/组合设计） | ⛔ **2026-08 已被 AI 团队关闭**（<2000 全部补齐） | — | 只剩**一般猜想** | 矩阵本身 | — | — | — | 极厚 | 无 | ⛔ **No-Go（格已被吃）** |
| **`R(5,5)` 下界 `43\to44`**（极值图论） | `[43,48]`；上界 2026 由 `LP+巨量枚举` 推到 `46` | 需 `44` 顶点 Ramsey 图 | 903 边的构造/穷尽 | 一个图（**自身即证书**） | `C2`（枚举）＋`C1`（证书） | 无 | 巨 | 极厚（Exoo／McKay／SAT） | 无 | ⛔ No-Go |
| **`R(3,k)` 上界**（极值图论） | `R(3,10)\le42` 等，**由 `e(3,k,n)` 精确值推进** | 逐 `1` 改进 | 依赖 `e(3,k,n)` 精确值与枚举 | 精确值＋枚举完备性 | `C2`＋`C1` | 无 | 大 | 极厚（Radziszowski DS1） | 无 | ⛔ No-Go（我们更慢） |
| **编码表项 `A(n,d)`**（编码论） | 表值部分精确、部分带界 | 某些小 `(n,d)` 精确值 | 上下界差 `1`，需构造/穷尽 | 码或穷尽证书 | `C2`＋`C1` | 无 | 中 | 厚（Brouwer 表） | 无 | ⚠️ 可能但**价值密度低** |
| **圆装填/Thomson 型**（可验证数值优化） | 小 `n` 已有**严格证书** | 更大 `n` 未认证 | 证书构造难（需分支-界＋区间） | 区间证书 | `C1`＋`C5` | ⚠️ 方法属既有 | 中 | 厚（Packomania 系） | 无 | ⛔ No-Go |
| **cap set／Zarankiewicz 小值**（有限组合） | 部分精确、部分界 | 小参数精确值 | 枚举规模＋对称 | 构造/穷尽证书 | `C2`＋`C1` | 无 | 大 | 活跃（AI 算力队） | 无 | ⛔ No-Go |

## §2 **结论（诚实，不美化）**

```
【表本身成立】 `Astra-type` 六条**全部是真实开放问题**，且**全部是"可测量增量"型** ✓ —— 形态判断正确 ✓
【但 Go/No-Go 全为否或低】**原因不是"缺想法"单一**：**(i)** 明显数字缺口**正被算力富集的 AI 团队快速收割**（`668` 已关；Ramsey 上界由 `LP＋巨量枚举` 推进）✓；**(ii)** 其余格子需要**同等巨量枚举**或**新构造想法**；**(iii)** 我们唯一可能的差异化（**证书形状重述**）**尚无一个活靶** ✓✓
【⟹ 精确处置】$$\boxed{\text{Astra-type 形态正确；但在当前竞争格局下，我们的 Go/No-Go 结论是 No-Go}}$$ ✓
【与您 §"这解释了我们为什么撞墙"一致】 RH＝`zero-slack global`；Astra 型＝`bound improvement / construction / finite certificate` ✓ —— 我们的失败**在形态上得到解释** ✓✓
【唯一的例外通道（若您要）】 选**一格**，做**长期（月级）**：只靠"证书形状重述"去赢一次枚举（＝`k=4` 的放大版），接受高失败率 ✓
【边界】 ⚠️ §0 两条事实为**逐字 snippet**（MathWorld／JGT 题录）；§1 各格"当前最佳/为何 OPEN/prior art"按**档级**（未逐字核）⟹ 采用前须核；⛔ 未制造候选／未启动搜索／未改状态／未碰 RH／未碰数论 ✓
```
