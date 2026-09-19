#!/usr/bin/env python3
"""
C-190 Step 7 第一刀：旧证书的 failure-cell inventory（阻尼 M=3）
目标 T：找出所有 LB(box) < T 的格子，及其到候选 x_* 的距离。
- 盒下界（可分）：min_box S_k = min_{φ1}cos(kφ1) + (r2^k 或 ·) ... 见下
- B_ρ(x_*) 内的盒子【跳过】（Step 6 已覆盖）
保守参数：SLACK=1e-12（每项），TEST_EPS=1e-9（π 命中判定）
用法：python3 damped_failure_inventory.py TARGET [BUDGET] [RHO] [TOPN]
"""
import sys, heapq, itertools, numpy as np, time

T = float(sys.argv[1]) if len(sys.argv)>1 else 0.3730721881
BUDGET = int(sys.argv[2]) if len(sys.argv)>2 else 200000
RHO = float(sys.argv[3]) if len(sys.argv)>3 else 0.004412      # 标准版局部半径（已证）
TOPN = int(sys.argv[4]) if len(sys.argv)>4 else 40
K = 15
XA = np.array([0.79051, 0.83021, 0.10911*np.pi, 0.82066*np.pi, 0.46172*np.pi])  # x_*
SLACK, TEST_EPS, PI = 1e-12, 1e-9, float(np.pi)

def mincos(k, lo, hi):
    """min_{φ∈[lo,hi]} cos(kφ)，保守（多算则返回 −1）"""
    if hi < lo: return -1.0
    if k*(hi-lo) >= 2*PI - TEST_EPS: return -1.0
    # 检查区间是否含 kφ ≡ π (mod 2π)
    t0, t1 = k*lo, k*hi
    n0 = np.floor((t0 - PI)/(2*PI)); n1 = np.ceil((t1 - PI)/(2*PI))
    if n1 >= n0: return -1.0
    return min(np.cos(t0), np.cos(t1)) - SLACK

def boxlb(lo, hi):
    """max_{k≤K} min_{box} S_k（可分下界）"""
    best = -1e18
    for k in range(1, K+1):
        c1 = mincos(k, lo[2], hi[2])
        c2 = mincos(k, lo[3], hi[3])
        c3 = mincos(k, lo[4], hi[4])
        # r^k 项：cos 负 ⟹ 取最大 r；cos 正 ⟹ 取最小 r
        t2 = (hi[0]**k if c2 < 0 else lo[0]**k) * c2
        t3 = (hi[1]**k if c3 < 0 else lo[1]**k) * c3
        v = c1 + t2 + t3
        if v > best: best = v
    return best - 3*SLACK

def inside_ball(lo, hi):
    """盒子是否整个落在 B_ρ(x_*) 内：取到【最远角点】的距离"""
    d = np.maximum(np.abs(XA-lo), np.abs(XA-hi))
    return float(np.linalg.norm(d)) <= RHO

def dist_box(lo, hi):
    d = np.maximum(np.maximum(XA-lo, 0.0), np.maximum(lo-XA, 0.0))
    return float(np.linalg.norm(d))

lo0 = np.array([0.0,0.0,0.0,0.0,0.0]); hi0 = np.array([1.0,1.0,PI,PI,PI])
_ctr = itertools.count()
heap = [(boxlb(lo0,hi0), next(_ctr), lo0, hi0)]
cnt = 0; neval = 0; unresolved = []; skipped = 0; certified = 0
t0=time.time()
while heap and neval < BUDGET:
    lb, _, lo, hi = heapq.heappop(heap); neval += 1
    if inside_ball(lo, hi): skipped += 1; continue
    if lb >= T: certified += 1; continue
    w = hi - lo
    if np.max(w) < 1e-12: unresolved.append((lb, lo.copy(), hi.copy(), dist_box(lo,hi))); continue
    j = int(np.argmax(w)); mid = 0.5*(lo[j]+hi[j])
    for (a,b) in ((lo[j],mid),(mid,hi[j])):
        l2, h2 = lo.copy(), hi.copy(); l2[j]=a; h2[j]=b
        heapq.heappush(heap, (boxlb(l2,h2), next(_ctr), l2, h2))
    cnt += 1
# 预算耗尽后，堆里剩下的即未认证格子
while heap:
    lb,_,lo,hi = heapq.heappop(heap)
    if inside_ball(lo,hi): skipped += 1; continue
    if lb < T: unresolved.append((lb, lo.copy(), hi.copy(), dist_box(lo,hi)))
    else: certified += 1
unresolved.sort(key=lambda t: t[0])
print(f"=== damped M=3 failure-cell inventory ===  T={T:.10f}  BUDGET={BUDGET}")
print(f"  评估盒数 {neval} | 认证 {certified} | 跳过(B_ρ内) {skipped} | 未认证 {len(unresolved)} | {time.time()-t0:.1f}s")
print(f"  ρ(Step6 球) = {RHO:.6f} rad = {np.degrees(RHO):.4f}°")
if unresolved:
    ds = [u[3] for u in unresolved]
    print(f"  未认证格距离到 x_*：min {min(ds):.6f}  max {max(ds):.6f}  (rad)")
    print(f"  其中 < ρ 的未认证格数 = {sum(1 for d in ds if d < RHO)}（应为 0，因 B_ρ 内已跳过）")
    print(f"  ⟹ 未认证格是否全在 B_ρ 外：{'是 ✓' if all(d>=RHO-1e-9 for d in ds) else '否 ✗'}")
    print(f"\n  最差 {min(TOPN,len(unresolved))} 个未认证格：")
    print(f"  {'LB':>12} {'dist(x_*)':>11} {'宽(max)':>10}  盒中心（r2,r3,φ1/π,φ2/π,φ3/π）")
    for lb,lo,hi,d in unresolved[:TOPN]:
        c=0.5*(lo+hi)
        print(f"  {lb:12.6f} {d:11.6f} {float(np.max(hi-lo)):10.5f}  ({c[0]:.4f},{c[1]:.4f},{c[2]/PI:.4f},{c[3]/PI:.4f},{c[4]/PI:.4f})")
else:
    print("  ✓ 无未认证格 ⟹ F ≥ T 在整个 X\\B_ρ(x_*) 上成立")
