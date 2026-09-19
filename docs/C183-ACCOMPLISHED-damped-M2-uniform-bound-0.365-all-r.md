已查地图（**先查后写**）：`C-181`（§8 引理 2、§10 甲的结构探索：阻尼曲线 d_2(r)、活跃集、单纯形签名）、`C-152`/`C-154`（M=2 单模的三段拼装）、`E4-ENGINE-1`（Montgomery Lemma 2.2 转引）。关键词回查：`网格桥接`=0、`箱下界证书`=0、`阻尼全覆盖`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 20:5x「可以继续甲」）**：执行甲 —— **阻尼 M=2 的中间区证书** ✓
**结论（先行）**：$$\boxed{\textbf{定理（本档，已严格证书）}：\ \forall r\in[0,1],\ \forall(\varphi_1,\varphi_2)\in[0,\pi]^2：\ \max_{1\le k\le10}\big[\cos(k\varphi_1)+r^k\cos(k\varphi_2)\big]\ \ge\ \mathbf{0.364984…}}✓✓$$
$$\qquad \Longrightarrow\ \textbf{阻尼 M=2 的一致下界}＝\mathbf{7.3\times}\ \text{Montgomery 的}\ \tfrac1{20}✓✓$$
$$\qquad \Longrightarrow\ \textbf{填补了}\ \text{C-181}\ \text{两条引理之间的【中间阻尼区】}\（\text{引理 1 需}\ \rho\ \text{小／}\ M\ \text{大；引理 2 需}\ \delta\ \text{小}\）✓✓$$

FREEZE-ACK: 本档即冻结期内的攻击性推导（依 `§8.1`；不产候选结论）

D0: 本档对象 = **阻尼 M=2 的一致性定理（网格证书 ＋ 10-Lipschitz 桥接）** —— 关系 = 新定理（证书型），非新机制
D1: 0

# C-183 · ⭐⭐ 甲完成：阻尼 M=2 的全区间一致下界（`0.365`，7.3× Montgomery）

---

## §1 定理与证明结构

$$\textbf{定理}：\ \forall r\in[0,1]\ \forall(\varphi_1,\varphi_2)\in[0,\pi]^2：\ \max_{1\le k\le10}\big[\cos(k\varphi_1)+r^k\cos(k\varphi_2)\big]\ \ge\ 0.364984\ldots✓$$
$$\textbf{证明（两步）}：$$
$$\textbf{① 逐点证书（}\text{334 个}\ r\ \text{网格点，全部通过}）\text{：}$$
$$\qquad \text{对每个}\ r_i=i\cdot\text{step}\ (\text{step}=1/333)\ \text{用【精确可分离箱下界 ＋ 自适应 B\&B】证明}$$
$$\qquad \max_{k\le10}\big[\cos(k\varphi_1)+r_i^k\cos(k\varphi_2)\big]\ \ge\ 0.38\qquad(\forall\varphi\in[0,\pi]^2)✓$$
$$\qquad \text{实测}：\text{每点}\ 768\text{–}2\,624\ \text{箱，}\mathbf{0}\ \text{未定}；\text{共}\ 473\,792\ \text{箱}／2.6\ \text{s}；\text{最差余量}\ 4.81\times10^{-6}✓$$
$$\textbf{② Lipschitz 桥接}：d_2(r):=\min_\varphi\max_k S_k(r,\varphi)\ \text{关于}\ r\ \text{是}\ \mathbf{10}\text{-Lipschitz}✓$$
$$\qquad \text{理由}：|\partial S_k/\partial r|=|k r^{k-1}\cos(k\varphi_2)|\le k\le10\ (r\le1,\ k\le10)；\text{max 的 Lipschitz 常数}\le\max_i(\text{各}f_i\ \text{的常数})✓$$
$$\qquad \Longrightarrow\ r\in[r_i,r_{i+1}]\ \text{时}\ d_2(r)\ \ge\ 0.38-10\cdot\tfrac{\text{step}}2=0.38-0.0150=\mathbf{0.36498}✓✓$$

