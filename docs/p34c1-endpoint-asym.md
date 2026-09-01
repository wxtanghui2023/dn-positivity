# P34-C' C1 升级：a_k(X) 端点主导渐近确认 + w=e^-x/2 form convergence 起步

> 2026-09-01 · 唐先生 C1 升级指令 · a_k(X)=X^{ik}/(1+ik)+o(1) · form convergence 主攻

## ① a_k(X) vs 端点主导公式（确认——可证明障碍）
**A_k(X) = X^{ik}/(1+ik) + o(1)——a_k(X) = (cos(k log X)+k sin(k log X))/(1+k²) + o(1)**
| k | X=5000 差 | X=20000 差 | X=100000 差 | X=500000 差 |
|---|---|---|---|---|
| 1 | 0.036 | 0.059 | −0.020 | −0.040 |
| 2 | 0.045 | −0.046 | 0.038 | −0.032 |
| 3 | −0.033 | 0.031 | 0.015 | −0.020 |

- **端点主导公式数值确认（差 ~0.02-0.06——o(1) 趋势）——固定 k 无普通 X→∞ 极限——可证明障碍**
- |a_k(X)| = O(1/k) 但不趋零（振荡——振幅尺度 1/k）

## ② a_1(X) 沿 X 振荡（无极限）
X=1000→10⁶：0.62 → 0.58 → 0.12 → −0.32 → −0.62 → −0.56 → −0.21 → 0.25 → 0.65 → 0.62
- **大振幅振荡——无普通极限——endpoint oscillation 强制——"w=1 naive 无 canonical cutoff limit"严格化支持**

## ③ w=e^-x/2——q_X[f] Cauchy 性（r=1——纯 cutoff——K=60）
- **(e2+e3)/√2：q = 0.18 → −0.27 → −0.38 → 0.19——差 0.45/0.10/0.57——不 Cauchy（漂移回正）**
- **(e2+e100)/√2：q = 0.04 → −0.10 → −0.13 → −0.12——差 0.14/0.03/0.01——倾向 Cauchy（慢）**
- ⚠️ r=1 时 Σ|a_k| ~ log 发散风险——q 收敛依赖测试向量（大素数对——w 衰减压振荡？——小素数对——漂移）——未定

## ⭐ 三分叉状态（唐先生表）
| 分支 | canonical limit | uniform sector | 当前状态 |
|---|---|---|---|
| w=1 naive | 否（endpoint oscillation） | 无法定义 | **可由 a_k(X) 渐近严格化（① ② 确认）** |
| w=e^-x/2 | 候选存在 | 数值显示 moving-edge | **最值得做 form convergence（③ 未完成）** |
| renormalized w=1 | 未知 | 未知 | 必须重新审计（Gate 2'） |

## ⚠️ 诚实边界
- ① 的差（0.02-0.06）——o(1) 趋势——但——需更严格（高阶项——PNT 误差）
- ③ 的 r=1（无 Abel——Σ|a_k|~log 发散风险）——form convergence 需系统做（dense core——Cauchy——semibounded——closable——Kato/Mosco）
- "w=1 naive 无 canonical limit"——只对含非零低阶 Mellin/Fourier mode 的测试类（未消除 endpoint modes）——renormalization/振荡扣除/不同 test space 仍可能给 canonical object（但需重新 Gate 2'）

## 下一步（w=e^-x/2 主攻）
- (a) form convergence 系统六步：dense core → q_X[f] Cauchy → semibounded → closable → Kato/Mosco → dim E((−∞,−ε))
- (b) r<1（Abel）下先做（避免 Σ|a_k| 发散）——再 r↑1
- (c) 唐先生指示
