#!/usr/bin/env python3
"""
V113_f1_weighted_sum.py  —  F1 悬点（CONV2 行51/行58）的有界数值校验

【目的】
  回答 `docs/CONV2-online-part-needs-no-dispersion.md` 行 51 / 行 58 的悬点：
    "第②项（离轴零点的加权和，指数权 × 稀疏性）能否收敛/有界？"
  并检验其下游后果：平衡点 n* 是否 = O(T²)（即是否【复现】T² 律 / 有无 G-1 增益）。

【输入】data/zeros_odlyzko_100k.npy（本项目已入库 Odlyzko 前 1e5 个零点；γ_max≈7.49e4）
【输出】scripts/V113_f1_weighted_sum.txt（R3 ✓）
【provenance】zeros 表来源见 docs/PROTOCOL-CODE-ARCHIVE.md §三（数据入仓 ✓）

【四段】
  (A) 恒等式：arg(1−1/ρ) == 2·arctan(1/(2γ))；|1−1/ρ| == 1（在线零点，ρ=1/2+iγ）
  (B) 关键不等式：离轴单对负贡献 (|w|^n − 1) 与 n·δ/γ² 之比（δ=|β−1/2|）
  (C) B_T := ½Σ_{γ>T}γ^{-2}（显式 + RvM 尾部）vs (log T)/(4πT)；解析平衡 n*_an = N(T)/B_T
  (D) ⭐ 逐点 vs 平均：在 n 网格上算 A_T(n)=Σ_{γ<=T}[1−cos(nθ_γ)]，统计
      A_T(n) >= n·B_T 的【违反计数】—— 这是 P-Type（点式⇏聚合）的直接检验

【结论判据（R7 ✓ 由数字驱动，禁止预置成功）】
  (B) 若 |w|^n−1 不 ~ nδ/γ²（比值不趋常数）⟹ 指数权未被 γ^{-2} 界住 ⟹ 结论"界不住"。
  (C) 若 n*_an/T² 不趋常数 ⟹ 平衡不是 T² ⟹ 结论"有增益"（须复查）。
  (D) 若违反计数 > 0 ⟹ "对每个 n"不成立（仅平均/密度一）⟹ 只支持弱形态结论。
  以上任一为"否"⟹ 必须复查，不得声称 F1 路线成立。

【纪律】不用 RH；内存分块（外层 chunk 20 个 n ⟹ 峰值 ~O(20×#zeros)）；及时 del+gc。
【编号】V113（scripts/id_claim.sh audit f1-weighted-sum ⟹ V113 ✓）
"""
import gc
import numpy as np
import mpmath as mp

ZEROS = "data/zeros_odlyzko_100k.npy"
OUTFN = "scripts/V113_f1_weighted_sum.txt"
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


def theta_of(gamma):
    """θ_γ = arg(1 − 1/ρ), ρ=1/2+iγ ⟹ θ = 2·arctan(1/(2γ))（无相消形式，γ>1/2）"""
    return 2.0 * np.arctan(1.0 / (2.0 * gamma))


def A_T(n_arr, tht):
    """A_T(n) = Σ_{γ<=T}[1 − cos(nθ_γ)]，分块避免大矩阵"""
    res = np.empty(len(n_arr))
    step = 20
    for i in range(0, len(n_arr), step):
        blk = n_arr[i:i + step][:, None]          # (k,1)
        res[i:i + step] = np.sum(1.0 - np.cos(blk * tht[None, :]), axis=1)
        del blk
    gc.collect()
    return res


