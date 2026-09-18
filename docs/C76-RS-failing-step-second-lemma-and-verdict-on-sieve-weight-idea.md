已查地图 + **外取原文**（所查：`A3-break-682-attempt.md`、`A3-third-moment-barrier.md`、`V185` §1／§3、`V186` §5、`C74`／`C75`（本会话前档）、`external_refs/`（**RS 原文不在本地** ✗，Duke 付费墙）；**外取**：`arXiv:2002.00595v1`（RS 证明的**讲解型**论文，含 `Second Lemma` 与 `Theorem 2` 逐字）、`arXiv:2603.28104`（Goldston–Suriajaya，**由唐先生核实并引用**）、`arXiv:2501.14545`（`BGSTB25` v3 摘要）、`arXiv:2503.15449`（`GLSS25`）、`aimath.org/~kaur/publications/58.pdf`（RS 高阶相关的转述））。**结论**：RS 范围 `X^k ≤ T^{2−ε}` 的**硬边来自一条"消失引理"**——`Second Lemma`：**若 `Σ|ξ_j| < (2−δ)/m` 则 `A_{r,s}=0` 除非 `n₁n₂⋯n_{r+s} ≪ T^{2−δ}`** ⟹ **"support > 1" 与"素数幂乘积超过 `T²`"是同一件事** ✓✓

# C-76 · **取到 RS 的失效步骤**：`Second Lemma`（消失引理）＋ 对"筛权重"设想的判定

> **时间**：2026-09-18 12:33 唐先生：① 更正我方措辞（"未被走过"→**它就是那堵众所周知的墙**）；② 要求取 **Rudnick–Sarnak 里 `k=3` 卡在 `X ≤ T^{2/3−ε}` 的具体失效步骤**原文
> **本档**：取回该步骤（**二手讲解源** ⚠️）＋ 对齐我们的 `T²` 结构 ＋ 对"更精细筛权重／Heath-Brown 式"设想的判定 ✓

---

## §0 ⚠️ 接受更正（先行）

$$\text{`C-75` §0 我写"}\textbf{1.04 档未被走过}\text{"}\ \Longrightarrow\ \textbf{措辞误导};\ \textbf{更正为}：$$
$$\boxed{\text{它不是被忽视的缝隙，而是}\ \textbf{那堵众所周知的墙}（\text{Montgomery 1973 起、几十年卡在同一处}）}✓$$
$$\qquad \text{我方贡献}\ \textbf{仅是精确化}：\text{把"缺 prime-pair candidate"变成"}\textbf{缺无条件三阶矩，且}\ \eta\ge0.04\ \textbf{就够}\text{"};\ \textbf{不改变难度评级}✓✓$$

---

## §1 **失效的那一步**（逐字取回；源＝`arXiv:2002.00595v1`）

