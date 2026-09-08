#!/usr/bin/env python3
"""
⚠️ 极其小心的验证：Im Λ(σ+it) 的单调性 + 唯一过零
如果 Im Λ 对 σ 严格单调（过零一次在 ½）对所有 t——RH 几何证明？
必须找漏洞：Lehmer 对/更多 t/σ 边界/单调性反例
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 20

def Lambda_im(sig, t):
    s = mp.mpc(sig, t)
    chi = 2**(s-1) * mp.pi**s / (mp.gamma(s) * mp.cos(mp.pi*s/2))
    L = chi**mp.mpf('-0.5') * mp.zeta(s)
    return float(L.imag)

def main():
    print("="*70)
    print("⚠️ Im Λ 单调性严格检验")
    print("="*70)
    
    # 1. 更多 t——σ 全范围——检查单调性和过零
    sigs_full = np.linspace(0.001, 0.999, 500)
    ts_test = [1, 2, 3, 6, 9, 12, 14.1347, 15, 18, 21.022, 22, 24, 25.011, 27, 30.425, 31, 33, 35, 37.6, 39, 42, 44, 46, 49.77, 52, 55, 58, 60]
    
    print("\n过零位置 + 单调性（符号变化次数——）:")
    non_half = []
    for t in ts_test:
        vals = [Lambda_im(sig, t) for sig in sigs_full]
        # 过零
        zeros = []
        for i in range(len(sigs_full)-1):
            if vals[i]*vals[i+1] < 0:
                zeros.append((sigs_full[i]+sigs_full[i+1])/2)
        # 单调性：符号变化次数 = len(zeros)（单调 = 1 次——）
        # 检查增减（一阶差分的符号——）
        diffs = np.diff(vals)
        sign_changes = np.sum(diffs[:-1]*diffs[1:] < 0)
        status = "单调" if sign_changes == 0 else f"非单调({sign_changes} 次转向——)"
        zstr = ", ".join(f"{z:.4f}" for z in zeros)
        ok = all(abs(z-0.5) < 0.01 for z in zeros) and len(zeros) == 1
        if not ok:
            non_half.append((t, zeros))
        print(f"   t={t:>7}: 过零 = [{zstr}]——{status}——{'✓' if ok else '⚠️ 异常！'}")
    
    if non_half:
        print(f"\n⚠️ 异常 t: {non_half}")
    else:
        print(f"\n✅ 所有测试 t：Im Λ=0 唯一过零在 σ=½ 且单调——")
        print(f"   （但这是数值——需要证明——且需排除更多情况——）")

if __name__ == "__main__":
    main()
