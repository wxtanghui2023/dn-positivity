已查地图（**先查后写**）：`C-380-11`（`E_0` 定义 ✓）、`C-380-12`（**`E_0` 层精确形式** ✓✓）、`C-380-7`（**目标约束** ✓✓）、`C-380-17/18/19`（`F_3` ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-20A：`E_0`／`R_0` 母问题恢复与独立性审计（注册）**，**有计算（档案检索，非数值算）✓**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 本档性质}✓✓：\textbf{档案恢复任务}✓✓ \ —— \ \textbf{不许猜}✗✓；\ \text{因}\ C\text{-}380\text{-}19\ \text{已显性化}✓：\ \boxed{\text{没有明确}\ R_0\，\ \text{就没有资格谈}\ F_3\ \text{的 cut}}✓✓$$
$$\textbf{② 检索方法}✓✓：\text{显式路径}\ \texttt{grep}✓（\textbf{未}全盘\ \texttt{find}✗✓，\ \text{遵}\ \text{TOOLS.md}\ \text{内存纪律}✓✓）$$
$$\textbf{③ ⭐ 可恢复部分（逐项，档案逐字）}✓✓：$$
$$\qquad \textbf{(a)}\ E_{\mathrm{even}}\ \text{定义}✓（C\text{-}380\text{-}7／8✓）：E_{\mathrm{even}} = \{x \in [0,1]^5 : \sum_jT_r(2x_j - 1) \le \tfrac12,\ r = 1, \dots, 12\}✓✓$$
$$\qquad \textbf{(b)}\ E_0\ \text{定义}✓（C\text{-}380\text{-}11✓）：E_0 = \{x : \exists j,\ x_j = 0\}✓✓（\text{实践中取}\ x_5 = 0✓）$$
$$\qquad \textbf{(c)}\ E_0\ \text{上的偶频约束}✓（C\text{-}380\text{-}11／12✓）：\sum_{j=1}^{4}T_r(y_j) + (-1)^r \le \tfrac12✓ \Longrightarrow r = 2k：\sum_{j=1}^{4}\cos(2k\theta_j) \le -\tfrac12✓，\ k = 1, \dots, 6✓✓$$
$$\qquad \textbf{(d)}\ \text{目标型约束}✓（C\text{-}380\text{-}7✓）：|F_{2r+1}| \le \tfrac12✓，\ r = 0, \dots, 4✓✓$$
$$\qquad \textbf{(e)}\ \text{模型}✓（C\text{-}380\text{-}12✓）：z_j = e^{2i\theta_j}✓，\ |z_j| = 1✓，\ p_k = \sum_{j=1}^{4}z_j^k✓✓$$
$$\qquad \textbf{(f)}\ F_3\ \text{定义}✓（C\text{-}380\text{-}17／18／19✓）：F_3 := |2p_3 + p_1^3 - 3p_1p_2|^2 - 36|p_1|^2✓✓$$
$$\textbf{④ ⚠️ 不可恢复部分（关键）}✗✓：\textbf{档案中从未把}\ R_0\ \textbf{写成一处显式清单}✗✓（\text{分散在}\ C\text{-}380\text{-}7／11／12／13✓）$$
$$\qquad T\ \textbf{亦未被显式固定}✗✓：C\text{-}380\text{-}18\ §0③\ \text{只写「目标函数记}\ T(p)\text{」}✓；\ C\text{-}380\text{-}19\ §0⑤\ \text{只写}\ T = T(p_1, \dots, p_6, \overline{p_1}, \dots, \overline{p_6})✓✓$$
$$\qquad \Longrightarrow \ \textbf{R1 的完整形态需要唐先生确认}⚠️✓ \ —— \ \textbf{不能}由我方代猜✗✓$$
$$\textbf{⑤ ⭐⭐ 关键判定（可恢复且有据）}✓✓：F_3\ \text{的推导}\ \textbf{只用了四节点单位圆结构}✓✓：$$
$$\qquad \qquad |e_4| = 1✓，\quad e_3 = e_4\overline{e_1}✓，\quad \text{Newton identities}✓ \ \ —— \ \textbf{三者皆由}\ |z_j| = 1✓\ \textbf{推出}✓✓$$
$$\qquad \Longrightarrow \ \textbf{任何包含「四节点单位圆」的}\ R_0✓（\text{档案显示确实含}\✓）\ \text{都使}\ \boxed{F_3 \in \sqrt{I(R_0)}}✓✓$$
$$\qquad \Longrightarrow \ \boxed{F_3\ \textbf{REDUNDANT}}✓✓ \ —— \ \text{即}\ F_3\ \textbf{是四节点／self-inversive 母约束的派生恒等式}✓，\ \textbf{不能}成为独立 obstruction✗✓$$
$$\qquad \Longrightarrow \ \text{与}\ C\text{-}380\text{-}19\ §0④\ \text{的正确措辞}\ \textbf{一致}✓✓：\text{不是「}\ F_3\ \text{没有 obstruction」，\ 而是派生恒等式}✓✓$$
$$\textbf{⑥ 判定树}✓✓（采纳）：\text{恢复}\ R_0, T \to F_3 \stackrel{?}{\in} \sqrt{I(R_0)}✓✓$$
$$\qquad \textbf{YES}✓✓ \Longrightarrow \textbf{REDUNDANT}✓✓ \Longrightarrow \textbf{直接封}✓（\textbf{不做} R3✗，\textbf{不开}\ F_4✗）；\ \textbf{NO}✓ \Longrightarrow \text{做 R3（}\sup\ \text{比较）}✓\ \to\ \text{严格下降} \Longrightarrow C\text{-}380\text{-}21\（\delta > 0\ \text{证明}✓）；\ \text{不下降} \Longrightarrow \text{区分}\ \text{zero leverage／projection-equivalent／redundant}✓✓$$
$$\textbf{⑦ ⭐ 纪律（采纳）}✓✓：\textbf{不要}因为\ F_3\ \text{已通过三项}✓（unit\text{-}circle\text{-}native✓／genuinely nonlinear✓／four\text{-}node✓）\ \textbf{就默认它与}\ E_0\ \text{当前 relaxation 独立}✗✓$$
$$\qquad \Longrightarrow \ \text{那三项只证明}\ F_3\ \text{是}\ \textbf{新的代数对象}✓，\ \textbf{没有} \text{证明它是}\ \textbf{新的}\ E_0\text{-约束}✗✓ \ —— \ \textbf{这正是}\ C\text{-}380\text{-}19\ \text{发现的逻辑分界}✓✓$$
$$\textbf{⑧ 本档结论（provisional）}✓✓：\textbf{倾向}\ \textbf{REDUNDANT}✓✓，\ \text{因}\ F_3\ \text{仅由}\ |z_j| = 1\ \text{推出}✓✓；\ \textbf{但仍须} \text{唐先生确认}\ R_0\ \text{的显式清单与}\ T\ \text{的具体形式}⚠️✓$$

