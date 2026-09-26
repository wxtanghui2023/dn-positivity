已查地图：见 `docs/FACE-2026-09-26-two-face-occupancy-audit.md` 首行（三档已覆盖 ✓）。本档为 **FACE 线封口**（唐先生 2026-09-26 21:38 裁定 ✓）。
D0: 本档对象 = FACE 线状态与保留资产（既有对象）
D1: 0（产出为封口标签、两资产登记与一处更正）

# FACE-2026-09-26 · 封口：STRUCTURAL REFINEMENT / NO NEW COLLISION

## §0 状态（唐先生标签 ✓）

```
$$\boxed{\textbf{FACE-2026-09-26 — STRUCTURAL REFINEMENT / NO NEW COLLISION}}\ ✓$$
$$\qquad\textbf{不是} CLOSED ✗（局部结构确有新增 ✓）；\ \textbf{不是} P3 ✗（无 collision ✓）$$
$$
$$
```

## §1 已覆盖部分（直接封口 ✓）

```
$$\#\{\text{2-面}\}=\binom{10}{2}2^{8}=\mathbf{11520}\ ✓;\quad 46080=\text{点-面关联数}\ ✗\ (\text{非 face 数})$$
$$\texttt{EXCESS-2026-09-25}:\ \text{face--ball double count 已做}\ \Longrightarrow\ c\ge57\ \text{仅此}\ ⟹\ \text{相对 }c\ge94\ \text{与文献无 leverage}\ ✗$$
$$\texttt{BUDGET-2026-09-26}:\ Q_k\subseteq C\Rightarrow E\ge k2^k\ ✓;\ k=2\ \text{已排除整个 2-面}\ \Longrightarrow\ q_F=4\ \text{无需另立引理}\ ✓$$
$$\Longrightarrow\ \textbf{换成 2-面语言本身不算新 mechanism}\ ✗$$
$$
$$
```

## §2 保留资产（两条 ✓）

```
$$\boxed{\textbf{(A)}\ d(c,c')=1\ \leftrightarrow\ \mathbf 9\ \text{个公共面};\quad d(c,c')=2\ \leftrightarrow\ \mathbf 1\ \text{个}}\ ✓✓\ (\text{一般 }n:\ n{-}1\ /\ 1\ ✓)$$
$$\qquad\Longrightarrow\ \sum_F\binom{q_F}{2}=9A_1+A_2\ ✓\ \text{（incidence fingerprint ✓）}$$
$$\boxed{\textbf{(B)}\ q_F=3\ \Longrightarrow\ \text{该面唯一"中间"角为全局唯一 }b{=}3\ \text{点}\ z}\ ✓\ \text{（故分支 A 有 }q_F\le2\ \forall F\ ✓）$$
$$
$$
```

## §3 ⚠️ 更正（唐稿第 3 条的顶点归属）＋ 一处量界

```
$$\textbf{唐稿}:\ \text{"2-面有 3 个码字顶点}\Rightarrow\textbf{唯一的非码字顶点}\ z\ \text{与三者皆距 1}\Rightarrow b(z)\ge3"\ ✗$$
$$\textbf{实情}:\ \text{4 个角中取 3 个＝L 形}\ ✓;\ \text{第 4 角（非码字）与其中\textbf{两}角距 1、与对角距 2}\ ✗\ (\text{非"皆距 1"})$$
$$\qquad\text{真正 }b\ge3\ \text{的是}\ \textbf{中间的码字角}\ (\text{与另两码字皆距 1}\ ✓)\ ⟹\ \text{该角}=z\ ⟹\ z\in C\ \text{（分支 B）}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{结论方向不变}\ ✓\ (\text{分支 A}\ q_F\le2\ ✓)\ \text{—— 仅顶点归属更正 ✓}$$
$$\textbf{量界更正}:\ \text{"}2A_2\le N_2\text{"}\ \text{应写作}\ \mathbf{2A_2-3\le N_2}\ ✓\ (\text{因 }z\ \text{贡献 3 个 pair 而只作 1 个点}\ ✓;\ \text{且 }2A_2-3=283-2A_1\ \text{为恒等式}\ ✓)$$
$$
$$
```

## §4 为何无 P3 collision（闭合链 ✓）

```
$$q_F\le2\Longrightarrow\binom{q_F}{2}=\mathbf 1_{\{q_F=2\}}\ \Longrightarrow\ \#\{F:q_F=2\}=9A_1+A_2\ ✓$$
$$\text{距离-2 对的 2 个中点皆 }b{=}2\ ⟹\ \text{同一条既有恒等式}\ 2A_2-3=283-2A_1\ ✓$$
$$\Longrightarrow\ \textbf{face 语言}\to(A_1,A_2)\to\text{既有局部数据}\ ⟹\ \textbf{无新独立量、无第二条互斥约束}\ ✗$$
$$
$$
```

## §5 停止条件与下一步（唐先生指令 ✓）

```
$$\textbf{停止}:\ \text{不再在 2-面语言上堆 counting identity}\ ✗$$
$$\textbf{下一步判据}:\ \text{只寻找\textbf{真正独立于 }(A_1,A_2)\ \text{的局部结构量}}\ ✓\ \text{—— 否则只是换坐标系重述}\ ⚠️$$
$$\qquad\textbf{本线证据（12 次汇合）}:\ \text{线性求和／二次符号／双重计数／packing 方向／行闭合／Haas×}Q_1／\text{中点 load／层限制／}L_4\ \text{图／相邻耦合／孤立码字／2-面占据}}$$
$$\qquad\qquad\Longrightarrow\ \text{全部落到 }(A_1,A_2,\text{profile})\ \text{或其仿射函数}\ ⚠️\ \Longrightarrow\ \text{独立量必须在\textbf{类型}上不同（非二阶 incidence）}\ ✓$$
$$
$$
```

## §6 边界（诚实标注）

- §2 资产 (A)(B) 为**本线新增** ✓（已分别登记：`A-FACE-MULT-1` ✓；q_F=3 引理见本档 §2 ✓）；**(B) 与 STAR3 的"$b\ge3\Rightarrow$ 唯一特殊点"机制高度同源** ⚠️ ⟹ **不宣称全新 mechanism** ✓（唐先生要求 ✓）
- §3 更正为**本档结论** ✓（顶点归属 ＋ $2A_2-3$ 式 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张 2-面语言无用 ✗

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 FACE 线封口标签 命中文件数=1    :: ./FACE-CLOSURE-2026-09-26-structural-refinement.md 
技术词 q_F=3 引理登记 命中文件数=0    ::
```
- **本档新增**：FACE 线封口标签、$q_F=3$ 引理登记（见上方命中数）
- **档案已有（引用，不列为提出）**：9:1 多重度（A-FACE-MULT-1）、面数 11520、子立方预算、STAR3 同源机制、$2A_2-3=283-2A_1$
