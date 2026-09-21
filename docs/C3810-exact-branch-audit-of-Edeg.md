已查地图（**先查后写**）：`C-380-9`（**`D(x)` 与退化层** ✓✓）、`C-380-8`（**Vandermonde 分层** ✓✓）、`C-380-7`（**可行性** ✓✓）、`C-358`（**限 `\mathcal Z`** ⚠️✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-10：`E_{\mathrm{deg}} \cap E_{\mathrm{even}}` 的精确分支审计（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 拆分原理}✓✓：\ \boxed{D(x) = 0 \iff (\exists j: x_j = 0) \lor (\exists i < j: x_i = x_j)}✓✓ \Longrightarrow \textbf{不}先算\ D\ \text{的连续优化}✗✓，\ \text{而}\ \textbf{精确拆成}\ E_{\mathrm{even}} \cap E_0\ \text{与}\ E_{\mathrm{even}} \cap E_{\mathrm{coll}}✓✓$$
$$\textbf{② 边界层}\ x_j = 0✓✓：\text{若}\ x_5 = 0✓ \Longrightarrow F_{2r} = \sum_{j=1}^{4}T_r(2x_j - 1) + (-1)^r✓✓ \Longrightarrow \text{原 5-node 系统}\ \textbf{降为 4-node Chebyshev 系统}✓✓$$
$$\qquad \text{问}\ \boxed{E_{\mathrm{even}} \cap E_0 = \varnothing\ ?}✓✓；\ \textbf{若 YES}✓ \Longrightarrow x_j \ge \varepsilon_0 > 0✓，\ \text{再由紧性追问}\ \textbf{显式}\ \varepsilon_0✓✓$$
$$\qquad \textbf{若 NO}✓✓ \Longrightarrow \textbf{不是坏消息}✗✓：\text{此时 odd layer}\ \textbf{只剩四个有效权重}✓✓ \Longrightarrow \text{可}\ \text{在此 4-node 层直接处理}\ \min_\sigma\max_{r \le 4}|\sum_{j=1}^{4}w_jR_r(x_j)|✓✓$$
$$\textbf{③ ⭐ collision 层（本档核心）}✓✓：\text{设}\ x_1 = x_2 = t✓ \Longrightarrow F_{2r} = 2T_r(2t - 1) + \sum_{j=3}^{5}T_r(2x_j - 1)✓✓$$
$$\qquad \textbf{odd layer 必须区分}✓✓：\sigma_1 = \sigma_2\ \textbf{与}\ \sigma_1 = -\sigma_2✓✓ \ —— \ \textbf{这是本档最漂亮的分叉}✓✓$$
$$\qquad \textbf{同号}✓✓：w_1 + w_2 = (\sigma_1 + \sigma_2)\sqrt{t} = \pm 2\sqrt{t}✓✓ \Longrightarrow \textbf{合并为一个权重}\ 2\sqrt{t}\ \text{的节点}✓✓$$
$$\qquad \textbf{异号}✓✓：w_1 + w_2 = 0✓，\ \text{且因}\ x_1 = x_2✓ \Longrightarrow \ \text{两节点对}\ \textbf{全部}\ R_r(x)\ \text{完全相同}✓✓ \Longrightarrow \ \boxed{\sigma_1 = -\sigma_2 \Longrightarrow \text{该两节点对全部奇频}\ \textbf{完全抵消}}✓✓$$
$$\textbf{④ collision 分支天然结构}✓✓：\ \boxed{\text{collision} = \text{同号合并} \ \dot\cup\ \text{异号完全消去}}✓✓ \ —— \ \textbf{比直接枚举 16 层强得多}✓✓$$
$$\qquad \textbf{异号情形}✓✓：\text{有效}\ \textbf{3-node odd system}✓：F_{2r+1} = \sum_{j=3}^{5}\sigma_j\sqrt{x_j}\,R_r(x_j)✓✓$$
$$\textbf{⑤ ⭐ 纪律锁死（唐先生口径）}✗✓：\textbf{不得}写\ x_1 = x_2 \Rightarrow \text{「退化层可以忽略」}✗✓$$
$$\qquad \textbf{正确}✓✓：x_1 = x_2 \Rightarrow \begin{cases} \sigma_1 = \sigma_2 : \text{节点合并}✓ \\ \sigma_1 = -\sigma_2 : \text{该节点对全部 odd}\ \textbf{完全消失}✓ \end{cases}$$
$$\qquad \Longrightarrow \ \text{第二种}\ \textbf{可能是最危险的 discrepancy 层}✓✓ \ —— \ \text{它把 5-node odd problem}\ \textbf{降到 3 个有效节点}✓，\ \textbf{而 even 约束仍保留两重复节点的权重}✓✓$$
$$\textbf{⑥ C-380-10 只允许三个出口}✓✓：\text{见 §1}✓$$

