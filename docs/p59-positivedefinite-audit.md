# P5.9: Positive-kernel / Parseval / spectral-gap hostile audit——最终判定

> 2026-09-01 · 唐先生指令 · 最后一个值得投入重火力的数学检查点
> 核心问题：能否绕过交叉项，直接从独立构造的正定二次型得到离轴贡献的 uniform lower bound？

## Lemma 3 的重新表述（obstruction proposition——降级）

**V(T) = D(T) + X(T)**——D 是对角二次型（离轴零点贡献），X 是交叉项：
- ✅ 已确认：D(T) 对 β>1/2 有正确增长尺度（T^{2β−2}）
- ✅ 已确认：density/spacing 工具控制零点"有多少、隔多远"
- ⚠️ 要推出 V(T) ≳ D(T)——需要 **uniform coercivity：X(T) ≥ −(1−η)D(T)，η>0**
- ⚠️ 最后一步需要**相位相关性的独立控制**——不是 density control

**论文命题（正式表述）**：
> **Proposition (Lower-bound obstruction).** The lower-bound route reduces the exclusion problem to a uniform coercivity problem for an oscillatory quadratic form X(T) ≥ −(1−η)D(T). Classical zero-density and spacing estimates do not by themselves supply such coercivity.

---

## P5.9-A：Quadratic-form reformulation（V(T) = ⟨K_T a, a⟩——spectral gap）

