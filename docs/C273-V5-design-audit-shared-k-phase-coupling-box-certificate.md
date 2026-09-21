已查地图（**先查后写**）：`C-272`（failure mode 审计：零反例 ＋ 粗箱积压 ＋ 间隙中位 1.83）、`C-271`（账本钉死 ＋ §3 诊断协议）、`C-181`（阻尼引理，u≤5）、`C-186`（Fejér／Andersson：**1/20 级对一切 M 已证**）、`v4` 引擎（`scripts/rpm_certificate_v4.py`）、`PLAN §12`（待办与冻结依赖图）。回查见 §6 ✓

D0: 本档对象 = **v5 候选证书设计 ＋ soundness lemma ＋ 第一刀机制淘汰／保留** —— 关系 = 由 `C-272` 的 failure mode 直接推出的机制设计审计（**不跑计算**、不产定理）
D1: 0
FREEZE-ACK: 本档即冻结期内的设计审计（依 §8.1）

---

## §0 正式状态与研究问题（单句 ✓）

$$\textbf{状态（采纳唐先生改判}✓✓）：\boxed{\texttt{C-272}：M=5/1/2\ \text{未闭合}；\ \textbf{failure mode} = \textbf{certificate relaxation／certification backlog}✓\ （\text{不是「预算不足}✗）}$$

$$\textbf{判据}✓（\texttt{C-272}✓）：L<\tfrac12\ \text{占}\ 70.3\%✓；\ U_{\rm sample}>\tfrac12\ \text{占}\ 100.0\%✓；\ U_{\rm sample}\le\tfrac12\ \text{反例}\ \mathbf{0}✓；\ \operatorname{median}(U-L)=\mathbf{1.83}✓；\ \text{箱宽中位}\ 0.262✓$$

$$\textbf{研究问题}✓（\text{粗盒上}）:\boxed{\text{能否以便宜的}\ \textbf{可证} \text{证书证明}\ \min_{\theta\in B}\max_{1\le k\le25}F_k(\theta)>\tfrac12\ ？}$$

$$\textbf{纪律}✓：\text{不跑}\ 60M✗；\text{不跑慢版}✗；\text{不开}\ M=6\text{–}11✗；\textbf{本轮零计算}✗$$

## §1 两个损失源必须分开（**设计的第一要求**✓✓）

$$\textbf{损失 I（外层交换}✓）：\ \max_k\min_{\theta\in B}F_k(\theta)\ \ \text{vs}\ \ \min_{\theta\in B}\max_kF_k(\theta)$$
$$\qquad \text{证书逐}\ k\ \text{取盒内最坏点}⟹\textbf{不同}\ k\ \textbf{的坏点不是同一个}\ \theta✗ \Longrightarrow \text{这是}\ \texttt{C-272}\ \text{中间隙}\ 1.83\ \text{的主源}✓$$
$$\textbf{损失 II（内层坐标}✓）：\text{某坐标区间含}\ \pi\ \text{的奇数倍}⟹ \text{该项被强制}\ -1✗（\text{与}\ k\ \text{无关}✓）$$
$$\boxed{\textbf{任何 v5 机制必须声明它打击 I 还是 II}✓；\text{未打击任一损失者}⟹\text{不算机制}✗}$$

## §2 五个候选机制逐项审计（✓）

| # | 机制 | 打击 | 成本 | 判定 |
|---|---|---|---|---|
| 1 | 共享-$k$ | — | — | **归入 #3**（它是问题重述，非独立机制 ✗）|
| 2 | 相位区间关系（$\\theta_j$ 间约束）| I | 低 | **淘汰**（$B$ 是**独立盒** ⟹ 无 $\\theta_j$ 间可证约束 ✗；除非引入解的**结构先验** ⟹ 不可证 ✗）|
| 3 | **多-$k$ 覆盖证书**（覆盖集 $K_B$）| **I** | $|K_B|\\times$ 单-$k$ 盒界 | **保留为主** ✓ |
| 4 | 中心 ＋ Lipschitz／二阶余量 | **II** | 一次中心评估 | **保留为廉价辅助** ✓（增量待专项对照 ✓）|
| 5 | 组合 3＋4 | I＋II | 相加 | 最后考虑 ✓ |

$$\textbf{⭐ 先例（重要}✓✓）：\texttt{C197-T13-B-w2}\ \textbf{一维覆盖证书已证}✓✓ \Longrightarrow \text{多-}k\ \text{覆盖机制}\ \textbf{在本项目内已有成功实例}✓（\text{维度}\ 1\to5\ \text{是真实方向}✓）$$

