已查地图（**先查后写**）：`C-380-20A`（**母问题恢复** ✓✓）、`C-380-19`（**点明 `R_0` 缺口** ✓✓）、`C-380-12`（**`z_j` 参数化** ✓✓）、`C-3815`（**`e_4` 结构** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-20B：`R_0`／`T` 精确语义恢复（注册）**，**有计算（档案检索，非数值算）✓**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① ⭐ 术语修正（采纳）}✓✓：\text{原写}\ F_3 \in \sqrt{I(R_0)}✓ \ \textbf{不妥}✗✓ \ —— \ \text{因}\ R_0\ \text{是}\ \textbf{带等式／不等式的半代数 feasible set}✓✓，\ \textbf{不是}单纯代数簇✗✓$$
$$\qquad \Longrightarrow \ \text{统一改为}\ \boxed{R_0 \models F_3 = 0}✓✓ \ \text{或}\ \boxed{\forall x \in R_0,\ F_3(x) = 0}✓✓$$
$$\qquad \text{若以后需要代数证明}✓，\ \text{再依具体等式约束讨论}\ \textbf{real radical／real algebraic ideal}✓✓ \ —— \ \textbf{不是结论改变，是逻辑载体要准确}✓✓$$
$$\textbf{② B1 检索结果}✓✓：\text{档案中}\ \textbf{从未}把\ R_0\ \text{写成显式清单}✗✓（\texttt{grep}\ \text{计数}：C\text{-}380\text{-}7／11／12／13\ \text{中}\ R_0\ \text{命中}\ = 0✓✓；\ \text{仅}\ C\text{-}380\text{-}19\ \text{提出该要求}✓）$$
$$\qquad \textbf{可确认者}✓：\text{参数化为}\ 「\textbf{令}\ z_j = e^{2i\theta_j}」✓（C\text{-}380\text{-}12\ §0③✓，\ \textbf{显式引入}✓）⟹ |z_j| = 1\ \text{由}\ y_j = \cos\theta_j✓\ \textbf{参数化内置}✓✓$$
$$\qquad \Longrightarrow \ |z_j| = 1\ \textbf{是}\ R_0\ \text{的}\ \textbf{派生后果}✓ \ \text{而}\ \textbf{从未}被列为显式约束✗✓$$
$$\textbf{③ ⚠️ 记号冲突（本档真实发现）}✗✓：C\text{-}380\text{-}12\ \text{用}\ z_j = e^{2i\theta_j}✓ \ \textbf{而}\ C\text{-}3815／16／17\ \text{用}\ z_j = e^{i\theta_j}✓✓ \ —— \ \textbf{同一符号两种定义}✗✗$$
$$\qquad \Longrightarrow \ \text{直接影响}\ p_k✓、\ e_1, \dots, e_4✓、\ F_3✓ \ \textbf{的数值语义}✗✓ \Longrightarrow \ \textbf{任何代数复用前必须解决}✗✓$$
$$\textbf{④ B2 检索结果}✗✓：T\ \textbf{未被显式固定}✗✓；\ \text{档案存在}\ \textbf{两种读法}✓✓：$$
$$\qquad \textbf{(i)}\ \text{全局目标}✓（C\text{-}380\text{-}7✓）：T = \min_{\sigma}\max_{0 \le r \le 4}|F_{2r+1}(x, \sigma)|✓ \ \text{或等价的逐点形式}✓✓$$
$$\qquad \textbf{(ii)}\ E_0\ \text{分支的}\ \textbf{可行性形式}✓（C\text{-}380\text{-}12／13✓）：\ E_0 \cap \{\Re\sum_jz_j^k \le -\tfrac12,\ k = 1..6\} = \varnothing\ ?✓✓$$
$$\qquad \Longrightarrow \ \textbf{读法 (ii) 中根本没有}\ \sup T✗✓ \Longrightarrow \ C\text{-}380\text{-}19\ \text{的 R3／R4（zero leverage）}\ \textbf{预设了读法 (i)}✓✓ \Longrightarrow \textbf{必须确认}⚠️✓$$
$$\textbf{⑤ ⭐ B3 检索结果（真实发现）}✓✓：C\text{-}380\text{-}11\ \text{写「\textbf{固定}}\ x_5 = 0\text{」}✓⟹ \textbf{分支选择}（doc 级 WLOG✓）；\ \text{而}\ \textbf{定义} \text{为}\ E_0 = \{x : \exists j,\ x_j = 0\}✓✓$$
$$\qquad \Longrightarrow \ \textbf{两者不等价}✗✓（\text{如唐先生所指出}✓）；\ \text{且档案}\ \textbf{从未论证} \text{该缩并}✗✓（\textbf{无}对称性论证记录✗✓）$$
$$\qquad \Longrightarrow \ \textbf{这是一个未闭合的缺口}✓✓：E_0^{\mathrm{union}} = \bigcup_{j=1}^{5}\{x_j = 0\}✓ \ \textbf{与}\ E_0^{(5)} = \{x_5 = 0\}✓ \ \textbf{不能默认等价}✗✓$$
$$\textbf{⑥ 需唐先生确认三项}✓✓：\ \boxed{R_0 = ?}✓；\ \boxed{T = ?}✓；\ \boxed{E_0\ \text{是}\ x_5 = 0\ \text{还是}\ \bigcup_j\{x_j = 0\}}✓✓$$
$$\qquad \textbf{第三条甚至影响}\ feasible\ set\ \text{的}\ \textbf{拓扑结构}✓✓（\text{union 是 5 片之交}／\text{单一分支是一片}✓）$$
$$\textbf{⑦ 本档不做}✗✓：\textbf{不}开新代数战线✗；\textbf{不}做\ R3✗；\textbf{不}算\ F_4／p_5, p_6✗✓；\textbf{不}自行补\ R_0✗✓$$
$$\textbf{⑧ 判定仍非常干净}✓✓：\ \boxed{R_0 \models F_3 = 0 \Rightarrow F_3\ \textbf{REDUNDANT}}✓✓；\ \textbf{仅当} R_0 \not\models F_3 = 0✓ \ \text{才允许进入}\ \sup_{R_0}T\ \text{vs}\ \sup_{R_0 \cap \{F_3=0\}}T✓✓$$

