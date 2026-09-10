# B4b：候选"第二对象"筛选（为下一轮目标 *Artin profile → A′ 双尺度* 备料）

**依据**：唐先生——B4=positive structure；不做 B5；下一轮目标 = 补一个**天然第二对象**使 profile 的"长度×高度"成为**可交换双尺度**
**约束**：不放入 $1/2$、不放入递推、不做 GPS 审计｜**L2 未动**｜`scripts/B4b_second_object.py`

---

## §1 已确认的保留事实（B4，唐先生点出）
$$C_{\rm tot}(H)=|G|-\frac{|G|}{|H|}\ \Longrightarrow\ \frac{|G_i|}{|G|}\cdot|G|\Bigl(1-\frac1{|G_i|}\Bigr)=|G_i|-1\ \Longrightarrow\ \sum_i(|G_i|-1)=24$$
**24 的 filtration–conductor 恒等式本身是 profile 的推论**，不是额外输入 ✓

## §2 ⭐ 新核验的候选（d）：自对偶伴随 $\rho\otimes\rho$
**两个 profile（同 conductor，不同形状）**：
| 层 | $\rho$（dim 2）codim | $\rho\otimes\rho$（dim 4）codim |
|---|---|---|
| $(-1,0]$（边界，$G_0$） | 2 | 3 |
| $(0,1]$（$G_1$） | 2 | 3 |
| $(1,2]$（$\langle\sigma\rangle$） | 2 | 2 |
| $(2,3]$（$\langle\sigma^2\rangle$） | 2 | **0** |
$$\int C_\rho=8=a(\rho),\qquad \int C_{\rho\otimes\rho}=8=a(\rho\otimes\rho)\ \Longrightarrow\ \textbf{同 conductor} = 8,\ \textbf{不同 profile：}(2,2,2)\ \text{vs}\ (3,2,0)$$
**分解（四个内积全部核验）**：
$$\rho\otimes\rho=\mathbf 1\oplus\chi_{(0,1)}\oplus\chi_{(1,0)}\oplus\chi_{(1,1)}\qquad(\langle\chi^2,\chi_i\rangle=1\ \text{四个皆}\ 1,\ \langle\chi^2,\chi_\rho\rangle=0)$$
$$\Longrightarrow\ a(\rho\otimes\rho)=a(\mathbf 1)+a(\chi_{01})+a(\chi_{10})+a(\chi_{11})=0+2+3+3=8=a(\rho)$$
【意义】$\rho\otimes\rho$ 是**中心层（非阿贝尔信息）与三个阿贝尔角色相会**的天然对象 ✓

## §3 四个候选"第二对象"的筛选结果
| 候选 | 状态 | 依据 |
|---|---|---|
| (a) 局部互反 / 单位 filtration $U^v$（Herbrand $\psi=\varphi^{-1}$） | **排除** | 只覆盖阿贝尔部分；且该配对在本例**退化**（B2：rank 1） |
| (b) Kummer 类 + Hilbert 配对 | **排除** | B2 已核验退化（radical $=\mathrm{span}\{[2]\}$） |
| **(c) Kummer 2-cover $K\to K'=K(\sqrt{\sqrt2})$** | **活跃候选** | 早前已构造并核验；是挂在同一分歧数据上的**第二算术对象** ✓ |
| **(d) $\rho\otimes\rho$（中心层的自对偶伴随）** | **活跃候选** | §2：同 conductor、不同 profile；中心×阿贝尔相会之处 ✓ |
$$\boxed{\text{结论：活跃的天然第二对象 = (c) 2-cover 与 (d) }\rho\otimes\rho;\ \text{(a)(b) 在本例被 B2 的退化性排除}}$$

## §4 边界
```
· 计算级：§2 的两个 profile 与积分（自检：∫C_ρ=8 ✓、∫C_{ρ⊗ρ}=8 ✓）；四个内积分解 ✓
· 引用（非我证明）：Herbrand 逆函数与局部互反的 u↔v 对应；Artin 诱导/conductor 的可加性 a(⊕)=Σa
· 结构性判断：§3 的筛选（(a)(b) 排除基于 B2 的已核验退化；(c)(d) 为活跃候选）
· 【未做】未放入 1/2；未放入递推；未审计；L2 未改；未声称与 ζ 连接
· 注意：a(ρ⊗ρ)=a(ρ) 在本例成立，**不声称一般性**
```

## §5 提交链
```
61e7e4b B4 → 本篇（B4b：第二对象筛选 + ρ⊗ρ 新核验）
```
