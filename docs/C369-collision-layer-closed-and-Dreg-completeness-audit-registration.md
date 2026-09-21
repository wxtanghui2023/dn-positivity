已查地图（**先查后写**）：`C-368`（**判空两步** ✓✓；勘误 ✓）、`C-367`（`P_5 \mid P_7` ✓✓）、`C-356`（**分层 D_reg／D_coll／D_∂** ✓✓）、`C-355`（五件套 ✓✓）、`C-361`（三重为空 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-369：碰撞层闭合 ＋ `\mathcal D_{\mathrm{reg}}` 完备审计注册**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 碰撞层正式闭合}✓✓：\ \mathcal D^{\mathrm{triple}}_{\mathrm{coll}} = \varnothing✓（C-361✓）＋ \mathcal D^{\mathrm{double}}_{\mathrm{coll}} \cap E = \varnothing✓（C-368✓；\text{且更强：}\ \mathcal D^{\mathrm{double}}_{\mathrm{coll}} = \varnothing✓） \Longrightarrow \boxed{\mathcal D_{\mathrm{coll}} \cap E = \varnothing}✓✓$$
$$\textbf{② ⭐ 证据等级精炼（采纳）}✓✓：\text{判空}\ \textbf{只需}\ E_5 \ne 0\ \text{on}\ \mathcal F✓✓（\text{即}\ P_5 > 0✓） \ —— \ \textbf{更不需}依赖\ E_7\ \text{的根分析}✗✓$$
$$\qquad \boxed{P_5 \mid P_7\ \text{是结构性坍缩}✓；\ P_5 > 0\ \text{on}\ \mathcal F\ \text{才是判空}}✓✓；\ P_7\ \text{的因式分解}\ = \ \textbf{交叉验证}✓，\textbf{非}判空依据✗✓$$
$$\textbf{③ 措辞纪律}✓✓：\text{可写}\ \textbf{「碰撞部分的}\ \mathcal Z \cap E\ \text{已排除」}✓✓；\ \textbf{不得}扩大成整个\ \mathcal Z \cap E✗✓$$
$$\textbf{④ ⭐ 战略转折}✓✓：\text{exact-cancellation 分支现仅余}\ \mathcal D_{\mathrm{reg}}✓✓（\mathcal D_{\partial}✓、\mathcal D^{\mathrm{triple}}_{\mathrm{coll}}✓、\mathcal D^{\mathrm{double}}_{\mathrm{coll}}✓\ \text{均已处理}✓）$$
$$\textbf{⑤ 下一档注册}✓✓：\ \mathcal D_{\mathrm{reg}}\ \textbf{完备审计}✓；\ \textbf{移植}\ C\text{-}355／C\text{-}356✓，\ \textbf{不新增方法}✗✓；\ \varepsilon\ \text{为}\ \textbf{分层参数}✓，\ \textbf{不假定} \text{固定}\ \varepsilon\ \text{已存在}✗✓$$

## §1 `\mathcal D_{\mathrm{reg}}` 定义（✓✓）

$$a_1, a_2, a_3 > 0✓；\ a_i \ne a_j✓（i \ne j✓） \ —— \ \textbf{非退化、无碰撞}✓✓$$
$$\textbf{四奇矩条件}✓：\sum_{i=1}^{3} a_i^{2r+1} = \beta^{2r+1} + b_2^{2r+1}✓，\ r = 0, 1, 2, 3✓✓（\text{即}\ r = 0\ \text{给和条件}✓；r = 1,2,3\ \text{给} a_i^3, a_i^5, a_i^7✓）$$
$$\textbf{计数}✓✓：\text{未知}\ 5\ \text{（}a_1, a_2, a_3, \beta, b_2\text{）}✓，\text{方程}\ 4✓ \Longrightarrow \textbf{一维族}✓✓ \Longrightarrow \text{须}\ \textbf{完备覆盖}✓（\text{非离散}✓）$$

## §2 分层参数（✓✓）

