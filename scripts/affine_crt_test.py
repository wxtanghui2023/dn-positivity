#!/usr/bin/env python3
# Affine prime dynamics CRT/representation factorization test
# T_p(x) = px+1 mod q (primorial q) — U_p 置换表示
# Tr(U_s^k) = Σ_words (ΠΛ(p_j)/p_j^s) · N_q(P,B), N_q = #{x: T_word(x)=x}
# 检查: (1) N_q 的 CRT 因子化 (2) Tr 的谱结构 (3) 是否角色/L函数类
import numpy as np, math
from math import gcd

def primorial(X):
    """q = ∏_{ℓ≤X} ℓ"""
    is_p = np.ones(X+1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(X**0.5)+1):
        if is_p[i]:
            is_p[i*i::i] = False
    q = 1
    for i in range(2, X+1):
        if is_p[i]:
            q *= i
    return q

def primes_upto(N):
    is_p = np.ones(N+1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(N**0.5)+1):
        if is_p[i]:
            is_p[i*i::i] = False
    return [int(i) for i in np.nonzero(is_p)[0]]

def fixed_points_count(p_list, q):
    """N_q = #{x mod q: T_{p_k}...T_{p_1}(x) = x}, T_p(x)=px+1"""
    # 直接枚举 (q 小)
    cnt = 0
    for x in range(q):
        cur = x
        for p in p_list:
            cur = (p*cur + 1) % q
        if cur == x:
            cnt += 1
    return cnt

def P_B_of_word(p_list):
    """P = Πp_j, B = affine offset"""
    P = 1
    for p in p_list:
        P *= p
    # B = 1 + p_k + p_k p_{k-1} + ... (从 T_{p_k}...T_{p_1})
    B = 1
    prod = 1
    for p in reversed(p_list):
        prod *= p
        B += prod  # 这是 x 系数之后? 重算: T_p(x)=px+1, 复合 T_{p_k}∘...∘T_{p_1}(x) = P x + B
    # B = Σ_{j=1..k} Π_{r=j+1..k} p_r  (1 对应最后 +1)
    # = 1 + p_k + p_k p_{k-1} + ...  上面循环算了 1+Σ 后缀积(含全积?) — 修正:
    B = 1
    prod = 1
    for p in reversed(p_list):
        B += prod  # 不对, 应从 p_k 开始
        prod *= p
    return P, B

def P_B_correct(p_list):
    """T_{p_k}∘...∘T_{p_1}(x) = Px + B, B = Σ_{j=1}^{k} Π_{r=j+1}^{k} p_r"""
    P = 1
    for p in p_list:
        P *= p
    B = 1  # 最后 +1
    suffix = 1
    # B = 1 + p_k + p_k p_{k-1} + ... + p_k...p_2
    for p in reversed(p_list[1:]):  # p_k ... p_2
        suffix *= p
        B += suffix
    return P, B

if __name__ == "__main__":
    X = 5
    q = primorial(X)  # 2·3·5 = 30
    print(f"q = primorial({X}) = {q}")
    # gcd(p,q)=1 的素数 p < q
    ps = [p for p in primes_upto(q-1) if gcd(p, q) == 1]
    print(f"gcd(p,q)=1 的素数 p<q: {ps}")
    # N_q 验证: CRT 因子化 N_q = ∏ N_ℓ?
    print("\nN_q CRT 因子化验证 (word 固定点数):")
    from itertools import combinations_with_replacement
    words = [(2,3),(2,5),(3,5),(2,3,5),(7,11),(5,7),(2,7)]
    # 只用 ps 里的素数
    words = [w for w in words if all(p in ps for p in w)]
    q_factors = [2,3,5]
    for w in words:
        P, B = P_B_correct(w)
        Nq = fixed_points_count(list(w), q)
        # 每 ℓ 的 N_ℓ
        Ns = []
        for ell in q_factors:
            Ns.append(fixed_points_count(list(w), ell))
        prod_Ns = 1
        for v in Ns:
            prod_Ns *= v
        print(f"  word {w}: P={P} B={B} N_q={Nq}  N_ℓ={Ns} ∏N_ℓ={prod_Ns}  CRT一致={Nq==prod_Ns}")
    # U_s 谱
    print("\nU_s 谱 (q=30, s=1):")
    s = 1.0
    n = q
    U = np.zeros((n, n))
    for p in ps:
        lam = math.log(p)
        # U_p: (U_p f)(x) = f(T_p^{-1}x) — 置换矩阵 U_p[x][T_p^{-1}(x)] = 1? 直接: U_p 作用 x -> 记录
        # 用函数: (U_p f)(x) = f( (x-1)*p^{-1} mod q )?  T_p^{-1}(x) = p^{-1}(x-1)
        pinv = pow(p, -1, q)
        for x in range(n):
            y = (pinv * (x - 1)) % q  # T_p^{-1}(x)
            U[x, y] += lam / p**s
    ev = np.linalg.eigvals(U)
    print(f"  U_s 特征值: max|λ|={np.max(np.abs(ev)):.4f}")
    print(f"  非零特征值数: {np.sum(np.abs(ev)>1e-10)}/{n}")
    # Tr(U_s^k)
    for k in range(1, 4):
        Uk = np.linalg.matrix_power(U, k)
        print(f"  Tr(U_s^{k}) = {np.trace(Uk):.6f}")
