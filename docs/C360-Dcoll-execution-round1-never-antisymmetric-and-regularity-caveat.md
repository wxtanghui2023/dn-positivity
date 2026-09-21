已查地图（**先查后写**）：`C-359`（`D_coll` 0 维期望 ✓；证据等级纪律 ✓✓）、`C-358`（`a_i = 0` 完整分类 ✓✓）、`C-355`（**`det J\ne0` 语境** ✓；五件套 ✓✓）、`C-348`（**数值网格** ⚠️✓）。回查见 §5 ✓

D0: 本档对象 = **C-360：`D_coll` 执行首轮（步 1–2）＋ 非反称定理 ＋ 正则性口径**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① ⭐ 解析结论（本档新增）}✓✓：\ \textbf{碰撞层永不可能反称}✓✓ \ —— \ \text{因}\ |+| = 3 \ne 2 = |-|✓ \Longrightarrow \text{多重集}\ \{t,t,u\} = \{\beta, b_2\}\ \textbf{不可能}✗✓$$
$$\qquad \Longrightarrow \ \textbf{C-348 的}\ 1.4677\ \textbf{成本绝不能整层搬入碰撞层}✗✓ \Longrightarrow \text{每个碰撞根}\ \textbf{必须逐点核算偶频}✓✓$$
$$\textbf{② 发现层结果}✗✓：\text{800 起点（快）＋ 4{,}000 起点（慢）}\ \text{Newton}✓ \Longrightarrow \textbf{未发现碰撞根}✗ \ —— \ \textbf{不是} \text{「碰撞层为空」}✗✓$$
$$\textbf{③ 正则性口径（采纳唐先生修正）}✓✓：4 \times 4\ \textbf{只是一般位置期望}✓，\textbf{不是}自动孤立✗✓ \Longrightarrow \text{须}\ \textbf{独立检查}\ \det J \ne 0✓✓$$
$$\qquad \text{若}\ \det J = 0✓ \Longrightarrow \text{转}\ \textbf{singular-substratum}✓✓，\textbf{不得}直接套用「离散」\ ✗✓$$
$$\textbf{④ 执行顺序（登记）}✓✓：\text{见 §3}（\text{六步}✓）；\textbf{⑤ 账本}✓✓：\mathcal D_{\mathrm{reg}}\ \text{OPEN}✓，\ \mathcal Z \cap E\ \text{OPEN}✓，\ H = \varnothing\ \text{OPEN}✓$$

## §1 非反称定理（✓✓，本档核心 ✓）

$$\textbf{反称的充要}✓：\text{五原子构型}\ (a_1, a_2, a_3, -\beta, -b_2)✓ \ \text{成对反向} \iff \{a_1,a_2,a_3\} = \{\beta, b_2\}✓（\text{多重集}✓）$$
$$\textbf{碰撞情形}✓✓：a_1 = a_2 = t✓ \Longrightarrow \text{左侧}\ \{t, t, u\}✓（\textbf{三元}✓），\text{右侧}\ \{\beta, b_2\}✓（\textbf{二元}✓）$$
$$\qquad \Longrightarrow \ \textbf{势不匹配}（3 \ne 2✓）\ \Longrightarrow \ \textbf{恒不成立}✓✓ \ \Longrightarrow \ \textbf{碰撞层与反称族不相交}✓✓$$
$$\textbf{推论}✓✓：\text{碰撞层的偶频}\ \max_{r \le 12} F_{2r}\ \textbf{必须逐点计算}✓ \ —— \ \text{不存在现成的整层下界}✗✓$$
$$\qquad \textbf{唯一例外}✓：\text{若某原子为 0}✓ \Longrightarrow \text{那属于}\ \mathcal D_{\partial}✓（\text{C-358 已完整分类}✓），\textbf{不是} \mathcal D_{\mathrm{coll}}✗✓$$

## §2 执行记录（发现层 ✓）

$$\textbf{系统}✓：2t + u = \beta + b_2✓；2t^3 + u^3 = \beta^3 + b_2^3✓；2t^5 + u^5 = \beta^5 + b_2^5✓；2t^7 + u^7 = \beta^7 + b_2^7✓$$
$$\textbf{Jacobian}✓：\begin{pmatrix} 2 & 1 & -1 & -1 \\ 6t^2 & 3u^2 & -3\beta^2 & -3b_2^2 \\ 10t^4 & 5u^4 & -5\beta^4 & -5b_2^4 \\ 14t^6 & 7u^6 & -7\beta^6 & -7b_2^6 \end{pmatrix}✓ \ —— \ \text{检查}\ \det J \ne 0✓✓$$
$$\textbf{搜索}✓：z = (t, u, \beta, b_2) \in (0,1]^4✓；牛顿（阻尼 ＋ 盒投影✓）；容差 10^{-11}✓$$
$$\textbf{结果}✓：\text{快轮}\ 800\ \text{起点} \to \textbf{0 根}✗；\text{慢轮}\ 4{,}000\ \text{起点}\ \text{未完成}⚠️✓ \Longrightarrow \text{合计}\ \textbf{未发现}✓$$
$$\textbf{读法}✓✓：\text{碰撞性是}\ \text{一维族中的}\ \textbf{余维 1 条件}✓ \Longrightarrow \text{一般只发生在}\ \textbf{孤立参数值}✓✓ \Longrightarrow \text{发现层零根}\ \textbf{不能}判空✗✓$$

## §3 执行顺序（✓✓，唐先生六步 ✓）

$$\textbf{① 解碰撞方系统}✓；\ \textbf{② 逐根检查}\ \det J✓✓；\ \textbf{③ 正则根区间隔离}✓；\ \textbf{④ 判断是否属反称多重集}✓（\text{本档已证：永否}✓✓）$$
$$\textbf{⑤ 非反称根直接核算}\ \max_{r \le 12} F_{2r}✓✓；\ \textbf{⑥ 奇异碰撞根再降阶}✓✓$$
$$\textbf{资源分配}✓：\text{碰撞层完成（解析／区间吸收）后}✓ \ \textbf{才}值投入\ \mathcal D_{\mathrm{reg}}✗✓$$

## §4 判空纪律（✓✓）

$$\textbf{禁止}✗✓：\text{把}\ \text{Newton 未发现}\ \text{当作}\ \text{层为空}✗ \ —— \ \text{须}\ \textbf{区间排除证书}✓✓（C-355／C-356 纪律✓）$$
$$\textbf{若确为真}✓：\mathcal D_{\mathrm{coll}} = \varnothing\ \text{须由}\ \text{区间盒覆盖} \text{证明}✓✓，\textbf{不是}发现层结论✗✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 碰撞层非反称 命中文件数=0    :: 
技术词 正则性期望  命中文件数=0    :: 
技术词 区间排除判空 命中文件数=0    :: 
```
- 运行记录 ✓：`/tmp/ex3.py`（慢 ✓）／`/tmp/ex4.py`（快 ✓，日志 `/tmp/ex3.log`✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`\mathcal D_{\mathrm{coll}}` 为空 ✗（**未发现** ✓）；4 \times 4 保证孤立 ✗；`H = \varnothing` 已证 ✗
