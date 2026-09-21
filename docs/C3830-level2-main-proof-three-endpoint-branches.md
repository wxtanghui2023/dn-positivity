已查地图（**先查后写**）：`C-380-29`（**`m = -1/8` 切片解析闭合** ✓✓）、`C-380-28`（**二维靶点** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-30：Level-2 主证明档（三端点分支）（注册＋三分支精确代入）**，**有计算（符号，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 端点原则（严格化，采纳）}✓✓：\text{对固定}\ m < -\tfrac18✓，\ \text{令}\ \mathcal S_m = \{s : Q_2, Q_3, Q_4 \le -\tfrac12,\ s \ge m^2\}✓✓$$
$$\qquad \text{若}\ \mathcal S_m\ \text{为}\ \textbf{闭区间}（\text{或空集}）✓，\ \text{且}\ B_m\ \textbf{凸}✓，\ \text{则}\ \boxed{\max_{s \in \mathcal S_m}B_m(s) = \max_{s \in \partial\mathcal S_m}B_m(s)}✓✓$$
$$\qquad \Longrightarrow \ \textbf{「端点原则」是严格的}✓✓，\ \textbf{而非数值直觉}✗✓ \ —— \ \textbf{但须先证}\ \partial\mathcal S_m\ \text{确实构成完整的可行边界集}✓✓$$
$$\qquad \text{且}\ \min_sQ_5 = 4m\max_sB_m(s)✓（\text{因}\ m < 0✓） \Longrightarrow \ \textbf{任务降为三分支}✓✓$$
$$\textbf{② ⭐ 分支 A（}s = \tfrac{7}{16}✓，Q_2\ \text{活跃}）✓✓：\text{精确代入}\ \Longrightarrow Q_5(m, \tfrac{7}{16}) = -256m^5 + 160m^3 - \tfrac{95m}{4}✓✓$$
$$\qquad \Longrightarrow \ \boxed{Q_5 - \tfrac{341}{128} = -\frac{(8m+1)P(m)}{128}}✓✓，\ P(m) = 4096m^4 - 512m^3 - 2496m^2 + 312m + 341✓✓$$
$$\qquad \qquad ⭐ \textbf{因式分解如愿出现}✓✓（\text{即}\ -(8m+1) = 8(-m - \tfrac18)✓）$$
$$\qquad \qquad ⚠️ \textbf{但}✗✓：P(-1) = 2141✓，\ P(-\tfrac34) = 215✓，\ \boxed{P(-\tfrac12) = -119}✗✓，\ P(-\tfrac14) = 131✓，\ P(-\tfrac18) = 265✓$$
$$\qquad \qquad \Longrightarrow P\ \textbf{有两个实根}✗✓，\ \text{在}\ m \approx -\tfrac12\ \text{附近}\ P < 0✗✓ \Longrightarrow \ \textbf{该分支不能仅靠因式分解闭合}✗✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{须用}\ Q_3\ \text{的}\ \textbf{容许性限制}✓✓（s = \tfrac{7}{16} \ge A(m)✓） \Longrightarrow \ \textbf{本分支}\ \textbf{未闭合}✗✓$$
$$\textbf{③ 分支 B（}s = A(m)✓，Q_3\ \text{活跃}）✓✓：\text{分子为 6 次多项式}✓✓：-131072m^6 + 122880m^4 - 5120m^3 - 23040m^2 - 2109m + 40✓（\text{分母}\ 1152m✓）$$
$$\qquad \qquad \textbf{在}\ m = -\tfrac18✓：\text{分子} = -\tfrac{135}{8}✓ \Longrightarrow Q_5 - \tfrac{341}{128} = \boxed{+0.1172 > 0}✓✓（Q_5 = \tfrac{89}{32} = 2.781✓✓）$$
$$\qquad \qquad \Longrightarrow \ \textbf{局部为正}✓✓；\ \textbf{全域未证}✗✓$$
$$\textbf{④ ⭐ 分支 C（}Q_4 = -\tfrac12✓）✓✓：\text{用}\ Q_4 = -\tfrac12\ \textbf{消掉}\ s^2✓✓：\boxed{s^2 = 4m^4 - 4m^2s + s - \tfrac{9}{64}}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{把}\ Q_5\ \textbf{降成关于}\ s\ \textbf{的一次式}✓✓：Q_5\big|_C = -m(-1024m^4 + 1280m^2s - 160m^2 - 80s + 25)✓✓$$
$$\qquad \qquad ⭐ \textbf{斜率} = -80m(16m^2 - 1)✓✓ \Longrightarrow \textbf{变号点在}\ m = -\tfrac14✓✓（\text{新结构}✓）$$
$$\qquad \qquad \Longrightarrow \ \textbf{这比直接处理根式干净得多}✓✓（\text{唐先生建议采纳}✓✓）；\ \textbf{但全域仍需结合}\ Q_2\ \text{或}\ Q_3\ \text{边界}✗✓$$
$$\textbf{⑤ }m = -\tfrac18\ \text{三支对照}✓✓：Q_5(s = \tfrac{7}{16}) = \boxed{\tfrac{341}{128}}✓✓（\textbf{等号点}✓）；\ Q_5(s = A) = \tfrac{89}{32} = 2.781 > \tfrac{341}{128}✓✓$$
$$\textbf{⑥ 诚实状态}✗✓：\textbf{Level 2 未闭合}✗✓ \ —— \ \text{三分支}\ \textbf{均未完成} \text{全域证明}✓；\ \textbf{但结构已彻底简化}✓✓：$$
$$\qquad \text{端点原则}✓ ＋ \text{A 因式分解}✓ ＋ \text{B 局部正}✓ ＋ \text{C 线性化}✓✓ \Longrightarrow \ \textbf{后续只需}\ \text{容许性} ＋ \text{单调性}✓$$
$$\textbf{⑦ 纪律（必须守住）}✓✓：\ \boxed{\text{two-level closure} \not\Rightarrow \mathcal F_0 = \varnothing}✓✓；\ \text{下一阶段才是}\ \text{一般四点与}\ \Delta_4 = 0\ \text{的距离关系}✓✓$$
$$\textbf{⑧ 账本}✓✓：\text{见 §2}✓$$

