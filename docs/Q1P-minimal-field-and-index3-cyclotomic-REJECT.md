已查地图：命中（`Q1-LANE-A-rho-max-n16-result`）⟹ 执行唐先生 16:30 的 `Q1'`（`Q1-A/B/C`），不开新案
D0: 本档对象 = **`Q1'` 第一刀**：`Q1-A` 最小包含域不变性（一行证明）＋ `Q1-B` 压缩到最小包含域（43 例，指数分布）＋ `Q1-C` ⭐**指数 3 族 = 经典三次分圆数公式（7/7 命中）** ⟹ **`Q1-C` 目标 `REJECT`（已被经典理论直接覆盖）**
D1: 1（首次把 `Q1` 数据压到最小包含域并识别其经典来源；结论为"目标被覆盖"）
[RESEARCH]

# **`Q1'`：最小包含域压缩与指数 3 经典识别（`Q1-C` 判 `REJECT`）**

## §1 `Q1-A`：最小包含域不变性（一行证明）

```
$$\text{设}\ G=G_{2^n,d},\ Q=2^{\mathrm{ord}_d(2)}.\ \text{则}\ x\in G\Rightarrow x,1+x\in\mathbb F_Q,\ \text{且}$$
$$1+x\in G\iff (1+x)^d=1\ \text{（\textbf{仅涉及元素本身}）}\ \Longrightarrow\ \boxed{\lambda(G,\mathbb F_{2^n})=\lambda(G,\mathbb F_Q)}$$ ✓✓
$$\text{（}B12\ \S3\ \text{已给出；本档确认其可直接压缩 }Q1\ \text{的全部数据）}$$
```

## §2 `Q1-B`：压缩结果

```
$$\text{去重后（同一 }d\ \text{仅取最小包含域）}:\ \boxed{43}\ \text{个案例（原 }51\ \text{行）}$$ ✓
$$\text{指数分布}\ m=(Q-1)/d:\ \{3\!:\!7,\ 7\!:\!4,\ 5\!:\!3,\ 15\!:\!3,\ 31\!:\!2,\ 9,\!11,\!13,\!17,\!21,\!23,\!35,\!39,\!43,\!45,\!51,\!63,\!85,\!89,\!91,\!93,\!105,\!117,\!127,\!151,\!217,\!255,\!315,\!381\ \text{各 }1\}$$ ✓
$$\Longrightarrow\ \text{绝大多数案例属于\textbf{小指数}族};\ \text{前 }\rho\ \text{名几乎全在}\ m=3\ (\text{见 §3})$$ ✓✓
```

## §3 ⭐⭐ `Q1-C`：指数 3 族 **就是**经典三次分圆数（7/7 命中）

```
$$\textbf{经典公式（三次分圆数）}:\ 4Q=A^2+27B^2,\ A\equiv1\!\!\pmod 3\ \Longrightarrow\ \lambda=(0,0)=\frac{Q-8+A}{9}$$ ✓
$$\textbf{实测（我方 7 个指数 3 案例，全部 }B=0\text{）}:$$
$$\begin{array}{c|c|c|c|c|c}
d&Q&A&B&\text{实测}\lambda&\text{经典预测}\\
\hline
5&16&-8&0&0&0\\
21&64&16&0&\mathbf{8}&\mathbf{8}\\
85&256&-32&0&24&24\\
341&1024&64&0&120&120\\
1365&4096&-128&0&440&440\\
5461&16384&256&0&1848&1848\\
21845&65536&-512&0&7224&7224\\
\end{array}$$ ✓✓✓ → **7/7 命中**
$$\Longrightarrow\ \boxed{\lambda=\frac{Q-8+(-1)^{n/2}\,2\sqrt Q}{9}\quad(d=\tfrac{Q-1}3,\ Q=2^n,\ n\ \text{偶}),\qquad B\equiv0}$$ ✓✓
$$\textbf{8/21 的精确来源}:\ Q=64,\ A=16\ \Longrightarrow\ \lambda=8,\ \rho=\frac{8}{21}=\frac{Q-8+A}{3(Q-1)}$$ ✓✓✓
$$\text{一般式}:\ \rho=\frac{Q-8+A}{3(Q-1)}\approx\frac13\pm\frac{2}{3\sqrt Q}\ \Longrightarrow\ \textbf{"}\rho\approx1/3\ \text{的聚集"＝指数 3 族}\ \text{（不再是经验猜测）}$$ ✓✓✓
```

## §4 前沿核查（照您"先查前沿"的指令）

