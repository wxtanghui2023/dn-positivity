已查地图：见 docs/TOPIC-INDEX.md（课题分档子档 · 本档为该课题总纲领）
D0: 本档对象 = 课题总纲领与行动方案（组织性）；非数学命题，不主张任何新值
D1: 0
ASSUMES: N/A (纲领档)

# CHARTER — **119 线（$K(10,1)$）**（空间 B）· 总纲领＋行动方案

## §1 目标
① **主目标**＝**复现 $K(10,1)\\ge107$**（等价：**排除 $M{=}106$**）；② 次目标＝改进上界 $120\\to119$（构造侧）。

## §2 证明链（**全链条，逐环节**）
| 环 | 内容 | 现状 |
|---|---|---|
| **L0** | 规范（覆盖码/集合覆盖 ILP） | 已知 ✓ |
| **L1** | 球界 94 | 已知 ✓ |
| **L2** | 上界 $\\le120$ | 已知 ✓（Fagioli；我方已复现构造） |
| **L3** | 96／97 | 已知 ✓ |
| **L4** | 103（van Wee 超量） | 已知 ✓（我方自导） |
| **L5** | 105（Zhang pair/triple） | 已知 ✓ |
| **L6** | 106（SDP-3 ＝ 105.2223） | 已知 ✓（我方复现） |
| **L7** | **107** | **待完成 ⏳** |
| **L8** | 上界 $120\\to119$ | **待完成 ⏳** |


## §2.7 **逻辑可杀预筛（Route Kill Test）**（唐先生 2026-10-01 16:42 令 ✓）

$$\boxed{\text{任何路线在\ \textbf{列为攻击点之前}，必须先通过三问；任一不过\ \Longrightarrow\ \textbf{不得列出}}（\text{或仅列"已剔除＋一行理由"}）}$$
$$\textbf{① 天花板问}：\text{该路线能达到的上限是否}\ >\ \text{目标？（}\text{对称性}/\text{松弛阶数}\text{ 常可先验算出）}$$
$$\textbf{② 对象问}：\text{它是否是\ \textbf{已知对象的改名/同一对象}？（如"权重法"与"分数覆盖数"对偶同物）}$$
$$\textbf{③ 量级问}：\text{其历史增益量级是否可能达标？（若需 }\sim8\times\text{ 于历史最强增益}\ \Longrightarrow\ \text{死}）$$
$$\text{配套纪律}：\text{复杂体系可试错，但\ \textbf{简单推导即知死路者不得浪费}；}\text{违者记为浪费（已犯多例 ✗）}$$


## §2.8 **已试判定前置**（唐先生 2026-10-01 16:47 令 ✓）

$$\boxed{\text{列表之前，必须先以\ \textbf{档案 grep}判定"该路线是否已试过"；已试者\ \textbf{一律不得列为攻击点}}}$$
$$\text{判定口径}：\text{命中档数}\ >\ 0\ \text{且存在\ \textbf{判定性档案}（判死/已穷尽/NO-GO/结果已得）}\ \Longrightarrow\ \textbf{已试} ✓$$
$$\text{每课题须明示}：\textbf{未试攻击点}＝\varnothing\ \text{或非空（若非空须列名并给出"未试"证据）}$$
$$\text{记教训}：\text{把已试路线重新包装为"存活点"＝\ 二次浪费 ✗（本日已犯）}$$

## §2.9 **价值评估前置**（唐先生 2026-10-01 16:56 令 ✓）

$$\boxed{\text{课题须先过}\ \textbf{价值评估}（V1 问题地位／V2 记录传播／V3 可验证性／V4 成本-收益／V5 竞争密度／V6 可发表性／V7 能力资产）\ \text{并给出"是否值得推进"裁定}}$$
$$\text{详见}\ \texttt{docs/VALUE-ASSESSMENT-2026-10-01-topics-worthiness.md}\ ✓$$


## §2.10 **命题级验证门**（唐先生 2026-10-02 10:03 令 ✓）

