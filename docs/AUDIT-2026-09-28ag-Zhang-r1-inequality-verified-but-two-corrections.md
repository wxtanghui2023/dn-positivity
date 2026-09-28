# AUDIT-2026-09-28ag — **Zhang $r{=}1$ 不等式已在 120-code 上核验 ✓，但两处须修正（系数写法 ＋ $Z'$）**

> **性质**：**审计（实测核验）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:40 ✓
> **唐先生令**：算 induced coefficient vectors 并做线性组合 ✓

**已查地图**：接续 `AUDIT-ab`（链实测）／`AUDIT-aa`（Zhang 系列）／`AUDIT-af`（Haas 2008）✓

D0: 本档对象 ＝ **档案已有**（$A_j(u)$／Zhang 不等式——无新数学对象 ✓）
D1: 0（产出＝**一条不等式核验 ＋ 两处修正 ＋ 一处层级读数** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ Zhang }r{=}1\ \text{不等式在 120-code 上\ \textbf{零违反}，最小值恰 }22\ (15\ \text{次达到}) \Longrightarrow \text{真且\ \textbf{紧}}}$$
$$\boxed{\text{② ✗ 系数写法须修正}:\ \text{正确为}\ \lambda=(m_1,m_1,1,1)=(5,5,1,1),\ \beta{=}22;\ \text{唐先生之 }(27,5,1,1)\ \text{为\ \textbf{弱化}}}}$$
$$\boxed{\text{③ ✗ }Z'\ (A_2{+}A_3\ge22,\ u\notin C)\ \textbf{为假}（788/904 违反）;\ \text{正确为}\ 5A_1{+}A_2{+}A_3\ge22\ (0\ \text{违反})}$$

## §1 ① 核验结果（**120-code 全量 ✓✓**）

$$\text{唐先生写法}\ \lambda=(27,5,1,1),\beta{=}22:\quad \textbf{零违反};\ \min = \mathbf{22}\ (\text{恰 }15\ \text{点达到}) \Longrightarrow \text{有效且紧}\ ✓$$
$$\text{样本}:\ u{=}0000000000\ (\notin C):\ (A_0,A_1,A_2,A_3)=(0,1,5,13)\Rightarrow LHS=23\ ✓;\quad u{=}0000000011\ (\in C):\ (1,0,5,18)\Rightarrow50\ ✓$$

## §2 ② 系数修正（**本档要点 ✓✓**）

$$\text{Zhang 原式（}r{=}1\text{）}:\ \sum_{i=0}^{r-2}(\cdots)+m_1\bigl(A_{r-1}(u)+A_r(u)\bigr)+A_{r+1}(u)+A_{r+2}(u)\ \ge\ m_0$$
$$\text{代 }r{=}1:\quad m_1\bigl(A_0(u)+A_1(u)\bigr)+A_2(u)+A_3(u)\ \ge\ m_0 \Longrightarrow \boxed{\lambda=(5,5,1,1),\ \beta=22}\ ✓$$
$$\text{唐先生写成 }(27,5,1,1)\ \text{——因}\ 27A_0+5A_1\ \ge\ 5A_0+5A_1\ \text{恒成立（}A_0\ge0\text{），\ \textbf{故为弱化}}}\ ✗$$
$$\textbf{后果（关键）}:\ \Sigma\lambda_j\binom{10}j = \begin{cases}5{+}50{+}45{+}120=\mathbf{220}=22\cdot10 & \text{正确读法}\\ 27{+}50{+}45{+}120=\mathbf{242}=22\cdot11 & \text{唐先生写法}\end{cases}$$
$$\therefore\ M\ \ge\ \frac{22\cdot1024}{220}=\mathbf{102.4}\Rightarrow\boxed{103}\ (\text{van Wee 级})\quad\text{vs}\quad \frac{22\cdot1024}{242}=\mathbf{93.09}\Rightarrow\boxed{94}\ (\text{球界级})$$

## §3 ③ $Z'$ 之修正（**✗✓**）

$$\text{唐先生 }Z':\ u\notin C\Rightarrow A_2(u)+A_3(u)\ge22.\quad\textbf{实测}: \text{违反 }\mathbf{788}/904\ \bigl(87\%\bigr)\ ✗✗$$
$$\text{成因}:\ u\notin C\ \text{时}\ A_0=0\ \text{但}\ A_1\ \textbf{未必为 }0\ (\text{覆盖条件仅给 }A_0{+}A_1\ge1);\ \text{故原式应读为}$$
$$\boxed{5A_1(u)+A_2(u)+A_3(u)\ \ge\ 22}\qquad\textbf{实测}: \text{违反 }\mathbf{0}/904\ ✓✓$$

## §4 层级读数（**本档最重要之战略结论 ✓✓**）

$$\therefore\ \boxed{\text{Zhang }r{=}1\ \text{不等式之\ \textbf{简单应用}（}\beta2^n/\Sigma\lambda_j\binom nj\text{）恰给 }\mathbf{103}\text{（van Wee 级）}}$$
$$\text{即}:\ \text{单条 Zhang 不等式}\ \textbf{不}直接给 }105\ \text{或 }107 \Longrightarrow \text{提升必来自\ \textbf{induced 不等式 ＋ 整数 rounding ＋ 非负线性组合}} ✓$$
$$\text{（与 Haas 2008 之结论一致}:\ \text{excess 族止于 }103;\ \text{故 }105/107\ \text{出自更高阶组合，而非单条不等式）}$$
$$\text{另}: \lambda{=}(5,5,1,1)\ \text{为球覆盖条件的加权重写（}\Sigma\lambda C{\cdot}=22(n{+}1)/11\cdot\ldots\text{）}\ \Longrightarrow \text{须 induced 才增信息}$$

## §5 下一步（**照唐先生 §11 ✓**）

$$\textbf{①}\ \text{取正确种子}\ Z=(5,5,1,1)_{22};\quad \textbf{②}\ \text{算 induced vectors}\ Z^{(i)}\ (i{=}1,2,3,\ldots)\ \text{（用}\ \alpha^k_{i,j}=\sum_t\binom kt\binom{n-k}{i-t},\ 2t=k{+}i{-}j\text{）};\quad \textbf{③}\ \text{整数 rounding};\ \textbf{④}\ \text{非负线性组合，使}\ \beta2^n/\Sigma\lambda_j\binom nj>106$$
$$\text{注}:\ \text{唐先生 }\S4\text{--}\S8\ \text{之 induced 系数计算（}270/50/8/3\text{）须以 }\lambda{=}(5,5,1,1)\ \text{为种子重算} ⚠️$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "Zhang式核验" "系数修正" "vanWee级"
技术词 Zhang式核验   命中文件数=0    ::
技术词 系数修正     命中文件数=0    ::
技术词 vanWee级    命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code 全量实测** ＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** Zhang／BÖW 公式 ✗；**不主张** $106$ 已排除 ✗（V290）
