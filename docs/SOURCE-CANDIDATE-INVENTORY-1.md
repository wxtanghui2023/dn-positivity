已查地图：命中（`E-20`／`E-22`／`E-23`／`E-24`／`AMEND-5/6/7/8`／`P1-α` 本线既有档）⟹ **引用，不开新案** ✓

# **`SOURCE` 候选盘点 · 第 1 轮**（只写 `SOURCE CARD`，**不计算** ✓；`COMPUTATION = LOCKED` ✓）

**依据**：`RESEARCH-CONSTITUTION` §8.1-AMEND-8 ✓ —— 盘点 = 求交：$$\text{已有数学问题}\cap\text{天然 }\zeta/L\text{ 接口}\cap\text{可计算}\cap\text{存在可预声明 }S4$$
**纪律**：⛔ 不跑 `CAS`／不扩大 `N,k,T`／不猜机制；每个候选只写五行卡；**零号 STOP**＝若写不出"若出现 `X` 则被迫引入 `F`（`F` 定义域不依赖本实验）"，则该候选**连计算阶段都不进** ✓

D0: 本档对象 = **`SOURCE` 候选盘点第 1 轮（4 候选，仅卡片，零计算）**（引本线自档；**未开 bridge 案** ✓）
D1: 0 （`[REVIEW]` 轮次：来源盘点为**搜索状态**登记，不主张新自由度 ✓）
FREEZE-ACK: D1=0 ✓
[REVIEW]

---

## 候选 1 —— **移位除数和（additive divisor problem）**

```
SOURCE:            Σ_{n≤x} d(n)d(n+h)（固定 h 族）——独立的经典算术问题（上界指数长期开放）
S1:                脱离 RH 后它本身是"算术平均/相关和的指数问题"，有独立文献与独立开放问题 ✓
S2:                已有接口：与 ζ 的零点/局部因子结构通过 Dirichlet 级数 ∑d(n)n^{-s}=ζ(s)^2 天然相连 ✓（非人工）
S3:                第一笔输入＝整数 h 与 x；输出＝Σ_{n≤x}d(n)d(n+h) 及其**精确**有限结构（整数/有理）✓ 不需 β/rank/support/parity/majorant ✓
S4-PRE:            **若**同一 h 族的精确值序列在**第二尺度**上出现"非拟合而来的"精确递推或因子化（如 A_{x'}=F(A_x) 且 F 不含 x 依赖），**则**被迫引入对象 F＝"该族的精确结构算子"（定义域＝所有 h 族，不依赖本次 x 取值）✓
S4-ANTI-POST-HOC:  <计算后填写，不得改写 S4-PRE>
STOP:              若所得只是 ① 有限差分/滑动窗口的标度（CAS 型）② 双表示截断缺陷（B-1 型）③ 算术↔零点表示的对应（C 型）④ ζ(s)^2 的已知 Euler–Dirichlet 结构 ⟹ **立即 CLOSED** ✓
```

## 候选 2 —— **最小二次非剩余序列（least quadratic non-residue mod p）**

```
SOURCE:            n(p) := min{n : (n|p) = −1} 的序列结构——独立经典问题（Burgess/Vinogradov 一线，仍开放）
S1:                脱离 RH 后是"符号序列 + 极值分布"问题，有独立数学生命 ✓
S2:                已有接口：Dirichlet L(s,χ_p) 与二次域类数/零分布天然相连 ✓
S3:                输入＝素数 p；输出＝n(p) 及**整数**结构（区间计数、差分的整值性）✓ 不用旧墙坐标 ✓
S4-PRE:            **若**{n(p)} 的**第二组素数尺度**上出现"非拟合"的精确因子化或消失（例：某固定组合在 2 个独立子族上同时精确为 0），**则**被迫引入对象 F＝"非剩余极值的精确代数量"（定义域＝全体素数，不依赖所取范围）✓
S4-ANTI-POST-HOC:  <计算后填写>
STOP:              若只是 ① Chebotarev/局部可容许性账本（`S6` lock）② 已知 L-函数零点账本 ③ CAS/B/C 同型 ⟹ **立即 CLOSED** ✓
```

## 候选 3 —— **虚二次域类数 h(−d)（class number formula 一线）**

