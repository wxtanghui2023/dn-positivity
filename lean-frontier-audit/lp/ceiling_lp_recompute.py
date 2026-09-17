#!/usr/bin/env python3
"""CEILING-LP-RECOMPUTE (2026-09-17) — 前沿带宽一证书天花板 0.6818287 的独立重算尝试.

§1 精确解析 LawN256.lean 的 256 组封闭区间 + 行条件 τ（精确有理数）
§2 精确读出文件头记录的目标值 p0 = 1 - a_N + 三项一致性检查
§3 唯一可硬算的刚性关系（网格对齐律被 Parseval 锁死）
§4 对偶侧 LP（盒松弛）：δ_box(M) = max_v [ ∫ r x dx − B_box(A v) ]
§5 解析候选窗的缺陷（高精度积分 vs Riemann 和）
§6 (β) 反推：命中 0.6818287 所需的 p_min，与 §7.2(b) 极值 2/3 对照
诚实边界：marks 几何（p 与 S 的耦合）不在 Lean 内，也不在本地；本脚本不编造它。
"""
from fractions import Fraction as F
import re, json
import numpy as np
from scipy.optimize import linprog
from scipy.integrate import quad

LEAN = "/home/node/.openclaw/workspace/dn-project/lean-frontier-audit/LawN256.lean"
OUTJ = "/home/node/.openclaw/workspace/dn-project/lean-frontier-audit/lp/ceiling_lp_recompute_out.json"
N = 256
K = 2 ** 140
TARGET = F(6818287, 10 ** 7)                                   # 0.6818287（散文/任务）
P0_EXACT = F(10909258999421303588095230195816054408197,
             16000000000000000000000000000000000000000)        # LawN256.lean 头部 p0 = 1 - a_N
D1 = F(82395317, 10 ** 8)                                      # RowCert: d1
TAU = F(3, 10 ** 40)                                           # RowCert: τ
THIRD = F(2, 3)

out = {}
def hr(t=""):
    print("\n" + "=" * 78 + ("\n" + t if t else "") + "\n" + "=" * 78)

# ---------------------------------------------------------------- §1
hr("§1 封闭区间解析与行条件（精确有理数）")
src = open(LEAN, encoding="utf-8").read()
body = re.search(r"encl\s*:=\s*\[(.*?)\]\s*\n", src, re.S).group(1)
encl = [(int(a), int(b)) for a, b in re.findall(r"\((-?\d+)\s*,\s*(-?\d+)\)", body)]
assert len(encl) == 256, len(encl)
print(f"解析到 {len(encl)} 组 [lo_j, hi_j]（K·S(j) 的区间端点），K = 2^140")
tau_seen = F(0)
tight_lo = 0
for j in range(1, N):
    lo, hi = encl[j - 1]
    a = abs(F(N * lo, K) - j); b = abs(F(N * hi, K) - j)
    tau_seen = max(tau_seen, a, b)
    if a == 0: tight_lo += 1
print(f"实测 max_(0<j<256) max_endpoint |N·S(j) − j| = {float(tau_seen):.6e}")
print(f"   = {tau_seen}")
print(f"前沿声称 τ = 3e-40 ⟹ 行条件 {'成立 ✓' if tau_seen <= TAU else '不成立 ✗'}"
      f"（实测/声称 = {float(tau_seen / TAU):.4f}，即实际更紧）")
print(f"lo 端点恰等于 j/256（偏差 0）的行数: {tight_lo}/{N-1}")
out["tau_max"] = str(tau_seen)

# ---------------------------------------------------------------- §2
hr("§2 记录值 p0 与三项一致性检查")
print(f"p0 = 1 − a_N = {P0_EXACT}")
print(f"            = {float(P0_EXACT):.15f}")
print(f"散文目标 0.6818287 = {float(TARGET):.7f}")
print(f"① 'rounded up, p0 ≤ 0.6818287': "
      f"{'成立 ✓' if P0_EXACT <= TARGET else '不成立 ✗'} (差 {float(TARGET - P0_EXACT):.3e})")
print(f"② '2/3 距其方法天花板 <0.016': 0.6818287 − 2/3 = {float(TARGET - THIRD):.7f} ✓")
Tmax = sum(F(int(e[1]), K) for e in encl)                    # 盒最坏 T_N = Σ hi_j/K
Sl = Tmax / N
S256 = F(int(encl[-1][1]), K)
print(f"③ d1 复现: 盒最坏 Σ_j s_j = T_N/N = {float(Sl):.14f}; "
      f"D(1) = {float(Sl - F(1,2)):.14f} vs d1 = {float(D1):.8f} (差 {float(Sl-F(1,2)-D1):.2e})")
