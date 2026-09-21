已查地图（**先查后写**）：`C-362`（三重层判空措辞锁定 ✓✓）、`C-361`（三重为空 ✓✓）、`C-360`（永非反称 ✓）、`C-355`（五件套 ✓✓）、`C-356`（分层 ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-363：双重碰撞层消元（降为二维两方程）**，**零计算（解析）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① C-362 封口}✓✓：\text{当前唯一未完成的碰撞分支}\ = \mathcal D^{\mathrm{double}}_{\mathrm{coll}}✓；\text{状态链}\ \mathcal D_{\partial}\ \text{已完备} \to \mathcal D^{\mathrm{triple}}_{\mathrm{coll}} = \varnothing\ \text{已解析判空} \to \mathcal D^{\mathrm{double}}_{\mathrm{coll}}\ \text{待完备} \to \mathcal D_{\mathrm{reg}}\ \text{未进入}✓✓$$
$$\textbf{② ⭐ 新增：消元降维（本档核心）}✓✓：\text{双重情形}\ a_1 = a_2 = t \ne u = a_3✓；\text{由}\ r = 1,3\ \textbf{消去}\ (\beta, b_2)✓✓：$$
$$\qquad \boxed{p\,s = 2t\,(t+u)^2}✓✓（s := \beta + b_2 = 2t + u✓，\ p := \beta b_2✓）$$
$$\Longrightarrow \ \text{未知降为}\ (t, u)✓，\ \text{余下}\ r = 5,7\ \text{给}\ \textbf{两方程}✓✓ \Longrightarrow \ \textbf{离散}✓ \Longrightarrow \text{二维审计域}✓✓$$
$$\textbf{③ 可行性约束}✓✓：\beta, b_2\ \text{为}\ x^2 - sx + p = 0\ \text{的两根}✓ \Longrightarrow \ s^2 - 4p \ge 0✓；\text{且}\ \beta, b_2 \in (0,1]✓ \Longrightarrow \textbf{根位约束}✓✓$$
$$\textbf{④ 判空纪律}✓✓：\mathcal D^{\mathrm{double}}_{\mathrm{coll}}\ \text{为空}\ \textbf{须由区间盒覆盖} \text{证明}✓✓；\text{发现层零根}\ \textbf{不能}判空✗✓$$
$$\textbf{⑤ 账本}✓✓：\mathcal D^{\mathrm{double}}_{\mathrm{coll}}\ \text{OPEN（本档将审计域降为二维）}✓；\mathcal D_{\mathrm{reg}}\ \text{OPEN}✓；\ \mathcal Z \cap E\ \text{OPEN}✓；\ H = \varnothing\ \text{OPEN}✓$$

## §1 消元推导（✓✓，逐行 ✓）

$$\textbf{条件}✓：2t + u = \beta + b_2 = s✓；\ 2t^3 + u^3 = \beta^3 + b_2^3✓；\ 2t^5 + u^5 = \beta^5 + b_2^5✓；\ 2t^7 + u^7 = \beta^7 + b_2^7✓$$
$$\textbf{牛顿恒等式}✓：\beta^3 + b_2^3 = s^3 - 3ps✓；\ \beta^5 + b_2^5 = s^5 - 5s^3p + 5sp^2✓；\ \beta^7 + b_2^7 = s^7 - 7s^5p + 14s^3p^2 - 7sp^3✓$$
$$\textbf{第一步}✓✓（r = 1,3✓）：s^3 = (2t+u)^3 = 8t^3 + 12t^2u + 6tu^2 + u^3✓ \Longrightarrow 2t^3 + u^3 = s^3 - 3ps✓$$
$$\qquad \Longrightarrow \ 3ps = 6t^3 + 12t^2u + 6tu^2 = 6t(t+u)^2✓ \Longrightarrow \ \boxed{ps = 2t(t+u)^2}✓✓ \Longrightarrow p = \dfrac{2t(t+u)^2}{s}✓$$
$$\textbf{第二步}✓✓：\text{代入}\ r = 5✓ \Longrightarrow 2t^5 + u^5 = s^5 - 5s^3p + 5sp^2✓ \Longrightarrow \text{以}\ s = 2t+u✓、p\ \text{表出}\ \Longrightarrow \textbf{方程 (E5)（仅含}\ t, u\text{）}✓✓$$
$$\textbf{第三步}✓✓：\text{同理}\ r = 7 \Longrightarrow \textbf{方程 (E7)（仅含}\ t, u\text{）}✓✓ \Longrightarrow \ (t,u)\ \textbf{两方程两未知}✓✓ \Longrightarrow \textbf{离散}✓$$
$$\textbf{对比三重情形}✓✓：\text{三重时}\ r = 1,3\ \text{已给}\ p = \tfrac{8}{3}t^2✓，\text{故}\ r = 5\ \text{直接矛盾}✓（C-361✓）；\text{双重时}\ p\ \text{仍是}\ t,u\ \text{的函数}✓，\text{故需}\ r = 5,7\ \text{两方程}✓✓$$

