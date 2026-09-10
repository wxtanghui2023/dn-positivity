# 数域版 A′：迹配对 / 分歧 filtration / $\sqrt{|D_K|}$（**构造性，未审计**）

**日期**：2026-09-10 20:15+ ｜ 依据：唐先生定位（A′ 在 transport 层构造性成功；**算术选择性 + ζ 接口 = OPEN**；他去推进数域化，我做配套构造）｜ 代码 `scripts/number_field_duality.py` ｜ 输出 `/tmp/nf_duality_out.txt`

---

## §0 定位（唐先生）
$$\boxed{\text{守恒} + \text{交换} + \text{canonical filtration} \Longrightarrow \text{同一 compatibility law 跨层传播}}$$
$$\mathcal T_j(\Lambda)=\Lambda\cap G[p^j]\ \Longrightarrow\ |\mathcal T_j(\Lambda)|=p^j=\sqrt{|G[p^j]|}\ \text{是【同一顶层对象的连续投影】}$$
**正面回答了 A′.4** ✓；**当前缺口已从"有没有 transport"变成**：$\boxed{\text{为什么算术结构会选择 cyclic locus}}$ **以及** $\boxed{\text{怎样让 pairing + filtration 本身具有算术特异性}}$
**本轮仍不做审计**；当前状态：
$$\boxed{A'=\text{constructively successful at the transport level},\quad\text{arithmetic selection }+\ \zeta\ \text{interface}=\text{OPEN}}$$
**三部件替换（唐先生）**：
| 有限侧 | 数域侧 |
|---|---|
| 有限辛配对 | 迹配对 $\operatorname{Tr}_{K/\mathbb Q}(xy)$ |
| $p$-power filtration | 分歧／素理想 filtration |
| $\sqrt{|G|}$ | $\sqrt{|D_K|}$（以及 $\mathfrak D_K^{-1}$） |

---

## §1 ⭐ 核心：自对偶**强制** $\sqrt{|D_K|}$（不是放进去的）
```
(C1 经典) 迹配对下理想 a 的对偶：  a* = a^{-1} 𝔇_K^{-1}     （𝔇_K = 不同）
自对偶 a = a*  ⟹  a² = 𝔇_K^{-1}  ⟹  a = 𝔇_K^{-1/2}  ⟹  N(a) = |D_K|^{-1/2}
```
$$\boxed{\text{平衡对象的尺度}=\sqrt{|D_K|}\ \text{是【自对偶条件的定理级后果】——与 A′ 的 }|\Lambda|=\sqrt{|G|}\ \text{同构}}$$

## §2 ⭐⭐ 算术选择性**是真的**（本轮的正面答案）
$$\boxed{\text{平衡存在}\iff\Big(\forall\mathfrak p:\ v_{\mathfrak p}(\mathfrak D)\ \text{为偶}\Big)\wedge\Big(\mathfrak D^{-1}\in Cl(K)^2\Big)}$$
**局部规则（经典）**：驯分歧 $\mathfrak p$：$d(\mathfrak p)=e-1$ ⟹ 需 $e-1$ 偶 ⟹ **$e$ 为奇**；野分歧（$2\mid e$）：需逐个核验
**二次域实算表**（按经典规则组装）：
| $d$ | $D_K$ | $v_{\mathfrak p}(\mathfrak D)$ | 全偶？ | 平衡存在？ |
|---|---|---|---|---|
| **−1** | **−4** | **{2: 2}** | **True** | **True** |
| −2 | −8 | {2: 3} | False | False |
| −3 | −3 | {3: 1} | False | False |
| 2 | 8 | {2: 3} | False | False |
| 3 | 12 | {3: 1} | False | False |
| 5 | 5 | {5: 1} | False | False |
| 6 | 24 | {2: 3, 3: 1} | False | False |
| −5 | −20 | {5: 1} | False | False |
| 7 | 28 | {7: 1} | False | False |
| 13 | 13 | {13: 1} | False | False |
| −7 | −7 | {7: 1} | False | False |
| 10 | 40 | {2: 3, 5: 1} | False | False |
$$\boxed{\text{二次域中【只有 }\mathbb Q(i)\text{ 通过】}（v_{(1+i)}(\mathfrak D)=2\ \text{偶}）}$$
**$\mathbb Q(i)$ 显式验证**：
```
𝔇 = (1+i)² = (2i)  ⟹  𝔞 = 𝔇^{-1/2} = (1+i)^{-1} = (1−i)/2
𝔞² = ((1−i)/2)² = (−2i)/4 = −i/2 = (2i)^{-1} = 𝔇^{-1}  ✓ 自对偶成立
N(𝔞) = (1²+1²)/4 = 1/2 = |D_K|^{-1/2}（|D_K| = 4，√|D_K| = 2）✓
```
**二次域之外的一例**（引用经典事实）：循环三次域、conductor $f=7$：$D=f^2=49$，$(7)=\mathfrak p^3$ ⟹ $e=3$（驯，$7>3$）⟹ 分歧指数 $=e-1=2$ **偶** ⟹ **通过**，$N(\mathfrak a)=1/7$（且 $\sqrt{|D|}=7\in\mathbb Z$）

$$\boxed{\text{与有限辛侧对比：Lagrangian 对【一切】}n\text{ 都存在（通用）；数域侧平衡是被【算术条件选出】的（非通用）}}$$
**⟹ 这正面回答了唐先生缺口①的一个版本：算术结构确实会"选择"，且选择律是显式的：**
$$\boxed{\text{驯分歧指数为奇} + \text{野}(2)\text{ 指数为偶} + \mathfrak D^{-1}\ \text{为平方类}}$$

## §3 失败意味着什么：$\sqrt{\mathfrak D}$ 不在 $K$ 内 ⟹ **2-cover 现象**
```
当某 v_p(𝔇) 为奇：K 内【不存在】𝔞 使 𝔞² = 𝔇^{-1}
⟹ 平衡条件只能在【2-cover / 2-descent】中满足
⟹ 障碍类 = 𝔇 在 Cl(K)/2Cl(K) 中的类（+ 局部奇偶数据）—— 这是一个【算术不变量】
⟹ 结构性识别：此处的"1/2"恰是一个 2-cover 现象（平方根在算术中天然属于 Kummer/2-下降）
```
⚠️ 这是**结构性判断**（非定理）：须验证"在 2-cover 中平衡确实存在"，本轮**未做**。

## §4 filtration 类比（构造性，未验证）
```
p-power filtration  →  分歧 filtration（高阶分歧群 / different 指数向量）
transport 𝒯_j        →  限制到分歧 filtration 的第 j 层（构造性类比）
```
**待做**：检查是否存在"同一 compatibility law 跨分歧层传播"（这是把"通用机器"变"算术机器"的关键一步）

## §5 诚实边界
```
· §0 的定位、状态、三部件替换表、以及"本轮仍不做审计"——唐先生指定
· §1 的自对偶→√|D| 推理、§2 的选择律组装与二次域表、§3 的 2-cover 识别、§4 的 filtration 类比——小灵本轮
· 【引用经典，非我证明】：（C1）迹配对下 𝔞* = 𝔞^{-1}𝔇^{-1}；（C2）驯 d=e−1、野 d≥e；（C3）循环三次域 conductor f ⟹ D=f²
· 【计算】：§2 的二次域表（按 (C2) 规则组装）+ ℚ(i) 的显式验证（𝔞²=𝔇^{-1}、N(𝔞)=1/2）——这两条是逐步可核的算术
· ⚠️ 未验证：§3 的 2-cover 存在性；§4 的 filtration transport；"只有 ℚ(i)" 是基于表内 12 个域与上述规则，**非穷尽证明**
· ⚠️ 仍保留在记录中：两项过程/纪律失误（pkill 自伤；层维度表照抄公式）——按唐先生指示，作为构造阶段的完整性纪律
· 本轮【未做审计】：未过 GPS 门、未反调参、未 Gate V/V-b；未声称临界指数；**未声称与 ζ 的连接**
```

## §6 新的 OPEN
```
① 2-cover 版本（Cl(K)/2Cl(K) 之外）是否给出"同一 law 跨层传播"？
② ζ 接口：𝔇、Cl(K)、分歧数据已出现在类数公式/Dedekind ζ 的分析结构中——但【本轮不声称】任何连接
③ 选择律的完整形式（把 tame/wild/平方类三条合并为一条 canonical 判据）
```

## §7 提交链
```
49104f1 A′ 跨层 transport → 本篇（数域版 A′：√|D| 定理级强制 + 算术选择律 + 2-cover 识别）
```
