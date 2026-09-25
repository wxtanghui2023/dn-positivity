已查地图：命中（`X1-AMEND-20-21-22-verdict-CLOSED.md` 记录 B1-a 状态；`SPACE-B-INTAKE-v1.md` 种子 S1；`RESEARCH-CONSTITUTION` AMEND-27/28）
D0: 本档对象 = **B1-b 结构枚举引擎**（以 `C₁₂₀` 为中心、owner-set 驱动）＋ **`|D| ≤ 4` 邻域的完整判定**
D1: 0（有限精确搜索＋结构剪枝型；**未**提出新机制）
[REVIEW]

# **B1-b：owner-set 结构引擎（第一阶段，不跑 CP-SAT）**

## §1 设计（照唐先生 14:2x 的一刀）

```
$$C'=(C_{120}\setminus D)\cup A;\qquad \text{关键}:\ \boxed{U(D)=\{v:\ S(v)\neq\varnothing\ \land\ S(v)\subseteq D\}}$$
$$\text{即：只有"全部 owner 都被删除"的点才需要新字覆盖};\quad \text{其余点仍由 }C_{120}\setminus D\ \text{覆盖} ✓$$
$$\textbf{算术更正（须声明）}:\ \text{要得 }119\ \text{码须 }|A|=|D|-1\ \boxed{\text{而非 }|D|+1}\ (\text{因 }120-|D|+|A|=119);\ \text{本引擎求\textbf{最小} }|A|\ \text{再与 }d-1\ \text{比较，两种读法都不丢} ✓$$
$$\textbf{必要条件（剪枝核心）}:\ |U(D)|\le 11\,|A|\le 11(d-1);\qquad \text{另加 packing 下界（两两距离}\ge3\ \text{的点需不同球）}$$
$$\textbf{覆盖搜索}:\ \text{对 }v\in U(D)\ \text{的候选新字}=\{v\}\cup\{v\oplus e_i\}\ (\text{11 个});\ \text{且它们\textbf{必不在} }C_{120}\setminus D\ \text{中（否则 }v\ \text{仍被覆盖}）\Longrightarrow\ \text{分支}\le 11$$
```

## §2 `C₁₂₀` 的 owner 结构（实测）

```
$$\text{mult. 分布}:\ m{=}1:\mathbf{801}\ \text{点}\mid m{=}2:172\mid m{=}3:36\mid m{=}4:8\mid m{=}5:7;\quad \max m=5,\quad \textstyle\sum m=1320=120\times11\ ✓$$
$$\text{每字私有点 }|P_1(c)|:\ \min=2,\ \text{中位}=6,\ \max=11;\quad \text{私有点}=0\ \text{的字}:\ \mathbf{0}/120$$
$$\Longrightarrow\ \boxed{\text{删任意一字必产生 }\ge2\ \text{个未覆点}}\ (\text{与"delete-1 至少需 2 次修补"一致} ✓)$$
$$\text{层数（不同 owner 集）}=330;\quad \text{最大 owner 基数}=5$$
```

## §3 结果（`d=|D|`，完整枚举）

| d | 枚举量 | 尺寸剪枝 | packing 剪枝 | 存活精确搜 | **发现 119** | 用时 |
|---|---|---|---|---|---|---|
| 1 | 120 | 120 | 0 | 0 | **0** | 0.0 s |
| 2 | 7,140 | 5,761 | 1,377 | 2 | **0** | 0.2 s |
| 3 | 280,840 | 61,400 | 218,980 | 460 | **0** | 9.5 s |
| 4 | **8,214,570** | 278,771 | 7,904,062 | 31,737 | **0** | **674.3 s** |

```
$$\Longrightarrow\ \boxed{\text{在 }|D|\le4\ \text{的"删除—补入"邻域内\textbf{不存在 }119\text{-码}}}$$
$$\textbf{新意（相对 B1-a/旧扫）}:\ d=3\ \text{为\textbf{首次完整}枚举}（\text{旧仅局部 }(3,2)\ \text{扫}）;\ d=4\ \text{同为此前\textbf{未做}的完整判定} ✓$$
$$\text{与旧结果一致}:\ \text{delete-1 无解} ✓;\ \text{delete-2-add-1 无解} ✓\ (\text{旧 7140 对 }\times 904\ \text{候选扫})$$
$$\text{引擎产物}:\ \texttt{work/k10/b1b\_layers.py}\ (\text{分层提取})\mid\texttt{b1b\_engine.py}\ (\text{结构枚举＋精确覆盖＋剪枝})\mid\texttt{b1b\_result\_*.json}$$
```

## §4 进行中 / 待做

```
$$\text{进行中}:\ \boxed{d=5}\ (\binom{120}{5}=190{,}578{,}024\ \text{组};\ \text{4 分片并行，按 }i_1\ \text{切})\ \text{目标 }|A|\le4$$
$$\text{待做}:\ d=6\ (\binom{120}{6}=5.4\times10^{8};\ \text{需更强剪枝或更多分片})$$
\textbf{判据（不跑 CP-SAT）}:\ \text{一旦发现 }|A|\le d-1\Longrightarrow\ \text{进独立 1024 点 verifier};\ \text{全部失败}\Longrightarrow\ \text{得\textbf{局部结构结论}（非 UNKNOWN）} ✓
```

## §5 边界（诚实）

```
(i)\ \text{这是\textbf{邻域}搜索}:\ \text{只覆盖"从 }C_{120}\ \text{删除 }\le d\ \text{字"可达的 119-码};\ \boxed{\text{不覆盖与 }C_{120}\ \text{相距更远的 119-码}} \Longrightarrow \textbf{不构成全局不存在性}
(ii)\ \text{判定依赖 }C_{120}\ \text{本身正确}（\text{Kamenetsky 码，已复核 1024/1024 覆盖} ✓）
(iii)\ \text{剪枝为\textbf{必要}条件};\ \text{存活者仍走\textbf{精确}最小覆盖搜索（非启发）} ✓
(iv)\ \text{引擎已做 }Yes\ \text{侧自检}:\ \text{对 }d=1,2\ \text{重现已知结论} ✓;\ \text{覆盖搜索候选必不在剩余码中的论证与实现一致} ✓
```

## §附 【技术词回查】（**先跑后写**，逐字粘贴）

```
$ bash scripts/tech_word_check.sh "owner set" "multiplicity" "U(D)" "删除—补入"
技术词 owner set        命中文件数=0    ::
技术词 multiplicity     命中文件数=37   :: ./grh-goldbach-paper-draft-v2.md ./E20-E40-zero-density-2026-read.md ./p49-phase-diagram-summary.md
技术词 U(D)             命中文件数=146  :: ./C112-W4-1d-three-gate-audit-C2-first-zero-cost-kill.md ./kloosterman_fractions.pdf ./C331-M5-gap-localization-complete-wait-for-new-mathematical-input.md
技术词 删除—补入  命中文件数=0    ::
```
**三分类**：
- **本档新增（回查前 0 档）**：`owner set`、`删除—补入` ⟹ 本档首次引入
- **档案已有（引用，不列为提出）**：`multiplicity`（37 档，但均为**异语境**：零点密度／Hadamard 等）⟹ 列为**通用词**
- **⚠️ 正则伪命中（须声明）**：`U(D)` 的 146 档系 `grep -E` 将 `(D)` 解释为**正则捕获组**、实际匹配字符串 `UD` ⟹ **非本档术语命中，不计**
- **⚠️ 新性边界**：本档**无**新性主张；交付物 = **有限邻域内的完整判定（K1 型）**，**不声称**全局不存在性
