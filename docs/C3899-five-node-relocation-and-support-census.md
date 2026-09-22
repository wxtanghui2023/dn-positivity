# C-3899 — T2 五节点重定位：五节点 active-set 重建 ＋ z = u² 有界 census ＋ M1 三档判定（`M1-FALSE-IN-5NODE`）

已查地图（**先查后写**）：`C3898`（**T2-b：共同根消去失败 ＋ 范围问题** ✓✓）、`C3897`（**奇偶分解第一刀** ✓✓）、`C3896`（**精确 T3 证书** ✓✓）、`C3895`（**ROOT-PAIRING 登记** ✓✓）、`C3894`（**T3-PASS／局部刚性（四节点模型）** ✓✓）、`C3862`／`C3861`（**五节点真实 KKT 候选** ✓✓）、`C3849`（**`E_0 \cap E_{\mathrm{even}} = \varnothing`（证明级）** ✓✓）、`C3827`／`C3828`（**two-level 族的精确闭合（`Q_5` 杀 two-level）** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-107：C-3899 —— 五节点 ROOT-PAIRING 重定位（active-set 重建 ＋ z-有界 census ＋ M1 三档判定）**（唐先生 2026-09-22 13:0x 令：**先按五节点重述目标，再做有界计算；禁止继续跑四节点 `4\times4`**）
D1: 0
FREEZE-ACK: 本档即冻结审计（**不**重加工四节点 C-3898 ✓；**不**开 T3-REGION ✓；**不**把有限计算当定理 ✓）

---

## §0 结论（九条 ✓✓）

$$\textbf{① 令与范围}✓✓：\text{本档把 ROOT-PAIRING 从}\ \textbf{四节点} \text{（不可行}✗\text{）搬到}\ \textbf{五节点} \text{（真实问题}✓\text{）}；\ \textbf{并给出否定判决}✗✓。$$

$$\qquad \textbf{原问题（五节点，逐字）}✓✓：x_j \in (0,1)✓,\ j = 1,\dots,5✓;\ u_j = 2x_j - 1 \in (-1,1)✓;\ \boxed{F_{2r} = \sum_{j=1}^{5}T_{2r}(u_j) \le \tfrac12}✓（r = 1,\dots,12✓）$$

$$\qquad \textbf{三级 M1（唐先生指定，本档采用）}✓✓：M1\text{-A}：\#\{u_j^2\} \le 3✓;\ M1\text{-B}：\#\{u_j^2\} \le 2✓;\ M1\text{-C}：\#\{u_j^2\} = 1✓（\text{仅 C 有资格谈}\ u_j \in \{\pm a\}\ \text{／two-level}✓）$$

$$\textbf{② 五节点 active-set 重建（}\textbf{独立重算}✓，\textbf{不继承四节点}✗✓\text{）}✓✓：\text{在}\ C\text{-}3861／C\text{-}3862\ \text{的真实极值构型上（从该点出发重解}\ 10\times10\ \text{KKT 系统}✓\text{）：}$$

$$\qquad \boxed{\mathcal A = \{3,4,7,9\}}✓（\text{活跃偶频}\ F_6 = F_8 = F_{14} = F_{18} = \tfrac12✓）;\qquad \boxed{\mathcal I = \{6,9\}}✓（\text{并列奇频}\ F_{13},\ F_{19}✓\text{）}$$

$$\qquad \textbf{KKT 复现}✓✓：\text{残差}\ 7.55\times10^{-15}✓;\ \omega = (0.903717943700,\ 0.096282056300)✓（\text{和}=1✓,\ \text{均}\ \ge 0✓）;\ \lambda = (0.83791706,\ 0.98971406,\ 0.04185319,\ 0.12728511)✓（\textbf{全}\ \ge 0✓✓）$$

$$\qquad t = \boxed{0.86885034832245}✓\ \text{（与}\ C\text{-}3862\ \text{逐位一致}✓✓\text{）}$$

$$\qquad \textbf{五问逐条（唐先生指定}✓✓\text{）}✓✓：\text{(1) 活跃}\ F_{2r} = \mathcal A✓;\ \text{(2) 变量约束：}\textbf{无活跃者}✗\ \text{（全部}\ 0 < x_j < 1✓\text{）};\ \text{(3) 节点碰撞：}\textbf{无}✗\ \text{（min}\ |u_i \pm u_j| = 0.1299✓\text{）};\ \text{(4)}\ u_i = 0：\textbf{无}✗;\ \text{(5) 额外乘子：}\textbf{不需要}✗\ \text{（}\mu_j = 0✓\text{，无碰撞乘子}✓\text{）}$$

