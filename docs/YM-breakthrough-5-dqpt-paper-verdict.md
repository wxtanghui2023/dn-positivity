# 突破口分析（五）：**"相变路线"文献已查清 —— 它是"检测/验证"框架，落回我们的墙**

**依据**：唐先生 2026-09-11 14:55（"继续"）｜**约束**：无 $1/2$ 输入；L2 未动
**标注**：【外部·未验证细节】【引用·经典】【推导】【已注册·本项目】

---

## §1 【外部】论文事实（检索所得；细节未独立核验）
```
标题：The Riemann Hypothesis manifested in dynamical quantum phase transitions
发表：Nature Communications 17 (2026) 8163 ；DOI 10.1038/s41467-026-74935-8
预印本：arXiv:2511.11199 [quant-ph]，2025-11-14；作者含 Wei, Lu, Yang, Gao, Zhai 等（10 人）
内容要点（摘要级）：
 · 把 ζ 的非平凡零点与【dynamical quantum phase transitions (DQPT)】对应；
   两个互补的工程化多体系统：**累积相位因子** 与 **Loschmidt 振幅**
 · 在 β = 1/2 时 Loschmidt echo 呈【vanishing-and-revival】，在临界时刻 t_c 消失，
   而这些 t_c 对应非平凡零点 ⟹ 产生速率函数的非解析性（DQPT 信号）
 · ⚠️ **"as the evolution time t increases, this correspondence becomes increasingly accurate"**
   ⟹ 该对应是【渐近近似】，不是精确恒等式
 · 实验：**NMR 量子处理器（5 qubit）** + 数值模拟：只有当参数【同时在临界线上且等于某零点】时
   探针量子比特的相干性才完全崩塌（= 检测到 DQPT）
 · 定位：**可用于"多项式和资源的量子算法去【验证】高阶零点"**
 · 相关引用：Peng et al., PRL 114, 010601 (2015)【实验观测 Lee–Yang 零点】；
   Cassettari–Mussardo–Trombettoni, "holographic realization of the prime number quantum potential" ✓
```

## §2 ⭐⭐ 判定：该框架是【检测/验证】，不是【证明】—— 且它落回本项目已识别的墙
```
① 目标：论文自述是"verify high-order zeros"（验证高阶零点）⟹ 【验证型】✗ 非证明型
② 对应是【渐近】的（"increasingly accurate as t increases"）⟹ 正是"极限/一致性"缺口 ✓✓
③ 检测 ≠ 排除：它检测"零点在临界线上"的现象，但【不排除】非临界零点 ⟹ 本项目 β-wall ✓✓
④ 更关键：若用它去【取极限】，仍需"与 t 一致"的精度 ⟹ 与本弧 §3 的 uniformity 缺口同址 ✓✓
```
$$\boxed{\text{该论文 = 物理实现（量子模拟）的"零点检测器"，落在【detection ≠ exclusion】与【渐近对应】两处已知墙上}}$$

## §3 与本项目历史的**直接对应**（重要验证）
```
本项目早期（2026-08 前后）已把 DQPT 作为【物理类比】探索过（见 MEMORY 索引：log-gas / 准晶 /
 Ferguson–Luttinger / DQPT / 金融市场类比），当时结论是：
   **物理类比在 γ-通道被验证，但【缺 β-通道】** ⟹ 即 β-wall ✓
⟹ 现在这篇 2025–2026 的 Nature Comms 论文，正是【同一路线】的成熟版本，
   而它【同样】停在检测层 ⟹ **独立群体独立地抵达同一面墙** 这是对本项目中心论断的【外部验证】✓✓
```

## §4 由该论文可提取的**一条可迁移线索**（诚实：仅线索）
```
框架核心 = "probe qubit coupled to a LOGARITHMIC spectrum" ⟹ 能级 = log n ✓
⟹ 物理实现用的是【log 尺度】，而非乘法尺度
⟹ 与本项目已注册结论一致："筛法/Mertens 的自然临界指数住在 log 变量" ✓
⟹ 可攻点：既然实现落在 log 尺度，那么"乘法尺度 → log 尺度"的转换处
   （即 n ↦ log n 的算术来源）是否就是缺失的那一环？—— 这是【新问题】，
   且与本项目 D3 的"两尺度"、E2 的"非分解决定 L"同族 ⚠️（未验证）
```

## §5 本轮净结果
```
① 未验证线索【已查清】：论文真实，是【检测/验证型 DQPT 框架】（NMR 5 qubit + 量子算法验证零点）
② 它【未】解决证明问题；且自述对应是【渐近】的 ⟹ 落在 uniformity 缺口 ✓
③ 它落在【detection ≠ exclusion】墙上 ⟹ 与本项目 β-wall 【同一堵墙】（外部独立验证 ✓）
④ 与本项目早期 DQPT 探索【同一路线】⟹ 结论一致（γ-通道成立，β-通道缺）
⑤ 新的（很窄）可攻点：物理实现住在【log 尺度】，故"乘法→log 尺度转换"可能是缺失环节 ⚠️
```

## §6 边界
```
· §1 全部为【外部·未验证细节】（检索摘要级；未读原文全文，未核验数值/实验）
· §2/§3 的判定为【推导 + 本项目已注册结论】；§4 为【线索·未验证】
· 【未做】未输入 1/2；未构造模型；未改 L2；未声称解决任何问题
```

## §7 提交链
```
ae7ced5（Hurwitz 路线）→ 本篇（DQPT 论文查清：检测型、渐近型、落回 β-wall）
```
