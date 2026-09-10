# L2 分歧 bookkeeping —— **权威状态文件**（取代早前数份散落文档）

**建立时间**：2026-09-10 20:28（真实时间；早前文档中的时刻标注不可靠，已不再使用）
**取代**：`ramification-lift-dynamics.md`、`layer2-bookkeeping-fix.md`、`round2-index-status.md`
（该三份保留作历史，但**已 superseded**；只认本文件）

---

## §1 已确立（可复现，有脚本 + 自检）

**结构**：$K=\mathbb Q(\sqrt2)\subset K'=\mathbb Q(\delta),\delta^4=2\subset L=\mathbb Q(\delta,i)$（$L$ 为 $K'$ 的 Galois 闭包，$G=D_4$）

### 1.1 Layer 1（局部数据）—— 精确
```
δ⁴=2｜N_{K'/Q}(δ) = −2 ⟹ (δ) 是 2 上唯一素理想
(2) = (δ)⁴ ⟹ e=4, f=1, v_{p₀}(δ)=1, v_{p₀}(2)=4
𝔇_{K'} = (4δ³) ⟹ v_{p₀}(𝔇_{K'}) = 2·4 + 3 = 11 ⟹ |D_{K'}| = 2¹¹ = 2048
TOWER：6（= 2·v_{(√2)}(𝔇_K)，𝔇_K=(√2)³）+ 5（𝔇_{K'/K}=(2δ)=(δ)⁵）= 11 ✓ 精确闭合
LIFT MAP：r₀ = 3 ⟶ r₀' = 3·e((δ)|(√2)) = 6（奇→偶）✓
```
**脚本**：`scripts/ramification_lift_dynamics.py`（⚠️ 其内部一处范数显示 bug 已注明：$4\delta^3$ 曾被误算为 $4\delta\cdot\delta^3$）

### 1.2 判据校准（$F=\mathbb Q_2(\zeta_8)$，真值 $d=8$）—— 关键，且**这才是正确做法**
```
同一判据 G_i={σ : min_{e∈B} v(σ(e)−e) ≥ i+1}、同一对象，只换基：
  极大基 B = O_F = {1,x,x²,x³}      ⟹ i_G = (σ₃:2, σ₇:2, σ₅:4) ⟹ |G_i| = 4,4,2,2,1 ⟹ d = 8  ✓ 与真值一致
  非极大基 B = {1,i,√2,i√2}          ⟹ i_G = (4,4,6)          ⟹ |G_i| = 4,4,4,4,2,2,1,1 ⟹ d = 14 ✗ 膨胀
```
$$ \boxed{\text{index trap}:\ \text{基不张成 }O\ \Longrightarrow\ i_G\ \text{偏大}\ \Longrightarrow\ G_i\ \text{偏大}\ \Longrightarrow\ d\ \text{膨胀}} $$
**三栏表（$F$）**：$|G_i|=4,4,2,2,1$；$\varphi(i)=0,1,1.5,2,2.25$；lower breaks $\gamma_1=1,\gamma_2=3$；upper breaks $\varphi=1,2$ 皆整数 ⟹ **Hasse–Arf ✓**
**脚本**：`scripts/ramification_bookkeeping_fix.py`

### 1.3 关于 $L$：**已确立一条不等式**
```
存在【7 个】半整数元素 (1/2)Σ_{j∈S} e_j 是整的 ⟹ [O_L : Z[δ,i]] > 1
⟹ Z[δ,i] 【不是】极大阶 ⟹ d(L/Q₂) < 30
```
**整性判据（已修正并验证）**：正则表示特征多项式整系数 ⟹ $1/2\mapsto$False ✓，$\delta/2\mapsto$False ✓，$1\mapsto$True ✓，$0\mapsto$True ✓
**脚本**：`scripts/round2_index.py`

### 1.4 Tower 记录
| 层 | $e$ | $f$ | $d$ | Galois | 备注 |
|---|---|---|---|---|---|
| $\mathbb Q_2(\sqrt2)/\mathbb Q_2$ | 2 | 1 | 3 | 是 | $\lvert G_i\rvert = 2,2,2,1$（$i_G(\sigma)=3$）✓ |
| $\mathbb Q_2(2^{1/4})/\mathbb Q_2$ | 4 | 1 | 11 | 否 | 闭包为 $L$（§1.1 ✓） |
| $L/\mathbb Q_2$ | 8 | 1 | **$<30$，真值未定** | 是 | 需 $O_L$ |

---

## §2 已**撤回**的说法（连同撤回原因；不要再被引用）
| 撤回的说法 | 原因 |
|---|---|
| $d(L)=50$ + filtration $8,8,8,8,8,8,4,4,2,2,1$ | 用了**非极大基** $\mathbb Z[\delta,i]$（index trap）⟹ 膨胀；已作废 |
| $d(L)=22$ + "引用"的 $D_4$ filtration | 我先前**错误断言** $L/K'$ 非分歧；实际 $e(L/K')=2$、相对 different $=(2i)=\mathfrak q^8$ |
| $|\mathrm{disc}\,\mathbb Q(\zeta_8)|=2^{10}=1024$ | 真值 $2^8=256$（$\mathrm{disc}(x^4+1)=4^4N(\zeta)^3$；$\mathbb Z[\zeta_8]$ 极大）⟹ 我据此做的"路线 C 标定"无效 |
| $d(L)=30$ / index $=1$ | 由两个 bug 造成：半整数坐标 $\mathrm{int}()$ 截断（255/255 假"整"）、Newton 恒等式下标配错 ⟹ 作废 |
| index 的**任何具体数值** | 格扩大取基仍有 bug（跑出 $1/8$，对 index 不可能）⟹ **不声称任何一个值** |
| "路线 C 通过两个测试例" | 撤回：其中一个测试例用的 $|D|$ 本身就是错的 |

---

## §3 未决（诚实清单）
```
① O_L 的明确对象与 index 的【数值】
② d(L/Q₂) 的真值（已知 23 ≤ d < 30：下界 2·11 + (e−1)=1，上界 <30 由 §1.3）
③ L 的正确 ramification filtration 与 i_G
④ F 的 uniformizer-法 与 basis-法 在个别 σ 上不一致的 bookkeeping 细节（已记录未解）
```

## §4 待修的工具（第三个 bug）
```
scripts/round2_index.py 的【格扩大取基】步骤错误 ⟹ index 出现 1/8
正确做法：对 15 个生成元（8 旧基 + 7 整性半元素）做真正的整数 HNF，迭代至稳定
（这是唯一不依赖 conductor-discriminant 的路径；若发现 Z[δ,i] 连候选 order 都不是，则先修 order 对象）
```

## §5 纪律与边界
```
· Layer 3/4（双尺度守恒 + 递推 r↦(r−1)/2 ⟹ 1/2 为不动点）**仅为结构猜想**，本轮及前轮均未建立
· 未做任何 GPS 审计；未声称临界指数；未声称与 ζ 连接
· 未为闭合 26/30 调整任何 filtration ✓
· 新增纪律（本轮起生效）：
   (i) 任何数值进文档前，必须由脚本产出且脚本自带"已知答案"自检
   (ii) 文档中每个数字标注【验证】/【引用】/【猜想】三态之一
   (iii) 每轮只更新本文件（不新建散落文档）；历史留在 git
   (iv) 回信只给结论（≤15 行），细节在本文件
```
