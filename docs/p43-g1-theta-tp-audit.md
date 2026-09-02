# P43-G1：Theta Kernel Total-Positivity Audit——第一轮

> 2026-09-02 11:48 · 唐先生 P43 指示 · TP Gate · TP₂/TP₃ 失败

## 框架（唐先生）
- **P42 封存**：RH ⟺ supp(div G) ⊂ (−∞,0) ⟺ G'/G negative-Herglotz（Hadamard/growth）——不在 Im(ζ'/ζ) 硬攻（另一种 analytic encoding）
- **P43**：Ξ(t) = ∫Φ(x)cos(tx)dx——**theta kernel 是否 TP∞ ⟹ Fourier 变换 ∈ Laguerre–Pólya 类？**——TP 约束"符号变化复杂度"——可能绕开 β-wall
- **危险**：Φ > 0 ≠ Φ ∈ TP∞——**P43-G1 严格 Gate**：G1.1（Φ>0）——G1.2（TP₂）——G1.3（TP₃）——**TP₂ 失败 = 立即换范式**

## ① Φ 构造（Mellin 核——验证）
- **Φ(x) = Σ(2π²n⁴x² − 3πn²x)e^{−πn²x}——g = θ−1——Φ = 2x²g'' + 3xg'——Mellin：∫Φ x^{s/2−1}dx = ξ(s) ✓（解析验证）**
- 注意：Mellin 核（x>0）——cos 变换核是换元版本——TP 可能不同

## ② G1.1——Φ(x) > 0？
- **x=0.01：Φ = −2.00（负！）——x=0.10：Φ ≈ −0.000000（临界）——x ≥ 0.3：正**
- **⚠️ G1.1 在 x 小处失败（Φ 负——Mellin 核）**——但——x 小处的"精确值"依赖抵消（n 截断）——需谨慎

## ③ G1.2——TP₂（差核偶延拓）
- **20000 随机——min det = −0.1997——负 det 数 = 8030——TP₂ 失败！**

## ④ G1.3——TP₃
- **8000 随机——min det = −0.086——负 det 数 = 4070——TP₃ 失败！**

## ⭐ 判定——普通 theta kernel 非 TP（唐先生预设确认）
- **TP₂ 失败（40% 负 det）——TP₃ 失败（51% 负 det）——普通 theta kernel（Mellin 核——差核偶延拓）不是 total positive——TP₂ 失败 = 立即换范式（唐先生的规则）**
- **"普通 theta-kernel total positivity 不是 RH 的新引擎"——确认（唐先生的失败也有价值预设）**

## ⚠️ 诚实
- Φ 用 Mellin 核（x>0——ξ Mellin 验证 ✓）——"cos 变换核"（换元）TP 可能不同——未测
- 差核用偶延拓（一种 TP 测试）——加法核（Φ(x+y)）/Mellin 域核——未测
- 测试点有限扫描（0.3-5.0）——非穷尽——但——负 det 比例高（40-51%）——不是边界情形
- x 小处 Φ 的符号（G1.1）依赖抵消（n 截断）——需更精确（mpmath 高精度）确认

## 下一步候选
- (a) **立即换范式（TP₂ 失败——唐先生规则）**——或——modified kernel e^{ax²}Φ(x)（热流——de Bruijn-Newman 型——最小 TP-threshold 是否恰好 0？）
- (b) "加法核 Φ(x+y)"或"cos 变换核"的 TP——补充测试（确认不是"差核偶延拓"的假象）
- (c) 唐先生指示
