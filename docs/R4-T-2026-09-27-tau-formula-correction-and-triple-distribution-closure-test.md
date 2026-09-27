# R4-T-2026-09-27 — **$\tau$ 公式修正** ＋ triple-distribution closure test（T1/T2/T3）

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗（★ 已核 `E58-triple-sum-collapse.md` 属**空间 A（RH）**，仅**同名冲突**，**不引用、不合并** ✓）。
> **范围（照唐先生 22:32 令 ✓）**：先做 T1–T3 的符号/有限筛选；**不上 SDP** ✗；零程序计算 ✓。

**已查地图：命中 ＋ ★ 一处必须修正（本档核心 ✓）**
所查：`docs/R4-P1b-2026-09-27-triple-layer-gates-T1-T2-T3-symbolic-screening.md`（**$\tau$ 公式与二分** ✓✓）｜`docs/R5-2026-09-27-triple-union-exact-values-and-the-global-inclusion-exclusion-identity.md`（**$U$ 值集 ＋ 全局恒等式** ✓✓）｜`docs/FIBER-2026-09-26-…`（**三阶不变量带证人** ✓）｜`docs/TERM-2026-09-27-…`（**邻域路线封存** ✗）｜`docs/E58-triple-sum-collapse.md`（**空间 A，同名，不跨** ✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §6）
D0: 本档对象 ＝ **档案已有** 三点 $\tau$／分布对象的**公式修正与 closure test**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**修正唐先生的 $\tau$ 公式（补因子 $[a\le2\wedge b\le2]$）＋ 给出正确二分 ＋ 完成 T1/T2/T3** ✓）
**[RESEARCH]**

---

## §0 结论（**一处修正 ＋ 两处确认 ＋ T1/T2/T3 完成**）

$$\boxed{\textbf{修正 ✗}:\ \tau=\tfrac{a+b-c}2+\mathbf 1[a{=}b{=}1]\ \textbf{缺因子}\ \mathbf 1[a\le2\wedge b\le2]\ ;\ \textbf{反例}\ (a,b,c)=(2,4,4):\ r=1\ \text{但}\ \tau=\mathbf 0\ ✗✓}$$
$$\boxed{\textbf{正确式 ✓✓}:\ \tau=\mathbf 1[\max(a,b,c)\le2]\ \Big(=\ r\cdot\mathbf 1[a\le2\wedge b\le2]+\mathbf 1[a\le1\wedge b\le1]\Big);\qquad \tau\in\{0,1\}✓}$$
$$\boxed{\textbf{确认 ✓}:\ \text{唐先生 §6／§7 恒等式\textbf{正确}}:\ \sum_{\{c_1,c_2,c_3\}}\tau=\sum_x\binom{b(x)}3=\tfrac16\big(\sum_x\delta(x)^3-285\big)✓✓}$$
$$\boxed{\textbf{T1/T2/T3 完成 ✓}:\ \text{T1 }\tau\ \text{值集（4 型）};\ \ \text{T2 marginal 方程};\ \ \text{T3 }\;T_3\ \text{由 }b\text{-profile 决定 ✓} \Longrightarrow \textbf{真问题＝profile 是否被 }A\text{ 决定}\ ⚠️}$$

---

## §1 修正的**反例与推导**（✓✓）

$$\text{唐先生路径}\ x=c_1\oplus e_i,\ i\in D_{12}\cap D_{13}:\ d(x,c_2)=a-1,\ d(x,c_3)=b-1✓\ \text{（\textbf{正确} ✓）}$$
$$\Longrightarrow\ \text{但须要求 }a-1\le1\ \textbf{且}\ b-1\le1\ ⟹\ a\le2\ \textbf{且}\ b\le2✓✓\ \text{（唐先生此处漏掉该条件 ✗）}$$
$$\textbf{反例（决定性 ✓）}:\ (a,b,c)=(2,4,4)\Longrightarrow r=\tfrac{2+4-4}2=1>0✓;\ \text{但}\ x=c_1\oplus e_i\ (i\in D_{12}\cap D_{13}):\ d(x,c_2)=1✓\ \text{而}\ d(x,c_3)=b-1=\mathbf 3>1✗$$
$$\qquad\Longrightarrow x\notin B_1(c_3)\ ✗;\qquad \text{且 }x=c_1:\ a=2>1⟹c_1\notin B_1(c_2)\ ✗ \Longrightarrow \boxed{\tau=0}\ ✓\ \text{（唐先生式给 }1\ ✗✓）$$
$$\text{（同型反例族 ✓）}:\ (a,b,c)=(4,2,4),\ (2,3,3)\ \text{等，凡 }\max>2\ \text{而}\ r>0\ \text{者 ✓}$$

## §2 正确公式与 T1（**值集 ✓**）

$$\tau=[\max(a,b)\le1]+n_{11}[a\le2\wedge b\le2]+n_{10}[a\le2\wedge n_{01}=0]+n_{01}[a=0\wedge b\le2]✓\ (\text{R4-P1b §2}✓)$$
$$\text{非退化下第 1、2 项\textbf{互斥}（}n_{11}\ge1\Rightarrow a=b=1\Rightarrow c=0\ \text{退化 ✗）⟹ }\boxed{\tau=\mathbf 1[\max(a,b,c)\le2]}\ ✓✓;\qquad \tau>0\iff\text{三点构成 }G_2\ \text{三角形}✓$$
$$\textbf{T1 值集 ✓}:\ \tau=1\ \text{的可达型（全部）}\ =\ \{\mathrm{perm}(1,1,2),\ (2,2,2)\}\ \text{共 }\mathbf 4\ \text{型}✓;\ \text{其余 admissible 型}\ \tau=0✓$$
$$\text{（admissible 条件 ✓，用户 ✓ 正确）}:\ a+b+c\ \text{偶}\ \wedge\ \text{三角不等式}\ \wedge\ a+b+c\le20✓$$

