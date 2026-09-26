已查地图：已跑 scripts/prework_map_check.sh A23-D4 blocker census ⟹ 执行自 A23D4-2026-09-26-P0-P1-P2-dossier 档；本档为**Step 2/3/5 实算报告**（唐先生 2026-09-26 18:52 询问 ✓）；**未跑 solver/SAT/CP-SAT** ✓（纯 bitset/枚举 ✓）。
D0: 本档对象 = C₀ 校验、全候选 blocker census（与论文三项基准对齐）、blocker 组结构、|S(D)| 分布、max α、枚举覆盖缺口
D1: 1（新增：**census 三项基准逐数字命中** ✓✓；**max |S(D)|=6 且 max α=4** ✓✓；**覆盖缺口精确刻画** ⚠️）

# A23D4-STEP235-2026-09-26

## §1 ✅ **C₀ 校验（数据源锁定 ✓）**

```
$$\text{源}: \texttt{https://aeb.win.tue.nl/codes/cwc/d6/a23.6.10.2969H}\ ✓\ (\$BASE=16,\ hex\ 5{-}8\ 位)\ ✓$$
$$|C_0| = \mathbf{2969}\ ✓;\quad \text{全部重量} = 10\ ✓;\quad \text{最小距离} = 6\ ✓\ (\text{合法 }(23,6,10)\ \text{码}\ ✓)$$
$$
$$

## §2 ✅✅✅ **全候选 blocker census：三项基准逐数字命中** ✓✓✓

```
$$\text{候选总数} = \binom{23}{10}-2969 = \mathbf{1{,}141{,}097}\ ✓\ (\text{论文同值}\ ✓✓)$$
$$\begin{array}{c|c|c}
\text{量} & \text{本档实测} & \text{论文} & \text{判定}\\ \hline
N_0\ (\text{零-blocker}) & \mathbf 0 & 0 & \checkmark\checkmark\\
N_{\le2} & \mathbf{1248} & 1248 & \checkmark\checkmark\\
N_{\le3} & \mathbf{7751} & 7751 & \checkmark\checkmark\\
N_{\le4} & \mathbf{30247} & 30{,}247 & \checkmark\checkmark\\
\end{array}$$
$$\Longrightarrow\ \textbf{独立重算与论文完全一致}\ ✓✓\ (\text{并给出论文未列的分解})$$
$$\boxed{N_1=\mathbf{70},\quad N_2=\mathbf{1178},\quad N_3=\mathbf{6503},\quad N_4=\mathbf{22496}}\ ✓\ (\text{论文只给累计值}\ ✓)$$
$$\text{完整分布}: \{1{:}70,\ 2{:}1178,\ 3{:}6503,\ 4{:}22496,\ 5{:}53701,\ 6{:}94419,\ 7{:}129502,\ 8{:}143544,\dots\}$$
$$
$$

## §3 ✅ **blocker 组结构 ＋ 引理 C 校验**

```
$$\text{精确组（不同 }B(s)\text{）数} = \mathbf{30117}\ ✓;\quad |B|{=}1{:}70,\ 2{:}1155,\ 3{:}6454,\ 4{:}22438\ ✓$$
$$\text{组内重数分布}: \{1{:}29992,\ 2{:}120,\ 3{:}5\}\ \Longrightarrow\ \textbf{组极小，最大重数仅 3}\ ✓✓$$
$$\textbf{引理 C 校验}\ (\text{B(s) 在 }G_8\ \text{中成团}): \textbf{违反 0}\ ✓✓\ (\text{严格结构定理实算确认}\ ✓)$$
$$
$$

## §4 ⭐⭐⭐ **Step 5：|S(D)| 与 α（可行族，~1920 万个 D）**

```
$$\textbf{枚举族}: \text{A} = \text{精确 4-组}\ (22438)\ ✓;\ \text{B} = \text{3-组}\cup\{x\}\ (19.16\text{M})\ ✓;\ \text{C} = \text{两个 2-组之并}\ ✓$$
$$|S(D)| = \sum_{\varnothing\ne B\subseteq D} g(B)\quad(\text{超集口径，正确}\ ✓)$$
$$\begin{array}{c|cccccc}
|S(D)| & 1 & 2 & 3 & 4 & \mathbf 5 & \mathbf 6\\ \hline
\text{D 数} & 15{,}337{,}823 & 3{,}479{,}963 & 308{,}579 & 35{,}027 & \mathbf{794} & \mathbf 6\\
\end{array}$$
$$\Longrightarrow\ \textbf{max }|S(D)| = \mathbf 6\ ✓;\quad |S(D)|\ge5\ \text{的 }D\ \text{仅}\ \mathbf{800}\ \text{个}\ ✓✓$$
$$\textbf{对这 800 个 }D\ \text{逐个建冲突图并求最大兼容族}: \boxed{\max\ \alpha = \mathbf 4\ <\ 5}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{这 800 个 }D\ \text{上\textbf{不存在} }|S|\ge5\ \text{的可行族}\ ✓\ \Longrightarrow\ \textbf{无 depth-4 正交换}\ ✓$$
$$
$$

