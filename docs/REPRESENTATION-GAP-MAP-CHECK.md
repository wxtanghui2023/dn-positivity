已查地图：命中 4 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
　判定：4 命中经复核为**同形异义／自命中**：`表示缺失` 1 档＝`C303`（Hilbert 符号失效机制，**RH 侧** ✗）；
　`混合表示` 1 档＝本日 `RH-interaction-mixed-invariant-MAP-CHECK`（**自命中** ✓）；`log-concavity`／`mixed volume` 命中为 `p26a14-mixed-flow` 等 ✗
　⟹ **本仓对"表示缺失／log-concavity–AF 无混合体积表示"零覆盖（MAP-NEW）** ✓

# **Representation-Gap / Missing-Formula · MAP CHECK**（R0 ＋ R1）

**唐先生令（2026-09-22 21:23）**：
① ⛔ **不要把 GAP④ 包装成"mixed volume 新机制"**；已确认 **interaction generator 基本 DEAD** ✓；
② 唯一留下的不是 mixed volume 路线，而是更窄的**表示缺失问题**：
　「**有定量不等式 ＋ 存在交叉量理论，但某类目标没有自然的交叉表示**」✓；
③ 攻击点改变：不问"能否发明新 mixed invariant"，而问
　「**一个已有的定量结构，为什么在某些对象上没有相应的表示？这种"不可表示性"本身能否形成独立数学问题？**」✓；
④ **只查两问**：**R0** ＝"没有 mixed-volume 表示"是否已是**成熟分类理论**（若是 ⟹ DEAD）✓；
　**R1** ＝是否存在独立问题满足〔**AF/BM 型定量现象已知** ∧ **标准表示缺失** ∧ **缺失本身尚未被系统解释**〕（成立才进 13 门）✓；
⑤ **只查一个非常窄的问题**：「**哪些已知 log-concavity／AF 型定量不等式没有 mixed-volume 或等价代数表示？**」✓
⑥ ⚠️ 若该问题本身也是成熟理论 ⟹ **再杀一个 generator** ✓

D0: 本档对象 = **表示缺失（Representation Gap）问题的 R0／R1 核验**（档案**零覆盖** ⟹ 新档；**未开案** ✓）
D1: 0
FREEZE-ACK: 零计算／零 Lean／未写程序／未碰 RH／未调用 C-380／未放宽门槛 ✓

---

## §1 protocol（先写死 ✓）

```
【R0】 "无 mixed-volume 表示"是否已有**完整分类理论**？若有 ⟹ **DEAD** ✓
【R1】 是否存在独立问题满足三条件：① AF/BM 型定量现象**已知** ② 标准表示**缺失** ③ ⭐**缺失本身尚未被系统解释** ✓
【证据等级】 **题录级**（未逐字全文精读）⚠️【预算】 一轮；**不开案** ✓
```

## §2 核验结果（**题录级 ⚠️**，带来源 ✓）

```
【⭐ 关键来源：van Handel（ICBS 2024 讲稿）——同段同时给出"缺口"与"解法"】
　· 缺口的**明文承认**（逐字）：「The study of log-concavity for the combinatorial problems discussed above is made possible by
　　the fact that the relevant combinatorial quantities **can be represented as mixed volumes**.
　　**However, for other problems where log-concavity has been conjectured, such a representation is not available.**」✓✓
　· ⭐ **但紧接着给出解法**（逐字）：「**while most combinatorial problems cannot be reformulated in terms of mixed volumes,
　　one can often still prove Alexandrov–Fenchel type inequalities directly in combinatorial applications**,
　　so that the log-concavity property arises essentially by **the same mechanism**」
　　（并点名 **Chan–Pak 方法** ✓）✓✓✓
　⟹ **"缺失"已被"直接证明 AF 型不等式"这一系统机制替代** ⟹ 不构成结构性空白 ✓✗
【统一表示框架（存在且活跃）】
　· **Lorentzian polynomials**（Brändén–Huh, *Annals* 192 (2020) 821–891）＋ 独立同期的
　　**completely log-concave polynomials**（Anari–Liu–Oveis Gharan–Vinzant）⟹ **log-concavity 的统一机器** ✓；
　　已被用于大量结果（引用清单逐字：`[BH20, EH20, MS21, HMMSD22, BL23, BLP23, Ros23, ALOGV24b, BES24, HMV24, KMSD24, MMS24, RU24]`）✓
　· **Hodge 理论／Kähler package**（Adiprasito–Huh–Katz, *Annals* 188 (2018) 381–452）⟹ 组合几何的另一条统一机器 ✓
　· 表示理论**仍在扩张**：**covolume polynomials**（Aluffi 2024）／**dually Lorentzian**（arXiv:2304.08399）✓
【⭐ 文献中存在"反向猜想"（决定性）】
　· Amini 讲稿逐字：「**Conjecture: There exist convex bodies P_α and Q_β so that log-concavity of matroids is explained by
　　log-concavity of mixed volumes**」✓✓ ⟹ **学界预期该"缺口"是可填的**（而非结构性空白）✓✗
【已解决的著名实例（说明该机制极其有效）】
　· **Read–Hoggar**（色多项式系数 log-concavity）⟹ **已由 June Huh（2009/2012）用代数几何（射影超曲面的 Milnor 数）证明** ✓✓
　· **Heron–Rota–Welsh**（拟阵特征多项式）✓｜**Mason 超对数凹**（独立集；Adiprasito–Huh–Katz；Anari 等）✓｜
　　**Stanley／Chung–Fishburn–Graham**（偏序集线性扩张；Stanley '81 经 AF）＋ 等价情形（Shenfeld–van Handel '23；Ma–Shenfeld '24）✓
【仍开放的实例（R1 的潜在候选）】
　· **Welsh**：Tutte 多项式对角线取值的 log-concavity（**开放**）✓
　· **Amelunxen–Bürgisser**：内蕴体积的 log-concavity 猜想（**开放**）✓
　· ⚠️ 但二者皆属**主流活跃猜想**，且 **AF 型直接证明／Lorentzian 机器**正是攻它们的现成工具 ⟹ 第三条件不满足 ✓
```

