# WITTHM-2026-09-28 — **① 第一步完成：Theorem 2.5 ＋ Theorem 4.9 完整抽取（含全部依赖命题）｜锚点出处核实｜\textbf{战略性发现}：$n{=}10$ 之 SDP $=105.2223<107\le K(10,1)$，距 120 尚远 ⟹ ① 不能供给 Type II 所需之 $q$ 上界**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:30 令 ✓）**：① 第一步 —— 抽 Theorem 2.5／4.9；**文献直读 ＋ 抽取**（非计算 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-473／C-472／C-427／C-426，非新案 ✓）**
`docs/WITT3-2026-09-28-…`（**Type III 审计／$n{=}6/7$ 状态 ✓✓**）｜`docs/WITPOBJ-2026-09-28-…`（**$q$ 上界工具缺口 ✓✓✓**）｜`docs/C-427 registry`（**公开区间 $107\le K\le120$；我方 SDP 105.2223 低于 107 ✓✓**）｜`docs/L2AUDIT-2026-09-26-…`（**arXiv:2504.01932v2 Table 5 直读 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §4）
D0: 本档对象 ＝ **档案已有** Gijswijt–Polak SDP／DLP1 系列对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次完成 Theorem 2.5 与 Theorem 4.9 之\ \textbf{完整陈述抽取}（含 Prop 2.1–2.4／4.2–4.8 与 Remark 2.1–2.3 ＋ 变量集 $I(2,n)$ ＋ $O(n^3)$ 复杂度）＋ 首次逐字核实 $n{=}6/7$ 锚点之出处（Table 5 第 1510–1511 行）＋ 首次指出 SDP 在 $n{=}10$ 处**不能**供给 $q$ 上界** ✓）
**[RESEARCH]**

---

## §0 Theorem 2.5（**完整陈述 ✓✓**）

