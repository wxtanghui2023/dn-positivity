# AUDIT-2026-09-28o — **$P_{-2}$ Truth-Location Audit：$K_2(10,1)$ 之公开状态（权威源直取）**

> **性质**：**审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:14 ✓
> **唐先生令**：**暂停 119 certificate**；做 $P_{-2}$ 真值定位审计；建 $107..120$ 证据表 ✓

**已查地图**：接续 `AUDIT-n`（certificate START）／C-427（107–120）／C-541（OEIS）✓ ｜ **Tavily 432 ⟹ 切 Firecrawl ✓**

D0: 本档对象 ＝ **档案已有**（$K_2(10,1)$／Kéri 表——无新数学对象 ✓）
D1: 0（产出＝**权威源审计 ＋ 两处档案修正** ⚠️）

---

## §0 审计结论（先给）

$$\boxed{\text{① 区间 }[107,120]\ \textbf{经权威源确认仍成立};\quad \text{② }n{=}10\ \textbf{明确 OPEN};\quad \text{③ 存在\ \textbf{活跃公开悬赏} 正打此格}}$$
$$\boxed{\text{④ ★对"为何 119"之回答}:\ 119\ \textbf{不是唯一被授权目标};\ \text{授权目标}＝\text{"严格beat }120"\ \text{或\ "抬高 }107"}$$

## §1 权威源（三处直取 ✓）

### (甲) OEIS A000983（直取 text 格式 ✓）

```
%S A000983 1,2,2,4,7,12,16,32,62
%C A000983 The next term a(10) is in the range 107-120. - Andrey Zabolotskiy, Sep 01 2016
%I A000983 M0329 N0124 #87 May 02 2026 09:22:11
%D A000983 R. Bertolo, P. R. J. Östergård, W. D. Weakley, An updated table of
          binary/ternary mixed covering codes, J. Combin. Designs 12 (2004)
```

$$\Longrightarrow\ \boxed{\textbf{序列止于 }n{=}9\ (\text{末项 }62);\ a(10)\ \textbf{不在 OEIS}}\ ✓\ \text{（**修正 C-427**：107–120 仅 2016 年之注释）}$$
$$\Longrightarrow\ \text{条目\ \textbf{末次编辑 2026-05-02}\ 仍无 }a(10) \Longrightarrow \textbf{截至 2026 年 5 月仍未定}\ ✓✓$$

### (乙) arXiv:2203.16901（Wu；Discrete Math 347(2), 2024）逐字

> "It is **still an open problem** to determine the domination number $\gamma(Q_n)$ for $n\ge10$ and $n\ne2^k,2^k-1$."

$$\Longrightarrow\ \boxed{n{=}10\ \textbf{明确 OPEN}}\ ✓;\ \text{其新界}\ \gamma(Q_n)\ge\frac{(n-2)2^n}{n^2-2n-2}\ \textbf{仅对 }n\ \text{为 6 之倍数成立} \Longrightarrow \textbf{n{=}10 不适用} ⚠️$$

### (丙) ★ Kéri 表（经 Recensorium 悬赏页逐字引用）

$$\textbf{n=10 R=1:}\quad \mathbf{107\ \ldots\ 120}\quad\text{（左＝最佳已发表下界，右＝最佳已发表上界）}$$
$$\text{同表另列 }n{=}10..16,R{=}1..3\ \text{共 13 格};\ \text{并逐字}:\ "\text{K(9,1)=62 is settled exactly and is not listed}"\ ✓$$

## §2 ★★ 活跃公开悬赏（**本档最重要发现 ✓✓**）

$$\text{Recensorium：}\textbf{"Shrink a binary covering code on a shipped parameter list"}\quad £175;\ \text{Active Aug 12 2026 → Aug 12 2027};\ \text{已 1 条提交}✓$$
$$\textbf{完成要求（逐字）}:\ \text{"a peer-reviewed paper that, for at least one pair }(n,R)\ \text{on the list, \textbf{strictly improves a published bound on }K(n,R)}"$$
$$\textbf{评分（逐字要点）}:\ \text{FULL}＝\text{①严格小于已发表上界之构造}\ \textbf{或}\ \text{②抬高已发表下界之证明}\ \textbf{或}\ \text{③确定 }K(n,R)\ \text{精确值}$$
$$\qquad\text{PARTIAL}＝\text{具名受限族（线性、给定自同构群）之精确最小值且穷举证};\quad \textbf{逐字}:\ "\textbf{Closing a route is a result}"\ ✓$$
$$\qquad\textbf{SCORES NOTHING}:\ "\text{a code whose size merely lies inside the published interval without beating its upper end}"$$

## §3 ★ 对唐先生"为何 119"之回答（**本档核心 ✓✓**）

$$\textbf{(1)}\ \text{授权目标}＝\textbf{any strict improvement}:\ \text{构造 }<120\ \text{者，或证下界 }>107\ \text{者}\ ✓$$
$$\textbf{(2)}\ 119\ \text{之特殊性}:\ \text{其为 }120\ \text{前最后一个整数};\ \text{证 }\ge119\ \Longrightarrow\ \text{区间缩至 }\{119,120\}\ \text{（强结果 ✓）}$$
$$\textbf{(3)}\ ⚠️\ \textbf{但}:\ \text{证 }\ge115\ \text{或 }\ge108\ \text{同样 FULL};\ \text{故 }119\ \textbf{非唯一目标} \Longrightarrow \textbf{唐先生之质疑成立}\ ✓✓$$
$$\textbf{(4)}\ ⚠️\ \textbf{且两个任务相异}:\ \text{"构造 119"\ (构造问题)} \ne\ \text{"证 }\ge119"\ (下界问题)}$$

## §4 ⚠️ 一处档案修正（**必录**）

$$\text{档案旧表述}:\ "\ K(10,1)\ge120\ \Longleftrightarrow\ \text{排除 119-覆盖}\ "\quad \textbf{不精确} ✗$$
$$\text{正确}:\ \text{排除 119-覆盖}\ \Longrightarrow\ K\ne119 \Longrightarrow\ K\le118\ \textbf{或}\ K\ge120\ (\text{非 }K\ge120\ \text{单独})$$
$$\text{（}\because\ \text{若 }k\ \text{码存在则 }k{+}1\ \text{码存在（加点）}\ ✓\text{）};\quad \text{欲得 }K\ge120\ \textbf{须排除一切 }|C|\le119 ✓$$

## §5 唐先生另一纠正之确认（**$N{=}9$ 不可外推 ✓✓**）

$$\frac{K_2(9,1)}{2^9}=\frac{62}{512}\approx0.1211 \Longrightarrow \text{密度外推 }1024\times0.1211\approx\mathbf{124}\ \textbf{＞已证上界 }120 ✗\ \text{（自相矛盾）}$$
$$\text{球面倍率}:\ n{=}9:\ 62/51.2\approx1.211;\quad n{=}10:\ 119/93.09\approx1.278\ \text{或}\ 120/93.09\approx1.289 \Longrightarrow \textbf{无延续规律}\ ✓$$

## §6 证据表（$107..120$）

| $k$ | 地位 |
|---|---|
| $107$ | 最佳已发表**下界**（Kéri 表；源 2004 BÖW） |
| $108..118$ | **未知**（无构造、无排除） |
| $119$ | **未知** |
| $120$ | 最佳已发表**上界**（Östergård 1991 构造） |

$$\boxed{\text{14 个整数字无\ \textbf{任何}一个被数据排除};\ 119\ \text{与 }108\ \text{等地位相同（皆未定）}}\ ✓$$

## §7 建议（**待唐先生定 ✓**）

$$\text{① 119 certificate\ \textbf{暂停}\ (照令 ✓);\quad \text{② 目标重定义}:\ \text{真值定位 → 目标选择 → }P_1}$$
$$\text{③ 关键仍未被回答者}:\ \textbf{"为什么相信真值接近 119？"}\ \text{—— 本档证明}:\ \text{现有公开数据\ \textbf{不支持} 该信念}\ ⚠️$$
$$\text{④ 候选行动（未做）}:\ (\text{i})\ \text{小规模构造搜索（beat }120\text{）};\ (\text{ii})\ \text{受限族精确最小值（悬赏 PARTIAL 认可）};\ (\text{iii})\ \text{停止本线}$$

## §8 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "真值定位审计" "活跃悬赏" "上界侧构造"
技术词 真值定位审计  命中文件数=0    ::
技术词 活跃悬赏    命中文件数=0    ::
技术词 上界侧构造   命中文件数=0    ::
```

## §9 边界（硬 ✓）

- **权威源直取**（OEIS text／arXiv 摘要／悬赏页）＋ 档案引证 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- 外部内容**未受信任** ⚠️（悬赏页为第三方）；本档**只作状态记录**，**不主张**任何新数学 ✗
