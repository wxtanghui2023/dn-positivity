> ⚠️ **SUPERSEDED**：本文件的权威版本为 `L2-RAMIFICATION-STATE.md`。
> 本文件保留作历史记录；其中的若干数值**已撤回**（见权威文件 §2），请勿引用本文件的数值结论。

# (a) round-2 index 判定：**状态报告（含未完成部分）**

**代码**：`scripts/round2_index.py`（含修正）、`scripts/index_final.py`｜**结论：未完成，不声称任何 index 数值**

## §1 已确立：判据正确 + 一个扎实的部分结果
```
整性判据（正则表示特征多项式整系数）修正后【验证正确】：
  charpoly_ints(1/2)     = False ✓（1/2 不整）
  charpoly_ints(delta/2) = False ✓
  charpoly_ints(1)       = True  ✓
  charpoly_ints(0)       = True  ✓
```
$$\boxed{\text{存在【7 个】半整数元素是整的} \Longrightarrow [\mathcal O_L:\mathbb Z[\delta,i]]>1 \Longrightarrow \mathbb Z[\delta,i]\ \text{【不是】极大阶} \Longrightarrow d(L)<30}$$
**⟹ 与 index trap 诊断一致**：$L$ 上我先前那个 $d=50$ 确系膨胀所致 ✓（且 $F$ 上的对照 $8$ vs $14$ 已独立演示该机制 ✓）

## §2 未完成：index 的**数值**仍不可信
```
用【8×8 子式 gcd】公式的稳健版本（index_final.py）跑出 index = 1/8  ← 对 index 而言【不可能】
⟹ 格扩大（row-reduction 取基）与 index 计算仍有 bug：我的"新基"步骤把格【缩小】了（除以 2 而未真正扩大）
⟹ **本轮不声称 index = 1、2、4 或 26 中的任何一个**
```
**已定位的 bug 清单**：
```
① 已修：轮循环中把半整数坐标 int() 截断 ⟹ 255/255 假"整"，index 假为 1（上一版的 30 由此而来，作废）
② 已修：Newton 恒等式下标配错（k·e_k = Σ_{j=1..k}(-1)^{j-1} e_{k-j} p_j）
③ 【仍存在】：格扩大的取基步骤错误（row-reduction 后直接取前 8 行，未取 HNF）⟹ index 出现 1/8
```

## §3 遵嘱确认
```
· 未为闭合 30 或 26 调整任何 filtration ✓
· 未开始②（conductor-discriminant）✓
· Layer 3/4 保持"结构猜想"，本轮未触碰 ✓
· 唐先生的关键原则已记录并在执行：**先定 O_L ⟶ 才能可靠算 i_G ⟶ 才能谈 G_i**
  ⟹ 而本轮证明：**O_L ≠ Z[δ,i]**（index > 1），所以 Z[δ,i] 上的 i_G 不可用 ✓
```

## §4 下一步（待批准）
```
(a1) 用正确的格算法重做：对 15 个生成元（8 个旧基 + 7 个整性半元素）做【真正的整数 HNF】，
     得到新基与 [new:old]，逐轮迭代至稳定 ⟹ 得 index（预计 2 的幂）
(a2) 或以【对偶/迹配对】方式求 index：index² = disc(Z[δ,i])/|D_L| 需要 |D_L|；而 |D_L| 又依赖②
     ⟹ 因此 (a1) 是唯一不依赖②的路径
⚠️ 若 (a1) 修正后发现 Z[δ,i] 连"正确候选 order"都不是（唐先生预设的第三种情况），
   则立即停在此处、先修整环对象，不再往下算
```
