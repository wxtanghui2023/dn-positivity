已查地图：已跑 scripts/prework_map_check.sh P1 support 层 separation non-reducibility ⟹ 执行自 `CLOSURE-2026-09-27-Q0-STOP-and-the-separation-pair`（✓）＋ 唐先生 12:28/12:30（开 P1 ＋ 问结果 ✓）；本档 = **P1 support 层筛选结果（两 Gate 分级 ✓）**。
D0: 本档对象 = support 层候选量在 separation pair 上的两 Gate 判定
D1: 1（新增：**support 恒等式 Σm²=Σ_{c,c'}C(|S∩S'|,2) ✓（核实 ✓）**；**P1 候选总表 ✓**；**P1-2 未建立的诊断 ✓**）

# P1 support 层筛选结果（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BA-1 Gate P1-1 separation: 全过 ✓)}\ \text{全部 8 个候选量在两码上均不同}\ ✓\ \text{（见 §2 表 ✓）}}$$
$$\boxed{\textbf{(BA-2 Gate P1-2 non-reducibility: 未建立 ⚠️)}\ \text{两码 }(A_1,A_2)=(7,66)\ \text{vs}\ (26,47)\ \textbf{本就不同} \Longrightarrow \text{「区分两码」≠「新信息」} ✗✓}$$
$$\qquad\Longrightarrow\ \text{判据必须升级为}:\ \exists C_i,C_j\ \text{with}\ (A_1,A_2)_i=(A_1,A_2)_j\ \text{but}\ J(C_i)\ne J(C_j)\ ✓\ \text{（唐先生 12:28 ✓）}$$
$$\boxed{\textbf{(BA-3 净资产 ✓)}\ \text{支持层恒等式（核实 ✓）}:\ \sum_{i<j}m_{ij}^2=\sum_{c,c'}\binom{|S(c)\cap S(c')|}2\ \text{（含对角 }c=c'\ ✓\text{）}}$$
$$\qquad\text{对角项}= \sum_c\binom{|S(c)|}2=J_1\ ✓;\ \text{非对角项给出**坐标方向共现**的成对结构 ✓}$$
$$
$$
```

---

## §1 定义与恒等式（**✓ 核实**）

```
$$S(c)=\{i\in[n]:\ c\oplus e_i\in C\}\ ✓;\quad d_1(c)=|S(c)|\ ✓;\quad m_{ij}=|\{c:i,j\in S(c)\}|\ ✓;\quad q_{ij}=\big|\{\{c,c\oplus e_i\oplus e_j\}\subseteq C\}\big|\ ✓$$
$$\sum_{i<j}m_{ij}=\sum_c\binom{d_1(c)}2=J_1\ ✓;\qquad \sum_{i<j}q_{ij}=A_2\ ✓$$
$$\textbf{恒等式（本机核实 ✓✓）}:\ \sum_{i<j}m_{ij}^2=\sum_{i<j}\Big(\sum_c\mathbf1[i,j\subseteq S(c)]\Big)^2=\sum_{c,c'}\binom{|S(c)\cap S(c')|}2\ ✓$$
$$\qquad\text{码#0}: 6=6\ ✓;\qquad \text{码#1}: 117=117\ ✓\ \text{（两版计算一致 ✓）}$$
$$\qquad\textbf{读数}:\ S(c)\cap S(c')\ \text{数的是\textbf{坐标方向}（非公共邻居／中点 ✓）—— 此前我一度误称"中点个数" ✗，已更正 ✓}$$
$$
$$
```

---

## §2 P1 候选总表（**Gate P1-1 全过 ✓**）

```
$$\begin{array}{c|c|c|c}
\text{量} & \text{码#0} & \text{码#1} & \text{分离}\\
\hline
A_1 & 7 & 26 & ✓\\
A_2 & 66 & 47 & ✓\\
J_1=\sum_c\binom{d_1(c)}2 & 6 & 27 & ✓\\
J_2=\sum_c d_1(c)^2 & 26 & 106 & ✓\\
J_3=\sum_{i<j}m_{ij}^2 & 6 & 117 & ✓\\
J_4=\max_{i<j}m_{ij} & 1 & 6 & ✓\\
J_5=\#\{(i,j):m_{ij}>0\} & 6 & 12 & ✓\\
J_6=\sum_{i<j}m_{ij}q_{ij} & 20 & 135 & ✓\\
J_7=\sum_{i<j}(m_{ij}-q_{ij})^2 & 292 & 36 & ✓\\
\sum_i a_i^2 & 13 & 150 & ✓\\
\end{array}$$
$$\Longrightarrow\ \textbf{Gate P1-1 全面通过} ✓\ \text{——但见 §3 警告 ⚠️}$$
$$
$$
```

---

## §3 Gate P1-2 的诊断（**关键 ⚠️**）

```
$$\text{问题}:\ \text{两 witness 的 }(A_1,A_2)\ \text{本就不同}\ \Longrightarrow\ \textbf{任何依赖 }A_1\ \text{或 }A_2\ \text{的量都会"区分"} ✗\ \text{⟹ 该 Gate 不足以证明新信息 ✓}$$
$$\text{已尝试的对照实验（本机 ✓）}:\ n=5,M=7\ \text{的全部 320 个极小覆盖码}:\ \textbf{同属一个 }(A_1,A_2)=(2,4)\ \text{类}\ ✓$$
$$\qquad\text{且 }J_2,J_3,\sum a_i^2,d_1\ \text{直方},J_1\ \text{全部唯一} ⚠️\ \text{—— 但该 320 码极可能\textbf{单一同构类} ⟹ 非决定性 ✗}$$
$$\Longrightarrow\ \text{当前数据\textbf{不能判定} support 层是否塌缩到 }(A_1,A_2)\ ⚠️\ \text{（需固定 }(A_1,A_2)\ \text{的更大码族 ✓）}$$
$$
$$
```

---

## §4 下一步（**决定性实验设计 ✓**）

```
$$\textbf{要做的}:\ \text{扩充 }C_{62}\ \text{类的\textbf{同 }(A_1,A_2)\ \text{码族}};\ \text{或改用中等 }n\ \text{的覆盖码族（同 }(A_1,A_2)\ \text{分组 ✓）}$$
$$\qquad\text{若组内 }J\ \text{变化} ⟹ \textbf{P1 candidate（新信息 ✓✓）};\ \text{若全钉住} ⟹ \textbf{support-2 层封顶} ⟹ \text{转 2-face/triple ✓（唐先生 12:28 ✓）}$$
$$\textbf{已知可用工具} ✓:\ \text{n=5 穷举（320 码，单类）；n=6 可穷举 }\binom{64}{12}\ ✗\ \text{过大} \Longrightarrow \text{用随机＋结构生成覆盖码族 ✓；或直接用档案的 }n=9\ \text{分类（若含更多码 ✓）}$$
$$\text{暂不碰（遵唐先生 ✓）}:\ n=10,M=119\ \text{的 SAT／大模型 ✗}$$
$$
$$
```

---

## §5 边界与更正（诚实标注）

- ⚠️ **本档更正**：先前 `ident.py` 输出的 45 vs 117 分歧 = **我脚本中 $m$ 计法不一致**（去对角／半计 ✗），已修正为 117 ✓；恒等式**成立** ✓
- ⚠️ 先前称「$d(c,c')=2\Rightarrow|S\cap S'|\le2$（中点个数）」**为误** ✗ —— $S\cap S'$ 计**坐标方向** ✓
- **未**声称任何 P1 量已具新信息 ✗（P1-2 未建立 ⚠️）；**未**改动 119 UNKNOWN ✓；**未**跑未授权的 $n=10$ 计算 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：P1 候选总表、支持层恒等式核实、Gate P1-2 诊断
- **档案已有（引用，不列为提出）**：separation pair、$A_1,A_2$、$d_1$、球交叠塌缩、Q0 STOP


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 P1 候选总表  命中文件数=1    :: ./P1-2026-09-27-support-layer-screen-results.md 
技术词 支持层恒等式 命中文件数=1    :: ./P1-2026-09-27-support-layer-screen-results.md
```
- **本档新增**：P1 候选总表、支持层恒等式核实、Gate P1-2 诊断（见上方命中数；0 命中者为自造语／内部标签 ✓）
