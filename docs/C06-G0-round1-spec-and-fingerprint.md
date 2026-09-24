已查地图：命中（`Mt07-CLOSURE-no-usable-cell` ＋ `CANDIDATE-CENSUS-v1` §9）⟹ `C06-G0` 第一轮，不开新案
D0: 本档对象 = **`C06` 原始 spec（逐字）** ＋ **该行不含 `(q,n,d)` 的确认** ＋ **G0-A 格池（6 项）** ＋ **G0-B/C 指纹预审（含 5 处文献）** ＋ **G0-D 新量问题** ＋ 本轮判定与唯一下一步
D1: 0（审计＋选格型，无数学推导）
[REVIEW]

# **`C06-G0` 第一轮：spec 与指纹预审**

## §0 `C06` 原始 spec（逐字，来自本仓 census）

```
$$\texttt{F5}\ |\ \texttt{C06}\ |\ \textbf{固定 }n\ \textbf{下最优码非同构个数}\ |\ P_4\ |\ \texttt{EV}$$
$$\qquad \text{（Batch-2 归入 }P_4=\{C06,C07,C09\}\text{；Round A 判 "}G1*/A0?"\text{）}$$
$$\boxed{\text{该行}\textbf{不含任何具体 }(q,n,d)}$$ ✓✓ \Longrightarrow\ \text{G0-A 必须由我方构造格池（与 }Mt07\ \text{同型）}$$
$$\text{先生上一轮已授权只开 G0；本档即 G0 第一轮（\textbf{零计算}）}$$
```

## §1 G0-A 格池（6 项）＋ G0-B/C 指纹预审

```
$$\begin{array}{c|l|l|l}
\#&\text{格}&\text{当前记录（抽取级）}&\text{指纹预审}\\\hline
C_a&\text{1-perfect 二元，}n=15& \boxed{5983}\ \text{个不等价（Östergård–Pottonen 2009 全分类）} & \boxed{\text{HARVESTED}}\ \text{（已全分类）}\\
C_b&\text{1-perfect 二元，}n=31& \text{计数开放；}\textbf{"no nontrivial upper bound is known"}\ \text{（AJC 枚举文）} & \text{开放，但}\textbf{渐近陈述}\（非有限格）\\
C_c&\text{等距最优码（equidistant）}& \text{MDPI Mathematics 10(5):740 (2022) 用 QPlus 枚举二/三元若干参数，给出 }\#\ \text{表} & \boxed{\text{HARVESTED（多参数）}}\\
C_d&\text{线性 }[n,k,d]_2\ \text{分类}& \text{Kurz 等：}[n,k,3]_2\ (n\le16\text{)、}[n,k,3]_2(n\le18\text{)、even}[\le19,k,4]_2\ \text{等计数全表} & \text{非线性读排除（本项目只看非线性）}\\
C_e&\text{近完美/准完美码}& \text{仅近完美已全知（Lindström 1977）；准完美计数无系统表} & \text{须核（可能有格）}\\
C_f&A_3(n,d)\ \text{缺口的非线性格}& \text{Brouwer 三元表大量上下界（如 }n{=}7,d{=}3:\ 99\!\sim\!111\text{）} & \text{缺口属"值未知"而非"计数未知"}\\
\end{array}$$ ✓✓
```

## §2 G0-D：新量问题（C06 能否留下来的核心）

```
$$\text{先生口径}:\ \boxed{\#\{\text{inequivalent optimal codes}\}\ \text{本身}\neq\text{新结果}}$$
$$\qquad \text{否则}\ \text{“我们重枚举出 17 个，论文已枚举 17 个”}\Rightarrow\ \textbf{立即 ARCHIVE}$$ ✓
$$\text{须存在结构量}\ \Phi(C):\ C\ \text{optimal}\Rightarrow\Phi(C)\in S,\ \text{且}\ \Phi\ \text{能区分现有分类未区分的对象}$$ ⚠️
$$\text{本轮扫描结论}:\ \text{现有已收割区（}C_a,C_c\text{）}\ \text{恰恰已把“分类＋计数”做完（如 5983 含 rank/kernel 维度分布表）}\Longrightarrow\ \text{留给 }\Phi\ \text{的缝隙窄}$$ ⚠️
```

## §3 ⭐ 本轮判定

```
$$\boxed{\text{C06-G0 第一轮结论}:\ \text{已核的有限格}\ (C_a,C_c)\ \textbf{均已被收割};\ \text{唯一明确开放项}\ (C_b)\ \text{是}\textbf{渐近陈述（非有限格）}}$$ ⚠️
$$\qquad \text{未核清}:C_e\ (\text{准完美码计数}),\ C_f\ (\text{三元缺口格的非线性读});\ \text{二者须再查一轮}$$ ✓
$$\textbf{按先生止损逻辑}:\ \text{若下一轮 }C_e/C_f\ \text{亦被覆盖}\Longrightarrow\ \textbf{不再从 Zone-A/B 续挑},\ \text{回完整候选表重做“独立问题 × 新量 × 可证明性”筛选}$$ ✓✓
```

## §4 唯一下一步

```
$$\boxed{\text{核查 }C_e\ \text{与 }C_f\ \text{两格}:\ (i)\ \text{准完美/近完美码的“不等价计数”是否已有系统表};\ (ii)\ \text{Brouwer 三元/四元表中“值已定但计数未列”的格是否存在}}$$
$$\qquad \text{工具}:\ \text{Brouwer 表（}\texttt{aeb.win.tue.nl/codes/}\text{）、Grassl 表、codetables.de；本轮只用检索，不下载大表}$$
【⛔ 纪律】 本轮**零数学计算**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 全部证据为**检索抽取级**；`5983` 与 `MDPI 2022` 的细节未逐字核验 ✓

## §附 【技术词回查】（补录）
```
技术词 fingerprint pre-audit 命中文件数=0    :: 
技术词 inequivalent count 命中文件数=0    :: 
```
