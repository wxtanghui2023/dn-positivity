已查地图：已跑 scripts/prework_map_check.sh 符号 Q A₂ E 钉住 ⟹ 执行自 PINNING-2026-09-26-n6-literature-code-closed 档；本档为**符号锁定 ＋ 类级数据**（唐先生 2026-09-26 10:59 指令）；不开新方向 ✓。
D0: 本档对象 = 记号规范与 n≤8 类级数据（非新对象）
D1: 0（无新自由度；产出为符号锁定与类级 A₁/A₂ 数据）

# PINNING-NOTATION-LOCK-2026-09-26

## §1 先做**零命中核验**（唐先生要求 ✓；结果：**档案无混用，不虚构 erratum** ✓）

```
$$\text{① 搜 } \texttt{Q=A_2}\ /\ \texttt{Q=A₁}\ /\ \texttt{"Q 就是距离 2 对数"}:\ \textbf{0 命中}\ ✓\ (\text{档案从未混用 ✓})$$
$$\text{② 恒等式表述 } \texttt{Q=2(A_1+A_2)-E}:\ \text{已存在且写法正确}\ ✓$$
$$\text{③ } E\ \text{定义}: \texttt{E=K(n,1)·(n+1)-2^n}\ \text{（正确形）}\ ✓;\ \text{未见任何 } \texttt{n=4, E=0}\ \text{之误}\ ✗$$
$$\text{④ 检索命中的 } \texttt{4 & 4 & 4 & 0}\ \text{为状态表行 } (n,K,E,Q)=(4,4,\mathbf{4},\mathbf{0})\ ✓\ \text{非 }E=0\ ✓$$
$$\Longrightarrow\ \textbf{不需要勘误} ✗;\ \text{改为增设"\textbf{符号锁定}"节（防未来漂移 ✓）}$$
```

## §2 **符号锁定**（notation lock ✓ —— 此后一切文档以此为准 ✓）

```
$$b(x):=|C\cap B_1(x)|\ (\text{闭球},\ |B_1|=n+1\ ✓);\qquad \delta(x):=b(x)-1\ \ge0\ (\text{覆盖 ⟹ }b\ge1\ ✓)$$
$$A_i:=\#\{\text{无序码字对}\ \{c,c'\}:\ d(c,c')=i\}\quad(\text{距离分布 ✓});\qquad E:=(n+1)M-2^n\ ✓$$
$$\boxed{Q:=\sum_x\binom{\delta(x)}{2}}\quad(\textbf{excess quadratic overlap}\ ✓)\qquad \sum_x\binom{b(x)}{2}=2(A_1+A_2)\ \Longrightarrow\ \boxed{Q=2(A_1+A_2)-E}\ ✓$$
$$\textbf{警示（本档要点）}:\ \boxed{Q\ne A_2\ \text{一般不等}}\ ✗\ ——\ \text{实例}: n=6\ \text{类2},\ A_2=12\ \text{而}\ Q=4\ ✓$$
$$\text{另}: \sum_x\binom{b}{2}=\sum_x\big[\binom{\delta}{2}+\delta\big]=\ Q+E=2(A_1+A_2)\ ✓\ (\text{因 }d\le2\ \text{的码字对恰有 2 个共同闭球心}\ ✓)$$
```

## §3 ⭐ **类级数据（新）**：非等价类、不同距离分布、**同一不变量** ✓✓

```
$$\begin{array}{c|c|c|c|c|c|c|c}
\text{对象} & E & A_1 & A_2 & A_1+A_2 & Q & (A_1..A_6)\\
\hline
n=6\ \text{类1}\ ✓ & 20 & \mathbf{4} & 8 & 12 & \mathbf{4} & [4,\ 8,\ 26,\ 22,\ 6,\ 0]\\
n=6\ \text{类2}=1986\text{文献码}\ ✓ & 20 & \mathbf{0} & 12 & 12 & \mathbf{4} & [0,\ 12,\ 36,\ 12,\ 0,\ 6]\\
n=8\ \text{doubled Hamming}\ ✓ & 32 & 16 & 0 & 16 & \mathbf{0} & —\\
\end{array}$$
$$\Longrightarrow\ \textbf{两类距离分布不同（}A_1=4\ \text{vs}\ 0\ ✓\text{）⟹ 确为非等价类}\ ✓,\ \text{但 } A_1+A_2\ \text{与}\ Q\ \textbf{完全相同}\ ✓✓$$
$$\text{（与 n=4 的"2 个非等价类同值"}✓✓\ \text{同型 ⟹ 钉住非对称性产物、非分布指纹产物}\ ✓）$$
```

## §4 状态表（唐先生拟定版 ✓，含 A₁+A₂ 列）

```
$$\begin{array}{c|c|c|c|c|c}
n & K(n,1) & E & A_1+A_2 & Q & \text{强度}\\
\hline
4 & 4 & 4 & 2 & 0 & \textbf{穷举} 40（2 类同值 ✓✓）\\
5 & 7 & 10 & 6 & 2 & \textbf{穷举 320} ＋ 文献代表元 ＋ 文献分类 ✓✓✓\\
6 & 12 & 20 & 12 & 4 & \textbf{2 个类}（我方枚举）＋ 文献码对接 ✓✓\\
7 & 16 & 0 & 0 & 0 & \textbf{纯推理}（完美码唯一 ✓✓）\\
8 & 32 & 32 & 16 & 0 & 仅 \textbf{1 例}（doubled Hamming）✗ 未判\\
\end{array}$$
$$\text{OPEN}: \text{全部 }B_6\text{-类}\ ✗\ |\ \text{全部 }B_8\text{-类}\ ✗\ |\ \textbf{n=10, M=119: UNKNOWN}\ ✓$$
```

## §5 证伪判据（唐先生口径 ✓，已部分执行）

```
$$\text{若存在第二个 }B_6\text{-类且 }Q\ne4\ \Longrightarrow\ \textbf{n=6 钉住立即破}\ ✗\ (\text{无需推到 }n=8,10\ ✓)$$
$$\text{实测}: \text{第二类已找到}\ ✓,\ \text{其 }Q=\mathbf{4}\ ✓\ \Longrightarrow\ \textbf{钉住存活}\ ✓\ (\text{从"171 随机样本"升级为"2/2 已知类"}\ ✓)$$
$$\text{唯缺}: \text{类数恰为 2 的文献确认}\ ✗$$
```

## §6 边界（诚实标注）

- §1 为**零命中核验**（grep ✓，逐条 ✓）；**未**发现历史错误 ⟹ **不勘误** ✓
- §3 数据为**实算**（两类的 A_i、b 分布、Q ✓；doubled Hamming ✓）
- §5 的"类数恰 2"**未证** ✗
- **未**排除任何 n ✗；**未**对 n=10 外推 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 符号锁定     命中文件数=0    :: 
技术词 非等价类同值 命中文件数=1    :: ./PINNING-2026-09-26-step1-step2-audit-and-n6-n8-data.md 
技术词 距离分布指纹 命中文件数=0    :: 
技术词 零命中核验  命中文件数=0    ::
```

- **本档新增**（命中数=0）：符号锁定、距离分布指纹、零命中核验
- **档案已有（引用，不列为提出）**：非等价类同值
