已查地图（**先查后写**）：`C-380-12`（**四点单位圆幂和** ✓✓）、`C-380-11`（**`E_0` 优先** ✓✓）、`C-281`（**存在≠定量强度** ⚠️✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-13：`E_0` 的正三角多项式对偶证书审计（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 对偶框架}✓✓：\text{当前问题}\ \Re p_k \le -\tfrac12✓，\ p_k = \sum_{j=1}^{4}z_j^k✓，\ |z_j| = 1✓，\ k = 1..6✓ \iff \sum_{j=1}^{4}\cos(k\theta_j) \le -\tfrac12✓✓$$
$$\qquad \text{任何}\ \textbf{非负权重}\ a_k \ge 0✓ \Longrightarrow \sum_{k=1}^{6}a_k\Re p_k \le -\tfrac12\sum_{k=1}^{6}a_k✓✓$$
$$\qquad \textbf{若能构造}\ \text{无常数项的三角多项式}\ Q(\theta) = \sum_{k=1}^{6}a_k\cos(k\theta)✓（a_k \ge 0✓）\ \text{满足}\ Q(\theta) \ge -c\ \forall\theta✓ \ \textbf{且}\ \boxed{4c < \tfrac12\sum_{k=1}^{6}a_k}✓✓$$
$$\qquad \Longrightarrow \ \text{直接矛盾}✓✓：\sum_jQ(\theta_j) \ge -4c > -\tfrac12\sum a_k \ge \sum_k a_k\Re p_k = \sum_jQ(\theta_j)✓✓$$
$$\textbf{② 归一化形式（C-380-13 第一问题）}✓✓：\ \boxed{\inf_{a_k \ge 0,\ \sum a_k = 1}\Big[-\min_\theta\sum_{k=1}^{6}a_k\cos(k\theta)\Big] < \tfrac18\ ?}✓✓$$
$$\qquad \textbf{若能构造}\ \text{显式有理／代数系数}\ a_k✓ \ \textbf{并精确证明}\ \min_\theta Q(\theta) > -\tfrac18✓ \Longrightarrow \boxed{E_0\ \textbf{立即关闭}}✓✓$$
$$\qquad \textbf{若该对偶条件不存在}✓✓ \Longrightarrow \text{说明}\ \text{「单一公共三角多项式 ＋ 正权组合」这一}\ \textbf{证书类型本身不足}✓✓ \Longrightarrow \textbf{停止调权}✗✓$$
$$\textbf{③ ⭐ 更强版本（允许常数项）}✓✓：P(\theta) = c_0 + \sum_{k=1}^{6}a_k\cos(k\theta) \ge 0✓ \Longrightarrow \sum_jP(\theta_j) = 4c_0 + \sum_{k=1}^{6}a_k\Re p_k \le 4c_0 - \tfrac12\sum a_k✓✓$$
$$\qquad \textbf{若}\ P \ge 0\ \textbf{且}\ \boxed{4c_0 < \tfrac12\sum_{k=1}^{6}a_k}✓✓ \Longrightarrow \text{矛盾}✓✓ \iff \boxed{\sum_{k=1}^{6}a_k > 8c_0}✓✓$$
$$\qquad \Longrightarrow \ \text{归约为}\ \boxed{\text{寻找一个}\ \deg \le 6\ \text{的}\ \textbf{非负三角多项式}✓，\ \text{其正频率质量足够大}}✓✓$$
$$\textbf{④ ⚠️ 陷阱锁死（采纳）}✗✓：\textbf{不能}因为找到\ P(\theta) \ge 0\ \textbf{就自动认为它能产生矛盾}✗✓$$
$$\qquad \textbf{必须}同时检查严格的\ \textbf{质量比}\ \boxed{\sum a_k > 8c_0}✓✓，\ \textbf{否则}只是一个非负三角多项式恒等式，\ \textbf{没有排除能力}✗✓$$
$$\qquad \textbf{这与}\ C\text{-}281\ \text{／uniform-margin 陷阱是}\ \textbf{同一种证明纪律}✓✓：\boxed{\text{存在一个结构对象}\ \ne\ \text{该对象具有所需定量强度}}✓✓$$
$$\textbf{⑤ 若判死（对偶类型不足）}✓✓：\text{若证明所有}\ \deg \le 6\ \text{的这种正三角多项式都满足}\ \sum a_k \le 8c_0✓ \Longrightarrow \textbf{不要}继续优化\ a_k✗✓$$
$$\qquad \Longrightarrow \text{记录}\ \boxed{E_0\ \textbf{不能由单一正三角对偶证书关闭}}✓✓ \Longrightarrow \text{进入下一层更强结构}✓✓$$
$$\qquad \Longrightarrow \ p_1, \dots, p_4\ \text{Newton} + |z_j| = 1 + p_5, p_6✓✓ \ —— \ \textbf{尤其}\ p_5, p_6\ \text{由四个节点的 elementary symmetric coefficients 决定}✓✓$$
$$\qquad \qquad \Longrightarrow \textbf{这时才真正使用「四节点而非六个独立变量」的信息}✓✓$$
$$\textbf{⑥ 严格顺序}✓✓：\ \boxed{\text{显式}\ P(\theta) \ge 0 \to \text{检查}\ \sum a_k > 8c_0 \to \begin{cases} E_0 = \varnothing✓ \\ \text{该对偶类型判死}✓ \end{cases}}✓✓$$
$$\textbf{⑦ 纪律}✓✓：\textbf{不}做随机角度搜索✗；\textbf{不}做数值优化✗；\textbf{不}碰\ E_{\mathrm{coll}}✗；\textbf{不}碰\ D✗；\textbf{不}碰\ F_{11} - F_{25}✗✓$$

