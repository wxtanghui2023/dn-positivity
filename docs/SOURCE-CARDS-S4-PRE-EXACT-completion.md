已查地图：命中（`E-25`／`AMEND-6/7/8` 本线自档）⟹ **引用，不开新案** ✓

# **`S4-PRE-EXACT` 补全**（四张卡；**零计算** ✓；`COMPUTATION` 仍 **LOCKED** ✓）

**唐先生令（2026-09-23 13:56）**：⛔ **表述更正** —— 4/4 通过的是「**可以预先定义 `S4` 检验**」的**格式门槛**：
　$$\boxed{\text{4/4 通过了「可以预先定义 }S4\text{ 检验」的格式门槛}}$$ ⛔ **不是**"4/4 已证明存在新对象生成机制"（后者须等实际计算之后）✓
　**并暴露下一道门**：四张卡的 `S4-PRE` 共同弱点是"**精确递推／因子化／跨形式结构**"这个候选对象族**偏宽** ⟹ 若不钉死，计算后极易走
　$$\text{发现规律}\to\text{选一个合适的 }F\to\text{宣布 forced object}$$ ⟹ **重开 `AMEND-7` 明禁的 post-hoc 路径** ⟹ 故**下一步仍不能计算** ✓
　**要求**：各卡加一道 `S4-PRE-EXACT`，在跑第一笔数据前写清 $$\boxed{X\Longrightarrow F\in\mathcal F_{\rm pre}}$$，`\mathcal F_{\rm pre}` **必须提前固定，不得计算后扩张** ✓；
　须预先规定四件事：**(1)** 对象形式（如 `F:\mathcal X\to\mathcal X`）｜**(2)** 判据有限性（第一层/第二层各满足哪些**精确**等式/递推）｜**(3)** **排除已有结构清单**（Euler 积、Hecke、Chebotarev、类数公式、已知卷积恒等式）｜**(4)** **第二尺度的固定对应关系** ✓✓

D0: 本档对象 = **四张 `SOURCE` 卡的 `S4-PRE-EXACT` 补全与可采性判定**（引本线自档；**未开 bridge 案** ✓）
D1: 0 （`[REVIEW]` 轮次：门槛补全，不主张新自由度 ✓）
FREEZE-ACK: D1=0 ✓
[REVIEW]

---

## §1 **统一钉死模板（`\mathcal T_{\rm pin}`；四卡共用同一形态，内容各异 ✓）**

```
【对象形式（预固定 ✓）】 $$\mathcal X:=\{\,A_h(X_i)\,\}_{h\le H_0,\ i\in\{1,2\}}\quad\text{（整数阵列）};\qquad F:=R_J\ \text{＝"阶}\le J_0\ \text{的整系数线性递推算子"}$$ ✓
【判据有限性（预固定 ✓✓）】 $$\textbf{第一层：}\ \exists (c_0,\dots,c_J)\neq 0,\ c_J=1,\ J\le J_0:\ \sum_{j=0}^{J}c_jA_{h+j}(X_1)=0\quad \forall h\le H_0-J$$；
　$$\textbf{第二层：}\ \textbf{同一组系数}\ (c_j)\ \text{在}\ X_2\ \text{上亦成立}$$（⛔ **禁止每尺度各拟合一组系数** ⟹ 此即 anti-post-hoc 条件 (2) 的机械形式 ✓✓）
【第二尺度固定（预固定 ✓）】 `X_1=10^6`、`X_2=10^7`（**事前写死**，⛔ 不得事后选 ✗）✓
【排除清单（事前列出 ✓）】 ① Euler 积/局部因子（含奇异级数 `\mathfrak S(h)`）② Hecke 关系 ③ Chebotarev/局部可容许性 ④ 类数公式/属理论 ⑤ 已知卷积恒等式 ⑥ 有限差分标度（`CAS` 型）⑦ 双表示截断缺陷（`B` 型）⑧ 算术↔零点对应（`C` 型）✓
【命中语义】 **命中** ⟹ `F` **被迫出现**（因系数跨两尺度同一、且形式与阶数事前限定）✓；**未命中** ⟹ **决定性负结果**（该族不存在此阶数的精确结构）✓
```

