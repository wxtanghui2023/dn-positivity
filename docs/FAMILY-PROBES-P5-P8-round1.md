已查地图：命中（`TOPIC-INVENTORY-v2-asset-driven-research-space`）⟹ 执行其 §7 四族探针，不开新案
D0: 本档对象 = **`P5`/`P6`/`P7` 探针结果**（`P8` 未做）：`P5` 三个具体候选 ＋ `P6`/`P7` 空手及原因 ＋ 竞争景观更新
D1: 0 （[REVIEW] 轮次：检索与筛选，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **四族探针 round 1**

## §1 ⭐ `P5` 命中三个具体候选

```
**【P5-a｜混合 additive／multiplicative Sidon 子集指数】**（`B` 族正中）
　`P`：确定混合二分法的**指数 `\alpha`** —— 任给有限 `A\subset\mathbb R`，是否必有 `\alpha>0` 使 `\max\{t^+(A),t^*(A)\}\gg|A|^{\alpha}`，**且 `\alpha` 的最优值是多少** ✓
　`K`（逐字）：**`\max\{t^+(A),t^*(A)\}\gg|A|^{5/8}`**（`Roche\text{–}Newton–Warren, Theorem 3.5`）✓；**反侧构造**：存在 `A`，其 additive 与 multiplicative Sidon 子集**都不超过 `|A|^{3/4}`**（`\varepsilon<1/4` 时原猜想为假）✓ ⟹ $$5/8\le\alpha\le3/4$$ ✓✓
　`G`：**`\alpha` 的真值未知**；且 `Roche–Newton` 原话："it also still remains to see whether there exists `\alpha>0`" ✓（`逐字`）
　`A`：`B`（容量/能量：`t^\pm`、`E^\pm` 都是我们把玩过的对象）✓ —— **但**：主战工具是**能量不等式/概率论证**，`D`（exact）**不直接对口** ⚠️
　`N`：**一个新指数**（`\alpha`）或**新的构造上界** ✓（量变明确）　`O`：sum-product 族、Sidon 族、能量方法 ✓
　**裁定：`G3`✓ `G4`✓ `G1`✓；`G2` ⚠️（`B` 对口但 `D` 不力）⟹ 候选，须找"可有限认证的切片"** ⚠️

**【P5-b｜`|A^2+A^2|` 下界（"平方之和"混合问题）】**
　`P`：证明 $$|A^2+A^2|=|\{x^2+y^2:x,y\in A\}|\ \ge\ c_\varepsilon|A|^{2-\varepsilon}$$ ✓（平方 = 乘法结构；求和 = 加法结构 ⟹ **`P5` 正统**）✓
　`K`（逐字）：当前最好为 **`|A^2+A^2|\ge|A|(\log|A|)^{c\log\log|A|}`**（`Schoen 2011`，用 `Freiman` 定理界）✓
　`G`：与猜想差**幂次级别** ✓✓ ⟹ 缺口巨大且明确 ✓
　`A`：`B`（乘法结构 + 加法求和）✓；`D` ✗ ⚠️　`N`：新指数 ✓　`O`：sum-product、二次剩余、圆法 ✓
　**裁定：缺口巨大 ⟹ 但同样属主流加性组合，我方 `D/E` 不对口** ⚠️

**【P5-c｜Sidon 数二阶项的 Erdős `\$500` 问题】**
　`P`：`F_1(n)`（`[n]` 中最大 Sidon 集）的**二阶项是否有界** ✓
　`K`（逐字）："it is still an open problem (originally valued at `\$500` by Erdős) whether the **lower order term is bounded or not**" ✓
　`G`：二阶项有界性未知 ✓　`A`：`B`；`D`（有限 `n` 的精确 `F_1(n)` 表可作**边界证据**，但**不能定二阶项**）⚠️　`N`：定二阶项 ✓
　**裁定：候选（须核精确陈述）** ⚠️
```

## §2 `P6`／`P7` 空手（含原因）

