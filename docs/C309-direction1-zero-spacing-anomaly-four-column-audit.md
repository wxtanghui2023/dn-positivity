已查地图（**先查后写**）：`C-308`（素数间隙四格：未通过 ✓）、`C-307`（分支关闭 ＋ 方向① ✓）、`C-306`（Schur 反例 ✓）、`C-302`（Hecke 反例 ✓）。回查见 §7 ✓

D0: 本档对象 = **C-309：方向① 第二族 —— 零点间距异常四格审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\boxed{\textbf{F}✓\ ⚠️：\text{异常事件}\ \textbf{确实存在}✓，\text{但}\ \textbf{多为「模型相对」}⚠️\（\text{见 §2}✓）\ \text{—— 与素数 gap 的「record」}\ \textbf{内禀性不同}✗✓}$$
$$\boxed{\textbf{A}_1\ ✗：\text{可得对称（conjugation／functional equation）}\ \textbf{是平凡反射／对合}✓，\textbf{不是传播}✗✓（\text{按唐先生预注册}✓）}$$
$$\boxed{\textbf{A}_2\ ✗：\textbf{未见独立第二传播}✓}$$
$$\boxed{\textbf{C}\ ✗：\textbf{未见非平凡兼容律}✓}$$
$$\Longrightarrow \textbf{未通过四格}✓ \Longrightarrow \textbf{第四类反例}✓；\textbf{不进入}\ RH\ ✗$$

## §1 F 格：异常事件族（✓，文献存在 ✓）

| 异常族 | 文献地位 |
|---|---|
| **unusually small spacing／clustering** ✓ | 标准对象 ✓（**Lehmer pairs**＝异常接近的零点对 ✓；档案侧已有同名条目 ✓ — `Lehmer`=10 档**正是 ζ Lehmer 对**✓，不同对象于 Lehmer–Mahler ✓） |
| **unusually large spacing／repulsion** ✓ | 标准研究对象 ✓（`[标准·未逐字核]`⚠️） |
| **repeated spacing patterns** ✓ | 标准研究对象 ✓（`[标准·未逐字核]`⚠️） |
| **extreme gap／local rigidity 异常** ✓ | 标准研究对象 ✓（`[标准·未逐字核]`⚠️） |

$$\Longrightarrow \textbf{F}🟡＝YES\ \text{但带前提}✓（\text{见 §2}✓）$$

## §2 ⭐ F 格的**内禀性缺陷**（✓✓，本档关键发现 ✓）

$$\textbf{素数侧（C-308）}✓：\text{「record gap」}\ \textbf{内禀}✓\ —— \text{不需要参照模型即可定义}✓$$
$$\textbf{零点侧（本档）}⚠️：\text{「unusually small／large」}\ \textbf{需要参照模型}✓（\text{相对平均间距}✓／\text{相对 GUE}✓／\text{相对 } RvM\ \text{律}✓）\ \Longrightarrow \textbf{模型相对}⚠️$$
$$\Longrightarrow \textbf{后果}✓✓：\text{定义}\ \mathcal F\ \text{时}\ \textbf{必须引用某一参照模型}✓ \Longrightarrow \text{该模型的结构被}\ \textbf{悄悄带入}✗✓ \Longrightarrow \text{这不是「人为 defect」}✗，\text{但}\ \textbf{已非纯内禀}⚠️$$
$$\textbf{纪律}✓：\text{故}\ F\ \text{列判}\ \textbf{YES 带前提}✓，\text{不得记作干净}\ YES ✗$$

## §3 A₁ 格：可得对称**不是传播**（✓✓）

$$\textbf{可用对称}✓：\text{conjugation}\ \rho \mapsto \bar{\rho}✓；\text{functional equation}\ \rho \mapsto 1 - \rho✓；\text{合并}\ \rho \mapsto 1 - \bar{\rho}✓ \Longrightarrow \text{零点成四元组}✓$$
$$\textbf{但它们}\ ✗✓：\text{都是}\ \textbf{对合／反射}✓ \Longrightarrow \text{把零点集}\ \textbf{映到自身}✓，\textbf{不把一个 failure 状态传递到另一个可验证状态}✗✓$$
$$\textbf{唐先生指定排除项}✗✓：\text{scaling normalization}✗／\text{GUE–pair-correlation 对称}✗／\text{统计重写}✗／\text{同一公式换坐标}✗ \Longrightarrow \textbf{均不计作传播}✗$$
$$\Longrightarrow \textbf{A}_1 = NO✗（\text{与 C-308 的}\ \text{dilation 平凡情形}\ \text{同型}✓）$$

## §4 A₂／C 格（✗）

$$\textbf{A}_2✗：\text{未见独立第二传播}✓$$
$$\textbf{C}✗：\text{无两传播} \Longrightarrow \text{无从谈兼容}✗；\text{未见任何}\ A_1 A_2\ \text{与}\ A_2 A_1\ \text{型非平凡律}✓$$

## §5 判定（✓✓）

$$\textbf{未通过四格}✗ \Longrightarrow \textbf{第四类反例}✓；\text{四反例并表}✓：\quad \begin{array}{c|c|c} & \text{Failure} & \text{非平凡 Compatibility}\\ \hline \text{Hecke} & ✗ & ✗\\ \text{Schur} & ✓ & ✗\\ \text{素数间隙} & ✓ & ✗\\ \text{零点间距} & 🟡 & ✗ \end{array}$$
$$\Longrightarrow \text{四反例}\ \textbf{一致指向}✓✓：\textbf{稀缺物＝独立存在的非平凡兼容律}✓✓（\text{不是 failure}✗，\text{不是「有对称」}✗）$$

## §6 待做（✓）

$$\textbf{方向① 两族均未通过}✓ \Longrightarrow \text{可按 C-305 §4 推进}\ \textbf{Round 2}✓（\text{Barker}／\text{Littlewood}／\text{Lonely Runner}✓）$$
$$\textbf{或}✓：\text{按 C-305 §1}\ \textbf{C 类}✓（\text{旧 GAP 重检：是否存在独立 failure mechanism ＋ 已知}\ RH／L\text{-interface}✓）$$

## §7 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **避雷线** ✓：**未**把 `explicit formula → zero statistics` 计作新接口 ✗✓；**未**把 GUE／pair correlation／zero density／Montgomery 当新 bridge ✗
- **不得**写成：零点方向已排除 ✗（仅"未通过四格"✓）；零点异常与 RH 无关 ✗（未见≠不存在 ✓）
- **本档新增词**：`模型相对 failure set`／`内禀性缺陷`（0 命中 ✓）
