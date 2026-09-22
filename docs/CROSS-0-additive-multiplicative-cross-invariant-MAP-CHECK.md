已查地图：命中 210 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
　判定：210 命中经定向复核，**全部为同形异义／非实质覆盖**：
　　`Gauss` 81 档**全为** "**Gaussian** 消元／求积" 与 "**Gauss–Manin** 单值化" ✗（**非**加性×乘性 Gauss sum）
　　`sum-product`／`加性角色`／`乘性角色`／`混合能量` ＝ **0 档** ✓
　⟹ **本仓对"加性×乘性交叉不变量"零覆盖（MAP-NEW）** ✓（与 C-α 同型：**地图新**）

# **CROSS-0**：Additive–Multiplicative Cross-Invariant · 四问核验

**唐先生令（2026-09-22 21:16）**：
① 攻击点＝**基底不相容**（非"障碍下降"）：`R_A` 下简单 ∧ `R_B` 下简单 ⟹ `R_A↔R_B` 转换产生**不可消除的混合项** ✓；
② ⛔ **Gauss sum 本身太老，直接 DEAD** ✓；③ 真正要问：**A-law ＋ M-law 能否推出一个"第三关系"**（而非把两已知定理并排）✓；
④ **只查四问**（见 §1）＋ **判定阶梯**（照录）：**已有同物 ⟹ DEAD｜只是换符号 ⟹ DEAD｜只有不等式、没有新结构 ⟹ DEAD｜真正出现第三关系 ⟹ GAP-HOLD｜且有独立问题价值 ⟹ 才进十三门** ✓✓；
⑤ **这一次就停在 CROSS-0**，不再往 failure/descent 转译 ✓；⑥ ⚠️ 若 CROSS-0 也被 Gauss/uncertainty/energy 吞掉 ⟹ **"两个表示交互"这条生成器正式封死**（不再换名字）✓✓

D0: 本档对象 = **加性×乘性交叉不变量（CROSS-0）的四问地图-文献核验**（档案**零覆盖** ⟹ 新档；**未开案** ✓）
D1: 0
FREEZE-ACK: 零计算／零 Lean／未写程序／未碰 RH／未调用 C-380／未放宽门槛 ✓

---

## §1 protocol（先写死 ✓）

```
【四问】 1 是否**已存在**精确定义的 additive×multiplicative invariant？｜
　　　　 2 若有，是否是 **Gauss sum／energy／uncertainty 的直接重写**？｜
　　　　 3 若无，是否有自然候选（**二阶 cross-correlation／mixed moment**）？｜
　　　　 4 ⭐ 能否从 **A-law ＋ M-law** 推出一个**第三关系**（而非并排放置）？✓
【阶梯（照录）】 已有同物 ⟹ DEAD｜只换符号 ⟹ DEAD｜只有不等式无新结构 ⟹ DEAD｜
　　　　　　　　 真出现第三关系 ⟹ **GAP-HOLD**｜且具独立问题价值 ⟹ **才进十三门** ✓
【证据等级】 **题录级**（检索标题/摘要/片段，**未**逐字全文精读）⚠️【预算】 一轮；**不开案** ✓
```

## §2 四问逐条结果（**题录级 ⚠️**，带来源 ✓）

