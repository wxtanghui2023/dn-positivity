已查地图（**先查后写**）：`C-340`（P4-D ✓）、`C-339`（**内部极小 ⟹ m >= 6** ✓）、`C-336`（`m_2 <= 11/4`✓；`m_2 - m_4 >= 9/16`✓；`m_4 >= 11/12`✓；幂和单调性 ✓）、`C-333`／`C-335`（五参数化 ✓）、`C-284`（gcd 坍缩 ✓）、`C-275`（可分层面组合＝单-k ✓）。回查见 §6 ✓

D0: 本档对象 = **C-341：偶频归约 ＋ 联合矩约束审计**，**零计算（解析）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 勘误（严格改写）}✓✓：\ \boxed{G_* \le 0.9738225286}✓ \ —— \ \textbf{只是上界}✓，\textbf{不是} G_* \approx 0.9738✗✓$$
$$\qquad \textbf{删去}✗：\text{「真极小值可能更低 ⟹ 余量只会更大」}\ \textbf{不作数学结论}✗；\text{仅可写}\ \textbf{「候选余量」} 0.9738 - 0.5 \approx 0.474✓（\text{相对候选值而}✓）$$
$$\textbf{② 三层分层}✓✓：\text{主线}\ H = \varnothing✓；\text{辅助线}\ \text{数值}\ G_{best}✓；\text{诊断线}\ m \ge 6✓ \ —— \ \textbf{三者不得混}✗✓$$
$$\textbf{③ 战略}✓✓：\text{证}\ H = \varnothing \ \textbf{不需} \text{先求}\ G_*✗✓（\text{唐先生口径}✓）$$
$$\textbf{④ ⭐ 偶频归约（本档核心）}✓✓：\ T_{2r}(c) = 2T_r(c)^2 - 1✓ \Longrightarrow F_{2r} = 2\sum_j T_r(c_j)^2 - 5✓；\text{且}\ T_{2r}\ \text{是}\ c^2\ \text{的多项式}✓ \Longrightarrow \textbf{偶频约束＝}\ [0,1]\ \text{上五点的}\ \textbf{矩约束}✓✓$$
$$\textbf{⑤ 现成框架}✓✓：\text{五点}\ [0,1]\ \text{矩问题的可行性＝经典}\ \textbf{矩空间／Tchebycheff 系统} \text{理论}✓✓（\text{Karlin--Studden}✓；\text{Hausdorff 矩条件}✓）\ —— \ \textbf{不是} separable 证书✗✓$$

## §1 勘误对照（✓✓）

| 项 | 原写法 ✗ | 严格改写 ✓ |
|---|---|---|
| 极值 | `G_* ≈ 0.9738` ✗ | **`G_* <= 0.9738225286`** ✓ |
| 余量 | "余量只会更大" ✗ | **"候选余量 = 0.474（相对候选值）"** ✓ |
| 推断 | 低值候选 `m <= 4` ⟹ 真极小更低 ✗ | **仅作方向感提示，不作结论** ✗✓ |

$$\textbf{理由}✓：\text{找到一个候选}\ c^{(0)}\ \text{给}\ G(c^{(0)}) = 0.9738225✓ \Longrightarrow \textbf{只}\ \text{得}\ G_* \le 0.9738225✗✓ \Longrightarrow \textbf{不得}\ \text{反推真值}✗$$

## §2 三层分层与路线（✓✓）

$$\textbf{主线}✓：\ F_1,\dots,F_{25} \le \tfrac12 \Longrightarrow \bot✓，\text{即}\ \textbf{直接证}\ H = \varnothing✓$$
$$\textbf{辅助线}✓：\text{数值给}\ G_{best}\ \text{与}\ \text{「很可能存在大非锐余量」}✓$$
$$\textbf{诊断线}✓：\ m \ge 6\ \text{识别内部 minimizer 结构}✓（\text{C-339}✓）$$
$$\textbf{重定位瓶颈}✓✓：\text{不是「把交换做得越来越精确」}✗，\text{而是}\ \boxed{\text{怎样直接利用 25 个}\ F_k\ \text{的联合约束证明它们不可能全部}\ \le \tfrac12}✓✓$$

## §3 ⭐ 偶频归约（✓✓，本档核心 ✓）