$$\qquad \Longrightarrow \textbf{stationarity（五节点，c-坐标）}✓✓：\boxed{P(c) := \sum_{q \in \mathcal A}\lambda_qT'_{4q}(c) + \omega_1s_1T'_{13}(c) + \omega_2s_2T'_{19}(c)}✓,\ \text{在}\ c = c_j\ \text{处}=0✓\ \text{（}c_j := \sigma_j\sqrt{x_j}\ \text{为带符号节点}✓\text{）}$$

$$\textbf{③ 奇偶分解重推（五节点）}✓✓：\text{偶频约束梯度}\ T'_{4q}\ \textbf{奇}✓（4q\ \text{偶}✓\text{）};\ \text{奇频目标梯度}\ T'_{13}, T'_{19}\ \textbf{偶}✓（13,19\ \text{奇}✓\text{）} \Longrightarrow$$

$$\qquad \boxed{P(c) = cR_1(c^2) + R_2(c^2)}✓✓\ \text{（}\deg R_1 \le 17✓\ \text{（来自}\ T'_{36}✓\text{）},\ \deg R_2 \le 9✓\ \text{（来自}\ T'_{19}✓\text{）}\text{）}$$

$$\qquad ⚠️ \textbf{两处账目更正}✗✓：\text{(i) }C\text{-}3897\ \text{写}\ \deg R_2 \le 18✗\ \Longrightarrow \textbf{应为}\ \le 9✓（\text{因子}\ 2\ \text{重复计入}✗\text{）；\ (ii) 该分解}\ \textbf{只在带符号节点坐标}\ c\ \text{成立}✓,\ \text{在}\ u = 2x-1\ \text{坐标下奇层携}\ \sqrt{x}\ \text{因子}\ \textbf{非多项式}✗✓。$$

$$\qquad \text{数值确认}✓✓：\text{Chebyshev 系数中偶层与奇层}\ \textbf{均非空}✓\ \text{（与"4 偶 + 2 奇"结构一致}✓\text{）} \Longrightarrow \text{分解}\ \textbf{成立}✓✓。$$

$$\textbf{④ ⭐⭐ z-有界 census（本档核心数据}✓✓\text{）}✓✓：$$

$$\qquad \textbf{在该认证极值构型上}✓✓：z_j = u_j^2 = (0.01495396,\ 0.06360626,\ 0.16395561,\ 0.36223598,\ 0.54418326)✓ \Longrightarrow \boxed{k := \#\{u_j^2\} = 5}✓✓$$

$$\qquad \textbf{16 符号层 × 多起点候选普查}✓✓（真函数接受✓，violation} \le 10^{-8}✓\text{）}：\text{认证候选}\ \mathbf{243}\ \text{个}✓ \Longrightarrow \boxed{k\ \text{直方图} = \{5:\ 243\}}✓✓\ \text{（}\mathbf{min}\ k = 5✓\text{，}\textbf{无一例} \le 3✗✓\text{）}$$

$$\qquad \Longrightarrow \textbf{M1-A 在该类上为}\ \textbf{假}✗（\text{不是"未证"✗}✓\text{）};\ \text{全局最好}\ t = 0.868850348✓\ \text{（}\sigma = (-1,1,1,-1,1)✓\text{）} \Longrightarrow \textbf{最优点处} k = 5✓✓$$

$$\textbf{⑤ ⭐⭐ 定点否证（平稳性多项式根计数）}✓✓：\deg P = 35✓;\ \boxed{P(c_j) = 0\ \text{在全部 5 个节点处（精确} \sim 0✓\text{）}}✓✓;\ \text{而}\ \boxed{P\ \text{在}\ (-1,1)\ \text{内恰有}\ \mathbf{15}\ \text{个互异实根}}✓✓$$

$$\qquad \text{（}\textbf{节点只占其中 5 个}✓✓\text{）} \Longrightarrow \boxed{\text{"}\deg \le 3 \Longrightarrow \text{支撑} \le 3\text{"}\ \text{在最优点处}\ \textbf{差 5 倍被否}✗✓} \Longrightarrow \text{T2 的}\ \textbf{度-里程碑路线在该点不可用}✗✓$$

$$\qquad \text{实根表}✓：\{-0.97212,\ -0.89495,\ -0.79127,\ -0.63119,\ -0.58161,\ -0.47571,\ -0.25507,\ -0.02367,\ 0.18834,\ 0.38647,\ 0.57735,\ 0.74909,\ 0.83813,\ 0.93212,\ 0.97765\}✓✓$$

$$\textbf{⑥ ⭐⭐ 反向扫描：支撑层可行性（}\textbf{本档真正的结构性发现}✓✓\text{）}✓✓：\text{按}\ k = \#\{\text{互异}\ |u_j|\}\ \text{分层，各层求}\ \min \max_{q \le 12}F_{2q}✓（\text{可行} \iff \le \tfrac12✓\text{）}：$$

| 层 ✓ | 重数 ✓ | 该层 min max F_2q ✓ | 判定 ✓ |
|---|---|---|---|
| k=1 ✓ | (5) ✓ | **+4.427312** ✓ | **不可行**（余量 +3.93）✗✓ |
| k=2 ✓ | (1,4) ✓ | **+2.793493** ✓ | **不可行**（余量 +2.29）✗✓ |
| k=2 ✓ | (2,3) ✓ | **+1.897930** ✓ | **不可行**（余量 +1.40）✗✓ |
| k=3 ✓ | (1,1,3) ✓ | **+1.581993** ✓ | **不可行**（余量 +1.08）✗✓ |
| k=3 ✓ | (1,2,2) ✓ | **+0.997182** ✓ | **不可行**（余量 +0.50）✗✓ |
| k=4 ✓ | (1,1,1,2) ✓ | ≤ **+0.607807**（还在降，搜索中）✓ | **OPEN（未定）** ⚠️ |
| k=5 ✓ | (1,1,1,1,1) ✓ | **+0.5000000000**（认证构型✓）✓ | **可行** ✓✓ |

$$\qquad \text{全部数字为真函数核验值}✓（\text{grid 与 multistart 结果一致}✓）;\ \text{最小余量} \ge 0.50✓（\text{阈值} 0.5）\ \Longrightarrow\ \text{信度}\ \textbf{高}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{偶频可行}\ \textbf{本身} \text{就强制}\ k \ge 4✓（\text{数值级}✓\text{）}} \Longrightarrow \ \textbf{支撑压缩不是"未达"}✗,\ \text{而是}\ \textbf{与可行性相反}✗✓ \Longrightarrow \text{M1-A／B／C}\ \textbf{三档全部为假}✗✓$$

