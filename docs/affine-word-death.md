# Affine groupoid primitive closed-word zeta：回答"否"——封档（2026-09-03 12:05）

## 对象
生成元 D_p(n→pn), T(n→n+1)——关系 D_pT = T^pD_p（分配律 p(n+1)=pn+p——）
词作用 = n → an+b——问：primitive closed words 能否产生非人为的 Euler product？

## 数值（生成元 D_2,D_3,D_5,T）
1. **词→(a,b) 大量碰撞（非自由）**：L6: 4096 词 → 1131 不同 (a,b)——729 碰撞组——最大多重性 90（随长度快速增长）
2. **N 上无闭词**（解析）：(a−1)n = −b——a≥1,b≥0 非平凡无解——所有词严格增
3. 分配律关系 D_pT = T^pD_p 成立（D_p∘T(n)=p(n+1)=pn+p=T^p∘D_p(n)——）

## 判断：回答"否"——不能产生 Euler product（affine-semigroup 范式封档）
1. **词非自由**（大量碰撞/关系——可解群——）——"primitive closed words ↔ prime powers"双射（Ihara 型——）需要自由/树结构的唯一分解——affine 群无（词多重表示）
2. **无闭词在 N 上**（严格增——）——"闭"只能模 q（有限——表示论已封）或群关系（平凡——分配律——）
3. **词结构由 affine 群（可解——Z⋊Q^+——）决定——素数只是 D_p 的标签——不进入词骨架**（谱骨架原则再确认）
4. 词 zeta（可解群——多项式增长——）无 Ihara 型非平凡 Euler

## 深层
要"词→Euler 积"需自由/树/双曲结构（Ihara——Selberg——prime cycles↔素数的刚性对应——）——但那是"图的素数"（闭测地线——）非算术素数
**深层怀疑**：整数 +× 的代数结构（分配律——半环——）本质可解（交换加群 × 交换乘群——半直积——）——无自由/双曲的算术结构——"算术群胚可解性 → 词 zeta 平凡"——可能是深层障碍

## 文件
scripts/affine_word_test.py, docs/affine-word-death.md
