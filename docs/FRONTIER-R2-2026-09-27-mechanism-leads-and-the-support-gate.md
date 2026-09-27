已查地图：已跑 scripts/prework_map_check.sh support 机制 前沿检索 Boolean quadric supercode ⟹ 执行自 `NONNEG-2026-09-27`（判死 ✓）＋ 唐先生 2026-09-27 09:32 ✓；本档为**三层判停 ＋ AMEND-35 ＋ 首轮机制检索**。
D0: 本档对象 = 三层结论、SUPPORT-VISIBILITY GATE、机制线索（检索对象）
D1: 1（新增：**AMEND-35 门槛** ✓；**三条机制线索** ✓ 附带检索原文 ✓）

# FRONTIER-R2-2026-09-27 · 机制线索与支持门槛

## §0 三层判停结论（唐先生 09:32 ✓）

```
$$\textbf{Layer 1（已证死机制 ✓）}:\quad \text{lattice＋box}\ \to\ f\ge0\ \to\ \text{低阶／自然统计量}\ ✗$$
$$\qquad n=4:\ \exists f\notin\{0,1\}^{16}\ \text{with}\ 1\le b\le3\ \text{——且\textbf{非稀有}（2720/7860 ✓）};\ \text{7 坐标（}\Sigma f,\Sigma f^2,\Sigma b,\Sigma b^2,\#\{b{=}3\},\mathrm{supp},\mathrm{cut}\text{）\textbf{全不分离}}\ ✗$$
$$\qquad\boxed{\text{强陈述}:\ \text{任何只依赖这些低阶统计坐标的证明，}\textbf{不可能识别 }f\in\{0,1\}}\ ✓✓\ \text{（强于"试了 7 个没成功" ✓）}$$
$$
$$

$$\textbf{Layer 2（119 真实缺口 ✓）}:\quad \boxed{\text{moment information}\ \not\Rightarrow\ \text{support information}}\ ✓$$
$$\qquad\text{真正 P1 障碍}:\ \text{找一种机制，把 }f=2\ \text{式\textbf{质量集中}排除掉 —— 即利用 support／global representation}\ ✓$$
$$
$$

$$\textbf{Layer 3（检索方向反转 ✓）}:\quad \text{不再搜"covering-code invariant"}\ ✗;\ \text{改搜}\ \boxed{\text{别人如何把\textbf{局部 multiplicity 约束}提升为\textbf{global support／representation 约束}}}\ ✓$$
$$\qquad\text{五类候选}:\ \text{① Fourier／character 表征};\ \text{② association scheme／Delsarte 的非线性增强};\ \text{③ switching／分类／同构};\ \text{④ set-system／超图（11-集 incidence）};\ \text{⑤ exact-cover／near-cover 刚性（excess 的拓扑／连通／支撑 ✓）}$$
$$
$$
```

---

## §1 AMEND-35 · SUPPORT-VISIBILITY GATE（唐先生 09:32 立 ✓）

```
$$\boxed{\text{候选必须解释}:\ \textbf{"为什么它能看到 support，而 moment／local machinery 看不到？"}}\ ✓$$
$$\qquad\text{解释不了}\ \Longrightarrow\ \textbf{DROP}\ ✗\ \text{（本线屡次教训：moment／local 族已证不分离 ✓）}$$
$$
$$
```

---

## §2 文献信号（用户 09:32 提供 ＋ 本档检索 ✓）

```
$$\text{(a) 经典下界路线集中于 covering excess／局部计数／线性不等式系统（Haas 型 ✓）}\ \Longrightarrow\ \text{继续在自然 scalar ＋ local counting 内挖＝\textbf{范式内增量}}\ ⚠️\ \text{（支持本档判定 ✓）}$$
$$\text{(b) 记录有达到 }1023/1024\ \text{的 }119\text{-covering（用户引 Science Atlantic 会议册 ✓）}\ \Longrightarrow\ \text{近失结构已知}\ ⚠️\ \textbf{未复核} ✗$$
$$
$$
```

---

## §3 首轮机制检索（三条线索，附原文命中 ✓）

