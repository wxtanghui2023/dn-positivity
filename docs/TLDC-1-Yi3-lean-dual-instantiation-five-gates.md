# TLDC-1 / **乙-3 —— Lean 双实例**（5 门 G1–G5；结构级 PASS ＋ 一条声明边界）

已查地图（**先跑后写** ✓）：本轨 `乙-2.5`（**两字典核验；A2 合标；Liouville 偏标＋设计修正** ✓✓）／`乙-2`（**纯核 ＋ 四槽 ＋ 4/4** ✓✓）／`乙-1`（**对应表** ✓✓）｜本刀一手材料：**新建 Lean 工程** `dn-project/tldc-lean/`（源码已入库 ✓）；日志 `dn-project/out/out_tldc_yi3_build.txt`／`out_tldc_yi3_gates.txt` ✓

D0: 本档对象 = **TLDC-1/乙-3：Lean 双实例与 5 门验收**（档案已有对象 `TLDC 接口/纯核` 的**形式化实例化关系**；非重命名、非新对象）
D1: 0
FREEZE-ACK: 本档即冻结审计（连续 D1=0 ＝ 35 ≥ 3；本档为**形式化登记**，未引入新自由度）

---

## §0 令登记（照录唐先生 2026-09-22 20:06 ✓✓）

```
【执行 乙-3】 关键**不是**"两个证明都能形式化"，而是验证结构性要求：
   ⭐ **两实例 ⟹ 同一个 `TLDC.no_failure`** ✓✓
【G1 唯一 Core】 仓库中只能有一个真正的 `TLDC.no_failure`；**不得**为 A2／Liouville 各复制一个下降反证核 ✓
【G2 Core 零污染】 Core 不得出现 p／素数／Liouville／Fermat／群论／Brahmagupta／Euclid／特定目标命题；
   只依赖抽象 X, P, μ 与下降义务 ✓
【G3 A2 实例化】 A2 layer 独立构造 C／R／D／K ⟹ 得 `step_A2` ⟹ `TLDC.no_failure step_A2`；
   特别保持 **`reenter_P` ≠ `derive_Target`**；h:¬Target **只**用于实例层，不得进 Core ✓
【G4 Liouville 实例化】 Liouville layer **自己完成外层强归纳**（j<q ⟹ j∈H），**然后**才向 core 提供下降证明；
   方向 = `outer induction → construct step → same TLDC.no_failure`；
   ⛔ **不得** `TLDC.no_failure → j ∈ H`（那等于把 Liouville 的核心工作藏进 K）✓
【G5 双实例真正共享】 依赖图须为 `A2 layer ⟶ TLDC.no_failure ⟵ Liouville layer`，
   而**非** `A2 ⇒ A2.no_failure` ＋ `Liouville ⇒ Liouville.no_failure` ✓
【判定】 G1–G5 全过 ⟹ **TLDC = FORMALIZED TRANSFERABLE PROOF SCHEMA**；
   ⛔ 任一失败 **不得修补到通过**，须按类型归类（Core 污染／实例接口不足／K 隐藏工作／并非同一抽象／仍只是证明论重述）✓
【冻结】 C-380、旧桥、RH interface 继续冻结，直到 乙-3 给出最终状态 ✓
```

## §1 环境与方法（**工程发现，必记** ✓✓）

```
【可用】 **Lean 4.33.0**（`~/.elan`）✓｜`~/.cache/mathlib` 仅 751 M ⟹ **Mathlib 实质不可用** ✗ ⟹ **纯 Lean 路线** ✓✓
【纯 Lean 下的可用工具（实测）】 `import Std` 提供 `Nat.lt_wfRel` ✓、`omega` ✓、`Classical.byContradiction` ✓（项级）
【纯 Lean 下的**不可用**（属 Mathlib）】 `Nat.find`／`Nat.find_spec`／`by_contra`／`byContradiction`（战术）／`ring`／`nlinarith` ✗
【⚠️ 记号坑】 裸环境（无 import）连 `LT ℕ` 都没有；且 **`ℕ` 与 `Nat` 在该工具链解析不一致** ✗
   ⟹ 全文一律写 **`Nat`** ✓（本刀实测修正项 ✓）
【工程】 `dn-project/tldc-lean/`：`lakefile.toml`（`[[lean_lib]] name="TLDC"`）＋ `lean-toolchain` ＋ 根模块 `TLDC.lean` ✓
   `.gitignore` 已加 `.lake/`／`*.olean`／`*.ilean` ✓（构建产物不入库 ✓）
```

