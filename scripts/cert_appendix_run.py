#!/usr/bin/env python3
"""
cert_appendix_run.py —— 可独立复核的证书附录生成器

对给定的 M（默认 3,4），用固定参数跑自适应证书，记录:
  M, N0, 评估箱数, 未决, 最小余量, 用时, SLACK, TEST_EPS, 结果哈希
并把结果写入 cert_appendix/manifest.json。

复现:  python3 scripts/cert_appendix_run.py 3 4
       （M=5 需要约 16 分钟；用 python3 scripts/cert_appendix_run.py 5 10 400000000 40）
"""
import json, hashlib, sys, os, subprocess, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CERT = os.path.join(ROOT, "scripts", "rpM_adaptive_certificate_idx.py")
OUT  = os.path.join(ROOT, "cert_appendix", "manifest.json")

# 已记录的运行参数（与 C-163 / C-164 / C-168 一致）
PARAMS = {3: (10, 20_000_000, 40), 4: (20, 20_000_000, 40), 5: (10, 400_000_000, 40)}

def run_one(M, N0, BUD, DEP):
    t0 = time.time()
    p = subprocess.run([sys.executable, CERT, str(M), str(N0), str(BUD), str(DEP)],
                       capture_output=True, text=True)
    el = time.time() - t0
    lines = [l for l in p.stdout.strip().split("\n") if l.strip()]
    jline = next((l for l in reversed(lines) if l.startswith("{")), None)
    res = json.loads(jline) if jline else {"raw": p.stdout}
    res["recorded_seconds_wall"] = round(el, 2)
    res["command"] = f"python3 scripts/rpM_adaptive_certificate_idx.py {M} {N0} {BUD} {DEP}"
    return res

def main():
    Ms = [int(x) for x in (sys.argv[1:] or ["3", "4"])]
    manifest = {"generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "algorithm": "adaptive branch-and-bound + exact per-box lower bound",
                "conservative": {"SLACK_per_term": 1e-12, "TEST_EPS_pi_test": 1e-9},
                "certifier_script": "scripts/rpM_adaptive_certificate_idx.py",
                "runs": []}
    for M in Ms:
        N0, BUD, DEP = PARAMS.get(M, (10, 50_000_000, 40))
        print(f"--- running M={M} (N0={N0}, budget={BUD}) ...", flush=True)
        r = run_one(M, N0, BUD, DEP)
        print("    ", json.dumps({k: v for k, v in r.items() if k != "depth_hist"}, ensure_ascii=False), flush=True)
        manifest["runs"].append(r)
    # 已记录但未在本次重跑的（M=5）
    if 5 not in Ms:
        manifest["runs"].append({
            "M": 5, "ok": True, "neval": 72440000, "unresolved": 0,
            "min_margin": 3.956783786618345e-06, "max_depth": 4, "N0": 10,
            "seconds": 951.27, "source": "C-168 记录（已跑完，未在本次重跑）",
            "command": "python3 scripts/rpM_adaptive_certificate_idx.py 5 10 400000000 40"})
    blob = json.dumps(manifest, sort_keys=True, ensure_ascii=False)
    manifest["manifest_sha256_16"] = hashlib.sha256(blob.encode()).hexdigest()[:16]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(manifest, open(OUT, "w"), ensure_ascii=False, indent=1)
    print("wrote", OUT, "manifest_sha256_16 =", manifest["manifest_sha256_16"])

if __name__ == "__main__":
    main()
