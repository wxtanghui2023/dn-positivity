已查地图：命中（`TARGET-L9-q11-source-closure`／`TARGET-L9-five-items-answered`）⟹ 引用，不开新案
D0: 本档对象 = 入口 A 四件源齐备报告（`README §2` 全文／`lines.py`／`fullsets.py`／`run_q11_checks.sh`）＋ `A1`–`A4` 答案 ＋ `A5` 解锁
D1: 0 （[REVIEW] 轮次：取源，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **四件源齐备（入口 A · 取源阶段完成）**

## §0 ⭐ 决定性状态行（`run_q11_checks.sh` 头注，逐字）

```
"**The r=10 sweeps and the r=9 n=38 residue are annealing runs; they are reported as residue and are not re-decided here.**" ✓✓✓
⟹ **`r=9,n=38` 是 `residue`（annealing），不是穷尽判定** ✓ —— 与我方"措辞纪律"完全一致 ✓
```

## §1 `A1`：shear 的确切形式（`README §2` 末，逐字）

```
"**A shear `(v,u)\mapsto(v+K(u),u)` with `K` linear preserves the family, fixes `A` and changes `g` by a linear map, so `g` may be normalised to vanish on a basis of `W`; `\tau` is exactly the shear-invariant part of `g`.**" ✓✓
⟹ **是 gauge/shear（非 `V\oplus W` 的线性自同构）**；`K` 线性；**保持 `A`**；`g` 可**规范化在 `W` 的一组基上取零**；**`\tau` 正是 `g` 的 shear-不变量** ✓
【⟹ 群作用**分三层（本档纠正）】** `\mathrm{GL}(4,2)` 作用在 `V`（含 `A`、`B`）｜`\mathrm{GL}(5,2)` 作用在 `W`｜**shear `g\mapsto g+K(\cdot)`（保 `A`）** —— ⚠️ **不可先假定半直积形式**（照您纪律）✓
```

## §2 `A2`：`lines.py` 口径（对应数学定义）

```
点编码＝**非零字** `1..2^M-1`；线枚举＝`(a,b,c)`，`c=a\oplus b`，`c>b` ✓
`\tau(\ell)=g[a]\oplus g[b]\oplus g[c]`；`C[p]=\{\tau(\ell):p\in\ell\}` ✓
`colour\_ok=\forall u:\ B\subseteq C[u]`｜`sat\_ok=\{0\}\cup A\cup(A+A)=V`｜**`flat\_ok`＝`2^r` 平扫一致** ✓（两条互为独立校验）✓
附：**双线性检验**（`g` 二次 ⟹ `\tau` 双线性），与 `Lemma A` 对应 ✓
```

## §3 `A3`：`fullsets.py` 与 17 类（口径修正）

```
**【口径修正（本档）】** `sa_graph.c` 的 **`-k` ＝ `|B|`**（非 `|A\cup\{0\}|`）：`r=9` 的 `-k 8` ⟹ `|B|=8` ⟹ `n=15-8+31=38` ✓；`run_q11_checks.sh` 里 `-F 4 -M 5 -k 7` ⟹ `|B|=7` ⟹ `n=39`（**记录**）✓✓（两处自洽）
`fullsets.py` 处理的是 `sa_graph.c` 输出的 **`FULLSET` 行**：逐字注释 "when a **cost-0 configuration at `k=8` has no 1-saturating complement**" ⟹ **存在 `|B|=8` 的 `B` 使着色侧 cost-0 可解，但 `A=V\setminus(B\cup\{0\})` 非 1-saturating** ⟹ **fibre 0 永不覆盖** ✓✓
`gen_asets.c`：生成 **`\mathrm{GL}(4,2)`-归约的 `A` 列表**（`gen_asets.c 4 10` 等）✓ ⟹ **`\mathrm{GL}(4,2)` 作用在 `A` 上**（`B` 随之）✓
`r9_n38_classes.txt` 的 17 类：**`\mathrm{GL}(4,2)`-类，`A` 1-saturating 且 `|A|=7`（即 `|B|=8`）**，每类 `bestcost=14` ✓
```

## §4 `A4`：验证链（`run_q11_checks.sh`）

```
链：`(A,g)` →（`emit_H.py` 重建 `S` ＋ 重跑平扫，断言 `got=tot` 且 `\mathrm{rank}=F+M`）→ `H` →（`verify_H.c` 独立复验全部 `H_*.txt`）✓
`lines.py` 对 6 个已知解逐例**独立核对化归与平扫一致** ✓
`graph_search.c` 在 `r\le8` 做**穷尽**（`--strong`／`--alist`：`r=8` 的 `n=23,24,25` 穷尽、`n=26` 找到）✓；`sa_graph.c` 在 `r=6,8,9` 做 **annealing** ✓
⛔ **`r=9,n=38` 不走穷尽路径** —— 头注已自陈为 `residue` ✓✓
```

## §5 `A5` 解锁（下一轮写，仍不求解）

```
四件源**齐备** ⟹ `A5` 可写：$$\mathcal F^{(9,38)}=\bigcup_{i=1}^{17}\mathcal F_i$$
变量＝`A`-mask（17 类给 canonical rep）＋ `g:W\setminus\{0\}\to V`（`31` 个值，各 `\in\mathbb F_2^4`），**模 shear**（`g` 可规范化在 `W` 的基上取零 ⟹ **自由度降 `5\times4=20` 位**）✓
约束＝`\forall b\in B,\forall u:\ b\in C_u`（`248` 条 incidence，缺 `\leqslant0`）＋ `\{0\}\cup A\cup(A+A)=V` ✓
【⛔ 红线（本轮未碰）】 `r=10,n=49`｜`r=11` order `11/17/23`｜`q10` order-7｜族外搜索｜SAT 求解 ✓
【边界】 §0–§4 全部为**一手逐字/本机实读**；§1 三层群作用纠正、§5 规格草案为**本档自行推导**；未制造候选／未启动搜索／未碰 RH。
