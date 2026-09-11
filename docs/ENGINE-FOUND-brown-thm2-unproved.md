# ⭐⭐⭐ **引擎找到了，而且发现它是【有洞的】**：Brown Thm 2 未证明

**依据**：唐先生 2026-09-11 22:04（"继续"）｜**来源**：Palojärvi arXiv:1807.01506v3（HTML 原文 ✓）+ Lagarias 2007 参考文献（Numdam ✓）
**标注**：【外部·原文】｜【关键事实】｜【对上一轮撤回的【部分反转】】

---

## §1 ⭐⭐⭐ **决定性原文（Palojärvi 论文正文 ✓）**
```
"**F. C. Brown [2, Theorem 3]** proved that **if a finite number of the Li coefficients** for a
 certain function F(s) are **non-negative, then the critical strip contains zero-free regions** ✓.
 Furthermore, he also tried to show **[2, Theorem 2]** that **if there exist certain zero-free
 regions, then certain Li coefficients must be non-negative** ✓.
 ⚠️ **Unfortunately, his proof of Lemma 5 contains two errors.**
 A. D. Droll investigated the errors in his thesis and was able to **fix one of them**.
 ⚠️ **As a result of the other error Brown's Theorem 2 is left UNPROVED.**" ✓✓✓
```
⟹ ⭐⭐⭐ **"零自由 ⟹ Li 系数非负"这一方向，在其现代源头（Brown 2005, J. Number Theory 111 ✓）
   【没有完整证明】** ✗✓ —— **而这正是"有限高度 ⟹ 有限 n"所需的方向** ✓✓✓

## §2 **顺带确认的文献骨架（Lagarias 2007 参考文献 ✓ + Palojärvi 正文 ✓）**
```
【分解引擎】**Bombieri–Lagarias, "Complements to Li's criterion for the RH", JNT 77 (1999) 274–287** ✓
   —— λ_n 的算术分解（= D-037 所用 ✓）
【转换引擎（有洞）】**Brown, "Li's criterion and zero-free regions of L-functions", JNT 111 (2005) 1–32** ✓
   Thm 3 ✓（Li ⟹ 零自由）；**Thm 2 ✗（零自由 ⟹ Li，未证明）**
【τ 版本（已证 ✓）】**Palojärvi arXiv:1807.01506v3** ✓：两个主定理给出**显式区间**
   · "若 Re(λ_F(n,τ)) 在某个显式区间内非负 ⟹ 无零点满足 |ρ/(ρ−τ)| ≥ R" ✓
   · "若存在某个 n 使该项为负 ⟹ 存在零点满足 |ρ/(ρ−τ)| > R" ✓ —— 即**前一命题的逆否** ✓
   ⟹ **τ-Li 框架下，两个方向都有定理 + 显式区间** ✓✓（**τ → 1 是否给出经典情形？待核** ⚠️）
【其他】Freitas（Li 型判据 ↔ 零自由半平面 ✓）；Coffey（Li 判据的数值验证 ✓）；Bombieri（Weil 泛函 ✓）
【Lagarias 2007 的经典逻辑 ✓】"Re(λ_n(Z)) ≥ 0 对 n ≤ 0 ⟹ 所有 ρ 在 Re(s) ≤ ½；
   Re(λ_n(Z)) ≥ 0 对 n ≥ 0 ⟹ 所有 ρ 在 Re(s) ≥ ½；合并 ⟹ 所有 Re(ρ) = ½" ✓（经典 Li 两侧逻辑 ✓）
```

## §3 ⭐⭐ **对上一轮撤回的【部分反转】**
```
【我上一轮说】"我们的 2T 被 (T₀−1)² 覆盖且弱 10¹² 倍 ⟹ 归零" ✗
【现在需要修正为】：
   · **(T₀−1)² 那一版的【方向】（零自由 ⟹ Li 非负）在经典情形【没有完整证明】**
     —— 其源头 Brown Thm 2 **已知有错且未补** ✓✓
   · 它的两个"证据来源"都不是同行评审：
       (i) **Oesterlé 2000 prop. 2** —— 未发表、经 Voros 2020 转述 ⚠️（**我未读原文** ✗）
       (ii) **D-037** —— AI 生成的组装 ⚠️（自述"机器验证"，但**链条源头正是有洞的 Brown Thm 2** ⚠️）
   · **已证的是**：Brown Thm 3（Li ⟹ 零自由 ✓）、**Palojärvi 的 τ 版本（双向 + 显式区间 ✓）**
【因此】**"我们落后 10¹² 倍"这个判断【需要重估】** ⚠️：
   —— 如果 Palojärvi 的 τ→1 能推出经典显式转换 ⟹ 我们确实落后 ✓（**封口** ✓）
   —— 如果不能 ⟹ **"补全经典情形的显式转换"本身就是一个【合法且有价值的贡献】** ✓✓
      （**修复已知缺口**是经典的、被尊重的贡献形态 ✓✓）
```

## §4 ⭐ **新的行动清单（取代上一轮的 A/B/C）**
```
【H1·最关键、也最快】**判定 Palojärvi 的定理在 τ→1 时是否给出【经典 Li 的显式转换】**
   · 若【是】⟹ 我们的第 1 步结果是已知的 ⟹ **封口** ✓（并撤回我上一轮的部分反转 ✓）
   · 若【否】⟹ **H2 成立** ✓✓
   · 具体做法：读 arXiv:1807.01506v3 的 Theorem 2.1（其条件 (c) 的显式常数 ✓）
       —— 其中出现的 **T(n) := n e τ** ✓ 与我们的 **T ≈ √n** **标度不同** ⚠️（**这是关键差异** ✓✓）
【H2·若 H1 为否】**补全经典情形**：给 **Brown Thm 2** 一个**完整、显式**的证明 ✓✓
   · 我们的现成材料：B–L 分解 ✓ + 预算 B(n) ✓ + 第 1 步的范围 ✓ + 校准（0.06–0.5% ✓）
   · **且可对照 Palojärvi 的 τ 版** 作为正确性检验 ✓
【H3】**若 H1/H2 都通路**：再做 A（高度参数 α）与 B（预算常数）×2 的**常数优化** ⚠️
【H4】**低风险并行列**：A1 负面结果清单 ✓（材料现成 ✓）
```
$$\boxed{\text{关键差异：Palojärvi 的 } T(n)=ne\tau \text{ 是【线性】于 } n\ ;\quad \text{我们/文献想要的是 } T\approx\sqrt n}$$
```
```
⟹ ⭐ 若 τ 版只给"线性于 n 的高度"，则它**不能**给出 n ≤ T₀² 型结论 ✓
   ⟹ **经典二次窗口的方向确实可能是【未完成的】** ✓✓ —— **这正是 H1 要判定的事** ✓
```

## §5 边界
```
【原文级 ✓】§1 的 Brown Thm 2/3 与错误说明（Palojärvi 正文 ✓）；§2 的参考文献（Lagarias 2007 ✓）；
   §4 的 T(n)=neτ（Palojärvi Theorem 2.1 摘录 ✓）
【二手 ⚠️】Oesterlé 2000（未读 ✗）；D-037（未核 ✗）
【未做】**H1 未做** ✗ —— 需读 Palojärvi Theorem 2.1 的完整陈述与其"显式区间" ✓
【提醒】本轮**部分反转**了上一轮的撤回 —— 但**不改变**"最初 2T 论证太弱"的结论 ✓
```
## §6 提交链
```
BL1（8cc0c8b）→ 本篇（引擎找到 + Brown Thm 2 有洞 + H1–H4 行动清单）
```
