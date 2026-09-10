#!/usr/bin/env python3
"""进位层 holonomy：RH1–RH3 + 一个可证坍缩点
(A) 总进位数：是否 coboundary（分组无关）？
    S_p(n)=p 进制数字和；经典恒等式  K(a,b) = (S(a)+S(b)-S(a+b))/(p-1)
(B) 进位【模式】holonomy：H_C(a,b,c) = 两分组进位位向量之差
(C) RH2：跨素数（CRT）统计能否分离？v_p(a+b) 与 v_q(a+b) 是否独立
"""
import random
from itertools import combinations

def digs(n, p, L):
    return [(n // p**i) % p for i in range(L)]

def S(n, p):
    s = 0
    while n: s += n % p; n //= p
    return s

def carry_vec(a, b, p, L):
    """schoolbook 进位位向量与总数"""
    v = []; c = 0
    for i in range(L):
        s = (a // p**i) % p + (b // p**i) % p + c
        c = 1 if s >= p else 0
        v.append(c)
    return v, sum(v)

L = 14
print('=== (A) 总进位数：经典恒等式 + 分组无关（= coboundary）===')
for p in [2, 3]:
    okid = True; okgrp = True
    for a in range(1, 80):
        for b in range(1, 80):
            for c in range(1, 40):
                K_ab = carry_vec(a, b, p, L)[1]
                pred = (S(a,p)+S(b,p)-S(a+b,p))//(p-1)
                if K_ab != pred: okid = False
                # 左：(a+b)+c   右：a+(b+c)
                KL = carry_vec(a+b, c, p, L)[1] + K_ab
                KR = carry_vec(b, c, p, L)[1] + carry_vec(a, b+c, p, L)[1]
                if KL != KR: okgrp = False
            if not okid and not okgrp: break
        if not okid and not okgrp: break
    print('  p=%d: 恒等式成立 %s | 分组无关(K_L=K_R) %s'
          % (p, '✓' if okid else '✗', '✓' if okgrp else '✗'))
print('  ⟹ 总进位数是【势函数的差】(coboundary)：K = [ΣS(in) − S(out)]/(p−1)')
print('     故它在结合律面上的 holonomy【恒为 0】——RH1（用计数版）自动失败')

print()
print('=== (B) 进位【模式】holonomy（位向量差）===')
for p in [2, 3]:
    nz = tot = 0
    for a in range(1, 50):
        for b in range(1, 50):
            for c in range(1, 25):
                vL1, _ = carry_vec(a, b, p, L); vL2, _ = carry_vec(a+b, c, p, L)
                vR1, _ = carry_vec(b, c, p, L); vR2, _ = carry_vec(a, b+c, p, L)
                CL = vL1 + vL2; CR = vR1 + vR2
                tot += 1
                if CL != CR: nz += 1
    print('  p=%d: 模式不同 %d/%d = %.4f  ⟹ RH1（模式版）%s'
          % (p, nz, tot, nz/tot, '通过 ✓' if nz/tot > 0.9 else '不通过'))
print('  但注意：模式由【路径中间值】唯一决定（carry_vec 是确定性函数）')
print('      ⟹ 属"历史硬编码"，任何保留中间值的零模型都复现 ⟹ 对 RH2 无判别力')

print()
print('=== (C) RH2：跨素数（CRT）统计能否分离？===')
random.seed(7)
for (p, q) in [(2,3), (2,5), (3,5)]:
    def vp(n, pr):
        k = 0
        while n % pr == 0: n //= pr; k += 1
        return k
    data = []
    for _ in range(30000):
        a = random.randint(1, 10**6); b = random.randint(1, 10**6)
        data.append((vp(a+b, p), vp(a+b, q)))
    def corr(d):
        n = len(d); mx = sum(x for x,_ in d)/n; my = sum(y for _,y in d)/n
        cov = sum((x-mx)*(y-my) for x,y in d)/n
        vx = sum((x-mx)**2 for x,_ in d)/n; vy = sum((y-my)**2 for _,y in d)/n
        return cov/(vx*vy)**0.5 if vx*vy > 0 else 0.0
    print('  p=%d,q=%d: corr(v_p(a+b), v_q(a+b)) = %+.6f' % (p, q, corr(data)))
print('  ⟹ 不同素数的赋值在随机输入下近似【独立】（CRT 的统计表现）')
print('     故"独立打乱 p-数字 / q-数字"的零模型与真实数据【统计不可分】⟹ RH2 失败')
