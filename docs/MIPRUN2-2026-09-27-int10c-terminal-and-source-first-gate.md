已查地图：已跑 `scripts/prework_map_check.sh source-first 私有覆盖 119-candidate` ⟹ 命中 2 处（`ASSETS-REGISTRY` 的 `A-PROJCUT-1` 状态锁定／`A-MIPRUN-1` 分叉锁定 🔒）—— 本档 = 该分叉 **②** 的执行记录（终态 ＋ source-first 核验 ＋ P2 首轮），**不开新案** ✓。
D0: 本档对象 = `int10c` 终态判定、既有专用搜索的 **source-first 算法核验**、P2 构造攻击首轮
D1: 2（① MIP 终态判定；② 归档内 `code119_candidate.txt` **无效**之纠正；③ 单字移动平台的**闭性**观察）

# MIPRUN-2（2026-09-27 16:36）· int10c 终态 ＋ source-first 门 ＋ P2 首轮

## §0 结论（先给）

```
$$\boxed{\textbf{(TA-1 终态 ✓)}\ \texttt{int10c.py}\ \text{跑满预算}:\ \textbf{Status = Time limit reached};\ \text{Dual bound}=99.0;\ \text{Primal}=137.99999999999915\ (=138);\ \text{Gap}=28.26\%;\ \text{Nodes}=3751;\ \text{Timing}=900.17\text{s}}$$
$$\qquad\Longrightarrow\ \text{无 }\le119\ \text{整数解 ✗};\ \text{且 Dual}=99\ \ll\ 120\ \Longrightarrow\ \textbf{按 (SB-1) 分支 ② ⟹ MIP STOP ✓}$$
$$\qquad\Longrightarrow\ \boxed{\text{但}\ 99\ \text{是\textbf{有限时间} bound ✓，\textbf{不是}"119 不存在"的证明 ✗}}$$
$$
$$
```

```
$$\boxed{\textbf{(TB-1 source-first 核验（4 项，逐字输出 ✓）)}}$$
$$\text{① }\textbf{基线 ✓}:\ \texttt{work/k10/kamenetsky120.txt}\ \text{独立复核（本档自写校验器，pyguard 512MB）}:\ \textbf{120 词}、\text{badlen}=0、\text{dup}=0、\text{覆盖}\ \mathbf{1024/1024}\ ✓$$
$$\text{② }\textbf{归档 119 候选 ✗ 无效}:\ \texttt{work/k10/code119\_candidate.txt}\ =\ \textbf{119 词但只剩 1007/1024 覆盖} \Longrightarrow \textbf{17 点未覆盖} \Longrightarrow \textbf{不是 119-witness ✗}$$
$$\qquad\text{（文件生成于 2026-09-24 22:59，\textbf{此前从未做独立覆盖验证} ⚠️；本档纠正 ✓——故"历史 }n{=}10,R{=}1\ \text{结果"仍\textbf{只能是} 120\ ✓）}$$
$$\text{③ }\textbf{坏循环 ✗}:\ \texttt{tabu\_np.py}\ \text{崩溃}\ \texttt{IndexError: index 92 is out of bounds for axis 0 with size 92} \Longrightarrow \texttt{np120.log}\ \text{中 }k<120\ \text{各行（"redundant removed"后 unc\to 数百）全是坏产物 ✗ 不可用}$$
$$\text{④ }\textbf{历史 CP-SAT ✓}:\ \texttt{cp119.py}\ (\text{$x_c$ bool, }\min\sum x,\ \text{hint}=120\text{-码减最不私有词}),\ 3600\text{s} \Longrightarrow \texttt{status: UNKNOWN};\ \text{档案已锁"不得表述为 119 不存在" ✓}$$
$$
$$
```

