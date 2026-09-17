已查地图：命中 `C-27`｜`EXTERNAL-TESTABILITY-AUDIT`｜`V316`｜CLOSED-ROUTES-MAP:721/731 → 本档＝**勘误＋Lean 家底＋两轴更正**

# 🔧 勘误：我此前把"**我方自推**"错读成"**外部不可复核**" —— 这是错的；附 Lean 家底

> 起因：唐先生 2026-09-17 18:02：「**我们有推导，有 lean，有 mathlib，为啥不能外部独立复核？**」✓✓
> **答**：确实可以复核。**我此前的分级表把两件不同的事混成一件**，本档更正。

---

## §1 我错在哪（一句话）
$$\text{我用了一根轴}\ [\textbf{L}]\text{文献}\big/[\textbf{O}]\text{自推}\big/[\textbf{M}]\text{元语言}，\ \text{却把}\ [\textbf{O}]\ \textbf{擅自读成} \text{"外部无法独立复核"}✗$$
$$\qquad \text{而}\ [\textbf{O}]\ \text{的本来含义只是}\ \textbf{"不是文献里已有的"（归属）}，\ \textbf{与"能不能被核验"无关}✗✗$$
$$\Longrightarrow \boxed{\text{正确做法＝}\textbf{两轴分立}}：\underbrace{\textbf{K：可核性}}_{\text{能不能验}}\quad\times\quad\underbrace{\textbf{P：归属}}_{\text{是不是新}}✓✓$$

## §2 更正后的 **K 轴（可核性）** 定义
$$\textbf{K1}\ \textbf{Lean 内核检查}（\text{最强}：\ \textbf{无需信任作者}，\text{一条命令可复现}）✓✓$$
$$\textbf{K2}\ \textbf{标准数学陈述}（\text{专家可逐步核}；\text{障碍是}\ \textbf{长度＋标记}，\ \textbf{不是不可核}）✓$$
$$\textbf{K3}\ \textbf{数值／计算}（\text{需公布脚本＋数据即} \textbf{可复算}）✓$$
$$\textbf{K0}\ \textbf{尚未成为命题}（\text{自造元语言；}\ \textbf{须先翻译} \text{成精确陈述 —— 这是}\ \textbf{唯一} \text{真正不可核的一类，且可修}）⚠️$$

## §3 **Lean 家底（本次实测，非自述）**
$$\text{环境}：\texttt{leanprover/lean4:v4.33.0}\ ✓\quad\text{Mathlib 预构建}\ \textbf{8702 个 .olean}\ ✓$$
$$\text{工程}：\texttt{\textasciitilde/lean-repro/zeta23-local/}\（\text{lakefile.toml}\ ✓）$$

| 文件 | 行数 | sorry | axiom | **编译** |
|:--|--:|--:|--:|:--|
| **`V316_kernel_bound.lean`**（**我方主产出**）| **1262** | **0** | **0** | ✅ **退出码 0，error=0**（2026-09-17 18:09 实测）|
| `Solution.lean` | 142 | 0 | 0 | （来源待核：工程内既有）|
| `ChallengeDeps.lean` | 109 | 0 | 0 | （同上）|
| `Challenge.lean` | 231 | 19 | 0 | 题目陈述（含 sorries，正常）|

$$\textbf{信任漏洞逐类扫描（V316）：}\ \text{sorry}=0\ \big|\ \text{sorryAx}=0\ \big|\ \text{axiom}=0\ \big|\ \text{admit}=0\ \big|\ \text{native\_decide}=0\ \big|\ \text{unsafe}=0\ \big|\ \text{implemented\_by}=0\ \big|\ \text{partial def}=0✓✓✓$$
$$\qquad \text{唯一警告}：\ \text{第 1220 行变量名}\ \texttt{s}\ \text{未引用（}\textbf{无害}）✓$$
$$\qquad \textbf{声明数}：56\quad\big|\quad \text{主定理链含}\ \texttt{Qfun\_global\_gap}\ (\lambda\le1),\ \texttt{integral\_sq\_eq\_zero\_of\_min},\ \texttt{minimizer\_uniqueness\_ae}✓✓$$
$$\textbf{复现命令}：\texttt{cd \textasciitilde/lean-repro/zeta23-local \&\& lake env lean V316\_kernel\_bound.lean}⟹ \text{退出码}\ 0✓✓$$

