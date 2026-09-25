已查地图：命中（`ASSET-TO-PROBLEM-MATCHING-v1` ＋ `RESEARCH-CONSTITUTION` AMEND-27）⟹ 空间 B 首刀 `B-LJCR-1`，不开新案
D0: 本档对象 = **账本修正（`B1-a` CLOSED ≠ `B1` CLOSED）** ＋ **`B1-b` 设计（改搜索策略，不改约束系统）** ＋ **`B-LJCR-1` 的 E4 结论：目标格被已发表定理判定为 `No`** ＋ 批量核查
D1: 0（审计＋核验型；结论为"非新结果/已知"）
[REVIEW]

# **账本修正 ＋ `B-LJCR-1` E4 结果**

## §0 账本修正（照先生 09:2x 的纠正）

```
$$\boxed{B1-a\ \textbf{CLOSED}\ \neq\ B1\ \textbf{CLOSED}}$$
$$\begin{array}{c|l}
\text{项}&\text{状态}\\\hline
B1-a&\boxed{\textbf{CLOSED}}\ (no\_lp\times4\ \text{seed}\times900s;\ \text{4 次 }UNKNOWN+incumbent=0;\ \text{无 proof})\\
B1-b&\boxed{\textbf{OPEN}，待设计}:\ \text{目标}=\textbf{改变搜索动力学}\ (\text{decision strategy／branching／phase／portfolio／结构化 warm-start})\\
B1-c&\text{后置}\ (\text{LNS／120-码结构扰动};\ \text{无 119 incumbent 时标准 LNS 无基础})\\
\end{array}$$
$$\textbf{依据（B1-a 的强读数）}:\ cf/br\approx0.0998\text{–}0.1003,\ prop/br\approx80.7\text{–}81.0\ (\text{4 seed 近乎重合})\ \Longrightarrow\ \boxed{\text{普通 seed 多样化已被榨干}}$$
$$\qquad \text{故 }B1\text{-}b\ \text{不应再做}\ \text{seed 55/66/77/88};\ \text{应改搜索策略};\ \text{但仍}\textbf{不改约束系统}\ (\Sigma x=119,\ \text{覆盖},\ x_0=1)$$
```

## §1 `B-LJCR-1`：E4 已穿透

```
$$\textbf{目标（已锁）}:\ \text{最小 }Open\ \text{格}=\boxed{DS(243,121,60,[3,9,9])}\ (\text{参数}=\text{skew Paley-Hadamard 型}:\ (4n-1,2n-1,n-1),\ n=61)$$
$$\textbf{数据表龄（E4）}:\ \text{数据仓 }\texttt{dmgordo/difference-sets}\ \text{最后推送}\ \mathbf{2026\text{-}04\text{-}24};\ \text{站点}\ 2026\text{-}09\text{-}03;\ \text{covering 库}\ \mathbf{2026\text{-}03\text{-}01}\ \text{冻结}$$
$$\textbf{同阶 7 群}:\ Z_{243}\ No\ (\text{Lander 4.38});\ Z_3{\times}Z_3{\times}Z_{27}\ No;\ \boxed{Z_3^5\ Yes\ (\text{Paley})};\ Z_3^3{\times}Z_9\ No;\ Z_3{\times}Z_{81}\ No;\ \boxed{Z_3{\times}Z_9{\times}Z_9\ Open};\ Z_9{\times}Z_{27}\ No\ (\text{Arasu–Ma 2001})$$
```

## §2 ⭐ 判定性定理（E4 命中）

