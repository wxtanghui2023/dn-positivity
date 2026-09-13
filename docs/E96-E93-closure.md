# E96 · ⛔ **E93 正式封档（DEAD）** ✗ —— 死因：**Theorem 4 属 $S_1$ 级，不是 $S$ 级**

> 判定 ✓ 唐先生（2026-09-13 21:03，**以原图逐式核对** ✓）｜执行 ✓ 小灵
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 判定与死因（✓ 精确 ✓）

$$\boxed{\textbf{E93 = DEAD}}\ ✗$$

$$\boxed{\text{死因 ＝ Theorem 4 的强 remainder 属 }S_1\text{，而 E93 需要 }S\text{；Karatsuba 的 }S\text{-level 分解【未给出】所需的 }L^{-1}\text{ 衰减}}$$

## 1. Theorem 4 的对象（✓ 原图裁决 ✓ —— **我的推断获确认 ✓**）

$$\int_T^{T+H}\Bigl|S_1(t)+\frac1\pi\int_{0.5}^{\infty}\log|\zeta(\sigma)|\,d\sigma-\frac1\pi\sum_{n<x}\frac{\Lambda(n)}{\sqrt n\log^2n}\cos(t\log n)\Bigr|^{2k}dt=O(HL^{-2k})$$
$$S_1(t)=\int_0^tS(u)\,du\ \ \Longrightarrow\ \ \boxed{\textbf{对象是 }S_1\text{ 级}\ ✗}$$

```
✅ **原图确认（非 OCR 误读 ✓）**：$\log^2n$ 签名成立 ✓（我此前的推断**正确** ✓）
⚠️ **我方 OCR 的一处偏差 ✓**：我曾读作 "$\int_0^\infty(\cdots)d\alpha$" ✗ ——
   实际是 $\frac1\pi\int_{0.5}^{\infty}\log|\zeta(\sigma)|d\sigma$ ✓（**以唐先生原图为准** ✓）
```

## 2. 第 930 页进入 $S$ 级的只有 $R_1,R_2$（✓ 逐字 ✓）—— **且不够** ✗

$$|S(t)|^{2k}=\frac1{\pi^{2k}}\Bigl|\sum_{p<x}\frac{\sin(t\log p)}{\sqrt p}\Bigr|^{2k}+O(R_1+R_2)$$
$$R_1=\Bigl|S(t)+\frac1\pi\sum_{p<x}\frac{\sin(t\log p)}{\sqrt p}\Bigr|^{2k},\qquad
R_2=\Bigl|\sum_{p<x}\frac{\sin(t\log p)}{\sqrt p}\Bigr|^{2k-1}\Bigl|S(t)+\frac1\pi\sum_{p<x}\frac{\sin(t\log p)}{\sqrt p}\Bigr|$$

$$\int_T^{T+H}R_1(t)dt=O(H)\ \ (50)\qquad
\int_T^{T+H}R_2(t)dt=O\bigl(H(\log\log T)^{k-\frac12}\bigr)\ \ (51)$$

$$k=1:\qquad \int R_1=O(H),\qquad \int R_2=O\bigl(H\sqrt{\log\log T}\bigr)\ \ \Longrightarrow\ \ \textbf{远达不到}\ \|R_S\|_2^2\lesssim\frac{H}{\log T}\ \ ✗$$

```
⚠️ **$R_1,R_2$ 是【非线性误差项】** ✓ —— 与 Theorem 4 里那个 $S_1$ 级 remainder **不是同一个对象** ✗
```

## 3. ⭐ **决定性逻辑：微分放大高频**（✓ 唐先生的模型 ✓）

$$R_{S_1}\ \text{控制的是}\ \int S,\qquad R_S=\frac{d}{dt}R_{S_1}\qquad\Longrightarrow\qquad
\|R_{S_1}\|_2\ll\frac{\sqrt H}{L}\ \ \not\Rightarrow\ \ \|R_S\|_2\ll\frac{\sqrt H}{L}\ \ ✗$$

$$\text{模型（唐先生 ✓）}：f(t)=\frac1L\sin(Lt)\ \Longrightarrow\ \|f\|_2\asymp\frac{\sqrt H}{L}\ \ \text{而}\ \ \|f'\|_2\asymp\sqrt H\ \ ✗$$

$$\boxed{\textbf{不存在合法的"把 Theorem 4 的 }L^{-2}\text{ 微分成 }S\text{ 级的 }L^{-2}\textbf{"的步骤}}$$

## 4. E93 账本的作废（✓）

$$\underbrace{2.4012\times10^{4}}_{\text{素数侧 ✓ 可留}}+\underbrace{\mathbf{2.3351\times10^{5}}}_{\textbf{来自错误替换 }R_S\rightsquigarrow R_{S_1}\ ✗}=\ 2.5752\times10^{5}\ \ (\text{4.1265× 余量})\ \ \Longrightarrow\ \ \textbf{不能进入最终证明}\ ✗$$

## 5. ⭐ 我 E95 结论的精确化（✓ 唐先生更正 ✓）

$$\boxed{\text{「逐项分离」}\ \neq\ \text{「逐项得到【小】余项」}}$$

```
✅ **我对的前半** ✓：证明里**没有**"从整体二阶矩反推余项"的偷换 ✗（确为逐项 $R_1,R_2$ ✓）
✗ **我错的后半** ✗：以为"逐项分离 ⟹ 足够"—— 实际分离出的 $R_1,R_2$ 只到 $O(H)$、$O(H\sqrt{\log\log T})$ ✓，
   **达不到 E93 门槛** ✗ ⟹ **分离 ≠ 小** ✓
```

## 6. 封档条款与**存留之物** ✓

```
⛔ **封档 ✓**：**不再**从 Karatsuba 的 Theorem 4／3／C 里继续挖同一缺口 ✗（照唐先生指示 ✓）
✅ **存留 ✓（重要 ✓）**：**E92 的"素数侧—chirp 非共振"【本身没有死】✓**
   —— 死的是**接口** ✗：用它 ＋ Karatsuba 的 $S_1$-remainder 去提供 **$S$ 级尾界** ✗
   ⟹ 今日真正留下的**更窄开放问题** ✓：
   $$\boxed{\text{能否【独立构造】}S(t)=P_x(t)+R_S(t)\ \text{使}\ \|R_S\|_2^2\lesssim H/\log T\ ?}$$
   ⟹ **若不能** ⟹ 非共振机制**随之封死** ✗；**若能** ⟹ 才值得**重开 E92** ✓
```

## 7. 今日教训（✓ 三条，入 HOT-STATE §八 ✓）

```
① **对象核对** ✓：$S$ vs $S_1$ —— **$\log^2n$ 是 $S_1$ 签名** ✓；凡引用定理必先钉对象 ✓
② **微分放大** ✗：**$L^2$ 界不可微** ✓ —— $O(H/L^2)$ 的 $S_1$ 余项**不蕴含**同阶的 $S$ 余项 ✗
③ **阈值归一化** ✗：今日对同类阈值**三次口径更正** ✓（$C$：0.05 → 0.33 → 19.785 ✓）⟹ 公式须先写清再代入 ✓
```

## 8. 纪律（✓）

```
✓ **未用 RH** ✓；**未跑 Lean** ✓
✓ **E93 状态已改正** ✓（原 doc 加封档横幅 ✗）；**未宣布 E93 成立** ✗；**未宣布 T1 已证** ✗
```
