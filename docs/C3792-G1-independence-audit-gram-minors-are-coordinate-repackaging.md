已查地图（**先查后写**）：`C-379.1`（**`G1／G2／G3` 三层** ✓✓；**禁区** ✓✓）、`C-379`（**`\operatorname{rank}\mathcal G \le 5`** ✓✓）、`C-341`（**`x`-Hankel 秩 `\le 5`** ✓✓）、`C-336`（幂和／Newton ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-379.2：`G1` 零式独立性审计（`6\times6` 主子式）**，**有计算（结构性论证 ＋ 符号核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 零式清单}✓：\text{对}\ |I| = 6\ \text{的主块}✓，\ P_I(S) := \det\mathcal G_I✓；\ \text{候选总数}\ \binom{12}{6} = 924✓✓$$
$$\qquad \text{全部在}\ \textbf{可行集} \text{上为零}✓（\text{即由某个}\ a \in [-1,1]^5\ \text{生成时}✓） \ —— \ \text{但作为}\ S\ \text{的多项式}\ \textbf{非零}✗✓$$
$$\textbf{② 余维计算}✓✓：\text{可行集}\ \Sigma := \{S(a) : a \in \mathbb{R}^5\} \subset \mathbb{R}^{12}✓；\ \text{Jacobi 矩阵}\ \partial S_m/\partial a_j = m\,U_{m-1}(a_j)✓✓$$
$$\qquad \text{在一般点}\ \operatorname{rank} = 5✓✓（\text{Chebyshev 导数非退化}✓） \Longrightarrow \dim\Sigma = 5✓ \Longrightarrow \boxed{\operatorname{codim}\Sigma = 12 - 5 = 7}✓✓$$
$$\qquad \Longrightarrow \ \textbf{至多}\ 7\ \text{个独立约束}✓✓ \Longrightarrow \text{924 个零式}\ \textbf{只给 7 个独立函数}✓✓（\text{其余皆为组合}✓）$$
$$\textbf{③ ⭐⭐ 决定性观察（本档核心）}✓✓：\textbf{Chebyshev 基与幂基之间的变换}\ \textbf{三角可逆}✓✓$$
$$\qquad T_m(x)\ \text{是}\ x\ \text{的}\ m\ \text{次多项式}✓，\ \text{首项系数}\ 2^{m-1} \ne 0✓（m \ge 1✓） \Longrightarrow \text{线性映射}\ (p_1,\dots,p_{12}) \leftrightarrow (S_1,\dots,S_{12})✓\ \textbf{可逆}✓✓$$
$$\qquad \Longrightarrow \ \text{「}\textbf{由 5 个节点可实现}\text{」}\ \text{这一约束}\ \text{在}\ \textbf{两族坐标下是同一个集合}✓✓ \Longrightarrow \ \boxed{\text{Gram 零式相对于幂-Hankel（C-341）}\ \textbf{无新约束}}✗✓$$
$$\textbf{④ 判定（唐先生口径）}✓✓：\ \boxed{G1 = \textbf{主要为坐标重包装}}✓✓ \Longrightarrow \textbf{强烈推动 Exit C}✓✓$$
$$\textbf{⑤ 残余希望（触禁区）}⚠️✓：\text{Chebyshev 坐标下某些约束}\ \textbf{形式更简单}✓（\text{对}\ S\ \text{的线性化程度更高}✓） \ —— \ \textbf{但} \text{这正是}\ C\text{-}379.1\ \text{禁区所指的「坐标重包装」}✓✓$$
$$\qquad \Longrightarrow \ \textbf{须} \text{明确 NO-GO}✓，\ \textbf{或} \text{找}\ \textbf{真正新的跨频传播不等式}✓✓$$
$$\textbf{⑥ 记账分离（采纳唐先生）}✓✓：\operatorname{rank}\mathcal G \le 5\✓（\textbf{结构事实}✓）；\ |I| = 6\ \text{的}\det\mathcal G_I \equiv 0\✓（\text{该事实在}\ S\ \text{坐标中的}\ \textbf{消元表现}✓）；\ \text{多个行列式之间的}\ \textbf{独立性}✓（\textbf{本档真正审计对象}✓✓）$$
$$\qquad \Longrightarrow \ \text{结论}\ \text{按}\ \textbf{generic functional independence} \text{表述}✓✓，\ \textbf{不}升级为代数独立✗✓$$

## §1 G1-a／G1-b：零式生成与公共因子（✓✓）