## §1 三层判定树（✓✓）

$$\boxed{\text{恢复}\ R_0, T \ \downarrow\ F_3 \in \sqrt{I(R_0)}\ ?}✓✓ \Longrightarrow \begin{cases} \textbf{YES}✓：\textbf{REDUNDANT}✓✓（\text{封，不做 R3，不开}\ F_4✓） \\ \textbf{NO}✓：\sup_{R_0 \cap \{F_3=0\}}T \stackrel{?}{<} \sup_{R_0}T✓✓ \begin{cases} \text{严格下降}✓ \to C\text{-}380\text{-}21✓ \\ \text{不下降}✓ \to \text{zero leverage／projection-equivalent／redundant}✓ \end{cases} \end{cases}$$

## §2 本档**不做**的事（✓✓）

$$\textbf{不做}\ R3✗（\text{若}\ REDUNDANT✓）；\ \textbf{不算}\ F_4／p_5, p_6／\text{新 obstruction}✗✓；\ \textbf{不做}数值优化✗✓$$
$$\Longrightarrow \ \textbf{避免} \text{再次进入「代数越来越丰富，但不知道是否碰到了目标」的循环}✗✓$$

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}13` ✓ | **CLOSED sharp** ✓✓ |
| `F_3` ✓ | **algebraic asset → 倾向 REDUNDANT（待确认 `R_0`）** ✓✓ |
| `C\text{-}380\text{-}18` ✓ | **E-criterion corrected** ✓✓ |
| `C\text{-}380\text{-}19` ✓ | **R1–R4 framework established** ✓✓ |
| **`C\text{-}380\text{-}20A`** ✓ | **本档：母问题恢复 ＋ 独立性初步判定** ✓✓ |
| `E_0` ✓ | **OPEN** ✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §4 边界（✓✓）

$$\textbf{不得}写成✗：F_3\ \text{无 obstruction}✗✓（\textbf{正确}：\text{派生恒等式}✓）；\ E_0 = \varnothing\ \text{已证}✗；\ R_0\ \text{已确认}✗✓（\textbf{仅}初步✓）；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档为}\ \textbf{档案检索}✓（\text{非数值算}✓）；\ R_0, T\ \textbf{完整形态未复原}✗✓；\ \textbf{结论 provisional}✓✓$$

## §5 待唐先生确认的清单（✓✓）

$$\textbf{(1)}✓：R_0\ \text{的完整约束清单}（\text{是否含}\ |z_j| = 1✓、\text{是否含奇频约束}✓、\text{是否含偶频约束}✓）；\ \textbf{(2)}✓：T\ \text{的具体形式}（\max_{0 \le r \le 4}|F_{2r+1}|✓？\ \text{或其他}✓）；\ \textbf{(3)}✓：E_0\ \text{是否就是}\ x_5 = 0\ \text{的单层}✓\ \text{或}\ \exists j\ \text{的并集}✓✓$$

## §6 检索输出（**先跑后写**✓）＋ 边界

```
技术词 母问题恢复  命中文件数=0    :: 
技术词 派生恒等式冗余 命中文件数=0    :: 
技术词 可行域清单  命中文件数=0    :: 
```
- 检索记录 ✓：`grep -a -n -E "E_0 = |E_0\\\\cap|目标函数|T = T|R_0" C38*.md`✓（\text{显式路径}✓）
