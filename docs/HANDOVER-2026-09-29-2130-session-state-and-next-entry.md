已查地图：未覆盖（关键词: 会话交接）—— 可开档，首行须照抄本行
D0: 本档对象 = 档案已有（V₂ 体系／三点 orbit／priv／BÖW-V_R）之**状态汇总**，非新数学
D1: 0

# 📦 HANDOVER 2026-09-29 21:30 —— 会话状态与下一入口

> 空间 B｜非 C 号｜唐先生令"先存档，开新会话"｜**不主张 107 可达**（V290）

## §0 四条工作约束（唐先生本轮明令，永久生效）

1. **不再把 BÖW 2004 原文获取作为方案**（论文不可得）
2. **不回退 103→105→106**（已完成资产）；**当前唯一缺口 = 106→107**
3. **不再把 SDP 当默认突破口**（2026 Gijswijt–Polak = NG-12）
4. 已有 K(10,1) 工作／NO-GO／$D_A$ 恒等式／P/Q 分解／106 推导 = **当前状态机**，不每轮重讲

## §1 目标（正名，三轮修正后）

$$\text{已知}\ 107\le K(10,1)\le 120\ (\text{别人成果});\quad \text{目标} = \textbf{改进任一端一格}$$
$$\text{下界侧}:\ K\ge L,\ L\in\{108..119\};\qquad \text{上界侧}:\ K\le 119\ (\text{构造})$$
$$\text{等价形式}:\ \Sigma\delta = 11M-1024 \ge cM,\quad c>1.34\Rightarrow107,\ c>1.52\Rightarrow108$$
$$\text{松弛天花板}\ c\le1.268\ (\text{SDP-3}=105.2223)\ \Longrightarrow\ \textbf{107 必须非松弛（整性/组合）}$$

## §2 本轮净成果（全部可核）

| # | 结果 | 文件/commit |
|---|---|---|
| A | **规则4 ROUTE-DEDUP GATE** 上线：pre-commit hook 比对已关闭路线指纹；双向实测（不申报→拒；申报→放行） | `docs/ROUTE-FINGERPRINTS.tsv`, `scripts/git-hooks/pre-commit` (37ea27f, 231e864) |
| B | **E1 恒等式核验**：$\sum_{x\in B(c)}(\mu(x)-1) = 2f(c)$，120/120 ✓；**E3**：$\sum\mu(\mu-1)=4N_{\le2}$（796=4·199）✓ | RESULT-29n (fa5553c) |
| C | **106→107 归约**：目标 ⟺ $N_{\le2}\ge 35.75\,\mu_{\max}$；**新推论：若 106-覆盖存在 ⟹ $\mu_{\max}\ge4$ 必成立** | RESULT-29n |
| D | **三点恒等式**：$\sum_x\binom{\mu(x)}3=\sum_{\{u,v,w\}}|B(u)\cap B(v)\cap B(w)|$（138=138）✓ | RESULT-29o (9dcd0e0) |
| E | **三点构型计数 (1,1,2)/(2,2,2) 独立于 V₂**（残差 12.83，相对 7.0%/3.2%） | RESULT-29o |
| F | **三点 orbit 族（13 型）独立于完整 μ 分布**（42 码/17 参数/自由度 25，13/13 独立） | RESULT-29p (4a813d3) |
| G | **rank 增量 = 13（满秩）**：$V_3\cap{\rm span}(V_2)=\{0\}$（33 码，17+13=30 列，合并秩 30） | 本轮实测 |
| H | **共点类（覆盖相关）t-子型 6/6 独立**（残差 18.2–46.2，相对 5.8–30%）⟹ 覆盖相关 V₃ **ALIVE** | 本轮实测 |
| I | **恒等式**：$X_{t\ge1}=\sum_{x\notin C}\binom{\mu}3+\sum_{x\in C}\binom{\mu-1}3$（比值 1.000；M=153 时 0.999）⟹ **总量**被 V₂ 决定 | 本轮实测 |
| J | **(2,3,3) 必无共球点**（含距离 3 对）⟹ 其独立性属"与覆盖无关"方向 | 纯逻辑 |
| K | **反向单调量定位**：8 个量中 **仅 priv/M 为逆单调**（r = −0.995）；其余（N₂/M、Σδ/M、max_nb2、X_tot/M、Xt/M、ΣC(μ,3)/M）皆**顺单调**（+0.8~+1.0） | 本轮实测 |
| L | **priv 路线被封**：目标等价 $|A|\ge143$，但 $|A|\le\Sigma\delta=142$ 是恒等式 ⟹ 不可达 ✗；唯一出口 = 逐码字 ${\rm priv}(c)$ 上界 | 本轮推导 |

