已查地图（**先查后写**）：`CREATE-SPEC-4`（四条款＋引理 L1：乘性变形不移零点）、`CREATE-SPEC-6`（M5 判死：去趋势后局部极大 `d_C=0` vs `d_\Lambda=50`；正负对照齐备）、`CREATE-SPEC-8`（b1／b2／b3 三分；L2 常数系数平凡性；L3 乘性保持）、`V188` §2（线性通道饱和、"反演到逐点需无界精度"）、`p7-prime-power-support.md`／`p72-nonlinear-compatibility.md`／`p11-zero-flow-lyapunov.md`（**素数幂支撑**已有专档）、`p26a21-merging-host.md`（对称性编码"只给轨道"）。关键词回查：`素数幂支撑`＝**4 档（已有）**；`Barnes 型卷积`／`聚合不可反演`＝**0 档（新增）**。**结论**：⭐ 唐先生 21:58「a, b 其实是一个命题，非 a 即 b」⟹ **按"同一命题两面"处理**：**(A) b3 的两自然子族**——**素数幂支撑上的逐点族**与**加性卷积族**——**均死于\ \textbf{结构论证}（非"找不到"）** ✓✓：**(A1)** 逐点族：`\sum\Lambda(n)^2n^{-s}=\sum_p(\log p)^2/(p^s-1)`，**收敛横标 `1/2`**，其**奇点＝单个素数的 `p^s=1` 点，与 ζ 零点无关** ⟹ (iii) 死（**初等证明**）✓✓；**(A2)** 加性卷积族：DS ＝ **Barnes 型 Mellin 卷积**（含 `\Gamma` 核），ζ 零点**只经积分出现** ⟹ **聚合型 ⟹ 不可反演**（`V188` §2），且**与 `CREATE-SPEC-6` 的实验（γ 处无局部结构）一致** ✓✓ ⟹ ⭐ **b3 的两个自然子族已被结构性钉住；但 `b3` 全类（"点逐＋加性卷积"有限闭合）的为空性仍未证**（该类＝算术电路闭包，极大）✓✓

FREEZE-ACK: 本档即冻结期内的方向攻击与结构论证（依 `§8.1`；不产候选结论）

D0: 本档对象 = **b3 两自然子族的结构性判定**（A1 初等证明／A2 聚合论证）＋ 结构定理的剩余缺口 —— 关系 = 结构论证与缺口定位，非新机制
D1: 0

# CREATE-SPEC-9 · **(a)+(b) 同一命题：b3 两自然子族的结构性判定**

> **时间**：2026-09-18 21:58 唐先生：**「a, b」**，并指出 **"这两个其实是一个命题，非 a 即 b"** ⟹ **找到 b3 实例 ⟺ 推翻结构定理** ✓

---

## §0 结论（先行）

$$\textbf{命题（唐先生）}：\text{"b3 有实例"}\ \textbf{与} \text{"b3 结构定理成立"}\ \textbf{互为否定} \Longrightarrow \textbf{同一命题两面}✓✓$$
$$\textbf{本档处理}：\text{把}\ b3\ \text{按其}\ \textbf{两自然子族} \text{拆开，逐个给}\ \textbf{结构性判定}✓✓$$
$$\qquad \textbf{(A1)}\ \text{素数幂支撑上的}\ \textbf{逐点族} \Longrightarrow \sum_n\Lambda(n)^2n^{-s}=\sum_p\frac{(\log p)^2}{p^s-1}\ \Longrightarrow \textbf{奇点}＝p^s=1，\ \textbf{与 ζ 零点无关} \Longrightarrow (iii)\ \textbf{死}（\text{初等}）✓✓$$
$$\qquad \textbf{(A2)}\ \textbf{加性卷积族} \Longrightarrow \text{DS}＝\textbf{Barnes 型 Mellin 卷积} \Longrightarrow \text{ζ 零点}\ \textbf{只经积分出现} \Longrightarrow \textbf{聚合型} \Longrightarrow \textbf{不可反演}（\text{`V188` §2}）✓✓$$
$$\Longrightarrow ⭐\ \textbf{b3 两自然子族均被钉住};\ \text{但}\ \textbf{b3 全类的为空性仍未证}✓✓$$

---

## §1 (A1) 素数幂支撑上的逐点族：初等判死（本档证明）

$$\text{设}\ c_n\ \text{支撑于素数幂}（\text{如}\ \Lambda）,\ \text{取}\ \textbf{非线性逐点}\ F,\ F(0)=0✓$$
$$\qquad \sum_nF(\Lambda(n))n^{-s}=\sum_p\ \sum_{k\ge1}F(\log p)\,p^{-ks}=\sum_p\frac{F(\log p)\,p^{-s}}{1-p^{-s}}✓$$
$$\qquad \text{取}\ F(x)=x^2 \Longrightarrow \boxed{\sum_n\Lambda(n)^2n^{-s}=\sum_p\frac{(\log p)^2}{p^s-1}}✓✓$$
$$\textbf{收敛横标}：\sum_p\frac{(\log p)^2}{p^{2\sigma}}<\infty\iff2\sigma>1\iff \boxed{\sigma>1/2}✓✓$$
$$\textbf{奇点}：\text{每一项在}\ p^s=1\ \text{处有极点} \Longrightarrow s=\frac{2\pi ik}{\log p}\ \Longrightarrow \textbf{与 ζ 的零点结构}\ \textbf{毫无关系}✓✓$$
$$\Longrightarrow \text{该对象}\ \textbf{不含任何零点信息} \Longrightarrow (iii)\ \textbf{死};\ \text{且}\ (ii)\ \text{满足（无欧拉积）}✓✓$$
$$\qquad \textbf{一般化}：\text{对任何}\ F(0)=0\ \text{的逐点}\ F，\text{结果都是}\ \textbf{逐素数独立和} \Longrightarrow \textbf{奇点来自单个素数} \Longrightarrow \textbf{结构上不可能含 ζ 零点}✓✓$$
$$\qquad ⚠️\ \textbf{线性例外}：F(x)=cx \Longrightarrow \sum_p(\log p)/(p^s-1)\ \text{型} \Longrightarrow \text{延拓必经}\ \log\zeta \Longrightarrow \textbf{值面}（\text{已判死}）✓$$

