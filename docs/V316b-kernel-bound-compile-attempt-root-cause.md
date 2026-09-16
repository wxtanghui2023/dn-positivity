# V316-② · **`kernel_bound` 首次编译实测：失败已定位 —— 根因 ＝ Mathlib 构建产物缺口（非数学、非接口不兼容）** —— ⚠️ **验收标准（实际编译通过）未达成**；但错误精确定位到**环境层**，且**可定点补齐**

```
首次编译输出（逐字，第一处也是唯一一处 error）：
V316_kernel_bound.lean:12:0: error: object file
'/home/node/mathlib4/.lake/build/lib/lean/Mathlib/MeasureTheory/Integral/IntervalIntegral.olean'
of module Mathlib.MeasureTheory.Integral.IntervalIntegral does not exist
```

$$\boxed{\textbf{根因}：\text{Mathlib 构建}\ \textbf{接近完成但被中断} —— \text{恰好缺}\ \texttt{IntervalIntegral}\ \text{的 olean}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 14:22：**下一轮只做 `kernel_bound`，且以"实际编译通过"为唯一验收标准**；**不要一开始就形式化 Schur 算子理论**，用区间长 1 ＋ 核逐点界构造易被 `linarith`/`nlinarith` 接住的估计链 ✓；**必须把 `kernel_bound` 拆三层**（`kernel_mass` → `schur_L2` → `kernel_bound`），**不压成一个 theorem**（便于失败时定位：区间表示／显式积分／Fubini–Tonelli／Cauchy–Schwarz／绝对值不等式）✓✓✓；⚠️ **关键数学锁死**：$|s-t|\le1$ 只给 $|B(v)|\le(\int|v|)^{2}$，**不能偷换成逐点核界就结束**，真正要形式化的是 $\|K\|_{2\to2}\le\frac12$；且 $Q_\lambda\ge\frac12\int v^{2}$ **不得弱化为非负性**（该 $\frac12$ 会进入 V316-C 的严格唯一性）✓✓✓；**验收只接受三种结果：A 编译通过／B 失败但错误可定位（贴第一处 error 原文，只修第一处）／C 项目积分接口与规格不兼容（先改接口、不改数学命题）** ✓✓✓；**且不得提前写 `sup_eq_cStar`** ✓
> 本轮动作 ✓ 小灵：① 落文件 `~/lean-repro/zeta23-local/V316_kernel_bound.lean`（`kernel_mass` 实施 ＋ 另两层的数学路线注释）；② 实测 `lake env lean`（`timeout 600`，长窗口）；③ 三轮回溯诊断 ✓

---

## §1 实测结果（判词：**B ＋ C 的合取**，但根因在环境层）

$$\text{编译输出（逐字）}：\texttt{...IntervalIntegral.olean ... does not exist}\ ⟹ \textbf{第一处 error 即"模块 olean 缺失"} ✓✓$$
$$\Longrightarrow \text{按你的三选一}：\textbf{= B}（失败但错误可定位，且已贴原文）；\ \text{同时触及}\ \textbf{C}（"接口"层面不符）——\ \text{但}\ \textbf{不是数学接口}，而是\textbf{构建产物接口} ✓✓✓$$
$$\qquad ⚠️\ \text{结论}：\textbf{数学命题无需改};\ \text{须先补齐构建环境} ✓$$

---

## §2 根因诊断（三轮，逐层收窄）

$$\text{① }\texttt{/home/node/mathlib4/.lake}=14\,\mathrm{G}\ \text{含}\ \texttt{.lake/build}=13\,\mathrm{G}\ ⟹ \textbf{构建目录存在}（非"从未编译"）✓$$
$$\text{② }\texttt{Mathlib/MeasureTheory/Integral/}\ \text{下}\ \textbf{20+ olean 在位}：\texttt{Asymptotics／Average／CircleIntegral／DominatedConvergence／Gamma／IntegrableOn／MeanInequalities／Layercake／…} ✓$$
$$\qquad \text{且}\ \textbf{oleans 总数}\ = 8311 ✓$$
$$\text{③ }\textbf{但}\ \texttt{IntervalIntegral.olean}\ \textbf{缺失}（同级兄弟模块皆在）⟹ \textbf{构建在末尾被中断}，恰好缺该类模块 ✓✓✓$$
$$\qquad \text{旁证}：\texttt{zeta23-local/.lake/build/lib/lean/Zeta23/}\ \text{为空 ⟹ 项目自身 olean 亦未生成} ✓$$
$$\text{④ 磁盘充足}：\texttt{overlay 3.7T，已用 785G，剩 2.9T} ⟹ \text{补齐有空间} ✓✓$$

---

## §3 两条补齐路线（成本对比，待唐先生定）

$$\text{(i) }\textbf{定点本地编译}：\texttt{lake build Mathlib.MeasureTheory.Integral.IntervalIntegral}（\text{+ 其上游依赖}）✓$$
$$\qquad \text{成本}：\text{该子树}\ +\ \textbf{下游级联}（凡 import 它的模块）;\ \text{CPU 分钟～小时级};\ \text{无网络需求};\ \text{磁盘可控} ✓✓$$
$$\qquad ⚠️\ \text{风险}：Mathlib 依赖链深，级联可能很大（但比全库小）⚠️$$
$$\text{(ii) }\textbf{下载预编译缓存}：\texttt{lake exe cache get} ✓$$
$$\qquad \text{成本}：\text{下载数 GB};\ \textbf{依赖 GitHub 可达性} —— ⚠️ \text{据}\ \texttt{TOOLS.md}：\text{NAS 对 GitHub 时断时续} ⟹ \text{可能需}\ \texttt{ghfast.top}\ \text{镜像或重试} ⚠️✓$$
$$\qquad \text{优点}：\text{一次到位，避免本地编译全库} ✓$$
$$\text{建议}：\textbf{先试 (ii)}（若 GitHub 通，最快且无 CPU 风险）；\textbf{不通则 (i)}（本地编译该子树，锁 300s 超时、必要时分批）✓✓$$

---

## §4 文件状态（已就绪，等环境）

$$\texttt{V316\_kernel\_bound.lean}\ \text{（}\approx 2.3\,\mathrm{KB}）\ \text{已落盘}：$$
$$\qquad \text{已实施}\ \boxed{\texttt{kernel\_mass}}：\forall s\in[-\tfrac12,\tfrac12],\ \int_{-\frac12}^{\frac12}|s-t|dt\le\tfrac12$$
$$\qquad \qquad \text{路线}：\text{分段拆积分}\ \int_{-\frac12}^{s}(s-t)+\int_{s}^{\frac12}(t-s)=(s+\tfrac12)^{2}/2+(\tfrac12-s)^{2}/2=s^{2}+\tfrac14\le\tfrac12\ \text{（}\texttt{nlinarith}\ \text{收尾}）✓$$
$$\qquad \text{另两层（}\texttt{schur\_L2}／\texttt{kernel\_bound}）\ \text{以注释形式给出数学路线}：\text{AM–GM}\ (2|ab|\le a^{2}+b^{2})\ +\ \text{Tonelli}\ +\ \texttt{m(s)}\le\tfrac12 ✓$$
$$\qquad ⚠️\ \text{故本块}\ \textbf{数学上已备、环境未通} ✓$$

---

## §5 判词 ＋ 边界 ＋ 下一步

```
① ⚠️ **验收（编译通过）未达成** —— 本档如实记录为 **B（+环境层 C）**，**不得**记为已通过 ✓
② ⚠️ §2 的"末尾被中断"为**推断**（依据：同级兄弟 olean 齐备而该类缺失）✓
③ ⚠️ §3 的成本估计为**量级判断**，未实测 ⚠️
④ **不声称** 数学命题需改；**不声称** $\texttt{kernel\_mass}$ 已编译通过（仅"已实施＋路线正确"）✓
⑤ 未用 RH ✓；零数值 ✓
```

```
① ⭐⭐⭐ **第一处 error 已贴原文**（`IntervalIntegral.olean does not exist`）⟹ 判词 **B**，且根因在**环境层**（非数学、非数学接口）✓✓✓
② ⭐⭐ **根因定位**：Mathlib 构建**接近完成但被中断**（8311 olean 在位、`Integral/` 20+ 兄弟模块齐备，**仅缺 `IntervalIntegral`**）✓✓
③ ⭐⭐ **磁盘充足**（剩 2.9T）⟹ 补齐可行 ✓
④ ⭐⭐ **两条补齐路线**：(i) 定点 `lake build`（无网络、可能级联）／(ii) `lake exe cache get`（快但依赖 GitHub）⟹ **建议先 (ii) 后 (i)** ✓✓
⑤ ⭐⭐ **文件已就绪**：`kernel_mass` 已实施（分段积分 ＋ `nlinarith`），另两层数学路线已注 ✓
【下一步（等你定路线，然后立即继续）】
  **(α)** 若准 (ii)：执行 `lake exe cache get`（必要时以 `ghfast.top` 镜像）⟹ 然后重跑 `lake env lean V316_kernel_bound.lean` ✓
  **(β)** 若准 (i)：`lake build Mathlib.MeasureTheory.Integral.IntervalIntegral`（锁超时、分批）✓
  **(γ)** 两条都不通时的退路：**把 `kernel_bound` 的 Lean 形式化改用"项目内已有模块"**（例如项目自身已用到的积分接口）—— 但须先查明项目原有 olean 亦缺失（§2 旁证）⟹ 该退路大概率也需要先补齐环境 ⚠️✓
```