## §3 本轮自伤记录（纪律）

- **欠定假象**：13 码 vs 19 参数 ⟹ 残差 0 是假象（两次）✗ ⟹ 硬规矩：**样本数必须 > 参数数**
- **单边线性探针是空的**：a=0,b=min 恒满足 ⟹ 松弛 0 无信息 ✗
- **$3X\le2A_2$ 界错误**：实测 3X/(2A₂) 达 2.579 ⟹ 撤回 ✗（错因：混淆球交 2 点与距离-2 球面交 16 点）
- **"覆盖相关层全部落回 V₂"判定错误**：只查了总量，未查 t-分布 ⟹ 撤回 ✗

## §4 结构性诊断（本轮最重要的一句）

$$\boxed{\text{覆盖码的 }V_3\ \text{统计量\emph{总量}几乎都随 }M\ \textbf{顺单调};\ \text{而排除 106 需要\ \textbf{小 }M\ \text{端}的约束}}$$
$$\therefore\ \text{要找的是\ \textbf{逆单调}（随 }M\ \text{减小而增大/不减）的量或非和式泛函（min/max 型）}$$

## §5 下一入口（按优先级）

1. **逐码字 priv(c) 上界**：${\rm priv}(c)\le 11-(\text{被他人覆盖数})$；找 c 的局部几何给出的上界，再求和
2. **min/max 型泛函**：$\min_c{\rm priv}(c)$、$\max_c{\rm priv}(c)$、$\min_c f(c)$ 等（已测 min_nb2 无显著相关 ⟹ 换定义再试）
3. **V_R 结构反推**：BÖW R=1 是"输出必须到 107"的未知机制指纹；用"必须给出 107"反解其参数族
4. **上界侧（独立于 107 机制）**：n=9 搜索校准到 62（现得 66，差 6.5%）→ 再攻 n=10 的 ≤119

## §6 【技术词回查】（实跑逐字）

```
技术词 三点orbit独立但顺单调 命中文件数=0    ::
技术词 priv逆单调 命中文件数=0    ::
技术词 反向单调量 命中文件数=0    ::
```
分类：本档新增 = 无；档案已有（引用）= V₂/A_d/n_j/orbit/priv/BÖW-V_R；通用词（不计）= 顺单调/逆单调。

ROUTE-CHECK: R02=NA R06=NA R07=NA R08=NA R16=NA R17=NA R18=DUPLICATE R19=DUPLICATE R20=DUPLICATE

---

## §7 新会话开案审查（2026-09-29 22:05，逐条查地图）【新增】

**规程**：照 `PROTOCOL-pre-work-map-check.md`；查 `CLOSED-ROUTES-MAP.md`／`MASTER-STATUS-AND-CLOSURES.md`／`MASTER-NOGO-AND-LIVE-PATHS.md`／`ASSETS-REGISTRY.md`／`ROUTE-FINGERPRINTS.tsv`。

| §5 入口 | 地图判定 | 既有依据（引用，非新案） |
|---|---|---|
| 1 逐码字 priv(c) 上界 | **不得开案 ✗** | R19（`BLOCKED-BY-\|A\|≤Σδ`）｜`AUDIT-2026-09-28c`：ownership/private-coverage 层＝covering 恒等式之重写 ⟹ 按令**已关** ✗｜`AUDIT-2026-09-29x`：private 点层**无强制 excess**（740/746 可零-excess 服务）＋**excess 密度逆势** ✗✗｜`RESULT-29n` §5 之 α3 ＝同内容 |
| 2 min/max 型泛函 | **未直接命中，须先越反例** ⚠️ | 无同名关闭条目；但 §2-K（8 量中 7 个顺单调）＋`AUDIT-2026-09-29x`（一切**强制型**论证逆势）⟹ min 型＝强制型 ⟹ **须先答「为何非强制型」** 再开 |
| 3 V_R 结构反推 | **触及禁区** ⚠️ | R09／R17（BÖW 正文不可得，唐先生明令）⟹ 反推**无地面真值可核验**，不得作为主路线 |
| 4a n=9 校准到 62（现 66，差 6.5%） | **干净可开案 ✓✓** | `ASSETS-REGISTRY` L1905：**上界侧 LIVE ✓✓**（C-427 战略更新）；无同名关闭条目 |
| 4b n=10 之 ≤119 | **命中 R14 ✗** | R14＝`LINE-ALREADY-ATTACKED`（`docs/119-ATTACK-R1-2026-09-27`） |

