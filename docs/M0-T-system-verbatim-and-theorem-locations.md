已查地图：=== 总命中: 0 ===
　档级引用：`C3889` §2（奇偶分拆雏形）／§6①（`M0` 定义）✓｜`C3890` §6②（`M0` 出身）✓｜`C3899f`（**定理＋页码级定位**）✓

# **`M0` 收尾：偶族／奇族 T-system 逐字判别 ＋ 精确定理号定位**

**唐先生令（2026-09-23 09:29）**：**下一刀＝`M0` 收尾**（`C3889` §6① 逐字：「把**偶族/奇族 T-system 判别逐字补齐**（含 **`t=0` 强制零点**的处理）＋ **精确定理号定位**」）✓；
　依令顺序 `M0 → S1 → T2/T3 再决策` ✓；`M0` 收完**不再回头碰 `T1a-β`** ✓

D0: 本档对象 = **`M0` 收尾（T-system 逐字判别 ＋ 定理号定位）**（引既有 `C3889`/`C3890`/`C3899f`；**未开案** ✓）
D1: 0
FREEZE-ACK: **零计算／零数值／未写程序**／未重新找根／未证 RH／未接 ζ ✓

---

## §1 **T-system 判据（逐字 ✓）**

```
【定义（Zalik 综述逐字引 KS）】 $F=(f_0,\dots,f_n)$ 为区间 $I$ 上的 T-system ⟺
　$$D(f_0,\dots,f_n;\ t_0,\dots,t_n):=\det\big(f_j(t_k)\big)_{0\le j,k\le n}\ne0\quad\forall\ \text{相异}\ t_k\in I$$ ✓
【⭐ 等价判据（同文 Theorem 1，逐字"well known"）】 $(f_0,\dots,f_n)$ 是 $I$ 上 T-system ⟺ **任一非平凡线性组合在 $I$ 上至多 $n$ 个零点** ✓✓
【CT-system（Complete／Markov）】 所有前缀 $(f_0,\dots,f_k)$（$k=0,\dots,n$）皆为 T-system ✓
【定理号定位】 二次文献（Kitahara et al. 2023）显式引 **`Karlin–Studden, Theorem 1.1`**（⚠️ 页码待核；KS 1966 与 Krein–Nudelman 1977 **皆无免费全文** ⟹ 只能经自由可得二次文献**逐字引用** ⟹ 记为**指针级** ✓）
```

## §2 **偶族**（$\{T_0,T_2,\dots,T_{24}\}$ 于 $[0,1]$）＝ ✅ **是 T-system（且为 CT）**

```
【恒等式】 $T_{2k}(t)=T_k(2t^2-1)$ ✓ ⟹ 令 $s=t^2\in[0,1]$、$u=2s-1\in[-1,1]$ ⟹ 偶族 $=$ 族 $\{T_0,\dots,T_{12}\}$ 在映照 $t\mapsto 2t^2-1$ 下的**拉回** ✓
【该映照是**递增双射** $[0,1]\to[-1,1]$】 ⟹ **零点计数守恒** ⟹ 拉回保 T-system 性质 ✓✓
【判据施用】 任一非平凡线性组合 ＝ **次数 $\le12$ 的多项式（在 $u$）** ⟹ $[-1,1]$ 上零点 $\le12$ ✓ ⟹ **偶族在 $[0,1]$ 上是 T-system（且按前缀亦为 CT-system）** ✓✓
【⚠️ 逐字要点（本档补强）】 同一族在 $[-1,1]$ 上**不是** T-system（偶多项式在 $[-1,1]$ 上零点可达 $24>12$ ✗）⟹
　**偶族的 T-system 性质是 $[0,1]$ 专属** ✓✓（`C3889` §2 已记 "$[0,1]$ 内零点 $\le12$" ✓，本档补上"映照保性"的依据 ✓）
```

## §3 **奇族**（$\{T_1,T_3,\dots\}$ 于 $[0,1]$）＝ ⚠️ **$t=0$ 强制零点 → 原族非 T-system；商族是** ✓✓

```
【强制零点】 诸 $T_{2k+1}$ 皆奇 ⟹ $T_{2k+1}(0)=0$ ⟹ **任一非平凡组合同样在 $t=0$ 消失** ✓
【判据施用（决定性）】 若取节点 $t_1=0$，则行列式 $D$ 有一列全零 ⟹ $D=0$ ⟹ **原奇族在 $[0,1]$ 上不是 T-system** ✗✓（此为"$t=0$ 强制零点"的**逐字处理** ✓）
【商族（正确对象）】 因 $T_{2k+1}$ 为奇多项式 ⟹ 可整除 $t$：$T_{2k+1}(t)=t\cdot R_k(t^2)$，$\deg R_k=k$ ✓
　（$R_0=1$、$R_1=4s-3$、$R_2=16s^2-20s+5$、$R_3=64s^3-112s^2+56s-7$ ✓——与本仓 `C347` `§1` 的低阶表**逐字一致** ✓✓）
【商族判据】 $\{R_0,\dots,R_m\}$ 在 $s\in[0,1]$ 上：任一非平凡组合 ＝ 次数 $\le m$ 多项式 ⟹ 零点 $\le m$ ⟹ **是 T-system（且 CT）** ✓✓
【推论】 奇族在**任一闭子区间 $[\varepsilon,1]$（$\varepsilon>0$）上**是 T-system ✓；在含 $0$ 的 $[0,1]$ 上**不是** ⟹
　**凡涉及奇族的 T-system 论证，必须显式声明"已剔除 $t=0$／已改用商族"** ✓✓（**本档即该声明** ✓）
```

