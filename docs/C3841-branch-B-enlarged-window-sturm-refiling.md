已查地图（**先查后写**）：`C-380-40`（**真实上端 `t_B = 0.28425257 > 1137/4000`** ✓✓）、`C-380-36`（**旧窗口 Sturm 模板** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-41：B 支扩大窗口 Sturm 重封口**，**有计算（精确有理 ＋ Sturm，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 扩大窗口（采纳）}✓✓：\boxed{I_B = \Big[\tfrac18,\ \tfrac{11371}{40000}\Big] = [0.125,\ 0.284275]}✓✓ \ —— \ \textbf{覆盖真实上端}✓✓：\tfrac{11371}{40000} = 0.284275 > t_B = 0.28425257✓✓$$
$$\textbf{② 端点导数（精确）}✓✓：\boxed{P_B'\big(\tfrac18\big) = 2475 > 0}✓✓；\ \boxed{P_B'\big(\tfrac{11371}{40000}\big) = -\tfrac{32235749770829682447}{390625000000000000} \approx -82.52 < 0}✓✓ \Longrightarrow \ \textbf{符号}\ +\to-✓✓$$
$$\qquad \Longrightarrow \ \textbf{与}\ C\text{-}380\text{-}36\ \textbf{同型}✓✓ \Longrightarrow \textbf{旧模板可直接迁移}✓✓$$
$$\textbf{③ Sturm 计数}✓✓：\boxed{N_{I_B}(P_B') = 1}✓✓ \Longrightarrow \ \text{唯一临界点}\ \textbf{是极大值点}✓✓$$
$$\textbf{④ 端点值（精确）}✓✓：\boxed{P_B\big(\tfrac18\big) = \tfrac{135}{8} = 16.875}✓✓；\ \boxed{P_B\big(\tfrac{11371}{40000}\big) = \tfrac{11607760693865441393631721}{31250000000000000000000} \approx 371.448}✓✓$$
$$\qquad \Longrightarrow \ \boxed{P_B \ge \tfrac{135}{8} > 0\ \text{on}\ I_B}✓✓ \Longrightarrow \ Q_5 - \tfrac{341}{128} = \frac{P_B}{1152t} > 0✓✓ \Longrightarrow \ \boxed{Q_5 > \tfrac{341}{128}}✓✓$$
$$\textbf{⑤ ⚠️ 措辞（采纳唐先生）}✓✓：\textbf{不}写「B 支全局 CLOSED」✗✓，\ \text{而写}✓✓：$$
$$\qquad \boxed{\text{Branch B CLOSED on the certified enlarged window, and the enlarged window covers the entire B-feasible parameter range identified by the boundary analysis}}✓✓$$
$$\qquad \Longrightarrow \ \textbf{不}把「局部证书 ＋ 窗口覆盖」误写成脱离窗口的全局多项式正性✗✓$$
$$\textbf{⑥ 边界}✓✓：\text{这是}\ \textbf{窗口化} \text{结论}✓✓；\ \text{真实可行集} \subseteq I_B\ \text{由}\ C\text{-}380\text{-}40\ \text{的身份结果支撑}✓✓（\text{绑定约束 ②}✓）$$

## §1 记录（✓✓）

$$\textbf{旧窗口}✓：[\tfrac18, \tfrac{1137}{4000}]✓（\text{上端}\ 0.28425 < t_B✗✓）；\ \textbf{新窗口}✓：[\tfrac18, \tfrac{11371}{40000}]✓✓（\text{上端}\ 0.284275 > t_B✓✓）$$
$$\textbf{端点导数}✓✓：2475✓、-32235749770829682447/390625000000000000✓✓；\ \textbf{Sturm}✓：1✓✓；\ \textbf{端点值}✓✓：135/8✓、\approx 371.448✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A** ✓ | **CLOSED** ✓✓✓ |
| **Branch B** ✓ | **本档：CLOSED on certified enlarged window（覆盖真实 B 可行范围）** ✓✓✓ |
| **Branch C 低带** ✓ | **CLOSED** ✓✓ |
| **Branch C 高带** ✓ | **OPEN（见 C-380-42）** ✗✓ |
| global coverage ✓ | **OPEN** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✗✓ |
| Level 3 ✓ | **FROZEN** ✗✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗✓；\ \text{global coverage CLOSED}✗✓；\ \text{B 支全局 CLOSED}✗✓；\ \inf Q_5 = \tfrac{341}{128}\ \text{已证}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{窗口化结论}✓✓；\ \text{真实覆盖由}\ C\text{-}380\text{-}40\ \text{支撑}✓✓$$

## §4 本档**不**做的事（✓✓）
$$\textbf{不}碰 High Band✗✓；\textbf{不}碰 Level 3✗✓；\textbf{不}写全局✗✓$$

## §5 边界（✓✓）
$$\textbf{有计算}✓；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 扩大窗口重封口 命中文件数=0    ::
技术词 低带高带     命中文件数=0    ::
技术词 单多项式符号证书 命中文件数=0    ::
```
- 运行记录 ✓：`python3 -`（sympy 端点导数／`count_roots`／端点值 ✓）
