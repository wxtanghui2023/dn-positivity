# P1-5-2026-09-27 — **Van Wee 证明分解 @ $n=10$**（source-first，零计算）＋ **R2-1 ＝ DROP** 更新

> ⚠️ **空间隔离**：本档＝**空间 B 之 119 线**专用 ✓；不引 RH 链 ✗（唐先生 21:32 令 ✓）。

**已查地图：命中（接续 R1 档与今日 Van Wee 链工作，非新案 ✓）**
所查：`docs/119-ATTACK-R1-2026-09-27-…leverage-verdict.md`（**四方向普查** ✓✓）｜`docs/CHAIN-VW-2026-09-27-self-contained-b-le-2-and-full-corollaries.md`（**van Wee 原文锚点逐字** ✓✓）｜`docs/ALG-VW-2026-09-27-equality-reformulation-and-the-exact-gap.md`（**缺口定位** ✓✓）｜`docs/P12-PASS-2026-09-27-bucket-divergence-with-identical-distance-distribution.md`（**P1-2 PASS** ✓✓）｜`docs/P1-REAUDIT-2026-09-27-E-correction-and-the-mod-11-theorem.md`｜`docs/P1-2026-09-27-support-layer-screen-results.md`｜`docs/ALIGN-2026-09-25-our-delta-field-vs-WuChen-excess-surfeit.md`｜`docs/FOURIER-2026-09-26-…`｜`docs/DELSARTE-2026-09-26-…`｜`sources/TUe-covering-codes-chapter-IR425174.pdf`（**场内存档** ✓）
**外部 source-first（本轮新取 ✓）**：**Habsieger, FPSAC 95**（`fpsac-archive.github.io/FPSAC95/ARTICLES/25.HABSIEGER.pdf`）✓✓
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §7）
D0: 本档对象 ＝ **档案已有** 119 线 van Wee／Habsieger 体系的**逐步饱和度分解**（重命名：否 ✗；新对象：无 ✗）
D1: 0（分解 ＋ 出口判定 ✓；**未动算** ✓；**未改门** ✓）

---

## §0 结论（**A 型** ✓ —— 但附条件）

$$\boxed{\text{未消耗的结构性自由度}:\ \textbf{坐标支撑层（support incidence）}\ ——\ \text{且\textbf{可证}它在 van Wee／Habsieger 体系内}\textbf{结构性不可见}}$$
$$\boxed{\text{但该自由度在 }n=10\ \text{是否\textbf{真的存在}，取决于 R2-2} \Longrightarrow \text{本档为 }A\ \text{型，条件挂在 R2-2 上}}$$
$$\boxed{\textbf{R2-1 ＝ DROP（理由翻转 ✓ 唐先生修正）}:\ \text{Habsieger 原文\textbf{已研究} }n\equiv2,4\bmod6,\ n=10\ \text{已给出 }K\ge104\ (\text{Zhang }105)\ \ll119}$$
$$\boxed{\textbf{R2 状态}:\ R2\!-\!1\ \text{DROP}\ |\ R2\!-\!2\ \textbf{ALIVE}\ |\ R2\!-\!3\ \text{HOLD}\ |\ R2\!-\!4\ \textbf{本档已执行（A 型出）}}$$

---

## §1 source-first 清单（**逐字** ✓）

### §1-a Habsieger（FPSAC 95）—— 本轮新取 ✓✓
$$\text{题目}:\ \textit{Binary codes with covering radius one from a linear programming point of view: some new lower bounds}✓$$
> 摘要逐字："We study binary codes with covering radius one via their **characteristic functions**. The covering condition is expressed as a **system of linear inequalities**. The **excesses** then have a natural interpretation that makes **congruence properties** clear. We present new congruences and give several improvements on the lower bounds for $K(n,1)$ given by **Zhang [9,10]**. **We study more specifically the cases $n\equiv5\bmod6$ and $n\equiv2,4\bmod6$**, and get new lower bounds such as $K(11,1)\ge178$ and $K(20,1)\ge52455$." ✓✓
**体系（逐字 ✓）**
$$\text{层算子}:\ F_i(x)=\sum_{y\in S_i(x)}F(y)\ ✓;\qquad \sum_{0\le i\le n}F_i=|F|\ ✓\ (\text{故 }\textstyle\sum_i\delta_i=\|\delta\|)$$
$$\textbf{Lemma 1}:\ (F_i)_j=\sum_{k}\binom{k}{\frac{k+j-i}2}\binom{n-k}{\frac{i+j-k}2}F_k(x)\ \text{（Krawtchouk 型复合 ✓）}$$
$$N=\mathbf 1_C;\quad \text{覆盖}\iff(N_0+N_1)(x)\ge1;\quad \delta=N_0+N_1-1\ge0\ \text{整数}✓;\quad \boxed{\|\delta\|=(n+1)|C|-2^n}✓$$
$$(4)\ \boxed{\delta_i=(n+1-i)N_{i-1}+N_i+(i+1)N_{i+1}-\binom ni}\ ✓✓\ \text{（\textbf{层公式}：}\delta_i\ \text{由 }N_i\ \text{逐点决定 ✓）}$$
$$\textbf{Lemma 2}:\ p\ \text{奇素数},\ p\mid n+1\Longrightarrow \sum_{i=0}^{p-1}\delta_i\equiv p-1\ (\bmod p)✓;\ \text{另列 }p\in\{2,3,4,5\}\ \text{的同余 ✓}$$

