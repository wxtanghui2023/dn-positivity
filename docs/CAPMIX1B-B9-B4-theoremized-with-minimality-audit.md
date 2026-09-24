已查地图：命中（`CAPMIX1B-B8-blind-class-is-subfield-class`）⟹ 执行其 §6 之 (A)，不开新案
D0: 本档对象 = **`B9`：B4 定理化**：**T1 定理**（已机器核验 `7/7` 零违例）＋ **T2 条件用法定位** ＋ **T3 最小性审计**（两条件皆必要；并抓到 **B4 原表述的错误**）
D1: 1 （新自由度：定理化 ＋ 条件修正（`\mathrm{ord}_d(2)` 偶 ⟹ **`-1\in\langle2\rangle_d`**））
[RESEARCH]

# **`CAP-MIX-1B · B9`：B4 定理化（含最小性审计）**

## §1 T1 — 定理（机器核验通过）

```
$$\boxed{\textbf{定理（充分判据）}:\quad \Big(\exists k\ge1:\ 2^{\,k}\equiv-1\ (\mathrm{mod}\ d)\Big)\ \wedge\ (3\nmid d)\ \Longrightarrow\ \lambda(G_{q,d})=0}$$ ✓✓✓
$$\text{其中}\ q=2^n,\ d\mid q-1,\ G_{q,d}\le\mathbb F_{2^n}^\times;\qquad \lambda(G)=\#\{x\in G:\ 1+x\in G\}$$ ✓
**【核验网格】** `n=2,\dots,13`（`q\le8192`），**全部** `d\mid 2^n-1,\ d\ge3` ⟹ `cases=56` ✓
$$\textbf{STATS}:\quad \texttt{hyp}=7,\qquad \boxed{\texttt{hyp\_lam0}=7},\qquad \boxed{\texttt{hyp\_viol}=0}$$ ✓✓✓
$$\text{即：满足假设者\textbf{全部} }\lambda=0,\ \textbf{零反例}$$ ✓✓
```

## §2 T2 — 条件在证明中的**使用位置**（逐步到底）

```
$$\textbf{设}\ x\in G,\ 1+x\in G,\ \text{且}\ d\mid2^k+1.$$
$$\textbf{步骤 1（用条件①）}:\quad 2^k\equiv-1\ (\mathrm{mod}\ d)\ \Longrightarrow\ x^{2^k}=x^{-1},\qquad (1+x)^{2^k}=(1+x)^{-1}$$ ✓
$$\textbf{步骤 2（Frobenius）}:\quad (1+x)^{2^k}=1+x^{2^k}=1+x^{-1}$$ ✓（char 2）
$$\textbf{步骤 3（合并）}:\quad 1+x^{-1}=(1+x)^{-1}\ \Longrightarrow\ (1+x)(1+x^{-1})=1\ \Longrightarrow\ \frac{(1+x)^2}{x}=1\ \Longrightarrow\ 1+x^2=x$$ ✓
$$\textbf{步骤 4}:\quad \boxed{x^2+x+1=0}\ \Longrightarrow\ x^3=1\ \text{且}\ x\ne1\ \Longrightarrow\ \mathrm{ord}(x)=3$$ ✓
$$\textbf{步骤 5（用条件②）}:\quad x\in G\Rightarrow\mathrm{ord}(x)\mid d\ \Longrightarrow\ 3\mid d\ \ \text{与}\ 3\nmid d\ \textbf{矛盾}$$ ✓✓
$$\Longrightarrow\ \text{不存在 } x\in G\ \text{使 }1+x\in G\ \Longrightarrow\ \lambda=0$$ ✓✓
$$\boxed{\text{条件①用于\textbf{实现 inversion ＋ 供 Frobenius 使用};\quad 条件②\textbf{恰好用于排除 }x^2+x+1=0}$$ ✓✓（**与您 §三刀 的期待一致**）✓
```

## §3 ⛔⭐ T3 审计发现：B4 原表述**错了**（`\mathrm{ord}_d(2)` 偶 ≠ 充分）

```
$$\text{原表述（B4 档）：条件①}\ 2^{\,k}\equiv-1\ \text{改写为}\ \mathrm{ord}_d(2)\ \textbf{偶}\ \text{\textbf{不成立}}$$ ✗
$$\textbf{反例（机器实测，5 例）}:\quad (8,256,85),\ (10,1024,341),\ (12,4096,35),\ (12,4096,91),\ (12,4096,455)$$ ✓✓
$$\qquad \text{均满足 }\mathrm{ord}_d(2)\ \text{偶}\ \wedge\ 3\nmid d,\ \text{但}\ \lambda>0$$ ✓✓
$$\textbf{原因}:\quad \text{“}\mathrm{ord}\ \text{偶}\iff-1\in\langle2\rangle\text{”\textbf{仅当单位群循环}（如 }d\ \text{素）};$$ ✓
$$\qquad d=35:\ \mathrm{ord}=12\ \text{偶，而}\ 2^6=64\equiv29\ne34=-1\ ((\mathbb Z/35)^*\ \text{有\ 3\ 个二阶元})$$ ✓✓
$$\Longrightarrow\ \boxed{\text{正确条件必须写\textbf{存在 }k:\ 2^k\equiv-1\ (\mathrm{mod}\ d)},\ \text{即 }-1\in\langle2\rangle_d}$$ ✓✓✓（**本档修正**）
$$\text{换用正确条件后重跑：}\texttt{hyp}=7,\ \texttt{hyp\_lam0}=7,\ \texttt{hyp\_viol}=0$$ ✓✓✓
```

