# arXiv 预印本提交包

> 状态：材料已就绪，提交需唐先生操作（arXiv 需要账号 + 背书）
> 日期：2026-08-21

---

## 文件清单（paper/ 目录）

| 文件 | 用途 |
|---|---|
| `paper-main.tex` | **arXiv 主源文件**（编译通过，7 页）|
| `paper-main.pdf` | 编译预览 |
| `LAGARIAS-REVIEW-REQUEST.md` | 预审材料（可选附件）|

## arXiv 元数据（填表用）

- **标题**: A Telescoping Positivity Criterion for the Riemann Hypothesis: $D_n>0$ for all $n$ implies RH
- **作者**: Hui Tang; Ning Tang
- **分类**: math.NT (Number Theory)
- **摘要**: 论文 Abstract 段（LaTeX 源中含）
- **关键词**: Riemann hypothesis; Li's criterion; zeta zeros; telescoping identity
- **DOI**: 10.5281/zenodo.22040623
- **Comments**: 7 pages; code and data at github.com/wxtanghui2023/dn-positivity

## 提交步骤

1. **账号**：arxiv.org → Register（需机构邮箱或已有账号）
2. **背书**：math.NT 分类需要背书人
   - 若已获 Lagarias 背书 → 直接提交
   - 否则：arXiv 搜索 `au:Bombieri` 或 `au:Lagarias` → "Which authors are endorsers?" → 发请求
3. **提交**：arxiv.org → Start new submission → 上传 `paper-main.tex`（arXiv 自动编译）
4. **审核**：1-2 天 → 上线（获取 arXiv ID，如 math.NT/2608.XXXXX）

## 注意

- arXiv 需要**LaTeX 源**（不是 PDF-only）——`paper-main.tex` 已就绪
- 提交后可将 arXiv ID 关联到 Zenodo 记录（Related identifiers）
- 首次提交可能触发管理员审核（RH 相关声明会格外仔细）

## 预印本 vs 期刊

- 预印本：立即公开（arXiv + Zenodo 已可引用）
- 期刊：预印本先行不损害投稿（T&F 明确允许 non-commercial preprint）
- 目标期刊（若通过预审）：Annals of Mathematics / Inventiones / JAMS
