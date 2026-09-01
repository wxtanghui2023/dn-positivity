# Theorem-Status Audit——五种状态彻底分开

> 2026-09-01 · 唐先生定稿指令 · 论文可信度的重要组成部分

## 五种状态定义
- **THEOREM**：严格证明的无条件命题（完整证明）
- **PROPOSITION**：有证明框架但依赖特定假设/待完成细节
- **NUMERICAL OBSERVATION**：数值验证（非证明）
- **CONJECTURE**：有数值/直觉支持但未证明
- **FAILED ROUTE**：审计后确认不提供 exclusion 的路线

## 完整清单

### THEOREM（严格证明）
| 编号 | 内容 | 证明要点 |
|------|------|------|
| T1 | ∫f_n·S·g = O(1)（定理 A） | Titchmarsh 截断 + van der Corput + stationary + R |
| T2 | Σf_n(γ_k) = ½nlogn + cn + O(1)（定理 B） | 任意零点配置 |
| T3 | mean(S(γ_k)) = ½ | 精确恒等式 |
| T4 | P_γ(δ) = δ²M₂/(2U²D₊D₋) ≥ 0（成对正性闭式） | 代数——轨道配对 |
| T5 | D = ΣP_γ ≥ 0 | T4 逐轨道 |
| T6 | 变分定理（在线虚部唯一最小化 S_proj） | Weil + 逐项代数 |
| T7 | 逻辑强度：C2 ⟺ RH（L² 版本——RH ⟹ C2 严格；C2 ⟹ RH 受阻于 coercivity） | 引理 1-4 + Lemma 3 审计 |
| T8 | 相位锁定 S(p) = O(1) | Guinand/Weil |
| T9 | GRH 判据（成对正性迁移——universal） | P_γ 不依赖 q/χ |
| T10 | Gram 正定 K_T ⪰ 0（无条件） | Hilbert 空间几何事实 |

### PROPOSITION（证明框架——依赖特定条件）
| 编号 | 内容 | 依赖 |
|------|------|------|
| P1 | Lower-bound obstruction（V(T)=D+X 需 uniform coercivity） | 引理 3 的交叉项控制（未建立） |
| P2 | Rigidity Gap（C_Λ = Σ\|b_r\|/b₀ < 1 ⟹ inf F > 0） | 严格充分——三角不等式不紧 |
| P3 | Coercivity gap for regular configurations（λ_min 超快退化） | 数值确凿——Cauchy det 严格证明待完成 |

### NUMERICAL OBSERVATION（数值验证）
| 编号 | 内容 | 数据 |
|------|------|------|
| N1 | β≈½（5 探针交叉） | Mellin/振幅/β体积/Im 展宽/密度对偶 |
| N2 | RvM 配置 F/bohr 稳定 ~0.03-0.05（J 到 4000） | 多配置扫描 |
| N3 | margin ~ 0.2/log J（对数退化——数值拟合非定理） | J 200-1600 |
| N4 | E_Λ 与 F 反相关（lattice E 大 ⟹ F 小） | 四模型对比 |
| N5 | 真实 ζ 零点 additive energy 低（9.7e4——规则排列 1/55） | 2M 数据 |
| N6 | 离轴配置 Λ' 泄漏随 δ 增大（0.026→0.303） | 修改 Hadamard |

### CONJECTURE（未证明）
| 编号 | 内容 | 支持 |
|------|------|------|
| C1 | RvM 型密度 + 分离 + 局部 regularity ⟹ C_arith | 数值（N2/N3——但 margin 退化——弱支持） |
| C2 | difference-spectrum non-concentration ⟹ uniform coercivity | 数值（P2 的精细版本——待证明） |
| C3 | ζ 零点满足某个更强的 difference-spectrum condition | N5（additive energy 低——但无条件性未知） |

### FAILED ROUTE（审计后确认不提供 exclusion）
| 编号 | 路线 | 失败原因 |
|------|------|------|
| F1 | 正性（Weil/轨道/Li/de Branges/HB） | 循环（正定性 ⟺ RH）或 penalty |
| F2 | 谱（HP/BK/Connes/散射） | 循环或类型不匹配 |
| F3 | 迹（Weil/trace/commutator） | 自适应（恒等） |
| F4 | 可实现性（D5/D6/Euler 兼容） | 一阶合法——二阶循环 |
| F5 | 算术几何（Arakelov/Deninger/THH） | 宿主有——约束无（无 Fr） |
| F6 | 正定核（K1-K2） | 两难（独立⟺不含β） |
| F7 | 变分/能量（D/E(ε)/图谱） | penalty——无排除型 |
| F8 | 动力学（de Bruijn-Newman/Φ） | Λ≤0=RH 循环——Φ 正性不够 |
| F9 | 密度→coercivity（RvM 候选） | margin 退化——不提供 uniform |
| F10 | additive energy→coercivity | 非决定性（quadratic 反例）——proxy |
| F11 | zero-prime coupling | 唯一性循环——无独立约束（初步） |

## 结论
**论文中五种状态严格分开**——THEOREM（10）+ PROPOSITION（3）+ NUMERICAL（6）+ CONJECTURE（3）+ FAILED（11）——**审稿人可逐项审计**——这是论文可信度的核心。
