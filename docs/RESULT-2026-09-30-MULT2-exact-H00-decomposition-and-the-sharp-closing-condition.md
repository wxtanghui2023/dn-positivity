# RESULT-2026-09-30-MULT2 — $H_{00}$ 之**精确分解**（三恒等式 ✓✓）＋ 收口条件之**尖锐化**

> 空间 B｜非 C 号｜唐先生 00:08「继续」（补那"1"）｜**不主张任何新值**（V290）

**已查地图**：承 `RESULT-MULT`（重数 4／5）／`REFUTE-2026-09-30b`／`DEFS-2026-09-29`／`INV3`
D0: 本档对象 = **档案已有**（$H_{00},H_{01},H_{11},A_2,P,H$）之**精确分解**（新数学对象：无；**新恒等式 3 条** ⚠️）
D1: 0（产出 = **三条恒等式 ＋ 一条收口条件之尖锐化** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 三恒等式（双码实测 ✓✓）}:\ H_{00}{+}H_{01}{+}H_{11}=A_2;\quad P=H_{01}{+}2H_{11};\quad H=2H_{00}{+}H_{01}}$$
$$\boxed{\text{② 推论（精确耦合，取代松弛式 }H_{00}\le A_2\text{）}:\quad A_2-H_{00}=H_{01}+H_{11};\qquad \boxed{H_{00}=\tfrac{H-P}2+H_{11}}}$$
$$\boxed{\text{③ 收口条件尖锐化}:\ \text{链闭合}\iff H_{00}\ \le\ \mathbf{99}\ (M{=}106,\ r_{A2}{=}5,\ A_1{\approx}50)\iff \#\{\text{有码字中点的距离-2 对}\}\ \ge\ A_2-99}$$

## §1 恒等式之定义与实测

$$H_{00},\ H_{01},\ H_{11}:=\#\{\text{距离-2 码字对，其两中点中码字数为 }0/1/2\}$$
$$\text{（每对恰 2 个中点}:\ |N[c]\cap N[d]|=2\iff1\le d(c,d)\le2\ ✓\text{）}$$
| 码 | $A_2$ | $H_{00}$ | $H_{01}$ | $H_{11}$ | $P$ | $H$ | 核验 |
|---|---|---|---|---|---|---|---|
| 120-码 | 149 | 110 | 37 | 2 | 41 | 257 | 三式皆 ✓ |
| 62-码（$n{=}9$） | 66 | 60 | 6 | 0 | 6 | 126 | 三式皆 ✓ |

$$H_{00}+H_{01}+H_{11}=A_2\ ✓\ (\text{分类穷尽});\quad P=H_{01}+2H_{11}\ ✓\ (\text{每对按中点码字数贡献楔});\quad H=2H_{00}+H_{01}\ ✓\ (\text{每对贡献"中点非码数"})$$
$$\Longrightarrow\ \boxed{A_2-H_{00}=H_{01}+H_{11}}\quad(\textbf{恰为"有码字中点的距离-2 对数"})\ ✓✓$$

## §2 收口条件（尖锐形式）

$$\text{链}: \sum_{v\notin C}\delta\ \ge\ 2754-2n_1,\qquad n_1\ \le\ 4A_1+5H_{00}+2A_2;\qquad \sum_{v\notin C}\delta=1562-4A_1-4A_2$$
$$\text{矛盾}\iff 1192>4A_1+10H_{00}\iff H_{00}<\frac{1192-4A_1}{10}\quad(A_1{=}50\Rightarrow H_{00}\le\mathbf{99})$$
$$\text{以 §1 之精确式代入}:\ H_{00}=\tfrac{H-P}2+H_{11}\Longrightarrow \text{等价形式}:\quad \boxed{A_2-(H_{01}+H_{11})\ \le\ 99}$$
$$\text{即}:\quad \#\{\text{有}\ge1\text{ 个码字中点的距离-2 对}\}\ \ge\ A_2-99\quad(\text{需 }A_2\ \text{不过大，或该比例不过小})$$

## §3 实测比（**决定可行性**）

$$H_{00}/A_2 = \mathbf{0.738}\ (120\text{-码},\ M{=}120);\qquad \mathbf{0.909}\ (62\text{-码},\ n{=}9\ \text{最优})$$
$$\Longrightarrow\ \text{若 }M{=}106\ \text{处沿用 }H_{00}\approx0.8A_2,\ \text{则需 }A_2\le\mathbf{124};\quad \text{而 INV2 只给 }A_1{+}A_2\le161\ (\Longrightarrow A_2\le161)\ ✗\ \text{过松}$$
$$\therefore\ \textbf{唯一剩余缺口}:\ \text{一条更紧的\ }A_2\ \text{上界（}\le124\text{ 即可）\ 或\ }H_{00}/A_2\ \text{之上界（}\le0.8\text{）} \ ⚠️$$

## §4 判定与去向

$$\text{① 本档收获}:\ H_{00}\ \text{之\ \textbf{精确分解}（取代松弛式）};\ \text{收口条件由"}"H_{00}\le A_2"\text{" 变为 }\boxed{H_{00}\le99};\ \text{且已由三恒等式改写为可验证形式}\ ✓$$
$$\text{② 剩余缺口极小且明确}:\ \text{只需 }A_2\le124\ \text{（而非 }\le161\text{）——即把 INV2 紧 37 个单位} ⚠️$$
$$\text{③ 可选下一刀}:\ ①\ \text{紧 }A_2\ \text{上界（用 Delsarte＋恒等式族之联合 LP，照 }A\text{-}DELSARTE\text{-}1\text{ 之法）};\ ②\ \text{证 }H_{00}/A_2\le0.8\ \text{之局部引理};\ ③\ \text{若均不成，}\delta{=}1\ \text{层记 CLOSED-不足}$$
$$\textbf{纪律}:\ \text{实测比 0.738/0.909 表明该路\textbf{临界}，不预设可成} ✓$$

## §5 边界（硬 ✓）

- **不主张**任何新值；恒等式为由定义直接展开并双码核验 ✓（分类穷尽＋楔计数）
- 未取论文原文（R16–17）✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
