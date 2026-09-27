已查地图：已跑 scripts/prework_map_check.sh 唯一 triple 点 P 二阶矩 三阶不变量 ⟹ 执行自 `FIBER-2026-09-26`（(Z-4) ✓）＋ 唐先生 2026-09-27 09:20 稿 ✓；本档为**核验 ＋ 自我否证**（含撤回 ✓）；含全枚举 ✓。
D0: 本档对象 = 唯一 triple 点的 $P$ 恒等式与三阶量的钉死性
D1: 0（产出为核验通过 ＋ **撤回 FIBER 档 (Z-4)** ✗ ✓）

# TRIP-2026-09-27 · 唯一 triple 点与 (Z-4) 的撤回

## §0 结论（先给）

```
$$\boxed{\textbf{(AA-1 核验)}\ \text{唐先生本轮三条恒等式在\textbf{唯一 triple 类}（}\Sigma\binom b3=1\text{）中\textbf{全部成立}}\ ✓✓\ (\text{n=4 全枚举 480 例 ✓})}$$
$$\qquad \sum P=(n+1)|C|-2N_1-2^n+1\ ✓;\quad \sum P^2=\sum P+6d_3\ ✓;\quad a_3+d_3=1\ ✓$$
$$\boxed{\textbf{(AA-2 撤回 ⚠️)}\ \text{我上一轮 (Z-4) 主张"}\sum P^2\ \text{为独立三阶不变量"}\ \textbf{被本档推翻}\ ✗✗}$$
$$\qquad\text{原因}:\ \text{该测试\textbf{未加"唯一 triple"限制} ⟹ \text{变化来自 }(a_3,d_3)\ \text{非唯一的情形}\ ✗\ (\text{测试错配 ✓})$$
$$\qquad\text{正解}:\ \text{固定 }(|C|,N_1)\ \text{后 }\sum P^2\ \textbf{零变化}\ (0/3\ \text{组}\ ✓) ⟹ \sum P^2\ \textbf{被 }(|C|,N_1,d_3)\ \text{完全钉死}\ ✗$$
$$\boxed{\textbf{(AA-3 判定)}\ \text{故 }\sum P^2\in\{286-2N_1,\ 292-2N_1\}\ \text{仅是 }(N_1,d_3)\ \text{的\textbf{重参数化}}\ ✗\ \text{——无独立杠杆}}$$
$$
$$
```

---

## §1 (AA-1) 唐先生推导：逐条核验 ✓（n=4 唯一 triple 类，480 例全枚举 ✓）

```
$$\checkmark\ \sum_x P(x)=(n+1)|C|-2N_1-2^n+1\ ✓\quad(\text{n=10, }|C|=119:\ =286-2N_1\ ✓)$$
$$\checkmark\ \sum_x P(x)^2=\sum_xP(x)+6d_3\ ✓\qquad\checkmark\ a_3+d_3=1\ ✓\ (\text{唯一 triple 点 ✓})$$
$$\checkmark\ P(x)=\tbinom{b(x)-f(x)}2\ \text{的取值表}\ \{0,1,3\}\ \text{与 }P=3\iff(f,b)=(0,3)\ \text{一致}\ ✓$$
$$
$$
```

---

## §2 (AA-2) 撤回 (Z-4)（诚实 ⚠️）

```
$$\textbf{前档 (Z-4) 原话}:\ \sum_xP(x)^2\ \text{不被 }(\text{profile},N_1,N_2)\ \text{决定} ⟹ \text{"真正新的三阶 Boolean 不变量"}\ ✗$$
$$\textbf{本档更正}:\ \text{该结论的证人组 }((6,6,4),4,5)\ \text{中，}\sum P^2\in\{10,22\}\ \text{的差异来自 }a_3+d_3\ne1\ (\text{即多 triple 点})\ ✗$$
$$\qquad\text{在\textbf{唯一 triple 类}中}:\ \text{固定 }(|C|,N_1)\ ⟹ \sum P^2\ \text{恒定}\ (\textbf{0/3 组变化}\ ✓) ⟹ \textbf{非独立量}\ ✗✗$$
$$\Longrightarrow\ \boxed{\text{(Z-4) 撤回}:\ \text{本线\textbf{迄今未获得独立的三阶不变量}}\ ✗}\ \text{（先前的"独立"为测试错配的假象 ✓）}$$
$$
$$
```

