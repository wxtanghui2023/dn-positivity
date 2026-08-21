# arXiv 投稿包

> 目标：arXiv math.NT 提交（需要背书人）
> 状态：材料已就绪，等待唐先生注册 arXiv 账号 + 联系背书人
> 日期：2026-08-21

---

## 文件清单

| 文件 | 用途 |
|---|---|
| `paper-arxiv.tex` | 主 LaTeX 源（pandoc 生成，article 类 + amsmath）|
| `paper.pdf` | 编译好的 PDF（提交预览用）|
| `paper-dn-positivity-EN.md` | 源 Markdown（修改用）|

## 提交信息（准备填表用）

- **标题**：On the Positivity of D_n = Σ_γ g_n(γ) for a Telescoping Test Function of the Riemann Zeta Zeros
- **作者**：Hui Tang（Independent Researcher）
- **分类**：math.NT（Number Theory）
- **摘要**：见 paper-arxiv.tex 或 EN.md 的 Abstract 段
- **关键词**：Riemann zeta zeros; explicit formula; positivity; telescoping identity
- **DOI**：10.5281/zenodo.22040623（已致谢）

## arXiv 提交步骤

1. **注册账号**：arxiv.org → Register（需机构邮箱或 .edu 邮箱；独立研究者需联系管理员或用已有邮箱验证）
2. **确认背书人**：arxiv.org → "Search endorsement" → 输入 math.NT 分类
   - 或在 arXiv 搜索 `au:Murty` `au:Rath` 的 analytic number theory 论文
   - 打开论文 → 页面底部 "Which authors of this paper are endorsers?"
3. **发背书请求邮件**（模板见 `ENDORSEMENT-EMAIL.md`）
4. **获得背书后**：Submit → 上传 `paper-arxiv.tex`（+ 如有图片一并上传）
5. **审核**：arXiv 自动编译，通过后分配 arXiv ID（如 math.NT/2608.XXXXX）

## 注意事项

- arXiv 不接收 PDF-only 提交（需要 LaTeX 源）——`paper-arxiv.tex` 已准备好
- 首次提交会有管理员审核（通常 1-2 天）
- 提交后如需修改：v2 版本，DOI 不变
- **Zenodo 与 arXiv 关联**：投稿后可在 Zenodo 记录页添加 arXiv 链接（Related identifiers）

## 时间线预期

- 背书请求发出 → 1-4 周回复
- 提交 → 1-2 天审核 → 上线
- 若背书人沉默 → Plan B（Zenodo+GitHub 已可引用）或 Plan C（期刊接受后自动获背书）
