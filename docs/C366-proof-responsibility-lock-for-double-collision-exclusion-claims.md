已查地图（**先查后写**）：`C-365`（**流水线登记** ✓✓；两条非蕴含 ✓✓）、`C-364`（**二维 Jacobian 口径** ✓✓）、`C-363`（消元降维 ✓✓）。回查见 §4 ✓

D0: 本档对象 = **C-366：证明责任锁定（双重碰撞层排除声明的三条件）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① C-365 封口}✓✓：\ \boxed{\mathcal D^{\mathrm{double}}_{\mathrm{coll}} \ \rightsquigarrow \ (E_5, E_7) + \mathcal F}✓✓ \ —— \ \text{该形式}\ \textbf{无需}再增数学框架✗✓$$
$$\textbf{② ⭐ 证明责任锁定（本档核心）}✓✓：\text{任何声称}\ \text{「双重碰撞层已排除」} \ \textbf{必须同时} \text{回答以下三事}✓✓：$$
$$\qquad \textbf{(1)}\ \text{二维可行域是否}\ \textbf{完整覆盖}✓；\ \textbf{(2)}\ \text{所有共同根}\ \textbf{以及}\ \det J = 0\ \textbf{奇异层} \text{是否}\ \textbf{完整处理}✓；\ \textbf{(3)}\ \text{每个}\ \textbf{实际可行根} \text{是否满足}\ \max_{r \le 12} F_{2r} > \tfrac12✓$$
$$\qquad \Longrightarrow \ \text{缺任何一项}✓ \Longrightarrow \ \textbf{只能停在 OPEN}✗✓$$
$$\textbf{③ ⭐ 覆盖非蕴含锁定}✓✓：\ \boxed{\det J \ne 0 \Longrightarrow \text{局部孤立} \ \not\Longrightarrow \ \text{全局分支覆盖}}✓✓$$
$$\qquad \Longrightarrow \ \text{即便 Krawczyk 对}\ \textbf{大量盒子} \text{给出唯一根}✓，\ \textbf{不能}把「已发现的根」升级成「所有根」\ ✗✓$$
$$\textbf{④ 账本与路线}✓✓：\text{见 §2／§3}✓ \ —— \ \textbf{不}新增框架✗，\textbf{不}越级✗$$

## §1 三条件的用途（✓✓）

$$\textbf{用途}✓✓：\text{它是}\ \textbf{引用纪律}✓ \ —— \ \text{未来任何}\ \text{「碰撞层已排除」} \ \text{的表述}✓ \ \textbf{必须} \text{附上}\ \text{三条件的证据位置}✓✓$$
$$\qquad \Longrightarrow \ \text{防止}\ \text{「发现若干根}\ \to\ \text{声称全支」} \ \text{的升级错误}✗✓（\text{与 C-354 三层分离同源}✓）$$
$$\textbf{与既有纪律的一致性}✓✓：\text{C-354}（\text{发现／证书／覆盖}✓）；\text{C-364}（\det J\ \text{口径}✓）；\text{C-365}（\text{两条非蕴含}✓） \ \Longrightarrow \ \text{本档为}\ \textbf{责任清单}✓✓$$

## §2 账本（✓✓）

| 层 ✓ | 状态 ✓ |
|---|---|
| `\mathcal D_{\partial}` ✓ | **完整｜解析** ✓✓ |
| `\mathcal D^{\mathrm{triple}}_{\mathrm{coll}}` ✓ | **`\varnothing`｜解析消元（`r=1,3,5`）** ✓✓ |
| `\mathcal D^{\mathrm{double}}_{\mathrm{coll}}` ✓ | **OPEN｜二维参数化** ✓ |
| `\mathcal D_{\mathrm{reg}}` ✓ | **OPEN** ✓ |
| `\mathcal Z \cap E` ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §3 路线（✓✓）

$$\mathcal D^{\mathrm{double}}_{\mathrm{coll}} \ \xrightarrow{\text{完备区间审计}} \ \text{碰撞层结论} \ \xrightarrow{\text{再处理}\ \mathcal D_{\mathrm{reg}}} \ \mathcal Z \cap E \ \xrightarrow{\text{最终桥}} \ H = \varnothing✓✓$$
$$\textbf{注意}✓✓：\text{第二箭头}\（\mathcal D_{\mathrm{reg}}\ \text{尚未进入}✓） \ \textbf{与}\ \text{第三箭头}\（\textbf{Bridge A}✓）\ \text{均}\ \textbf{未开始}✗✓$$

## §4 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 证明责任三条件 命中文件数=0    :: 
技术词 局部孤立非全局覆盖 命中文件数=0    :: 
技术词 碰撞层结论  命中文件数=0    :: 
```
- **零计算** ✗（责任清单档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`\mathcal D^{\mathrm{double}}_{\mathrm{coll}}` 已排除 ✗；`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗
