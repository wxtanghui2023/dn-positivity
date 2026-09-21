已查地图（**先查后写**）：`C-380-20B／20C`（**三缺口** ✓✓）、`C-380-7`（**全局形式** ✓✓）、`C-380-12`（**`E_0` 原命题** ✓✓）、`C-3815`（**坐标 A** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-21A：`E_0` 原问题语义重建（A1／A2／A3）**，**有计算（档案检索，非数值算）✓**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① A1 原始坐标（已恢复）}✓✓：\text{链}\ x_j \to y_j = 2x_j - 1 \to \theta_j \to z_j✓✓$$
$$\qquad \textbf{`E_0` 判定实际用的坐标}✓✓：\ \boxed{z_j = e^{2i\theta_j}}✓✓（C\text{-}380\text{-}12\ §0③✓，\ \textbf{显式「令」}✓） \ —— \ \text{因偶频约束}\ T_{2k}(y_j) = \cos(2k\theta_j)✓✓$$
$$\qquad \textbf{而}\ C\text{-}3815／16／17\ \text{用的坐标}✓：\boxed{z_j = e^{i\theta_j}}✓✓（C\text{-}3815\ §0②✓）$$
$$\qquad \Longrightarrow \ \textbf{记号冲突确认}✗✓：\ \text{`E_0` 侧坐标是}\ \textbf{B}（e^{2i\theta_j}）✓✓，\ \text{后续代数用的是}\ \textbf{A}（e^{i\theta_j}）✗✓$$
$$\qquad \Longrightarrow \ \textbf{结论}✓✓：C\text{-}3815 \sim 17\ \text{的}\ F_3\ \text{是在}\ \textbf{坐标 A} \text{中算的}✗✓，\ \textbf{并非}\ E_0\ \text{的坐标 B}✓✓$$
$$\qquad \Longrightarrow \ \textbf{统一规定}✓✓：\text{以后}\ p_k := \sum_jz_j^k\ \textbf{只允许} \text{在统一坐标下使用}✓✓；\ \text{旧档另一套必须标}\ p_k^{(A)}✓，\ p_k^{(B)}✓✓，\ \textbf{不得}裸写\ p_k✗✓$$
$$\textbf{② ⭐ A2 原命题（本档重要发现）}✓✓：\text{档案}\ \textbf{两种形式都存在}✓✓：$$
$$\qquad \textbf{(i) feasibility}✓（C\text{-}380\text{-}12\ §0④✓）：\{z_1, \dots, z_4 \in S^1 : \Re\sum_jz_j^k \le -\tfrac12,\ k = 1, \dots, 6\} = \varnothing\ ?✓✓$$
$$\qquad \textbf{(ii) 全局／优化形式}✓（C\text{-}380\text{-}7\ §0③✓，\ C\text{-}380\text{-}3\ §0⑧✓）：\inf_{x \in E_{\mathrm{even}}}\min_\sigma\max_{0 \le r \le 4}|F_{2r+1}| > \tfrac12✓✓$$
$$\qquad ⭐ \Longrightarrow \ \textbf{二者由}\ \textbf{量词基本等价} \text{相连}✓✓：\forall x \exists k \iff \neg\exists x \forall k✓✓ \Longrightarrow \ \textbf{不是两个独立问题}✓✓$$
$$\qquad \Longrightarrow \ \textbf{路径 III（桥）不需要}✓✓，\ \text{而}\ C\text{-}380\text{-}20C\ \text{的「目标类型错配」}\ \textbf{部分消解}✓✓$$
$$\qquad \textbf{唯一须核}⚠️：\text{档案}\ \textbf{是否显式写出} \text{该等价}✗（\text{检索只找到}\ \forall\text{-形式}✓） \ —— \ \textbf{但等价本身是一步}✓✓$$
$$\textbf{③ ⭐ A3 对称性（本档第二个发现）}✓✓：\text{档案}\ \textbf{未记录} \text{对称性论证}✗✓（C\text{-}380\text{-}20B\ 已注✓）；\ \textbf{但它}\ \textbf{可一步证明}✓✓：$$
$$\qquad \textbf{①} E_{\mathrm{even}} = \{x : \sum_jT_r(2x_j - 1) \le \tfrac12\}✓ \ \textbf{对}\ S_5\ \textbf{对称}✓✓（\text{对}\ j\ \text{求和}✓）$$
$$\qquad \textbf{②} E_0 = \bigcup_{j=1}^{5}\{x_j = 0\}✓ \ \textbf{对}\ S_5\ \textbf{对称}✓✓；\ \text{且}\ S_5\ \text{在}\ \{E_j\}\ \text{上}\ \textbf{传递}✓✓ \Longrightarrow g(E_j) = E_5✓✓$$
$$\qquad \textbf{③} \text{目标}\ F_{2r+1} = \sum_j\sigma_j\sqrt{x_j}R_r(x_j)✓ \ \text{在置换}\ (\text{连同}\ \sigma\ \text{的同步置换}✓)\ \text{下不变}✓✓ \Longrightarrow \min_\sigma\ \textbf{不变}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\text{WLOG}\ \bigcup_{j=1}^{5}E_j \sim E_5\ \textbf{合法}}✓✓ \ —— \ \textbf{此处非「doc 级 WLOG」}✓✓，\ \text{而是}\ \textbf{可证对称性}✓✓$$
$$\textbf{④ 三问小结}✓✓：\textbf{A1} \text{有真冲突（须重标坐标）}✗✓；\ \textbf{A2} \text{两形式等价（\textbf{不是}两个问题）}✓✓；\ \textbf{A3} \text{对称性可证（WLOG 合法）}✓✓$$
$$\Longrightarrow \ C\text{-}380\text{-}20C\ \text{的「三缺口」中，}\textbf{两项消解}✓✓，\ \textbf{仅坐标一项留真问题}✗✓$$
$$\textbf{⑤ 对}\ F_3\ \text{的后果}✓✓：\text{因}\ F_3\ \text{是在}\ \textbf{坐标 A} \text{中推导}✗✓，\ \text{而}\ E_0\ \text{的约束在}\ \textbf{坐标 B}✓✓ \Longrightarrow \ F_3\ \textbf{必须先在 B 坐标重写}✗✓$$
$$\qquad \text{重写后形式}✓✓（\text{由}\ p_k^{(B)} = p_{2k}^{(A)}✓）：F_3^{(B)} = \big|2p_6^{(A)} + (p_2^{(A)})^3 - 3p_2^{(A)}p_4^{(A)}\big|^2 - 36|p_2^{(A)}|^2✓✓ \ —— \ \textbf{与}\ F_3^{(A)}\ \textbf{不同}✗✓$$
$$\qquad \Longrightarrow \ \textbf{须重新核验}：F_3^{(B)}\ \text{是否仍由}\ |z_j^{(B)}| = 1\ \text{推出}✓✓ \ —— \ \textbf{这一步未做}✗✓$$
$$\textbf{⑥ 判定顺序（不变）}✓✓：\text{coordinate normalization} \to \text{objective identification}✓（\textbf{本档已解}✓✓） \to \text{branch symmetry}✓（\textbf{本档已解}✓✓） \to F_3\ \text{redundancy test}✓✓$$
$$\textbf{⑦ 封存项不变}✓✓：F_4／p_5, p_6\ \textbf{SEALED}✗✓；\ \text{新 obstruction search}\ \textbf{SEALED}✗✓$$
$$\textbf{⑧ 路径}✓✓：\text{因 A2 等价}✓✓，\ \text{路径 I 与 III 合并}✓✓ \Longrightarrow \ \text{主问题即}\ \boxed{R_0 \cap E_0 \stackrel{?}{=} \varnothing}✓✓（\text{等价于}\ \inf > \tfrac12✓）$$

