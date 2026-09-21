已查地图（**先查后写**）：`C-371`（**`\mathcal D_{\mathrm{reg}} = \varnothing`；`\mathcal Z \cap E = \varnothing`** ✓✓）、`C-370`（四次方程／尺度 × 形状 ✓✓）、`C-369`（协议移植 ✓✓）、`C-355`（紧性纪律 ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-372：Bridge A 两阶段形式化 ＋ 证据边界归档**，**零计算（形式化登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① } \mathcal Z \cap E = \varnothing\ \textbf{已闭合}✓✓：\mathcal D_{\partial} \cap E = \varnothing✓；\ \mathcal D_{\mathrm{coll}} \cap E = \varnothing✓；\ \mathcal D_{\mathrm{reg}} = \varnothing✓（C-371✓） \Longrightarrow \boxed{\mathcal Z \cap E = \varnothing}✓✓$$
$$\textbf{② 维数修正归档（唐先生口径）}✓✓：\text{齐次尺度作用}\ (a_i, \beta, b_2) \mapsto (\lambda a_i, \lambda\beta, \lambda b_2)✓ \Longrightarrow \text{五维分解为}\ \boxed{\text{尺度}(1) + \text{形状}(4)}✓✓$$
$$\qquad \text{四个独立奇矩条件作用于形状空间}✓：4 - 4 = 0✓ \Longrightarrow \boxed{\text{离散形状} \times \text{尺度}}✓✓ \ —— \ \textbf{不是} \text{一维形状曲线}✗✓$$
$$\textbf{③ ⭐ Bridge A 两阶段形式化（本档核心）}✓✓：\text{Stage 1}\ E \xrightarrow{\text{紧性}} \operatorname{dist}(E, \mathcal Z) > 0✓✓；\ \text{Stage 2}\ \operatorname{dist}(E, \mathcal Z) > 0 \Longrightarrow \max_{k \le 25} F_k > \tfrac12✓✓（\textbf{困难所在}✓✓）$$
$$\textbf{④ 方向纪律}✓✓：\textbf{不能}仅因\ \mathcal Z \cap E = \varnothing\ \text{就声称存在统一}\ \delta✗✓ \ —— \ \textbf{须先} \text{确认}\ E\ \text{的}\ \textbf{紧性／闭性} \text{与}\ \textbf{距离／奇矩范数} \text{定义}✓✓$$
$$\textbf{⑤ 证据边界}✓✓：\mathcal Z \cap E = \varnothing\ \text{的依据} = \textbf{C-371 的消元等价链逐步证明}✓✓（\textbf{非} resultant 数值✓）；\ \text{4000 起点最小二乘}\ = \ \boxed{\textbf{independent sanity check}}✓✓，\textbf{非}判空依据✗✓$$

## §1 Bridge A 的中间命题（✓✓，反证型 ✓）

$$\boxed{\max_{1 \le r \le 12} F_{2r} \le \tfrac12 \Longrightarrow \text{奇矩向量}\ (F_1, F_3, F_5, F_7)\ \text{距}\ \mathcal Z\ \text{足够近}}✓✓$$
$$\text{等价定量形式}✓✓：\text{在偶频约束}\ E\ \text{内证明}\ \boxed{\|(F_1, F_3, F_5, F_7)\| \ge \delta > 0}✓✓$$
$$\textbf{与既有资产的关系}✓✓：\text{C-341／C-342 的偶频归约}（x_j = c_j^2✓，F_{2r} = \sum_j P_r(x_j)✓）\ \text{提供}\ E\ \text{的显式描述}✓✓；\ \mathcal Z\ \text{由四奇矩零点定义}✓$$
$$\textbf{Stage 2 的困难}✓✓：\text{奇矩范数下界}\ \textbf{不} \text{自动给}\ \max_{k \le 25} F_k\ \text{的下界}✗✓ \ —— \ \text{须}\ \textbf{桥} \text{奇矩距离} \to \text{全频最大}✓✓$$