## §5 ⚠️ **枚举覆盖缺口（精确刻画，诚实 ✓）**

```
$$\text{已覆盖}: D\ \text{含 4-组};\ D\ \text{含 3-组};\ D\ \text{含两个 2-组}（\text{union}=4）\ ✓$$
$$\textbf{未覆盖（2 族）}:$$
$$\qquad\text{(i) }D = (\text{两个 2-组},\ |\text{union}|=3)\cup\{x\}\ ✗$$
$$\qquad\text{(ii) }D = (\text{一个 2-组})\cup\{x,y\}\ ✗$$
$$\qquad\text{(iii) 仅单元素组}: \text{至多 4 个候选} \le4\ ✗\ \text{自动排除}\ ✓$$
$$\textbf{为何未覆盖}: \text{两族需枚举 } O(|G_2|\cdot M)\ \text{量级}\ \sim10^9\ ✗\ (\text{超出本轮预算}\ ⚠️)$$
$$\textbf{故严格结论}: \boxed{\text{在 \textbf{1920 万个已枚举 }D\ 上，depth-4 正交换不存在}}\ ✓✓\ \text{（非全量证明}\ ⚠️)$$
$$
$$

## §6 与论文的关系（定位 ✓）

```
$$\text{论文}: \text{depth-3 已证 infeasible}\ ✓;\ \text{depth-4 模型 (30247 candidates, ~888k pairs) \textbf{未闭合}}\ ⚠️$$
$$\text{本档}: \text{depth-4 问题被压成 \textbf{800 个候选 }D\ \text{状态}（每个 |S(D)|\le6）}\ ✓✓\ \text{且其中 \textbf{max }\alpha=4<5}\ ✓$$
$$\qquad\Longrightarrow\ \text{论文的 CP-SAT 表述（30247 变量）被替换为\textbf{有限 4-deletion 状态表的判定}}\ ✓✓$$
$$\text{收益口径（唐先生修正 ✓）}: \text{若最终全量闭合} \Longrightarrow \textbf{depth-4 局部最优性定理}\ ✓\ (\textbf{不是新下界}\ ✗)$$
$$
$$

## §7 下一步（待批 ✓）

```
$$\textbf{Step 6}: \text{补完 (i)(ii) 两族} —— \text{可行路径}: \text{对每个 2-组 }\{a,b\}\ \text{枚举 }(x,y)\ \text{但只取\textbf{与 }a,b\ \text{成边的 }x,y}（\text{即 2-组图的邻域}\ ✓)$$
$$\qquad\text{若 2-组图稀疏（度数小），则枚举量骤降至可行}\ ✓\ \Longrightarrow\ \text{完成全量} \Longrightarrow\ \text{定论}\ ✓$$
$$\textbf{Step 7}: \text{若全量 } \max\alpha\le4 \Longrightarrow \text{写出 depth-4 局部最优性定理（含完整 800+ 状态表作为 certificate）}\ ✓✓$$
$$
$$

## §8 边界（诚实标注）

- §1–§4 为**实算**（numpy bitset，无 solver ✓，总用时 <5 分钟 ✓）；§5–§6 为**范围刻画** ✓
- **未跑 SAT/CP-SAT/ILP** ✓；**未扩大模型** ✓
- 本条线与 G/119 **无关** ✓（独立新题 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 4-deletion 状态表 命中文件数=1    :: ./A23D4-STEP235-2026-09-26-census-and-alpha-results.md 
技术词 枚举覆盖缺口 命中文件数=1    :: ./A23D4-STEP235-2026-09-26-census-and-alpha-results.md 
技术词 max α 判定    命中文件数=1    :: ./A23D4-STEP235-2026-09-26-census-and-alpha-results.md
```
- **本档新增**（扣自引后 = 0）：4-deletion 状态表、枚举覆盖缺口、max α 判定
- **档案已有（引用，不列为提出）**：blocker、|S(D)|、G₈ clique
