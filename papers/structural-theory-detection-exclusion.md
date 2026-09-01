# A Structural Framework for Detection without Exclusion
## From Detection to Exclusion: Structural Boundaries in Riemann-Type Problems
## 从检测到排除：Riemann 型问题中结构性刚性缺口的统一框架

> 作者：Hui Tang · 2026-09-01 · 结构性审计论文草稿 v1
> 定位：不是 RH 的证明，也不是反证——是回答"为什么如此多完全不同的模型都能稳定看到 1/2，却无法从'看到'跨越到'强制'"

---

## 摘要

本文建立 Riemann 猜想（RH）及其相关猜想（GRH/哥德巴赫/孪生素数）统一框架的**结构性审计**。核心贡献不是证明 RH，而是回答一个精确的问题：**为什么一大类 RH 型结构能够稳定产生临界线信号（检测），却无法自动产生排除机制？**

论文主轴分四层：
- **I. 无条件结构层**：A_min ⟹ F_U（Euler 积/显式公式/素数统计/轨道结构/正性/变分——RH 不进入基础公理）；
- **II. 检测层**：prime data ⟹ β-sensitive observables（振幅/Mellin/V(T)/矩谱）——**β can be detected**（但不是 forced）；
- **III. 排除层**：正式定义 rigidity mechanism（independent construction + β-sensitive observable + uniform coercivity）——只有 coercivity 把检测升级为排除；
- **IV. Rigidity Gap**：**Detection ⇏ Exclusion**——缺失的中间桥梁不是更多数据/更漂亮的表示——而是 **independent rigidity / coercivity**。

**冻结结论（三句）**：
1. **Detection is unconditional; exclusion requires additional rigidity.**
2. **The audited positive-kernel constructions do not yield uniform coercivity.**
3. **No independent coercive mechanism was identified within the audited framework.**

P5.9（正定化/spectral-gap 审计）确认：Gram positivity 不蕴含 uniform coercivity；可用的非平凡正性机制导向 RH 级信息。本文并未证明数学宇宙中不存在第三种机制——只是在本审计覆盖的范围内未发现。

**关键认识论结论**：本文最有价值的可复用资产是——**一套识别"看起来像 RH 证明、实际上只是检测"的机制的方法**。

---

## 1 引言：检测与排除的分离

### 1.1 问题的精确定位
经过对 ~30 条独立路线的系统探索（正性/谱/迹/可实现性/算术几何/正定核/变分/能量/动力学/统计），一个统一的现象反复出现：

> 所有模型都能**检测**离轴（β ≠ ½ 留下不同信号），但没有任何模型能**排除**离轴（证明 β ≠ ½ 与无条件结构不相容）。

这不是偶然失败——而是**结构性事实**的体现：无条件算术结构（Euler 积/显式公式/函数方程）到 β-sensitive observables 的通道是**无损且自适应的**——它编码离轴信息（检测），但不产生排除（约束）。

### 1.2 本文不是
- 不是 RH 的证明（不声称 β=½）；
- 不是 RH 的反证（不声称存在离轴零点）；
- 不是"又找到一个 RH 等价条件"（D=ΣP_γ 明确标注为等价刻画——组织方式新——机制非新）。

### 1.3 本文是
对统一框架的**结构性审计**：建立无条件骨架、精确刻画检测与约束的分离、给出逻辑强度地图、做框架失真测试、提出 rigidity gap 作为结构障碍。

---

## 2 命题 A：无条件骨架 F_U

### 2.1 定义
```
F_U = (A_U, R_U, O_U)
```
- **A_U（无条件输入）**：A1 素数点过程；A2 Euler 积（σ>1）；A3 解析延拓+唯一性；A4 Gamma 性质+函数方程。**RH ∉ A_U**。
- **R_U（严格推理）**：由 A_U 推出的全部无条件定理（T1-T10，见 §2.2）。
- **O_U（可计算 observable）**：θ(t)/V(T)/V_p/Mellin observable/P_γ/S(p)/密度对偶——全部可由素数数据或零点数据计算。

