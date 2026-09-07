#!/usr/bin/env python3
"""
D* 最终确认——500 类——更大 k + 离散化 pairwise max-ent null
将 x ∈ [−2,2] 离散化为 ±1（符号——）或 3 类——套 max-ent
"""
import json
import numpy as np
from sympy import primerange
import random

def load_classes(fn='data/ec_classdata_3000.json'):
    return json.load(open(fn))

def x_k(ap_p, k):
    if k == 0:
        return 1.0
    x0, x1 = 1.0, ap_p
    for _ in range(1, k):
        x0, x1 = x1, ap_p*x1 - x0
    return x1

def main():
    classes = load_classes()
    primes = list(primerange(2, 100))
    big_primes = [p for p in primes[8:] if p < 97]
    random.seed(81)
    
    print("="*60)
    print("D* 确认：跨 k 的三体信号扫描")
    print("="*60)
    
    for k in [1, 2, 3, 4, 5, 6]:
        samples = []
        for c in classes:
            N = c['conductor']
            ap = c['aplist']
            good = []
            for i, p in enumerate(primes):
                if i >= len(ap):
                    break
                if p in big_primes and N % p != 0:
                    good.append((p, ap[i]))
            if len(good) < 3:
                continue
            sel = random.sample(good, 3)
            xv = [x_k(ap_val/np.sqrt(p), k) for p, ap_val in sel]
            samples.append(xv)
        samples = np.array(samples)
        
        # 符号离散化（x 的符号——sign——）
        sgn = np.sign(samples)
        # 三体矩（符号——）
        T_sgn = np.mean(sgn[:,0]*sgn[:,1]*sgn[:,2])
        # pairwise null（符号——独立（跨 p 独立——）——理论 T=0）
        rng = np.random.default_rng(83)
        boot = []
        for _ in range(300):
            idx = rng.integers(0, len(samples), len(samples))
            s = sgn[idx]
            boot.append(np.mean(s[:,0]*s[:,1]*s[:,2]))
        bs = np.std(boot)
        print(f"k={k}: 样本 {len(samples)}——符号三体 T = {T_sgn:.4f}——bootstrap std = {bs:.4f}——z = {T_sgn/bs:.2f}")
    
    print("\n" + "="*60)
    print("结论")
    print("="*60)
    print("若所有 k 的 |z| < 3 且无稳定 profile——按唐先生预判：")
    print("Hecke-local recursion + family ensemble ⇏ new higher-order propagation——D 整代关闭")

if __name__ == "__main__":
    main()
