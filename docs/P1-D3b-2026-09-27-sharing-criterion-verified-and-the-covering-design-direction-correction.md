# P1-D3b-2026-09-27 — **共享判据核验** ＋ **方向性纠正**（$C(s,4,3)$ 不能直接当 $d_4$ 下界）＋ 数值现实检查

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。**范围**：核验共享分析；检查 covering-design 升级是否成立；零程序计算 ✓。

**已查地图：命中（接续 P1-D3／P1-MICRO／P1-TWO，非新案 ✓）**
`docs/P1-D3-2026-09-27-…`（**被迫高层码字定理／$d_4\ge\lceil\binom s3/4\rceil$** ✓✓）｜`docs/P1-TWO-2026-09-27-…`｜`docs/P1-MICRO-2026-09-27-…`｜`docs/R7-2026-09-27-…`（**四族目录／$T_4=N_{\rm claw}+N_{\rm star}$** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** $d_4$ 下界对象的**判据核验与方向纠正**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出共享判据的完整核验 ＋ $C(s,4,3)$ 升级的\*\*方向性反例分析\*\* ＋ $s=10$ 零改进判定** ✓）
**[RESEARCH]**

---

## §0 结论（**判据正确 ✓｜结构澄清 ✓｜方向纠正 ✗✓｜零改进 ✗**）

$$\boxed{\textbf{(1) 共享判据核验通过 ✓✓}:\ x_{T_1},x_{T_2}\ (T_1,T_2\subseteq S(c),|T|=3)\ \text{共用一 weight-4 码字}\iff|T_1\cap T_2|=\mathbf 2\ ✓;\ \text{此时 }S=T_1\cup T_2\ \textbf{唯一}✓✓}$$
$$\boxed{\textbf{(2) 结构澄清 ✓}:\ |T_1\cap T_2|=2\ \text{的四 triples 两两交 2（tetra-\textbf{面}组合 ✓），但四个 }d=3\ \text{点构成\textbf{已实现的 star}（球心 }=c\oplus S✓）\Longrightarrow \text{它计入 }T_4\ \text{而非 }\Delta_4✓✓}$$
$$\boxed{\textbf{(3) ✗ 方向性纠正（关键）}:\ d_4(c)\ge C(s(c),4,3)\ \textbf{未成立}✗;\ \text{有效下界仍是容量界}\ \lceil\binom s3/4\rceil✓;\ \text{因\textbf{混合块（3 内＋1 外）未被禁止}⚠️}}$$
$$\boxed{\textbf{(4) 数值现实检查 ✗}:\ s=10\ \text{时}\ \lceil\binom{10}3/4\rceil=30=C(10,4,3)\ \big(\text{Witt }S(3,4,10)✓\big)\ \Longrightarrow\ \textbf{升级给出恰好零改进}✗✗}$$

---

## §1 共享判据的**核验**（**照唐先生 ✓✓**）

$$y=c\oplus S\ (|S|=4)\ \text{同时覆盖 }x_{T_1},x_{T_2}\iff d(y,x_{T_i})=1\iff|e_{(S)}\oplus e_{(T_i)}|=1\iff T_i\subset S,\ |S\setminus T_i|=1✓$$
$$\Longrightarrow T_1\cup T_2\subseteq S\ (|S|=4)\Longrightarrow|T_1\cup T_2|=6-|T_1\cap T_2|\le4\Longrightarrow\boxed{|T_1\cap T_2|\ge2}\ ✓✓$$
$$\text{三种情形 ✓}:\ |T_1\cap T_2|=0\ \text{或}\ 1\Longrightarrow\textbf{不能共享}✓;\ =2\Longrightarrow\textbf{可共享且 }S=T_1\cup T_2\ \textbf{唯一}✓✓$$
$$\textbf{（唯一性 ✓）}:\ T_1\cup T_2\ \text{是含有二者的唯一 4-集（}|T_1\cup T_2|=4✓\big)\ \Longrightarrow\ \text{共享码字被唯一确定}✓$$

