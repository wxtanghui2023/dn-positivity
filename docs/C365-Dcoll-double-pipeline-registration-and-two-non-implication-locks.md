已查地图（**先查后写**）：`C-364`（**二维 Jacobian 口径** ✓✓；可行域门槛 ✓）、`C-363`（消元降维 ✓✓）、`C-362`（措辞锁定 ✓✓）、`C-361`（三重解析判空 ✓✓）。回查见 §4 ✓

D0: 本档对象 = **C-365：`\mathcal D^{\mathrm{double}}_{\mathrm{coll}}` 流水线登记 ＋ 两条非蕴含锁定**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① 审计对象已确定}✓✓：\ \boxed{\mathcal D^{\mathrm{double}}_{\mathrm{coll}} \ \rightsquigarrow \ (E_5(t,u),\ E_7(t,u)) \ + \ \mathcal F(t,u)}✓✓ \ —— \ \textbf{二维解析审计对象}✓✓，\textbf{不是}新猜想✗✓$$
$$\textbf{② ⭐ 两条非蕴含锁定}✓✓：$$
$$\qquad \boxed{\text{二维参数化} \ \ne \ \text{二维判空}}✓✓；\qquad \boxed{\det J = 0 \ \ne \ \text{无根}}✓✓$$
$$\textbf{③ 流水线登记（\textbf{不执行}}✓）✓✓：\text{见 §1}✓；\ \textbf{不提前执行}✗、\ \textbf{不新增方法}✗✓$$
$$\textbf{④ 上限锁定}✓✓：\text{即便得}\ \mathcal D^{\mathrm{double}}_{\mathrm{coll}} \cap E = \varnothing✓，\ \textbf{仍只是碰撞层排除}✓✓ \ —— \ \textbf{不是}\ \mathcal Z \cap E = \varnothing✗，\ \textbf{更不是}\ H = \varnothing✗✓$$

## §1 流水线（✓✓，登记不执行 ✓）

$$\textbf{① 二维域覆盖}✓：\text{细分}\ (t,u) \in (0,1]^2✓；\ \textbf{② 可行性过滤}\ \mathcal F✓✓（\textbf{前置门槛}✓：s^2 - 4p \ge 0✓；0 < \beta, b_2 \le 1✓；s \le 2✓；1 - s + p \ge 0✓）$$
$$\textbf{③ 共同根隔离}✓：\text{区间求值}\ (E_5, E_7)✓ \Longrightarrow \text{排除盒} ＋ \text{候选盒细分}✓；\ \textbf{④ } \det J \ne 0✓ \Longrightarrow \text{逐根隔离}✓✓（Krawczyk✓）$$
$$\qquad \det J = 0✓ \Longrightarrow \textbf{singular-substratum}✓✓（\text{不得记无根}✗✓）$$
$$\textbf{⑤ } (\beta, b_2)\ \text{回溯}✓（\text{由}\ s, p✓）；\ \textbf{⑥ 偶频核算}✓：\max_{r \le 12} F_{2r} > \tfrac12\ ?✓✓$$
$$\textbf{覆盖义务}✓✓：\text{仅当}\ \textbf{全部} \text{二维共同根}\ \textbf{及奇异层} \text{完成覆盖}✓ \Longrightarrow \text{才得}\ \mathcal D^{\mathrm{double}}_{\mathrm{coll}} \cap E = \varnothing✓✓$$
$$\qquad \textbf{注意}✓✓：\text{逐根}\ \det J \ne 0\ \text{只给}\ \textbf{局部孤立}✓，\text{不构成}\ \textbf{全支覆盖}✗✓$$

## §2 状态表（✓✓）

| 层 ✓ | 状态 ✓ | 证据 ✓ |
|---|---|---|
| `\mathcal D_{\partial}` ✓ | **完整** ✓✓ | 解析 ✓ |
| `\mathcal D^{\mathrm{triple}}_{\mathrm{coll}}` ✓ | **`\varnothing`** ✓✓ | **解析消元（`r=1,3,5`）** ✓✓ |
| `\mathcal D^{\mathrm{double}}_{\mathrm{coll}}` ✓ | **OPEN** ✓ | **二维参数化** ✓ |
| `\mathcal D_{\mathrm{reg}}` ✓ | **OPEN** ✓ | 尚未进入 ✓ |
| `\mathcal Z \cap E` ✓ | **OPEN** ✓ | — ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ | — ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal D^{\mathrm{double}}_{\mathrm{coll}} = \varnothing\ \text{已证}✗；\mathcal Z \cap E = \varnothing\ \text{已证}✗；H = \varnothing\ \text{已证}✗；\det J = 0 \Rightarrow \text{无根}✗$$
$$\textbf{纪律}✓✓：\text{当前路线}\ \textbf{无逻辑越级}✓✓，\ \textbf{无新增方法}✓✓；\text{C-364 封口}✓$$

## §4 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 二维参数化非判空 命中文件数=0    :: 
技术词 雅可比零非无根 命中文件数=0    :: 
技术词 碰撞层排除上限 命中文件数=0    :: 
```
- **零计算** ✗（登记档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