## §4 T3 — 最小性审计（两条件**皆必要**）

```
$$\textbf{去掉条件②（允许 }3\mid d\text{）}:\quad \texttt{cond2\_only\_drop\_viol}=9\ \text{反例}$$ ✓✓
$$\qquad d=3:\ \text{6 例全部 }\lambda=2>0\ (\text{因 }1+\omega=\omega^2\in G)\ \Longrightarrow\ 3\nmid d\ \textbf{不可去}$$ ✓
$$\textbf{去掉条件①（允许 }-1\notin\langle2\rangle_d\text{）}:\quad \texttt{cond1\_only\_drop\_viol}=16\ \text{反例}$$ ✓✓
$$\qquad \text{如 }d=7\ (\mathrm{ord}_7(2)=3):\ \lambda=6>0\ \Longrightarrow\ \text{条件①\textbf{不可去}}$$ ✓
$$\Longrightarrow\ \boxed{\text{两条件\textbf{皆必要}；判据在同尺度上\textbf{不冗余}}}$$ ✓✓
```

## §5 边界清单（照您第五刀）

```
$$\begin{array}{c|c}
\text{边界项}&\text{实测}\\
\hline
d=1&不列（子群平凡，无意义）\\
d=3&\text{属条件②的排除侧};\ \lambda=2>0\ (\text{6 例})=>\ 3\nmid d\ \text{必要}\\
3\mid d&9\ \text{例违例（去②后）}=>\ 必要\\
d\mid2^n-1\ \text{但无所需 }k&\text{47 例 }\lambda>0\ \text{中占多数};(\ref{23,89})\ \text{另有 }\lambda=0\ \text{2 例（定理不覆盖）}\\
d=2^k+1\ \text{典型值}&d=5,17,65\ \text{皆 }\lambda=0\ (\text{条件①满足},\ k\ \text{偶});\ d=9,33\ (k\ \text{奇})\ \text{则 }3\mid d\ \text{被②排除}\\
k\ \text{非最小}&2^k\equiv-1\ \text{对任意}\ k\equiv k_0\ (\mathrm{mod}\ \mathrm{ord}_d(2))\ \text{皆可用}\ \Longrightarrow\ \text{定理\textbf{不依赖最小 }k}\\
k\equiv0\ (\mathrm{mod}\ n)&2^k\equiv1\ (\mathrm{mod}\ d)\ne-1\ (d>2)\ \Longrightarrow\ \text{不满足假设（无害）}\\
d=q-1\ (\text{全群})&\mathrm{ord}=n;\ 3\mid2^n-1\iff n\ \text{偶}\ \Longrightarrow\ \textbf{假设永不被 }d=q-1\ \text{满足}\ (\text{与 }\lambda=q-2>0\ \text{不冲突})\\
\end{array}$$ ✓✓
```

## §6 结论与状态

```
$$\boxed{\text{T1 定理成立（充分，机器核验 }7/7\text{ 零违例）};\quad \text{T2 两条件用法已定位};\quad \text{T3 两条件皆必要}}$$ ✓✓✓
$$\boxed{\text{最终形态}:\quad \text{Frobenius–inversion 条件}\ (2^k\equiv-1)+\text{无 }\mu_3\ (3\nmid d)\ \Longrightarrow\ \lambda=0}$$ ✓✓
$$\boxed{\text{严格标为\textbf{充分判据}}（不代表等价）;\quad (23,89)\ \text{保持为未解释零点，}\textbf{不污染}该定理}$$ ✓✓
$$\text{存活资产}: \text{B9 定理化+B4 充分判据};\ \text{未解释}:\ (23,89);\ \lambda=0\ \text{但 }\mathrm{ord}\ \text{奇（2 例）}$$ ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**不回 RH** ✓
【数据】 `out/capmix1B9b_theorem.txt`（56 行网格）；脚本 `scripts/capmix1B9_theorem_audit.py`（已修正条件）✓
【边界】 §1/§3/§4 为**机器实测**；§2 为**逐步推导**（每步已与实测一致）✓

## §附 【技术词回查】（补录）
```
技术词 sufficient criterion 命中文件数=0    :: 
技术词 minimality       命中文件数=6    :: ./ZF-G5G6-PL-gate-and-reverse-scan.md ./ID-CLAIMS.tsv ./V166-C66-global-identification-ominimality-obstruction-terminal-A-conditional.md 
```
