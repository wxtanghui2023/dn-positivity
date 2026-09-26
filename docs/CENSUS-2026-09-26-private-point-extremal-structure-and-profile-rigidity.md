已查地图：已跑 scripts/prework_map_check.sh 钉住普查 private point profile 极值 ⟹ 执行自 MECHANISM-2026-09-26 档；本档为**钉住普查实做结果**（唐先生 2026-09-26 12:32 指令）；用既有 n=4,5 全枚举 ✓，未跑 solver ✓，未开 n=9 ✓。
D0: 本档对象 = 极值壳上的 private-point 一阶/二阶结构与重数剖面刚性
D1: 1（新增：**重数剖面在极值壳被强制** ✓✓（比"Q 钉住"更强）；两处否定（T4 失败、二阶 private 非极值特异））

# CENSUS-2026-09-26 · 普查结果

## §1 T1/T2 极值特异性筛（**全部通过者众** ✓）

```
$$\begin{array}{c|c|c|c}
\text{量} & M=K\ \text{恒定?} & M>K\ \text{变化?} & \text{判定}\\
\hline
Q & ✓（n=4:0;\ n=5:2） & ✓ & \textbf{极值特异}\ ✓\\
A_{\le2} & ✓（2;\ 6） & ✓ & \textbf{极值特异}\ ✓\\
\text{私有点总数 }P & ✓（12;\ 24） & ✓ & \textbf{极值特异}\ ✓\\
\sum_c r(c)^2 & ✓（36;\ 90） & ✓ & \textbf{极值特异}\ ✓\\
\min_c r(c) & ✓（3;\ 3） & ✓（降至 0） & \textbf{极值特异}\ ✓\\
\max_c r(c) & ✓（3;\ 6） & ✓ & \textbf{极值特异}\ ✓\\
P_{2,\mathrm{self}} & ✓ & ✓ & \textbf{极值特异}\ ✓\\
P_2\ (\text{原始二阶}) & \textbf{✗}（n=4,M=4:\{32,36\}） & ✓ & \textbf{非极值特异}\ ✗\\
\end{array}$$
$$

## §2 ⭐⭐ **本轮头条：重数剖面本身在极值壳被强制** ✓✓

```
$$\text{剖面} := \bigl(N_j\bigr)_{j\ge1},\ N_j=\#\{x:b(x)=j\}\ ✓$$
$$\textbf{n=4}: M=4(=K):\ \textbf{剖面唯一}:\ (N_1,N_2)=(12,4)\ ✓✓\ (\text{40 个码全同}\ ✓)$$
$$\qquad\qquad M=5:\ 2\ \text{种剖面}\ ✗;\quad M=6:\ 5\ \text{种剖面}\ ✗$$
$$\textbf{n=5}: M=7(=K):\ \textbf{剖面唯一}:\ (24,6,2)\ ✓✓\ (\text{320 个码全同}\ ✓)$$
$$\qquad\qquad M=8:\ 5\ \text{种剖面（采样）}\ ✗$$
$$\boxed{\text{极值壳}\ (M=K)\ \Longrightarrow\ \textbf{重数剖面被强制；}M>K\ \text{时立即释放}\ ✓✓}$$
$$\Longrightarrow\ \text{因 }Q\ \text{是剖面的函数}\ ✓,\ \textbf{Q 的钉住是"剖面强制"的推论}\ ✓\ ——\ \text{机制靶点应上移为\textbf{剖面}}\ ✓✓$$
$$

## §3 ⛔ 否定①：T4 对 private 量**失败**（换皮 ✓）

```
$$\textbf{恒等发现}: \boxed{P=\sum_c r(c)=N_1}\ ✓✓\ (\text{全部 }n,M\ \text{无一例外}\ ✓)$$
$$\text{（理}: \text{被恰好一个码字覆盖的点}\ \iff\ \text{该码字的私有点}\ ✓）$$
$$\Longrightarrow\ P\ \text{是\textbf{剖面的函数}}\ ✓\ \text{与 }Q\ \text{同源}\ ✗\ \Longrightarrow\ \text{corr}(Q,P)=1.0000\ (n{=}4,M{=}5)\ \text{只是\textbf{剖面刚性的后果}}\ ✗$$
$$\text{同理}: \text{私有点向量 }r\ \text{的\textbf{多重集}在 }n=5,M=7\ \text{就有 6 种}\ ✗\ (\text{非恒定}\ ✓)\ \Longrightarrow\ r\ \text{向量不满足 T1}\ ✗$$
$$\text{（n=4,M=4 例外: }r=(3,3,3,3)\ \textbf{唯一}\ ✓✓\ ——\ \text{但那是最小情形的巧合，非普遍}\ ✗）$$
$$

## §4 ⛔ 否定②：二阶 private incidence **不是**极值特异（唐先生"最值得查"项 ✗）

```
$$P_2=\sum_{c,d}|\mathrm{Priv}(c)\cap B_2(d)|\ \text{在 }n=4,M=4(=K)\ \text{上取 }\{32,36\}\ \textbf{两种值}\ ✗$$
$$\Longrightarrow\ \text{它\textbf{在极值壳上就不恒定}}\ ✗\ \Longrightarrow\ \text{不满足 T1，直接淘汰}\ ✗\ (\text{无需再看 T2–T4}\ ✓)$$
$$

