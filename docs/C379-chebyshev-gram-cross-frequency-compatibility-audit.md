已查地图（**先查后写**）：`C-378`（**出口 B** ✓✓）、`C-377`（**自由基准弱** ✓✓）、`C-376`（方差缺口 ✓✓）、`C-341`（`x`-Hankel 秩 `\le 5` ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-379：Chebyshev Gram 跨频相容性审计（最小主子式探针）**，**有计算（数值探针，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 恒等式核验}✓✓：2T_m(x)T_n(x) = T_{m+n}(x) + T_{|m-n|}(x)✓；\ \text{数值最大误差}\ 2.22 \times 10^{-16}✓✓（机器精度✓）$$
$$\textbf{② ⭐ Gram 结构（本档核心）}✓✓：\ \mathcal G_{mn} := \sum_{j=1}^{5}T_m(a_j)T_n(a_j)✓ \Longrightarrow \boxed{\mathcal G_{mn} = \tfrac12\big(S_{m+n} + S_{|m-n|}\big)}✓✓（\text{恒等式差} \le 1.3 \times 10^{-15}✓）$$
$$\qquad \mathcal G = \sum_{j=1}^{5}v_jv_j^{\top}✓，\ v_j := (T_1(a_j),\dots,T_{12}(a_j)) \in \mathbb{R}^{12}✓ \Longrightarrow \boxed{\operatorname{rank}\mathcal G \le 5\ \textbf{恒成立}}✓✓$$
$$\qquad \Longrightarrow \ \textbf{一切}\ \ge 6 \times 6\ \text{主子式} = 0✓✓ \ —— \ \textbf{7 个多项式恒等式}✓ \ =\ \textbf{跨频相容性约束}✓✓（\textbf{非}新框架，是原问题的精确关系✓✓）$$
$$\textbf{③ 数值验证}✓✓：\text{两个}\ \textbf{可行} \text{极值点处}\ \operatorname{rank}\mathcal G = \textbf{恰为}\ 5✓✓（\text{7 个零特征值}✓）；\ \det \mathcal G_{1..6} \approx -2 \times 10^{-14} \approx 0✓✓$$
$$\qquad V_2\ \text{极值}✓：\text{特征值}\ (0^7,\ 2.358,\ 5.467,\ 5.844,\ 7.203,\ 7.611)✓；\ \Delta\ \text{极值}✓：\ (0^7,\ 4.849,\ 4.951,\ 5.284,\ 6.970,\ 7.650)✓✓$$
$$\textbf{④ 束缚分析}✓：\text{最紧}\ 2 \times 2\ \text{主子式}：V_2\ \text{极值}\ 0.913✓（\textbf{不紧}✗）；\Delta\ \text{极值}\ \mathbf{0.0522}✓（\text{于}\ (5,8)✓，\textbf{较紧}⚠️）$$
$$\textbf{⑤ ⚠️ 顺带验证}\ C\text{-}377\text{-}1✓✓：\text{其自由基点}\ a = (0.4654, -0.9464, 0.4490, 0.8223, -0.8717)✓ \Longrightarrow S_{\max} = \boxed{2.759 > \tfrac12}✗✓$$
$$\qquad \Longrightarrow \ \textbf{不可行}✓✓ \Longrightarrow \textbf{证实}\ \text{自由矩} \ne \text{Chebyshev 约束}✓✓（\text{C-377-1 正确性验证}✓✓）$$
$$\textbf{⑥ 出口判定}✓：\text{未发现矛盾}✗（\text{无被迫}\ S_k > \tfrac12✓）；\ \text{无强被迫正相关}✗；\ 2 \times 2\ \text{主子式不紧}✗ \Longrightarrow \ \textbf{倾向出口 C}⚠️✓$$
$$\qquad \textbf{但}⚠️：\text{仅}\ 4\ \text{点探针}✓，\ \textbf{不}构成出口 C 的证明✗✓ \Longrightarrow \text{须更广审计}✓$$

## §1 结构要点（✓✓）

