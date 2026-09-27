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

---

## §3.1 P2 首轮执行记录（2026-09-27 17:14 收账 ✓）

### (a) 实跑与逐字裁决 ✓

```
[seed table] [(2, 505), (2, 692), (3, 492), (3, 508), (3, 643), (3, 659)]
[chain 1] seed unc=2 t=0s
[chain 1 it 100000] unc=4 best_unc=2 wmax=24 t=491s
[chain 1] seed priv=2 end best_unc=2 iters=181754 t=900s
[verdict] |C|=119 distinct=119 uncovered=2 no 119 witness in budget | chains=1 iters=181754 elapsed=900s
```

- 脚本：`work/k10/p2_119k_search.py`（k=119 固定、预算 900s）；日志 `/tmp/p2k119.log`；结果 `work/k10/p2k119_best.json`（64K，写于 16:56）
- **裁决：无 119-witness ✗**（`witness:false`、`uncovered:2`）——18.2 万次迭代、单链，**未**逃出 unc=2

### (b) 独立复核（本档自写校验器 `work/k10/verify_p2k119.py`，pyguard 512MB，与生成端**不同代码** ✓）

```
json.size=119  json.uncovered=2  witness=False
|C|=119  distinct=119  in_range=True
INDEP: 覆盖=1022/1024  未覆盖=2  => [473, 507]
私有覆盖数 min=2 max=11
洞 y=473 候选替换词数=11 ; 洞 y=507 候选替换词数=11
两洞公共 B1 交集 = [475, 505]
```

- ✓ **与生成端一致**：`|C|=119`、`distinct=119`、覆盖 **1022/1024**、未覆盖点 = **{473, 507}**
- ✓ **两洞距离 = 2**（`d(473,507)=2`），且 `B1(473) ∩ B1(507) \ C = {475, 505}` **非空** ⟹ 存在**同时覆盖两洞**的单词 ⟹ §0 (TC-1) 闭性论证的"除非距离≤2"**例外情形在本候选上真的发生了** ⚠️ ⟹ 必须实证补扫，不得靠论证带过 ✓

### (c) ⭐ 完整 1-flip 穷举（本档新增 = **穷举实测**；词 `1-flip` 档案已有 ⟹ 见 (g) 回查 ✓；`work/k10/flip_scan_119.py`）

```
base unc = [473, 507]
d(473,507) = 2
1-flip 最优 = (2, None)      ← 全部 119×905 次替换（精确重算 unc）
1-flip 无 witness（unc 最小值 = 2）⟹ 单字邻域确为平台 ✓
```

- **结论**：即使落入 (TC-1) 的例外情形（两洞距离=2、有公共覆盖词），**穷举全部单字替换**后 `unc` 最小值仍为 **2** ⟹ `unc=2` 在本候选上是**真 1-flip 局部最优** ✓
- **机制**：删任一词 loss ≥ 2（私有覆盖数 min=2），加公共覆盖词 gain ≤ 2 ⟹ **最多持平、不可能归零** ⟹ §0 (TC-1) 的"1-flip 平台"由**实测穷举**钉死 ✓（原论证仅作一般性陈述，本档补证例外情形）
- ⟹ **单字邻域已穷尽 ⟹ 下一步必须走出 1-flip**（2-opt/k-opt 或允许上坡的退火）✓

### (d) 弱机制对照（旁证，支持选"(甲)"）

| 变体 | 参数 | 结果（逐字） | 判定 |
|---|---|---|---|
| `anneal.py` | m=119 纯退火，4 次 restart × 20s | `best_unc=27/24/25/24` | ✗ 远劣于 unc=2 |
| `repair119.py` | 随机洞 + 最小私有数替换 + tabu + SA | m=120 **自检** 60 次 restart × 15s：`best_unc` **26–37**，**never 0** ⟹ `m=120 自检失败 ✗ 机制太弱 ⚠️` | ✗✗ **该变体在 k=120（witness 已知存在）都到不了 0** ⟹ 结构性太弱 |

- ⚠️ **`repair119.py` 存在预算 bug**：`for r in range(60): search(m, bd/6.0, ...)` ⟹ 实际最长 = **60 × bd/6 = 10 × bd** ⟹ m=120 段 900s（原意 90s）、m=119 段 **6000s**（原意 600s）——超预算 10 倍，已在 (e) 按 PID 终止 ✓
- ⟹ 两条"允许上坡"的朴素实现均**远劣**于当前 targeted-repair 机制 ⟹ 单纯加退火 ≠ 出路，**(甲) 2-opt/k-opt 更对症** ✓

### (e) 收尾核查 ✓

- **残留进程**：`ps -eo pid,comm,etime,args | grep pytho[n]3` ⟹ **空** ✓（`repair119.py` PID 45880，已运行 22:44，按 PID `kill -TERM` 终止 ✓，未受其进程组牵连 ✓）
- **core dump**：`dn-project` 内 `find -maxdepth 3 -name core*` ⟹ **无** ✓；仅 `/tmp/core_backup/core`（17MB，**2026-08-21 旧物**，非本次产物，未动）
- **资源**：load 1.05；Mem used 3780MB / avail 309MB + cache 4115MB ✓

### (f) ⟹ §3 提请拍板（未动，待唐先生）

```
$$\text{(甲)}\ \text{2-opt/k-opt P2（对症 unc=2 平台）};\quad \text{(乙)}\ \text{退火};\quad \text{(丙)}\ \text{停手并更新总图（写"未闭合"）}$$
$$
$$
```

- **建议倾向（参谋意见，非决定）**：**(甲)**——(c) 已证 1-flip 穷尽、(d) 两条退火类实现实测远劣 ⟹ 2-opt/k-opt 是唯一未试的对症邻域；但未见证 119 存在，**仍不得表述为"119 不存在"或"119 存在"** ✓

### (g) 【技术词回查】（定稿前实跑、逐字粘贴 ✓）

```
技术词 1-flip           命中文件数=2    :: ./ASSETS-REGISTRY.md ./MIPRUN2-2026-09-27-int10c-terminal-and-source-first-gate.md 
技术词 公共覆盖     命中文件数=1    :: ./MIPRUN2-2026-09-27-int10c-terminal-and-source-first-gate.md 
技术词 穷举           命中文件数=160    :: ./EXPERIMENT-filter-misfire-audit-1.md ./POS3-provably-positive-mechanisms-enumeration.md ./MECHANISM-2026-09-26-pinning-as-extremal-M-and-what-is-actually-new.md 
```

- **本档新增**：`公共覆盖`（**首次命名** ✓，命中 1 档 = 本档）；`1-flip **穷举实测**`（**行为**新增 ⟹ §0 (TC-1) 例外情形之实证排除）
- **档案已有（引用，不列为提出）**：词 `1-flip`（命中 2 档，`ASSETS-REGISTRY.md` 已在）
- **通用词（不计）**：`穷举`（命中 160 档）