```
【Q1 是否已有精确定义的交叉不变量？】 ⟹ ⛔ **已有同物，且极标准** ✓✓
　· **Gauss sum** `G(χ,ψ) = Σ_x χ(x)ψ(x)` ＝ **加性角色与乘性角色的交叉矩阵元**
　　（Handbook of Finite Fields 明释为把 additive character 展开到 multiplicative-character basis 的系数）✓
　　⭐ 且已**形式化**：`Mathlib.NumberTheory.GaussSum` 定义 `gaussSum χ ψ`（`MulChar` × `AddChar`）并证基本性质 ✓✓
　· **Jacobi sum** `J(χ₁,χ₂) = Σ_c χ₁(c)χ₂(1−c)`（可由 Gauss sum 表出）✓｜**Ramanujan sum**（加法指数在既约剩余类上的和）✓
　· **mixed energy** `E₊(A,B)`（有限域，**sum–product 分析关键**；`Glibichuk 2011`）✓；
　　`Mudgal`（AJM）：`E_s(A₁,…,A_{2s})`／`M_s(A₁,…,A_{2s})` 与"**B、C 之间低的算术交互**"（逐字 `low arithmetic interaction`）✓
【Q2 是否 Gauss／energy／uncertainty 的直接重写？】 ⟹ ⛔ **是**（上述对象**本身即** Gauss sum／mixed energy）✓
【Q3 自然候选（二阶 cross-correlation／mixed moment）是否仍空白？】 ⟹ ⛔ **不空白**
　· **mixed energy／cross energy** 即"混合矩／交叉相关" ✓（已见 Q1）
　· 相关新近工作：`A bound on the multiplicative energy of a sum set and extremal sum-product problems`（arXiv:1410.1156）｜
　　`On the distribution of additive energy revisited`（arXiv:2602.01781，**2026**）✓
【Q4 ⭐ 能否由 A-law ＋ M-law 推出"第三关系"？】 ⟹ ⛔ **精确型第三关系已存在且经典** ✓✗
　· **Hasse–Davenport 乘法关系**（`Davenport–Hasse 1935`）：`Π_a τ(χρ^a,ψ) = −χ^{-m}(m)·τ(χ^m,ψ)·Π_a τ(ρ^a,ψ)`
　　＝ **Gauss 乘法公式的函数域类比** ⟹ 它**正是**把 A 侧与 M 侧锁在一起的**精确关系** ✓（经典 ⟹ 已有同物 ✗）
　· 另有 **lifting relation**（`(−1)^s τ(χ,ψ)^s = −τ(χ',ψ')`）｜**norm relation**（`G(χ,ψ)·overline{G(χ,ψ)} = p`）｜
　　**Stickelberger**（素理想分解）｜**explicit multiplicative relations between Gauss sums**（LSU 学位论文）✓
　· 其余交叉结果**皆为不等式型**：**sum–product**（Erdős–Szemerédi／Bourgain–Katz–Tao／Guth–Katz／Rudnev）｜
　　**Tao 加性界** `|supp f| + |supp \hat f| ≥ p+1`（经 Chebotarëv）｜**乘性乘积界** `|supp f|·|supp \hat f| ≥ |G|` ✓
　⟹ 依阶梯："**只有不等式、没有新结构 ⟹ DEAD**" ✓
```

## §3 ⭐ 判定

```
【CROSS-0 判定】 ⛔ **DEAD**（**三重触发**：Q1 已有同物 ✓｜Q2 直接重写 ✓｜Q4 只有不等式型 ✓）✓✓
【⭐ 生成器级后果（依唐先生 21:16 预告条款，条件已满足）】
　$$\boxed{\text{"两个表示交互"生成器 = 正式封死（不再以"换两种表示／换交叉量名称"续命）}}$$ ✓✓
【⚠️ 关于那条 2026 预印本（诚实标注）】
　· 出处＝**viXra / rxiv**（`vixra.org/abs/2601.0101`）⟹ **非同行评审** ⚠️ ⟹ **不可作权威证据** ✓
　· 但其"**加法×乘法不相容**"的 framing **本不新**（**sum–product 理论即经典**）⟹ 唐先生"不能把 A×M 不相容申报为新机制"的判断**成立**，且**不依赖**该预印本 ✓
　· 它给的作用＝**筛子**（若我方 cross-invariant 只是"additive/multiplicative 不相容"的包装 ⟹ DEAD ✓）——本档已按其筛 ✓
【与既有负资产一致】 与 `D-11`（C-α：下降环被反例结构性排除）同型：本档＝**"交互"机制被既有交叉机器全覆盖** ✓
```

## §4 边界与回查（✗✓）

```
✗ 零计算／未写程序／未碰 RH／未调用 C-380／未放宽门槛／**未开案** ✓
✗ 不把"三问皆 DEAD"记为战绩 ✓；**未**声称加性-乘性分析领域无价值（该领域**活跃** ✓）
⚠️ 证据等级＝**题录级**；⚠️ 一条来源为**非同行评审预印本**（已标注，且其结论不依赖该源 ✓）
【技术词回查（`scripts/tech_word_check.sh`，**先跑后写** ✓；逐字粘贴 ✓）】
　技术词 加性乘性交叉  命中文件数=0 ⟹ **本档新增** ✓
　技术词 交叉守恒律    命中文件数=0 ⟹ **本档新增** ✓
　技术词 第三关系      命中文件数=0 ⟹ **本档新增** ✓
　技术词 基底不相容    命中文件数=0 ⟹ **本档新增** ✓
　技术词 cross-invariant 命中文件数=0 ⟹ **本档新增** ✓
【外部来源（**题录级**）】 Keith Conrad, *L-functions for Gauss and Jacobi sums* ✓｜Wikipedia, *Hasse–Davenport relation*（1935；lifting／product 两式）✓｜
　Mathlib `NumberTheory.GaussSum`（`gaussSum χ ψ` 已形式化）✓｜Handbook of Finite Fields（Gauss sum 作基变换系数）✓｜
　Glibichuk 2011（mixed energy）｜Mudgal（AJM，mixed energies ＋ low arithmetic interaction）｜arXiv:1410.1156｜arXiv:2602.01781（2026）｜
　Tao 加性不确定性；有限阿贝尔群乘性不确定性 ✓
```
