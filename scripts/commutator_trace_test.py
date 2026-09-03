#!/usr/bin/env python3
# Arithmetic noncommutative defect: [A,M] commutator trace 测试
# (Af)(n) = Σ_{p<=N-n} Λ(p)f(n+p)  加法迁移 (严格增: n -> n+p)
# (Mf)(n) = Σ_{p<=N/n} Λ(p)f(np)    乘法迁移 (严格增: n -> np, p>=2)
# 预测: A,M 严格上三角 => C=[A,M] 严格上三角 => 谱{0} => Tr(C^k)=0 所有k => det(I-zC)=1
import numpy as np, math

def prime_power_lams(N):
    is_p = np.ones(N+1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(N**0.5)+1):
        if is_p[i]:
            is_p[i*i::i] = False
    items = []
    for p in range(2, N+1):
        if is_p[p]:
            lp = math.log(p)
            pk = p
            while pk <= N:
                items.append((pk, lp))
                pk *= p
    return items

def build_operators(N):
    pp = prime_power_lams(N)
    A = np.zeros((N, N))
    M = np.zeros((N, N))
    # 索引 0..N-1 对应整数 1..N
    for n in range(1, N+1):
        i = n-1
        # A: n -> n+p <= N
        for p, lp in pp:
            if n + p > N: break
            A[i, n+p-1] += lp
        # M: n -> np <= N
        for p, lp in pp:
            if n * p > N: break
            M[i, n*p-1] += lp
    return A, M

if __name__ == "__main__":
    N = 60
    A, M = build_operators(N)
    print(f"N={N}")
    # 上三角检查
    print("A 上三角(对角下为0):", np.allclose(np.tril(A, -1), 0))
    print("M 上三角(对角下为0):", np.allclose(np.tril(M, -1), 0))
    C = A @ M - M @ A
    print("C=[A,M] 上三角:", np.allclose(np.tril(C, -1), 0))
    print("C 对角:", np.diag(C)[:10], "... 全零:", np.allclose(np.diag(C), 0))
    # 特征值
    ev = np.linalg.eigvals(C)
    print(f"C 特征值: max|λ|={np.max(np.abs(ev)):.2e}, 全零={np.allclose(ev, 0)}")
    # Tr(C^k)
    for k in range(1, 5):
        Ck = np.linalg.matrix_power(C, k)
        tr = np.trace(Ck)
        print(f"Tr(C^{k}) = {tr:.4e}")
    # det(I - zC) 数值 (z=1)
    print("det(I-C):", np.linalg.det(np.eye(N) - C))
    # C 的非零元检查 (是否完全零?)
    print("C 非零元数:", np.count_nonzero(C), "/", N*N)
    # 最大非零元
    if np.count_nonzero(C):
        print("C max|元素|:", np.max(np.abs(C)))