---

## §3 (AA-3) 可得的新陈述：干净的二分（无杠杆 ✗）

```
$$\boxed{\text{Case A }(a_3=1,d_3=0):\ \sum P^2=286-2N_1}\ ✓\qquad\boxed{\text{Case B }(a_3=0,d_3=1):\ \sum P^2=292-2N_1}\ ✓$$
$$\textbf{性质}:\ \text{两式皆 }\sum P^2\ \text{关于 }(N_1,d_3)\ \text{的\textbf{仿射重写}}\ ✗\ \text{——与 FACE／THIRD 等档同型（重参数化 ✓）}$$
$$\qquad\Longrightarrow\ \text{四门判定}:\ N\ ✗\ (\text{非新量});\ \text{方向}\ —;\ \Longrightarrow\ \textbf{不计推进}\ ✗$$
$$
$$
```

---

## §4 唯一 triple 点邻域的实测数据（n=4 ✓，供下一刀参考）

```
$$\begin{array}{c|c|c}
(a_3,d_3) & \text{可实现 }N_1\ (\text{n=4}) & \text{备注}\\
\hline
(0,1)\ (t\notin C) & \{1\} & \text{仅 1 例范围}\\
(1,0)\ (t\in C) & \{2,3\} & \\
\end{array}$$
$$\qquad⚠️\ \textbf{n=5 抽样 30 万未命中}（随机 f 极难同时满足 }b\in[1,3]\ \text{与唯一 triple}\ ✓\text{）⟹ 须\textbf{构造式}取例（greedy 覆盖 ✓）方可扩样 ⚠️$$
$$
$$
```

---

## §5 判定与下一刀（诚实 ✓）

```
$$\textbf{本轮净结果}:\ \text{唐先生三条恒等式成立}\ ✓;\ \textbf{但 (Z-4) 独立量撤回}\ ✗\ ⟹\ \text{三阶路线\textbf{迄今只产出重参数化}}\ ✗$$
$$\textbf{下一刀（唐先生建议 ✓）}:\ \text{唯一 triple 点 }t\ \text{的 }10\text{-邻域引理}:\ N(t)\ \text{为独立集（}Q_{10}\ \text{无三角 ✓）};\ t\ \text{的 }3\ \text{个码邻两两距 }2 ✓$$
$$\qquad\text{待证目标}:\ \text{该邻域结构是否迫使 }N_1\ \text{落入更小离散集（并与 }d_3\ \text{耦合）}\ ✓$$
$$\qquad\textbf{诚实预期 ⚠️}:\ \text{3 个码邻两两距 2 ⟹ 与既有匹配定理＋中点结构\textbf{同源}} ⟹ \text{很可能再次给出 }A_1\le59/60\ \text{型同界}\ ✗\ \text{（须实测方可断言 ✓）}$$
$$\textbf{若再次只给出同界} ⟹ \text{建议把"三阶耦合"整体记为\textbf{重参数化类}并封存} ✗\ \text{（避免第 17 次同型 ✓）}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1–§3 为 **n=4 全枚举核验 ＋ 推导** ✓；§4 为**实测数据** ✓（n=4）
- **(Z-4) 撤回为本档正式结论** ✓（前档正文保留为历史记录 ✓，本档为更高级别更正 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张唯一 triple 邻域引理无用 ✗（待实测 ✓）
- 本轮未跑 SAT/CP-SAT ✓（仅全枚举 ＋ 抽样 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Z-4 撤回       命中文件数=0    :: 
技术词 唯一 triple 类 P 恒等式 命中文件数=0    ::
```
- 实跑 `scripts/tech_word_check.sh` 逐字输出见上（`Z-4 撤回` 命中 **0**；`唯一 triple 类 P 恒等式` 命中 **0**）⚠️
- **按纪律判定**：二者皆为**内部标签／描述性短语**（正文写作「（Z-4）撤回」与「唯一 triple 类的 $P$ 恒等式核验」），**非新造技术术语** ⟹ **不列为新命名** ✓；本档的实质是**撤回＋核验**，不含新术语 ✓
- **档案已有（引用，不列为提出）**：$P=\binom{S}{2}$、匹配定理、$N_1+N_2=143$、唯一 triple 点