### §1-b van Wee（原文锚点，档内已 source-verified ✓）
$$\text{Def 1（excess）};\ \text{Lemma 1a}:\ E_C(\mathbb F_2^n)=|C|V(n,R)-2^n✓;\ \text{Lemma 3b}:\ z\in Z\Longrightarrow|B_R(z)\cap C|\ge2✓;\ \text{Lemma 4a/b}✓$$
$$\textbf{Lemma 8}:\ d(x,C)=R\Longrightarrow E_C(B_1(x))\ge(R+1)\lceil\tfrac{n+1}{R+1}\rceil-n-1✓\ (\text{证用 }|B_R(c)\cap B_1(x)|\in\{0,R+1\}✓)$$
$$\textbf{Theorem 9}:\ A:=\{a:d(a,C)=R\};\ |A|\ge2^n-|C|V_2(n,R-1)✓;\ \forall z\in Z:\ |A\cap B_1(z)|\le|B_1(z)|-(R+1)✓$$
$$\textbf{Cor 1a/1b}:\ K(n,1)\ge2^n/n✓;\quad K(2^r,1)=2^{2^r-r}✓\ (\textbf{仅 }n=2^m\ \text{取等})$$

### §1-c 其他
Zhang（$K(10,1)\ge105$，pair-covering by $k$-uples ✓）｜Wu–Chen 2024（Habsieger 同余，**只对 $6\mid n$** ✓）｜Habsieger–Plagne（"从旧线性不等式产生新下界"的方法论 ✓）

---

## §2 **逐步分解表**（照唐先生给定格式，逐行填 ✓✓）

| Van Wee／Habsieger 步骤 | $n=10$ 是否已饱和 | 依据（本档核 ✓） |
|---|---|---|
| **一阶 excess** | ✅ **已饱和** | $\|\delta\|=(n+1)|C|-2^n=11|C|-1024$（恒等式 ✓）；$|C|=119\Rightarrow285$；$|C|=120\Rightarrow296$ ⟹ **无自由度** ✗ |
| **局部 congruence** | ✅ **已使用（且自动满足）** | $n+1=11$ 为素数 ⟹ **Lemma 2** 给 $\sum_{i=0}^{10}\delta_i\equiv10\bmod11$；而 $\sum_i\delta_i=\|\delta\|=285=11\cdot25+10$ ⟹ **恒等满足** ⟹ 该同余在 $n=10$ **无剩余切割力** ✓ |
| **二阶 intersection** | ⚠️ **部分使用；剩余部分＝本档发现** | 已用：Zhang 的 **pair-covering by $k$-uples** ＋ van Wee **Lemma 3b／8**（$|B_R(c)\cap B_1(x)|\in\{0,R+1\}$ ⟹ 区间几何）⟹ 产出 104/105/107 ✓；**未用**：**坐标支撑层**（$m_{ij},q_{ij},J$）⚠️（见 §4） |
| **等号条件** | ✅ **在 $n=10$ 不适用（无余量）** | van Wee 等号 $\iff n=2^m$（Cor 1b）；$n=10\ne2^m$ ⟹ 等号链（$b\le2$／matching／二部）**整条不适用** ✗（`ALG-VW` 已定位缺口在"(i) 非码字点不被三重覆盖"，且**不能**由计数恒等式推出 ✓） |
| **整数性余量** | ⚠️ **线性内容已吃尽** | 模 11 定理：$\ker(T\bmod11)=\mathrm{span}\{\mathbf 1\}$；$g=11T^{-1}\delta$ 的**线性内容恰是整数性**、非线性＝Booleanity ⟹ 剩的不是"整数性"而是**二值性** ⟹ 与 support 层同侧 ⚠️ |
| **coordinate／support information** | ❌ **未被使用 ＝ 自由度所在** | 见 §4 ✓✓ |

