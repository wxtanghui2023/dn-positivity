#!/usr/bin/env python3
# ACPC 最小模型骨架测试
# 最小 incidence: a+b = qm = n
# C(X) = Σ_{a+b=qm≤X} Λ(a)Λ(b)Λ(q)Λ(m) = Σ_n A(n)·M(n)
#   A(n) = 加性卷积: Σ_{a+b=n} Λ(a)Λ(b)  (素数幂对)
#   M(n) = 乘性卷积: Σ_{qm=n} Λ(q)Λ(m)  ((Λ*Λ)(n), 数论卷积)
# 检查: log Z 的连通化结构 + 增长 + 是否退化
import math, time

def prime_powers_lam(X):
    """von Mangoldt Λ(n) 支撑: 素数幂, 值 log p"""
    # 筛素数
    is_p = [True]*(X+1)
    is_p[0]=is_p[1]=False
    for i in range(2, int(X**0.5)+1):
        if is_p[i]:
            for j in range(i*i, X+1, i):
                is_p[j]=False
    lam = [0]*(X+1)
    pp = []  # (素数幂, log p)
    for p in range(2, X+1):
        if is_p[p]:
            lp = math.log(p)
            pk = p
            while pk <= X:
                lam[pk] = lp
                pp.append((pk, lp))
                pk *= p
    return lam, pp

def compute(X):
    lam, pp = prime_powers_lam(X)
    # A(n) = Σ_{a+b=n} Λ(a)Λ(b), a,b 素数幂 >= 2
    A = [0]*(X+1)
    pp_vals = [v for v,_ in pp]
    for i, (a, la) in enumerate(pp):
        if a >= X: break
        for b, lb in pp:
            n = a+b
            if n > X: break
            A[n] += la*lb
    # M(n) = Σ_{qm=n} Λ(q)Λ(m) (q,m 素数幂 >=2; 注: 素数幂含 1? 不含, Λ(1)=0)
    M = [0]*(X+1)
    for q, lq in pp:
        if q > X: break
        for m, lm in pp:
            n = q*m
            if n > X: break
            M[n] += lq*lm
    # C(X) = Σ_{n<=X} A(n)M(n); 也测 Σ A(n), Σ M(n)
    cumA = [0]*(X+1); cumM=[0]*(X+1); cumC=[0]*(X+1)
    sA=sM=sC=0
    for n in range(1, X+1):
        sA+=A[n]; sM+=M[n]; sC+=A[n]*M[n]
        cumA[n]=sA; cumM[n]=sM; cumC[n]=sC
    return A, M, cumA, cumM, cumC

if __name__ == "__main__":
    X = 20000
    t0=time.time()
    A, M, cumA, cumM, cumC = compute(X)
    print(f"X={X}, 耗时 {time.time()-t0:.1f}s")
    # 检查 A, M 的非零结构与增长
    print("\nA(n)=加性卷积 Λ*_+Λ 结构:")
    nz = [(n, A[n]) for n in range(2, X+1) if A[n] > 0]
    print(f"  非零 n 数: {len(nz)}")
    # 增长拟合: cumA(X) ~ X·log^α? cumC ~ ?
    print(f"\n{'X':>10} {'ΣA(n)':>14} {'ΣM(n)':>14} {'Σ A·M':>16}  A·M/ΣA·ΣM*X")
    for x in [500, 1000, 2000, 5000, 10000, 15000, 20000]:
        if x > X: continue
        ratio = cumC[x] / (cumA[x]*cumM[x]) * x if cumA[x]*cumM[x] else 0
        print(f"{x:>10} {cumA[x]:>14.0f} {cumM[x]:>14.0f} {cumC[x]:>16.0f}  {ratio:.6f}")
    # 归一化检查: ΣA ~ X log X? ΣM ~ X log^2 X? (Λ*Λ 平均 ~ log^2)
    print("\n归一化 ΣA/(X log X):")
    for x in [5000, 10000, 15000, 20000]:
        print(f"  X={x}: ΣA={cumA[x]:.0f}, /(X log X)={cumA[x]/(x*math.log(x)):.3f}")
    print("归一化 ΣM/(X log^2 X):")
    for x in [5000, 10000, 15000, 20000]:
        print(f"  X={x}: ΣM={cumM[x]:.0f}, /(X log^2 X)={cumM[x]/(x*math.log(x)**2):.3f}")
    # 检查 A(n) 是否有"加法结构" (A 非零的 n 的密度)
    print(f"\nA(n)>0 密度: {len(nz)/X:.3f}  (n 到 {max(n[0] for n in nz)})")
    # 前几个 A(n) 值 (小 n 结构)
    print("\n小 n 的 A(n), M(n):")
    for n in range(2, 30):
        if A[n]>0 or M[n]>0:
            print(f"  n={n}: A={A[n]:.3f} M={M[n]:.3f}")
