已查地图：命中（`lindelof-reanalysis.md`（原始推导所在）／`m1-o1-proof.md`／`ZF-PD-2-explicit-expansion-and-verdict.md`（算术周期）／`META-OBSTRUCTION T1/T2`）⟹ **引用，不开新案** ✓
D0: 本档对象 = 「几乎周期推导中周期在哪里／如何体现／能否有限→无限」的精确回答
D1: 0 （`[REVIEW]` 轮次：定位与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **那条「几乎周期」推导里，周期在哪里？（精确回答）**

## §1 **先定位：原推导是什么**

```
【原始对象（逐字取自 `lindelof-reanalysis.md` §方向 2）】 $$S(t)=-\frac1\pi\sum_{p\le t}\frac{\sin(t\log p)}{\sqrt p\,\log p}+O(1)\qquad(\text{RH 下 }O(1),\ \text{无条件 }O(\log))$$ ✓
【实质】 这是**三角和**：频率 `\lambda_p=\log p`，系数 `c_p=1/(\sqrt p\log p)` ⟹ 即**准周期/Dirichlet 型三角级数** ✓
```

## §2 ⚠️ **「周期」在哪里？——不存在精确周期（第一层答案）**

```
【频率的独立性（唯一分解 ⟹ 初等）】 若 `\sum_p a_p\log p=0`（`a_p\in\mathbb Q`）则全部 `a_p=0` ⟹$$\boxed{\{\log p\}\ \text{在 }\mathbb Q\ \text{上线性无关}}$$ ✓✓
【⟹ 后果】 两个不同素数即 `\log q/\log p\notin\mathbb Q` ⟹ `e^{it\log p}` 与 `e^{it\log q}` **无公共周期** ⟹ 整个三角和**没有精确周期**（除常数）✓✓
【⟹ 「周期」的正确替代物】 **Bohr 意义下的 ε-几乎周期集**：$$\mathcal T_\varepsilon=\{\tau:\ |S(t+\tau)-S(t)|<\varepsilon\ \forall t\}\ \text{在 } \mathbb R\ \text{中相对稠密}$$ ✓ —— 这才是"几乎周期"一词的**精确含义**：不是"有周期"，而是"**平移近似回原样**"✓✓
```

## §3 **如何体现（定量）：密度随频率数**指数退化** ✓✓**

```
【Dirichlet 盒原理 + Kronecker】 对 `n` 个频率 `|\lambda_j|\le\Lambda`，`\mathcal T_\varepsilon` 在 `[0,T]` 内的密度下界 $$\gtrsim\Bigl(\frac{\varepsilon}{2}\Bigr)^{\!n}\frac{T}{\Lambda}$$ ✓✓ —— **随频率数 `n` 指数退化** ✓
【⟹ 读法】 「几乎周期」是**有限频率**的现象；每加一个频率，几乎周期集就**指数变稀** ⟹ 素数越多，几乎周期性越弱 ✓✓
```

## §4 ⭐⭐⭐ **有限 → 无限：能否靠这个"周期"完成？——不能（三条精确理由）**

```
**(i) 无精确周期**：`\ge2` 个频率即无理频率比 ⟹ 无周期可"整周期平移"⟹ 无法做**周期化延拓/取极限** ✓✓
**(ii) 均匀几乎周期性失效**：`\mathcal T_\varepsilon` 密度 `\asymp(\varepsilon/2)^n` 随 `n\to\infty` **指数塌缩** ⟹ Bohr 理论的核心假设（**一致**几乎周期）对**全素数三角和**不成立 ✗
　（⚠️ 档级：Bohr 证明 `\zeta(\sigma+it)` 在 `\sigma>1/2` 上（`\sigma`-依赖、局部一致）几乎周期；`\sigma\downarrow1/2` 时几乎周期集退化 ⟹ 临界线上的"均匀"版本**不可得**）✓
**(iii) 截断误差发散（致命）**：从 `p\le T` 截断到全部素数，误差 $$\sum_{p>T}\frac{1}{\sqrt p\,\log p}\ \longrightarrow\ \infty$$ ✗ ⟹ **无穷和的过渡本身就是发散的那一步** ⟹ 这正是本线的**聚合/截断墙**（＝`T1/T2` 型：有限分辨率信息不足）✓✓✓
【⟹ 判定】 $$\boxed{\text{「几乎周期」无法承担有限→无限：它既无精确周期，又随频率数指数退化，且截断发散}}$$ ✓✓
```

