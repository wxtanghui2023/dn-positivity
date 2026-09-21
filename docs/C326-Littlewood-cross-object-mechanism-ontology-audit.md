已查地图（**先查后写**）：`C-325`（Barker 跨对象审计：恒等式级联合约束资产 ✓）、`C-311`（Littlewood 四格：**性质型 failure ＋ 只有对合等距** ✓，**本轮不重审** ✓）、`C-292`（Littlewood 深审回执：`K_n`／`L_n` 分离 ＋ Kahane 1980 ＋ 2020 定理精确出处 ＋ Saffari–Smith 1988 含错 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-326：Littlewood 跨对象机制本体审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（三条 ✓✓）

$$\textbf{① 出口}✓：\boxed{\textbf{NO SUCH COMPATIBILITY FOUND}}✓（\text{就}\ \textbf{操作级} \text{而言}✓，\text{与}\ C\text{-311 一致}✓）$$
$$\textbf{② 资产}✓✓：\text{存在}\ \textbf{恒等式级联合约束}✓（\text{Fejér／Wiener–Khinchin}✓；\text{Golay 配对}✓；\text{Barker} \Longrightarrow \text{上界}✓）\ —— \text{与 Barker 侧}\ \textbf{同类}✓，\textbf{非}操作级✗✓$$
$$\textbf{③ 纪律}✓✓：\textbf{不}重审 `C-311`✗；\textbf{不}触碰 RH✗；\textbf{不}建新框架✗$$

## §1 ① 精确定义（✓✓，防混淆 ✓）

$$\textbf{两类严格分开}✓✓：L_n = \{\sum_{k=0}^{n-1} a_k z^k : a_k \in \{\pm1\}\}✓（\text{Littlewood}✓）；K_n ＝ \text{unimodular}✓（a_k \in \mathbb{C},\ |a_k| = 1✓）\ \Longrightarrow L_n \subset K_n✓$$
$$\textbf{flatness 分级}✓：\textbf{flat}✓＝\text{双侧}\ (1 \pm \varepsilon)\sqrt{n}✓；\textbf{ultraflat}✓＝\varepsilon_n \to 0✓；\textbf{bounded flatness}✓（\text{Littlewood 1966}✓）＝\exists 0 < \delta < \Delta✓，\delta\sqrt{n} \le |P| \le \Delta\sqrt{n}✓$$
$$\textbf{Parseval}✓：\frac{1}{2\pi}\int_0^{2\pi} |P|^2 = n✓ \Longrightarrow |P| \equiv \sqrt{n}\ \textbf{不可能}✗（n \ge 1✓）$$
$$\textbf{归一化陷阱}✓⚠️：\text{BBM 用}\ \sqrt{n}\ \text{对应次数}\ n（即\ n+1\ \text{个系数}✓），\text{而 ultraflat 定义用}\ \sqrt{n+1}✓ \Longrightarrow \textbf{不得混用}✗✓$$

## §2 ② 关系性质分层（✓✓，逐项标 ✓）

| 结果 | 层级 |
|---|---|
| **Kahane 1980** ✓：`K_n` 上 ultraflat **存在** ✓ | **定理（在 `K_n` 上）** ✓✓ —— **不下降为 `L_n` 的结论** ✗✓ |
| **BBM 2020**（Annals 192(3):977–1004 ✓）：`L_n` 上 **bounded flatness 存在** ✓ | **定理（仅 bounded ✓）** ✗✓ —— **不蕴含 ultraflat** ✗✓ |
| **Shapiro／Rudin** ✓：`sup = O(\sqrt{n})` 的**显式构造** ✓ | **构造** ✓（**非传播** ✗✓） |
| **Beck 1991／Bombieri–Bourgain 2009** ✓ | **构造／在 `K_n` 上的定理** ✓ |
| **Saffari–Smith 1988** ✓：曾宣称 `L_n` 上不存在 ultraflat ✓ | **含错，作者自认** ✓ ⟹ **问题仍开放** ✓ |
| **Erdős 在 `L_n` 上的猜想** ✓ | **猜想** ✓（`[待核]`⚠️：问题编号 22 vs 26 并存 ✓） |
| Littlewood 1966 猜想 ✓ | **已定理化** ✓（BBM 2020✓） |
| 小次数 flatness 表 ✓ | **数值** ✓ |