$$\boxed{\text{推导中用到的\ \textbf{每一个数学命题}，在\ \textbf{作为前提使用之前}，必须先附\ \textbf{机器检验}（脚本＋输出）；未验证者标 CONJECTURED，\textbf{不得作前提}}}$$
$$\text{三档状态}：\textbf{VERIFIED-SMALL}（\text{小规模穷举，反例}=0）｜\textbf{VERIFIED-EXACT}（\text{精确计算/证书}）｜\textbf{REFUTED}（\text{有反例}）；\quad \text{台账}＝\texttt{docs/PROPOSITIONS.tsv}$$
$$\text{硬要求}：\text{任何脚本\ \textbf{先写文件 → \texttt{python3 -m py_compile} → 最小样例自检 → 再跑}};\ \text{任何"保持某不变量"之构造，\textbf{先做反例搜索}}$$
$$\text{记教训}：\text{本日 }P\text{-001（"2-switch 保 }λ\text{"）为\ \textbf{100\% 错}（36/36），\text{十行穷举即可杀死}} \Longrightarrow \textbf{\text{"先理论推导"若不带反例检验，等于没推导}}$$

## §4 **逐环节：全部思路 × 可行性**

| 环 | 思路 | 可行性 |
|---|---|---|
| **L0** | a) 组合定义；b) 集合覆盖 ILP；c) 混合码 $K_{2,3}(b,t;R)$ | 皆**已知** ✓ |
| **L1** | a) 球界；b) 平均计数 | **已知** ✓ |
| **L2** | a) Fagioli 显式 120 词；b) 混合码替换（Östergård 1991：60 词混合→120）；c) 我方 CP-SAT 复现 | 皆**已知** ✓ |
| **L3** | a) Stanton–Kalbfleisch 1968；b) Cohen–Lobstein–Sloane 1986 | **已知** ✓ |
| **L4** | a) van Wee 超量法（原式取 `arXiv:2608.12595` equ(5)）；b) Struik 简化版；c) 我方自导重推 | 皆**已知** ✓ |
| **L5** | a) Zhang pair 不等式；b) Zhang–Lo triple；c) 我方向量重推 | **已知** ✓（>97 但 <107） |
| **L6** | a) 三阶 Parseval 松弛（Gijswijt–Polak `2504.01932`）；b) LP/Krawtchouk 复现；c) 高阶升阶？ | a,b **已知** ✓；**c 低-中 ⚠️**（须查是否仍属 Theorem A 天花板） |
| **L7** | a) BÖW 原公式（**不可得** ✗）；b) 混合码**新一般界**（非松弛）；c) 非松弛/整数性机制；d) 元素级 0/1 可实现性；e) 双向缺口（$W$ 下界＋$A_2(R)$ 上界）；f) 坐标式构造（**包络✗**）；g) 高阶 SDP；h) 同族第 8 家族（**七族皆≤103✗**）；i) 精确分类穷尽（**✗**）；j) 混合码参数扫描 | **b,c,e 中 ⚠️**；d 中低 ⚠️；g,j 低-中 ⚠️；a,f,h,i **低/已排除 ✗** |
| **L8** | a) 定向局部搜索（**六次过弱✗**）；b) 精确 SAT/ILP＋对称破缺；c) 代数/群构造；d) 120 码删词＋修补；e) 混合→二进制构造迁移；f) LNA/LNS（Marosi 2608.19872） | **b,c,d 中 ⚠️**；e,f 中低 ⚠️；a **低 ✗** |



## §2.8 **已试判定前置**（唐先生 2026-10-01 16:47 令 ✓）

$$\boxed{\text{列表之前，必须先以\ \textbf{档案 grep}判定"该路线是否已试过"；已试者\ \textbf{一律不得列为攻击点}}}$$
$$\text{判定口径}：\text{命中档数}\ >\ 0\ \text{且存在\ \textbf{判定性档案}（判死/已穷尽/NO-GO/结果已得）}\ \Longrightarrow\ \textbf{已试} ✓$$
$$\text{每课题须明示}：\textbf{未试攻击点}＝\varnothing\ \text{或非空（若非空须列名并给出"未试"证据）}$$
$$\text{记教训}：\text{把已试路线重新包装为"存活点"＝\ 二次浪费 ✗（本日已犯）}$$


