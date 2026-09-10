# C2-a Closure Certificate ｜ 运输曲率支线关闭证书

**日期**：2026-09-10 ｜ **拍板**：唐先生 ｜ **状态**：正式关闭

---

## 证书（按唐先生措辞定稿）

> **C2-a Closure Certificate**
>
> 对实际构造的 radical/product transport curvature，四状态差分后的每个 $\omega_p$
> 均可**精确归约**为有限个 $p\mid\ell(a,b)$ 指示函数的线性组合；因此其状态依赖
> 完全由 $(a,b)\bmod p$ 决定，$K_p=1$。
>
> 所以该曲率**没有 $p$-adic 跨尺度记忆**；任何 $D_p>1$ 的原始算术深度均在
> 四状态曲率投影中被消掉。
>
> **结论：该 radical/product transport-curvature 分支关闭。**

## 逻辑链（封存版）

$$\boxed{\text{四状态差分}\;\Longrightarrow\;\text{有限个线性整除指标}\;\Longrightarrow\;\omega_p=f_p(a\bmod p,b\bmod p)\;\Longrightarrow\;K_p=1}$$

**不是**（已作废）：

$$\text{"radical 型"}\Longrightarrow K_p=1$$

## 边界（必须随证书引用）

$$\boxed{\text{非线性 }v_p\text{ 状态尚未被此证书覆盖}}$$

且：**它不能作为本分支的"救活理由"，而应视为完全不同的模型重置。**

---

## 封存过程留档（本轮完整链条，供日后复核）

```
1. 原命题（两行证明泛化到"任何 radical 型"）—— 作废
2. 反例定位漏洞：c=10, c'=25, p=3 → rad(c)≡1, rad(c')≡2 (mod 3)
      ⟹ rad(n) mod p 不是 n mod p 的函数（命题为假）
3. 缩窄命题：假设 ω_p 可归约为 Σ_j c_j 1_{p|ℓ_j(a,b)}，ℓ_j=u_j a+v_j b
4. 实际曲率验证该假设（有限域 rank 检验，精确有理高斯消元）：
      p=3: rank(C)=5, rank(C ∪ {ω_p})=5      (5 维 ⊂ F_3² 的 9 维)
      p=5: rank(C)=7, rank(C ∪ {ω_p})=7      (7 维 ⊂ F_5² 的 25 维)
      幂型：精确 telescoping ω_p = 3α(1_{p|b+c} − 1_{p|c})
      p=2,3,5 各 22500 样本，反例 0（含混合权 rad(abc)/(abc)）
5. 数值表纠错：
      p=3 正确表（a 外层, b 内层）= [0,0,0,0,2,−2,0,−2,2]
      唐先生先前引用的 [0,1,−1,−1,0,1,1,0,0] 非此口径 ⟹ 已更正，不再引用
      手验：(1,1): 0−1−0+3=+2 ✓   (1,2): 1−1−3+1=−2 ✓
```

## 索引

- 复核版定理：`docs/theorem-depth1-review-version.md`
- 原版（作废，留档）：`docs/theorem-depth1-transport.md` §3
- 脚本：`scripts/verify_span_minimal.py`、`scripts/verify_telescoping.py`、`scripts/C2a_depth.py`
- 登记册：`docs/NOGO-registry-and-screens.md`

**不再在本分支上迭代。**
