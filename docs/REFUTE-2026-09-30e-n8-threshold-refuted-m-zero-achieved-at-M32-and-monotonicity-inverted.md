# REFUTE-2026-09-30e — $n{=}8$ 阈值**被否**（$M{=}32$ 之真覆盖码 $m{=}\mathbf0$，已验证 ✓）；单调性**反向**（加词只增 $m$）⟹ 按 §8 判据 **CLOSED-INSUFFICIENT**

> 空间 B｜非 C 号｜唐先生 10:16「压 $n{=}8$ 阈值，先做单调性 ＋ local 分类」｜**不主张任何新值**（V290）
> 时间：2026-09-30 11:4x

**已查地图**：承 `EXPLORE-2026-09-30-m0`／`ANALYSIS-INV2`／`AUDIT-29j`
D0: 本档对象 = **档案已有**（$m$、$(a_1{+}a_2)$ 层）之**覆盖校验实测**（新数学对象：无 ✗）
D1: 0（产出 = **一条阈值否证 ＋ 一条单调性反向 ＋ 一条方法学预筛** ⚠️✓）

---

## §0 判定（先给）

$$\boxed{\textbf{① 阈值否证}:\ \text{存在\ \textbf{已验证} 之\ }n{=}8,\ M{=}32\ ({=}K(8,1))\ \text{覆盖码，其 }m=\mathbf0\ \Longrightarrow\ \text{"}n{=}8\Rightarrow m\ge23\text{"}\ \textbf{为假}}\ ✗✗}$$
$$\boxed{\textbf{② 单调性反向}:\ C\to C\cup\{x\}\ \text{之}\ \Delta m\ \textbf{恒}>0\ (\Delta m\in[+3,+20],\ \text{无一个 }\le0) \Longrightarrow\ \text{不可归约到 }M{=}44\ \text{之最坏情形}\ ✗}$$
$$\boxed{\textbf{③ 按唐先生 §8 判据}:\ n{=}8\ \text{存在 }m\le22\ \text{之真覆盖码（}m{=}0,11,22\text{）} \Longrightarrow\ \textbf{CLOSED-INSUFFICIENT}\ ✓}$$

## §1 Test A：单调性（实跑，$n{=}8$）

$$C\to C\cup\{x\}\ (x\notin C):\ \Delta m\ \text{分布（5 个码，各 ~200 个 }x\text{）} =\ \{3{:}3,4{:}8,\dots,18{:}1\}\ \textbf{全为正}\ ✓$$
$$C\to C\setminus\{c\}\ (\text{仍覆盖时}):\ \Delta m=-7\ (\text{删词亦增 }m)\ \text{或不可删}$$
$$\therefore\ \textbf{加词使 }m\ \text{上升（非下降）} \Longrightarrow\ \text{“}M\ \text{越大越坏”之假设\ \textbf{反向}};\ \text{小 }M\ \text{才是 }m\ \text{较小之区} ✗$$

## §2 Test B：$n{=}8$ 之 $(M,m)$（**全部覆盖校验 ✓**）

| $M$ | $m$ | 备注 |
|---|---|---|
| **32** | **0** | $=K(8,1)$ **最优尺寸** ✓✓ |
| 35 | 11 | ✓ |
| 37 | 22 | ✓ |
| 39 | 55, 59, 61 | ✓ |
| 40 | 60, 65 | ✓ |

$$\therefore\ m{=}0\ \text{在 }n{=}8\ \textbf{可达}（且在最优点 }M{=}32\text{）;\ m\ \text{随 }M\ \text{单调上升} \Longrightarrow \textbf{“}n{=}8\ \text{阈值”不存在} ✗$$

## §3 加倍测试（$n{=}8\to n{=}9$）

$$\text{将 }(n{=}8,M{=}32,m{=}0)\ \text{码加倍}: C'=\{(c,0),(c,1)\}\ (M{=}64)\ \Longrightarrow\ \text{覆盖 ✓ 但}\ m=\mathbf{64}\ ✗\ (\text{性质\ \textbf{不被保持}})$$
$$\text{又 }n{=}9\ \text{之裁剪贪心码（24 次，皆覆盖 ✓）}:\ M\in[77,83],\ m\in[323,379] \Longrightarrow \text{我方工具\ \textbf{到不了 } }M\approx62\ \text{之近最优区} ⚠️$$

## §4 方法学收获（**本档最有价值之产出 ✓**）

$$\boxed{\textbf{预筛法}:\ \text{任何新提出的“}m\ \text{下界”式，先对已知小 }n\ \text{反例作检查};\ \text{本档反例}: (n{=}8,M{=}32,m{=}0)\ \text{已\ \textbf{杀掉一族通用式}}}$$
$$\text{更普遍}: \textbf{“}M<K(n,1)\text{”之区\ \textbf{数据不可及}（无此类码）⟹ 数据只能\ \textbf{否证} 不能\ \textbf{确认} 所需不等式} \Longrightarrow \text{设计路线须靠\ \textbf{证明结构} 而非数据} ⚠️✓$$

## §5 累计（**本线七条路线已否**）

$$\text{① }n_A\le9A_1\ (301/338);\ \text{② }A_1\le60;\ \text{③ }P\ge181;\ \text{④ }H_{11};\ \text{⑤ }R;\ \text{⑥ }INV2\text{-近等号（循环）};\ \text{⑦ }n{=}8\ \text{阈值（本档，含 }m{=}0\ \text{反例）}$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**覆盖校验实测 ＋ 判据执行** ✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
