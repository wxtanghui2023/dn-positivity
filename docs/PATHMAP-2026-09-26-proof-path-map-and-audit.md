已查地图：已跑 scripts/prework_map_check.sh 证明路径 审计 n=8 b≤2 Q*(8) ⟹ 执行自 DECIDE-2026-09-26 档；本档为**规划层地图 ＋ 路径审计**（唐先生 2026-09-26 11:56 指令）；性质 = 编排，非新数学方向 ✓。
D0: 本档对象 = 从 P₀ 到 M1/M2/M3 的可达路径集合与瓶颈定位（规划层）
D1: 0（无新自由度；产出为路径地图、审计表、三张状态表）

# PATHMAP-2026-09-26 · 证明路径地图与审计

## §0 工作纪律（**上位框架** ✓，唐先生 2026-09-26 11:56 立）

```
$$\text{① 先锁定命题精确逻辑形式（}\forall n\ /\ \text{逐 }n\ /\ \text{单点}\ ✓）；\text{明确每步等价/蕴含}\ ✓$$
$$\text{② 每增加一个剪枝（WLOG／minimality／private point／capacity／}b\le2\Rightarrow Q^*=0\text{）\textbf{必须先给合法性证明}}\ ✓$$
$$\text{③ \textbf{严格分层}: 定理/引理} \Rightarrow \text{合法缩减} \Rightarrow \text{有限实例} \Rightarrow \text{完整枚举/UNSAT certificate}\ ✓$$
$$\qquad \textbf{UNKNOWN 永停在"证据"，不得跨层升级为定理}\ ✗$$
$$\text{④ 每次计算前先问: 它关闭证明链上的哪一个 OPEN？(只"跑更久"⟹ 不作主线}\ ✗)$$
$$\text{⑤ 优先找\textbf{结构性不变量}，而非堆搜索}\ ✓;\qquad \text{⑥ 每轮维护三张表: CLOSED / EVIDENCE / OPEN}\ ✓$$
$$\text{（本纪律记为 } \textbf{AMEND-30}\ \text{候选，待唐先生批准入宪 ✓）}$$
```

## §1 当前位置 P₀ 与目标分层

```
$$P_0:\ K(8,1)=32\ \text{已知 ✓};\ \text{目标 } b(x)\le2\ \forall x\iff Q^*(8)=0\ \iff A_1+A_2\le16\ ✓\ (\text{因 }Q=2(A_1+A_2)-E,\ E=32\ ✓)$$
$$\text{现状}: \text{CP-SAT/SAT} \Rightarrow \textbf{UNKNOWN}\ ✗\ (\text{证据，非证明}\ ✗)$$
$$M_1\ (\text{最有价值}): \text{结构定理}: \text{最优覆盖}\Rightarrow\text{结构约束}\Rightarrow b\le2\ ✓\ (\text{不依赖全枚举}\ ✓)$$
$$M_2: \text{结构约束}\Rightarrow\text{有限剩余构型}\Rightarrow\text{完整 certificate}\ ✓\ (\text{solver 只跑最后一公里}\ ✓)$$
$$M_3: Q^*(8)=0\ \text{并抽机制}\Rightarrow Q^*(n)\ \text{规律 / 一般 }n\ ✓$$
```

## §2 ⭐ 本轮数学新结果：**excess 集中度的算术约束**（P₀ 直接可用 ✓）

