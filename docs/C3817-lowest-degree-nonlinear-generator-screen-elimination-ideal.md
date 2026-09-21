已查地图（**先查后写**）：`C-380-16`（**实代数化 ＋ 三把刀** ✓✓）、`C-380-15`（**Newton／self-inversive** ✓✓）、`C-380-13`（**sharp 封口** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-17：消元理想的最小非线性生成元筛查（注册＋首轮核验）**，**有计算（数值核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① } \det H_5 = 0\ \textbf{本身不算} \text{obstruction}✗✓：H_5 = (p_{i+j})_{0 \le i,j \le 5} = V^{\top}V✓ \Longrightarrow \operatorname{rank} \le 4✓ \Longrightarrow \det H_5 = 0✓✓（\textbf{严格}✓，\ \textbf{真正用「四节点」}✓）$$
$$\qquad \textbf{但它只是}\ \boxed{\text{四节点 moment variety 的 defining equation}}✓，\ \textbf{而不是}\ \boxed{\text{作用于}\ E_0\ \text{的 obstruction}}✗✓$$
$$\qquad \Longrightarrow \ \textbf{第一验收点}✓✓：\textbf{不要}直接估计\ \det H_5✗✓，\ \text{而是}\ \textbf{与}\ E_0\ \text{的具体约束}\ \textbf{联立后消元}✓✓$$
$$\textbf{② 分层优先}✓✓：\text{变量}\ p_1, \dots, p_6✓\ \text{与}\ q_k = \overline{p_k}✓；\ \text{按次数分层}\ \deg F = 2, 3, 4, \dots✓✓$$
$$\qquad \textbf{优先结构}✓✓：p_ap_b✓，\ p_a\overline{p_b}✓，\ |p_a|^2✓，\ p_ap_b\overline{p_c}✓ \ \textbf{而非} \text{纯线性}\ \sum c_kp_k + \sum d_k\overline{p_k}✗✓$$
$$\qquad \Longrightarrow \ \boxed{\text{线性层已被}\ C\text{-}380\text{-}13\ \textbf{sharp 封死}}✓✓$$
$$\textbf{③ ⭐⭐ 二次层首候选（本档核心）}✓✓：\text{由}\ p_2 = e_1^2 - 2e_2✓ \Longrightarrow e_2 = \frac{p_1^2 - p_2}{2}✓；\ e_3 = e_4\overline{e_1} = e_4\overline{p_1}✓；\ p_3 = p_1^3 - 3p_1e_2 + 3e_4\overline{p_1}✓✓$$
$$\qquad \Longrightarrow \ \boxed{6e_4\overline{p_1} = 2p_3 + p_1^3 - 3p_1p_2}✓✓\ \Longrightarrow \ \text{用}\ |e_4| = 1✓（p_1 \ne 0✓）\ \Longrightarrow \ \boxed{F_3 := |2p_3 + p_1^3 - 3p_1p_2|^2 - 36|p_1|^2 = 0}✓✓$$
$$\qquad ⚠️ \textbf{勘误（唐先生写法）}✗✓：\text{原写}\ 6e_4\overline{p_1} = 2p_3 - p_1^3 + 3p_1p_2✓ \ \textbf{符号有误}✗✓ \ —— \ \textbf{数值}：\text{正确版残差}\ 2.1 \times 10^{-14}✓✓，\ \text{原写版残差}\ 9.7 \sim 39✗✗$$
$$\qquad \qquad \text{且}\ |A_2| \ne |A_1|✓ \Longrightarrow \textbf{取模层也不等价}✗✓（\text{原写版}\ F_3\ \text{数值残差}\ 6.6 \times 10^2✗✗）$$
$$\qquad \textbf{性质}✓✓：F_3\ \textbf{同时使用} \text{Newton 结构}\ (p_1, p_2, p_3)✓，\ e_3 = e_4\overline{e_1}✓，\ \textbf{最关键}\ |e_4| = 1✓✓ \Longrightarrow \textbf{明显非线性}✓✓$$
$$\textbf{④ ⭐ 反包装三项（本档已完成首轮）}✓✓：$$
$$\qquad \textbf{(i) unit-circle-native}✓✓：\text{一般复根下满足者}\ 0/3000✓✓ \Longrightarrow \text{去掉}\ |e_4| = 1\ \text{后关系}\ \textbf{不再成立}✓✓$$
$$\qquad \textbf{(ii) 依赖结构（Ablation）}✓✓：\text{一般节点下}\ 6e_3 = A_1\ \text{恒成立}✓（3000/3000✓） \Longrightarrow \ \boxed{A_1\ \text{的右端是}\ 6e_3\（\textbf{Newton 层}✓），\ \textbf{额外} \text{等式}\ e_3 = e_4\overline{p_1}\ \text{才把它接到}\ e_4}✓✓$$
$$\qquad \textbf{(iii) 非线性性}✓✓：A_1\ \text{与}\ 6\overline{p_1}\ \text{不等者}\ 2000/2000✓✓ \Longrightarrow \ \textbf{含真正乘积／模结构}✓✓，\ \text{非纯实部线性}✗✓$$
$$\textbf{⑤ } p_4\ \text{消}\ e_4\ \text{（更漂亮）}✓✓：p_4 = e_1^4 - 4e_1^2e_2 + 2e_2^2 + 4e_1e_3 - 4e_4✓✓，\ \text{代入后}\ e_4\ \textbf{只以}\ e_4\ \text{与}\ e_4\overline{p_1}\ \text{出现}✓✓$$
$$\qquad \Longrightarrow \text{与}\ 6e_4\overline{p_1} = A_1\ \textbf{联立完全消掉}\ e_4✓✓ \Longrightarrow \ \boxed{F_4(p_1, \dots, p_4, \overline{p_1}, \dots, \overline{p_4}) = 0}✓✓$$
$$\qquad \textbf{比直接上}\ 6 \times 6\ \text{Hankel determinant}\ \textbf{更有价值}✓✓；\ p_5, p_6\ \textbf{后置}✓✓（\text{用于检查该 ideal 是否产生}\ \textbf{新的独立关系}✓✓）$$
$$\textbf{⑥ 五项硬验收}✓✓：$$
$$\qquad \textbf{A}✓：\text{找}\ \textbf{最低次数} \text{非线性}\ F✓（\text{优先}\ \deg 2／3／4✓）；\ \textbf{B}✓✓：\text{明确指出}\ \textbf{哪一步用}\ |e_4| = 1✓；\ \textbf{C}✓✓：\text{哪一步用}\ e_3 = e_4\overline{e_1}／\text{四节点}✓；$$
$$\qquad \textbf{D}✓✓：\text{完全展开并做}\ C\text{-}380\text{-}13\ \text{反包装}✓；\ \textbf{E}✓✓：\text{将}\ F = 0\ \text{与}\ E_0\ \text{联立}✓，\ \textbf{证明它}\ \textbf{实际缩小 feasible set}✓✓ \ \textbf{否则只能记为 algebraic asset}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\textbf{E 是真正的生死线}}✓✓$$
$$\textbf{⑦ 对}\ C\text{-}380\text{-}17\ \text{的当前判定}✓✓：\text{反包装 (i)(ii)(iii)}\ \textbf{已通过}✓✓，\ \textbf{但 E 未做}✗✓ \Longrightarrow \ \text{目前}\ F_3\ \text{的等级} = \ \boxed{\textbf{algebraic asset}}✓✓（\textbf{尚未} \text{是 obstruction}✗✓）$$
$$\textbf{⑧ 路线}✓✓：\ \boxed{p_1, p_2, p_3, p_4 \Longrightarrow e_4\ \text{elimination} \Longrightarrow F_4 = 0}✓✓$$
$$\qquad \textbf{本次意义}✓✓：\textbf{不是}再换坐标／再换 Fourier 权重✗✓，\ \text{而是}\ \textbf{第一次} \text{拿到可明确标记为}\ \boxed{unit\text{-}circle + self\text{-}inversive + four\text{-}node}\ \text{的非线性候选}✓✓$$

