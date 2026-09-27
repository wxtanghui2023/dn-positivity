# P1-SCREEN-2026-09-27 — **C-418 预筛门**（机械可执行）＋ **首轮过门筛**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 23:17 令 ✓）**：把"候选量必须在 degree profile 之外"硬化成**预筛门**；并对候选族做首轮过门筛；零程序计算 ✓。

**已查地图：命中（接续 C-417／P1-COV／C-409，非新案 ✓）**
`docs/P1-COV-2026-09-27-…`（**球面恒等式族／度数决定判定** ✓✓）｜`docs/P1-AVOID-2026-09-27-…`（**占用恒等式与 $\{n_j\}$ 同源** ✓✓）｜`docs/R7-LOCK-2026-09-27-…`（**profile 层 STOP** ✓✓）｜`docs/P1-D4b-…`｜`docs/R2-2-2026-09-27-…`（**自由坐标引理** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，**已分线**，见 §5）
D0: 本档对象 ＝ **档案已有** 筛查判据（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次把"候选量必须在 degree profile 之外"固化为机械预筛门 ＋ 首轮过门筛（含被门拦下的既有量）** ✓）
**[RESEARCH]**

---

## §0 结论（**门已固化 ✓✓｜首轮筛选完成 ✓｜未产生新约束 ⚠️**）

$$\boxed{\textbf{(1) C-418 预筛门（机械 ✓✓）}:\ \textbf{候选量 }Q\ \text{若由\textbf{逐位置度数多重集}}\ \big\{(d_1(c),\dots,d_{10}(c))\big\}_{c\in C}\ \text{或其任何聚合（}\{N_j\}\text{、}\{n_j\}\text{）决定} \Longrightarrow \textbf{直接 STOP}✗}$$
$$\qquad\textbf{（附注 ✓）}:\ \text{由 C-417 的恒等式族，}\{E_k(c)\}\ \text{已由逐位置度数决定} ⟹ \text{"球面超额"族被\textbf{强读法即拦下}✓✓;\ C-409 的占用族亦同 ✓}$$
$$\boxed{\textbf{(2) 正向必需判据（至少满足其一 ✓）}:\ \text{① 交叉结构};\ \text{② 关联结构（二阶/高阶关联矩阵、共同邻居分布 ✓）};\ \text{③ 谱/特征值信息};\ \text{④ 覆盖映射的非均匀性（witness 重叠拓扑 ✓）};\ \text{⑤ 全局拓扑/同调类 ✓}}$$
$$\boxed{\textbf{(3) 首轮过门筛结果 ✓}:\ \text{① }\textbf{内部见证计数}\ \text{PASS}✓;\ \text{② }\textbf{码字交图的谱}\ \text{PASS}✓;\ \text{③ }q_{ij}\ \text{支撑指纹 PASS 门但受\textbf{自由坐标引理}限制}✗;\ \text{④ }\sum_{w\in C}\binom{b(w)}2\ \textbf{被门拦下}✗✓;\ \text{⑤ 同调类：待自建 ⚠️}}$$
$$\boxed{\textbf{(4) 诚实 ⚠️}:\ \text{本档\textbf{未}产生新约束}✗;\ \text{产出＝\textbf{门}＋\textbf{短名单}}✓}$$

---

## §1 **预筛门的定义**（**机械可执行 ✓✓**）

