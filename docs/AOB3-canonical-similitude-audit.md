# AOB3：char 0 是否存在 canonical arithmetic similitude？—— **element vs conjugacy class**

**依据**：唐先生 2026-09-11 09:39（撤回"period domain 产生 modulus"；新靶 = canonical arithmetic similitude $\Phi^\dagger Q\Phi=NQ$；若审计亦死则 AOB 封死到"char 0 缺 Frobenius-like similitude"）｜**约束**：无 $1/2$ 输入；L2 未动
**标注**：【引用·经典】【推导】【已注册·本项目】

---

## §0 登记撤回（采纳）
$$\boxed{\text{period domain}\Rightarrow\text{phase home}\ \text{✓ 但}\ \text{period domain}\not\Rightarrow\sqrt N\ \text{✗}}$$
$$\text{正确形式：}(Q,F^\bullet,\Phi)\to\lambda(\Phi,F)\ ;\ \Phi^\dagger Q\Phi=NQ\ \text{才给}\ |\lambda|=\sqrt N$$
函数域的不可替代核心 = **similitude 关系** $\Phi^\dagger Q\Phi=qQ$（极化 + arithmetic dilation 的绑定）✓

---

## §1 ⭐⭐⭐ 核心发现：char p 与 char 0 的差别**不是"有没有 Frobenius"，而是"元素 vs 共轭类"**
```
char p：Gal(𝔽̄q/𝔽q) 是【pro-cyclic】⟹ 存在【canonical 生成元】Frobenius
        ⟹ 可以对【元素】取【本征值】⟹ 本征值同时带【模】(√q) 与【辐角】(θ) ✓✓
char 0：Frobenius（在 p 处）只是 Gal(ℚ̄/ℚ) 中的【共轭类】，不是元素
        —— 共轭类【不能】canonically 取本征值（代表元需选择 ⟹ 非 canonical ✗）
        —— 共轭类能被 canonically 探测的【唯一】方式 = 【character / trace】（Chebotarev / Artin）
        ⟹ 于是"canonical 输出"自动是 character 型 ⟹ L-函数 ⟹ β-盲 ✓✓✓
```
$$\boxed{\text{char p：可以取【本征值】}\quad\text{char 0：只能取【character/trace】}}$$
$$\boxed{\Longrightarrow\ \text{全项目反复"崩回 character / L-函数"不是构造缺陷，而是【共轭类 vs 元素】强制的}}$$
【引用·经典】pro-cyclic 的绝对 Galois 群（有限域）；Chebotarev/Artin 只给出 trace/character 数据

---

## §2 局部 similitude 在 char 0 **确实存在**（但只是局部）
```
✓ Frobenius 类（在 p 处）作用在 ℓ-adic 上同调，配 Weil 配对/相交形式 ⟹ similitude，乘子 p^w
  （Deligne 定理：本征值的模 = p^{w/2} ✓）
✓ Hecke 本征值 λ_p 带 Ramanujan/Deligne 界 |λ_p| ≤ 2p^{(k−1)/2} ⟹ 同类结构 ✓
⟹ 但这些【逐素数】的局部数据合起来给出的是【Euler 因子】= 算术窗口（σ>1 收敛）
【已注册·本项目】Euler 积只在 σ>1 收敛；零点在窗口【之外】(0≤σ≤1) ⟹ 局部 similitude 看不到零点 ✓
```
$$\boxed{\text{char 0 有【局部】similitude ⟹ 给出 Euler 因子；但看不到零点（算术断裂）}}$$

---

## §3 全局候选的两条路，都死
| 路线 | 是否 canonical operator | 结果 |
|---|---|---|
| **(i) Galois 侧**（Frobenius 类、Hecke、对应） | 元素 ✗（只是共轭类） | 见 §1：canonical 提取 ⟹ character/trace ⟹ L-函数 ⟹ β-盲 ✗ |
| **(ii) 非 Galois 侧**（Deninger 型 flow/derivation，其生成元**不是**共轭类 ✓） | ✓ 有 canonical 生成元 | 但需【canonical polarization Q】使 $\Phi^\dagger Q\Phi=NQ$；**char 0 缺相交形式/正性** ⟹ 停在同一处 ✗ |
【已注册·本项目】Deninger 纲领停点 = 无限维上同调 + **正性**；Connes 6.6(i)(ii)（$k_\lambda\approx\theta_x$ 已数值否证）；C6-C：char 0 无条件 √-正性都来自【有限性】

---

## §4 于是对唐先生硬问题的回答
$$\boxed{\text{char 0 【没有】canonical arithmetic similitude —— 且有两个独立命名原因}}$$
```
(α) Galois 侧：Frobenius 是【共轭类】而非元素 ⟹ canonical 探测被迫走 character/trace ⟹ L-函数 ⟹ β-盲
(β) 非 Galois 侧：存在 canonical 算子（flow 的生成元）但【缺 canonical polarization】
    ⟹ 正是 Deninger/Connes 的停点与 C6-C（char 0 缺正性/相交形式）
⟹ AOB 按唐先生的预设【封死】："char 0 缺 Frobenius-like similitude"
   而且比"缺 Frobenius"更精确：缺的是【元素性】与【极化】两件事
```

## §5 一条建设性推论（对"第一个可构造入口"的判断）
```
唐先生希望 AOB 若活则得到"可实际构造的 RH 新架构入口"。
由 (α)：任何 Galois 侧 Φ 都受共轭类阻碍 ⟹ 必须走【非 Galois canonical 算子】
由 (β)：该算子还必须有【canonical polarization】
⟹ 所需的是【两件已知的难事】之合，而不是一件 ⟹ 门槛比 Deninger 单挑正性更高
（唯一活口仍是：非 Galois canonical 算子 + canonical polarization —— 即 Deninger 纲领的开放核心）
```

## §6 定位与边界
```
· §1 是【本轮最重要的结构发现】：element vs conjugacy class 解释了全项目的 character 崩塌
· §2 的局部 similitude（Deligne、Ramanujan）与 Euler 窗口为【引用·经典 + 已注册】
· §3(ii) 的停点为【已注册·本项目】（Deninger/Connes/C6-C）
· §4 的结论为【结构性】，且明确标注是在【已识别 canonical 来源】内
· 【未做】未输入 1/2；未构造模型；未改 L2；未声称与 ζ 连接
```

## §7 提交链
```
b7137b9 AOB2 → 本篇（AOB3：canonical similitude 审计 + element/conjugacy-class 机制）
```