$$\textbf{#4 的诚实说明}✓：\text{随机实验显示中心式与分离式几乎相同}⟹\text{一般箱上}\textbf{无增益}✗；$$
$$\qquad \text{但随机箱中子集「含}\ \pi\ \text{奇数倍}\+」\text{罕见}✗ ⟹ \textbf{pending 箱恰是那批罕见箱}✓ ⟹ \text{其增益必须用}\textbf{pending 箱专项对照}✓\ \text{才能判定}✓（\text{尚未做}✗）$$

## §3 必须证明的 soundness lemmas（四条 ✓）

$$\textbf{L1（覆盖}\Longrightarrow\text{下界}）✓：\exists K_B\subset[1,25]\ \text{使}\ \forall\theta\in B:\ \max_{k\in K_B}F_k(\theta)>\tfrac12 \Longrightarrow \min_{\theta\in B}\max_{1\le k\le25}F_k(\theta)>\tfrac12$$
$$\textbf{L2（好集扩张）}✓：\text{若}\ F_k(c)>\tfrac12+\rho_k\ \text{则}\ \forall\theta\in B:\ F_k(\theta)>\tfrac12，\ \text{一阶可取}\ \rho_k=\tfrac{k}{2}\sum_j w_j✓（\text{用二阶余量可缩小}\ \rho_k✓）$$
$$\textbf{L3（覆盖判据，}\textbf{真正困难的一步}✗）✓：\text{给出}\ \bigcup_{k\in K_B}G_k\supseteq B\ \text{的}\ \textbf{可验证充分条件}✓（\text{如「盒内坏集为空」的算术判据}✓）$$
$$\textbf{L4（廉价性}✓）：\text{每步}\ O(|K_B|\cdot M)✓\ \text{且}\ \textbf{不引入细分裂}✗ \Longrightarrow \text{粗盒直接认证}✓✓$$
$$\qquad \text{其中}\ G_k:=\{\theta\in B: F_k(\theta)>\tfrac12\}✓$$

## §4 第一刀预注册判据（✓）

$$\textbf{成功}✓：\text{在 pending 粗箱样本上，用}\ \text{L1–L4}\ \text{可直接认证的比例}>90\%✓（\text{且全部界可证}✓）$$
$$\textbf{失败}✗：\text{若}\ L3\ \text{在粗盒上所需}\ |K_B|\ \text{远超}\ 25✗，\text{或仍需细分裂}✗ ⟹ \text{说明}\ m_5\ \text{贴}\ \tfrac12\ \text{太紧}✓ ⟹ \text{回命题层重审}✓$$
$$\textbf{有利先验}✓（\text{已实测}✓）：U_{\rm sample}\ \text{在}\ 100\%\ \text{的 pending 箱上}>\tfrac12✓，\text{中位}\ 2.18\gg\tfrac12✓ \Longrightarrow \text{覆盖很可能在粗尺度成立}✓，\textbf{但未证}✗$$

## §5 边界

$$\textbf{① 不声称}\ v5\ \text{能闭合}\ M=5✗；\text{不声称 max–min 间隙可消除}✗（\text{本轮只是机制设计}✓）$$
$$\textbf{② 未跑任何计算}✗；\text{未改}\ v4✓；\text{未改他档正本}✓；\text{未用}\ RH✓$$
$$\textbf{③ #2 的淘汰基于「}\ B\ \text{为独立盒」这一结构事实}✓；\text{将来若引入解的先验须重审}✓$$
$$\textbf{④ }\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗（\texttt{C-270}✓），\text{本档不改变}✓$$

## §6 【技术词回查】输出（**先跑后写**✓）

```
技术词 覆盖证书     命中文件数=1    :: ./C197-T13-B-w2-one-dimensional-cover-certificates-PROVED.md
技术词 好集扩张     命中文件数=0    ::
技术词 损失分离     命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\textbf{好集扩张}✓（0 命中）、\textbf{损失分离}✓（0 命中）\Longrightarrow \textbf{本档首次命名}✓$$
$$\qquad \textbf{覆盖证书}✗：\text{命中}\ 1\ \text{处} \Longrightarrow \textbf{档案已有}✓（\texttt{C197}\ \text{一维已证实例}✓）；\text{本档}\textbf{引用}\text{而不列为提出}✗✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{可证余弦包围}✓（v4✓）；\text{认证间隙／交换损失}✓（\texttt{C-271}✓）；\text{粗箱积压／零反例审计}✓（\texttt{C-272}✓）$$
