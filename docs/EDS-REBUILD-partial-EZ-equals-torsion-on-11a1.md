已查地图：命中（`EDS-INPUT-INVALID-P-is-5-torsion`／`CONVENTION-AUDIT-result`）⟹ 引用，不开新案
D0: 本档对象 = EDS 合法重建**部分结果**：`11a1` 上 `E(\mathbb Z)`＝挠群 ⟹ 非挠 `P` 有 `I(E,P)=\varnothing`；重建**未完成**
D1: 0 （[REVIEW] 轮次：部分结果与未完成声明，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **EDS 合法重建：部分结果（未完成）**

## §1 实算（本机）

```
**整点扫描** `x\in[-8,25]`：唯一整点＝`(5,5),(5,-6),(16,60),(16,-61)` ⟹ **恰好就是挠群 `\mathbb Z/5`** ✓✓
【⟹ 推论 1】 `11a1` 上 `E(\mathbb Z)=E(\mathbb Q)_{\rm tors}\cong\mathbb Z/5` ⟹ **不存在非挠整点** ✓
【⟹ 推论 2】 对非挠 `P`：`nP\in E(\mathbb Z)\Rightarrow nP` 挠 `\Rightarrow nP=O`（`5\mid n`）⟹ 与 `P` 非挠矛盾 ⟹ $$\boxed{I(E,P)=\{n:B_n=1\}=\varnothing\ \ (\text{非挠 }P,\ 11a1)}$$ ✓✓ —— **`B_n=1` 这一污染源在本曲线上自动消失** ✓
【⟹ 推论 3】 故 `11a1` 上的合法数据层应为 `B_n>1` 对所有 `n\ge2` 成立 ✓
```

## §2 ⛔ 重建未完成（诚实声明）

```
【卡点】 需要 `11a1` 上**非挠且有有理坐标**的 `P`；本次扫描范围（`x\in[-8,25]`）**只找到挠点** ⟹ **未取得合法 `P`** ⟹ **数据层尚未建立**，`CAP-1` **未跑** ✓
【下一步（明确）】 **(a)** 扩大 `x` 扫描范围 或 **(b)** 用 `11a1` 已知 Mordell–Weil 生成元（有理坐标，分母非 1）作 `P`；随后**硬断言** `nP\ne O`（`1\le n\le N`）✓
【审计项（就绪待跑）】 `m\mid n\Rightarrow B_m\mid B_n`；`\gcd(B_m,B_n)=B_{\gcd(m,n)}`（失败时**先查最小模型/坏约化/归一化，不改数据**）✓
【CAP 判据（不变）】 `T(S)=\{n>1:B_n>1,\ P_n\subseteq S\}`，$$\boxed{|T(S)|>|S|\ ?}$$ 且 `T` **不含** `B_n=1` 指标 ✓
【⛔ 纪律（照录）】 **不追 abc／不追 `N_0`**；首轮无 exceptional surplus 即**降级 EDS 线** ✓
【⛔ 撤回】 此前 `EDR`/`ZF-EDR` 各轮基于 `P=(5,5)` 的**全部数值结论标为 `invalid input / withdrawn`** ✓✓
【边界】 §1 为本机实算（`out/eds_legal_rebuild.txt`，可复跑）；§2 未完成声明为**本档自行推导**；未制造候选／未启动搜索／未碰 RH。
