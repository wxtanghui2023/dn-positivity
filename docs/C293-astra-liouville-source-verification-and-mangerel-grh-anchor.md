已查地图（**先查后写**）：`C-291`（事件登记 ＋ §8 唐先生核查 ✓）、`C-292`（四份深审回执 ✓）、`C-287`（封口账 ✓）。原始材料：arXiv:2412.17199（**abs ＋ HTML v1 逐字**✓）、openai.com/index/ten-advances-in-mathematics（✓）。回查见 §5 ✓

D0: 本档对象 = **C-293：Astra／Liouville 原始材料核验 ＋ Mangerel 的 GRH 承重点定位**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（三条，对应唐先生三件事 ✓✓）

**① 原始材料：Astra 侧查无** ✗✓
- 已检索 OpenAI 官方材料（`ten-advances-in-mathematics`、GPT-6 Astra 模型页）与公开报道：**十项清单不含** Liouville／Goldbach ✗；**未见**该 claim 的论文、preprint、Lean 仓库或 OpenAI 原始说明 ✗
- 唯一来源是**二手中文报道** ✗ ⟹ 按纪律 **记为 `claim only`** ✓✓

**② Mangerel 侧：GRH 承重点已逐字定位** ✓✓
- **承重处**：非主特征乘积 L-函数的**一致零自由区**（论文 Lemma 3.3）⟹ 用于对**素数支撑的特征和**取**一致上界**（即短素数区间上的抵消 ✓）
- **论文自述的必要性**（Remark 6 原文）："Given current knowledge about Dirichlet L-functions, **it cannot be ruled out** that there are characters (mod N) whose prime sums over an interval [P,2P] with **P = N^{o(1)}** yields **no cancellation**. Therefore, in order to obtain a suitable lower bound we must obtain an estimate like ..." ✓✓
- **实际所需远弱于完整 GRH**（Remark 1 原文）：只需形如 `Re(s) > 1 - 1/(log N)^c`、`|Im(s)| <= (log N)^3` 的零自由区 ✓✓

**③ 数学状态判定** ✓✓
- Mangerel = **条件定理**（在 GRH 型零自由区下成立 ✓）—— **不是**无条件 verified theorem ✗
- Astra claim = **unverified claim** ✗（无原始材料 ✓）
- **两者不同层级，不可混称** ✗✓

---

## §1 逐字锚点（**核验依据**✓✓）

Mangerel, arXiv:2412.17199（2024-12-23 提交）摘要逐字要点：
- 设 λ 为 Liouville 函数。**Assuming GRH for Dirichlet L-functions**，we show that for every sufficiently large even integer N there are a,b ≥ 1 such that
  `a + b = N` 且 `lambda(a) = lambda(b) = -1` ✓
- **This conditionally answers** an analogue of the binary Goldbach problem for the Liouville function, **posed by Shusterman** ✓
- 该结论是下述**定量下界**的推论：assuming GRH, 存在 C > 0，使对**每个** sign pattern `(eta_1, eta_2) in {-1,+1}^2` 与每个素数 N ≥ N_0：
  `|{n < N : (lambda(n), lambda(N-n)) = (eta_1, eta_2)}| >> N e^{-C (log log N)^6}` ✓✓
- **技术特色**：证明**本质使用**有理数 n/N 的 **Pierce 展开**（may be of interest in other binary problems ✓）

承重点（HTML v1 逐字）：
- **Lemma 3.3**：设 `prod_{chi mod N, chi != chi_0} L(s, chi)` 在 `{alpha < Re(s) <= 1, |Im(s)| <= (log N)^3}` 内无零点，则对 `3 <= P < N/2` 有素数平均估计 ✓
- **Remark 6**：若要避免该假设，须用**零密度估计**并隔离「缺少适当零自由区的小特征集 S」；但**按当前知识无法排除**存在素数和在 `[P,2P]`（`P = N^{o(1)}`）上**完全无抵消**的特征 ✓✓ ⟹ **这就是 GRH 承担的不可替代作用** ✓✓
- **Remark 1**：Theorem 1.2／1.3 的证明**并不需要 GRH 的全部力量**，只需 `Re(s) > 1 - 1/(log N)^c` 型零自由区 ✓✓
- 指数说明：作者注明 `(log log N)^6` 中的 6 **可改进但不能降到 1 以下**（以该论证而言 ✓）

## §2 与 Mangerel 逐段对照：审计问句的精确化（✓✓）

- **原问句**（唐先生）：它究竟消掉了 Mangerel 证明中的哪个 GRH 依赖？
- **本档收窄后**（可核验 ✓✓）：
  > **Astra（若为真）是否给出了「素数支撑特征和在长度 `N^{o(1)}` 的区间上的抵消」——或等价地，是否绕开了对这类抵消的需求？**
- 理由：Mangerel 自述该抵消**不可由当前知识保证**（Remark 6 ✓），且只需**弱零自由区**（Remark 1 ✓）
  ⟹ 核验时只需盯**两处** ✓：① 是否给出一致短区间特征和抵消；② 是否只需弱化零自由区而其余论证不变 ✓

## §3 状态判定表（按唐先生四项分级 ✓）

| 对象 | 判定 |
|---|---|
| Mangerel 2412.17199 | **条件定理**（GRH 型零自由区下）✓ —— 非无条件定理 ✗ |
| Mangerel IMRN 2024 | **定理**（已发表、Open Access ✓；内容为 λ 卷积界 ✓） |
| Astra Liouville claim | **unverified claim** ✗（无原始材料：无论文／无 Lean 仓库／无 OpenAI 说明 ✓） |

## §4 纪律（**未放宽**✓✓）

- **不接入** M-TOWER ✗；**不建**新判据 ✗；**不与** L／F／B／R **排序** ✗；**不问** RH（先不问 ✓）
- 二手中文报道**不作为证明来源** ✗✓；`claim only` 标记**保留至取得原始材料** ✓
- 外部来源**按不可信数据处理** ✓

## §5 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（C-291 §8 已先行登记同源事实 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：「Astra 已无条件解决 Liouville-Goldbach」✗；「Mangerel 用满了 GRH」✗（实际只需弱零自由区 ✓）；「该 claim 已被验证」✗
- **本档新增词**：`GRH 承重点`／`原始材料核验`（0 命中 ✓）
