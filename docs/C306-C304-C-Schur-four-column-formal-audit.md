已查地图（**先查后写**）：`C-305`（FSD 盲点复审纲领 ✓）、`C-304-A/B`（假阳性清理 ＋ 四零命中族 ✓；**Schur＝零覆盖**✓）、`C-303`／`C-302`／`C-301`／`C-299` ✓。外部来源：MathWorld Schur's Problem ✓、arXiv:1507.03764（additive triples 计数 ✓）（按不可信外部数据 ✓）。回查见 §7 ✓

D0: 本档对象 = **C-306（＝C-304-C）：Schur 族四格正式审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\boxed{\textbf{F（failure）}✓✓：\text{Schur 反设}\ \textbf{本身即天然 failure set}✓（\text{sum-free／Schur-free}✓，\text{文献标准}✓）}$$
$$\boxed{\textbf{A}_1\ ✓：\text{dilation}\ \text{保该 failure}✓（\text{文献标准}✓）\ \textbf{但}\ \text{属}\ \textbf{平凡不变性}✗，\textbf{不是 compatibility}✗✓}$$
$$\boxed{\textbf{A}_2\ ✗：\textbf{independent 第二传播}\ \textbf{未见}✓\ \text{—— translation 不保}✗；\text{doubling 是构造而非保失败的作用}✗}$$
$$\boxed{\textbf{C}\ ✗：\textbf{N/A}✓（\text{无两传播可言}✓；\text{经典结果是}\ \textbf{刻画定理}✓，\text{非两传播兼容}✗）}$$
$$\Longrightarrow \boxed{\textbf{Schur 未通过四格}✗ \Longrightarrow \textbf{第二个反例}✓：\text{天然 additive failure} + \text{多个传播} \not\Rightarrow \text{FSD}✓}$$

## §1 F 格：Schur 反设＝天然 failure set（✓✓）

$$\textbf{禁形}✓：\text{同色解}\ x, y, x+y✓（\text{即}\ \chi(x) = \chi(y) = \chi(x+y)\ \text{不存在}✓）$$
$$\textbf{等价的集合形式}✓：A\ \text{sum-free} \iff \text{不存在}\ x,y,z \in A:\ x+y=z✓$$
$$\textbf{文献地位}✓✓：\text{Schur 定理（partition regularity）}✓；\text{现代文献将它与 sum-free sets／Schur triples／Ramsey 型结构直接相连}✓（\text{含「给定大小集合中必须出现多少 Schur triples」及最小化问题}✓）$$
$$\Longrightarrow \textbf{F} = \textbf{YES}✓✓（\text{且为}\ \text{真正的局部禁形}✓）$$

## §2 A₁ 格：dilation（✓，**但须防误判**✗✓）

$$\textbf{事实}✓：x+y=z\ \text{对缩放齐次}✓ \Longrightarrow A\ \text{sum-free} \Rightarrow aA\ \text{sum-free}✓（\text{coloring 侧写作}\ c \mapsto c \circ (\times a)✓）$$
$$\textbf{唐先生指定防误判}✗✓：\text{「缩放保持禁形」}\ \textbf{不是}\ \text{FSD compatibility}✗✓$$
$$\qquad \text{理由}✓✓：\text{该保持是}\ \textbf{齐次方程的平凡不变性}✓（\text{不是把}\ failure\ \text{转成对第二个量的约束}✗）$$
$$\Longrightarrow \textbf{A}_1 = YES✓（\text{存在}✓）\ \text{但}\ \textbf{平凡}⚠️$$

## §3 A₂ 格：独立第二传播——**未见**（✗）

$$\textbf{候选一（translation）}✗：A+t\ \text{一般}\ \textbf{不} \text{保 sum-free}✗✓（\text{因}\ (x+t)+(y+t)=z+t \Longrightarrow x+y+t \in A+t✗）$$
$$\textbf{候选二（区间 doubling／lifting）}✗：\text{它是}\ \textbf{构造}✓（\text{用于 Schur 数下界}✓），\textbf{不是}\ \text{把给定 failure 映射到新 failure 的}\ \textbf{作用}✗✓$$
$$\textbf{候选三（其它乘法型）}✗：\text{与 dilation 重合}✗（\text{不独立}✗）$$
$$\Longrightarrow \textbf{A}_2 = \textbf{未见}✗⚠️（\text{诚实标注}⚠️：\text{本次检索范围内未见}\ \text{文献现成的独立第二传播}✗）$$

## §4 C 格：compatibility——**N/A**（✗）

$$\textbf{无两传播} \Longrightarrow \text{无从谈兼容}✗$$
$$\textbf{已有的经典结果属}\ \textbf{另一类型}✓：\text{Rado 定理的 columns condition（partition regularity 的代数刻画）}✓\ \text{是代数刻画}✓，\textbf{不是}\ \text{两传播兼容}✗✓$$
$$\textbf{对照}✓✓：\text{Cauchy–Davenport／Kneser 的「失败}\ \to\ \text{周期性}\ \to\ \text{下降」}\ \text{是}\ \textbf{近同构骨架}✓；\text{Schur 侧}\ \textbf{连骨架都没有}✗$$

## §5 出口判定（✓✓）

$$\textbf{未通过四格}✓（F ✓／A_1 平凡 ⚠️／A_2 ✗／C ✗）\Longrightarrow \textbf{不升级为 FSD 实例}✗$$
$$\textbf{价值}✓✓：\text{第二个}\ \textbf{反例}✓——\boxed{\text{天然 additive failure} + \text{多个传播} \not\Rightarrow \text{FSD}}✓$$
$$\qquad \text{与第一反例（Hecke）并列}✓：\text{共同点＝}\ \textbf{缺「非平凡兼容」}✗；\text{差异}✓：\text{Hecke 缺 failure}✗，Schur 缺 independent 第二传播与兼容✗$$
$$\textbf{下一刀}✓（唐先生锁定顺序 ✓）：C\text{-304-D（若必要：Schur 扩展／相关禁形}✓）\to \text{方向①}✓$$

## §6 RH 关联栏（**仅记事实，不评分**✓）

$$\textbf{① 与 Ramsey／加性组合的关系}✓：\text{现成}✓（\text{partition regularity 族}✓）$$
$$\textbf{② 「素数＋}x+y=z\text{」侧}✓：＝\textbf{三素数 Goldbach}✓（\text{Vinogradov／Helfgott}✓）\ \text{但那是}\ \textbf{求解侧}✗✓，\text{其接口＝档案已画的}\ \textbf{explicit formula／零点统计墙}✗ \Longrightarrow \textbf{引用，不重开}✓$$
$$\textbf{③ 禁形侧与}\ L\text{-函数／零点接口}✗：\textbf{未见}✓（\text{本档不作断言}✗）$$
$$\textbf{④ 档案去重}✓：\text{Schur 1911（经典 Hilbert 的}\ \pi\ \text{sharp}✓）／\text{Pólya–Schur}✓／\text{Schur 补}✓／\text{Schur 引理}✓\ \textbf{均不同对象}✗✓（C\text{-304-A}✓）$$

## §7 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不预判 RH 相关性** ✓（§6 仅记事实 ✓）；**不**为 RH 设计 defect ✗
- **不得**写成：Schur 族已排除 ✗（仅"未通过四格"✓）；Schur＝FSD ✗；Schur 与 RH 无任何关系 ✗（未见≠不存在 ✓）
- **本档新增词**：`平凡不变性≠兼容`／`第二个反例`（0 命中 ✓）