## §1 三层语义清单（✓✓，供唐先生填）

$$\textbf{B1（}\ R_0\ \text{逐条）}✓：\text{每条标记}\ \text{exact equality／inequality／derived constraint／parametrization／projection／numerical relaxation}✓✓$$
$$\qquad \textbf{尤其单独回答}✓✓：\boxed{|z_j| = 1\ \text{是否属于}\ R_0\ \text{的定义？}}✓✓（\text{而}\ \textbf{不是} \text{「它是否可以从此前模型推出」}✗✓）$$
$$\textbf{B2（}\ T\ \text{逐字）}✓：T = \max_{0 \le r \le 4}|F_{2r+1}|✓？\ T = \sum_{r=0}^{4}|F_{2r+1}|^2✓？\ \text{或某个单独}\ F_1, F_3, \dots\ \text{投影}✓？$$
$$\qquad \textbf{没有}\ T✓，\ \text{就没有合法的「zero leverage」}✗✓$$
$$\textbf{B3（}\ E_0\ \text{语义）}✓：\text{若实际只研究}\ x_5 = 0✓，\ \text{须记录这是}\ \textbf{symmetry reduction／branch selection}✓ \ \text{还是}\ \text{档案本来就把}\ x_5\ \text{固定为}\ 0✗✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}20A` ✓ | **通过（母问题恢复）** ✓✓ |
| **`C\text{-}380\text{-}20B`** ✓ | **本档：语义闭合 ＋ 两处真实发现** ✓✓ |
| `R_0` ✓ | **档案无清单；须唐先生确认** ✗✓ |
| `T` ✓ | **未固定；两种读法** ✗✓ |
| `E_0` 语义 ✓ | **分支缩并未论证** ✗✓ |
| 记号冲突 ✓ | **`e^{2i\theta_j}` vs `e^{i\theta_j}`** ✗✓ |
| `C\text{-}380\text{-}21` ✓ | **不在本档开启** ✗✓ |
| Bridge A ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：R_0\ \text{已确认}✗✓；\ T\ \text{已固定}✗✓；\ E_0\ \text{语义已闭合}✗✓；\ F_3\ \text{已判 REDUNDANT}✗✓（\textbf{仅}倾向✓）；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档为}\ \textbf{档案检索}✓；\ \textbf{两处发现}✓✓（\text{记号冲突／分支缩并}）；\ \text{三项待唐先生确认}⚠️✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{语义闭合只做三件}✓✓（\text{B1／B2／B3}✓）；\ \textbf{不开}新代数战线✗✓；\ \textbf{不}进入\ C\text{-}380\text{-}21✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（档案检索✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 检索输出（**先跑后写**✓）＋ 边界

```
技术词 语义闭合     命中文件数=0    :: 
技术词 记号冲突     命中文件数=0    :: 
技术词 分支缩并     命中文件数=0    :: 
```
- 检索记录 ✓：`grep -a -n -E "令 z_j|z_j = e\^|固定 x_5|x_5 = 0|max_\{0 \\\\le r \\\\le 4\}|Re\\\\sum"`＋`grep -c R_0`✓（\text{显式路径}✓）