## §1 符号记录（✓✓）

$$\textbf{A}✓✓：Q_5(m, \tfrac{7}{16}) = -256m^5 + 160m^3 - \tfrac{95m}{4}✓；\ \text{乘 128 后因式}\ -(8m+1)(4096m^4 - 512m^3 - 2496m^2 + 312m + 341)✓✓$$
$$\textbf{B}✓✓：\text{分母}\ 1152m✓；\ \text{分子（6 次）}✓；\ \text{六次项}\ -131072m^6✓$$
$$\textbf{C}✓✓：s^2\ \text{替换式}✓；\ Q_5|_C\ \text{线性形式}✓；\ \text{斜率}\ -80m(16m^2 - 1)✓；\ \text{常数}\ m(1024m^4 + 160m^2 - 25)✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}29` ✓ | **PARTIAL LEVEL-2 ANALYTIC CLOSURE** ✓✓ |
| 端点原则 ✓ | **本档：严格陈述完成** ✓✓ |
| 分支 A ✓ | **因式分解完成；全域未闭合（P 变号）** ✗✓ |
| 分支 B ✓ | **`m = -\tfrac18` 处正；全域未证** ✗✓ |
| 分支 C ✓ | **降为 `s` 一次式；全域未证** ✗✓ |
| Level 2 ✓ | **OPEN（三分支结构已建立）** ✗✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **未解析证明** ✗✓ |
| Level 3 ✓ | **尚未启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓；\ \inf = \tfrac{341}{128}\ \text{已证}✗✓；\ \text{分支 A 已闭合}✗✓；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{因式分解}\ \textbf{不等于} \text{闭合}✗✓；\ \text{本档为}\ \textbf{结构档}✓✓，\ \text{非闭合档}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不做}全局二维搜索✗✓；\textbf{不}上\ SOS／Gram✗✓；\textbf{不}把\ B_m\ \text{凸性当充分证明}✗✓；\textbf{不}从「边界被杀」跳到「完整模型被杀」✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy 精确代入／因式分解，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 端点原则严格化 命中文件数=0    :: 
技术词 分支线性化  命中文件数=0    :: 
技术词 容许性限制  命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（sympy 三支代入 ＋ 因式分解 ＋ 根计数 ✓）