## §2 **四卡逐条（钉死结果 ＋ 可采性判定 ✓）**

```
【卡 1 · 移位除数和 `A_h(X)=\sum_{n\le X}d(n)d(n+h)`】
　钉死：`\mathcal X`＝`h\le H_0=40`、`X\in\{10^6,10^7\}` 的**整数**阵列（`d(n)d(n+h)` 整数 ⟹ 和整数 ✓）；`F=R_J`，`J_0=4` ✓
　排除：奇异级数 `\mathfrak S(h)` 的**乘性**解释（若 `(c_j)` 由 `\mathfrak S` 决定 ⟹ CLOSED）｜`d=1\star1` 已知卷积｜⑥⑦⑧ ✓
　判定：$$\boxed{\text{S4-EXACT 可采 ✓}}$$｜**诚实先验**：`\mathfrak S(h)` 乘性 ⟹ 低阶线性递推**很可能不存在** ⟹ 预期为**决定性负结果**（若存在则是强对象 ✓）
【卡 2 · 最小二次非剩余 `n(p)`】
　钉死：`\mathcal X`＝`n(p)` 在**预固定子族** `p\equiv1\ (4)` 与 `p\equiv3\ (4)` 上的**经验计数向量** `v\in\mathbb Z^{K}`（`K=20` 事前固定）✓；`F=R_J`，`J_0=3` ✓
　排除：Chebotarev／`S6` 局部可容许性｜`L(s,\chi_p)` 零点账本｜⑥⑦⑧ ✓
　判定：$$\boxed{\text{S4-EXACT 可采 ✓}}$$（子族与向量维度事前固定，非事后选择 ✓）
【卡 3 · 虚二次类数 `h(-d)`】
　钉死：形式**可以**钉死（`\mathcal X`＝`h(-d)` 整数阵列；`F=R_J`）；⚠️ **但**排除清单**已包含答案**：属理论给出**精确**结构 `h=2^{t-1}\cdot(\text{奇部})`（`t`＝判别式素因子数），且解析类数公式锁定 `h\leftrightarrow L(1,\chi_{-d})` ⟹
　$$\boxed{\text{任何此类线性关系都会被"属理论＋类数公式"预先吸收} \Longrightarrow \text{S4-EXACT \textbf{不可采} ✗}}$$
　（**理由**：检验**在计算前就已注定**无法迫使**新**对象 ⟹ 属"预先吸收"，非"可能被迫出现" ✓）
【卡 4 · 模形式系数 `\{a_p\}`】
　钉死：`\mathcal X`＝两个**事前固定**的权/水平新形式 `f,g` 的 `\{(a_p(f),a_p(g))\}_{p\le P_0}`（`P_0` 事前固定）✓；`F=R_J`，`J_0=3`（**跨形式**同一组系数）✓
　排除：Hecke 关系（单形式内）｜Ramanujan 猜想/同余已知结果｜⑥⑦⑧ ✓
　判定：$$\boxed{\text{S4-EXACT 可采 ✓}}$$（若某组系数使 `\sum c_j a_{p_j}(f)=0` 与 `\sum c_j a_{p_j}(g)=0` 跨尺度同一成立 ⟹ 迫使**跨形式不变量** ✓）
```

## §3 **本轮账本（照录您给定格式 ✓✓）**

