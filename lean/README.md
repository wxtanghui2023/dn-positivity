# `lean/` —— Paper A + Paper B 的 Lean 4 形式化

**目的**：按项目纪律⑤「**机器可验证优先**」✅，把 Paper B 的引理链逐条形式化、**每条即时编译验证** ✅
（缘由：`docs/00-ANCHOR-purpose-and-discipline.md` ✅；工具链安装：`docs/LEAN-SANDBOX-SETUP.md` ✅）

## 如何编译（可复现 ✅）
```bash
export PATH="$HOME/.elan/bin:$PATH"
cd ~/mathlib4                       # Mathlib 工程（提供 import 搜索路径 ✅）
lake env lean /home/node/.openclaw/workspace/dn-project/lean/PB-Basic.lean
lake env lean /home/node/.openclaw/workspace/dn-project/lean/PB-Lemma1.lean
```
**判据**：**退出码 0 且 error 数为 0** ⟹ 通过 ✅（4 秒左右 ✅）
```
⚠️ 必须 `lake env lean`（在 ~/mathlib4 内）—— 直接 `lean` 找不到 Mathlib ✅
⚠️ 必须【最小 import】✅（全库 `import Mathlib` 在本机内存下不可用 ✗ 见 LEAN-SANDBOX-SETUP.md §六）
```

