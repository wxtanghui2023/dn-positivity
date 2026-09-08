#!/usr/bin/env python3
"""
定理 A 的 f_n 族 vs M(T)——覆盖检验
定理 A：∫ f_n(t)S(t)g(t)dt = O(1) 对所有 n（无条件——）
f_n = 4sin²(n·θ₁(t))——θ₁ = arctan(1/(2t))——g = 2π/(t log²(t/2π))

如果 f_n·g 族能"逼近" M(T) 的权重（1_[0,T]——）——M(T) 的 O(1) 可从定理 A 推
但定理 A 已证——若真能推——Lindelöf 已被证（不可能）——所以必有缺口
检验：f_n·g 的累积权重形状——能否覆盖 [0,T] 的长区间？
"""
import numpy as np
from math import log, pi

def main():
    print("="*70)
    print("定理 A f_n 族覆盖检验")
    print("="*70)
    
    # f_n(t) = 4sin²(n·θ₁(t))——θ₁ = arctan(1/(2t))
    # g(t) = 2π/(t·log²(t/2π))
    # 权重 w_n(t) = f_n(t)·g(t)
    
    ts = np.linspace(15, 2000, 20000)
    g = 2*pi/(ts * np.log(ts/(2*pi))**2)
    
    # 不同 n 的 f_n
    for n in [1, 10, 100, 1000]:
        theta1 = np.arctan(1/(2*ts))
        fn = 4*np.sin(n*theta1)**2
        wn = fn * g
        # 权重形状——累积
        cum = np.cumsum(wn) * (ts[1]-ts[0])
        print(f"\nn={n}: f_n·g 的累积积分 = {cum[-1]:.4f}（到 t=2000——）")
        print(f"   max|f_n·g| = {np.abs(wn).max():.4f}——在 t={ts[np.argmax(np.abs(wn))]:.0f}")
        # f_n 的振荡尺度（在哪 t 振荡快——）
        print(f"   （f_n 振荡——每零点穿越——需要看结构——）")
    
    # 关键：f_n·g 是"振荡权重"（正负交替——）——不是正权重（像 M 的 1_[0,T]——）
    # M(T) = ∫1_[0,T]·S——正权重——f_n·g 振荡（正负——）
    # 所以 f_n 族探测 S 的"振荡矩"——不是"裸累积"
    print("\n关键区别：")
    print("   M(T) 权重 1_[0,T]：恒正——测 S 的累积（漂移——）")
    print("   f_n·g 权重：振荡（正负——）——测 S 的振荡矩（~0——）")
    print("   ⟹ f_n 族不能直接给 M(T)——测的是不同结构")
    
    # 但——f_n 的"零频分量"？
    # f_n = 4sin²(nθ₁) = 2 - 2cos(2nθ₁)——常数部分 2——振荡部分 -2cos(2nθ₁)
    # ∫f_n·S·g = 2∫S·g - 2∫cos(2nθ₁)S·g
    # ——第一部分 2∫S·g（n 无关——）——第二部分振荡（n 依赖——）
    print("\nf_n = 2 - 2cos(2nθ₁)——常数部分 2：")
    print(f"   ∫S·g（n 无关部分——）——g 衰减——∫S·g 应该 O(1)？")
    # ∫S·g 数值——用零点数据
    print(f"   如果 ∫S·g = O(1)（g 衰减——）——那已经是加权 M（g 权重——）")
    print(f"   与 M(T)（1_[0,T] 权重——）不同——g 衰减快（1/(t log²t)——）")
    print(f"   g 的主要质量在 t ~ 15-100——不是大 T——")

if __name__ == "__main__":
    main()