## §3 ⭐ 判定

```
【R0】 ⛔ **实质 DEAD**：虽**无"哪些现象有表示"的完整分类定理**，但"缺失"已有**系统替代机制**
　（**直接证明 AF 型不等式**〔van Handel 逐字；Chan–Pak〕＋ **Lorentzian／completely-log-concave** ＋ **Hodge·Kähler package**）
　⟹ **"不可表示性"不是一个空白，而是一个有标准处理路径的技术状态** ✓✗
【R1】 ⛔ **不成立（第三条件失败）**：① AF/BM 型现象已知 ✓ ② 标准表示确实缺失 ✓ ③ **但"缺失本身已被系统解释** ✗✗
　（解释＝上述统一机器 ＋ 直接 AF 机制）✓；且文献中的**反向猜想**（Amini：matroid log-concavity **可**由 mixed volume 解释）表明
　学界视之为**可填之缺口**；剩余开放实例（Welsh Tutte 对角／Amelunxen–Bürgisser）属**主流活跃猜想** ⟹ 不构成"未覆盖接口" ✓
【⭐ 生成器级后果】 ⟹
　$$\boxed{\text{Representation-Gap（缺失即空白）generator = DEAD}}$$ ✓✓
　（依唐先生 ⑥：若该问题本身亦为成熟理论 ⟹ **再杀一个 generator** ⟹ **条件成立，generator 封死** ✓）
【准确的收窄结论（保留可复用处 ✓）】 真正**活着**的不是"缺失即空白"，而是
　「**能否把 AF 型不等式直接证明到某个尚无此证明的对象上**」——但这**已属主流活跃研究**（Chan–Pak 一类）⟹
　依继承规则（**必须换出一个尚未被现有理论吸收的新不变量**）⟹ **不构成本仓新接口** ✓
```

## §4 边界与回查（✗✓）

```
✗ 零计算／未写程序／未碰 RH／未调用 C-380／未放宽门槛／**未开案** ✓
✗ 不把"再杀一个 generator"记为战绩 ✓；**未**声称 log-concavity 领域无价值（该领域**极活跃** ✓）
⚠️ 证据等级＝**题录级**（未逐字全文）⟹ 升为逐字全文级须另授权 ✓
【技术词回查（`scripts/tech_word_check.sh`，**先跑后写** ✓；逐字粘贴 ✓）】
　技术词 表示缺口         命中文件数=0 ⟹ **本档新增** ✓
　技术词 Representation-Gap 命中文件数=0 ⟹ **本档新增** ✓
　技术词 不可表示性       命中文件数=0 ⟹ **本档新增** ✓
　技术词 表示缺失         命中文件数=1 ⟹ **档案已有（`C303`，RH 侧 Hilbert 符号机制）⟹ 异义，引用不主张** ✓
　技术词 混合表示         命中文件数=1 ⟹ **自命中**（本日 interaction 档）⟹ 不主张 ✓
【外部来源（**题录级**）】 van Handel, *The Alexandrov–Fenchel Inequality*（ICBS 2024 讲稿；**缺口＋直接 AF 机制＋Chan–Pak**）✓｜
　Brändén–Huh, *Lorentzian polynomials*, Annals 192 (2020) ✓｜Adiprasito–Huh–Katz, *Hodge theory for combinatorial geometries*, Annals 188 (2018) ✓｜
　Huh, *Milnor numbers … and the chromatic polynomial*（JAMS；解 Read–Hoggar）✓｜Shenfeld–van Handel（AF 等价情形）＋ Ma–Shenfeld '24 ✓｜
　Amini, *Log-concavity in combinatorics and geometry*（**反向猜想**）✓｜Chan–Pak（AF 型直接证明方法）✓
```
