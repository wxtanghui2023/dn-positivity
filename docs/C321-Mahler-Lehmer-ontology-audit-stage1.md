已查地图（**先查后写**）：`C-320`（C-314 清单走完 ✓；M=5 保持 OPEN/AUDIT ✓）、`C-292`（四份深审回执：Lehmer 档 ✓✓，含出处／常数／year 冲突／层级纪律 ✓）、`C-289`／`C-290`（候选池 ＋ 事实审计卡 ✓）。回查见 §8 ✓

D0: 本档对象 = **C-321：Mahler／Lehmer 本体审计（第一阶段）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① 本体审计第一阶段完成}✓：\text{按}\ \text{Problem} \to \text{Structure} \to \text{Existing theorem／identity} \to \text{genuine unresolved interface}\ \text{推进}✓$$
$$\textbf{② 结构丰富且}\ \textbf{内禀}✓✓：\text{对象为}\ \textbf{代数整数的乘法动力学}✓，\textbf{不是} 有限整数频率三角}✗／\textbf{不是} B\&B 箱}✗／\textbf{不是} divisor 局部指数向量}✗$$
$$\textbf{③ 现成非平凡兼容关系}\ \textbf{存在}✓：\text{Jensen 恒等式}✓／\text{Kronecker 刚性}✓／\text{Smyth 二分}✓／\text{Northcott 有限性}✓／\text{Boyd 型}L\text{-值链接}✓$$
$$\textbf{④ 不预设}\ RH\ \text{接口}✓；\text{有效出口包括}\ \text{「独立且有趣，但无}\ RH\ \text{接口」}✓✓$$

## §1 Problem（✓，精确表述 ✓）

$$\textbf{Lehmer 问题}✓（Lehmer 1933, Ann. of Math. 34(3) 461--479✓，DOI 10.2307/1968172✓）：\exists \varepsilon > 0\ \text{使一切非分圆}\ P \in \mathbb{Z}[x]\ \text{满足}\ M(P) \ge 1 + \varepsilon✓$$
$$\textbf{等价形式}✓✓：\text{①}\ 1\ \text{不是 Mahler 测度集合的}\ \textbf{极限点}✓；\text{② 高度形式}✓：\exists c > 0:\ h(x) \ge c\cdot \deg(x)✓（x\ \text{非单位根}✓）$$
$$\textbf{关键量化结构}✓✓：\text{固定次数}\ d\ \text{时}\ \inf\{M(P)\}\ > 1\ \textbf{自动成立}✓（\text{Northcott 有限性}✓）\ \Longrightarrow \text{本题}\ \textbf{本质是}\ \deg \to \infty\ \text{的渐近问题}✓✓$$

## §2 Structure（✓✓，内部结构 ✓）

$$\textbf{对象}✓：M(P) = \prod_i \max(1, |\alpha_i|)✓；\text{等价积分形}✓：M(P) = \exp\left(\frac{1}{2\pi}\int_0^{2\pi} \log|P(e^{i\theta})|\,d\theta\right)✓（\text{由}\ \textbf{Jensen}✓\ \text{等价}✓）$$
$$\textbf{基本性质}✓：\textbf{乘性}✓\ M(PQ) = M(P)M(Q)；\log M \ge 0✓；\ M(P) = 0 \iff P = x^k \times \text{分圆}✓（\textbf{Kronecker}✓）$$
$$\textbf{高度联系}✓：h(\alpha) = \frac{1}{\deg \alpha}\log M(\alpha)✓；\ \text{house}(\alpha) \le M(\alpha)✓$$
$$\textbf{核心结构}✓✓：\text{对代数整数，}\ \prod_v |\alpha|_v = 1✓（\textbf{乘积公式}✓）\ \Longrightarrow \ M\ \text{恰是}\ \textbf{阿基米德位的贡献}✓✓ \Longrightarrow \text{它是}\ \textbf{加性高度对象}✓，\text{与}\ \textbf{Galois 作用} \text{天然相容}✓$$
$$\textbf{Galois 不变性}✓✓：\text{共轭置换不改}\ M✓ \Longrightarrow M\ \text{是}\ \textbf{Galois 不变量}✓$$

## §3 Existing theorem／identity（✓，层级已核 ✓）