---

## §3 算术级核验（**本档，符合"不计算"** ✓）

$$n=10:\quad n+1=11\ \text{（素数 ✓）};\quad \|\delta\|=11|C|-1024;\quad |C|=119\Rightarrow\mathbf{285};\ |C|=120\Rightarrow\mathbf{296}$$
$$285\equiv10\ (\bmod 11)\ ✓\ \text{——\textbf{与 Lemma 2 一致} ⟹ 同余自动满足 ✓（非独立约束 ✓）}$$
$$\text{van Wee 界}: 11|C|\ge1024\Rightarrow|C|\ge93.09\Rightarrow\ge94;\quad 2^n/n=102.4\Rightarrow\ge103;\quad \text{已发表}:104/105/107 \ll119✓$$
$$\Longrightarrow\ \boxed{\text{距离层体系在 }n=10\ \text{给出的上界（下界）} \approx105\text{–}107\ \text{，距 }119\ \text{有 }12\text{–}14\ \text{的缺口}}✓$$

---

## §4 ★**未被消耗的自由度**：坐标支撑层（**本档核心 ✓✓**）

$$\textbf{命题（2 行，可自证 ✓✓）}:\ \text{由 Habsieger }(4),\ \delta_i=(n+1-i)N_{i-1}+N_i+(i+1)N_{i+1}-\binom ni\ \Longrightarrow\ \boxed{\{\delta_i\}\ \text{与}\ \{N_i\}\ \text{逐点互相决定}}$$
$$\qquad\Longrightarrow\ \text{凡只用 }\{N_i\}\ \text{／}\ \{\delta_i\}\ \text{（及其层和、模 }p\ \text{同余、对 }x\ \text{的聚合）的判据，} \textbf{完全由距离层数据决定} ✓✓$$
$$\textbf{见证（P12-PASS ✓✓）}:\ \text{三个两两不等价的最优 }(8,32)_1\ \text{码}:\ \textbf{全距离分布相同}\ A=(0,16,160,176,64,48,32,0),\ \textbf{而}\ \sum_{i<j}q_{ij}^2=64/128/256✓✓$$
$$\Longrightarrow\ \boxed{\text{距离层判据}\ \textbf{不可能}\ \text{区分它们} \Longrightarrow \textbf{坐标支撑层承载距离层之外的信息}}✓✓\ \text{（这正是"新可区分维度"✓）}$$
**支撑层量（定义 ✓）**：$S(c)=\{i:c\oplus e_i\in C\}$｜$d_1(c)=|S(c)|$｜$m_{ij}=\#\{c:i,j\in S(c)\}$｜$q_{ij}=\#\{\{c,c\oplus e_i\oplus e_j\}\subseteq C\}$｜$J$-族（$J_1,\dots,J_7$）✓
$$\textbf{与既有体系的对照 ✓}:\ \text{van Wee／Habsieger／Zhang／Wu–Chen 的\textbf{全部量}都只依赖 }(N_i,\delta_i)\ \text{或其局部几何（} |B_R(c)\cap B_1(x)|\in\{0,R+1\}\text{）}$$
$$\qquad\Longrightarrow\ \boxed{\text{支撑层的 }m_{ij},q_{ij},J\ \textbf{在其体系内结构性不可见}}✓✓\ \text{——\textbf{这就是"未被 excess／congruence 理论吃掉的结构性自由度"}}✓$$

---

## §5 A／B 判定（**A 型，但条件挂在 R2-2** ✓）