```
$$\text{Schmidt 综述（Difference Sets: an Update）}\ \textbf{Theorem 4.4}\ \text{逐字（引 Chen–Xiang–Sehgal 1994）}:$$
$$\boxed{\text{“Let }G\text{ be an abelian }p\text{-group, }p\equiv3\bmod4,\ |G|=p^m,\ \exp(G)=p^s.\ \text{If }G\text{ admits a skew Paley-Hadamard difference set and }s\ge2,\ \text{then }s\le(m+1)/4.”}$$
$$\qquad \text{并附}:\ \text{“shows that Conjecture 4.3 is true for }m\le5”$$
$$\textbf{代入我们的格}:\ p=3,\ m=5,\ \exp(Z_3{\times}Z_9{\times}Z_9)=9\Rightarrow s=2;\quad s\ge2\Rightarrow s\le(5+1)/4=1.5\Rightarrow\boxed{\text{矛盾}}$$
$$\Longrightarrow\ \boxed{DS(243,121,60,[3,9,9])=\textbf{No}}\ (\text{该群不存在 skew Hadamard 差集});\ \text{且 }m=5\ \text{时}\textbf{只有初等阿贝尔群可行}$$
$$\qquad \text{内部一致性检查}:\ Z_3^5=Yes\ (\text{唯一 }s=1)\ ✓;\ v=27\ (m=3):\ Z_3{\times}Z_9=No\ ✓\ \text{与定理一致} ✓✓$$
```

## §3 交付物归类（照先生四类）

```
$$\boxed{\text{第 ④ 类}:\ \text{“严格证明该候选并非新结果／已知”}}\ ——\ \text{不是新构造（该群\textbf{不可能}有构造），而是}\textbf{数据库更正}:\ Open\to No\ (\text{依据 CXS 1994／Schmidt Thm 4.4})$$
$$\textbf{这也正是 }B\text{-}LJCR\text{-}1\ \text{要验证的事}:\ \text{AMEND-27 账本能区分"真数学产出"与"重新发现已知"}\ ——\ \text{本刀结论}=已知（但 DB 漏记）$$
$$\textbf{E4 的价值（实证）}:\ \text{若不做 E4，我们会去\textbf{构造一个可证不存在的东西}}\ \Longrightarrow\ \text{白烧算力（正是先生预判的风险）} ✓✓
```

## §4 批量核查（进行中）

```
$$\text{对 }\mathbf{102{,}719}\ \text{个 }Open\ \text{格，筛出}\ \text{skew-Paley-Hadamard 型}\ \text{且为 }\ p\text{-群}\ (p\equiv3\bmod4)\ \text{者，套用 Thm 4.4 判定}$$
$$\qquad \Longrightarrow\ \text{产出}\ \boxed{\text{DB 更正清单}}\ (\text{例如 }v=343=7^3:\ Z_7{\times}Z_{49}\ (s=2,m=3)\ \text{亦应判 }No)$$
$$\text{脚本}:\ \texttt{work/ljcr/cxs\_resolved.json}\ (\text{逐格：}v,k,\lambda,G,p,m,s)$$
【⛔ 纪律】 本档零"新机制"主张;\ 结论为审计级;\ \text{未声称新定理} ✓
【边界】 Thm 4.4 陈述取自 Schmidt 综述的抓取文本（OCR），\ \text{原文 CXS 1994 为 Springer 付费墙 ⟹ }\textbf{第二源待补};\ arXiv:1405.0045 摘要印证"该族存在 exponent bounds" ✓

## §附 【技术词回查】（**先跑后写**，逐字粘贴）

```
$ bash scripts/tech_word_check.sh "Chen Xiang Sehgal" "exponent bound" "skew Hadamard difference set" "数据库更正"
技术词 Chen Xiang Sehgal 命中文件数=0    ::
技术词 exponent bound   命中文件数=1    :: ./B-LJCR-1-E4-result-and-ledger-fix.md
技术词 skew Hadamard difference set 命中文件数=0    ::
技术词 数据库更正  命中文件数=1    :: ./B-LJCR-1-E4-result-and-ledger-fix.md
```
**三分类**：
- **本档新增（档案内首次出现）**：`Chen Xiang Sehgal`（0 档）｜`skew Hadamard difference set`（0 档）—— 为本档首次引入的文献/对象名
- **档案已有（引用，不列为提出）**：`exponent bound` 与 `数据库更正` 的唯一命中即本档自身 ⟹ 亦为首次出现，但**均为通用词**（不计新性）
- **通用词（不计）**：`exponent bound`、`数据库更正`

**⚠️ 新性边界（必须声明）**：本档的 `CXS 指数界`结论**不是数学新结果** —— 定理出自 Chen–Xiang–Sehgal 1994（经 Schmidt 综述 Thm 4.4 转述）；本档交付物属**第 ④ 类「证明该候选并非新结果／已知」**，即**数据库更正**（`Open → No`），**不得**表述为发现新定理。
