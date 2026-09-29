# CALIBRATE-K9-c（2026-09-29）—— **加 cap 后仍为 $52$（rich 集合为空）；含我自身两处 bug 之更正**

> **性质**：**自查 ＋ 修正（P-a 纪律）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 15:0x ✓

**已查地图**：`CALIBRATE-K9-b`／`CALIBRATE-K9`✓

D0: 本档对象 ＝ **档案已有**（纤维约束／cap——皆经典 ✓）
D1: 0（产出＝**两处自我更正 ＋ cap 无效之验证** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ⚠️ 我上一档遗漏了一个上界}:\ |N_1(A)|\le2^{n-r}\ (\text{纤维只有 }2^{n-r}\ \text{点})}$$
$$\boxed{\text{② ✓ 但加 cap 后\ \textbf{仍为 }52}:\ r{=}1,2,3\ \text{之最优\ \textbf{rich 集合为空}\ (}S{=}\varnothing),\ M_{\min}{=}51.2}$$
$$\boxed{\text{③ ⚠️ 且我首次尝试之 MILP\ \textbf{有优先级 bug}（}\texttt{1<<(9-r)+(10-r)-1}\ \text{被解析为 }\texttt{1<<16}\text{）}\Longrightarrow\ \text{"}M_{\min}{=}48\text{"}\ \textbf{为垃圾}}$$
$$\boxed{\text{④ ⟹ 结论\ \textbf{维持}:\ 线性局部账目层封顶于 }52\text{；}\textbf{非}\ \text{技术不足}}$$

## §1 ① 遗漏之上界（**⚠️ 诚实**）

$$\text{上一档我写}:\ 256\le|N_1(A)|+b\le9a+b\ (\text{仅用 trivial }|N_1(A)|\le9a)$$
$$\text{遗漏}:\ \boxed{|N_1(A)|\le2^{\,n-r}=256}\ (\text{纤维本身只有 }256\ \text{点})$$
$$\therefore\ \text{正确形式}:\ 256\ \le\ \min\bigl(2^{\,n-r},\ (10{-}r)N_u\bigr)+\sum_{v\sim u}N_v$$

## §2 ② cap 不改善（**✓ 验证于 $r{=}1,2,3$**）

$$\text{cap 之等价形式（析取）}:\ \text{对每个 }u:\ \text{或}\ N_u\ge\text{thr}\ (\text{rich, 约束自动满足});\ \text{或}\ (10{-}r)N_u+\sum_{v\sim u}N_v\ge2^{\,n-r}$$
$$\text{thr}=\lceil2^{\,n-r}/(10{-}r)\rceil:\ r{=}1\Rightarrow29;\quad r{=}2\Rightarrow16;\quad r{=}3\Rightarrow10$$
| $r$ | $2^{n-r}$ | thr | $M_{\min}$（带 cap） | 最优 rich 集合大小 |
|---|---|---|---|---|
| $1$ | $256$ | $29$ | $\mathbf{51.2}$ | $\mathbf{0}$ |
| $2$ | $128$ | $16$ | $\mathbf{51.2}$ | $\mathbf{0}$ |
| $3$ | $64$ | $10$ | $\mathbf{51.2}$ | $\mathbf{0}$ |

$$\therefore\ \boxed{\text{最优解取 }S=\varnothing\ (\text{无 rich 纤维})\Longrightarrow\ \text{cap 从未被激活}\Longrightarrow\ \text{界仍为 }52}✓$$
$$\text{直觉}:\ \text{使某纤维 rich 需 }N_u\ge\text{thr},\ \text{其代价高于所换得的松弛}\Longrightarrow\ \text{不划算}✓$$

## §3 ③ 我自身两处 bug（**⚠️ 更正**）

$$\text{bug-1（优先级）}:\ \texttt{1<<(9-r)+(10-r)-1}\ \text{在 Python 中被解析为}\ \texttt{1<<16}=65536\Longrightarrow\ \text{thr}=7281\ (\text{荒谬})$$
$$\qquad\Longrightarrow\ \text{big-M 松弛变成无穷大}\Longrightarrow\ \text{约束\ \textbf{全空}}\Longrightarrow\ \text{"}M_{\min}{=}48\text{"（搜索下限）为\ \textbf{垃圾}}✗$$
$$\text{bug-2（首档之方向论证亦须精确化）}:\ \text{我此前说"用精确 }|N_1(A)|\ \text{只会更弱"}\ ——\ \text{该句\ \textbf{对 }|N_1(A)|\ \text{本身成立}}$$
$$\qquad\text{但\ \textbf{不等于}"加 cap 也无效"};\ \text{cap 是\ \textbf{另一个}（上）界，须单独检验}\Longrightarrow\ \text{本档已检验}\ ✓$$

## §4 ④ 结论（**维持**）

$$\boxed{\text{LINEAR-LOCAL-ACCOUNTING = CLOSED at }52}\ ✓\ (\text{一阶纤维 LP ＋ 二阶 multiplicity profile ＋ cap 三层皆不破 }52)$$
$$\text{推广}:\ \text{求和论证 }\sum_u[(10{-}r)N_u+\sum_{v\sim u}N_v]=10M\ \text{对一切 }r\ \text{恒给 }52✓$$

## §5 下一层之关键警告（**供唐先生决策**）

$$\text{有限类型层}\ \tau(F)\ \text{之\ \textbf{致命问题}}:\ \text{兼容条件为\ \textbf{集合级}}:\ N_1(A)\cup B=\mathbb F_2^{\,n-r}$$
$$\therefore\ \tau\ \text{若只记\ \textbf{计数统计}（weight dist／multiplicity）}\ \text{则\ \textbf{不能判定}兼容}\ \Longrightarrow\ \text{类型数不压缩}✗$$
$$\therefore\ \text{可用之 }\tau\ \text{必须记录\ \textbf{defect 集合结构}}:\ D_A=\mathbb F_2^{\,n-r}\setminus N_1(A)\ (\text{且 }D_A\subseteq B,\ D_B\subseteq A)$$
$$\text{而 }r{=}1\ \text{时}\ \text{此即\ \textbf{精确重述}}\ (K(n,1)=\min\{|A|{+}|B|:N_1(A)\cup B=N_1(B)\cup A=\mathbb F_2^{n-1}\})\Longrightarrow\ \textbf{无压缩}✗$$
$$\therefore\ \boxed{\text{建议}:\ \text{类型层之 }\tau\ \text{须以 defect 集合为主变量，且从\ \textbf{小 }n\ \text{之已知值递归校准}}\ (K(5,1){=}7,\ K(6,1){=}12,\ K(7,1){=}16,\ K(8,1){=}32)✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "cap不改善" "rich集合为空" "优先级bug更正"
技术词 cap不改善     命中文件数=0    ::
技术词 rich集合为空   命中文件数=0    ::
技术词 优先级bug更正  命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **cap 析取枚举（$r{=}1,2,3$ 全量 $2^m$ 子集 × LP）** ✓；**不占 C 号** ✓；**未用 SAT/CP-SAT** ✓
- **两处自我更正已如实记录** ✓；**结论维持**（线性层封顶 52）✓