## §2 **结构澄清**（**本档补充 ✓**）

$$\text{一个 4-集 }S=\{a,b,c,d\}\ \text{的四个 triples }abc,abd,acd,bcd\ \text{两两交 2 ✓（＝ tetra 的四个面的组合学 ✓）}$$
$$\textbf{但对应点的几何 ✓}:\ \text{四点为 }x_T=c\oplus e_{(T)}\ (|T|=3)✓;\ d(x_{T_1},x_{T_2})=|T_1\triangle T_2|=2✓;\ d(y,x_T)=1✓\ (\text{§1 ✓})$$
$$\Longrightarrow\ \text{四点是}\ y=c\oplus S\ \text{的\textbf{四个邻居}} \Longrightarrow\ \text{按 R7 四族目录}: \textbf{star}✓（\textbf{已实现}，球心 }y✓）$$
$$\Longrightarrow\ \textbf{故该结构计入 }T_4=N_{\rm claw}+N_{\rm star}\ \textbf{而非 }\Delta_4✓✓\ \text{—— 它不产生亏空 ✓（有价值：说明 forced-}d_4\ \text{结构与 }T_4\ \text{耦合 ✓）}$$

> 🩹 **勘误横幅（2026-09-27，见 P1-G2 档 §1 ✓）**：本节原有的「四点构成\*\*已实现 star\*\*、计入 $T_4$」断言**有误** ✗ —— 四个 forced 点 $x_T$（$T\subset S$，$|T|=3$）满足 $T\subseteq S(c)$，由 $(\alpha)$ 知 $x_T\notin C$ ⟹ **皆非码字** ⟹ **不构成 $G_2(C)$ 的团、不计入 $T_4$** ✓。仍成立的部分：四点两两距离 2、共享 $y$、构成 $G_2(Q_{10})$（**全图**）的 $K_4$ —— 但那是全图结构，与 $C$ 无关 ✓。

## §3 ✗ **方向性纠正**（**$C(s,4,3)$ 不能直接作 $d_4$ 下界**）

$$\textbf{框架 ✓（唐先生对）}:\ F_4(c):=\{S:\ c\oplus S\in C,\ |S|=4\}\ \text{须覆盖 }S(c)\ \text{的全部 3-子集 }T✓;\ \text{故这是\textbf{覆盖设计型}问题 ✓✓}$$
$$\textbf{但块的三种类型（关键 ✗）}:\ \text{令 }j:=|S\cap S(c)|:\ \ j=4\ (\text{全内})\ \text{计入 }\binom43=\mathbf 4\ \text{个待覆盖 }T✓;\ j=3\ (\textbf{混合}，3 内+1 外)\ \text{计入 }\binom33=\mathbf 1\ ✓;\ j\le2\ \text{计入 0 ✗}$$
$$\textbf{容量下界 ✓（有效）}:\ \text{每块计入}\le4\ \Longrightarrow\ d_4(c)\ge\Big\lceil\tfrac14\binom{s(c)}3\Big\rceil✓\ \text{—— \textbf{本档确认此为有效下界}✓}$$
$$\textbf{而 }C(s,4,3)\ \text{的地位 ✗}:\ C(s,4,3)\ \text{＝"仅用 }j=4\ \text{块"时的最小块数 ✓;}\ \text{但 }j=3\ \text{混合块\textbf{未被任何已证约束禁止}}⚠️\ \Longrightarrow\ \text{含混合块的族其块数可\textbf{少于} }C(s,4,3)✓$$
$$\qquad\Longrightarrow\ \boxed{d_4(c)\ \ge\ \Big\lceil\tfrac14\binom{s(c)}3\Big\rceil\ \text{（有效）};\qquad d_4(c)\ \ge\ C(s(c),4,3)\ \textbf{未成立}\ ✗✓}$$
$$\qquad\text{（等价地 ✓）}:\ C(s,4,3)\ \text{是"纯内块需求"，是 }d_4\ \text{的\textbf{上界侧}参考，而非下界 ✓——方向须颠倒才自洽 ✓}$$

