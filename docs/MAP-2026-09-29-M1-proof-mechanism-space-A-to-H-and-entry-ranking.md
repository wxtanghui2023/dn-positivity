# MAP-2026-09-29-M1 — 证明机制空间（A–H）展开 ＋ 逐项查重 ＋ 入口排序

> 空间 B｜非 C 号｜唐先生 23:02 方法论纠正：「我们**不在**优化一条已有道路，而在寻找**第一条能走通的道路**」✓
> ｜**不主张任何新值**（V290）
> 时间：2026-09-29 23:3x

**已查地图**：`CLOSED-ROUTES-MAP`（L3256 禁形｜L3272–3276 开邻域｜L3460–3482）／`MASTER-FAILURE-MAP` §2–§6／`ASSETS-REGISTRY`（L745／L1882–1905／L3392／L3937）／`ROUTE-FINGERPRINTS.tsv`／今晚 `zg–zl` ＋ `ERRATUM-n1`
D0: 本档对象 = **证明动作（机制）之分类与查重**（新数学对象：无 ✗；新工具：机制清单 ⚠️）
D1: 0（产出 = **机制地图 ＋ 入口排序** ⚠️✓）

---

## §0 为什么需要这张图（唐先生的诊断成立 ✓）

$$\text{档案 200+ 档的绝大多数属\ \textbf{同一个坐标系的局部搜索}:\ \text{选可计算量}\to\text{恒等式}\to\text{不等式}}$$
$$\text{今晚的类级标定（}AUDIT\text{-}zj\text{）是**独立证据**}:\ \text{该类在 }n{=}9\ \text{连 }M{=}61\ \text{都判可行}\ ✗✗$$
$$\therefore\ \text{下一步须在\ \textbf{证明动作空间}\ 中找入口，而非再加一个数值量}\ ✓$$

## §1 机制空间 A–H：含义 · 档案查重 · 入口

| # | 机制 | 对 $K(10,1)$ 的具体含义 | 档案状态 | 可执行入口（判定标准） |
|---|---|---|---|---|
| **A** | 强迫**存在**某局部构型 | 由覆盖＋计数证"任何 106-码必含构型 $\mathcal X$" | **主力**，且**多数已死**：`R08` hole 强制 $=$ NO-MECHANISM ✗；`AUDIT-29x` 无强制 excess ✗ | 已被否 ✗（勿再走"强制型"） |
| **B** | 强迫**不存在**某局部构型（禁形） | 证"构型 $\mathcal Y$ 在 $Q_{10}$ 中不可能" | **试过 1 例**：`D4-5` 局部禁形 $x\!-\!1\!-\!p\!-\!2\!-\!q$ ⟹ **存在 3655/5472** ✗（被反例推翻） | 需**系统性**枚举禁形候选（非单个猜）|
| **C** | 交换／替换**构造更优** | 由 120-码做 $j$-for-$(j{-}1)$ 得 $\le119$ | **低阶已做**：单删 0/120、2-for-1 0/7140（`AUDIT-28r`）✗；**3-for-2 档案列为"未做候选"** | ★**本档已执行**（见 §2）|
| **D** | 极值构型的**刚性** | 证"若 $M{=}106$ 则结构被钉死" | 部分：匹配定理 $A_1\le59$／$A_1\le49$；`LEMMA-L1`（今晚）| 刚性强但**不足以成矛盾** ⚠️ |
| **E** | **分类**全部边界构型 | 把"离最优最近"的构型分类穷举 | 部分：三点 orbit **13 型**（`RESULT-29p`）／`P12-PASS` 支撑层分类 | 需与**可实现性**接合 ⚠️ |
| **F** | **映射到另一有限对象** | 把二元 $n{=}10$ 覆盖码映到**混合字母表**等族，借其更强的定理 | **几乎未试**：fiber＝`R05 EXACT-RESTATEMENT` ✗（已封）；**混合码 = BÖW 之历史机制**（原文不可得）| ★**最高杠杆未试入口**（见 §3）|
| **G** | **对称性商** | 用 $\operatorname{Aut}(Q_{10})$ 商掉构型做计数/穷举 | 部分：定理 A（不变泛函 $\le105.2223$）为**否证**型 ✗ | 商掉构型后**穷举**（非泛函）⚠️ |
| **H** | **局部规则传播**成全局矛盾 | 一条局部蕴含沿立方体传播 | 部分：`WITSTAR`/`WITGA` 之 "private witness propagation"；今晚 `L1` | ★以 `L1` 为种子做**传播闭包**（见 §3）|

## §2 机制 C 的可执行入口：3-for-2 穷举（**本档已执行**）

