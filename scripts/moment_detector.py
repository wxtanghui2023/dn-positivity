#!/usr/bin/env python3
"""矩检测器（Moment Detector）——RH 离轴零点检测工具
=====================================================
原理：
  c_k = Σ_ρ 1/ρ^k（无条件——ξ 在 s=0 的导数——只含非平凡零点）
      = −(1/(k−1)!)·d^{k−1}(ξ'/ξ)/ds^{k−1}|_0
  β 扫描：Σ 2·Re[1/(β+iγ)^k]（用零点虚部数据 + 假设实部 β）
  匹配检验：β=½ 时矩匹配（尖峰——分辨率 ~1e-4——k=3,4,5）
  失配 ⟹ 该数据区间存在离轴零点（β≠½）

用法：
  python3 moment_detector.py [zeros_file] [--beta 0.5] [--k 3,4,5] [--scan]
  默认：/tmp/zeros_odlyzko_2M.npy——β=0.5——k=3,4,5

依赖：numpy + mpmath（c_k 计算）
"""
import sys
import numpy as np
import mpmath as mp
mp.mp.dps = 40


# ---------- c_k 计算（无条件——ξ 在 0 的导数） ----------
def _f_series(s, N=500):
    """f(s) = 1/s + ½ψ(s/2) 的正则部分（级数——避开 s=0 极点）"""
    total = -mp.euler / 2
    for n in range(N):
        total += 0.5 * (1 / (n + 1) - 1 / (n + 1 + s / 2))
    return total


def _xi_ratio(s):
    """ξ'/ξ(s) = f(s) + 1/(s−1) − ½logπ + ζ'/ζ(s)——在 s=0 正则"""
    return _f_series(s) + 1 / (s - 1) - 0.5 * mp.log(mp.pi) + mp.zeta(s, derivative=1) / mp.zeta(s)


def c_k_exact(k):
    """c_k = Σ 1/ρ^k = −(1/(k−1)!)·d^{k−1}(ξ'/ξ)/ds^{k−1}|_0（无条件——含所有非平凡零点）"""
    if k < 2:
        raise ValueError("k ≥ 2")
    deriv = mp.diff(_xi_ratio, mp.mpf(0), k - 1)
    return float(-deriv / mp.factorial(k - 1))


# ---------- 矩扫描 ----------
def moment_sum(gamma, beta, k):
    """Σ 2·Re[1/(β+iγ)^k]——γ>0 配对——向量化"""
    r = np.abs(beta + 1j * gamma)
    theta = np.arctan2(gamma, beta)
    return float(np.sum(2 * r ** (-k) * np.cos(-k * theta)))


def detect(gamma, k_list=(3, 4, 5), beta=0.5, tol_scale=100.0):
    """矩检测：匹配 ⟹ β=½——失配 ⟹ 离轴
    返回：(匹配?, 各 k 的差, 阈值)
    阈值 = tol_scale × 参考差（β=½ 的匹配差——数值精度）
    """
    results = {}
    for k in k_list:
        ck = c_k_exact(k)
        s = moment_sum(gamma, beta, k)
        results[k] = abs(s - ck)
    # 参考：β=½ 的匹配差（2M 数据——k=3:2.5e-7, k=4:1.7e-10, k=5:1.2e-13）
    ref = {2: 5e-4, 3: 3e-7, 4: 2e-10, 5: 2e-13}
    matched = all(results[k] < tol_scale * ref.get(k, 1e-7) for k in results)
    return matched, results, {k: tol_scale * ref.get(k, 1e-7) for k in results}


def beta_scan(gamma, k_list=(3, 5), beta_range=(0.40, 0.60, 0.01)):
    """β 扫描——找最优匹配（尖峰 = β=½）"""
    print(f"β 扫描（k={k_list}——{beta_range}）:")
    best = {}
    for beta in np.arange(beta_range[0], beta_range[1] + 1e-9, beta_range[2]):
        row = []
        for k in k_list:
            ck = c_k_exact(k)
            s = moment_sum(gamma, beta, k)
            row.append(abs(s - ck))
            if k not in best or row[-1] < best[k][0]:
                best[k] = (row[-1], beta)
        print(f"  β={beta:.2f}: " + "  ".join(f"k={k}:{d:.2e}" for k, d in zip(k_list, row)))
    print("\n最优匹配:")
    for k in k_list:
        print(f"  k={k}: β={best[k][1]:.3f}（差 {best[k][0]:.2e}）")
    return best


def main():
    zeros_file = "/tmp/zeros_odlyzko_2M.npy"
    beta = 0.5
    k_list = (3, 4, 5)
    scan = False
    args = sys.argv[1:]
    if args and not args[0].startswith("--"):
        zeros_file = args[0]
    for i, a in enumerate(args):
        if a == "--beta" and i + 1 < len(args):
            beta = float(args[i + 1])
        elif a == "--k" and i + 1 < len(args):
            k_list = tuple(int(x) for x in args[i + 1].split(","))
        elif a == "--scan":
            scan = True

    print(f"=== 矩检测器（Moment Detector）===")
    print(f"数据: {zeros_file}——β 假设: {beta}——k: {k_list}")
    gamma = np.load(zeros_file)
    print(f"零点数: {len(gamma)}（γ: {gamma[0]:.1f} - {gamma[-1]:.1f}）")

    print("\nc_k（无条件——ξ）:")
    for k in k_list:
        print(f"  c_{k} = {c_k_exact(k):+.12f}")

    if scan:
        beta_scan(gamma, k_list)
    else:
        matched, diffs, thresholds = detect(gamma, k_list, beta)
        print("\n检测结果:")
        for k in k_list:
            status = "✅" if diffs[k] < thresholds[k] else "⚠️"
            print(f"  k={k}: 差 {diffs[k]:.2e}（阈值 {thresholds[k]:.2e}）{status}")
        print(f"\n结论: {'✅ β=½ 匹配——数据区间无离轴（β 锁定）' if matched else '⚠️ 失配——可能存在离轴！'}")


if __name__ == "__main__":
    main()
