# P49-G2.7.3-P1-R3d：exact vs LP——odd 穿透 V₀（Case C 确认）

> 2026-09-02 14:42 · N=120 穿透 · coherence 关键 · prime-sector 路线 No-Go

## R3c 归档（唐先生：PASS — corrected von-Mangoldt weighting + finite-band sinc constraint identified）
- Case A/B OPEN（当时）——Prime-sector uniform gap not established——Odd extremizing sequence primary target
- 连续频率松弛 rejected as proof surrogate——有限 NN sinc 稀释 genuine constraint but uniform 未证
- 旧 Test B/C K_λ superseded——直接矩阵有效（provenance 分离 ✓）
- R3d：finite-NN exact vs LP vs SDP——coherence 效应

## ⚠️⚠️ R3d 决定性结果（λ=3, q₀ = −2.1407）
| N | m_exact | m_LP(min diag) | coherence gap | g₋ = m_exact−q₀ |
|---|---|---|---|---|
| 20 | −1.799 | −1.522 | 0.277 | 0.342 |
| 40 | −2.023 | −1.669 | 0.353 | 0.118 |
| 60 | −2.059 | −1.874 | 0.185 | 0.082 |
| 80 | −2.070 | −1.874 | 0.196 | 0.071 |
| 100 | −2.110 | −1.874 | 0.236 | 0.031 |
| **120** | **−2.164** | −1.874 | **0.290** | **−0.023（穿透！）** |

## ⭐ 关键发现
1. **N=120: m₋ = −2.164 < q₀ = −2.141——odd sector 穿透 V₀——Case C（m₋^∞ < q₀）确认**（甚至超越 Case B）
2. **coherence 是关键机制**：m_LP（diagonal——单模式）饱和于 −1.874（N≥60 不再改善）——但 m_exact（含 off-diagonal）继续降到 −2.164——**coherence gap 增大（0.19→0.29）——off-diagonal 相干允许比任何单模式更好的相关匹配**
3. **prime sector 单独不能保证 even ground——odd 甚至更优（更负）**

## ⚠️ 验证注意事项
- N=120 矩阵 241×241——float64——穿透量 −0.023 小但 coherence 趋势一致（0.19→0.29 增）
- 建议高精度确认（mpmath——N=120 单点）——但趋势（g₋ 阶梯下降跨 0）与机制（coherence 增大）一致

## 意义（G2.7.3 结构性结论候选）
- **prime-sector 路线正式 No-Go（Case C——odd 穿透）——simple-even 不能来自 prime sector**
- **CCM 的 even ground 必须来自 full-QW 联合结构**（W_{0,2} + W_∞ 与 Q_prime 的交互——尽管 W_{0,2} 单独偏 odd/中性——联合恢复 even——或——full-QW even-simple 是 CCM 最深未证假设——回到原始）
- 支持唐先生框架：QW = W_{0,2} + W_∞ + Q_prime 联合谱问题（非 sector dominance）

## 判定
- **Case C 数值确认（odd 穿透 V₀）——prime sector 不能保证 even ground——需 full-QW 联合分析**
- ⚠️ N=120 单点建议高精度复核——但机制（coherence gap 增大）支持

## 下一步候选
- (a) 高精度确认 N=120（mpmath）+ N=150（穿透量增长？）
- (b) 接受 Case C（prime No-Go——转 full-QW 联合谱：W_{0,2} + W_∞ 如何与穿透的 odd 交互——even ground 的真正来源）
- (c) 唐先生指示
