#!/usr/bin/env python3
"""[A_x, A_y] = [M_x*M_x, M_y*M_y] 的计算——内积依赖检查
问题：A_x = M_x*M_x 是否非平凡（非交换——）？
——如果内积是共轭不变的（Hermitian——<y,z>=Tr(y z̄)——）
  M_x* = M_{x̄}——A_x = M_{|x|²}（乘法——）→ 交换（L 交换——）→ 死
——如果内积是双线性的（全实——<y,z>=Tr(yz)——）——可能非零
测试：L = Q(√2)、Q(∛2)——两种内积——[A_x,A_y] 的 HS 范数
"""
import numpy as np

def mult_matrix(elems, x, basis_products=None):
    """乘 x 的矩阵（在基 elems——）——x = 系数向量"""
    n = len(elems)
    M = np.zeros((n, n))
    for j, e in enumerate(elems):
        # x * e_j = Σ_i coeff_i * (e_i * e_j)——需要乘法表
        prod = x @ e  # 用嵌入算（下面——）
    return M

# 用嵌入方法（更简单——）：L 的元素 → 共轭向量（σ_i(x)——）
# M_x 在"共轭基"是对角的（diag(σ_i(x))——）——但我们需要在"整基"（关于 trace 形式——）

def field_data(alpha_min_poly_roots):
    """L = Q(α)——α 的共轭 = roots——n = len——整基 {1, α, ..., α^{n-1}}（张成的 Q-空间——）
    返回：共轭矩阵 C（σ_i(α^j)——）——乘 x（系数 a）→ 共轭值 = C·(a 展开)"""
    pass

# 简单方式：直接构造 L = Q(θ)，θ = √2 或 ∛2——用幂基 {1,θ,...,θ^{n-1}}
# 元素 x = 系数向量 a——σ_i(x) = Σ_j a_j σ_i(θ)^j（σ_i(θ) = 共轭——）

def mult_op(a, roots):
    """乘 x（系数 a——）的矩阵（在幂基——）：x·θ^j = Σ_k c_k θ^k——"""
    n = len(roots)
    # x·θ^j 的系数（用最小多项式约化——）——用数值（幂基乘——）
    M = np.zeros((n, n))
    for j in range(n):
        # x * θ^j = Σ_i a_i θ^{i+j}——约化（θ^n = Σ c_k θ^k 用最小多项式——）
        # 数值：用共轭表示（乘 x 在共轭空间对角——再变回——）
        pass
    # 用 Vandermonde：V = [σ_i(θ)^j]——乘 x（系数 a）在共轭空间 = diag(σ_i(x))
    # 幂基系数 → 共轭值：c = V·a——乘 x（共轭——）→ 共轭基矩阵 = diag(σ_i(x))·V·a
    # 幂基矩阵：M_x = V^{-1} diag(σ_i(x)) V
    V = np.array([[r**j for j in range(n)] for r in roots])
    sx = V @ a  # σ_i(x)
    return np.linalg.inv(V) @ np.diag(sx) @ V

def trace_form_matrix(roots):
    """Gram（Tr(x y)——对全实/复——幂基——）：G_ij = Tr(θ^i θ^j) = Σ_k σ_k(θ)^i σ_k(θ)^j"""
    n = len(roots)
    V = np.array([[r**j for j in range(n)] for r in roots])
    return V.T @ V  # Σ_k σ_k(θ)^i σ_k(θ)^j——（对复的用共轭——这里全实/或复共轭修正——）

def commutator_HS(A, B):
    C = A @ B - B @ A
    return np.linalg.norm(C, 'fro')**2

# ===== 测试 1: L = Q(√2)——全实——n=2 =====
print('=== L = Q(√2)——n=2——===')
roots2 = [np.sqrt(2), -np.sqrt(2)]
G2 = trace_form_matrix(roots2)
print(f'Gram（Tr 形式——幂基——）= {G2}')
# 元素 x = 1+√2, y = √2
ax = np.array([1.0, 1.0]); ay = np.array([0.0, 1.0])
Mx = mult_op(ax, roots2); My = mult_op(ay, roots2)
print(f'M_x = {Mx}——M_y = {My}')
# 内积 1: Hermitian 共轭（<y,z> = Tr(y conj(z))——全实 = 双线性同——）
# 对全实——Tr 形式对称正定——A_x = G^{-1} M_x^T G M_x（关于内积的伴随——）
# 伴随（关于 <u,v> = u^T G v——）：M* = G^{-1} M^T G
def adjoint(M, G):
    return np.linalg.inv(G) @ M.T @ G
Ax = adjoint(Mx, G2) @ Mx
Ay = adjoint(My, G2) @ My
print(f'A_x = {np.round(Ax,4)}——A_y = {np.round(Ay,4)}')
print(f'[A_x,A_y] HS² = {commutator_HS(Ax, Ay):.6f}')
# 检查 A_x 是否 = M_{|x|²} 类（乘法——交换——）
print(f'A_x A_y − A_y A_x = {np.round(Ax@Ay - Ay@Ax, 6)}')
print()

# ===== 测试 2: L = Q(∛2)——n=3——（一个实共轭 + 一对复——）=====
print('=== L = Q(∛2)——n=3——===')
cr = 2**(1/3)
roots3 = [cr, cr*(-0.5+0.86602540378j), cr*(-0.5-0.86602540378j)]
# 复的——用 Hermitian（共轭——）
G3h = np.array([[sum(r**i * np.conj(r)**j for r in roots3) for j in range(3)] for i in range(3)])
print(f'Gram（Hermitian——）= {np.round(G3h,4)}')
ax3 = np.array([1.0, 1.0, 0.0]); ay3 = np.array([0.0, 1.0, 1.0])
Mx3 = mult_op(ax3, roots3); My3 = mult_op(ay3, roots3)
# Hermitian 伴随——M* = G^{-1} M^H G
def adjoint_h(M, G):
    return np.linalg.inv(G) @ M.conj().T @ G
Ax3 = adjoint_h(Mx3, G3h) @ Mx3
Ay3 = adjoint_h(My3, G3h) @ My3
print(f'[A_x,A_y] HS²（Hermitian——）= {commutator_HS(Ax3, Ay3):.6f}')
# A_x 是否 = M_{|x|²}？（如果 Hermitian 伴随 = 乘共轭——）
# |x|² = x·conj(x)（在 L——）= 系数（x̄ 的系数——共轭——）
print(f'A_x（应 = M_{{|x|²}} 若交换——）对角性: {np.round(Ax3,4)}')
# 双线性伴随（Tr(yz)——非共轭——）
G3b = np.array([[sum(r**i * r**j for r in roots3) for j in range(3)] for i in range(3)])
def adjoint_b(M, G):
    return np.linalg.inv(G) @ M.T @ G
Ax3b = adjoint_b(Mx3, G3b) @ Mx3
Ay3b = adjoint_b(My3, G3b) @ My3
print(f'[A_x,A_y] HS²（双线性 Tr——）= {commutator_HS(Ax3b, Ay3b):.6f}')
