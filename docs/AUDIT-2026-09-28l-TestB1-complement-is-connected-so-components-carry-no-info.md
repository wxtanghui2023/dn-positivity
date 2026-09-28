# AUDIT-2026-09-28l — **Test-$B1$：补图恒连通（1 分支）⟹ components 候选无信息 ⟹ 边界层降级**

> **性质**：**实验/审计**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:56 ✓
> **唐先生令**：跑 Test-$B1$（候选**缩为一个**：补图连通分支结构）；门修正＝验"是否被**现有数据**（一/二/三点）决定" ✓

**已查地图**：接续 `AUDIT-k`（边界门）／`AUDIT-j`（$\Phi_2$ 降格）✓

D0: 本档对象 ＝ **档案已有**（补图／连通分支／覆盖码——无新数学对象 ✓）
D1: 0（产出＝**Test-$B1$ 负结果 ＋ 边界层降级判定** ⚠️）

---

## §0 结论（先给）

$$\boxed{\textbf{Test-}B1:\ \text{18/18 覆盖码之补图}\ G=Q_{10}[V\setminus C]\ \textbf{全部连通}（分支数{\equiv}1）}\ ✓✓$$
$$\boxed{\Longrightarrow\ \text{Gate }B1\text{-B 触发}:\ \text{分支结构\ \textbf{退化}（无中间层）} \Longrightarrow \text{components 候选\ \textbf{KILL}};\ \text{边界层\ \textbf{降级}}}\ ✗$$

## §1 实测（18 个极小覆盖码，$K{=}143..192$ ✓）

| | $K$ 范围 | 分支数 | 最大分支 |
|---|---|---|---|
| jit=0（6 码） | $143$–$146$ | $\mathbf 1$ | $878$–$881$ |
| jit=1（6 码） | $152$–$192$ | $\mathbf 1$ | $832$–$872$ |
| jit=2（6 码） | $164$–$171$ | $\mathbf 1$ | $853$–$860$ |

$$\textbf{分桶测试（按 }(K,N_1,N_2)\text{ 及按 a-profile）}:\ \text{桶数}=18,\ \textbf{多分支结构桶}=0\ ⚠️$$

## §2 原因分析（**为何退化 ✓**）

$$\text{相关 }K\ \text{范围内}:|V\setminus C|=1024-K\approx\mathbf{880}\ \text{（巨大）};\ \text{每点度数}=10-a_x\approx8\text{–}10\ \text{（稠密）}$$
$$\Longrightarrow\ \text{补图\ \textbf{极可能被 covering-radius-1 强制连通}}\ \text{（18/18 支持 ✓）}$$
$$\text{对照}:\ K\to1024\ \text{时 }|V\setminus C|\ \text{小} \Longrightarrow \text{可断（如仅剩两个相距}\ge2\text{ 之点）}\ \text{——但\ \textbf{不在射程}} ⚠️$$

**诚实边界**：§2 之"强制连通"为**经验 ＋ 稠密度启发**，**未证** ⚠️（$\deg\ge10-K$ 之平凡界在 $K{\approx}119$ 时无信息）

## §3 判定（**照唐先生 Gate $B1$-B ✓**）

$$\text{可获构型中分支结构\ \textbf{恒定}（}\equiv1\text{）且极可能由 covering 强制} \Longrightarrow \text{按令\ \textbf{直接 KILL}}\ ✗$$
$$\boxed{\text{中间层（components）\ \textbf{不存在}} \Longrightarrow \text{按唐先生"若不成立，边界层整体降级" ⟹ \textbf{边界层降级}}}\ ✗$$

## §4 系统性剥除总表（**本档汇总 ✓**）

| # | 表示 | 归宿 |
|---|---|---|
| 1 | 一阶 ownership $\rho$ | sphere-bound ledger |
| 2 | coset size | linear counting |
| 3 | subspace LP | $93.0909$ |
| 4 | integer coset classification | 同层重编码 |
| 5 | $\Phi_2$（方向重数） | 三点距离层 |
| 6 | **补图 components（边界层）** | **恒连通 ⟹ 退化** |

$$\boxed{\text{6 类表示全部剥除};\ \text{且 5、6 皆\ \textbf{早期廉价杀}}\ ✓}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "补图连通性" "分支结构退化" "边界层降级"
技术词 补图连通性   命中文件数=0    ::
技术词 分支结构退化  命中文件数=0    ::
技术词 边界层降级   命中文件数=0    ::
```

## §6 边界（硬 ✓）

- 有限计算（18 码）＋ 结构性启发 ＋ 既有档引证 ✓；**不占 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §2 之"强制连通"**未证** ⚠️；若唐先生要求，可做解析证明（但预期不产生新资产）