## §1 与前档的关系（✓✓）

$$\textbf{C-380-12}\ \text{已排除}\ ✓✓：\text{简单}\ \textbf{等权求和}✗✓（\text{六项余弦和下界}\ > -2✓，\ \text{四点}\ > -8\ \text{不足以对}\ -3✓）$$
$$\qquad \Longrightarrow \ C\text{-}380\text{-}13\ \textbf{不是} \text{「再试一个求和权重」}✗✓，\ \text{而是}\ \textbf{对偶证书}✓✓（\text{允许非等权 ＋ 常数项}✓）$$
$$\textbf{判据}✓✓：\text{对偶不成立}\ \Longrightarrow \ \text{「正三角多项式}\ \textbf{这一类型}」判死✓✓，\ \textbf{不是}\ \text{「}E_0\ \text{不可关闭」}✗✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}12` ✓ | **CLOSED（求和法判不足）** ✓✓ |
| **`C\text{-}380\text{-}13`** ✓ | **NEXT ← 本档注册** ✓✓ |
| `E_0` ✓ | **OPEN ↔ 本档首次获\ \textbf{对偶判据}✓✓** |
| `E_{\mathrm{coll}}` ✓ | **OPEN（暂不碰）** ✗✓ |
| `\inf D` ✓ | **DEFERRED** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：E_0 = \varnothing\ \text{已证}✗；\ \text{对偶证书已构造}✗；\ \text{对偶类型已判死}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \inf\ \text{判据}\ \textbf{未判定}✗✓；\ \text{质量比门槛为}\ \textbf{必要} \text{非充分}✓✓$$

## §4 术语纪律（✓✓）

$$\textbf{「对偶类型判死」}✓✓ \ne \text{「}E_0\ \text{不可证」}✗✓ \ —— \ \text{前者限于}\ \textbf{单一正三角多项式} \text{类型}✓✓$$
$$\textbf{与}\ C\text{-}379\text{「坐标重包装」}\ \text{同型纪律}✓✓：\text{判死}\ \text{必须}\ \textbf{限定类型}✓✓$$

## §5 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 正三角对偶证书 命中文件数=0    :: 
技术词 质量比门槛  命中文件数=0    :: 
技术词 对偶类型判死 命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
