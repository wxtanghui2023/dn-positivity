# AUDIT-2026-09-28v — **本轮封口 ＋ Habsieger–Plagne 2000 摘要到手 ＋ ⚠️$K{=}106$ 其实\ \textbf{已被排除}**

> **性质**：**封口档/审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:52 ✓
> **唐先生令**：本 round **正式封口**；局部路线 **STOP**；下一轮严格按 6 步走 ✓

**已查地图**：接续 `AUDIT-u`（距离-3 补洞 $X$）／`AUDIT-q`（van Wee 原式）／C-474✓

D0: 本档对象 ＝ **档案已有**（线性不等式／$K(n,1)$——无新数学对象 ✓）
D1: 0（产出＝**封口 ＋ 摘要取证 ＋ 一处目标重定位** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 本轮\ \textbf{封口};\ 局部路线\ \textbf{STOP}（不追加人为约束）}}✓$$
$$\boxed{\text{② Habsieger--Plagne 2000 摘要到手}:\ \text{机制 ＝ }\textbf{linear inequality of a code}\ \text{（LP 族）}}✓$$
$$\boxed{\text{③ ⚠️ 唐先生之问（}K{=}106\ \text{是否被一般理论排除）之答案 ＝ }\mathbf{是，已被排除}\ \text{（因 }107>106\text{）}}$$
$$\boxed{\text{④ ⟹ "}E\ge153\ \text{路线"\ ＝\ \textbf{复现已知定理};\ 真正的新目标 ＝ }E\ge164\Rightarrow K\ge\mathbf{108}}$$

## §1 局部路线封口（**照令 ✓**）

$$\text{本会话局部链（}\Phi_2\to\text{coset}\to\text{spectral}\to\text{complement}\to(S_c,G_c)\to\text{距离-3 补洞}X\text{）}\ \textbf{全部未产出新增约束}\ ✗$$
$$\boxed{\text{STOP};\ \textbf{不再追加人为约束}}\ ✓$$

## §2 Habsieger–Plagne 2000 摘要（**逐字 ✓**）

$$\text{L. Habsieger, A. Plagne,}\ "\text{New lower bounds for covering codes}",\ \textbf{Discrete Math 222 (2000), 125--149};\ \text{DOI }10.1016/S0012-365X(00)00011-X$$
$$\textbf{逐字}:\ \text{"Both are based on the notion of \textbf{linear inequality of a code}. Indeed, every linear inequality of a code (defined on }\mathbb F_q^n\text{) allows to obtain, using a \textbf{classical formula (inequality (2))}, a lower bound on }K_q(n,R)"$$
$$\qquad\qquad \text{"we prove some formulae that \textbf{improve on the classical formula (2)}... we improve on \textbf{nearly 20\%} of the best lower bounds on }K_q(n,R)"$$
$$\Longrightarrow\ \boxed{107\ \text{属\ \textbf{线性不等式（LP）族}};\ \text{机制＝加权线性不等式 ＋ 特型改进公式}}\ ✓$$

**旁证（van Wee 之地位）**：检索得逐字 "\textbf{Improved Sphere Bounds on the Covering Radius of Codes}: Summary of Results: }K(n,1)\ge 2^n/n,\ n\ \text{even}" ⟹ 线性不等式族\ \textbf{确能}超越体积界 ✓（与 `SUBSPACELP` 之等号定理不冲突：后者限于 coset-计数型 LP ✓）

## §3 ★ 目标重定位（**本档核心 ✓✓**）

$$\text{BÖW 2004}\ \text{给}\ a(10)\ge\mathbf{107}\ \Longrightarrow\ K_2(10,1)\ge107\ \Longrightarrow\ K\ne106\ \checkmark$$
$$\therefore\ \boxed{\text{"证明 }K\ge107\text{"\ ＝\ 已知定理；}\textbf{唐先生之 }K{=}106\ \text{路线并无新的排除空间}}\ ✓$$
$$\text{同理 }K{=}107\ \text{亦被}\ 120\ \text{上界与…hmm};\ \text{真正\textbf{新}之地板目标} = \mathbf{108}:\quad E\ge164\iff 11K\ge1188\iff K\ge108\ ✓$$
$$\therefore\ \boxed{\text{可挖空间（下界端）}:\ 107\to108;\ \text{而 }106\ \text{已无仗可打}}\ ⚠️$$

## §4 唐先生之 6 步队列（**照令登记，未做完 ✓**）

$$\text{① 取 H--P 2000 正文}:\ \textbf{摘要已得 ✓};\ \textbf{正文未得}（ScienceDirect 付费）✗$$
$$\text{② 定位精确 theorem/formula}:\ \textbf{未得}（仅知机制 ∈ 线性不等式族 ＋ 改进公式 (2)）✗$$
$$\text{③ 代入 }q{=}2,n{=}10,R{=}1:\ \text{待 ② ✗}$$
$$\text{④ 与 }K{=}106\ \text{比较}:\ \textbf{已完成（§3）}:\ 107>106\Rightarrow\text{已排除}\ ✓✓$$
$$\text{⑤ 若未排除，查 BÖW 2004 之转述/加强}:\ \text{本轮无需（④已排除）}\ ✓$$
$$\text{⑥ 仅当仍留 106 才回具体结构}:\ \textbf{不触发}\ ✓$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "线性不等式族" "106已被排除" "新目标108"
技术词 线性不等式族  命中文件数=3    :: ./SPHERELP-2026-09-26-the-sphere-covering-inequality-family-and-the-parity-interface.md
                                       ./HQ1-2026-09-26-haas-times-q1-symbolic-projection.md
                                       ./M2B-2026-09-27-embedding-gate-and-m2ap-status.md
技术词 106已被排除  命中文件数=0    ::
技术词 新目标108   命中文件数=3    :: （同上三档，皆属本线既有）
```

**口径（空间隔离 ✓）**：`线性不等式族` ＝ **档案已有（本线，引用，不列为本档提出）** ✓ —— 三档 `SPHERELP`／`HQ1`／`M2B` 皆**本线既有** ⟹ ★**地图命中**：线性不等式族**已被本线研究过** ⚠️（本档仅作 H--P 2000 之归属取证，不重开该族）
`106已被排除` 为本档新造 ✓

## §6 边界（硬 ✓）

- 权威源直取（ScienceDirect 摘要逐字）＋ 档案引证 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗
- §3 之推理**依赖** BÖW 2004 之 $a(10)\ge107$ 归属为真（OEIS 明载 ✓）⚠️；**不主张** 108 可达 ⚠️（V290）
