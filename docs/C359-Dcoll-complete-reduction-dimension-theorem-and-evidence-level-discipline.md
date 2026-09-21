已查地图（**先查后写**）：`C-358`（**`a_i = 0` 完整分类** ✓✓）、`C-357`（奇异层命中 ✓✓）、`C-355`（四锁 ✓✓）、`C-350 §2`（2+2 多重集相等 ✓✓）、`C-348`（**1.4677 为数值网格结果** ⚠️✓）。回查见 §5 ✓

D0: 本档对象 = **C-359：`\mathcal D_{\mathrm{coll}}` 降阶分类（维数定理）＋ 证据等级纪律**，**零计算（解析）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 三分拆解}✓✓：\ 3+2 = \mathcal D_{\partial} \ \cup\ \mathcal D_{\mathrm{coll}} \ \cup\ \mathcal D_{\mathrm{reg}}✓；\ \mathcal D_{\partial}\ \text{（}a_i = 0\text{）}\ \textbf{已结构性排除}✓✓（C-358✓）$$
$$\textbf{② ⭐ `\mathcal D_{\mathrm{coll}}` 维数定理}✓✓：\text{原族}\ 1\ \text{维}✓；\text{碰撞}\（a_i = a_j✓）\ \text{为}\ \textbf{一个额外条件}✓ \Longrightarrow \ \boxed{\mathcal D_{\mathrm{coll}}\ \text{为}\ 0\ \text{维（离散）层}}✓✓$$
$$\qquad \text{代入后}✓：\text{未知}\ (t, u, \beta, b_2) = 4✓，\text{方程}\ 4✓ \Longrightarrow \textbf{方系统}✓✓ \Longrightarrow \text{解}\ \textbf{孤立}✓ \Longrightarrow \textbf{可逐点区间验证}✓✓$$
$$\textbf{③ 非自动反称}⚠️✓：\text{碰撞点}\ (t, t, u, -\beta, -b_2)✓ \ \textbf{一般不成对反向}✗✓（\text{仅当}\ \{t,t,u\} = \{\beta, b_2\}\ \text{时落入反称}✓） \Longrightarrow \textbf{须逐点核}✓✓$$
$$\textbf{④ 证据等级纪律（采纳）}✓✓：\ \textbf{边界结构分类} \ > \ \textbf{数值排除}✓✓ \ —— \ \text{不得因}\ a_i = 0\ \text{的精确分类而升级}\ (2+2)\ \text{的数值结论}✗✓$$
$$\textbf{⑤ 账本}✓✓：\text{见 §4}✓（\ a_i = a_j\ \text{与}\ \mathcal D_{\mathrm{reg}}\ \text{均}\ \textbf{OPEN}✓；\ \mathcal Z \cap E\ \text{与}\ H = \varnothing\ \text{仍}\ \textbf{OPEN}✓）$$

## §1 `\mathcal D_{\mathrm{coll}}` 降阶（✓✓）

$$\textbf{设}✓：a_1 = a_2 = t✓，a_3 = u✓（\text{重标号后}\ a_1 = a_3\ \text{同型}✓） \Longrightarrow \text{系统}✓：$$
$$\qquad 2t + u = \beta + b_2✓；\quad 2t^3 + u^3 = \beta^3 + b_2^3✓；\quad 2t^5 + u^5 = \beta^5 + b_2^5✓；\quad 2t^7 + u^7 = \beta^7 + b_2^7✓$$
$$\textbf{计数}✓✓：\text{未知}\ 4\ \text{（}t, u, \beta, b_2\text{）}✓，\text{方程}\ 4✓ \Longrightarrow \textbf{方系统}✓✓ \Longrightarrow \text{Jacobian 一般非奇异}✓ \Longrightarrow \textbf{孤立解}✓✓$$
$$\textbf{关键差别}✓✓：\text{与}\ \mathcal D_{\partial}\ \text{不同}✗ \ —— \ \mathcal D_{\mathrm{coll}}\ \textbf{不能}整层吸收✗✓，\text{但}\ \text{其}\ \textbf{离散性} \text{使逐点验证} \text{成为有限任务}✓✓（\text{与 C-355 五件套②同型}✓）$$
$$\textbf{三重碰撞}✓：a_1 = a_2 = a_3 = t✓ \Longrightarrow 3t = \beta + b_2✓；3t^3 = \beta^3 + b_2^3✓；3t^5 = \cdots✓；3t^7 = \cdots✓$$
$$\qquad \Longrightarrow \text{未知}\ 3\ \text{、方程}\ 4✓ \Longrightarrow \textbf{超定}✓ \Longrightarrow \text{一般}\ \textbf{无解}✓✓（\text{若有解则离散}✓，\text{须单独核}✓）$$

