已查地图：已跑 scripts/prework_map_check.sh 119 incidence geometry 覆盖者超图 高阶交 ⟹ **命中既有两档**：`FAILSET-2026-09-26` ✓、`WHYPER-2026-09-26` ✓（**故此方向非新开** ✓）；本档为**定位修正＋对象表示转向登记**（唐先生 2026-09-26 22:37 ✓）；未跑计算 ✓。
D0: 本档对象 = 119 研究定位与对象表示策略（方法论对象）
D1: 0（产出为定位修正、诊断表与地图核对；无新数学量）

# STRATEGY-2026-09-26 · 定位修正与对象表示转向

## §0 定位修正（唐先生 22:37 ✓）

```
$$\boxed{\text{119 的"无解感"主要来自\textbf{未找到正确的表示}，而非问题本身接近 RH 难度}}\ ✓$$
$$\text{RH}:\ \text{困难\textbf{有解释力}}（\beta\text{-blind／moment collapse／local}\to\text{global 鸿沟／adaptive 破坏}\ ✓)\quad\text{119}:\ \text{缺这样的解释}\ ✗$$
$$\textbf{分叉（唐先生 ✓）}:\quad \text{RH}:\ \text{继续找\textbf{新信息源}}\ ✓;\qquad \boxed{\text{119}:\ \text{找\textbf{新对象表示}，而不是继续找新不等式}}\ ✓✓$$
$$
$$
```

---

## §1 诊断表：低阶压缩坐标尽墨（本档汇总 ✓）

```
$$\begin{array}{c|c}
\text{坐标} & \text{结果}\\ \hline
A_1 & \text{无 target-coupled compression}\ ✗\\
A_2,\ \text{moments} & \text{distance-distribution collapse}\ ✗\\
2\text{-faces} & \text{回到 }A_1,A_2\ ✗\\
\text{3-point (Terwilliger 最小形)} & \text{独立但不够强}\ ✗\\
\text{Green 核} & \text{mixed-sign}\ ⟹\ \text{无最大原理}\ ✗\\
\texttt{PREIMAGE}\ \text{1-point} & \text{局部可行（mod 11 结构性退化）}\ ✗\\
\texttt{PREIMAGE}\ \text{2-point} & \textbf{全部可行} ⟹\ \text{CLOSED}\ ✗\\
\end{array}$$
$$\Longrightarrow\ \text{证据指向}:\ \boxed{\text{我们选择的坐标系不对}}\ ✓\ \text{而\textbf{非} }\boxed{\text{119 本身 RH 级难}}\ ✗$$
$$
$$
```

---

## §2 关键结构性观察（唐先生 ✓）

```
$$\text{把 }f\ \text{变成 }b\ \text{后，\textbf{藏起了最重要的非线性结构}}\ ✓:\quad \text{本质是 }\boxed{f^2=f}\ \textbf{与}\ \boxed{(I+A)f\ge1}\ \textbf{同时存在}\ ✓$$
$$\Longrightarrow\ \text{应研究\textbf{集合级结构}}（\text{incidence geometry}\ ✓）:\ \{B_1(c)\}\ \text{作为集合系统};\ \text{其交与高阶交}\ ✓$$
$$\qquad\text{与 face counting 的\textbf{本质区别}}:\ \text{后者最终压成 }A_1,A_2\ ✗;\ \text{要找的是\textbf{不能被距离分布完全表达}的 incidence 结构}\ ✓✓$$
$$
$$
```

---

## §3 地图核对（诚实 ✓：此方向已开过，非新）