## §5 L(c)≥1 的地位（T3 ✓ 但非刻画 ✗）

```
$$L(c):=\#\{x:\ x\ \text{仅由 }c\ \text{覆盖}\}=r(c)\ ✓\ (\text{同一量}\ ✓)$$
$$\text{尺寸最小性}\Longrightarrow L(c)\ge1\ \forall c\ ✓\ (\textbf{可证}\ ✓,\ \text{私有点引理}\ ✓)\ \Longrightarrow\ T3\ \textbf{通过}\ ✓$$
$$\text{但反面\textbf{不成立}}\ ✗:\ n=5,M=8\ \text{有 }r_{\min}\in\{1,2,3\}\ \text{的码}\ ✓\ \Longrightarrow\ L\ge1\ \textbf{不刻画最优性}\ ✗$$
$$

## §6 机制问题的**收窄**（本轮最大战略收益 ✓）

```
$$\text{原先}: \text{"为什么 }Q\ \text{被钉住？"}\ ✗\ (\text{间接}\ ✓)$$
$$\boxed{\text{现在}: \text{"为什么 }|C|=K(n,1)\ \text{会强制重数剖面 }(N_j)\ \text{？"}}\ ✓✓\ (\text{更本质、更干净}\ ✓)$$
$$\text{可类比}: \text{NP1CC 论文从\textbf{界取等}推出剖面/距分布}\ ✓\ ——\ \text{我们观察到\textbf{最小 }M\ \text{同样强制剖面}}\ ✓$$
$$\qquad\Longrightarrow\ \text{候选统一机理}: \boxed{\text{极值性（取等 or 最小 }M)\Longrightarrow\text{incidence 结构被强制}}\ ✓\ (\text{待证}\ ✗)$$
$$

## §7 三张表 ＋ 下一步

```
$$\textbf{CLOSED}: \ldots;\ \textbf{剖面在极值壳唯一（}n=4,5\ \text{全枚举}\ ✓✓）;\ P=N_1\ \text{恒等};\ \text{私有点引理};L\ge1\ \text{非刻画};\ P_2\ \text{非极值特异}\ ✗$$
$$\textbf{OPEN}: \textbf{极值}\Rightarrow\text{剖面强制（机理）};\ n=6\ \text{的剖面刚性检验};\ \text{非取等 }n\ \text{的 }Q^*;\ \textbf{119 UNKNOWN}\ ✓$$
$$\text{下一步}: \text{① }n=6,M=12\ \text{的目标搜索（收集多个 }(6,12)_1\ \text{码）⟹ 检验剖面是否唯一}\ ✓\ (\text{需构造/局部搜索，预估 }10\text{--}30\ \text{分钟}\ ⚠️)$$
$$\qquad\quad\text{② 若 }n=6\ \text{亦唯一} \Longrightarrow\ \text{立"\textbf{极小覆盖码剖面刚性}"猜想，并找可证来源}\ ✓$$
$$\qquad\quad\text{③ 纪律}: \text{不跑更大 }n\ ✗;\ 119\ \text{保持 UNKNOWN}\ ✓$$
$$

## §8 边界（诚实标注）

- §1–§5 全部为**既有穷举数据**（n=4 全枚举 ✓、n=5 M=7 全枚举 ✓、n=5 M=8 采样 ✓）＋**我方代码** ✓
- §2 的"剖面强制"对 n=4,5 为**事实** ✓；对一般 n 为**猜想** ✗（明确标注 ✓）
- **未跑 solver** ✓；**未**开 n=9 ✗；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 profile 强制   命中文件数=0    :: 
技术词 重数剖面     命中文件数=3    :: ./X1-K10-2-results-rigidity-and-negative-neighbourhoods.md ./X1-K10-3-rigidity-certificate-1-1-2-1-3-2.md ./ASSET-TO-PROBLEM-MATCHING-v1.md 
技术词 删除敏感度  命中文件数=0    :: 
技术词 私人点向量  命中文件数=0    ::
```

- **本档新增**（命中数=0）：删除敏感度、私人点向量
- **档案已有（引用，不列为提出）**：重数剖面
