#!/usr/bin/env python3
"""
closure_gate.py —— AMEND-28 的 E0/E4 入场闸（可执行版）

用法:
    python3 scripts/closure_gate.py <candidates.json> [--registry scripts/family_theorem_registry.json]

候选 schema（每条）:
  {
    "id": "...",
    "object_type": "difference_set_skew_hadamard" | "forbidden_configuration_boundary" | ...,
    "params": {"v": 243, "k": 121, "lam": 60, "G": [3,9,9], "abelian": true, "skew": true},
    "fingerprint": "自由文本：该候选攻击什么",
    "e4": {"e4_1": {"verdict": "OPEN|CLOSED|PASS|FAIL", "evidence": "..."},
           "e4_2": {...}, "e4_3": {...}, "e4_4": {...}}
  }

判定:
  · 机器可判定理命中（CXS 指数界 / 素数幂必要条件 / 计数必要条件）⟹ BLOCKED
  · 指纹命中非机器条目 ⟹ BLOCKED（指纹命中，需人工确认匹配）
  · 四闸证据齐备且 verdict ∈ {OPEN, PASS} ⟹ ADMIT
  · 否则 HOLD（缺证据）
"""
import json
import sys
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(2, n + 1) if s[i]]


PRIMES = sieve(200000)


def factor(x):
    f = {}
    for p in PRIMES:
        if p * p > x:
            break
        while x % p == 0:
            f[p] = f.get(p, 0) + 1
            x //= p
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def machine_checks(cand):
    """return list of (registry_id, reason) for machine-decidable kills"""
    kills = []
    p = cand.get("params") or {}
    v, k, lam = p.get("v"), p.get("k"), p.get("lam")
    G = p.get("G") or []
    ot = cand.get("object_type", "")

    if v and k and lam:
        # 1) 计数必要条件
        if k * (k - 1) != lam * (v - 1):
            kills.append(("SHDS-counting-relation", f"k(k-1)={k*(k-1)} != λ(v-1)={lam*(v-1)}"))
        # 2) skew Hadamard 参数型 + 素数幂必要条件
        if k == 2 * lam + 1 and v == 4 * lam + 3:
            if len(factor(v)) != 1:
                kills.append(("SHDS-v-prime-power", f"v={v} 非素数幂，而 abelian skew Hadamard 要求 v=p^m"))
            # 3) CXS 指数界（需 p-群）
            if G:
                facs = {}
                for g in G:
                    for q, e in factor(g).items():
                        facs[q] = facs.get(q, 0) + e
                if len(facs) == 1:
                    pr, mm = next(iter(facs.items()))
                    if pr % 4 == 3:
                        s = max(factor(g).get(pr, 0) for g in G)
                        if s >= 2 and s > (mm + 1) // 4:
                            kills.append(("CXS-exponent-bound",
                                          f"p={pr}, m={mm}, s={s} > floor((m+1)/4)={(mm+1)//4}"))
    return kills


def fingerprint_hits(cand, registry):
    """显式关键词匹配：需 ≥2 个 keyword 命中（避免误伤）"""
    fp = cand.get("fingerprint") or ""
    hits = []
    for e in registry:
        if e.get("machine_check") == "yes":
            continue
        kws = e.get("keywords") or []
        n = sum(1 for k in kws if k and k in fp)
        if kws and n >= 2:
            hits.append((e, n))
    return [e for e, _ in hits]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cands = json.load(open(sys.argv[1]))
    reg_path = ROOT / "scripts" / "family_theorem_registry.json"
    if "--registry" in sys.argv:
        reg_path = Path(sys.argv[sys.argv.index("--registry") + 1])
    registry = json.load(open(reg_path))["entries"]

    n_block = n_admit = n_hold = 0
    for c in cands:
        kills = machine_checks(c)
        hits = fingerprint_hits(c, registry)
        e4 = c.get("e4") or {}
        ok4 = all(str((e4.get(g) or {}).get("verdict", "")).upper() in ("OPEN", "PASS")
                  for g in ("e4_0", "e4_1", "e4_2", "e4_3", "e4_4"))
        missing = [g for g in ("e4_0", "e4_1", "e4_2", "e4_3", "e4_4") if not (e4.get(g) or {}).get("evidence")]
        if kills or hits:
            verdict = "BLOCKED"
            n_block += 1
        elif ok4 and not missing:
            verdict = "ADMIT"
            n_admit += 1
        else:
            verdict = "HOLD"
            n_hold += 1
        print(f"[{verdict:7s}] {c.get('id')}")
        for rid, why in kills:
            print(f"           · 机器判定理命中: {rid} —— {why}")
        for e in hits:
            print(f"           · 指纹命中: {e['id']} —— {e['conclusion'][:70]}")
        if verdict == "HOLD" and missing:
            print(f"           · 缺证据（闸）: {', '.join(missing)}")
    print(f"\n合计: BLOCKED={n_block}  ADMIT={n_admit}  HOLD={n_hold}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
