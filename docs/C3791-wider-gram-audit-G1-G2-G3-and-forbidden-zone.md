已查地图（**先查后写**）：`C-379`（**`\operatorname{rank}\mathcal G \le 5` 精确化** ✓✓；**倾向 C（4 点探针）** ⚠️）、`C-378`（**出口 B** ✓✓）、`C-341`（`x`-Hankel 秩 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-379.1：更广 Gram 审计（`G1／G2／G3`）＋ 禁区登记**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① } C\text{-}379\ \text{落档为正式资产}✓✓（f3897e5✓）：\ \mathcal G_{mn} = \tfrac12(S_{m+n} + S_{|m-n|})✓，\ \mathcal G \succeq 0✓，\ \operatorname{rank}\mathcal G \le 5✓✓$$
$$\qquad \textbf{要点强调}✓✓：\det \mathcal G_{1:6} = 0\ \textbf{不是}数值现象✗✓，\ \text{而是}\ \textbf{五个节点导致的精确秩约束}✓✓$$
$$\qquad \textbf{与}\ C\text{-}341\ \text{的关系}✓✓：\text{同源于「5 个节点」}✓，\ \textbf{但} \text{这里是}\ \textbf{Chebyshev 乘法结构下的新表达}✓✓（T_mT_n✓，非\ x^ix^j✓）$$
$$\textbf{② ⭐ 自我约束（采纳唐先生）}✓✓：\text{目前只能得}\ \boxed{\text{低阶 Gram}\ \textbf{尚未显示直接矛盾}}✓✓；\ \textbf{不能}得\ \boxed{\text{低阶 Gram}\ \textbf{不可能}产生矛盾}✗✓$$
$$\textbf{③ ⭐ 计数纪律（本档核心）}✓✓：\ \boxed{\text{「7 个}\ 6 \times 6\ \text{恒等式」}\ \ne\ \text{「7 个有效独立约束」}}✓✓$$
$$\qquad \text{它们来自}\ \operatorname{rank} \le 5✓，\ \text{但在}\ S_k\ \text{坐标中}\ \textbf{可能存在代数依赖}✓✓ \Longrightarrow \textbf{须明确计算秩／独立性}✓✓，\ \textbf{不}按「7 条」计数✗✓$$
$$\textbf{④ } C\text{-}379.1\ \text{三层}✓✓：\text{G1}\ \textbf{零式独立性}✓✓（\textbf{不需}数值优化✗✓）；\ \text{G2}\ \textbf{PSD 真正约束强度}✓✓；\ \text{G3}\ \textbf{出口判定}✓✓（\text{见 §1／§2／§3}✓）$$
$$\textbf{⑤ ⭐ 禁区}✓✓：\textbf{不}把\ \operatorname{rank}\mathcal G \le 5\ \textbf{重新包装成「另一个 Hankel 方法」}✗✓$$
$$\qquad \textbf{有价值} \text{的链}✓✓：\ \boxed{T_mT_n \to T_{m+n} + T_{|m-n|} \to \text{跨频 PSD／秩约束} \to \text{奇频放大}}✓✓$$
$$\qquad \textbf{若} \text{最终只得「5 点矩问题的另一种坐标表示」}\ \Longrightarrow \textbf{明确 NO-GO}✓✓；\ \textbf{若} \text{能产生}\ \textbf{以前没有的跨频传播不等式}✓ \Longrightarrow \text{才进}\ C\text{-}380✓✓$$
$$\textbf{⑥ 账本（唐先生口径）}✓✓：C\text{-}379\ \textbf{CLOSED（结构发现）}✓；\ \textbf{Gram 是否构成有效压缩}\ \textbf{OPEN}✓；\ \textbf{Exit C}\ \textbf{未证}✓；\ C\text{-}380\ \textbf{暂不开}✗✓；\ \text{Bridge A}\ \textbf{OPEN}✓；\ H = \varnothing\ \textbf{OPEN}✓$$

## §1 G1：`6 \times 6` 零式的精确独立性（✓✓）

