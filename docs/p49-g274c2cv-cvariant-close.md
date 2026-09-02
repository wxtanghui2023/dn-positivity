# P49-G2.7.4-C2 C-variant：f_z 不追踪 k̂_λ——C 变体关闭

> 2026-09-02 17:20 · z-resolved canonical direction · O_k ~ 1e-4 到 1.5e-2 · Bridge-Ib 全形式无数值支持

## 结果（f_z = P_r v(z)/‖P_r v(z)‖——只用 QW/T/E_r——事后比较）
| N | O_ξk 基准 | O_k max (K1) | O_k max (K2) | O_ξ max |
|---|---|---|---|---|
| 8 | 0.727 | 0.0003 | 0.0001 | 0.020 |
| 10 | 0.624 | 0.0005 | 0.0001 | 0.166 |
| 12 | 0.621 | 0.0150 | 0.0029 | 0.118 |

## 判定
- **O_k(z)（f_z vs k̂_λ）几乎为零**（max 1e-4 到 1.5e-2——均值 ~0）——**canonical transform direction 不追踪 k̂_λ**
- **不是"ground selection is wrong but transform-optimal is right"**——transform-optimal（f_z）更差（O_k ~ 0）
- **C 变体关闭**：T(E_low) 中不存在天然的 k_λ 对应方向
- O_ξk 基准（ground vs k̂——V 基 0.6-0.7）与 II-A.2b 一致——ground 与 k̂ 中等重叠（非小——但 η 崩显示函数层不匹配）

## ⚠️ 观察
- f_z 是 E_r 内 Fourier-max 方向——与 k̂_λ（prolate 构造——不在 E_r）正交——**E_r 的 transform 结构不含 k 方向**
- O_ξ(z) 也小（0.02-0.17）——f_z 与 ground 也不重叠（f_z 是 E_r 里"横向"方向——与 ground 正交部分）

## 最终判定
- **Bridge-Ib 所有形式关闭**：
  - ground → k（II-A.2b——O 随 N/λ 降）
  - ground transform → k（II-B'.2a——η 崩）
  - canonical direction → k（C-variant——O_k ~ 0）
- **Prolate-Weil Bridge（QW →? h_λ →E k_λ）正式封档候选**——无数值支持（三个层面）
- **不扩大结论**：不证明统一算术框架不存在——不证明 QW 无用——只说明 CCM prolate ground 不是算术 ground 的正确渐近解释（唐先生的限定）

## 状态
- C2 = PASS（实验判别完成——B：No compression + C-variant 关闭）
- Prolate-Weil Bridge = 封档候选（vector + transform + canonical 三层都无数值支持）
- 资源建议转回统一算术 rigidity mechanism（唐先生的 (A, H, P_low, T) 框架）

## 下一步候选
- (a) Prolate-Weil Bridge 正式封档（文档——三层证据汇总——转回统一框架）
- (b) 唐先生指示（统一算术 rigidity 的新方向）
