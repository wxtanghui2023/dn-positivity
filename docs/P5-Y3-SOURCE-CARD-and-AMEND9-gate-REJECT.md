已查地图：命中（`P5-YI-and-P7-round2-hits` §3）⟹ 本档出 `P5-乙-3` 的 `SOURCE CARD` ＋ 七问 ＋ `AMEND-9` 闸门，不开新案
D0: 本档对象 = **`P5-乙-3`（乘法子群 × 加法容量"能量失配"）的 `AMEND-9-PRE` 闸门**：≥3 个标准化定义 ＋ `S1`–`S5` ＋ `L1`–`L4` ⟹ 判定 **`REJECT`**
D1: 0（闸门档，零计算、零实现）
[REVIEW]

# **`P5-乙-3` SOURCE CARD 与 `AMEND-9` 闸门判定：`REJECT`**

## §1 原条取回（逐字，`P5-YI-and-P7-round2-hits` §3）

```
$$P:\ \text{给定乘法子群 }H\le\mathbb F_p^*\ \text{与集合 }A\subseteq H,\ \text{加法能量 }E^+(A)\ \text{能被乘法结构压到多低？}$$ ✓
$$K:\ \text{Kowalski 讲义与 Fourier 方法给出 }|H|\ \text{大时强结果};\ \text{小 }|H|\ \text{方法失效}（\text{逐字}:"\text{only succeed if }H\text{ is quite large}"）$$ ✓
$$G:\ \text{小乘法子群（}|H|\ll p^\varepsilon\text{）时的加法能量界};\qquad A:\ A+B+D;\qquad N:\ \text{小 }|H|\ \text{的新界}$$ ✓
```

## §2 ⭐ 硬检查（您的口径）：把"能量失配"写成 ≥3 个标准化定义

```
$$\textbf{(D1) additive energy}:\ E^+(A)=\#\{(a,b,c,d)\in A^4:\ a+b=c+d\}$$ ⟹ **标准量** ✓✓
$$\textbf{(D2) multiplicative energy}:\ E^\times(A)=\#\{(a,b,c,d)\in A^4:\ ab=cd\}$$ ⟹ **标准量** ✓✓
$$\textbf{(D3) mixed/cross energy}:\ E^{+\times}(A;B)=\#\{(a,b,c,d):\ a+b=cd\}\ \text{等价类}$$ ⟹ **标准量（已有专线）** ✓✓
$$\textbf{(D4) "失配"= (D1) 与 (D2) 之比/差}:\ \Delta(A):=\frac{E^+(A)}{E^\times(A)}\ \text{或}\ E^+(A)-E^\times(A)$$ ⟹ **非新量（两标准量的函数）** ✗
$$\textbf{(D5) 加法可分解性（}A=B+C\text{）／"not a sumset"}$$ ⟹ **标准研究对象（Shkredov 线）** ✓✓
$$\Longrightarrow\ \boxed{\text{五个标准化无一产生新量：}D4\ \text{是 }D1,D2\ \text{的组合};\ D1,D2,D3,D5\ \text{均为标准对象}}$$ ✓✓✓
```

## §3 `AMEND-9` §1 触发与七问

```
$$\texttt{S3}/\texttt{S4}:\ \boxed{\text{余项}/\text{结构型} —— \text{加法能量本身＝典型"结构性计数"}};\qquad \texttt{S5}:\ \text{单参数 }|H|\ \text{控制全部} \Longrightarrow \textbf{触发}$$ ✓✓
$$Q4:\ \text{OBJECT 是否改名？}\quad \boxed{\textbf{是}:\ \text{"能量失配" = 加法能量／乘性能量／混合能量的组合，无新对象}}$$ ✗✗
$$Q5:\ \text{第二尺度仍强迫？}\quad \text{该领域自己在大 }|H|\ \text{与小 }|H|\ \text{两侧都在推进（见 §4）}$$ ✗
$$\Longrightarrow\ \text{七问未过（}Q4,Q5\text{）};\ \text{但按您的纪律仍执行完整 }L1\text{–}L4$$ ✓
```

## §4 ⭐ `L1`–`L4` 文献封锁（**逐层命中**）

```
$$\textbf{L1 对象}:\ \boxed{\textbf{标准}} —— \text{"multiplicative subgroups 的加法性质／加法能量"是成熟领域}：$$
$$\qquad \text{Kowalski《exponential sums over small subgroups, revisited》（\textbf{即原条所引讲义}）};\ \text{Shkredov 系列};\ \text{"ADDITIVE PROPERTIES OF MULTIPLICATIVE SUBGROUPS OF }\mathbb F_p\text{"}$$ ✓✓✓
$$\textbf{L2 计数/结果状况}:\ \text{大 }|H|:\ \text{已有强结果（Kowalski／Fourier）};\ \textbf{小 }|H|:\ \text{标准方法失效（原条逐字）}\ \Longrightarrow\ \textbf{但该 regime 本身就是\textbf{已知开放问题}}$$ ✓✓
$$\qquad \text{（例：}MathOverflow\ \text{讨论"almost trivial subgroups"，已知界 }|G|\le c\,p^{3/4}\ \text{（Jacobi 和），并明确提问能否 }\lesssim\sqrt p\cdot\mathrm{polylog}）$$ ✓✓
$$\textbf{L3 方法}:\ \text{character sums／Jacobi sums／Stepanov／sum-product};\qquad \boxed{\text{我方 }D\ \text{只能"小 }p\ \text{精确核验"，\textbf{不能产生界}}}$$ ✗
$$\textbf{L4 特殊化（最关键）}:\ \boxed{\text{我们的 }A\subseteq H\ \text{表述本身已被覆盖}} —— \text{已有文献研究"\textbf{sets with small multiplicative doubling} 的加法性质"}$$ ✓✓✓
$$\qquad \text{（即 }A\subseteq H\Rightarrow A\ \text{乘性加倍受控}\ \Longrightarrow\ \text{其加法性质＝既有研究对象）};\ \text{另有 }arXiv{:}2304.13801\ (\text{大子群不可加分解})$$ ✓✓
$$\Longrightarrow\ \boxed{\text{L1 标准};\ L2\ \text{小 }|H|\ \text{是已知开放 regime};\ L3\ \text{我方资产无力};\ L4\ A\subseteq H\ \text{表述已被覆盖}}$$ ✓✓✓
```

