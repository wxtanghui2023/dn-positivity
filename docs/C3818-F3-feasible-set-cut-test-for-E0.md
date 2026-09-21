已查地图（**先查后写**）：`C-380-17`（**`F_3` ＝ algebraic asset** ✓✓）、`C-380-16`（**三把刀** ✓✓）、`C-380-13`（**sharp 封口** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-18：`F_3` 对 `E_0` 的 feasible-set cut test（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（九条 ✓✓）

$$\textbf{① 勘误固定（本档第一句）}✓✓：\ \boxed{6e_4\overline{p_1} = 2p_3 + p_1^3 - 3p_1p_2}✓✓ \Longrightarrow \ \boxed{F_3 = |2p_3 + p_1^3 - 3p_1p_2|^2 - 36|p_1|^2 = 0}✓✓$$
$$\qquad \Longrightarrow \ \textbf{错误符号版必须彻底从后续资产中剔除}✗✓$$
$$\textbf{② } C\text{-}380\text{-}18\ \text{定义}✓✓：\boxed{C\text{-}380\text{-}18 = F_3\ \text{对}\ E_0\ \text{的 feasible-set cut test}}✓✓$$
$$\qquad \textbf{核心问题只有一个}✓✓：\ \boxed{\mathcal F(E_0) \stackrel{?}{\supsetneq} \mathcal F(E_0) \cap \{F_3 = 0\}}✓✓$$
$$\qquad \text{更准确}✓✓：\textbf{比较} \text{不使用}\ F_3\ \text{与}\ \textbf{强制使用}\ F_3\ \text{时}\ E_0\ \text{目标量的}\ \textbf{可达范围}✓✓$$
$$\textbf{③ 第一层：确认不是「恒等式但无方向性」}✓✓：\mathcal M_4 = \{(p_1, p_2, p_3, p_4) : \text{四个单位圆节点}\}✓；\ \text{目标函数记}\ T(p)✓✓$$
$$\qquad \textbf{需要比较}✓✓：\ \sup_{\mathcal M_4}T\ \quad \text{vs.} \quad \sup_{\mathcal M_4 \cap \mathcal C_{E_0}}T✓✓$$
$$\qquad \textbf{若加入}\ F_3 = 0\ \text{后 supremum}\ \textbf{完全不变}✗✓ \Longrightarrow \ \boxed{F_3 = \text{algebraic asset only}}✓✓ \ —— \ \text{即使非常漂亮、非常非线性，}\ \textbf{也不能升格}✗✓$$
$$\textbf{④ ⭐ 第二层：最强「去掉单位圆」对照（Ablation 表）}✓✓：\text{结构拆成}\ \text{Newton} + \boxed{e_3 = e_4\overline{p_1}}✓ + \boxed{|e_4| = 1}✓✓$$
$$\qquad \begin{array}{c|c} \textbf{约束}✓ & \textbf{对}\ E_0\ \textbf{可行域的影响}✓ \\ \hline \text{Newton only}✓ & ?✓ \\ \text{Newton} + \text{self-inversive}✓ & ?✓ \\ \text{Newton} + \text{self-inversive} + |e_4| = 1✓ & ?✓ \end{array}$$
$$\qquad \Longrightarrow \ \textbf{若只有最后一步} \text{真正切掉}\ E_0\ \text{的极值区域}✓ \Longrightarrow \text{obstruction 的来源}\ \textbf{非常明确}✓✓$$
$$\textbf{⑤ ⭐⭐ 第三层：不做单纯数值采样，而做「接触点」审计}✓✓：\text{若数值显示}\ T_{\max}^{\mathrm{free}} > T_{\max}^{F_3}✓ \ \textbf{还不能立即宣布成功}✗✓$$
$$\qquad \textbf{必须找到接触结构}✓✓：F_3 = 0✓，\ T = T_{\max}✓，\ \textbf{并检查是否存在}\ \textbf{严格正的 gap}✓✓：\ \boxed{T \le C - \delta,\quad \delta > 0}✓✓$$
$$\qquad \textbf{否则} \text{可能只是有限采样没有找到原来的极值点}✗✓$$
$$\qquad \textbf{推荐顺序}✓✓：\text{① 找}\ E_0\ \text{原始极值候选}✓；\text{② 检查该候选是否}\ \textbf{自动满足}\ F_3 = 0✓；\text{③ 若自动满足} \Longrightarrow F_3\ \text{对该极值}\ \textbf{没有切削作用}✓✓；$$
$$\qquad \qquad \text{④ 若不满足}✓ \Longrightarrow \text{才继续求加入}\ F_3 = 0\ \text{后的}\ \textbf{新极值}✓；\text{⑤ 最后要求}\ \textbf{可审计的严格 gap}✓✓（\textbf{而非}「随机采样看起来下降」✗✓）$$
$$\textbf{⑥ ⭐ 特别值得检查的现象}✓✓：F_3\ \text{本质上来自}\ |e_4| = 1✓ \Longrightarrow \text{很可能只是把一个}\ \textbf{隐藏的相位自由度}\ \text{消掉}✓，\ \textbf{而不一定} \text{限制}\ E_0\ \text{所看的}\ \textbf{实部方向}✓✓$$
$$\qquad \text{若}\ E_0\ \text{只依赖某个}\ \textbf{低维投影}✓，\ \text{而}\ F_3 = 0\ \text{所消掉的方向恰位于该投影的}\ \textbf{纤维内部}✓ \Longrightarrow F_3 = 0\ \text{对}\ E_0\ \text{的投影}\ \textbf{可能完全无效}✗✓$$
$$\qquad \Longrightarrow \ \textbf{这正是 E 条款必须做的事情}✓✓$$
$$\textbf{⑦ } F_4\ \textbf{暂时封存}✓✓：\text{因目前}\ F_3 \in \text{Algebraic Assets}✓ \ \textbf{而不是}\ F_3 \in \text{Obstructions}✗✓$$
$$\qquad \textbf{在未完成 E 之前} \text{继续从}\ p_4, p_5, p_6\ \text{生成更多}\ F_k✗ \Longrightarrow \textbf{很容易再次进入「越来越多漂亮恒等式，但没有切到目标」的循环}✗✓$$
$$\textbf{⑧ ⭐ 三种判定}✓✓：\textbf{A. 严格切削}✓✓：\ \sup T|_{F_3=0} < \sup T✓ \Longrightarrow F_3\ \textbf{升为 candidate obstruction}✓✓$$
$$\qquad \textbf{B. 极值自动落在}\ F_3 = 0✓✓：T_{\max}\ \text{的所有接触点均满足}\ F_3 = 0✓ \Longrightarrow F_3\ \text{对}\ E_0\ \textbf{zero leverage}✓✓$$
$$\qquad \textbf{C. 投影后等价}✓✓：\text{加入}\ F_3\ \text{后}\ E_0\ \text{的}\ \textbf{可行投影不变}✓ \Longrightarrow \ \boxed{\textbf{GAP：self-inversive quartic algebra alone does not obstruct}\ E_0}✓✓$$
$$\textbf{⑨ ⭐ 负结果纪律}✓✓：\textbf{建议把 B／C 当作成功的负结果对待}✓✓ \ —— \ \text{它们}\ \textbf{能一次性告诉我们} \text{「继续挖低阶 self-inversive identity」是否值得}✓✓$$
$$\qquad \textbf{而不是} \text{再靠直觉开下一刀}✗✓$$

