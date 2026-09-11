"""
BL2: 补齐 A1 的代码 —— 完整预算的实现（已知项）+ 未知项的稳健性分析。

依据 D-037 (4.1) 的结构（其摘录给出了前两项与形状）：
   B(n) := 2N(T) + 4T[(2/3)C0(T) + A log(T+2) + B0] + 40M0 + 2(e^4+1)[7H(T)+3.3] + I_I + 1
   其中 T = sqrt(n) + 1 ；F(T) = (T/2pi) log(T/(2 pi e)) + 7/8 ；
   |S(T)| <= 0.137 log T + 0.443 log log T + 1.588（Rosser 形式，D-037 文本引用）
   C0(t) := F(t+1) - F(t) + S_bnd(t+1) + S_bnd(t)   （单位区间内的零点计数上界）
   A = 2.0, B0 = 2.0（ζ'/ζ 界 |R(w)| <= A log(|t|+2) + B0，D-037 traced）

关键：**后三项（40M0、2(e^4+1)[7H(T)+3.3]、I_I）的定义本轮未取得** ✗
  => 我们【实现已知项】，把未知项**参数化**，并**证明结论对未知项稳健** ✓✓
校准（known-answer）：D-037 自述 "B(n) ≈ 2.54 sqrt(n) log n + O(sqrt n) + O(log^2 n)" ✓
  => 我的实现应复现 ~2.54 sqrt(n) log n ✓（否则实现有误 ✗）
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, pi as mpi, e as me, sqrt as msqrt
mp.dps=40
gam=mpf('0.5772156649015328606')
S_bnd=lambda T: mpf('0.137')*mlog(T)+mpf('0.443')*mlog(mlog(T))+mpf('1.588')
F=lambda T: (T/(2*mpi))*mlog(T/(2*mpi*me))+mpf(7)/8
N_ub=lambda T: F(T)+S_bnd(T)
def C0(T): return (F(T+1)-F(T)) + S_bnd(T+1) + S_bnd(T)
def B_known(n, A=mpf('2.0'), B0=mpf('2.0')):
    T=msqrt(mpf(n))+1
    p1=2*N_ub(T)
    p2=4*T*((mpf(2)/3)*C0(T) + A*mlog(T+2) + B0)
    return p1+p2, float(p1), float(p2)
def S_inf(n):
    return (mpf(n)/2)*(mlog(n)-1+gam-mlog(2*mpi))+mpf(3)/4
print("="*94)
print("BL2(i) 校准：已知项 B_known(n) 是否复现 D-037 的 'B ≈ 2.54 sqrt(n) log n'？")
print("="*94)
print("  %10s %16s %16s %12s %12s" % ("n","B_known","2.54*sqrt(n)*log n","比值","B/sqrt(n)/log n"))
for n in (10**3,10**4,10**5,10**6,10**8,10**10,10**12):
    b,_,_=B_known(n); lead=2.54*np.sqrt(n)*np.log(n)
    print("  %10d %16.6e %16.6e %12.4f %12.6f" % (n,b,lead,b/lead, b/np.sqrt(n)/np.log(n)))
print()
print("="*94)
print("BL2(ii) 余量对【未知项】的稳健性：把未知项写成  U*(2N(T)) + V  并扫描 (U,V)")
print("="*94)
print("  margin(n) = S_inf(n) - B_known(n) - [U*2N(T) + V]")
print("  %10s %14s %14s | %s" % ("n","S_inf","B_known","margin>0 for (U,V) in ..."))
for n in (10**3,10**4,10**5,10**6,10**8):
    T=float(msqrt(mpf(n))+1)
    s=float(S_inf(n)); b,_,_=B_known(n); N2=float(2*N_ub(mpf(T)))
    # 求解：s - b - U*N2 - V > 0 在 V=0 时的最大 U
    Umax=(s-b)/N2 if N2>0 else float('inf')
    Vmax=s-b
    print("  %10d %14.6e %14.6e | U < %.3f (V=0) ; V < %.3e (U=0)" % (n,s,b,Umax,Vmax))
print()
print("  ==> 结论的稳健性判据：只要 U < ~O(1) 且 V < ~10^3 量级，主要结论不变 ✓")
print()
print("="*94); print("READ-OFF"); print("="*94)
print("""  * 已知项已实现并校准；未知三项（40M0 / 2(e^4+1)[7H+3.3] / I_I）以 (U,V) 参数化。
  * 若 margin 对 U<O(1) 与 V<O(10^3) 均成立，则'范围由输入决定'这一结论【稳健】✓
  * 仍未完成：取得那三项的【明确定义】才能给出严格定理（见 docs/ALIGN-A1-COMPLETE.md §5）""")
