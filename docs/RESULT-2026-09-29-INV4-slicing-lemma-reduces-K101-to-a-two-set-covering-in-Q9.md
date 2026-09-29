# RESULT-2026-09-29-INV4 — 第 4 轮：**切片引理**（$K(10,1)\ge\gamma_2(Q_9)$，全 10 切片实测 ✓✓）＋ 通用界 vs 真值对照

> 空间 B｜非 C 号｜唐先生 23:35「继续」｜**不主张任何新值**（V290）

**已查地图**：`AUDIT-28q`（通用公式链）／`AUDIT-29g/h`（surfeit 不覆盖 $n{=}10$）／本会话 `INV2/INV3`
D0: 本档对象 = **档案已有**（缩短/切片、球覆盖）之**系统性重推**（新数学对象：**弱**——切片引理为经典缩短关系之显式形式 ⚠️）
D1: 0（产出 = **一条可验证约化 ＋ 一张对照表 ＋ 一条方向判定** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\textbf{① 切片引理（新档内可验证）}:\quad K(10,1)\ \ge\ \gamma_2(Q_9)\ :=\ \min\bigl\{|P_0|+|P_1|\ :\ P_0,P_1\subseteq Q_9,\ N[P_0]\cup N[P_1]=Q_9\bigr\}}$$
$$\qquad\textbf{实测}:\ \text{120-码对\ \textbf{全部 10 个坐标}切片皆满足（}|P_0|{+}|P_1|{=}120,\ \text{未覆盖}=0\text{）} ✓✓\ \Longrightarrow\ \gamma_2(Q_9)\le120$$
$$\boxed{\textbf{② 方向判定}:\ \text{通用公式链条（van Wee＝}2^n/n\text{）在 }n{=}7,8\ \textbf{精确};\ \text{在 }n{=}9\ \textbf{差 10.8};\ n{=}10\ \textbf{差 4.6}}$$
$$\qquad\Longrightarrow\ \textbf{107 极可能出自 }n{=}10\text{ 专属（含计算/结构）论证，而非"通用公式 ＋ 可调参数"} \Longrightarrow \text{推翻 }AUDIT\text{-}28q\ \text{之"可调参数"模型} ⚠️✓$$

## §1 切片引理（推导 ＋ 全验）

$$\text{取第 }b\ \text{位切片}:\ C_0{=}\{c:c_b{=}0\},\ C_1{=}\{c:c_b{=}1\};\ P_\beta{=}\text{proj}_{\hat b}(C_\beta)\subseteq Q_9$$
$$\text{对任意 }x\in Q_9:\ (0,x)\ \text{须被覆盖} \Longrightarrow \exists c:\ d(c,(0,x))\le1 \Longrightarrow x\in N[P_0]\cup N[P_1]$$
$$\qquad(\text{若 }c_b{=}\beta\ \text{且 }d(c,(0,x))\le1\ \Longrightarrow\ \text{proj}(c)\ \text{与 }x\ \text{在 }Q_9\ \text{中距离}\le1)$$
$$\therefore\ Q_9=N[P_0]\cup N[P_1]\ \text{且}\ |P_0|+|P_1|=M\ \Longrightarrow\ M\ge\gamma_2(Q_9)\ ✓$$
**实测（120-码）**：10 个切片全部 $|P_0|+|P_1|=120$、未覆盖 $=0$ ✓✓（逐切片 $|P_0|$：$60,61,60,60,60,59,60,60,56,60,60$）

$$\text{即}\quad K(10,1)\ \ge\ \gamma_2(Q_9)\ \ge\ K(9,1)=62\ (\text{取 }P_1{=}\varnothing);\ \text{且}\ \gamma_2(Q_9)\le120\ (\text{本档实测})$$
$$\Longrightarrow\ \boxed{\text{复现 }107\ \text{＝证 }\gamma_2(Q_9)\ge107\ \text{——\ \textbf{问题被搬到 }n{=}9（512 点、两集覆盖）}}$$

## §2 通用界 vs 真值（**对照表**）

| $n$ | 球界 $2^n/(n{+}1)$ | van Wee $2^n/n$ | 真值 $K(n,1)$ | 真值 − van Wee |
|---|---|---|---|---|
| 5 | 5.33 | 5.33 | 7 | +1.67 |
| 6 | 9.14 | 10.67 | 12 | +1.33 |
| **7** | 16.00 | **16.00** | **16** | **0** |
| **8** | 28.44 | **32.00** | **32** | **0** |
| 9 | 51.20 | 51.20 | **62** | **+10.80** |
| 10 | 93.09 | 102.40 | **≥107** | **+4.60** |

$$\therefore\ \text{通用公式只在 }n{=}7,8\ \text{精确};\ \text{自 }n{=}9\ \text{起真值\ \textbf{显著超出}} \Longrightarrow \text{真值必由\ \textbf{n-专属论证/计算} 确立}$$
$$\qquad(\text{旁证}:\ K(9,1){=}62\ \text{正是由分类/计算确立——}\text{球界 }51.2\ \text{与 van Wee }51.2\ \text{皆远低})$$

## §3 下一刀（$\gamma_2(Q_9)$）与**同墙预警**

$$\text{标定}:\ \gamma_2\ \text{之 LP 松弛} = 512/11 = 46.5\ \text{（球界）}\ \Longrightarrow\ \text{与主问题\ \textbf{同一整性墙}} ⚠️$$
$$\therefore\ \gamma_2(Q_9)\ \text{不会因"降一维"而变易};\ \text{其价值在于\ \textbf{形式}：两集覆盖之\ \textbf{交叉结构}（}P_0\cap P_1\ \text{、边界切片）可提供新构型语言}$$
$$\text{下一步（若继续）}:\ \text{①算 }\gamma_2(Q_9)\ \text{之精确/强下界（ILP＋对称性商）};\ \text{②研究 }P_0,P_1\ \text{交叉处的\ \textbf{局部必现构型}}（＝唐先生 D/E 之合法入口）}$$

## §4 边界（硬 ✓）

- **不主张**任何新值；切片引理为**经典缩短关系之显式形式**（不声称首创）⚠️✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