## §2.9 **价值评估前置**（唐先生 2026-10-01 16:56 令 ✓）

$$\boxed{\text{课题须先过}\ \textbf{价值评估}（V1 问题地位／V2 记录传播／V3 可验证性／V4 成本-收益／V5 竞争密度／V6 可发表性／V7 能力资产）\ \text{并给出"是否值得推进"裁定}}$$
$$\text{详见}\ \texttt{docs/VALUE-ASSESSMENT-2026-10-01-topics-worthiness.md}\ ✓$$


## §2.10 **命题级验证门**（唐先生 2026-10-02 10:03 令 ✓）

$$\boxed{\text{推导中用到的\ \textbf{每一个数学命题}，在\ \textbf{作为前提使用之前}，必须先附\ \textbf{机器检验}（脚本＋输出）；未验证者标 CONJECTURED，\textbf{不得作前提}}}$$
$$\text{三档状态}：\textbf{VERIFIED-SMALL}（\text{小规模穷举，反例}=0）｜\textbf{VERIFIED-EXACT}（\text{精确计算/证书}）｜\textbf{REFUTED}（\text{有反例}）；\quad \text{台账}＝\texttt{docs/PROPOSITIONS.tsv}$$
$$\text{硬要求}：\text{任何脚本\ \textbf{先写文件 → \texttt{python3 -m py_compile} → 最小样例自检 → 再跑}};\ \text{任何"保持某不变量"之构造，\textbf{先做反例搜索}}$$
$$\text{记教训}：\text{本日 }P\text{-001（"2-switch 保 }λ\text{"）为\ \textbf{100\% 错}（36/36），\text{十行穷举即可杀死}} \Longrightarrow \textbf{\text{"先理论推导"若不带反例检验，等于没推导}}$$

## §4.5 **未试攻击点：$$\varnothing$$** ✗（原列三条**皆已试**）

| 原列 | 档案证据 | 裁定 |
|---|---|---|
| 非松弛/整数性机制（元素级 0/1） | **27 档**；一夜九层（计数/谱/投影/运输/矩/双核/同组/三核块）**全部无矛盾** ⟹ 该族**已饱和** | **已试** ✗ |
| 支撑/排列交叠结构 | `AUDIT-…-Fourier-divisibility-…-exhausted`：该对象＝**已穷尽之 T-Walsh 对象**，复现守卫**明文禁止第三次回潮** | **已试（已封）** ✗ |
| 上界 119 构造 | `ASSETS-REGISTRY`：SA/tabu **六次重启 best_unc 25–34** ⟹ 机制过弱 | **已试** ✗ |

$$\Longrightarrow\ \textbf{119 线：未试攻击点 }=\varnothing;\ \text{同上三类出路};\ \text{注：档案已判"119 侧唯一未闭合之合法碎片"＝\textbf{Recensorium 悬赏（受限族精确最小值＋穷尽证书）}}✓$$

## §5 行动方案 ＋ 纪律
$$\\textbf{S1}\\,\\text{钉住 BÖW 出处（A）};\\ \\textbf{S2}\\,\\text{试 F（唯一未饱和层）};\\ \\textbf{S3}\\,\\text{E 定向构造（时间盒）}$$
**纪律**：不得把 106 当"已证 107" ✗；`INFEASIBLE/UNKNOWN` 不作不存在证据；九层已饱和者**不得重走** ✗

## §6 文档存储

$$\\text{存储}：\\texttt{topics/119/CHARTER.md}\\ \\checkmark\\quad \\text{主档}：\\texttt{docs/MASTER-FAILURE-MAP-107-LINE.md}\\quad \\text{路线}：\\texttt{docs/ROUTE-FINGERPRINTS.tsv}\\quad \\text{假设}：\\texttt{docs/ASSUMPTIONS.tsv}$$
