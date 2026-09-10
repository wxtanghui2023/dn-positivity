# 甲：2-cover 的显式构造（$K=\mathbb Q(\sqrt2)$）—— **纯构造/实算，未审计**

**日期**：2026-09-10 20:30+ ｜ 依据：唐先生（先做甲；五步目标；不做 GPS 审计）｜ 代码 `scripts/two_cover_construct.py` ｜ 输出 `/tmp/two_cover_out.txt`

---

## §0 任务（唐先生）
$$\boxed{\mathfrak a^2=\mathfrak D_K^{-1}\ \text{在 }K\text{ 中无解}\ \Longrightarrow\ \text{存在一个【自然的】2-cover，使其可解}}$$
**要求做成明确对象**（不只是"可以开平方"）：
$$\mathcal C_K=\{\text{fractional ideals / ideal classes together with a chosen square root datum}\},\qquad \pi:\mathcal C_K\to Cl(K),\qquad \widetilde{\mathfrak a}^{\,2}=\pi^*(\mathfrak D_K^{-1})$$
**五步**：① $\mathfrak D_K$ 的素理想分解 ② 奇偶性为何阻止 $K$ 内平方根 ③ 具体构造 quadratic/2-descent lift ④ lift 后平方关系是否真成立 ⑤ **确认 obstruction 是否真的落在 $Cl(K)/2Cl(K)$ + 局部 parity，而不是事后赋予的名称**

## §1 对象与映射（显式）
$$\mathcal C_K:=\bigsqcup_{\gamma\in K^\times/(K^\times)^2}\Big\{(\gamma,\mathfrak a)\ :\ \mathfrak a\ \text{is a fractional ideal of}\ K(\sqrt\gamma),\ \mathfrak a^2=\mathfrak D_K^{-1}\mathcal O_{K(\sqrt\gamma)}\Big\}$$
```
π_naive : C_K -> Cl(K),  (γ,𝔞) ↦ [𝔇_K]
⚠️ 但 §3 显示：π_naive 【丢失局部 parity】，故正确的目标是
   π_ref : C_K -> Cl(K)/2Cl(K) × 𝒫,   𝒫 = 局部 parity 数据（Kummer 数据）
```

