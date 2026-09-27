已查地图：已跑 scripts/prework_map_check.sh surfeit 受限泛函 supercode 嵌入性 ⟹ 执行自 `M2-PREWORK-2026-09-27` ✓＋ 唐先生 09:39 ✓；本档为 **M-2A′ 状态核查（档案原文为准）＋ M-2B 嵌入性 gate（纯 PRE-WORK ✓）**。
D0: 本档对象 = surfeit 受限泛函的档案状态与 supercode 的嵌入性前提
D1: 0（产出为两项无入口判定 ＋ 本轮汇总）

# M2B-2026-09-27 · 嵌入性 gate 与 M-2A′ 状态

## §0 结论（先给）

```
$$\boxed{\textbf{(EE-1 M-2A′ 无活口)}\ \text{surfeit 受限泛函的"候选割"}\ \textbf{有效性从未被证明}\ ✗\ (\texttt{ALIGN}\ \S2\ \text{审计: "有效性未证"}\ ✓);\ \text{且下游 pair 链}\ \textbf{无法闭合}\ ✗\ (\texttt{SECOND-ORDER}\ ✓)$$
$$\Longrightarrow\ \textbf{M-2A′} = \text{无入口}\ ✗$$
$$\boxed{\textbf{(EE-2 M-2B 无入口)}\ \text{supercode 所需的嵌入}\ C\subseteq C_0\ \textbf{不被}\ 119\text{-cover 结构强迫}\ ✗\ \Longrightarrow\ \textbf{DROP}\ ✗\ \text{（按唐先生自设 gate ✓）}}$$
$$\boxed{\textbf{(EE-3 本轮汇总)}\ \text{唯一真收获＝P1-A 关闭}\ ✓✓;\ \text{M-1／M-2A／M-2A′／M-2B \textbf{四杀}}\ ✗;\ \text{规模下界仍为唯一靶心}\ ✓}$$
$$
$$
```

---

## §1 (EE-1) M-2A′ 状态：档案原文（不凭上下文猜 ✓）

```
$$\texttt{ALIGN-2026-09-25}\ \S2\ \text{审计修正版（23:33 ✓）}:\ \text{原"surfeit 切掉均匀解"\ \textbf{有定义混淆}}\ ✗\ \Longrightarrow\ \text{更正为\textbf{三泛函 A／B／C}}$$
$$\qquad\text{A（无切割力）}: -1024\ ✗;\quad \mathbf{B}\ \text{（受限·两步 ＝ Wu--Chen surfeit 结构）}:\ \Sigma_{v\notin C}(\mathrm{ball}(v)-1)=1556,\ \text{均匀点处}\ -(10/11)\cdot1024=-930.9091<0\ \Longrightarrow\ \textbf{候选割}\ ✓\ (\text{⚠️ 有效性未证}\ ✗)$$
$$\qquad\text{C（受限·一步）}: 196,\ =0\ \Longrightarrow\ \text{不切}\ ✗$$
$$\qquad\text{原文"不可锁死"}:\ \text{"surfeit 已切掉 }z=1/11\text{"\ \textbf{不可}写成事实}\ ✗\ \text{—— 须先确定各泛函归属；B 仅\textbf{候选}，\textbf{有效性待证或待引原文}}\ ✗$$
$$\texttt{SECOND-ORDER-2026-09-25}\ \text{结论}:\ \text{"层 }i\ge1\ \text{的 }\delta_i\ \textbf{不直接进入}\ \text{pair 层}\ ✗\ \Longrightarrow\ \textbf{pair 链自身无法闭合}}\ ✓$$
$$\texttt{HQ1-2026-09-26}:\ \text{一阶层式（含 Haas 线性不等式族）在 }Q=1\ \text{子空间上\textbf{不产生任何 }A_1\ \text{依赖}}\ ✗\ \Longrightarrow\ \text{STOP}\ ✓$$
$$\Longrightarrow\ \textbf{判定}:\ \text{surfeit 路线\textbf{唯一残留}＝B 候选割的\textbf{有效性}（需原文或自行推导 ✓）;\ 而 }n=10\ \text{落在 Wu--Chen}(6\mid n)\ \text{与 Haas}(n\equiv-1\bmod3)\ \text{两个"好同余情形"}\ \textbf{之外}\ ✗\ (\texttt{ALIGN}\ \text{已记 ✓})$$
$$
$$
```

---

## §2 (EE-2) M-2B 嵌入性 gate（纯 PRE-WORK ✓，不算 bound ✓）

