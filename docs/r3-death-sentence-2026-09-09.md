# R₃ 死亡判决 + 单样本因子变换范式 NO-GO（2026-09-09 19:41）

## 最后一刀（唐先生执行——修正 g_k(r) 定义后直接消掉间隙残留）
```
g_k(r) = max{ℓ: ℓ|k, ℓ<r, ℓ prime}（严格小于 r 的最大素因子——无则 1——）
——修正：不是"次大素因子"——是相邻素因子（k 的 factorization poset 的
  nearest-neighbor 信息——）——

关键论证：
① N_{k,r}(n) = Σ_{p|n}1{g_k(r)<p<r}——固定 (k,r) 的 divisor-counting weight
   ——固定 (k,r) 后 N_{k,r}(n)B_r(k−n) = 标准 divisor-weight shifted convolution
② g_k(r) 无新自由度：完全由 k 的素因子集合决定——(g_k(r), r) = k 的
   相邻素因子 gap——自由度仍只是 (p,q,k)——非独立四体 (p,g,r,q,k)
③ "无中间素因子"条件（no ℓ|k: p<ℓ<r——）可 Möbius 化：
   1{no ℓ} = Σ_{d|∏_{p<ℓ<r}ℓ} μ(d)
   → Σ_{p,r,d} μ(d)·1{p|n}·1{dr|n+m}·B_r(m)——sieve/CRT/divisor-correlation 型
```

## R₃ 死亡链（闭合）
```
R₃ → 素因子序比较 → 区间命中 → Möbius 区间筛 → 按 r 换序
  → divisor-weight shifted convolution → 相邻素因子 gap
  → 再次 Möbius/sieve 展开 → 标准 divisor correlation / shifted convolution
死亡原因：factorization-order transformation 最终只产生 k = n+m 的
  素因子区间筛——移动 gap 由相邻素因子条件 + Möbius IE 消去
  ——不能形成独立的非局部三体核——
```

## R₁/R₂/R₃ 统一坍缩谱系
```
R₁：动态模数（P^+(p+q)——）→ weighted Goldbach/HL
R₂：最大素因子尺度（P^+(n+m)/P^+(n)P^+(m)——）→ friable/factorization statistics
R₃：因子序变换（ρ_k 序投影——）→ moving sieve → divisor correlation
——统一机制：单样本 (n,m,n+m) 内操作单整数 factorization data——
  ——逃不出：divisor sums + sieve + additive convolution + factorization stats——
```

## 范式级 NO-GO（唐先生定案）
```
【单样本 (n,m,n+m) 的因子变换范式——没有继续堆复杂度的价值——】
——不是数学上"不可能存在任何例外"——
——但作为候选生成范式——可以暂时封存——
下一轮若继续寻找 RH 机制——候选必须在定义层面引入
  【跨样本、跨尺度或跨轨道的关系】——
  否则大概率只是把 sieve/convolution machinery 再换包装——
```

## 与今天的完整谱系衔接（130+ 层）
- 局部态几何（K_p ½ 刚性——非 Tate——）保留（A4 成果——）
- 三死亡舱 + 五类封闭（primewise/单 n/加性标量/二次加性/整除性——）+ R 家族（动态模数/因子统计/因子序——）全封闭
- 剩余方向：跨样本/跨尺度/跨轨道的关系（定义层面的——）
