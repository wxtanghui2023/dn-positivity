已查地图：已跑 scripts/prework_map_check.sh P1-2 桶 分叉 Theorem13 TypeB ⟹ 执行自 `CHAIN-VW-2026-09-27-...`（✓）＋ 唐先生 13:15（补跑 e≠0 完整构造域 ✓）；本档 = **P1-2 PASS（同桶 J 分叉，双算法 ✓✓）＋ 机制透明化** ✓✓。
D0: 本档对象 = Theorem-13 构造域内的同桶 J 分叉
D1: 3（**P1-2 PASS ✓✓**；**三见证码（距离分布亦相同）✓**；**机制透明化 ✓**）

# P1-2 PASS：同 (A₁,A₂) 而 J 分叉（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BM-1 ⭐P1-2 PASS ✓✓)}\ \text{存在三个\textbf{两两不等价}的最优 }(8,32)_1\ \text{覆盖码},\ (A_1,A_2)=\mathbf{(0,16)}\ \text{相同},\ \textbf{全距离分布亦相同},\ \text{但}\ J_7\ \text{分别为}\ \mathbf{64,\,128,\,256}\ ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{(A}_1,\textbf{A}_2)\ \text{不决定 support-2 fingerprint}}\ \Longrightarrow\ \text{"collapse 假设"}\ \textbf{被否证} ✗\ \text{(在 }n=8\ \text{的 Theorem-13 域内 ✓)}$$
$$\boxed{\textbf{(BM-2 机制透明 ✓)}\ \text{分叉的载体 = Type B（}k=0\text{，两半为\textbf{不交}完美码 ✓）};\ \text{其 distance-2 对必为跨半对}\ (c,0),(c+e_i,1)\ \Longrightarrow\ \textbf{全部 }q_{ij}\ \text{仅落在 }\{i,7\}\ \text{型坐标对上} ✓}$$
$$\qquad\Longrightarrow\ J_7=\sum_{i=0}^{6}q_{i7}^2\ \text{（}16\ \text{的一个分拆的平方和 ✓）}\ \Longrightarrow\ 64=4^2\cdot4\ ✓,\ 128=8^2\cdot2\ ✓,\ 256=16^2\ ✓\ \text{——\textbf{分叉完全被解释} ✓✓}$$
$$\boxed{\textbf{(BM-3 更锐 ✓)}\ \text{三见证码\textbf{连全距离分布都相同}}:\ A=(0,16,160,176,64,48,32,0)\ ✓\ \Longrightarrow\ \text{分离\textbf{只在坐标支撑层}} ✓✓\ \text{（正是全场要找的"新可区分维度" ✓）}$$
$$
$$
```

---

## §1 构造域与去重（**✓ 两个精确降维**）

```
$$\text{Theorem 13（论文 ✓）}:\ C_1,C_2\ \text{为长 }2^r-1\ \text{的完美码} \Longrightarrow C=\{(c_1,0)\}\cup\{(c_2,1)\}\ \text{是 NP1CC};\ \text{Corollary 14}:\ \text{Type A/B/C 由 }C_1\cap C_2\ \text{定} ✓$$
$$\text{原始表示}: (\pi,e)\in S_7\times\mathbb F_2^7\ \Longrightarrow\ 5040\times128=645120\ \text{（唐先生 ✓）}$$
$$\text{降维 ①}:\ \pi\ \text{只通过 }\pi H\ \text{起作用} \Longrightarrow\ \text{互异子空间仅 }30=5040/|Aut(H)|=5040/168\ ✓;\quad \text{降维 ②}:\ \text{码级去重} \Longrightarrow 240\ \text{互异码} ✓✓$$
$$\qquad\text{（两处均为\textbf{表示级去重}，非等价类商 ✓；且 }e\ \text{的 128 个值全部枚举，未提前商 ✓，遵唐先生 13:15 纪律 ✓）}$$
$$
$$
```

---

## §2 桶表（**Gate 1 ＋ Gate 2 ✓**）

```
$$\begin{array}{c|c|c|c|c}
\text{桶}\ (A_1,A_2) & \text{码数} & k=|H\cap(\pi H+e)| & \#\text{不同 }J=({\Sigma a^2},J_7) & \text{判据}\\
\hline
(0,16) & 105 & \{0\} & \mathbf 3 & \textbf{分叉 ✓✓}\\
(2,14) & 64 & \{2\} & 1 & 全同\\
(4,12) & 56 & \{4\} & 1 & 全同\\
(8,8) & 14 & \{8\} & 1 & 全同\\
(16,0) & 1 & \{16\} & 1 & 全同\\
\end{array}$$
$$\textbf{结构事实 ✓}:\ \boxed{A_1=k}\ \text{（每个共享字 }h\in C_1\cap C_2\ \text{给出距离 1 对 }(h,0),(h,1)\ ✓\text{，且无其它距离 1 对 ✓）};\quad A_2=16-A_1\ ✓\ \text{（}A_1{+}A_2=M/2\ ✓\text{）}$$
$$\textbf{分叉仅在 }k=0\ \text{（Type B ✓）};\ k>0\ \text{时 }J\ \text{唯一 ✓（}(2,14)\to(4,28),\ (4,12)\to(16,48),\ (8,8)\to(64,64),\ (16,0)\to(256,0)\ ✓\text{）}$$
$$
$$
```

---

## §3 三见证码（**✓ 双算法 ＋ 全距离分布 ✓**）

```
$$\begin{array}{c|c|c|c|c}
J_7 & |C| & \text{全距离分布}\ A_1..A_8 & a & q\ \text{支撑}\\
\hline
\mathbf{64} & 32 & (0,16,160,176,64,48,32,0) & (0,\ldots,0) & 4\ \text{对}:\ (0,7),(6,7),(2,7),(4,7)\ \text{各 }4\\
\mathbf{128} & 32 & (0,16,160,176,64,48,32,0) & (0,\ldots,0) & 2\ \text{对}:\ (0,7),(4,7)\ \text{各 }8\\
\mathbf{256} & 32 & (0,16,160,176,64,48,32,0) & (0,\ldots,0) & 1\ \text{对}:\ (0,7)\ \text{为 }16\\
\end{array}$$
$$\textbf{复核 ✓✓}:\ \text{第二算法（按坐标差集直接枚举 pair）给出同值}\ \{64{:}64,128{:}128,256{:}256\}\ ✓;\ \text{三者 }A_1=0,\ A_2=16,\ \text{覆盖性已验}\ ✓$$
$$\qquad\Longrightarrow\ \textbf{它们必两两不等价} ✓\ \text{（Hamming 等距变换保持 }J ✓\text{，而 }J\ \text{不同 ✗）};\ \text{见证已存 }work/k10/c62/np1cc/witness\_0\_16.txt\ ✓$$
$$
$$
```

---

## §4 机制（**为什么 J 能分叉 ✓**）

```
$$\text{Type B}:\ C_1\cap C_2=\varnothing\ \Longrightarrow\ A_1=0\ ✓;\ \text{所有距离 2 对都是\textbf{跨半对}}\ (h,0)\leftrightarrow(h+e_i,1)\ \text{（}h\in H\ ✓\text{，因两半不交 ⟹ 末位必异 ✓）}$$
$$\qquad\Longrightarrow\ \text{方向差集}=\{i,7\}\ \Longrightarrow\ \text{所有 }q\ \text{落在 }(i,7)\ \text{型坐标对 ✓}\ \Longrightarrow\ J_7=\sum_{i=0}^6q_{i7}^2\ ✓$$
$$\qquad\text{而}\ \sum_iq_{i7}=A_2=16\ \Longrightarrow\ J_7=\text{"16 沿 7 个方向的\textbf{集中度}"}\ ✓\ \text{⟹ 自由度 = }C_2\ \text{相对 }C_1\ \text{的\textbf{对齐方式} ✓✓}$$
$$\qquad\Longrightarrow\ \text{三个值 }64/128/256\ \text{分别对应分拆 }4{+}4{+}4{+}4\ /\ 8{+}8\ /\ 16\ ✓\ \text{——\textbf{机制完全透明} ✓✓}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§3 为本机精确计算（240 互异码全覆盖 ✓，双算法复核 ✓）；§4 为**机制解释** ✓（推导 ＋ 数值一致 ✓）
- ⚠️ **结论范围**：**限 }n=8\ \text{的 Theorem-13 族}** ✓（240 码 ✓）；**未**声称一般 $n=2^m$ 或所有 10 类最优码 ✗；**未**涉及 $n=10/119$ 判定 ✓
- ⚠️ 本档**否证**"$(A_1,A_2)$ 决定 support-2"的 collapse 假设 ✗（此前 YIP 档的谨慎结论得到**正面答案** ✓）
- **注意**：这是 P1-2 的**正结果（PASS）** ✓，即 support 层确有独立可观测性 ✓，不是 119 的进展 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：P1-2 PASS（同桶分叉）、k=A₁ 结构事实、Type B 机制透明化、240 互异码精确域
- **档案已有（引用，不列为提出）**：Theorem 13、Corollary 14、Type A/B/C、$A_1+A_2=M/2$、$J_7$、$q_{ij}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 P1-2 PASS        命中文件数=5    :: ./P12-PASS-2026-09-27-bucket-divergence-with-identical-distance-distribution.md ./YI-2026-09-27-classification-pool-bucket-analysis.md ./FINAL-2026-09-27-K8-1-verdict-and-ledger-update.md 
技术词 Type B 机制透明化 命中文件数=1    :: ./P12-PASS-2026-09-27-bucket-divergence-with-identical-distance-distribution.md
```
- **本档新增**：P1-2 PASS（同桶分叉）、$k=A_1$ 结构事实、Type B 机制透明化、240 互异码精确域（见上方命中数；0 命中者为自造语／内部标签 ✓）