## §2 可行性约束（✓✓）

$$\textbf{实根条件}✓✓：s^2 - 4p \ge 0✓ \Longrightarrow s^2 \ge \dfrac{8t(t+u)^2}{s}✓ \Longrightarrow s^3 \ge 8t(t+u)^2✓（s > 0✓）$$
$$\textbf{根位条件}✓✓：\beta, b_2 \in (0,1]✓ \Longrightarrow s \le 2✓；\ p \le \min(\beta, b_2)\,s✓；\text{且}\ 1 - s + p \ge 0✓（\text{两根} \le 1✓）$$
$$\qquad \Longrightarrow \ \text{审计域}\ (t,u) \in (0,1]^2✓ \ \text{须再加}\ \textbf{可行性过滤}✓✓（\text{否则}\ (t,u)\ \text{解可能对应不可行的}\ \beta, b_2✓）$$

## §3 二维区间完备协议（✓✓，登记不执行 ✓）

$$\textbf{对象}✓✓：\text{在}\ (t,u) \in (0,1]^2✓ \ \text{上解}\ (E5) \wedge (E7)✓ \ \text{并施加 §2 过滤}✓$$
$$\textbf{步骤}✓✓：\text{① 二维细分}✓；\text{② 区间求值}\ (E5),(E7)✓ \Longrightarrow \text{排除盒}（\text{残差区间不含 0}✓）＋ \text{候选盒细分}✓；\text{③ 收缩至容差}✓ \Longrightarrow \text{Krawczyk}✓$$
$$\qquad \text{④ 每根检查}\ \textbf{双侧 Jacobian}（\text{对}\ (t,u)✓）\ \det J \ne 0✓✓；\text{⑤ }\det J = 0 \Longrightarrow \textbf{singular-substratum}✓✓；\text{⑥ 回溯}\ \beta, b_2✓（\text{由}\ s, p✓）\ \text{并逐根偶频核算}\ \max_{r \le 12} F_{2r}✓✓$$
$$\textbf{优势}✓✓：\text{审计域由}\ 4\ \text{维降为}\ 2\ \text{维}✓✓ \ —— \ \text{区间覆盖成本}\ \textbf{大幅下降}✓✓；\text{且仍}\ \textbf{不}新增方法✗（\text{沿用 C-355 五件套}✓）$$

## §4 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal D^{\mathrm{double}}_{\mathrm{coll}} = \varnothing\ \text{已证}✗；\mathcal Z \cap E = \varnothing\ \text{已证}✗；H = \varnothing\ \text{已证}✗；\text{降维即判空}✗$$
$$\textbf{诚实标注}⚠️✓：\text{本档只完成}\ \textbf{参数化（消元）}✓，\ \textbf{未}做区间覆盖✗✓；\ (E5),(E7)\ \text{的显式展开}\ \textbf{待写}✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 双重碰撞消元 命中文件数=0    :: 
技术词 二维审计域  命中文件数=0    :: 
技术词 判别式可行性 命中文件数=0    :: 
技术词 参数化降维  命中文件数=0    :: 
```
- **零计算** ✗（解析 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：降维即判空 ✗；`\mathcal D^{\mathrm{double}}_{\mathrm{coll}}` 为空 ✗；`H = \varnothing` 已证 ✗
