# P9.2：Theta-Minor Rigidity——M(a,b) minors——数值被杀（初步）

> 2026-09-01 · 唐先生 P9.2 理论审计 · ①-⑤ 步

## 唐先生的 SR∞ 独立性审计（采纳）
1. **"Φ ∈ SR∞ ⟹ RH"不能直接说**——PF∞ kernel ⟷ Laplace 倒数 ∈ LP（Schoenberg）——且——有结果把 RH 等价为 1/Ξ 的变换是 PF 函数——**直接定义成 PF∞ 条件——循环（Weil/Li 型）**
2. **分叉**：对"变换后的 kernel"做——不是 Φ 的 PF∞——而是 M(a,b) = Φ(a+b)Φ(a−b) 的 infinite-order minors
3. **对应**：density statistics ↔ finite-order kernel positivity——difference-spectrum rigidity ↔ infinite-order total positivity——**"缺失层"可能是阶数极限**
4. **P9-A'（最看好）**：D_n = det[M(a_i,b_j)]——固定符号？——theta structure ⟹ SR∞(M) ⟹ Ξ ∈ LP

## P9.2 数值结果（高精度 mpmath——可靠）
### Φ 变号确认（真实）
Φ(−2) = −1.8e-24（负）——Φ(−1.5) = +6.5e-24（正）——Φ(0) = 0.447——**Φ 变号真实（非噪声）——Φ 不是正函数**

### D_n 有序 minors（高精度——近区）
| 阶 | D_n | 符号 |
|---|---|---|
| 2×2 | −4.06e-4 | **负** |
| 3×3 | −2.22e-9 | **负**（多偏移一致） |
| 4×4 | +3.21e-20 | **正** |

**D_2 负 + D_4 正——变号——无固定符号——无规则 SR 模式（(−1)^n 不匹配——(−1)²=+ 应正但 D_2 负）**

## ⭐ 判定——Theta-Minor Rigidity Conjecture 数值被杀（初步）
- **SR∞(M) 不成立**（至少近区/该选择——D_2 负已是"全正"反例）
- **M 的 minors 变号——继承 Φ 的变号（乘积结构）**
- **"theta-generated positivity"所有候选（Φ 的 PF∞——不适用；Φ 的 SR∞——变号不够；M 的 SR∞——数值不成立）——撞墙**

## 有价值的判断（方向性）
**zeta 的 kernel（Φ/M）没有足够强的全正性——"total positivity 路线"（P9）本质关闭（与 P5-P8 一致）**——但——**"为什么 zeta 的 kernel 没有全正性"本身值得理解**（可能与 RH 的困难相关——kernel 的变号结构是"算术的"——不是"全正的"）

## 诚实边界
- 数值只测了近区/特定选择——但——**D_2 负（明确）已是"SR∞ 全正"的反例**
- 换 kernel（M 的变形）——无自然判据——换 observable 困境
- "SR∞(M) 需要零点信息"的循环检查——**未到（对象已数值被杀）**

## 下一步（P9 系列）
- (a) 接受 P9-A' 数值被杀——P9 核心对象（SR∞(M)）不成立
- (b) P9-B（de Bruijn-Newman discriminant/index——拓扑障碍——未打）
- (c) 唐先生指示
