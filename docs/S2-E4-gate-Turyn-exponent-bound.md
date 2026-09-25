已查地图：命中（`RESEARCH-CONSTITUTION` AMEND-28 §2/§3/§7 与 §8；`SPACE-B-INTAKE-v1.md` 种子 S2）
D0: 本档对象 = **S2 的 E4-0..4 闸门证据**（Turyn 指数界 → 一般差集 Open 格的批量核验）
D1: 0（K4 审计／核验型；**无**新定理、**无**新构造）
[REVIEW]

# **S2 闸门档：Turyn 指数界（一般差集）**

## §1 E4-0 语义闸（**三一致**）

```
$$\begin{array}{c|l|l}
\text{项}&\text{内容}&\text{判定}\\\hline
\text{数据源对象定义}&(\text{README 逐字})\ (v,k,\lambda)\text{-DS in a group }G:\ \text{每非零元素恰 }\lambda\text{ 次表示}&\text{一般差集}\\
\text{定理对象}&(\text{Thm 9.11 逐字})\ \text{abelian }G\text{ 上的 }(v,k,\lambda)\text{-DS}&\textbf{一致}\ ✓\\
\text{结论类型}&\text{违反必要条件}\Longrightarrow\text{该群\textbf{不存在}该参数差集} = \text{与 DB 的 }No\ \text{语义一致}&\textbf{一致}\ ✓\\
\end{array}$$
$$\Longrightarrow\ \boxed{E4\text{-}0=\textbf{PASS}}\ (\text{对象}=\text{问题}=\text{结论强度}\ \text{三者一致})$$
$$\textbf{对照}:\ \text{CXS 界仅约束 \textbf{skew} 子问题} \Longrightarrow \text{对本数据库\textbf{不适用}}（\text{见 ERRATUM 档}）$$
```

## §2 逐字定理（E4-2 证据）

**源①（主，含证明）** —— G. M. Trout, *Difference Sets in Abelian Groups and Their Generalizations*, MSc thesis, University of Delaware, Summer 2017（导师 **Qing Xiang**），**Theorem 9.11**：
> *“**Turyn’s Exponent Bound:** Let G be an abelian group which contains a (v,k,λ)-difference set D. Let p be a prime such that p | v and let P denote the Sylow p-subgroup of G. Suppose there exists a ∈ ℕ such that p^{2a} | n, and let U ≤ G such that U ∩ P = {1}. If p is self-conjugate modulo the exponent of G/U, then* $\exp(P)\le|U||P|/p^{a}$*.”*
（该论文注明 "some authors distinguish two versions of Turyn's exponent bound. The first is really a special case of the second"；证明按 Moore–Pollatsek 给出）

**源②（更强，但本族不适用）** —— 同论文 **Theorem 9.12（Schmidt 指数界）**：
> *“Let D be a (v,k,λ)-difference set in a group G. Suppose U ≤ G such that G/U is cyclic of order k. Then* $k\le\left(2^{s-1}F(k,n)/n\right)^{1/2}v$*.”*
```
$$\text{不适用原因}:\ \text{需 }G/U\ \text{循环阶 }k\Longrightarrow k\mid v;\quad \text{而本族 }k=(v-1)/2\ (\text{Hadamard 型})\ \text{或一般情形多不满足}\ k\mid v$$
```

**源③（机制确认）** —— B. Schmidt, *Difference Sets: an Update*（NTU）：自共轭 ⟹ 特征值退化为平凡解 $\varphi(D)=u\cdot(\text{单位根})$ ⟹ 必要条件的来源 ✓

## §3 适用性分析（**关键结构发现**）

```
$$\textbf{最强形式（取 }U=\{1\}\text{）}:\ \boxed{\exp(P)\le|P|/p^{a}}\ \Longleftrightarrow\ p^{s}\le p^{m_p-2a}\ \Longleftrightarrow\ s\le m_p-2a$$
$$\textbf{假设（必须全满足）}:\quad p\mid v;\quad \exists a\ge1:\ p^{2a}\mid n;\quad p\ \text{自共轭 mod}\ \exp(G)\ (\Longleftrightarrow\exists j:\ p^{j}\equiv-1\bmod m',\ m'=p\text{-自由部分})$$
$$\boxed{\text{Hadamard 型族（}k=2\lambda+1,\ v=4\lambda+3\text{）恒有 }p\nmid n}\ \Longrightarrow\ p^{2a}\mid n\ \text{不可能}\ \Longrightarrow\ \boxed{\text{Turyn 界对该族\textbf{完全不适用}}}$$
$$\qquad \Longrightarrow\ \boxed{\text{我们的 }243\ \text{格（及 CXS 批 74 格）\textbf{不受触及}，}\text{撤回状态维持}\ Open}\ ✓\ (\text{与 ERRATUM 一致})$$
```

