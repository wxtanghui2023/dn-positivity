# RESULT-2026-09-30-DS243b — $\mathbb Z_9^2$-fiber 细筛：**6 个分布塌缩为唯一 $\{36,40,45\}$** ✓；便宜条件**全部存活** ✗（无 P1 非存在性路线）

> 空间 B｜非 C 号｜唐先生 12:44「选 (b)：先做 $\mathbb Z_9^2$ 的 6 个 fiber 分布细筛，再决定是否上 (a)」｜**不主张任何新值**（V290）
> 时间：2026-09-30 13:0x

**已查地图**：承 `DS243-2026-09-30`（乘子约化／商群条件／探针）／`POOL-V2`（Survivor-1）
D0: 本档对象 = **档案已有**（$H{=}\mathbb Z_9^2$ 之 6 分布）之**细筛**（新数学对象：无 ✗）
D1: 0（产出 = **一条塌缩结论 ＋ 三条条件之存活判定** ⚠️✓）

---

## §0 **核心结果：6 → 1（唯一分布，仅剩排列）** ✓✓

$$H=\mathbb Z_9^2\ (\text{阶 }81,\ 3\ \text{陪集});\quad \sum_i r_i=121;\quad \sum_i r_i(r_i-1)=\lambda(|H|-1)=60\cdot80=4800 \Longrightarrow \sum_i r_i^2=4921$$
$$\text{枚举 }0\le r_i\le81\ \Longrightarrow\ \textbf{唯一（无序）解}:\quad \boxed{\{r_0,r_1,r_2\}=\{36,\ 40,\ 45\}}$$
$$(3!=6\ \text{个排列} = \text{此前 DP 报的"6 个解"} ✓;\ \text{无序仅 1 种}) \Longrightarrow \textbf{fiber 尺寸被完全确定} ✓✓$$

## §1 三条便宜条件之存活判定（**全部 survive** ✗）

$$\textbf{(C1) 逐元容量（跨 coset）}:\ z\in \text{非零 coset}\ \Longrightarrow\ 60=N^{(1,0)}_z+N^{(2,1)}_z+N^{(0,2)}_z,\quad N^{(a,b)}_z\le\min(r_a,r_b)$$
$$\qquad\Longrightarrow\ \text{必要条件}\ \sum_{i<j}\min(r_i,r_j)\ge60;\quad \text{实测}\ 36+40+36=112\ \ge60\ \Longrightarrow\ \textbf{survive} ✗$$
$$\textbf{(C2) 链上界（同 coset，}z\ \text{阶 }d）：\ N^{(i,i)}_z\le r_i-\lceil r_i/d\rceil;\quad d{=}9:\ 32{+}35{+}40=107\ge60;\ d{=}3:\ 24{+}26{+}30=80\ge60\ \Longrightarrow\ \textbf{survive} ✗$$
$$\textbf{(C3) 嵌套子群一致性（本档新增）：}K\le H\ \text{之 coset 细化须同时满足两个二次恒等式}$$
$$\qquad K\ \text{阶 }9\ (27\ \text{陪集},r\le9):\ \text{解数}=\mathbf{378}\ >0;\qquad K\ \text{阶 }27\ (9\ \text{陪集},r\le27):\ \text{解数}=\mathbf{47}\ >0\ \Longrightarrow\ \textbf{survive} ✗$$
$$\qquad\text{例（}K\ \text{阶 }9）：组 36=(0,0,3,4,5,5,6,6,7)；组 40=(4,4,4,4,4,5,5,5,5)；组 45=(5^9)$$

## §2 判定（对唐先生流程之回应）

$$\boxed{\text{6 个 case \textbf{无一}被便宜条件排掉} ✗ \Longrightarrow \textbf{“P1 非存在性路线”\ 未出现}}$$
$$\text{但收益是\textbf{结构性}的}:\ \text{候选空间从"3 个自由尺寸"} \to \textbf{唯一分布}\{36,40,45\}\ \Longrightarrow\ \text{可作硬约束喂给强搜索} ✓✓$$

## §3 纪律记录（照唐先生指示 ✓）

$$\textbf{(D1)}\ \text{v3 之 }1016\to344\ \textbf{只能记 "feasibility signal only"}，\textbf{不得}解作"接近存在" ✗\ (\text{目标为 242 个差同时精确 }=60) ✓$$
$$\textbf{(D2)}\ \textbf{61-乘子定理之确切假设仍待核实} ⚠️;\ \text{当前仅作\ \textbf{计算搜索约束}使用}，\text{文档中\ \textbf{不写成理论闭合} ✓}$$
$$\textbf{(D3)}\ \text{本轮无新数学对象};\ \text{未取文献原文（R16–17）} ✓;\ \text{未碰 RH} ✓$$

## §4 去向（待唐先生定）

$$\textbf{(a)}\ \text{强搜索（MILP/CP-SAT 或增量 delta 局部搜索）} \textbf{加硬约束}\ \{r_i\}=\{36,40,45\}\ \text{与 }\sigma\text{-不变性} \Longrightarrow \text{搜索空间再降一档} ✓$$
$$\textbf{(a′)}\ \text{或先做}\ H\text{-内差谱之 Fourier/整性细筛（更便宜）} ✓$$
$$\textbf{(b′)}\ \text{若 (a) 无解} \Longrightarrow \text{考虑以 }K\ \text{阶 }9\ \text{之 378 解为二级约束逐层收窄} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