$$\textbf{分层}✓✓：a_i \ge \varepsilon✓，\ |a_i - a_j| \ge \varepsilon✓ \ —— \ \text{仅作}\ \textbf{分层参数}✓✓，\textbf{不假定} \text{某个固定}\ \varepsilon\ \text{已存在}✗✓$$
$$\textbf{已消层}✓✓：\mathcal D_{\partial}✓（a_i = 0✓；C-358✓）→ \text{归}\ (2+2)✓；\ \mathcal D^{\mathrm{triple}}_{\mathrm{coll}}✓（C-361✓）；\ \mathcal D^{\mathrm{double}}_{\mathrm{coll}}✓（C-368✓）$$
$$\qquad \Longrightarrow \ \textbf{仅余}\ \mathcal D_{\mathrm{reg}}✓✓ \ —— \ \text{故}\ \varepsilon\text{-分层}\ \text{不再是「待处理障碍」}✓，\ \text{而是}\ \textbf{审计参数化}✓✓$$

## §3 协议移植（✓✓，不新增方法 ✓）

$$\textbf{C-355 五件套}✓✓：\text{① 参数覆盖}✓（\text{含端点}✓）\ \text{② 根盒隔离}✓（Krawczyk✓）\ \text{③ 排除盒}✓（\text{区间证书}✓）\ \text{④ 奇异层}✓（\det J = 0✓）\ \text{⑤ 偶频下界}✓✓$$
$$\textbf{C-356 分层}✓✓：\mathcal D_{\mathrm{reg}} \ \dot\cup \ \mathcal D_{\mathrm{coll}} \ \dot\cup \ \mathcal D_{\partial}✓ \ —— \ \textbf{后两者已解析清除}✓✓ \Longrightarrow \text{工作量}\ \textbf{集中于}\ \mathcal D_{\mathrm{reg}}✓✓$$
$$\textbf{对象}✓✓：\text{四奇矩条件在}\ \mathcal D_{\mathrm{reg}}\ \text{上的}\ \textbf{一维解族}✓；\ \text{对每支}\ \text{算}\ \max_{r \le 12} F_{2r}✓✓（\text{判}\ > \tfrac12✓）$$

## §4 关键箭头（✓✓）

$$\boxed{\mathcal D_{\mathrm{reg}}\ \text{完备覆盖} \Longrightarrow \mathcal Z \cap E = \varnothing}✓✓ \ —— \ \text{此箭头}\ \textbf{现才} \text{可能成立}✓✓（\text{因 boundary／collision 已处理}✓）$$
$$\textbf{Bridge A 暂不跳}✗✓：\text{先}\ \text{把}\ \mathcal Z \cap E\ \text{的}\ \textbf{exact-cancellation} \text{本身处理干净}✓✓；\text{顺序}\ \text{不可颠倒}✗✓$$

## §5 账本（✓✓）

| 层 ✓ | 状态 ✓ | 证据 ✓ |
|---|---|---|
| `\mathcal D_{\partial}` ✓ | **完整** ✓✓ | 解析 ✓ |
| `\mathcal D^{\mathrm{triple}}_{\mathrm{coll}}` ✓ | **`\varnothing`** ✓✓ | 解析消元 ✓ |
| `\mathcal D^{\mathrm{double}}_{\mathrm{coll}} \cap E` ✓ | **`\varnothing`** ✓✓ | **解析因式分解 ＋ 正性** ✓✓ |
| `\mathcal D_{\mathrm{reg}}` ✓ | **OPEN（下一目标）** ✓ | 协议已移植 ✓ |
| `\mathcal Z \cap E` ✓ | **OPEN** ✓ | — ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ | — ✓ |

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 碰撞部分排除 命中文件数=0    :: 
技术词 分层参数非假定 命中文件数=0    :: 
技术词 协议移植     命中文件数=0    :: 
技术词 战略转折     命中文件数=1    :: ./numberfield-positivity-CLOSED-2026-09-09.md 
```
- **零计算** ✗（注册档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗；`\mathcal D_{\mathrm{reg}}` 已处理 ✗；Bridge A 已启动 ✗
