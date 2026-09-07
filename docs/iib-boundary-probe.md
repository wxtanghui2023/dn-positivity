# II-B 数值探索——边界形式朴素实现失败

> 2026-09-07 15:20 · II-B（arithmetic boundary form）首测

## 对象
B_N(f,g) = ⟨Df,g⟩_N − ⟨f,D^♯g⟩_N——D = 卷积 A_a——D^♯ = dilation B_b
测试 h_s(n) = n^{−s}

## 数值结果
| 对 | Re B 行为 |
|---|---|
| a=b=1（伴随——） | ≡ 0（1e-15——）——无信息 |
| a=1, b=μ | **发散**（N=60: −15 → N=300: −27——） |
| a=μ, b=1 | +发散（反号——） |

## 分析
1. **伴随对**（D^♯ = D*——）：B ≡ 0（Re 精确抵消——）——无边界项
2. **非伴随对**：B_N ~ 发散（σ=½ 时 Σn^{−2σ} 调和型——）——无 vanishing 条件
3. **朴素实现不工作**：要么恒零——要么发散——没有干净的"边界 vanishing 条件"

## Mellin-Parseval 视角（概念——）
- 乘性卷积的 Mellin 表示天然在 Re = ½ 轮廓（Parseval——）
- "边界项" = 轮廓移动扫过的留数——vanishing 条件需仔细定义
- **风险**：轮廓移动 + 留数 = Mellin 变换技巧——靠近显式公式（死线——）

## 判定（初步——）
II-B 朴素实现（h_s 对角测试——）失败：
- 无干净 vanishing 条件（伴随零/非伴随发散——）
- Mellin-Parseval 正规化方向靠近显式公式（死线——）
- **II-B 需要：① 正确的 Green 恒等式离散类比（非 ⟨Df,g⟩−⟨f,D♯g⟩ 对角——）或 ② 概念上确认与 Lax-Phillips 散射的区别**

## 与 Lax-Phillips/de Branges 的重叠风险（重要——）
- "边界条件选择 zero mode" = 散射理论的核心（Lax-Phillips——de Branges 追的——）
- II-B 若无"算术独有"的边界结构——会滑入散射理论（V 类已审计——）
- 需要明确：II-B 的"算术边界"与散射的"无穷远边界"本质区别是什么？

## 文件
- scripts/iib_boundary_probe.py
