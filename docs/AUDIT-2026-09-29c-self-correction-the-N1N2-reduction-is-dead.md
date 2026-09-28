# AUDIT-2026-09-29c — **★自查纠错：$N_1{+}N_2$ 归约\ \textbf{失效}（框架等价于球界）；路线 (A) 当场死亡**

> **性质**：**自查纠错 ＋ 路线判定**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 08:4x ✓
> **唐先生令（逐字）**：「A」（攻 pair 数上界）✓

**已查地图**：★**推翻本线** `AUDIT-29b` §2 之"归约" ⚠️

D0: 本档对象 ＝ **档案已有**（恒等式／van Wee 框架——无新数学对象 ✓）
D1: 0（产出＝**一处自查纠错 ＋ 一条路线判定** ⚠️✓）

---

## §0 结论（先给，含纠错）

$$\boxed{\text{① ✗✗ 自查纠错}:\ \texttt{AUDIT-29b}\ \S2\ \text{之"归约"}\ \textbf{无效};\ N_1{+}N_2\ \text{框架不能闭合}}$$
$$\boxed{\text{② 另一处数字错}:\ \texttt{AUDIT-29b}\ \S3\ \text{所写"下界 }117"\ \textbf{应为 }71\ (\text{C-S 实为 }41)}$$
$$\boxed{\text{③ ★ 根因}:\ \text{上下界之差} ＝ 25M-2310>0\ (M>92.4) \Longrightarrow \textbf{该框架仅等价于球界}}$$
$$\boxed{\text{④ ⟹ 路线 (A)\ \textbf{当场死亡};\ 建议转 (B) 高阶 SDP 或 (C) 取原文}}$$

## §1 ★ 纠错之实测（**✓✓**）

$$\text{恒等式}:\ 4(N_1{+}N_2)=E+\sum_x\delta(x)^2,\qquad E=11M-1024$$
$$\text{下界（}\delta^2\ge\delta\text{）}:\ \sum\delta^2\ge E\ \Longrightarrow\ N_1{+}N_2\ \ge\ E/2$$
$$\text{上界（van Wee 路线）}:\ 4(N_1{+}N_2)\le122M-11288\ \Longrightarrow\ N_1{+}N_2\ \le\ (122M-11288)/4$$

| $M$ | $E$ | 下界 $E/2$ | C-S 下界 | van Wee 上界 |
|---|---|---|---|---|
| $106$ | $142$ | $\mathbf{71}$ | $40.4$ | $\mathbf{411.0}$ |
| $107$ | $153$ | $77$ | $44.0$ | $441.5$ |
| $120$ | $296$ | $148$ | $95.4$ | $838.0$ |

$$\therefore\ M{=}106:\ \boxed{71\ \le\ N_1{+}N_2\ \le\ 411}\ \Longrightarrow\ \textbf{下界}\not>\textbf{上界}\ \Longrightarrow\ \text{无矛盾}\ ✗$$
$$\text{（注}:\ \texttt{AUDIT-29b}\ \S3\ \text{所写"下界 }117"\ \text{系误读（把 }2(N_1{+}N_2)\ \text{之下界当成 }N_1{+}N_2\text{）};\ \text{正确下界 }=\max(71,41)=71\ ⚠️\text{）}$$

## §2 ★ 根因（**本档核心 —— 为何该框架必死 ✓✓**）

$$\text{上界}-\text{下界}=\frac{122M-11288}{4}-\frac{11M-1024}{2}=\frac{100M-9240}{4}=25M-2310$$
$$\therefore\ 25M-2310>0\iff M>92.4\ \Longrightarrow\ \boxed{\text{该框架\ \textbf{仅在 }M\le92\ \text{时排除}\ } \Longrightarrow \text{等价于球界（}\lceil1024/11\rceil=94\text{）级}}✗✗$$
$$\therefore\ \boxed{\text{van Wee 之论证\ \textbf{不能}改写为"对 }N_1{+}N_2\ \text{之双边夹逼"——其力量来自 }A\ (\text{deep holes})\ \text{之结构，而非 }N_1{+}N_2}$$
$$\text{（故 }\texttt{AUDIT-29b}\ \S2\ \text{之"自证出档案所述缺件"为\ \textbf{误判}；该上界与所需方向无关 ⚠️）}$$

## §3 路线判定（**照唐先生令之 (A) ✓**）

$$\text{路线 (A) ＝ "攻 pair 数上界"}\ \Longrightarrow\ \text{其自然框架（}N_1{+}N_2\text{）}\ \textbf{已证等价于球界} \Longrightarrow \boxed{\text{(A) 死亡}}✗$$
$$\text{若要 (A) 复活，需\ \textbf{非} }N_1{+}N_2\ \text{之量};\ \text{但本会话已实测: 全部 }\Phi(A_j)\ \text{型量（}\)excess／shell／induced／FM／}\theta\text{）皆止于 }103{-}104$$
$$\therefore\ \boxed{\text{在\ \textbf{可实现之算术族}内，(A) 无入口};\ \text{须转 (B) 或 (C)}}$$

## §4 当前总账（**诚实收束 ✓**）

| 路线 | 现状 |
|---|---|
| 可实现算术族（7 族） | $\mathbf{103}$（上确界） |
| $\theta$ 精化 | $\approx104$（被真实码 $\theta{=}8.31$ 卡住） |
| $N_1{+}N_2$ 框架 | **等价球界**（本档） |
| level-3 SDP（Gijswijt--Polak 2025） | $\mathbf{105.2223}\Rightarrow K\ge106$ |
| **(B)** 高阶 SDP | **未做**（或可 $>106$） |
| **(C)** Zhang 1991／BÖW 2004 原文 | **未得**（付费墙） |
| **(D)** 待查：107 是否有\ \textbf{其他}来源 | 未查 |

$$\boxed{\text{结论}:\ \text{我们\ \textbf{未能}复现 }107;\ \text{缺口确实存在于"覆盖效率"之外——须非松弛型（integrality）论证}}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "归约失效" "自查纠错" "框架等价球界"
技术词 归约失效    命中文件数=0    ::
技术词 自查纠错    命中文件数=0    ::
技术词 框架等价球界  命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **自查 ＋ 实测**（含推翻本线前档）✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- **不主张** $107$ 不可达 ✗（V290）；**不主张** (B) 必成 ✗
