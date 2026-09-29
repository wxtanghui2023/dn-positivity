# AUDIT-2026-09-29t — **局部三元组覆盖 ＝ 覆盖设计数 $C(v,3,2)$（＝Zhang 1991 机制）；精确化后仍\ \textbf{不足}**

> **性质**：**实测核验 ＋ 机制辨识 ＋ 决定性扫描**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 12:1x ✓
> **唐先生令**：局部分层框架（$U$／$F_c$／$r_u$／$t_3$／Steiner 障碍）✓

**已查地图**：`WITFIB`（fiber ≡ 覆盖）／`29m`（全局计数可行域非空）✓

D0: 本档对象 ＝ **档案已有**（分层／$F_c$／覆盖设计——无新数学对象 ✓）
D1: 0（产出＝**框架验证 ＋ 表之精确化 ＋ 机制辨识 ＋ 否定性扫描** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 你的框架\ \textbf{完全成立}}:\ \text{120-code 上}\ L1/L4/L5/\text{边覆盖\ \textbf{零违例}}}$$
$$\boxed{\text{② ★★ 你的 §4 表\ \textbf{可精确化}}:\ \text{局部界} ＝ C(v,3,2)\ (\text{覆盖设计数}),\ \text{在 }a_1\in\{0,2,4,6\}\ \text{强 }+2{+}1{+}1{+}1}$$
$$\boxed{\text{③ ★★ 机制辨识}:\ C(v,3,2)\ \textbf{恰是}\ Zhang\ 1991\ \text{之"covering pairs by }k\text{-tuples"}}$$
$$\boxed{\text{④ ✗ 但决定性扫描:\ 局部设计界＋Delsarte＋覆盖\ \textbf{对 }M{=}106\ \text{可行}（}A_1{=}0..7\text{）}\Longrightarrow\ \textbf{不排除}}}$$

## §1 ① 框架验证（**✓✓ 零违例**）

$$\text{修正我上轮之 bug（}t_3/t_2\ \text{须用翻转集 }w\oplus c）：\ \text{边覆盖}\ 3t_3+t_2\ \ge\ \tbinom v2-|F_c|\ \text{\textbf{零违例}}✓$$
$$\text{余量分布}\ 0..14;\ L1/L4/L5\ \text{亦零违例}✓\quad(\text{上轮我的"24/24 违例"系我之错，已改})$$

## §2 ② 表之精确化（**★★**）

$$\text{局部问题}:\ \text{用三元组覆盖 }K_{v}-F_c\ \text{之边};\ \text{其\ \textbf{精确}}最小数} ＝ \text{覆盖设计数}\ C(v,3,2)$$

| $a_1$ | $v$ | 你的表 $\lceil\binom v2/3\rceil$ | **精确** $C(v,3,2)$ | 差 |
|---|---|---|---|---|
| $0$ | $10$ | $15$ | $\mathbf{17}$ | $+2$ |
| $1$ | $9$ | $12$ | $12$ | $0$ |
| $2$ | $8$ | $10$ | $\mathbf{11}$ | $+1$ |
| $3$ | $7$ | $7$ | $7$ | $0$ |
| $4$ | $6$ | $5$ | $\mathbf{6}$ | $+1$ |
| $5$ | $5$ | $4$ | $4$ | $0$ |
| $6$ | $4$ | $2$ | $\mathbf{3}$ | $+1$ |
| $7$ | $3$ | $1$ | $1$ | $0$ |

$$\text{（}v\equiv1,3\bmod6\ \text{时 Steiner 存在 }\Rightarrow\ \text{无间隙};\ \text{其它 }v\ \text{有真间隙}）✓$$
$$\text{Schönheim 下界}\ C(v,3,2)\ge\lceil\frac v3\lceil\frac{v-1}2\rceil\rceil\ \text{给出}\ 17/11/6/3\ \text{之证书}✓$$

## §3 ③ 机制辨识（**★★ 关键**）

$$\texttt{zbMATH}\ \text{之}\ Zhang\ 1991\ \text{评审逐字}:\ "\text{a classic problem of }\textbf{covering pairs by }k\text{-tuples}"$$
$$\text{而我们此前复原 Zhang 之式时正是}:\ m_0=m_1+F(n{-}r{+}1,r{+}2),\quad F(10,3)=C(10,3,2)=\mathbf{17}\ \Longrightarrow\ m_0=5+17=\mathbf{22}✓✓$$
$$\therefore\ \boxed{\text{你的局部框架\ \textbf{就是} Zhang 之机制（不含新机制）};\ \text{故其上限仍在 }103{-}105\ \text{族}}$$

## §4 ④ 决定性扫描（**✗**）

$$\text{约束}:\ \text{Delsarte}(k{=}1..10)\ +\ \Sigma A_i{=}106\ +\ \text{覆盖}(9A_1{+}A_2{+}3A_3\ge45)\ +\ \text{局部设计}(A_3\ge\hat h(A_1)-A_2)$$
$$\hat h=\text{凸包络（顶点 }(0,17),(1,12),(3,7),(7,1),(8,0))$$

| $A_1$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|---|---|
| 最小可行 $A_2$ | $1.29$ | $1.02$ | $1.19$ | $2.54$ | $5.75$ | $9.81$ | $14.41$ | $20.49$ | **✗ 不可行** |

$$\therefore\ \boxed{A_1=0..7\ \text{皆\ \textbf{可行}（取适度 }A_2\text{）}\Longrightarrow\ \textbf{不排除 }M{=}106}✗$$
$$\text{（仅 }A_1{=}8\ \text{被排除——非决定性的角落）}$$
$$\text{⚠️ 诚实标注}:\ \text{本扫描用 }A_2^{\rm all}\ \text{代替}\ A_2^{UU}\ \text{扣减（\textbf{偏保守/偏弱}）};\ \text{若用 }A_2^{UU}\ \text{之下界可再收紧}-\ -\ \text{但缺口甚大（}A_1{=}0\ \text{仅需 }A_2\gtrsim1.3\text{）}$$

## §5 结论（**收束 ✓**）

$$\boxed{\text{局部设计障碍\ \textbf{真实}（}\lceil\cdot\rceil\ \text{漏掉 }+1\sim+2\text{）但\ \textbf{力度不足}}:\ \text{与 Delsarte 不碰撞}}$$
$$\text{根因}:\ \text{该机制}＝\text{Zhang 覆盖设计（}\equiv\ \text{本会话已封闭之 }103{-}105\ \text{族）}$$
$$\therefore\ \text{欲 }107\ \text{须\ \textbf{非}覆盖设计型之新信息}（\text{本会话已排除}\ 6\ \text{族＋纤维＋覆盖设计}）$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "局部设计界" "覆盖设计数" "构型扫描"
技术词 局部设计界   命中文件数=0    ::
技术词 覆盖设计数   命中文件数=0    ::
技术词 构型扫描    命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code 全量 ＋ LP 二次验证（120-code 通过 Delsarte）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 含**我上轮 bug 之更正** ✓ 与**本次扫描之保守性标注** ✓；**不主张** $107$ 不可达 ✗（V290）
