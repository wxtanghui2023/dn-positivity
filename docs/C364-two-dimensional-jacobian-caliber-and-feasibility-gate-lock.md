已查地图（**先查后写**）：`C-363`（**消元降维** ✓✓；证据等级 ✓）、`C-362`（三重措辞锁定 ✓✓）、`C-361`（**三重解析判空** ✓✓）、`C-355`（五件套 ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-364：二维 Jacobian 口径 ＋ 可行域门槛锁定**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 消元公式确认}✓✓：\ \boxed{p\,s = 2t(t+u)^2}✓，\ \boxed{p = \dfrac{2t(t+u)^2}{2t+u}}✓（s = 2t + u✓） \ —— \ (\beta, b_2)\ \textbf{确实被消去}✓✓$$
$$\textbf{② 必须保留}\ (E_5, E_7)✓✓：\text{双重情形无即时矛盾}✓（\text{与 triple 不同}✓）；\text{仅在其}\ \textbf{共同零点} \text{区间覆盖后}\ \text{才谈判空}✓✓$$
$$\textbf{③ 可行域过滤前置}✓✓：\text{作为}\ \textbf{门槛}✓（\text{非事后检查}✓）：s^2 - 4p \ge 0✓；\ 0 < \beta, b_2 \le 1✓；\ \text{等价约束}\ s \le 2✓，\ 1 - s + p \ge 0✓✓$$
$$\qquad \Longrightarrow \ \textbf{否则}会把虚根或区间外根误计入✗✓$$
$$\textbf{④ ⭐ Jacobian 口径锁定（本档核心）}✓✓：\ J := \dfrac{\partial(E_5, E_7)}{\partial(t,u)}✓ \ —— \ \textbf{最终二维系统} \text{的 Jacobian}✓✓，\ \textbf{不是}原始四变量系统的✗✓$$
$$\qquad \det J(t_*, u_*) \ne 0 \Longrightarrow \text{二维共同根}\ \textbf{局部孤立}✓✓；\ \det J = 0 \Longrightarrow \textbf{不能判空}✓，\text{进}\ \textbf{singular-substratum}✓✓$$
$$\qquad \textbf{措辞禁令}✗✓：\textbf{不得}把「二维化后一般离散」\ \text{写成}\ \text{「所有根必孤立」}✗✓$$
$$\textbf{⑤ 证据等级（本档判定）}✓✓：\textbf{解析参数化／消元}✓；\ \textbf{区间完备}✗；\ \textbf{判空}✗ \ \Longrightarrow \ \textbf{绝不能写}\ \mathcal D^{\mathrm{double}}_{\mathrm{coll}} = \varnothing✗✓$$

## §1 链条（✓✓）

$$\boxed{\mathcal D^{\mathrm{double}}_{\mathrm{coll}} \ \longrightarrow \ (E_5(t,u),\ E_7(t,u)) \ + \ \mathcal F(t,u)}✓✓ \ —— \ \mathcal F = \text{由}\ (s, p)\ \text{恢复}\ \beta, b_2\ \text{的可行性条件}✓✓$$
$$\textbf{六步}✓✓：\text{二维区间覆盖} \to \text{共同根隔离} \to \det J \to \text{奇异层} \to (\beta, b_2)\ \text{回溯} \to \text{偶频核算}✓✓$$

## §2 证据等级对照（✓✓）

| 层 ✓ | 证据 ✓ | 可写出的结论 ✓ |
|---|---|---|
| `D_coll^triple` ✓ | **解析消元（`r=1,3,5`）** ✓✓ | **`= \varnothing`** ✓✓ |
| `D_coll^double` ✓ | **仅解析参数化／消元** ✓ | **`(E_5, E_7) + \mathcal F` 形式已定** ✓（**不得**写判空 ✗✓） |
| `D_reg` ✓ | 未进入 ✓ | OPEN ✓ |

$$\textbf{纪律}✓✓：\text{两者}\ \textbf{证据等级差异明确}✓✓ \ —— \ \text{三重的「判空」}\ \textbf{不能}类推到双重✗✓$$

## §3 下一步（✓✓，登记不执行 ✓）

$$\textbf{登记}✓✓：\text{执行}\ \textbf{二维区间完备协议}✓（\text{C-363 §3}✓＋\text{本档门槛与 Jacobian 口径}✓）；\ \textbf{不提前执行}✗、\ \textbf{不新增方法}✗✓$$
$$\textbf{仅当}✓✓：\text{二维覆盖完成且}\ \textbf{逐根偶频} > \tfrac12✓ \Longrightarrow \text{才可写}\ \mathcal D^{\mathrm{double}}_{\mathrm{coll}} \cap E = \varnothing✓✓$$
$$\textbf{且即便如此}✓✓：\ \mathcal Z \cap E\ \text{与}\ H = \varnothing\ \text{仍}\ \textbf{OPEN}✓✓（\text{还须}\ \mathcal D_{\mathrm{reg}}✓）$$

## §4 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal D^{\mathrm{double}}_{\mathrm{coll}} = \varnothing✓\ \text{已证}✗；\text{二维化}\ \Longrightarrow\ \text{所有根孤立}✗；\ H = \varnothing\ \text{已证}✗；\text{降维即判空}✗$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓，\text{仅锁定}\ \text{门槛与口径}✓；\ (E_5),(E_7)\ \text{的显式展开}\ \textbf{仍待写}✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 二维雅可比口径 命中文件数=0    :: 
技术词 可行域门槛  命中文件数=0    :: 
技术词 证据等级对照 命中文件数=0    :: 
```
- **零计算** ✗（口径锁定档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