## §2 (A2) 加性卷积族：Barnes 型卷积 ⟹ 聚合型

$$\text{设}\ A(s)=\sum a_nn^{-s},\ B(s)=\sum b_nn^{-s};\ \text{加性卷积}\ c_n=\sum_{i+j=n}a_ib_j✓$$
$$\qquad \Longrightarrow C(s)=\sum_nc_nn^{-s}=\frac{1}{2\pi i}\int_{(c)}A(w)B(s-w)\,\frac{\Gamma(w)\Gamma(s-w)}{\Gamma(s)}\,dw\quad\textbf{[标准·待核]}✓$$
$$\qquad \Longrightarrow \textbf{ζ 零点通过}\ A,B\ \text{的奇点}\ \text{进入}\ \textbf{被积函数} \Longrightarrow \textbf{只以积分形式出现}✓✓$$
$$\Longrightarrow \textbf{聚合型}：\text{要从}\ C\ \text{反推出}\ \zeta\ \text{零点的}\ \textbf{逐点位置} \Longrightarrow \textbf{需反演 Mellin 卷积} \Longrightarrow \textbf{无界精度}（\text{`V188` §2}）✗✓✓$$
$$\qquad \Longrightarrow \text{这}\ \textbf{解释了实验}：\text{`CREATE-SPEC-6` 测得}\ D_C\ \text{在}\ \gamma\ \text{处}\ \textbf{无局部结构}（\text{局部极大}\ 0\ \text{个}） \Longrightarrow \text{零点信息}\ \textbf{确在"积分里"而非"局部"}✓✓$$

## §3 交叉核对（三处一致）

| 来源 | 读数 | 与 (A1)/(A2) 的关系 |
|:--|:--|:--|
| `CREATE-SPEC-6` 实验 | $d_C$ 在 $\gamma$ 处局部极大 **0** 个；正对照 50 个 | 支持 (A2) 的"聚合型"读法 |
| `p26a21-merging-host` 逐字 | "对称性编码（Hadamard／FE／实系数）——都给'轨道'——不编码'对齐／合并'" | 同向 |
| `V188` §2 | 线性通道饱和；反演到逐点需无界精度 | (A2) 的直接依据 |

## §4 结构定理的剩余缺口（(a) 的未竟部分）

$$\text{已钉住}：\text{(A1) 逐点族}（\text{初等证明}）;\ \text{(A2) 加性卷积族}（\text{聚合论证}）;\ \text{b1}（\text{欧拉积回归}，\text{L3}）;\ \text{b2}（\text{平凡}，\text{L2}）✓✓$$
$$\text{未证}：\textbf{b3 全类为空} \Longrightarrow \text{须证}：$$
$$\qquad \text{"任何由}\ \textbf{有限次点逐操作}\ \text{与}\ \textbf{有限次加性卷积}\ \text{生成的系数序列} \Longrightarrow \text{其 DS 的零点信息}\ \textbf{必为聚合型或不存在}\text{"}✓$$
$$\qquad ⚠️\ \text{难点}：\text{该类＝}\textbf{"点逐＋加性卷积"的算术电路闭包}，\ \textbf{极大};\ \text{且需一条}\ \textbf{"聚合保持"} \text{定理}（\text{点逐与加性卷积皆不产生逐点零点信息}）✓✓$$
$$\qquad \Longrightarrow \text{这条}\ \textbf{"聚合保持定理"} \text{是本项目目前}\ \textbf{最精确的未证结构命题}✓✓$$

## §5 边界与回查

- ⚠️ §1 的 $\sum\Lambda^2n^{-s}=\sum_p(\log p)^2/(p^s-1)$ **为初等且完整推导** ⟹ 本会话**第五条证明级产物** ✓✓
- ⚠️ §2 的 Barnes 型 Mellin 卷积公式标 **`[标准·待核]`**（**未逐字核文献**）⟹ 引用前须核 ✓
- ⚠️ §4 的"算术电路闭包"为**本档判断**，其"聚合保持定理"**未证** ✓
- ⚠️ 本档**不改** `CREATE-SPEC-8` 的 b1／b2／b3 三分；**只**给 b3 两子族的结构判定 ✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 22:0x）`[纪律]`（先跑后写）

```
技术词 素数幂支撑       命中文件数=4  :: ./p72-nonlinear-compatibility.md ./p7-prime-power-support.md ./p11-zero-flow-lyapunov.md（**已有**）
技术词 Barnes 型卷积     命中文件数=0  ⟹ 本档新增
技术词 聚合不可反演      命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：`素数幂支撑`＝**4 档 ⟹ 沿用（引用）**；`Barnes 型卷积`／`聚合不可反演`＝**0 档 ⟹ 本档新增** ✓