$$\textbf{双层恒等式}✓✓：\ T_{2r}(c) = 2T_r(c)^2 - 1✓（\text{倍角}✓）\ \Longrightarrow \ \boxed{F_{2r} = 2\sum_{j=1}^{5} T_r(c_j)^2 - 5}✓✓$$
$$\textbf{偶性}✓✓：\ T_{2r}\ \text{为}\ c\ \text{的偶多项式}✓ \Longrightarrow T_{2r}(c) = P_r(c^2)✓，\ P_r\ \text{次}\ r✓$$
$$\Longrightarrow \text{置}\ \boxed{x_j := c_j^2 \in [0,1]}✓ \Longrightarrow F_{2r} = \sum_{j=1}^{5} P_r(x_j)✓ \Longrightarrow \textbf{偶频约束＝}\ [0,1]\ \text{上五点的}\ \textbf{矩约束}✓✓$$
$$\textbf{幂和记法}✓：s_m := \sum_j x_j^m✓ \Longrightarrow \text{偶频约束}\ \textbf{只通过}\ s_1,\dots,s_r\ \text{作用于}\ F_{2r}✓✓$$
$$\textbf{为何这是新对象}✓✓：\text{它}\ \textbf{直接处理联合约束}✓（\text{矩向量}✓），\textbf{不是}\ \text{把每个频率分别做 box-min}✗ \Longrightarrow \textbf{没有}\ \text{掉回}\ C\text{-273／}C\text{-284 的 separable 墙}✓✓$$
$$\textbf{与}\ C\text{-284 的关系}✓✓：\ \gcd\{2,4,\dots,24\} = 2✓ \Longrightarrow \ C\text{-284 预测坍缩到}\ \cos 2\theta\ \text{变量}✓ \ —— \ \text{正是}\ x = c^2✓✓ \Longrightarrow \textbf{不冲突，反而印证}✓✓$$

## §4 已导出的矩不等式链（✓✓）

$$F_2 \le \tfrac12 \Longrightarrow \boxed{s_1 \le \tfrac{11}{4}}✓；\qquad F_4 \le \tfrac12 \Longrightarrow \boxed{s_2 \le s_1 - \tfrac{9}{16}}✓✓（\text{即}\ \sum_j x_j(1 - x_j) \ge \tfrac{9}{16}✓）$$
$$F_6 \le \tfrac12 \Longrightarrow s_3 \le \tfrac{3}{2}s_2 - \tfrac{9}{16}s_1 + \tfrac{11}{64}✓；\qquad F_6\ \text{另给}\ \boxed{s_2 \ge \tfrac{11}{12}}✓$$
$$\textbf{单调性}✓（x_j \in [0,1]✓）：s_1 \ge s_2 \ge s_3 \ge \cdots \ge 0✓$$
$$\Longrightarrow \ \boxed{\tfrac{11}{12} \le s_2 \le s_1 - \tfrac{9}{16} \le \tfrac{35}{16}}✓✓（\text{区间}\ \textbf{相当窄}✓）$$

## §5 判定与可攻击路线（✓⚠️）

$$\textbf{本档未能}\ \text{给出显式矛盾}✗：\text{低阶三条可由}\ x = (0,\ 0.5,\ 0.5,\ 0.5,\ 0.5)✓\ \text{类构型近似满足}✓（s_1 = 2✓，s_2 = 1✓，s_3 = 0.5✓ \le 0.5469✓）$$
$$\textbf{登记可攻击路线}✓✓：\text{把偶频子集}\ K \subseteq \{2,4,\dots,24\}✓ \text{的矩约束代入}\ \textbf{Tchebycheff 系统／矩空间判据}✓✓（\text{Karlin--Studden}✓）\ \text{或低阶}\ \textbf{Hausdorff 矩条件}✓$$
$$\textbf{判据形态}✓✓：\exists \mu_r \ge 0\ \text{使}\ Q(x) := \sum_r \mu_r P_r(x)✓ \Longrightarrow \sum_r \mu_r F_{2r} = \sum_j Q(x_j)✓；\text{若}\ \min_{x \in [0,1]} Q(x) > \tfrac{1}{5}\sum_r \mu_r✓ \Longrightarrow \textbf{矛盾}✓✓$$
$$\qquad \textbf{诚实标注}⚠️：\text{此形态}\ \textbf{看似}\ \text{可分}✓，\text{但其可行性由}\ \textbf{整个矩向量} \text{决定}✓✓ \Longrightarrow \textbf{不}等于} C\text{-275 的可分空洞情形✗✓（\text{待逐项核}⚠️）$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 偶频归约     命中文件数=0    :: 
技术词 矩空间        命中文件数=0    :: 
技术词 矩可行性     命中文件数=0    :: 
```
- **零计算** ✗（仅解析 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`G_* ≈ 0.9738` ✗；余量"只会更大" ✗；偶频路线已给矛盾 ✗；`C-284` 阻挡本路线 ✗（**不阻挡** ✓）
