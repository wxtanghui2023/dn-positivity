# 期刊投稿 Cover Letter（模板）

> 推荐期刊：Experimental Mathematics（Taylor & Francis）
> 定位：**黎曼猜想的望远镜正性判据**（D_n > 0 ⟺ RH，Li 判据）
> 状态：模板已就绪，唐先生填写后通过期刊投稿系统提交
> 日期：2026-08-21（更新至 RH 定位版）

---

## 英文 Cover Letter

```
[Date]

Dear Editor,

We are pleased to submit our manuscript "A Telescoping Positivity
Criterion for the Riemann Hypothesis: D_n > 0 and the Li Coefficients"
for consideration in Experimental Mathematics.

**Main contribution.** We prove a new telescoping identity for the
non-trivial zeros of the Riemann zeta function:

    g_n(t) = cos(nθ(t)) - cos((n+1)θ(t)),
    θ(t) = π - 2arctan(2t),

which yields the exact difference relation for the Li coefficients

    λ_{n+1} - λ_n = 2D_n,    D_n = Σ_γ g_n(γ).

Consequently, by Li's criterion (1997), **D_n > 0 for all n is
equivalent to the Riemann Hypothesis**. The paper establishes:

1. The telescoping identity (Theorem 1), verified analytically and
   numerically to <10^-10;
2. A vanishing-integral reduction (Theorem 2): D_n is a pure zero sum;
3. **Strict positivity for n ≤ 43** (Theorem 3) — an unconditional
   partial verification of the RH criterion;
4. An asymptotic framework (Theorem 4): phase-region split with
   closing margin 0.1934·log n > 0, conditional on a single explicit
   S-function bound Σ_m|ε_m| = O(1);
5. Numerical verification to n ≤ 10^4 with the first 10^5 zeros of
   Odlyzko (cross-validated vs mpmath, error ≤ 2.5×10^-9).

**Honest statement of the open point.** The single remaining step is
the S-function bound Σ_m|ε_m| = O(1). It is numerically overwhelming
(≤ 0.74, far below the margin), but its proof requires
Selberg-moment/van der Corput techniques of research depth. Section 6.2
documents our technical analysis: we exclude the M(T)-boundedness route
(∫|g_n''|dt grows linearly) and identify oscillation cancellation as
the correct mechanism.

We believe this fits Experimental Mathematics well: a clean numerical
discovery (telescoping identity), a partially rigorous framework
toward RH, overwhelming numerical evidence, and an honest, precisely
formulated open problem with a technical roadmap.

All code, data, and full proof documentation are openly available
(DOI: 10.5281/zenodo.22044629, GitHub: wxtanghui2023/dn-positivity).

Thank you for your consideration.

Sincerely,
Hui Tang (Independent Researcher)
Hui Tang (Independent Researcher)
[Emails]
```

---

## 投稿前检查清单

- [x] 摘要明确 RH 目标 + 开放问题（ε_m 的 O(1) 界）
- [x] 引言提及 Murty-Rath 2018 + Li 判据等价性
- [x] 致谢 Zenodo DOI 和 GitHub
- [x] Section 6.2 含技术路线图（M(T) 排除 + 振荡抵消）
- [ ] Cover letter 填写作者邮箱
- [ ] 投稿系统上传：manuscript（PDF）+ cover letter
- [ ] 可选：补充材料（代码/数据链接）

## Experimental Mathematics 投稿信息

- 出版社：Taylor & Francis
- 投稿：Submission Portal（期刊主页 → Submit an article）
- 评审：单盲（single anonymized）| 接受率 16%
- 期刊主页：https://www.tandfonline.com/journals/uexm20
- 格式：LaTeX 优先（paper-arxiv.tex 或 PDF）
- 审稿周期：通常 2-4 个月

## 备选期刊（若被拒）

| 期刊 | 特点 |
|---|---|
| Integers | 开放获取，快速 |
| Involve | 中等难度 |
| Ramanujan Journal | 解析数论方向 |
| J. Number Theory | 更严格，需完全严格证明 |