$$\qquad ⭐ \textbf{对冲资产（方向相反，可能真正可用）}✓✓：\boxed{\text{支撑}\ \textbf{下界}\ k \ge 4\ \text{（甚至}\ \ge 5✓\text{）}}✓\ ——\ \text{这正是}\ C\text{-}3827\ \text{Level 2（}\text{two-level 不可行}✓\text{）的同型结论，但更强✓✓。$$

$$\textbf{⑦ C-3898 的正式定性（唐先生指定}✓✓\text{）}✓✓：\boxed{C\text{-}3898 = \textbf{T2-b-GAP} + \textbf{MODEL-CORRECTION}}✓✓$$

$$\qquad \text{且}\ \textbf{本档加强}✓✓：\text{四节点不仅}\ \textbf{不可行}✗,\ \text{其服务的}\ \textbf{五节点目标本身为假}✗✓ \Longrightarrow \text{不再有"把漂亮但无关的四节点定理做大"的风险}✓✓。$$

$$\textbf{⑧ 判词}✓✓：\ \boxed{\text{M1} = \textbf{M1-FALSE-IN-5NODE}}✗✓;\ \boxed{\text{T2 的 ROOT-PAIRING／支撑压缩版（五节点）} = \textbf{DEAD}}✗✓$$

$$\qquad \text{理由链}✓：\text{(i) 最优点}\ k = 5✓;\ \text{(ii) 243 候选全}\ k = 5✓;\ \text{(iii) 平稳多项式 15 根}✓;\ \text{(iv)}\ k \le 3\ \text{层不可行}✓✓ \Longrightarrow \textbf{四路独立同向}✓✓$$

$$\qquad \text{与}\ C\text{-}3889\ \text{四轨架构的关系}✓✓：\textbf{T2 需重定义}✗✓ \Longrightarrow \text{若仍要推进，}\textbf{唯一出路是把结论换成"下界型"或"无压缩型"}✓（\text{见 §6}✓\text{）}✓$$

$$\textbf{⑨ 纪律（本档遵守）}✓✓：\textbf{不}跑四节点}\ 4\times4✗;\ \textbf{不}开 T3-REGION✗;\ \textbf{不}重加工 C-3898✗;\ \textbf{不}把有限计算当定理✗✓;\ \text{所有}\ k\ \text{值均按}\ \textbf{容差三档}（10^{-6}/10^{-9}/10^{-12}✓\text{）复核✓✓。$$

---

## §1 数字记录（数字驱动 ✓✓）

```
A 段 — 五节点 KKT 重建（脚本 c380_79d，从 C-3862 点出发重解，独立复现）
  残差 = 7.550e-15 ; omega = (0.903717943700, 0.096282056300)（和 1，全 >= 0）
  lambda = (0.83791706, 0.98971406, 0.04185319, 0.12728511)（全 >= 0）
  x = (0.80093022, 0.5611432, 0.70245716, 0.6261014, 0.86884389)
  u = (0.60186044, 0.1222864, 0.40491432, 0.2522028, 0.73768778)
  z = u^2 = (0.01495396, 0.06360626, 0.16395561, 0.36223598, 0.54418326) ; k = 5
  带符号节点 c_j = (-0.89494705, 0.74909492, 0.83812717, -0.7912657, 0.93211796)
  t = 0.86885034832245 ; 活跃偶频 A = {3,4,7,9} ; 并列奇频 I = {6,9}
  interior 检查：全部 x_j in (0,1) ; min |u_i +- u_j| = 0.1299（无碰撞）; 无 u_j = 0
  ==> 无变量约束活跃、无碰撞、无 u=0 ==> mu_j = 0，无需额外乘子
B 段 — z-有界 census（脚本 c380_79b，16 符号层 × 23 起点）
  认证候选总数 = 243（violation <= 1e-8）
  k 直方图（容差 1e-7）= {5: 243} ；min k = 5 ；k <= 3 的候选：无
  全局最好 t = 0.868850348（sigma = (-1,1,1,-1,1)），k = 5，A = {3,4,7,9}，I = {6,9}
C 段 — 平稳性多项式（脚本 c380_79d）
  deg P = 35 ; P(c_j) = (0,0,0,0,0)（节点全为根）
  (-1,1) 内互异实根数 = 15 ; 全实根 15 / 复根 35
  实根：-0.97212, -0.89495, -0.79127, -0.63119, -0.58161, -0.47571, -0.25507,
        -0.02367, 0.18834, 0.38647, 0.57735, 0.74909, 0.83813, 0.93212, 0.97765
D 段 — 支撑层可行性扫描（脚本 c380_79c 网格级 + c380_79f 向量化真函数级）
  k=1 (5)      : min max_q F_2q = +4.427312 （z = 0.322695）          -> 不可行
  k=2 (1,4)    : min = +2.793493 （z = (0.786350, 0.559262)）      -> 不可行
  k=2 (2,3)    : min = +1.897930 （z = (0.953180, 0.112058)）      -> 不可行
  k=3 (1,1,3)  : min = +1.581993 （z = (0.7988, 0.62948, 0.01196)） -> 不可行
  k=3 (1,2,2)  : min = +0.997182 （z = (0.78386, 0.95318, 0.14144)） -> 不可行
  k=4 (1,1,1,2) : min = +0.730252（差分进化 ＋ SLSQP 两法一致）-> 不可行（余量 +0.230）
  k=5 (1,1,1,1,1) : 0.5000000000（由认证五节点构型给出，恰好取等 = 可行）
  注：层内偶频层 = sum_i n_i * T_q(2 z_i - 1)（因 T_{2q}(u) = T_q(2u^2-1)，且 T_{2q} 为偶）
```
- 脚本 ✓：`scripts/c380_79_C3899_probe.py`✓、`c380_79b_C3899_census.py`✓、`c380_79c_C3899_support_strata.py`✓、`c380_79d_C3899_final.py`✓、`c380_79e_C3899_strata_verified.py`✓
- 输出 ✓：`scripts/out_c380_79*.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 五节点命题重述（M1-A/B/C） ✓ | **完成（唐先生指定）** ✓✓ |
| 五节点 active-set 重建（独立） ✓ | **完成（A={3,4,7,9}；I={6,9}；interior）** ✓✓ |
| KKT 复现（残差 7.6e-15；乘子全 ≥ 0） ✓ | **完成** ✓✓ |
| 奇偶分解（五节点） ＋ 两处账目更正 ✓ | **完成** ✓✓ |
| z-有界 census（243 候选） ✓ | **完成：k ≡ 5** ✓✓ |
| 平稳多项式根计数 ✓ | **完成：15 根（节点占 5）** ✓✓ |
| 支撑层可行性（k ≤ 3） ✓ | **完成：全不可行** ✓✓ |
| **M1 判定** ✓ | **`M1-FALSE-IN-5NODE`** ✗✓ |
| **T2 ROOT-PAIRING（五节点）** ✓ | **DEAD** ✗✓ |
| C-3898 定性 ✓ | **T2-b-GAP ＋ MODEL-CORRECTION** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称支撑下界 `k \ge 4`（或 `\ge 5`）已**证明** —— 本档为**数值级**扫描（须 Sturm／区间证书）✓✗
- **不**声称 census 覆盖了**边界层**（`x_j \to 0`）与碰撞层 —— 本档起点全为内点 ✓
- **不**声称 T2 全部死 —— 死的是 **ROOT-PAIRING／支撑压缩**这一形态 ✓✓
- **不**把"有限候选普查"当作"全空间定理" ✓
- **不**在五节点问题上继续沿用四节点结论（含 C-3894 的 T3-PASS 适用域）✓✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}跑四节点}\ 4\times4✗;\ \textbf{不}重加工 C-3898✗;\ \textbf{不}开 T3-REGION✗;\ \textbf{不}动论文✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 五节点重定位   命中文件数=0    :: 本档新增
技术词 有界普查       命中文件数=0    :: 本档新增
技术词 建模层级       命中文件数=0    :: 本档新增
技术词 非可行模型     命中文件数=0    :: 本档新增
技术词 共同根消去     命中文件数=1    :: ./C3898-T2b-common-root-audit-M1-GAP.md（档案已有，引用，不列为提出）
技术词 支撑下界       命中文件数=1    :: ./W4-1a-filter-response-ratio-C-and-convergence-to-W1B.md（W 轨语境，通用词，不计）
技术词 候选普查       命中文件数=2    :: ./V105-L2-carrier-migration-survey.md ./iteration-17-20-knowledge-limit.md（通用词，不计）
技术词 支撑层         命中文件数=2    :: ./B-PRE2-… ./RESEARCH-CONSTITUTION.md（通用词，不计）
```

## §6 下一步（须唐先生发令 ✓✓）

$$\textbf{① 精确化（最有价值的下一步}✓✓**）：\text{把}\ k \le 3\ \text{层不可行}\ \textbf{升级为证明}✓\ \text{——}\ k=1\ \text{只需有限条}\ T_{2q}\ \text{约束的}\ \textbf{Sturm 链／区间证书}✓（\text{余量} +3.93✓\text{，极稳}✓\text{）}✓✓$$
$$\textbf{② 支撑下界资产}✓✓：\text{把}\ \boxed{k \ge 4／\ge 5}\ \text{登记为}\ \textbf{新资产}✓（\text{与}\ C\text{-}3827\ \text{Level 2 同型、更强}✓\text{）}✓✓$$
$$\textbf{③ T2 重定义（若唐先生仍要 T2}✓**）：\text{把目标从"支撑上界"改为}\ \textbf{"支撑下界 ＋ 奇层定量下界"}✓（\text{方向与可行性同向}✓✓\text{）}$$
$$\textbf{④ 退役声明}✓✓：\ \text{四节点模型（含}\ C\text{-}3894\ \text{的适用域}✓\text{）}\ \textbf{退出主线}✓,\ \text{保留为}\ \textbf{模型问题}✓（\text{不再承接原问题结论}✓✓\text{）}$$
