# GitHub 发布操作手册：dn-positivity 仓库

> 目标：为黎曼猜想相关论文（D_n 正性）建立**独立** GitHub 仓库 + 分配 DOI + 管理权
> 状态：本地仓库已就绪（53 文件，commit 51c48a5），等待凭据执行远程操作
> 日期：2026-08-21

---

## 为什么需要独立仓库

唐先生现有 GitHub 目录用于**金融市场论文**。本工作（D_n 正性 / 黎曼 zeta 零点研究）是独立数学项目，需单独仓库以保持：
- 主题隔离（金融 vs 数论）
- 独立的 DOI 与引用记录
- 独立的管理权/权限设置

---

## 仓库规划

| 项 | 建议值 | 说明 |
|---|---|---|
| 仓库名 | `dn-positivity` | 或 `zeta-zero-positivity` |
| 可见性 | public | 论文发布需公开 |
| 描述 | Positivity of D_n = Σ g_n(γ), telescoping test function, Riemann zeta zeros | |
| 主题 | number-theory, riemann-zeta, riemann-hypothesis, explicit-formula | |
| 默认分支 | main | |
| License | CC-BY-4.0（论文）/ MIT（代码）| 建议 |

---

## 步骤一：GitHub 创建仓库

### 方式 A：唐先生提供凭据，我执行

唐先生提供以下任一：
1. **GitHub Personal Access Token**（classic，勾选 `repo` 权限），或
2. **SSH 部署 key**（我生成公钥，唐先生在 GitHub 添加），或
3. 安装 gh CLI 并 `gh auth login`（设备码方式，唐先生手机确认）

我收到凭据后执行：
```bash
# 创建远程仓库（需要 gh 或 API token）
gh repo create dn-positivity --public --source=. --remote=origin --push
# 或手动
git remote add origin https://github.com/<OWNER>/dn-positivity.git
git push -u origin main
```

### 方式 B：唐先生手动创建

1. GitHub → New repository → 命名 `dn-positivity` → Public → Create
2. 复制仓库 URL（https 或 SSH）
3. 告诉我 URL，我执行：
```bash
git remote add origin <URL>
git push -u origin main
```

---

## 步骤二：分配 DOI（Zenodo 集成）

**推荐：GitHub-Zenodo 集成**（自动分配 DOI）：

1. 登录 zenodo.org（可用 GitHub 账号 OAuth）
2. Zenodo → GitHub → 勾选 `dn-positivity` 仓库 → 开启
3. **创建 GitHub Release**（v1.0.0）时，Zenodo 自动归档并分配 DOI
4. DOI 形如 `10.5281/zenodo.XXXXXXX`，显示在 Release 页面

**触发方式**（我或唐先生执行）：
```bash
git tag v1.0.0
git push origin v1.0.0
```
+ GitHub 网页上创建 Release（附 paper PDF + README 元数据）

**备选**：手动 Zenodo 上传（upload → New upload → 拖入 paper PDF + 代码 zip），立即获得 DOI。

---

## 步骤三：管理权（Collaborators）

| 角色 | 建议 |
|---|---|
| 唐先生 | **Owner**（默认，建仓者）|
| 小灵 | 可选：添加为 collaborator（Write 权限）以便后续维护 |
| 审阅人（如 Murty/Rath 联系后）| 可选：Read 权限（审阅用）|

添加 collaborator：GitHub → Settings → Collaborators → Add people → 输入 GitHub 用户名。

---

## 步骤四：发布后确认

- [ ] 仓库公开可访问
- [ ] DOI 已分配（Release 页面显示 10.5281/zenodo...）
- [ ] README 元数据完整（标题、作者、摘要、关键词）
- [ ] 代码可复现（requirements 或 install 说明）
- [ ] 数据文件（zeros_odlyzko_100k.npy）已包含

---

## 当前本地状态（已就绪）

```
dn-project/ (本地 git 仓库, commit 51c48a5)
├── release/paper-dn-positivity-EN.pdf   # 论文 PDF
├── release/paper-dn-positivity-EN.md    # 英文论文
├── release/paper-dn-positivity-CN.md    # 中文论文
├── release/README.md                    # 发布说明
├── *.md (8 文档)                        # 证明/审计/文献
├── scripts/ (36)                        # 复现代码
├── data/zeros_odlyzko_100k.npy          # 数据
└── .gitignore
```

**等待唐先生：提供凭据（方式 A）或告知手动创建的仓库 URL（方式 B）。**
