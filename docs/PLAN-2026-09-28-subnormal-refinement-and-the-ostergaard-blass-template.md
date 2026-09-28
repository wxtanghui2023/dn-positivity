# PLAN-2026-09-28 — **文献链审计 ＋ 新三段式候选链（subnormal → refinement → LP）＋ 三处校准**

> **性质**：**计划/审计**（非研究轮）——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:33 ✓

**已查地图**：承 `AUDIT-…b/c/d/e` ＋ C-541/545/546/547（三族门检）✓

D0: 本档对象 ＝ **计划/审计**（无新数学对象 ✗）
D1: 0（产出＝文献链定位 ＋ 候选链 ＋ 三处校准 ⚠️）

---

## §0 文献链结论（**唐先生 20:33 审计 ✓**）

$$\text{global relaxation chain（成熟）}:\ \text{sphere}\to\text{excess/congruence}\to\text{linear ineq}\to\text{weighted covering}\to\text{subspace+LP}\to\text{ILP}\to\text{SDP}$$
$$\boxed{119\ \text{恰落在该链\ \textbf{未触及} 之位置}}\ ✓$$
$$\boxed{K_2(10,1)\ \text{仍记录为}\ 107\le K_2(10,1)\le120\ \Longrightarrow\ 119\ \text{为\ \textbf{合法开放目标}}\ ✓}$$

## §1 ★新三段式候选链（**本档登记 ✓**）

$$\boxed{C\ \overset{\text{subnormal}}{\longrightarrow}\ (C_0,C_1)\ \overset{\text{subspace refinement}}{\longrightarrow}\ \text{finite local states}\ \overset{\text{discharging/LP}}{\longrightarrow}\ \text{118 infeasibility}}$$

**与我们旧路之别** ✓：引入 **$C$-dependent partition ＋ finite-state refinement**，而非继续研究固定 Best 码 $I$ ✓

**模板（历史 precedent ✓）**：$K(9,1){=}62$（Östergård–Blåss 2001）**非**靠神奇 inequality，而是
$$\text{subspace distribution}\to\text{refinement}\to\text{inequivalent cases}\to\text{LP}\to\text{dimension }0$$

## §2 优先级表（**照唐先生 ✓**）

| 候选 | 文献基础 | $C$-依赖 | 119 leverage | 判断 |
|---|---|---|---|---|
| Haas／Plagne | 极强 | ✓ | 低 | **关闭** |
| excess／congruence | 极强 | ✓ | 低 | **关闭** |
| SDP | 最新 | ✓ | 低 | **关闭** |
| private coverage | 强 | ✓ | 已证退化 | **KILL** |
| fixed Best-code geometry | 强 | **✗** | $0$ | **KILL** |
| generic subnormality | 强 | ✓ | 未知 | **审计** |
| **subnormal ＋ refinement** | 强 | ✓ | **中高** | **重点 ★** |
| **subspace distribution ＋ LP** | $n{=}9$ 先例 | ✓ | **高** | **重点 ★** |
| ILP dual certificate | 成熟工具 | ✓ | 中高 | 第二重点 |
| discharging | 图论成熟 | ✓ | 中高 | 探索 |
| pure census | 可做 | ✓ | 低 | 最后 |

## §3 ⚠️ 三处校准（**本档实测 ✓，须先钉死**）

### (A) subnormal 划分对 $(|C_0|,|C_1|)$ 之约束 **无改进** ✗

$$\text{覆盖两半}:512\le10a+b,\ 512\le10b+a\ \text{（}a{+}b{=}K\text{）}\ \Longrightarrow\ 11K\ge1024\ \Longrightarrow\ K\ge93.09$$
（实测 $K{=}135$：四坐标皆 $10a{+}b,10b{+}a\in\{738,747\}\ge512$ ✓ ⟹ 与 `AUDIT-d` 一致，**无改进**）

### (B) ★ "subspace distribution ＋ LP" 在 $n{=}10$ **就是** Haas 型 ✗

$$\text{固定 }k\ \text{之\ \textbf{单次} subspace-distribution LP}\ =\ \text{Haas 型}\ \Longrightarrow\ \text{C-546 已算}:n{=}10\ \text{主项}\max{=}94.4\ \text{（已封 ✓）}$$
$$\therefore\ \boxed{\text{新意\ \textbf{必在"迭代 refinement"}（refine until dim 0），非单次 LP}}\ ✓✓$$

### (C) 规模对比（状态数爆炸风险）

| $n$ | $|Q|$ | 球覆盖下界 | 目标 | 目标/下界 |
|---|---|---|---|---|
| $9$ | $512$ | $\lceil512/10\rceil{=}52$ | $62$ | $1.19$ |
| $10$ | $1024$ | $\lceil1024/11\rceil{=}94$ | $119$ | $\mathbf{1.27}$ |

$$\Longrightarrow\ n{=}10\ \text{之\ \textbf{相对 gap 更大}（1.27>1.19）};\ \text{但绝对状态数 }1024\ \text{仍小} \Longrightarrow \text{可行性须知实测} ⚠️$$

## §4 关键风险（**第一步**）

$$\boxed{\text{最大风险}:\ \text{能否找到\ \textbf{比 generic subnormality 更强}、且真依赖 }|C|\le118\ \text{之 refinement rule？}}$$
$$\text{若成立} \Longrightarrow n{=}10\ \text{之有限性反成\ \textbf{优势}}\ ✓$$

**诚实标注** ⚠️：generic subnormality 已由 `AUDIT-d` 判**无改进**（校准 A）；故有效者必为**其 refinement 版本**，尚待构造 ✗

## §5 具体首测提案（**可执行，待唐先生批准**）

$$\textbf{Test-1}:\ \text{取 }n{=}10\ \text{之一维划分（}k{=}1\text{）与二维（}k{=}2\text{），枚举 coset 上之 codeword distribution 型；}$$
$$\qquad\text{执行\ \textbf{一轮} refinement（剔除可由上一层 LP 排除之型），比较所得 }K\ \text{下界是否 }>94.4$$
$$\textbf{判据}:\ \text{若单轮 refinement 已 }>94.4 \Longrightarrow \text{迭代路线\ \textbf{值得全量投入}};\ \text{否则须先解决 §4 之 refinement rule ✗}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "迭代refinement" "跨层候选链" "状态数爆炸"
技术词 迭代refinement  命中文件数=0    ::
技术词 跨层候选链     命中文件数=0    ::
技术词 状态数爆炸     命中文件数=0    ::
```

## §7 边界（硬 ✓）

- 文献审计（唐先生提供）＋ 有限复算 ＋ 既有档引证 ✓；**无新数学** ✗；**不加 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §5 为**提案**，未执行 ✗；**不主张**该路线必成功 ⚠️