**审查结论**：§5 四条入口中，**仅 4a（上界侧 n=9 校准）为干净可开案项** ✓；第 1 条已被三层独立证据封闭（R19 ＋ 28c ＋ 29x）✗；第 4b 已有专案 ✗；第 2／3 条须先补前置理由（非强制型论证／可核验性）⚠️。

ROUTE-CHECK: R01=NA R02=NA R03=NA R04=NA R05=NA R06=NA R07=NA R08=NA R09=FINGERPRINT-CITED R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=NA R16=NA R17=FINGERPRINT-CITED R18=NA R19=FINGERPRINT-CITED R20=NA

---

## §7.1 溯源判定（唐先生 21:56 命：block 是 119 的 NO-GO，还是 107 的复现？）【新增】

$$\boxed{\text{判定}:\ \text{该 block ＝ \textbf{排除侧机制族 NO-GO}，其内容与 \textbf{107 下界线同一堵墙};\ 对 \textbf{119 目标的 NO-GO 不成立} ✗}}$$

**证据链（逐条可核）**：

1. `PLAN-119-GOAL-ASSETS-GAPS-AND-WORKFLOW.md` §3 诊断（**决定性**）：**目标在上界（构造）侧，而近期精力全在下界（排除）侧 ⟹ 资产/方法错配** ✗✓ ⟹ 119 目标 ＝ $\exists$ 9-cover $U$，${\mathcal L}_9(U)\le119$（**构造问题**）。
2. `K101-119-LINE-ARCHIVE-2026-09-26-OPEN-structurally-audited.md` §0（唐先生 09-26 21:26 裁定）：状态 ＝ **OPEN — structurally audited / current mechanisms NO-GO**；逐字「**不是** CLOSED ✗；**不是**『119 不存在』✗」；障碍 ＝ "缺一个真正改变 quantity 的**新不变量**"。
3. `MASTER-STATUS-AND-CLOSURES.md` §119-P1-CONSOLIDATION：**21 mechanisms CLOSED ⟶ irreducible core ＝ exact Boolean feasibility（整性）** —— 与 107 线「**须非松弛（整性/组合）论证**」**是同一句**。
4. `MASTER-FAILURE-MAP-107-LINE.md` §2 定理 A／B：两线**共享同一结构性墙**（Aut-不变松弛族天花板 ⟹ 107 必非松弛；目标等价 ＝ 覆盖问题本身）。
5. `ASSETS-REGISTRY.md` L3937：逐字「**107/120 复现＝仅学技术，非目标**」⟹ 复现 107 **从不是** 119 目标。
6. `ASSETS-REGISTRY.md` L1905：**上界侧（文献 120 → 119）：LIVE ✓✓**。

$$\therefore\ \text{存在的是\ \textbf{排除侧机制族 NO-GO}，而该族正是 107 下界线所用工具（局部 incidence 量／守恒律／松弛族）}\ \Longrightarrow\ \text{性质上属\ \textbf{「107 复现」侧}，}\ \textbf{不封锁 119 构造目标}\ ✓$$

**对 §7 的修正**：§5.4b 一行由「命中 R14 ✗」改为 ⟹「**构造侧 LIVE ✓✓；R14 之『已攻击』记录属排除侧**」。**建议**（**待唐先生定，不自裁 ✗**）：`ROUTE-FINGERPRINTS.tsv` 之 R14 判定字段由 `LINE-ALREADY-ATTACKED` 改为 `EXCL-SIDE-NOGO-构造侧LIVE`。

ROUTE-CHECK: R01=NA R02=NA R03=NA R04=NA R05=NA R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=NA R16=NA R17=NA R18=NA R19=NA R20=NA

---

## §0.1 优先级更正（唐先生 2026-09-29 22:21，**永久生效**）【新增】

