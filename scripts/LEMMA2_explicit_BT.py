"""LEMMA 2: explicit upper bound for B_T = (1/2) sum_{gamma>T} gamma^{-2}."""
import numpy as np
from mpmath import mp, mpf, log as mlog, pi as mpi, e as me
mp.dps=50
g=np.load('data/zeros_odlyzko_2M.npy').astype(float).ravel(); g=np.sort(g)
Tdata=float(g[-1])
def B_bound(Tv):
    Tv=mpf(Tv)
    # 2*int_T^inf (x/2pi) log(x/(2 pi e)) x^{-3} dx = (1/pi)(1 + log(T/(2 pi e)))/T
    L = mlog(Tv/(2*mpi*me))
    t1 = (1/mpi)*(1+L)/Tv
    t2 = mpf(7)/8/Tv**2                      # from the 7/8 in F
    lx = mlog(Tv); llx = mlog(lx) if lx > 1 else mpf(0)
    t3 = mpf('0.112')*(1+2*lx)/(2*Tv**2)     # 2 int 0.112 log x x^-3
    t4 = mpf('0.278')*(1+2*llx+llx**2)/(2*Tv**2)  # generous bound for 2 int 0.278 loglog x x^-3
    t5 = mpf('2.510')/Tv**2
    t6 = mpf('0.2')/(2*Tv**3)
    return t1+t2+t3+t4+t5+t6, (t1,t2,t3,t4,t5,t6)
print("="*96); print("LEMMA 2: explicit B_T upper bound (all terms elementary)"); print("="*96)
print("  B_T = (1/2) sum_{gamma>T} gamma^{-2} = (1/2)[ -N(T)/T^2 + 2 int_T^inf N(x)x^{-3}dx ]")
print("      <= (1/2)[ 2 int_T^inf (F(x)+R(x)) x^{-3} dx ]   (dropping the negative -N(T)/T^2 term)")
print()
print("  %12s | %14s | %14s | %10s" % ("T","B_T <= (explicit)","nominal","ratio"))
for Tv in (Tdata, 1e6, 1e9, 3.000175e12):
    tot,parts=B_bound(Tv)
    nominal=(float(np.log(Tv))+1)/(4*np.pi*float(Tv))
    print("  %12.6g | %14.6e | %14.6e | %10.4f" % (Tv, float(tot), nominal, float(tot)/nominal))
    print("        parts: " + "  ".join("%.3e"%float(p) for p in parts))
print()
print("="*96); print("CONSEQUENCE: the needed window count with the EXPLICIT B_T bound"); print("="*96)
C1=1.0-float(mp.cos(mpf('0.5')))
print("  %12s | %18s | %18s | %s" % ("n","need (nominal B_T)","need (explicit B_T)","available count"))
from mpmath import cos as mcos
def count_le(x,Tv):
    gg=np.sort(g); return int(np.searchsorted(gg, x))
for n in (10**5, 10**6, int(2*Tdata)-20):
    if n>2*Tdata: continue
    tot,_=B_bound(Tdata)
    need_exp = n*float(tot)/C1
    need_nom = n*((np.log(Tdata)+1)/(4*np.pi*Tdata))/C1
    lo=n/2.0; hi=min(2.0*n,Tdata)
    cw = count_le(hi,Tdata)-count_le(lo,Tdata) if hi>lo else 0
    print("  %12d | %18.4f | %18.4f | %d" % (n,need_nom,need_exp,cw))
print()
print("  => even with the EXPLICIT (larger) B_T bound the needed count stays O(10),")
print("     so the explicit constants remain irrelevant away from the endpoint.")
print("="*96); print("READ-OFF: both lemmas are now explicit and elementary."); print("="*96)