## §5 判定与禁令

```
$$\boxed{\texttt{P5-乙-3} = \textbf{REJECT}}$$ ✓✓✓
$$\text{三条独立理由}:\ (1)\ \text{"能量失配"标准化后＝}D1/D2/D3/D5\ \text{的组合，\textbf{不产生新量}};\ (2)\ \text{对象与小 }|H|\ \text{regime 均属\textbf{已知开放问题}};\ (3)\ \textbf{我方资产（}A/B/D\text{）无新方法} —— D\ \text{仅能核验，不能给界}$$ ✓✓
$$\textbf{Gate 2 失败};\ \textbf{Gate 3（必须产生新量）失败};\ \text{且 }L4\ \text{显示连表述都已覆盖}$$ ✓
$$\textbf{禁止重开形态}:\ \text{不得"换 }p\text{／换 }A\text{／换成 }E^\times\ \text{再试"；不得把 }Kowalski\ \text{讲义的 quote 当缺口（它就是"方法在大 }|H|\ \text{才有效"的陈述）}$$ ⚠️
```

## §6 ⭐ 战略观察（本档新增，值得入台账）

```
$$\text{连续三次闸门结果}:\ \boxed{\texttt{CAP-MIX}\ \text{已知理论实例}\ |\ \texttt{P7-2}\ \text{REJECT}\ |\ \texttt{P5-乙-3}\ \text{REJECT}}$$ ✓✓
$$\text{共同点}:\ \text{候选由"在文献里找开放问题"生成};\ \text{而文献的开放问题\textbf{正是该领域自己在猛攻的}} \Longrightarrow\ \text{我们不缺问题，\textbf{缺差异化机制}}$$ ✓✓
$$\text{数学原因}:\ \text{我方资产（}A/B/D/E/G\text{）是\textbf{通用型}}（有限结构／容量／精确核验），\text{对"已知对象 + 已知方法"的战场不产生独占优势}$$ ✓✓
$$\Longrightarrow\ \text{按 }CAPMIX\ \S15\ \text{与 }AMEND\text{-}9\ \S3:\ \textbf{合法动作＝等新源}，\text{而非把剩余清单逐条磨}（\text{P8／P5-乙-2／P6 预计同型遇阻}）$$ ✓✓
$$\text{诚实标注}:\ \text{上述为\textbf{经验判断}，非定理};\ \text{若要逐条核实，须各出一次闸门卡（零计算）}$$ ⚠️
```

## §7 指针更新（照规则 6）

```
$$\texttt{P5-乙-3}\ \to\ \textbf{REJECT};\qquad \texttt{P7-2}\ \to\ \textbf{REJECT};\qquad \texttt{CAP-MIX}\ \to\ \textbf{ARCHIVED}$$ ✓
$$\textbf{剩余合法条目}:\ \texttt{P8}\ (\text{硬禁 }\neq\text{RH 变体});\quad \texttt{P5-乙-2}\ (\text{coset 余维数});\quad \texttt{P6}\ (\text{仅 failure-mechanism})$$ ✓
$$\boxed{\textbf{下一动作}:\ \text{由唐先生指定}\ \Longrightarrow\ \text{出该条闸门卡（零计算）};\ \text{或按 §6 建议\textbf{转入等新源}}}$$ ✓（**方向选择权保留给唐先生**）
【⛔ 纪律】 本轮**零计算、零实现**；`U_{2,3}` 暂停；**不回 RH**；`T-1` 仅 calibration ✓
【边界】 §1 为逐字取回；§2 为标准化；§3–§4 为**外部检索证据（文档级，未逐字核原文 PDF）**；§5–§6 为判定与经验判断 ✓

## §附 【技术词回查】（补录）
```
技术词 additive energy  命中文件数=14   :: ./CROSS-0-additive-multiplicative-cross-invariant-MAP-CHECK.md ./E20-E40-zero-density-2026-read.md ./C305-FSD-blind-spot-audit-program-four-classes-dual-ledger-five-rounds.md 
技术词 multiplicative energy 命中文件数=3    :: ./CROSS-0-additive-multiplicative-cross-invariant-MAP-CHECK.md ./P5-Y3-SOURCE-CARD-and-AMEND9-gate-REJECT.md ./TOPIC-INVENTORY-v2-asset-driven-research-space.md 
```
