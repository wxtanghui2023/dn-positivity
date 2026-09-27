# 119-ATTACK-R1-2026-09-27 — **P1 全局不变量普查（四方向）＋ 逐环节难点拆解 ＋ 杠杆判定**

> ⚠️ **空间隔离**：本档＝**空间 B 之 119 线（$K(10,1)$）**专用 ✓；**不引 RH 链** ✗（唐先生 21:32／21:35 令 ✓）。

**已查地图：命中（本线 P1 工作今日已成体系，本档为**接续式普查**，非重造 ✓✓）**
所查：`docs/P1-REAUDIT-2026-09-27-E-correction-and-the-mod-11-theorem.md`（**E 纠错＋模 11 定理** ✓✓）｜`docs/P1-2026-09-27-support-layer-screen-results.md`（**两 Gate 分级** ✓✓）｜`docs/P12-PASS-2026-09-27-bucket-divergence-with-identical-distance-distribution.md`（**P1-2 PASS** ✓✓✓）｜`docs/CHAIN-VW-2026-09-27-self-contained-b-le-2-and-full-corollaries.md`｜`docs/ALG-VW-2026-09-27-equality-reformulation-and-the-exact-gap.md`｜`docs/ALIGN-2026-09-25-our-delta-field-vs-WuChen-excess-surfeit.md`｜`docs/FOURIER-2026-09-26-convolution-reformulation-audit.md`｜`docs/DELSARTE-2026-09-26-krawtchouk-route-and-the-a1-bound.md`｜`docs/M1-2026-09-27-bqp-lift-verdict-and-the-p1-split.md`｜`docs/ODDENGINE-2026-09-26-…`｜`docs/HANDOFF-2026-09-27-119-line-session-handoff.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §10）
D0: 本档对象 ＝ 119 线**已有** P1 工作链的**四方向普查与难点拆解**（重命名：否 ✗；新对象：无 ✗）
D1: 0（普查／拆解型 ✓；**未动算** ✓；**未改门** ✓）

---

## §0 结论速览

$$\boxed{\text{四方向普查结果}:\ ①\ \text{恒等式（无独立杠杆）}\ \big|\ ②\ \textbf{ALIVE（新可区分维度已证）}\ \big|\ ③\ \text{线性内容＝整数性（无新条件）}\ \big|\ ④\ \textbf{被否证（}A_i\ \text{不足）}}$$
$$\boxed{\textbf{本线真正的资产}:\ \text{support（坐标支撑）层在}\textbf{全距离分布相同} \text{下仍可分叉}\ (J_7=64/128/256)\ ——\ \text{即"超出距离分布的新可区分维度"}\ ✓✓}$$
$$\boxed{\textbf{本线真正的难点}:\ \text{该杠杆只在}\ n=2^m\ \text{族（Theorem 13／Type B 结构）成立；}n=10\ \text{无 perfect-code 构造}\ \Longrightarrow\ \textbf{杠杆不直接迁移}\ ⚠️}$$

---

## §1 P0｜精确定义与**外部**现状（**逐字 ✓✓**）

$$\text{目标}:\ K(10,1)=\gamma(Q_{10});\quad \text{已知}:\ K(10,1)\le120\ (\text{构造});\ \textbf{下界远低};\ \text{target}:\ |C|\le119$$
**外部权威读数**（`arXiv:2203.16901`，Wu–Chen，Discrete Math **347**(2) 2024）逐字 ✓：
> "A dominating set on an $n$-dimensional hypercube is equivalent to a binary covering code of length $n$ and covering radius 1. **It is still an open problem to determine the domination number $\gamma(Q_n)$ for $n\ge10$ and $n\ne2^k,2^k-1$** ($k\in\mathbb N$). When $n$ is a multiple of 6, the best known lower bound is $\gamma(Q_n)\ge\frac{2^n}{n}$, given by **Van Wee (1988)**. In this article, we present a new method using **congruence properties due to Laurent Habsieger (1997)** and obtain an improved lower bound $\gamma(Q_n)\ge\frac{(n-2)2^n}{n^2-2n-2}$ **when $n$ is a multiple of 6**." ✓✓

$$\Longrightarrow\ \boxed{\text{P0 三条}:\ (i)\ n=10\ \text{属 open 集（}8<10<15\text{）}\ ✓;\ (ii)\ \text{van Wee 界 }2^n/n=102.4;\ (iii)\ \textbf{Wu–Chen 的改进只覆盖 }n\equiv0\bmod6\ ——\ n=10\equiv4\ \text{不在内}\ \text{⚠️(待 R2 核)}}$$
**对照**：van Wee **Corollary 1b** 逐字 $K(2^r,1)=2^{2^r-r}$（即 $n=2^m$ **格精确已知**；$n=8{:}32$ ✓）⟹ **$2^m$ 族无待证问题** ✓
**档案侧**：$n=10$ 最佳下界记 **107（BÖW 2004）** ⚠️（**档级**，R2 须重钉：与 $102.4$／$105.2$ 的来源须对齐 ✓）

---

## §2 图谱：**唐先生四方向 ↔ 档案已有工作 ↔ 结果**

| # | 唐先生方向 | 档案已有工作（**今日**） | 结果 |
|---|---|---|---|
| **①** | **全局 excess** | `P1-REAUDIT`（E 纠错 ＋ 模 11）｜`ALIGN`（δ-场 ↔ Wu–Chen excess/surfeit） | **恒等式** ⟹ 单用无杠杆；且**措辞须纠**（见 §3） |
| **②** | **excess × 局部几何（二阶/三阶）** | `P1`（support 层两 Gate）｜**`P12-PASS`（同桶 $J$ 分叉）** ｜`CHAIN-VW`（$J_1..J_7$） | **ALIVE** ✓✓ —— **新可区分维度已证**（§4） |
| **③** | **Fourier／association scheme** | `FOURIER`（卷积重述）｜`DELSARTE`（Krawtchouk，$A_1$ 界）｜**模 11 定理** | **线性内容＝整数性** ⟹ **无新必要条件** ✗（§5） |
| **④** | **距离分布 $A_i$** | `P12-PASS` 三见证码 | **被否证** ✗ —— $A$ **不足**，正确层＝坐标支撑（§6） |

---

## §3 方向①｜全局 excess —— 难点拆解

$$E:=\sum_x\delta(x)=\sum_x\big(b(x)-1\big)=11|C|-1024\ ✓;\qquad |C|=119\Longrightarrow E=285;\quad |C|=120\Longrightarrow E=296$$
$$\text{（档案 120-码实测 } \sum\delta=296\ \checkmark\ \text{—与 Wu–Chen 的 }(n+1)|D|-2^n\ \textbf{同一恒等式}✓）$$
| 环节 | 难点 | 状态 |
|---|---|---|
| **恒等式性** | $E$ 是 $|C|$ 的**纯函数**（与覆盖无关）⟹ 不能单独给排除 ⟹ 此前"$E\ge286\iff$ 119-码不存在"**用词错误** ✗✓ | **已纠**（`P1-REAUDIT` OA-1 ✓） |
| **充分路线** | 正确形态：**若从覆盖假设推出 $E\ge286$ ⟹ $|C|\ge120$ 与 $|C|=119$ 矛盾** ✓（**充分**，非等价 ✓） | 保留 ✓ |
| **δ-型泛函** | $\sum\delta$／$\sum b\delta=4(A_1{+}A_2)$／$\sum\delta^2=\cdots$ 等**全部**被 profile 恒等式钉住 ⟹ **只用 $b(x)$ 统计的论证不可能给出 $E\ge286$** ✗ | **已定**（`GAPTHEOREM`／`SUM-P1P4`／`LOCAL-AVG-GATE`）✓ |
**⟹ ①难点** ✓：**excess 的量是"恒等式级"信息** ⟹ **必须与"跨中心/支撑"信息耦合**，否则零杠杆 ✓（→ 方向②）

---

## §4 方向②｜excess × 局部几何（**唯一 ALIVE** ✓✓）—— **逐环拆解**

**②-a support 层恒等式（已核 ✓）**
$$\sum_{i<j}m_{ij}^2=\sum_{c,c'}\binom{|S(c)\cap S(c')|}2\ \text{（含对角）}✓;\qquad \text{对角}=\sum_c\binom{|S(c)|}2=J_1✓$$
$$S(c)=\{i:c\oplus e_i\in C\}\ \big|\ d_1(c)=|S(c)|\ \big|\ m_{ij}=\#\{c:i,j\in S(c)\}\ \big|\ q_{ij}=\#\{\{c,c\oplus e_i\oplus e_j\}\subseteq C\}✓$$

**②-b 两 Gate（已分级 ✓）**
| Gate | 判据 | 结果 |
|---|---|---|
| **P1-1 分离性** | 候选量在两码上**须不同** | **全过 ✓**（8/8） |
| **P1-2 非约化** | 升级为：$\exists C_i,C_j$ 使 $(A_1,A_2)$ **相同**而 $J$ **不同** | **PASS ✓✓**（见 ②-c） |

**②-c ★P1-2 PASS（决定性 ✓✓）**
$$\text{存在三个\textbf{两两不等价}的最优 }(8,32)_1\ \text{码}:\ (A_1,A_2)=(0,16)\ \textbf{相同},\ \textbf{全距离分布亦相同}\ A=(0,16,160,176,64,48,32,0),\ \text{而}\ J_7=64/128/256✓✓$$
$$\Longrightarrow\ \boxed{\text{距离分布}\ \textbf{不}决定 support-2 fingerprint} \Longrightarrow \textbf{"collapse 假设"被否证}✓✓\ \text{（}n=8\ \text{Theorem-13 域内）}$$
**机制透明化 ✓**：分叉载体＝**Type B**（$k=0$，两半为**不交**完美码）；其距离-2 对必为跨半对 $\Longrightarrow$ 全部 $q_{ij}$ 只落在 $\{i,7\}$ 型坐标对 $\Longrightarrow J_7=\sum_{i=0}^6q_{i7}^2$（16 的一个分拆的平方和）⟹ $64=4^2\!\cdot\!4$、$128=8^2\!\cdot\!2$、$256=16^2$ **全解释 ✓✓**
$$\Longrightarrow\ \boxed{\text{分离\textbf{只在坐标支撑层}} \Longrightarrow\ \textbf{这正是全场要找的"新可区分维度"}\ ✓✓}$$

**②-d 难点（本方向唯一的硬点 ⚠️）**
$$n=8\ \text{杠杆依赖两件事}:\ (i)\ n=2^m;\ (ii)\ \text{Theorem 13（两半＝长 }2^r-1\ \text{的\textbf{完美码}}）$$
$$n=10:\ 9=2^t-1\Longrightarrow2^t=10\ \text{非 2 的幂} \Longrightarrow \textbf{长 9 的完美码不存在} \Longrightarrow \textbf{无 Theorem-13 型构造} \Longrightarrow \boxed{\text{杠杆不直接迁移}} ⚠️$$

---

## §5 方向③｜Fourier／association scheme —— 难点拆解（**已闭合** ✓）

$$T=I+\sum_{i=1}^{10}\sigma_i\ \text{（覆盖算子）被 Walsh 基对角化，特征值 }11-2w\ (w=0..10)✓;\quad 11-2w\equiv-2w\ (\bmod 11)$$
$$\Longrightarrow\ \boxed{\ker(T\bmod 11)=\mathrm{span}\{\mathbf 1\}}✓✓\quad(1024\equiv1\bmod11\ \Longrightarrow\ \text{Walsh 基在 }F_{11}\ \text{可逆}✓)$$
$$\Longrightarrow\ \text{推广}:\ Tg\equiv0\ (\bmod 11)\iff g\ \text{各分量同余}✓;\quad g:=11T^{-1}\delta=11f-\mathbf 1\in\{-1,10\}^{1024}✓$$
$$\Longrightarrow\ \boxed{\textbf{结论}:\ g\text{-形的\textbf{线性内容}恰是\textbf{整数性}（}=Tf\ge1,\ \textstyle\sum f=119\text{ 的整数松弛），\textbf{非线性内容}＝二值性（Booleanity）}}\ ✗\ \text{无新必要条件}$$
**另：BQP 提升亦循环** ✗ —— 精确提升下 $y_{uv}\le x_v\iff x_v(x_u-1)\le0\iff x_u\le1$ ⟹ **等于直接加 Booleanity** ✓（`M1-bqp-lift` ✓）
$$\Longrightarrow\ \boxed{\text{③ 无杠杆}:\ \text{线性/谱路线的内容已被分离干净 = 整数性 + 二值性 = 原问题}}✓$$

---

## §6 方向④｜距离分布 $A_i$ —— 已被否证（**负结果，价值高** ✓）

$$③④\ \text{合读}:\ \text{距离分布 }A_i\ \textbf{不}决定 support 层；而 $\delta$-型泛函（含 }\sum b\delta=4(A_1{+}A_2)\text{）\textbf{只}看 }A_i$$
$$\Longrightarrow\ \boxed{\text{凡"只用 }A_i\text{"的论证\textbf{必然}无法区分 ②-c 的三见证码} \Longrightarrow \textbf{方向④单独不足}}✗✓$$
$$\text{正确坐标}:\ \textbf{坐标支撑层}（S(c),\ m_{ij},\ q_{ij},J\text{-族}）✓$$

---

## §7 结构性难点：**为什么 $n=10$ 缺杠杆**（本档核心拆解 ✓✓）

$$\boxed{n=2^m\ \text{族}}:\ \text{van Wee 等号}\ \Longrightarrow\ b\le2\ \text{（}b\in\{1,2\}\forall x\text{）}\ \Longrightarrow\ \text{matching}\ (d_1(c)\le1)\ \wedge\ J_3=J_6=0\ \wedge\ A_1{+}A_2=M/2\ \wedge\ \textbf{二部结构}✓✓$$
$$\qquad\text{且 Theorem 13 给出**显式构造域**（Type A/B/C 由 }C_1\cap C_2\ \text{定}✓)\ \Longrightarrow\ \text{可分叉 → 可当**反例发生器**}\ ✓✓$$
$$\boxed{n=10\ \text{（非 }2^m\text{）}}:\ \textbf{三条工具全不可用}:\ (i)\ \text{van Wee 等号不适用};\ (ii)\ \text{完美码构造不存在};\ (iii)\ \text{故无"n=8 式"的反例发生器}⚠️$$
$$\qquad\Longrightarrow\ \text{剩下的只是**一般覆盖码**（无结构族）}\ \Longrightarrow\ \text{这正是 }n=10\ \text{P1 的**真实难度位置**}\ ✓✓$$
$$\text{（另有独立难点 ✓）}\ \delta\text{-型/层重分配不变量}\ \textbf{无切割力}\ \text{（`ALIGN`：我方"局部守恒律"＝Wu–Chen excess 恒等式的层重分配 ⟹ 非独立不变量 ✗）}$$

---

## §8 杠杆判定（**诚实** ✓）

$$\boxed{\text{现行 T-资产包 }+\ \text{四方向}\ \Longrightarrow\ \textbf{未产生作用于任意 119/120-cover 的、带 P1 杠杆的全局不变量}}$$
| 方向 | 杠杆 |
|---|---|
| ① 全局 excess | **无**（恒等式；需外部信息）✗ |
| ② excess×局部几何 | **有，但仅 $n=2^m$**（$n=8$ 已证；$n=10$ 不迁移）⚠️ |
| ③ Fourier/谱 | **无**（内容＝整数性＋Booleanity）✗ |
| ④ 距离分布 | **无**（被否证）✗ |
**⚠️ 措辞纪律** ✓：**"未产生"≠"不存在"** ✗（V290）；**"未找到"≠"无杠杆"** —— 本档只陈述"**在已普查的四族内未获杠杆**" ✓

---

## §9 R2 攻击点候选（**不计算** ✓；每条须走 P0→P0.5→单出口）

| # | 攻击点 | 为何可能 | 须先核（G-4 ✓） |
|---|---|---|---|
| **R2-1** | **同余路线在 $n\equiv4\bmod6$（含 $n=10$）的情形** | Wu–Chen 用 Habsieger 同余**只做了 $n\equiv0\bmod6$** ⟹ $n=10$ 可能未覆盖 ⚠️ | 是否已有工作覆盖 $n\equiv4$；须**正面 open 证据**，不得以"未见表"充数 ✗ |
| **R2-2** | **$n=10$ 的"支撑层分叉"存在性**：能否**构造性**给出两个 $(A_1,A_2)$ 相同而 $J$ 不同的 $10$ 维码 | 复用 ②-c 的机制（改载体：无完美码 ⟹ 试其它对称族）⚠️ | 需**理论构造**（禁大规模计算 ✓）；若不可能 ⟹ 本身即"$A$ 决定 $J$"的新定理 ✓ |
| **R2-3** | **$n=10$ 的 $b\le2$ 极限情形**（$|C|=120$ 时 $E=296$） | 120-码**已知存在** ⟹ 其 $b$-profile 可作**对照锚**（是否 $b\le2$？） | 只做**读文献/读已知码**层面（不算）✓ |
| **R2-4** | **van Wee 证明内部等号分析**的 $n=10$ 类比 | `ALG-VW` 已定位：$b\le2$ 的难点在"(i) 非码字点不被三重覆盖"，且**不能**由计数恒等式推出（有反例构造 ✓）⟹ 唯一取法是**进 vW 证明内部** | 该内部机制对偶数（非 6 倍数）$n$ 是否可用 ⚠️ |

---

## §10 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "support 层"
技术词 support 层      命中文件数=5    :: ./P12-PASS-2026-09-27-bucket-divergence-with-identical-distance-distribution.md ./P1-2026-09-27-support-layer-screen-results.md ./YIP-2026-09-27-full-pool-and-the-vacuity-correction.md
$ bash scripts/tech_word_check.sh "分离性"
技术词 分离性          命中文件数=17   :: ./C3899h-T1-closure-and-gamma13-M1-seven-wall-screening.md ./lemma3-hostile-audit.md ./arp2-framework.md
$ bash scripts/tech_word_check.sh "非约化"
技术词 非约化          命中文件数=1    :: ./NOGO-QUOTIENT-N1-N7.md
$ bash scripts/tech_word_check.sh "模 11"
技术词 模 11           命中文件数=6    :: ./ASSETS-REGISTRY.md ./grh-migration-probe.md ./C238-B2-1-theorem-audit-two-patches-and-c1-preview.md
$ bash scripts/tech_word_check.sh "集中度"
技术词 集中度          命中文件数=8    :: ./CHAIN-VW-2026-09-27-self-contained-b-le-2-and-full-corollaries.md ./P12-PASS-2026-09-27-bucket-divergence-with-identical-distance-distribution.md ./ASSETS-REGISTRY.md
$ bash scripts/tech_word_check.sh "Booleanity"
技术词 Booleanity      命中文件数=16   :: ./M1-2026-09-27-bqp-lift-verdict-and-the-p1-split.md ./FOURIER-2026-09-26-convolution-reformulation-audit.md ./ASSETS-REGISTRY.md
```
- **本档新增**：**0** 个术语 ✓（六词**全部**为 119 线既有档内用语 ⟹ **纯普查／拆解**，无新性主张 ✓✓）
- **档案已有（引用，不列为提出）**：`support 层`（5）｜`分离性`（17）｜`非约化`（1）｜`模 11`（6）｜`集中度`（8）｜`Booleanity`（16）✓

