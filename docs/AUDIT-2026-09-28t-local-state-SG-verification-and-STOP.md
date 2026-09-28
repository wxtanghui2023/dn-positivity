# AUDIT-2026-09-28t — **局部状态 $(S_c,G_c)$ 核验：恒等式全对，但局部条件不给下界 ⟹ STOP**

> **性质**：**实验/审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:46 ✓
> **唐先生令**：把局部量再推一步；**若只给出 $E\ge142$ 而无新增 $\ge1$，立即停** ✓

**已查地图**：接续 `AUDIT-s`（profile 审计）／`EXCESS-2026-09-25`（$\delta$-场恒等式）✓

D0: 本档对象 ＝ **档案已有**（$s(c),t(c),\delta$／恒等式——无新数学对象 ✓）
D1: 0（产出＝**局部推导核验 ＋ STOP 判定** ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{① 唐先生之邻居恒等式\ \textbf{完全成立}（$0$ 违例）};\ \text{② 求和恒等式\ \textbf{全对}};\ \text{③ \textbf{但}局部状态不给下界}}$$
$$\boxed{\text{④ 按唐先生 STOP 条件 ⟹ }\mathbf{立即停}\ ✓\ \text{（}\min(s+t)=0\ \text{可达} \Longrightarrow \text{无新增约束）}}$$

## §1 核验（$120$-code 实测 ✓）

$$\textbf{邻居恒等式}:\ a(c\oplus e_i)=1+\mathbf 1_{c\oplus e_i\in C}+d_i(c)\qquad \text{违例数}=\mathbf 0\ ✓✓$$
$$\text{（其中 }d_i(c)=\#\{j\ne i:c\oplus e_i\oplus e_j\in C\}\text{）}$$

$$\boxed{\sum_c s(c)=\mathbf{100}=2N_1\ ✓};\qquad \boxed{\sum_c t(c)=\mathbf{298}=2N_2\ ✓};\qquad \boxed{\sum_c E_c=\mathbf{796}=4(N_1+N_2)\ ✓✓}$$
$$\therefore\ \boxed{E_c=2\big(s(c)+t(c)\big)}\ \text{与}\ \boxed{\sum_c E_c=E+\textstyle\sum_x\delta(x)^2=4(N_1+N_2)}\ \textbf{皆核实}\ ✓$$

**⚠️ 诚实记录（本档自查之误）**：脚本首行把 $2(s+t)$ 与 $\delta(c){=}a(c){-}1{=}s(c)$ 相比 ⟹ 报"$114$ 违例" ⚠️ —— 系**比较对象写错**（$E_c{=}\sum_{x\in B_1(c)}\delta(x)$，非 $\delta(c)$），**非恒等式错**；求和层核验（上行三式）为准 ✓

## §2 ★ STOP 判定（**照令 ✓**）

$$\textbf{局部状态}:\ (S_c,G_c),\ S_c\subseteq[10],\ G_c\subseteq K_{10};\quad \textbf{私有条件}:\ s(c)>0\Rightarrow\exists i\notin S_c:\deg_{G_c}(i)=0\ ✓\ (\text{推导成立 ✓})$$
$$\textbf{但可达之最小}:\ (S,G)=(\varnothing,\varnothing)\Rightarrow(s,t)=(0,0)\Rightarrow E_c=\mathbf 0\ \text{合法}\ (s{=}0\ \text{使私有条件空})$$
$$\qquad\qquad (S,G)=(\{1\},\varnothing)\Rightarrow(s,t)=(1,0)\Rightarrow E_c=\mathbf 2\ \text{合法}$$
$$\therefore\ \boxed{\min(s+t)=0 \Longrightarrow \text{局部状态\ \textbf{不给出} } \sum_c(s+t)\ \text{之下界} \Longrightarrow \textbf{无新增约束}}\ ⚠️$$
$$\text{唯一可用者}:\ \delta\ge0\Rightarrow\textstyle\sum_x\binom{a(x)}2\ge E \Rightarrow N_1+N_2\ge E/2\ (K{=}106\Rightarrow\ge71)\ \text{——\ 即唐先生 §6 已知}\ ✓$$
$$\therefore\ \boxed{\text{按令: 只给 }E\ge142\ \text{而无新增}\ \ge1 \Longrightarrow \textbf{STOP}}\ ✓✓$$

**旁注（本档补充，仍不救）**：$\min\ d(C)\ge3\Rightarrow$ 球互不相交 $\Rightarrow K\le\lfloor1024/11\rfloor=93$ ⟹ $K{=}106$ 必有距离 $\le2$ 对 ⟹ $N_1{+}N_2\ge1$ —— 远弱于 $71$，**不改变判定** ⚠️

## §3 ★ 文献线索（本档附记，供 $107$ 原式用 ✓）

$$\text{BÖW 2004 之\textbf{参考文献}（fetch 所得）含}:\ \textbf{L. Habsieger \& A. Plagne,}\ "\text{New lower bounds for covering codes}",\ \textbf{Discrete Math 222 (2000), 125--149}\ ✓$$
$$\qquad \text{另含 Blass--Litsyn 1998（IEEE TIT 44, 1998--2002）、Haas 2000（Discrete Math 219, 97--106）、Cock--Östergård 1997、Di Pasquale--Östergård 2003} ✓$$
$$\therefore\ \boxed{\text{"general lower bound for }R{=}1"\ \text{之最可能源}\Rightarrow\textbf{Habsieger--Plagne 2000}}\ ⚠️\ \text{（下一步取它）}$$

## §4 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "局部状态可拼接性" "私有邻点条件" "无新增约束即停"
技术词 局部状态可拼接性 命中文件数=0    ::
技术词 私有邻点条件   命中文件数=0    ::
技术词 无新增约束即停   命中文件数=0    ::
```

## §5 边界（硬 ✓）

- 有限核验（$120$ 码全码字）＋ 既有档引证 ＋ 外部参考文献线索 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**不主张** 119/106 之不可能 ✗（V290）
- §2 之 STOP **只**针对"局部 $(S,G)$ ＋ 私有条件"这一层；**不主张**一切局部方法皆不可行 ⚠️
