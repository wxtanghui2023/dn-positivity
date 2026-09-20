已查地图（**先查后写**）：查 `C-212`（乙）、`C-210`（勘误 E1）、`C-211`（甲）、`C-201`／`C-203`／`C-205`／`C-206`／`C-207`（受影响各档）。回查见 §6 ✓

D0: 本档对象 = **乙-2 舍入余量收尾**（两条独立实现）＋ **甲：C-201～C-207 定量账本统一修订**（勘误 E1 的逐档落实 ＋ 三层区分）—— 关系 = 勘误落实 ＋ 账本封口
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 乙-2 收尾：显式舍入余量（两条独立实现交叉）

$$\text{impl A}（\text{均值形式}）：|\cos(a\pi)-\cos(a\pi_{\rm mid})|\le a\cdot\delta\pi/2✓ \ \textbf{＋ 逐项 slack}\ 10^{-130}✓✓$$
$$\text{impl B}（\texttt{mpmath.iv}\ \text{区间算术}）：\pi\in[\pi_{\rm lo}-10^{-150},\ \pi_{\rm hi}+10^{-150}]✓（\text{吃掉端点转换误差}✓）；\cos\ \text{直接取区间}✓$$
$$\qquad \text{工作精度}：\mathrm{dps}=220✓,\ \mathrm{iv.prec}=500✓$$

$$\textbf{结果}：两实现逐}\ k\ \text{的}\ U_k\ \text{差}\le6.8\times10^{-100}✓（\text{同量级于区间宽度}✓ \Longrightarrow \text{一致}✓）$$
$$\qquad U_{\rm new}^{\rm safe}(\text{A})=U_{\rm new}^{\rm safe}(\text{B})=0.764081100745853885147562674721✓（k=1✓）$$

$$\boxed{\ U_{\rm new}^{\rm safe}=0.76408110074585388514756267472105✓✓\ }$$
$$\qquad \text{检查}\ U_{\rm new}^{\rm safe}<0.7640811007458538851475626748 \Longrightarrow \textbf{True}✓（\text{裕量}\ 7.895\times10^{-29}✓）$$
$$\qquad \text{对照旧认证上界}\ 0.76408110090337578 \Longrightarrow \text{改进}\ 1.575\times10^{-10}✓$$

$$\boxed{\ \textbf{最终账本}：0.76\ \le\ m_3\ \le\ 0.76408110074585388514756267472105\ }✓✓$$

## §1 甲：旧账本统一修订（勘误 E1 的逐档落实）

$$\textbf{受影响的错误}（\texttt{C-210}\ §0）：\ \max_k(a_k+b_k)\ge\max_ka_k+\max_kb_k\ ✗✗$$
$$\qquad \textbf{统一替换为}：\ \boxed{F(x+\delta)\ \ge\ F(x)-\delta_A+c\|\delta\|-\tfrac R2\|\delta\|^2}✓✓,\qquad \delta_A=F(x)-\min_{k\in A}S_k(x)✓$$

| 档 | 受影响论断（原文 ✗） | 更正后 ✓ | 现行状态 |
|---|---|---|---|
| `C-201` | "Type-A 入口 = $\vert A\vert=4\wedge\mathrm{rank}\Delta=3\wedge c>0$" ✗ | 追加 $\delta_A$ 项且要求 $\rho_{\rm lower}<\rho_{\rm upper}$ ✓；并须紧容差 or 用自洽性检验 ✓ | **判据已更正** ✓ |
| `C-203` | "对 $\|\delta\|\le2.2503\times10^{-3}$ 有 $F\ge F(x_0)+0.273110304\|\delta\|$" ✗ | 严格上升区间改为 $(\rho_{\rm lower},\rho_{\rm upper}]$ ✓；$0<\|\delta\|\le\rho_{\rm lower}$ 内不声称 ✓ | **定量界更正** ✓ |
| `C-205` | 三簇并列表同型 ✗ | 补 $\delta_A$／$\rho_{\rm lower}$ 列 ✓（见 §2 表） | **定量界更正** ✓ |
| `C-206` | 抽象命题第②步用超可加 ✗；facet 法未验"0 在内" ✗ | ②改为 $\max_k(a_k+b_k)\ge\min_ka_k+\max_kb_k$ ✓；containment 用 $\lambda>0$ 线性解作证书 ✓ | **命题已更正** ✓ |
| `C-207` | 连续族排除用容差型 $\max_{k\in A}$ ✗ | 须用【精确 active 集】✓；真极小点处四项精确相等 ✓ ⟹ 结论不变 ✓ | **论证已更正** ✓ |
| `C-208`／`C-209` | 分类用固定 $10^{-5}$ 容差 ✗ | 容差须匹配收敛质量 ＋ 追加自洽性检验 ✓；四项硬输出不变 ✓ | **判据已更正** ✓ |
| `C-211` | （更正后实施）✓ | 已用更正形式 ✓ | **即为正确版本** ✓ |
| `C-212`／本档 | （生效）✓ | 上界证书与 KKT 解耦 ✓✓ | **严格** ✓ |

## §2 ⭐ 三层区分（唐先生要求：严格已证／数值自洽性／未覆盖）