### 2.2 无条件定理（T1-T10——每步标注来源与逻辑强度）
| 定理 | 陈述 | 来源 | 强度 |
|------|------|------|:--:|
| T1 | ∫f_n·S·g = O(1) | Titchmarsh p≤t + van der Corput + stationary + R 项 | 严格 |
| T2 | Σf_n(γ_k) = ½nlogn + cn + O(1)（任意零点配置） | 定理 B | 严格 |
| T3 | mean(S(γ_k)) = ½ | 精确恒等式 | 严格 |
| T4 | P_γ(δ) = δ²M₂/(2U²D₊D₋) ≥ 0（|δ|<½, γ≥γ₁） | 轨道配对+代数（全正系数） | 严格 |
| T5 | D = ΣP_γ(δ) ≥ 0 | T4 逐轨道 | 严格 |
| T6 | 在线虚部唯一最小化 S_proj（合法配置） | Weil 无条件 G=W/2 + 逐项代数 | 严格 |
| T7 | V(T) 衰减指数 = 2β_max − 2 | 对角主导+共轭平均+交叉项 vdc | 严格 |
| T8 | 相位锁定 S(p) = O(1) | Guinand/Weil 显式公式 | 严格 |
| T9 | 对偶守恒 v·dN ≈ 1/2π | 素数定理 + RvM | 严格 |
| T10 | GRH 判据（成对正性迁移——8 模 universal） | P_γ 不依赖 q/χ | 严格 |

**逻辑强度标注**：T1-T10 全部无条件——不引用 RH/GRH——每步来源可追溯。

### 2.3 最小生成集
A_min = {A1, A2, A3, A4}（素数点过程/Euler 积/延拓/Gamma）——生成全部 R_U。**A_min 不包含 RH**——框架无条件层不依赖任何猜想。

---

## 3 命题 B：检测—约束分离（论文主轴）

### 3.1 形式化
定义 **Detect(O, β)**：observable O 对 β 敏感——存在离轴配置使 O 的值与在线不同（可检测偏离）。

定义 **Exclude(O)**：存在无条件定理——O ∈ C ⟹ β = ½（从 O 的值排除离轴）。

### 3.2 主观察（Detect ≠ Exclude）
本文的全部实验（E1-E9）确认：
```
大量 observable 满足 Detect（对 δ 有响应——数值——如 V(T)：δ=0.2 改变 13.6×）
但没有任何已知无条件机制满足 Exclude（O 的值 ⟹ β=½——需要独立刚性——未找到）
```
**检测—约束分离**：β-sensitive ⇏ β-forcing。

### 3.3 为什么分离（结构性解释）
无条件算术结构（A_U）到 β-sensitive observable 的通道是**无损且自适应的**（显式公式对任何零点配置成立——素数数据与零点配置唯一耦合=恒等通道）。恒等通道只产生等式（编码离轴代价 D ≥ 0），不产生不等式（不能编码排除 D ≤ 0）。任何跨越两侧的量要么恒等（自适应）要么独立（无连接）。

---

## 4 命题 C：逻辑强度谱系 C0-C4（严格版——并入 §4.2 审计结果）

### 4.1 定义（精确意义）
```
C0:  V < ∞                      （V = V(1)——全积分收敛）
C1_a: V(T) = O(T^{−a})          （固定 a ∈ (0,1]——L² 尾部衰减）
C2:  V(T) = O(T^{−1+ε})         （所有 ε > 0——L² 尾部——ε-松弛）
C3:  V(T) = O(T^{−1})           （L² 尾部——精确——无 ε）
C4:  ψ(x) − x = O(x^{1/2+ε})    （pointwise——所有 ε > 0）
```
**意义**：C0-C3 是 **L² 尾部**（积分）意义——C4 是 **pointwise** 意义。

### 4.2 预备引理（Lemma 1-4——详细证明见附录，Lemma 3 的交叉项控制见 §4.3 hostile audit）
- **Lemma 1（L² 上界）**：β_max ≤ β ⟹ V(T) = O(T^{2β−2+ε})——无条件（显式公式 + Hadamard + van der Corput + 零点间距下界）
- **Lemma 2（零点间距下界）**：γ_{n+1}−γ_n ≥ c/log γ_n——无条件经典
- **Lemma 3（L² 下界）**：β_max > ½ ⟹ V(T) ≥ c·T^{2β_max−2}——**⚠️ 见 §4.3 hostile audit（交叉项控制待严格确认）**
- **Lemma 4（函数方程桥）**：β_max ≤ ½ ⟺ RH——无条件（函数方程）