## §11 边界（硬 ✓）

- **未动算** ✓（唐先生"第一阶段禁止大规模计算" ✓）；**未改门** ✓；**不跨空间** ✓
- 不写"不可能／不存在／无杠杆"作为终局判断 ✗（V290）—— 只写"**在已普查四族内未获杠杆**" ✓
- R2 四条**均为候选**，**不得**预设 open／ADMIT ✓（G-4：须正面证据 ✓）
- `/tmp/cov`（covering-**design** 搜索器）与 code 搜索**严格分账** ✗


---

## §12 ⚠️ 更新（2026-09-27 21:42 唐先生修正）

$$\boxed{R2\!-\!1\ \textbf{DROP}\ |\ R2\!-\!2\ \textbf{ALIVE}\ |\ R2\!-\!3\ \textbf{HOLD}\ |\ R2\!-\!4\ \textbf{PRIORITY（已由 P1-5 执行）}}$$
- **R2-1 理由翻转 ✓✓**：**不是**"$n=10$ 未被同余路线覆盖"，而是**恰恰相反** —— **Habsieger 原文（FPSAC 95）明确研究 $n\equiv2,4\bmod6$**，$n=10$ 给 $K(10,1)\ge104$，Zhang 提高至 $105$（远低于 119）⟹ **该路线已处理过且缺口巨大** ⟹ **DROP** ✓
- **R2-4 ＝ PRIORITY 并已执行**：见 `docs/P1-5-2026-09-27-van-Wee-proof-decomposition-at-n10-and-R2-1-DROP.md`（**A 型输出：未消耗自由度＝坐标支撑层，且可证其在 van Wee／Habsieger 体系内不可见** ✓✓；条件挂在 R2-2 ✓）


