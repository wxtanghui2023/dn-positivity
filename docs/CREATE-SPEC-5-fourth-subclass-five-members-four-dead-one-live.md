已查地图（**先查后写**）：`CREATE-SPEC-4`（(iv′) 修正＋**引理：乘性变形不移动零点**＋张力三角；缺口＝"非乘性＋系数侧＋移零点＋极限恢复"的第四子类）、`acpc-minimal-test.md`（C ＝ `ΣA(n)M(n)n^{−s}`：**逐点积（Hadamard 积）—— 无简单 ζ 表达 —— 谱非显然**；"真正测试需要配分函数版"）、`acpc-loop-death.md`（链退化，判死——但**只判链部分**）、`viii-monodromy-derivation.md`（素数 zeta `P(s)=Σ_p p^{−s}` 的奇点＝缩放轨道、延拓必经 `log ζ`）、`V191`／GORZ（Jensen 多项式超曲性）、`p26a21-merging-host.md`（**逐字**："ζ 的对称性编码（Hadamard／FE／实系数）—— 都给'轨道'—— 不编码'对齐／合并'"）。**结论**：攻第四子类得**五个成员，四个已死、一个未判死** ✓✓：**素数限制系数**（`P(s)`）⟹ 延拓必经 `log ζ` ⟹ (iii) 的"可证上界"失败；**除子卷积**（`a_n↦Σ_{d|n}a_d`）⟹ DS＝`ζ(s)A(s)` ⟹ **正是 §2 引理所辖**（只"借入"ζ 的零点，不移）；**平滑／平均**⟹ 截断类（M2，需无界精度）；**Taylor 系数非线性**（Jensen 多项式）⟹ `V191`／GORZ 已闭；⭐ **唯一未判死者 ＝ ACPC 的 `C` 对象**（系数侧 Hadamard 积 `ΣA(n)M(n)n^{−s}`，非乘性、非欧拉积、谱"非显然"）⟹ 但原档自述"**真正测试需要配分函数版**" ✓✓；⚠️ **同名不同物登记**：档案 8 处"Hadamard 积"皆指 **Hadamard 分解**（ξ 的因子分解），**本档所指为系数侧 Hadamard 积**，二者不得混用 ✓✓

FREEZE-ACK: 本档即冻结期内的构造尝试与查图（依 `§8.1`；不产候选结论）

D0: 本档对象 = 第四子类的**成员枚举**（五成员／四死／一未判）—— 关系 = 构造尝试与查图，非新机制成立
D1: 0

# CREATE-SPEC-5 · **(甲-1)：攻第四子类 —— 五成员，四死一未判**

> **时间**：2026-09-18 21:38 唐先生：**「两个都试试」** ⟹ (甲-1) 第四子类 ＋ (甲-2) 引理小注 ✓

---

## §0 结论（先行）

$$\text{第四子类}＝\text{"}\textbf{非乘性 ＋ 系数侧 ＋ 移零点 ＋ 极限恢复}\text{"};\quad \textbf{五成员，四死一未判}✓✓$$
$$M_1\ \text{素数限制系数}\ ✗;\quad M_2\ \text{除子卷积}\ ✗（\text{引理所辖}）;\quad M_3\ \text{平滑／平均}\ ✗;\quad M_4\ \text{Taylor 系数非线性}\ ✗;\quad \boxed{M_5\ \text{ACPC 的}\ C\ \text{对象}\ ——\ \textbf{未判死}}✓✓$$

---

## §1 五成员逐条

### (M1) 素数限制系数：`a_n\mapsto a_n\cdot1_{\mathbb P}`

$$\zeta\ \text{的素数限制}\ =\ P(s)=\sum_p p^{-s}\ \text{（素数 zeta）}✓$$
$$\qquad \text{非乘性} ✓(i);\ \text{无欧拉积} ✓(ii);\ \text{奇点＝缩放轨道}\ \{\rho/k\},\ \textbf{确实触碰零点}✓$$
$$\qquad ⚠️\ \text{但}\ P(s)=\sum_k\frac{\mu(k)}{k}\log\zeta(ks) \Longrightarrow \textbf{延拓必经}\ \log\zeta \Longrightarrow \text{值面}（\text{`viii-monodromy`}）✗$$
$$\qquad \Longrightarrow \text{即}\ \text{`C-122`}\ \text{的}\ \textbf{(iii) 失败}（\text{右端奇点无独立可证上界}）✗✗$$

### (M2) 除子卷积：`a_n\mapsto\sum_{d\mid n}a_d`

$$\qquad \text{DS}\ ＝\ \zeta(s)\cdot A(s) \Longrightarrow \textbf{正是 §2 引理所辖}（\text{乘一整因子}）✓$$
$$\qquad \Longrightarrow \text{它"借入"ζ 的零点，}\ \textbf{但不移动它们} \Longrightarrow \textbf{零新信息}✗$$

### (M3) 平滑／平均：`a_n\mapsto\frac1H\sum_{|m-n|\le H}a_m`