### 4.3 条件强度表（最终形式——拒绝模糊"~"符号）
| 条件 | 已证明方向 | 与 RH 的关系 | 意义 |
|------|------|------|:--:|
| **C0** | 无条件成立（PNT——ψ−x=O(xe^{−c√logx}) 平方积分收敛） | **严格弱**（任何 β_max<1 满足——不排除 ½<β<1） | L² |
| **C1_a**（a<1） | 无条件可得（⟺ β_max ≤ (2−a)/2——Lemma 1,3） | **严格弱**（a<1——β_max ≤ (2−a)/2 < ½+ε——编码部分零点信息） | L² |
| **C1_1**（a=1） | 双向（Lemma 1,3） | **⟺ RH**（β_max ≤ ½——Lemma 4） | L² |
| **C2** | **RH ⟹ C2 严格**（pointwise 直接积分）——**C2 ⟹ RH 受阻**（需 Lemma 3 弱版 B——coercivity 缺失——见 §4.3） | **单向严格——完整等价未完成**（obstruction：L² 下界的相位相关性控制） | L² |
| **C3** | **C3 ⟹ RH 严格**（C3⟹C2⟹RH——但 C2⟹RH 受阻——因此 C3⟹RH 同样受阻） | **RH ⟹ C3 需单独证明**（交叉项无 log 因子）——**C3 ⟹ RH 受阻**（同 coercivity） | L² |
| **C4** | 经典（教科书） | **⟺ RH**（von Mangoldt 类经典等价） | pointwise |

### 4.4 逻辑蕴含图（已证明的箭头——不提前填满）
```
      C4 (pointwise)
     /  \
    /    \            ──── 无条件蕴含（已证明）
   ▼      ▼           - - - 待证明/需额外技术条件
  C3     RH
   \      /
    ▼    ▼
  C2 (V(T)=O(T^{−1+ε}))  ⟺ RH（双向严格）
    │
    ▼
  C1_a (a<1)——严格弱于 RH（⟺ β_max ≤ (2−a)/2）
    │
    ▼
  C0 (V<∞)——无条件——太弱
```
**已证明**：C4⟹C3（pointwise⟹L² 直接积分）——C4⟺RH（经典）——C3⟹C2（O(T^{−1})⊂O(T^{−1+ε})）——C2⟹C1_a（a<1）——C1_a⟹C0——C1_1⟺RH
**⚠️ 受阻（Lemma 3 审计后）**：**C2 ⟹ RH**（需弱版 B——coercivity 缺失——见 §4.3 Lemma 3 audit）——**C3 ⟹ RH**（经 C2——同样受阻）——RH ⟹ C3（交叉项无 log 因子——待精细）
**RH ⟹ C2 严格**（pointwise 直接积分——不依赖 Lemma 3）
**明确不存在的反向**：C0⇏C1_a（C0 平凡）——C1_a⇏C2（a<1）——C3⇏C4（L²⇏pointwise）

### 4.5 谱系的含义
**越想让 observable 真正"排除"离轴零点——就越接近 RH 本身**：
- C0（无条件——太弱——任何 β<1）
- C1_a（a<1——编码部分零点信息——严格弱于 RH）
- **C2 ⟺ RH**（L²——双向严格）——**C3 ⟹ RH 严格——RH ⟹ C3 待证**——**C4 ⟺ RH**（经典）
- **在本审计覆盖的已知无条件工具中，未发现严格弱于 RH 且独立可证的中间条件**（不是"数学上不存在"）

### 4.6 修正记录
1. **C3 修正**：早期草稿写"RH ≤ C3"（C3 比 RH 强）——**错误**——修正为 **C3 ⟹ RH 严格——RH ⟹ C3 待单独证明**（交叉项无 log 因子）
2. **拒绝"~"符号**：C2/C3/C4 不再写"~RH"——每个条件单独列出已证明方向