print(f"   S(256)（盒上端）= {float(S256):.6f}")
out["p0"] = str(P0_EXACT); out["S256_box_hi"] = float(S256); out["sum_s_worst"] = float(Sl)

# ---------------------------------------------------------------- §3
hr("§3 刚性关系：网格对齐标记律（x_i ∈ Z）")
print("若所有 x_{c,i} ∈ {0..255}，则 M_k = Σ_{i:x_i=k} m_{c,i}, Σ M_k = N, n2 = #{M_k = 2}:")
print("  Parseval: Σ_{j=1}^{256} S(j) = (1/256)Σ_{j=0}^{255}|DFT M(j)|² = Σ_k M_k² = N + 2n2 = N(2 − p)")
rows_sum = F(sum(range(1, N)), N)                    # Σ_{j<N} j/256 = 127.5
for lab, SN in (("S(N)=1 (sine-kernel 端值)", F(1)), (f"S(N)=盒上端 {float(S256):.3f}", S256)):
    p = 2 - (rows_sum + SN) / N
    print(f"  {lab:28s} ⟹ p = {float(p):.9f}")
print(f"  记录值 p0 = {float(P0_EXACT):.9f} 与 2/3 = {float(THIRD):.7f} 均不在此二值上")
# 追加：整数位置恒有 S(N) = |Σm_i|²/N = N = 256（因为 e^{2πi·256·x_i/256} = 1），
# 而公布包络给 S(256) = 211.432 ⟹ 最优律位置必非整数（仅由 Lean 数据即可判定）
SN_int = F(N)                                     # 整数位置律：S(N) = N = 256
p_int = 2 - (rows_sum + SN_int) / N
print(f"  追加（不依赖 Parseval 求和约定）：整数位置律恒有 S(N)=N=256 ⟹ p = {float(p_int):.9f}")
print(f"     而公布包络 j=256 给 S(256) = {float(S256):.6f} ≠ 256（差 {float(F(N)-S256):.3f}）")
print(f"     ⟹ 最优律的原子位置 **必不为整数**（mod 256）—— 仅由 Lean 数据即可判定 ✓✓")
out["p_if_integer_positions"] = float(p_int)
print("  ⟹ 可硬算的结论：最优律**非网格对齐**（位置必为非整数有理数，与 docstring 逐字一致），")
print("     故 Parseval 不适用，p 与 S 之间**没有**可硬算的刚性耦合 ⟹ 这正是缺失的 marks 几何。")
out["p_grid_SN1"] = float(2 - (rows_sum + F(1)) / N)
out["p_grid_SNbox"] = float(2 - (rows_sum + S256) / N)

# ---------------------------------------------------------------- §4
hr("§4 对偶侧 LP（盒松弛）：δ_box(M) = max_r [ ∫ r x dx − B_box(r) ]")
hj = np.array([int(e[1]) / K for e in encl], dtype=float)      # ≈ j/256
grid = np.arange(1, N + 1) / N
print("B_box(r) = (1/N)Σ_j h_j r(j/N) + (1/(N·K))·Σ_j max(0, −r(j/N))   [盒内最坏]")
print("真实 LP 值 = p_min + δ_box（δ_box ≥ 0 = 盒松弛富余）；band-limited 窗取 r(1)=0。\n")

def pl_matrix(M):
    """分段线性 hat 基: 节点 t_i = i/M, 宽度 h = 1/M。
       A[j,i] = φ_i(j/N)（网格插值值）,  W[i] = ∫₀¹ φ_i(x)·x dx（闭式，避免 quad 在折点上失准）。"""
    t = np.arange(M + 1) / M
    h = 1.0 / M
    A = np.maximum(0.0, 1.0 - np.abs(grid[:, None] - t[None, :]) / h)   # [N, M+1]
    W = np.empty(M + 1)
    for i, ti in enumerate(t):
        a = max(0.0, ti - h); b = min(1.0, ti + h)
        # ∫_a^{ti} ((x−a)/h)x dx + ∫_{ti}^{b} ((b−x)/h)x dx
        def seg(p0, p1, lin):          # lin(x) = (x−a)/h 或 (b−x)/h
            if p1 <= p0: return 0.0
            m = lin(p0); n = lin(p1)
            L = p1 - p0
            return m * (p1 ** 2 - p0 ** 2) / 2 + ((n - m) / L) * ((p1 ** 3 - p0 ** 3) / 3 - p0 * (p1 ** 2 - p0 ** 2) / 2)
        W[i] = (seg(a, ti, lambda x: (x - a) / h) + seg(ti, b, lambda x: (b - x) / h))
    return t, A, W