```
SOURCE:            h(−d)（d>0 无平方因子）——独立经典问题（Gauss 类数问题，长期开放）
S1:                脱离 RH 后是"类数分布/极值"问题，独立数学生命 ✓（Gauss、Heilbronn、Goldfeld–Gross–Zagier 一线）
S2:                已有接口：**解析类数公式** h(−d) ↔ L(1,χ_{−d}) ↔ ζ/L 的零点与局部因子 ✓（经典、非人工）
S3:                输入＝d；输出＝h(−d) 与类群不变量（整数矩阵的精确 rank/det 等）✓ 不用旧墙坐标 ✓
S4-PRE:            **若**{h(−d)} 与其类群不变量在**第二尺度**上出现"非拟合"的精确乘法因子化（如 h(−d)=R·S 且 R、S 各自有独立定义域且非已知公式给出），**则**被迫引入对象 F＝"类数因子的新不变量"（定义域＝全体判别式）✓
S4-ANTI-POST-HOC:  <计算后填写>
STOP:              若只是 ① 解析类数公式本身 ② Euler–Dirichlet 乘积 ③ Siegel 零/零点统计账本 ④ CAS/B/C 同型 ⟹ **立即 CLOSED** ✓
```

## 候选 4 —— **模形式系数 a_p（固定权/水平，Hecke 特征值序列）**

```
SOURCE:            {a_p} 的精确整数结构——独立经典问题（Sato–Tate、Galois 表示、同余性质一线）
S1:                脱离 RH 后是"整数序列的乘性/同余结构"问题 ✓
S2:                已有接口：a_p 就是 L(s,f) 的 Euler 因子系数，与 ζ/L 结构天然相连 ✓
S3:                输入＝p 与形式 f；输出＝a_p 及**整数**结构（消失、整值递推）✓ 不用旧墙坐标 ✓
S4-PRE:            **若**在**第二组模形式/第二尺度**上出现"非拟合"的精确结构（如某组合恒为 0 且不能用 Hecke 关系解释），**则**被迫引入对象 F＝"跨形式的精确系数不变量"（定义域＝形式空间，不依赖所取 p 范围）✓
S4-ANTI-POST-HOC:  <计算后填写>
STOP:              若只是 ① Hecke 关系/乘性（成熟账本）② Ramanujan 猜想/同余的已知结果 ③ CAS/B/C 同型 ⟹ **立即 CLOSED** ✓
```

---

## §X **本轮盘点判定（零号 STOP 逐条核 ✓）**

```
【通过零号 STOP（可写出"若 X 则被迫引入 F"）】 4/4 均**能**写出该句 ⟹ 均**有资格**进入"待写完整 `SOURCE CARD` 并申请 `S1–S4/STOP` 审核" ✓
【⚠️ 但按 `AMEND-7`】**`SOURCE` 先验资格 ≠ 候选机制资格** ⟹ 4/4 **尚未**获得计算资格；`COMPUTATION` 仍 **LOCKED** ✓
【未进入本轮的候选（已排除或已属既有线）】 `CAS`/`B`/`C` 的任何变体 ✗｜`P1-α` 素数竞赛（**本仓既有资产线** ⟹ 不重复登记 ✓）｜Gauss 和型加性×乘性交叉（`CROSS-0` 已 DEAD ✓）｜`J-1…J-4`（`JAM` 已 ARCHIVED ✓）
【统计】 新登记候选 **4**；其中**尚无**一份完整 `SOURCE CARD` 通过 `S1–S4/STOP` 审核 ⟹ $$\boxed{\text{NO ADMITTED NEW SOURCE YET}}$$ ✓
【⛔ 本轮不做】 未计算／未命名机制／未接 RH／未宣布任何"新"结构 ✓
```

**状态**：`D/B/C`＝CLOSED｜`JAM`＝ARCHIVED｜`D_new`＝0｜RH target＝OPEN｜**SOURCE search＝ACTIVE**｜**COMPUTATION＝LOCKED**｜`S4`＝primary gate｜`STOP`＝predeclared ✓

---

## §Y 【技术词回查】（`scripts/tech_word_check.sh`，**先跑后写** ✓；逐字粘贴 ✓）

```
技术词 SOURCE 候选盘点 命中文件数=0    :: 
技术词 零号 STOP      命中文件数=3    :: ./ASSETS-REGISTRY.md ./SOURCE-CANDIDATE-INVENTORY-1.md ./RESEARCH-CONSTITUTION.md 
技术词 先验资格     命中文件数=5    :: ./C112-W4-1d-three-gate-audit-C2-first-zero-cost-kill.md ./ASSETS-REGISTRY.md ./SOURCE-CANDIDATE-INVENTORY-1.md 
技术词 discovery-source 命中文件数=1    :: ./RESEARCH-CONSTITUTION.md 
```
【三分类标注】 `0` ⟹ **本档新增**；`>0` ⟹ **档案已有（引用，不列为提出）** ✓
【说明】 本档为**来源盘点（搜索状态登记）**，**不含新数学主张** ✓
