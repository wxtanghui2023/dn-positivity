#!/usr/bin/env python3
"""
D* 最小探测——2 个 level-1 form（权重 12, 16——）
对象：X_{f,p,k} = 归一化 Hecke λ_f(p^k)
问题：跨 (p, p') 的三体残差（控制 pairwise 后——）是否存在？

注意：ensemble 只有 2 个 f——统计弱——本探测只回答"有没有值得追的信号"
"""
import re
import numpy as np

def parse_traces(fn):
    with open(fn) as f:
        lines = f.readlines()
    data_line = [l for l in lines if l.strip().startswith('[')]
    if not data_line:
        return None
    return [int(x) for x in re.findall(r'-?\d+', data_line[0])]

def lam_pk(tau, p, k, wt):
    """归一化 λ(p^k) = τ(p^k)/p^{k(w-1)/2}"""
    return tau[p**k] / p**(k*(wt-1)/2) if p**k < len(tau) else None

def main():
    forms = {}
    for wt in [12, 16]:
        taus = parse_traces(f'/home/node/.openclaw/workspace/dn-project/data/lmfdb_1.{wt}.traces.txt')
        if taus:
            forms[wt] = taus
    print(f"forms: {list(forms.keys())}——系数到 {len(forms[12])}")
    
    # 素数
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    ps = [int(p) for p in primes if p < 900][:150]
    print(f"素数: {len(ps)}")
    
    # 构建数据：对每个 form——每个素数 p——λ(p), λ(p²), λ(p³)（Hecke 链——）
    # 先看基本结构——Sato-Tate 检查（a_p 分布——）
    print("\n归一化 a_p = λ(p) 的统计（权重 12——Δ——）:")
    wt = 12
    tau = forms[wt]
    a_ps = [tau[p] / p**((wt-1)/2) for p in ps if p < len(tau)]
    a_arr = np.array(a_ps)
    print(f"  mean = {a_arr.mean():.4f}——std = {a_arr.std():.4f}（Sato-Tate 期望 std=1——）")
    print(f"  范围: [{a_arr.min():.3f}, {a_arr.max():.3f}]（理论 [−2,2]——）")
    
    # 沿 k 链：验证 λ(p²) vs λ(p) 的关系（二次——）
    print("\n沿 k 链压缩检查（λ(p²) 是否 = λ(p)² 的函数——）:")
    lp = np.array([tau[p]/p**5.5 for p in ps if p < len(tau)])
    lp2 = np.array([tau[p*p]/p**11 for p in ps if p < len(tau) and p*p < len(tau)])
    # Hecke: λ(p²) = λ(p)² − 1（权重 12——χ=1——w−1=11——p^{11}/p^{11}=1——）
    pred = lp**2 - 1
    resid = lp2 - pred
    print(f"  λ(p²) − (λ(p)² − 1) 残差: max|·| = {np.abs(resid).max():.2e}（应 ~0——确认一维压缩——）")
    
    # 三体探测：跨 p 的"乘性分离"检查
    # 若 λ 乘性——λ(p)λ(q)λ(r) 无三体——但测"误差"（非乘性部分——）
    # 更强的：用两个 form——(f,p,k) 场——测 k-相关跨 f
    print("\n跨 form 结构（权重 12 vs 16 的 a_p 相关——）:")
    tau16 = forms[16]
    a12 = np.array([tau[p]/p**5.5 for p in ps if p < len(tau)])
    a16 = np.array([tau16[p]/p**7.5 for p in ps if p < len(tau16) and p < len(tau)])
    # 共同 p
    common = min(len(a12), len(a16))
    a12c, a16c = a12[:common], a16[:common]
    corr = np.corrcoef(a12c, a16c)[0, 1]
    print(f"  corr(a_{'{12}'}(p), a_{'{16}'}(p)) = {corr:.4f}")
    print(f"  （不同 form 的 a_p 应独立——corr ≈ 0——）")
    
    # 三体：测 E[a12(p)·a16(p)·a12(q)] 型（混合 f 与 p——）vs pairwise 预测
    print("\n混合三体初步：E[a_f1(p)·a_f2(p)·a_f1(q)] vs 分解——")
    # 若独立——E = E[a_f1(p)]E[a_f2(p)]E[a_f1(q)] ≈ 0（均值 0——）——直接测样本
    import random
    random.seed(61)
    triples = []
    for _ in range(2000):
        p, q = random.sample(ps, 2)
        if p >= common or q >= common:
            continue
        triples.append(a12c[p]*a16c[p]*a12c[q])
    T = np.mean(triples)
    # bootstrap
    rng = np.random.default_rng(63)
    boot = []
    for _ in range(100):
        idx = rng.integers(0, len(triples), len(triples))
        boot.append(np.mean([triples[i] for i in idx]))
    print(f"  T = {T:.4f}——bootstrap std = {np.std(boot):.4f}——z = {T/np.std(boot):.2f}")
    print(f"  （若 |z| < 3——无信号——乘性/独立性解释一切——）")

if __name__ == "__main__":
    main()