def solve_delta(M, B=8.2, band_limited=True, verbose=False, r0_zero=False):
    """对偶侧 LP（盒松弛）: max_{r} [ ∫₀¹ r(x)x dx − B_box(r) ] =: δ_box。

    记号: 节点 t_i=i/M, 值 v_i, 斜率 s_k=(v_{k+1}−v_k)/h, h=1/M,
          故 v_i = v0 + h·Σ_{k<i} s_k,  v_M = r(1)。
    B_box(r) = (1/N)Σ_j h_j r(j/N) + (1/(N·K))·Σ_j max(0, −r(j/N))   （盒内最坏）
    正则（前沿口径）: |r′(1)| + ∫₀¹|r″| = |s_{M−1}| + Σ_{k≥1}|s_k − s_{k−1}| ≤ B
    band-limited: r(1) = 0。
    """
    t, A, W = pl_matrix(M)
    h = 1.0 / M
    ns, ncon, nw = M, N, M - 1
    offs = 1                       # [v0 | s | u | w | tM]
    offu = offs + ns
    offw = offu + ncon
    offT = offw + nw
    n = offT + 1
    tail = np.cumsum(W[::-1])[::-1]                 # tail[k] = Σ_{i≥k} W_i
    rowsum = A.sum(axis=1)                          # Σ_i A_ji
    suf = np.array([float((hj / N) @ A[:, k + 1:].sum(axis=1)) for k in range(ns)])
    # 目标: maximize (W·v) − B_box → min −(...)
    c = np.zeros(n)
    c[0] = float(A.sum(0)[0] * 0)                   # placeholder (下面重设)
    c[0] = float((hj / N) @ rowsum) - float(W.sum())
    c[offs:offs+ns] = h * suf - h * tail[1:]
    c[offu:offu+ncon] = 1.0 / (N * K)
    rows_ub, rhs_ub = [], []
    # u_j ≥ −(Av)_j
    M1 = np.zeros((ncon, n))
    M1[:, 0] = -rowsum
    for k in range(ns):
        M1[:, offs + k] = -h * A[:, k + 1:].sum(axis=1)
    M1[:, offu:offu+ncon] = -np.eye(ncon)
    rows_ub.append(M1); rhs_ub.append(np.zeros(ncon))
    # |s_{M−1}| ≤ tM
    for sgn in (1.0, -1.0):
        r = np.zeros(n); r[offs+ns-1] = sgn; r[offT] = 1.0
        rows_ub.append(-r[None, :]); rhs_ub.append(np.array([0.0]))
    # |s_i − s_{i−1}| ≤ w_i
    for i in range(1, ns):
        for sgn in (1.0, -1.0):
            r = np.zeros(n); r[offs+i] = sgn; r[offs+i-1] = -sgn; r[offw+i-1] = 1.0
            rows_ub.append(-r[None, :]); rhs_ub.append(np.array([0.0]))
    # tM + Σ w ≤ B
    r = np.zeros(n); r[offT] = 1.0; r[offw:offw+nw] = 1.0
    rows_ub.append(r[None, :]); rhs_ub.append(np.array([B]))
    rows_eq, rhs_eq = [], []
    if band_limited:                                # r(1) = v0 + hΣ_k s_k = 0
        r = np.zeros(n); r[0] = 1.0; r[offs:offs+ns] = h
        rows_eq.append(r[None, :]); rhs_eq.append(np.array([0.0]))
    if r0_zero:
        r = np.zeros(n); r[0] = 1.0
        rows_eq.append(r[None, :]); rhs_eq.append(np.array([0.0]))
    A_ub = np.vstack(rows_ub); b_ub = np.concatenate(rhs_ub)
    kw = {}
    if rows_eq:
        kw["A_eq"] = np.vstack(rows_eq); kw["b_eq"] = np.concatenate(rhs_eq)
    bounds = [(None, None)] * (1 + ns) + [(0, None)] * (ncon + nw + 1)
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs", **kw)
    assert res.success, res.message
    v0 = res.x[0]; sl = res.x[offs:offs+ns]
    v = np.array([v0 + h * sl[:i].sum() for i in range(M + 1)])
    d = -res.fun
    if verbose:
        sv = abs(sl[-1]) + res.x[offw:offw+nw].sum()
        print(f"   M={M:3d}: δ_box = {d:+.5e}   |r′(1)|+∫|r″| = {sv:.4f}"
              f"   r(0) = {v[0]:+.4f}  r(1) = {v[-1]:+.2e}   max|r| = {np.max(np.abs(v)):.4f}")
    return d, v, W

