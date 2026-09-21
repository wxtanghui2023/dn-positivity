已查地图（**先查后写**）：`C-331`（缺位定位：箱级 max–min 交换 ✓）、`C-330`（现有证书不能闭合 ✓）、`C-284`（同点／有限整数频率**泛函**坍缩 ✓）、`C-275`（组合空洞定理：可分层面混合＝单-k ✓）、`C-277`（覆盖：几何不强制 r>=1 ✓）、**`C-152`／`C-153`（M=2 已用覆盖型证明成功** ✓✓）、**`C-197`（一维 cover certificates PROVED** ✓✓）、`C-273`（Loss I／Loss II 分离 ＋ C-197 先例 ✓）。回查见 §6 ✓

D0: 本档对象 = **C-332：M5-覆盖审计（攻击联合坏集）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 路线纠正}✓✓：\text{停的是}\ \textbf{盲目枚举外部候选}✗；\textbf{不是} \text{我们自己研究缺口}✗✓ —— \textbf{两件事完全不同}✓$$
$$\textbf{② 命题等价改写}✓✓：\ \forall\theta\ \exists k:\ F_k(\theta) > \tfrac12 \iff H = \varnothing✓，\text{其中}\ H := \bigcap_{k=1}^{25} \{F_k \le \tfrac12\}✓$$
$$\textbf{③ 证书逻辑类型改变}✓✓：\text{固定频率证书（}\max_k \min_B F_k✓）\ \to\ \textbf{覆盖型证书}（\ B \subseteq \bigcup_k U_k✓，U_k := \{F_k > \tfrac12\}✓）$$
$$\textbf{④ 覆盖不在}\ C\text{-284 的闭合类内}✓✓：C\text{-284 封的是}\ \text{同点}＋\text{有限整数频率}＋\textbf{泛函}✓；\ \textbf{联合系统} \text{不是该对象}✓✓$$
$$\textbf{⑤ 三问答案}✓（\text{见 §3–§5}✓）：\textbf{可攻击}✓；\textbf{可绕开固定}\ k✓；\textbf{已有两类机制}＋\textbf{两项本项目先例}✓✓$$

## §1 对象改写（✓✓，关键一步 ✓）

$$\textbf{原命题}✓：\ \forall\theta \in [0,\pi]^5,\ \exists k \le 25:\ F_k(\theta) > \tfrac12✓，F_k(\theta) = \sum_{j=1}^{5} \cos(k\theta_j)✓$$
$$\textbf{等价的坏集形式}✓✓：\ H := \bigcap_{k=1}^{25} \{F_k \le \tfrac12\}✓ \Longrightarrow \text{命题} \iff H = \varnothing✓$$
$$\textbf{上包络}✓：\ G(\theta) := \max_{1 \le k \le 25} F_k(\theta)✓ \Longrightarrow \text{命题} \iff \inf_{\theta} G(\theta) > \tfrac12✓$$
$$\textbf{证书逻辑}✓✓：\text{命题}\ \textbf{从未要求} \text{「整个箱用同一个}\ k\text{」}✗✓；\text{separable 证书}\ \textbf{却强制} \text{如此}✗ \Longrightarrow \textbf{这正是交换缺口的来源}✓✓$$

## §2 跨 k 结构（✓✓，可分证书丢弃的信息 ✓）

$$\textbf{Chebyshev 联系}✓✓：\text{置}\ c_j := \cos\theta_j✓ \Longrightarrow F_k = \sum_{j=1}^{5} T_k(c_j)✓ \Longrightarrow H\ \text{是}\ c \in [-1,1]^5\ \text{中的}\ \textbf{半代数集}✓✓$$
$$\textbf{窗口内}\ \gcd = 1✓✓：\text{频率集}\ \{1,\dots,25\}\ \text{的}\ \gcd = 1✓ \Longrightarrow \text{C-284 的坍缩}\ \textbf{在此为恒等}✓（\text{不构成障碍}✓✓）$$
$$\textbf{可分证书丢掉的}✓✓：\text{它只取}\ \min_{I_j} \cos(k\,\cdot)✓（\text{逐坐标最坏}✓）\ \Longrightarrow \textbf{丢弃}\ \text{了}\ F_k\ \text{之间}\ \textbf{的跨}\ k\ \text{相关性}✓✓ \Longrightarrow \text{而}\ H\ \textbf{恰由该相关性定义}✓✓$$
$$\textbf{联合系统}✓：\text{假设}\ \theta \in H \Longrightarrow \text{得}\ \textbf{25 个不等式的联合约束}✓✓ \Longrightarrow \text{这是 separable 证书}\ \textbf{永远看不到} \text{的信息}✓✓$$

