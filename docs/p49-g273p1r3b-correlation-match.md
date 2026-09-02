# P49-G2.7.3-P1-R3b：机制确认——odd ground 逼近 V₀ 相关函数

> 2026-09-02 14:34 · C(logn) 采样比较 · 负定 vs 正定结构差异 · gap 来源定位

## P1-R3 判定（唐先生：PASS — Strong Numerical Refutation Candidate）
- 结论标签：Odd-Sector Prime Uniform Gap — Strong Numerical Refutation Candidate
- 保留：liminf g₋ = 0 strongly indicated, not yet proved
- **下一步最有价值：构造 odd extremizing sequence**（从 o16/o38 提取频谱结构——f_K 使 Q_prime(f_K) → q₀——若成功——P1 No-Go theorem）
- Riemann-Lebesgue 救援路线判定错误（试验函数随 N 变——固定 f 振荡衰减不能 uniform 化）
- 若 P1 No-Go：QW = W_{0,2} + W_∞ + Q_prime 联合谱问题（Q_prime 偏 even——W_{0,2} 偏 odd——full 极小 gap——联合 cancellation）

## 机制确认（C(logn) 采样比较）
odd ground 的 (f**f)(logn) vs V₀ 的 C₀(logn) = (L−logn)/L：
| n | C₀ | N=40 ground | 比 | N=100 ground | 比 |
|---|---|---|---|---|---|
| 2 | 0.685 | +0.584 | 0.85 | +0.569 | 0.83 |
| 3 | 0.500 | +0.407 | 0.81 | +0.403 | 0.81 |
| 4 | 0.369 | +0.375 | 1.02 | +0.353 | 0.96 |
| 5 | 0.268 | +0.273 | 1.02 | +0.306 | 1.14 |
| 7 | 0.114 | +0.147 | 1.28 | +0.205 | 1.79 |
| 8 | 0.054 | +0.134 | 2.50 | +0.112 | 2.09 |

- **Q_prime 重组验证 ✓**（−2.0225/−2.1097 精确一致——公式正确）
- **机制确认**：odd ground 逼近 V₀ 相关函数——**n=2,3（最大权重）欠匹配 15-19%——n≥4 匹配 ~1（n=7,8 超——但权重小）**

## 新洞察（gap 来源定位）
- **n=2,3 欠匹配 = g₋ 的主要来源**（Λ(2)n^{−1/2}, Λ(3)n^{−1/2} 最大——欠 15-19%——贡献 gap）
- **可能机制**：odd f 的 (f**f) **负定**（Fourier = F̂² = −|F̂|² ≤ 0——因 F̂ 纯虚奇——C_odd(0) = −‖F‖² = −1）——vs V₀ 的 C₀ **正定**（C₀(0) = +1）——**C_odd 从 −1 爬升——在 log2（小 y）达 +0.57 已接近 C₀(log2) = 0.68 但差 15%**
- **⚠️ 分叉**：若负定约束给"硬欠匹配"（n=2,3 永远差 ~15%）——**g₋ 停 > 0（Case A 复活——小正 gap）**——若可通过更高频消除欠匹配——g₋ → 0（Case B）——数值趋势（0.03 且降）提示后者——但未定

## 判定
- 机制确认（逼近 V₀ 相关函数——n=2,3 欠匹配——gap 来源定位）
- ⚠️ 负定 vs 正定结构差异可能给硬 gap（Case A）或可消除（Case B）——**未定——构造 extremizing sequence 的决定性实验**

## 下一步候选
- (a) 构造 extremizing sequence（分析欠匹配能否消除——n=2,3 的 C_odd(log2/3) 上限——moment/负定约束分析）
- (b) 更高 N 确认（g₋ 是否停 > 0 或趋 0）
- (c) 唐先生指示