$$\Longrightarrow \boxed{\text{即：}\textbf{"}\lambda\le1\Rightarrow G\le0.6725\text{" 那一项，}\ \text{外部}\ \textbf{不需要读我方任何档、也不需要信任我方} \text{，}\ \text{跑一条命令即可核验}}✓✓✓$$

## §4 **更正后的 22 项两轴表**（替换 tracker §1d 的旧单轴版）
| # | 项 | **K 可核性** | P 归属 | 复核方式（具体）|
|:--:|:--|:--:|:--|:--|
| 1 | W1 | K2 | [L] Lamzouri | 读 arXiv:2609.02882（文献）|
| 2 | W2 | K2 | [O] | 读 V181/B1–B5 陈述 |
| 3 | W3 | K2 | [O] | 读 E1–E4 映射 |
| 4 | W4 | K2 | [O] | 逐步核 V172 A-leak 扩张 |
| 5 | W5 | K2 | [L]+[O] | Weil 正性经典部分可查 |
| 6 | W6 | K2 | [L] | 读 arXiv:2608.13637 Remark 1.1 |
| 7 | W7 | K2 | [O] | 读 ⑫关 判定 |
| 8 | W8 | K2 | [O] | 读 FPCA 更正 |
| 9 | W9 | K2 | [L] | AKS 文献 |
| 10 | W10 | K2 | [O] | 读四线审计 |
| 11 | W11 | K2 | [L]+[O] | 非自伴谱经典 + 五族审计 |
| 12 | **W12** | ⭐**K1**＋K2 | [O]＋[L] | **`lake env lean V316_kernel_bound.lean`** ✓✓ |
| 13 | D1 | K2 | [O] | 读 CONV2/3 |
| 14 | D2 | K3 | [O] | 数值脚本 |
| 15 | D3 | K2＋K3 | [L]＋[O] | Karatsuba 文献 + E92/E93 脚本 |
| 16 | D4 | K2 | [O] | 读 E123 |
| 17 | D5 | K2 | [O] | 读 P27–P33 |
| 18 | D6 | K2 | [O] | 读 V113/V114 |
| 19 | D7 | ⚠️**K0** | [M] | **须先翻译**（"三关"→精确陈述）|
| 20–21 | D8/D9 | ⚠️**K0** | [M] | 同上（纪律项，非命题）|
| 22 | D10 | K2 | [O] | 读 AOB2 |

$$\boxed{\textbf{更正后的汇总}：K1\ \ge1\（\text{V316 Lean}\）；K2\ \textbf{绝大多数}；K3\ \text{数项}；\textbf{K0 仅 D7/D8/D9 三项元语言}}✓✓$$
$$\qquad ⟹ \textbf{撤回} \text{我此前"外部独立可判}\approx5\ \text{项，其余＝框架内自洽"的结论}✗✗\ —\ \textbf{那是错的}✓$$

## §5 真实障碍（更正后的诚实版）
$$\text{(i)}\ \textbf{不是"不可核"}，\ \text{而是}\ \textbf{阅读成本}：\ \text{编号史／叙事壳／长度}\ \Longrightarrow \ \text{外部读者被拖进"学我方语言"}✓$$
$$\text{(ii)}\ \textbf{K0 三项}（\text{D7/D8/D9 的元语言}）\ \text{确实须先翻译成精确陈述}✓$$
$$\text{(iii)}\ \text{论文级结果}\ \text{若要有外部评审，}\ \textbf{标准做法}＝\text{写成}\ \textbf{标准格式预印本}(\text{含定理／证明／引理编号})＋\ \textbf{附 Lean 工程}⟹ \text{这正是本项目}\ \textbf{还没做} \text{的一步}✓✓$$

## §6 边界
$$\text{(i)}\ §3\ \text{为}\ \textbf{本次实测}（\text{编译时间}\ 18:04\text{--}18:09；\text{命令与退出码均在档}）✓✓；\ \text{"Solution.lean 来源待核"}\ \text{为诚实标注}✓$$
$$\text{(ii)}\ \textbf{未用 RH}；\ §4\ \text{为新分级，}\textbf{替换} \text{旧单轴版}✓✓$$