## §1 三问对照表（✓✓）

| 问 ✓ | 结论 ✓ | 状态 ✓ |
|---|---|---|
| **A1 坐标** ✓ | `E_0` 侧 = **B**（`e^{2i\theta_j}`）✓；`C-3815–17` = **A**（`e^{i\theta_j}`）✗ | **真冲突，须重标** ✗✓ |
| **A2 命题** ✓ | 两形式 **量词等价** ✓✓（`∀x∃k ⟺ ¬∃x∀k`）| **消解：同一问题** ✓✓ |
| **A3 对称** ✓ | `E_even`、`E_0`、`min_σ` 目标均 `S_5`-不变；`S_5` 在 `{E_j}` 上传递 ✓ | **消解：WLOG 合法** ✓✓ |

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}13` ✓ | **CLOSED sharp** ✓✓ |
| `F_3` ✓ | **valid nonlinear identity；semantic identity unresolved（坐标 A vs B）** ✗✓ |
| `C\text{-}380\text{-}19` ✓ | **framework retained，not executable** ✗✓ |
| `20A／20B／20C` ✓ | **CLOSED semantic recovery** ✓✓ |
| `R_0` ✓ | **UNRESOLVED** ✗✓ |
| `T` ✓ | **本档部分消解：与 feasibility 等价** ✓✓ |
| `E_0` branch symmetry ✓ | **本档解决：可证 WLOG** ✓✓ |
| `F_3` redundancy ✓ | **BLOCKED**（坐标未统一）✗✓ |
| `F_4, p_5, p_6` ✓ | **SEALED** ✗✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：F_3\ \text{REDUNDANT}✗✓；\ R_0\ \text{已确认}✗✓；\ E_0 = \varnothing\ \text{已证}✗；\ \text{Bridge A 已闭合}✗✓；\ \text{坐标冲突已解决}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档为}\ \textbf{档案检索}✓；\ \textbf{A2／A3 消解}✓✓（\text{A3 为一步证明}✓）；\ \textbf{A1 仍为真冲突}✗✓；\ F_3^{(B)}\ \textbf{未核验}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}重写\ F_3^{(B)}✗（\text{仅给出形式}✓）；\textbf{不}开新代数战线✗；\textbf{不}做\ R3✗；\textbf{不算}\ F_4／p_5, p_6✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（档案检索✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 检索输出（**先跑后写**✓）＋ 边界

```
技术词 原问题语义重建 命中文件数=0    :: 
技术词 量词等价     命中文件数=0    :: 
技术词 坐标归属     命中文件数=0    :: 
```
- 检索记录 ✓：`grep -a -n`（显式路径 ✓；模式含 z_j 的两套写法、varnothing、inf、forall、对称／置换／S_5 各关键词 ✓）
