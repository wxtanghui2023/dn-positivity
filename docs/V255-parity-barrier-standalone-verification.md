# V255 · **parity barrier 独立核验档**（[待核／参照档]，**不并入 V254 判词**）

> 委托 ✓ 唐先生 2026-09-15 22:25：**"关于 parity barrier：建议单独开档核验，不要提前并入 V254 的判词。它可能提供'signed sieve 的结构性极限'这一侧的参照，但目前没有数学蕴含链把它接到 $\beta_*=1/2$。"** ✓✓
> 本档定位 ✓ **独立核验档**，不是结论档；**V254 判词已移除 parity barrier**（见 V254 §11 T9）✓
> 纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ **V255**

---

## §1 为什么单开（定位）

$$\textbf{理由一}：\text{V254 判词说的是}\ \textbf{"canonical}\ \text{signed-L-function 家族没有提供独立的 B 型突破"};$$
$$\qquad \text{parity barrier 讲的是}\ \textbf{"可构造的 signed sieve 权重类的能力上限"} \text{——}\textbf{命题类型不同} ⇔ \text{并入会污染判词} ✓$$
$$\textbf{理由二}：\text{两者之间}\ \textbf{目前没有数学蕴含链};\ \text{单开可保留一个}\ \textbf{干净的待核项} \text{，而不必先表态} ✓$$

## §2 parity barrier 的精确陈述（⚠️ **凭记忆，未逐条核对** —— 本档任务之一即核验）

$$\text{(i)}\ \textbf{命题（口语版）}：\text{组合筛／Selberg 筛／线性筛}\ \textbf{无法区分}\ \Omega(n)\ \textbf{的奇偶性} ✓$$
$$\qquad \text{即：筛法}\ \textbf{不能}\ \text{把"素数集"与"同阶半素数集（}\Omega=2\text{）"分开} ⟹ \text{筛法}\ \textbf{单独无法"探测素数"} ✓$$
$$\text{(ii)}\ \textbf{典型后果}：\text{线性筛给出}\ \{n:\ n\ \text{无小于}\ z\ \text{的素因子}\}\ \text{的上／下界，}\textbf{但}\ \text{对"筛出素数"这一类目标}\ \textbf{系统性失效} ✓$$
$$\text{(iii)}\ \textbf{出处（待核）}：\text{Selberg 的 parity principle};\ \text{Friedlander–Iwaniec}\ \text{《Opera de Cribro》}\ \text{相关章} ✓$$
$$\qquad ⚠️\ \textbf{三行均为凭记忆陈述，原文级核对未做};\ \text{核验后须就地更正} ✓$$

## §3 为什么它**不是** RH 障碍定理（三条独立理由）

$$\textbf{(i) 命题类型不同}：\text{parity barrier 是关于}\ \textbf{"某类筛法权重的能力上限"};\ \text{不是关于}\ \zeta\ \text{的零点} ✓$$
$$\textbf{(ii) 无蕴含链}：\text{目前}\ \textbf{既无} \text{"parity barrier}\Longrightarrow\beta_*\le\tfrac12\ \text{的某约束"},\ \textbf{也无反向} ✓✓$$
$$\textbf{(iii) 方法类别不同}：\text{筛法权重是}\ \textbf{被构造} \text{的（Selberg}\ \lambda_d\ \text{可选}）,\ \textbf{不是 L-函数商};\ \text{故它}\ \textbf{不属} \text{V254 的 canonical 家族} ✓$$

## §4 ⭐ 它能提供什么（**结构参照**，不是定理）

$$\textbf{一个正面事实}：\text{存在一类}\ \textbf{可构造的、带符号的} \text{抵消来源，其能力有}\ \textbf{可证上限} ✓✓$$
$$\textbf{与 V254 的对照（这是本档最有用的一格）}：$$

| | 抵消来源 | 上限性质 |
|:--|:--|:--|
| `V254` §2 | **典范**（$\mu$／$\chi$／Hecke，即 L-函数商族） | **循环**（上限＝$\beta_*$；推到 $\tfrac12$ ⟺ RH） |
| `V255` §2 | **可构造**（Selberg／Rosser–Iwaniec 筛法权重） | **可证**（parity barrier） |