```
$$\boxed{\textbf{(TC-1 ⭐结构性观察（本档新增 ✓）)}\ \text{取 120-码并\textbf{删去私有覆盖点最少的词} \Longrightarrow \mathbf{k=119,\ unc=2}\ ✓\（seed table: priv 计数 }2,2,3,3,3,3,\dots\text{）}}$$
$$\qquad\textbf{闭性论证 ✓}:\ \text{删后余下 119 词的私有覆盖数}\ \ge2 \Longrightarrow\ \text{任一单字替换}\ \text{loss}\ge2\ \text{而}\ \text{gain}\le2\ (\text{因 }\mathrm{unc}=2) $$
$$\qquad\Longrightarrow\ \boxed{\text{除非两未覆盖点距离}\le2\ \text{（有公共覆盖词），单字移动\textbf{不可能}降低 unc ⟹ } \mathrm{unc}=2\ \text{是 1-flip 平台 ✓}$$
$$\qquad\textbf{实测印证 ✓}:\ \text{我方搜索 v4（权重 breakout，k=119 固定）40s / 8147 it \textbf{停在 unc=2} ✗；与历史 }\texttt{tabu\_120\_1.log}\ (\text{k=120, best } \mathrm{unc}=92)\ \text{一致：单字邻域走不动 ⟹ 须 \textbf{2-opt/k-opt 或允许上坡的退火} ✓}$$
$$
$$
```

## §1 既有专用搜索清册（**source-first 逐项钉死 ✓**）

| 脚本 | 目标函数 | 接受规则／移动 | repair | 结果（逐字） |
|---|---|---|---|---|
| `cp119.py`（CP-SAT） | $\min\sum_c x_c$ s.t. 覆盖 $\ge1$，$x_c$ bool | 完整求解＋hint（120−最不私有词） | 无 | `status: UNKNOWN wall=3600.1s` ✗ |
| `tabu_np.py` | 固定 $k$，$\min$ unc | tabu＋restart | 「redundant removed」 | **崩溃** IndexError ✗ |
| `ws120`（witness） | 从 120 码丢词 | 贪心 | 无 | `start k=120 unc=0 (dropped 0)` ✗ |
| `kamenetsky120.txt` | — | — | — | **120 词，1024/1024 ✓（基线）** |
| `code119_candidate.txt` | — | — | — | **119 词，17 未覆盖 ✗ 无效** |

## §2 状态（**✓**）

```
$$\boxed{\text{MIP STOP ✓（分支 ② 已执行 ✓）};\ \text{P2 首轮 = }\texttt{work/k10/p2\_119k\_search.py}\ (\text{k=119 固定、权重 breakout、900s 后台、日志 }\texttt{/tmp/p2k119.log}\text{）};\ \textbf{不启动额外 exact 119 计算 ✓};\ \text{未得 witness 前\textbf{不得}表述"119 不可达" ✗}$$
$$
$$
```

## §3 下一步（**提请唐先生拍板 ✓**）

```
$$\text{(甲)}\ \text{2-opt/k-opt P2（针对 }\mathrm{unc}=2\ \text{平台，最对症 ✓）};\quad \text{(乙)}\ \text{退火（允许上坡，温度调度）};\quad \text{(丙)}\ \text{停手并更新总图（写"未闭合" ✓）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出 ✓）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 终态           命中文件数=19   :: ./FINAL-LABEL-20260916-search-space-closed-proof-space-not-closed.md ./rct-four-layer-final.md ./V106-L3-Q3-independent-sqrt-positivity-audit.md
技术词 私有覆盖     命中文件数=4    :: ./P1-2-2026-09-27-controlled-construction-attempt-and-verdict.md ./X1-K10-2-results-rigidity-and-negative-neighbourhoods.md ./PINNING-2026-09-26-step1-step2-audit-and-n6-n8-data.md
技术词 平台期        命中文件数=0    ::
```
- **本档新增**：`int10c` 终态判定、`code119_candidate.txt` 无效之纠正（17 未覆盖）、单字移动平台之**闭性**观察（1-flip 平台 ＋ loss≥2 *vs* gain≤2）
- **档案已有（引用，不列为提出）**：`A-PROJCUT-1`／`A-MIPRUN-1` 分叉条款、Kamenetsky 120 基线、`cp119.py` UNKNOWN 记录、`FRONTIER-2026-09-25` §1 前沿快照
- **通用词（不计）**：终态、私有覆盖（命中见上）