$$\textbf{输入 ✓}:\ \text{候选量 }Q\ \text{（对任意 119-cover 定义 ✓）及其\textbf{定义式}}$$
$$\textbf{判定 ✓（三步）}:\quad\textbf{S1}:\ Q\ \text{是否仅依赖 }\{(d_j(c))\}\ \text{（逐位置度数）或 }\{N_j\}\text{／}\{n_j\}\ \text{？}\ \text{是} \Longrightarrow \textbf{STOP}✗$$
$$\qquad\textbf{S2}:\ \text{否} \Longrightarrow Q\ \text{是否依赖\textbf{码字的排列方式}（哪些码字在何处 ✓）、交叠模式、或谱数据？是} \Longrightarrow \textbf{PASS 门}✓$$
$$\qquad\textbf{S3}:\ \text{PASS 门后仍须过 }\textbf{范围闸}:\ Q\ \text{是否在近最优区间 }119\le|C|\le123\ \text{可取到？（自由坐标引理限制 ✓）}$$
$$\textbf{STOP 依据（已登记 ✓✓）}:\ \text{① C-409：占用类量与 }\{n_j\}\ \text{同源}✗;\ \text{② C-417：球面超额 }\leftrightarrow\ \text{度数\textbf{完备线性关系}}✗;\ \text{③ R7-LOCK：profile 层 STOP}✗$$

## §2 **已确认被拦下的族**（登记 ✓）

$$\textbf{① }b\text{-profile 族}:\ \{n_j\}\ \text{及其一切函数（含 }b\ \text{矩、球面超额 ✓）} \Longrightarrow \text{STOP}✗;\qquad \textbf{② 占用/度数族}:\ \sum_c|S(c)\cup V(H_c)|\text{、}d_j(c)\ \text{的聚合} \Longrightarrow \text{STOP}✗$$
$$\textbf{③ 球面超额族}:\ \{E_k(c)\}\ \text{（C-417 逐位置度数决定 ✓）} \Longrightarrow \text{STOP}✗;\qquad \textbf{④ 距离分布族}:\ \{N_j\}\ \text{及其线性函数} \Longrightarrow \text{STOP}✗$$
$$\Longrightarrow\ \text{故"再做一次球面/占用/profile 型计数"已\textbf{结构性排除}✓（照唐先生 23:17 ✓）}$$

## §3 **首轮过门筛**（**逐候选 ✓**）

$$\textbf{① 内部见证计数（PASS 门 ✓）}:\ N_{\rm int}(c):=\#\{T\subseteq S(c):|T|=3,\ \text{其见证含于 }S(c)\}\ \big(\text{P1-G2 §2 情形 B ✓}\big)$$
$$\qquad\text{依赖"哪些三元组被内部块覆盖"\ ⟹ \textbf{排列级}✓\ \text{非度数决定}✓ \Longrightarrow \textbf{PASS}✓;\ \text{且直接绑定 C-415 的逃逸口 ✓（下一个最自然的量 ✓）}$$
$$\textbf{② 码字交图的谱（PASS 门 ✓）}:\ \text{取 }G_2(C)\ \text{（码字为顶点、距离}\le2\ \text{连边 ✓）之邻接谱 }\{\lambda_i\}✓$$
$$\qquad\text{由 }N_1,N_2\ \text{只能得边数，\textbf{不能}定谱 ✓} \Longrightarrow \textbf{PASS}✓;\ \text{且支持层信息（P12-PASS 的三例同 }A\text{、异 }J_7\ \text{✓）正是谱型分离 ✓}$$
$$\textbf{③ }q_{ij}\ \text{支撑指纹（PASS 门，但被范围闸拦 ✗）}:\ \text{已证非 }A\text{-data 决定（P12-PASS，}n=8\ ✓），\text{且可升到 }n=10\（\text{R2-2 提升引理 ✓}\big)$$
$$\qquad\textbf{但}:\ \text{由\textbf{自由坐标引理}（R2-2 §3 ✓）}:\ C=D\times\mathbb F_2\ \text{型分解} \Longrightarrow |C|\ge2K(9,1)=124 \Longrightarrow \text{近最优区间}\ 119\text{–}123\ \textbf{不可达}✗✓ \Longrightarrow \textbf{STOP（范围）}✗$$
$$\textbf{④ }\sum_{w\in C}\binom{b(w)}2\（\textbf{被门拦下 ✗✓}）:\ b(w)=1+d_1(w) \Longrightarrow \text{该量由逐位置 }d_1\ \text{多重集决定} \Longrightarrow \textbf{STOP}✗✓$$
$$\qquad\textbf{（示范 ✓）}:\ \text{此例正是"看起来像二阶（共同邻居总数 ✓）实为度数函数"的\textbf{陷阱}，门有效拦下 ✓✓}$$
$$\textbf{⑤ 同调类（待自建 ⚠️）}:\ \text{须先给出 119-cover 特异的复形（如见证超图／码字交复形 ✓）};\ \text{空谈"同调类"不过门 ✓}$$