## §2 非自动反称（✓✓）

$$\text{碰撞点构型}✓：\text{原子}\ (t,\ t,\ u,\ -\beta,\ -b_2)✓ \ —— \ \text{成对反向}\ \iff \{t, t, u\} = \{\beta, b_2\}✓（\text{多重集}✓）$$
$$\qquad \Longrightarrow \ \text{一般} \textbf{不成立}✗✓（\text{需}\ t = \beta\ \text{与}\ u = b_2✓\ \text{等特殊关系}✓） \Longrightarrow \textbf{须逐点核算偶频}✓✓（\text{不可整层引用反称成本}✗✓）$$
$$\textbf{乐观情形}✓：\text{若}\ \text{碰撞层解}\ \textbf{皆} \text{落入反称}✓ \Longrightarrow \text{整层吸收}✓✓（\text{同 C-358 结论}✓）；\text{否则}\ \text{须}\ \text{逐点区间证书}✓✓$$

## §3 证据等级纪律（✓✓，采纳唐先生 ✓）

$$\textbf{层级}✓✓：\textbf{边界结构分类}（\text{如 C-358 的精确归约}✓✓） \ > \ \textbf{数值网格排除}（\text{如 C-348 的}\ 1.4677✓ \ —— \ \text{网格}\ 4{,}004{,}001\ \text{点}⚠️✓） \ > \ \textbf{发现层结果}（\text{如 C-357 轮次 A}✗）$$
$$\Longrightarrow \ \text{故}\ (2+2) \cap E = \varnothing\ \text{须}\ \textbf{继续标注} \text{「数值结构证据」}✓✓，\ \textbf{不得}因\ a_i = 0\ \text{的精确分类而升级}✗✓$$
$$\textbf{推论}✓✓：\text{若最终要}\ \text{正式升级}\ (2+2)\ \Longrightarrow \text{须}\ \text{补}\ \textbf{解析或区间证书}✓✓（\text{如把}\ 1.4677\ \text{做成区间下界}✓）$$

## §4 账本（✓✓，唐先生表 ✓）

| 层 ✓ | 状态 ✓ |
|---|---|
| `a_i = 0` ✓ | **结构性归入 `2+2`** ✓✓ |
| `4+1` ✓ | **已排除** ✓ |
| `a_i = a_j` ✓ | **OPEN，待降阶（本档给出：0 维／方系统／可逐点验证）** ✓✓ |
| `\mathcal D_{\mathrm{reg}}` ✓ | **OPEN** ✓ |
| `\mathcal Z \cap E` ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 碰撞层维数  命中文件数=0    :: 
技术词 离散孤立解  命中文件数=0    :: 
技术词 方系统逐点验证 命中文件数=0    :: 
技术词 证据等级纪律 命中文件数=0    :: 
```
- **零计算** ✗（解析 ✓）；`D1 = 0` ✓；未改他档正本 ✓（`C-348` 的数值性质仅在**本档**标注 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`D_coll` 已排除 ✗（**仅给维数与离散性** ✓）；`2+2` 已升级为解析结论 ✗；`H = \varnothing` 已证 ✗
