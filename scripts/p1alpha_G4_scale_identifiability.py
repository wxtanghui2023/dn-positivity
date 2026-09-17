# G4: 标度辨识能力实验 (不是"拟合RH实验")
# A: R(X)=D(N)-D(X),  D(X)=sum_{p<=X} chi4(p)/p          -> 期望包络指数 beta-1
# B: pi(x;4,1)-pi(x;4,3) = sum chi4(p)                    -> 期望指数 beta
# C: psi_chi(x) = sum_{p<=x} chi4(p) log p                -> 期望指数 beta
# + 多窗口 beta_eff + 人工 beta 对照 (beta=0.50,0.55,0.60,0.65, gamma=6.0209)
import numpy as np
N = 10**8
print("sieve to", N, "...", flush=True)
s = np.ones(N+1, dtype=bool); s[:2] = False
for i in range(2, int(N**0.5)+1):
    if s[i]: s[i*i::i] = False
pr = np.nonzero(s)[0].astype(np.int64); del s
print("primes:", len(pr), flush=True)
chi = np.where(pr % 4 == 1, 1.0, -1.0); chi[pr == 2] = 0.0
lp  = np.log(pr.astype(np.float64))
A = np.cumsum(chi / pr)                 # D(X)
B = np.cumsum(chi)                      # prime race
C = np.cumsum(chi * lp)                 # psi_chi
print(f"D(N)={A[-1]:+.6f}   B(N)={B[-1]:.0f}   C(N)={C[-1]:.1f}", flush=True)

lo, hi = np.log(1e3), np.log(float(N)); M = 1500
ug = np.linspace(lo, hi, M); xg = np.exp(ug)
idx = np.clip(np.searchsorted(pr, xg, side='right') - 1, 0, len(pr)-1)

def envelope_exp(sig, d_env=0.30, d_fit=0.60):
    v = np.abs(sig[idx]); env = np.empty(M)
    for i in range(M):
        env[i] = v[np.abs(ug-ug[i]) <= d_env].max()
    le = np.full(M, np.nan)
    for i in range(M):
        m = np.abs(ug-ug[i]) <= d_fit
        if m.sum() > 8:
            le[i] = np.polyfit(ug[m], np.log(np.maximum(env[m],1e-300)), 1)[0]
    return le

R = A[-1] - A                       # 尾项 (参考点 = N)
chans = {"A: R(X)  [期望 beta-1]": R, "B: 素数竞赛 [期望 beta]": B, "C: psi_chi [期望 beta]": C}
decades = [(3,4),(4,5),(5,6),(6,7)]
res = {}
for name, sig in chans.items():
    le = envelope_exp(sig)
    med = []
    for (a,b) in decades:
        m = (ug >= a*np.log(10)) & (ug <= b*np.log(10))
        med.append(np.nanmedian(le[m]))
    res[name] = med
    print(f"\n[{name}]  逐十年窗口 local-exponent 中位数:")
    for (a,b),v in zip(decades, med):
        print(f"    1e{a}--1e{b}:  {v:+.4f}")

# ---------- 人工 beta 对照 (标度辨识能力) ----------
print("\n=== 人工对照: 信号 X^{p-1}cos(g log X+phi),  g=6.0209 ===")
g = 6.0209
for beta in [0.50,0.55,0.60,0.65]:
    vals = []
    for phi in [0.0, 1.0, 2.0, 3.0]:
        sg = np.exp((beta-1)*ug) * np.cos(g*ug + phi)
        le = envelope_exp(sg)
        m = (ug >= 3*np.log(10)) & (ug <= 7*np.log(10))
        vals.append(np.nanmedian(le[m]))
    print(f"  true beta={beta:.2f} -> 估得指数 {np.mean(vals):+.4f}  (各相位 {np.round(vals,4)})  期望 {beta-1:+.4f}")
print("\n=== 人工对照: 信号 X^{beta}cos(g log X+phi) (B/C 类比) ===")
for beta in [0.50,0.55,0.60,0.65]:
    vals = []
    for phi in [0.0, 1.0, 2.0, 3.0]:
        sg = np.exp(beta*ug) * np.cos(g*ug + phi)
        le = envelope_exp(sg)
        m = (ug >= 3*np.log(10)) & (ug <= 7*np.log(10))
        vals.append(np.nanmedian(le[m]))
    print(f"  true beta={beta:.2f} -> 估得指数 {np.mean(vals):+.4f}  (各相位 {np.round(vals,4)})  期望 {beta:+.4f}")