## §1 与既有封口的关系（✓✓）

$$\textbf{已封口}✓✓：C\text{-}380\text{-}12\（\text{等权求和}✓）、C\text{-}380\text{-}13\（\text{单一正三角对偶，sharp}\ 6✓✓）$$
$$\textbf{本档界限}✓✓：\text{任何化归为}\ \sum a_k\Re p_k \le C\ \text{的对象}\ \Longrightarrow \textbf{归回}\ C\text{-}380\text{-}13✗✓$$
$$\qquad F_3\ \textbf{不属} \text{该类型}✓（\text{含模平方}\✓） \Longrightarrow \text{但}\ \textbf{仍须} \text{过 E 条款}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}13` ✓ | **CLOSED（sharp）** ✓✓ |
| `C\text{-}380\text{-}17` ✓ | **`F_3` = algebraic asset** ✓✓ |
| **`C\text{-}380\text{-}18`** ✓ | **NEXT ← 本档注册（E 条款）** ✓✓ |
| `F_4` ✓ | **封存（E 未完成前不开）** ✗✓ |
| `E_0` ✓ | **OPEN** ✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：F_3\ \text{已是 obstruction}✗✓；\ \text{可行域已缩小}✗；\ E_0 = \varnothing\ \text{已证}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ E\ \textbf{未执行}✗✓；\ \text{三层测试}\ \textbf{均为方案}✓✓$$

## §4 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §5 边界（✓✓）

$$\textbf{纪律}✓✓：\delta > 0\ \textbf{必须可审计}✓✓；\ \text{不得以采样下降代替严格 gap}✗✓；\ \textbf{B／C 记为成功负结果}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 可行域切削  命中文件数=0    :: 
技术词 接触点审计  命中文件数=0    :: 
技术词 零杠杆判定  命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
