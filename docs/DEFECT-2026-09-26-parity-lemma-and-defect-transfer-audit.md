已查地图：已跑 scripts/prework_map_check.sh 奇偶 Q=2A≤2−E 缺陷传递 van Wee 松弛 ⟹ 执行自 NEXT-2026-09-26（C1）与 2026-09-25 的 SECOND-ORDER/EXCESS 档；本档为**奇偶引理一般化 ＋ 缺陷传递审计（含一项诚实否定）**（唐先生 2026-09-26 12:16 指令）；纯推导＋数值校准，未跑 solver ✓。
D0: 本档对象 = Q 与 A_{≤2} 的桥、其奇偶推论、以及"van Wee 缺陷 → A_{≤2} excess"传递的可行性
D1: 1（新增独立结论：偶数 n 的奇偶判据 `Q ≡ M (mod 2)`；并关闭一条不可行的传递假桥）

# DEFECT-2026-09-26 · 奇偶引理 ＋ 缺陷传递审计

## §0 恒等式的**档案归属**（避免重复宣称 ✓）

```
$$Q=2A_{\le2}-E\quad(\star)\ \text{与}\ \sum_x\binom{b(x)}2=2A_{\le2},\quad E=M(n+1)-2^n\ \text{——\textbf{已立于 }2026\text{-}09\text{-}25\ \text{档}}\ ✓$$
$$\text{（见 docs/SECOND-ORDER-2026-09-25-*.md 与 docs/EXCESS-2026-09-25-*.md；本档\textbf{不}重复宣称新性}\ ✓）$$
$$\text{本档新增}: \text{奇偶引理的\textbf{一般化与推论}}（§2）\ \text{与 \textbf{缺陷传递的否定审计}}（§3）\ ✓$$
```

## §1 数值校准（120-码 ✓，防索引混淆 ✓）

```
$$\text{恒等式}: 2A_{\le2}-E=2\cdot199-296=102=Q_{\text{实测}}\ \Longrightarrow\ \textbf{一致}\ ✓✓$$
$$\sigma:=\sum_{x\notin C}|B_2(x)\cap C|=6202;\quad \frac{M(n+\binom n2)-\sigma}{2}=\frac{6600-6202}{2}=199=A_{\le2}\ \Longrightarrow\ \textbf{一致}\ ✓✓$$
$$\text{Struik 型一般不等式}: \sum_{x\notin C}\mathrm{OC}(B_1(x))=2460\ \ge\ 2^n-M=904\ \Longrightarrow\ \text{成立但\textbf{松弛 }2.72\times}\ ✗$$
```

## §2 ⭐ **奇偶引理**（一般化 ＋ 新推论 ✓）

```
$$\text{由 }(\star):\ Q\equiv E\equiv M(n+1)-2^n\ (\mathrm{mod}\ 2)\ ✓\ \Longrightarrow\ \textbf{新增}: \ n\ \text{偶}\ \Longrightarrow\ Q\equiv M\ (\mathrm{mod}\ 2)\ ✓✓$$
$$\boxed{\textbf{推论 P1}:\ n\ \text{偶且 }K(n,1)\ \text{奇}\ \Longrightarrow\ Q^*(n)\ge1\ (\text{无条件}\ ✓,\ \text{独立于 van Wee/NP1CC}\ ✓)}$$
$$\text{对候选 }(10,119)_1:\ E=285\ \text{奇}\ \Longrightarrow\ Q\in\{1,3,5,\dots\}\ \Longrightarrow\ \boxed{Q\ge1}\ ✓\ (\text{与 }2026\text{-}09\text{-}25\ \text{结论一致}\ ✓)$$
$$\text{对 }n=9\ (\text{奇}):\ E=62\cdot10-512=108\ \text{偶}\ \Longrightarrow\ Q\ \text{偶}\ \Longrightarrow\ \boxed{Q^*\in\{0,2,4,\dots\}}\ ✓\ \text{（比"}>0"更锐}\ ✓✓)$$
$$\text{适用范围}: \text{仅在 }M\ \text{奇}\ \text{且}\ n\ \text{偶时给出 }Q\ge1\ ✓;\ \text{已知 }K\ \text{在偶 }n\ \text{处目前全为偶数}\ ✗\ \Longrightarrow\ \text{P1 暂\textbf{无用例}，但为 C1 开放半边提供了\textbf{独立的算术通道}}\ ✓$$
```

## §3 ⛔ **缺陷传递的否定审计**（关键诚实项 ✓）

