已查地图：已跑 scripts/prework_map_check.sh EXT-L 极值普查 逐顶点收费 ⟹ 执行自 WILLE-4-ITEMS-2026-09-26 档；本档为**EXT-L 全极值普查＋三条否证性发现＋目标重估**（唐先生 2026-09-26 16:28 裁定甲 ✓）；未跑 solver ✓。
D0: 本档对象 = 6 个极值实例的 EXT-L 普查表、逐顶点收费规则检验、方阵表示依赖性发现、EXT-L 降级建议
D1: 1（新增：**6 实例普查表** ✓✓；**逐顶点朴素规则被真实极值对象否证** ✗✓；**方阵非极值不变量（S_q∈{0,3}）** ✓✓）

# EXTL-CENSUS-2026-09-26

## §0 ⚠️ 口径纠正（先纠后算 ✓）

```
$$\text{唐先生原写}\ L_\square=P-M-C\ ✗\ \longrightarrow\ \textbf{实测口径为}\ \boxed{L_\square=M+C}\ ✓\ (\text{private 不计入}\ ✓)$$
$$\text{验证}: \text{Wille 码 }P=60,\ M=6,\ C=6\ \Longrightarrow\ M+C=12=L_\square\ ✓✓;\quad (9,64):\ 0+0=0\ ✓$$
$$

## §1 ⭐⭐ **六个极值实例的完整普查表**

```
$$\begin{array}{c|rrrr|rr|rrrrr}
\text{实例} & L_\square & S & I_{\rm nw} & \mathbf D & E & Q_2 & |V_\square| & S_q & \sum(r{-}2)_+ & \sum_{\rm sh}(d_C{-}2) & \#{\rm rep}\\
\hline
(4,4)=K & 0 & 0 & 0 & \mathbf{+0} & 4 & 0 & 0 & \mathbf 0 & 0 & 0 & 0\\
(5,7)=K & 0 & 7 & 1 & +8 & 10 & 2 & 0 & \mathbf 0 & 0 & 0 & 0\\
(6,12)=K\ \text{类#1} & 0 & 14 & 2 & +16 & 20 & 4 & 0 & \mathbf 0 & 0 & 0 & 0\\
(6,12)=K\ \text{类#2} & 0 & 24 & 0 & +24 & 20 & 4 & 0 & \mathbf 0 & 0 & 0 & 0\\
(9,62)=K\ \text{码#1} & 0 & 126 & 6 & +132 & 108 & 38 & 0 & \mathbf 0 & 0 & 0 & 0\\
(9,62)=K\ \text{码#2 (Wille)} & \mathbf{12} & 67 & 17 & \mathbf{+72} & 108 & 38 & \mathbf{10} & \mathbf 3 & 10 & 2 & 2\\
\end{array}$$
$$\Longrightarrow\ \text{全部 }D\ge0\ ✓\ (\text{EXT-L 在极值层\textbf{未遇反例}}\ ✓)$$
$$

## §2 ⛔ **否证性发现①：EXT-L 在极值层几乎全是平凡的** ✗

```
$$\textbf{六个极值实例中，只有 Wille 码一个 }S_q>0\ ✗\ \Longrightarrow\ \text{其余五个 }L_\square=0\ \Longrightarrow\ \text{EXT-L \textbf{平凡成立}}\ ✗$$
$$\qquad\Longrightarrow\ \text{EXT-L 的\textbf{非平凡证据只有 1 个数据点}}\ ✗\ \text{且该点 }D=+72\ (\textbf{毫无紧性})\ ✗$$
$$

## §3 ⛔ **否证性发现②：逐顶点朴素收费规则被真实极值对象否证** ✗✓

```
$$\text{候选规则}: L_v\le (d_C(v)-2)_+ + s_v$$
$$\text{实测}: \textbf{Wille 码违反 2 处}\ ✗✓\ ——\ \text{恰是两个共享顶点}\ (000101010,\ 001101010):\ L_v=2\ \text{而右端}=1\ ✗$$
$$\text{（其余 8 个顶点均紧 }\checkmark)$$
$$\text{加"重叠罚项"后的修正式}: L_v=(d_C(v)-2)_+ + s_v + (m(v)-1)\ \text{在 10 个顶点上\textbf{全部取等}}\ ✓\ (m=\text{方阵数})$$
$$\qquad\text{但此式在单一实例上取等 }\Longrightarrow\ \text{可能是\textbf{定义性恒等}}\ ✗\ \text{而非定理}\ ⚠️\ (\text{不予登记为资产}\ ✗)$$
$$

## §4 ⛔⛔ **否证性发现③（最重要）：方阵不是极值不变量** ✗✗

```
$$\text{两个}M=K(9,1)=62\ \text{最优码}: S_q\in\{0,\ 3\}\ ✗;\quad |V_\square|\in\{0,\ 10\}\ ✗;\quad L_\square\in\{0,\ 12\}\ ✗$$
$$\qquad\text{但刚性量完全相同}: Q_2=38\ ✓,\ (N_j)=\{1{:}432,2{:}62,3{:}8,4{:}10\}\ ✓,\ d_{\max}=3\ ✓$$
$$\Longrightarrow\ \boxed{\text{方阵结构\textbf{由表示决定}，不影响刚性层}}\ ✓✓$$
$$\Longrightarrow\ \textbf{EXT-L 无法连接到刚性层}\ ✗\ ——\ \text{即使证出 EXT-L，也不解释"为何 }Q_2/\ (N_j)\ \text{刚性"}\ ✗$$
$$

## §5 判决与建议（诚实 ✓）

```
$$\boxed{\textbf{EXT-L 应降级}}\ ⚠️\ \text{理由四条}:\ \text{(i) 极值层 5/6 平凡}\ ✗;\ \text{(ii) 唯一非平凡点 }D=72\ \text{无紧性}\ ✗;\ \text{(iii) 逐顶点朴素规则被否证}\ ✗;\ \text{(iv) 方阵非极值不变量}\ ✗✗$$
$$\text{保留为已登记事实}: \text{全部极值实例 }D\ge0\ ✓\ (\text{弱支持}\ ⚠️);\ \text{机制"共享顶点}\Rightarrow d_C\ge3"\ \text{在真实对象验证}\ ✓✓\ (\text{该机制\textbf{不}依赖 EXT-L}\ ✓)$$
$$\text{资源应收束到}: \boxed{\text{为何 }Q_2=38\ \text{与 }(N_j)\ \text{刚性（两码同值、跨表示不变）}}\ ✓✓\ ——\ \text{唯一有跨表示证据的靶心}\ ✓$$
$$

## §6 状态

```
$$\textbf{两码在手}\ ✓;\ \textbf{刚性层}\ \{E,Q_2,A_{\le2},(N_j),d_{\max},N_1\}\ ✓✓;\ \textbf{表示层}\ \{S_q,|V_\square|,L_\square,I,S,A_1,A_2,I_{\rm nw}\}\ ✗$$
$$\textbf{EXT-L}: \text{降级为弱猜想}\ ⚠️\ (\text{不投入主要资源}\ ✓);\quad \textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §7 边界（诚实标注）

- §1–§4 为**实算**（6 实例全部验证覆盖 ✓）；§4 的"表示决定"为**两码对照的直接推论** ✓
- §3 的修正式**仅在单实例取等** ⟹ **不登记为定理/资产** ✗（纪律 ✓）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：极值普查表、表示依赖性、重叠罚项
- **档案已有（引用，不列为提出）**：EXT-L、逐顶点收费、方阵
