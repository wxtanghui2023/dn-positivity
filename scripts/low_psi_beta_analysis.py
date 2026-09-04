#!/usr/bin/env python3
# Low-region beta-sensitive analysis: psi(x) - x at low x.
# psi(x) - x = -sum_rho x^rho/rho - ... (explicit formula, beta enters via x^beta)
# Low x => dominated by LOW zeros => gives beta constraints on low zeros (measurable, verifiable).
import numpy as np

X = 10**6
# sieve primes up to X
sieve = np.ones(X+1, dtype=bool)
sieve[:2] = False
for i in range(2, int(X**0.5)+1):
    if sieve[i]:
        sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]
print(f"primes up to {X}: {len(primes)}")

# psi(x) = sum_{p^k <= x} log p : compute via prime powers
# Use cumulative: psi(x) = sum_{p<=x} log p * floor(log x / log p)  (all prime powers)
logp = np.log(primes)
# for each x grid point, psi via prefix over primes with multiplicity floor(log_x/log_p)
# Efficient: psi(x) = sum over primes p<=x of log p * (number of k with p^k <= x)
# = sum_{p<=x} log p * floor(log(x)/log(p))... but simpler: sum over prime powers
# Build psi on grid points 10^3 .. 10^6 (log-spaced fine grid)
grid = np.unique(np.concatenate([np.arange(1000, 10000, 10),
                                 np.arange(10000, 100000, 100),
                                 np.arange(100000, X+1, 1000)]))
psi = np.zeros(len(grid))
# brute over prime powers: for each prime p, add log p at x >= p, p^2, ...
for p, lp in zip(primes, logp):
    pk = p
    while pk <= X:
        idx = np.searchsorted(grid, pk)
        if idx < len(grid):
            psi[idx:] += lp
        pk *= p
R = psi - grid  # psi(x) - x

# Explicit formula main oscillatory term from first zero: -2 Re(x^rho1/rho1), rho1 = 1/2 + i*gamma1
gamma1 = 14.134725141734693
# with beta = 1/2 + delta: -2 Re(x^(1/2+delta+i gamma1)/(1/2+delta+i gamma1))
def first_zero_term(x, delta):
    rho = (0.5+delta) + 1j*gamma1
    return -2*np.real(x**(rho)/rho)

# Also second zero contribution for better fit
gamma2 = 21.022039638771555
def second_zero_term(x, delta):
    rho = (0.5+delta) + 1j*gamma2
    return -2*np.real(x**(rho)/rho)

# Compare: fit delta by comparing R(x) - first_zero_term(x,0) - second_zero_term(x,0) residual
# If zeros are on-line, residual should be small; off-line delta shifts amplitude x^delta
resid0 = R - first_zero_term(grid, 0.0) - second_zero_term(grid, 0.0)
# normalize by x^(1/2) to see the oscillatory envelope
env = resid0 / np.sqrt(grid)

print(f"\n=== Residual after subtracting first 2 on-line zeros ===")
print(f"R(x) range: {R.min():.1f} .. {R.max():.1f} (x up to {X})")
print(f"residual (on-line assumption) max|resid|/sqrt(x) = {np.max(np.abs(env)):.4f}")
print(f"  (should be O(log^2 x) if on-line; high zeros contribute ~1/gamma_k each)")

# Beta constraint on gamma1: if delta>0, first-zero term amplitude grows as x^delta
# compare data vs delta=0 vs delta=0.01 at high x end
x_hi = grid[grid > 500000]
R_hi = R[grid > 500000]
for delta in [0.0, 0.005, 0.01, 0.02]:
    t1 = first_zero_term(x_hi, delta) + second_zero_term(x_hi, delta)
    resid = R_hi - t1
    # normalized residual (should be same scale regardless of delta if delta correct)
    # key: total oscillatory amplitude |R| scales as x^(1/2+delta)*|1/rho| factor
    # measure: correlation of R with the delta-term shape
    amp = np.max(np.abs(R_hi)) 
    corr = np.corrcoef(R_hi, t1)[0,1]
    print(f"  delta={delta}: corr(R, term)={corr:.6f}")

# Simpler beta probe: amplitude of R at x vs x^(1/2).  If a beta>1/2 zero dominates, amp ~ x^beta.
# Take log of |R| at oscillation peaks... crude: fit log|R| vs log x slope on windows
print(f"\n=== Amplitude growth of R(x) ===")
# windowed max of |R| over log intervals
logx = np.log(grid)
logR = np.log(np.abs(R)+1e-9)
# bin by log x
bins = np.linspace(np.log(1000), np.log(X), 20)
slopes = []
for i in range(len(bins)-1):
    m = (logx >= bins[i]) & (logx < bins[i+1])
    if m.sum() > 5:
        # max |R| in bin
        mx = np.max(np.abs(R[m]))
        slopes.append((np.exp(bins[i+1]), np.log(mx)))
print("  x_max -> log(max|R|):")
for xm, lm in slopes[::3]:
    print(f"    x~{xm:.0e}: log max|R| = {lm:.2f} (x^0.5 slope would be {0.5*np.log(xm):.2f})")
