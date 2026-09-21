已查地图（**先查后写**）：`C-349`（抵消理想 ✓✓；**§3 待降级** ⚠️）、`C-348`（反称族 `\not\subset E`✓）、`C-347`（奇偶层分离 ✓✓）、`C-343`（straddling ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-350：零矩流形审计 ＋ Bridge A／B 拆分**，**零计算（解析）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① C-349 §3 已降级}✓✓（\text{采纳唐先生}✓）：\text{四矩消失}\ \not\Rightarrow\ \text{已证的精确加倍分类}✗✓ \ —— \ \text{理由}✓：\text{权重为}\ \sqrt{x_j}✓（\text{非自由}✓），\text{仅四矩方程}✓，\text{五个非零原子}\ \textbf{不自动唯一}✗✓$$
$$\textbf{② 已补证的一个情形}✓✓：\textbf{2+2 分裂 ＋ 成对结构} \Longrightarrow \textbf{反称}✓✓（\text{证明见 §2}✓）\ \Longrightarrow \text{C-349 的结论}\ \textbf{只在受限情形成立}✓✓$$
$$\textbf{③ Z 可能严格更大}⚠️✓：3+2／4+1 分裂\ \textbf{未被排除}✗✓ \Longrightarrow \ \mathcal Z\ \textbf{不等于} \text{反称族}✗✓ \ —— \ \text{分类是}\ \textbf{真任务}✓$$
$$\textbf{④ ⭐ 决定性等价}✓✓：\ \boxed{\mathcal Z \cap E \ne \varnothing \Longrightarrow H \ne \varnothing}✓✓ \ —— \ \text{因}\ \mathcal Z\ \text{上奇频恰为 0}✓（\le \tfrac12✓）\ \Longrightarrow \text{只剩偶频}✓✓$$
$$\textbf{⑤ Bridge A 的精确障碍}✓✓：\text{矩映射在}\ 5\ \text{原子处 Jacobian 秩}\ 4✓ \Longrightarrow \text{局部} 1\ \text{维}✓；\text{但在}\ \textbf{退化点}（\text{原子碰撞／权重趋零}✓）\ \text{处秩掉}✗ \Longrightarrow \textbf{统一常数不可得}✗✓$$

## §1 C-349 §3 降级（✓✓）

$$\textbf{原主张}✗：\text{「}p + q = 5,\ r = 4\ \text{为 Gauss 边界}\ \Longrightarrow\ \text{零矩配置}\ \textbf{完全分类}」✗✓$$
$$\textbf{降级后}✓：\text{四矩消失}\ \Longrightarrow\ \text{仅得}\ \textbf{强零点计数／交错约束}✓（\text{函数族}\ y, y^3, y^5, y^7\ \text{为 T-system}✓），\textbf{不}\ \text{自动得}\ \text{成对＋零结构}✗✓$$
$$\textbf{变量形式}✓✓：y_j := \sqrt{x_j} > 0✓ \Longrightarrow \text{条件} = \sum_j \sigma_j y_j^{2m+1} = 0\ (m = 0,1,2,3)✓✓ \iff \text{带号幂和}\ p_n := \sum_j \sigma_j y_j^n\ \textbf{在}\ n = 1,3,5,7\ \text{处为 0}✓✓$$

## §2 已证情形：2+2 分裂 ⟹ 反称（✓✓）

$$\textbf{设定}✓：\text{取}\ y = (y_1, y_2, y_3, y_4, 0)✓，\sigma = (+, +, -, -, \cdot)✓ \Longrightarrow \text{条件}\ \sum_{i \le 2} y_i^n = \sum_{i \ge 3} y_i^n\ (n = 1, 3, 5, 7)✓✓$$
$$\textbf{关键}✓✓：\text{两个二元多重集的} \textbf{前四阶幂和相等}✓ \Longrightarrow \text{二者}\ \textbf{作为多重集相等}✓✓（\text{二元多重集由前两阶幂和确定}✓，四阶为冗余但仍一致✓）$$
$$\Longrightarrow \ y_1 + y_2 = y_3 + y_4✓，\ y_1y_2 = y_3y_4✓ \Longrightarrow \{y_1, y_2\} = \{y_3, y_4\}✓✓ \Longrightarrow \textbf{反称族}✓（c = (a, -a, b, -b, 0)✓）$$
$$\Longrightarrow \textbf{结论}✓✓：\text{在 2+2 分裂且两侧各为二元的情形下，}\ \mathcal Z\ \text{的这一分支}\ \textbf{恰为反称族}✓✓ \ —— \ \text{与 C-348 的成本}\ 1.4677✗\ \text{相容}✓$$

## §3 `\mathcal Z` 的更大性（⚠️✓）

