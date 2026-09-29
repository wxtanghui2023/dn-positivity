# REFUTE-2026-09-30b — 修订版之核心一步 **"A 型 ⟹ C-C 距离-1 边" 被真实码推翻**（A2 子情形占 89%）

> 空间 B｜非 C 号｜唐先生 00:03 之修订版 P1 链｜**本档为验证档：结论＝该链仍断**（不主张任何值，V290）

**已查地图**：承 `REFUTE-2026-09-30`（第一版反例）／`DEFS-2026-09-29`／`AUDIT-28q`（$A_1\le59$ 属 119 线 $Q{=}1$ 语境）
D0: 本档对象 = **档案已有**（$\delta,a_1,r$ 之局部分布）之**实测反证**（新数学对象：无 ✗）
D1: 0（产出 = **第二处反例 ＋ 第二处遗漏子情形定位** ⚠️✓）

---

## §0 判定（先给）

$$\boxed{\text{修订版之核心一步}\ \text{"A 型}\Rightarrow\{c,d\}\ \text{之 C-C 距离-1 边"}\ \textbf{被真实码推翻}\ ✗✗}$$

| 类（120-码） | 计数 | 占比 |
|---|---|---|
| $\delta{=}1,\ a_1{=}1$ 之非码字点 | **338** | 100% |
| 其中 **A1**（excess 落码字 $c$）| **37** | 11% |
| 其中 **A2**（excess 落非码字邻点）| **301** | **89%** ✗ |

$$\text{其唯一码字 }c\ \text{之}\ e(c)\ \text{分布} = \{0{:}\mathbf{301},\ 1{:}37\} \Longrightarrow \textbf{89\% 情形 }e(c){=}0\ \text{（}c\ \text{无距离-1 码字邻居）}\ ✗$$

## §1 根因：A2 子情形（**第三次同型遗漏**）

$$\text{设 }a_1(v){=}1,\ \delta(v){=}1\ (\text{平移 }v{=}0,\ c{=}e_1,\ a_2{=}5);\ \text{excess 落点 }p\in\{e_1,\dots,e_{10}\}\ \text{三档}:$$
$$\textbf{A1}:\ p{=}e_1\Longrightarrow \mu(e_1){=}2\Longrightarrow e(c){=}1\Longrightarrow c\ \text{恰有 1 个距离-1 码字邻居}\ ✓\ (\text{唐先生所论})$$
$$\textbf{A2}:\ p{=}e_j\ (j{\ge}2)\Longrightarrow \mu(e_j){=}2,\ \text{且}\ \mu(e_1){=}1\Longrightarrow e(c){=}0 \Longrightarrow \textbf{无 C-C 边可计}\ ✗$$
$$\qquad\text{A2 之局部结构}: \text{5 个距离-2 码字皆不含坐标 1};\ \text{其在 }\{2..10\}\ \text{上诱导度列} = (2,1,1,\dots,1)$$
$$\qquad(\text{一端点为 2 度，其余 8 点为 1 度};\ \Sigma\deg{=}10{=}5\ \text{边}\times2\ \text{端点}\ ✓\ \textbf{自洽，无矛盾})$$
$$\therefore\ \text{A2 完全相容（占实测 89%）} \Longrightarrow \text{"A 型}\Rightarrow\text{C-C 边" 为假} \Longrightarrow \boxed{n_A\le9A_1\ \textbf{不成立}}$$

## §2 对全链之影响

$$\text{原链}:\ n_1\le9A_1{+}2A_2\Longrightarrow\Sigma_{v\notin C}\delta\ge1692-4A_2>1562-4A_1-4A_2$$
$$\text{其中 A 型计数支（}n_A\le9A_1\text{）\textbf{失效}} \Longrightarrow \text{该链\ \textbf{再次断裂}}\ ✗$$
$$\text{（A2 型点无 C-C 边可收费；其可用结构仅为"5 词在 9 点上之度列}"，尚未转化为对 }A_1,A_2\ \text{之计数）}$$

## §3 承重假设 `A₁ ≤ 59` 之框架核查（**顺带**）

$$\text{档案 }ASSETS\text{-}REGISTRY\ L3479:\ \text{119 线参数现状}\ 0\le A_1\le49,\ A_2\in[94,143],\ 2A_2-3=283-2A_1$$
$$\qquad\Longrightarrow A_1{+}A_2=143=\tfrac{286}2=\tfrac12\Sigma\binom{\mu}2\ \text{（}M{=}119,\ E{=}285\text{）} \Longrightarrow \textbf{与本框架同层 ✓（非 P/Q 的另一物）}$$
$$\text{但该界之得出依赖 }Q{=}1\ \text{（profile }740,283,1\text{）；}M{=}106\ \text{无此假设} \Longrightarrow \text{不可直接借用} ⚠️$$
$$\text{且实测}: M{\approx}146\text{--}153\ \text{之覆盖码 }A_1\ \text{可达 }82 \Longrightarrow \textbf{"}A_1\le59\text{" 非 }M\text{-无关之普遍定理} ⚠️$$

## §4 本档保留／作废

$$\text{保留}:\ \text{二型分类 }(a_1,a_2)\in\{(1,5),(2,4)\}\ ✓;\ n_B\le2A_2\ ✓\ (\text{B 型映射到距离-2 对，2 中点 ✓});\ \text{恒等式}\ \Sigma_{v\notin C}\delta=1562-4N_{\le2}\ ✓$$
$$\text{作废}:\ n_A\le9A_1\ \text{及其下游}\ ✗$$

## §5 边界（硬 ✓）

- **不主张**任何新值；本档为**反例档**（$K(10,1)\ge107$ 之修订链未成立）✗
- 未取论文原文（R16–17）✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