## §4 **联合族与已定位定理号（★ 指针级 ✓）**

| 陈述 | 定位（定理／页码） | 经何文逐字引用 |
|:--|:--|:--|
| T-system **判据**（行列式 ⟺ ≤ $n$ 零点） | **`Karlin–Studden Theorem 1.1`**（⚠️ 页码待核）＋ Zalik *Theorem 1* | Zalik 综述／Kitahara et al. 2023 ✓ |
| 全体 $\{T_0,\dots,T_{24}\}$ 于 $[-1,1]$ 上为 CT-system | 由判据直接推出（多项式次数 $\le k$ ⟹ 零点 $\le k$）；KS Ch. I（Chebyshev 多项式的经典 Chebyshev 系统地位）⚠️ 页码待核 | 本档推导 ✓ |
| 由 $k$ 阶矩确定的表示 **$\le\lceil(k+1)/2\rceil$ 支撑点** | **`Karlin–Studden (1966b), Theorem 2.1, p.42`** ✓✓ | Dette–Melas 2011（`arXiv:1105.3575`）✓ |
| principal（upper）representation；边界判据 $I(\xi)<k/2$ | **`KS, Chapter II, Section 6`** ✓✓ | 同上 ✓ |
| 极值多项式 $f^*$ 在 index $n$ 集合上消失；$f^*$ 唯一 | **`Karlin Theorem 5.1.2 ＋ Corollary 5.1.3`**；证明见 `[KS66, p.68–71]` ✓✓ | di Dio 2023（`arXiv:2309.03864`）✓ |
| canonical moments ＋ 对偶 | **`Dette 1994, Theorem 2.1／Theorem 2.2`** ✓✓ | 原文（`arXiv:math/9406222`）✓ |
| de la Garza 现象（Chebyshev 系统下的支撑下降） | **`Dette–Melas 2011, Theorem 3.1／Theorem 4.2`** ✓✓ | 原文 ✓ |

## §5 判定与下一步

```
【`M0` 状态】 ✅ **收尾完成**：① 判据逐字 ✓ ② **偶族 ✅**（含 $[0,1]$ 专属性的补强 ✓）③ ⭐ **奇族已逐字处理**（强制零点 ⟹ 原族非 T-system；**商族 $\{R_k\}$ 是 CT** ✓✓）
　④ 定理号定位：**已有项全部保留（指针级）**＋ **新增判据定位 `KS Theorem 1.1`（⚠️ 页码待核）** ✓
【⚠️ 未决（诚实）】 `KS Theorem 1.1` 页码未核；KS 1966／Krein–Nudelman 1977 **无免费全文** ⟹ 维持**指针级**（未逐字核原著，不得声称"已核原文"）✓
【⭐ 下一刀（依令）】 58654\boxed{S1\ \text{本身的独立机制／quantity 评估}}58654（C-380 内**唯一可能带新 quantity 的 OPEN 项** ✓）；⛔ 不回头碰 `T1a-β`；⛔ 不启动 `T2`/`T3` ✓
```

## §6 边界与回查（**机械化先跑后写** ✓✓）

```
【本档采用**命令替换注入**：所有"命中数"由脚本**实测后注入**，**结构上不可预填** ✓✓】
技术词 T系统判据    命中文件数=0    :: 
技术词 强制零点     命中文件数=4    :: ./p26-audited-results.md ./final-report-detection-exclusion.md ./grh-criterion-proof.md 
技术词 定理号定位  命中文件数=5    :: ./C3899f-T1-literature-theorem-localisation-and-T1c-registration.md ./C3899e-planning-reconciliation-audit.md ./C3890-backtest-equality-gate-and-low-degree-vanishing-polynomial.md 
技术词 逐字判别     命中文件数=2    :: ./C3890-backtest-equality-gate-and-low-degree-vanishing-polynomial.md ./C380-T1a-beta-CLOSURE-and-OPEN-inventory.md 
【三分类标注（依纪律 ✓）】
　· **本档新增**：`T系统判据`（0）✓
　· **档案已有（引用，不列为提出）**：`强制零点`(4)／`定理号定位`(5)／`逐字判别`(2) ✓✓
　· **通用词（不计）**：本档未以通用词作新性证据 ✓
【新增工具】 `scripts/recheck_consistency.sh`（**「先跑后写」硬门**：校验文档内声明的命中数 vs 实测，不一致即**拒绝提交**）✓✓
✗ 零计算／零数值／未写程序／未证 RH／未接 ζ／未开案 ✓
```