def delta_of_r(fvals, W=None, M=None):
    """给定 r 在节点上的值, 直接算 ∫rx − B_box(r)（用于验证 LP 实现）"""
    M = len(fvals) - 1
    t, A, W = pl_matrix(M)
    v = np.asarray(fvals, float)
    rj = A @ v
    integral = float(W @ v)
    bbox = float((hj / N) @ rj) + float(np.maximum(0, -rj).sum()) / (N * K)
    return integral - bbox

print("（无正则化版本已实测为无界 ⟹ 必须按前沿口径加 |r′(1)|+∫|r″| ≤ B；下同）")
print("  验证 LP 实现（band-limited 解析候选，B=8.2 不绑）:")
for nm, f in (("1 − x²", lambda x: 1 - x * x), ("1 − x", lambda x: 1 - x),
              ("x(1 − x)", lambda x: x * (1 - x)), ("(1 − x)²", lambda x: (1 - x) ** 2)):
    Mv = 100
    fv = np.array([f(i / Mv) for i in range(Mv + 1)])
    d_direct = delta_of_r(fv)
    d_lp, v_lp, _ = solve_delta(Mv, B=8.2, band_limited=True)
    print(f"    r = {nm:10s}: 直接算 δ = {d_direct:+.6e} ; LP δ = {d_lp:+.6e}"
          f" ; 差 = {d_lp - d_direct:+.2e}")
print()
for B in (8.2, 1.0):
    print(f"  --- 正则上界 B = {B} ---")
    for M in (20, 50, 100):
        d_bl, v_bl, W = solve_delta(M, B=B, band_limited=True, verbose=True)
        out[f"delta_box_B{B}_M{M}_bandlimited"] = d_bl
    # r(1) 自由（= 用上 0.824|r(1)| 惩罚的通道）
    try:
        d_fr, _, _ = solve_delta(100, B=B, band_limited=False)
        print(f"        r(1) 自由时 δ_box(100) = {d_fr:+.4e}")
    except AssertionError as e:
        d_fr = None
        print(f"        r(1) 自由: LP **无界**（{str(e).splitlines()[0]}）⟹ 与前沿 d₁|r(1)| 项一致：")
        print(f"                   证书值可随 r(1)→∞ 无限增长，故必须取 r(1)=0（band-limited）。")
    out[f"delta_box_B{B}_free"] = d_fr

# ---------------------------------------------------------------- §5
hr("§5 解析候选窗的缺陷（r(1)=0；∫ 用高精度求积，Riemann 和用盒上端 h_j）")
def defect(f, name):
    I = quad(lambda x: x * f(x), 0, 1, epsabs=1e-14, epsrel=1e-14)[0]
    R = sum(hj[j - 1] / N * f(grid[j - 1]) for j in range(1, N + 1))
    print(f"  r(x) = {name:10s}: ∫ r x dx = {I:.10f};  (1/N)Σ h_j r(j/N) = {R:.10f};  缺陷 = {I - R:+.4e}")
    return I - R
for f, nm in [(lambda x: 1 - x * x, "1 − x²"), (lambda x: x * (1 - x), "x(1−x)"),
              (lambda x: 1 - x, "1 − x"), (lambda x: 1 - x ** 4, "1 − x⁴"),
              (lambda x: (1 - x) ** 2, "(1−x)²")]:
    out[f"defect_{nm}"] = defect(f, nm)

# ---------------------------------------------------------------- §6
hr("§6 (β) 反推：命中 0.6818287 所需的 p_min")
print("真实 LP 值 = p_min + δ_box；故 target = p_min + δ_box ⟹ p_min = target − δ_box\n")
for M in (20, 50, 100):
    d = out[f"delta_box_B8.2_M{M}_bandlimited"]
    print(f"  M={M:3d}: δ_box = {d:.4e}  ⟹  需 p_min = {float(TARGET) - d:.7f}"
          f"   (与记录 p0 差 {float(TARGET) - d - float(P0_EXACT):+.2e})")
d100 = out["delta_box_B8.2_M100_bandlimited"]
print(f"\n  与 §7.2(b) 极值 2/3 对照: target − 2/3 = {float(TARGET - THIRD):.7f}"
      f"  ≫  δ_box ≈ {d100:.1e}")
print("  ⟹ 目标**不能**写成 '2/3 + 证书缺陷'（缺陷小 ~1e-5～1e-3 量级）；")
print("     所以 p_min 本身必须 ≈0.6818，而记录值 p0 = 1 − a_N 正落在此 —— 说明")
print("     目标值 = 律自身的简单点比例 = primal LP 最优值；证书侧（对偶）只是它的重述。")

json.dump(out, open(OUTJ, "w"), indent=1, ensure_ascii=False)
print(f"\n[已存] {OUTJ}")