$$\textbf{问题}✓✓：\text{对不同}\ 6 \times 6\ \text{主子式}✓，\ \text{检查它们作为}\ (S_1,\dots,S_{12})\ \text{多项式关系的}\ \textbf{独立秩}✓✓$$
$$\qquad \text{只回答}\ \boxed{\text{C-379 的「7 个零式」究竟提供多少}\ \textbf{真正的新代数信息}}✓✓$$
$$\textbf{手段}✓✓：\textbf{符号}计算（\textbf{不}数值优化✗✓）—— 例如对子式集合求 Jacobian 的秩✓，或求理想成员的独立性✓$$
$$\textbf{可能的两极}✓✓：\text{(i) 独立秩}\ \textbf{大}✓ \Longrightarrow \text{真新信息}✓；\ \text{(ii) 独立秩}\ \textbf{小}✓ \Longrightarrow \text{多为}\ \textbf{坐标重包装}✗✓（\text{触}\ §0⑤\ \text{禁区}✓）$$

## §2 G2：PSD 的真正约束强度（✓✓）

$$\textbf{对象}✓✓：\text{对可行点计算}\ \lambda_{\min}(\mathcal G_I)✓ \ \text{以及适当的}\ \textbf{Schur 补}✓✓（\textbf{不}再盯单个\ 2 \times 2✓）$$
$$\qquad \text{特别看}\ \det \mathcal G_I\ \text{对}\ I \subset \{1,\dots,5\}\ \text{的低阶主块}✓，\ \text{以及由}\ 6 \times 6\ \text{零式消去后的}\ \textbf{剩余 PSD 不等式}✓✓$$
$$\textbf{目标}✓✓：\text{找}\ \textbf{统一正余量}✓ \ \boxed{Q(S_1,\dots,S_{12}) \ge c > 0}✓ \ \text{或者反过来}\ \text{发现所有候选量都可趋近}\ 0✓✓$$
$$\textbf{纪律}✓✓：\textbf{不}用大规模矩阵✗；\textbf{不}做随机采样✗；\textbf{不}重搜 active set✗✓$$

## §3 G3：出口判定（✓✓，只允许三种 ✓）

$$\textbf{B}✓✓：\text{出现}\ \textbf{统一的跨频强制}✓（\text{某些}\ S_k\ \text{或 Gram 组合被迫进入接近}\ \tfrac12✓，\ \text{且}\ \textbf{能自然接到奇频放大}✓） \Longrightarrow \textbf{开}\ C\text{-}380✓✓$$
$$\textbf{C}✓✓：\text{经足够覆盖后，PSD／秩条件在}\ \mathcal C_1\ \text{上}\ \textbf{始终只有零余量}✓、\ \text{且}\ \textbf{没有新的可传播量}✓ \Longrightarrow \textbf{正式写}\ \boxed{C\text{-}379\ \text{Gram 低阶路线 NO-GO}}✓✓$$
$$\qquad \Longrightarrow \text{然后}\ \textbf{才} \text{进入更高阶 moment／Hankel}✓✓$$
$$\textbf{A}✓✓：\text{若直接由 PSD ＋}\ S_k \le \tfrac12\ \text{推出矛盾（}\mathcal C_1 = \varnothing✓） \Longrightarrow \textbf{直接关闭 Bridge A}✓✓$$
$$\textbf{判定原则}✓✓：\text{仅当出现}\ \textbf{统一正余量} \text{或}\ \textbf{统一零余量} \text{时才下结论}✓✓；\ \textbf{不}因少数点下结论✗✓$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}379`✓ | **CLOSED（结构发现）** ✓✓ |
| Gram 是否构成有效压缩 ✓ | **OPEN ← 本档对象** ✓✓ |
| Exit C ✓ | **未证** ✓ |
| `C\text{-}380`（奇频放大）✓ | **暂不开** ✗✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 下一步（✓✓）

$$\textbf{唯一下一刀}✓✓：\ \boxed{\text{只问 Gram／PSD 是否产生「跨频传播量」}}✓✓$$
$$\textbf{不}回节点几何✗✓（\text{C-378 已 CLOSED}✓）；\textbf{不}扩大随机采样✗✓；\textbf{不}上大规模矩阵✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 零式独立性  命中文件数=0    :: 
技术词 统一正余量  命中文件数=0    :: 
技术词 跨频传播量  命中文件数=0    :: 
技术词 坐标重包装禁区 命中文件数=0    :: 
```
- **零计算** ✗（登记 ✓）；`D1 = 0` ✓；未改他档正本 ✓（`C-379` 正本未动 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：Exit C 已证 ✗；Gram 路线已 NO-GO ✗（**待** `G1／G2` ✓）；Bridge A 已闭合 ✗；`H = \varnothing` 已证 ✗