```
$$\boxed{\begin{aligned}&\text{SOURCE cards}=4,\\&\text{S4-format admissible}=4,\\&\text{S4-exactly admissible}=3,\\&\text{COMPUTATION}=\text{LOCKED},\\&D_{\rm new}=0.\end{aligned}}$$
【说明】 卡 1／2／4 可采（`\mathcal F_{\rm pre}` 已钉死）；卡 3 **不可采**（属理论＋类数公式**预先吸收**）⟹ 按 `AMEND-8`，**可采 ≠ 已跑**；`COMPUTATION` 仍 **LOCKED** ✓
【⭐ 价值（照录）】 `AMEND-8` **没有把门槛放松**，而是成功把"**有想法的候选**"与"**值得消耗计算预算的候选**"再次分开 ✓✓
【下一步（供裁，⛔ 不代跑）】 从卡 1／2／4 中选一张，进入 `RUN`（首笔最小计算）；我建议 **卡 1**（最经典、`\zeta` 接口最直接、首笔计算可行：`h\le40`、`X=10^6` 与 `10^7` 的精确整数阵列）✓
```

**状态**：`D/B/C`＝CLOSED｜`JAM`＝ARCHIVED｜`D_new`＝0｜RH target＝OPEN｜SOURCE search＝ACTIVE｜**COMPUTATION＝LOCKED**｜`S4`＝primary gate｜`STOP`＝predeclared ✓

---

## §4 **卡 1 的 `RUN` 前三项补钉（照录唐先生令 2026-09-23 13:58 ✓✓）**

```
【必须补的原因】 "`\mathcal X` 是 `h\le40` 的整数阵列"**不足以唯一确定** `R_J` 作用于哪个离散坐标（沿 `h`？沿 `X` 的两个尺度？两者同时？）⟹
　$$\boxed{R_J\ \text{到底沿哪个离散坐标作用？}}$$ —— **必须在计算前固定** ✓
【① 作用坐标（照录用 ✓✓）】 $$\boxed{(R_JX)_h=\sum_{j=0}^{J}c_jX_{h+j},\qquad c_j\in\mathbb Z,\quad J\le4}$$ ✓
【② 数据与双尺度（照录）】 $$X^{(1)}_h=\sum_{n\le10^6}d(n)d(n+h),\qquad X^{(2)}_h=\sum_{n\le10^7}d(n)d(n+h),\qquad 0\le h\le40$$ ✓
　要求**同一组** `(c_0,\dots,c_J)` 同时满足 $$R_JX^{(1)}=0\quad\text{和}\quad R_JX^{(2)}=0$$ ✓
【③ 归一化（本档钉死 ✓）】 **首一归一化**：`c_J=1`（消除整体倍数自由度）✓；`c_j\in\mathbb Z` ⟹ 解集是 `\mathbb Z`-格 ✓
【④ 有限枚举规则（照录精神 ＋ 本档机械实现 ✓✓）】 ⛔ **不是**"先找某个共同系数族再测试"；✅ **先规定搜索空间 `J\le4,\ c_j\in\mathbb Z`，然后完整确定该空间中全部合法归一化解**：
　$$\text{解空间}=\{\,c\in\mathbb Z^{J+1}:\ \begin{pmatrix}H_1\\H_2\end{pmatrix}c=0\,\},\qquad H_i=(\text{Hankel}(X^{(i)})),\ i=1,2$$
　**实现＝精确有理零空间**（有限、完备、非抽样）：对堆叠系统取 `\mathbb Q` 上零空间 ⟹ 再查整性与 `c_J=1` 归一 ⟹ 报告维数与全部解 ✓
　（若坚持有界枚举：**事前固定** `|c_j|\le B`，`B=40`；与零空间法等价，且零空间法更完备 ✓）
【⑤ 解释纪律（照录 ✓✓）】 若结果为**无 `R_J`**，结论**只能**是：
　$$\boxed{\text{在 }h\le40,\ X\in\{10^6,10^7\},\ J\le4\ \text{的预设实验域内，没有发现共同低阶整系数递推}}$$ ✓
　⛔ **不能**写成"除数相关不存在递推结构" ✗；⛔ **更不能**因预期负结果而**提前归入 `CLOSED`** ✗ ✓
　若真得 $$R_JX^{(1)}=R_JX^{(2)}=0$$ ⟹ **才触发真正 `S4`**：$$\boxed{\text{共同精确递推}\Rightarrow\text{检查是否被 }\mathfrak S(h)\text{、已知卷积结构等吸收}}$$；
　**只有无法被事前列出的旧结构解释**，才进入 `FORCED OBJECT` 审核 ✓✓
【⑥ 卡 1 最终状态（照录 ✓✓）】 $$\boxed{\begin{array}{ll}S1&\checkmark\\S2&\checkmark\\S3&\checkmark\\S4\text{-PRE}&\checkmark\\S4\text{-EXACT}&\checkmark\（\text{作用方向已补钉}\）\\COMPUTATION&\textbf{LOCKED}\\RUN&\textbf{尚未授权}\end{array}}$$ ✓
【⑦ 纪律（照录）】 $$\boxed{\text{先钉死 }S4\text{，再跑第一笔；绝不先跑再解释}}$$ ✓；卡 3 已正确 `CLOSED`；卡 2／4 **暂不抢跑** ✓
```

