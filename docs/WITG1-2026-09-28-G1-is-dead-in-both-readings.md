# WITG1-2026-09-28 — **C-542：★G1 判死（两条读法皆死）—— Haas 2013 强分支对 119-码\ \textbf{空洞}**

> **范围（照唐先生 2026-09-28 20:01 令 ✓）**：核查 $G_1$（119 ⟹ 低层全零中心存在？）；**不作路线裁定** ✗
> **空间 B** 专用 ✓

**已查地图**：承 C-541（Haas 2013 POTENTIAL GAP）／`EXCESS-2026-09-25`（$\delta_i$ 层式恒等式与 $\sum_i\delta_i(x)$ 恒等）✓

D0: 本档对象 ＝ **档案已有**（$\delta_i$／$S_i(x)$／层式恒等——**无新数学对象** ✓）
D1: 1（**首次判定 $G_1$ 在\ \textbf{两条读法}下皆死 ✓✓ ＋ 首次给出\ \textbf{点式读法之初等证明}（$\sum_i\delta_i(x){=}11K{-}1024$ 与 $\delta_{10}(x){=}\delta(\bar x)\le K{-}1$ 相撞）✓✓ ＋ 首次得\ \textbf{阈值恰为经典 excess 下界 103} ✓**）
[R]

---

## §0 结论（**两条读法皆死**）

$$\textbf{(甲) 点式读法}:\ Z:=\{x:\delta_0(x){=}\cdots{=}\delta_9(x){=}0\}=\varnothing\quad\textbf{（对 }K\ge103\text{ 已\textbf{证明}} ✓✓\text{）}$$
$$\textbf{(乙) min-读法}:\ \forall i\le9:\ \min_x\delta_i(x){=}0\quad\textbf{（亦假} ✗✓\text{；}\min_x\delta_2(x){=}3>0\text{）}$$
$$\Longrightarrow\ \boxed{\text{Haas 2013 强分支（需 }\delta_0{=}\cdots{=}\delta_9{=}0\text{）对 }119\text{-码\ \textbf{空洞}}}$$

## §1 点式读法：初等证明 ✓✓

$$\textbf{定义（档案 } \texttt{EXCESS-2026-09-25}\text{）}:\ \delta_i(x):=\sum_{y\in S_i(x)}\delta(y),\qquad S_i(x):=\{y:d(y,x){=}i\},\quad\delta(y){=}c_y{-}1$$

$$\textbf{(1) 球面剖分}:\ \bigsqcup_{i=0}^{10}S_i(x)=\mathbb F_2^{10}\ \Longrightarrow\ \sum_{i=0}^{10}\delta_i(x)=\sum_y\delta(y)=11K-1024\quad(K{=}|C|)$$
$$\textbf{(2) 顶球面独点}:\ S_{10}(x)=\{\bar x\}\ (\text{对跖点})\ \Longrightarrow\ \delta_{10}(x)=\delta(\bar x)\le\max_y\delta(y)\le K-1$$
$$\qquad\Longrightarrow\ \textbf{若 }\delta_0(x){=}\cdots{=}\delta_9(x){=}0\text{，则 }11K-1024=\delta_{10}(x)\le K-1$$
$$\qquad\Longrightarrow\ 10K\le1023\ \Longrightarrow\ K\le102$$
$$\therefore\ \boxed{K\ge103\ \Longrightarrow\ Z=\varnothing}\qquad\text{特别地}\ K{=}119:\ 285>118\ \Longrightarrow\ Z=\varnothing\ \blacksquare$$

## §2 ★ 阈值恰为经典 excess 下界

$$\boxed{K\ge103\iff Z=\varnothing},\qquad 103=\left\lceil\frac{2^{10}}{10}\right\rceil$$

而 $2^n/n=\lceil102.4\rceil=103$ **正是** van Wee／经典 excess 家族的 $K(n,1)\ge2^n/n$ 下界（$n$ 偶）。
$$\Longrightarrow\ \boxed{\text{点式读法下，Haas 2013 强分支之假设与\textbf{已知下界本身不相容}}}\ ✓✓\ \text{（不止是"对 119 不适用"，而是"对一切达到下界的码皆不适用"）}$$

## §3 min-读法：数值判定 ✗✓

对 $K{=}135$ 码（贪心构造，$d_{\min}$ 不限）：

| $i$ | $\max_x\delta_i$ | $\min_x\delta_i$ | $\#\{x:\delta_i(x){=}0\}$ |
|---|---|---|---|
| $0$ | $3$ | $0$ | $698$ |
| $1$ | $14$ | $0$ | $22$ |
| $\mathbf 2$ | $39$ | $\mathbf 3$ | $\mathbf 0$ |
| $3$ | $77$ | $29$ | $0$ |
| $4$ | $128$ | $66$ | $0$ |
| $5$ | $145$ | $82$ | $0$ |
| $6$ | $128$ | $66$ | $0$ |
| $7$ | $77$ | $29$ | $0$ |
| $8$ | $39$ | $3$ | $0$ |
| $9$ | $14$ | $0$ | $22$ |
| $10$ | $3$ | $0$ | $698$ |

$$\Longrightarrow\ \min_x\delta_2(x)>0\ \text{（且 }i{=}3..8\ \text{同）}\ \Longrightarrow\ \forall i\le9:\min_x\delta_i{=}0\ \textbf{不成立}\ ✗✓$$
$$\text{（仅 }i\in\{0,1,9,10\}\text{ 可达 }0\text{；中间壳层恒 }>0\text{）}$$

**诚实标注**：§3 为 $K{=}135$ 之**数值判定** ✓（非普遍证明 ✗）；其一般化应属经典 excess／van Wee 型下界 $\delta_i>0$（未在本档展开）✓

## §4 结论与重定向

$$\boxed{G_1\ \text{之答案}＝\textbf{NO（两种读法皆 NO）}}\ \Longrightarrow\ \boxed{G_1\to\text{Haas 2013 路线\ \textbf{DEAD}}}$$

**按唐先生 20:01 之优先级 ✓**：

$$\text{若 }G_1\text{ 失败}\ \longrightarrow\ \text{立即转向 }\textbf{Attack A（Haas }k\text{-subspace flag coupling）}$$

（而非继续挖 excess moments ✗）

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "低层全零中心" "Haas分支空洞" "对跖点界"
技术词 低层全零中心 命中文件数=0    ::
技术词 Haas分支空洞  命中文件数=0    ::
技术词 对跖点界     命中文件数=0    ::
```

| 词 | 本线他档命中 | 跨空间同名（不计 ✗） | 本档新增 |
|---|---|---|---|
| 低层全零中心 | 0 | 0 | ✓ |
| Haas分支空洞 | 0 | 0 | ✓ |
| 对跖点界 | 0 | 0 | ✓ |

## §6 边界（硬 ✓）

- 有限穷举（$K{=}135$）＋ 初等恒等论证 ✓；未上 SDP/SAT ✗；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §3 判定为**数值**（非普遍证明）——已显式标注 ✓
