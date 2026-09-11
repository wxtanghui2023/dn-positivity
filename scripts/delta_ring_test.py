#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# δ-环跨素数测试: p-导子 δ_p(n) = (n - n^p)/p 的交换子
# 检查: δ_pδ_q(n) - δ_qδ_p(n) 是否 = pq 的乘法函数(平凡/C8) 或 n 的非平凡函数(新)
def delta(p, n):
    """p-导子: δ_p(n) = (n - n^p)/p (Fermat: n^p≡n mod p, 整除)"""
    return (n - n**p) // p

def commutator(p, q, n):
    """δ_pδ_q(n) - δ_qδ_p(n)"""
    return delta(p, delta(q, n)) - delta(q, delta(p, n))

if __name__ == "__main__":
    print("δ_pδ_q - δ_qδ_p 交换子测试 (整数 p-导子)")
    pairs = [(2,3), (2,5), (3,5)]
    for (p,q) in pairs:
        print(f"\n(p,q)=({p},{q}):")
        print(f"  n:  交换子值  (δ_pδ_q(n), δ_qδ_p(n))")
        for n in range(2, 15):
            c = commutator(p, q, n)
            a = delta(p, delta(q, n))
            b = delta(q, delta(p, n))
            print(f"  {n:>2}: {c:>12}  ({a:>10}, {b:>10})")
    # 检查: 交换子是否 = F(p,q)·g(n)? 或 = h(p,q,n) 非平凡?
    print("\n交换子随 n 的结构检查 (是否 = 某简单函数):")
    p, q = 2, 3
    vals = [commutator(p, q, n) for n in range(2, 12)]
    print(f"  (2,3): {vals}")
    # 检查 n = pq, 2pq, 3pq 等特殊值
    print("\n特殊 n (含 p,q 因子) 的交换子:")
    for n in [6, 12, 18, 30, 60]:
        print(f"  n={n}: δ_2δ_3-δ_3δ_2 = {commutator(2,3,n)}")
    # 增长检查
    print("\n交换子增长 (n 大):")
    for n in [20, 30, 50]:
        try:
            print(f"  n={n}: |δ_2δ_3-δ_3δ_2| = {abs(commutator(2,3,n))}")
        except Exception as e:
            print(f"  n={n}: 溢出 {e}")
