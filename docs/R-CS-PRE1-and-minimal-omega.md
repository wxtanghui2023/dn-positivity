# R-CS-PRE1（存在性预筛）+ 最小 Ω 构造尝试

**日期**：2026-09-10 14:48+ ｜ 依据：唐先生本轮预筛 + 小灵执行 ｜ 预算：纸面/纯算术

---

# 第一部分：R-CS-PRE1 预筛登记（唐先生）

## X0 形式化
$$\boxed{\text{X0}:\ T\neq\text{group cocycle}（T_{X,Y}=\rho_Y(g)\cdot\rho_X(g)^{-1}）,\qquad T\neq\text{coboundary}（T_{X,Y}=\Phi_Y^{-1}\Phi_X）}$$
**判据**：前者的 $T_{Y,Z}T_{X,Y}=T_{X,Z}$ 只是群作用 cocycle 且闭环 $T_{X,X}$ 无记忆；后者是势函数差 ⟹ 亦为 coboundary。

## 预筛表
| 类型 | X0 | X4 | X5 | X6 | 状态 |
|---|:-:|:-:|:-:|:-:|---|
| 群作用 | ✗ | ✓ | ✗ | 可人为 | **杀** |
| coboundary | ✗ | ✓ | ✗ | 可人为 | **杀** |
| 可逆 transport（双射+严格合成+固定状态空间 ⟹ groupoid） | 高危 | ✓ | ✗ | — | **杀** |
| generic semigroup（$e^{tA}$） | △ | ✓ | ✗ | — | **杀** |
| Markov / 概率 | ✓ | ✓ | △ | — | **统计杀** |
| Euclid / continued fraction | ✓ | ✓ | △ | ✓ | **旧 NO-GO（Round 3）** |
| substitution / symbolic | ✓ | ✓ | △ | △ | **X5 不足** |
| ordinary category | ✓ | ✓ | ✗ | △ | **记忆不足**（严格 composition 仍路径无关） |
| **non-associative arithmetic transport** | ✓ | ✓* | **潜在** | **潜在** | **保留** |
| **arithmetic coarse-graining** | ✓ | ✓ | **潜在** | **潜在** | **保留** |

（*需特殊 composition law，不能普通 category 化）

$$\boxed{R_{\rm CS}\ \text{的搜索空间已压缩到两类：A. arithmetic irreversible coarse-graining}\ |\ \textbf{B. arithmetic non-associative transport}}$$

**两条关键防线（唐先生）**：
```
① 不得把 Ω=T_{YZ}T_{XY}−T_{XZ} 直接叫"曲率"（connection/holonomy 已关闭）
   ⟹ 用更弱的名字：**arithmetic composition defect**；仅在证明其 gauge-invariance/cocycle 型变换律后
      才考虑曲率类解释（否则把 Round 3 的和乐重新包装回来）
② X0 陷阱：不得用人为 projection（T_{X,Y}=P_Y U P_X）制造 defect
   ⟹ 那只是 projection/trace-class machinery（Connes/P49 已遇）
   ⟹ **projection 本身必须由算术生成，而非为制造 defect 引入**
```

## X6 的结构版本（唐先生 §8）
$$\boxed{T_{X,H\to X,X/H}=\mathcal J^{-1}T_{X,X/H\to X,H}\mathcal J,\qquad \mathcal J^2=1}$$
在 $H=\sqrt X$ 处 $H=X/H$ ⟹ $T_{\sqrt X}=\mathcal J^{-1}T_{\sqrt X}\mathcal J$
$$\boxed{\text{不是"最后发现最优尺度恰是 }\sqrt X\text{"，而是【传输律自身拥有 }H\leftrightarrow X/H\text{ 对称，不动点必然是 }\sqrt X】}$$

---

# 第二部分：小灵执行 —— 最小 Ω 构造尝试

## 1. 自然候选：**截断范围组合 defect**
```
尺度 X 处的算术状态取为【素数范围截断】𝓐_X（如 Π_{p≤X}(1−p^{−s})^{−1} 与 [1,X] 的算术数据）
组合律取【乘法】（截断狄利克雷级数之积）
```
$$\Omega(X,H):=\big(\text{截断到 }H\big)\circ\big(\text{截断到 }X/H\big)-\big(\text{截断到 }X\big)$$
**defect 的内容 = 跨范围乘积项**：$p\cdot q$（$p\le H<q\le X/H$ 之类）
⟹ 因为**截断 Euler 积/截断狄利克雷级数不相乘**：两个截断之积会生成跨范围的新系数

