已查地图：命中（`TARGET-L9-q11-dir-probe`／`TARGET-L9-five-items-answered`）⟹ 引用，不开新案
D0: 本档对象 = 入口 A **取源闭包**：q11 族定义／line-colouring 化归／17 类／`14` 的精确对象（一手逐字）
D1: 0 （[REVIEW] 轮次：取源，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`q11` 取源闭包（入口 A · A1–A4 达成）**

## §0 源（本地）

```
源：`~/.openclaw/workspace/github/maths-main.zip` → 解包至 `~/.openclaw/workspace/maths-src/maths-main/` ✓
`problems/covering/compute/q11/` 共 19 文件：`README.md`(9654)／`r9_n38_classes.txt`(994)／`fullsets_r9_k8.txt`／`fullsets.py`／`lines.py`／`emit_H.py`／`run_q11_checks.sh`／`sa_graph.c`／`graph_search.c`／`gen_asets.c`／`verify_graph.py`／`verify_H.c`／`H_r{4,6,7,8,9,10,11}_n{5,13,19,26,39,54,86}_fibered.txt` ✓
```

## §1 ⭐ 族定义（`README.md` §1，逐字）

```
`\mathbb F_2^r=V\oplus W`，`\dim V=F`（fibre），`\dim W=M`（base），`r=F+M` ✓
取 `A\subseteq V\setminus\{0\}`、`g:W\setminus\{0\}\to V`：$$S=\{(v,0):v\in A\}\cup\{(g(u),u):u\in W\setminus\{0\}\},\qquad n=|A|+2^M-1$$
覆盖条件按 fibre 拆成**恰好两条**：**(i) fibre `0`**：`\{0\}\cup A\cup(A+A)=V` ⟹ **`A` 在 `V` 中 1-saturating**（故 `|A|\ge\ell_2(F,2)`）；**(ii) fibre `u\ne0`**：$$B+g(u)\subseteq D_u,\quad B:=V\setminus(A\cup\{0\}),\ D_u:=\{g(w)+g(w+u):w\notin\{0,u\}\}$$ ✓✓
**长度公式** $$n=2^F-1-|B|+2^M-1$$ ⟹ **`n` 随 `|B|` 递减** ⟹ **全部问题＝`|B|` 能做多大** ✓✓
```

## §2 ⭐ line-colouring 化归（`README.md` §2，逐字）

```
`\{w,w+u\}` 与点 `u` 张同一平面 ⟹ 同一条 `\mathrm{PG}(M-1,2)` 的**线** ✓
$$g(w)+g(w+u)=\tau(\ell)+g(u),\qquad \tau(\ell):=g(a)+g(b)+g(a+b)\ (\ell=\{a,b,a+b\})$$
⟹ `\tau` 是 `\mathrm{PG}(M-1,2)` 的 `\frac{(2^M-1)(2^{M-1}-1)}{3}` 条线到 `V` 的**着色**（＝`g` 的**对称 2-cocycle**，在线内三对点上为常数）✓✓
令 `C_u=\{\tau(\ell):\ell\ni u\}`，fibre 条件化为 $$\boxed{B\subseteq C_u\ \text{对每个点 }u}$$ ⟺ **每个色类 `L_b=\tau^{-1}(b)`（`b\in B`）是一组"覆盖每个点"的线，且各类互不相交** ✓✓
```

## §3 ⭐⭐ 17 类与 `14` 的精确对象（`r9_n38_classes.txt` 逐字）

```
【头注逐字】"`r=9,n=38`: the **17 `\mathrm{GL}(4,2)`-classes of 1-saturating kernel blocks with `|A|=7`**，and the annealing floor reached on each (`sa_graph.c -A <mask>`, 3e6 iters × 60 tries). **cost = missing (point, colour) incidences out of `8\times31=248`**. None reached 0." ✓✓
【数据格式】17 行：`mask  NOSOLUTION F=4 M=5 k=8 bestcost=14`（mask 例：`00007648`,`00007660`,`00007c28`,…）✓
【⟹ `A4` 的精确对象（本档定稿）】 `r=9`：`F=4,\ M=5`；`|A|=7`（`k=8=|A\cup\{0\}|`）；`B=V\setminus(A\cup\{0\})` ⟹ $$|B|=2^4-7-1=8$$ ✓
　**缺失 incidence ＝ 序对 `(b,u)`**，`b\in B`（`8` 个）、`u` 为 `\mathrm{PG}(4,2)` 的点（`2^5-1=31` 个），**缺 `b\in C_u`** ⟹ 总数 `8\times31=248` ✓✓✓
　**`bestcost=14` ＝ 这 248 条 incidence 中缺 14 条**（17 类全是 `14`，**无一为 0**）✓
【长度自检（本档）】 `n=2^F-1-|B|+2^M-1=15-8+31=38` ✓✓ **与目标 `n=38` 精确吻合** ✓✓
```

## §4 状态与下一步（仍**不分析、不求解**）

```
【`A1`–`A4`】 ✓ **达成**（清单／族定义／17 类／`14` 的精确对象，全部一手）✓
【`A5` 剩余】 写正式有限规格：变量＝`A`-mask（17 类已定）＋ `g:W\setminus\{0\}\to V`（`31` 点各取 `V\cong\mathbb F_2^4`）；约束＝`\forall b\in B,\forall u:\ \exists\ell\ni u,\tau(\ell)=b`；对称商＝`\mathrm{GL}(4,2)`（`V`）／`\mathrm{GL}(5,2)`（`W`）／**shear**（`README` §2 末被截断，**下一轮补读**）✓
【⚠️ 未读到（下一轮）】 `README.md` §2 末"`A shear…`"之后的内容（含 `lines.py`／`fullsets.py`／`run_q11_checks.sh` 的具体口径）✓
【⚠️ 措辞纪律】 17 类的确切命题是 $$\boxed{\text{17 GL}(4,2)\text{-classes exhaust the specified \textbf{fibered} family at }r=9,n=38}$$ —— **不得**升级为"穷尽全部 `9\times38` 码" ✓✓
【⛔ 红线（未碰）】 `r=10,n=49`｜`r=11` 的 order `11/17/23`｜`q10` order-7｜族外搜索｜SAT 求解 ✓
【边界】 §0–§3 全部为**一手逐字/本机实测**；§4 规格草案为**本档自行推导**；未制造候选／未启动搜索／未碰 RH。
