#!/usr/bin/env python3
"""
P27-G8.1 重铸实验 v2：Lamzouri Bessel 风格 vs 我们 Sylvester 精确惯性

核心问题：
1. 我们的 n_-(K_rho) = 1（Sylvester——精确——系数矩阵 C 的性质——）vs
   Lamzouri 的 Bessel 三段式（不等式——）——各能看到什么？
2. β盲核（Lamzouri——平移不变）vs β敏感核（我们——绝对定位）对"离轴"的区分能力
3. 为什么 Lamzouri 的 2/3 与"少量离轴"相容（=我们的集体量 β盲）——数值演示

关键：C = I_4 ⊕ (-2σ_x)——n_-(C) = 1 是纯线性代数（不依赖具体测度）
"""
import numpy as np

def main():
    print("="*70)
    print("实验 1：Sylvester 精确惯性 n_-(C) = 1——系数矩阵的直接性质")
    print("="*70)
    # C = I_4 ⊕ (-2σ_x)
    C = np.zeros((6, 6))
    C[:4, :4] = np.eye(4)
    C[4:, 4:] = -2 * np.array([[0, 1], [1, 0]])
    eig_C = np.linalg.eigvalsh(C)
    print(f"C 特征值: {np.sort(eig_C)}")
    print(f"n_-(C) = {np.sum(eig_C < 0)}——n_+(C) = {np.sum(eig_C > 0)}——n_0 = {np.sum(abs(eig_C) < 1e-12)}")
    print(f"inertia(C) = (5, 1, 0)——n_- = 1 ✓（解析——不依赖测度）")
    
    # 负见证向量
    eigvecs = np.linalg.eigh(C)[1]
    x_neg = eigvecs[:, 0]
    print(f"\n负见证 x（C 最小特征向量）: {np.round(x_neg, 4)}")
    print(f"x*Cx = {x_neg @ C @ x_neg:.6f} < 0 ✓")
    # 见证的结构：x = (0,0,0,0, 1/√2, -1/√2)？——检查
    print(f"见证只在最后两分量（在线参考——ψ5,ψ6）非零: {np.sum(abs(x_neg[:4])) < 1e-10}")
    
    print("\n" + "="*70)
    print("实验 2：负方向的物理意义——见证向量 = ψ5 与 ψ6 的反相组合")
    print("="*70)
    # ψ5(u)=e^{(½+iγ)u}, ψ6(u)=e^{(½-iγ)u}——见证 g(u) = (ψ5 - ψ6)/√2 = i·e^{u/2}sin(γu)·√2
    # ⟨g, K_rho g⟩ < 0——离轴缺陷核在"在线参考振荡"上为负
    print("""
见证 g(u) = (1/√2)(ψ5 - ψ6) = i√2·e^{u/2}·sin(γu)
⟨g, K_rho g⟩ = -2·(1/√2)(1/√2)·2 = -2 < 0（交叉项 -2σ_x 的贡献）

物理意义：K_rho = 离轴缺陷核（cosh(δs)-1 项——正——）
            + 参考修正（-cos(γt) 项——负——）
负方向来自"参考修正"——不是来自离轴正项！
→ 离轴 quartet 的缺陷核 K_rho 不是正定的——有一个负方向——
  这个负方向"编码"了离轴的存在（δ≠0 时 C 有 -2 块——δ=0 时整块消失）
""")
    
    print("="*70)
    print("实验 3：β盲核（Lamzouri——）vs β敏感核（我们——）对离轴的区分")
    print("="*70)
    # Lamzouri：K(z-s) = η̂²(z-s)——平移不变——K(z-s) 只依赖差
    # 演示：对"在线对"（γ1,γ2）与"近线离轴对"（β=½+ε 的 γ1,γ2）——K 值几乎相同
    # 近线：ρ = ½+ε+iγ——z = i(ρ-½)logT/2π = iεlogT/2π - γlogT/2π——Re z = -εlogT/2π（极小）
    # 用高斯核 K(u) = e^{-u²}（示意——平移不变）
    def K_gauss(diff):
        return np.exp(-np.abs(diff)**2)
    
    # 模拟：在线零点对 vs 近线离轴零点对
    T = 1e6
    L = np.log(T)/(2*np.pi)
    g1, g2 = 14.13, 21.02
    # 在线：z = -γL（实——）——差 z1-z2 = -(γ1-γ2)L
    diff_online = -(g1-g2)*L
    # 近线离轴：ε = 1e-6——z = iεL - γL——差 ≈ 相同 + iεL
    eps = 1e-6
    diff_near = -(g1-g2)*L + 1j*eps*L
    print(f"T = {T:.0e}——L = logT/2π = {L:.1f}")
    print(f"在线对差: z1-z2 = {diff_online:.4f}——K = {K_gauss(diff_online):.6e}")
    print(f"近线对差: z1-z2 = {diff_online:.4f} + {eps*L:.4f}i——K = {K_gauss(diff_near):.6e}")
    print(f"K 值差: {abs(K_gauss(diff_online) - K_gauss(diff_near)):.2e}——几乎不可分！")
    print(f"→ β盲核无法区分'在线'与'ε=1e-6 的近线离轴'（连续依赖——）")
    print(f"→ 少量离轴对 ΣK² 贡献 ≈ 0——Lamzouri 2/3 与离轴相容 ✓")
    
    print("\n我们 β敏感核（示意——绝对定位）:")
    # 我们的"核"感测 δ = β-½——cosh(δu)-1 型——δ=0 时为零——δ≠0 时非零
    for d in [0, 1e-6, 1e-3, 0.1, 0.4]:
        # cosh(δ)-1 在 u=1 处的值（示意）
        val = np.cosh(d) - 1
        print(f"  δ={d:8.1e}: cosh(δ)-1 = {val:.4e}（δ=0 精确 0——δ≠0 非零——能区分！）")
    print("→ β敏感核在 δ=0 处精确为零（在线无信号）——δ≠0 非零（离轴有信号）")
    print("→ 但——β敏感核的代价：无无条件估计（Weil 正性墙——P28——）")

    print("\n" + "="*70)
    print("实验 4：Lamzouri 三段式 vs 我们的 n_-——信息极限对比")
    print("="*70)
    print("""
Lamzouri Prop 2.1（不等式——弱——无条件）：
  #简单实 >= 2|Z| - ΣK²——用 BGST（γ 层——）估 ΣK²——得 2/3
  特性：对"任何共轭不变 Z"成立——不需要知道哪些在线哪些离轴
  盲区：有限个离轴（β盲核看不到——）——O(1/N) 贡献

我们 G8.1（精确——强——条件性——）：
  n_-(K_rho) = 1——对"任何单离轴 quartet"成立
  特性：精确计数负方向（Sylvester——刚性——）
  代价：K_rho 是 β敏感核——无法无条件估计（需要知道离轴存在——）

形式对比：
  Lamzouri：Σ_z∈Z 1 的"实部计数下界"——一次对整个 Z（统计——）
  我们：    单 quartet 的"缺陷核惯性"——一次对一个轨道（局部——）
  
两者不能互相推出：
  - Lamzouri 的论证不含 β 信息——无法"看到"n_- = 1（需要 δ≠0 输入）
  - 我们的 n_- = 1 是局部的——不给出"多少比例在线"（需要求和——遇到相位——）
""")

if __name__ == "__main__":
    main()