## 2. ✅ 正面发现：**它精确实现了 X6 的对合结构**
$$\text{范围对换}\ \mathcal J:(\text{范围}_1,\text{范围}_2)\longmapsto(\text{范围}_2,\text{范围}_1)\quad\Longleftrightarrow\quad H\longleftrightarrow \frac XH$$
$$\boxed{\text{跨项集合在 }H\leftrightarrow X/H\ \text{下不变 ⟹ }\mathcal J\ \text{是 canonical 算术对合}}$$
$$\boxed{\text{两个范围重合处}=H=\frac XH\iff H=\sqrt X\ \Longrightarrow\ \text{不动点正是 }\sqrt X\ \text{（内生！）}}$$
**⟹ X6 的对合半部分【可以被 canonical 实现】** ✓✓（且不需要事后代入 $H=\sqrt X$）
**这直接与 R3「尺度对合」残差接合**——对合本身找到了。

## 3. ⚠️ 但是 defect 的**内容**落回经典结构
```
跨范围乘积项 + "两个范围在 √X 处重合"的双计数结构
   = **Dirichlet 双曲线法**的记账结构（d ≤ √n 与 e ≤ n/d 两个范围，边界重合于 √n）
⟹ Round 2 已识别并登记为 **N43**
```
$$\boxed{\text{最小 }\Omega\ \text{的【形式】通过 X1/X2/X3/X6，但其【内容】= 双曲线跨项 = N43}}$$

## 4. ⟹ **"截断 × 乘法"整族的受限 NO-GO**
$$\boxed{\text{任何"尺度截断 + 乘法组合"的非结合 defect，其内容必为【两范围跨项】⟹ 双曲线型 ⟹ 被 N43 吸收}}$$
（本质原因：截断不相乘 ⟹ defect 必落在跨范围乘积上；而两范围结构 = 双曲线）
**⟹ 类 B 的最自然子族被受限关闭**

## 5. ⭐⭐ 本轮最有价值的产出：**把 X6 与 X5 分开**
$$\boxed{\text{X6 的【对合】半部分：可获得（范围对换，canonical，不动点 }\sqrt X\text{）✓}}$$
$$\boxed{\text{X5 的【内容】半部分：崩塌（落回双曲线跨项 N43）✗}}$$
**⟹ 诊断精确化**：
```
R_CS 缺的不是【尺度对合】（那是可用且 canonical 的：两范围对换），
而是【一个其 content 不是经典两范围跨项的 defect】
```
**⟹ 类 B 的逃逸条件（清晰形式）**：
$$\boxed{\text{须找一个非结合算术组合律，其 defect 不是两范围跨项}}\\
\text{（即不能是"截断 × 乘法"型；而任何【被定义的】非结合 T 又有"人为改造规则"的风险 ⟹ 双向夹逼）}$$

## 6. 类 A（coarse-graining）的现状（从预筛表）
```
X0/X4 通过，X5/X6 潜在；但唐先生已指出：普通 RG 的 fixed point 通常是【人为选择的动力学尺度】，
非算术 √X ⟹ 需 §2 的 Θ 结构把它钉在 √X
且类 A 容易退化为 entropy/density flow ⟹ 弱
本轮未对类 A 做构造（资源集中于 B）
```

## 7. 诚实边界
```
· 第一部分全部为唐先生本轮（结构性整理 + 定义）
· §1 的候选构造为小灵提出；"截断不相乘 ⟹ defect 落在跨范围乘积"为【严格的初等事实】
· §2 的"H↔X/H 对换是 canonical 对合、不动点 = √X"为【严格初等】
· §3/§4 的"内容 = 双曲线型 = N43"为【结构性识别】（跨项集合与双曲线的两范围结构同型），
  非定理；须注意：双曲线的对象是计数 Σd(n)，此处是截断乘积的系数——【结构同型】不等于【同一对象】，
  此点保留为待严格化
· §5 的"X6 可获 / X5 崩塌"为结构性诊断
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 8. 提交链
```
c6f04e1 R8-FL-Closure → 本篇（R-CS-PRE1 + 最小 Ω）
```