---

## 5 命题 D：Rigidity Gap 与排除机制分类（P5.9 审计结果）

### 5.1 定义（概念量——非标准数学定义）
```
G = β-sensitive information − independent rigidity
```
- β-sensitive information：从无条件算术结构可提取的全部离轴信息（检测能力）。
- independent rigidity：不依赖零点/β 的刚性原理（把离轴从允许提升为不相容）。
- **G > 0**：存在 rigidity gap（信息丰富但无排除机制）——本文的全部证据支持这一图景。

### 5.2 Rigidity mechanism 定义（排除层的正式对象）
结构 M 若满足：
```
independent construction + β-sensitive observable + uniform coercivity（独立于零点位置）
```
则具有 **exclusion power**。只有第三项（coercivity）真正把 detection 升级为 exclusion。

### 5.3 统一分类表（已审计机制）
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

**P5.9 的贡献**：L² tail 路线的"coercive"列从"✗（未找到）"升级为"缺失（结构性——spectral-gap 层面）"。

### 5.4 P5.9 核心命题（Lower-bound obstruction——正式表述）
> **Proposition (Lower-bound obstruction).** The attempted lower-bound route reduces exclusion of off-critical-line zeros to a uniform coercivity estimate for an oscillatory quadratic form. Classical zero-density and spacing estimates, together with the elementary Gram positivity of the associated kernel, **do not by themselves provide** such a coercivity estimate.

**措辞边界（明确）**：
- 不是"no such coercivity exists"——而是"**do not by themselves provide**"。
- 不是"the intermediate layer does not exist"——而是"**No independent intermediate coercive mechanism was identified within the audited classes**"。
- Gram positivity ⟹ uniform coercivity 不成立；可用非平凡正性机制导向 RH 级信息——但本文**未证明数学宇宙中不存在第三种机制**。

### 5.5 Weil 正定的谨慎表述（防定义过宽）
- 本文说的"非平凡正定 ⟺ RH"特指 **Weil criterion 的特定二次型 W(f,f) ≥ 0**——不是泛泛的"nontrivial positivity is equivalent to RH"。
- Gram kernel 的 K_T ⪰ 0 只是 **Hilbert 空间几何事实**（任何配置成立）。
- 真正需要的是 coercivity：⟨K_T a, a⟩ ≥ η||a||²（η > 0 uniform in T）——**两个概念在全文严格分开**。

### 5.6 全部路线的统一压缩
prime array / log gas / crystal / Mellin / geometry / scattering / Arakelov / THH-TP / positive kernels / L² tail——**全部产生 β-sensitive observable——但最终没有产生 independent rigidity gap > 0**。这是跨越 ~30 条路线后的共同结构。

---

## 6 P5.8 框架失真测试（W_δ）

### 6.1 构造
RH-agnostic surrogate world W_δ：满足 F_U 的全部 15 个无条件约束（Euler 型乘性/PNT 渐近/函数对称/素数相关/P_γ 正性/C₂ 结构/标度律）——但 β_max = ½+δ。W_δ 是抽象的"另一个世界"（内部自洽——不是伪造 Euler 积离轴 ζ——那会触及 RH 本身）。

### 6.2 结果（严谨表述）
**在所定义的 15 个无条件约束组成的抽象系统中，构造的 W_δ 未被任何约束排除；因此该约束系统本身不提供 RH 的逻辑分离。**

### 6.3 诚实边界（主动"自杀式"表述）
**P5.8 并不证明不存在独立刚性原理；它证明的是，在本研究所覆盖的公理与构造范围内，没有发现能够排除 W_δ 的独立刚性机制。** 未来可能出现新的刚性原理——但那必须来自新的对象（提供 independent rigidity），而不是新的表示（observable）。

---

## 7 RH/GRH/哥德巴赫/孪生素数的共同算术架构

