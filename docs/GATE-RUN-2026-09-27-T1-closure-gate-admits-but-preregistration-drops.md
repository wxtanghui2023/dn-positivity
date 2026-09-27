# GATE-RUN-2026-09-27 — T-1 过 `closure_gate`（ADMIT）**但**预登记判除 ⟹ DROP；并发现**门缺口** ⚠️

**已查地图：命中（本档为既有门／既有条目之运行与审计，非新案）**
所查：`scripts/closure_gate.py`（**E0 判定主体已逐行读取** ✓）｜`scripts/family_theorem_registry.json`（**8 条：3 机器判定理 ＋ 5 关键词指纹** ✓）｜`docs/Zarankiewicz-A3-source-check.md`（**记录型 #4 判定 D ＋ 预登记** ✓）｜`docs/RESEARCH-CONSTITUTION.md`（**AMEND-21 原文** ✓）｜`docs/FOUR-GATE-RESCREEN-2026-09-24.md`（G1–G4 定义 ✓）｜`docs/FRONTIER-R1-2026-09-26-...md`、`FRONTIER-R3-2026-09-27-...md` ✓
D0: 本档对象 ＝ **档案已有**门（`closure_gate.py`）与**既有条目** T-1 的**运行结果与规则审计**（重命名：否 ✗；新对象：无 ✗）
D1: 0（门运行 ＋ 审计；不主张新自由度 ✓）

**纪律** ✓：**零计算**（门为规则判定，非数值推导）✗｜未改门、未改宪章 ✗（唐先生/宪章未批 ✓）

---

## §0 判定（先给 · 两条并列，不可混）

$$\boxed{(1)\ \textbf{E0/closure\_gate：ADMIT}\ \text{（5 闸齐 OPEN/PASS ＋ 无机器判定理 ＋ 无指纹命中）}\ ✓✓}$$
$$\boxed{(2)\ \textbf{项目预登记：判除（DROP）}\ \Longrightarrow\ \textbf{T-1 仍 DROP}\ \text{——依据}＝\text{预登记，}\textbf{不是}\text{门}\ ✓✓}$$
$$\boxed{(3)\ ⚠️\ \textbf{门缺口}：`closure_gate.py` \textbf{未实现} AMEND-21 的「未覆盖}≠\text{未知」禁令，亦\textbf{未含} owner/工业化（E5）前置问} \Longrightarrow \text{门会放行项目已判除的条目}\ ⚠️$$
**跑门输出（逐字，`scripts/T1_CHECK_closure_gate.txt`）** ✓
```
[ADMIT  ] T-1-zL(5,5)
[BLOCKED] CTRL-P7-2-forbidden-configuration-boundary
           · 指纹命中: EJC-DS20v2-Thm-1.13-1.14 —— KNOWN — 边界已被完全判定（下一层由 Anstee–Sali 猜想支配）
合计: BLOCKED=1  ADMIT=1  HOLD=0
```
**⟹ 阳性对照 BLOCKED ⟹ 门**本身**工作正常** ✓（1/1 对照命中）；T-1 的 ADMIT **非**门故障，而是**门规则未覆盖该类风险** ⚠️

---

## §1 E0 完整判定规则（逐字取自 `closure_gate.py` ✓）

```
① 机器判定理（machine_checks）：计数必要条件 k(k-1)=λ(v-1)；skew Hadamard 参数型的素数幂必要条件；
   CXS 指数界（p-群、p≡3 mod 4、s>⌊(m+1)/4⌋）——**仅对差集/skew Hadamard 型对象生效** ✓
② 指纹命中（fingerprint_hits）：对 registry 中 machine_check≠yes 的条目，fingerprint 文本命中
   **≥2 个关键词** ⟹ 命中 ⟹ **BLOCKED**（需人工确认匹配 ✓）
③ E4 五金：e4_0 语义／e4_1 精确实例／e4_2 家族定理／e4_3 必要条件闭包／e4_4 现状核验
   ——**五者 verdict ∈ {OPEN,PASS} 且 evidence 非空 ⟹ ADMIT**；否则 **HOLD** ✓
④ kills 或 hits 非空 ⟹ **BLOCKED**（优先级最高）✓
```
**注册表实况** ✓：`machine_check=yes` 3 条（CXS-exponent-bound／SHDS-v-prime-power／SHDS-counting-relation）；`machine_check=no` 5 条（EJC-DS20v2 边界分类／乘法子群∩加法平移／small-doubling／cyclotomic-order-3／ramsey-DS1.18）— 关键词组见上输出 ✓

---

## §2 为何仍 DROP（三条依据，独立充分 ✓）

**依据 1（项目预登记 · 最硬）**：`docs/Zarankiewicz-A3-source-check.md`（**2026-09-24 22:33**，晚于 T-1 的"首攻"标记 13:39／13:52）逐字：
> 「A3 定式输出 …… 4 │ limited augmented Zarankiewicz $z_L$ │ MDPI Symmetry 18(7):1076 (2026) │ 构造＋上界论证 │ **是** │ **D**」
> 「**AMEND-21（主闸）＝ 判除** —— 计算路线成熟且**正在高速产出**（单年数十个新精确值）⟹ 不因"数学上未完全解决"而生成 A 候选」
> 「照预登记规则：**不在 Zarankiewicz 内部改参数救场**；直接进入 A4」✓✓

**依据 2（AMEND-21 禁令本身）**：标题即「**"三合一未覆盖"＋"未覆盖≠未知"禁令**」⟹ 文献未覆盖 **不得**当作"可攻/未知" ⟹ T-1 恰属此类（我方"未覆盖"但**有主且高产**）✓

