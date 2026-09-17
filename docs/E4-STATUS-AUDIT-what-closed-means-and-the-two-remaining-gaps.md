已查地图：**未覆盖**（所查档：`E4-palojarvi-finitely-many.md`（本档对象）、`PENDING-ITEMS-MASTER.md`（A1-3 行）、`V290`／`V291`（Palojärvi 误述勘误）、`MASTER-STATUS-AND-CLOSURES.md`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`Palojärvi`、`至多一个离轴`、`有限多个离轴`、`Lemma 2.2`、`Montgomery Ten Lectures`、`A1-3`。**结论：本档不新增路线，只对既有条目 `E4-palojarvi-finitely-many.md` 做状态审计与独立复核**）

# E4（Palojärvi 推广）状态审计： "已闭合" 指什么 + 两块真实剩余

> **任务**：唐先生 2026-09-17 19:35 追问 —— 在 candidate-proof-v1 严格化（`C-38`）之后，"②E4-Palogärvi（至多一个离轴零点 ⟹ 有限多个，已闭合）这个呢？"
> **对象**：`docs/E4-palojarvi-finitely-many.md`（2026-09-12；源头 `docs/Palojarvi-2019-tau-Li-explicit-zero-free.pdf` = arXiv:1807.01506v3）
> **证据等级**：`[出处]` 原档逐字 ｜ `[复核]` 本档独立跑出 ｜ `[严格]` 本档给出证明 ｜ `[缺口]` 未核

---

## §0 先说结论（一句话对照）

$$\textbf{candidate-proof-v1(}C\text{-}38\text{)：}\textbf{循环}（缺口\iff\text{RH}）\ \Longrightarrow\ \text{只值一个判据；}\qquad
\textbf{E4：}\textbf{不循环}，是真推广\ \Longrightarrow\ \text{值一个}\textbf{条件性定理}，\text{但条件无法满足}$$

即：**E4 的"闭合"与 candidate-proof-v1 的"严格化"不是同一件事**。E4 没有循环错误；它的问题是**假设**（$m$），不是**推导**。

---

## §1 "已闭合" 的确切含义 `[复核]`

原档 §5b 标题即"constant-level gap, CLOSED (2026-09-12)"，其内容 = 把原论文证明第 20 页的三尺度比较
$\log R=\tfrac23\log R+\tfrac14\log R+\tfrac1{12}\log R$ 在常数 $C\to C(m):=40(K_{F,1}+K_{F,4})+20m$ 下重做。

**本档独立重跑** `scripts/E4b_palojarvi_constant.py`（exit 0，输出 `scripts/E4b_palojarvi_constant.txt`）：

| 核验项 | 脚本输出 | 判定 |
|:--|:--|:--|
| (1) $m=1$ 退化精确 | `C(1) equals the published constant exactly` | ✓ |
| (2) 窗口 $[N_m,5mN_m]$ 全窗成立 | 最差 log-ratio $+32.1289$（$m=1$） | ✓ |
| (3) $m$ 的代价是对数级 | 线性代价只在窗口与 $5m$ | ✓ |
| (4) 阈值中的 12 承重 | 去掉则左端点失败 | ✓ |
| 结论行 | `E4 gap CLOSED` | ✓ 可复现 |

**所以"已闭合"= 常数级闭合 + 骨架成立，且可复现** ✓。**它不等于"整条链自足严格"**（见 §3、§4）。

---

## §2 本档独立复推：一处措辞应精确化 `[复核]`

原档 §5(iii) 写：
$$R^n\ \ge\ 40(K_{F,1}+K_{F,4})\,n\log n+20m\qquad\text{"i.e. (using }n\log n\ge1\text{)"}\qquad R^n\ \ge\ n\log n\cdot C(m)$$
本档符号化复算两右端之差：
$$n\log n\,C(m)-\big[40(K_{F,1}+K_{F,4})n\log n+20m\big]=20m\,(n\log n-1)$$
$n\log n\ge1$（$n\ge e$）时该差 $\ge0$，故两条件**不严格等价**：**后者更强、蕴含前者** ✓（原档同句已注明 $n\log n\ge1$，故无数学错误；但"$=$i.e.$=$"应读作"$\Longleftarrow$（充分）"）。**处置**：措辞级，不影响闭合 ✓。

---

## §3 真实剩余之一：引擎 Lemma 2.2 的证明**未读**（引用件） `[缺口]`

原档 §8 自标 **`未读`：Montgomery, *Ten Lectures*, Ch. 5 Thm 11（Lemma 2.2 的证明）；Brown 2005；McCurley 1984**。

