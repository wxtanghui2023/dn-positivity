# Arithmetic Frobenius Flow——最终过滤器（2026-09-09 16:53 定稿——）

## Prime Power Orbit Test 最终逻辑链
Euler 因子 p^n：代数展开 vs 动力 Euler 积（轨道绕行——）
——p^n：代数幂 → 轨道绕行（比"存在周期轨"更强——）
三类已知缺口：Frob（迭代✓ 缺范数/长度与次数耦合——）
Selberg（轨道✓ 长度 = log(基本单位) ≠ log p——）
BC（n log p✓ 无轨道——）

## Power Compatibility（本轮新增硬约束——）
P：φ_{n log p} = (φ_{log p})^n——γ_p^n ↔ p^n
——很多"像算术动力"的对象在此失败——

## 最终过滤器（Q1-Q6——）
Q1: p ↔ γ_p（Prime Orbit——）
Q2: T(γ_p) = log p
Q3: h_top = 1（PNT——）
Q4: γ_p^n ↔ p^n（Power Compatibility——本轮新增——）
Q5: F_p 内生产生（非定义——）
Q6: ∞ 位提供对偶/函数方程（Archimedean——）

## 定位（严格——）
"连续 Frobenius flow" = 【最小满足条件的候选结构】（非结论——）
缺失对象不是 HP 算子——是 Arithmetic Frobenius Flow：
  γ_p ↔ p——T_p = log p——γ_p^n ↔ p^n——h = 1——F_p 内生——
真正新增点：log p 的长度来源 + p^n 的绕行来源（两个独立硬约束——）
——必须由同一个算术动力对象同时产生——

## 17:00 严格版（唐先生定稿——）
A = (X_Q, φ_t, F_p, Θ)——必须同时满足：
Q1 p ↔ γ_p（闭点 = 动力对象非标签）
Q2 T(γ_p) = log p（内部产生——非外部赋值）
Q3 h_top = 1（PNT 全局统计）
Q4 γ_p^n ↔ p^n（φ_{n log p} = (φ_{log p})^n——Power compatibility——）
Q5 F_p 属于 End(X_Q) 或其增强（非选定表示/人工/ζ 重写）
Q6 Θ* = 1−Θ（函数方程 = 内部对偶——含 ∞ 位补全）

## 本轮新增（核心缺口分裂——）
缺口 A：Length generation（p → log p——范数→周期——）
缺口 B：Power generation（p^n → γ_p^n——代数幂→动力绕行——）
——不能分别解决（只有 A = 有频率无轨道——只有 B = Selberg 型长度错——）

## 三个不可约条件
Arithmetic Length（T_p = log p）*
Arithmetic Iteration（γ_p^n = p^n）*
Arithmetic Duality（Θ* = 1−Θ）
——分别解决：Euler 因子时间来源/幂展开动力来源/RH 对称性——

## 关键贡献（Power Compatibility——）
任何真正的算术动力化不仅须解释素数作为周期——
——还须解释 Euler 因子的幂指数作为轨道迭代——
——未来候选若只能产生 log p 不能产生 p^n ↔ γ_p^n：
  【直接判为形式 Euler 化（非真正动力化——）】


> ⚠️ **勘误（T10 ✓ 2026-09-14，小灵）**：本档把 **Q4（$\gamma_p^n\leftrightarrow p^n$ 幂相容 ✓）** 列为**独立硬约束** ✗。经 `docs/E141-Q4-independence-audit.md` 终审 ✓：**在半群作用（流）成立的前提下 ✓，Q4 是【重言式 ✗】** —— 由 $\varphi_{t+s}=\varphi_t\varphi_s$ 与长度加法同态两步恒等即得 ✓，无独立自由度 ✓。本档所称"多数候选在 Q4 失败 ✗"**实为在 Q1/Q2（长度来源 ✗）与 Q5（$F_p$ 内生成 ✗）失败** ✓（与本档同行的"分裂说明"一致 ✓）。⟹ **规格应读作 $Q1,Q2,Q3,Q5,Q6$ 五项 ✓（Q4 冗余 ✓）**。原文本**保留不删** ✓（T10 ✓）。


> ⚠️ **勘误 2（T10 ✓ 2026-09-14，小灵）**：**Q3 写作 "$h_{\rm top}=1$"【未分离下界与上界】** ✗。经 `docs/E142-Q3-definitional-audit.md` ✓：**下界 $h_{\rm top}\ge1$ 自动** ✓（由 $Q1+Q2+$PNT ✓：$\pi(e^T)\sim e^T/T$ ✓）；**只有【上界 $h_{\rm top}\le1$】才有独立内容** ✗。且记号 $h_{\rm top}$ 在档内**未显式定义** ✗（仅附理由"PNT" ✓）。**建议读法 ✓**：若取"素数标记子系统指数率"（✓ 与"PNT"理由一致 ✓）或取 Bowen 良性假设 ✓ ⟹ **Q3 删除 ✓，规格缩为 $Q1,Q2,Q5,Q6$ 四项 ✓**；否则应改写为"$h_{\rm top}\le1$ 上界约束" ✓。原文**保留不删** ✓（T10 ✓）。
