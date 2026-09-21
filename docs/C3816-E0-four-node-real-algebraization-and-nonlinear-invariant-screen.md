已查地图（**先查后写**）：`C-380-15`（**Newton／self-inversive** ✓✓）、`C-380-14`（**sharp 封口** ✓✓）、`C-380-13`（**正三角对偶 CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-16：`E_0` 的四节点实代数化 ＋ 非线性不变量筛查（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（九条 ✓✓）

$$\textbf{① } C\text{-}380\text{-}15\ \text{定性}✓✓：\textbf{真正值得继续的一刀}✓✓，\ \text{但下一步}\ \textbf{必须} \text{从「写出代数表达式」}\ \textbf{迅速进入「找不可约的新关系」}✓✓$$
$$\qquad \text{验收条件第}\ ②③④\ \text{条}\ \textbf{堵住了} \text{最容易重新包装成}\ C\text{-}380\text{-}13\ \text{的路径}✓✓$$
$$\textbf{② ⭐ 实代数化（第一目标：无共轭歧义的坐标系）}✓✓：e_4 = u + iv✓（u^2 + v^2 = 1✓）；\ e_1 = a + ib✓；\ e_2 = c + id✓✓$$
$$\qquad \text{由}\ e_2 = e_4\overline{e_2}✓ \Longrightarrow \ \boxed{c(1 - u) - dv = 0,\qquad d(1 + u) - cv = 0}✓✓$$
$$\qquad ⭐ \textbf{结构}✓✓：\text{除}\ e_2 = 0\ \text{的退化情形外}✓，\ \boxed{e_2\ \text{的相位被}\ e_4\ \textbf{锁定到半角方向}}✓✓ \iff \boxed{e_2 = e^{i\arg(e_4)/2}\,r,\quad r \in \mathbb{R}}✓✓$$
$$\qquad \qquad （\text{半角的符号选择吸收到}\ r\ \text{中}✓）$$
$$\qquad \text{而}\ e_3 = e_4\overline{e_1}✓ \Longrightarrow \ \boxed{e_3 = (u + iv)(a - ib) = (ua + vb) + i(va - ub)}✓✓$$
$$\qquad \Longrightarrow \ \text{四个单位圆根的 self-inversive 结构}\ \textbf{已把系数空间压到非常低维}✓✓$$
$$\textbf{③ } p_5, p_6\ \text{显式展开}✓✓：p_1 = e_1✓；\ p_2 = e_1^2 - 2e_2✓；\ p_3 = e_1^3 - 3e_1e_2 + 3e_3✓；\ p_4 = e_1^4 - 4e_1^2e_2 + 2e_2^2 + 4e_1e_3 - 4e_4✓✓$$
$$\qquad \boxed{p_5 = e_1^5 - 5e_1^3e_2 + 5e_1e_2^2 + 5e_1^2e_3 - 5e_2e_3 - 5e_1e_4}✓✓$$
$$\qquad \boxed{p_6 = e_1^6 - 6e_1^4e_2 + 9e_1^2e_2^2 - 2e_2^3 + 6e_1^3e_3 - 12e_1e_2e_3 + 3e_3^2 - 6e_1^2e_4 + 6e_2e_4}✓✓$$
$$\qquad \Longrightarrow \ \textbf{然后才} \text{代入}\ e_3 = e_4\overline{e_1}✓，\ |e_4| = 1✓✓$$
$$\textbf{④ 共轭对称}✓✓：\overline{p_k} = p_{-k}✓✓ \ —— \ \textbf{本身不是新东西}✗✓；\ \textbf{真正应检查}✓✓：\text{正、负频率之间能否}\ \textbf{通过四节点的有限阶代数关系形成低阶非线性恒等式}✓✓$$
$$\textbf{⑤ ⭐ 三把「非线性刀」}✓✓：$$
$$\qquad \textbf{A. Hankel／Toeplitz rank-4}✓✓：H_5 = (p_{i+j})_{0 \le i,j \le 5}✓ \Longrightarrow \det H_5 = 0✓✓ \ —— \ \textbf{但还不够}✗✓$$
$$\qquad \qquad \textbf{验收关键}✓✓：\text{把这个行列式完全消去后}✓，\ \text{看它能否产生涉及}\ p_1, \dots, p_6\ \text{与}\ \overline{p_1}, \dots, \overline{p_6}\ \text{的}\ \textbf{非线性约束}✓✓，\ \textbf{而不是}最后化成\ \sum a_k\Re p_k \le C✗✓$$
$$\qquad \qquad \textbf{区别}✓✓：\text{Fourier 对偶给出}\ \textbf{线性泛函的界}✓；\ \text{rank-4 给出 moment 序列的}\ \textbf{代数簇约束}✓✓$$
$$\qquad \textbf{B. Gram determinant／Vandermonde 消元}✓✓：\Delta = \prod_{i<j}(z_i - z_j)✓ \Longrightarrow |\Delta|^2 = \prod_{i<j}|z_i - z_j|^2 \ge 0✓✓，\ \text{可写成}\ e_1, \dots, e_4\ \text{的对称多项式}✓$$
$$\qquad \qquad \text{代入 self-inversive 后}\ \textbf{有机会} \text{得到}\ \textbf{真正利用单位圆几何的非线性半代数约束}✓✓（\text{非负性源自 Vandermonde 的几何分离结构}✓）$$
$$\qquad \qquad \textbf{小心}✗✓：\text{若最终只是经过恒等变形变成某个 Toeplitz／Fejér PSD 条件} \Longrightarrow \textbf{仍要反包装}✗✓$$
$$\qquad \textbf{C. 四节点特有的 Newton 消元理想（优先）}✓✓：\text{把}\ e_3 - e_4\overline{e_1} = 0✓，\ e_2 - e_4\overline{e_2} = 0✓，\ e_4\overline{e_4} - 1 = 0✓ \ \text{与 Newton 关系一起考虑}✓✓$$
$$\qquad \qquad \textbf{目标不是}「证明有关系」✗✓，\ \text{而是找}\ \textbf{最小次数} \text{的}\ \boxed{F(p_1, \dots, p_6, \overline{p_1}, \dots, \overline{p_6}) = 0}✓✓$$
$$\textbf{⑥ ⭐ } F\ \text{的五条要求（采纳）}✓✓：\text{①}\ genuinely\ nonlinear✓；\ \text{② 使用了}\ |z_j| = 1✓✓；\ \text{③ 使用了「四个节点」}✓✓；\ \text{④}\ \textbf{不能}只通过取实部／线性组合退化成\ C\text{-}380\text{-}13✗✓；\ \text{⑤ 对}\ E_0\ \text{的目标不等式}\ \textbf{确实产生新的约束}✓✓$$
$$\textbf{⑦ ⭐ 「不要浪费时间」测试（采纳）}✓✓：\text{找到任何候选 obstruction}\ F\ \text{后}\ \textbf{立即} \text{做}\ \boxed{F \stackrel{?}{=} G(\Re p_1, \dots, \Re p_6)}✓✓$$
$$\qquad \textbf{若}\ G\ \text{只是}\ \textbf{线性泛函}✗，\ \text{或可由若干}\ \sum a_k\Re p_k \le C\ \text{组合得到}✗ \Longrightarrow \textbf{直接归回}\ C\text{-}380\text{-}13✓✓$$
$$\qquad \textbf{反之}✓✓：\text{若出现如}\ |p_2 - p_1^2/4|^2 \le \Phi(\Re p_1, \Re p_2, \dots)✓ \ \text{这种含}\ \textbf{真正乘积、模平方、行列式或秩约束} \text{的对象}✓✓ \Longrightarrow \textbf{值得继续}✓✓$$
$$\textbf{⑧ 压缩路线}✓✓：\ \boxed{C\text{-}380\text{-}15 \to \text{实代数化} \to \text{rank-4／Vandermonde} \to \text{非线性恒等式} \to E_0}✓✓$$
$$\qquad \textbf{而不是}✗✓：\ C\text{-}380\text{-}15 \to \text{再找一个 Fourier 权重} \to C\text{-}380\text{-}13✗✓$$
$$\textbf{⑨ ⭐ 下一刀最有价值的产物}✓✓：\textbf{不是}「证明}\ E_0\text{」✗✓，\ \text{而是}\ \textbf{先判定}✓✓：$$
$$\qquad \boxed{\text{四节点单位圆约束的消元理想中，是否存在一个能真正作用于}\ E_0\ \text{的、非线性的、不可还原为正三角对偶的 obstruction}}✓✓$$
$$\qquad \textbf{若只吐出线性 Fourier 边界}✓✓ \Longrightarrow C\text{-}380\text{-}15\ \text{给出}\ \textbf{很干净的 GAP}✓✓：\boxed{\text{四节点 self-inversive 代数本身不足以提供新障碍}}✓✓$$
$$\qquad \textbf{若吐出非线性约束}✓✓ \Longrightarrow \text{才值得进入}\ \textbf{第二层的定量估计}✓✓$$

## §1 与既有封口的关系（✓✓）

$$\textbf{已封口}✓✓：C\text{-}380\text{-}12\（\text{等权求和}✓）、C\text{-}380\text{-}13\（\text{单一正三角对偶，sharp}\ 6✓✓）$$
$$\textbf{本档界限}✓✓：\text{任何最终化归为}\ \sum a_k\Re p_k \le C\ \text{的对象}\ \Longrightarrow \textbf{归回}\ C\text{-}380\text{-}13✗✓$$
$$\qquad \textbf{纪律}✓✓：\text{「非线性」必须}\ \textbf{可核验}✓（\text{乘积／模平方／行列式／秩}✓），\ \textbf{不能}只靠措辞✗✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}12` ✓ | **CLOSED** ✓✓ |
| `C\text{-}380\text{-}13` ✓ | **CLOSED（sharp）** ✓✓ |
| **`C\text{-}380\text{-}16`** ✓ | **NEXT ← 本档注册** ✓✓ |
| `E_0` ✓ | **OPEN** ✓ |
| `E_{\mathrm{coll}}` ✓ | **OPEN（不碰）** ✗✓ |
| `D` ✓ | **DEFERRED** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：E_0 = \varnothing\ \text{已证}✗；\ \text{已找到非线性 obstruction}✗；\ \text{消元理想已判定}✗；\ E_0\ \text{不可证}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{三把刀}\ \textbf{均未执行}✗✓；\ \text{半角锁定为}\ \textbf{已述结构}✓✓（\text{待显式核验}⚠️）$$

## §4 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §5 边界（✓✓）

$$\textbf{纪律}✓✓：\text{任何「新」主张}\ \textbf{必须}可核验✓；\ \text{反包装测试}\ \textbf{无条件执行}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 实代数化坐标系 命中文件数=0    :: 
技术词 半角锁定     命中文件数=0    :: 
技术词 非线性不变量筛查 命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
