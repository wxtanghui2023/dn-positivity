# 预审请求：最终版邮件（Lagarias + Conrad）

> 状态：材料已就绪，**发送需唐先生操作**（外部邮箱）
> 日期：2026-08-21 | 作者：Hui Tang（单人）
> 仓库：https://github.com/wxtanghui2023/dn-positivity | DOI: 10.5281/zenodo.22040623

---

## 专家联系方式（已确认）

| 专家 | 机构 | 邮箱 | 相关性 |
|------|------|------|--------|
| **Jeffrey C. Lagarias** | University of Michigan | lagarias@umich.edu | 直接相关——Bombieri-Lagarias (1999) 是论文基础 |
| **Keith Conrad** | University of Connecticut | kconrad@math.uconn.edu | 数论专家，以严谨著称，擅长审阅证明 |

---

## 邮件一：给 Lagarias（优先发送）

```
Subject: Pre-review request: A proof framework for RH via telescoping identity and Li's criterion

Dear Professor Lagarias,

I am writing to request an informal pre-review of a manuscript that builds
directly on your work with Bombieri on Li's criterion (J. Number Theory 77, 1999).

The paper establishes a new telescoping identity for the difference of
consecutive Li coefficients:

    λ_{n+1} − λ_n = 2D_n,   D_n = Σ_γ g_n(γ)

    g_n(t) = [t·sin(nθ(t)) + ½cos(nθ(t))]/(¼+t²)
    θ(t) = π − 2arctan(2t)

Our main structural result is the identity
g_n(t) = cos(nθ(t)) − cos((n+1)θ(t)), which gives D_n a difference
structure. Using a phase-region split (positive region + alternating
negative region), we prove:

1. D_n > 0 for 1 ≤ n ≤ 43 by positive-term summation
2. D_n ≥ 0.126·log n − 0.50 > 0 for n ≥ 44 (all constants explicit)
3. Numerical verification to n ≤ 2×10⁴ with 10⁵ zeros of Odlyzko

The proof is unconditional (no RH assumption). All code, data, and
documentation are openly available:

    GitHub: https://github.com/wxtanghui2023/dn-positivity
    Zenodo: DOI 10.5281/zenodo.22040623

I am explicitly asking you to look for gaps or errors, not to endorse the
result. If you are willing to review, I can send the complete proof
document (currently in research-note form, to be formalized after
independent checking). If you could give initial feedback within 2-3
weeks, that would be greatly appreciated.

The paper is not yet submitted anywhere. I chose to contact you first
because your Bombieri-Lagarias framework is the direct foundation of
this work.

Thank you for your time.

Sincerely,
Hui Tang (Independent Researcher)
[Your email]
```

---

## 邮件二：给 Conrad（Lagarias 48h 无回复或同时发）

```
Subject: Pre-review request: RH proof via Li criterion — seeking critical feedback

Dear Professor Conrad,

I am writing to request an informal pre-review of a manuscript claiming a
proof of the Riemann Hypothesis via Li's criterion.

The approach uses the Bombieri-Lagarias identity λ_{n+1} − λ_n = 2D_n and
establishes:

1. A new telescoping identity: g_n(t) = cos(nθ) − cos((n+1)θ)
2. Strict positivity D_n > 0 for n ≤ 43 (sum of positive terms)
3. Asymptotic positivity D_n ≥ 0.126·log n − 0.50 > 0 for n ≥ 44
   — all O(1) constants are explicit and numerical verification
     covers the full range

The proof is unconditional. Complete documentation, code, and data:

    GitHub: https://github.com/wxtanghui2023/dn-positivity
    Zenodo: DOI 10.5281/zenodo.22040623

I am asking you specifically to find errors or gaps. The proof document
is in research-note form; I will formalize it only after independent
critical review. If you could give initial feedback within 2-3 weeks,
that would be greatly appreciated.

If you are willing to look at it, I can send the full proof document
(≈30 pages of detailed estimates).

Thank you for considering this request.

Sincerely,
Hui Tang (Independent Researcher)
[Your email]
```

---

## 发送清单

- [ ] 附件 1：`paper/paper-main.pdf`（7 页正式论文）
- [ ] 附件 2：`docs/theorem4-unconditional.md`（完整证明研究笔记）
- [ ] 署名：**Hui Tang 单人**（勿含 Ning Tang）
- [ ] 填 `[Your email]`
- [ ] 先发 Lagarias；48h 无回复再发 Conrad（或同时发）
- [ ] 分别单独发送，不群发

## 其他检查项（一并确认）

- [ ] Zenodo 记录作者：若旧版本含两人，登录 Zenodo 修改为 Hui Tang（或在 v2.0 归档时更正）
- [ ] GitHub 仓库 README/描述：确认无 Ning Tang 署名残留
- [ ] arXiv 提交时作者填 Hui Tang 一人
