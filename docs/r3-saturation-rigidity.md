# R3 精化——saturation + rigidity（阶段 B 入口）

> 2026-09-07 15:00 · 唐先生 R3 定稿——阶段 A 结束——定向数学考古开始

## R3 核心问题
**什么数学结构能在完全不输入零点位置的情况下，使 RH-free 正性条件的可行域自动退化到 Re ρ = ½？**

- 正性控制符号（sign）——不控制支撑（support）——P27-P33 卡因
- R3 ≠ 另一个 positivity——是 support rigidity / equality rigidity

## 抽象模板
```
RH-free positivity
+ exact arithmetic identity
+ rigidity/equality principle
⟹ supp μ ⊆ {δ = 0}
```
- positivity：对象不能负贡献
- identity：必须达到极限
- rigidity：极限 → 结构唯一性
- support：临界线

## 五类刚性来源
| 类 | 结构 | RH 对应 |
|---|---|---|
| I 等号刚性 | Q₁,Q₂≥0 + Q₁+Q₂=0 ⟹ 等号条件 ⟹ δ=0 | 最干净原型 |
| II 自伴/反演（弱形式） | 有限/弱自伴 ⟹ 谱定位 | HP 墙风险——需弱形式 |
| III 不确定性原理 | 互补约束 + A·B=1 饱和 | 尺度对偶 + 饱和 |
| IV 矩/测度确定性 | M_{2k}=0 + 确定性 ⟹ support | 零矩 + 确定性 |
| V 反演/唯一延拓 | FE + 正性 + 唯一性 | FE 只给对称——需额外 |

## 反循环原则（第一死亡测试）
**算术侧不知道 β——但其极值/等号结构自己暴露 β=½**
- 死亡：等号条件证明用了 β−½——或 RH——或零点——或显式离轴测试函数
- 合格：Q=0 ⟺ δ=0 的等价不引用 β

## 与旧路线区别
| 路线 | 缺口 |
|---|---|
| Rédei | 高阶信息不传播 |
| D* | 传播被局部递推吸收 |
| C | 传播只是显式公式 |
| P27-P33 | 正性没有 support rigidity |
| **新目标** | **exact saturation + rigidity** |

## 阶段 B 入口
定向数学考古：围绕"RH-free 精确饱和定理——等号刚性 ⟺ 临界线支撑"
