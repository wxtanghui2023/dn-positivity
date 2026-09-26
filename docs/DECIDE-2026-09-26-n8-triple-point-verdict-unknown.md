已查地图：已跑 scripts/prework_map_check.sh n=8 判定 CP-SAT Q*(8) 三重覆盖 ⟹ 执行自 PINNING-2026-09-26-per-n-statement-and-n8-method-failures 档；本档为**n=8 决定性判定的首轮结果**（唐先生 2026-09-26 11:40 指令）；不开新方向 ✓。
D0: 本档对象 = 「∃ (8,32)_1 码含三重覆盖点」的完备可满足性判定（非新对象）
D1: 0（无新自由度；产出为 UNKNOWN 结论、冲突统计、编码改进方案）

# DECIDE-2026-09-26 · n=8 三重覆盖点判定

## §1 模型（完备判定 ✓，非启发式 ✓）

```
$$\text{变量}: y_c\ (c\in\mathbb F_2^8,\ 256\ \text{个布尔});\qquad \sum_c y_c=\mathbf{32}\ ✓$$
$$\text{覆盖}: \forall x:\ \sum_{c\in B_1(x)}y_c\ \ge1\quad(256\ \text{条，每条 9 变量}\ ✓)$$
$$\text{三重}: \sum_{c\in B_1(0)}y_c\ \ge3\quad(\text{平移 WLOG 把三重中心钉在 }0^8\ ✓)$$
$$\text{判定意义}: \text{UNSAT}\iff\text{不存在含 }b\ge3\ \text{的 }(8,32)_1\iff b(x)\le2\ \forall x\iff \boxed{Q^*(8)=0}\ ✓$$
```

## §2 ⏱ 首轮结果：**UNKNOWN**（900 s 上限用尽）✗

```
$$\text{CP-SAT}: \texttt{status=UNKNOWN},\ \textbf{conflicts=18{,}508{,}167},\ \text{branches}=63{,}730{,}815,\ \text{wall}=900.0\text{s}\ ✗$$
$$\text{纯 CNF/SAT}\ (\text{Glucose4},\ 28{,}961\ \text{子句},\ \text{seqcounter 基数编码}\ ✓):\ \text{首轮被我误杀}\ ✗;\ \text{已用 } \texttt{setsid}\ \text{重开，仍在跑}\ ⏳$$
$$\textbf{关键读数}:\ 18.5\text{M}\ \text{冲突内\textbf{未找到任何可行解}} \Longrightarrow \textbf{强烈提示 UNSAT}\ ✓\ \text{（但\textbf{不是证明}}\ ✗)$$
```

## §3 编码改进（下一轮，按收益排序 ✓）

```
$$\text{① \textbf{坐标置换对称破缺}（最值钱，}\approx 8!=40320\ \text{倍）}:\ \text{三重中心钉在 }0^8\ \text{后，坐标置换仍保持 }B_1(0)\ ✓$$
$$\qquad\Longrightarrow\ \text{可 WLOG 要求坐标度数降序 } d_1\ge d_2\ge\cdots\ge d_8\ ✓\ (\text{廉价、有效}\ ✓)$$
$$\text{② \textbf{最小性约束}（合法 ✓）}:\ \text{因 }K(8,1)=32\ \text{且任何 32 字覆盖都最小}\ \Longrightarrow\ \text{每个码字有私有点}\ ✓\ (\text{需辅助变量})$$
$$\text{③ 更长时间}:\ \text{UNKNOWN 属于"未决"}\ ✗\ \Longrightarrow\ \text{可给 1–2 小时预算再跑}\ ✓$$
```

## §4 状态

```
$$\text{n=8}: \text{判定未决}\ ✗\ (\text{证据偏向 UNSAT}\ ✓\ \text{但未证}\ ✗)\ |\ \text{纯 SAT 仍在跑}\ ⏳$$
$$\text{pinning}: \textbf{B/OPEN}\ ✓\ (\text{n=4,5,7 已定}\ ✓;\ \text{n=6 = 2/2 类同值}\ ✓✓;\ \text{n=8 未决}\ ✗)$$
$$\textbf{n=10, M=119}: \textbf{UNKNOWN}\ ✓\ (\text{不外推}\ ✗)$$
```

## §5 工程教训（已记 TOOLS.md ✓）

```
$$\text{后台长任务必须 } \texttt{setsid nohup ... \&}\ ✓\ ——\ \texttt{nohup}\ \text{单独不够}:\ \text{中止 exec 会连带杀死同进程组}\ ✗$$
$$\text{并再次踩中 } \texttt{pkill -f "含自身命令行"}\ \text{陷阱}\ ✗\ (\text{杀掉了自己的 shell}\ ✗)\ \Longrightarrow\ \text{一律用字符类技巧或 PID}\ ✓$$
```

## §6 边界（诚实标注）

- §2 的 **UNKNOWN ≠ UNSAT** ✗——**不得**写成"已证明不存在" ✗
- 18.5M 冲突无可行解 **只是证据** ✓，非证明 ✗
- 未对 n=10 外推 ✗；未触碰 119 ✓

## 【技术词回查】（定稿前逐字输出）

```
技术词 完备判定     命中文件数=2    :: ./DECIDE-2026-09-26-n8-triple-point-verdict-unknown.md ./CAPMIX1A-6-ledger-reconciled-and-decision-procedure.md 
技术词 对称破缺     命中文件数=16   :: ./ALIGN-2026-09-25-our-delta-field-vs-WuChen-excess-surfeit.md ./DECIDE-2026-09-26-n8-triple-point-verdict-unknown.md ./p44-round2-mechanism-classes.md 
技术词 坐标度数降序 命中文件数=1    :: ./DECIDE-2026-09-26-n8-triple-point-verdict-unknown.md 
技术词 最小性约束  命中文件数=1    :: ./DECIDE-2026-09-26-n8-triple-point-verdict-unknown.md
```

- **本档新增**（首次命名；回查命中 1 次 = 本档自身 ⟹ 属自命中，按纪律排除 ✓）：`坐标度数降序`、`最小性约束`
- **档案已有（引用，不列为提出）**：`完备判定`（另有 CAPMIX1A-6-ledger-reconciled-and-decision-procedure.md ✓）、`对称破缺`（16 档，含 ALIGN-2026-09-25-…、p44-round2-mechanism-classes.md ✓）