```
$$\text{恒等式（general }n\text{）}: \sum_x\delta^2=4(A_1+A_2)-E\ \Longrightarrow\ \sum_x\delta^2\equiv -E\ (\mathrm{mod}\ 4)\ ✓$$
$$\text{本例}: E=32\ \Longrightarrow\ \boxed{\sum_x\delta^2\equiv0\ (\mathrm{mod}\ 4)}\ ✓;\qquad \delta\ \text{非负整数};\ \sum_x\delta=32\ ✓$$
$$\text{单点集中（该点 }\delta=m-1\text{，其余 }m\le2\text{）的算术可行性}:$$
$$\begin{array}{c|c|c|c|c}
m & \delta=m-1 & \text{需 }\delta{=}1\ \text{点数} & \sum\binom{b}{2} & \text{判定}\\
\hline
3 & 2 & 30 & 33\ (\text{奇}) & ✗\ \textbf{排除}\\
4 & 3 & 29 & 35\ (\text{奇}) & ✗\ \textbf{排除}\\
5 & 4 & 28 & 38 & ✓\ \text{允许}\\
6 & 5 & 27 & 42 & ✓\ \text{允许}\\
7 & 6 & 26 & 47\ (\text{奇}) & ✗\ \textbf{排除}\\
8 & 7 & 25 & 53\ (\text{奇}) & ✗\ \textbf{排除}\\
9 & 8 & 24 & 60 & ✓\ \text{允许}
\end{array}$$
$$\Longrightarrow\ \textbf{单个三重点、单个四重点被纯奇偶排除}\ ✓✓\ \Longrightarrow\ \text{最小违例需 }\ge2\ \text{个三重点（或 }m=5/6/9\ \text{型单点）}\ ✓$$
```

## §3 ⭐⭐ **战略发现：n=8 有"额外同余"可用**（改变路线优先级 ✓）

```
$$\text{此前 }n=10\ \text{的阻塞之一}: 10\equiv1\ (\mathrm{mod}\ 3)\ \Longrightarrow\ \textbf{Haas 2013 三进制 excess 同余不适用}\ ✗$$
$$\boxed{n=8=3\cdot3-1\equiv-1\ (\mathrm{mod}\ 3)\ \Longrightarrow\ \textbf{该同余在 n=8 适用}}\ ✓✓$$
$$\Longrightarrow\ \text{除了 }\mathrm{mod}\ 4\ \text{（本条 ✓），尚有 \textbf{Haas 型 mod 3 约束}可用 ⟹ 同余压缩是本线\textbf{最可期的桥梁}}\ ✓$$
$$\text{（这也解释了为何 }n=8\ \text{在文献中可解、而 }n=10\ \text{先天更难 ⟹ 与我们在 }n=10\ \text{的经验吻合}\ ✓）$$
```

## §4 六条路线 × 五问审计

```
$$\begin{array}{c|c|c|c|c|c}
\text{路线} & \text{入口（已证 ✓）} & \text{桥梁（缺的 lemma ✗）} & \text{技术} & \text{出口} & \text{可推广} & \text{类}\\
\hline
A\ \text{局部容量→刚性} & \delta_i\ge0,\ \sum_i\delta_i=32,\ \text{层预算} & \text{禁形组合（哪些 }\delta_i\ \text{不可共存）} & \text{组合+容量指纹} & b\le2\ (\text{直攻}) & \text{可能一般化} & \mathbf{A}\\
B\ \text{private point} & \text{minimality（须挂 }K(8,1)=32\ ✓） & \textbf{private-point lemma 本身} & \text{组合} & \text{骨架}\Rightarrow\text{较弱} & \text{部分} & \mathbf{B}\\
C\ \text{距离分层/同余} & A_i\ \text{分布}+\text{层恒等式} & \textbf{Haas mod 3 ＋ mod 4 约束} & \text{谱/LP/同余} & \text{profile 限制} & \text{强} & \mathbf{A}\\
D\ \text{双计数/excess} & \sum_x(b-1)=32\ ✓ & \text{集中度上界 32} & \text{incidence} & \text{同 A} & \text{中} & \mathbf{A/B}\\
E\ \text{反证+最小坏构型} & b\ge3\Rightarrow\delta\ge2\ ✓ & \text{局部种子→传播→容量冲突} & \text{组合+SAT 局部} & b\le2 & \text{中} & \mathbf{B/A}\\
F\ \text{计算→反向猜测} & \text{near-miss 指纹} & \text{把经验律升成 lemma} & \text{SAT/ILP+数据挖掘} & \text{lemma} & ? & \mathbf{C}
\end{array}$$
$$\text{类}: \mathbf{A}=\text{直攻核心缺口}\ ✓;\ \mathbf{B}=\text{提供桥梁}\ ✓;\ \mathbf{C}=\text{只给证据}\ ✗;\ \mathbf{D}=\text{可能重复旧墙}\ ✗$$
```