```
$$\textbf{(1) }\texttt{FAILSET-2026-09-26}\ (14{:}42\ ✓):\ \text{覆盖者集 }W(x)=\{c:x\in B_1(c)\}\ ✓,\ \mathrm{holes}(S)\ ✓$$
$$\qquad\text{minimality}\iff\forall c\ \exists x:W(x)=\{c\}\ ✓;\quad \text{census }\{W(x)\}=\textbf{全局对象}\ ✓;\quad \text{我方一条公式被否}\ ✗;\ \text{修正恒等式}\ \sum_{\text{pairs}}|\mathrm{holes}|=(M-1)N_1+N_2\ ✓$$
$$\textbf{(2) }\texttt{WHYPER-2026-09-26}\ (14{:}44\ ✓):\ \boxed{\text{G}_2\ \text{（2-边图）判死}}\ ✗\ (\text{如 }(9,64):\ |E(G_2)|=0\ \text{而}\ Q_2=64\ ✓);\quad \boxed{\text{高阶交＝excess 载体（#3 证实 ✓✓）}}$$
$$\qquad\text{新不等式}\ Q_2\le T_3\le\tfrac{n+1}{3}Q_2\ ✓;\quad \text{目标形态（该档 §0）}:\ \Phi(\mathcal W)\ge f(E)\ \text{且}\ \Phi(\mathcal W)\le g(A_{\le2})\ \Longrightarrow\ \text{若 }f(E)>g(2)\ \textbf{打穿 P1}\ ✓✓$$
$$\Longrightarrow\ \textbf{结论}:\ \text{incidence 方向\textbf{不是新开}} ✓;\ \text{且已定位}\ \boxed{\text{"高阶交"是唯一未死的载体}}\ ✓✓$$
$$\qquad\⚠️\ \textbf{待核实}:\ \text{该载体的\textbf{利用}是否已被后续档做过 —— 档案检索未见明确后续，但\textbf{不得断言"未做"}}\ ✗\ \text{（须先核实 ✓）}$$
$$
$$
```

---

## §4 下一刀的正确形态（四门链适用 ✓）

```
$$\text{对象}:\ \text{census }\{W(x)\}\ \text{的\textbf{高阶部分}}（T_3\ \text{类量}\ ✓）$$
$$\text{目标形态（沿用 }\texttt{WHYPER}\ \S0\ ✓）:\ \Phi\ge f(E)\ \text{且}\ \Phi\le g(A_{\le2})\ ——\ \textbf{必须用 }A_{\le2}\ \text{作上界载体}\ ✓\ \text{（这正是"不能被距离分布表达"的检验 ✓）}$$
$$\text{强制声明（AMEND-32 ✓）}:\ \text{对哪个 target variable sensitive ＋ 约束方向}\ ✓$$
$$\text{失败判据}:\ \text{若 }\Phi\ \text{的上界仍只依赖 }A_{\le2}\ \text{且不超过 }f(E)\ \Longrightarrow\ \text{该载体亦死}\ ✗\ \text{（＝第 14 次汇合 ⚠️）}$$
$$
$$
```

---

## §5 状态锁定（本档 ✓）

```
$$\boxed{119:\ \text{scalar-invariant 压缩}\ \textbf{PAUSED}}\ ✓\ \text{（理由＝表示未找对 ✓，\textbf{非}"太难"}\ ✗）$$
$$\boxed{A_1\text{-route}:\ BLOCKED}\ ✓;\qquad \boxed{\texttt{PREIMAGE-local 1-point}:\ BLOCKED}\ ✓;\qquad \boxed{\texttt{PREIMAGE-local 2-point}:\ CLOSED\ (\text{无杠杆})}\ ✓$$
$$\textbf{新的最高优先}:\ \boxed{\text{核实 }\texttt{WHYPER}\ \text{高阶交载体的后续状态}}\ ✓\ \text{（核实后方可决定是否开下一刀 ✓）}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §0–§2 为**策略登记** ✓；§1 表为**本日结果汇总** ✓（各项均有细档 ✓）
- §3 为**地图核对** ✓（引用既有档 ✓，**不列为新提出** ✓）；"待核实"项**明确标注未证实** ✓
- §4 为**下一刀形态** ✓（未执行 ✓）；§5 的状态为**登记** ✓
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；本轮未跑计算 ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 表示问题非难度问题 命中文件数=1    :: ./STRATEGY-2026-09-26-repositioning-and-object-representation.md 
技术词 对象表示转向登记 命中文件数=1    :: ./STRATEGY-2026-09-26-repositioning-and-object-representation.md
```
- **本档新增**：定位修正（表示问题非难度问题）、对象表示转向登记（见上方命中数；0 命中者为自造语 ✓）
- **档案已有（引用，不列为提出）**：FAILSET 框架、WHYPER（G₂ 判死／高阶交载体／Q₂≤T₃ 不等式）、AMEND-32、PREIMAGE 1/2 点