$$\textbf{设定 ✓}:\ q\ge2,\ n\ge1;\ \mathbb E=[q]^n\cong(\mathbb Z/q\mathbb Z)^n;\ C\subseteq\mathbb E\ \text{covering radius }r✓;\ (M_C)_{\mathbf u,\mathbf v}=\mathbf 1[\mathbf u,\mathbf v\in C]✓$$
$$M:=\tfrac1{|\mathrm{Aut}(q,n)|}\sum_{\sigma}M_{\sigma C}✓;\quad M':=\tfrac1{|\mathrm{Aut}|}\sum_{\sigma:\mathbf 0\in\sigma C}M_{\sigma C}✓;\quad M'':=\tfrac1{|\mathrm{Aut}|}\sum_{\sigma:\mathbf 0\notin\sigma C}M_{\sigma C}✓\quad(6)$$
$$\textbf{Prop 2.1（基本不等式与对称 ✓）}:\ M\ \text{为}\ \mathrm{Aut}(q,n)\text{-不变},\ M',M''\ \text{为}\ \mathrm{Aut}_{\mathbf 0}\text{-不变};\quad M_{\mathbf u,\mathbf v}=M'_{\mathbf 0,\mathbf v-\mathbf u}✓,\ M''_{\mathbf u,\mathbf v}=M'_{\mathbf 0,\mathbf v-\mathbf u}-M'_{\mathbf u,\mathbf v}✓$$
$$\qquad 0\le M'_{\mathbf u,\mathbf v}\le M'_{\mathbf 0,\mathbf u}✓;\quad 0\le M''_{\mathbf u,\mathbf v}\le M''_{\mathbf u,\mathbf u}✓;\quad \text{三点轨道不变性 ✓}$$
$$\textbf{Prop 2.2（半正定 ✓✓）}:\ M'\succeq0,\ M''\succeq0✓;\quad \boxed{R(1-M'_{\mathbf 0,\mathbf 0},\ M'')\succeq0}\ ✓\ \Big(R(c,A):=\begin{pmatrix}c&(\diag A)^*\\ \diag A&A\end{pmatrix}✓;\ R\succeq0\iff cA-(\diag A)(\diag A)^*\succeq0\ \text{（Schur）}✓\Big)$$
$$\textbf{Prop 2.3（目标函数 ✓✓）}:\ \boxed{|C|=q^nM'_{\mathbf 0,\mathbf 0};\quad |C|^2=q^n\sum_{\mathbf u}M'_{\mathbf u,\mathbf u};\quad |C|^3=q^n\sum_{\mathbf u,\mathbf v}M'_{\mathbf u,\mathbf v}}\ ✓✓$$
$$\textbf{Prop 2.4（Lasserre 约束 ＋ matrix cut ✓✓）}:\ N:=\tfrac1{|\mathrm{Aut}|}\sum_\sigma M_{\sigma C}\big(\sum_{\ell=0}^n\lambda_\ell|\sigma C\cap S_\ell(\mathbf 0)|-\beta\big)\quad(7)$$
$$\qquad\text{(i)}\ R(c,N)\succeq0,\quad c=\sum_{\ell=0}^n\lambda_\ell|S_\ell(\mathbf 0)|\cdot M'_{\mathbf 0,\mathbf 0}-\beta✓;\qquad\text{(ii)(iii)}\ N\ \text{三性 ✓};\qquad\text{(iv) 四条 matrix cut 不等式 ✓}$$
$$\qquad\text{(iii 之式 ✓)}:\ N_{\mathbf u,\mathbf v}=-\beta M_{\mathbf u,\mathbf v}+\sum_{\ell=0}^n\lambda_\ell\sum_{\mathbf w\in S_\ell(\mathbf 0)}M'_{\mathbf u-\mathbf w,\mathbf v-\mathbf w}✓;\quad\text{(iv)}\ \beta M'_{\mathbf 0,\mathbf u}\le\sum_\ell\lambda_\ell\sum_{\mathbf w\in S_\ell(\mathbf v)}M'_{\mathbf u,\mathbf w}\ \text{等四条 ✓}$$
$$\boxed{\textbf{Theorem 2.5（Covering lower bound ✓✓✓）}:\ }\text{若每个 covering radius }r\ \text{之 }C\subseteq\mathbb E\ \text{满足}\ (\lambda_0,\dots,\lambda_n)\beta\ \big(\text{即}\ \sum_i\lambda_i|C\cap S_i(\mathbf u)|\ge\beta\ \forall\mathbf u✓\big)\ \text{则}$$
$$\qquad\boxed{K_q(n,r)^3\ \ge\ \min_{M,M',M'',N}\ q^n\sum_{\mathbf u,\mathbf v\in\mathbb E}M'_{\mathbf u,\mathbf v}}\ ✓✓\ \text{（约束＝Prop 2.1 ＋ 2.2 ＋ 2.4 ✓）}$$
$$\textbf{Remark 2.2 ✓✓}:\ \text{由 2.1(i)／2.4(iii)，}M,M'',N\ \text{皆由 }M'\ \text{表出}\Longrightarrow \boxed{\text{变量可仅取 }M'}\ ✓\ \text{（关键：降维之起点 ✓）}$$
$$\textbf{Remark 2.3 ✓}:\ \sqrt[3]{q^n\sum_{\mathbf u,\mathbf v}M'_{\mathbf u,\mathbf v}}\ge\sqrt{q^n\sum_{\mathbf u}M'_{\mathbf u,\mathbf u}}\ge q^nM'_{\mathbf 0,\mathbf 0}✓\ \text{（三者中最紧为立方根式 ✓）}$$
$$\textbf{Remark 2.1（来源 ✓✓）}:\ \text{(i)–(iii) 之 }N\ \text{来自\ \textbf{Lasserre 层级}（大小 }\le1\ \text{之子集，}\mathrm{Aut}\text{-平均 ✓）};\ \text{(iv) 之四式来自\ \textbf{matrix cut 不等式}（引用 }[16]✓\big)$$

---

## §1 Theorem 4.9（**对称约化后之 $q{=}2$ 版 ✓✓**）