### 闭式
```
K_T(ρ,ρ') = ∫_{logT}^∞ e^{(ρ+ρ̄'−2)u}du = T^{ρ+ρ̄'−2}/(2−ρ−ρ̄')
V(T) = Σ_{ρ,ρ'} a_ρ ā_{ρ'} K_T(ρ,ρ') = ⟨a, K_T a⟩
```
**K_T 是 Gram 矩阵**（内积 <e^{ρu}, e^{ρ'u}>_{L²([logT,∞), e^{−2u}du}）——**恒正定（无条件——任何配置）**

### 数值（真实零点——β=0.6 假想离轴）
- λ_min(K̃_T)（归一化相关矩阵）：J=60 时 ~0.19——J=100 时 ~0.132——**随 T 稳定（不退化）——随 J 温和减小（对数级：λ_min×log γ：1.57→0.72）**

### 关键障碍（为什么 spectral-gap 不能直接成立）
- **Gershgorin（模）失败**：行和 Σ_{k≠j}|K̃[j,k]| = Σ (2−2β)/√((2−2β)²+(γ_j−γ_k)²) ~ Σ1/|γ_j−γ_k|——**谐波——对数发散**——Gershgorin 不适用
- **需要"相位相消"的精细论证**（模上界不够——允许完全相消）——**真实零点的相位结构——ζ 的——可能 RH 相关**
- **数值 λ_min ~ 0.13 支持"实际相位相消"——但——严格证明需要相位信息——没有绕过 phase-correlation obstruction——只是重述为"K̃_T 的 spectral gap"**

### ⭐ 确认唐先生预判
**"kernel 的 spectral gap/coercivity 本身就是缺失的 rigidity"**——不是"某个展开式的 cancellation"——而是核层面的结构缺口

---

## P5.9-B：正定化搜索（三类方法）

| 方法 | 结果 |
|------|------|
| **1. Parseval 型恒等式** | ∫\|F\|² = ∫\|F̂\|²——F̂ 含极点（零点）——**回到零点——不绕过** |
| **2. 正定核/reproducing-kernel** | K_T 是 Gram（正定——无条件）——但——spectral gap 需频率分离（A 的结果）——**不绕过** |
| **3. 特殊 test function（交叉消失）** | 需"对角化"——接近零点不可分离（测不准权衡）——log 因子不可避免——**不绕过** |

**结论**：**不存在"独立构造的正定二次型"同时满足：① 正定（无条件）② 有 coercivity（λ_min 下界）③ 不依赖零点信息**——正定（①）平凡（Gram）——coercivity（②）需要频率分离/相位信息（③ 循环）——**三者的同时满足正是缺失的 rigidity**

---

## P5.9-C：与已知 RH-equivalent criteria 对照

| 判据 | 正定形式 | 正定性状态 |
|------|------|:--:|
| Littlewood | Σλ_n/n^s 类 | ⟺ RH（循环） |
| Weil | W(f,f) ≥ 0 | ⟺ RH（循环） |
| Nyman–Beurling | span 完备性 | ⟺ RH（循环） |
| Báez-Duarte | ρ(nθ)/n 类 | ⟺ RH（循环） |
| Li | λ_n ≥ 0 | ⟺ RH（循环） |
| explicit-formula 二次型 | 自适应 | 恒等式（非判别） |
| **我们的 K_T（Gram）** | **⟨a, K_T a⟩ ≥ 0** | **无条件（平凡正定——非判别）** |

### ⭐ 关键区别（Rigidity Gap 的正定化形态）
- **Weil 正定**：非平凡——"W(f,f) ≥ 0"⟺ RH（循环——正定性即 RH）
- **K_T 正定（Gram）**：平凡——恒成立（任何配置）——**给不了 coercivity**
- **"统计 → 排除"候选的最终命运**：**K_T 的 Gram 正定性（无条件）≠ Weil 的非平凡正定性（⟺ RH）——中间缺的正是 coercivity（λ_min 下界）——而 coercivity 需要零点信息（循环）**
- **C2 没有产生新的中间刚性——它落入（或试图落入）RH 的正定等价判据族——但——连"正定性"都只是平凡的（Gram）——更别说 coercivity**

---

## ⭐ P5.9 最终判定

**能否绕过交叉项，直接从独立构造的正定二次型得到离轴贡献的 uniform lower bound？——不能（在审计范围内）**：

1. **Gram 正定性（无条件）**——✓ 存在——但——**平凡**（任何配置）——不提供 coercivity
2. **coercivity（λ_min 下界）**——✗——需要频率分离/相位信息：
   - Gershgorin（模）失败（谐波发散）
   - 相位相消需要真实零点结构（可能 RH 相关）
   - 数值 λ_min ~ 0.13 支持——但严格证明未建立
3. **正定化（Parseval/核/test function）**——✗——都回到频率分离/零点信息
4. **与 RH 等价族对照**——**K_T 的平凡正定 vs Weil 的非平凡正定——中间缺 coercivity——这正是 Rigidity Gap**

### 比 P5.8 更强的结论
**Rigidity Gap 不只是"某个展开式的 cancellation 问题"——而是"正定化/spectral-gap 层面的结构缺口"**：
- 任何"从正定二次型排除离轴"的尝试——需要"非平凡正定 + coercivity"
- "非平凡正定"（Weil 类）⟺ RH（循环）——"平凡正定"（Gram）给不了 coercivity
- **中间层（非循环的正定 coercivity）——不存在（在审计范围内）**

### C2/C3 的论文表述（最终）
```
RH ⟹ C2：严格（pointwise 直接积分）
C2 ⟹ RH：open within the present derivation——attempted proof reduces to
           a uniform coercivity problem（oscillatory quadratic form）——
           classical zero-density/spacing estimates do not supply such coercivity
C3 ⟹ RH：可走（经 C2——同受阻）
RH ⟹ C3：未完成（交叉项无 log 因子）
```
**C2 不称"RH 等价"——C3 保持单向——不填闭环**：
```
      RH
     /  \
    ↓    ?
   C2   C3
    ↑    ↑
   C1    ?
    ↑
   C0
```

---

## 研究问题转向（唐先生建议——确认采纳）
从"研究 ζ 的表示"转向"**研究排除机制的分类**"：

**Rigidity mechanism 定义**：结构 M 若满足
```
independent construction + β-sensitive observable + uniform coercivity（独立于零点位置）
```
则具有 exclusion power。

**统一分类表**：
| 机制 | β-sensitive | 独立 | coercive | exclusion |
|------|:--:|:--:|:--:|:--:|
| Euler/Mellin | ✓ | ✓ | ✗ | ✗ |
| explicit formula | ✓ | ✓ | ✗ | ✗ |
| scattering | ✓ | ✓ | ✗ | ✗ |
| Arakelov | 间接 | ✓ | ✗ | ✗ |
| THH/TP | 部分 | ✓ | ✗ | ✗ |
| positive kernels | ✓ | 部分 | 条件 | ✗ |
| **L² tail（K_T）** | ✓ | ✓ | **缺失** | ✗ |
| hypothetical HP | ✓ | 若存在 | ✓ | ✓ |

**P5.9 的贡献**：L² tail 路线的"coercive"列从"✗（未找到）"升级为"**缺失（结构性——spectral-gap 层面）**"——这是分类表中最精确的一格。