**依据 3（同形赛跑 ＋ 工业化）**：MDPI 文 §1 逐字：「These results are obtained by **enumerating all non-isomorphic extremal $C_4$-free graphs** … for $5\times3$ and $5\times4$ are provided in the appendices」⟹ 5×5 正是**同组下一步**；且第二组（arXiv:2605.09926）已把 5×5 推到 $z_{3L}(5,5)\ge16$；叠加 `A3` 的 **E5 校准**（"dent＋证书＋入库"形态已被 AI 加速独立研究者工业化）✓

---

## §3 门缺口（⚠️ 本轮新发现 · 待唐先生裁决是否补门）

| # | 缺口 | 后果 | 建议（**须唐先生批** ✓） |
|---|---|---|---|
| G-1 | **无 owner／工业化前置问（E5）** | 门会放行"有主且高产"的条目（如 T-1） | 增 **E5 闸**：候选 JSON 增 `owner: {exists, route, recent_outputs}` ⟹ owner 存在且近期高产 ⟹ **BLOCKED/HOLD** |
| G-2 | **未实现"未覆盖≠未知"禁令** | "文献检索未覆盖"被当成 E4-1/E4-2 的 OPEN 证据 | E4 增加**反证义务**：OPEN 须附"为何不是'无人做'造成的假 OPEN"（即须给近期产出清单） |
| G-3 | E4 五闸可**同类证据重复填**（本档即诚实填法） | 五 OPEN 齐即可 ADMIT，实际风险未被表达 | 增 **evidence 独立性**要求（五闸 evidence 不得同源） |

**纪律说明** ✗：**不擅自改门**（`RESEARCH-CONSTITUTION` 明文：在出现真机制前不改宪章）⟹ 本档**只登记缺口并请示** ✓

---

## §4 T-1 三点 source 核验（**已跑完** ✓ · 详见姊妹档）

| 点 | 结果 | 档 |
|---|---|---|
| ① `z_L` 定义逐字 | **锁定 ✓✓**（Symmetry 18(7):1076 §1/§2：1-edges／2-edges 四元组／非退化·行退化·列退化／禁 generalized $C_4$） | `docs/T1-CHECK-2026-09-27-...md` §1 |
| ② 是否仍 open | **仍 open ✓✓**（arXiv:2604.04111 逐字：*"The exact value of $z_L(5,5)$ remains open; here a lower bound of 15 was established"*；并解决库存"14 vs 15"疑点：14＝前作下界） | 同上 §2 |
| ③ extremal $C_4$-free 5×5 分类 | **未被收割，但是同组下一步** ⚠️（作者已对 5×3／5×4 做完整枚举并置于附录） | 同上 §3 |

**⟹ 点②为"真 open"**（作者自述）⟹ 门 ADMIT 合理；**但**依据 §2 三条 ⟹ **DROP** ✓

---

## §5 交棒 §T-5（下一刀 · 仍不计算 ✓）

**T-5 三点**（**不得预设 $n=8$ 首攻** ✓）：
1. **规模核实**：目标阶**图数**（库存"约 $10^4$"仅为估计 ⟹ 须以 $n\,C_2$ 计数／OEIS 核）
2. **已知完备阶数**：文献已解决的**阶数阈值**
3. **公开证书状态**：**结果已解决** vs **仅有算法／部分族**？是否有公开库/程序产出完整表？（**E5 前置问** ✓）
**红线**：**"存在算法" ≠ "问题已解决"** ✗；三点未过不得设计计算 ✗

## §6 诚实边界

- 门为**规则判定**，非数学证明 ✓；本档**不主张** T-1 在数学上不可做 ✗（V290）—— 只写"**该条目已归位：记录型、有主、同形赛跑**" ✓
- 缺口 G-1～G-3 为**建议**，未落地 ✗；未改任何既有文件 ✓

## §7 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "门缺口"
技术词 门缺口        命中文件数=2    :: ./ASSETS-REGISTRY.md ./GATE-RUN-2026-09-27-T1-closure-gate-admits-but-preregistration-drops.md
$ bash scripts/tech_word_check.sh "工业化"
技术词 工业化        命中文件数=8    :: ./ASSETS-REGISTRY.md ./LJCR-A5-difference-sets-source-check.md ./WHY-OTHERS-GO-FAR.md
$ bash scripts/tech_word_check.sh "未覆盖"
技术词 未覆盖        命中文件数=169  :: ./CANDIDATE-SCAN-1-mathematical-content-review.md ./BFREEZE-2026-09-27-transferable-assets-T1-T5-and-stop-rationale.md ...
$ bash scripts/tech_word_check.sh "owner"
技术词 owner         命中文件数=15   :: ./EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md ./STRATEGY-2026-09-25-two-lines-missing-global-invariant.md ./ASSETS-REGISTRY.md
```
- **本档新增**：**0** 个术语 ✓（`门缺口` 命中 2 档，均为**本档产出线**（本档 ＋ 本档同步更新的 `ASSETS-REGISTRY` 条目）⟹ 仅**标签级**首次使用，**不作新性主张** ✓）
- **档案已有（引用，不列为提出）**：`工业化`（8 档，含 `A3` 的 E5 校准 ✓）｜`未覆盖`（169 档）｜`owner`（15 档）✓
- **通用词（不计）**：`闸`／`证据`／`放行` ✓
- **声明**：G-1～G-3 是**既有门规则的缺口**（非新对象）；其"新"指「**项目此前未登记**」，属**审计发现**，不构成数学新性主张 ✓
