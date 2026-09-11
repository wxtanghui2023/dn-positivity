#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# Affine groupoid primitive word 测试
# 生成元: D_p (n->pn, p素数), T (n->n+1) — 关系 D_pT = T^p D_p (分配律)
# 词作用 = n -> an+b。检查:
# 1. 词→(a,b) 的碰撞率 (非自由性: 可解群大量关系 vs 自由群唯一)
# 2. 是否有"闭合词" (在 N 上: an+b=n 无解 a>=1,b>=0 除平凡)
# 3. 词增长 vs (a,b) 值空间
import math
from itertools import product

def apply_word(word, n):
    """word = 序列 of ('D',p) or ('T',) — 从右到左应用? 定义: 词按序复合"""
    # 生成元按序列顺序: 先应用第一个? 约定: word = g1 g2 ... gk 作用 = gk∘...∘g1
    # 我们按"从左到右读, 作用复合"——用显式: 词 D_p 表示 n->pn, T 表示 n->n+1
    # 作用顺序: 词 [g1,...,gk] 表示先 g1 后 g2 ... (右复合)
    cur = n
    for g in word:
        if g[0] == 'D':
            cur = g[1] * cur
        else:
            cur = cur + 1
    return cur

def word_to_ab(word):
    """词作用 n -> an+b"""
    a, b = 1, 0
    for g in word:
        if g[0] == 'D':
            a, b = g[1]*a, g[1]*b
        else:
            b = b + 1
    return a, b

if __name__ == "__main__":
    gens = [('D',2), ('D',3), ('D',5), ('T',)]
    print("affine 词测试 (生成元 D_2,D_3,D_5,T)")
    print("\n1. 词→(a,b) 碰撞率 (非自由性):")
    for L in [2,3,4,5,6]:
        total = 0
        seen = {}
        for word in product(gens, repeat=L):
            a, b = word_to_ab(word)
            seen.setdefault((a,b), []).append(word)
            total += 1
        collisions = sum(1 for v in seen.values() if len(v) > 1)
        print(f"  长度{L}: 词数 {total}  不同(a,b) {len(seen)}  碰撞组 {collisions}  最大多重性 {max(len(v) for v in seen.values())}")
    print("\n2. N 上闭合词 (an+b=n, a>=1, b>=0):")
    # an+b = n => (a-1)n = -b => a=1 且 b=0 (平凡) 或无解
    print("  解析: (a-1)n = -b — a>=1, b>=0: a=1,b=0 平凡(空词); a>1: (a-1)n=-b<0 无解; a=1,b>0: 0=-b 无解")
    print("  ⟹ N 上无非平凡闭词 (所有词严格增)")
    print("\n3. 词作用在 n=1 的值分布 (长度4):")
    vals = {}
    for word in product(gens, repeat=4):
        v = apply_word(word, 1)
        vals[v] = vals.get(v, 0) + 1
    print(f"  不同值: {len(vals)}, 值范围: [{min(vals)}, {max(vals)}]")
    print(f"  最大多重性 (同一值的词数): {max(vals.values())}")
    # 检查同一值的词 — 关系的体现
    print("\n4. 关系示例 (同一作用的不同词 — 可解群关系):")
    target = None
    for word in product(gens, repeat=3):
        a,b = word_to_ab(word)
        if (a,b) == (6, 0) or (a,b) == (2,2):
            print(f"    {word} -> ({a},{b})")
    # D_2 T vs T^2 D_2?  (D_2,T): a=2,b=0 then +1 => (2,1)? 
    # 直接验证分配律关系: D_p T 与 T^p D_p
    print("\n5. 分配律关系验证 D_pT = T^pD_p:")
    for p in [2,3]:
        w1 = [('D',p), ('T',)]  # D_p 然后 T: n -> pn -> pn+1
        # T^p D_p: +1 p次 然后 ×p: n -> (n+p)*p? 不对 — 词顺序:
        w2 = [('T',)]*p + [('D',p)]  # 先 T^p (n->n+p) 后 D_p (n->p(n+p))
        a1,b1 = word_to_ab(w1)
        a2,b2 = word_to_ab(w2)
        print(f"  p={p}: D_pT -> (a,b)=({a1},{b1})   T^pD_p -> ({a2},{b2})  相同: {(a1,b1)==(a2,b2)}")