$$\qquad \Longrightarrow \text{截断／平滑类}（M2\ \text{类}） \Longrightarrow \textbf{极限需无界精度}（\text{`V188` §2}）✗✗$$

### (M4) Taylor 系数非线性：Jensen 多项式

$$\qquad \text{Jensen 多项式超曲性}\iff\text{RH}（\text{Pólya};\ \text{GORZ}） \Longrightarrow \text{`V191`／`V157` 已闭}✗$$

### (M5) ⭐ ACPC 的 `C` 对象（**唯一未判死**）

$$C(X)=\sum_{a+b=qm\le X}\Lambda(a)\Lambda(b)\Lambda(q)\Lambda(m)=\sum_{n\le X}A(n)M(n),\qquad \text{DS}\ ＝\ \sum_n A(n)M(n)n^{-s}✓$$
$$\qquad A\ \text{（加性卷积）}\ \textbf{非乘性} \Longrightarrow \text{DS}\ \textbf{无欧拉积}✓(ii);\ \ M\ \text{（乘性卷积）}\ \text{DS}＝(\zeta'/\zeta)^2✓$$
$$\qquad \text{系数侧}\ \textbf{Hadamard 积}（\text{逐点积}） \Longrightarrow \textbf{非乘性非线性操作} \Longrightarrow \textbf{移零点}✓$$
$$\qquad \text{档案自述（`acpc-minimal-test` 逐字）}：\text{"C 的 DS}：\Sigma A(n)M(n)n^{-s}——\text{逐点积（Hadamard 积）——}\textbf{无简单 ζ 表达——谱非显然}\text{"}✓✓$$
$$\qquad ⚠️\ \text{原档}\ \textbf{未判死}，\ \text{自述}：\text{"}\textbf{真正测试需要配分版定义}\text{"};\ \text{且}\ \text{`acpc-loop-death`}\ \textbf{只判链部分}（\kappa\ \text{退化}）, \ \textbf{未判}\ C\ \text{本身}✓✓$$
$$\qquad \Longrightarrow \textbf{它是第四子类唯一的活口};\ \text{其}\ (iii)\ \textbf{是唯一待检项}✓✓$$

## §2 ⚠️ 同名不同物登记（纪律）

$$\text{档案 8 处"Hadamard 积"}\ \text{（`grh-criterion-*`, `p26a21-merging-host`, `p5-framework-independence` 等）}\ \textbf{皆指 Hadamard 分解}（\xi=e^{A+Bs}\prod(1-s/\rho)e^{s/\rho}）✓✓$$
$$\qquad \text{本档所指}\ ＝\ \textbf{系数侧 Hadamard 积}（\Sigma a_nb_n n^{-s}）;\ \text{二者}\ \textbf{不得混用}✓✓$$
$$\qquad \text{且}\ \text{`p26a21-merging-host` 的判词可直接引用}：\text{"ζ 的对称性编码（Hadamard／FE／实系数）——}\textbf{都给"轨道"——不编码"对齐／合并"}\text{"}✓$$

## §3 下一步（唯一待办）

$$\text{对}\ M_5\ \text{的唯一待检项}\ ＝\ \text{`C` 的谱是否}\ \textbf{恢复零结构}（(iii)）✓$$
$$\qquad \text{可行的最小测试}：\text{把}\ \text{`C` 的 DS}\ \textbf{沿}\ \sigma\ \text{扫描}，\ \text{看其}\ \textbf{奇点／零点集}\ \text{是否}\ \textbf{含}\ \{\operatorname{Re}\rho\}\ \text{或}\ \{\rho\}\ \text{的}\ \textbf{非平凡痕迹}✓$$
$$\qquad ⚠️\ \text{预算提示}：\text{这需要}\ \textbf{复平面数值}（\text{`C` 的 DS 的解析性质}），\ \text{非本档纸面可判}✓$$

## §4 边界与回查

- ⚠️ 本档**未判死** `C`；**亦未声称** `C` 可用 ⟹ 它是**活口**，不是**候选** ✓
- ⚠️ §1 各成员的"死因"为**本档判断**（M1 依 `viii-monodromy`；M2 依 §2 引理；M3 依 `V188` §2；M4 依 `V191`）✓
- ⚠️ §2 同名不同物**必须**保留（防未来误引）✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 21:3x）`[纪律]`（先跑后写）

```
技术词 第四子类          命中文件数=1  :: ./CREATE-SPEC-4-…（**本会话已用**）
技术词 素数限制系数        命中文件数=0  :: ⟹ **本档新增**
技术词 系数侧 Hadamard 积   命中文件数=0  :: ⟹ **本档新增**（⚠️ 与档案 8 处"Hadamard 积"＝**分解**，同名不同物）
```
**读数（按实测）**：`素数限制系数`／`系数侧 Hadamard 积`＝**0 档 ⟹ 本档新增** ✓；`第四子类`＝**1 档**（`CREATE-SPEC-4`，本会话已用）✓；⚠️ **同名不同物登记**：档案"Hadamard 积"＝**Hadamard 分解**（8 档），本档所指为**系数侧 Hadamard 积**，须分列 ✓
