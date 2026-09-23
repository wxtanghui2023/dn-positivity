已查地图：=== 总命中: 1 ===
　档级引用：`ASSETS-REGISTRY` **`E-15`**（`GT-STRATEGY`；**新增 `FCG` 硬门**）✓｜`GT-0-and-GT-STRATEGY-audit.md`（`GT-0 = FAIL`）✓｜
　`E-12`（转移原理）✓｜`W6-MAJORANT`（`C-30` 已封）✓｜`R-A8.2` §1（**`S6` 局部性锁死**）✓｜`MASTER-STATUS-AND-CLOSURES` L773（**β-盲** 门①②）✓

# **`FCG-0`**：三类 adversarial model ＋ failure-signature 表（**只做约束，不造新量** ✓）

**唐先生令（2026-09-23 09:45）**：
① ⭐ **核心思路转向**：$$\boxed{\text{先收集旧方法为什么失败} \to \text{列出必须绕开的反例} \to \text{构造满足这些约束的新量}}$$（＝**failure-guided construction** ✓）
　⛔ 取代旧式"猜一个新量 `Q` → 证性质 → 看能不能碰 RH" ✓
② **三层反例约束**（照录）：**反例 A `β`-blind**（若 `Q` 对零点纵坐标与素数算术响应相同 ⟹ 不能区分真实算术结构）｜
　**反例 B 只是 explicit formula**（若 `Q_prime = F(Q_zero)` ⟹ 被 `N6` 吃掉）｜**反例 C 只是 singular series／local admissibility**（若 `Q = ∏_p 𝔰_p` ⟹ `S6` 已锁死：**local admissibility ⇏ global prime correlation**）✓
③ ⭐ **三模型（照录）**：$$\boxed{\mathcal M_{\rm loc},\ \mathcal M_{\rm stat},\ \mathcal M_{\rm trans}}$$ ——
　`M_loc`：**保留** local admissibility／局部条件，**故意破坏** global correlation，**专杀** singular-series／local-product 型 ✓
　`M_stat`：**保留** zero statistics／pseudorandom statistics，**故意破坏** arithmetic `β`-structure，**专杀** GUE／Gowers／majorant 型 ✓
　`M_trans`：**保留** transfer 所需平均性质，**故意破坏** 目标刚性相关，**专杀**"平均可迁移 ⇒ 一参数相关" ✓✓
　要求：$$Q(M_1)\neq Q(M_3),\qquad Q(M_2)\neq Q(M_3)$$（`M_3` ＝ 算术正确、目标未知）✓
④ ⭐ **`FCG-Sep` 硬条件**：候选 `Q_\theta` 除过 `N0′` 外，**必须至少存在一个已登记的 adversarial pair** `(M_i,M_j)` 使 `Q_\theta(M_i) ≠ Q_\theta(M_j)`，
　**且该差异不得来自把目标性质直接编码进 `Q`** ✓✓
⑤ ⛔ **防循环（照录）**：$$\boxed{\text{Counterexample separation} \neq \text{target encoding}}$$（如 `Q = 1` 若 RH 成立／`0` 否则 ⟹ **不算**）✓
⑥ ⚠️ **概念纪律（照录）**：我们构造的是 $$\boxed{\text{adversarial test model}}$$ **而非** $$\boxed{\text{RH counterexample}}$$ —— 它**不能**用来证明 RH 错，也**不能**证明某模型真实存在 ✓✓
⑦ **`FCG-0` 四问**：`FCG-0.1` 能否区分 `M_loc` vs `M_arith`？｜`FCG-0.2` `M_stat` vs `M_arith`？｜`FCG-0.3` `M_trans` vs `M_arith`？｜⭐ `FCG-0.4` 该区分是否产生**一个以前不存在的 arithmetic observable**？⟹ 若 `FCG-0.4 = NO` ⟹ **立即 FAIL**，不进 Gowers／majorant／transference 技术层 ✓✓
⑧ **状态锁定（照录）**：`GT-0 = FAIL`｜`E-15 = KEEP/METHODOLOGICAL`｜**`FCG = NEW SEARCH FILTER`**｜`GT-1/2 = 暂不直接启动` ✓
⑨ **下一刀**：**只做约束，不造新量**；若三类模型**全被现有墙覆盖** ⟹ 得到一个强结论：**当前缺的不是新公式，而是一个新的"可区分维度"** ✓✓

