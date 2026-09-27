# T4-CHECK-2026-09-27 — T-4（SNIEP $n=5$ 完整刻画）source-first ⟹ **DROP**（资产—问题映射层面）

**已查地图：命中（**本档首先撞上我方自己的 M03 线** —— 该线已用我方资产跑过同一问题）**
所查：`docs/M03-P2-SNIEP-FINAL-STAGE-REPORT.md`（**该线终局** ✓✓）｜`docs/M03-3b-final-registration-and-residual-target.md`（(3b) 登记＋真残余靶区 ✓✓）｜`docs/M03-3a-proof-chain-alignment-and-sharpness.md`（2026 原文证明链对齐 ✓）｜`docs/M03-3b-power-sum-necessary-condition-extends-W.md`｜`docs/M03-3cA-JMP-interlacing-CLOSED-no-new-exclusion.md`｜`docs/TOPIC-DOSSIER-v1-six-columns-and-relations.md`（T-4 原定义）｜`docs/M1-FAMILY-CLOSURE-2026-09-27-…md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §8）
D0: 本档对象 ＝ **档案已有**条目 T-4（SNIEP $n=5$）＋ **档案已有** M03 线的**收口核验与出口判定**（重命名：否 ✗；新对象：无 ✗）
D1: 0（source＋前序线核验型，无新自由度 ✓）

**纪律** ✓：**零计算** ✗｜未写计算脚本 ✗｜**G-1…G-4 只登记、不改门** ✓（唐先生 21:20）

---

## §0 单一出口：**DROP**（四条依据 ✓ · 不预设 ADMIT）

$$\boxed{\textbf{T-4 ＝ DROP}}$$
1. **我方自己已经跑过这条线，且已判"新性失败"** ✗✗（**最硬**）：`M03-P2-SNIEP-FINAL-STAGE-REPORT.md` §0 逐字：
   > "**P2-SNIEP 分支：数学机制成功，独立新性失败** ⟹ 降级为「**已知 SNIEP 区域的独立局部机制复核资产**」"，且清单逐字：独立新性 **否**／SNIEP 新结果 **否**／RH 直接桥接 **否**；**Krawczyk 新性路线关闭** ✓✓
   ⟹ 再用 T1–T5 做 T-4 ＝ **同一资产生第二次跑同一问题** ⟹ 正是唐先生禁止的"**旧约束换参数**" ✗
2. **区域层已被实测为 FAIL** ✗：`(3b)` 登记逐字：**MECHANISM EXTENSION / NO REGION EXTENSION**；区域层 **FAIL（无新区域）**，$W_{\rm PS}\subseteq\{\text{JMP-已排除}\}\cup\{\text{Loewy-已排除}\}$ ✓
3. **同形赛跑（同族／同技术）** ✗：我方研究族被 **JMP 2017** 直接覆盖（逐字："其族**即**我方低迹条带 $S$；其 line 4 $\equiv$ 我方 $y=0$ 边界；其 Thm 1 $\equiv$ 我方 $u$-条件"）；我方点被 **Marijuán 2023**（$a\le\frac{\sqrt5-1}4\Rightarrow$ 恒可对称实现）与 **2026-05 WSU 学位论文**（充分区含 $1+4\lambda_2\lambda_5\ge0$）覆盖 ✓；最新 **Jin–Ke–Sui 2026-08** 用的**对角移位＋临界高迹边界＋加权五环**正是我方 `(3a)` 已对齐的**同一技术** ✓
4. **$n=5$ 数学上**仍**未收口**（如实标注 ✓）：`arXiv:2608.19435` 摘要逐字只声称 "*We present a **new impossibility region** for the $5\times5$ SNIEP … lies in the low-trace regime … has not been identified previously*" ⟹ **加区域，非完成** ✓
   ⟹ **重要区分**：**问题 open ≠ 我方对该问题仍有边际**。本档关闭的是**后者**（资产—问题映射），**不是**前者 ✗✓

---

## §1 P0｜对象指纹

$$\text{SNIEP}_{5}:\ \text{刻画 }\{\sigma\in\mathbb R^5:\ \exists A\in S_5(\mathbb R),\ A\ge0\ (\text{逐元}\ ),\ \operatorname{spec}(A)=\sigma\}\ ✓$$
- **等价／规约**（已入档 ✓）：迹归一 $\sum\lambda_i\ge0$；**研究族** $(1,t,t,-(q+\varepsilon),-(q+\varepsilon))$ ⟹ 即 **Loewy Example 3.2** 的两参数族 $(1,a,a,b,b)$（$a=t,\ b=-(q+\varepsilon)$）✓
- **不可混** ✗：① **RNIEP**（非对称，$n\le4$ 与 SNIEP 等价、$n\ge5$ 不同）；② **DNIEP**（可对角化非负）；③ **Soules 集 $S_5$** vs **可实现集 $R_5$**（$n=5$ 二者**性质不同** ⚠️ 不得互替）
- **当前精确 open instance（档案已钉 ✓）**：低迹条带内的**真残余靶区**
$$\Bigl\{\tfrac49<t<\tfrac{15}{31},\ 4t-2<\varepsilon<\varepsilon_2(t)\Bigr\},\qquad \varepsilon_2(t)=3t-2+\tfrac12\sqrt{5t^2-2t+1}\ ✓\ (\text{非空；}u>0,\ v>0\ \text{—— 不触碰任何既有墙})$$

---

## §2 P0.5｜后继引用链（追到 2026 ✓ · 逐字）

| 环节 | 内容 | 出处 |
|---|---|---|
| 族覆盖 | 研究族 $1,a,a,-(a+d),-(a+d)$ 已研究；Thm 1 ≡ 我方 $u$-条件 | **JMP 2017**, LAA **512**, 129–135 ✓ |
| 补充注记 | 5×5 非负对称谱的进一步注记（$n=5$ 为最低未决 $n$） | **Loewy 2021**, ELA **37**, pp.1–13（**原文已入档** `sources/Loewy-2021-…pdf` ✓） |
| 充分条件 | $a\le\frac{\sqrt5-1}4\Rightarrow$ 恒可对称实现（常对角） | **Marijuán 2023**, LAA ✓ |
| **2026 最新（不可能区域）** | "*new impossibility region … low-trace regime … diagonal shift → critical high-trace boundary → weighted five-cycle*" | **arXiv:2608.19435**（Jin–Ke–Sui, **2026-08-19**, 45 pp）✓✓ |
| 2026 学位论文 | $\sigma=(1,\lambda_2,\lambda_2,\lambda_5,\lambda_5)$ 族＋充分区（含 $1+4\lambda_2\lambda_5\ge0$） | **WSU thesis 2026-05** ✓ |
| 可实现侧（标题级 ⚠️） | *Symmetric Nonnegative 5×5 Matrices Realizing Previously Unknown Region* | 检索片段（**round-1** ⚠️） |
| 早期刻画 | 迹零 5×5 对称非负的刻画 | LAA **434(4)**, 1000–1017 (2011) ✓ |
**⟹ 读数**：该问题**活跃且拥挤**；且**我方族／我方点／我方技术**三者**均被覆盖** ✓✗

---

## §3 P0.75｜同形赛跑（逐项）

| 维度 | 判定 | 依据 |
|---|---|---|
| same parameter | 撞上 ✗ | 同一 SNIEP $n=5$ |
| same equivalence | 撞上 ✗ | 同一"可实现性／区域" |
| same family | 撞上 ✗✗ | **我方研究族 ＝ JMP 2017 的族**（逐字 ✓） |
| same technique／lineage | 撞上 ✗ | 对角移位＋五环技术（我方 `(3a)` 已与其对齐）；Loewy／Marijuán／Jin–Ke–Sui 同一文献簇 |
**⟹ 依规则：任一撞上即 DROP／HOLD，不进入计算** ✓

---

## §4 P1/P2｜新攻击点（**答不出** ⟹ DROP）

**唐先生必答**：rank／inertia／trace 资产能否给出**新约束**（而非"旧约束换参数"）？
| 攻击面 | 状态（档案已实测 ✓） | 依据 |
|---|---|---|
| 线性层 | **已关闭**（$K_{PM}\cap R=K_{Kellogg}\cap R=K_{Borobia}\cap R=\varnothing$） | M03 线 ✓ |
| Soules-1 | **已升级为解析定理（恒失败）** | M03 线 ✓ |
| Soules-2 | **UNDECIDED**（未决） | M03 线 ✓ |
| 幂和必要条件 | **机制扩张 ✓／区域扩张 ✗**（$W_{\rm PS}\subseteq$ 既有墙） | `(3b)` ✓ |
| JMP 交错 | **CLOSED，无新排除** | `M03-3cA` ✓ |
| Krawczyk | **新性路线关闭**（仅剩"独立复核"价值） | 终局报告 ✓ |
$$\Longrightarrow\ \textbf{全部可行攻击面均已被跑过，且无一产生新约束}\ \Longrightarrow\ \text{答不出}\ \Longrightarrow\ \textbf{DROP}\ ✓$$

---

## §5 P3｜deliverable（**无法预先说清** ⟹ 与 DROP 一致 ✓）

- 可能产物只有：① 对**已知区域**的复核／重现 ✗；② 对残余条带的**再参数化**（无新区域）✗ ⟹ **两项均为唐先生明确排除者** ✓
- **不足以**承诺：新普适必要条件／排除某参数区间／新的可实现族构造／新分类定理 ✓

---

## §6 保留与交棒（**关键：残余条带是登记项，不是目标** ✓）

$$\boxed{\text{保留登记：残余靶区 }\Bigl\{\tfrac49<t<\tfrac{15}{31},\ 4t-2<\varepsilon<\varepsilon_2(t)\Bigr\}\ \text{—— 但它\textbf{不是}当轮目标}}$$
**重开条件（照 `M1-FAMILY-CLOSURE` §2 同一口径 ✓）**：
1. 出现**新资产** $X$ 使该条带产生**新的排除/构造**（且非"旧约束换参数"）✓
2. 且该条带须有**正面 open 证据**（作者自述未覆盖／明确未做）—— **本轮未取到**，**不得**以"我未见表"充数 ✗（G-4）
**模式提示（供唐先生决策 ⚠️，非决定）**：M1 族四格 ＋ T-4 **均**在"资产—问题映射"层面关闭 ⟹ 池内剩余可查者主要是 **T-2**（$AG(7,3)$ 最大 cap）／**T-3**（疑似已解）／**T-8**（缺口未锁定）／**T-9**（已 REJECT）⟹ **池的"待筛密度"已很低** ⚠️

---

## §7 证据表（含 ID／URL ✓）

| # | 内容 | 出处 | 级别 |
|---|---|---|---|
| E1 | M03 线终局：机制成功／新性失败；独立新性 否；Krawczyk 关闭 | `docs/M03-P2-SNIEP-FINAL-STAGE-REPORT.md` ✓ | 档内 ✓ |
| E2 | (3b) ＝ MECHANISM EXTENSION／NO REGION EXTENSION；残余靶区 | `docs/M03-3b-final-registration-and-residual-target.md` ✓ | 档内 ✓ |
| E3 | 三处覆盖证据（JMP 2017／Marijuán 2023／WSU 2026-05） | 同上 E1 §2 ✓ | 档内（**摘要级** ⚠️） |
| E4 | 2026 原文：**新不可能区域**（低迹；移位＋临界高迹边界＋加权五环）；45 pp | **arXiv:2608.19435**（Jin–Ke–Sui, 2026-08-19）`arxiv.org/abs/2608.19435` ✓✓ | **逐字** ✓ |
| E5 | Loewy 2021 ELA 37；（我方 `(3a)` 已对齐其与 2026 文证明链） | `docs/M03-3a-…md` ＋ `sources/Loewy-2021-…pdf` ✓ | 档内 ✓ |
| E6 | Soules $S_5$ 与 $R_5$ 对 $n=5$ 性质不同 | 检索片段（academia）⚠️ | round-1 ⚠️ |

## §8 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "SNIEP"
技术词 SNIEP            命中文件数=17   :: ./S2-HANDOFF-zone-members-and-count-fix.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./T7-CHECK-2026-09-27-fingerprint-race-and-asset-isolation-DROP.md
$ bash scripts/tech_word_check.sh "residual target"
技术词 residual target  命中文件数=1    :: ./M03-3b-final-registration-and-residual-target.md
$ bash scripts/tech_word_check.sh "impossibility region"
技术词 impossibility region 命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`impossibility region` 命中 0 ⟹ 为**外部文献术语**（2026 原文），**引用**，不作新性主张 ✓）
- **档案已有（引用，不列为提出）**：`SNIEP`（17 档）｜`residual target`（1 档，M03 线）✓

## §9 诚实边界

- 本档为 **round-1 source 快照 ＋ 前序线核验**（未逐段重读 Jin–Ke–Sui 45 页；未跑 closure_gate）⟹ 结论**只到"该键在资产—问题映射层关闭"** ✓
- **未动算** ✓；不改门 ✓；**不写"SNIEP 方向已死／不存在"** ✗（V290）—— 措辞为"**$n=5$ 仍 open，但我方资产对该问题的边际已被实测为零（区域层 FAIL）**" ✓
- E3／E6 为**摘要级／round-1** ⚠️；如唐先生需要，下一步可只做"**残余条带 open 状态**"的单点取证（**不计算**）✓