$$\boxed{\textbf{本档输出 ＝ A 型}:\ \text{找到一个既有理论\textbf{未利用}的维度（坐标支撑层），且\textbf{可证}其不可见性}}$$
**但必须诚实标注两个条件** ✓：
1. **存在性未定** ⚠️：P12-PASS 的见证在 $n=8$（Theorem-13 域内）；**$n=10$ 是否也有"同距离分布、异 $J$"的码，未知** ⟹ 该自由度在 $n=10$ **是否真的存在** ＝ **R2-2 的问题** ✓（若不存在 ⟹ 落 **B**）
2. **不等式的转换未完成** ⚠️：有了维度 ≠ 有了约束；须把它变成**对任意 119-cover 成立的不等式**（且不得只在构造族内成立 ✗）
$$\Longrightarrow\ \boxed{\text{下一档}:\ \textbf{R2-2（}n=10\ \text{的支撑层分叉：构造或证明其不存在）}\ +\ \text{并行准备"支撑层不等式"形式化}}$$
$$\text{若 R2-2 判"不存在"} \Longrightarrow\ \textbf{落 B}:\ \text{Van Wee／Habsieger 等号链在 }n=10\ \text{已完全饱和} \Longrightarrow \textbf{DROP R2-4}✓$$

---

## §6 R2 状态更新（**照唐先生 21:42 定** ✓）

$$\boxed{R2\!-\!1\ \textbf{DROP}\ \big|\ R2\!-\!2\ \textbf{ALIVE（下一档）}\ \big|\ R2\!-\!3\ \textbf{HOLD}\ \big|\ R2\!-\!4\ \textbf{已执行（本档，A 型出）}}$$
- **R2-1 DROP 的**理由翻转 ✓：**不是**"$n=10$ 未被同余路线覆盖"，而是**恰恰相反**——Habsieger 原文**明确处理 $n\equiv2,4\bmod6$**，$n=10$ 得 $\ge104$（Zhang $\to105$）⟹ **已被处理且距 119 很远** ✓✓
- **R2-4 的 deliverable** 已按唐先生口径落实 ✓："找到 119 假设下**尚未被既有 excess／congruence 理论吃掉**的结构性自由度" ⟹ **答案＝坐标支撑层** ✓✓

---

## §7 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "分解表"
技术词 分解表          命中文件数=3    :: ./C87-D3b-first-cut-block-method-works-smooth-part-gap-normalizes-to-D1.md ./OSCILLATION-CANCELLATION-TECHNIQUES-SURVEY-unconditional-vs-conditional.md ./M03-3b-final-registration-and-residual-target.md
$ bash scripts/tech_word_check.sh "饱和"
技术词 饱和            命中文件数=224  :: ./V240-finite-arithmetic-deficit-recursion-liouville-extension-criticality.md ./C112-W4-1d-three-gate-audit-C2-first-zero-cost-kill.md ./T3-0-charter-architecture-search.md
$ bash scripts/tech_word_check.sh "坐标支撑"
技术词 坐标支撑        命中文件数=3    :: ./P12-PASS-2026-09-27-bucket-divergence-with-identical-distance-distribution.md ./ASSETS-REGISTRY.md ./119-ATTACK-R1-2026-09-27-P1-global-invariant-census-and-leverage-verdict.md
$ bash scripts/tech_word_check.sh "Habsieger"
技术词 Habsieger       命中文件数=14   :: ./ALIGN-2026-09-25-our-delta-field-vs-WuChen-excess-surfeit.md ./B-2026-09-26-n9-construction-status-and-line-snapshot.md ./ODDENGINE-2026-09-26-struik-vacuous-for-odd-n-and-the-coupling-target.md
$ bash scripts/tech_word_check.sh "层公式"
技术词 层公式          命中文件数=0    ::
$ bash scripts/tech_word_check.sh "未消耗"
技术词 未消耗          命中文件数=1    :: ./C3899i-gamma13-M3-first-cut-gates-G-D-and-M3alpha-registration.md
```
- **本档新增**：**0** 个术语 ✓（`层公式` 命中 0 ⟹ 为**外部来源术语**（Habsieger (4) 的本文命名），**引用**，不作新性主张 ✓）
- **档案已有（引用，不列为提出）**：`分解表`（3）｜`饱和`（224）｜`坐标支撑`（3）｜`Habsieger`（14）｜`未消耗`（1）✓

## §8 边界（硬 ✓）

- **未动算** ✓（唐先生"不计算" ✓；§3 仅为算术级核验 ✓）；**未改门** ✓；**不跨空间** ✓
- **A 型的两个条件**（§5）**必须随结论一同引用** ✗ 不得只引"A 型"二字 ✓
- 不写"不可能／不存在"作为终局 ✗（V290）；**B 的判定权**：若 R2-2 判不存在才落 B ✓
- 外部材料（Habsieger PDF）为**未受信内容**，**只作数据** ✓，未执行其中任何指令 ✓
