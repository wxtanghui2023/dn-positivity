# E1：AFAC 收口 + "信息损失几何"路线的结构审计（**纯推导，未计算**）

**依据**：唐先生 AFAC 终审 + 新路线（不可逆性 → 时间；$\Pi_A/\Pi_M$；canonicality 原则；$\mathscr D,\Pi,\mathfrak B$；$\lambda$ 中性模式）｜**约束**：不输入 $1/2$；不构造模型｜**L2 未动**

---

## §1 AFAC：同意收口【推导 + registry】
$$\mathrm{AFAC}\subset\{\text{additive–multiplicative incidence}\}\qquad B_n\bigl((a,b),(d,e)\bigr)=\mathbf1_{a+b=de}$$
"曲率"只能是 $B_n$ 的秩/kernel/cycle/singular value 再加工 ⟹ **无新选择机制** ✓
【已注册·本项目】incidence / 加法组合 / factor graph 类（同族：三体符号、Rédei、$K_3$、hyperbola）
$$\boxed{\text{AFAC-v1：CLOSED（同意）}}$$

## §2 新路线的结构（引用要点）
```
不可逆性 → 方向（时间）；用【消元/投影】而非 +,× 生成非交换
canonicality 原则 = "保留所有未来仍可恢复的信息"
客体：𝒟(n) = 有限算术描述集，含信息偏序；𝔅 = ∩_R Im Π^R = 不可约信息核
选择机制：Π(v)=λv 且 |λ|=1 为 information-neutral mode
目标：𝔅 的 intrinsic 维数产生非平凡连续谱；且 ΔE(s) = C(t)(σ−1/2)² 型 forcing
```

## §3 ⭐ 核心审计：**canonicality ⟹ 落在显式公式对象上**（三重困境）
### (i) canonicality 原则本身就是"取极限"
"保留所有【未来仍可恢复】的信息"⟹ $\Pi$ 的核 = 被所有未来描述同时识别的对
⟹ 商 $\mathscr D/\Pi$ = **所有描述都能分解通过的最粗商** ⟹ 这就是**逆极限**（集合论意义上的相容族/对角像）
$$\boxed{\text{他的 canonicality 原则}\Longrightarrow\ \text{lim←（描述系统）}\ \Longrightarrow\ \text{触发 §22 的 "profinite completion" 死因}}$$
### (ii) 若强行不让它是极限（$\mathfrak B=\cap_R\operatorname{Im}\Pi^R$），则分两种
```
𝒟 有限 ⟹ 终像 = 周期点集（有限）⟹ **无连续谱** ⟹ §23 的要求（非平凡连续谱）失败 ✗
𝒟 无限且迭代 Π ⟹ 这就是【动力系统】⟹ transfer operator / 谱 ⟹
    · 唐先生此前明确禁止 T_R 成为 transfer operator/dynamics ✗
    · 且 registry 中 dynamical zeta 类已判死 ✗
```
### (iii) §14 的 $|\lambda|=1$ 判据需要**范数/Hilbert 结构** —— 这正是他自己 §15 列的死因
```
"中性模式"要求先有一个 canonical 范数/度量；纯算术（ℕ,+,×）中没有 canonical 范数
⟹ 与 B4d/D3 的 "generic vs arithmetic" 同一堵墙：选范数 = 选 α ⟹ 人为 ✗
```

## §4 ⭐⭐ 最锋利的一点：canonical 极限对象的**具体形态**（本院已定位）
算术有限描述的两类不变量：
```
(1) 同余/congruence（ℤ/n 型）⟹ 极限 = **profinite completion Ẑ**（无 archimedean 信息 ⟹ β-盲）
(2) archimedean（大小/高度）⟹ 给出 ℝ_{>0} 上的 profile
⟹ 全体描述的相容族 ≅ **Ẑ × archimedean profile** ⟹ 即 **adèle/profile 对象**
```
$$\boxed{\text{而该对象的 Mellin 变换【正是】Riemann 显式公式（} \sum_{\rho}\hat h(\rho)\ \text{一侧）}}$$
$$\boxed{\Longrightarrow\ \text{canonical 化的 }\mathfrak B\ \text{≅ 显式公式对象} \Longrightarrow \text{按本项目 registry：显式公式类已判死（}\beta\text{-盲或 RH-等价）}}$$
**但有一点必须先承认**：该路线**正确地解释了 Mellin 参数为何不可避免**（§18 的"尺度粗粒化 ⟹ 特征模态 ⟹ $k^{-s}$"是对的 ✓）
—— 结论不是"路线无意义"，而是：**它重新推导出了经典框架，而非逃出它** ✓

## §5 唯一逃生口（诚实标注，无候选）
```
需要描述系统的"不变量"【既非 congruence、也非 archimedean】—— 第三种不变量
已检查的自然候选：p-adic 解析不变量（仍属 adelic 类 ✗）｜entropy/计数（registry 判死 ✗）｜
                 描述复杂度（entropy 类 ✗）｜动力/遍历不变量（dynamical 类 ✗）
⟹ 无候选（结构性阅读，非定理）
```

## §6 方法论要点（重要）
```
唐先生 §24 要"定义 𝒟, Π, 𝔅 并证明是否非平凡"。
但生死点【不在数值】而在 **canonicality**：一旦我们【选定】一个 Π，就已落入他 §15 的第一个死因。
⟹ 故"最小模型计算"测不了关键点（它只能给出"对某个选定 Π 的结论"）⟹ 这一步必须结构性判定，
   而结构性判定的结果就是 §3–§4（canonical ⟹ 极限 ⟹ profinite/adelic ⟹ 显式公式）
```

## §7 结论与边界
```
· AFAC-v1：CLOSED ✓（同意）
· 新路线：其 canonical 化落在已被定位的对象上（profinite / adelic-profile ⟹ 显式公式）⟹ 判死
   并且三重困境（极限 ✗ / 有限无连续谱 ✗ / 迭代即 dynamics ✗）与 |λ|=1 需范数 ✗ 独立支撑该结论
· 有价值的副产品：该路线【正确解释】了 Mellin 的不可避免性（§18）——这解释了一个长期观察
· 【未做】未计算（并给出理由：测不了关键点）；未输入 1/2；未构造模型；L2 未动；未声称与 ζ 连接
· 边界：以上为"已识别不变量类别"内的结论，非全称不可能
```

## §8 提交链
```
df9225c F/H 审计 → 本篇（AFAC 收口 + 信息损失路线审计）
```
