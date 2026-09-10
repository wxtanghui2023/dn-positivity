# B-PRE2：非截断、非人为非结合律来源审计

**日期**：2026-09-10 14:50+ ｜ 依据：唐先生 B1–B5 预筛 + 小灵执行 ｜ 预算：纸面

---

## 第一部分：预筛登记（唐先生）

**筛选条件**：$\boxed{\text{canonical}\cap\text{non-associative}\cap\text{non-truncation}\cap\text{scale-complement compatible}}$
| 类别 | 非结合 | 非截断 | 非人为 | $\sqrt X$ 对合 | 判定 |
|---|:-:|:-:|:-:|:-:|---|
| B1 gcd/lcm 混合 | ✓ | ✓ | ✓ | ✗ | **杀**（三体 defect 有内容，但 **scale involution 无来源**） |
| B2 Farey/mediant | ✓ | ✓ | ✓ | ✗ | **杀**（非结合来自 projective normalization；且天然给加法比例几何 $(a+c,b+d)$ 而非乘法尺度） |
| B3 归一化卷积 | ✓ | ✓ | ✗ | — | **杀**（结合内核 + 人为 canonicalize ⟹ **假 defect**；与 projection 陷阱同族） |
| **B4 三因子天然组合路径** | ? | ✓ | ✓ | ? | **核心活口** |
| B5 local/global 原生双组合 | ? | ✓ | ✓ | ? | **待构造**（CRT 封闭／p-adic local-global 已 NO-GO／holonomy 已关 ⟹ 须"两种原生组合"） |

**搜索问题改写（唐先生）**：
$$\boxed{\text{什么天然算术三体关系具有两种不可等价的组合路径？其 defect 不来自截断/归一化/投影/holonomy？且其中两个尺度天然构成 }H,\ X/H？}$$
**第一死亡测试**：$\boxed{\Omega(a,b,c)\ \text{能否在不引入 }X,H\text{ 的情况下先独立存在？}}$（不能 ⟹ 尺度被人为塞入 ⟹ 杀）
**次测**：$\Omega(H,X/H,\cdots)\stackrel{?}{=}\pm\Omega(X/H,H,\cdots)$；**末测**：是否产生二阶量（非退回 additive convolution / 双曲线）

---

## 第二部分：小灵执行

### 2.1 ⭐ B2 ⊆ B3（证明级统一）
```
在【齐次坐标】上 mediant 就是向量加法： (a,b)⊕(c,d)=(a+c,b+d) —— **这是结合的**
⟹ B2 的非结合性【全部】来自【约化/归一化】这一步（化到最简分数）
⟹ B2 与 B3 是【同一死因】（结合内核 + canonicalization）
```
$$\boxed{\text{B2}\ \subseteq\ \text{B3：两者的非结合性都可归属到【归一化】}}$$

### 2.2 ⭐⭐ 五重筛查门（本轮的通用产出）
任何候选非结合律，其 defect **不得可归属**于下列五类之一，否则杀：
```
S1 截断边界（truncation）           —— 已知：内容落双曲线跨项（N43）
S2 归一化/约化（normalization）     —— B2/B3；"结合内核 + canonicalize" = 假 defect
S3 投影（projection）               —— Connes/P49 已遇
S4 holonomy/connection              —— Round 3 已关
S5 传输结构（transport of structure）—— 若 a★b=φ⁻¹(φ(a)·φ(b)) 则★【自动结合】⟹ 杀
```
**⟹ 候选必须是【非可传输（non-transportable）】的真正 loop**

### 2.3 ⭐⭐ B4 的预注册分叉预测（小灵）
```
观察：所有 canonical 算术运算只活在两层之一：
  ① 整除/素支撑层（divisibility / prime-support）⟹ **Sym(ℙ)-协变** ⟹ 无绝对尺度
     ⟹ 拿不到 H↔X/H 对合（= B1 的死因）
  ② 加法/archimedean 层（additive / archimedean）⟹ 有尺度，但其对合来自【两范围边界】
     ⟹ 内容落 N43（= 最小 Ω 的死因）
```
$$\boxed{\text{预注册预测}:\ \text{B4 一旦具体实例化，将落入上述【二分】之一}}$$
**若下一轮实例化全部落入某支 ⟹ 有充分理由回头攻 A（唐先生的条件）**

### 2.4 B4 的两个具体测试对象（附继承风险，须诚实标注）
**对象 I：二元二次型的 Gauss 合成**
```
Gauss 合成仅在【等价类】上良定义 ⟹ 形式层面的合成【非结合】，其 defect = **ambiguity class**
天然对合：形式 ↦ 逆形式；不动点 = **ambiguous forms**（等价于自身逆的形式）
⚠️ 风险：ambiguous forms ↔ 判别式的平方根分解、且与 √D 的连分数周期纠缠
   ⟹ 很可能【继承】Euclid/连分数旧 NO-GO 与 N43 支
```
**对象 II：Hecke 代数的非乘性**
```
经典 Hecke 关系：T_m T_n = Σ_{d|gcd(m,n)} χ(d) d^{k−1} T_{mn/d²}
⟹ **两路径差异是 canonical 的**（不是 T_m T_n = T_{mn}）
⚠️ 风险：修正项依赖 **gcd(m,n)** ⟹ gcd 是 Sym(ℙ)-协变 ⟹ 落分支 ①（无绝对尺度对合）= B1 死因模式
```
**⟹ 两个具体对象【各自指向二分的一支】——正是 §2.3 预测的形态**（尚待完整审计）

### 2.5 本轮裁决
$$\boxed{\text{B4 仍是唯一核心活口，但已带上【预注册分叉预测】；两个候选对象各指向一支}}$$
```
· 若下一轮完整审计确认二分 ⟹ 回头攻 A（唐先生设定的条件）
· 若出现【不属于二分任一支】的 defect ⟹ 那才是 R_CS 的第一个真正新增量
```

## 第三部分：诚实边界
```
· 第一部分（B1–B5 表、搜索问题改写、三个测试）为唐先生本轮
· §2.1 的"齐次坐标下 mediant = 向量加法 ⟹ 非结合全来自约化"为【严格初等事实】
· §2.2 五重筛查门为小灵归纳（S1–S4 分别有既有登记支撑；S5 为初等事实）
· §2.3 的分叉预测为【结构性论证 + 预注册】，非定理；"所有 canonical 算术运算只活两层"为经验概括
· §2.4 的对象 I/II 均为【候选 + 风险标注】，**未经完整审计**；其"指向某支"是结构性预判
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 提交链
```
d86e843 R-CS-PRE1 + 最小 Ω → 本篇（B-PRE2）
```