$$\textbf{3+2 分裂}✓：\text{需}\ \sum_{i \le 3} y_i^n = \sum_{i \ge 4} y_i^n\ (n = 1,3,5,7)✓ \ —— \ \text{四方程}、\text{五未知}✓ \Longrightarrow \text{一般有}\ \textbf{一维解族}✓✗$$
$$\qquad \textbf{即}✓：\text{一个}\ \textbf{三原子}\ \text{测度用四矩匹配另一}\ \textbf{二原子}\ \text{测度}✓ \ —— \ \text{权重仍受}\ y_j\ \text{约束}✓，\text{故}\ \textbf{不能}\ \text{断定无解}✗✓$$
$$\textbf{4+1 分裂}✓：\text{更极端}✓（\text{单原子匹配四矩}⟹\text{需该原子权重为 0}✓ \Longrightarrow \text{排除}✓）$$
$$\Longrightarrow \ \boxed{\mathcal Z\ \text{的结构}\ \textbf{未知}✗✓} \ \Longrightarrow \text{必须先分类}\ \mathcal Z✓（\text{或至少给出定量邻域控制}✓）$$

## §4 ⭐ 决定性等价（✓✓，本档核心 ✓）

$$\text{因}\ \mathcal Z\ \text{上}\ F_1 = F_3 = F_5 = F_7 = 0✓ \Longrightarrow \text{奇频约束}\ \textbf{自动满足}✓（0 \le \tfrac12✓）$$
$$\Longrightarrow \ \boxed{\text{找}\ (x, \sigma) \in \mathcal Z\ \text{使}\ \max_{r \le 12} F_{2r} \le \tfrac12 \ \Longrightarrow \ H \ne \varnothing✓✓}$$
$$\textbf{读法}✓✓：\text{「问题 2」（}\mathcal Z\ \text{邻域是否必有偶频成本}\ > \tfrac12✓）\ \ \textbf{就是}\ H = \varnothing\ \text{的一个子情形}✓✓ \ —— \ \text{且是}\ \textbf{最危险} \text{的子情形}✓✓$$
$$\textbf{副产品}✓✓：\text{这给出}\ \textbf{最廉价的反例搜索} \text{形式}✓：\text{在}\ \mathcal Z\ \text{上只查偶频}✓（\text{而非全 25 频}✓）✓✓$$

## §5 Bridge A／B 拆分（✓✓，采纳唐先生 ✓）

$$\textbf{Bridge A}✓：\max_{r \le 3}|F_{2r+1}| \le \tfrac12 \Longrightarrow \operatorname{dist}(x, \mathcal Z) \le \Phi(\tfrac12)✓$$
$$\qquad \textbf{障碍定位}✓✓：\text{矩映射}\ \Phi_4: y \mapsto (p_1, p_3, p_5, p_7)✓ \ \text{的 Jacobian 秩为}\ 4✓ \Longrightarrow \text{局部} 1\ \text{维水平集}✓；\text{但}\ \textbf{退化点}（y_i\ \text{碰撞}✓、\ y_i \to 0✓、\text{符号抵消退化}✓）\ \text{处秩掉}✗✓$$
$$\qquad \Longrightarrow \ \text{须} \textbf{先排除／分类退化点}✓✓，\text{否则}\ \Phi\ \text{无统一常数}✗✓ \ —— \ \text{这是 Bridge A 的真正难点}✓✓$$
$$\textbf{Bridge B}✓：\operatorname{dist}(x, \mathcal Z) \le \delta \Longrightarrow \max_{r \le 12} F_{2r} \ge \tfrac12 + \eta(\delta)✓$$
$$\qquad \text{已知}✓：\mathcal Z\ \text{的反称分支上成本} \ge 1.4677✓（C-348✓）\ \Longrightarrow \ \eta(0) \ge 0.9677✓✓；\text{连续化（}\eta(\delta)✓）\ \textbf{未证}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 零矩流形     命中文件数=0    :: 
技术词 定量单射性  命中文件数=1    :: ./C349-cancellation-ideal-and-bridge-inequality-candidate.md 
技术词 退化点        命中文件数=2    :: ./C281-two-pair-supply-uniform-margin-compactness-continuity-existence-closure.md ./C234-B2-1-first-step-2D-KKT-framework-and-w-to-infinity-leading-structure.md 
技术词 决定性等价  命中文件数=0    :: 
```
- **零计算** ✗（解析 ✓）；`D1 = 0` ✓；未改他档正本 ✓（`C-349` §3 仅在**本档**降级 ✓，其正本未改 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`\mathcal Z` 已分类 ✗；Gauss 边界已给完全分类 ✗（**已降级** ✓）；Bridge A／B 已证 ✗；`H = \varnothing` 已证 ✗
