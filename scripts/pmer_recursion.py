## 仅用于回测研究，不包含实盘下单逻辑
"""PMER: prefix-multiplicity exact recursion.
状态 = 层 k 上的 multiplicity profile m: Q_k -> Z>=0, sum = M.
转移 = 整数分裂 (每个前缀 v 分成 v0 取 x_v, v1 取 m(v)-x_v).
剪枝 = F_{k+1}: 对每个 w in Q_{k+1}: ((n+1)-(k+1))*m(w) + sum_{w'~w} m(w') >= 2^(n-k-1).
商    = Aut(Q_k) = affine 群 (坐标置换 x 平移), 阶 2^k * k!.
"""
import itertools, sys, time, collections

def aut_group(k):
    """返回 Aut(Q_k) 作为 0..2^k-1 上的置换列表."""
    pts = list(range(1 << k))
    perms = []
    for perm in itertools.permutations(range(k)):
        for t in range(1 << k):
            img = []
            for v in pts:
                # 置换坐标
                w = 0
                for i in range(k):
                    b = (v >> i) & 1
                    w |= b << perm[i]
                img.append(w ^ t)
            perms.append(tuple(img))
    return perms

def canon(prof, perms):
    best = None
    for img in perms:
        # 新 profile 在位置 v 取值 = 旧 profile 在 img^{-1}(v)?? 这里用: 对置换 g, 新(v)=旧(g(v))
        cand = tuple(prof[g] for g in img)
        if best is None or cand < best:
            best = cand
    return best

def nb(k):
    return [ [v ^ (1 << i) for i in range(k)] for v in range(1 << k) ]

def children(prof, k, n, M, NBS, deadline=None, budget=[0]):
    """DFS 生成所有满足 F_{k+1} 的 children profile (长度 2^(k+1))."""
    k1 = k + 1
    K = (n + 1) - k1          # 系数
    need = 1 << (n - k1)      # 常数
    pts = list(range(1 << k))
    # 依赖: 对 v, 约束 (w=v0, w=v1) 涉及 x_v, m(v) 与 {x_u: u~v}
    order = pts[:]
    x = {}
    out = []
    def ok_after(v):
        # v0 约束
        if K * x[v] + (prof[v] - x[v]) + sum(x[u] for u in NBS[v]) < need:
            return False
        # v1 约束
        if K * (prof[v] - x[v]) + x[v] + sum(prof[u] - x[u] for u in NBS[v]) < need:
            return False
        return True
    def ready(v):
        return all(u in x for u in NBS[v])
    def dfs(i):
        budget[0]+=1
        if deadline is not None and (budget[0]%500==0) and time.time()>deadline:
            raise TimeoutError('deadline')
        if i == len(order):
            child = [0] * (1 << k1)
            for v in pts:
                child[2 * v] = x[v]
                child[2 * v + 1] = prof[v] - x[v]
            out.append(tuple(child))
            return
        v = order[i]
        for xv in range(prof[v] + 1):
            x[v] = xv
            # 检查所有已可判定之约束
            good = True
            for u in pts:
                if u in x and ready(u) and not ok_after(u):
                    good = False; break
            if good:
                dfs(i + 1)
            del x[v]
    try:
        dfs(0)
    except TimeoutError:
        return None
    return out

def run(n, M, kmax, tlimit=240.0, cap=2000000):
    t0 = time.time()
    print(f"=== PMER  n={n}, M={M} ===", flush=True)
    # k=1: 由 F_1 生成
    k = 1
    K = (n + 1) - k; need = 1 << (n - k)   # 对于 k=1: 系数 n, 常数 2^(n-1)
    lvl = []
    for a in range(M + 1):
        b = M - a
        if K * a + b >= need and K * b + a >= need:
            lvl.append((a, b))
    perms = aut_group(1)
    lvl = sorted({canon(p, perms) for p in lvl})
    print(f"  k=1: N_1 = {len(lvl)}   ({lvl})", flush=True)
    all_lvl = {1: lvl}
    for k in range(1, kmax):
        if time.time() - t0 > tlimit:
            print(f"  [时间上限 {tlimit}s 达到，停在 k={k}]", flush=True); break
        NBS = nb(k)
        perms1 = aut_group(k + 1)
        nxt = set()
        nchild = 0
        incomplete=False
        for idx, prof in enumerate(all_lvl[k]):
            ch = children(prof, k, n, M, NBS, deadline=t0+tlimit)
            if ch is None:
                incomplete=True
                print(f"  [!] k={k}->{k+1} 在第 {idx}/{len(all_lvl[k])} 个状态处超时（本层不完整 ⚠️）", flush=True)
                break
            nchild += len(ch)
            for c in ch:
                nxt.add(canon(c, perms1))
            if len(nxt) > cap or time.time() - t0 > tlimit:
                incomplete=True
                print(f"  [!] 触发上限/超时（本层不完整 ⚠️）", flush=True)
                break
        if incomplete: break
        all_lvl[k + 1] = sorted(nxt)
        print(f"  k={k+1}: N_{k+1} = {len(nxt)}   (原始 children 累计 {nchild}; 用时 {time.time()-t0:.1f}s)", flush=True)
        if len(nxt) == 0:
            print(f"  >>> S_{k+1} = EMPTY  ==> K({n},1) > {M} ✓✓", flush=True); break
    return all_lvl

if __name__ == "__main__":
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 106
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    KMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    run(n, M, KMAX)