## §3 第一问：能否用递推／交互结构得到更强联合约束（✓）

$$\textbf{可得的结构}✓：\text{① } \sum_{k=1}^{25} F_k(\theta) = \sum_{j=1}^{5} D(\theta_j)✓（\textbf{Dirichlet 型核}✓）\ —— \ \textbf{纯跨}\ k\ \text{恒等式}✓✓；\text{② Chebyshev 递推}✓ T_{k+1} = 2xT_k - T_{k-1}✓ \Longrightarrow F_{k+1} = 2\sum_j c_j T_k(c_j) - F_{k-1}✓（\textbf{跨}\ k\ \text{递推}✓✓）；\text{③ Fejér 正性}✓（\sum_k \lambda_k \cos(k\theta) \ge -\tfrac12✓，C-274 ✓）$$
$$\textbf{诚实标注}⚠️：\text{① 的}\ \textbf{无权重和}\ \text{并不直接给下界}✓（D\ \text{可正可负}✓）；\textbf{需}\ \text{配权重}✓；\text{② 的递推是}\ \textbf{真结构}✓，\text{但本档}\ \textbf{未}\ \text{证它能给出}\ H\ \textbf{非空性的排除}✗（\text{登记为}\ \textbf{可攻击入口}✓）$$

## §4 第二问：能否不靠固定 k 证明 `B ∩ H = ∅`（✓✓）

$$\textbf{能}✓✓：\text{这正是}\ \textbf{覆盖型证书}✓：\ B \subseteq \bigcup_{k=1}^{25} U_k✓，U_k := \{F_k > \tfrac12\}✓$$
$$\textbf{本项目已有两项先例}✓✓（\text{非外部}✓）：\text{① }\textbf{M=2}\ \text{已用「极小点处精确代数 ＋ 其余 Liposchitz」的}\ \textbf{覆盖型} \text{证明成功}✓✓（C-152／C-153✓，覆盖平面✓）；\text{② }\textbf{一维 cover certificates}\ \textbf{已证}✓✓（C-197✓，1-D 覆盖证书 ✓）$$
$$\textbf{但}✓✗：\text{不能用「区间宽度」类}\ \textbf{naive 覆盖}✗ —— \ C-277\ \text{已证几何}\ \textbf{不}\ \text{强制}\ r \ge 1✗✓ \Longrightarrow \text{覆盖证书}\ \textbf{必须用箱级／结构化信息}✓✓，\textbf{不是}\ \text{只用宽度}✗$$

## §5 第三问：机制命名（**只在发现之后命名** ✓）

$$\textbf{已实际指认的机制}✓✓：\text{① }\textbf{覆盖／有限子覆盖}✓（\text{两项本项目先例}✓）；\text{② }\textbf{联合半代数证书}✓（H\ \text{是}\ c\ \text{中的半代数集}✓；\text{SOS／Positivstellensatz 型}✓\ —— \textbf{不被}\ C\text{-284 阻挡}✓✓，\text{因}\ \gcd = 1✓）；\text{③ }\textbf{核恒等式／递推}✓（Dirichlet 和✓；Chebyshev 递推✓；Fejér 正性✓）$$
$$\textbf{登记纪律}✓✓：\textbf{不}\ \text{预先建筛选器}✗；\textbf{不}\ \text{命名新框架}✗；\text{只在}\ \textbf{实际用到}\ \text{时登记}✓✓；\text{当前}\ \textbf{未}\ \text{产出任何 M=5 证明}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 覆盖审计     命中文件数=5    :: ./V109-coverage-argument-charter.md ./EXPLORATION-POINTS-REGISTER.md ./C104-mechanism-extraction-audit-five-primitives-vs-archive-FZ2-FZ3.md 
技术词 上包络        命中文件数=0    :: 
技术词 联合半代数证书 命中文件数=0    :: 
技术词 覆盖型证书  命中文件数=0    :: 
```
- 本档新增 ✓：`覆盖审计`／`联合半代数证书`／`覆盖型证书`（依上表判 ✓；`覆盖证书` 已在 `C-197` 存在 ⟹ **引用不新命名** ✓）
- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：M=5 已可证 ✗；覆盖＝成功 ✗；C-284 阻挡覆盖路线 ✗（**不阻挡** ✓）；本档已产出证明 ✗