| 结果 | 层级 |
|---|---|
| **Smyth 1971** ✓：非互反 ⟹ `M >= theta_0 = 1.324717957...`（最小 Pisot，Siegel 1944 ✓）；**Lehmer 被归约到互反情形** ✓✓ | 定理（完整解决该子类 ✓） |
| **Dobrowolski 1979** ✓：`log M > c (loglog d / log d)^3`，原常数 `c = 1/1200` ✓ | 定理（**一般最优已知下界** ✓） |
| **Voutier 1996** ✓：显式化 `1 + (1/4)(loglog D / log D)^3` ✓ | 定理 ✓ |
| **Borwein–Dobrowolski–Mossinghoff 2007** ✓：奇系数类 `log M >= (log 5)/4 (1 - 1/n)` ✓ | 定理 ✓ |
| **Borwein–Hare–Mossinghoff 2004** ✓：奇系数＋非互反 ⟹ 最优常数 `phi` ✓ | 定理 ✓ |
| **次数 <= 40 已穷尽** ✓（Flammang 等 2006 ✓；Mossinghoff–Rhin–Wu 2008 ✓） | 计算型结论 ✓ |
| **Lehmer 十次多项式** ✓ `M = 1.176280818...` | **构造／例，非定理** ✗✓ |
| **Breuillard 2011**（Annals 174(2) 1055–1109 ✓） | **类比定理**（线性群高度间隙 ✓），**不解决原猜想** ✗✓ |
| **Breuillard–Varjú 2019** ✓ | 有限域计数**等价重述** ✓ |

## §4 真正的"异常"是什么（✓✓）

$$\textbf{异常}✓✓：\ \text{「存在}\ M\ \text{仅略高于}\ 1\ \text{的非分圆对象」}✓ \Longrightarrow \text{载体}\ \textbf{具体}✓（\text{Lehmer 十次式}✓；次小已知}\ d = 18,\ M = 1.18836815✓）$$
$$\textbf{结构来源}✓✓：\ \textbf{Salem 数}✓（\text{全部共轭模} \le 1✓，\text{且至少一个恰在单位圆上}✓）\ \Longrightarrow \text{异常＝}\ \textbf{近 Salem 配置}✓✓$$
$$\textbf{且}\ \textbf{内禀}✓✓：\text{无需参照模型}✓（\text{与}\ C\text{-309 零点间距的「模型相对」形成对比}✓✓）$$

## §5 现成非平凡兼容关系 ＋ 立即排除（✓✓）

**存在** ✓：① **Jensen** ✓（积分形与乘积形相等的恒等式 ✓）；② **Kronecker 刚性** ✓（`m = 0` 的完全刻画 ✓）；③ **Smyth 二分** ✓（非互反／互反之分是**真的结构分界** ✓✓）；④ **Northcott 有限性** ✓（逐次数自动有下界 ⟹ 说明**为何必须次数无界** ✓✓）；⑤ **Boyd 型链接** ✓（特定多项式的测度 ↔ `L`-值 ✓，`[待逐字核]`⚠️）
**立即排除** ✗✓：仅**不同表述**者不计入 ✓（积分形 vs 乘积形＝同一对象 ✓；`h = (1/deg)log M`＝换语言 ✓；有限域计数等价＝重述 ✓）

## §6 genuine unresolved interface（✓）

$$\textbf{未解决核心}✓：\ \text{「测度集合在}\ 1\ \text{之上是否有正间隙」}✓；\text{一般无条件下界仍停在}\ (\log\log d / \log d)^3✓，\textbf{1979 年至今未改进}✓$$
$$\textbf{未决子类}✓：\ \textbf{互反情形}✓（Smyth 已解决非互反 ✓）\Longrightarrow \text{真正的开放面}\ \textbf{收窄到互反／Salem 侧}✓✓$$

## §7 RH 接口事实栏（**仅记事实，不评分**✓）

- **`L`-值侧** ✓：Boyd 型猜想把特定多项式测度与 `L`-值相连 ✓（属**值面** ✓，`[待逐字核]`⚠️）
- **与档案的已知接触面** ✓：Deninger 型解释（测度作为 regulator／Deligne 上同调 ✓）在档案中已有条目 ✓ ⟹ **引用，不重开** ✓
- **本档不作断言** ✗：未见／未见即不写"无接口" ✗✓（第一阶段的出口允许"独立且有趣、无 RH 接口" ✓✓）

## §8 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 本体审计     命中文件数=0    :: 
技术词 乘法动力学  命中文件数=0    :: 
技术词 近Salem配置   命中文件数=0    :: 
技术词 加性高度     命中文件数=0    :: 
```
- 本档新增 ✓：`本体审计`／`近 Salem 配置`（依上表判 ✓）；`加法高度`／`乘法动力学` 视命中判 ✓
- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：Lehmer 问题已解决 ✗；Lehmer 十次式＝定理 ✗；Breuillard 2011 解决原猜想 ✗；已有 RH bridge ✗
- **M=5** ✓：仍保持 **OPEN/AUDIT** ✓，**暂不**当作下一条 RH 主线 ✗✓