```
$$\textbf{(M-1) Boolean quadric polytope ／ 提升 ＋ cut 不等式}\ ✓\ \text{（Padberg 型 ✓）}$$
$$\qquad\text{命中}:\ \text{"A simultaneous lifting strategy for identifying new classes of facets for the BQP"（ScienceDirect ✓）};\ \text{"The boolean quadric polytope: Some characteristics, facets and relatives"（Padberg, Springer ✓）};\ \text{"The Bipartite BQP"（SIAM／SFU ✓，含 Padberg cut 不等式 }-u(S)-v(E(S))+v(S{:}T)-v(E(T))\le0\ ✓)$$
$$\qquad\textbf{机制}:\ \text{提升变量 }y_{uv}=f(u)f(v)\ \text{＋ facet\/cut 族} \Longrightarrow\ \textbf{成对支持可见}\ ✓\ \text{（\textbf{结构性不同于}线性 moment ✗）}$$
$$
$$

$$\textbf{(M-2) Multicovering 界 ← 线性不等式 ＋ \textbf{supercode}}\ ✓\ \text{（Klapper 等 ✓）}$$
$$\qquad\text{命中}:\ \text{"Improved Multicovering Bounds from Linear Inequalities and Supercodes"（uky.edu ✓）};\ \text{"Lower bounds on }t[n,k]\ \text{from linear inequalities"（Zhang--Lo ✓）};\ \text{Sloane "Further Results on the Covering Radius of Codes"（线性不等式节 ✓）}$$
$$\qquad\textbf{待查}:\ \text{supercode 机制的具体形态（是否属"局部→全局"型 ✓）}\ ⚠️$$
$$
$$

$$\textbf{(M-3) 常权元组的 invariant set 分类 ⟹ covering scheme 界}\ ✓\ \text{（2026 新 ✓）}$$
$$\qquad\text{命中}:\ \text{"A classification of invariant sets of constant-weight tuples and ... new upper bounds on covering scheme numbers"（Springer, Cryptogr.\ Commun.\ ✓）}$$
$$\qquad\textbf{机制}:\ \text{分类型（classification／invariant set ✓）}\ ⚠️\ \text{是否命中 support 待判 ✓}$$
$$
$$
```

---

## §4 Gate 预判与下一步（P0–P5 ✓）

```
$$\begin{array}{c|c|c|c}
\text{线索} & \text{能否解释"看得到 support"} & \text{可测性} & \text{初步判定}\\
\hline
\text{(M-1) BQP 提升＋cut} & \text{是 ✓（成对支持显式入变量 ✓）} & \textbf{可直接测}:\ \text{其 cut 族能否分离 }n=4\ \text{两族} ✓✓ & \textbf{首选} ✓\\
\text{(M-2) supercode} & \text{待查 ⚠️} & \text{需读原文} & \text{次选} ⚠️\\
\text{(M-3) invariant 分类} & \text{待查 ⚠️} & \text{需读原文} & \text{次选} ⚠️\\
\end{array}$$
$$\textbf{下一刀（本档建议 ✓）}:\ \text{对 (M-1) 做}\ \textbf{P0＋gate 实测}:\ \text{把 }n=4\ \text{的 }7860\ \text{个非负解提升到 }(f,y=f\otimes f)\ \text{空间，检查经典 cut 族是否\textbf{分离} Boolean／非 Boolean} ✓$$
$$\qquad\text{若分离}\ \Longrightarrow\ \text{首个"通过 SUPPORT-VISIBILITY GATE 且实测有效"的机制 ✓✓};\ \text{若不分离}\ \Longrightarrow\ \text{该机制亦 DROP ✗（并记为强负结果 ✓）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §0–§1 为**纪律登记** ✓；§2(b) 为**未复核的用户引文** ⚠️（明确标注 ✓）
- §3 为**检索命中原文** ✓（标题／来源照录 ✓）；**未**读全文 ✗
- §4 的判定为**预判** ⚠️（(M-1) 的可测性最高 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；未跑求解器 ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 SUPPORT-VISIBILITY GATE 命中文件数=1    :: ./FRONTIER-R2-2026-09-27-mechanism-leads-and-the-support-gate.md 
技术词 机制线索     命中文件数=5    :: ./PROTOCOL-R6-support-ceiling.md ./p49-g274iia1-material.md ./FRONTIER-R2-2026-09-27-mechanism-leads-and-the-support-gate.md
```
- **本档新增**：`SUPPORT-VISIBILITY GATE`（1 档 ✓）、`三层判停结论`（内部标签 ✓）
- **档案已有（引用，不列为提出）**：`机制线索` —— 命中 **5 档** ⚠️（含 `PROTOCOL-R6-support-ceiling.md`、`p49-g274iia1-material.md` 等）⟹ 该词为既有术语 ✓，本档仅**沿用** ✓（**不**列为新命名 ✓）
- 📌 附带发现：档案中已有 `PROTOCOL-R6-support-ceiling.md`（**support ceiling** 协议 ✓）⟹ 与 AMEND-35 主题相邻，**下一步须先读该档**以免重复 ✓（属 PRE-WORK 纪律 ✓）
- **档案已有（引用，不列为提出）**：格＋盒、区分量扫描、GAPTHEOREM 诊断