## §5 **唯一存在**精确周期**的地方：算术侧 `h_p`（但只能一个素数）**

```
【逐字承 `PD-2`】 $$h_p=\frac{2\pi i}{\log p},\qquad r^{-h_p}=1\iff \frac{\log r}{\log p}\in\mathbb Z\iff r\in p^{\mathbb N}$$ ✓ —— 对**第 `p` 个 Euler 因子精确周期**，且 `\Delta_p` **精确杀掉 `p`-primary** ✓✓
【⛔ 但第二个素数即失效】 `q^{-h_p}=e^{-2\pi i\log q/\log p}\ne1`（`\log q/\log p\notin\mathbb Q`）⟹ **无一公共周期** ✓✓（＝`PD-2` 封口的根因 ✓）
【⟹ 结论】 精确周期只存在于**单素数局部**；**不可提升到多素数/全素数** ⟹ 故也不能靠精确周期做有限→无限 ✗
```

## §6 **正确的替代工具：有无限极限，但只给统计（不是定位）**

```
【能处理无限和的两件】 **Kronecker/Weyl 等分布**（`\{t\log p\}` 的联合分布）＋ **Bohr–Jessen 值分布**（`\log\zeta` 的极限分布）⟹ 它们**确实**给出**无限极限定理** ✓
【⛔ 但性质】 给的是**值分布的测度论陈述**（"多大比例"），**不是逐零点定位** ⟹ 无法从"几乎周期"读出任一单个零点的位置 ⟹ 与 `T1/T2`（σ-对称统计信息不能定位）**一致** ✓✓
【⟹ 一句话】 周期/几乎周期能给的只有**统计**；而我们要的是**定位** ⟹ 这就是那条路走不通的**结构性原因** ✓
```

## §7 **结论 ＋ 边界**

```
【三问三答】 **(1) 周期在哪里？** —— **不存在**；频率 `\{\log p\}` 有理独立，故只有 Bohr ε-几乎周期集 ✓ **(2) 如何体现？** —— 体现为 `\mathcal T_\varepsilon` 的**相对稠密**，其密度 `\asymp(\varepsilon/2)^n` **随频率数指数退化** ✓ **(3) 能否有限→无限？** —— **不能**：无精确周期 ＋ 一致几乎周期性失效 ＋ 截断误差发散（＝`T1/T2` 型截断墙）✓✓
【补答】 唯一**精确周期**在算术侧 `h_p=2\pi i/\log p`，但**只对单素数**成立，第二个素数即失效（`PD-2` ✓）
【边界】 ⚠️ Bohr 几乎周期性的 `\sigma`-依赖与退化按**档级**；§2 频率独立、§3 密度估计、§5 单素数周期为**初等/本档推导** ✓；⛔ 未制造候选／未启动搜索／未改状态 ✓
```

## §8 【技术词回查】（逐字粘贴 ✓）

```
技术词 几乎周期     命中文件数=17   :: ./M(T)-attack-summary.md ./M(T)-lindelof-connection.md ./M(T)-phase-results.md 
技术词 准周期        命中文件数=12   :: ./breakthrough-exploration.md ./m-o1-bl-connection.md ./p49-g273r2c-first-round.md 
技术词 Bohr             命中文件数=29   :: ./CANDIDATE-SCAN-1-mathematical-content-review.md ./V106-L3-Q3-independent-sqrt-positivity-audit.md ./p510-proof-path.md 
```
【三分类】 **本档新增**：三问三答的**定位性结论**（周期不存在／密度指数退化／截断发散 ⟹ 不能有限→无限）✓；**档案已有（引用）**：`几乎周期`／`Bohr`（见上逐字）；**通用词（不计）**：`准周期` ✓