$$\textbf{变量集 ✓}:\ I(2,n)=\{(i,j,t)\mid 0\le t\le i,j,\ i+j\le n+t\}✓;\quad M^t_{i,j}\in\{0,1\}^{n}\text{-侧矩阵 ✓};\quad \mathcal A_{2,n}=\Big\{\sum_{(i,j,t)\in I(2,n)}x^t_{i,j}M^t_{i,j}\Big\}✓\ \big(\text{＝Terwilliger 代数 ✓}\big)$$
$$\textbf{（关键恒等式 ✓）}:\ \mathbf 1_{S_i(\mathbf 0)}(\mathbf 1_{S_j(\mathbf 0)})^{\mathsf T}=\sum_{t:(i,j,t)\in I(2,n)}M^t_{i,j}✓$$
$$\textbf{约化 ✓}:\ M'=\sum_{(i,j,t)}x^t_{i,j}M^t_{i,j}\ (20)✓;\quad \text{Lemma 4.1}:\ M=\sum x^0_{i+j-2t,0}M^t_{i,j}✓,\ M''=\sum\big(x^0_{i+j-2t,0}-x^t_{i,j}\big)M^t_{i,j}✓$$
$$\boxed{\textbf{Theorem 4.9 ✓✓✓}:\ }\text{若每个 covering radius }r\ \text{之 }C\subseteq\mathbb E\ \text{满足}\ (\lambda_0,\dots,\lambda_n)\beta\ \text{则}$$
$$\qquad\boxed{K_2(n,r)^3\ \ge\ \min_{x}\ 2^n\sum_{(i,j,t)\in I(2,n)}\binom{n}{i-t,\ j-t,\ t}x^t_{i,j}}\quad(30)✓✓$$
$$\qquad\text{约束 ＝ Prop 4.2（基本不等式／对称）＋ 4.3（半正定）＋ 4.5（Lasserre 约束）＋ 4.8（matrix cut 不等式）✓}$$
$$\qquad\text{其中 Lasserre 式（29）之系数 ✓}:\ \lambda^{i,j,t}_{j',t'}:=\sum_{d=0}^n\lambda_d\,\alpha^{(i,j,t)}_{(i,j',t'),d}✓\ \big(\alpha＝\text{Terwilliger 连结系数（§3 ✓）}\big)$$
$$\qquad\text{Prop 4.5 之四条（逐字 ✓）}:\ \sum_{j',t'}x^{t'}_{i,j'}\lambda^{i,j,t}_{j',t'}\ge x^0_{i,0}\beta✓;\ \ \sum_{j',t'}\big(x^0_{j',0}-x^{t'}_{i,j'}\big)\lambda^{i,j,t}_{j',t'}\ge\big(x^0_{0,0}-x^0_{i,0}\big)\beta✓;\ \ \text{另两条同型 ✓}$$
$$\boxed{\textbf{复杂度 ✓✓✓}:\ }\text{约化后 SDP 之\ \textbf{变量数}与\ \textbf{块尺寸平方和}皆为}\ \boxed{O(n^3)}\ ✓\ \big(\text{引 }(16)✓\big)\Longrightarrow\boxed{n{=}6,7,10\ \textbf{皆可算}}\ ✓✓$$

---

## §2 链条与"谁加了什么"（照唐先生 §B ✓✓）

$$\boxed{\text{Delsarte LP}\ \subset\ \text{Theorem 2.5（SDP）}\ \subset\ \text{Theorem 4.9（对称约化）}}\ ✓✓$$
$$\textbf{（论文自述，逐字 ✓✓）}:\ \text{"The LP bound requires nonnegativity of certain expressions involving Krawtchouk polynomials, which is equivalent to PSD of }M=M'+M''\text{;}\ \text{The LP bound further requires that a small subset of the matrix cut inequalities are satisfied.}\ \text{Thus the LP constraints are implied by the SDP constraints of Theorem 2.5."}\ ✓✓$$
$$\textbf{⟹ SDP 相对 LP 之\ \textbf{真实增益}＝三项 ✓✓}:\ \text{(a) }M',M''\ \textbf{分别}\ \text{PSD ＋ }R(1-M'_{\mathbf 0\mathbf 0},M'')\succeq0\ \text{（Prop 2.2 ✓）};$$
$$\qquad\text{(b) Lasserre 约束 }R(c,N)\succeq0\ \text{（Prop 2.4(i) ✓）};\quad \text{(c) 四条 matrix cut 不等式之\ \textbf{全族}（Prop 2.4(iv) ✓）}$$
$$\textbf{（4.9 相对 2.5 ✓）}:\ \text{非新约束，而是\ \textbf{块对角化}（Terwilliger 代数）⟹ 可算性 ✓（}O(n^3)✓\big);\ \text{计算所用 }(\lambda,\beta)\ \text{＝\ \textbf{球覆盖不等式 ＋ Van Wee 不等式}两族 ✓✓}$$
$$\qquad\text{（论文逐字 ✓）}:\ \text{"We computed the lower bounds following from Theorem 4.9 using the two }(\lambda_0,\dots,\lambda_n)\beta\ \text{coming from the sphere covering inequalities and the Van Wee inequalities."}\ ✓$$

---

## §3 锚点核实（**逐字出处 ＋ 对照真值 ✓✓**）

