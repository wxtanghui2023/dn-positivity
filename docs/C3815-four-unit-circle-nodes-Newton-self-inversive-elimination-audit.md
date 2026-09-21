已查地图（**先查后写**）：`C-380-14`（**sharp 封口** ✓✓）、`C-380-13`（**正三角对偶 CLOSED** ✓✓）、`C-380-12`（**四点幂和** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-15：四单位圆节点的 Newton／self-inversive 消元审计（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① } C\text{-}380\text{-}14\ \text{落档}✓✓：\text{该刀已把}\ \text{上一刀从「合理判断」}\ \textbf{提升为}\ \text{sharp 的}\ \textbf{类型封口}✓✓$$
$$\textbf{② ⭐ 结构设定}✓✓：z_j = e^{i\theta_j}✓（j = 1..4✓）；p_k = \sum_{j=1}^{4}z_j^k✓；\ f(z) = \prod_{j=1}^{4}(z - z_j) = z^4 - e_1z^3 + e_2z^2 - e_3z + e_4✓✓$$
$$\qquad |z_j| = 1✓ \Longrightarrow \tfrac1{z_j} = \overline{z_j}✓ \Longrightarrow \text{倒数根仍来自同一组四节点}✓✓ \Longrightarrow \textbf{self-inversive 约束}✓✓：$$
$$\qquad \qquad \boxed{e_3 = e_4\overline{e_1}✓,\qquad e_2 = e_4\overline{e_2}✓,\qquad |e_4| = 1}✓✓$$
$$\qquad \Longrightarrow \ \textbf{自由参数可压缩为}\ \boxed{(e_1, e_2, e_4)}✓✓$$
$$\textbf{③ Newton identities}✓✓：p_1 = e_1✓；\ p_2 = e_1p_1 - 2e_2 = e_1^2 - 2e_2✓✓；\ p_3 = e_1p_2 - e_2p_1 + 3e_3✓；\ p_4 = e_1p_3 - e_2p_2 + e_3p_1 - 4e_4✓✓$$
$$\qquad k > 4✓：\ p_k = e_1p_{k-1} - e_2p_{k-2} + e_3p_{k-3} - e_4p_{k-4}✓✓$$
$$\textbf{④ ⭐ 关键结论（本档核心）}✓✓：\ \boxed{p_5 = e_1p_4 - e_2p_3 + e_3p_2 - e_4p_1}✓✓；\ \boxed{p_6 = e_1p_5 - e_2p_4 + e_3p_3 - e_4p_2}✓✓$$
$$\qquad \Longrightarrow \ \boxed{p_5, p_6\ \textbf{是前四阶 moment 与单位圆 self-inversive 约束共同决定的}✓，\ \textbf{不是}两个额外自由坐标}✓✓$$
$$\textbf{⑤ ⚠️ 陷阱锁死}✗✓：\textbf{不能}仅证明「存在这些代数关系」然后就宣布\ E_0\ \text{被关闭}✗✓$$
$$\qquad \Longrightarrow \ \textbf{保持}\ C\text{-}380\text{-}14\ \text{的纪律}✓✓：\ \boxed{\text{代数降维}\ \ne\ \text{所需排除不等式}}✓✓$$
$$\textbf{⑥ 最小目标}✓✓：\text{在}\ z_1, \dots, z_4 \in \mathbb{T}\ \text{下}✓，\ \text{把原来的}\ E_0\ \text{条件}\ \textbf{完全改写} \text{为}\ (e_1, e_2, e_4)\ \text{的}\ \textbf{实代数约束}✓✓$$
$$\qquad \text{然后检查该约束是否存在一个}\ \boxed{\textbf{新的、非正三角多项式型}\ \text{的 universal obstruction}}✓✓$$
$$\textbf{⑦ 尤其避免退回}✗✓：\ \sum a_k\Re p_k \le \text{constant}\ \text{这种}\ \textbf{已被}\ C\text{-}380\text{-}13\ \textbf{封死} \text{的线性正对偶}✗✓$$
$$\qquad \textbf{真正值得检查}✓✓：\textbf{四节点特有的非线性关系}✓：|e_4| = 1✓，e_3 = e_4\overline{e_1}✓，\ \text{以及由此产生的}\ p_k\ \text{与}\ \overline{p_\ell}\ \text{之间的}\ \textbf{耦合}✓✓$$
$$\textbf{⑧ 路线}✓✓：\ \boxed{\text{正 Fourier 对偶} \times \text{FAILED} \longrightarrow \text{四节点单位圆代数}}✓✓ \ \textbf{而不是} \text{「换坐标继续做同一个对偶问题」}✗✓$$

## §1 四条硬验收条件（✓✓，唐先生口径 ✓）

$$\textbf{① 先完整消元}✓✓：\textbf{明确写出}\ p_1, \dots, p_6\ \text{对}\ (e_1, e_2, e_4)\ \text{的表达}✓✓$$
$$\textbf{② 显式使用}\ |z_j| = 1✓✓：\textbf{不能}只使用 Newton recurrence✗✓ \ —— \ \textbf{必须} \text{显式进入}\ e_3 = e_4\overline{e_1}✓ \ \text{与}\ |e_4| = 1✓✓$$
$$\textbf{③ 反重包装}✓✓：\textbf{证明} \text{新的 obstruction}\ \textbf{确实不是}\ C\text{-}380\text{-}13\ \text{的重新包装}✓✓$$
$$\textbf{④ 归回条款}✓✓：\text{若最终}\ \textbf{只}得到\ \sum a_k\Re p_k \le C\ \text{或等价的}\ \textbf{正三角多项式}✗✓ \Longrightarrow \textbf{立即归回}\ C\text{-}380\text{-}13\ \textbf{CLOSED}✓✓，\ \textbf{不得}重新包装✗✓$$

## §2 与既有封口的关系（✓✓）

$$\textbf{已封口}✓✓：C\text{-}380\text{-}12\（\text{等权求和}✓）、C\text{-}380\text{-}13\（\text{单一正三角对偶，sharp}\ 6✓✓）$$
$$\textbf{本档关系}✓✓：\text{本档}\ \textbf{不}重开上述两类型✗✓，\ \text{而是}\ \text{第一次}\ \textbf{真正使用「四节点」代数结构}✓✓$$
$$\qquad \textbf{关键区分}✓✓：\text{正三角对偶}\ \textbf{只看到} \text{各阶}\ \sum_j\cos(k\theta_j)\ \text{的统一线性界}✗✓ \ —— \ \textbf{完全未用} \text{「只有四个节点」}✓✓$$

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}12` ✓ | **CLOSED** ✓✓ |
| `C\text{-}380\text{-}13` ✓ | **CLOSED（sharp）** ✓✓ |
| **`C\text{-}380\text{-}15`** ✓ | **NEXT ← 本档注册** ✓✓ |
| `E_0` ✓ | **OPEN** ✓ |
| `E_{\mathrm{coll}}` ✓ | **OPEN（不碰）** ✗✓ |
| `D` ✓ | **DEFERRED** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §4 边界（✓✓）

$$\textbf{不得}写成✗：E_0 = \varnothing\ \text{已证}✗；\ \text{消元}\ \Longrightarrow\ \text{排除}✗；\ \text{新 obstruction 已找到}✗；\ E_0\ \text{不可证}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{消元}\ \textbf{未执行}✗✓；\ \text{四条验收条件}\ \textbf{均为门槛}✓✓$$

## §5 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 自反约束     命中文件数=0    :: 
技术词 代数降维非排除 命中文件数=0    :: 
技术词 重包装归回  命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