## §2 箱下界的构造（可分离性，精确）

$$\text{对箱}\ B=I_r\times I_1\times I_2\ \text{与固定}\ k：S_k\ \textbf{在}\ (\varphi_1,\varphi_2)\ \text{上可分离}：\ \min_B S_k=\min_{I_1}\cos(k\varphi_1)+r^k\min_{I_2}\cos(k\varphi_2)✓$$
$$\qquad \Longrightarrow\ \mathrm{LB}(B)=\max_{k\le10}\Big[\min_{I_1}\cos(k\varphi_1)+r^k\min_{I_2}\cos(k\varphi_2)\Big]\ \le\ \min_B\max_k S_k✓$$
$$\qquad （\text{依据}\ \max_k\min_B\le\min_B\max_k；\text{单区间}\ \cos\ \text{最小只在奇倍}\ \pi\ \text{取}\ -1，\text{否则端点取小}）✓$$
$$\qquad \text{保守化}：\text{每项扣}\ \mathrm{SLACK}=10^{-12}；\text{奇倍}\ \pi\ \text{检测加}\ \mathrm{TEST\_EPS}=10^{-9}\ \text{（保守判为命中）}✓$$

## §3 意义（三条）

$$\textbf{① 补上中间区}：\text{C-181 引理 1（重阻尼／大}\ M\text{）与引理 2（近单位模）之间的空档，}$$
$$\qquad \text{在}\ \mathbf{M=2}\ \text{时被本档完整覆盖}✓✓\（\text{数值最坏}\ r^\ast=0.70\ \text{处也}\ \ge0.42\gg0.365✓\）$$
$$\textbf{② 常数}：0.365＝\mathbf{7.3\times}\ \tfrac1{20}✓\ ——\ \text{这是【阻尼情形】首次拿到优于 Montgomery 的一致常数}✓✓$$
$$\textbf{③ 方法可复用}：\text{"网格 ＋ Lipschitz 桥接"避开高维 B\&B；}\text{对}\ M=3,4\ \text{可加一个维度（}\varphi\ \text{维），}\text{成本按}\ 2^M\ \text{增长}✓$$

## §4 边界（诚实）

- ⚠️ 证书依赖 `SLACK=1e-12`（每项浮点误差界）与 `TEST_EPS=1e-9`（π 检测保守化）——**与本项目其它证书同族假设**；区间算术版**未做**（下一步 ✓）
- ⚠️ 定理覆盖 `r ∈ [0,1]`（阻尼已完整）与 `φ ∈ [0,π]²`（由 `cos` 偶性＋`2π` 周期性，等价于全平面 ✓）
- ⚠️ 窗口 `k ≤ 10`（= `5M`，`M=2`）✓；**不声称** `M ≥ 3` 的阻尼版 ✗
- ⚠️ 定理为 **plus**（正下界）而非最优常数：数值真值 `min_r d_2(r) ≈ 0.4216` ✗（本界 0.365 留有余地 ✓）
- **未用** RH；**未改**他档 ✓；**纪律**：先查后判 ✓、**先跑后写** ✓

## §5 复现

```
脚本: scripts/damped_m2_certificate.py（单点证书；RLO=RHI=r）
      scripts/damped_m2_grid_certificate.py（全区间网格 + 桥接）
复现: python3 scripts/damped_m2_grid_certificate.py 334 0.38 6000000
结果: {"certified": true, "n_fail": 0, "total_neval": 473792, "bridged_bound": 0.364984…,
       "worst_margin": 4.81e-06, "seconds": 2.6, "sha16": "5c5e5de44d8e60cd"}
```

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`）`[纪律]`

```
技术词 网格桥接   命中文件数=0 ::  ⟹ 本档新增
技术词 箱下界证书  命中文件数=0 ::  ⟹ 本档新增
技术词 阻尼全覆盖  命中文件数=0 ::  ⟹ 本档新增
```
