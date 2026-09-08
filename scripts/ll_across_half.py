#!/usr/bin/env python3
# ζ'/ζ（素数运动）沿 σ 穿过 σ=1/2——多高度（零点 vs 非零点——）——看 σ=1/2 是否普适特征
import mpmath as mp
mp.mp.dps = 12

def L(s):
    """ζ'/ζ = d/ds log ζ"""
    return mp.diff(mp.zeta, s)/mp.zeta(s)

print("=== Re[ζ'/ζ] 沿 σ 穿过 σ=1/2——多高度 ===")
print("（零点高度 γ1=14.13, γ2=21.02——非零点 16, 18, 23——）")
heights = [14.1347, 16.0, 18.0, 21.022, 23.0, 25.01]
for t in heights:
    print(f"t={t}:")
    for sg in [0.7, 0.6, 0.55, 0.52, 0.5, 0.48, 0.45, 0.4]:
        try:
            v = L(complex(sg, t))
            print(f"  σ={sg:.2f}: Re={float(v.real):+10.3f}  Im={float(v.imag):+8.3f}")
        except Exception as e:
            print(f"  σ={sg:.2f}: 极点/错误")
    print()

print("=== 关键：σ=1/2 处 Re[ζ'/ζ] 的符号/发散（所有高度——）===")
for t in heights:
    for sg in [0.51, 0.5, 0.49]:
        try:
            v = L(complex(sg, t))
            print(f"  t={t}: σ={sg}: Re={float(v.real):+12.3f}")
        except:
            print(f"  t={t}: σ={sg}: 极点")
    print()
