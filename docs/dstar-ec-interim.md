# D* 椭圆曲线版——中间状态（数据 + 初步探测）

> 2026-09-07 13:30 · 唐先生 D* 设计（椭圆曲线同源类 ensemble——）

## 数据
- LMFDB `ec_classdata` API——aplist（a_p 素数序——）——同源类（lmfdb_iso——class_size——）
- 已确认索引：aplist[i] = a_{第 i+1 素数}——aplist 到 p=97（25 素数——）
- 已拉 100 类（API 限速——继续拉中——）
- Sato-Tate 验证：mean −0.012——std 1.0025（完美——）✓

## 初步探测（100 类——cumulant 粗筛——）
跨 p 三体 (x_E(p^k), x_E(q^k), x_E(r^k))：
```
k=1: κ3 = −0.073——z = −0.85（无——）
k=2: κ3 = −0.003——z = −0.04（无——）
k=3: κ3 = +0.146——z = +1.56（弱——<3σ——）
```
- 100 类初步无显著信号（z < 2——）
- **ensemble 太小不能判死**——需 1500-3000 类

## 状态
- 数据拉取受 LMFDB API 限速（后台继续——）
- 下一步：数据齐后跑完整 D*（Δ₃ vs pairwise max-ent——离散化——k 稳定 profile——）

## 文件
- scripts/fetch_ec_classdata.py / fetch_ec_v2.py——数据拉取
- scripts/hecke_dstar_probe.py——初步探测
- data/ec_classdata_3000.json——100 类（临时——）
- data/lmfdb_1.12/1.16.traces.txt——level-1 form（备用——）
