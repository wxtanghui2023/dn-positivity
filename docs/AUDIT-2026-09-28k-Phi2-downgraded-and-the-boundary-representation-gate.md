# AUDIT-2026-09-28k — **$\Phi_2$ 正式降格 ＋ 补集/边界表示门 $P_{-1}^{\rm boundary}$**

> **性质**：**审计/实验**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:53 ✓
> **唐先生令**：暂停 $\Phi_2$；**不做** $n{=}10$ 穷举；换到 complement/boundary 层 ✓

**已查地图**：接续 `AUDIT-h/i/j`（$\Phi_2$）／`AUDIT-d/e`（机制族穷尽）✓

D0: 本档对象 ＝ **档案已有**（$\Phi_2$／补集结构／距离数据——无新数学对象 ✓）
D1: 0（产出＝**降格 ＋ 边界门之两点结构判定** ⚠️）

---

## §1 $\Phi_2$ 正式降格（**照令 ✓**）

$$\boxed{\Phi_2\ \longrightarrow\ M_3\ \longrightarrow\ \text{三点距离数据}\ \Longrightarrow\ \Phi_2\ \textbf{降格为三点层}\ ✗}$$
$$\text{且 `AUDIT-j` 自纠："}M_3\ \text{结构定理"本身即 tautology ⟹ \textbf{未留任何隐藏新量}}\ ✓$$

**局部计数型 representation 族之系统性剥除（本档汇总 ✓）**：

| 表示 | 归宿 |
|---|---|
| 一阶 ownership $\rho$ | sphere-bound ledger |
| coset size | linear counting |
| subspace LP | $93.0909$ |
| integer coset classification | 同层重编码 |
| $\Phi_2$ | 三点距离层 |

$$\Longrightarrow\ \boxed{\text{不是"没找到证明"，而是系统性剥掉了局部计数型表示族}}\ ✓$$

## §2 不做 $n{=}10$ 穷举之理由（**照唐先生 ✓**）

$$\text{目标命题}:\ \nu(c_1,c_2,c_3)=F(d_{12},d_{13},d_{23})\ \text{为\ \textbf{局部} hypercube 几何事实}$$
$$\text{（}n{=}6,7\ \text{已穷举证};n{=}10\ \text{只增算量，\textbf{不改研究层级}} ✗\ \text{——除非需解析分类，否则不值得包装成资产）}$$

## §3 ★ 新门 $P_{-1}^{\rm boundary}$

$$\boxed{C\ \to\ Q_{10}\setminus C\ \to\ \partial(Q_{10}\setminus C)\ \to\ \text{boundary/flow invariant}}$$
$$\text{与 private-neighbor ledger 之别 ✓}:\ \rho(c)\ \text{在\ \textbf{码字周围} 计数};\ \text{新对象在\ \textbf{非码点之邻接结构} 上计数}\ ✓$$

## §4 ★★ 两点结构判定（**本档核心 ⚠️✓**）

### (甲) 一阶边界量已被距离分布吸收 ✗（实测 ✓）

$$\partial:=\#\{(c,x):c\in C,\ x\notin C,\ d(c,x)=1\}\ \overset{\textbf{实测}}{=}\ 10K-2N_1\ ✓\ \big(\text{三例皆等}\ ✓\big)$$
$$\big|E(Q_{10}\setminus C)\big|=\tfrac12\big(10(1024-K)-\partial\big)\ \Longrightarrow\ \text{亦由}(K,N_1)\ \text{决定}\ ✗$$
$$\therefore\ \text{一阶边界量\ \textbf{全部}被距离分布吸收}\ ✗$$

### (乙) ⚠️ 但"完整补集结构"是**完全不变量** ⟹ 无归约

$$\mathbb F_2^{10}\setminus C\ \text{确定}\ C\ ✓\ \Longrightarrow\ \text{补集之同构型}\ \Longleftrightarrow\ C\ \text{之同构型}\ \text{（\textbf{极大不变量}）}$$
$$\therefore\ \text{补集结构\ \textbf{必不被} 距离/三点数据决定（一般）}\ ✓;\ \text{但同时也\ \textbf{等价于 }C\ \text{本身}} \Longrightarrow \textbf{无归约} ⚠️$$
$$\text{（同 `AUDIT-g` §1 之"完整 state ＝ }C\text{" 之形态 ⟹ \textbf{同一陷阱警告}} ⚠️)$$

## §5 因此边界门之**唯一有意义形式**（待唐先生定）

$$\boxed{\text{须寻\ \textbf{中间层} 边界不变量}:\ \text{细于一阶（}\partial,|E|\text{）、但粗于完整补集（＝}C\text{）}}$$
$$\textbf{判据（照唐先生）}:\ \exists\ \text{两 covering 构型同距离/三点数据而边界不变量不同？}$$
$$\text{若"否" ⟹ 亦被关联方案吸收 ⟹ \textbf{停止构造}}\ ✗;\ \text{若"是" ⟹ 进 }P_1\ ✓$$
$$\textbf{候选（本档建议，未做）}:\ \text{补图之\ \textbf{环空间/连通分支/边界算子核}（同调量）}\ ⚠️\ \text{——须先验其距离决定性}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "补集完全不变量" "边界表示门" "一阶边界吸收"
技术词 补集完全不变量 命中文件数=0    ::
技术词 边界表示门   命中文件数=0    ::
技术词 一阶边界吸收  命中文件数=0    ::
```

## §7 边界（硬 ✓）

- 有限计算（三例）＋ 结构性论证 ＋ 既有档引证 ✓；**不占 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §4(乙) 之"完全不变量"为**集合论显然事实** ✓；§5 候选**未做** ✗