## §4 **数值现实检查**（**零改进 ✗**）

$$\text{当 }s\equiv2,4\ (\mathrm{mod}\ 6)\ \text{时 Steiner 系 }S(3,4,s)\ \text{存在} \Longrightarrow C(s,4,3)=\binom s3/4\ \textbf{恰为容量界}✓✓\ (\text{每 triple 恰覆盖一次 ✓})$$
$$\textbf{关键例 ✓}:\quad s=\mathbf{10}:\ C(10,4,3)=\tfrac{120}4=\mathbf{30}=\Big\lceil\tfrac14\binom{10}3\Big\rceil\ \big(\text{Witt }S(3,4,10)✓\big);\qquad s=8:\ 14=14\ \big(\mathrm{SQS}(8)✓\big)✓$$
$$\Longrightarrow\ \boxed{\text{在最大情形 }s=10\ \text{与 }s=8\ \text{下，covering-design 升级给出\textbf{恰好零改进}}✗✗}$$
$$\qquad\text{只有 }s\not\equiv2,4\ (\mathrm{mod}\ 6)\ \text{时才有小差额（如 }s=7:\ \text{容量 }9\ \text{vs 无 Steiner 系 ⟹ }>9✓\ \text{（具体值档级 ⚠️）}）✓$$
$$\Longrightarrow\ \textbf{结论 ✓}:\ \text{covering-design 框架\textbf{结构上正确}✓，但\textbf{数值上近乎无力}✗（最大情形零收益 ✓）}$$

## §5 现状与下一步（**诚实 ✓**）

$$\textbf{已确立 ✓}:\ \text{① 共享判据 }|T_1\cap T_2|=2\ ✓;\ \text{② 共享结构的几何 ＝ \textbf{已实现 star}（入 }T_4✓\text{）};\ \text{③ }d_4\ \text{的\textbf{有效下界}＝容量界 ✓};\ \text{④ }C(s,4,3)\ \text{不作下界 ✗}✓$$
$$\textbf{仍缺 ✓}:\ \textbf{独立的 }d_4\ \textbf{上界}（\text{用于与下界夹逼}）⚠️\ \text{—— 这正是唐先生 §4 指出的方向 ✓};\ \text{且该上界须\textbf{非 profile 型}（见 R7 STOP／C-409 ✓）}$$
$$\textbf{（诚实边界 ⚠️）}:\ \text{本档\textbf{未}产生矛盾};\ \text{未证明 forced-}d_4\ \text{与 }d_4\ \text{上界可夹逼 ✓}$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "共享判据"
技术词 共享判据        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "覆盖设计"
技术词 覆盖设计        命中文件数=4    :: ./E220-tower-residual-repair-four-steps.md ./HUNT-R2-OPEN-MATH-POOL-round1.md ./ASSET-TO-PROBLEM-MATCHING-v1.md
$ bash scripts/tech_word_check.sh "混合块"
技术词 混合块          命中文件数=0    ::
$ bash scripts/tech_word_check.sh "Steiner"
技术词 Steiner          命中文件数=12   :: ./FOURIER-2026-09-26-convolution-reformulation-audit.md ./LEDGER-2026-09-27-k101-closed-form-and-next-round-protocol.md ./FRONTIER-R3-2026-09-27-phase1-steiner-cells-mechanism-inventory.md
```
- **本档新增**：**0** 个术语 ✓（`共享判据`／`混合块` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`覆盖设计`／`Steiner` 档案已有 ✓）
- **注 ✓**：本档实质＝**§1 核验 ＋ §2 结构澄清 ＋ §3 方向纠正 ＋ §4 零改进判定**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** P1 成立 ✗（V290）；**不声称** $C(s,4,3)$ 路线无望 ✗ —— 只写"**其在 $s=10$ 零改进、且不作下界**" ✓
- §4 的 $s=7$ 具体值**标档级** ✓（未逐字核 ✓）；Witt／SQS 存在性为**已知事实**（档级引用 ✓）