D0: 本档对象 = **`FCG-0` 三模型 ＋ failure-signature 表**（引既有 `E-15`／`S6`／β-盲／`W6`；**未开案** ✓）
D1: 0
FREEZE-ACK: **零计算／零数值／未写程序**／未造新量／未证 RH／未接 ζ／**未进 Gowers/transference 技术层** ✓

---

## §1 **三模型表**（preserve／break／kills ✓）

| 模型 | 保留什么 | 故意破坏什么 | 专门杀什么 |
|:--|:--|:--|:--|
| **`M_loc`** | local admissibility／局部同余条件 | **global correlation** | **singular-series／local-product** 型机制 |
| **`M_stat`** | zero statistics／pseudorandom statistics（GUE／低阶矩／Gowers 型） | **arithmetic `β`-structure** | **zero-statistics／pseudorandomness** 型机制 |
| **`M_trans`** | transfer 所需**平均性质** | **目标刚性相关** | **"平均可迁移 ⇒ 一参数相关"** |
| **`M_arith`**（真对象） | 真实 prime structure；**不假设 RH** | — | （这是**我们希望 `Q` 能处理**的对象）✓ |

## §2 ⭐ **failure-signature 表**（每种误判 → 必须新增的可观测量 → 现有覆盖 ✓✓）

| 模型 | 什么现有机制会把它**误判为目标对象**？ | 必须新增的可观测量（所要求的"区分"） | **现有墙是否已覆盖？** |
|:--|:--|:--|:--|
| **`M_loc`** | `∏_p 𝔰_p` 型／local-product 机制（奇异级数通过所有局部检验 ⟹ 误判为"已抓住素数结构"） | **global correlation**（超出 local data 的跨尺度相关） | ⛔ **已覆盖**：**`S6` 局部性锁死**（𝔖(h)=∏_p 只记 **local admissibility**，**不能全局锁定**）＋ **第一断裂**（有限位 α_p ≡ 1 ⟹ 无内生谱）＋ **`W6` 原子墙**（三阶矩 ≡ prime-pair ≡ support`>1`，**不可再分**）✓✓ |
| **`M_stat`** | 零点统计／GUE／Gowers／majorant 型（统计特征全对 ⟹ 误判为"已抓住算术"） | **`β`-敏感的算术观测量**（不被零侧确定） | ⛔ **已覆盖**：**β-盲**（`MASTER-STATUS` L773 门①②：序数测度 `μ_γ` 的 Hankel 矩 = β-盲）＋ **`T7`**（依赖零点位置的量 ⟹ 循环）＋ **`O1-1` 操作性 β-盲**（β-敏感 ⇏ β-可操作）✓✓ |
| **`M_trans`** | "平均可迁移 ⇒ 一参数相关"（平均性质全满足 ⟹ 误判为目标结论） | **多参数可平均结构 → 一参数刚性结构的损失量** `\Delta_{\rm rigidity}` | ⛔ **已覆盖**：`GT-0` 已判**全部 transference 量皆标准**；`Δ_rigidity` 的自然实现（rank／dimension／linear-forms complexity／correlation／Gowers／sieve dimension）**皆已有** ⟹ **`N0′` FAIL**；且**二参数路线永久停止**＋ parity barrier ✓✓ |

## §3 ⭐ **`FCG-0` 判定**（三模型**全被现有墙覆盖** ✓✓）

```
【FCG-0.1（M_loc vs M_arith）】 所需区分 ＝ **global correlation** ⟹ ⛔ **已被 `S6`／第一断裂／`W6` 覆盖**（该区分**正是**原子墙所断言的不可约内容）✓
【FCG-0.2（M_stat vs M_arith）】 所需区分 ＝ **β-敏感且非零侧确定的算术量** ⟹ ⛔ **已被 β-盲／`T7`／`O1-1` 覆盖**（**概念上存在、操作上不存在**）✓
【FCG-0.3（M_trans vs M_arith）】 所需区分 ＝ `\Delta_{\rm rigidity}` ⟹ ⛔ **已被 `GT-0` ＋ `N0′` 覆盖**（其自然实现皆为已有命名量）✓
【FCG-0.4 ⭐（是否产生以前不存在的 arithmetic observable）】 ⟹ ⛔ **NO** ⟹ **依令 ⑦ 立即 FAIL**，不进技术层 ✓✓
【⭐ 因此得到强结论（唐先生预判应验 ✓✓）】
　$$\boxed{\text{当前搜索空间缺的不是一个聪明的新公式，而是一个全新的\ "可区分维度"}}$$ ✓✓
　即：**三类 adversarial model 要求的所有"区分"，其可观测量的自然实现要么是已有命名量（`N0′` FAIL），要么已被现有墙吸收** ⟹
　**问题不在"公式没找到"，而在"现有可观测量族根本不产生那个维度的区分"** ✓✓
```