## §4 **短名单**（登记未做 ✓）

$$\textbf{优先级 ✓}:\ \text{① }\boxed{N_{\rm int}(c)\ \text{（内部见证计数 ✓ PASS 门 ✓ 且绑定逃逸口 ✓）}};\ \text{② }G_2(C)\ \text{谱（PASS ✓ 但须找其与 119 约束的接口 ⚠️）};\ \text{③ 见证超图的同调（待建 ⚠️）}$$
$$\textbf{通用纪律 ✓}:\ \text{任何新候选先过 §1 门；}\textbf{不得}先推导再发现只是 profile 恒等式 ✗（照唐先生 23:17 ✓）}$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "预筛门" "二阶关联" "共同邻居" "关联矩阵" "同调类"
技术词 预筛门        命中文件数=1    :: ./RESEARCH-CONSTITUTION.md
技术词 二阶关联      命中文件数=2    :: ./ASSETS-REGISTRY.md ./R3-2026-09-27-coordinate-labelled-excess-and-the-no-go-test.md
技术词 共同邻居      命中文件数=1    :: ./FIBER-2026-09-26-boolean-fiber-and-the-third-order-invariant.md
技术词 关联矩阵      命中文件数=4    :: ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./C325-Barker-cross-object-mechanism-ontology-audit.md ./T3MIN1-2026-09-26-minimal-three-point-psd-attack.md
技术词 同调类        命中文件数=6    :: ./E4-3-R3-B1-complement-carrier-mechanism-audit.md ./V211-finite-infinite-anomaly-audit-taxonomy-and-self-kill.md ./CLOSED-ROUTES-MAP.md
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 预筛门 | 1（`RESEARCH-CONSTITUTION.md` ✓） | 0 | 0（既有词 ✓） |
| 二阶关联 | 2（`ASSETS-REGISTRY.md`／`R3-…` ✓） | 0 | 0（既有词 ✓） |
| 共同邻居 | 1（`FIBER-2026-09-26-…` ✓） | 0 | 0（既有词 ✓） |
| 关联矩阵 | 1（`TOPIC-DOSSIER-v1` ✓） | 3（`C325-…`／`T3MIN1-…`／`CLOSED-ROUTES-MAP` **属线未定 ⟹ 不计** ✗） | 0（既有词 ✓） |
| 同调类 | 0 | 6（`E4-3-R3-B1`／`V211`／`UNIFY-7MILLENNIUM` 等 **空间 A** ✗ ＋ 共享档 2 ✓ 不计） | 0（既有词 ✓） |

- **本档新增**：**0** 个术语 ✓（五词皆既有 ✓；`同调类` 的 6 档命中**全为空间 A／共享档** ⟹ 不计 ✗ ✓）
- **注 ✓**：本档实质＝**§1 门定义 ＋ §2 已拦族 ＋ §3 首轮过门筛**（判据性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门（指 closure gate／nogo gate ✓）** ✓；**不跨空间**（§5 已分栏 ✓）
- **本档未产生新约束** ✗（诚实 ✓）；**不声称** P1 成立 ✗（V290）；**不声称** 短名单中任一项有效 ✗
- **C-418 为\*\*筛查判据\*\*，非新数学命题** ✓（照唐先生 23:17 定位 ✓）；若唐先生要求，可将其并入 `closure_gate` 体系（须显式批准 ⚠️）
