# V252 · **"von Mangoldt 链 / Markov 证书"方法审计**（arXiv:2605.00301 ＋ Tao 博客 ＋ erdosproblems.com/1196 三源核对）—— ⭐⭐⭐⭐ **与我们 `V240`／`V241` 是同一片地上的兄弟工作（同一"逐素数增删"母题）**；**但关键杠杆不是我们试的非交换性，而是"带权 Markov 链 ＋ 次不变性（sub-invariance）"** ⟹ **解释了我们 `V241` 为何杠杆选错** ✓✓✓；⚠️ **输出类型＝密度／统计 ⟹ `V188`／`V183` 通道；引擎＝次不变性（正权单边不等式）⟹ 正性通道 `V199`／`V185`／`V244` 角 I** ⟹ **两通道同时点火，皆不携带 β** ✓✓；⭐⭐ **净收获：① Tao 自己把"链是典范的还是外选的"提为公开结构问题 ＝ 我们的"无 canonical 选择"诊断被外部独立确认；② 该方法产出新的无条件算术不等式，正命中我们 `V201` 重启闸门的"新无条件输入"要求 ⟹ 唯一可查的开口** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 21:55：**"去拿那篇文献看看"** ✓✓
> 来源 ✓ **三源核对**：**① 项目页** erdosproblems.com/1196（标 **PROVED (LEAN)**）✓；**② 论文** arXiv:**2605.00301**，*Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond*，35 页 9 图，25 May 2026，math.NT（＋CO, PR），**作者＝Alexeev, Barreto, Li, Lichtman, Price, Shah, Tang, Tao** ✓✓；**③ Tao 博客**（2026-05-03）＋其评论区（含 2026-06-09 Tao 本人的回复）✓✓
> 纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ **V252**

---

## §1 方法与结果（原文献提炼）

