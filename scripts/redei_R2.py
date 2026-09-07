#!/usr/bin/env python3
"""
R2：pairwise-matched null——Δ₄ 分布对比
Null：保持模类（mod 8）与 pairwise Legendre 状态——重采样素数——破坏 Rédei 三体代数
比较：真实 Δ₄ 非零率 vs null 的非零率（10³ null——经验 p-value——）
"""
import math, sys, random
sys.path.insert(0, 'scripts')
from redei_v4 import redei_v4, legendre
import numpy as np

def R_val(a, b, c):
    """R ∈ {0,1}"""
    v = redei_v4(a, b, c)
    return None if v is None else (0 if v == 1 else 1)

def collect_quadruples(pool, n_target=60):
    """收集四点配置（固定 b——a₁,a₂ 与 b 互余——c₁,c₂ 与全互余——）"""
    configs = []
    random.seed(51)
    for _ in range(500):
        b = random.choice(pool)
        a_pool = [a for a in pool if a != b and legendre(a, b) == 1]
        if len(a_pool) < 25:
            continue
        a1, a2 = random.sample(a_pool, 2)
        c_pool = [c for c in pool if c not in (a1, a2, b) 
                  and legendre(b,c)==1 and legendre(a1,c)==1 and legendre(a2,c)==1]
        if len(c_pool) < 15:
            continue
        c1, c2 = random.sample(c_pool, 2)
        # 四点真实值
        triples = [(a1,b,c1),(a2,b,c1),(a1,b,c2),(a2,b,c2)]
        vals = []
        ok = True
        for (x,y,z) in triples:
            v = R_val(x,y,z)
            if v is None:
                ok = False
                break
            vals.append(v)
        if not ok:
            continue
        configs.append({
            'a1': a1, 'a2': a2, 'b': b, 'c1': c1, 'c2': c2,
            'vals': vals, 'R': vals
        })
        if len(configs) >= n_target:
            break
    return configs

def delta4(vals):
    return (vals[0] + vals[1] + vals[2] + vals[3]) % 2

def main():
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    pool = [int(p) for p in primes if p % 4 == 1 and p > 5 and p < 8000][:350]
    print(f"素数池: {len(pool)}")
    
    configs = collect_quadruples(pool, 50)
    print(f"四点配置: {len(configs)}")
    if len(configs) < 20:
        print("配置太少——扩大池——")
        return
    
    # 真实 Δ₄
    real_delta = [delta4(c['R']) for c in configs]
    real_nonzero = sum(real_delta) / len(real_delta)
    print(f"\n真实 Δ₄≠0 比例: {real_nonzero:.3f}（{sum(real_delta)}/{len(real_delta)}）")
    
    # Null：模类匹配重采样——对每个配置——生成 null 版本
    # 用"随机 ±1 但保持 admissibility 模拟"——更实际的 null：对同一批素数重配对
    # 方案：洗牌 R 值中的 c 关联——保持 a₁,a₂,b 固定——c₁',c₂' 从同类重采样
    # 简化 null：随机打乱四点的配对（a₁ 配 c 随机——但保持 pairwise 状态）
    # 用重采样：null Δ₄ 从"随机 ±1 四点"（Bernoulli 50/50——）但需要保持某种结构——
    # 用"模类匹配"：对每个配置的 (a1,a2,b,c1,c2)——从同类（mod 8）素数重采样 c1',c2'——
    # 但重采样后 pairwise Legendre 可能不保持——先按同类 + 互余条件重采样——
    
    n_null = 500
    null_nonzeros = []
    random.seed(53)
    for _ in range(n_null):
        nd = []
        for cfg in configs:
            a1, a2, b = cfg['a1'], cfg['a2'], cfg['b']
            # 同类（mod 8——）的 c 重采样（保持与 a1,a2,b 互余——）
            c_pool = [c for c in pool if c not in (a1,a2,b)
                      and c % 8 == cfg['c1'] % 8  # 保持 c1 的类
                      and legendre(b,c)==1 and legendre(a1,c)==1 and legendre(a2,c)==1]
            if len(c_pool) < 3:
                nd.append(None)
                continue
            # 随机重连：c1' 与 c2' 从池中随机（可能相同——近似——）
            c1p, c2p = random.sample(c_pool, 2)
            triples = [(a1,b,c1p),(a2,b,c1p),(a1,b,c2p),(a2,b,c2p)]
            vals = []
            ok = True
            for (x,y,z) in triples:
                v = R_val(x,y,z)
                if v is None:
                    ok = False
                    break
                vals.append(v)
            nd.append(delta4(vals) if ok else None)
        valid = [d for d in nd if d is not None]
        if valid:
            null_nonzeros.append(sum(valid)/len(valid))
    
    null_mean = np.mean(null_nonzeros) if null_nonzeros else 0
    null_std = np.std(null_nonzeros) if null_nonzeros else 0
    print(f"\nNull（同类 c 重采样——）Δ₄≠0 比例: mean={null_mean:.3f}——std={null_std:.3f}（{n_null} 次——）")
    
    # 经验 p-value
    if null_nonzeros:
        p_val = sum(1 for x in null_nonzeros if x >= real_nonzero) / len(null_nonzeros)
        print(f"经验 p-value（null ≥ real——）: {p_val:.4f}")
        effect = (real_nonzero - null_mean) / (null_std + 1e-9)
        print(f"效应量（real−null）/std: {effect:.2f}")
    
    # 判定
    print("\n" + "="*60)
    if null_nonzeros and real_nonzero > null_mean + 3*null_std:
        print("✅ R2 通过：真实 Δ₄ 显著高于 pairwise-matched null——真三体 excess 确认")
    elif null_nonzeros and real_nonzero > null_mean:
        print(f"⚠️ 真实高于 null 但 < 3σ——需更多样本——（real={real_nonzero:.3f} vs null={null_mean:.3f}）")
    else:
        print("❌ R2 判死：真实 Δ₄ ≈ null——R1 的 39% 是 admissibility/pairwise 结构假象")

if __name__ == "__main__":
    main()
