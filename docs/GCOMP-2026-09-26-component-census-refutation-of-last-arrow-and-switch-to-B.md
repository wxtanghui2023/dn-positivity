已查地图：已跑 scripts/prework_map_check.sh G_C 连通分量 路径 K13 三角形 ⟹ 执行自 REPAIR-2026-09-26 档；本档为**G_C 连通分量普查＋最后箭头否证＋转 ② 决定**（唐先生 2026-09-26 15:22 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = G_C（距离-1 图）连通分量结构、极值壳上的路径/分支普查、"I≥3⟹h>0"的否证
D1: 1（新增：**I≥3⟹h>0 被否（30 反例）** ✗✓；**极值壳上 G_C 为线性森林且 maxpath≤2（数据）** ✓；**分支仅出现在非极值壳** ✓）

# GCOMP-2026-09-26

## §0 ✅ 几何事实（唐先生 ✓）：三角形/K₄ 不可能

```
$$\text{若 }a,b,c\ \text{两两距离 1}\ ✓:\ a+b=e_i\ ✓,\ b+c=e_j\ ✓\ \Longrightarrow\ a+c=e_i+e_j\ \text{权重}\ 2\ ✗\ (\text{除非 }i=j\Rightarrow a=b=c\ ✗)$$
$$\Longrightarrow\ \textbf{无三角形}\ ✓;\ K_4\ \text{同理}\ ✗;\ G_C\subseteq Q_n\ \text{诱导子图}\ \Longrightarrow\ \textbf{二分}\ ✓\ (\text{无奇环}\ ✓)$$
$$\text{定级}: \textbf{P0 几何事实}\ ✓\ (\text{非新 P1}\ ✗)\ ——\ \text{唐先生判断正确}\ ✓$$
$$

## §1 ⛔ **"额外 wedge ⟹ I≥3 ⟹ h>0" 被否** ✗✓（关键纠正）

```
$$\text{逻辑}: h\le I/3\ ⟹\ I\ge3\ \text{只给}\ h\le1\ ✗\ ——\ \textbf{推不出 }h>0\ ✗$$
$$\textbf{数值反例}: 180\ \text{样本中}\ I\ge3\ \text{且}\ h=0\ \text{的样本} = \mathbf{30}\ ✗✓$$
$$\qquad\text{例}: (n{=}4,M{=}6):\ I=4,\ h=0,\ \deg_{\max}=2,\ \text{两个 path 分量}\ ✓\ (\text{maxpath}=3\ ✓)$$
$$\Longrightarrow\ \textbf{路径/wedge 本身完全不迫使 }h>0\ ✗\ ——\ \text{唐先生最后一个箭头\textbf{不成立}}\ ✗✓$$
```

## §2 ⭐ **极值壳 G_C 结构普查（本轮产品 ✓）**

```
$$\begin{array}{c|c|c|c|c|c|c}
(n,M) & \text{态} & I & h & \deg_{\max} & \text{分量类型} & \text{maxpath}\\
\hline
(4,4)=K & \text{极值} & 0 & 0 & \le1 & \textbf{全 path} & \le1\\
(4,5) & >K & 0,1,3 & 0,1 & 1,2,3 & \text{path}+\text{branch}(3) & \le2\\
(4,6) & >K & 1..6 & 0,1 & 2,3,4 & \text{path}+\text{branch}(3),(4) & \le5\\
(5,7)=K & \text{极值} & 1 & 0 & \mathbf{2} & \textbf{全 path（300/300）} & \mathbf{2}\\
(5,8) & >K & 1..8 & 0,1 & 2,3 & \text{path}+\text{branch}(3) & \le5\\
\end{array}$$
$$\textbf{极值壳结论}: (4,4):\ \deg\le1\ ✓\ (\text{孤立点+边}\ ✓);\ (5,7):\ \deg=2\ \text{且全部是 path}\ ✓,\ \text{maxpath}=2\ ✓,\ \text{结构}=\{P_3\}\cup\{4\ \text{孤立点}\}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{极值壳上无长度}\ge3\ \text{的路径}\ ✓✓}\ (\text{唐先生问句的答案：}\textbf{否}\ ✗)\ ——\ \text{且 }n=6\ \text{由 }h=0\ \text{推 }\deg\le2\ ✓$$
$$\qquad\Longrightarrow\ \textbf{分支（}K_{1,3}\text{）只出现在非极值壳}\ ✓✓\ (M>K\ \text{时 }\deg\ \text{达 }3,4\ ✗)$$
$$

## §3 诚实定级

```
$$\textbf{本轮成果}: \text{① 否证"wedge⟹h>0"（30 反例）}\ ✗✓;\ \text{② 极值壳 }G_C\ \text{为线性森林、maxpath}\le2\ (\text{数据}\ ⚠️,\ \textbf{未证}\ ✗)$$
$$\textbf{未获}: \text{任何与 }M=K\ \text{的矛盾}\ ✗\ \Longrightarrow\ \textbf{按唐先生判据：应转 ②（}n=9\ \text{构造）}\ ✓✓$$
$$\text{为何到此为止}: \text{① 无三角形/K}_4\ \text{是 P0}\ ✓;\ \text{② I}\le2A_2\ \text{已取等}\ ✗;\ \text{③ 路径结构无矛盾}\ ✗\ \Longrightarrow\ \textbf{超立方体禁形路线收益已尽}\ ✗✓$$
$$

## §4 转 ② 的理由与形态

```
$$\text{为什么要 }n=9:\ \textbf{唯一能引入新数据}（\text{打破 }n\le6\ \text{局限}\ ✓）;\ \text{且 }K(9,1)=62\ \text{已确证}\ [L]\ ✓$$
$$\text{已知难点}: \text{文献 }62\ \text{码的显式构造只在 Wille 1996 正文（付费/未获）}\ ✗;\ \text{我方早期搜索未达 }62\ ✗$$
$$\text{可行的入口}: \text{① 用 }n=9\ \text{的 }M=62\ \text{码测 }I\ \text{是否}\le2\ ✓\ (\text{若 }\{0,2\}\ \text{则猜想延续}\ ✓);\ \text{② 继续向文献索取 Wille 构造}\ ✓$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §5 边界（诚实标注）

- §0 为**证明** ✓；§1 为**数值否证**（180 样本，30 反例 ✓）；§2 为**数值普查**（n=4,5 全枚举 ✓）
- §1/§2 的"极值壳无分支"为**数据结论** ⚠️（**未证** ✗，不得当定理 ✓）
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 连通分量普查 命中文件数=1    :: ./GCOMP-2026-09-26-component-census-refutation-of-last-arrow-and-switch-to-B.md 
技术词 线性森林结构 命中文件数=1    :: ./GCOMP-2026-09-26-component-census-refutation-of-last-arrow-and-switch-to-B.md 
技术词 分支仅非极值 命中文件数=1    :: ./GCOMP-2026-09-26-component-census-refutation-of-last-arrow-and-switch-to-B.md 
技术词 楔形不迫高度 命中文件数=1    :: ./GCOMP-2026-09-26-component-census-refutation-of-last-arrow-and-switch-to-B.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：连通分量普查、线性森林结构、分支仅非极值、楔形不迫高度
- **档案已有（引用，不列为提出）**：minimality、excess、A≤2