$$\textbf{出处（逐字 ✓✓）}:\ \texttt{l2txt.txt}\ \text{第 1510–1511 行（＝arXiv:2504.01932v2 Appendix A, Table 5, }q{=}2\big):\ \texttt{| 6 | 11.5980 | X | X | X | X | X |}\ ;\ \texttt{| 7 | 15.9999 | X | X | X | X | X |}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{n{=}6\to\mathbf{11.5980},\quad n{=}7\to\mathbf{15.9999}}\ ✓✓\ \text{（}R{=}1\ \text{列；其余 }R\ \text{为 X＝未给值 ✓）}$$
$$\qquad\textbf{含义 ✓}:\ \text{二者为 }K_2(n,1)\ \text{之\ \textbf{下界值}（非立方值 ✓）}\Longrightarrow\ \sqrt[3]{11.5980}\approx2.26✗\ \text{不符 ⟹ 确为界值本身 ✓✓}$$
| $n$ | SDP 锚点 | 真值 $K_2(n,1)$ | 差 |
|---|---|---|---|
| 6 | 11.5980 | **12**（shortened Hamming ✓） | **0.402** ✓ |
| 7 | 15.9999 | **16**（perfect Hamming ✓） | **0.0001** ✓✓ 近乎精确 |
| 10 | **105.2223** | $\ge\mathbf{107}$（公开下界 ✓ C-427） | **−1.78** ✗ 低于已知下界 |
$$\boxed{\textbf{★战略性发现（本档 ✓✓✓）}:\ }\text{目标任务 }K(10,1)\ \text{需证}\ \ge\mathbf{120}\ \text{（或排除 119-cover ✓）};\ \text{而本体 SDP 在 }n{=}10\ \text{仅给}\ \mathbf{105.2223}\ ✗✗$$
$$\qquad\Longrightarrow\ \boxed{\text{① 抽取成功，但该工具在 }n{=}10\ \textbf{不能}供给 Type II 所需之 }q\ \text{上界（距 120 越 14.8，且低于已知 107 ✓✗）}$$
$$\qquad\Longrightarrow\ \text{与档案一致 ✓✓}:\ \text{C-426"同工具再算撞不到窗口"}\ ✓;\ \text{C-427"105.2223 低于 107，真实缺口 }=120-107=13\text{"}\ ✓$$

---

## §4 复现计划（**可行，但只验证实现、不改战略 ✓**）

$$\textbf{可算性 ✓✓}:\ \text{变量数与块尺寸平方和 }O(n^3)\Longrightarrow n{=}6{:}\ \sim216,\ n{=}7{:}\ \sim343✓\ \text{（cvxpy+scs 已实测可用 ✓）}$$
$$\textbf{尚缺之源（诚实 ✗）}:\ \text{§3 之 }\alpha^{(i,j,t)}_{(i,j',t'),d}\ \text{（Terwilliger 连结系数）}\ \textbf{未抽}✗\ \text{（决定 }\lambda^{i,j,t}_{j',t'}✓\big);\ \text{及 }M^t_{i,j}\ \text{之显式定义 ✓}$$
$$\qquad\Longrightarrow\ \boxed{\text{复现门（照唐先生 ✓）}:\ \text{论文 }n{=}6,7\ \text{独立复现}\ \to\ \text{同值 11.5980／15.9999}\ \to\ \text{才谈 }n{=}10}\ ✓✓\ \text{（复现不过，}n{=}10\ \text{不开 ✓）}$$
$$\qquad\textbf{但（本档之诚实边界 ✓✓）}:\ \text{即使复现成功，}n{=}10\ \text{之值仍为 }105.2\ \text{级}\ ✗\Longrightarrow\ \text{可为 119 线提供之信息\ \textbf{有限}};\ \text{故应视作\ \textbf{工具审计}而非\ \textbf{主攻路线}}✓$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "定理抽取" "锚点核对" "复现门"
技术词 定理抽取 命中文件数=0    ::
技术词 锚点核对 命中文件数=0    ::
技术词 复现门   命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 定理抽取 | 0 | 0 | ✓（自造标签 ✓） |
| 锚点核对 | 0 | 0 | ✓（自造标签 ✓） |
| 复现门 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓
- **抽取源已归档 ✓✓**：`sources/GijswijtPolak-2025-arXiv2504.01932v2-EXTRACT-S2-full.txt`（31,316 B ✓）；`sources/GijswijtPolak-2025-arXiv2504.01932v2-EXTRACT-full-html2txt.txt`（168,069 B ✓）

## §6 边界（硬 ✓）

- **文献直读＋抽取** ✓（非计算 ✓；无数值实验 ✓）；**未上 SDP 求解** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **两处必记**：① 锚点为**界值**而非立方值（已核 ✓）；② **$n{=}10$ 之 SDP 不能供给 $q$ 上界**（本档 ★ ✓✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a{=}45$ 已排除 ✗（V290）；**不声称** ① 已死 ✗（仅记其在 $n{=}10$ 处之读数 ✓）
