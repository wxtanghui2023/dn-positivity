# P34-C' C2.1：固定 r<1 的 form convergence——q_{X,r}[f] 不 Cauchy（端点振荡继承）

> 2026-09-01 · 唐先生 C2.1 门 · 对象一致性审计 · dense core form convergence

## ⭐ 结果——固定 r<1——f 含小素数——q_{X,r}[f] 不 Cauchy
**r=0.5, 0.8, 0.95——e_2, e_3, (e2+e3)/√2, (e2+e100)/√2——全部不 Cauchy✗**（差 0.02-0.5——不衰减）
**唯一 Cauchy✓：(e100+e200)/√2（大素数对——差 ~0.001——但——w=e^-x/2 衰减——数值小——非真收敛）**

**η_r(X) 未充分衰减**（(e2+e3)：差 0.34/0.09/0.27——波动——不 →0）

## ⭐⭐ 关键解读——不是"小素数效应"——是端点振荡的全局继承
- **q_{X,r}[f] = Σ_k a_k(X) r^k (S_c²+S_s²)——a_k(X) 随 X 振荡（端点主导——(1+k²)^(−1/2) 振幅——无极限）——q 继承 X 振荡（即使 r<1 固定）**
- **"不收敛"是 X 截断的固有振荡（a_1(X) 的 X 振荡——影响所有含 k=1 mode 的 f）——不是 r 边界效应——不是"小素数效应"（唐先生正确——不能简单归因）**
- **"q_X[f] 对自然 dense core（含有限支撑——小素数）不 Cauchy ⟹ 不能声称存在 canonical closed form"（唐先生警报——确认！）**

## ⭐ 判定——C 分支（regularization obstruction）倾向
- **form convergence 失败（f 含小素数——r<1 固定也不 Cauchy）——dense core 上无 canonical closed form**
- **大素数对"Cauchy"是 w 衰减的数值小（e^{-100/2}≈0——贡献忽略）——非真收敛**
- **w=e^-x/2 的 canonical limit——仍未建立（不是"canonical-looking"——是"不收敛"）**

## ⚠️ 出路——a_k(X) 端点振荡扣除（renormalization）
- **"a_k(X) 端点主项 (cos(k log X)+k sin(k log X))/(1+k²) 可显式扣除"——剩余（o(1)）可能收敛？**
- **这对应唐先生三分叉表的第三行（renormalized w=1——未知——需重新审计 Gate 2'）**
- **任何含 a_k(X) 的构造都继承端点振荡——除非换 a_k 定义（renormalization/subtraction/不同 prime measure）**

## ⚠️ 诚实边界
- K=80 cutoff——X≤200000——"Cauchy"判定（差 <0.01——启发式）
- a_k(X) 用当前 X（无 X 独立极限）——q_{X,r} 的振荡是真实的（非数值）
- "端点振荡扣除"的 renormalization——未尝试——是下一候选

## 下一步
- (a) a_k(X) 端点振荡扣除测试（renormalized a_k^ren = a_k(X) − 端点主项——q 是否收敛）
- (b) C2.2（r-uniform control——但——先解决 X 振荡——否则无意义）
- (c) 唐先生指示