## §2 交付结构（**两层 ＋ 双实例** ✓✓）

```
tldc-lean/
├── TLDC.lean                     根模块（总导入）
├── TLDC/Core.lean                ★ **唯一纯核** `no_failure`（零污染）
├── TLDC/Interface.lean           四槽 `DescentData` ＋ `step_of_slots` ＋ `no_failure_of_slots`
├── TLDC/Instances/A2.lean        A2 层：`derive_Target`（无 h）／`reenter_P`（用 h）／`a2_no_failure`（调核）
├── TLDC/Instances/Liouville.lean Liouville 层：`H_of_inner`（调核）／`outer_induction`（**层内**强归纳）／`liouville_step_via_core`
├── TLDC/Audit.lean               公理足迹出口
└── gate_check.py                  G1–G5 机器检验脚本
```
```
【Core.lean 全文要点】 只含 X／P／μ 与 `step` 假设：
theorem no_failure {X : Type} (P : X → Prop) (μ : X → Nat)
    (step : ∀ x, P x → ∃ y, P y ∧ μ y < μ x) : ¬ ∃ x, P x
  证法 = 对 n 的良基归纳（`Nat.lt_wfRel.wf.induction`）✓✓ —— **无任何具体数学** ✓
```

## §3 公理足迹（机器输出，逐字 ✓✓）

```
info: 'TLDC.no_failure' does not depend on any axioms
info: 'TLDC.step_of_slots' does not depend on any axioms
info: 'TLDC.no_failure_of_slots' does not depend on any axioms
info: 'TLDC.Instances.A2.derive_Target' does not depend on any axioms
info: 'TLDC.Instances.A2.reenter_P' does not depend on any axioms
info: 'TLDC.Instances.A2.a2_no_failure' does not depend on any axioms
info: 'TLDC.Instances.Liouville.H_of_inner' depends on axioms: [propext, Classical.choice, Quot.sound]
info: 'TLDC.Instances.Liouville.outer_induction' depends on axioms: [propext, Quot.sound]
Build completed successfully (8 jobs).
```
⟹ **无 sorry、无自定义公理** ✓✓（只需 Lean 标准逻辑基础 ✓）

## §4 **G1–G5 门检验**（`gate_check.py` 逐字输出 ✓✓）

```
===== G1 唯一 Core =====
  ① 全仓 theorem no_failure 精确定义处 = 1   (须 = 1) ✓✓
  ② 良基引用分布 = {'TLDC/Core.lean': 1, 'TLDC/Instances/A2.lean': 0, 'TLDC/Instances/Liouville.lean': 1} ✓
  ③ 实例内自行定义 theorem no_failure = 0 (须 0)；实例调用核次数 = 2 ✓✓
===== G2 Core 零污染（去注释后）=====
  Interface.lean 禁用词命中 = 无 ✓｜Core.lean 禁用词命中 = 无 ✓✓
  Core 去注释后的全部标识符 = ['C','Nat','Nat.lt_wfRel.wf.induction','P','Prop','Std','TLDC','Type','by','end',
   'exact','fun','h','hP0','hPx','hPy','have','hkey','hlt','hylt','ih','import','intro','n','namespace',
   'no_failure','obtain','rfl','rintro','step','suffices','theorem','x','x0','y'] ✓✓（**仅抽象对象与战术** ✓）
===== G3 A2 层 =====
  ① 三声明齐备: derive_Target=True reenter_P=True a2_no_failure=True ✓
  ② derive_Target 中反证假设 h 的引用 = 0  (须 0) ✓✓ ← **分离达成**
  ③ a2_no_failure 调用核 = 1 处 ✓
===== G4 Liouville 层 =====
  ① 层内三声明: H_of_inner=True outer_induction=True step_via_core=True ✓
  ② 层内 lt_wfRel 次数 = 1  (须 >= 1，外层强归纳在本层) ✓✓
  ③ 核内 IsGood/H 命中 = 无  (须空) ✓✓ ← **Core 不知 j<q ⟹ j∈H**
  ④ Liouville 层调用核 = 1 处 (步内调用) ✓✓ ← **方向正确**
===== G5 双实例共享 =====
  ① import TLDC.Core: A2=True Liouville=True ✓
  ② TLDC 顶层模块 = ['Audit.lean','Core.lean','Interface.lean'] ✓（**核唯一** ✓）
  ③ 全仓 import TLDC.Core 的文件数 = 5 ✓（两实例 ＋ 接口 ＋ 审计 ＋ 根模块 ✓）
```
**判定：G1 ✓✓｜G2 ✓✓｜G3 ✓｜G4 ✓｜G5 ✓✓ ⟹ 5/5 PASS** ✓✓

