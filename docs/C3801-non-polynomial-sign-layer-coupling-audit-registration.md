已查地图（**先查后写**）：`C-380-0`（**多项式跨层 NO-GO** ✓✓）、`C-379.3`（**防重复墙** ✓✓）、`C-376`（`\operatorname{dist}(E, \mathcal Z) > 0` ✓✓）、`C-349`（四阶 signed moment ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-1：符号层 `\sigma_j\sqrt{x_j}` 的非多项式耦合审计（注册）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① } C\text{-}380\text{-}0\ \text{正式落账}✓✓：\ \boxed{\text{多项式型偶} \to \text{奇耦合} = \textbf{NO-GO}}✓✓$$
$$\qquad \textbf{严格表述}✓✓：\text{在 Chebyshev 奇偶分解下}✓，\ \text{任何仅由}\ x_j\ \text{多项式构成的偶-奇乘积／组合}✓ \ \textbf{不}产生新的独立跨层量✗✓$$
$$\qquad \qquad \text{其奇部分仍可化回既有奇频}\ S_{2r+1}（\text{或}\ F_{2r+1}）\ \text{坐标}✓✓ \Longrightarrow \textbf{不能} \text{作为新的跨层传播机制}✗✓$$
$$\qquad \textbf{勘误保留}✓✓：2T_{2r}T_{2s+1} = T_{2(r+s)+1} + T_{|2(r-s)-1|}✓✓（\textbf{非}\ +1✗✓）$$
$$\textbf{② } C\text{-}380\ \text{入口收窄（本档核心）}✓✓：\ \boxed{\mathfrak C = \mathfrak C(x, \sigma)\ \text{且必须显式利用}\ \sigma_j\sqrt{x_j}}✓✓$$
$$\qquad \text{因}\ F_{2r} = \sum_j P_r(x_j)✓ \ \textbf{完全不看符号}✗✓；\ F_{2r+1} = \sum_j \sigma_j\sqrt{x_j}\,R_r(x_j)✓ \ \textbf{第一次真正看到符号层}✓✓$$
$$\qquad \Longrightarrow \ \text{结构}\ = \ \underbrace{x}_{\text{偶层}} + \underbrace{\sigma\sqrt{x}}_{\text{奇层}}✓✓ \ —— \ \textbf{不是} \text{继续在}\ x\ \text{上制造更高阶多项式}✗✓$$
$$\textbf{③ } C\text{-}380\text{-}1\ \text{目标}✓✓：\ \boxed{\max_{r \le 12}F_{2r} \le \tfrac12 \Longrightarrow \text{对全部}\ 16\ \text{个}\ \sigma\ \text{给出统一奇频下界}}✓✓$$
$$\qquad \textbf{理想形式}✓✓：\ \boxed{\mathcal Q(x) \le \tfrac12 \Longrightarrow \min_{\sigma \in \mathcal S}\max_{0 \le r \le 12}\Big|\sum_j \sigma_j\sqrt{x_j}\,R_r(x_j)\Big| > \tfrac12}✓✓$$
$$\qquad \Longrightarrow \ \text{这才是真正可能}\ \textbf{关闭 Bridge A} \text{的量}✓✓$$
$$\textbf{④ ⭐ NO-GO 纪律（关键）}✓✓：\ \boxed{\text{若最终只是重新证明}\ \mathcal Z \cap E = \varnothing\ \Longrightarrow \textbf{NO-GO}}✓✓$$
$$\qquad \text{因}\ C\text{-}372 \sim C\text{-}376\ \text{已给}\ \operatorname{dist}(E, \mathcal Z) > 0✓✓ \Longrightarrow \ C\text{-}380\ \textbf{必须} \text{进一步把}\ \textbf{符号层距离} \text{传播到}\ \textbf{高奇频}✓✓$$
$$\qquad \qquad \textbf{不能}只重新证明「不存在精确零」✗✓$$
$$\textbf{⑤ 账本}✓✓：\text{见 §3}✓$$

## §1 入口与结构（✓✓）

$$\textbf{偶层}✓：\text{仅依赖}\ x_j = c_j^2 \in [0,1]✓；\ \text{约束}\ E_{\mathrm{even}} : \sum_j T_r(2x_j - 1) \le \tfrac12✓（r = 1,\dots,12✓）✓✓$$
$$\textbf{奇层}✓：F_{2r+1} = \sum_j \sigma_j\sqrt{x_j}\,R_r(x_j)✓ \ —— \ \textbf{唯一的非多项式入口}✓✓（\text{含}\ \sqrt{x_j} \ \text{与}\ \sigma_j✓）$$
$$\textbf{符号层}✓✓：\sigma \in \{\pm 1\}^5 / \{\pm I\}✓，\ |\mathcal S| = 16✓✓（\text{C-344 已证}\ \sigma \leftrightarrow -\sigma\ \text{同值}✓）$$
$$\textbf{禁项}✓✓：\textbf{不}在\ x\ \text{上升阶}✗；\textbf{不}重证\ \mathcal Z \cap E = \varnothing✗✓$$

## §2 判据（✓✓）

$$\textbf{出口 A（成功）}✓✓：\text{建立}\ \boxed{\mathcal Q(x) \le \tfrac12 \Longrightarrow \min_\sigma\max_r|F_{2r+1}| > \tfrac12}✓✓（\text{或等价：}\ \min_\sigma\max_r F_{2r+1} > \tfrac12\ \text{方向}✓） \Longrightarrow \textbf{关闭 Bridge A}✓✓$$
$$\textbf{出口 B（NO-GO）}✓✓：\text{若}\ \text{一切候选}\ \mathfrak C\ \text{最终}\ \textbf{只是重证}\ \mathcal Z \cap E = \varnothing✗✓ \ \text{或}\ \text{化回}\ S\text{-坐标}✗ \Longrightarrow \textbf{NO-GO}✓✓$$
$$\textbf{出口 C（DISCOVERY）}✓：\text{仅数值相关，无统一不等式} \Longrightarrow \textbf{不得}进主线✗✓$$

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}378` ✓ | **node geometry CLOSED** ✓✓ |
| `C\text{-}379` ✓ | **Gram CLOSED／NO-GO** ✓✓ |
| `C\text{-}380\text{-}0` ✓ | **polynomial coupling CLOSED／NO-GO** ✓✓ |
| **`C\text{-}380\text{-}1`** ✓ | **non-polynomial sign-layer coupling OPEN** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

$$\textbf{结构性小结}✓✓：\text{终于落到此前一直缺失的}\ \boxed{\textbf{换量}：\ \sigma_j\sqrt{x_j}}✓✓$$

## §4 边界（✓✓）

$$\textbf{不得}写成✗：\text{Bridge A 已闭合}✗；\ \mathcal Z \cap E = \varnothing\ \text{可重证即算进展}✗✓；\ \text{多项式路线}\ \textbf{结构性}不可能✗（\textbf{仅} NO-GO✓）；\ H = \varnothing\ \text{已证}✗$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{目标不等式的}\ \textbf{任何部分均未证明}✗✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 符号层耦合  命中文件数=0    :: 
技术词 距离传播非重证 命中文件数=0    :: 
技术词 统一奇频下界 命中文件数=0    :: 
```
- **零计算** ✗（注册档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
