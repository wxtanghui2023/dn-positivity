# §7 Projection/Trace——C1-C3 审计（第一轮——）

> 2026-09-07 22:40 · 唐先生主攻 (c)——C1-C3 死亡审计

## C1：表示独立性（W_∞ = projection trace ≡ Weil form？）
- 公式 (19) W_∞(f) = log(TW)f(1) + Trace(ϑ(f)/(1−P_T−P̂_W))——Archimedean
- 公式 (22) −Σ_{v∈S}W_v(f) = log(TW)f(1) + Trace(ϑ(f)/(1−P^S_T−P̂^S_W))——semilocal（含素数——）
- **这是 Connes 1998 trace formula（[17]——）——已证明的等式**
- 判定：**⚠️ 形式等价**——(22) ≡ Weil 二次型（等式——）——但需问：投影代数是否给 Weil 外的新信息

## C2：Arithmetic injection（Λ(n) 是否在投影内部——）
- §7 的素数进入：通过 P^S_T, P̂^S_W 的 **module 定义**（semilocal——）——非早期 QW_λ 的显式 −ΣΛ(n)T(n) 项
- **但**——module 的素数参数（S——）与零点位置 β 的关系——需经 Weil 求和（显式公式——）
- 判定：**⚠️ 半通过**——素数在投影"内部"（module——）——但到 β 的桥仍是显式公式（循环风险——）

## C3：β visibility（数值——关键——）
- **Landau-Pollak 谱 μ_n(c) 纯 TW**：c=5: 1 个 >0.5——c=10: 2 个——c=15: 3 个（2TW 规律 ✓）
- μ_n 无素数/零点参数——**对假设离轴零点 δ 的响应 = 0**
- semilocal 版（P^S——）：素数在 module——但 module 参数 ≠ 零点参数——到 β 需循环
- 判定：**❌ 普通 concentration 谱 β-盲**——semilocal 需循环插入

## 额外强论据（自检发现——）
**§7.4 的 semilocal trace formula 功能定位 = 支持 6.6②**：
- Connes 原文："A step towards a conceptual justification of this numerical fact"（6.6② 的 k_λ≈θ_x——）
- 而 6.6② = P49 II-A——已三层否证——
- **§7.4 trace formula 服务于已否证的桥——失去目标**
- 它不独立产生 β 机制——是"如果 6.6② 成立的概念理由"——但 6.6② 不成立

## C1-C3 综合判定
**§7 的 projection/trace 结构 = Weil 的等价表示（1998——）**：
- 公式等价（C1——）——concentration 谱纯 TW（C3 数值——β-盲——）
- 素数在 module（C2——）——但到 β 的桥 = 显式公式（循环——）
- **投影代数没有提供 Weil 外的独立 β 机制**——§7 = 表示变换（把 Weil 用投影迹写——）

## 结论（倾向——）
**§7 projection/trace = C1-C3 审计失败（初步——）**：
- 不是"新机制"——是 Weil form 的投影迹等价表示
- concentration 谱（C_{T,W}——）纯 TW——β-盲
- 无独立 time-frequency arithmetic invariant 产生 β 约束

## 与 6.6② 的关系
- 6.6②（k_λ≈θ_x——）= P49 II-A（已否证——）
- §7（projection trace——）= Weil 等价表示（C1-C3 失败——）
- Connes 2026 的两个"新结构"都被审计排除（或已否证——）

## 文件
- scripts/s7_c3_concentration.py——C3 数值
