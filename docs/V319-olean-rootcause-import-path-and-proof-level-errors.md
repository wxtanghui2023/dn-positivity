# V319 · **olean 悬案结案：根因 ＝ import 路径（非构建缺失）⟹ 无需上传；错误已降至证明层**（唐先生 14:36 问"需要的话我可以下载了上传"）

## 结论先行：**不需要上传**

$$\text{唐先生问}：\text{"如果需要，我可以下载了上传 openclaw"} ⟹ \boxed{\textbf{不需要}} ✓✓✓$$
$$\qquad \text{理由（本档实测）}：\textbf{Mathlib 已完整构建} —— \text{源文件}\ 8311\ \text{个}，\ \text{olean}\ 8311\ \text{个，}\textbf{完全匹配} ✓✓✓$$

## 根因（三轮诊断的最终落点）

$$\text{① 首次编译报错}：\texttt{object file .../Mathlib/MeasureTheory/Integral/IntervalIntegral.olean does not exist} ✓$$
$$\text{② 目录核查}：\texttt{Integral/IntervalIntegral}\ \textbf{是目录}（\text{非 } .lean \text{ 文件}），\text{内含}\ 12\ \text{子模块}：$$
$$\qquad \texttt{Basic.lean／FundThmCalculus.lean／DerivIntegrable.lean／Periodic.lean／IntegrationByParts.lean／TrapezoidalRule.lean／…} ✓✓$$
$$\text{③ 关键引理定位}：\texttt{grep -l "integral\_add\_adjacent\_intervals\|intervalIntegrable\_const"} ⟹ \textbf{命中}\ \texttt{IntervalIntegral/Basic.lean} ✓✓✓$$
$$\Longrightarrow \boxed{\text{正确 import}\ ＝\ \texttt{Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic}} ✓✓✓$$
$$\qquad \text{（即：Mathlib 该版本把}\ \texttt{IntervalIntegral}\ \textbf{拆分为目录};\ \text{我用了过时路径）} ✓$$

## 修复效果：错误层级下降（环境层 → 证明层）

$$\text{改 import 后（同时按指令 1 删去}\ \texttt{Pow.Real}\ \text{，import 由 3 降至 2）：}$$
$$\qquad \text{保留}\ \texttt{IntervalIntegral.Basic}\ ＋\ \texttt{Bochner.Basic}\ ⟹ \textbf{环境层错误消失} ✓✓✓$$
$$\qquad \text{现余}\ 4\ \text{处}\ \textbf{证明层错误}（判据 B）：$$
```
37:13  typeclass instance problem is stuck — NormedSpace ℝ ?m.168
41:6   Type mismatch: integral_congr … has type (∫…=∫…) but is expected to have type IntervalIntegrable …
35:74  unsolved goals — case hbc ⊢ IntervalIntegrable (fun t => s - t + ∫ t in s..1/2, t - s) volume ?m.162 s
49:8   Ambiguous term: integral_neg ⇒ 需写 intervalIntegral.integral_neg
```
$$\Longrightarrow \text{即：}\ \texttt{hsplit}\ \text{的}\ \textbf{分段策略用法不对}（\texttt{integral\_add\_adjacent\_intervals}\ \text{需先给可积性}）;
\ \text{且}\ \texttt{integral\_neg／integral\_sub}\ \text{在}\ \texttt{intervalIntegral}\ \text{命名空间下被歧义} ✓✓$$

## 判据对照（唐先生三选一）

$$\boxed{\textbf{B}}：\text{失败但错误可定位}（\text{已贴第一处与其余三处原文}）;\qquad \textbf{C 已被采用并完成}：\text{改接口、不改数学命题（只改 import 路径）} ✓✓$$
$$\qquad ⚠️\ \textbf{环境层障碍已消除};\ \text{剩余纯为 Lean 证明细节，}\textbf{无需任何下载/上传} ✓✓✓$$

## 下一步（纯本地迭代，零下载）

```
① hsplit 重写：先证两段的可积性（intervalIntegrable_iff.mpr / IntegrableOn 提供），
   再用 intervalIntegral.integral_add_adjacent_intervals 的**正确参数形态**；
② 显式限定命名空间：**intervalIntegral.integral_neg** / intervalIntegral.integral_sub / integral_const / integral_id；
③ 每段算完用 ring/nlinarith；末步 s² + 1/4 ≤ 1/2 用 hs' : |s| ≤ 1/2 与 sq_abs；
④ 仍按唐先生纪律：**逐块编译、只修第一处、不提前写 sup_eq_cStar**。
```