## §2 步骤 ①–④ + 核验
**① 分解**：$\mathcal O_K=\mathbb Z[\sqrt2]$，$f=x^2-2$，$\mathfrak D_K=(f'(\alpha))=(2\sqrt2)=(2)(\sqrt2)=(\sqrt2)^3$
$$\boxed{v_{(\sqrt2)}(\mathfrak D_K)=3\ \text{（奇）};\quad |D_K|=8\ \text{不是完全平方}}$$
**② 为何 $K$ 内无解（范数障碍，纯算术）**
$$\mathfrak a^2=\mathfrak D_K^{-1}\ \Longrightarrow\ N(\mathfrak a)^2=\frac1{|D_K|}=\frac18\ \Longrightarrow\ N(\mathfrak a)=\frac1{\sqrt8}\notin\mathbb Q$$
而任何分式理想的范数是**正有理数** ⟹ **$K$ 内不存在这样的 $\mathfrak a$** ✓（非命名约定，是范数/有理性障碍；$1/8$ 非有理平方已核验）
**③ 显式 2-cover（由分歧元素强制）**
```
取 γ = √2（分歧元素，在分歧素处 valuation = 1）
K' = K(δ), δ² = γ = √2  ⟹  K' = Q(2^{1/4}),  [K':K] = 2
核验：δ² = (0,0,1,0) = √2 ✓（(δ)² = (√2) 作为主理想成立）；N(δ) = −2 ✓，N(δ²) = 4 ✓
```
**④ lift 后平方关系**：
$$\mathfrak a'=(\delta^{-3})\ \Longrightarrow\ \mathfrak a'^2=(\delta)^{-6}=(\delta^6)^{-1}=\big(\mathfrak D_K\mathcal O_{K'}\big)^{-1}=\mathfrak D_K^{-1}\mathcal O_{K'}\quad\boxed{\checkmark\ \text{精确成立}}$$
```
范数核验：N_{K'/Q}(𝔞')² = 1/|D_K|^{[K':K]} = 1/8² = 1/64 ⟹ N(𝔞') = 1/8 ∈ ℚ ✓（64 = 8² 为完全平方）
指数加倍：v_δ(√2) = 2 ⟹ v_δ(𝔇_K O_{K'}) = 3×2 = 6（偶）✓
```

## §3 ⑤ **obstruction 的真实位置** —— 并更正我此前的说法
```
Cl(Q(√2)) = 1  ⟹ Cl/2Cl 【平凡】。而 obstruction 却是真的。
⟹ **不能**把此例的 obstruction 归因于 Cl(K)/2Cl(K)——那个商在这里消失
⟹ 真实障碍 = 【局部 parity 数据】 v_(√2)(𝔇_K) = 3 奇
   其自然居所 = Kummer 数据 K^×/(K^×)²（等价地：idèle 类群的 2-挠部分），**不是** Cl(K)/2Cl(K)
```
$$\boxed{\textbf{更正（errata to bfa4227）}:\ \text{"obstruction} = \mathfrak D\ \text{在}\ Cl/2Cl\ \text{的类"是【不完整】的}}$$
$$\boxed{\text{修正后的分解}:\ \text{obstruction} = (\text{局部 parity 数据})\times(\text{2-descent／类群数据})}$$
```
局部因子：在 cover 中由【分歧加倍估值】修掉
2-descent 因子：决定"【一个】2-cover 是否足够"
K = Q(√2)：局部因子非平凡（v=3 奇），2-descent 因子平凡（h=1）⟹ 一个 cover 足够 ✓（已显式构造并验证）
```

## §4 为何这个 cover 是 **canonical**（不是我们挑的）
```
① 取 γ = 被分歧元素本身 ⟹ cover 由【算术数据】强制，无人为选择
② 一般机制：degree-2 Kummer cover 使分歧素处 valuation 【加倍】⟹ 一切【奇】指数变【偶】
   等价地：提升后的 different 范数 = |D_K|² = 64 = 8² 是【完全平方】
   ⟹ **2-cover 恰好"把判别式变成平方"**，这正是 §2 第二步所缺的有理性
```

## §5 诚实边界（含**第二条勘误**）
```
· §0 的任务、五步、以及"本轮不做 GPS 审计"——唐先生指定
· §1 的 𝒞_K 与 π 定义、§2 的分步核验、§3 的定位与更正、§4 的 canonical 论证——小灵本轮
· 【经典引用，非我证明】：（C1）𝔇_K=(f'(α))；（C2）(2)=(√2)² 于 ℚ(√2)；𝔞* = 𝔞^{-1}𝔇^{-1}；Cl(ℚ(√2))=1
· 【实算】：δ²=√2、N(δ)=−2、N(δ²)=4、N(δ³)=−8、𝔞'²=𝔇^{-1}O_{K'}（元素恒等式，精确）；1/8 非有理平方（有界搜索）
· ⚠️ 未验证：一般的"一个 2-cover 总是足够"（本文件只对 ℚ(√2) 显式验证；一般情形为论证）
· ⚠️ **未给出** 2-descent 因子非平凡（即 [𝔇] ∉ Cl²）的具体例子 —— 诚实缺口
· ⚠️ **第二条勘误（to bfa4227）**：二次域表中 d ≡ 3 mod 4 各行（3, −3, 7, −7, −11）的【指数向量不完整】：
      漏了 2 上素理想的偶指数 2（如 ℚ(√5) 无关；ℚ(√3)：𝔭₂ 指数 2、3 处指数 1）
      ⟹ **存在性 verdict 全部不变**（失败仍由奇指数处造成），但**记录需更正**（本项目纪律要求）
· 本轮仍未做任何审计；未声称临界指数；未声称与 ζ 连接
```

## §6 下一步（唐先生指示：若甲成立则做乙）
```
乙 = 把这个 2-cover 上的 pairing 与 ramification filtration 接起来：
    检查 2-cover 上的兼容律能否【跨分歧层传播】（即把 A′ 的 transport 从 p-power 层换成分歧层）
```

## §7 提交链
```
bfa4227 数域版 A′ → 本篇（甲：2-cover 显式构造 + obstruction 归属更正）
```
