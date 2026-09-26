已查地图：已跑 scripts/prework_map_check.sh Wille 方阵 见证 极值猜想 ⟹ 执行自 C62-WILLE-RECOVERED-2026-09-26 档；本档为**真实 Wille C₆₂ 的 4 项精确清单＋不等式逐项检验＋极值特定新猜想**（唐先生 2026-09-26 16:30 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = Wille 码 3 个方阵的精确顶点表、全局 r(v) 结构、L□ 与见证计数、8 条不等式的逐项检验、去重口径回测、极值特定猜想
D1: 1（新增：**Wille 三态全表（P=60/M=6/C=6，L□=12）** ✓✓；**8 条不等式在真实极值对象上全通过** ✓✓；**极值特定猜想（M=K ⟹ L□≤S+I_nw）** ✓✓）

# WILLE-4-ITEMS-2026-09-26

## ① 三个方阵（精确顶点表 ✓）

```
$$\#1:\ \text{基点}\ 001101010,\ \text{方向}(5,6);\quad \text{顶点}\ \{000001010,\ 000101010,\ 001001010,\ 001101010\}\ \leftarrow\ \textbf{恰是 Wille 指纹四词}\ ✓✓✓$$
$$\#2:\ \text{基点}\ 101101010,\ \text{方向}(6,8);\quad \text{顶点}\ \{000101010,\ 001101010,\ 100101010,\ 101101010\}\ ✓$$
$$\#3:\ \text{基点}\ 111110101,\ \text{方向}(5,8);\quad \text{顶点}\ \{011010101,\ 011110101,\ 111010101,\ 111110101\}\ ✓$$
$$\textbf{重叠}: 3\times4=12\ \text{去重后}\ |V_\square|=\mathbf{10}\ \Longrightarrow\ \textbf{2 个共享顶点}\ ✓\ (\#1\cap\#2=\{000101010,\ 001101010\}\ ✓;\ \#3\ \text{与两者不交}\ ✓)$$
$$\boxed{\textbf{关键事实}}: \text{方阵 }\#1\ \textbf{就是} Wille 指纹四词本身\ ✓✓✓\ \Longrightarrow\ \text{唐先生的指纹 = 该码的一个方阵}\ ✓$$
$$

## ② 全局 r(v) 结构（10 个顶点 ✓）

```
$$\begin{array}{c|c|c|c|c|c}
\text{顶点} & \text{方阵数} & r(v)=|\cup| & |\cap| & |U(v)|=n-|\cap| & d_C\\
\hline
000101010 & \mathbf{2} & 3 & 1 & 8 & \mathbf{3}\ \leftarrow\text{共享}\\
001101010 & \mathbf{2} & 3 & 1 & 8 & \mathbf{3}\ \leftarrow\text{共享}\\
000001010 & 1 & 2 & 2 & 7 & 2\\
001001010 & 1 & 2 & 2 & 7 & 2\\
011010101 & 1 & 2 & 2 & 7 & 2\\
011110101 & 1 & 2 & 2 & 7 & 3\\
100101010 & 1 & 2 & 2 & 7 & 2\\
101101010 & 1 & 2 & 2 & 7 & 2\\
111010101 & 1 & 2 & 2 & 7 & 3\\
111110101 & 1 & 2 & 2 & 7 & 2\\
\end{array}$$
$$\boxed{\textbf{机制验证}\ ✓✓}:\ \text{"}|\cap|<2\ \Longrightarrow\ d_C\ge3\text{"}\ \textbf{成立}\ ✓;\quad \text{且}\ \textbf{共享顶点} \Longrightarrow d_C\ge3\ \textbf{成立}\ ✓\ (\text{两个共享顶点 }d_C=3\ ✓✓)$$
$$

## ③ L□ 与 private / witness 计数