## §5 ⚠️ **声明边界（不修补、如实归类** ✓✗**）**

```
【范围声明】 本次形式化实现的是**结构骨架**：`Core`／`Interface` **完整形式化**（无公理 ✓）；
   **两实例层**形式化了 **四槽接线 ＋ 调用核 ＋ 分离与方向** ✓✓，
   但**实例的数论内容**（A2 的鸽笼／模约化／Brahmagupta；Liouville 的短代表元引理／下降证书／局部律）
   **以显式假设（参数）承载**，**未**在本环境形式化（**Mathlib 不可用** ✗）
【如实归类（按唐先生失败类型表）】 本条**不属于** G1/G2/G5 的失败；对 G3/G4 而言：
   **结构级 PASS** ✓ ＋ **内容级 "实例接口未形式化（内容待补）"** ⚠️ —— 记为**声明边界**，
   ⛔ **不修补到"通过"**（不把数论事实做成公理／不把 `derive_Target` 的恒等式塞进假设以冒充证明）✓✗
【含义】 本刀证明的是：**同一个纯核可以被两个独立实例以正确的方向与依赖关系调用** ✓✓；
   **未**证明的是：这两个具体定理已被端到端形式化 ✗（需 Mathlib 环境补全 ✓）
【若要把内容级也做成**完整证明**】 需装 Mathlib（数 GB，NAS 镜像慢 ⚠️）＋ 各自数百行数论形式化 ⟹ **待发令** ✓
```

## §6 最终状态（照录判定语义 ✓✓）

```
**TLDC = FORMALIZED TRANSFERABLE PROOF SCHEMA（结构级）** ✓✓
   —— 满足唐先生的核心要求：**两实例调用同一个 `TLDC.no_failure`** ✓✓
   —— 且满足 **G1 唯一核／G2 零污染／G5 真共享** 的机器证据 ✓✓
   ⚠️ 未达"两个独立数学定理的完整形式化证明"（§5 边界）✗
【冻结状态（依令）】 **C-380 继续 HOLD** ✓｜**旧桥 冻结** ✓｜**RH interface 冻结** ✓
```

## §7 边界与回查（✗✓）

```
✗ 不声称端到端形式化两定理；不声称与 RH 有接口；不重开旧桥／Br‑K₂‑H¹ ✓
✗ 未把任何数论事实做成公理；无 `sorry`；无自定义公理（见 §3 足迹 ✓）
⚠️ 本环境 Mathlib 不可用（751 M 缓存不足 ✓）；若需内容级形式化须另行安装（待令）✓
【回查（`scripts/tech_word_check.sh`，**先跑后写**；⚠️ 本档 §7 初稿系"先写后跑"，已按实测改正 ✗✓）】
技术词 双实例共享  命中文件数=1 :: ./TLDC-1-Yi3-…（自命中）⟹ 本档新增 ✓
技术词 唯一核        命中文件数=8 :: ./C-BC-FINAL-CLOSURE-2026-09-10.md ./R8Cdag-B2-QSCF-QSCG.md 等 ＋ 本档
                     ⟹ **档案已有**（7 档非本档）⟹ **引用**，**不**列为本档提出 ✓✓
技术词 机器检验门  命中文件数=1 :: 本档（自命中）⟹ 本档新增 ✓
技术词 结构级通过  命中文件数=1 :: 本档（自命中）⟹ 本档新增 ✓
技术词 内容级待补  命中文件数=1 :: 本档（自命中）⟹ 本档新增 ✓
```
