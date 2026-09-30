# DECISION-2026-09-30-m82 — 判定实验：**$n{=}9$ 最优码（62 词）$m=\mathbf{82}$**（非 0）⟹ **阈值现象存活 ✓**；且 $m$ **不是 $A_2$-账之重述** ✓

> 空间 B｜非 C 号｜唐先生 10:24「纯判定实验：用 KERI 62-码测 $m$」｜**不主张任何新值**（V290）
> 时间：2026-09-30 11:5x

**已查地图**：承 `REFUTE-2026-09-30e`（$n{=}8$ 阈值被否，$m{=}0$ 可达）／`EXPLORE-m0`／`ANALYSIS-INV2`
D0: 本档对象 = **档案已有**（KERI 62-码 ＋ $m$ 定义）之**判定测量**（新数学对象：无 ✗）
D1: 0（产出 = **一条判定（阈值存活） ＋ 一条独立性判定 ＋ 一处常数更正** ⚠️✓）

---

## §0 判定（**三支选择中落在"第 3 支"**）

$$\boxed{\textbf{① }m=\mathbf{82}\ \text{（最优 }n{=}9,M{=}62\text{ 码）}\ \ne0 \Longrightarrow \text{阈值不在 }n{\le}8\text{ 之内侧};\ n{=}9\ \text{起 }m\ \text{被迫远离 0}\ ✓}$$
$$\boxed{\textbf{② }m/(2^n{-}M)=0.182\ >\ \text{所需 }c{>}0.046 \Longrightarrow \text{量级信号\textbf{正向}（与七条已否路线不同）} ✓}$$
$$\boxed{\textbf{③ }m\ \textbf{不是 }A_2\text{-账之重述}:\ \text{两码 }A_2{=}66\ \text{与 }47\ \text{相差甚远，而 }m\ \text{与 }(a_1{+}a_2)\text{-分布\ \textbf{完全相同}}\ ✓}$$

## §1 判定数据（**KERI 62-码 ＋ classif 两码，皆覆盖校验 ✓**）

| 码 | $M$ | $A_1$ | $A_2$ | $(a_1{+}a_2)$ 分布 | $\Sigma\max(0,a_1{+}a_2{-}6)$ | $\mathbf m$ | $m/(2^n{-}M)$ |
|---|---|---|---|---|---|---|---|
| KERI 62-码 | 62 | 7 | 66 | $\{5{:}148,\ 6{:}220,\ 7{:}72,\ 8{:}10\}$ | 92 | **82** | 0.182 |
| classif-A | 62 | 7 | 66 | 同 上 | 92 | **82** | 0.182 |
| classif-B | 62 | **26** | **47** | 同 上（**同一分布**） | 92 | **82** | 0.182 |
| 120-码（$n{=}10$） | 120 | 50 | 149 | $\{6{:}338,7{:}417,8{:}106,9{:}29,10{:}8,11{:}6\}$ | 778 | **566** | 0.626 |

$$\textbf{恒等式核验}:\ \sum_{v\notin C}(a_1{+}a_2)=M\bigl(n+\tbinom n2\bigr)-2(A_1{+}A_2);\quad n{=}9,M{=}62:\ 2790-146=2644=\Sigma\ \text{分布} ✓✓$$

## §2 **一处常数更正**（本档自查）

$$\text{球 excess 恒等式之常数是 }(n{+}1)\ (\textbf{非固定 11}):\quad \delta_{N[v]}=(n{+}1)\mathbf1_{v\in C}+2a_1+2a_2-(n{+}1)$$
$$\therefore\ n{=}9\ \text{之"INV2"是 }a_1{+}a_2\ \ge\ \mathbf5\ \ (\text{因 }\delta=2(a_1{+}a_2)-10\ge0);\ \text{而 }n{=}10\ \text{才}\ \ge\mathbf6$$
$$\qquad\text{实测吻合}:\ n{=}9\ \text{码之 }(a_1{+}a_2)\ \text{最小值}=5\ ⟹ \min\delta=0 ✓;\quad n{=}10\ \text{之最小值}=6\ ⟹ \min\delta=1 ✓$$
$$\text{（注：唐先生 §1 之 }m=\Sigma\max(0,6-a_1-a_2)\ \text{恒为 0（因该式是"亏损"且已被下界排除）⟹ 本档沿用既有定义 }m:=\#\{a_1{+}a_2\ge7\} ✓）$$

## §3 为何②③是本线第一次**正向**信号

$$\text{前七轮之否证模式}:\ \text{提案之不等式在\textbf{真实码上被直接违反}（}n_A{\le}9A_1,\ P{\ge}181,\ H_{11},\ R,\ n{=}8\ \text{阈值…）\ ✗}$$
$$\text{本档}:\ \text{所测之 }m\ \text{在最优尺寸处\ \textbf{天然远离 0}（}82\text{）且比值 0.182 高于所需 0.046}\ ✓\ \text{且}\ \textbf{与 }A_2\ \text{无关}（A_2{=}66/47\ \text{同 }m） ✓$$
$$\Longrightarrow\ m\ \text{是\ \textbf{独立于 }A_2\text{-账} 的结构量（不像 }H_{11}/R\ \text{那样是从属量）} ✓$$

## §4 **警戒**（唐先生已指出，本档固化）

$$\text{本档只测了 }3\ \text{个（且可能同源的）最优 }n{=}9\ \text{码} \Longrightarrow \textbf{不能推出"所有 }M{=}62\ \text{码皆 }m{\ge}82\text{"} ⚠️$$
$$\text{要变成证明，须攻}:\ \textbf{“一切 }(n{=}9,M{=}62)\ \text{覆盖码皆 }m\ge82\text{”}\ \text{或至少 }m\ge1$$

## §5 后续（**可执行，按优先级**）

$$\textbf{(甲)}\ \text{更多最优 }n{=}9\ \text{码}:\ \text{从 KERI 索引页（}\texttt{sources/KERI-CD-index-page-snapshot.html}\text{）或文献表提取更多 62-码样本 ⟹ 检验 }m{=}82\ \text{是否为类函数} ✓$$
$$\textbf{(乙)}\ \text{对已知 62-码作保覆盖之扰动（局部替换、自同构群之商）} \Longrightarrow \text{测 }m\ \text{之稳健性} ✓$$
$$\textbf{(丙)}\ \text{若 }m\ \text{为类函数}（\text{仅依赖 }n,M\text{）} \Longrightarrow \text{则本线可化为\ \textbf{类函数定理}（比"存在性"论证干净得多）} ✓$$
$$\textbf{(丁)}\ \text{若 }(\甲)(乙)\ \text{显示 }m\ \text{可被压到小值} \Longrightarrow \text{本线亦否；届时按 §6 归档} ⚠️$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**判定测量 ＋ 一处常数更正** ✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