## §13 ⚠️ 更新（2026-09-27 21:45 唐先生令：只做 R2-2）

$$\boxed{\text{R2-2 必行结论}:\ \textbf{分支①「发现 10D 分离」成立 ✓（构造性）}:\ A\not\Rightarrow J\ \text{在}\ n=10\ \text{成立}}$$
- **构造 ✓**：$C=C_1\times\mathbb F_2^2$ 与 $C'=C_2\times\mathbb F_2^2$（$C_1,C_2$ ＝ P12-PASS 的 $n=8$ 见证）⟹ 均为 $\mathbb F_2^{10}$ 半径 1 覆盖码、$|C|=128$、$A(C)=A(C')$、support 指纹不同 ✓✓（**提升引理**，3 行可自证 ✓）
- **但（本档第二产出）**：**自由坐标引理** ⟹ $|C|\le123$ 的 $\mathbb F_2^{10}$ 覆盖码**不可分**（由 $K(9,1)=62$）⟹ 上述分离**必然**落在 $|C|=128$ 的可分族，**与 P1 相关范围（119–120）不相交** ⚠️
- ⟹ **下一刀收紧为 R2-2′**：**近最优范围（$|C|\le123$，无自由坐标）内的分离**；门②（$J$ 进覆盖条件）**须建立在门①之上**，否则空转 ⚠️
- 档：`docs/R2-2-2026-09-27-n10-support-layer-separation-constructible-and-free-coordinate-lemma.md`（**零计算** ✓）
