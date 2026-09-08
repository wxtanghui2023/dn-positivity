#!/usr/bin/env python3
"""
T1 构造尝试：两尺度约束系统的具体实例化

对象 X = 正整数 n 的"分解态"：
- 组合尺度（composition）：n 的乘法分解（素因子多重集——）
- 分辨尺度（resolution）：n 的"位置"（log n——加法尺度——）

构造 E_comp 和 E_res 的候选——测尺度交换律是否给 a=½
"""
import numpy as np
from math import log, sqrt

def omega(n):
    """素因子总数（带重数——）"""
    cnt = 0
    d = 2
    while d*d <= n:
        while n % d == 0:
            cnt += 1
            n //= d
        d += 1
    if n > 1:
        cnt += 1
    return cnt

def divisors_list(n):
    return [d for d in range(1, n+1) if n % d == 0]

def main():
    print("="*70)
    print("T1 构造尝试：两尺度分解")
    print("="*70)
    
    # 候选 1：E_comp = 因子分解的"复杂性"——E_res = 位置的"复杂性"
    # 组合：n 的分解树数 ~ C(Ω−1)（Catalan——）——log ~ Ω
    # 分辨：n 在 [1,N] 的位置——log n——"信息量" log log n？
    print("\n1. 尺度量候选:")
    print("   E_comp(n) ~ Ω(n)（分解的素数个数——）")
    print("   E_res(n) ~ log n（位置的信息量——）")
    print("   对 n = 2^k: Ω = k——log n = k·log2——都 ~k——同尺度？")
    for n in [2**5, 2**10, 3**5, (2*3*5*7*11)**1, 2**5*3**5]:
        print(f"   n={n}: Ω={omega(n)}——log n={log(n):.1f}——比值 Ω/log n = {omega(n)/log(n):.4f}")
    
    # 关键：Ω(n) vs log n 的标度——Ω ~ log n/log log n（平均——）——不是线性
    # "组合尺度"（Ω——）和"分辨尺度"（log n——）不是同一标度！
    print("\n2. 标度分析:")
    print("   Ω(n) 平均 ~ log log n（Hardy-Ramanujan——）")
    print("   log n ~ log n")
    print("   ——两尺度的'维数'——d = Ω/log n ~ 1/log log n → 0？")
    print("   ——不是 d 和 1−d 的对偶结构——不匹配唐先生框架——")
    
    # 候选 2：除数的 log 分布——自对偶（模板 4——）
    print("\n3. 除数 log 分布的自对偶:")
    for n in [12, 60, 360]:
        ds = divisors_list(n)
        logs = sorted([log(d) for d in ds])
        mid = (log(1) + log(n))/2
        # 除数 log 的均值
        mean_log = sum(logs)/len(logs)
        print(f"   n={n}: 除数 log 均值 = {mean_log:.4f}——中点 ½log n = {0.5*log(n):.4f}——差 = {mean_log-0.5*log(n):.2e}")
    
    # 候选 3：真正检查——是否有"两套独立约束"在整数上——给兼容点 ½
    print("\n4. 兼容性检查——什么约束在整数上'两尺度'？")
    print("   (a) 素数性（不可分解——）——局部——")
    print("   (b) 位置（大小——）——整体——")
    print("   兼容：素数在 [1,x] 的分布——π(x)~x/log x——PNT——无条件")
    print("   ——但 PNT 无 ½——误差项（RH——）才有 ½——")
    print("   ——'约束'（筛法——）给主项——不给误差的 ½——")

if __name__ == "__main__":
    main()