$$\textbf{防误写}✓✓：\textbf{「存在一个构造」} \ne \textbf{「传播机制」}✗✓$$

## §3 ③ 跨对象操作（✓）

$$\textbf{接受者}✓：\text{① 系数侧} \to \textbf{自相关侧}✓（\text{非周期自相关} C_k✓）\ —— \text{已有对象对应}✓；\text{② 自相关侧} \to \textbf{谱侧}✓（\text{见 §4 恒等式}✓）；\text{③} \to \textbf{Golay 互补对}✓（|P|^2 + |Q|^2 ＝ \text{常数}✓，Golay 1951✓，\text{已有结构}✓）$$
$$\textbf{已在} C\text{-311 判掉、本轮不复算}✗✓：\text{互反} P \mapsto P^*✓（\text{对合等距}✗）；P \mapsto P(z^m)✓（\textbf{离开} \pm1\ \text{类}✗）；\text{整体取负}✗$$

## §4 ④ ⭐ compatibility（✓✓，本档核心 ✓）

$$\textbf{恒等式级联合约束存在}✓✓：\boxed{|P(e^{i\theta})|^2 = \sum_{k} C_k e^{ik\theta}}✓（\textbf{Fejér／Wiener–Khinchin}✓）\ \Longrightarrow \text{系数侧约束}\ \textbf{强制} \text{投到谱侧}✓$$
$$\qquad \text{实例}✓：\text{Barker 型}\ |C_k| \le 1✓ \Longrightarrow |P|^2 \le n + 2\sum_{k \ge 1} |C_k|✓ \Longrightarrow \textbf{上界}✓（\text{跨问题联系}✓✓）；\text{反之 flatness}\ \textbf{限制} \text{自相关平均}✓$$
$$\qquad \text{Golay}✓：|P|^2 + |Q|^2 ＝ \text{常数}✓ \Longrightarrow \text{两多项式的}\ \textbf{联合} \text{谱约束}✓✓$$
$$\textbf{文献已用}✓：\text{BBM 2020 的证明}\ \textbf{用到}\ \text{Rudin–Shapiro 与组合／差异法}✓ \Longrightarrow \text{跨对象结构确实参与证明}✓$$
$$\textbf{但}✓✗：\text{以上均为}\ \textbf{恒等式级}✓（\text{表示或定义式}✓），\textbf{不是}\ \textbf{操作级兼容}✗✓ \Longrightarrow \textbf{不}\ \text{计为兼容律}✗✓$$

## §5 出口与纪律（✓✓）

$$\boxed{\textbf{NO SUCH COMPATIBILITY FOUND}}✓（\text{操作级}✓）$$
$$\textbf{资产}✓✓：\text{Littlewood 内部跨对象资产}＝\text{恒等式级联合约束}✓（\text{Fejér 恒等式}✓；\text{Golay 配对}✓；\text{Barker} \to \text{上界}✓）\ \Longrightarrow \textbf{不}触碰 RH✗✓$$
$$\textbf{队列}✓（\text{唐先生固定}✓）：\text{C-325 Barker 封口}✓ \to \text{C-326 Littlewood}✓ \to \textbf{Lonely Runner}✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 跨对象机制层 命中文件数=0    :: 
技术词 恒等式级联合约束 命中文件数=1    :: ./C325-Barker-cross-object-mechanism-ontology-audit.md 
技术词 谱对应        命中文件数=10   :: ./ASSETS-REGISTRY.md ./p2p-anticircular-audit.md ./V155-C6-definition-audit-and-nine-arrow-forms-exhaustion.md 
```
- 本档新增 ✓：`跨对象机制层`／`谱对应`（依上表判 ✓）
- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：`K_n` 结论下降为 `L_n` ✗；2020 定理＝ultraflat ✗；恒等式级＝操作级 ✗；Littlewood 已找到兼容律 ✗
