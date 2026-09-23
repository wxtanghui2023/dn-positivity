已查地图：命中（`ZF-ZLG-2`（分岔＝anomaly 等价）／`ZF-ZAI-2`（阈值死因：解析性⟹非解析⟹阈值）／`E-44`／`T7` 本线自档）⟹ **引用，不开新案** ✓
D0: 本档对象 = `PD-2` 的 Euler 项完全展开（精确公式）＋ `p`-primary 精化 ＋ 收敛/续算墙 ＋ 兼容性普遍性 ＋ 判定
D1: 0 （`[REVIEW]` 轮次：展开与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-PD-2`：`\mathcal C_{p,q}` 的精确展开与判定**（本档全为自行计算 ✓✓）

## §1 **精确展开（本档核心计算 ✓✓）**

```
【设定】 `h_p=2\pi i/\log p`、`\Delta_p f(s)=f(s+h_p)-f(s)`、`f_r(s):=\dfrac{r^{-s}}{1-r^{-s}}=-\dfrac{\zeta'/\!\log}{}` 之单项 ✓
【记】 `x:=r^{-s}`、$$\lambda_r:=r^{-h_p}=e^{-2\pi i\log r/\log p}$$（同 `\mu_r:=r^{-h_q}`）✓ ⟹ 注意 `\lambda_r=1\iff r` 是 `p` 的幂 ✓✓
【单差分】 $$\Delta_p f_r=\frac{x(\lambda_r-1)}{(1-x\lambda_r)(1-x)}$$ ✓
【⭐⭐ 双差分（本档精确公式）】 逐项展开 ⟹
　$$\boxed{\ \Delta_p\Delta_q f_r=\sum_{k\ge1}x^k\bigl(\lambda_r^{\,k}-1\bigr)\bigl(\mu_r^{\,k}-1\bigr)\ }$$ ✓✓
　（首项 `x(\lambda-1)(\mu-1)`；因 `|x|<1` 当 `\sigma>0`，级数收敛 ✓）
【等价闭式】 $$\Delta_p\Delta_q f_r=x\Bigl[\tfrac{\lambda\mu}{1-x\lambda\mu}-\tfrac{\lambda}{1-x\lambda}-\tfrac{\mu}{1-x\mu}+\tfrac{1}{1-x}\Bigr]$$ ✓
```

## §2 ⭐ **`p`-primary 精化（对您 §16 的加强 ✓）**

```
【加强】 `\Delta_p f_r=0` **不仅**当 `r=p`，而是当且仅当 **`r` 是 `p` 的幂**（因 `\lambda_r=1\iff \log r/\log p\in\mathbb Z\iff r\in p^{\mathbb N}`，由唯一分解 ✓✓）
【⟹ ⟹ 结构陈述】 $$\boxed{\Delta_p\ \text{精确杀掉 }p\text{-primary 分支}}$$；$$\boxed{\Delta_p\Delta_q\ \text{精确杀掉 }p^{\mathbb N}\cup q^{\mathbb N}}$$ ✓✓
【⟹ 显式余项】 $$\mathcal C_{p,q}(s)=-\!\!\sum_{r\notin p^{\mathbb N}\cup q^{\mathbb N}}\!\!(\log r)\sum_{k\ge1}r^{-ks}\bigl(\lambda_r^k-1\bigr)\bigl(\mu_r^k-1\bigr)$$ ✓（对 `\Re s>1` 绝对收敛 ✓；且 `r\notin p^{\mathbb N}\cup q^{\mathbb N}` 时 `\lambda_r^k,\mu_r^k\ne1\ (\forall k)` ✓✓）
```

## §3 ⛔ **收敛结构：无改善（本档）**

```
【双重差分是否改善收敛？】 `|\Delta_p\Delta_q f_r|\le 4\,r^{-\sigma}/(1-r^{-\sigma})` ⟹ 与单项同阶 ⟹ $$\boxed{\text{收敛域仍是 }\Re s>1\ \text{（无改善）}}$$ ✓✓
【⟹ 续算墙原样存在】 `\operatorname{Res}_{s=\rho}\mathcal C_{p,q}=m` 是**带内**恒等式 ⟹ 任何**从余项直接算 residue** 的尝试都需**解析延拓** ⟹ 撞 `T7`/ZAI 的**有限-精确墙** ✗ ✓✓
【振荡性（您的期望）】 `(\lambda^k-1)(\mu^k-1)` 确为 `r` 的双频振荡因子（频率 `k/\log p, k/\log q`）✓ —— 但**不足以扩展收敛域** ✗（Bohr/Voronoi 型改善不达临界带）✓
```

## §4 ⭐⭐ **`\operatorname{Res}` 的两条致命性质（本档判定核心）**

```
**(i) `p,q`-无关（本档）** 由定义 `\mathcal C_{p,q}=\Delta_p\Delta_q(\zeta'/\zeta)`，`s+h_p,s+h_q,s+h_p+h_q` 处 `\zeta'/\zeta` 在 `\rho` **无极点**（除非 `\rho-h_p` 等恰为零，测度零情形）⟹ 四项中只有 `+(\zeta'/\zeta)(s)` 贡献极点 ⟹
　$$\boxed{\operatorname{Res}_{s=\rho}\mathcal C_{p,q}=m\qquad\text{（对所有 }p,q\text{ 相同）}}$$ ✓✓
**(ii) 因此 `\operatorname{Res}` 只记录重数** ⟹ 对简单零点 `m=1` ⟹ **β-盲** ✓✓（与 argument principle 同型，您 §4 已察 ✓）
【⟹ ⭐ 关键否定（针对您 §19）】 "离轴零点是否只与有限多个 `p` 兼容？" —— **不成立**：兼容性（`\operatorname{Res}=m`）对**一切** `p,q` **普遍成立** ⟹ $$\boxed{\text{兼容性无离散性；§19 的"有限兼容"希望落空}}$$ ✓✓✓
```

## §5 **最终判定**

```
【`PD-2` 的净结果】 精确公式 ✓（§1）｜`p`-primary 精化 ✓（§2）｜但：
　**(W1) 续算墙**：余项求和仅在 `\Re s>1` 收敛 ⟹ 带内 residue 须解析延拓 ⟹ 有限-精确墙原样 ✗
　**(W2) 整数指标 β-盲**：唯一整数（`\operatorname{Res}=m`）`p,q`-无关且只记录重数 ✗
　**(W3) 阈值墙（承 `ZAI-2`）**：`\mathcal C_{p,q}` 在 `\rho` 的**正则部分*确*依赖 β**（`r^{-\beta}` 幅度 ✓），但它是解析量 ⟹ 由 `ZAI-2` 死因：**非解析取离散 ⟹ 只剩阈值型** ✗✓✓
【⟹ 判定】 $$\boxed{\text{`PD-2`：CLOSED —— 三墙（续算／整数 β-盲／阈值）逐条命中}}$$ ⛔ 不再展开 `\mathcal C_{p,q,p'}` 等高阶版本（同型，无新信息）✓
【保留的可复用部分】 `h_p=2\pi i/\log p` 的**精确周期性** ＋ `\Delta_p` 杀 `p`-primary 的**精确性** ＋ §1 的**精确差分公式** —— 三者作为**工具**保留（以后若有新接口可直接取用）✓
```

```
【账本】 `EDR`/`RPC-1` PASS/保留｜离轴→稀有算术集 CLOSED｜显式公式 CLOSED｜局部 jet CLOSED｜分岔范式 CLOSED｜**`PD-2`（素数周期双差分）本档 CLOSED（三墙）**｜自生分岔（零点算术描述）OPEN（比原 GAP 更强）｜finite event→finite zeros 已有工具可接 ✓
【边界】 ⚠️ §4(i) 的"测度零例外"为常规技术情形（档级）；⛔ 未制造候选／未启动搜索／未改状态；⭐ §1–§4 全为**本档自行计算/推导** ✓
```
