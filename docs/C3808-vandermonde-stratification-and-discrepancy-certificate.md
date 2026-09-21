已查地图（**先查后写**）：`C-380-7`（**有限半代数可行性** ✓✓）、`C-380-6`（**`\det A = 2^{20}`** ✓✓）、`C-376`（方差缺口 ✓✓）、`C-281`（**满秩但无 uniform margin 的先例** ⚠️✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-8：Vandermonde 分层 ＋ discrepancy 证书（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① discrepancy 提法}✓✓：\text{固定}\ x \in E_{\mathrm{even}}✓，\ \text{记}\ v_r(x) := \big(\sqrt{x_1}R_r(x_1), \dots, \sqrt{x_5}R_r(x_5)\big)✓（r = 0..4✓）$$
$$\qquad \Longrightarrow \ F_{2r+1}(x, \sigma) = \langle\sigma, v_r(x)\rangle✓✓ \Longrightarrow \ C\text{-}380\text{-}7\ \text{内核} = \boxed{\inf_{E_{\mathrm{even}}}\min_{\sigma}\max_{0 \le r \le 4}|\langle\sigma, v_r(x)\rangle| > \tfrac12}✓✓$$
$$\qquad \textbf{性质}✓✓：\text{5 个符号} \times \text{5 个线性泛函}✓ \ \textbf{恰为方阵}✓✓ \Longrightarrow \text{可写成}\ \min_\sigma\|V(x)\sigma\|_\infty > \tfrac12✓✓（V\ \text{见 §1}✓）$$
$$\textbf{② ⚠️ 警告一（采纳）}✗✓：\textbf{平均平方大}\ \textbf{不}推出最小\ \ell_\infty\ \text{大}✗✓ \ —— \ \sum_\sigma\langle\sigma, v_r\rangle^2 = 16\|v_r\|_2^2✓ \ \text{只是}\ \textbf{入口}✓，\ \textbf{不是}证书✗✓$$
$$\textbf{③ ⭐ 路线 B（消除「哪个 σ 最坏」）}✓✓：\textbf{若} \text{能在}\ E_{\mathrm{even}}\ \text{上证}\ \sigma_{\min}(V(x)) \ge c > 0✓✓ \Longrightarrow \|V\sigma\|_2 \ge c\sqrt5✓✓$$
$$\qquad \text{再由}\ \|z\|_\infty \ge \|z\|_2/\sqrt5✓ \Longrightarrow \max_{r \le 4}|F_{2r+1}| \ge c✓✓ \Longrightarrow \ \text{只需}\ \boxed{c > \tfrac12}✓✓$$
$$\qquad \textbf{优点}✓✓：\textbf{完全消除} \text{「哪一个}\ \sigma\ \text{最坏」的问题}✓✓ \ —— \ \textbf{不需}证\ \sigma_*\ \text{最坏}✗，\ \textbf{不需}逐个证 16 层✗✓$$
$$\textbf{④ ⚠️ 警告二（致命可能性，采纳）}✗✓：\det V(x)\ \textbf{未必} \text{在}\ E_{\mathrm{even}}\ \text{上远离}\ 0✗✓ \ —— \ \textbf{不得}未经审计走「uniformly invertible」✗✓$$
$$\qquad \textbf{精确式}✓✓：\ \boxed{\det V(x) = C\Big(\prod_{j=1}^{5}\sqrt{x_j}\Big)\prod_{i<j}(x_j - x_i)}✓✓（C \ne 0✓） \Longrightarrow \ \text{某}\ x_j = 0\ \text{或}\ x_i = x_j\ \text{时}\ \det V = 0✓✓$$
$$\textbf{⑤ 分层}✓✓：\ \boxed{E_{\mathrm{even}} = E_{\mathrm{gen}} \cup E_{\mathrm{deg}}}✓✓，\ E_{\mathrm{gen}} = \{x : x_j > 0,\ x_i \ne x_j\}✓；\ E_{\mathrm{deg}} = \{x : \prod_jx_j\prod_{i<j}(x_i - x_j) = 0\}✓$$
$$\textbf{⑥ 纪律（唐先生口径）}✓✓：\textbf{不}随机✗、\textbf{不}优化✗、\textbf{不}用\ F_{11} - F_{25}✗✓；\ \textbf{且}\ \textbf{不}把\ E_{\mathrm{gen}}\ \textbf{直接当可行路线}✗✓$$
$$\qquad \Longrightarrow \ \textbf{首先必须证}\ E_{\mathrm{even}}\ \text{上存在}\ \textbf{相应定量下界}✓✓，\ \textbf{否则} \text{退化成另一个「满秩但没有 uniform margin」的旧坑}✗✓$$

