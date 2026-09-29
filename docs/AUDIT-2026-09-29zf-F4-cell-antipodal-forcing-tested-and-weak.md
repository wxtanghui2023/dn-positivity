# AUDIT-2026-09-29zf —— $F_4$-cell 分解（对极强迫）：**实测真但弱** ✗（第 9 条）

> **性质**：**审计＋实测**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 18:20 ✓
> **唐先生令**：按"最优构造所用坐标系"（$F_4\times F_2^7\times F_2$）调整资产后再测 ✓

**已查地图**：`CONNECTION-AUDIT`（断层＝整性压缩）／`AUDIT-29ze`（次线性）／证书档 ✓

D0: 本档对象 ＝ **档案已有**（混合码分解／对极结构—经典 ✓）
D1: 0（产出＝**一候选实测否证（类 2）** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 分解}:\ Q_{10}=F_4\times F_2^7\times F_2\ (4\cdot128\cdot2=1024);\ \text{cell}=F_2^8\ \text{之 256 个，各 4 点}}$$
$$\boxed{\text{② 新特征}:\ \text{cell 内码字 }(a,u)\ \text{只覆盖 3/4 点};\ \text{对极点 }(\bar a,u)\ \text{须由\ \textbf{相邻 cell} 覆盖}}$$
$$\boxed{\text{③ 实测}:\ \Sigma_u\delta_u\in[94,120]\ (\text{45 种 }F_4\text{-选择});\ \text{相邻容量}\approx8\times\#\text{码字}\ \Longrightarrow\ \textbf{松弛巨大}\ ✗}$$
$$\boxed{\text{④ 判定}:\ \text{类 2（真但弱）;\ 且一阶计数仍＝球界}\Longrightarrow\ \text{不立项}\ ✗}$$

## §1 分解（✓）

$$Q_{10}=F_4\times F_2^7\times F_2;\quad |F_4\times F_2^7\times F_2|=4\cdot128\cdot2=1024\ ✓$$
$$\text{cell }u=(y,z)\in F_2^8;\ \text{每 cell 4 点}\ \{(a,u):a\in F_4\}$$
$$\text{码字 }(a,u)\ \text{覆盖}\ (a',u)\iff d_{F_4}(a,a')\le1\Longrightarrow\ \text{覆盖 cell 内 3 点（自身＋2 邻），\textbf{不含对面}}✓$$

## §2 对极强迫（✓ 该分解独有）

$$\text{cell }u\ \text{内 }S_u=\{a\in F_4:(a,u)\in C\};\quad \delta_u:=\#\{\bar a: a\in S_u,\ \bar a\notin S_u\}$$
$$m_u{=}4\Rightarrow\delta{=}0;\quad m_u{=}2\ \text{对极对}\Rightarrow\delta{=}0;\quad m_u{=}1\Rightarrow\delta{=}1;\quad m_u{=}2\ \text{相邻}\Rightarrow\delta{=}2\ ✓$$
$$\therefore\ \Sigma\delta_u\ =\ \text{必须由相邻 cell 承担的覆盖需求}$$

## §3 实测（✗ 弱）

| $I$（$F_4$ 坐标） | $\Sigma\delta$ | $m$ 分布 |
|---|---|---|
| $(0,7)$ | $94$ | $\{0{:}161,\ 1{:}72,\ 2{:}21,\ 3{:}2\}$ |
| $(0,4)$ | $98$ | $\{0{:}163,\ 1{:}77,\ 2{:}6,\ 3{:}9,\ 4{:}1\}$ |
| $(5,6)$ | $120$（最大） | $\{0{:}142,\ 1{:}108,\ 2{:}6\}$ |

$$\text{需求}\ \Sigma\delta\in[94,120];\quad \text{容量}\ \approx8\times(\text{邻 cell 码字数})\ \gg\ \text{需求}\ ✗$$
$$\text{一阶：}\ \sum_u\sum_a\bigl[\text{cell 内}+\text{邻 cell}\bigr]=3M+8M=11M\ \ge\ 4\cdot256=1024\ \Longrightarrow\ \text{球界}\ ✗$$

## §4 判定（✓ 按 7 类）

$$\boxed{\text{类 2（正确但太弱）；松弛巨大 ⟹ 不能排除 }M{=}106\ ✗}$$
$$\therefore\ \text{第 9 条候选死；断层（整性压缩）未被跨过}\ ✗$$

## §5 边界（硬 ✓）

- **实测（45 种 $F_4$ 选择的 $\Sigma\delta$、$m$ 分布、一阶计数）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；本档仅**实测否证一候选** ✓
