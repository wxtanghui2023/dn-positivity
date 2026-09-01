# P5.12 收口：Uniform coercivity is not controlled by density statistics alone

> 2026-09-01 · 唐先生收口指令 · 反例构造失败——停止 P5 数值路线

## 最终反例搜索（P5.12-C3——只做一次）
目标：构造满足 R₀+R₁+R₂ + 强 additive-energy bound（差频分散——E 低）但 inf_θ F → 0 的配置。

| 构造 | margin(J=400) | E_Λ(400) | 合法性 |
|------|:--:|:--:|:--:|
| 代数(β=0.001) | 0.106 | 3.9e5 | ✓（间距 OK） |
| 代数(β=0.005) | 0.341 | 3.5e5 | ✓ |
| 代数(β=0.010) | 0.483 | 3.4e5 | ✓ |
| 随机块相位 | 0.076 | 5.1e5 | ✗（负间距） |
| sin 调制 | 0.69-0.78 | 4.3-4.6e5 | ✗（负间距） |
| lattice(0.5 密) | → 0（0.003@J=1200） | **5.3e6（E 极大）** | ✓ 但违反强 additive-energy bound |

## ⭐ 结论：反例构造失败——停止 P5 数值路线（唐先生指令）
- **合法构造（保持间距/RvM 密度——差频分散——E 低）——margin 全部稳定 > 0（0.08-0.78——甚至大于 RvM 的 0.03）——反例失败**
- **唯一 margin → 0 的是 lattice(0.5 密)**——但——差频集中（E=5.3e6——违反"强 additive-energy bound"）
- **"R₀+R₁+R₂+low additive energy ⇏ uniform coercivity"未被构造出**——**但——"R₀+R₁+R₂ ⟹ uniform coercivity"也未证明**

**最严谨结论（唐先生）**：现有实验支持需要一个比 R₀-R₂ 更强的 difference-spectrum condition——但该充分条件尚未识别。

## 论文定型（唐先生的修改——采纳）
**标题**："Uniform coercivity is not controlled by density statistics alone"

| 层次 | 状态 |
|------|:--:|
| F ≥ 0（Gram positivity） | 严格 |
| F > 0（pointwise nonvanishing） | 逐配置成立——不自动 uniform |
| **inf_θ F ≥ η > 0（uniform coercivity）** | **核心未知** |
| R₀+R₁+R₂ ⟹ uniform coercivity | **未证明** |
| ζ 零点满足所需条件 | 未知 |
| 推出 RH | 不成立/未触及 |

## 最关键的一句话（唐先生——Rigidity Gap 的最精确形态）
> **density information controls how many frequencies there are;**
> **coercivity controls how their difference spectrum can interfere at its worst phase.**
> 两个信息层次之间的缺口——就是目前最精确的 Rigidity Gap。

## P5 系列数值路线正式终点
- 从 P5.1（框架独立性审计）到 P5.12（difference-spectrum 分析）——**完整走过"检测 ≠ 排除"的每一层**
- **核心定位**：Rigidity Gap = density 信息（频率数量）与 coercivity 信息（差谱最坏相位干涉）之间的缺口
- **不再做无止境参数扫描**（唐先生指令）
- 下一步（如果继续）：**识别"uniform difference-spectrum rigidity"的充分条件**——纯调和分析（脱离 ζ）——或——暂停让结论沉淀
