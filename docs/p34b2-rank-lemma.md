# P34-B 升级：B7 finite-rank inertia lemma——rank-2 Gram deformation

> 2026-09-01 · 唐先生 P34-B 关键升级 · 结构性上界（非数值现象）

## ⭐ B7 finite-rank inertia lemma
**For the prime kernel K_pq = (log p + log q − 2)cos(log p − log q)——every finite prime truncation satisfies n₋(K) ≤ 2. Consequently, no infinite-dimensional uniformly negative sector can arise from this kernel under any nested prime embedding.**

**证明**：
- C_pq = cos(x_p − x_q) = cos x_p cos x_q + sin x_p sin x_q——**C = UU^T（U 两列——[cos x, sin x]）——rank C ≤ 2**
- K = DC + CD（D = diag(x_p − 1)）= DUU^T + UU^TD
- **n₋(DUU^T + UU^TD) ≤ rank U ≤ 2**（标准有限秩惯性事实）

## ⭐ 数值验证
| pmax | n（素数） | rank(C) | n₋(K) |
|---|---|---|---|
| 100 | 25 | 2 | 2 ✓ |
| 400 | 78 | 2 | 2 ✓ |
| 1500 | 239 | 2 | 2 ✓ |
| 3000 | 430 | 2 | 2 ✓ |

- ||C − UU^T||_F = 5.6e-15（rank-2 分解确认）
- ||K − (DUU^T+UU^TD)||_F = 4.7e-14（K = DC+CD 确认）
- **变体（D1=x−1——D2=x²−4——D3=1−x/2——D4=x−2）：全部 n₋ ≤ 2——"有限秩符号变形"普遍**

## ⭐⭐ 关键结论
- **n₋=2 是结构性上界（rank ≤ 2）——不是数值现象**
- **dim E_{(−∞,−ε)}(K_B7) ≤ 2 ∀ε>0——任何阈值以下负谱维数最多 2——无 uniform infinite sector（结构排除）**
- **ε₁ 变深（−4.2→−20.5→−30.8）不矛盾：negative depth ↑ ⇏ negative dimension ↑——谱值可向 −∞ 漂移而负惯性维数保持有限**
- **与 P28-P33 互补**（P28-P33：很多浅负方向 margin→0——B7：少而深的负方向维数有限）

## ⭐ P34-B 真正成果——新筛选原则（Gate 2'：Structural-rank audit）
**对每个 prime-side candidate 先问：kernel 的有效 rank/factorization 是多少？**
- K = DA + AD 或 K = Σ_k(D_k A_k + A_k D_k)——A_k ⪰ 0 rank < ∞ → 有限负惯性上界

**搜索空间压缩**：
- ① translation invariant → positive/trivial（P34-A）
- ② finite-rank nontranslation → finite negative core（P34-B——B7）
- ③ **infinite-rank + sign-indefinite + arithmetic-specific → Problem II 候选（需找！）**——且避免 Weil explicit-formula 包装

## 下一道门槛（Problem II 候选的精确定义）
```
K^(P) independent of zeros
rank K^(P) = ∞
K^(P) genuinely sign-indefinite
n₋(K_N^(P)) → ∞
且存在可能的 uniform negative sector
```
**若候选在前两步就满足 rank < ∞——无需继续数值谱扫描——它从结构上已经不可能解决 Problem II。**

## 分叉状态（B7）
- B7 → "finite negative core"（分类②）——非 moving-edge——非 Problem II 候选
- **P34-B 成果不是"B7 失败了"——而是发现新筛选原则：有限秩符号变形的负性至多 finite persistent core——要 Problem II 候选必须 infinite-rank arithmetic kernel**

## 下一步
- (a) 第三类候选（infinite-rank + sign-indefinite + arithmetic-specific）——构造搜索
- (b) Gate 2' 框架的正式化（structural-rank audit 文档）
- (c) 唐先生指示
