已查地图（**先查后写**）：`C-357`（**奇异层命中** ✓✓；A 零根＝发现失败 ✓）、`C-356`（分层执行 ✓✓）、`C-355`（四锁／五件套 ✓✓）、`C-350 §2`（**2+2 ⟹ 多重集相等** ✓✓）、`C-348`（反称成本 1.4677 ✓）。回查见 §5 ✓

D0: 本档对象 = **C-358：`a_i = 0` 边界层完整分类 ＋ `\mathcal D_{\mathrm{reg}}(\varepsilon)` 执行口径**，**零计算（解析）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 采纳}✓✓：\text{轮次 A 的}\ \textbf{零根＝发现失败}✓✓（\text{非空集证据}✗），\text{且}\ \text{退化解}\ \textbf{已结构性吸收}✓✓：3+2\ \text{singular} \to 2+2 \to \max F_{2r} \ge 1.4677✓$$
$$\textbf{② ⭐ 本档新增（完整分类）}✓✓：a_3 = 0\ \text{时，四奇矩条件仅用}\ \textbf{r = 1 与 r = 3}✓ \Longrightarrow \textbf{两二元多重集相等}✓✓ \Longrightarrow \textbf{反称族}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\mathcal D_{\partial}(a_i = 0) \cap E = \varnothing}✓✓ \ —— \ \textbf{该层为完整结论}✓✓（\text{非代表点}✗✓）$$
$$\textbf{③ 域拆分与执行口径}✓✓：\mathcal D_{\mathrm{reg}}(\varepsilon) := \{a_i \ge \varepsilon,\ b_2 > 0,\ \text{非碰撞}\}✓；\ \varepsilon = 10^{-3}\ \textbf{仅计算分层参数}✓✓，\textbf{不是}定理✗✓$$
$$\textbf{④ 三类盒纪律}✓✓：\text{certified root}✓／\text{certified exclusion}✓／\ \textbf{unresolved 必须继续细分}✓✓，\textbf{不得}记为无根✗✓$$
$$\textbf{⑤ 状态表}✓✓：\text{见 §4} \ —— \ \textbf{后两行（}\mathcal Z \cap E,\ H = \varnothing\text{）}\ \textbf{不提前升级}✗✓$$

## §1 `a_i = 0` 层完整分类（✓✓，本档核心 ✓）

$$\textbf{设定}✓：a_3 = 0✓ \Longrightarrow \text{条件退化为}\ a_1^r + a_2^r = \beta^r + b_2^r✓（r = 1,3,5,7✓）$$
$$\textbf{关键}✓✓：\text{两二元多重集}\ \{a_1, a_2\}\ \text{与}\ \{\beta, b_2\}✓ \ \text{的}\ \textbf{前两阶幂和} \text{相等即已足够}✓：$$
$$\qquad p_1 = a_1 + a_2 = \beta + b_2✓（\text{即}\ r = 1✓）；\quad p_3 = a_1^3 + a_2^3 = \beta^3 + b_2^3✓（r = 3✓）$$
$$\qquad \text{由}\ p_1 = s✓、\ p_3 = s^3 - 3ps✓ \Longrightarrow p = (s^3 - p_3)/(3s)✓（s > 0✓，\text{因全为正}✓）\ \Longrightarrow \textbf{多重集由}\ (p_1, p_3)\ \textbf{唯一确定}✓✓$$
$$\Longrightarrow \ \{a_1, a_2\} = \{\beta, b_2\}✓✓ \Longrightarrow \text{五原子}\ (a_1, a_2, 0, \beta, b_2)✓ \ \textbf{成对反向}✓✓ \Longrightarrow \textbf{反称族}✓✓$$
$$\Longrightarrow \ \max_{r \le 12} F_{2r} \ge 1.4677 > \tfrac12✓（C-348✓）\ \Longrightarrow \ \mathcal D_{\partial}(a_i = 0) \cap E = \varnothing✓✓（\text{完整}✓）$$

## §2 `\mathcal D_{\mathrm{reg}}(\varepsilon)` 执行口径（✓✓）

$$\mathcal D_{\mathrm{reg}}(\varepsilon)✓：a_i \ge \varepsilon✓（\text{如}\ 10^{-3}✓）、b_2 > 0✓、\text{无碰撞}✓（a_i \ne a_j✓） \ \Longrightarrow \ \text{Jacobian 非退化}✓✓$$
$$\textbf{手段}✓✓：\textbf{区间排除}（\text{区间求值}\ \text{证无根}✓）＋ \textbf{Krawczyk 根隔离}（\text{存在性＋唯一性}✓✓）$$
$$\textbf{三分类}✓✓：\text{certified root box}✓；\text{certified exclusion box}✓；\ \textbf{unresolved box}✓ \Longrightarrow \textbf{必须细分}✗✓（\text{禁止记无根}✗）$$
$$\textbf{参数域}✓：\beta \in (0,1]✓ \ \text{细分}✓；\text{端点另案}✓（\beta = 1✓，\beta \to 0^+✓ ← C-355 锁 (1)✓）$$

## §3 碰撞层 `\mathcal D_{\mathrm{coll}}` 降阶（✓✓）

$$\textbf{不用通用 Newton}✗✓：a_i = a_j✓ \ \Longrightarrow \textbf{合并变量＋重写降阶矩方程}✓✓$$
$$\textbf{预期分裂}✓：3+2 \to 2+2✓（\text{合并后二元}✓）；3+2 \to 1+2+2✓（\text{若含二重根}✓） \ \Longrightarrow \text{逐类降阶审计}✓$$
$$\textbf{注}✓✓：\mathcal D_{\mathrm{coll}}\ \text{与}\ \mathcal D_{\partial}(a_i = 0)\ \text{可能相交}✓，\text{须}\ \textbf{按最退化者} \text{归类}✓✓$$

## §4 状态表（✓✓，唐先生口径 ✓）

| 项 | 状态 |
|---|---|
| `2+2 \cap E` ✓ | **`= \varnothing`（数值结构证据，按既有证书口径使用）** ✓ |
| `4+1 \cap E` ✓ | **`= \varnothing`** ✓ |
| `3+2` singular ✓ | **已发现并退化到 `2+2`** ✓（**本档补完整分类** ✓✓） |
| `3+2` regular ✓ | **OPEN** ✓ |
| `\mathcal Z \cap E` ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

$$\textbf{纪律}✓✓：\text{最后两行}\ \textbf{不因}\ C\text{-357／}C\text{-358}\ \text{的结构结果而提前升级}✗✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 降阶层完整分类 命中文件数=0    :: 
技术词 计算分层参数 命中文件数=0    :: 
技术词 未决盒        命中文件数=0    :: 
技术词 反称归约     命中文件数=0    :: 
```
- **零计算** ✗（解析 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗；`\varepsilon` 是数学定理 ✗；`unresolved` 即无根 ✗