---

## §5 **执行层边界错位修正（唐先生 2026-09-23 14:00 ✓✓；`RUN` 仍未授权）**

```
【⚠️ 错位（唐先生指出，本档确认 ✓）】 原写法 `(R_JX)_h=\sum_{j=0}^Jc_jX_{h+j}`，`h\le40,\ J\le4` ⟹ 当 `h=40,\ J=4` 需 **`X_{40},X_{41},X_{42},X_{43},X_{44}`**，
　而数据只声明到 `0\le h\le40` ⟹ **最后四个 `h` 的递推方程并不存在** ✗
【✅ 采用方案 A（照录并采纳 ✓✓）】 保持 `h\le40` 为**递推方程范围**，而把**数据范围扩展**为 $$\boxed{0\le h\le44}$$，
　于是对 $$h=0,\dots,40$$ **完整构造方程** ✓
　（语义不变：$$\boxed{\text{固定 }h\le40\text{ 的 }41\text{ 个目标位置}}$$；`h+J` 仅是**递推所需右侧数据**，**不改变测试对象** ✓✓）
【✅ 方程与堆叠（修正后）】 对每个 `J\in\{1,2,3,4\}`，`h\in\{0,\dots,40\}`：$$\sum_{j=0}^{J}c_jX^{(i)}_{h+j}=0\ (\,i=1,2\,)$$ ⟹ `M^{(i)}` 为 **41×(J+1)** 矩阵 ⟹ 堆叠 $$M=\begin{pmatrix}M^{(1)}\\M^{(2)}\end{pmatrix}$$ ✓
【⭐⭐ 最终判定口径修正（照录 ✓✓）】 必须报告 $$\boxed{\exists\,c\in\mathbb Z^{J+1}:\ Mc=0,\quad c_J=1}$$ ⛔ **而不是**仅报 $$\dim_{\mathbb Q}\ker M>0$$ ✓✓
　**理由（照录）**：有非零有理零空间**并不自动**意味着存在**首一整系数**递推 ✓
　**本档机械化（等价形式）**：`\exists c` ⟺ 存在有理零空间向量 `v` 使 `v_J\neq0` **且** `v/v_J\in\mathbb Z^{J+1}` ⟹ 逐 `J` 报告：`\dim\ker`、**是否存在首一整解**、以及**若存在则给出显式 `c`** ✓
【卡 1 状态（照录 ✓✓）】 $$\boxed{\begin{array}{c}S1\text{–}S4\text{-EXACT}=\checkmark\\\text{execution-boundary}=1\ \text{项待修正}\to\textbf{已修正}\\COMPUTATION=\textbf{LOCKED}\\RUN=\textbf{NOT YET AUTHORIZED}\end{array}}$$ ✓
【授权后首轮 `RUN-1` 的冻结范围（照录 ✓✓）】 $$X^{(1)},X^{(2)}\to M\to\ker_{\mathbb Q}M\to\text{首一整系数可行性}$$；
　⛔ **不增加 `J`、不增加尺度、不扩大 `h`、不改变 `S4`** —— 这才是一次真正**可审计**的 `RUN-1` ✓✓
```