$$\Longrightarrow \text{两类}\ \textbf{都有 cap}，\ \text{但 cap 的性质不同（一个循环、一个可证）};\ \textbf{且无已知蕴含链把后者接到前者} ✓✓✓$$
$$\Longrightarrow \text{对 V254 T6 的}\ \textbf{对象型搜索规格} \text{提供}\ \textbf{一个负面参照点}：\text{新对象}\ \textbf{不应属于"筛法权重类"}（\text{其 cap 已知、且与}\ \beta_*\ \text{无链}）✓✓$$

## §5 [待核] 三个具体核验项（本档的实际任务）

$$\textbf{(a)}\ \text{parity barrier 的}\ \textbf{精确陈述} \text{（原文级：哪一类筛、被禁止的到底是什么）} ✓$$
$$\textbf{(b)}\ ⭐\ \textbf{它是否可重述为"某 Dirichlet 级数的收敛横坐标上界"？若有，该横坐标是多少？} ✓✓$$
$$\qquad \textbf{这是唯一可能把它接到}\ \beta_*\ \text{的技术路径};\ \text{本档}\ \textbf{目前没有} \text{这一重述};\ \text{若核验发现存在}\ \Longrightarrow \textbf{立刻回报} ✓✓✓$$
$$\textbf{(c)}\ \text{它与}\ \mu\ \text{的可证上界（}\text{PNT 定量：}M(x)=O(xe^{-c\sqrt{\log x}})\text{）之间}\ \textbf{是否有已知蕴含关系} ✓$$

## §6 判词（**不并入 V254**）

$$\boxed{\textbf{V255}：\text{状态＝}\textbf{[待核／参照档]}，\ \textbf{不是结论}};\qquad \text{V254 判词}\ \textbf{不含} \ \text{parity barrier} ✓✓$$

## §7 边界

$$\text{§2 三行}\ \textbf{凭记忆};\ \text{§4 的对照表为本档}\ \textbf{整理};\ \text{§5 的}\ \textbf{(b) 是唯一的接链候选}，\ \text{目前不存在} ⚠️;\ \textbf{未用 RH};\ \text{未跑 Lean};\ \textbf{零数值} ✓$$

```
⚠️ 委托（唐先生 22:25）：parity barrier 建议单独开档核验，不要提前并入 V254 判词；它可能提供
   "signed sieve 的结构性极限"这一侧的参照，但目前没有数学蕴含链把它接到 β*=1/2
⚠️ 本档定位：独立核验档（不是结论档）；V254 判词已移除 parity barrier（见 V254 §11 T9）
⚠️ §2 parity barrier 精确陈述（⚠️ 凭记忆，未逐条核对）：(i) 组合筛/Selberg 筛/线性筛无法区分
   Ω(n) 的奇偶性；(ii) 后果：筛法单独无法探测素数（不能把素数集与同阶半素数集分开）；
   (iii) 出处（待核）：Selberg parity principle；Friedlander–Iwaniec《Opera de Cribro》
⚠️ §3 为什么它不是 RH 障碍定理：(i) 命题类型不同（是"某类筛法权重的能力上限"，不是关于 ζ 零点）
   (ii) 无蕴含链（既无 parity ⟹ β* 约束，也无反向）(iii) 方法类别不同（筛法权重是被构造的，
   不是 L-函数商，故不属 V254 的 canonical 家族）
⚠️ §4 它能提供什么（结构参照）：存在一类可构造的、带符号的抵消来源，其能力有可证上限；
   与 V254 对照 —— 典范（μ/χ/Hecke，L-函数商族）上限＝循环（=β*，推到 1/2 ⟺ RH）；
   可构造（Selberg/Rosser–Iwaniec）上限＝可证（parity barrier）
   ⟹ 两类都有 cap，但 cap 性质不同（一个循环、一个可证），且无已知蕴含链把后者接到前者
   ⟹ 为 V254 T6 的对象型搜索规格提供负面参照点：新对象不应属于"筛法权重类"
⚠️ §5 三个待核项：(a) parity barrier 精确陈述（原文级）(b) ⭐ 它是否可重述为"某 Dirichlet 级数的
   收敛横坐标上界"？若是，该横坐标是多少？—— 这是唯一可能把它接到 β* 的技术路径；本档目前没有
   这一重述；若核验发现存在则立刻回报 (c) 它与 μ 的可证上界 M(x)=O(xe^{-c√log x}) 之间是否有
   已知蕴含关系
⚠️ §6 判词：V255 状态＝[待核/参照档]，不是结论；V254 判词不含 parity barrier
⚠️ §7 边界：§2 凭记忆；§4 为整理；§5(b) 是唯一接链候选但目前不存在；未用 RH；未跑 Lean；零数值
```
