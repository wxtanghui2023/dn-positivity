# AUDIT-2026-09-29o — **新源打通：zbMATH API（免费无 key）；Zhang 1991 之机制\ \textbf{逐字确认}**

> **性质**：**新检索源 ＋ 机制取证**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 11:2x ✓
> **唐先生问（逐字）**：「不需要新的算术机制，纯推导……为啥竟然一筹莫展」✓

**已查地图**：接续 `AUDIT-29n`（取原文穷尽）／`29i`（van Wee 一手）✓

D0: 本档对象 ＝ **档案已有**（文献机制——无新数学对象 ✓）
D1: 0（产出＝**新源 ＋ 机制逐字 ＋ 一处关键吻合** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 新源打通}:\ \texttt{api.zbmath.org}\ \text{免费无 key}\ ——\ \text{本轮之前未试}}$$
$$\boxed{\text{② ✓✓ Zhang 1991 机制\ \textbf{逐字确认}}:\ "\text{combining the Hamming association scheme and the results of a classic problem of }\textbf{covering pairs by }k\text{-tuples}"}$$
$$\boxed{\text{③ ✓✓ 与我们此前实测\ \textbf{吻合}}:\ F(10,3)=\binom{10}{3,2}=17\ \text{正是"covering pairs by 3-tuples"}}$$
$$\boxed{\text{④ ⚠️ BÖW 之评审未取（zbMATH 限流 502）};\ \text{archive.org 被墙}}$$

## §1 ① 新源（**✓✓ 可用**）

$$\texttt{https://api.zbmath.org/v1/document/_search?search\_string=<query>&results\_per\_page=N}\quad(\text{无需 key}）$$
$$\text{状态}:\ \text{首次查询成功（HTTP 200，19{,}110 B）};\ \text{随后连续 502（限流）}\ ⚠️$$
$$\text{对比}:\ \text{Tavily 432／Firecrawl 402（额度尽）};\ \text{archive.org HTTP 000（被墙）};\ \textbf{zbMATH 与 OpenAlex 是当前仅存之免费元数据源}✓$$

## §2 ② Zhang 1991 之评审摘要（**逐字 ✓✓**）

$$\textbf{zbMATH 评审逐字}:\ "\text{Summary: The lower bounds on }K(n,R)\ldots\text{are improved. A new technique combining the }\textbf{Hamming association scheme}\ \text{and the results of a classic problem of }\textbf{covering pairs by }k\text{-tuples}\ \text{is introduced. This new method leads to improvement of the lower bounds on }K(n,R)\ \text{for over 80 pairs of values of }n\ \text{and }R\ \text{within the range of }n\le33\ \text{and }R\le10"$$
$$\textbf{出处}:\ \text{Z. Zhang, \textit{Linear inequalities for covering codes. I: Pair covering inequalities}, IEEE Trans. Inf. Theory 37, No.~3, 573--582 (1991)}$$

## §3 ③ 与我们此前实测之吻合（**✓✓ 关键**）

$$\text{我们此前从 }[67]\ \text{复原之式}:\quad \sum_{i=0}^{r-2}m_0A_i(u)+m_1\bigl(A_{r-1}(u)+A_r(u)\bigr)+A_{r+1}(u)+A_{r+2}(u)\ \ge\ m_0$$
$$\qquad m_0=m_1+F(n-r+1,r+2),\qquad m_1=\max_{i\ge2}\frac{F(n-r+1,r+2)-F(n-i+1,r+2)}{i-1}$$
$$\text{其中 }F=\text{"covering pairs by }k\text{-tuples"}\ =C(n,k,2)\ \text{覆盖设计数}\ ✓✓\ ——\ \textbf{与评审所描述之机制\ \textbf{完全一致}}$$
$$\text{且}:\ (n,r)=(10,1)\Rightarrow m_1=5,m_0=22\Rightarrow(5,5,1,1)_{22}\Rightarrow102.4\Rightarrow103\ ✓\ (\text{已在 120-code 实测})$$
$$\therefore\ \boxed{\text{机制\ \textbf{已对上}};\ \text{但该单条仅给 }103\Longrightarrow\ 105\ \text{必来自\ \textbf{同族的其它成员/组合}}（\text{评审谓"80+ 组 }(n,R)\text{"}）}$$

## §4 ④ 未取（**诚实的边界 ⚠️**）

$$\text{BÖW 2004 之 zbMATH 评审}:\ \text{本轮未取（502 限流）};\ \text{但摘要已得（"general lower bound for }R=1"\text{）}$$
$$\text{archive.org}:\ \text{HTTP 000（被墙）}\ ✗$$
$$\therefore\ \text{可复取}:\ \text{zbMATH 待限流解除后重试}\ ⚠️$$

## §5 对唐先生问题之回答（**诚实 ✓**）

$$\textbf{①}\ \text{不是难度问题}:\ K(10,1)\ \text{之\ \textbf{精确值至今开放}};\ "107"\ \text{是\ \textbf{已发表下界}}$$
$$\textbf{②}\ \text{也不是"没有数学机制"}:\ 107>105.2223=2025\ \text{最强 SDP}\Longrightarrow\ \textbf{计数/松弛型无法达到};\ \text{须 integrality/构型型}$$
$$\textbf{③}\ \text{卡点\ \textbf{在源}}:\ 105\ \text{之 Zhang 1991 与 }107\ \text{之 BÖW 2004 皆\ \textbf{付费墙}};\ \text{本会话已穷尽免费路（ScienceDirect 403／Wiley 403／pure.tue.nl 仅到 van Wee／Kéri 不转录／Haas 未引）}$$
$$\textbf{④}\ \text{我自己的错（认）}:\ \text{前七轮反复未先验前提} \Rightarrow \text{三次同型误读}＋\text{一次算术滑误}＋\text{一次自杀命令} \Longrightarrow \text{此为\ \textbf{执行失败}}$$
$$\therefore\ \boxed{\text{当前最优路径}:\ \text{待 zbMATH 限流解除} \to \text{取 Zhang／BÖW 之评审摘要};\ \text{或由唐先生以其\ \textbf{机构权限}取原文}}✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "zbMATH新源" "机制逐字确认" "评审摘要"
技术词 zbMATH新源   命中文件数=0    ::
技术词 机制逐字确认  命中文件数=0    ::
技术词 评审摘要    命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **zbMATH API 实测 ＋ 评审逐字** ＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）