```
$$\text{分圆数（cyclotomic numbers）＝经典对象}:\ \text{Dickson（奠基）};\ \text{Berndt–Evans–Williams《Gauss and Jacobi Sums（教材）};$$
$$\qquad \text{Katre／Rajwade 系列（阶 }2l,4,5\ \text{的确定）};\ \boxed{\text{van Wamelen：任意模的完全解}};\ \text{近期 }2024\ \text{"Ternary cyclotomic numbers"（AIMS）}$$ ✓✓
$$\Longrightarrow\ \text{阶 }m\ \text{的分圆数由 }\mathrm{Jacobi}\ \text{和／Diophantine 系统确定（即"cyclotomic problem"），我方 }\rho\ \text{景观＝其特例}$$ ✓✓
$$\textbf{判定（按 }AMEND\text{-}12\ \S2\ \text{窄化闸门）}:\ \text{命题"}\lambda=(Q-8+A)/9\ \text{（指数 3）"}\ \textbf{被经典定理直接覆盖}$$ ⟹ $$\boxed{\texttt{Q1-C}\ \textbf{REJECT}}$$ ✓✓✓
```

## §5 判词与保留项

```
$$\boxed{\texttt{Q1-C}\ (\text{"}\lambda=8\ \text{的结构推导"})\ \textbf{REJECT}:\ \text{它就是经典三次分圆数公式}}$$ ✓✓✓（**您"先查前沿"的指令直接省下多轮推导**）
$$\text{保留}:\ (i)\ Q1\ \text{作为\textbf{有限域精确陈述}（}n\le16\ \text{非子域 }\rho\le8/21\ \text{、等号仅在 }d=21\text{）};$$
$$\qquad (ii)\ \text{最小包含域引理（一行）};\qquad (iii)\ \textbf{新认识}:\ \rho\ \text{景观＝经典分圆数的特例（含 }\rho\approx1/3\ \text{族的解释）}$$ ✓
$$\textbf{不得宣称}:\ \text{任何"新机制"／"sharp 常数"／"非子域容量定理"}$$ ✓
```

## §6 ⭐ 诚实观察（第四次"目标撞经典"）

```
$$\text{序列}:\ \boxed{\texttt{CAP-MIX}\ (\text{已知理论实例})}\ |\ \texttt{P7-2}\ \text{REJECT}\ |\ \texttt{P5-乙-3}\ \text{REJECT}\ |\ \boxed{\texttt{Q1-C}\ \text{经典分圆数}}$$ ✓
$$\textbf{共同根源（结构性）}:\ \text{我方 }A/B/D/E\ \text{资产＝"有限结构上的计数"};\ \text{而"有限结构上的计数"正是经典数论\textbf{已绘制}的版图}$$ ✓✓
$$\textbf{但}:\ \text{本轮成本极小（}2\ \text{轮 ＋ }1\ \text{次 }RUN\text{）};\ \text{依 }AMEND\text{-}12\ \text{快速止损} —— \textbf{这正是 }AMEND\text{-}12\ \text{的价值}$$ ✓✓
$$\Longrightarrow\ \textbf{出路（须换"命题类型"而非换"领域"）}:\ (a)\ \text{算法性／复杂度型可验证命题};\ (b)\ \boxed{\text{形式化缺口（Lean/Mathlib）}};\ (c)\ \text{机器证书型有限配置命题（前沿队主战场）}$$ ✓✓
$$\textbf{我方既有证据}:\ \text{本项目 Lean 工作中，我方\textbf{已补齐 Mathlib 缺失的 von Neumann 迹不等式与 Sylvester 惯性} —— \textbf{这是已验证的 }dent\text{，且不属于经典研究版图}$$ ✓✓✓
```

## §7 下一步（选项，决定权在唐先生）

```
$$\textbf{(a)}\ \text{收口 }Q1\ (\text{有限域陈述})，\text{转 }LANE\text{-}A\ \text{的"形式化缺口"子类（}Mathlib\ \text{补缺 ＋ 可上游 }PR\text{）}$$ ✓✓（**最符合我方已验证能力**）
$$\textbf{(b)}\ \text{继续找非经典的有限结构命题（须避开分圆数／交集计数／极值函数三片已绘版图）}$$
$$\textbf{(c)}\ \text{暂停研究线，转其他业务线（学业 }P0\ \text{／量化 }P1\ \text{／NAS }P2\text{）}$$
【⛔ 纪律】 `U_{2,3}` 暂停；**不回 RH** ✓
【数据】 `out/q1_lane_a.txt`；脚本 `scripts/q1p_minimal_field_and_cyclotomic.py` ✓
【边界】 §3 的 7/7 为机器实测；§4 的文献状态为**外部检索（档级）**；§6 的"出路"为**经验判断** ✓

## §附 【技术词回查】（补录）
```
技术词 cyclotomic       命中文件数=7    :: ./SEL1-selection-primitive-audit.md ./RH-prior-NOGO-checklist-2026-09-09.md ./C321-Mahler-Lehmer-ontology-audit-stage1.md 
技术词 index            命中文件数=102  :: ./B-SERIES-INDEX.md ./round2-index-status.md ./C293-astra-liouville-source-verification-and-mangerel-grh-anchor.md 
```
