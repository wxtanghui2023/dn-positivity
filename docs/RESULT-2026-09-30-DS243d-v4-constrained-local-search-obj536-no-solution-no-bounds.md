# RESULT-2026-09-30-DS243d — v4 强搜索（硬约束 $\{36,40,45\}$ ＋ $\sigma$-不变）：**obj 2340→536，无解、无界** ✗（按判读纪律：不作存在性/不存在性证据）

> 空间 B｜非 C 号｜唐先生 12:59「不再开新理论支线，等 v4 结果；并按判读纪律区分 not-proved vs infeasible」｜**不主张任何新值**（V290）
> 时间：2026-09-30 13:2x

**已查地图**：承 `DS243c`（(a′) 新条件 $\sum m^2=601$，无 P1）
D0: 本档对象 = **档案已有**（Survivor-1 之搜索）之**受约束执行记录**（新数学对象：无 ✗）
D1: 0（产出 = **一条搜索读数 ＋ 一条判读 ＋ 一条下一刀判定** ⚠️✓）

---

## §0 结果（`tender-lagoon`，240 s，exit 0）

$$\text{硬约束}:\ \text{逐陪集尺寸}\{r_i\}=\{36,40,45\}\ ✓\ (\text{全程保持});\quad \sigma\text{-不变（99 轨道）}\ ✓;\quad |D|=121\ ✓$$
$$\textbf{读数}:\ \text{可行互换 } 82{,}867\ \text{次};\quad \text{obj（}=\Sigma_z(c_z-60)^2\text{）}: \mathbf{2340 \to 536};\quad \textbf{未达 0} ✗$$
$$\text{对照 v3（无硬约束）}:\ \text{obj } 1016\to\mathbf{344}\ (\text{180 s})\ \Longrightarrow\ \text{加约束后可达之最小值\ \textbf{更差}（536>344）} ✓\ \text{与"约束为实"一致}$$

## §1 **判读（严格照唐先生纪律 ✓）**

$$\textbf{(i)}\ \text{这是\ \textbf{局部搜索}，不是精确求解器} \Longrightarrow \textbf{零 infeasibility 证据} ✗;\ \text{"240 s 未达 0"\ \textbf{≠} "不存在"} ✗$$
$$\textbf{(ii)}\ \text{incumbent\ \textbf{存在}（obj=536）};\ \text{但\ \textbf{lower/upper bound 皆无}（局部搜索不产界）} ✗$$
$$\textbf{(iii)}\ \text{“哪条硬约束先冲突”\ \textbf{本轮不可判}（无冲突诊断机制）} ⚠️$$
$$\therefore\ \boxed{\text{本轮结论仅为: 受约束搜索 240 s 内未找到可行解；\textbf{不作任何存在性判定}}} ✓$$

## §2 若要有**界**（判 infeasibility 之唯一途径）

$$\text{须\ \textbf{精确方法}:\ MILP/CP-SAT ＋ \textbf{线性化}\ \big(y_Oy_{O'}\ \text{pair 变量}\big)} \Longrightarrow \text{约 }5\times10^3\ \text{二值变量}、242\ \text{个差计数等式}$$
$$\text{可加二级约束}:\ \sum_{i,j}m_{i,j}^2=601\ (\text{a′ 新条件}),\ K\ \text{阶 }9\ \text{之 }378\ \text{局部解}$$
$$\text{代价}:\ \textbf{贵}（分钟–小时级）;\ \text{收益}:\ \text{可给 bound／可证 infeasible（若确有）} ✓$$

## §3 本档保留之两件硬数据（照唐先生指示 ✓）

$$\boxed{\{r_i\}=\{36,40,45\}}\qquad\text{与}\qquad\boxed{\sum_{i,j}m_{i,j}^2=601}$$
$$\text{后者＝对 }3H\text{-陪集占用矩阵之\ \textbf{二次矩约束}，是下一轮诊断 infeasibility 之重要切口} ✓$$

## §4 边界与纪律

$$\textbf{(D1)}\ \text{v3/v4 皆只记 "feasibility signal only"} ✓;\quad \textbf{(D2)}\ \text{61-乘子假设仍待核 ⚠️（仅作计算约束）};\quad \textbf{(D3)}\ \text{未主张任何新值／未取文献原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
