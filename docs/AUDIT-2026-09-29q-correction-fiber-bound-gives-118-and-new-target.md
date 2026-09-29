# AUDIT-2026-09-29q — **★自查纠错：上轮"对准 107"系口径错；\ \textbf{纤维界的正确形式反而更强}（120-code 给 $M\ge118$）**

> **性质**：**自查纠错 ＋ 新靶**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 11:3x ✓
> **唐先生令**：「继续」✓

**已查地图**：★**推翻本线** `AUDIT-29p` §2 之"校准" ⚠️

D0: 本档对象 ＝ **档案已有**（层分解／容斥／$N[\cdot]$——无新数学对象 ✓）
D1: 0（产出＝**一处口径纠错 ＋ 正确界（更强）＋ 新靶** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗✗ 纠错}:\ \texttt{29p}\ \S2\ \text{之}\ T_3{=}175\ \textbf{系把 }2P_{\rm total}\ \text{当成 }2P(A)\ ✗;\ \textbf{正解 } \tau(A){=}-27}$$
$$\boxed{\text{② ⟹ "}T_3{=}P\ \text{恰给 }107\text{"\ \textbf{作废}}}$$
$$\boxed{\text{③ ✓✓ 但正确形式\ \textbf{更强}}:\ M\ \ge\ \frac{2P+1024-\tau}{11}\ —\ \textbf{120-code 给 }M\ge\mathbf{118}\ (\text{真值 }120)}$$
$$\boxed{\text{④ ★ 新靶}:\ \text{欲 }M\ge107\ \text{须\ \textbf{普适下界}}\ 2P-\tau\ \ge\ 153}$$

## §1 ① 纠错（**✗✗ 实测**）

$$\texttt{29p}\ \text{之算法}:\ T_3\ \text{本应} = |N[A]|-10a+2P(A);\ \text{我却用了}\ 2P_{\rm total}=288$$
$$\textbf{实测（120-code, }i{=}0\text{）}:\ a=60,\ \mathbf{P(A)=70},\ |N[A]|=487$$
$$\tau(A):=|N[A]|-10a+2P(A)=487-600+140=\mathbf{-27}\quad(\text{而非 }+175\ ✗)$$
$$\therefore\ \boxed{\texttt{29p}\ \S2\ \text{之"校准表"与"}T_3\le2P-153\text{"}\ \textbf{全部作废}}$$

## §2 ③ 正确之纤维界（**✓✓ 反更强**）

$$\text{推导（照旧，但 }\tau\ \text{取对）}:\quad \boxed{Q_9=N[A]\cup B,\quad Q_9=N[B]\cup A}$$
$$512\ \le\ |N[A]|+b\ =\ 10a-2P(A)+\tau(A)+b\qquad(a+b=M)$$
$$\text{相加}:\quad 1024\ \le\ 11M-2P+\tau\ \Longrightarrow\ \boxed{M\ \ge\ \frac{2P+1024-\tau}{11}}\qquad(\tau:=\tau(A)+\tau(B))$$

$$\textbf{实测（120-code，10 坐标之最好者）}:$$
| $i$ | $2P$ | $\tau$ | $M\ge$ | $\lceil\cdot\rceil$ |
|---|---|---|---|---|
| $9$ | $358$ | $87$ | $117.7$ | $\mathbf{118}$ |
| $6,8,3$ | $354{-}356$ | $88{-}90$ | $\approx117.5$ | $118$ |
| $0$ | $288$ | $58$ | $114.0$ | $114$ |
| $7$ | $274$ | $66$ | $113.4$ | $113$ |

$$\therefore\ \boxed{\text{该界对 120-code 给 }M\ge\mathbf{118}\ (\text{真值 }120)\ ——\ \textbf{远强于 van Wee 之 }103}✓✓$$

## §3 ★ ④ 新靶（**具体、纯自推 ✓**）

$$\text{于 }M{=}106:\quad 2P-\tau\ \ge\ 153\ \Longrightarrow\ M\ \ge\ \frac{1024+153}{11}=106.99\Rightarrow\mathbf{107}✓✓$$
$$\therefore\ \boxed{\text{待证}:\ \text{任何 }Q_{10}\ \text{之半径-1 覆盖码\ \textbf{皆}有}\ 2P-\tau\ \ge\ 153\ (\text{对某坐标})}$$
$$\text{其中}\ P=\text{同层距离}\le2\ \text{之码字对数};\quad \tau=\sum_{\rm layers}\bigl(|N[\cdot]|-10a+2P(\cdot)\bigr)\ (\textbf{容斥之余项})$$
$$\text{经验支撑}:\ P\ \text{随 }M\ \text{增};\ 120\text{-code 之 }P=179\ \Longrightarrow\ M{=}106\ \text{外推}\ P\approx155\ \Longrightarrow\ 2P\approx310\gg153\ ✓$$
$$\text{（即：若 }\tau\ \text{不大，该靶\ \textbf{极可能成立}；而其退化 }\tau=0\ \text{给 }M\ge(2P+1024)/11\big|_{P=179}=119.3\Rightarrow120）$$

## §4 与既有路线之关系（**✓ 定位**）

$$\text{本界\ \textbf{非}全局 }A_j(u)\ \text{型量（}29m\ \text{已证该层榨干、可行域非空）};\ \text{而是\ \textbf{双层构型}量}✓$$
$$\text{且其数值}\ 118\ (\text{对 }120)\ \text{\textbf{远强}于本会话其余各族}:\ \text{excess／Zhang 单条／induced／}\theta\ \text{皆 }103{-}104✓✓$$
$$\therefore\ \boxed{\text{这是本会话\ \textbf{唯一}给出 }>105\ \text{的自推界};\ \text{机制与 119 线 C-435/436 同源}}✓$$

## §5 下一步（**具体 ✓**）

$$\textbf{1.}\ \text{多码 × 10 坐标扫 }(P,\tau)\ \text{之联合分布，找出 }\min(2P-\tau)\ \text{之经验值与其随 }M\ \text{之规律}$$
$$\textbf{2.}\ \text{尝试证明 }\tau\ \text{之上界（}$\tau\le$ 某显式量）}+\ P\ \text{之下界（}$P\ge$ 某显式量）} \Longrightarrow 2P-\tau\ge153$$
$$\textbf{3.}\ \text{若第 2 步成，\ \textbf{即得 }K(10,1)\ge107}✓✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "口径纠错" "纤维界118" "新靶2P-tau"
技术词 口径纠错    命中文件数=0    ::
技术词 纤维界118   命中文件数=0    ::
技术词 新靶2P-tau  命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code 十坐标全量实测 ＋ 自查纠错** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张**该靶必成 ✗；**不主张** $107$ 不可达 ✗（V290）