$$\text{找 }T\subseteq C\ (|T|{=}3),\ W\subseteq Q_{10}\ (|W|{=}2):\quad (C\setminus T)\cup W\ \text{仍覆盖}\ \iff U(T)\subseteq\textstyle\bigcup_{w\in W}N[w]$$
$$\text{其中 }U(T):=\{x:\ \mathrm{own}(x)\subseteq T\};\ \text{高效法：对每对 }W\ \text{先算 }M,\ \text{再取 }Good{=}\{c:\mathrm{priv}(c)\subseteq M\}\ (\text{必要条件})$$
**脚本** `scripts/three_for_two_n10.py`；**读数见 `out/three_for_two.log`**（本档运行中）

## §3 入口排序（**我的判断**）

$$\boxed{\textbf{① F（映射到另一有限对象）}——\text{唯一有"历史有效性"背书的机制}:\ 107\ \text{正是由混合码框架产出}}$$
$$\qquad\therefore\ F\ \text{是"未找到的机制"之\ \textbf{fingerprint}（与唐先生/GPT 之判一致 ✓）；且}R05\ \text{只封了 fiber 一种映射，非全部}$$
$$\boxed{\textbf{② H（局部规则传播）}——\text{以今晚 }L1\ \text{的局部刚性为种子做闭包}}$$
$$\qquad(\text{局部刚性}\to\text{蕴含图}\to\text{传播至全局矛盾};\ \text{与 }A\ \text{的"计数版"本质不同})$$
$$\boxed{\textbf{③ G（对称性商 ＋ 穷举）}——\text{把"构型分类"（E）升级为\ \textbf{商空间上的有限穷举}}}$$
$$\qquad(\text{注意}\ G\ \text{对\ \textbf{泛函}\ 已被定理 A 否证};\ \text{但对\ \textbf{构型计数/穷举}\ 未被否证}\ ⚠️)$$

## §4 边界（硬 ✓）

- **不主张**任何新值；本档为**方法论地图**（不产生数学结果）⚠️✓
- 已明确区分"**机制 A 的计数版已死**"与"**A 本身**"，避免把机制层与实现层混为一谈 ✓
- 未取论文原文（R16–17）／未重攻 pair 层（R02）／fiber（R05）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA

---

## §2.1 机制 C 入口**执行结果**（3-for-2，**已完成**）✓✓

**实跑**（`scripts/three_for_two_n10.py`，日志 `out/three_for_two.log`）：

$$\text{[验证]}\ 2\text{-for-}1\ \text{复算} = \mathbf{0}\ \text{命中（与档案 }0/7140\ \text{一致）} \Longrightarrow \text{算法可信}\ ✓$$
$$\text{[主搜索]}\ 3\text{-for-}2:\ \text{全扫 } \mathbf{523{,}776}\ \text{对（}\binom{1024}2\text{）},\ \text{其中 }Good{\ge}3\ \text{者} = \mathbf{0}\ \Longrightarrow\ \textbf{穷举下 3-for-2 不可能}\ ✗$$

$$\boxed{\text{结构原因（可作引理）}:\ \text{对\ \textbf{任意}两词 }\{v,w\}\subseteq Q_{10},\ \#\{c\in C:\ \mathrm{priv}(c)\subseteq N[v]\cup N[w]\}\ \le\ \mathbf 2}$$
$$\qquad\text{而有效 3-for-2 需三个此类码字} \Longrightarrow \textbf{永不可能};\ \text{（}\mathrm{priv}\ \text{= 私有域，}Q_{10}\ \text{中 120-码之 }\Sigma|\mathrm{priv}|{=}801,\ \text{均值 }6.675\text{）}$$

$$\therefore\ \text{档案「未做候选 ①」}\ \textbf{现已闭合};\ \text{机制 C 在该码上的局部替换阶梯}\ \ge3\ \text{阶\ \textbf{全负}}\ (2\text{-for-}1\ ✗\to3\text{-for-}2\ ✗)$$

**下一阶（4-for-3）之判据（供续线）**：需 $\exists$ 四词 $T$ 与三球 $W$ 使 $\Sigma_{c\in T}|\mathrm{priv}(c)|\le|M_W|{\le}33$；由均值 $6.675$ 知计数上**勉强可行**（$\approx26.7{\le}33$）⟹ 须实算；
但 $W$ 之三元组 $\binom{1024}3{=}1.78\times10^8$ 太大 ⟹ 须换向：**从 $T$（$\binom{120}4{=}8.2\times10^6$）出发**算 $U(T)$ 再判"3 球可覆盖性"（小集覆盖，可精确解）⚠️