## §3 T2：$N_{abc}$ 的 **marginal 方程**（✓）

$$N_{abc}:=\#\{\text{无序码字三元组}\};\ \text{三点距离为其}(a,b,c)\ \text{（含重排）}✓$$
$$\textbf{二阶 marginal（精确 ✓）}:\quad \sum_{(a,b,c)}N_{abc}\cdot\#\{i\in\{1,2,3\}:d_i=k\}=(m-2)\,A_k^{(u)}✓\ \big(A^{(u)}=\text{无序对计数},\ m=|C|✓\big)$$
$$\qquad\text{（因每个距离-}k\ \text{对恰属于 }m-2\ \text{个三元组 ✓；且 }\sum_{abc}N_{abc}=\binom m3✓\big）$$
$$\textbf{T2 判定 ✓}:\ \text{上述方程\textbf{不}决定 }N_{abc}✓\ \text{（与"同边数异三角形数"同型 ✓）} \Longrightarrow \textbf{三阶自由度确实存在}✓\ \text{（＝FIBER 的 }\sum_xP(x)^2\ \text{结论同型 ✓ 非新 ✗）}$$

## §4 T3：**covering 耦合**（用户 §6／§7 ✓ 正确）

$$T_3:=\sum_{\{c_1,c_2,c_3\}}\tau=\sum_{abc}N_{abc}\tau(a,b,c)=\sum_x\binom{b(x)}3=\tfrac16\Big(\sum_x\delta(x)^3-285\Big)✓✓\ (\text{唐先生公式 ✓ 正确})$$
$$\text{（与本档 R5 的修正一致 ✓）}:\ \sum_x\binom{b(x)}3=T_3\ \textbf{（不是 }6T_3\text{）}✓;\ \text{且 }T_3=Q+\sum_x\binom{\delta(x)}3✓ \Longrightarrow T_3\ge Q\ge1✓✓$$
$$\textbf{T3 判定（诚实 ✓）}:\ T_3\ \text{是 }b\text{-profile 的函数}:\ T_3=\sum_j\binom j3n_j\ ✓\ \Longrightarrow\ \textbf{T3 本身\textbf{不}提供超出 profile 的覆盖耦合}✗$$
$$\qquad\Longrightarrow\ \boxed{\textbf{真问题＝}\ b\text{-profile }\{n_j\}\ \text{是否被 }A=\{A_k\}\ \text{决定}？}\ ⚠️\ \textbf{开放}✓\ \text{（＝FIBER／TERM 留下的同一边界 ✓）}$$
$$\qquad\text{（若 YES ⟹ 三点层整体被二阶吸收 ✗；若 NO ⟹ 三点层有独立覆盖含量，但仍须与 }119\ \text{的其它约束耦合 ⚠️）}$$

## §5 与档案的关系（**防重复 ✓**）

| 项 | 档案 | 本档判定 |
|---|---|---|
| 三点层超二阶自由度 | `FIBER-2026-09-26`（$\sum_xP(x)^2$ 不被二阶决定，**带证人**） | **同型 ⟹ 不主张为新** ✗ |
| triple 邻域局部结构 | `TERM-2026-09-27`（$n=4$ 全枚举 ⟹ 邻域结构零变化 ⟹ **封存** ✗；$n=5$ **无数据**） | 已封（对象＝**邻域**，非本档的**计数** ✓） |
| `E58-triple-sum-collapse` | **空间 A（RH）** | **同名冲突，不跨空间** ✓✗ |
| **$\tau$ 公式修正 ＋ 正确二分 ＋ $U\in\{28,29,31,33\}$ ＋ 全局恒等式** | 未见 | **本档 ✓**（沿用 R4-P1b／R5 ✓） |

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "三点分布"
技术词 三点分布        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "N_{abc}"
技术词 N_{abc}         命中文件数=0    ::
$ bash scripts/tech_word_check.sh "兼容性判据"
技术词 兼容性判据      命中文件数=0    ::
$ bash scripts/tech_word_check.sh "三阶矩"
技术词 三阶矩          命中文件数=49   :: ./E58-triple-sum-collapse.md ./GT-0-and-GT-STRATEGY-audit.md ./FCG-0-adversarial-models-and-failure-signatures.md
$ bash scripts/tech_word_check.sh "profile 决定"
技术词 profile 决定    命中文件数=6    :: ./CONGRUENCE-119-2026-09-27-global-integer-audit-collapse.md ./R4-P1-2026-09-27-private-point-deficit-lemma-and-codeword-labelled-occupancy.md ./ASSETS-REGISTRY.md
```
- **本档新增**：**0** 个术语 ✓（`三点分布`／`N_{abc}`／`兼容性判据` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`三阶矩`（49）／`profile 决定`（6）为档案已有 ✓）
- **注 ✓**：本档实质＝**§1 反例修正 ＋ §2 正确二分 ＋ §3/§4 closure test**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/Terwilliger** ✗；**未碰** R3 线／$\mu$／PSD／SAT ✓；**不跨空间**（E58 ✗）✓；**未开门②** ✓；**未改门** ✓
- **不声称** $K(10,1)\ge120$ ✗（V290）；**不声称** 三点层必然破局 ✗ —— 只给**公式修正**＋**正确二分**＋**closure test 的诚实边界** ✓
- **修正已显式标注** ✓（防后续复用错误 $\tau$ 式 ✗）