## §2 Stage 1 前提清单（✓✓）

$$\textbf{(i) 紧性}✓✓：E\ \text{是否闭且有界}?✓ \ —— \ \text{C-342}\ E = \{x \in [0,1]^5 : F_{2r}(x) \le \tfrac12\}✓ \Longrightarrow \text{闭（连续不等式}✓）＋ 有界（[0,1]^5✓） \Longrightarrow \textbf{紧}✓✓$$
$$\textbf{(ii) 距离／范数定义}✓✓：\text{须}\ \textbf{显式} \text{选定}✓（\text{如}\ \|(F_1,F_3,F_5,F_7)\|_2✓）\ —— \ \text{不同范数给不同}\ \delta✓，\textbf{不得}含混✗✓$$
$$\textbf{(iii) }\mathcal Z\ \text{的闭性}✓✓：\mathcal Z\ \text{由连续等式定义}✓ \Longrightarrow \textbf{闭}✓✓；\ \text{且}\ \mathcal Z \cap E = \varnothing✓ \Longrightarrow \operatorname{dist}(E, \mathcal Z) > 0✓✓（\text{紧} \cap \text{闭}\text{分离}✓）$$
$$\textbf{注}✓✓：\operatorname{dist}(E, \mathcal Z) > 0\ \text{是}\ \textbf{存在性}✓ \ —— \ \textbf{不}给\ \delta\ \text{的数值}✗✓（\text{与 C-281 的存在性闭合同型}✓）$$

## §3 路线（✓✓，三选一，登记不执行 ✓）

$$\textbf{路线 A 紧性分离}✓：\text{沿 C-281／C-282 的经验}✓ \ —— \ \text{紧性} \to \text{连续性} \to \text{正下界}✓；\ \text{但}\ \text{Stage 2}\ \text{须}\ \textbf{额外} \text{结构}✓✓$$
$$\textbf{路线 B Jacobian／局部逆映射}✓：\text{用四奇矩映射的}\ \textbf{局部单射性} \text{把距离下界转成偶频代价}✓✓；\ \text{注意}\ \det \ne 0\ \text{只给局部}✓（C-366✓）$$
$$\textbf{路线 C 直接构造定量不等式}✓✓：\text{找}\ \Delta - \Gamma\ \text{型显式不等式}✓（\text{与 C-282 阈值桥同型}✓） \ —— \ \textbf{最硬}✓$$
$$\textbf{纪律}✓✓：\textbf{先} \text{把 Bridge A 写成可证命题}✓✓，\ \textbf{再} \text{决定路线}✗✓；\ \textbf{不}立即大规模数值搜索✗✓$$

## §4 账本（✓✓）

| 对象 ✓ | 状态 ✓ |
|---|---|
| `\mathcal D_{\partial}` ✓ | **✓ 解析** ✓✓ |
| triple collision ✓ | **✓ 解析** ✓✓ |
| double collision ✓ | **✓ 解析** ✓✓ |
| `\mathcal D_{\mathrm{reg}}` ✓ | **✓ C-371 解析判空** ✓✓ |
| `\mathcal Z \cap E` ✓ | **✓ 完整闭合** ✓✓ |
| **Bridge A** ✓ | **OPEN ← 唯一下一主线** ✓✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

$$\textbf{禁项}✓✓：\textbf{不再}挖 exact-cancellation✗✓（\text{C-371 已彻底封口}✓✓）；\ \textbf{不}跳步✗；\textbf{不}写\ H = \varnothing✗✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 桥A形式化    命中文件数=0    :: 
技术词 紧性分离两阶段 命中文件数=0    :: 
技术词 独立健全性检查 命中文件数=0    :: 
```
- **零计算** ✗（形式化登记 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`H = \varnothing` 已证 ✗；`\operatorname{dist}(E, \mathcal Z) > 0` 已算出数值 ✗；`E` 的紧性已核闭 ✗（**待核** ⚠️✓）