## §4 批量结果（K4 审计产物）

```
$$\text{扫描}:\ 102{,}719\ \text{个 }Open\ \text{格（全参数型，非仅 Hadamard 型）};\quad \text{其中 Hadamard 型 }=12{,}925$$
$$\text{Turyn 假设成立（存在 }p\mid v,\ p^{2a}\mid n\ (a\ge1),\ \text{自共轭）} = 13{,}780\ \text{例}$$
$$\Longrightarrow\ \boxed{\textbf{138}\ \text{格违反 Turyn 界}\ \Longrightarrow\ \text{判 }No}\ (\text{逐格数据}:\ \texttt{work/ljcr/turyn\_resolved.json};\ \text{脚本}:\ \texttt{turyn\_batch.py})$$
$$\text{样例（手工复核）}:\ DS(16896,6976,2880,[2,16,528]):\ n=4096=2^{12},\ a=6,\ |P|=2^{9},\ \exp(P)=2^{4};\ \text{界}=2^{9-6}=2^{3}<2^{4}\ \Longrightarrow\ \text{违反}\ ✓$$
```

## §5 **决定性自校验（E4-4）**

```
$$\text{把同一定理套到数据库\textbf{已知存在构造的 }Yes\ \text{格}}:\ 31{,}388\ \text{格};\quad \text{假设成立 }940\ \text{例};\quad \boxed{\text{违反}=\mathbf{0}}\ ✓✓$$
$$\qquad \Longrightarrow\ \text{我的转录与实现与"数据库自身正例体系"完全相容};\ \text{这是抓出 skew/general 越界的同一套自检法} ✓$$
```

## §6 交付物归类（照四类）

```
$$\boxed{\text{第 ④ 类}:\ \text{数据库状态纠正（}Open\to No\text{）}_{138\ \text{格}}};\quad \text{依据}=\text{Turyn 1965 的经典指数界}$$
$$\textbf{不是}:\ \text{新定理}／\text{新构造}／\text{新计算证书};\quad \textbf{是}:\ \text{K4 表格核验（AMEND-26 能力类）} ✓$$
$$\textbf{方法论价值}:\ \text{这是\textbf{语义更正之后}的正确续做} —— \text{先用 CXS 越界被撤，今以正确工具族重做并通过 }E4\text{-}0..4\ ✓$$
```

## §7 边界（诚实）

```
(i)\ \text{逐字陈述取自 }\mathbf{Trout\ 2017}\ \text{学位论文（单一二手源，含证明）};\ \textbf{Turyn 1965 原文为扫描件（无文本层）} \Longrightarrow \text{未能核对原始铅字}
(ii)\ \text{Schmidt 界（Thm 9.12）形式更强但因 }k\mid v\ \text{不成立而\textbf{未使用}}
(iii)\ \text{138 格为\textbf{机器批量}结果};\ \text{虽经 }Yes\ \text{格 0 违反校验，仍应做\textbf{第二套独立实现}复核（待办）}
(iv)\ \textbf{不声称}数据库"错误"（其 }Open\ \text{语义=未见构造）;\ \text{只主张"按 Turyn 界应为 }No\text{"}
(v)\ \text{结论依赖定理假设的逐项验证};\ \text{自共轭判定用 }\exp(G)=\mathrm{lcm}(\text{不变量因子})\ \text{精确计算} ✓
```

## §附 【技术词回查】（**先跑后写**，逐字粘贴）

```
$ bash scripts/tech_word_check.sh "Turyn" "指数界" "一般差集" "exp(P)"
技术词 Turyn            命中文件数=8    :: ./LJCR-B1-batch-E4-audit-and-cell243-RESOLVED.md ./SPACE-B-INTAKE-v1.md ./C292-four-deep-audit-receipts-and-C290-errata.md
技术词 指数界        命中文件数=5    :: ./B-LJCR-1-E4-result-and-ledger-fix.md ./SPACE-B-INTAKE-v1.md ./RESEARCH-CONSTITUTION.md
技术词 一般差集     命中文件数=3    :: ./SPACE-B-INTAKE-v1.md ./RESEARCH-CONSTITUTION.md ./ERRATUM-LJCR-B1-semantics-skew-vs-general.md
技术词 exp(P)           命中文件数=0    ::
```
**三分类**：
- **本档新增（档案内首次出现）**：`exp(P)`（0 档）
- **档案已有（引用，不列为提出）**：`Turyn`（8 档，本线前档已用）、`指数界`（5 档）、`一般差集`（3 档，ERRATUM 档已建立该术语）
- **通用词（不计）**：`Turyn`（人名）、`指数界`
- **⚠️ 新性边界**：本档**无**任何新性主张；交付物为**第 ④ 类**（数据库状态纠正）。
