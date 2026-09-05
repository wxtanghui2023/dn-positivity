#!/usr/bin/env python3
# δ-生成代数下中心列测试
# D = <δ_2, δ_3>, δ_p(n) = (n - n^p)/p
# 下中心列: D^(1)=D, D^(k+1)=[D, D^(k)] (交换子 = 函数组合差)
# 检查: 每阶主导指数 (log|值|/log n) 是否倍增(幂塔/乘法迭代) 还是新结构
def delta(p, n):
    return (n - n**p) // p

def compose(f, g, n):
    """f∘g(n) = f(g(n))"""
    return f(g(n))

def comm(f, g, n):
    """[f,g](n) = f(g(n)) - g(f(n))"""
    return f(g(n)) - g(f(n))

def make_delta(p):
    return lambda n: delta(p, n)

if __name__ == "__main__":
    d2 = make_delta(2)
    d3 = make_delta(3)
    print("δ-下中心列测试 (生成元 δ_2, δ_3)")
    print("每阶: [δ_2, C_k] 的主导指数 (log|val|/log n, 大 n 近似)")
    
    # C_2 = [δ_2, δ_3]
    C = lambda n: comm(d2, d3, n)
    print(f"\nC_2 = [δ_2,δ_3]:")
    for n in [5, 7, 10]:
        v = C(n)
        print(f"  n={n}: {v}  log|v|/log n = {abs(v) and __import__('math').log(abs(v))/__import__('math').log(n):.3f}")
    
    # C_3 = [δ_2, C_2]
    C3 = lambda n: comm(d2, C, n)
    print(f"\nC_3 = [δ_2,[δ_2,δ_3]]:")
    for n in [3, 4, 5]:
        try:
            v = C3(n)
            print(f"  n={n}: {v}  log|v|/log n = {__import__('math').log(abs(v))/__import__('math').log(n):.3f}")
        except Exception as e:
            print(f"  n={n}: 溢出/错误")
    
    # C_3' = [δ_3, C_2]
    C3b = lambda n: comm(d3, C, n)
    print(f"\nC_3' = [δ_3,[δ_2,δ_3]]:")
    for n in [3, 4, 5]:
        try:
            v = C3b(n)
            print(f"  n={n}: {v}  log|v|/log n = {__import__('math').log(abs(v))/__import__('math').log(n):.3f}")
        except Exception as e:
            print(f"  n={n}: 溢出/错误")
    
    # C_4 = [δ_2, C_3]
    C4 = lambda n: comm(d2, C3, n)
    print(f"\nC_4 = [δ_2,[δ_2,[δ_2,δ_3]]]:")
    for n in [2, 3]:
        try:
            v = C4(n)
            print(f"  n={n}: {v}  log|v|/log n = {__import__('math').log(abs(v))/__import__('math').log(n):.3f}")
        except Exception as e:
            print(f"  n={n}: 溢出/错误 ({e})")
    
    # 理论: 若 C_k ~ n^{e_k}, δ_2 作用 ~ 平方 (δ_2(n^a) ~ n^{2a}), 则 e_{k+1} = 2·e_k? (幂塔)
    # 若 e_2 = 6 (pq), e_3 = 12 (2·6), e_4 = 24 (2·12) → 幂塔 (乘法迭代)
    print("\n理论预期 (若幂塔): e_2=6, e_3=12, e_4=24 (每阶 ×2)")
    print("若 e_3 ≠ 12 或 e_4 ≠ 24 → 非纯幂塔 → 可能有新结构")
