#!/usr/bin/env python3
"""整数环格的 shape 探索——trace form 特征值散布（非 covolume——）
问题：O_L 的 trace form（T_ij = Tr(e_i e_j)——整基——）的谱散布
（λ_max/λ_min 类——形状——）是否含非局部/非乘性内容？
——det = 判别式（乘性——covolume——）——散布 = 形状（——）——
对塔（Q ⊂ L ⊂ M——）看散布的 tower 行为
"""
import numpy as np

def trace_form_integral_basis(conjs_of_basis, conj_map):
    """整基 {e_i}——Gram_ij = Σ_k σ_k(e_i)σ_k(e_j)（对全实——共轭——）
    conjs_of_basis[i][k] = σ_k(e_i)——"""
    n = len(conjs_of_basis)
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            G[i, j] = sum(conjs_of_basis[i][k] * conjs_of_basis[j][k] for k in range(len(conjs_of_basis[i])))
    return G

# ===== Q(√2)——全实——整基 {1, √2} =====
print('=== Q(√2)——O = Z[√2]——基 {1,√2} ===')
s2 = np.sqrt(2)
G = trace_form_integral_basis([[1,1],[s2,-s2]], None)  # σ₁=+√2 作用 e=1→1, √2→√2；σ₂
# 上面错误——重做：conjs[i][k] = σ_k(e_i)——e_0=1: σ=1,1——e_1=√2: √2,-√2
G = np.array([[1*1+1*1, 1*s2+1*(-s2)], [1*s2+1*(-s2), s2*s2+(-s2)*(-s2)]])
print(f'Gram = {G}')
ev = np.linalg.eigvalsh(G)
print(f'特征值 = {ev}——散布 λmax/λmin = {ev[-1]/ev[0]:.4f}——det = {np.linalg.det(G):.1f}')
print(f'判别式 Δ = det = {np.linalg.det(G):.1f}（应 8——）')

# ===== Q(∛2)——整基 {1, ∛2, ∛4}——一个实 + 复对 =====
print()
print('=== Q(∛2)——基 {1,∛2,∛4} ===')
cr = 2**(1/3)
w = -0.5 + 0.86602540378j
conjs = [cr, cr*w, cr*w**2]  # σ(∛2) 的三个值
# 整基 e_0=1, e_1=∛2, e_2=∛4——σ_k(e_j) = σ_k(∛2)^j
V = np.array([[c**j for c in conjs] for j in range(3)])  # V[j][k] = σ_k(e_j)
G3 = V @ V.conj().T  # Σ_k σ_k(e_i) conj(σ_k(e_j))
print(f'Gram = {np.round(G3.real,3)}')
ev3 = np.linalg.eigvalsh(G3.real)
print(f'特征值 = {np.round(ev3,4)}——散布 = {ev3[-1]/ev3[0]:.4f}')
print(f'det = {np.linalg.det(G3):.4f}（判别式应 -108 的 |·| 类——）')

# ===== Q(√2,√3)——整基 {1,√2,√3,√6}——全实 =====
print()
print('=== Q(√2,√3)——基 {1,√2,√3,√6} ===')
# 共轭：σ(a+b√2+c√3+d√6) = a ± b√2 ± c√3 ± d√6——4 个（全实——）
conj4 = []
for s2s in [1,-1]:
    for s3s in [1,-1]:
        conj4.append(lambda x, s2s=s2s, s3s=s3s: x[0]+s2s*x[1]*np.sqrt(2)+s3s*x[2]*np.sqrt(3)+s2s*s3s*x[3]*np.sqrt(6))
basis = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
G4 = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        G4[i,j] = sum(conj4[k](basis[i])*conj4[k](basis[j]) for k in range(4))
print(f'Gram = {np.round(G4,2)}')
ev4 = np.linalg.eigvalsh(G4)
print(f'特征值 = {np.round(ev4,4)}——散布 = {ev4[-1]/ev4[0]:.4f}')
print(f'det = {np.linalg.det(G4):.2f}（判别式应 8²·3²=576 类——）')

# ===== 塔比较：Q ⊂ Q(√2) ⊂ Q(√2,√3)——形状（散布）的 tower 行为 =====
print()
print('=== 塔的散布比较（非乘性——？）===')
spr2 = ev[-1]/ev[0]  # Q(√2)
spr4 = ev4[-1]/ev4[0]  # Q(√2,√3)
print(f'散布 Q(√2) = {spr2:.4f}——散布 Q(√2,√3) = {spr4:.4f}')
print(f'散布比（Q(√2,√3)/Q(√2)——）= {spr4/spr2:.4f}')
# 如果是乘性/判别式类——散布² ~ Δ^{1/n} 类——检查
print(f'（若乘性——散布应 ~ Δ 的幂的组合——这里比较——）')
# Q(√2) 的 Δ=8——Q(√2,√3) 的 Δ=576——(576/8)^{1/2} = 8.5？——散布比 2.6/2 = 1.3？——非乘性
print(f'  判别式比 (576/8) = 72——散布比 = {spr4/spr2:.3f}——（散布比 ≪ 判别式比——非乘性——）')