## §1 数值核验记录（✓✓）

$$\textbf{恒等式}✓✓：\max|A_1 - 6e_4\overline{p_1}| = 2.132 \times 10^{-14}✓✓（3000\ \text{组}✓）；\ \max\big||A_1|^2 - 36|p_1|^2\big| = 7.390 \times 10^{-13}✓✓$$
$$\textbf{自反性}✓✓：|e_3 - e_4\overline{e_1}| \approx 4.4 \times 10^{-16}✓，\ ||e_4| - 1| = 0✓，\ |e_2 - e_4\overline{e_2}| \approx 4.4 \times 10^{-16}✓✓$$
$$\textbf{原写版}✗✓：\max\big||A_2|^2 - 36|p_1|^2\big| = 6.605 \times 10^2✗✗ \Longrightarrow \textbf{不成立}✗✓$$
$$\qquad ⚠️ \textbf{我方首轮核验亦有缺口}✗✓：\text{首轮}\ \textbf{只测了错误版本}✗✓（\text{漏测}\ A_1✓），\ \text{已在本档补齐}✓✓$$
$$\textbf{一般复根}✓✓：0/3000✓✓；\ \textbf{一般节点下}\ 6e_3 = A_1\ \text{恒成立}✓✓（3000/3000✓）$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}12` ✓ | **CLOSED** ✓✓ |
| `C\text{-}380\text{-}13` ✓ | **CLOSED（sharp）** ✓✓ |
| `C\text{-}380\text{-}16` ✓ | **COMPLETE** ✓✓ |
| **`C\text{-}380\text{-}17`** ✓ | **NEXT ← 本档注册；`F_3` 反包装 (i)(ii)(iii) 通过；E 未做** ✓✓ |
| `E_0` ✓ | **OPEN** ✓ |
| `E_{\mathrm{coll}}` ✓ | **OPEN（不碰）** ✗✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：E_0 = \varnothing\ \text{已证}✗；\ F_3\ \text{已是 obstruction}✗✓（\textbf{仅} algebraic asset✓）；\ \text{可行域已缩小}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档有}\ \textbf{数值核验}✓✓；\ \textbf{勘误一条}✗✓（原写符号）；\ \textbf{我方首轮核验缺口一条}✗✓（\text{已补}✓）$$

## §4 边界（✓✓）

$$\textbf{有计算}✓（数值核验✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §5 边界（✓✓）

$$\textbf{纪律}✓✓：\text{每一「新」主张须}\ \textbf{数值或显式代数核验}✓✓；\ \text{反包装测试}\ \textbf{无条件执行}✓✓；\ \textbf{E 未过不得升级}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 消元理想最小生成元 命中文件数=0    :: 
技术词 单位圆原生  命中文件数=0    :: 
技术词 生死线验收  命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（恒等式／符号／unit-circle-native／ablation／非线性 ✓）