```
**【`P6` 空手】** 直接检索"最小反例/机制失效"未得**具体公开目标**；反而命中一个**关键景观信息**：
$$\text{Xena Project (2026-07-20): "Human mathematicians are being outcounterexampled"}$$ ✓ —— **AI 已在批量产出反例**（例：`Jacobian` 猜想 3 维反例，百年问题）✓✓
$$\Longrightarrow\ \textbf{纯"反例搜寻"已被 AI 主导}\ \Longrightarrow\ \textbf{`P6` 必须落在"机制层"（输出 failure mechanism）才可能有壁垒}$$ ✓✓（**与您对 `P6` 的定义正好吻合，但这也意味着 `P6` 的门槛更高**）⚠️

**【`P7` 空手（检索式不对）】** 用"阈值/临界值"检索命中的是**随机结构阈值**（satisfiability 阈值 `k=3` 仍开）与复杂度下界，**不是**"已有定理 `\mathcal C_k\Rightarrow P` 在何处失效"型 ✓
$$\Longrightarrow\ \textbf{`P7` 需要换检索式}:\ \text{按领域搜"theorem proved for }k\le n\text{, open/false for }k=n+1\text{"型表述}$$ ✓✓
【`P8`】**本轮未做** ✓
```

## §3 竞争景观更新（重要，影响选题）

```
**【逐字/档级】** `NYT (2026-09-08)`：**OpenAI 称已解决一个"千禧年问题"** ✓；`OpenAI (2026)` 另有 **cycle double cover 猜想证明** 与 **平面点集单位距离** 两份证明 ✓（档级）
**【arXiv:2605.22763】** 大规模评测：**353 个开放 Erdős 问题解决 9 个**；**492 个 OEIS 猜想证明 44 个** ✓（档级）
$$\Longrightarrow\ \textbf{结论}:\ \text{"著名问题 ＋ 计数/搜索型"}\ \textbf{不要碰};\ \text{我方位置仍是\textbf{机制层}}$$ ✓✓
```

## §4 `P5` 的诚实评估（本档新增）

```
**【问题】** `P5-a`／`P5-b`／`P5-c` **全部**落在**主流加性组合**，主战工具是**能量不等式/概率论证/解析方法** ⟹ $$\textbf{我方 }D\ \text{(exact 枚举＋证书) \textbf{不直接对口}},\ E\ \text{亦不对口}$$ ⚠️
**【⟹ 两种处置】**
　**(甲)** 只取 `P5` 中**可有限认证的切片**（如"给定小 `|A|` 的最大混合 Sidon 子集的精确值表"）⟹ 退回 `P2` 形态，价值下降 ⚠️
　**(乙)** 承认 `P5` 的**主流切片我们打不动**，改为寻找 `P5` 的**"混合约束 + 有限结构"交叉处**（例：**有限域上同时受加法与乘法禁配的极值问题**，那里 `A`（有限结构）＋`D` 可用）✓✓
⟹ **本档建议取 (乙)**：把 `P5` 的重心从"实数的能量不等式"移到 **`\mathbb F_q` 上的混合约束极值**（我方 `A+D` 才真正进场）✓✓
```

## §5 下一步（单点）

```
**(1)** 核 `P5-c` 的精确陈述（Erdős `\$500` 问题）✓
**(2)** 按 **(乙)** 检索：**`\mathbb F_q` 上混合 additive/multiplicative 禁配的极值问题**（找具体公开缺口）✓✓
**(3)** `P7` **换检索式**重打（"定理在 `k` 处失效"型）✓
【⛔ 纪律】 本轮**未计算、未实现**；`U_{2,3}` 暂停；`T-1` 仍为 calibration ✓
【边界】 §1 三候选的 `K` 栏含**逐字**片段（`RICAM rep21-19`、`Schoen 2011` 转述、`Wötzel` 引文）；§3 含**档级** ✓

## §附 【技术词回查】（补录）
```
技术词 mixed constraint 命中文件数=0    :: 
技术词 additive energy  命中文件数=12   :: ./CROSS-0-additive-multiplicative-cross-invariant-MAP-CHECK.md ./E20-E40-zero-density-2026-read.md ./C305-FSD-blind-spot-audit-program-four-classes-dual-ledger-five-rounds.md 
```