## §1 矩阵 V 与行列式（✓✓）

$$V(x) = \begin{pmatrix} v_0(x)^{\top} \\ \vdots \\ v_4(x)^{\top} \end{pmatrix}✓，\ V_{rj} = \sqrt{x_j}\,R_r(x_j)✓✓ \Longrightarrow \det V = \Big(\prod_j\sqrt{x_j}\Big)\det\big[R_r(x_j)\big]_{r,j=0}^{4}✓✓$$
$$\textbf{因子化}✓✓：\det V(x) = C\big(\prod_j\sqrt{x_j}\big)\prod_{i<j}(x_j - x_i)✓✓（\text{因}\ R_r\ \text{为}\ \deg \le 4\ \text{的完整基}✓ \Longrightarrow \text{广义 Vandermonde}✓✓）$$
$$\textbf{直接推论}✓✓：\text{退化恰在}\ x_j = 0\ \text{或}\ x_i = x_j✓ \Longrightarrow \text{与}\ \mathcal D_{\partial}／\text{碰撞层}\ \text{同源}✓✓（\text{C-358／C-361／C-368 已解析清除}✓✓）$$

## §2 两支审计（✓✓）

$$\textbf{① 非退化层}\ E_{\mathrm{gen}}✓✓：\text{审计是否可由}\ V\ \text{的}\ \sigma_{\min}\ \text{或 Gram 行列式得}\ \inf_{E_{\mathrm{gen}}}\sigma_{\min}(V) > \tfrac12✓✓$$
$$\qquad \textbf{若不能}✗ \Longrightarrow \text{寻找更弱的}\ \ell_\infty\text{-discrepancy 下界}✓✓（\text{不}退回逐层枚举✗）$$
$$\textbf{② 退化层}\ E_{\mathrm{deg}}✓✓：\textbf{不用}极限偷渡✗✓，\ \text{分别处理}\ x_j = 0\ \text{与}\ x_i = x_j✓✓$$
$$\qquad \textbf{预期}✓✓：\text{这些层} \text{降低节点数／有效符号自由度}✓ \Longrightarrow \textbf{很可能反而更容易} \text{直接用}\ F_{2r} \le \tfrac12\ \text{排除}✓✓$$
$$\qquad \Longrightarrow \ \text{与既有的}\ \mathcal D_{\partial}／\mathcal D_{\mathrm{coll}}\ \text{解析结论}\ \textbf{对接}✓✓$$

## §3 与既有坑位的对照（✓✓）

$$\textbf{旧坑}⚠️✓：\text{C-281}\ \text{已遇过}\ \text{「紧致性给}\ \textbf{存在性}✓ \ \text{而} \text{不}\ \text{给}\ \textbf{数值}\ margin✗」\ ——\ \text{本档}\ \textbf{须避免} \text{同型陷阱}✗✓$$
$$\qquad \Longrightarrow \ \text{证书必须给出}\ \textbf{显式常数} \text{或}\ \textbf{严格闭合的紧性论证}✓✓，\ \textbf{不能}只写\ \sigma_{\min} > 0✗✓$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}7` ✓ | **OPEN** ✓ |
| `C\text{-}380\text{-}8` ✓ | **本档注册（PROPOSED）** ✓✓ |
| `E_{\mathrm{gen}}` 上 `\sigma_{\min}` 定量下界 ✓ | **OPEN ← 关键** ✓✓ |
| `E_{\mathrm{deg}}` 分层排除 ✓ | **OPEN（预期较易）** ⚠️✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 边界（✓✓）

$$\textbf{不得}写成✗：\text{Bridge A 已闭合}✗；\ \text{路线 B 可行}✗（\textbf{待}证 \sigma_{\min} > \tfrac12✓）；\ \det V \ne 0\ \text{在}\ E_{\mathrm{even}}\ \text{上}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{两支}\ \textbf{均未审计}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 范德蒙分层  命中文件数=0    :: 
技术词 统一奇异值证书 命中文件数=0    :: 
技术词 满秩无余量陷阱 命中文件数=0    :: 
```
- **零计算** ✗（注册档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
