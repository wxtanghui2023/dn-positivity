# P34-D2″(II)(III)：三量 + 双极限——(II) 显示 T_K 停滞（X=50000）——(III) 截断

> 2026-09-02 · 唐先生 (II)(III) 核心实验 · Does cancellation survive the joint (X,k) limit?

## (II) 三量（X=50000）——T_K 停滞！
| K | T_K | T̂_K = T_K/loglogX | C_K(ρ) |
|---|---|---|---|
| 10 | 0.0372 | 0.0156 | 0.0348 |
| 20 | 0.0334 | 0.0140 | 0.0351 |
| 40 | 0.0348 | 0.0146 | 0.0509 |

- **⭐⭐ T_K 随 K 不降反微升（0.0372→0.0334→0.0348——波动——非单调降！）——"L_B(X) = lim_K T_K(X)"在 X=50000 不 → 0（停滞 ~0.034——R3 风险！）**
- T̂_K 稳定（0.014-0.016）——C_K(ρ) 稳定（0.035-0.051）
- **⚠️ 但——D2' 数据（X=2000: 0.238→0.081——X=10000: 0.087→0.037）显示 T_K 随 K 下降——X 不同行为不同！——"X-uniformity"问题（T_K 的 K 行为依赖 X）**

## (III) 双极限——截断（未显示）
- L_A(K)（固定 K——X 方向）——未显示
- L_B(X)（固定 X——K 方向）——(II) 显示 X=50000 停滞（~0.034）
- K(X) 路径（log X/sqrt(log X)/X^0.3）——未显示

## ⭐ 初步判定
- **T_K 的 K 方向行为依赖 X（X=2000/10000 下降——X=50000 停滞）——"X-uniformity"障碍——"uniform tail（sup_X T_K → 0）"严重存疑**
- **"L_B(X) = lim_K T_K(X)"——X=50000 停滞 ~0.034——"R3（uniform-tail obstruction）"风险——但——需 (III) 完整（L_A/L_B 比较——K(X) 路径——联合极限）**

## ⚠️ 诚实边界
- (III) 截断（输出进程结束）——需补
- Kmax=100——X≤10⁶——L_A/L_B 是有限截断估（非真极限）
- "T_K 停滞 vs 慢降"——X=50000 的波动（0.037→0.033→0.035）——需更多 K 点确认

## ⭐ 状态（唐先生）
**P34-D: partial operator cancellation, uniform tail OPEN**
- 三件扎实：finite-rank obstruction（n₋≤O(1)）——endpoint obstruction（a_k 无 canonical cutoff limit）——partial cancellation（ρ≈0.05-0.09）
- 缺最后一层：Does cancellation survive the joint (X,k) limit?——D2″ 真正终点
- 标签：R1-O OPEN——R3 OPEN——canonicalization obstruction 强候选但未封口

## 下一步
- (a) 补 (III)（L_A/L_B 完整——K(X) 路径——联合极限判定）
- (b) 唐先生指示
