# D*（椭圆曲线 Hecke 传播）——L3 判死

> 2026-09-07 13:45 · 唐先生 D* 设计的完整执行

## 设计（唐先生——）
- ensemble：椭圆同源类（LMFDB ec_classdata——aplist——）
- 对象：x_E(p^k)——Hecke 传播 x(p^{k+1}) = x(p)x(p^k) − x(p^{k−1})
- 测：跨 p 的 (x_E(p^k), x_E(q^k), x_E(r^k)) 三体残差
- 预判：若只恢复 Sato-Tate/Hecke 局部统计——L3 死——D 整代关闭

## 数据
- LMFDB ec_classdata API——500 同源类（conductor 10⁴-10⁸——）
- aplist[i] = a_{第 i+1 素数}（到 p=97——）
- Sato-Tate 验证：std = 1.0025（完美——）✓

## 结果（500 类——跨 k——）
### cumulant 粗筛
```
k=1: z = 0.84——k=2: z = −1.57——k=3: z = −0.53
```
### 符号离散化三体（±1——）
```
k=1: z = 0.61——k=2: z = 0.10——k=3: z = 1.76
k=4: z = 0.00——k=5: z = −0.51——k=6: z = −0.57
```
**全部 |z| < 3——无稳定 profile——符号随机摆动——**

## 判定：❌ D* 判死（按唐先生预判——）
**Hecke-local recursion + family ensemble ⇏ new higher-order propagation**
- 跨 p 的 x_E(p^k) 统计完全由 Sato-Tate（每 p 独立——）+ Hecke 递推解释
- 无 pairwise 不可约的三阶传播
- **D 这一整代（filtration/Hecke 传播方向——）关闭**

## 战略意义
- 椭圆曲线 a_p（有真实 Euler factor + Hecke 递推 + ensemble——）仍无三体传播
- 与 Rédei 结论一致：**算术的局部代数结构（无论多真实——）不自动产生跨位置的高阶统计传播**
- 强化 L3 门槛：候选必须显示 pairwise null 无法吸收的传播

## 文件
- scripts/fetch_ec_classdata.py / fetch_ec_v2.py——数据
- scripts/hecke_dstar_probe.py / hecke_dstar_final.py——探测
- data/ec_classdata_3000.json——500 类