### 7.1 P_γ 结构作为共同架构
```
P_γ ⟶ { RH channel（β=½ 边界）
       { Goldbach channel（C₂ 常数）
       { Twin-prime channel（C₂ 常数）
```
三个猜想共享 P_γ 骨架（轨道配对 + 代数正性——无条件）+ C₂ 常数（数值 E4：C₂ = 0.661377 ≈ 已知 0.6601618——孪生渐近与哥德巴赫奇异级数共享）。

### 7.2 明确边界
**common architecture ≠ common proof**：
- C₂ 的数值吻合是 computational evidence / structural observation——**不是定理**（没有严格推出 C₂ 渐近）。
- 三个猜想的"共同"是**同源**（同一 P_γ 对象的不同通道）——不是"一个定理同时蕴含三者"。
- "更基础的可实现性定理"（存在 + 唯一稳定实现）是候选形态——但"唯一稳定实现"未证（= RH 的变分表述）。

---

## 8 方法论：识别"看起来像 RH 证明、实际上只是检测"的机制

### 8.1 判据（可复用研究资产）
一个机制是"检测"而非"证明"，如果它满足以下任一特征：
1. **等价性**：机制的核心条件与 RH 等价（如 C2——L² 版本的 ψ=x+O(x^{1/2+ε})）——循环。
2. **自适应性**：机制的正性/恒等式对任何零点配置成立（如 Weil/显式公式/轨道正性 P_γ ≥ 0——penalty 不排除）——只给代价不给排除。
3. **依赖零点**：机制的正性/谱构造需要零点知识（如 de Branges/Hermite-Biehler/交织算子）——循环。
4. **数值支撑**：机制的"证据"是数值（β≈½——5 探针）——检测非约束。
5. **未构造**：机制依赖未构造对象（Θ/动力学吸引子/特征多项式）——不可审计。

### 8.2 应用
这套判据可用于快速筛除任何新提出的"RH 证明"候选——判断它是否真正提供 independent rigidity，还是仅仅是检测的重新包装。**这是经过大范围搜索后非常少见且真正可复用的研究资产。**

---

## 9 结论：杀手图——Detection ⇏ Exclusion

```
UNCONDITIONAL MATHEMATICS
│
┌───────────┴───────────┐
│                       │
β-sensitive          structural
observables          identities
│                       │
▼
DETECTION
│
│  missing bridge（Rigidity Gap）
▼
┌───────────────────┐
│   INDEPENDENT      │
│   RIGIDITY         │
│   / COERCIVITY     │
└───────────────────┘
│
▼
EXCLUSION
│
▼
RH
```

**问号（RH）就是整个问题**——不是"我们还缺一个漂亮模型"。P1-P5 五轮的意义：逐层检查这个缺口能否被已有结构填上——**目前答案是：没有找到（不是：不存在）**。

### 冻结结论（三句——全文强度）
1. **Detection is unconditional; exclusion requires additional rigidity.**
2. **The audited positive-kernel constructions do not yield uniform coercivity.**
3. **No independent coercive mechanism was identified within the audited framework.**

### 四层主轴的最终定位
- **I. Unconditional structural layer**：A_min ⟹ F_U——RH 不进入基础公理。
- **II. Detection layer**：prime data ⟹ β-sensitive observables——**β can be detected**（不是 forced）。
- **III. Exclusion layer**：rigidity mechanism（independent + β-sensitive + uniform coercivity）——P5.9 在此。
- **IV. Rigidity Gap**：**Detection ⇏ Exclusion**——缺失的中间桥梁是 **independent rigidity / coercivity**——不是更多数据/更漂亮的表示。

本文不是"我们没证明 RH"的论文——而是一篇明确研究：**为什么一大类 RH 型结构能够稳定产生临界线信号，却无法自动产生排除机制**。

---

## 附录 A：成果降维表（详见 paper-dimension-reduction.md）
T1-T10 新定理 / O1-O5 新组织 / E1-E9 计算实验 / C1-C6 解释性框架。

## 附录 B：已审计路线清单（C1-D7 + P1-P5 + K1-K2 + THH/Arakelov）
正性（Weil/轨道/Li/de Branges/HB）/谱（HP/BK/Connes/散射）/迹/可实现性/算术几何/正定核/变分/能量/动力学/统计——全部收敛到 rigidity gap。