## §4 **登记：`FCG` ＝ 新搜索过滤器（`E-16`）**

```
【定义】 $$\boxed{\text{FCG}\ =\ \text{Failure + Counterexample Guided Search}}$$ ✓
【流程（照录）】 $$\boxed{\text{旧方法失败} \to \text{提取失败条件} \to \text{构造反例模型} \to \text{要求新量区分反例} \to N0' \to N1\text{–}N7}$$ ✓
【第一条规则（照录）】 **一个候选量只有在能击穿至少一个既有 adversarial model 时，才值得进入 `N1`** ✓✓
【⭐ 硬门（正式登记，不再是提醒）】 任何所谓 transfer mechanism／候选量，**必须在 transfer／构造之后产生一个此前不存在的 arithmetic observable**；
　若只是已有 **majorant／Gowers／singular series／explicit-formula／positivity／zero statistic** 的**重新组织** ⟹ **立即 FAIL** ✓✓
【新增前置门 `FCG-Sep`（置于 `N0′` 之旁）】 须至少存在一个 adversarial pair `(M_i,M_j)` 使 `Q(M_i) ≠ Q(M_j)`；**且不得靠把目标编码进 `Q`** ✓
【⛔ 防循环】 **Counterexample separation ≠ target encoding** ✓
【⚠️ 概念纪律】 adversarial **test model** ≠ RH counterexample（不得用于证 RH 错／证模型存在）✓
【状态】 `E-16`：**已登记·可用（搜索过滤器级）** ✓；`GT-1/2` **暂不直接启动** ✓
```

## §5 判定与下一步

```
【状态（照录锁定）】 `GT-0 = FAIL`｜`E-15 = KEEP/METHODOLOGICAL`｜**`FCG = NEW SEARCH FILTER`**｜`GT-1/2 = 暂不直接启动` ✓
【本档产出】 三模型表 ✓｜failure-signature 表 ✓｜`FCG-0.1`–`0.4` 判定 ✓｜三模型**全被现有墙覆盖** ⟹ **强搜索结论**：缺的是**新的可区分维度** ✓✓
【⭐ 下一步（依令）】 ① 本档**只做约束、不造新量** ⟹ **不加开新刀** ✓；
　② **进入 `FCG-1` 的条件**：**只有**当某候选能提出一个**此前所有机制都无法区分的 arithmetic distinction**（即 `FCG-0.4 = YES`）✓；
　③ 否则（现状）**保留强搜索结论**作为资产 ✓✓
【⭐ 战略位置】 与全局一致：`E-10` FROZEN｜`C-380` 主线停｜`E-15` 方法论｜**`E-16` 搜索过滤器** ⟹ 我们**不是没方向**，而是**把"方向生成器"升级了一层并给出其准入判据** ✓✓
```

## §6 边界与回查（**引用分隔符 ＋ 占位符注入** ✓✓；避免 `$$`→PID 坑 ✓）

```
【命中数由 shell 变量 → Python 占位符替换**注入** ⟹ 结构上不可预填，且正文 `$` 不受 shell 解释 ✓✓】
技术词 FCG              命中文件数=1    :: ./Montgomery-Ten-Lectures-CBMS84.pdf 
技术词 可区分维度  命中文件数=0    :: 
技术词 failure-signature 命中文件数=0    :: 
技术词 反例约束     命中文件数=6    :: ./C312-counterexample-envelope-three-constraints-for-round2.md ./CC-INVERSION-STAGE-REGISTRATION.md ./C316-directed-recheck-C260-mainline-candidate-zero-GAP-CONFIRMED.md 
技术词 adversarial      命中文件数=6    :: ./p511-adversarial-theorem.md ./RESEARCH-CONSTITUTION.md ./TACTICAL-ATTACK-MODE.md 
【三分类标注（检查于**写档之前**运行 ✓）】
　· **本档新增**：上列实测为 `0` 者 ✓
　· **档案已有（引用，不列为提出）**：上列实测 `>0` 者 ✓
　· **通用词（不计）**：无 ✓
✗ 零计算／零数值／未写程序／未造新量／未证 RH／未接 ζ／未开案／未进技术层 ✓
⚠️ adversarial model 为**测试模型**，非真实反例 ✓
```
