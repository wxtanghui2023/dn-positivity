已查地图：已跑 scripts/prework_map_check.sh 119 preimage 两点 联合同余 ⟹ 执行自 `PREIMAGE-2026-09-26`（单点同余 ✓）＋ `MOD11-CHECK-2026-09-26`（mod 11 退化 ✓）；本档为 **PREIMAGE-2**（唐先生 2026-09-26 22:32 令 ✓）；含 LP 可行性计算 ✓。
D0: 本档对象 = 两点联合同余系统（既有对象）
D1: 0（产出为 CLOSED 判定：两点无杠杆）✗

# PREIMAGE2-2026-09-26 · 两点联合同余（CLOSED）

## §0 结论（先给）

```
$$\boxed{\textbf{PREIMAGE-2}:\ \text{两点联合同余（含\textbf{加强判据}）在 }t=1,\dots,10\ \text{与全部 }(f(x),f(y))\in\{0,1\}^2\ \text{下\textbf{均可行}}\ ✗\ \Longrightarrow\ \textbf{CLOSED（无杠杆）}}$$
$$\qquad\Longrightarrow\ \text{按唐先生预设 GO/NO-GO}:\ \text{"两点仍存在所有解"\ ⟹ CLOSED};\ \text{且与单点合并 ⟹ }\textbf{同余路线本身不足，应停止扩展}\ ✓$$
$$
$$
```

---

## §1 判据加强（本档关键 ✓）

```
$$\textbf{此前（弱化版）}:\ \text{只查同余}\ \sum_iK_iN_i(x)\equiv0\ (\mathrm{mod}\ D)\ ✗$$
$$\boxed{\textbf{本档（精确值版）}:\ Df(x)=\sum_iK_iN_i(x)\ \in\ \{0,\ D\}\ \text{（因 }f(x)\in\{0,1\}\ ✓\text{）}}$$
$$\qquad\text{两点}:\ \Big(\sum_iK_iN_i(x),\ \sum_iK_iN_i(y)\Big)\in\{0,D\}^2\quad(\text{联合，非两条独立同余}\ ✓)$$
$$
$$
```

---

## §2 计算（§LP 可行性，每 t 一个局部模型 ✓）

```
$$\text{变量}:\ m_{a,b}=\sum_{z:\ d(x,z)=a,\ d(y,z)=b}b(z)\ ✓;\ \text{盒}\ m_{a,b}\in[|C_{a,b}|,\ 3|C_{a,b}|]\ ✓\ (b\in\{1,2,3\}\ ✓)$$
$$\text{约束}:\ \sum m_{a,b}=1309\ ✓;\quad u:=\sum K_a m_{a,b}\in\{0,D\}\ ✓;\quad v:=\sum K_b m_{a,b}\in\{0,D\}\ ✓$$
$$\begin{array}{c|cccccccccc}
t & 1&2&3&4&5&6&7&8&9&10\\
\hline
\text{类数} & 20&27&32&35&36&35&32&27&20&11\\
\text{可行 }(f(x),f(y)) & \multicolumn{10}{c}{\text{全部 4 种}\ (0,0),(0,1),(1,0),(1,1)\ \text{皆可行}\ ✓}\\
\text{判定} & \multicolumn{10}{c}{\textbf{无杠杆}\ ✗}
\end{array}$$
$$
$$
```

---

## §3 结构性原因（为何 2 点必然无杠杆 ✓）

```
$$\text{自由变量}:\ \text{类数 }20\text{--}36\ ✓;\quad \text{约束数}:\ 3\ (\text{总和 ＋ 两个泛函})\ ✓$$
$$\qquad\Longrightarrow\ \text{自由度}\approx 17\text{--}33\ \gg 0\ \Longrightarrow\ \text{可行性\textbf{泛型成立}}\ ✗$$
$$\text{趋势}:\ \text{单点}\ (11\ \text{变量}, 1\ \text{泛函})\ \text{可行}\ ✗\ \to\ \text{两点}\ (20\text{--}36\ \text{变量}, 2\ \text{泛函})\ \text{可行}\ ✗\ \Longrightarrow\ k\ \text{点只会\textbf{更自由}}\ ⚠️$$
$$
$$
```

---

## §4 判定与状态锁定（按唐先生设定 ✓）

```
$$\boxed{119:\quad A_1\text{-route BLOCKED}}\ ✓$$
$$\boxed{\texttt{PREIMAGE-local-1-point}:\ BLOCKED}\ ✓\ (\text{mod 11 结构性退化 ✓；mod }9/5/7\ \text{局部可满足 ✓})$$
$$\boxed{\texttt{PREIMAGE-local-2-point}:\ \textbf{CLOSED}\ (\text{无杠杆})}\ ✓✓$$
$$\textbf{诊断}:\ \text{剩余难点\textbf{只在\textbf{跨 }x\ \text{的共同 }preimage\ \text{相容性}}（1024 点联合整数结构 ✓）——\ 即完整 }0/1\ \text{条件（＝原问题 ⚠️）}$$
$$\textbf{建议（依唐先生预设规则 ✓）}:\ \textbf{停止扩展局部同余路线}（不再做 3 点／4 点／新模数 ✗）；若继续 PREIMAGE，必须换到\textbf{非局部}机制 ⚠️$$
$$
$$
```

---

## §5 边界（诚实标注）

- §2 的可行组合为 **LP 显式可行性** ✓（每 t 每组合独立求解 ✓，非抽样 ✓）
- §3 的"k 点更自由"为**趋势判断** ✓，**非**定理 ✗（未排除某特殊 k 联合不可行 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张同余支无价值 ✗（只主张其局部形式（1 点／2 点）无杠杆 ✓）
- 本轮未跑 CP-SAT ✓（仅 10 个小 LP ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 两点联合同余 CLOSED 命中文件数=1    :: ./PREIMAGE2-2026-09-26-two-point-joint-congruence-closed.md 
技术词 精确值判据  命中文件数=1    :: ./PREIMAGE2-2026-09-26-two-point-joint-congruence-closed.md
```
- **本档新增**：两点联合同余 CLOSED、精确值判据（{0,D} 版）（见上方命中数；0 命中者为自造语 ✓）
- **档案已有（引用，不列为提出）**：单点同余、mod 11 退化、$D=3465$、四门链