```
$$\textbf{第一问（唐先生指定 ✓）}:\ \text{119-cover 的结构是否\textbf{强迫}\ }C\subseteq C_0\ (\text{低余维 linear／supercode}?)\ ✓$$
$$\text{① 唯一\textbf{典范}线性 }C_0\supseteq C\ \text{＝}\ \mathrm{span}(C)\ ✓;\ \text{但其结构}\ \textbf{由 }C\ \text{决定}\ ⟹\ \text{用于 bound 即\textbf{量身定制}}\ ⟹\ \textbf{循环}\ ✗$$
$$\text{② 一般位置}:\ 119\text{-子集}\ \text{以压倒概率张成}\ \mathbb F_2^{10}\ ⟹\ \mathrm{rank}=10\ ⟹\ \text{余维 }0\ ⟹\ \text{无结构}\ ✗$$
$$\text{③ 超平面情形（余维 1}）:\ \textbf{可能}\ ✓\ \text{但}\ \textbf{不被强迫}\ ✗\ \text{（说明：若 }C\subseteq H\ \text{（超平面）}，则 }H\ \text{内每点 }x\ \text{需被 }C\cap H\ \text{覆盖，其"H-内球"大小}=1+(10-\mathrm{wt}(u))\ ✓\ \Longrightarrow\ \text{计数门槛}\ |C|\ge512/10=51.2\ ✓<119\ ⟹\ \text{不被排除}\ ⚠️\text{）}$$
$$\Longrightarrow\ \boxed{\text{嵌入}\ C\subseteq C_0\ \textbf{既非强迫、亦非典范}\ ✗\ \Longrightarrow\ \text{Klapper supercode 方法对 119 属}\textbf{外加假设}}\ ✗\ \text{（按唐先生 gate ✓）}$$
$$\qquad\textbf{附}:\ \text{若要走 M-2B，须\textbf{先}有一条结构定理（如"任何 }119\text{-cover 的 rank}\le 9\text{"}）——\ \text{该定理不存在且未必为真}\ ⚠️$$
$$
$$
```

---

## §3 (EE-3) 本轮（Frontier R2）汇总（诚实 ✓）

```
$$\begin{array}{c|c|c}
\text{候选} & \text{结果} & \text{依据}\\
\hline
\text{M-1 BQP 提升} & \textbf{KILL}\ ✗ & \text{其"分离"≡ }f_u\le1\ \text{改写 ⟹ 循环}\ ✓\\
\text{M-2A 单点 refined-weight LP} & \textbf{KILL}\ ✗ & \text{档案已做，LP 恰}=1024/11\ ✓\\
\text{M-2A′ surfeit 受限泛函} & \textbf{无入口}\ ✗ & \text{B 候选割有效性未证 ＋ pair 链不闭合}\ ✓\\
\text{M-2B supercode} & \textbf{无入口（DROP）}\ ✗ & \text{嵌入非强迫、非典范 ⟹ 外加假设}\ ✓\\
\hline
\mathbf{P1-A（Booleanity）} & \mathbf{永久关闭}\ ✓✓ & \text{它只是 0/1 条件，平凡约束即可 ⟹ 红鲱鱼}\ ✓
\end{array}$$
$$\Longrightarrow\ \textbf{净收获}:\ \text{一条结构性澄清（问题形态锁定为 }K(10,1)\ge120?\ ✓\text{）};\ \textbf{无新杠杆}\ ✗$$
$$\qquad\textbf{119 状态不变}:\ \texttt{OPEN}\ ✓;\ \text{唯一靶心＝}\textbf{规模下界}\ ✓$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**档案原文引用** ✓（ALIGN／SECOND-ORDER／HQ1 ✓，不列为新提出 ✓）
- §2 为**纯 PRE-WORK 分析** ✓（未跑任何 bound 计算 ✓）；③ 的计数门槛为**说明用**（未证超平面情形可达 119 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张 supercode 方法普适无效 ✗（只主张对 119 无强迫入口 ✓）
- 后台 `p2b`（(supp,δ|supp) 是否决定 Booleanity ✓）仍在跑 ⚠️

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 嵌入性 gate   命中文件数=1    :: ./M2B-2026-09-27-embedding-gate-and-m2ap-status.md 
技术词 无活口判定  命中文件数=1    :: ./M2B-2026-09-27-embedding-gate-and-m2ap-status.md
```
- **本档新增**：M-2A′ 无活口判定、M-2B 嵌入性 gate 判定（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：三泛函 A/B/C、surfeit 候选割、pair 链不闭合、Haas 单点 LP、P1-A 关闭