**Lemma 2.2（原档逐字引用）**：设 $M\ge1$，$z_1,\dots,z_M\in\mathbb C$，$\max_j|z_j|=1$，则
$$\max_{1\le n\le 5M}\ \mathrm{Re}\Big(\sum_{j=1}^{M}z_j^n\Big)\ \ge\ \frac1{20}$$

**本档独立数值检验**（随机 4000 组 + 爬山精修；$|z_j|\le1$，至少一个 $|z_j|=1$）：

| $M$ | 1 | 2 | 3 | 5 | 8 | 12 |
|:--|--:|--:|--:|--:|--:|--:|
| $\min\max_{n\le5M}\mathrm{Re}\sum_j z_j^n$ | 0.500 | 0.529 | 0.685 | 0.807 | 0.958 | 0.983 |

（$M=1$ 解析值：$\min_\theta\max_{1\le n\le5}\cos(n\theta)=0.5000$ ✓）

**读数**：引用常数 $\tfrac1{20}=0.05$ **远低于**搜索到的最坏值（$\ge0.5$）⟹ **该引用的"陈述"在数值上很安全**（宽松 10 倍以上）✓；但**它的证明仍未核** ⟹ 严格意义上 E4 至今**依赖一件未读的引用**。

**可行动的严格化路径**（本档提议，未执行）：给 Lemma 2.2 或**任一显式 $c>0$ 的替代**一个自足证明（Fejér 核路线只给下界 $-\tfrac12$ 每项，本档已试、不足），然后以 $c$ 替代 $\tfrac1{20}$ 重跑常数簿记 ⟹ 可把 E4 升级为"自足（模源文 Theorem 2.1／3.1 引用）"。

---

## §4 真实剩余之二：假设 $m$ 无法供给（这是"买不到东西"的根源） `[缺口]`

推广后的定理**条件**是"$\Re\rho>\tau/2$ 的零点至多 $m$ 个"。原档 §6 逐字：
- Dirichlet $L$-函数：$m=1$ 经典可得（McCurley 1984；Brown Cor. 1）；
- **一般 $F$：无显式上界** ⟹ **定理可证，但仅在外部给出离轴零点计数时可用** —— 而这正是 $\tau$-Li 框架本来想避免的输入。
- 代价：$n$-窗口线性拉长（$[N_m,5mN_m]$）、常数线性退化（$C(m)$）——由 Lemma 2.2 的 "$5M$" 强制，不可通过重标度规避。

**本档判定**：E4 的定理形状 = **检测型条件判据**（"存在离轴零点 $\iff$ 某个 $n$ 越过阈值"），其**力量完全由 $m$ 的外部可得性决定**；对一般 $F$（含 $\zeta$）$m$ 未知/巨大 ⟹ **对 RH 无杠杆** ✓（与原档 §7 逐字一致："buys nothing unless you can independently bound the number of off-line zeros"）。

---

## §5 与 $C$-38 的对照（同一把尺子）

| | candidate-proof-v1（C-38） | E4（本档） |
|:--|:--|:--|
| 推导是否自足 | 引理 A/B/C/D **严格成立**（本档已给完整证明） | 骨架成立（模源文 Theorem 2.1／3.1 引用） |
| 致命环节性质 | **循环**：缺口 $\iff$ RH（严格双向） | **条件**：需外部 $m$，一般 $F$ 无 |
| 闭合所指 | ——（无法闭合） | 常数级闭合（可复现 ✓） |
| 产出性质 | 判据（重述） | **条件性检测定理**（真推广） |
| 对 RH 的杠杆 | 无（$\iff$ RH） | 无（$m$ 不可供给） |
| 剩余可行动作 | ——（已到顶） | ①引擎自足化（§3）；②$m$ 的独立界（= 新输入） |

**共同点**：两者都**不是 RH 的证明**，且都被同一类障碍挡住 —— **"需要一个外部的、本来就不该存在的东西"**（前者是不循环的分离量，后者是离轴零点计数）。

---

## §6 边界与不声称

- 本档**只做状态审计与独立复核**：不新增定理、不改动 `E4-palojarvi-finitely-many.md`（原档保持不动）。
- `[复核]` 数值为实际运行（脚本 exit 0）；`[缺口]` 两项（Lemma 2.2 证明未读、$m$ 无供给）为**诚实标注**，非"不存在"。
- 未使用 RH；未使用任何零点位置作为推导输入；数值仅作核对。
- 与 `V291` 的关系：`V291` 已登记 `V290` §3 把 Palojärvi Thm 4.1 误述为"无条件结构定理"的勘误 ⟹ **Thm 4.1 的"至多一个"是假设**；本档沿用该更正后的读法 ✓。