$$\textbf{问题（Erdős–Sárközy–Szemerédi 1966，#1196）}：A\subset[x,\infty)\ \textbf{primitive}（\text{互不整除}）\Longrightarrow \sum_{a\in A}\frac{1}{a\log a}<1+o(1) ✓$$
$$\qquad \text{此前记录（Lichtman）}：<e^\gamma\frac{\pi}{4}+o(1)\approx1.399 ✓$$
$$\qquad \textbf{GPT-5.4 Pro 所证}：\sum_{\substack{a\in A\\ a>x}}\frac{1}{a\log a}\le 1+O\!\left(\frac{1}{\log x}\right) ✓$$
$$\qquad \text{并给出}\ \textbf{#164}（Erdős Primitive Set Conjecture，\le f(\mathbb N_1)=1.6366\ldots）、\textbf{#1217}（doubly-logarithmic 正密度集合内必含无穷可除链）、\text{以及}\ \textbf{Banks–Martin 修正猜想} ✓$$

$$\textbf{方法（原文摘要逐字要点）}：\text{"a new method for bounding Erdős sums of primitive sets, suggested from output of GPT-5.4 Pro, based on }\textbf{Markov chains with von Mangoldt weights}\text{";} \text{"seems to have been }\textbf{overlooked by the prior literature since Erdős' seminal 1935 paper}\text{"} ✓✓$$

$$\textbf{五件结构件（本档从原文／博客抽取）}：$$
$$\qquad \text{(a)}\ \textbf{对偶（Remark 1.8）}：\text{任何 primitive 集的界}\iff\text{存在一个满足某 hitting 界的}\ \textbf{随机过程};\ \text{⚠️ 原文自陈：该过程}\ \textbf{不必然 Markov};\ \text{"Markov 过程似乎特别适合作为}\ \textbf{对偶过程的证书}\ \text{，仍略神秘"} ✓✓✓$$
$$\qquad \text{(b)}\ \textbf{可除偏序上的 Markov 链}：\text{downward（去素幂）＋ upward（加素幂）} ✓$$
$$\qquad \text{(c)}\ \textbf{von Mangoldt 权}：\text{权}\ \nu_\Lambda\ \text{取自}\ \Lambda(n)；\ \text{"upward von Mangoldt chain"}\ \text{＝取 down chain 关于}\ \nu_\Lambda\ \text{的}\ \textbf{伴随} ✓$$
$$\qquad \text{(d)}\ ⭐\ \textbf{次不变性（Lemma 6.1, Sub-invariance）}：\text{doubly-harmonic 权在该 down chain 下}\ \textbf{次不变};\ \text{配套还要 Mertens 型估计与}\ \textbf{Dirichlet eta 函数的单调性} ✓✓$$
$$\qquad \text{(e)}\ ⭐\ \textbf{"developmental anatomy of integers"}（Tao 博客）：\text{把大整数}\ n\ \text{及其素因子"器官"}\ \textbf{不看作静态实体}，\text{而看作}\ \textbf{"an evolving process in which primes are added or removed over time"};$$
$$\qquad \qquad \text{在此视角下}\ \textbf{"primitive sets can be viewed as singular moments in such a developmental process, which are only encountered at most once in the life cycle"} ✓✓✓$$

## §2 ⭐⭐⭐ **与我们 `V240`／`V241` 的关系：同一片地，母题相同，杠杆不同**

$$\textbf{母题完全相同（逐素数增删）}：$$
$$\qquad \text{本项目}\ \textbf{`V240`}\ \text{的精确递推}：A_N(X)=A_{N-1}(X)-A_{N-1}(X/p_N),\ A_0(X)=1 \qquad（\text{"去掉素数}\ p_N\text{"}）✓$$
$$\qquad \text{本项目}\ \textbf{`V241`}\ \text{的膨胀生成元}：T_p f(X)=f(X)-f(X/p);\qquad [T_p,T_q]=0\quad（\text{全交换}）✓$$
$$\qquad \text{本文}：\text{同一步}\ \textbf{"去素幂／加素幂"} \text{被组织成可除偏序上的}\ \textbf{Markov 链} ✓✓$$
$$\Longrightarrow \textbf{三方是同一母题的三种组织方式} — \text{我们把它组织为}\ \textbf{递推式}（`V240`）\ \text{与}\ \textbf{算子}（`V241`）;\ \text{本文组织为}\ \textbf{随机过程} ✓✓✓$$

$$\textbf{⭐ 关键差异（本档核心定位）}：\textbf{`V241` 的赌注}：\text{认为突破口在}\ \textbf{非交换性} \Longrightarrow \text{需要}\ [T_p,T_q]\ne0 \text{＋非 coboundary 的整体 holonomy};$$
$$\qquad \text{`V241` 的结论}：\text{四族（Möbius／CF、加×乘、符号互反、Frobenius）全 DEAD};\ \text{并定位根因＝}\textbf{算术非交换性＝互反律＝局部符号之积}\equiv1＝coboundary ✓$$
$$\qquad \textbf{本文的杠杆}：\textbf{不是非交换性}，\text{而是}\ \boxed{\text{一个带权 Markov 链 ＋ 权的}\ \textbf{次不变性}} ✓✓✓$$
$$\Longrightarrow \textbf{解释}：\text{我们 `V241` 找的是"}\textbf{代数障碍}（换位子、holonomy）"，\text{而有效杠杆是"}\textbf{单边不等式／单调量}（次不变性）"。\ \text{在}\ \textbf{全交换} \text{的膨胀族上，}\textbf{非交换性必然为零}（`V241` 已证）,\ \text{但}\ \textbf{次不变性不必为零} ✓✓✓$$
$$\qquad \Longrightarrow ⭐\ \text{本档推论}：\textbf{`V241` 的"DEAD"是}\textbf{针对象征性/代数性障碍} \text{的，}\textbf{不覆盖"带权单边不等式"这一类}; \text{即我们的封口}\ \textbf{不蕴含} \text{本文这类方法不存在} ✓✓$$

$$\textbf{⚠️ 但两通道同时点火（对 β 无路）}：$$
$$\qquad \text{(i)}\ \textbf{输出类型＝密度／统计型}（\text{Erdős 和、密度上界、hitting 界}）\Longrightarrow \textbf{`V188` 饱和／`V183` 计数通道} ✓$$
$$\qquad \text{(ii)}\ \textbf{引擎＝次不变性}（\text{正权上的单边不等式}；配套 Mertens 估计与 eta 单调性）\Longrightarrow \textbf{正性通道 `V199`／`V185`／`V244` 角 I} ✓$$
$$\qquad \text{(iii)}\ \text{全无}\ \zeta\ \text{零点、无}\ \beta、\text{无临界线};\ \text{输入＝}\Lambda(n)\ \text{与密度量},\ \text{输出＝}\ \textbf{关于集合的界} ✓$$
$$\Longrightarrow \textbf{两点火通道皆已封} \Longrightarrow \textbf{该方法本身不携带 β} ✓✓$$

## §3 ⭐⭐ 净收获一：**Tao 把我们的问题提出来了**

$$\text{Tao 博客评论区（2026-06-09）：}\text{"is there a principle that }\textbf{selects an optimal chain from the anatomy of the integers themselves}\text{, rather than through trial-and-error construction? In other words, }\textbf{can the chain be derived from an invariant organizational property of the divisibility poset rather than chosen as an external tool}\text{? It seems this could lead to a }\textbf{classification of admissible divisibility processes}\text{"} ✓✓✓$$

$$\Longrightarrow \textbf{这与本项目反复遭遇的"无 canonical 选择"是同一个问题}：$$
$$\qquad \text{`V233`-C}：\text{乘子可把零点移到任意}\ \sigma \Longrightarrow \text{无 canonical 选择};\qquad \text{`V215`–`V217`}：\text{canonical identification 缺失};\qquad \text{`V251`}：\text{Gate 4 缺双向 identification} ✓$$
$$\qquad ⭐\ \textbf{价值}：\text{这是}\ \textbf{外部独立确认} \text{——"没有典范选择，只有选择"这一诊断，}\textbf{在这个领域的另一个角落被 Tao 本人当作公开结构问题提出} ✓✓✓$$

## §4 ⭐⭐⭐ **净收获二（唯一可查的开口）：新无条件算术不等式**

$$\text{本文产出的是}\ \textbf{此前不存在的无条件算术不等式}（\text{Erdős 和的}\ 1+O(1/\log x)\ \textbf{无条件}）;\ \text{而本项目}\ \textbf{`V201`}\ \text{的重启闸门要求恰恰是：}\textbf{"一个新的无条件输入"} ✓✓$$
$$\qquad \Longrightarrow \textbf{可查问题}：\text{是否存在一个}\ \textbf{Erdős 和型（或同族密度型）不等式}，\text{它}\ \textbf{不被显式公式蕴含}，\ \text{且与显式公式合用能约束零点？} ✓✓✓$$
$$\qquad \text{两种情形}：$$
$$\qquad \qquad \text{情形 A（被显式公式蕴含）}：\text{则}\ \textbf{`V188` 饱和定理}\ \text{适用} \Longrightarrow \text{无新信息} \Longrightarrow \text{封} ✓$$
$$\qquad \qquad \text{情形 B（不被蕴含）}：\text{则它是一个}\ \textbf{真正的新无条件算术输入} \Longrightarrow \text{恰好命中}\ \textbf{`V201` 重启闸门} \text{的开口} ✓✓✓$$

## §5 判词 ＋ 状态表 ＋ 边界

$$\boxed{\textbf{V252}：\text{与}\ \text{`V240`／`V241`}\ \text{同母题、不同杠杆};\ \text{杠杆＝带权 Markov 链＋次不变性} \Longrightarrow \text{揭示我们 `V241` 的 DEAD 只覆盖代数性障碍，}\textbf{不覆盖带权单边不等式类}};$$
$$\qquad \textbf{但输出＝统计型、引擎＝正性型} \Longrightarrow \textbf{两封口同时点火} \Longrightarrow \textbf{不携带 β};\ \textbf{两份净收获：Tao 独立提出"典范选择"问题 ＋ 该类产出新无条件不等式（命中 `V201` 开口）} ✓✓✓$$

| 项 | 判定 | 依据 |
|:--|:--|:--|
| 是否与我们同一片地 | **是**（整数解剖学／可除偏序） | `V240`／`V241`／`E180`–`E210` |
| 母题是否相同 | **是**（逐素数增删） | `V240` 递推＝"去 p_N" |
| 杠杆是否我们试过的 | **否**（次不变性 ≠ 非交换性） | `V241` 已证全交换 ⟹ 代数障碍必为零 |
| `V241` 的 DEAD 是否覆盖它 | **不覆盖**（只覆盖代数性/象征性障碍） | 本档 §2 |
| 输出类型 | 密度／统计 ⟹ `V188`／`V183` | 原文 |
| 引擎类型 | 正性（次不变性）⟹ `V199`／`V185`／`V244` 角 I | 原文 Lemma 6.1 |
| 是否携带 β | **否** | 全无零点/β/临界线 |
| Tao 的"链是否典范"问题 | ⭐ **＝我们的"无 canonical 选择"诊断（外部确认）** | Tao 博客 2026-06-09 |
| 新无条件不等式 | ⭐ **命中 `V201` 开口（唯一可查处）** | 本档 §4 |

$$\textbf{边界（诚实）}：\text{本档为}\ \textbf{三源核对的方法审计}（\text{项目页＋arXiv 摘要＋Tao 博客及评论}），\ \textbf{未逐行读完整篇 35 页论文} ⚠️;$$
$$\qquad \text{§2 的"母题相同"是本档判断};\ \text{§2 的"`V241` DEAD 不覆盖次不变性类"是本档}\ \textbf{[结构性]} \text{推论};\ \text{§4 的"命中 `V201` 开口"是}\ \textbf{待查} \text{（未做）；}$$
$$\qquad \textbf{不写"该方法不可能帮助 RH"};\ \textbf{未用 RH 作推导} ✓;\ \text{未跑 Lean} ✓;\ \textbf{零数值} ✓$$

```
⚠️ 委托（唐先生 21:55）"去拿那篇文献看看"
⚠️ 三源核对：① erdosproblems.com/1196（标 PROVED (LEAN)）② arXiv:2605.00301 "Primitive sets and von Mangoldt chains:
   Erdős Problem #1196 and beyond"（35 页 9 图，25 May 2026，math.NT/CO/PR；作者 Alexeev, Barreto, Li, Lichtman,
   Price, Shah, Tang, Tao）③ Tao 博客 2026-05-03 ＋评论（含 2026-06-09 Tao 本人回复）
⚠️ §1 方法与结果：
   #1196（Erdős–Sárközy–Szemerédi 1966）：primitive 集 A⊂[x,∞) ⟹ Σ 1/(a log a) < 1+o(1)；前记录 Lichtman
   < e^γ π/4 + o(1) ≈ 1.399；GPT-5.4 Pro 证 ≤ 1+O(1/log x)；并给 #164（≤ f(N_1)=1.6366…）、#1217、Banks–Martin 修正
   方法原文："new method ... based on Markov chains with von Mangoldt weights"；"seems to have been overlooked by the
   prior literature since Erdős' seminal 1935 paper"
   五件结构件：(a) 对偶 Remark 1.8（primitive 集界 ⟺ 某随机过程的 hitting 界；⚠️ 原文自陈不必然 Markov，" Markov
   过程似乎特别适合作为对偶过程的证书，仍略神秘"）(b) 可除偏序上 downward/upward Markov 链 (c) von Mangoldt 权
   ν_Λ；upward chain = down chain 关于 ν_Λ 的伴随 (d) ⭐次不变性 Lemma 6.1（doubly-harmonic 权）；配套 Mertens
   型估计 + Dirichlet eta 函数单调性 (e) ⭐"developmental anatomy of integers"（Tao）：整数不是静态实体，而是
   "an evolving process in which primes are added or removed over time"；"primitive sets can be viewed as singular
   moments in such a developmental process, which are only encountered at most once in the life cycle"
⚠️ §2 与 V240/V241 的关系：同一母题（逐素数增删）——V240 递推 A_N(X)=A_{N-1}(X)−A_{N-1}(X/p_N)；V241 生成元
   T_p f(X)=f(X)−f(X/p)，[T_p,T_q]=0；本文把同一步组织成 Markov 链
   ⭐ 关键差异：V241 赌注在非交换性（需 [T_p,T_q]≠0 + 非 coboundary holonomy），结论四族全 DEAD 且根因=算术非交换性
   =互反律=coboundary；本文杠杆不是非交换性，而是"带权 Markov 链 + 权次不变性"
   ⟹ 解释：我们找的是代数障碍（换位子/holonomy），有效杠杆是单边不等式（次不变性）；全交换族上非交换性必为零
   （V241 已证），但次不变性不必为零
   ⟹ 本档推论：V241 的 DEAD 针对象征性/代数性障碍，不覆盖"带权单边不等式"这一类
   ⚠️ 但两通道同时点火（对 β 无路）：(i) 输出=密度/统计 ⟹ V188 饱和/V183；(ii) 引擎=次不变性（正权单边不等式）
   ⟹ 正性通道 V199/V185/V244 角 I；(iii) 全无 ζ 零点/β/临界线
⚠️ §3 净收获一（⭐ Tao 把我们的问题提出来了）：Tao 博客评论 2026-06-09："is there a principle that selects an optimal
   chain from the anatomy of the integers themselves, rather than through trial-and-error construction? ... can the
   chain be derived from an invariant organizational property of the divisibility poset rather than chosen as an
   external tool? It seems this could lead to a classification of admissible divisibility processes"
   ⟹ 与本项目"无 canonical 选择"（V233-C / V215–V217 / V251 Gate 4）是同一个问题 ⟹ 外部独立确认
⚠️ §4 净收获二（唯一可查开口）：本文产出此前不存在的无条件算术不等式；V201 重启闸门要求的恰恰是"新的无条件输入"
   ⟹ 可查问题：是否存在 Erdős 和型不等式，不被显式公式蕴含，且与显式公式合用能约束零点？
   情形 A（被蕴含）⟹ V188 饱和 ⟹ 封；情形 B（不被蕴含）⟹ 真正的新无条件算术输入 ⟹ 命中 V201 开口
⚠️ §5 边界：三源核对的方法审计，未逐行读完整 35 页论文；§2"母题相同"为本档判断；"V241 DEAD 不覆盖次不变性类"为
   [结构性] 推论；§4 为待查；不写"该方法不可能帮助 RH"；未用 RH；未跑 Lean；零数值
✅ 净产出：① 三源核对该方法（原始文献到手，非二手）② 定位其与我们 V240/V241 同母题、杠杆不同（次不变性≠非交换性）
   ③ ⭐ 推论：V241 的封口不覆盖"带权单边不等式"类 ④ ⭐ 净收获一：Tao 独立提出"链是否典范"＝我们的"无 canonical 选择"
   ⑤ ⭐⭐ 净收获二：该类产出新无条件不等式，正命中 V201 开口（唯一可查处）⑥ 判词：不携带 β（统计型输出＋正性型引擎，
   两通道同时点火）
```