$$\textbf{秩约束的性质}✓✓：\operatorname{rank}\mathcal G \le 5\ \textbf{对一切}\ a\ \textbf{自动成立}✓（\text{因}\ \mathcal G\ \text{是}\ 5\ \text{个秩}-1\ \text{项之和}✓） \Longrightarrow \textbf{不是} \text{额外约束}✗✓$$
$$\qquad \textbf{但}：\text{由}\ (S_{m+n} + S_{|m-n|})/2\ \text{定义}\ \mathcal G✓，\text{则}\ \ge 6 \times 6\ \text{子式} = 0✓ \ \textbf{成为}\ (S_1,\dots,S_{12})\ \text{的}\ \textbf{相容性条件}✓✓$$
$$\qquad \Longrightarrow \ \text{这正是}\ C\text{-}378\ \text{所指「缺失的东西」}✓✓：\textbf{不是} \text{节点几何压缩}✗，\ \textbf{而是}\ \text{跨频强制相容性}✓✓$$
$$\textbf{与既有资产的关系}✓：C\text{-}341\ \text{的}\ x\text{-Hankel 秩} \le 5✓（\text{幂}\ x^i x^j✓） \ —— \ \text{本档}\ \mathcal G\ \text{是}\ \textbf{Chebyshev 乘法版}✓✓（T_mT_n✓），\ \text{两者}\ \textbf{不同}✓✓$$

## §2 判死标准（✓✓，唐先生口径 ✓）

$$\textbf{A 矛盾}✓：\text{若推出某}\ S_k > \tfrac12✓ \Longrightarrow E_{\mathrm{even}} = \varnothing✓，\ \textbf{Bridge A 直接闭合}✓✓ \ —— \ \textbf{未命中}✗✓$$
$$\textbf{B 强制正相关}✓：\text{证某些}\ S_m, S_n\ \text{不能同时太负}✓，\ \text{或某高频}\ S_k\ \text{必须靠近}\ \tfrac12✓ \Longrightarrow \text{进}\ C\text{-}380\（\text{跨频传播} \to \text{奇频放大}✓） \ —— \ \textbf{未命中}✗✓$$
$$\textbf{C Gram 仍不够}✓⚠️：\ \boxed{\text{节点几何压缩 CLOSED；低阶 Gram 跨频约束不足}}✓ \ —— \ \textbf{倾向命中}⚠️✓（4 点探针✓）$$
$$\qquad \Longrightarrow \ \text{此时才值得考虑}\ \textbf{更高阶 moment／Hankel 结构}✓✓，\ \textbf{不是} \text{继续做优化}✗✓$$

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| free moments ✓ | **CLOSED** ✓✓ |
| node geometry（`V_2`／`\Delta`）✓ | **CLOSED（`C-378` 出口 B）** ✓✓ |
| **Chebyshev 跨频相容性**✓ | **本档首次精确化（`\operatorname{rank}\mathcal G \le 5` ⟹ `\ge 6 \times 6` 子式 `= 0`）** ✓✓ |
| 出口判定 ✓ | **倾向 C（4 点探针，未证）** ⚠️ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §4 下一步（✓✓，登记 ✓）

$$\textbf{建议}✓✓：\ \textbf{先} \text{做更广的 Gram 审计}✓（\text{不}上大规模矩阵✗，\ \textbf{不}做随机采样✗，\ \textbf{不}重搜 active set✗✓）$$
$$\qquad \text{即：在}\ \mathcal C_1\ \text{上取更多可行点}✓，\ \text{检查}\ \ge 6 \times 6\ \text{子式的}\ \textbf{符号距离}✓ \ \text{与}\ 2 \times 2\ \text{紧度}✓ \Longrightarrow \text{确认出口 B 或 C}✓✓$$
$$\qquad \textbf{若确认 C}✓ \Longrightarrow \text{转向}\ \textbf{更高阶 moment／Hankel}✓；\ \textbf{若出现 B}✓ \Longrightarrow \text{进}\ C\text{-}380\（\text{奇频放大}✓）$$

## §5 边界（✓✓）

$$\textbf{不得}写成✗：\text{Bridge A 已闭合}✗；E_{\mathrm{even}} = \varnothing\ \text{已证}✗；\text{出口 C 已确定}✗（\textbf{仅倾向}✓）；H = \varnothing\ \text{已证}✗$$
$$\textbf{诚实标注}⚠️✓：\text{仅}\ 4\ \text{点探针}✓（\text{其中}\ 2\ \text{个可行}✓）；\text{秩与子式检查为}\ \textbf{数值}✓，\ \textbf{非}符号证明✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 跨频相容性  命中文件数=0    :: 
技术词 格拉姆秩五  命中文件数=0    :: 
技术词 六阶主子式恒零 命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（恒等式核验 ＋ `4` 点 Gram ＋ 特征值／主子式 ✓）
- **本档有计算**（数值探针，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