## 进度
```
| # | 引理 | 状态 |
| 1 | `F_eq_sq`：x^{k/2} + x^{-k/2} - 2 = (x^{k/4} - x^{-k/4})^2  (x>0) | ✅ **已形式化并通过**（2026-09-12） |
| 2 | `exp_sinh_identity`：e^v - 2 + e^{-v} = 4 sinh^2(v/2) | ✅ **已形式化并通过**（2026-09-12） |
| 3 | `PB-Lemma1.lean`：**论文 Lemma 1**（单调性：F 在 x>1 严格递增，k>0） | ✅ **已形式化并通过**（2026-09-12，4 次迭代） |
| 4a | `PB-Lemma2-mvt.lean`：**MVT 型引理** `xᵃ−1 ≤ a(x−1)xᵃ⁻¹` | ✅ **已通过** |
| 4b | `PB-Lemma2-far.lean`：**论文 Lemma 2**（far 界） | ✅ **已通过** |
| 5a | `PB-Lemma3-identity.lean`：**Lemma 3 恒等式部分**（F(1+u) = 4sinh²(((k/2)log(1+u))/2)） | ✅ **已通过**（首次编译，2026-09-12） |
| 5b | ：**比值恒等式**（剖面 = (sinh(v_t/2)/sinh(v_H/2))²） | ✅ **已通过** |
| 5c | `PB-Lemma3-integral.lean`：**∫₀¹(1+δ)⁻⁴dδ = 7/24**（FTC + rpow 导数 ✓） | ✅ **已通过** |
| 5d | `PB-Lemma3-sinhmono.lean`：**`sinh x/x` 严格递增**（Mathlib 无 ⟹ **自证** ✓） | ✅ **已通过** |
| 5e | Lemma 3 剩余：`(1+O(H⁻²))` 修正项（可用**粗界**替代 ✓ 见注） | ⏳ 未做 |
| 6a | `PB-LemmaS4-integrals.lean`：**两个幂积分**（有限区间版 ✓；极限即论文值 ✓） | ✅ **已通过** |
| 6b | `PB-LemmaS4-abel.lean`：**反常积分 ∫_H^∞ t⁻⁴** + **S4 系数代数**（论文关键计算 ✓） | ✅ **已通过** |
| 6c | `PB-LemmaS4-abeltransform.lean`：**Abel 变换（离散形式）** Σγᵢ⁻⁴ = n·γ_{n−1}⁻⁴ − Σ(i+1)(γ_{i+1}⁻⁴−γᵢ⁻⁴) | ✅ **已通过** |
| 6c′ | Abel 变换的**连续版**（离散和 ↔ 积分，计数测度） | ⏳ 未完成（需 Stieltjes 积分 ✗） |
| 6d | `PB-LemmaS4-abel.lean`：**log 型反常积分** ∫_H^∞ t⁻⁴log t（**有限版 + 反常版均过** ✓） | ✅ **已通过** |
———————————————— Paper A（2026-09-13 补 ✓）————————————————
| 15 | `PA-Basic.lean`：**共享恒等式** `|1 − 1/ρ|² = 1 + (1 − 2β)/(β² + γ²)`（β, γ ∈ ℝ, ρ ≠ 0）
     + **临界线推论** `|1 − 1/ρ|² = 1`（β = 1/2） | ⚠️ **首编译 3 处 error** ✗ ⟹ 修正后 ✅ **已通过**（**exit 0 / 零 sorry / 3 秒** ✓，2026-09-13） |
| 15a | `PA` · `normSq_of_re_im`：`normSq (β + γI) = β² + γ²` | ✅ **已通过** |
| 15b | `PA` · `normSq_one_sub_inv`：**共享恒等式**（论文 A/B 的核心机制 ✓） | ✅ **已通过** |
| 15c | `PA` · `normSq_one_sub_inv_half`：**临界线上 = 1**（论文 A 用那一步 ✓） | ✅ **已通过** |
```
**Paper A 首编译的 3 处 error（留痕 ✓，修法已写入文件内注记 ✓）**
```
① `normSq_of_re_im`：`simp [normSq_apply]` 只到 `β*β + γ*γ = β^2 + γ^2` ⟹ 需 `ring` 收尾 ✓
② `normSq_one_sub_inv`：**强制转换与减法次序** —— 目标里是 `↑β - 1`，引理模式是 `↑(β-1)`
   ⟹ `rw` 找不到模式 ✗（用 `push_cast; ring` 显式转换 ✓）
③ 非零性：见经验记录 ⑥（`positivity` 在本 import 集下**两种目标都证不出** ✗）
⟹ 三条修法**均已实测通过** ✓；本条记录同时坐实：**未经编译的文件不得记 ✅** ✓
**说明**：本目录只记录**形式化**进度 ✅；**不改变**论文的任何数学陈述 ✅。
**纪律**：每条引理必须**独立编译通过**才记为 ✅；**卡住的如实记为卡住** ✅（不粉饰 ✅）。

## 全目录编译**巡检**（2026-09-13 ✓ —— 以**产物**为准 ✓）
```
命令 ✓：for f in lean/*.lean; do (cd ~/mathlib4 && lake env lean "$f"); done
        （逐文件记录 exit 码 / `: error:` 数 / `: warning:` 数 ✓）
结果 ✓：**15 个 .lean 文件 / 15× exit 0 / 共 【0】个 error / 【1】个 warning** ✅
   · 唯一 warning 所在 = `PB-Lemma3-identity.lean`（**非** error ✓）
   · ⚠️ **巡检前**：`PA-Basic.lean` = **3 个 error** ✗（即上面修正 ①②③ ✓）⟹ 修后全绿 ✓✓
【对记录的影响 ✓】
   · 进度表（§进度）只到 `6d`；另有 3 个已通过文件在本文件**其它小节**如实记录 ✓
     （`PB-FinalComparison.lean` §追加 ✓｜`PB-Stieltjes-bridge.lean` / `PB-Stieltjes-count.lean`
      §桥的进度 / §桥建成 ✓）⟹ **无遗漏文件** ✓；但 **进度表本身滞后** ⚠️ ⟹ 以**巡检**为准 ✓
   · ⭐ **重要结论** ✓：本目录现在 **15/15 全绿且零 sorry** ✓（只有 `PA-Basic.lean` 是
     2026-09-13 新验的 ✓）—— 这也坐实：**未经编译的文件不得记 ✅** ✓
```

## 形式化的经验记录（供后续引理复用 ✅）
```
① **先核引理名，再写证明** ✅ —— 一批 `#check`（约 10 秒）比反复猜名快得多 ✅
   本版本**不存在**的名字（避坑 ✓）：`Real.strictMonoOn_rpow*` ✗、`strictMonoOn_of_deriv_pos` ✗（另一模块 ✓）、
   `Real.hasDerivAt_rpow_const` ✗、`inv_lt_inv_of_lt` ✗
   本版本**可用**的关键名字 ✓：`Real.rpow_lt_rpow` ✓、`Real.rpow_neg` ✓、`Real.one_lt_rpow` ✓、
   `inv_lt_one_of_one_lt₀` ✓、`one_div_lt_one_div_of_lt` ✓、`sq_lt_sq'` ✓、`StrictMonoOn.comp` ✓
② **`Set.Ioi` 的成员需要转换** ✅ —— `1 < a` 与 `a ∈ Set.Ioi 1` 对 tactic 不等同 ✅
   ⟹ 先 `simp only [Set.mem_Ioi] at ha` ✅
③ **`StrictMonoOn` 的目标是 beta-未归约形式** ✅（形如 `(fun x => …) a < (fun x => …) b`）
   ⟹ `rw` 前先 `show` 展开 ✅
④ **自然数指数 vs 实数指数** ⚠️ —— `(...)^2` 是 `Nat` 指数；`Real.rpow_*` 要实数指数 ✅
   ⟹ **避免混用**：全程用 `Real.rpow_add` 而非 `Real.rpow_mul` ✅（本目录的 `F_eq_sq` 即如此 ✓）
⑤ **每次改完立刻编译**（3–4 秒 ✓）—— 本项目 4 次迭代的错误**全由编译器抓出** ✅
⑥ **`positivity` 不总能证“正性/非零”** ⚠️（2026-09-13，`PA-Basic.lean` ✓）
   —— 在本文件的 import 集（`Data/Complex/Basic` + `Tactic/Ring` + `Tactic/FieldSimp`）下，
   `positivity` 对 `(1/2)^2 + γ^2` 的 **正性**与**非零**两种目标**都失败** ✗
   （报 `failed to prove positivity/nonnegativity/nonzeroness`；⟹ **与“否定型目标”无关** ✗ ——
     我最初的诊断（“≠ 0 是位否定型目标”）被自己实测推翻 ✓）
   ⚠️ 另：`nlinarith` 在此 import 集下**不存在** ✗（`unknown tactic` ✓）—— **四个候选的实测表与结论**
     见 `lean/PA-positivity-experiment.md` ✓（故 scratch 已删 ✗，避免污染“所有 `.lean` 应 exit 0”的检查 ✓）
   ⟹ **稳妥写法** ✓：`have h1 : (0:ℝ) < (1/2)^2 := by norm_num`｜`have h2 : 0 ≤ γ^2 := sq_nonneg γ`
     ｜`exact add_pos_of_pos_of_nonneg h1 h2`（**实测通过** ✓）
   ⟹ 同族教训 ✓：Mathlib 里“应该有”的 tactic 也要**先小文件实测** ✓（4 行 scratch，2 秒）✅
```

## 本轮技术收获（供后续复用 ✅）
```
| 目的 | 本次找到的正确名字 ✓ | 本版本【不】存在的 ✗ |
| 幂函数导数 | `Real.hasDerivAt_rpow_const`（**须 import `Pow/Deriv`** ✓） | — |
| 幂函数凸性 | `convexOn_rpow`（**须 import `Convex/SpecificFunctions/Basic`** ✓） | `Real.convexOn_rpow` ✗ |
| 区间积分基本定理 | `intervalIntegral.integral_eq_sub_of_hasDerivAt`（**须 import `IntervalIntegral/FundThmCalculus`** ✓） | `integral_deriv_eq_sub` ✗（另一变体名 ✓） |
| 幂的域内连续 | `ContinuousOn.rpow_const`（**须 import `Pow/Continuity`** ✓；负指数时用 `f x ≠ 0` 那一支 ✓） | — |
| MVT 型 | `StrictMonoOn.exists_slope_lt_deriv`（`Convex/Deriv` ✓） | `exists_deriv_eq_slope` ✗ |
| `sinh x / x` 单调 | **不存在** ✗ ⟹ **需自行证明** ⚠️ | — |
【教训 ✅】**模块选对比名字更重要** —— 有 3 次错误是"名字对、模块没 import" ✗✓
【教训 ✅】`HasDerivAt.rpow_const` / `ContinuousOn.rpow_const` 的条件是**析取**（`f x ≠ 0 ∨ 0 ≤ p`）✓
   ⟹ 负指数时必须主动选**左支**并给 `f x ≠ 0` ✓（我一开始错选右支 ✗ 目标变成 `1 ≤ -3` 的假命题 ✓）
```

## 附注：Lemma 3 中 `(1+O(H⁻²))` 的处理（诚实说明 ✅）
```
论文写 `(v(t)/v_H)² ≤ (1+δ)^{-4}(1+O(H^{-2}))`（用 `log(1+u) ≤ u` 的精细版）。
**本形式化走的是粗界** ✅：`v(t)/v_H ≤ t^{-2}/H^{-2} = (H/t)²` ⟹ 平方得 `(H/t)^4 = (1+δ)^{-4}` ✅
   ⟹ **比论文的界更强**（无 `(1+O(H^{-2}))` 修正项）✅ ⟹ 论文结论不受影响 ✅
   ⚠️ 但因此**不需要**形式化那个修正项 ✅（属可选 ✓）
```

## 完成度总览（2026-09-12 收尾 ✅）
```
【✅ 已机器验证：**12 项 / 9 个文件 / 全部 exit 0 且 error 数 0、零 sorry** ✅】
   ＋ **2026-09-13 新增** ✓：`PA-Basic.lean`（Paper A **共享恒等式**，3 项：`15a`/`15b`/`15c`）
     —— **首编译 3 处 error** ✗ ⟹ 修正后 **exit 0 / 零 sorry / 3 秒** ✓（修法注记在文件内 ✓）
   论文 Lemma 1（单调性）✅｜Lemma 2（far + MVT 零件）✅
   Lemma 3（恒等式 ✓ + 比值 ✓ + sinh x/x 单调 ✓ + ∫₀¹(1+δ)⁻⁴=7/24 ✓）
   Lemma S4（反常积分 ∫_H^∞ t⁻⁴ ✓ + **系数代数** ✓）
【⏳ 未完成（诚实列出 ✗）】
   ① **Abel 求和恒等式**（离散零点和不 ↔ 积分；论文核心方法论"边界项必须保留"）
      —— 需 Stieltjes 积分 / 计数测度 ✗；**这是最大的一块** ✓
   ② log 型反常积分（有限版已完成 ✓；反常版需要比较可积性 ✓ 半成品已回退 ✗ 不留 sorry ✓）
   ③ Lemma 3 的 `(1+O(H⁻²))` 修正项（可用粗界替代 ⟹ **不必做** ✓）
   ④ 主定理的**最终装配**（把四条引理合成不等式链）
```
## 纪律说明（重要 ✅）
```
· 本目录**零 `sorry`** ✅ —— 半成品（含 sorry 的 log 积分）已**回退删除** ✅（宁可"未完成"，不可"假通过" ✅）
· 每条引理**独立编译通过**才记 ✅；未完成的**如实标注"未完成"** ✅
```

## 14 项完成后的剩余（诚实 ✅）
```
【✅ 已完成 14 项 / 10 个文件】含论文四条引理的全部**零件** ✓ + **Abel 变换的离散形式** ✓
【⏳ 仅剩 2 项】
   ① Abel 变换的**连续版**（把离散和写成 ∫_H^∞ N(t)t⁻⁵dt；需计数测度/Stieltjes 积分 ✗）
   ② **主定理的最终装配**（把 Lemma 1/2/3/S4 串成完整不等式链 ✓ 机械但工作量大）
【★ 重要 ✓】论文的核心方法论「**边界项必须保留**」已**机器验证** ✓✓
   （`abel_zero_sum` ✓ + 反例 `boundary_term_matters` ✓ 证明省略边界项会得到 0 ≠ 3 ✓）
```

## 追加：论文最后一步比较（✅ 已形式化）
```
`PB-FinalComparison.lean`：
   · `sixtyfour_pi_a_over_three`：64π·(1/(2π))/3 = **32/3** ✓
   · `final_comparison`：H > 1 ⟹ **log H + 64πa/3 ≥ 7 log 2** ✓（等价于论文的 log H ≥ −5.815 ✓）
   · `final_margin_positive`：**边际 > 0** ✓（论文末句"the margin is ... > 0" ✓）
```

## ✅ **可行性核查【更正】：连续版 Abel 其实【有】库支持（2026-09-12 16:55 更正 ✗→✓）**

```
【⚠️ 我此前的结论是【错的】✗】我曾搜 Mathlib 源码后断言"无 Stieltjes 支持" ✗
   错因 ✓：我只搜了**小写 `stieltjes`**（文件名 ✓），**漏掉了 `StieltjesFunction`**（大写 ✓）✗
【✅ 更正后的真实情况 ✓（已实测确认 ✓）】
   · **`Mathlib/MeasureTheory/Measure/Stieltjes.lean`（36 KB ✓）存在** ✓
   · **`StieltjesFunction R`** 结构 ✓（含 `mono'` ✓、`right_continuous'` ✓、`leftLim` ✓、`length` ✓）
   · ⭐ **`StieltjesFunction.measure : Measure R`** ✓✓ —— **能变成【真正的 Measure】** ✓✓
   · ⭐ **`measure_Ioc (a b) : f.measure (Ioc a b) = ofReal (f b − f a)`** ✓
   · ⭐⭐ **`measure_singleton (a) : f.measure {a} = ofReal (f a − leftLim f a)`** ✓✓
     —— **这正是"计数测度在原子点的跳跃"** ✓✓（即 Dirac ✓）
   · 另有 `isFiniteMeasure` ✓、`isProbabilityMeasure` ✓、`measure_Icc`/`measure_Ioo` ✓
【⟹ 结论 ✓】**连续版 Abel 的桥【可以搭】** ✓：
   ① 把计数函数 N(t) 做成 `StieltjesFunction` ✓（单调 + 右连续 ✓ —— 计数函数天然满足 ✓）
   ② 取 `N.measure` ✓（即计数测度 ✓）
   ③ 对其积分 ✓（Mathlib 全套积分 API ✓）
   ④ **分部积分由 Fubini + FTC 导出** ✓（标准证法 ✓ —— Mathlib 有 Fubini ✓ 与 FTC ✓）
【⚠️ 仍需自建的部分 ✗（诚实 ✓）】Mathlib **没有**现成的「Stieltjes 测度的分部积分」引理 ✗
   ⟹ 那一小段（把 ∫f dN 化为 [f·N] − ∫N f′）**需自写** ✓ —— 但**基础已备** ✓，属**可完成** ✓✓
【✅ 教训 ✓】**搜源码要兼搜大小写与 API 名** ✓ —— 只看文件名会漏掉整个 API ✗
```

## 🌉 桥的进度（连续版 Abel，2026-09-12 17:00 ✅）
```
| 步 | 内容 | 状态 |
| ① | **计数函数是合法 `StieltjesFunction`**（单调 + 右连续） | ✅ **已通过**（`PB-Stieltjes-bridge.lean`） |
| ② | 其 `measure` 在原子处取 1（`measure_singleton` = 跳跃 ✓） | ✅ **已通过** |
| ③ | **计数测度 = Dirac 测度** ⟹ `∫ g d(measure) = g γ` | ✅ **已通过** |
| ③′ | **有限多个零点**：`Σᵢ g(γᵢ) = ∫ g d(计数测度)` | ✅ **已通过**（`PB-Stieltjes-count.lean`） |
| ④a | **FTC 核心**：`Σᵢ f(uᵢ) = |s|·f(H) + Σᵢ ∫_H^{uᵢ} f'`（边界项 + 区间积分 ✓） | ✅ **已通过** |
| ④b | **Fubini/指示函数重排** | ✅ **已通过** |
【① 的细节 ✓】`stepAt γ := fun x => if γ ≤ x then 1 else 0` ✓
   · 单调性 ✓：按 `γ ≤ a` 分情形 ✓
   · **右连续性 ✓**：`x ≥ γ` 时右侧邻域常值 1 ✓；`x < γ` 时用**局部邻域**（`isOpen_Iio` ✓）常值 0 ✓
      ⚠️ 踩坑：我起初误以为「`x < γ` 时整个 `[x,∞)` 上都是 0」✗ —— **错** ✗（y 可以越过 γ ✓）
      ⟹ 必须用**局部**邻域 ✓（这正是右连续的定义 ✓）
【教训 ✓】`open scoped Topology` 才认 `𝓝` ✓；`Set.mem_Iio.mp` 才能把成员关系变成 `<` ✓
```

## 🎉 桥的关键突破（2026-09-12 17:10 ✅）
```
**①②③ 三步全部机器验证 ✓✓ —— 且【无需给 Mathlib 打补丁】✓（用 `StieltjesFunction.measure` ✓）**

| 步 | 内容 | 状态 |
| ① | 计数函数是合法 `StieltjesFunction`（单调 + 右连续） | ✅ |
| ② | `leftLim = 0` ⟹ `measure {γ} = 1`（**一个零点 = 一份质量** ✓） | ✅ |
| ③ | **`measure = Measure.dirac γ`** ⟹ **`∫ g d(measure) = g γ`** ✓✓ | ✅ |
| ③′ | **有限多个零点**：`Σᵢ g(γᵢ) = ∫ g d(计数测度)` | ✅ **已通过**（`PB-Stieltjes-count.lean`） |
| ④a | **FTC 核心**：`Σᵢ f(uᵢ) = |s|·f(H) + Σᵢ ∫_H^{uᵢ} f'`（边界项 + 区间积分 ✓） | ✅ **已通过** |
| ④b | **Fubini/指示函数重排** | ✅ **已通过** |

【③ 的实现 ✓】`Measure.ext_of_Ioc`（在 `Ioc` 上一致 ⟹ 测度相等 ✓）
   + `StieltjesFunction.measure_Ioc`（增量 ✓）+ `Measure.dirac_apply'`（Dirac 的作用 ✓）
   + 分情形：`γ ∈ (a,b]` ⟹ 两侧皆 1 ✓；`γ ≤ a` ⟹ 两侧皆 1 ⟹ 差 0 ✓；`b < γ` ⟹ 两侧皆 0 ⟹ 差 0 ✓
   ⟹ 测度相等 ✓ 再由 **`integral_dirac`** 得 `∫ g = g γ` ✓✓

【⭐ 意义 ✓】**"零点求和 ↔ 测度积分"这座桥已经搭成** ✓✓
   ⟹ 论文的 `S₄(H) = ∫_H^∞ t^{-4} d(2N(t))` 现在**有严格的形式化基础** ✓✓
   ⟹ 剩下的 ④ 只是**分部积分**（Fubini + FTC ✓ —— 库里有 ✓）

【今日踩坑（供后续 ✓）】
   · `StieltjesFunction` 的强制转换需 `@[simp]` 展开引理 ✓（否则 `if` 改写找不到目标 ✗）
   · `omega` **处理不了**带命题合取的否定 ✗ ⟹ 用 `by_cases` + `by_contra` ✓
   · `not_lt.mp`（不是 `le_of_not_lt` ✗）
```

## 🎉🎉 桥建成（2026-09-12 17:20 ✅✅）
```
**核心定理（机器验证 ✓）**：`Σᵢ g(γᵢ) = ∫ g d(计数测度)` ✓✓
   —— 即「**对零点求和 = 对计数测度积分**」✓✓
   —— **论文 `S₄(H) = ∫_H^∞ t⁻⁴ d(2N(t))` 的形式化基础已经成立** ✓✓

【实现链条（全部用库内工具 ✓ 无需打补丁 ✓）】
   ① `stepAt γ` 是合法 `StieltjesFunction` ✓（单调 + 右连续 ✓）
   ② `leftLim = 0` ⟹ `measure {γ} = 1` ✓
   ③ **`measure = Measure.dirac γ`** ✓（`Measure.ext_of_Ioc` ✓）
   ④ 计数函数 `countFn = Σᵢ stepAt(γᵢ)` ✓（`StieltjesFunction.add` ✓）
   ⑤ **`(countFn).measure = Σᵢ Dirac(γᵢ)`** ✓（`StieltjesFunction.measure_add` ✓ 归纳 ✓）
   ⑥ **`∫ g d(countFn.measure) = Σᵢ g(γᵢ)`** ✓✓（`integral_finsetSum_measure` ✓ + `integral_dirac` ✓）

【❗ 对「可行性问题」的最终回答 ✓】
   用户问："是否有可行的解决方案补齐 Mathlib" ✓
   ⟹ **答：不需要"补"✓ —— Mathlib【已有】所需的一切** ✓✓
      我此前断言"无 Stieltjes 支持"是**错的** ✗（只搜了小写文件名 ✓）
      **实际：`StieltjesFunction.measure` 就是计数测度的现成构造** ✓✓
```

## ⚠️→✅ 第 ④b 步失败的【根因】（2026-09-12 17:15 已定位并修复 ✅）

**结论：不是数学错误 ✓ —— 是「形式／约定」层面的两个陷阱** ✗

```
【根因 ①：指示函数的判据是「成员关系」而非「不等式」✗】
   `Set.indicator_apply (s) (f) (a) : s.indicator f a = if a ∈ s then f a else 0` ✓
   ⟹ 判据须写成 t ∈ Ioc H (u i) ✓；我写成 t ≤ u i ✗ ⟹ 模式匹配失败 ✗
   ⟹ 报错原文直接点出："Did not find an occurrence of the pattern `if t ≤ u i then …`" ✓
   ⟹ 修法：条件写成 if H < t ∧ t ≤ u i then 1 else 0 ✓
【根因 ②：rw/conv 与「库的定义展开」打架 ✗】
   · ∫ t in s, f t 在库中定义为 ∫ t, f t ∂(volume.restrict s) ✓
     —— 【并不是】定义等同的「指示函数积分」✗
     （实测：example : (∫ t in s, f t) = ∫ t, s.indicator f t := rfl  → 失败 ✗）
   · rw 会命中【所有】出现位置 ✗ ⟹ 会把不该动的地方也改写 ✗
     ⟹ 正确工具是 setIntegral_congr_fun（逐点／a.e. 意义 ✓）
   · noncomputable def 的展开须用 simp only [名] ✓（rw [名] 会失败 ✗）
   · 化简后残留 beta-redex（(fun t => …) t ✗）须 simp only [] ✓
   · 最后残留 f' t = f' t * 1 ✗ ⟹ 补 ring ✓
```

**★ 两条纪律（已入档 ✓）**
```
· 【不要假设"定义等同"】✓ —— 用 rfl 或 #check 实测 ✓
  这次正是靠「rfl 失败」才定位到根因 ② ✓✓
· 【报错信息要逐字读】✓ —— 上面那条 "pattern if t ≤ u i" 直接指出了根因 ① ✓
```

## 🎉 Lemma S4 零件【全部完成】（2026-09-12 17:15 ✅）

```
| 件 | 内容 | 状态 |
| 桥 ①②③③′ | 零点求和 = 对计数测度积分 | ✅ |
| ④a | 求和 = 边界项 + 各区间积分 | ✅ |
| ④b | 各区间积分 = 对「计数函数」的一次积分（Fubini 重排） | ✅ |
| 积分 | ∫_H^∞ t⁻⁴ ✓、∫_H^∞ t⁻⁴ log t ✓ | ✅ |
| 系数 | S4 系数代数 ✓ | ✅ |
⟹ Lemma S4 的数学内容【已全部机器验证】✓✓
   （含论文强调的「边界项必须保留」✓）
```
