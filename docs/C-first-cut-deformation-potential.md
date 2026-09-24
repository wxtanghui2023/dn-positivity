已查地图：命中（`B2-2-explicit-kernel-and-inversion-obstacle`（⇒ 唯一入口＝形变）／`EXP-A-1-partner-odd-kill`／`WHY-CANNOT-CREATE-TOOLS-bohr-and-tao`（`\Lambda`-型单调流））⟹ 引用，不开新案
D0: 本档对象 = `C` 首刀设计：形变族上的有界势能 `P_t` ＋ 一阶形变响应判据 ＋ **prior-art 风险标注**
D1: 0 （[REVIEW] 轮次：设计与风险标注，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`C` 首刀：形变族上的有界势能**

## §1 设计（本档）

```
【形变族候选】 **(i) heat-flow 型**（`t` 参数使零点沿 `\Lambda`-型流移动）；**(ii) 测试族连续变形**（`h_\theta`）；**(iii) 权重变形**（`r` 连续化）✓
【有界势能定义】 $$P_t(\gamma,w):=\frac{\#\{\rho:\ \gamma_\rho\in\text{窗}\ w,\ \Re\rho=\frac12\}}{\#\{\rho:\gamma_\rho\in w\}}\in[0,1]$$ ✓
【单调性来源】 **`CNV` 型定理**（实零点数随 `t` 单调）⟹ `t\mapsto P_t` 单调（⚠️ 依赖该硬定理，不可自造）✓
【一阶响应判据】 $$\boxed{P_{t+\Delta}(\gamma,w)-P_t(\gamma,w)\ \ge\ c\cdot\Phi(|\delta|)\ >0\quad(\delta\ne0)}$$ ⟹ 反解 `\Phi` 即得 `|\delta|` 的**尺度寿命上界** ✓
```

## §2 ⚠️ prior-art 风险（必须标注，且**先核查再计算**）

```
【风险根源】 `P_t` 的自然形式**就是 `\Lambda`（de Bruijn–Newman）概念的局部化**：某高度的"实零点比例随流时间变化" ⟹ 与既有 `\Lambda`／`\Lambda_{DH}` 研究**同族** ⚠️⚠️
【故本档判定】 `C` **可以设计**，但**开工前必须做一次 30 分钟核查**：是否已有"局部化 `\Lambda`／窗口实零点比例随形变时间"的工作 ⟹ 若有 ⟹ `C` 记为 CLOSED（prior art）✓
【对照本线前车】 `I`（`DH` parity）与 `B-1` 均因 prior-art 撞车而 CLOSED ⟹ **不做核查就开算＝重复犯错** ✓
```

## §3 状态与下一步

```
【`A`】 完成：β 信息丢弃清单（坐标 → 标签）✓
【`B2-2`】 完成：核可算，但检测＝**反演** ⟹ PARTIAL，不能出不等式 ✓
【`C`】 设计已定；**下一步＝30 分钟 prior-art 核查**（不是计算）✓
【边界】 §1 设计为**本档自行推导**；`CNV` 单调性／`\Lambda` 研究属既有文献（档级）；未制造候选／未启动搜索／未碰 RH 总攻。
