#!/usr/bin/env python3
"""
低 p 主导验证——S̄ 的段面积交替性
如果 S̄ ~ 低 p（p=2 主导——）纯正弦类——段面积完美交替（ρ→-1——）
高 p 是"小振幅噪声"——不破坏交替
M(T)=O(1) ⟺ 段面积强交替（数值 ρ=-0.78——）

验证：
1. S̄ 去高 p（拟合低 p——）后——面积交替性（ρ——）
2. 高 p 残差的大小（对段面积的影响——）
3. 交替性 → M 界的关系
"""
import numpy as np
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def main():
    print("="*70)
    print("低 p 主导验证")
    print("="*70)
    
    K = 50000
    z = load_zeros(K)
    mid = (z[:-1]+z[1:])/2
    dg = np.diff(z[:K])
    
    def IntN0(t):
        if t <= 1: return 0.0
        return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
    
    kk = np.arange(1, K)
    IntN = np.array([IntN0(t) for t in z[:K]])
    Sbar = kk - (IntN[1:] - IntN[:-1])/dg
    
    # 1. 拟合低 p 分量——S̄_low = Σ_{p≤P} a_p sin(γ̄ log p)
    # 用前面拟合的 a_p（实际系数——）
    ps_fit = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    # 重新最小二乘拟合（前 30000——）
    A = []
    for p in ps_fit:
        A.append(np.sin(mid*log(p)))
    A = np.array(A).T
    coef, _, _, _ = np.linalg.lstsq(A[:30000], Sbar[:30000], rcond=None)
    Sbar_low = A @ coef
    
    # 2. 段面积（S̄_low 的——）交替性
    def segment_analysis(sig):
        Minc = sig * dg
        signs = np.sign(sig)
        flips = np.where(signs[:-1] != signs[1:])[0] + 1
        bounds = np.concatenate([[0], flips, [len(sig)]])
        areas = np.array([Minc[bounds[i]:bounds[i+1]].sum() for i in range(len(bounds)-1)])
        if len(areas) > 3:
            rho = np.corrcoef(areas[:-1], areas[1:])[0,1]
            cum = np.cumsum(areas)
            return rho, np.abs(cum).max(), len(areas)
        return 0, 0, 0
    
    rho_full, cummax_full, nseg_full = segment_analysis(Sbar)
    rho_low, cummax_low, nseg_low = segment_analysis(Sbar_low)
    print(f"\n1. 段面积交替性:")
    print(f"   完整 S̄:     ρ(面积)={rho_full:+.4f}——max|累积|={cummax_full:.4f}（n={nseg_full}——）")
    print(f"   低 p 拟合:   ρ(面积)={rho_low:+.4f}——max|累积|={cummax_low:.4f}（n={nseg_low}——）")
    
    # 3. 残差（高 p——）的大小
    resid = Sbar - Sbar_low
    print(f"\n2. 残差（高 p——）统计:")
    print(f"   S̄ std = {Sbar.std():.4f}——残差 std = {resid.std():.4f}——占比 {resid.std()/Sbar.std()*100:.1f}%")
    
    # 4. 残差的段面积影响
    rho_res, cummax_res, _ = segment_analysis(resid)
    print(f"   残差段面积: ρ={rho_res:+.4f}——max|累积|={cummax_res:.4f}")
    
    # 5. 纯 p=2 的段面积（理论完美交替——）
    p2_part = coef[0]*np.sin(mid*log(2))
    rho_p2, cummax_p2, _ = segment_analysis(p2_part)
    print(f"\n3. 纯 p=2: ρ(面积)={rho_p2:+.4f}——max|累积|={cummax_p2:.4f}（应接近 -1/小——）")
    
    # 6. 系数分布
    print(f"\n4. 拟合系数（a_p——）:")
    for p, c in zip(ps_fit, coef):
        print(f"   p={p:>2}: a={c:+.5f}——|a|/|a₂|={abs(c/coef[0]):.3f}")

if __name__ == "__main__":
    main()
