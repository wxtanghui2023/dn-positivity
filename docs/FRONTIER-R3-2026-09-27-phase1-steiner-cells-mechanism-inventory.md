已查地图：已跑 scripts/prework_map_check.sh Steiner 3-designs 机制清单 rank LP derived ⟹ 执行自 `FRONTIER-R1-CHECK-2026-09-26`（五格核查 ✓）＋ 唐先生 2026-09-27 09:44 ✓；本档为 **第一阶段：原文核验 → fingerprint → 机制清单 → P1 筛选**（**未动算** ✓）。
D0: 本档对象 = 三 Steiner cell（41/46/50）＋ CSQS(94) ＋ RoSQS 五格的机制账目
D1: 1（新增：**机制占用表（USED vs 未用）** ✓；**一个 P1 候选（p-rank 扩张障碍）** ✓）

# FRONTIER-R3-phase1-2026-09-27 · Steiner cell 机制清单

## §0 判定（先给）

```
$$\boxed{\textbf{(GG-1 原文核验)}\ \text{KKW 论文（arXiv:2509.23483）中 }\\texttt{rank}\ \text{出现}\ \mathbf 0\ \text{次};\ \\texttt{linear programming}\ \mathbf 0\ \text{次};\ \text{反证了"rank／LP 已用于此 cell"}\ ✓✓}$$
$$\boxed{\textbf{(GG-2 机制占用)}\ \text{USED}:\ \text{导数设计＋指定扩张群＋Kramer--Mesner＋paramodification＋群穷举}\ ✓;\ \textbf{未用}:\ \text{p-rank／Smith 形／域依赖约束／LP}\ ✓$$
$$\boxed{\textbf{(GG-3 P1 候选)}\ \textbf{一个}:\ \text{导数设计的 p-rank 作为\textbf{扩张障碍}}\ ✓\ \text{（标准机制但\textbf{未用于此 cell} ✓）；其余族 DROP}\ ✗$$
$$
$$
```

---

## §1 (GG-1) 原文核验（KKW 论文逐处 ✓）

```
$$\text{方法关键词频次（s3.txt 实测 ✓）}:\ \text{Kramer 9／Mesner 9／extension 92／automorphism 28／group 96／derived 17／paramodif 2／prescrib 40};\ \mathbf{rank\ 0};\ \mathbf{linear\ programming\ 0}\ ✓$$
$$\text{核心方法（原文）}:\ \text{"extending Steiner 2-designs using \textbf{prescribed extension groups}"}＋\text{Kramer--Mesner}＋\text{paramodification}\ ✓$$
$$\text{逐 cell 原文（关键句 ✓）}:$$
$$\qquad S(3,6,46):\ \text{"with ... extension groups of orders }|G|>10,\ \text{and even with most groups of orders 8 and 10 ... but we didn't get any }S(3,6,46)\ \text{designs. \textbf{The search would take too long for smaller extension groups}}"}\ ✓\ \Longrightarrow\ \textbf{群法已饱和}\ ✗$$
$$\qquad S(3,5,41):\ \text{"Derived designs ... }S(2,4,40).\ \text{The \textbf{classical example is PG(3,3)}; we managed to construct many more examples by prescribing various groups ... Kramer--Mesner"}\ ✓$$
$$\qquad S(3,5,50),\ CSQS(94):\ \text{"No such design could be found"}\ ✓;\ \text{CSQS}:\ \text{"not able to construct ... nor to rule it out"}\ ✓;\ \text{RoSQS}:\ \text{46／92 已构造} ⟹ 5\ \text{格存留}\ ✓$$
$$
$$
```

---

## §2 (GG-2) 对象 fingerprint（本档计算 ✓）

```
$$\begin{array}{c|c|c|c|c|c}
\text{cell} & v & b & r & \lambda_2 & \text{导数设计}\\
\hline
S(3,5,41) & 41 & 1066 & 130 & 13 & S(2,4,40)\ (b'=130)\\
S(3,6,46) & 46 & 759 & 99 & 11 & S(2,5,45)\ (b'=99)\\
S(3,5,50) & 50 & 1960 & 196 & 16 & S(2,4,49)\ (b'=196)\\
\hline
CSQS(94) & 94 & 33511 & — & — & \text{循环 }\mathbb Z_{94}\ \text{作用}\ ✓\\
RoSQS(56\dots98) & — & — & — & — & \mathbb Z_{v-1}\ \text{旋转群＋不动点}\ ✓\ (\text{基块}\approx153\dots440\ ✓)
\end{array}$$
$$
$$
```

---

## §3 (GG-2) 机制占用表（唐先生四列格式 ✓）