```
$$\text{逐方阵（各 4}\times\text{(n-2)=28 壳点）}: \#1,\#2,\#3\ \text{均为}\ \mathbf{P=24,\ M=2,\ C=2}\ ✓\ (\text{三者同型}\ ✓)$$
$$\text{全局去重（U(v) 口径）}: \mathbf{P=60,\ M=6,\ C=6}\ \Longrightarrow\ \boxed{L_\square=\mathbf{12}}\ ✓$$
$$\text{见证重数分布} = \{2{:}2,\ 1{:}2\}\ \Longrightarrow\ \textbf{2 个见证重数}>1\ ✓\ (\text{重复见证机制\textbf{被实现}}\ ✓✓)$$
$$

## ④ 逐项检验此前被否的 shell 不等式（真实 Wille C₆₂）

```
$$\begin{array}{l|c|c|c}
\text{检验项} & \text{左} & \text{右} & \text{结果}\\
\hline
T1\ L_\square\le S+I_{\rm nw} & 12 & 84 & \checkmark\\
T2\ L_\square\le(n-2)(S+I_{\rm nw}) & 12 & 588 & \checkmark\\
T3\ |V_\square|\ge S_q & 10 & 3 & \checkmark\\
T4\ 4S_q\le Q_2 & 12 & 38 & \checkmark\\
T5\ 4S_q\le N_1 & 12 & 432 & \checkmark\\
T6\ I\ge|V_\square| & 27 & 10 & \checkmark\\
T7\ I_{\rm nw}\ge0 & 17 & 0 & \checkmark\\
T8\ \sum_{\rm shared}(d_C-2)\ge1 & 2 & 1 & \checkmark\\
R_2\ \text{命题（0 违反）} & — & — & \checkmark\\
\end{array}$$
$$\Longrightarrow\ \textbf{全部通过}\ ✓✓\ (\text{含此前在 }(4,8)\ \text{被否的 }T1\ ✓)$$
$$

## ⑤ ⚠️→✅ 去重口径回测：反例仍站得住，但**极值层全通过** ✓✓

```
$$\text{回测 }(4,8)\ (\text{非极小}\ M=8\gg K(4,1)=4\ ✓):$$
$$\qquad\text{实例1}: \text{口径A}\ L_\square=24\ \✗;\ \text{口径B（去重）}\ 24\ \✗\ \Longrightarrow\ \textbf{反例\textbf{仍成立}}\ ✗✓$$
$$\qquad\text{实例2/3}: \text{口径A}\ 17\ ✗;\ \text{口径B}\ 15\ \checkmark\ \Longrightarrow\ \textbf{去重口径救回部分实例}\ ✓$$
$$\textbf{全部极值实例}:\ n=4\ (0\le0\ ✓),\ n=5\ (10\le10\ \textbf{紧}\ ✓),\ n=9\ (\text{Wille}:12\le84\ ✓)\ \Longrightarrow\ \textbf{无一失败}\ ✓✓$$
$$

## ⑥ ⭐⭐ **新猜想（极值特定 ✓）**

```
$$\boxed{\text{猜想 EXT-L}\ :\quad M=K(n,1)\ \Longrightarrow\ L_\square\le S+I_{\rm nw}\ }$$
$$\text{依据（全部极值数据）}: n=4:\ 0\le0\ ✓;\quad n=5:\ 10\le10\ (\textbf{紧}\ ✓);\quad n=9\ \text{Wille}:\ 12\le84\ ✓$$
$$\text{反例仅在非极小区}: (4,8)\ (M\gg K)\ ✗\ \Longrightarrow\ \textbf{该不等式是\textbf{极值特定}的，不是一般定理}\ ✗✓$$
$$\text{与既有模式一致}: \text{与}T1/T2\ \text{筛选、}\Phi\ \text{淘汰、}\Delta\to A_{\le2}\ \text{同一"极值特定"现象}\ ✓$$
$$

## ⑦ 状态

```
$$\textbf{两项均在手}: \text{码#1}\ (\texttt{K\_9\_1.txt})\ ✓;\ \text{码#2 = 真实 Wille}\ ✓✓\ (\text{含全部 4 个 Wille 词}\ ✓)$$
$$\textbf{刚性层}: \{E,\ Q_2,\ A_{\le2},\ (N_j),\ d_{\max},\ N_1\}\ ✓✓;\quad \textbf{表示层（分叉）}: \{A_1,A_2,I,S,S_q,|V_\square|,I_{\rm nw}\}\ ✗$$
$$\textbf{机制（真实对象验证}\ ✓✓)}: \text{方阵重叠}\to\text{共享顶点}\to d_C\ge3\ \to\ h>0\ ✓$$
$$\textbf{新猜想}: \text{EXT-L}\ (\text{极值特定}\ ✓)\ \text{待证}\ ⚠️;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## ⑧ 边界（诚实标注）

- §1–§5 为**实算**（Wille 码已验证覆盖 ✓）；§6 为**猜想**（非定理 ✓，仅极值数据支持 ✓）
- **反例仍在** ✗（(4,8) 非极小区 ✓）⟹ EXT-L **不可上升为一般定理** ✗
- **未跑 solver** ✓；**未扩大任何模型** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：极值特定猜想、去重口径回测、共享顶点机制
- **档案已有（引用，不列为提出）**：方阵、见证、L□、T8
