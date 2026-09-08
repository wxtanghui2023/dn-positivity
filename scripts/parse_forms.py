#!/usr/bin/env python3
"""
解析 LMFDB level-1 eigenform traces——构建 (f,p,k) 场
归一化：λ_f(p^k) = a_f(p^k)/p^{k(w-1)/2}——或直接用未归一化做内部比较——
对三体检验：用 Hecke 递推生成 λ(p^k) 从 λ(p)（验证——）
"""
import re, json
import numpy as np

def parse_traces(fn):
    """解析 traces 文件——返回 τ_f(n) 列表（n=0..N）"""
    with open(fn) as f:
        lines = f.readlines()
    data_line = [l for l in lines if l.strip().startswith('[')]
    if not data_line:
        return None
    nums = re.findall(r'-?\d+', data_line[0])
    return [int(x) for x in nums]

def main():
    weights = [12, 16, 18, 20, 22, 26]
    forms = {}
    for wt in weights:
        fn = f'/home/node/.openclaw/workspace/dn-project/data/lmfdb_1.{wt}.traces.txt'
        taus = parse_traces(fn)
        if taus:
            forms[wt] = taus
            print(f"权重 {wt}: {len(taus)} 个系数——τ(1)={taus[1]}——τ(2)={taus[2]}")
    
    # 保存
    np.savez('/home/node/.openclaw/workspace/dn-project/data/level1_forms.npz',
             **{f'w{wt}': np.array(forms[wt]) for wt in forms})
    print(f"\n已保存 {len(forms)} 个 form（权重 {list(forms.keys())}——）")
    
    # 验证 Hecke 递推（用 Δ——权重 12——）
    taus = forms[12]
    print("\nHecke 递推验证（权重 12——）：")
    for p in [2, 3, 5, 7]:
        if p*p >= len(taus):
            break
        tp, tp2 = taus[p], taus[p*p]
        pred = tp*tp - p**11
        print(f"  p={p}: τ(p²)={tp2}——预测 {pred}——{'✓' if tp2 == pred else '✗'}")
    
    # 归一化 Satake（用于三体——）——X_{f,p} = a_f(p) = τ(p)/p^{(w-1)/2}
    print("\n归一化 a_f(p)（跨 f 同 p 比较——）:")
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')[:20]
    for p in primes[:8]:
        p = int(p)
        vals = []
        for wt in weights:
            t = forms[wt]
            if p < len(t):
                a = t[p] / p**((wt-1)/2)
                vals.append(f"{a:+.3f}")
        print(f"  p={p}: " + "  ".join(vals))

if __name__ == "__main__":
    main()
