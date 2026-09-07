#!/usr/bin/env python3
"""
D* 三体探测（初步——100 类 ensemble——）
对象：x_E(p^k)——E 同源类 ensemble——p 素数——k 传播深度
测：跨 p 的 (x_E(p^k), x_E(q^k), x_E(r^k)) 三体残差 vs pairwise max-ent

Hecke：x(p^{k+1}) = x(p)·x(p^k) − x(p^{k−1})（归一化——权重 2 椭圆曲线——χ=1——）
"""
import json
import numpy as np
from sympy import primerange

def load_classes(fn='data/ec_classdata_3000.json'):
    return json.load(open(fn))

def x_k(ap_p, k):
    """x(p^k) 从 x(p) = ap_p/√p 用 Chebyshev/Hecke 递推
    x_0 = 1（λ(1)——）x_1 = x——x_{k+1} = x·x_k − x_{k−1}"""
    if k == 0:
        return 1.0
    x0, x1 = 1.0, ap_p
    for _ in range(1, k):
        x0, x1 = x1, ap_p*x1 - x0
    return x1

def main():
    classes = load_classes()
    primes = list(primerange(2, 100))
    print(f"ensemble: {len(classes)} 类——素数到 {primes[-1]}")
    
    # 对每个类——每个好素数——记录 x_E(p)（归一化——）
    # 注意 aplist[i] = a_{primes[i]}——aplist 长度 25（primes[:25]——）
    n_ap = min(len(primes), 25)
    
    # 构建数据：对每个类 E——好素数 p——x_E(p)
    # 三体：固定 k——取 3 个素数 p,q,r（好——）——跨 E 测三阶残差
    import random
    random.seed(71)
    
    # 选 3 个素数（中等的——避免小 conductor 的坏素数问题——p > 20——）
    big_primes = [p for p in primes[8:] if p < 97]  # p ≥ 23
    print(f"候选素数（≥23——）: {big_primes}")
    
    for k in [1, 2, 3]:
        # 收集 (x_p, x_q, x_r) 三体样本（跨 E——）
        samples = []
        for c in classes:
            N = c['conductor']
            ap = c['aplist']
            # 取 3 个好素数
            good = []
            for i, p in enumerate(primes):
                if i >= len(ap):
                    break
                if p in big_primes and N % p != 0:
                    good.append((p, ap[i]))
            if len(good) < 3:
                continue
            # 随机取 3 个（或固定 3 个——）
            sel = random.sample(good, 3)
            xv = [x_k(ap_val/np.sqrt(p), k) for p, ap_val in sel]
            samples.append(xv)
        samples = np.array(samples)
        print(f"\nk={k}: 样本 {len(samples)}——")
        if len(samples) < 30:
            print("  样本不足——")
            continue
        # 三阶矩
        T = np.mean(samples[:,0]*samples[:,1]*samples[:,2])
        # pairwise max-ent 残差（简化：用累积量——cumulant 方法——）
        # κ3 = E[xyz] − E[xy]E[z] − E[xz]E[y] − E[yz]E[x] + 2E[x]E[y]E[z]
        mx, my, mz = samples.mean(axis=0)
        cxy = np.mean(samples[:,0]*samples[:,1])
        cxz = np.mean(samples[:,0]*samples[:,2])
        cyz = np.mean(samples[:,1]*samples[:,2])
        # 三阶 cumulant（近似三体残差——）
        k3 = T - cxy*mz - cxz*my - cyz*mx + 2*mx*my*mz
        # bootstrap
        rng = np.random.default_rng(73)
        boot = []
        for _ in range(200):
            idx = rng.integers(0, len(samples), len(samples))
            s = samples[idx]
            bT = np.mean(s[:,0]*s[:,1]*s[:,2])
            bmx, bmy, bmz = s.mean(axis=0)
            bcxy = np.mean(s[:,0]*s[:,1])
            bxz = np.mean(s[:,0]*s[:,2])
            byz = np.mean(s[:,1]*s[:,2])
            bk3 = bT - bcxy*bmz - bxz*bmy - byz*bmx + 2*bmx*bmy*bmz
            boot.append(bk3)
        bs = np.std(boot)
        print(f"  T = {T:.5f}——cumulant κ3 = {k3:.5f}——bootstrap std = {bs:.5f}——z = {k3/bs:.2f}")
        print(f"  （|z| < 3 → 无信号——）")

if __name__ == "__main__":
    main()