$$\textbf{层 1 —— 严格已证}✓✓（\text{依赖：}\pi\ \text{的标准位数 ＋ mpmath 正确性 ＋ 初等推导}✓）$$
$$\qquad \text{① 上界}：m_3\le0.76408110074585388514756267472105✓（\text{合法有理构型}✓）$$
$$\qquad \text{② 下界}：m_3\ge0.76✓（\texttt{C-195}\ \text{区间算术四门}✓）$$
$$\qquad \text{③ 初等结果}：\text{Lemma C}\ (M{=}1)✓、\text{pigeonhole 定理}✓、\text{covering 引理}✓、\text{Case A}✓、\text{周期单调性引理}✓、\text{近似周期引理}✓、m_M\le M-1\ (2\le M\le11)✓、\lambda_{\max}=2-\sqrt3✓、\kappa_N\ \text{等号集}✓$$

$$\textbf{层 2 —— 数值自洽性审计}✓（\text{可引用，但须注明是数值}✓）$$

| 簇 | $c$（facet） | $\delta_A$ | $\rho_{\rm lower}$ | $\rho_{\rm upper}$ | 球内采样 $\Delta F$ | 下降 $\Delta F$ |
|---|---|---|---|---|---|---|
| 0 | $0.540247961$ | $9.269\times10^{-8}$ | $1.7157\times10^{-7}$ | $1.465756\times10^{-3}$ | $+3.916\times10^{-5}$ | $+7.772\times10^{-15}$ |
| 3 | $1.218503802$ | $1.603\times10^{-12}$ | $1.3157\times10^{-12}$ | $2.050227\times10^{-4}$ | $+1.481\times10^{-5}$ | $+4.992\times10^{-11}$ |
| 5 | $0.750466653$ | $3.440\times10^{-12}$ | $4.5841\times10^{-12}$ | $1.858471\times10^{-3}$ | $+7.435\times10^{-5}$ | $+1.787\times10^{-14}$ |

$$\qquad \text{另属层 2}：\text{census 四项硬输出}✓、\text{KKT／rank 数据}✓、\text{盆地捕获校准}✓、\text{自洽性检验（否决型）}✓$$

$$\textbf{层 3 —— 尚未覆盖}✗（\text{明确列出，避免误引用}✓）$$
$$\qquad \text{① 每簇的极小半径区}：(0,\ \rho_{\rm lower}]✓（\delta_A\ \text{控制跌幅}✓，但无严格上升}✗）$$
$$\qquad \text{② 簇间空档}：[\rho_{\rm upper},\ 0.4425]✓（\text{三簇两两距离}2.359／0.4425✓）\textbf{无任何证书}✗$$
$$\qquad \text{③ 全局缺口}：m_3\in[0.76,\ 0.7640811\ldots]✓ \text{ 的下界侧}——\text{即"是否存在更低极小"}\textbf{未解决}✗✓$$

## §3 T13-A 状态块（唐先生指定格式）

$$\boxed{\ \begin{array}{c} \text{已发现并局部审计：3 个 Type-A 候选轨道}✓\\ \text{严格上界：}0.76408110074585388514756267472105✓\\ \text{严格下界：}0.76✓\\ \textbf{全局下界／全局覆盖：尚未完成}✗ \end{array}\ }✓$$

## §4 边界

- §0 的两条实现**互相独立**✓（均值形式 vs 区间算术 ✓）；一致性到 $10^{-100}$ ✓ ⟹ 可复核 ✓
- 层 1 的严格性依赖：$\pi$ 的标准 100 位展开正确 ✓、mpmath 的 `cos`/区间运算正确 ✓（与项目既有证书同类假设 ✓）
- ⚠️ **不**声称 $m_3$ 精确值 ✗；**不**声称 $x^*$ 全局最小 ✗；**不**声称只有 3 个极小 ✗
- 层 2 的数字**可引用**但须标注"数值"✓；层 3 区域**不得**引用为已证 ✗
- **未用** RH；**未改** 他档原文（勘误以本档为统一出处 ✓）

## §5 与丙的关系（唐先生已定：暂不开 ✓）

$$\text{上界侧已是】独立、可复核的严格证书}✓✓ \Longrightarrow \text{真正剩下的核心问题}：\textbf{把}\ 0.76\ \text{这一侧向上推进}✓$$
$$\qquad \text{即"是否存在更低极小构型"}✗ \Longrightarrow \text{这才是是否投入全局区间覆盖的决策依据}✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 舍入余量收尾 命中文件数=1    ::  ./C213-YI-slack-closure-and-JIA-ledger-unification.md
技术词 三层区分     命中文件数=1    ::  ./C213-YI-slack-closure-and-JIA-ledger-unification.md
技术词 账本统一修订 命中文件数=1    ::  ./C213-YI-slack-closure-and-JIA-ledger-unification.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 本档自我失误

$$\textbf{① impl B 用 float(LO) 构造}\ \pi\ \text{区间}✗✗ \Longrightarrow \text{把 100 位有理数压成双精度}✓ \Longrightarrow \text{区间未正确包住}\ \pi✓ \Longrightarrow \text{假上界（偏大}\ 1.07\times10^{-16}✓）$$
$$\qquad \textbf{被两条独立实现交叉抓住}✓✓ \Longrightarrow \text{改用高精度 mpf 构造区间}✓（\text{教训：跨实现比对是有效防线}✓✓）$$
$$\text{②}\ \texttt{findroot}\ \text{参数签名错}✗（\texttt{C-212}\ \text{已记}✓）$$
$$\qquad \Longrightarrow \text{①–② 均为实现错，非数学错}✓（\text{第 31–32 次同类应验}✓）$$
