# AUDIT-2026-09-29m — **"真者系统"可行域\ \textbf{非空}（无内禀矛盾）；所需 $A_3\le552$ 与密度趋势\ \textbf{相冲}**

> **性质**：**整数规划可行性 ＋ 趋势核验**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 11:1x ✓
> **唐先生令**：「继续」（跑最小整数规划）✓

**已查地图**：接续 `AUDIT-29l`（校正后之真者系统）／`29k`（$N_1{+}N_2\le161$）✓

D0: 本档对象 ＝ **档案已有**（$A_1,A_2,A_3$／(N)——无新数学对象 ✓）
D1: 0（产出＝**可行性判定 ＋ 唯一所需约束之定位 ＋ 趋势否证** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ 真者系统\ \textbf{可行域非空}}:\ \text{可行点 }(A_1,A_2,A_3)=(71,0,582)\ \Longrightarrow\ \textbf{无内禀矛盾}}$$
$$\boxed{\text{② 系统强制 }A_3\ \ge\ \mathbf{552};\ \text{须一条独立上界 }A_3\le552\ \text{方能与 (N) 碰撞}}$$
$$\boxed{\text{③ ✗✗ 但该上界与趋势相冲}:\ A_3/\binom M2\approx0.122{-}0.128\ \text{稳定}\Rightarrow M{=}106\ \text{时}\ A_3\approx696>552}$$
$$\boxed{\text{④ ✓ 唯一近饱和之约束} ＝ A_1{+}A_2\le161\ (\text{趋势}\approx156);\ \text{而锐化它\ \textbf{正是已证死的 }\theta\ \text{问题}}}$$

## §1 ① 可行性（**✗ 决定性**）

$$\text{变量 }(A_1,A_2,A_3)\ \text{之约束}:\quad 0\le A_1\le71;\quad A_1+A_2\le161;\quad 9A_1+A_2+3A_3\ge2385;\quad A_1+A_2+A_3\le\binom{106}2=5565$$
$$\text{LP 判定}:\quad \textbf{可行}\ ✓\quad\text{可行点例}:\ (A_1,A_2,A_3)=(71,\ 0,\ 582)$$
$$\therefore\ \boxed{\text{本会话所建\ \textbf{全部}真者约束\ \textbf{不构成}对 }M{=}106\ \text{的排除}}✗$$

## §2 ② 唯一所需约束之定位（**✓**）

$$\text{若再给一条 }A_3\ \text{之上界，则需 }A_3\ \le\ 552\ \text{方可碰撞}:\ \text{由}\ \max(9A_1+A_2)=729\ (A_1{=}71,A_2{=}90)\ \Longrightarrow\ 3A_3\ge2385-729=1656$$
$$\therefore\ \boxed{A_3\ \ge\ \mathbf{552}\ \text{被强制}};\qquad \text{排除 }106\ \text{需}\ \boxed{A_3\le552}\ \text{型独立上界}$$

## §3 ③ 趋势否证（**✗✗**）

| $M$ | $A_1$ | $A_2$ | $A_3$ | $A_1{+}A_2$ | $A_3/\binom M2$ |
|---|---|---|---|---|---|
| $120$ | $50$ | $149$ | $912$ | $199$ | $0.1277$ |
| $128$ | $62$ | $197$ | $1016$ | $259$ | $0.1250$ |
| $140$ | $72$ | $272$ | $1210$ | $344$ | $0.1244$ |
| $155$ | $99$ | $367$ | $1458$ | $466$ | $0.1222$ |
| $161$ | $107$ | $404$ | $1574$ | $511$ | $0.1222$ |

$$\therefore\ A_3/\binom M2\ \approx\ 0.122{-}0.128\ (\textbf{稳定})\ \Longrightarrow\ M{=}106:\ A_3\ \approx\ 0.125\cdot5565\ \approx\ \mathbf{696}\ \gg\ 552$$
$$\therefore\ \boxed{\text{所需之 }A_3\le552\ \text{要求密度}\le0.0992,\ \textbf{比实测低 }\approx21\%\ \Longrightarrow\ \text{与该族趋势\ \textbf{相冲}}}}✗✗$$
$$\text{（诚实标注}:\ \text{趋势由 }M\ge120\ \text{之码外加码字测得};\ \text{外推到 }106\ \text{系\ \textbf{假设}，非定理}⚠️\text{）}$$

## §4 ④ 唯一近饱和之约束（**✓ 关键读数**）

$$A_1+A_2\ \text{之趋势}:\ M{=}106\ \text{外推}\approx0.028\cdot5565\approx\mathbf{156}\ \text{vs 上界 }161\ \Longrightarrow\ \textbf{近饱和（差 }5\text{）}$$
$$\text{而该上界之来源}:\ \sum_{x\in A}(\text{球 excess})=11E-4(N_1{+}N_2)\ \ge\ |A|\ \text{＋}\ \text{van Wee 之逐点界}\ |A\cap B(z,1)|\le n{-}R=9$$
$$\therefore\ \text{锐化它} \Longleftrightarrow \theta\ \text{从 }9\ \text{降};\ \text{而 }\theta\ \text{问题本会话已证死}:\ \text{实测 }\theta{=}8.31\Rightarrow\ \text{极限}\approx104\ ✗$$
$$\therefore\ \boxed{\text{唯一近饱和之链恰是\ \textbf{已封之链}}};\ \text{其余约束\ \textbf{大面积松}}}$$

## §5 本轮净结论（**收束 ✓✓**）

$$\boxed{\text{所有 106-specific 真者约束皆可行且大部分松；唯一近饱和者之锐化 ＝ 已封之 }\theta\ \text{问题}}$$
$$\therefore\ \text{须之新约束}\ \textbf{不属于}"计数/奇偶/excess"型}\ (\text{本会话已系统覆盖});\ \text{指向\ \textbf{几何构型}（深洞邻接图之局部形状）或\ \textbf{原文}}\ (BÖW)$$
$$\text{（与 }\texttt{AUDIT-29d/e}\ \text{一致}:\ 107>105.2223=\text{最强松弛}\Rightarrow\text{须非松弛型机制）}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "可行域非空" "A3下界552" "密度趋势"
技术词 可行域非空   命中文件数=0    ::
技术词 A3下界552   命中文件数=0    ::
技术词 密度趋势    命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **LP 可行性 ＋ 六档趋势实测** ＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）；趋势外推**系假设** ⚠️