> 唐先生原话：「**我们首先是复现 107，然后才能知道怎么去走 120→119 与 107→108**」

$$\boxed{\textbf{硬次序}:\ \text{① 复现 }107\ (\text{＝排除 }M{=}106)\ \Longrightarrow\ \text{② 才谈 }120{\to}119\ \text{与}\ 107{\to}108}$$
⟹ **两端改进暂缓** ✗；**§5.2（min/max 泛函）等 107 线上的子课题降为从属** ⚠️；
⟹ 理由（唐先生）：**不先掌握 107 是"怎么被做出来的"，两端的攻击设计无据** ✓✓

## §7.2 「复现 107」状态与主路径（查地图＋引既有档）【新增】

**A. 复现账（引 `AUDIT-2026-09-29f` §1，逐字）**

$$\text{可复现}:\ \text{上界 }120\ ✓\ (\text{证书在手}),\ \text{下界 }94\ ✓\ (\text{球界}),\ 103\ ✓\ (\text{van Wee excess 自推})$$
$$\text{不可复现}:\ 96,\ 97,\ 105,\ 107\ ✗$$
$$\textbf{读法}:\ \text{上界已握在手里；缺口全在\textbf{下界中段} }97\to105\to107$$

**B. 三条已死（引既有档，**不得重攻**）**

| 路线 | 判定 | 依据 |
|---|---|---|
| pair 层（任何形式） | **CLOSED-103** ✗ | `ROUTE-FINGERPRINTS` R02（三重独立失败，皆 103） |
| 高阶 SDP | **DEAD-BY-AUTHORS** ✗ | R15／`AUDIT-29d` |
| **单条**线性不等式 | **已证不可能** ✗✓ | `AUDIT-2026-09-29e`：任何单条给界 ≤ LP ≤ 105.2223 < 107 |

**C. 107 复现的**最锐等价形式**（＝本线主目标，与 `RESULT-29n` §3–§4 同）**

$$\boxed{\text{复现 }107\ \iff\ \textbf{排除 }M{=}106\ \iff\ \text{证}\ \Sigma\delta\ge143\ ({\rm iff}\ N_{\le2}\ge\tfrac{143}{4}\mu_{\max},\ \text{配}\ \mu_{\max}\ge4)}$$
$$\text{缺口} = \textbf{一格}:\ \text{现有 }N_{\le2}\ge142,\ \mu_{\max}{=}4\ \text{分支下差 }1$$

**D. 档案指定之下一步（`AUDIT-29d` ＋ `MASTER-FAILURE-MAP` §6 甲，**唯一未被封闭的组合路线**）**

$$\textbf{（甲）}\ \text{Zhang--Lo 1992 \textbf{三重覆盖}不等式之 }r{=}1\ \text{类比}\ \text{（原式未取 ⟹ 须\textbf{自推}）}$$
⟹ pair 层已封（R02）而**三重层未试** ⟹ 且**非单条 linear** ⟹ 与 29e 的不可能性**不冲突** ✓✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=NA R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA

---

## §7.3 ⚠️ 勘误：106→107 归约有 ×2 漏因子（2026-09-29 22:3x）【新增】

$$\boxed{\text{`RESULT-29n` §3 之 }N_{\le2}\ge\Sigma\delta\ \textbf{错};\ \text{正确为 }N_{\le2}\ge\tfrac12\Sigma\delta}$$
- **反向验证**：$n{=}9$ 62-码 $N_{\le2}{=}73<\Sigma\delta{=}108$ ✗；$n{=}10$ 120-码 $N_{\le2}{=}199<\Sigma\delta{=}296$ ✗ ⟹ **两个已知码双双违反** ✓✓
- **后果**：§2 净成果 (C) 之「$\mu_{\max}\ge4$ 推论」**作废** ✗；「一格缺口」应为 $\approx\mathbf{72}$（$N_{\le2}$ 单位）✗；§4「结构诊断」之前提须重估 ⚠️
- 详 `docs/ERRATUM-2026-09-29-n1-factor-two-in-the-106-107-reduction.md`
- **未受影响** ✓：复现 107 $\iff$ 排除 $M{=}106$｜恒等式 $E1/E2/E3$｜恒等式 $T$｜`AUDIT-29e` 之禁令
- **顺带有效新式** ✓：$P\le2A_2$
