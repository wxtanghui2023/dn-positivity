# AUDIT-2026-09-29e — **结论：单条线性不等式\ \textbf{不可能}给 $107$**（实测反例 ＋ 结构上限）

> **性质**：**结论性审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 10:0x ✓
> **唐先生令**：「自行推导」→「结论」✓

**已查地图**：接续 `AUDIT-29d`（(B) 死）／`29c`（(A) 死）／`29a`（上确界 103）✓

D0: 本档对象 ＝ **档案已有**（$A_j(u)$／线性不等式／LP--SDP 层级——无新数学对象 ✓）
D1: 0（产出＝**实测反例 ＋ 结构上限 ＋ 最终结论** ⚠️✓）

---

## §0 结论（先给，一句话）

$$\boxed{\text{「自行推导\ \textbf{一条}不等式」\ \textbf{不可能}给 }107;\ \text{上限}\ \le\mathbf{105.2223}<107}$$

## §1 实测：自然候选**全部为假**（**✓✓ 决定性反例**）

$$\text{生成 12 个随机贪心覆盖码（}\mathbb F_2^{10}\text{）：}M\in[144,152]$$
$$\textbf{实测}:\ \min_u\bigl(A_0(u)+A_1(u)+A_2(u)\bigr)\ =\ \mathbf{1}\ (\text{seed }0,5)\ \text{或}\ 2\ (\text{其余}10\ \text{个})$$
$$\therefore\ \boxed{\text{「}A_0+A_1+A_2\ge6\text{」（本来可给 }110\text{）\ \textbf{为假}}✗✗$$
$$\text{同理}:\ \min_u(A_1+A_2)=0\ \text{或}\ 1\ \Longrightarrow\ \text{「}A_1+A_2\ge\beta\text{」型亦\ \textbf{全假}}✗$$
$$\text{唯一真者}:\ \min_u(A_0+A_1)=\mathbf 1\ \Longrightarrow\ \text{仅\ \textbf{覆盖条件本身}（球界 }94\text{）}\ ✓$$
$$\text{读法}:\ \text{真实覆盖码中存在\ \textbf{极稀疏点}（2 球内仅 1 个码字）} \Longrightarrow \textbf{任何"局部密度"不等式都站不住}}$$

## §2 结构：单条线性不等式之上限（**✓✓ 本档核心**）

$$\text{任何单条有效不等式}\ \sum_j\lambda_jA_j(u)\ \ge\ \beta\ \text{给}\quad M\ \ge\ \frac{\beta\,2^n}{\sum_j\lambda_j\binom nj}$$
$$\text{而该界\ \textbf{恰为}覆盖 LP（level-2 松弛）之\ \textbf{对偶} \Longrightarrow \text{LP 最优} \le \text{SDP 最优}}$$
$$\text{Gijswijt--Polak 2025（level-3，已是最强）}:\quad \text{SDP}_{n=10,r=1}\ =\ \mathbf{105.2223}$$
$$\therefore\ \boxed{\text{任何单条线性不等式所给界}\ \le\ \text{LP}\ \le\ 105.2223\ <\ 107}✗✓$$
$$\text{（旁证}:\ \text{Zhang }r{=}1\ \text{单条}\ \to 102.4;\ \text{其 induced 全表}\ \to 102.4\ (11/11);\ \text{与 LP 级一致）}$$

## §3 三层路线之最终账（**收束 ✓✓**）

| 路线 | 判定 | 硬依据 |
|---|---|---|
| **(A)** pair 数上界 | **死** | 框架 ≡ 球界（`29c`：$25M{-}2310$） |
| **(B)** 高阶 SDP | **死** | 原作者：higher levels "difficult to compute"（`29d`） |
| **(C)** **单条线性不等式** | **死** | **本档：上限 $\le105.2223<107$；且自然候选实测全假** |
| **(D)** **integrality／非松弛论证** | **唯一存活** | 由上三条**反推**：$107$ 只能来自非松弛机制 |

$$\boxed{\text{⟹ 要 }107\text{，须\ \textbf{非松弛型（integrality）}论证 —— 这正是 Zhang 1991 的 rounding 与 BÖW 2004 之所在}}✓✓$$

## §4 给唐先生的直白结论

$$\textbf{①}\ \text{「自行推导一条不等式」\ \textbf{不可能}成功——\text{已验证其上限}}$$
$$\textbf{②}\ \text{这不是我的实现失败，而是\ \textbf{方法学定理}：}107>105.2223=\text{最强松弛}$$
$$\textbf{③}\ \text{因此 }107\ \text{必含\ \textbf{整数性/组合}步骤};\ \text{而该步骤的原文（Zhang 1991／BÖW 2004）\ \textbf{未得}}$$
$$\textbf{④}\ \text{唯一可自做者}:\ \text{自建\ \textbf{integrality 论证}（如"假设 }M{=}106\Rightarrow\text{结构 }\Rightarrow\bot\text{"），而非造不等式}}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "单条不等式上限" "稀疏点反例" "非松弛必要"
技术词 单条不等式上限  命中文件数=0    ::
技术词 稀疏点反例    命中文件数=0    ::
技术词 非松弛必要    命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **12 码实测 ＋ 结构论证** ＋ 资源前置/收尾检查（load 0.84／&#8594;低；Python 进程 1）✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）
