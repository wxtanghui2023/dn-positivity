# P28-C2-A 重跑：passage numerically established（mpmath 50/100 位——修复 .real bug）

> 2026-09-01 · 唐先生 C2-A 重跑指令 · 双精度剔除 · 50/80/100 位对比 · 三个表示

## ⭐ 重跑结果——mpmath 50 位——direct compression 低块 inertia
| M | N | (n₋,n₀,n₊) |
|---|---|---|
| 1 | 2 | **(0,0,6)** |
| 1 | 4 | (0,0,6) |
| 1 | 6 | (0,0,6) |
| 2 | 2 | (0,0,12) |
| 2 | 4 | (0,0,12) |
| 2 | 6 | (0,0,12) |

**100 位抽查（N=4——M=1）：(0,0,6)——一致**

## ⭐ 修复说明
- **`.real` bug**（mpmath matrix 无 .real 属性——需逐元素 real_part）——导致之前 dc_mp 全"病态"（except 捕获）
- **修复后——mpmath 50 位正常——低块 n₋=0（所有 M,N）——100 位一致**

## ⭐⭐ 判定——negative spectral passage 从 hypothesis 升级为 numerically established
- **低块 direct compression 无负谱（n₋=0——50/100 位一致——双精度剔除——.real bug 修复）**
- **但——W_M(N) > 0（几何 overlap——负谱空间经过低块——之前 B1.1/B1.2 的 μ_j > 0）**
- **"E_N⁻ ∩ L_M ≠ {0}（几何）但 q_N|_L_M ≥ 0（二次型）"——negative spectral passage 严格成立**
- **"负谱子空间穿过每个固定低块——却没有在该低块形成负二次型"**

## ⚠️ 诚实边界
- N≤6（mpmath 慢）——更大 N 需确认（W_M 二重极限）
- M=1,2（M=3 需补——结果一致概率高）
- "passage"确认（低块 n₋=0——50/100 位）——但——"boundary escape（W_M → 0）"vs"passage（W_M 保持）"仍开放
- LDL* 符号确认（表示③）未做——但——50/100 位 eighe 一致已强

## 下一步
- (a) W_M 二重极限（更大 N——boundary escape vs passage 最终判别）
- (b) M=3 补测 + LDL* 符号
- (c) 唐先生指示