## §1 三个出口（✓✓）

$$\textbf{出口 1}✓✓：E_{\mathrm{even}} \cap E_{\mathrm{deg}} = \varnothing✓ \Longrightarrow \text{才有资格进入}\ \textbf{B1}✓，\ \textbf{且} \text{还须}\ \textbf{继续} \text{证定量远离}✓：\inf_{E_{\mathrm{even}}}D(x) > 0✓✓$$
$$\qquad \textbf{注意}✗✓：\textbf{不能}把「没有退化点」直接升级成正距离✗✓，\ \textbf{除非} \text{把闭集／紧性关系}\ \textbf{写完整}✓✓$$
$$\textbf{出口 2}✓✓：\text{退化层存在}✓，\ \textbf{但可直接证低维 odd amplification}✓：\ \inf_{E_{\mathrm{even}} \cap E_{\mathrm{deg}}}\min_\sigma\max_{r \le 4}|F_{2r+1}| > \tfrac12✓✓$$
$$\qquad \Longrightarrow \text{退化层}\ \textbf{直接关闭}✓✓，\ \textbf{B2 只需处理}\ E_{\mathrm{gen}}✓✓$$
$$\textbf{出口 3}✓✓：\text{退化层存在}\ \textbf{且出现}\ \min_\sigma\max_{r \le 4}|F_{2r+1}| \le \tfrac12✓ \Longrightarrow \textbf{这才是真正的}\ C\text{-}380\text{-}7\ \text{障碍}✓✓$$
$$\qquad \textbf{此时}✓✓：\textbf{不应}再包装成 Vandermonde 问题✗✓，\ \text{而应记录为}\ \boxed{\text{低奇频 5-direction discrepancy 本身存在}\ \textbf{退化障碍}}✓✓$$
$$\qquad \Longrightarrow \text{才考虑}\ F_{11}\ \text{以后是否必要}✓✓$$

## §2 顺序（✓✓）

$$\boxed{x_j = 0 \ \longrightarrow\ x_i = x_j \ \longrightarrow\ \begin{cases} \sigma_i = \sigma_j \\ \sigma_i = -\sigma_j \end{cases}}✓✓$$
$$\textbf{禁项}✓✓：\textbf{不}计算\ \sigma_{\min}✗；\textbf{不}优化\ D✗；\textbf{不}使用\ F_{11} - F_{25}✗✓；\textbf{不}做随机搜索✗✓$$

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}9` ✓ | **OPEN** ✓ |
| **`C\text{-}380\text{-}10`（`E_{\mathrm{deg}}` 精确分支）** ✓ | **OPEN ← 下一刀** ✓✓ |
| `E_{\mathrm{even}} \cap E_0` ✓ | **未判定** ✗✓ |
| `E_{\mathrm{even}} \cap E_{\mathrm{coll}}` ✓ | **未判定** ✗✓ |
| `\inf D(x)` ✓ | **搁置（待 C-380-10 后）** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §4 边界（✓✓）

$$\textbf{不得}写成✗：E_{\mathrm{deg}} \cap E_{\mathrm{even}} = \varnothing\ \text{已证}✗；\ \text{退化层可忽略}✗；\ \inf D > 0\ \text{已证}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{两分支}\ \textbf{均未判定}✗✓；\ \text{异号抵消为}\ \textbf{精确结构事实}✓✓（\text{非}数值✗）$$

## §5 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 异号完全消去 命中文件数=0    :: 
技术词 有效三节点  命中文件数=0    :: 
技术词 退化层最危险支 命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