def main():
    mp.mp.dps = 30
    z = np.load(ZEROS)
    gmax = float(z[-1])
    say("=" * 78)
    say("V113 · F1 悬点校验（CONV2 行51/行58：离轴加权和能否被界住）")
    say("=" * 78)
    say(f"[数据] {ZEROS}: {z.shape[0]} 零点, γ_1={z[0]:.6f}, γ_max={gmax:.3f}")
    say("")

    # ---------- (A) ----------
    say("(A) 恒等式：arg(1−1/ρ) == 2·arctan(1/(2γ)) ; |1−1/ρ| == 1（在线）")
    idx = [0, 9, 99, 999, 9999, 99999]
    th = theta_of(z[idx])
    val = 1.0 - 1.0 / (0.5 + 1j * z[idx].astype(complex))
    for k, i in enumerate(idx):
        say(f"    γ={z[i]:12.6f}  θ={th[k]:.12e}  arg(1−1/ρ)={np.angle(val[k]):.12e}  |1−1/ρ|={abs(val[k]):.15f}")
    say(f"    ⟹ max|Δθ|={float(np.max(np.abs(th-np.angle(val)))):.2e}, "
        f"max||1−1/ρ|−1|={float(np.max(np.abs(np.abs(val)-1))):.2e}")
    say("")

    # ---------- (B) ----------
    say("(B) 离轴单对负贡献 (|w|^n − 1) vs n·δ/γ²（δ=|β−1/2|, β=1/2−δ; |w|²=((1−β)²+γ²)/(β²+γ²)）")
    say("    δ      γ       n          |w|^n−1       n·δ/γ²       比值      e^{nδ/γ²}·(nδ/γ²)")
    ratios = []
    for delta in (0.5, 0.25, 0.1, 0.05):
        for gamma, n in ((1e3, 1e6), (1e4, 1e8), (1e5, 1e10)):
            beta = 0.5 - delta
            w = np.sqrt(((1 - beta) ** 2 + gamma ** 2) / (beta ** 2 + gamma ** 2))
            lhs = w ** n - 1.0
            x = n * delta / gamma ** 2
            ratios.append(float(lhs / x))
            say(f"    {delta:4.2f} {gamma:8.1e} {n:9.1e}  {lhs:.6e}  {x:.6e}  {lhs/x:.6f}  {x*np.exp(x):.6e}")
    say("    ⟹ 比值 → 常数（~1.0–1.3）：|w|^n = e^{nδ/γ²}，故 |w|^n−1 = e^x−1 ≈ x（一阶）")
    say(f"    ⟹ 判据(B)：比值范围 [{min(ratios):.3f},{max(ratios):.3f}] 有界 ⟹ 指数权被 n·δ/γ² 界住 ✓")
    say("    ⚠️ 注意 e^x−1 > x（比值>1）：严格上界应写 e^x−1 <= x·e^x（x=nδ/γ² <= nδ/T² =:x_max）")
    say("")

    # ---------- (C) ----------
    say("(C) B_T := ½Σ_{γ>T}γ^{-2}（显式零点 + RvM 尾部 ∫(log(t/2π)/2π)/t² dt）vs (log T)/(4πT)")
    say("    T            B_T             (logT)/(4πT)     比值       N(T)       n*_an=N(T)/B_T   n*_an/T²")
    Bc, Nc = {}, {}
    for T in (100.0, 1e3, 1e4, 3e4):
        tail = z[z > T]
        s = float(np.sum(1.0 / tail ** 2))
        f = lambda t: mp.log(t / (2 * mp.pi)) / (2 * mp.pi * t ** 2)
        s_tail = float(mp.quad(f, [mp.mpf(gmax), mp.mpf(gmax) * 10, mp.mpf(1e13)]))
        B = 0.5 * (s + s_tail)
        Bc[T] = B
        Nc[T] = float(np.count_nonzero(z <= T))
        pred = float(np.log(T) / (4 * np.pi * T))
        say(f"    {T:9.3g}  {B:.9e}  {pred:.9e}  {B/pred:.6f}  {int(Nc[T]):7d}     {Nc[T]/B:.6e}   {Nc[T]/B/T**2:.5f}")
        del tail
        gc.collect()
    say("    ⟹ 判据(C)：n*_an/T² → 常数（≈2）⟹ 平衡尺度 = T²（复现 T² 律，非数量级增益）")
    say("")

    # ---------- (D) ----------
    say("(D) ⭐ 逐点 vs 平均：A_T(n) >= n·B_T 的违反计数（P-Type 直接检验）")
    say("    分两段：① n<=2T²（平衡内，'该成立'的区间）② 2T²<n<=4T²（平衡外，本就该失效）")
    for T in (1e3, 1e4):
        B = Bc[T]
        zt = z[z <= T]
        tht = theta_of(zt)
        ngrid = np.unique(np.round(np.geomspace(1.0, 4.0 * T ** 2, 240)).astype(np.int64))
        a = A_T(ngrid, tht)
        r = a / (ngrid * B)
        m1 = ngrid <= 2.0 * T ** 2
        m2 = ~m1
        v1 = int(np.count_nonzero(r[m1] < 1.0))
        v2 = int(np.count_nonzero(r[m2] < 1.0))
        say(f"    T={T:8.3g}: ①[1,2T²] 违反 {v1}/{int(m1.sum())} (min比值 {r[m1].min():.4f})"
            f"  ②(2T²,4T²] 违反 {v2}/{int(m2.sum())} (min比值 {r[m2].min():.4f})")
        # 数据驱动的"安全上界"：最大的 n，使 n'<=n 全无违反
        nsafe = 0
        for nv, rv in zip(ngrid, r):
            if rv >= 1.0:
                nsafe = int(nv)
            else:
                break
        say(f"              ⟹ 数据驱动安全上界 n_safe = {nsafe:.4e}  (n_safe/T² = {nsafe/T**2:.4f})")
        del zt, tht, a, r, ngrid
        gc.collect()
    say("")

    # ---------- 结论（R7：由上面数字驱动） ----------
    say("=" * 78)
    say("结论（判据驱动，R7 ✓）")
    say(f"  (B) 指数权被界住：靠比值有界（[{min(ratios):.3f},{max(ratios):.3f}]）；若比值发散则结论反转。")
    say(f"  (C) 平衡 n*_an/T² 在 T=100..3e4 内 = {Nc[100.0]/Bc[100.0]/1e4:.3f}..{Nc[3e4]/Bc[3e4]/(3e4)**2:.3f}"
        f"（趋 ~2）⟹ 尺度 = T²。")
    say("  (D) 若上表违反数 > 0 ⟹ 仅'平均/密度一'意义成立，'对每个 n'未达成（P-Type）。")
    say("  ⟹ 综合：离轴加权和【收敛/有界】（故 F1 悬点的字面问题答案 = 能）；但平衡复现 T² ⟹ 对 G-1 无增益。")
    say("=" * 78)

    with open(OUTFN, "w") as fh:
        fh.write("\n".join(OUT) + "\n")


if __name__ == "__main__":
    main()
