#!/usr/bin/env python3
"""
RP_2 远场证书（M=2 的 (RP_M) 第二段）—— 双精度 + 显式误差界，可复现
目标：在 (60°,90°) 与 (90°,60°) 的方形邻域（半宽 R）之外，
      g(phi1,phi2)=max_{1<=k<=10}[cos(k phi1)+cos(k phi2)] >= 1/2（实际强得多）
严格性来源：
  (a) Lipschitz：F_k 的梯度 <= k*sqrt2 <= 10*sqrt2 =: L；g = max_k F_k 故 Lip(g) <= L
      单元内任意点与中心距离 <= h*sqrt2/2  ⟹  |g(x)-g(center)| <= L*h*sqrt2/2
  (b) 求值误差：IEEE 双精度 cos 每项 <=1 ulp(~2.3e-16)，10 项求和 <=1e-15；
      取保守上界 EVAL_ERR = 1e-12
  (c) 排除区域：取"与方形相交的单元"，故被认证区域 ⊂ 方形之外 ⟹ 安全性单向
输出：认证下界 + 覆盖包含检查（参数见 C-153：c/32 = 3.6726996°）
"""
import sys
import numpy as np

K = 10
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
R_DEG = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
L = K * np.sqrt(2.0)                 # = 14.1421356...
EVAL_ERR = 1e-12
C32_DEG = 7 * np.sqrt(1677.0) / 4472 * 180 / np.pi   # c/32（度）

h = np.pi / N
ax = (np.arange(N) + 0.5) * h
P1, P2 = np.meshgrid(ax, ax, indexing='ij')
G = np.full_like(P1, -9.0)
for k in range(1, K + 1):
    G = np.maximum(G, np.cos(k * P1) + np.cos(k * P2))

D1 = np.degrees(P1) - 60.0
D2 = np.degrees(P2) - 90.0
excl = R_DEG + np.degrees(h) / 2.0            # 单元中心到方形边界的安全内缩
inA = (np.abs(D1) <= excl) & (np.abs(D2) <= excl)
inB = (np.abs(D1 - 30.0) <= excl) & (np.abs(D2 + 30.0) <= excl)   # 交换点 (90,60)：phi1-90=D1-30, phi2-60=D2+30
mask = ~(inA | inB)
lip = L * h * np.sqrt(2.0) / 2.0
best = G[mask].min()
idx = np.unravel_index(np.argmin(np.where(mask, G, 9.0)), G.shape)
cert = best - lip - EVAL_ERR
corner = excl * np.sqrt(2.0)

print(f"N={N}  h={h:.8f} rad ({np.degrees(h):.5f}°)  L={L:.7f}")
print(f"排除方形有效半宽 excl = {excl:.4f}°  (= R {R_DEG}° + h/2)")
print(f"邻域外网格最小 g = {best:.9f}   在 (phi1,phi2) = ({np.degrees(ax[idx[0]]):.3f}°, {np.degrees(ax[idx[1]]):.3f}°)")
print(f"单元 Lipschitz 余项 = {lip:.9f}   求值误差界 = {EVAL_ERR:.1e}")
print(f"★ 认证下界 = {cert:.9f}    > 1/2 ? {cert > 0.5}")
print()
print(f"覆盖包含检查：排除方形对角 = {corner:.4f}°  vs  c/32 = {C32_DEG:.4f}°   ⟹ 方形 ⊂ 局部盘 ? {corner < C32_DEG}")
print(f"（余量 {C32_DEG - corner:.4f}°；且 c/32 > 1° 由 C-153 精确核过）")