```
$$\text{拟议链}: \text{van Wee 缺陷 }\Delta>0\ \Longrightarrow\ \text{额外 }A_{\le2}\ \Longrightarrow\ Q>0\ ✗$$
$$\textbf{否定①}: \text{在 }(10,119)_1\ \text{处 van Wee 界\textbf{根本不紧}}: \ 10M=1190\ \text{vs}\ 2^{10}=1024\ ✓\ \Longrightarrow\ \text{松弛 }\sim16\%\ ⟹\ \Delta\ \text{不是绑定约束}\ ✗$$
$$\textbf{否定②}: \text{唯一可用的\textbf{局域}van Wee/Struik 不等式（}n\ \text{偶}:\ \mathrm{OC}(B_1(x))\ge1\ \forall x\notin C\ ✓)\ \text{实测松弛 }2.72\times\ ✗$$
$$\qquad\Longrightarrow\ \text{它\textbf{给不出}"额外一对"的强制}\ ✗\ (\text{聚合值 }2460\ \text{远大于下界 }904\ ✓)$$
$$\Longrightarrow\ \boxed{\text{§3 拟议链的第 1–2 步在 }M=119\ \text{处\textbf{不可用}}\ ✗\ \text{—— 应记为\textbf{关闭的假桥}}\ ✓}$$
$$\text{（其根因与 }2026\text{-}09\text{-}26\ \text{的 class E 判定同源}: \text{excess 型机器在 }M=119\ \text{的头部余量 }285\ \text{过大}\ ✓)$$
```

## §4 Q=1 路线的现行状态（不重启 ✓）

```
$$\text{Q=1 的 profile 锁定 }(N_1,N_2,N_3)=(740,283,1),\ A_{\le2}=143\ \text{——\textbf{已立于 }2026\text{-}09\text{-}25\ \text{档}}\ ✓$$
$$\text{其\textbf{局域禁形}攻击（唯一三重点 }\to\ \text{局部 Hamming 禁形}\ \to\ \text{矛盾）\textbf{今日已执行并关闭}}\ ✗$$
$$\qquad\text{依据}: \text{shadow-ledger 定量 no-go}\ ✓\ (\text{局域账本单位成本}\le33\ \text{点}\ \ll\ \text{头部余量 }285\ ⟹\ \text{原理上无法把三重点数压到 1}\ ✓)\ \text{—— class E}\ ✗$$
$$\Longrightarrow\ \textbf{不得重启该路线}\ ✗;\ \text{C1 开放半边的真正堵点} = \boxed{\text{需比"excess/局域计数"更强的\textbf{覆盖可视机制}}}\ ✗$$
```

## §5 n=9 的定位（唐先生定 ✓：只作检验机，不承担证明 ✓）

```
$$\text{若 }K(9,1)=62:\ E=108,\ Q=2A_{\le2}-108;\ \text{C1 预测 }Q>0\ ✓$$
$$\text{由 §2 收紧}: \ n=9\ \text{奇}\ \Longrightarrow\ Q\ \text{偶}\ \Longrightarrow\ \boxed{\text{C1 预测 } Q^*(9)\ge2}\ ✓\ (\text{零/二可判别}\ ✓)$$
$$\text{应输出}: (A_1,A_2,A_{\le2},Q)\ \text{＋}\ G_2(C)\ \text{局部度数分布}\ ✓\ (\text{即使 }Q=0\ \text{仍可问 }A_{\le2}=54\ \text{是否有禁形}\ ✓)$$
$$\textbf{不外推} n=10/119\ ✗;\ \textbf{119 保持 UNKNOWN}\ ✓$$
```

## §6 三张表（更新）

```
$$\textbf{CLOSED}: (\star)\ \text{恒等式};\ \sigma\ \text{式};\ \text{奇偶引理};\ \textbf{P1};\ Q=1\ \text{profile};\ \text{局域禁形路线（class E）};\ n=2^m/2^m-1\Rightarrow Q^*=0\ ✓$$
$$\textbf{RETRACTED/关闭假桥}: \text{n=8 三进制同余};\ \boxed{\Delta\to A_{\le2}\ \text{传递（}M=119\ \text{处不可用）}}\ ✗$$
$$\textbf{OPEN}: \text{比 excess 更强的覆盖可视机制};\ \text{非取等 }n\ \text{的 }Q^*(n);\ n=9\ \text{数据点（待定）};\ K(2^m,1)\ \text{出处};\ \textbf{119 UNKNOWN}\ ✓$$
```

## §7 边界（诚实标注）

- §1 为**数值校准**（120-码 ✓，我方代码 ✓）；§2 为**我方推导** ✓；§3 为**我方否定**（并给根因 ✓）
- §4 的"已关闭"依据为**今日档案** ✓（SHADOW-LEDGER 档 ✓）
- **本轮未跑 solver** ✓；**未**开 n=9 ✓（遵唐先生"不盲跑"✓）；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 奇偶引理     命中文件数=0    :: 
技术词 缺陷传递     命中文件数=0    :: 
技术词 覆盖可视机制 命中文件数=0    :: 
技术词 松弛审计     命中文件数=0    ::
```

- **本档新增**（命中数=0）：奇偶引理、缺陷传递、覆盖可视机制、松弛审计
- **档案已有（引用，不列为提出）**：—
