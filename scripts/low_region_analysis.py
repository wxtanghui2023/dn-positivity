#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# Low-region structural analysis: what does the low end (first N zeros) teach us?
# Focus: per-zero evolution (Tang's "low first, then recurse" strategy)
import numpy as np

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
print(f"zeros loaded: {len(zeros)}, γ1={zeros[0]:.6f}, γ1000={zeros[999]:.6f}")

# --- 1. Basic: gamma_k stats, gaps ---
g = zeros[:1000]
gaps = np.diff(g)
print(f"\n=== Basic stats (first 1000) ===")
print(f"γ1={g[0]:.6f}  γ2={g[1]:.6f}  mean gap (local, first 100)={np.mean(np.diff(g[:100])):.4f}")
print(f"mean gap (first 1000)={np.mean(gaps):.4f}  min gap={gaps.min():.4f} at k={gaps.argmin()+1}")

# --- 2. Phase structure theta_k = 2 arctan(1/(2 gamma_k)) (telescope/Cayley) ---
th = 2*np.arctan(1/(2*g))
print(f"\n=== Phase (telescope/Cayley) ===")
print(f"θ1={th[0]:.6f}  θ1000={th[-1]:.8f}  θ decreases to 0")

# --- 3. Telescoping D_n for first N zeros: how does positivity evolve with N? ---
# D_n(N) = sum_{k<=N} [cos(nθ_k) - cos((n+1)θ_k)]
print(f"\n=== Telescoping D_n(N) evolution (positivity vs N) ===")
for n in [1, 5, 10, 20, 43]:
    row = []
    for N in [43, 100, 300, 1000]:
        s = np.sum(np.cos(n*th[:N]) - np.cos((n+1)*th[:N]))
        row.append(f"N={N}: {s:+.4f}")
    print(f"  n={n}: " + "  ".join(row))

# --- 4. Per-zero incremental structure: adding zeros one at a time ---
# Key: does D_n(N) stay monotone/stable as N grows (per-zero increments)?
print(f"\n=== Per-zero increments d_n(k) = [cos(nθ_k)-cos((n+1)θ_k)] ===")
for n in [5, 20, 43]:
    inc = np.cos(n*th) - np.cos((n+1)*th)
    neg_frac = np.mean(inc < 0)
    # where do negative increments start?
    first_neg = np.argmax(inc < 0) + 1 if np.any(inc < 0) else -1
    print(f"  n={n}: negative increment fraction={neg_frac:.4f}, first negative at k={first_neg}")
    # for n=43, all should be positive per theory (theta1*(43.5) < pi)
    print(f"    min increment={inc.min():.6f} at k={inc.argmin()+1}")

# --- 5. Sign stability of cumulative D_n: running sum ---
print(f"\n=== Running sum D_n(N) sign stability ===")
for n in [1, 5, 10, 20, 43, 100]:
    run = np.cumsum(np.cos(n*th) - np.cos((n+1)*th))
    neg = np.any(run < 0)
    print(f"  n={n}: running sum min={run.min():+.4f}, stays positive={not neg}, final={run[-1]:+.4f}")

# --- 6. Local gap statistics vs GUE expectation (pair correlation quick check) ---
print(f"\n=== Gap normalization (first 1000, mean=1) ===")
mg = np.mean(gaps[:999])
norm = gaps[:999]/mg
print(f"  normalized gap std={norm.std():.4f} (GUE ~0.52, Poisson ~1.0)")

# --- 7. Density/N(T) check: gamma_k vs 2pi k / log k ---
print(f"\n=== Counting asymptotic check ===")
ks = np.arange(1, 1001)
approx = 2*np.pi*ks/np.log(ks)
rel = g/approx
print(f"  γ_k/(2πk/log k): first={rel[0]:.3f}, k=100={rel[99]:.3f}, k=1000={rel[-1]:.3f} (→1 slowly)")
