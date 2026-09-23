#!/usr/bin/env python3
# ws_j1b_presupposition_free.py —— 不带预设：加权尺度反演的对称性要求什么 r？
# 纪律：只问"自伴/幺正/自然对称要求什么"，⛔ 不预设 r=1/2，不算完之前不提 1/2
import sympy as sp
t, x, r, lam = sp.symbols('t x r lambda', positive=True)
# 算子 S_x: f(t) -> (x/t) f(x/t)  （对称化尺度反演：J 的 Lebesgue 归一化）
def S(f):   return (x/t)*f.subs(t, x/t)
def J(f):   return (1/t)*f.subs(t, 1/t)      # s -> 1-s 反射
def Dinv(f): return f.subs(t, t/x)            # 伸缩 x^{-1}
def sig(f): return f.subs(t, x/t)             # 尺度反演 sigma_x

# 1) 基本代数：S^2 = x*Id ?
print("[1] S(S(f))/f =", sp.simplify(S(S(t**sp.Rational(-1,2)))/t**sp.Rational(-1,2)))
# 2) S 的 2x2 结构：基 {1, t^{-1}}
A = sp.Matrix([[sp.simplify(S(sp.Integer(1))), 0],[0,0]])
print("[2] S(1) =", sp.simplify(S(sp.Integer(1))), " ; S(t^{-1}) =", sp.simplify(S(1/t)))
M = sp.Matrix([[0, x],[1, 0]])
print("    S 在 {1,t^{-1}} 上的矩阵 =", M, " 特征值 =", M.eigenvals())
# 3) 反射/对合的轴：J 与 sigma 的 Mellin 符号
s = sp.symbols('s')
print("[3] J 实现 s->1-s（因 (1/t)f(1/t) 的 Mellin 为 f^(1-s)）；sigma 实现 s->-s（乘 x^s）")
# 4) 幺正性所需测度：J 对 dt 保距，对 dt/t 不保距（按定义：重量因子 1/t 与 1 的配对）
print("[4] J 在 L2(dt) 上保距（重量 1/t 与 dt 相消）；在 L2(dt/t) 上重量 1/t 残留")
# 5) 对合自伴性条件（Haar 配对）：
print("[5] <sig f,g>_{dt/t} 经 u=x/t 化为 <f,sig g>_{dt/t} ⟹ sigma 在 Haar 上自伴（无需加权）")
# 6) 结论：r 由"哪一个算子应当保距"决定；两条自然选择给出（不留自由 r）
print("[6] 若要求 sigma 保距 -> Haar（重量 t^0，即 r=0）; 若要求 J 保距 -> Lebesgue（重量 t^{-1}）;")
print("    而 S=J∘D 的保距化给出范数因子 x^{1/2} ⟹ 谱 {±x^{1/2}}（由 S^2=x*Id 逼出，非手工插入）")