## §5 DAG（串联/并联/互验）

```
```
  ┌─ 距离分层/同余 (C) ──┐
  │                      │
P₀ ─ 覆盖/双计数 (D) ─────┼─► excess 集中度约束 ──► M1 (b≤2 结构定理)
  │                      │            │
  ├─ 局部容量/禁形 (A) ───┘            │
  │                                    ▼
  └─ b≥3 局部种子 (E) ──► 局部不可延拓 ──► M2 (有限 certificate ⟸ SAT/ILP)
                                        │
                                        ▼
                                   Q*(8)=0 ──► 机制抽取 ──► M3
```
```

## §6 三张状态表（每轮维护 ✓）

```
$$\textbf{CLOSED（已证 ✓）}: K(5,1)=7,\ K(6,1)=12,\ K(7,1)=16,\ K(8,1)=32\ \text{（文献+表 ✓）};\ E=32;\ \sum_i\delta_i(x)=32\ \forall x;\ \sum\delta^2\equiv0\ (\mathrm{mod}\ 4)\ ✓$$
$$\qquad\qquad \text{单三重点/单四重点不可行}\ ✓;\ Q\equiv E\ (\mathrm{mod}\ 2)\ ✓;\ \text{WLOG: 平移钉 }0^8\ ✓,\ \text{坐标置换规范型}\ ✓,\ \text{残块度数降序}\ ✓$$
$$\textbf{EVIDENCE（计算确认未证 ✗）}: \text{CP-SAT }900\text{s}/18.5\text{M conflicts 无可行解}\ ✓;\ \text{案 A/B 对称破缺版（进行中}\ ⏳);\ \text{doubled Hamming}\ Q=0\ \text{单例}\ ✓$$
$$\textbf{OPEN（真缺口 ✗）}: b\le2\ \text{的结构性理由}\ ✗;\ \text{Haas mod 3 在 }n=8\ \text{的具体形式}\ ✗;\ A_1+A_2\le16\ \text{的独立证明}\ ✗;\ private\text{-}point\ \text{lemma}\ ✗;\ \textbf{n=10, M=119}\ ✗$$
```

## §7 下一刀（按"关闭哪个 OPEN"排序 ✓）

```
$$\text{① \textbf{同余压缩}}（关闭 OPEN ②③）: \text{导出 Haas mod 3 在 }n=8,M=32,E=32\ \text{的显式约束}\ ✓\ \text{——最可期}\ ✓$$
$$\text{② 局部禁形}（关闭 OPEN ①）: \text{从 }\delta_i\ \text{层预算推"哪些局部型不可共存"}\ ✓$$
$$\text{③ 案 A/B 对称破缺}：若出 \textbf{UNSAT} ⟹ 升为 }M_2\ \text{级 certificate}\ ✓\ (\text{但须独立复核证书}\ ✓)$$
$$\text{④ private-point lemma}：独立证明，不得从 }|C|=32\ \text{单独推}\ ✗$$
```

## §8 边界（诚实标注）

- §2 为**手算+程序核验** ✓（`Σδ²≡−E mod 4` ✓，单点表 ✓）
- §3 的"Haas 适用性"为**我方判断** ✓（依据：该同余适用条件 n ≡ −1 mod 3 ✓，n=8 ✓）——**须逐字核对原文后**才可正式使用 ⚠️
- 求解器的 UNKNOWN **仅是证据** ✗；**未**排除任何 n ✗；**未**触碰 119 ✓

## 【技术词回查】（定稿前逐字输出）

```
技术词 证明路径地图 命中文件数=0    :: 
技术词 路径审计     命中文件数=0    :: 
技术词 excess 集中度 命中文件数=0    :: 
技术词 同余压缩     命中文件数=0    ::
```

- **本档新增**（命中数=0）：`证明路径地图`、`路径审计`、`同余压缩`、`excess 集中度`（含空格，回查解析器按首词匹配 ✓）
- **档案已有（引用，不列为提出）**：—
