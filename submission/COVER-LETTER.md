# 期刊投稿 Cover Letter（模板）

> 推荐期刊：Experimental Mathematics（Taylor & Francis）
> 状态：模板已就绪，唐先生填写后通过期刊投稿系统提交
> 日期：2026-08-21

---

## 英文 Cover Letter

```
[Date]

Dear Editor,

We are pleased to submit our manuscript "On the Positivity of
D_n = Σ_γ g_n(γ) for a Telescoping Test Function of the Riemann
Zeta Zeros" for consideration in Experimental Mathematics.

We study the quantity

    D_n = Σ_γ g_n(γ),   g_n(t) = [t·sin(nθ(t)) + ½cos(nθ(t))]/(¼+t²)

where γ runs over the positive imaginary parts of the non-trivial
zeros of ζ(s) and θ(t) = π - 2arctan(2t). Our main result is the
positivity D_n > 0 for all n ≥ 1.

The paper combines three elements typical of Experimental Mathematics:

1. A new telescoping identity g_n = cos(nθ) - cos((n+1)θ), verified
   analytically and numerically to <10^-10.

2. A hybrid proof: strict positivity for n ≤ 43 by positive-term
   summation, and an asymptotic bound D_n ≥ 0.1934·log n - O(1) for
   large n via a phase-region split (positive main term + alternating
   series with Leibniz bound).

3. Extensive numerical verification to n ≤ 10^4 using the first
   10^5 zeros of Odlyzko (cross-validated against mpmath).

The work connects to explicit formulas (Murty–Rath 2018) and Li's
criterion. All code, data, and the complete proof documentation are
openly available (DOI: 10.5281/zenodo.22040623).

We believe this fits the scope of Experimental Mathematics well:
a clean numerical discovery, a partially rigorous framework, and an
honest statement of the remaining open problem (a research-level
bound on an S-function error term).

Thank you for your consideration.

Sincerely,
Hui Tang (Independent Researcher)
Ning Tang (Harbin Institute of Technology, Shenzhen)
[Emails]
```

---

## 投稿前检查清单

- [ ] 摘要标注开放问题（ε_m 的 O(1) 界）— ✅ 已在论文 Section 6.2
- [ ] 引言提及 Murty-Rath 2018 — ✅ 已在论文 Section 6.1
- [ ] 致谢 Zenodo DOI 和 GitHub — ✅ 已在论文头部
- [ ] Cover letter 填写作者邮箱
- [ ] 投稿系统上传：manuscript（PDF）+ cover letter
- [ ] 可选：补充材料（代码/数据链接）

## Experimental Mathematics 投稿信息

- 出版社：Taylor & Francis
- 投稿系统：ScholarOne（https://mc.manuscriptcentral.com/uexm）
- 格式：LaTeX 优先（可用我们的 .tex 或 .md → PDF）
- 审稿周期：通常 2-4 个月
- 开放数据：该刊鼓励，我们的 GitHub+Zenodo 是加分项

## 备选期刊（若被拒）

| 期刊 | 特点 |
|---|---|
| Integers | 开放获取，快速 |
| Involve | 中等难度 |
| Journal of Number Theory | 更严格，需完全严格证明 |
| Ramanujan Journal | 解析数论方向 |
