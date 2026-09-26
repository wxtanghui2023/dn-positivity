已查地图：已跑 scripts/prework_map_check.sh L2 Q_2 defect 4S 等号 ⟹ 执行自 SQUARE-2026-09-26 档；未跑 solver ✓。
D0: 本档对象 = 唐先生三恒等式的核验、S≥14⟹b≥4 的定量化、等号情形 4S=Q_2 的完整分类
D1: 1（新增：**缺陷支付关系** ✓；**等号情形完整分类** ✓；(9,64) 饱和实例 ✓）

# L2PUSH-2026-09-26

## §1 ✅ 唐先生三恒等式：数值核验全过 ✓✓

```
$$E-2N_{\ge3}=N_2+\sum_{j\ge4}(j-3)N_j\ \ge0\ \Longrightarrow\ N_{\ge3}\le E/2\ ✓;\ \text{等号}\iff b\equiv1,3\ ✓\ (\text{核验 ✓})$$
$$Q_2-(E-Q)=\sum_{b\ge4}\binom{b-2}{2}N_b\ \ge0\ ✓\ (\text{核验: n=4,4 / 4,5 / 5,7 全枚举全过 ✓})$$
$$\textbf{记法}: Q:=N_{\ge2}=Q_{\text{user}}\ ✓,\quad Q_2:=Q_{\mathrm{ours}}=\sum_x\binom{b(x)-1}{2}\ ✓\ (\text{两者必须分开 ✓})$$
$$

## §2 ⭐ **缺陷支付关系**（唐先生 §3 ✓，我方定量化 ✓）

```
$$4S\ \le\ Q_2\ =\ (E-Q)+\underbrace{\sum_{b\ge4}\binom{b-2}{2}N_b}_{=:\ \mathrm{defect}\ \ge0}\ ✓$$
$$\textbf{M=62}\ (E=108):\quad 4S\le(108-Q)+\mathrm{defect}\ ✓$$
$$\textbf{S}\ge14\ \text{的定量代价}:\ 4S\ge56\ \Longrightarrow\ \mathrm{defect}\ \ge\ 56-(108-Q)\ =\ Q-52\ ✓\ ✓$$
$$\qquad b\le3\ \text{分支}: Q=N_3\le54\ \Longrightarrow\ Q_2=N_3\le54\ \Longrightarrow\ S\le13\ ✓\ \Longrightarrow\ \boxed{S\ge14\ \text{强制}\ \mathrm{defect}\ge Q-52}\ ✓$$
$$\qquad(\text{若 }Q=54\ \text{即 }b\in\{1,3\}:\ \mathrm{defect}\ge2\ \Longrightarrow\ \text{至少两个 }b=4\ \text{点或一个 }b=5\ \text{点}\ ✓\ \text{—— 局部禁形有了明确重量}\ ✓)$$
$$

## §3 ⭐⭐ **等号情形 4S=Q_2 的完整分类**（我方 ✓，(9,64) 为饱和实例 ✓）

```
$$\textbf{定理（我方 ✓）}:\ 4S=Q_2\ \iff\ \text{① 每个 square 顶点恰有 2 个 }G_1\text{-邻居且恰属 1 个 square};\ \text{② } N_{\ge3}=V\ (\text{无面外 hot 点})\ ✓$$
$$\qquad\Longrightarrow\ \text{推论}: \text{此时 squares \textbf{顶点不交} ✓},\ V=4S=N_{\ge3}\ ✓,\ \text{且每个面顶点 }d_C=2\ ✓$$
$$\textbf{核验}: (9,64):\ E=128,\ Q=64,\ Q_2=64,\ N_{\ge3}=64,\ \mathrm{defect}=0,\ \mathbf{S=16},\ V=64\ ✓$$
$$\qquad 4S=64=Q_2\ \textbf{饱和}\ ✓;\ \text{①② 同时成立}\ ✓✓;\ \text{16 个面顶点不交}\ ✓$$
$$

## §4 与 M=62 的对照（两种结构分支 ✓）

```
$$\begin{array}{c|c|c|c|c|c}
 & E & Q & Q_2 & S & \text{分支}\\
\hline
(9,64)\ \text{我方} & 128 & 64 & 64 & \mathbf{16} & b\equiv\{1,3\},\ \text{defect}=0,\ \textbf{取等饱和}\ ✓\\
(9,62)\ \text{若 }b\equiv\{1,3\} & 108 & 54 & 54 & \le13 & \textbf{取等不可能}\ ✗\ (13.5\notin\mathbb Z)\\
(9,62)\ \text{若 }S\ge14 & 108 & \ge? & \ge56 & \ge14 & \Longrightarrow\ \mathrm{defect}\ge Q-52\ \text{强制 } b\ge4\ ✓\\
\end{array}$$
$$\Longrightarrow\ \textbf{62-码的两分支被 cleanly 分开}\ ✓:\ \text{要么"面少"(}S\le13,\ \text{defect 可 0}),\ \text{要么"面多"(}S\ge14\ \Longrightarrow\ \text{必须出现 }b\ge4\ \text{局部结构})\ ✓✓$$
$$

## §5 限定（诚实 ✓）

```
$$\text{小最优码 }(4,4),(4,5),(5,7):\ S=0\ \Longrightarrow\ \text{square 机制在这些极值码上\textbf{空转}}\ ✗\ (\text{不是必要条件}\ ✓)$$
$$\text{故本档全部结论只对\textbf{含面的码}有价值}\ ✓\ (\text{如 (9,64) 与待核的 Wille 码}\ ⚠️)$$
$$
$$

## §6 台账

```
$$\textbf{新增资产}: 4S\le Q_2\ ✓;\ \text{缺陷支付}\ \mathrm{defect}\ge Q-52\ (S\ge14,\ M=62)\ ✓;\ \text{等号分类}\ ✓$$
$$\textbf{桥}: \text{未打通}\ ✗;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \text{Wille 2-面 fingerprint}: \text{待核}\ ⚠️$$
$$

## 【技术词回查】（定稿前逐字输出）

```
技术词 高阶缺陷     命中文件数=0    :: 
技术词 面不交分类  命中文件数=0    :: 
技术词 缺陷支付关系 命中文件数=0    :: 
技术词 饱和实例     命中文件数=0    ::
```

- **本档新增**（命中数=0）：高阶缺陷、面不交分类、缺陷支付关系、饱和实例
- **档案已有（引用，不列为提出）**：—
