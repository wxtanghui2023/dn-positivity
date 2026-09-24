已查地图：命中（`C3-modular-coverage-range-and-free-next-stop`／`C3-problem16-17-verbatim-parameter-space`）⟹ 引用，不开新案
D0: 本档对象 = **免费源 `arXiv:math/0601502`（`RGPF-II`）抓取成功**＋其参数级内容提取＋语义定位（属"有限成员存在"档，**不移除 `D`**）
D1: 0 （[REVIEW] 轮次：取证，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`RGPF-II`（免费源）抓取与参数级提取**

## §1 下载（技术记要）

```
`arXiv` **直连可用**：`https://arxiv.org/pdf/math/0601502` ⟹ **`312277` 字节，`30` 页** ✓（`export.arxiv.org` 与 `ghfast.top` 本次均失败）
存：`sources/monson-schulte-RGPF-II-math0601502.pdf` ✓
⚠️ **操作失误（已记）**：首个 `for` 循环无 `break`，把好文件**覆盖**成 `14` 字节垃圾 ⟹ **重下并逐项验证**（`bytes`/`pages`/`head`）✓
```

## §2 认篇与定位

```
`B. Monson` ＆ `E. Schulte`，**"Reflection Groups and Polytopes over Finite Fields, II"**（`arXiv:math/0601502v1`，`2006-01`；＝前档引用 `[9]`）✓✓
**该文正是"以素模 `p` 讨论 \textbf{全部} locally toroidal 4-polytopes `P(G_p)`"的那一篇** ✓✓
```

## §3 参数级内容（提取）

```
**【哪些 `G` 给 locally toroidal】** 逐字："If `[k,l]` is Euclidean, then `G=[4,4,3]`、`[6,3,3]` or `[6,3,4]`，and `P` is locally toroidal."（★ **注意：此处未含 `[3,6,3]`** —— 后者在 §7 单独处理）✓✓
**【出现的具体类】** `\{\{6,3\}_{(3,0)},\{3,3\}\}`；`\{\{6,3\}_{(3,0)},\{3,4\}\}`；`\{\{6,3\}_{(3,0)},\{3,6\}_{(3,0)}\}`（★ 两个**不同** polytope 同群阶 `1944`）✓；`\{\{6,3\}_{(1,1)},\{3,6\}_{(1,1)}\}`；`\{\{3,3\},\{3,6\}_{(3,0)}\}`；**`\{\{3,6\}_{(1,1)},\{6,3\}_{(3,0)}\}`** ✓✓；`\{\{3,6\}_{(1,1)},\{6,4\}_4\}`；`\{\{3,6\}_{(3,0)},\{6,4\}_4\}` ✓
**【群阶样本】** `\{6,3\}_{(3,0)}` 型：`2592`；`\{3,6\}_{(1,1)}`／`\{6,3\}_{(3,0)}` 组合：`3888`（或 `432`，视 vertex-figure 为 `(3,0)` 或 `(1,1)`）✓
**【特征参数】** 素模下反复出现 **`(1,1)`、`(3,0)`、`(p,0)`** ⟹ 与 `1992`/书的自对偶有限集 `(1,1),(2,0),(3,0)` **同族特征** ✓✓
```

## §4 ⚠️ 语义定位（承前档更正，必须重申）

```
本文给出的是**具体有限 polytope（构造/商）**，**不是**"universal polytope 有限" ⟹ $$\boxed{\text{本文内容归入"该类存在有限成员"档}\ \Longrightarrow\ \textbf{不移除}\ D}$$ ✓✓
【⟹ 对 `D` 的影响】**零**（只证明该类非空）⟹ **`D` 仍需"已决 universal 情形清单"来定** ✓
```

## §5 状态与下一步

```
$$\begin{array}{c|c}
\text{项目}&\text{状态}\\
\hline
\text{参数空间}&\checkmark\\
\text{三分（存在/群/有限）}&\checkmark\\
\text{modular 覆盖范围（含素模与一般 }d)&\checkmark\\
\text{free 源 `RGPF-II` 抓取}&\checkmark\\
\text{已决 universal 情形清单（`\{11E,H\}`/`1992`）&\textbf{OPEN}\\
\text{最小未决 }(s_*,t_*,u_*,v_*)&\textbf{OPEN}\\
H\ \text{固定维？}\ H>0\iff\text{finite？}&\textbf{OPEN}\\
\end{array}$$ ✓
【唯一缺口不变】**`1992 CMH` 或书 `§11E/H` 的"已决 universal 情形"清单** ⟹ 得**补集** ⟹ `D` ⟹ 最小未决 ⟹ 两硬问 ✓
【可试项（下轮，低成本）】**本 PDF 内可能另有汇总表**（`p10` 提到"eleven possibly distinct basic systems"）⟹ 可再扫一次找汇总清单 ✓
【⛔ 纪律】**不计算、不实现**；`C2` 暂停 ✓
【边界】 §3 为**本地 `pymupdf` 提取的逐字/近逐字片段**（原文已归档）；§4 语义定位为**本档推理**；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 reflection groups over finite fields 命中文件数=0    :: 
```