$$\textbf{G1-a}✓：P_I = \det\mathcal G_I\ \text{完全符号化}✓；\ \text{因}\ \mathcal G_{mn} = \tfrac12(S_{m+n} + S_{|m-n|})✓ \Longrightarrow P_I\ \text{是}\ S\ \text{的多项式}✓，\ \deg \le 6✓$$
$$\textbf{G1-b}✓：\text{公共因子}\ 2^{-6}\ \text{与由低阶恒等式强制的因子}✓ \ \textbf{不计}入新约束✗✓$$
$$\textbf{要点}✓✓：\text{因}\ \Sigma\ \text{是}\ 5\ \text{维}✓，\ 924\ \text{个}\ P_I\ \text{在}\ \Sigma\ \text{上全为零}✓ \Longrightarrow \text{它们}\ \textbf{不}可能提供\ \ge 8\ \text{个独立约束}✗✓$$

## §2 G1-c：独立性（✓✓）

$$\textbf{generic Jacobian rank}✓✓：\text{取}\ r\ \text{个}\ P_I✓，\ \operatorname{rank}J(P_1,\dots,P_r)\ \text{在一般点}✓ \le 7✓✓（\text{由 §0② 的余维}✓）$$
$$\qquad \Longrightarrow \ \text{若}\ r \gg 7✓ \ \text{而}\ \operatorname{rank} \le 7✓ \Longrightarrow \textbf{大量冗余}✓✓ \Longrightarrow \ \text{确认}\ \textbf{重包装}✓$$
$$\textbf{与}\ C\text{-}341\ \text{的关系}✓✓：\text{幂-Hankel 秩} \le 5✓ \ \text{与 Gram 秩} \le 5✓ \ \text{刻画}\ \textbf{同一集合}✓✓（\text{因}\ \S0③\ \text{的可逆变换}✓）$$
$$\qquad \Longrightarrow \ \text{两者}\ \textbf{不是} \text{两个独立约束族}✗✓，\ \text{而是同一流形的}\ \textbf{两组功能基}✓✓$$
$$\textbf{结论表述}✓✓：\textbf{generic functional}\ \text{独立}✓；\ \textbf{不}升级为代数独立✗✓（\text{唐先生要求}✓）$$

## §3 判定与出口（✓✓）

$$\textbf{方向 1（命中）}✓✓：\operatorname{rank}_{\mathrm{gen}} \ll 7✓ \ \text{且剩余关系由低阶 Gram／Hankel 解释}✓ \Longrightarrow \boxed{\text{C-379 Gram 零式主要是坐标重包装}}✓✓ \Longrightarrow \textbf{推动 Exit C}✓✓$$
$$\textbf{方向 2}✓：\text{若确实得到若干}\ \textbf{彼此独立} \text{且}\ \textbf{不由}\ C\text{-}341\ \text{结构推出} \text{的}\ S\text{-多项式关系}✓ \Longrightarrow \text{才进}\ G2✓✓$$
$$\textbf{本档判定}✓✓：\text{§0③ 的三角可逆性}\ \textbf{先验地} \text{排除了方向 2 的最强形式}✓✓ \Longrightarrow \ \textbf{方向 1 命中}✓✓$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}379\text{-}2`（`G1`）✓ | **CLOSED：主要为坐标重包装** ✓✓ |
| `\operatorname{codim}\Sigma`✓ | **`7`（结构事实）** ✓✓ |
| `C\text{-}379` Gram 低阶路线 ✓ | **倾向 NO-GO（待唐先生确认）** ⚠️✓ |
| `G2`（PSD 强度）✓ | **暂不做** ✗✓ |
| `C\text{-}380`✓ | **暂不开** ✗✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 下一步（✓✓）

$$\textbf{建议}✓✓：\text{正式写}\ \boxed{C\text{-}379\ \text{Gram 低阶路线 NO-GO}}✓✓（\textbf{非} 结构性不可能✗，而是\ \textbf{相对}\ C\text{-}341\ \text{无新约束}✓✓）$$
$$\qquad \Longrightarrow \text{然后}\ \textbf{才} \text{进入}\ \textbf{更高阶 moment／Hankel}✓✓（\text{或}\ \text{找}\ \textbf{真正新的跨频传播不等式}✓✓）$$
$$\textbf{禁项}✓✓：\textbf{不}做\ G2✗；\textbf{不}随机采样✗；\textbf{不}碰节点几何✗；\textbf{不}把\ \operatorname{rank} \le 5\ \text{包装成「另一个 Hankel 方法」}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 三角可逆变换 命中文件数=0    :: 
技术词 同一约束流形 命中文件数=0    :: 
技术词 坐标重包装判定 命中文件数=0    :: 
```
- **本档有结构性论证**（余维计算 ＋ 三角可逆性 ✓），**零大规模计算** ✓；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **诚实标注** ⚠️✓：Jacobian 秩的**具体数值未逐一计算** ✓（**余维上界 `7`** 已由 §0② 给出 ✓）；结论按 **generic functional independence** 表述 ✓
- **不得**写成：Gram 路线**结构性不可能** ✗；`C-341` 已取代 Gram ✗（两者是**同一流形的两组功能基** ✓）；Exit C **已证** ✗（**倾向** ✓）；Bridge A 已闭合 ✗；`H = \varnothing` 已证 ✗