```
$$\begin{array}{c|l|l|l}
\text{对象} & \text{OPEN 命题} & \textbf{USED} & \text{未用／可组合}\\
\hline
S(3,5,41) & \text{存在 }3\text{-}(41,5,1) & \text{导数设计＋指定扩张群＋KM＋paramodification}\ ✓ & \mathbf{p\text{-}rank／Smith 形／域依赖}\ ✓;\ \text{LP／}\tau\text{-design 界}\ ✓\\
S(3,6,46) & \text{存在 }3\text{-}(46,6,1) & \text{同上 ＋ 群穷举（}|G|>10\ \text{及多数 }8,10\ ✓\ \text{已饱和}\ ✗） & \text{同上；＋ 65＋1000 个已知 }S(2,5,45)\ \text{的 rank 数据}\ ✓\\
S(3,5,50) & \text{存在 }3\text{-}(50,5,1) & \text{同上}\ ✓ & \text{同上}\ ✓\\
CSQS(94) & \text{存在循环 }SQS(94) & \text{扩张法（失败}\ ✗\text{）＋文献 }\texttt{[15,Thm 4.6]}\ ✓ & \text{循环轨道／差族约束（}\textbf{差族已用}\ ⚠️\text{）};\ \text{p}\text{-}rank\ \text{型轨道障碍}\ ✓\\
RoSQS\ 5\ \text{格} & \text{构造（存在性）} & \text{乘积构造（Ji--Zhu）＋指定群}\ ✓ & \textbf{无 P1 形态}\ ✗\ \text{（下界障碍缺位 ⟹ 按 gate}\ \textbf{不启动}\ ✗）
\end{array}$$
$$
$$
```

---

## §4 (GG-3) P1 筛选（本档核心 ✓）

```
$$\textbf{唯一存活候选}:\ \boxed{\text{导数设计的 }p\text{-rank}\ \text{作为\textbf{扩张障碍}}}\ ✓$$
$$\qquad\textbf{P1 形态（唐先生格式 ✓）}:\ \text{假设 }S(3,5,41)\ \text{存在}\ \Longrightarrow\ \text{其导数 }S(2,4,40)\ \text{必须\textbf{可扩张}}\ \Longrightarrow\ \Phi_{\rm rank}(\text{incidence})\ge L\ \Longrightarrow\ \text{与已知矛盾／缺口}\ ✓$$
$$\qquad\textbf{机制占用（文献核查 ✓）}:\ \text{p-rank 机制\textbf{标准}（Doyen--Hubaut--Vandensavel 1978: STS 的 GF(2)-rank 下界\ ✓;\ Hamada 型：几何设计\ ✓;\ 且 DHV 明言"study \textbf{extensions}"}\ ✓\text{）}$$
$$\qquad\qquad\Longrightarrow\ \text{但检索\textbf{未见}其用于 }S(3,5,41)\ /\ S(3,6,46)\ /\ S(3,5,50)\ ✓\ \Longrightarrow\ \text{属}\textbf{"标准机制、未用于此 cell"}\ ✓\ \text{（按唐先生规则：不自动算新，但\textbf{可作组合候选}}\ ✓\text{）}$$
$$\textbf{其余判定}:\ \text{LP／}\tau\text{-design 界：文献成熟（Delsarte 型）}\ ⚠️\ \text{且对\textbf{存在性}非天然工具}\ ✗;\ \text{CSQS 差族：已用}\ ⚠️;\ \text{RoSQS：无 P1 形态}\ ✗\ \text{（gate 不通过 ⟹ }\textbf{不启动 SAT}\ ✗\text{）}$$
$$
$$
```

---

## §5 下一步（第一阶段收束 ✓）

```
$$\textbf{唯一可进入第二阶段的 cell}:\ S(3,5,41)\ \text{（及同法 }46／50\ ✓\text{）};\ \text{载体}:\ \text{导数设计的 }p\text{-rank}\ \text{扩张障碍}\ ✓$$
$$\textbf{第二阶段（须先做，仍不动算 ✓）}:\ \text{① 读 DHV 1978 与 Hamada 型原文，确认 }p\text{-rank--扩张 的\textbf{精确关系式}}\ ⚠️;\ \text{② 写出\textbf{可检验的 }P1\ \text{不等式}}\ ✓;\ \text{③ 若得到 P1 ⟹ 才进入计算/构造}\ ✓$$
$$\textbf{禁止}:\ \text{未过 gate 就开 SAT}\ ✗;\ \text{把 KU／群法重新包装成新机制}\ ✗$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1 为**原文引用** ✓（`s3.txt` 关键词频次与逐句 ✓，不列为新提出 ✓）
- §2 为**参数计算** ✓（纯组合 ✓）；§3–§4 为**账目与筛选** ✓
- §4 的候选为**"标准机制、未用于此 cell"** ✓ —— **不主张**它必能给出 P1 ✗（需 §5 的原文关系式 ✓）
- RoSQS 五格**未死亡** ✓（仅不通过本 gate ✓；作为构造路线仍属另一 lane ✓）
- 本档**未动算** ✓（无 SAT／无求解器 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 机制占用表  命中文件数=1    :: ./FRONTIER-R3-2026-09-27-phase1-steiner-cells-mechanism-inventory.md 
技术词 p-rank 扩张障碍 命中文件数=1    :: ./FRONTIER-R3-2026-09-27-phase1-steiner-cells-mechanism-inventory.md
```
- **本档新增**：Steiner cell 机制占用表、p-rank 扩张障碍候选（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：KKW 方法、Kramer–Mesner、paramodification、Ji–Zhu、DHV 1978、CSQS(94)