$$\textbf{Second Lemma}：\text{"It says that if}\ \Phi\ \text{is supported in}\ |\xi_1+\ldots+\xi_n|\le\frac{2-\delta}{m}\ \text{then}\ A_{r,s}(n,T)=0\ \text{\textbf{unless}}\ |n_j|\ll T\ \text{and}\ \boxed{n_1n_2\ldots n_{r+s}\ll T^{2-\delta}}"$$
$$\textbf{Theorem 2}：\text{"Let}\ \Phi\in C^1\ \text{be supported in}\ \sum_{j=1}^n|\xi_j|<\frac 2m,\ \text{and let}\ f(x)=\int\Phi(\xi)\delta(\xi_1+\cdots+\xi_n)e(-x\xi)d\xi.\ \text{Then for}\ h_j\ \text{as in (2) we have…}"$$
$$\qquad \text{证明机制（该源）：由积分表示，若}\ \sum_j\eta_j=0\ \text{且}\ \eta\in\operatorname{Supp}\Phi，\ \text{则}\ |T(\eta_jL\pm\log n_j)|\ll1\ \Longrightarrow\ \text{乘积被}\ \textbf{支撑} \text{条件卡住}✓$$

$$\Longrightarrow\ \textbf{关键等价（本档读出的核心）}：\qquad \text{support}\ \sum_j|\xi_j|<\tfrac2m\ \Longleftrightarrow\ \text{素数幂乘积}\ n_1\cdots n_{r+s}\ll T^{2-\delta}\ ✓✓$$
$$\qquad k\ \text{个素数幂各}\ \asymp X\ \Longrightarrow\ X^k\le T^{2-\delta}\ \Longleftrightarrow\ X\le T^{(2-\delta)/k}\ \Longrightarrow\ \boxed{k=3:\ X\le T^{2/3-\varepsilon}}\ \text{（与前沿 §7.2(e) 逐字吻合）}✓✓$$

## §2 为什么这解释了 `η ≥ 0.04` 的门槛

$$\text{把 support 从}\ 1\ \text{推到}\ 1+\eta\ \Longleftrightarrow\ \text{允许}\ n_1\cdots n_{r+s}\ \textbf{超过}\ T^2\ \text{（哪怕只超}\ T^{0.08}）✓$$
$$\qquad \Longrightarrow\ \text{离开消失引理的适用区} \Longrightarrow\ \text{剩下的相＝}\textbf{素数幂之间的乘性关系} \Longrightarrow\ \text{即}\ \textbf{Hardy--Littlewood 型（prime-pair／triple）输入}✓✓$$
$$\text{（}k=2\ \text{情形正是我们的}\ \texttt{Problem A}：n_1n_2\ll T^{2-\delta}\iff X\le T^{1-\delta/2}（\text{Montgomery 无条件}）；\ \text{推到}\ X\le T^{1+\eta}\ \text{即离开该引理}）✓✓$$
$$\Longrightarrow\ \boxed{\text{"support}>1\text{"、}\text{"无条件三阶矩"、}\text{"乘积超过 }T^2\text{"、}\text{"prime-pair 输入"}\quad \textbf{四者是同一件事}}\ ✓✓✓$$

## §3 对"更精细的筛法权重／Heath-Brown 式处理"的判定

$$\text{结构上：消失引理是}\ \textbf{恒等式型} \text{命题（由显式公式＋}\operatorname{Supp}\Phi\ \text{推出）};\ \text{改}\ \textbf{权重} \text{改的是}\ \textbf{检验函数}，\ \textbf{不改变乘积界}\ n_1\cdots n_{r+s}\ll T^{2-\delta}✗$$
$$\qquad \Longrightarrow\ \text{单靠权重精细化}\ \textbf{不能} \text{越过这个边界};\ \text{权重只能在同一范围内榨常数}（\text{这正是}\ 0.6725\to0.682\ \text{所做的}）✓$$
$$\text{且我方档案已有两条独立证据指向同一结论}：$$
$$\qquad \textbf{(i)}\ \texttt{V254}\text{／}\texttt{V255}\ \text{parity barrier（局部权重的信息上限）};\quad \textbf{(ii)}\ \texttt{V255-5b}\ \textbf{型判据}：\text{系数侧}\to\text{零侧}\ \textbf{必须造转换}，\ \text{单型}\ \textbf{不可能}✓$$
$$\qquad ⚠️\ \text{但不排除}\ \textbf{换机制}：\text{若用}\ \text{large sieve／decoupling} \text{替换 MV 的某一步}，\ \text{改变的是}\ \textbf{估计方法} \text{而非}\ \textbf{支撑条件} \Longrightarrow\ \text{仍受同一乘积界限制}（\text{待核}）⚠️$$

## §4 三个**可抠的具体点**（建议按此顺序）

$$\textbf{(1)}\ ⭐\ \text{`Problem A` 的}\ \texttt{SQ1}：\text{MV 对该核是否}\ \textbf{sharp}？\ \text{即真实算子范数}\ \sup|O_1|/(\sum n|a_n|^2)\ \text{是否}\ \ll L^2X\cdot T^{-c} \Longrightarrow\ \text{若否，障碍是}\ \textbf{ℓ² 方法伪影} \text{而非硬墙}✓✓$$
$$\textbf{(2)}\ \text{`Problem A` 的}\ \texttt{SQ3}：\Lambda\ \text{vs}\ \mu^2\ \text{判别实验}\ \Longrightarrow\ \text{障碍在"素数提取"还是"双体双线性结构"}✓$$
$$\textbf{(3)}\ \text{指数}\ \textbf{2}\ \text{的来源审计}：\text{`}T^{2-\delta}\text{` 中的 2}\ \text{是否可换来源}（\text{k 阶矩的 }L^2\text{ 结构／large sieve／diagonal 结构}）\ \Longrightarrow\ \text{这是"能否在同一支撑下换估计"的技术问}✓$$

## §5 出处与可信度（⚠️ 必读）

| 源 | 性质 | 可信度 |
|:--|:--|:--|
| `arXiv:2002.00595v1` | RS 证明的**讲解／重写**（含 `Second Lemma`／`Theorem 2` 逐字）| ⚠️ **二手**（且其英文有拼写错误，如"supproted"）⟹ **引用前须与 Duke 原文核对** |
| **Rudnick–Sarnak 1996**（Duke **81**(2) 269–322；DOI `10.1215/S0012-7094-96-08115-6`）| **一手** | ✗ **本地无副本**（付费墙）；`external_refs/` 内亦无 |
| `arXiv:2603.28104`（Goldston–Suriajaya，*Zeta Zeros in a Narrow Vertical Box*）| 唐先生**已核实**并引用（`b=b(T)→0` ⟹ ≥2/3；`b=0.3185` 逐字对得上）| ✓ 由唐先生核 |
| `arXiv:2501.14545`（`BGSTB25` v3）／`arXiv:2503.15449`（`GLSS25`）| 摘要／转述 | `[外搜／未读全文]` ⚠️ |

$$\Longrightarrow\ \textbf{下一步文献动作}：\text{设法取得 Duke 原文（或 Hejhal 1994 IMRN）以}\ \textbf{逐字确认} \text{ `Second Lemma` 的原始编号与陈述}⚠️$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 12:4x）`[纪律]`

```
技术词 消失引理     命中文件数=1    :: ./C76-RS-failing-step-second-lemma-and-verdict-on-sieve-weight-idea.md
技术词 四方同址     命中文件数=1    :: ./C76-RS-failing-step-second-lemma-and-verdict-on-sieve-weight-idea.md
技术词 乘积界      命中文件数=1    :: ./C76-RS-failing-step-second-lemma-and-verdict-on-sieve-weight-idea.md
技术词 筛权重      命中文件数=4    :: ./TYPE-MATCH-matching-types-exist-explicit-formula-and-large-value-density.md ./V255-5b-attack-no-restatement-type-mismatch-abscissa-vs-zero.md ./C76-RS-failing-step-second-lemma-and-verdict-on-sieve-weight-idea.md
```
**读数（按实测）**：`消失引理`／`四方同址`／`乘积界`＝**仅本档（1 档 ⟹ 本档新增）** ✓；⚠️ `筛权重`＝**4 档 ⟹ 档案已有**（`TYPE-MATCH`／`V255-5b` 等已讨论同一设想）⟹ §3 为**引用＋判定**，**不列为本档提出** ✓

## §7 边界

- `[逐字]` §1 的 `Second Lemma`／`Theorem 2` 取自 `arXiv:2002.00595v1`（**二手**，已标注）⚠️；§5 的 Duke 出处为一手但未取得
- `[本档]` §1 的关键等价（support ⇔ 乘积界）、§2 的四方同址、§3 的判定、§4 的三点 ✓
- **不声称**：`η*>0` 成立／不成立 ✗；不声称已破 `0.682` ✗；不判筛权重路线死 ✗（仅判"单靠权重不够"）；不证 RH ✗；不修改原档 ✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓；未跑 Lean ✓

```
⚠️ 唐先生 12:33：① 更正我方"未被走过"措辞（它就是那堵众所周知的墙）；② 要求取 RS 里 k=3 卡在 X≤T^{2/3−ε} 的具体失效步骤原文
⚠️ 已取回（arXiv:2002.00595v1，二手讲解源）：Second Lemma "if Φ is supported in |ξ1+…+ξn| ≤ (2−δ)/m then
   A_{r,s}(n,T)=0 unless |n_j| ≪ T and n₁n₂…n_{r+s} ≪ T^{2−δ}"；Theorem 2 "Φ supported in Σ|ξ_j| < 2/m"
⚠️ 关键等价（本档）：support Σ|ξ_j| < 2/m ⟺ 素数幂乘积 n₁⋯n_{r+s} ≪ T^{2−δ}；k 个各 ≍X ⟹ X^k ≤ T^{2−δ} ⟹ k=3 即 X ≤ T^{2/3−ε}
   ⟹ "support>1" / "无条件三阶矩" / "乘积超过 T²" / "prime-pair 输入" 四者同一件事
⚠️ 对"筛权重/Heath-Brown 式"判定：消失引理是恒等式型（由显式公式＋Supp Φ 推出），改权重不改变乘积界 ⟹ 单靠权重不够
   （权重只能同范围内榨常数 = 0.6725→0.682 那 0.01）；旁证：V254/V255 parity barrier + V255-5b 型判据
⚠️ 三个可抠点：(1) Problem A SQ1（MV 对该核是否 sharp ⟹ 障碍是 ℓ² 伪影？）(2) SQ3（Λ vs μ² 判别）(3) 指数 2 的来源审计
⚠️ 出处与可信度：Duke 原文本地无（付费墙）；2002.00595 为二手且有拼写错误 ⟹ 引用前须与原文核对；Goldston-Suriajaya 2603.28104 已由唐先生核实
✅ 净产出：①RS 失效步骤取回（含逐字与机制）✓；②support⇔乘积界 的关键等价 ✓；③四方同址 ✓；④筛权重设想的判定 ✓；⑤三个可抠点 ✓
```
