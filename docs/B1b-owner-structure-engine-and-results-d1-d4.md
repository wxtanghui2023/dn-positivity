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

---

## §6 补录（唐先生 14:56 收口 + 仪表要求）

**① 证书措辞（正式收口 `d≤4`）**：先生给出的形式为
$$\forall D\subset C_{120},\ |D|\le4:\quad \min\{|A|:(C_{120}\setminus D)\cup A\ \text{covers}\ Q_{10}\}>|D|+1$$
**我方实测更强**（因 119 相关阈值为 `|A| ≤ d−1`）：
$$\min|A|>|D|-1=3\ (\text{对 }d=4)\ \Longrightarrow\ \text{蕴含上式}\ ✓\qquad \text{两式一并登记}$$
$$\boxed{\text{不存在与该 }120\text{-code 删除距离}\le4\ \text{的 }119\text{-code}}\quad(\text{局部结论，\textbf{不得}写成全局 }K(10,1)>119)$$

**② `d=3` 裕量仪表（新，仪器化版 `b1b_engine2.py`）**：
```
tested=280,840 | L1 快剪剔 280,682 | 存活 158 | τ 直方图 {3: 158}
最小裕量 τ−(d−1)=1   ← 全部近命中**恰好差一个球**
τ = d+1 = 3 的近命中候选已留 50 例（near_miss_candidates）
```
**③ 独立验证（要求⑤）**：取三例近命中，用**独立代码路径**（完备分支，不复用引擎函数）复核：
```
D=[0,47,83] |U|=15: 1字=None 2字=None 3字=[3, 406, 662]
D=[2,47,83] |U|=19: 1字=None 2字=None 3字=[24, 406, 662]
D=[3,47,83] |U|=21: 1字=None 2字=None 3字=[41, 406, 662]
```
⟹ 引擎 τ 计算被证实 ✓；**结构观察**：三例的 3 字覆盖**均含 `406` 与 `662`** ⟹ 疑似"通用修补字"，列入观察项。

**④ 仪表化字段**（照先生 14:56 要求，已实现于 `b1b_engine2.py`）：
```
总 D 数 | |U| 分布 u_hist | packing 剪枝数 | 精确搜索进入数(need_lower) |
τ 直方图 tau_hist | 最小裕量 min_margin_vs_dminus1 与 vs_dplus1 |
τ ≤ d+1 近命中候选留存（≤50 例/档，含 D, τ, |U|）| τ > d+2 的 cap_hits
```
**⑤ 状态登记**：`B1-b = OPEN`；`d≤4 = COMPLETE/found=0`；`d=5 = RUNNING`（4 分片，按 `i₁ mod 4` 均衡）；`K(10,1) ≤ 119 = 尚未证明`。

---

## §7 A 线：158 个 `(d=3, τ=3)` 近命中的四层结构分析（2026-09-25 15:0x）

### §7.1 先自查并**更正**一处我自己的错误结论

```
$$\text{我此前称 "}406,662\ \text{是通用修补字"}\ \Longrightarrow\ \boxed{\textbf{假象（取样假象＋重加结构）}}$$
$$\text{原因}:\ \text{三例里我\textbf{固定了索引 }47,83\ (\text{字 }406,692)\ \text{只变第一个};\ \text{且覆盖面 }\{WORDS[i],406,662\}\ \text{中 }406,692\in D\ \text{是\textbf{重加}}$$
$$\text{正式判定见 §7.3}:\ L2\ \text{universal}=\varnothing,\ L3\ \text{forced}=\varnothing \Longrightarrow \textbf{不存在跨 }D\ \text{的通用／强制修补字}$$
```

### §7.2 极小覆盖的频率（L1）

```
$$\text{全部极小 3-覆盖（含重加）top}:\ 406(218)\mid 662(119)\mid 692(119)\mid 475(26)\mid 505(26)\mid 492,939,959,1010(14)$$
$$\text{其中 }406,692\ \text{是\textbf{码字}（在 }D\ \text{内 ⟹ 重加）};\ 662,475\ \text{才是新字}$$
$$\boxed{\text{纯新字 }3\text{-覆盖}: \textbf{0 例}/158}\ \Longrightarrow\ \text{任何极小修补都必须把已删字放回}\ ✓$$
```

### §7.3 L2 universal / L3 forced（正式定义下）

```
$$L2:\ \bigcap_{D}\bigcup_{A\in\mathcal S_D}A=\varnothing\ \Longrightarrow\ \textbf{无 universal 修补字}$$
$$L3:\ \bigcap_{D}\bigcap_{A\in\mathcal S_D}A=\varnothing\ \Longrightarrow\ \textbf{无 forced 修补字}$$
$$\Longrightarrow\ \text{局部缺陷\textbf{不集中于固定字集}};\ \text{不存在"}\{406,662\}\ \text{核心"这样的结构} ✓$$
```

### §7.4 为什么它们不特殊（L4）＋ orbit

```
$$662:\ |B(662)\cap U_D|\in[0,5],\ \text{均值 }2.89;\quad 475:\ \text{均值 }0.35\ (\text{几乎无用})$$
$$\text{平移稳定子}\ |\mathrm{Stab}(C_{120})|=1\ (\text{仅恒等})\ \Longrightarrow\ \text{码无平移对称}\ \Longrightarrow\ 406,662\ \text{不可能同 orbit} ✓$$
$$\text{L5 聚类}:\ 15\ \text{个签名类（按 }|U_D|,\ \text{覆盖型签名）};\ \text{主类}=\{2\ \text{重加}+1\ \text{新字}\}\ \text{或}\ \{3\ \text{重加}\}$$
```

### §7.5 ⭐ 真正的结构量 `ρ(D)`（**纯新字**最小覆盖）

```
$$\rho(D):=\min\{|A|:\ A\subseteq Q_{10}\setminus C_{120},\ A\supseteq\text{覆盖 }U_D\}$$
$$\textbf{d=3（全 158 例）}:\quad \rho=5:\ 7\ \text{例}\mid \rho=6:\ 28\ \text{例}\mid \rho\ge7:\ 123\ \text{例}$$
$$\textbf{d=4（抽 60 例）}:\quad \rho\ge6\ (\text{全部};\ \text{cap=5 未命中})\ \Longrightarrow\ \rho-d\ge2$$
$$\text{对照目标}:\ 119\ \text{码需 }|A|=d-1\ \Longrightarrow\ \text{纯新字路线差}\ \ge3\ \text{个量级裕度} ✓$$
```

### §7.6 机制：为什么新字不够用

```
$$\text{新字最大重叠}:\ \max_{w\notin C_{120}}|B(w)\cap U_D|\le 5\ (\text{124/158 例}=4)$$
$$\text{重加字重叠}:\ \max_{c\in D}|B(c)\cap U_D|=7\text{–}11\quad(\text{因其\textbf{拥有} }U_D\ \text{的点})$$
$$\Longrightarrow\ \text{计数下界}\ \lceil |U_D|/\max_{\text{new overlap}}\rceil\approx 3\text{–}6\ (\text{均值 }4.56)\ \text{与实测 }\rho=5\text{–}7\ \text{同量级} ✓$$
$$\boxed{\text{机制}:\ U_D\ \text{的点"几乎私有"于被删字};\ \text{新字每次只能吃掉 }4\text{–}5\ \text{点} \Longrightarrow \text{修补必须重加}}$$
```

### §7.7 可写的结构结论（**本档范围**）

```
$$\boxed{\text{对 }|D|=3:\ \text{任何极小修补必须重加}\ge2\ \text{个被删字};\ \text{纯新字修补需}\ge5\ \text{个}}$$
$$\boxed{\text{对 }|D|=4\ (\text{抽样}):\ \text{纯新字修补需}\ge6\ \text{个}}$$
【边界】 \text{以上为} C_{120}\ \text{的\textbf{局部}计算事实};\ \textbf{不构成} K(10,1)>119\ \text{的全局论断};\ \rho\ \text{的 d=4 部分为抽样}
【产物】 \texttt{work/k10/b1b\_a\_line.py}\mid\texttt{b1b\_a\_line.json}\mid\texttt{b1b\_a\_line\_rho.json}\mid\texttt{b1b\_a\_overlap*.json}
【进行中】 \text{d=4 仪器化}（CAP=4）\mid \text{d=5 四片}（CAP=4，决策阈值 d−1=4）

## §附 A 线【技术词回查】（**先跑后写**）

```
$ bash scripts/tech_word_check.sh "universal 修补字" "纯新字" "ρ(D)" "局部刚性"
技术词 universal 修补字 命中文件数=0    ::
技术词 纯新字        命中文件数=0    ::
技术词 ρ(D)            命中文件数=0    ::
技术词 局部刚性     命中文件数=30   :: ./C207-T13A-YI-4-continuous-family-exclusion-renaming-and-T13B2-seal.md ./C204-T13-A-YI-1-cluster-separation.md ./C222-B-interval-newton-KKT-strict-box-X0-existence-and-uniqueness.md
```
- **本档新增**：`universal 修补字`、`纯新字`、`ρ(D)`（回查前均 0 档）
- **档案已有（引用）**：`局部刚性`（30 档，但均**异语境**）⟹ 列为通用词，不计新性
- **⚠️ 新性边界**：本档**无**数学新性主张；结果为**特定码的局部计算事实**

---

## §8 A 线第二刀（15:2x）：packing 证书 ＋ M₃ 分类

### §8.1 `d=3` 升级为 **packing 证书**（不再需要精确覆盖搜索）

```
$$\alpha_2(U_D)\ \text{分布（158 个幸存者，精确值）}=\boxed{\{3:\ 158\}}\ \Longrightarrow\ \text{全部 }\alpha_2=3$$
$$\text{被剪的 }280{,}682\ \text{个 }D:\ \text{其 }u_1\subseteq U_D\ \text{内已含 3 点两两距离}\ge3\ \text{的贪心见证} ✓$$
$$\boxed{\forall D,\ |D|=3:\ \alpha_2(U_D)\ge3}\ \Longrightarrow\ \text{半径-1 球至多覆盖其中 1 点}\ \Longrightarrow\ \min|A|\ge3>d-1=2$$
$$\Longrightarrow\ \text{无 delete-3-add-2}\ \Longrightarrow\ \text{该距离内无 }119\text{-码}\ ✓\quad(\text{证书形式}=\text{有限个 3 点见证})$$
$$

### §8.2 `M₃ = 5` 与 owner-pattern 分类（**"统一 ≤4" 猜想已撤**）

```
$$M(D)\ \text{分布}=\{3:23\mid4:124\mid5:11\}\ \Longrightarrow\ \boxed{M_3=5}\ (\text{与唐先生 15:09 的观察一致})$$
$$\text{达到 }M_3\ \text{的 }(D,w)\ \text{对}=12\ \text{个，分层模式}:\quad \boxed{q_1=5:\ 8\ \text{例}}\mid\boxed{q_1=4,\ q_2=1:\ 4\ \text{例}}\mid q_3\ \text{从不参与}$$
$$\text{例}:D=[18,47,83],\ w=182,\ \text{owner\_sets}=[(18),(18),(47),(47),(83)]$$
$$\Longrightarrow\ \boxed{\text{overlap}=5\ \text{只能来自"近乎私有"的点}}\ (\text{唐先生 15:09 的严格 owner-pattern 猜想成立}) ✓$$
$$

### §8.3 框架级发现：**所有 119-码都在"删除 d／补入 d−1"族内**

```
$$\text{设 }C'\ \text{为 119-码},\ D:=C_{120}\setminus C',\ A:=C'\setminus C_{120};\quad |A|=119-|C'\cap C_{120}|=|D|-1\ ✓$$
$$\Longrightarrow\ \boxed{\text{packing 引理}\ \alpha_2(U_D)\ge|D|\ \text{对给定 }d\ \text{成立}\ \Longrightarrow\ \text{该 }d\ \text{处无 }119\text{-码}}$$
$$\text{上限}:\ \alpha_2\le A(10,3)=\mathbf{72}\ \Longrightarrow\ \text{该引理只能覆盖小 }d\ (\text{恰为 B1-b 邻域设定})$$
$$\text{对比}:\ d=3\ \text{已证}\ \alpha_2\ge3=|D|\ ✓;\quad d=4\ \text{进行中（见 §8.4）}$$
$$

### §8.4 `d=4` packing 证书（进行中）

```
$$\text{进度}(4{,}000{,}000/8{,}214{,}570):\quad \text{cand}=3{,}815{,}295,\ \text{贪心见证成功}=3{,}796{,}612\ (99.5\%)$$
$$\text{剩余}\approx18{,}700\ \text{例贪心失败}\ \Longrightarrow\ \text{待精确 }\alpha_2\ \text{复核（便宜）}$$
\text{脚本}:\ \texttt{work/k10/b1b\_pack\_cert.py}\mid\text{产物}:\ \texttt{b1b\_packcert\_d4*.json}
$$
**【边界】** `d=3` 的 packing 证书为**局部邻域证书**（仅排除与 `C_{120}` 删除距离 3 的 119-码）；**不构成**全局 `K(10,1)>119`；`d=4` 尚在进行。

---

## §9 **统一 packing 证书：`d ≤ 4` 完成**（2026-09-25 16:2x）

### §9.1 `d=4` packing 证书（完整）

```
$$\text{枚举全量}:\ \text{tested}=\mathbf{8{,}214{,}570}\ (\text{全部 }\binom{120}{4})$$
$$\text{需查（u1 内无 4 点见证者）}=\text{cand}=7{,}950{,}947;\quad \text{贪心见证成功}=\text{cert}=7{,}919{,}048$$
$$\text{贪心失败}=\mathbf{31{,}899}\ (0.40\%)\ \Longrightarrow\ \text{对这 31{,}899 例做\textbf{精确 }4\text{-clique decision}}$$
$$\boxed{\text{精确判定}:\ \text{PASS}=31{,}899\ \mid\ \text{FAIL}=\mathbf{0}}\ \Longrightarrow\ \forall D,\ |D|=4:\ \alpha_2(U_D)\ge4\ ✓✓$$
$$\text{判定仅用 }6\ \text{秒（clique decision，非 }\tau\ \text{搜索）}$$
```

### §9.2 **统一证书（d ≤ 4）**

```
$$\boxed{\forall D\subseteq C_{120},\ |D|\le4:\quad \alpha_2(U_D)\ \ge\ |D|}$$
$$\Longrightarrow\ \text{半径-1 球至多覆盖 packing 中 1 点}\ \Longrightarrow\ \rho(D)\ \ge\ |D|\ >\ |D|-1$$
$$\Longrightarrow\ \boxed{\text{deletion distance}\le4\ \text{内不存在 }119\text{-码}}\ (\text{局部证书})$$
$$\text{对照旧形式}:\ \text{旧}=280{,}840+8{,}214{,}570\ \text{个精确覆盖问题全失败};\ \text{新}=\text{统一 packing 命题}+\text{有限见证}$$
```

### §9.3 方法（照唐先生 16:0x 指示）

```
$$\text{① 贪心见证}（\text{快}）\to\text{② 失败例做\textbf{精确 clique decision}}（\text{只判是否存在 }K_d，不求完整 }\alpha_2）$$
$$\text{判定器自检（同一套 }has\_clique）：60\ \text{个已知 }\alpha_2=3\ \text{的 }d=3\ \text{例}:\ \text{target3}=\mathbf{60/60\ PASS},\ \text{target4}=\mathbf{0/60\ PASS}\ ✓✓$$
$$\text{上界提醒}:\ \alpha_2\le A(10,3)=72\ \Longrightarrow\ \text{packing 证书只能覆盖小 }d\ (\text{与邻域设定吻合})$$
```

### §9.4 本阶段自查出的 4 个自身缺陷（全部已修）

```
(i)\ \textbf{键类型 bug}:\ 分层索引把单点层键写成元组、查询用 int\ \Longrightarrow\ \text{私有点丢失}\ \Longrightarrow\ d=5\ \text{早期 }\text{cert}=0\ \text{是\textbf{假象}}（\text{已修}; \text{引擎版无此错}）
(ii)\ \text{失败例列表原封顶 }20\ \Longrightarrow\ \text{改为\textbf{流式落盘}}（\text{否则无法做精确阶段}）
(iii)\ \texttt{pkill}\ \text{自杀陷阱}\ \times2:\ \text{同一命令行含目标字面名}\ \Longrightarrow\ \text{杀自身 shell}（\text{TOOLS.md 已记，仍复发}）
(iv)\ \text{重复启动 }6\ \text{个同任务进程写同一文件}\ \Longrightarrow\ \text{数据污染};\ \text{改为\textbf{单次运行纪律}}
$$

### §9.5 状态与边界

```
$$\text{进行中}:\ \boxed{d=5}\ (\text{四片并行，目标 }\alpha_2\ge5)\ \text{预计}\sim45\ \text{分钟}$$
$$\textbf{边界（必须遵守）}:\ \text{本证书为\textbf{邻域证书}}（\text{仅排除与 }C_{120}\ \text{删除距离}\le4\ \text{的 }119\text{-码}）$$
$$\qquad \textbf{不得}写成全局\ K(10,1)>119;\quad \text{全局结论需 }packing\ \text{引理对所有 }D\ \text{成立（含大 }D）\ \text{或其它论证}$$
\text{产物}:\ \texttt{b1b\_packcert\_d4.json}\mid\texttt{b1b\_packfail\_d4.jsonl}\mid\texttt{b1b\_packfail\_d4\_exact4.json}\mid\texttt{exact\_pack.py}
```

---

## §10 SDR 路线（结构性升级的第二刀，2026-09-25 17:1x）

### §10.1 判据替换：从 "greedy + U_D" 到 **私有代表系（SDR）**

```
$$\textbf{SDR 判据}:\ \exists\ \text{选取 } v_c\in P_1(c)\ (c\in D)\ \text{使}\ d_H(v_c,v_{c'})\ge3\ \forall c\ne c'$$
$$\Longrightarrow\ \text{所有 }v_c\in U_D\ \Longrightarrow\ \alpha_2(U_D)\ge|D|\ \Longrightarrow\ \rho(D)\ge|D|>|D|-1\ ✓$$
$$\text{优点}:\ \text{只需预计算 }P_1(c)\ (\text{内存极小})\ \text{且速度快}\ \sim8\times\ (\text{greedy 版 }17.5\text{k/s}\to\text{SDR 版 }134\text{k/s})$$
$$

### §10.2 三条结构事实（实测）

```
$$\textbf{(i) 对偶引理}:\ \forall c\ne c'\ \exists v\in P_1(c),\ v'\in P_1(c'):\ d(v,v')\ge3\quad\Longrightarrow\ \text{失败 }\mathbf{0/7140}\ ✓\ \textbf{普适}$$
$$\textbf{(ii) 命中性}:\ \forall c,\ \forall X\ (\le4\ \text{点，来自它字私有点})\ \exists v\in P_1(c):\ d(v,X)\ge3\ \Longrightarrow\ \text{失败 }\mathbf{4/4800}\ ✗\ \textbf{非普适}$$
$$\qquad \Longrightarrow\ \text{贪心\textbf{必须回溯}}（\text{解释了 }sdr\_ok\ \text{需要 backtrack}）$$
$$\textbf{(iii) }P_1(c)\ \text{内部}:\ \mathbf{120/120}\ \text{个字的私有点都含"距离}=1\ \text{的相邻对}\ \Longrightarrow\ \text{私有点成对相邻（强规律）}$$
$$

### §10.3 `d=5` 证书（进行中，2 片 · 断点续跑）

```
$$\text{分片}:\ i_1\in[0,14]\ (\text{A})\ \text{与}\ [15,119]\ (\text{B});\quad \text{每完成一个 }i_1\ \text{写 state 文件}\ \Longrightarrow\ \text{重启可续} ✓$$
$$\text{实测速率}:\ 134\text{k D/s/片};\quad \text{已证 }12{,}506{,}877/190{,}578{,}024\ (\text{fail}=\mathbf{0},\ \text{unk}=\mathbf{0})$$
$$\text{ETA}\approx12\ \text{分钟}$$
$$

### §10.4 **CPU/内存纪律（唐先生 17:13 提醒后立规）**

```
$$\text{事故}:\ \text{我曾同时跑 6+ 个进程}\ \Longrightarrow\ \text{load 峰值 }\mathbf{104}\ (\text{4 核})\ \Longrightarrow\ \text{容器于 }17{:}06\ \text{重启};\ \text{后台任务全失}$$
$$\textbf{新纪律}:\ (a)\ \text{后台进程}\le\mathbf{2};\quad (b)\ \textbf{必须断点续跑}（state 文件）;\quad (c)\ \text{低内存设计}（\text{流式落盘、勿累积}）$$
$$\qquad (d)\ \text{勿在 exec 内用 }|\ tail\（\text{缓冲吞输出}）;\quad (e)\ \text{不并发跑额外测试脚本}$$
$$\text{现状}:\ \text{load }3.0/4\ \text{核};\ \text{可用内存 }5.9\text{G}\ ✓$$
$$

### §10.5 下一步（照唐先生 17:0x）

```
$$\text{若 }d=5\ \text{亦 }\text{fail}=0\ \Longrightarrow\ \textbf{立即攻击 SDR 引理的结构性证明}（\text{不再机械扩到 }d=6）$$
$$\text{证明种子}:\ \text{(i) 对偶引理（}\mathbf{0/7140}\ \text{普适）};\quad \text{(iii) }P_1(c)\ \text{的相邻对结构};\quad \text{(ii) 的 }4\ \text{个反例（界定了贪心边界）}$$
$$\textbf{边界}:\ \text{仍为相对 }C_{120}\ \text{的局部证书};\ \textbf{不得}写成 }K(10,1)>119$$
```

---

## §11 **d=5 完成** ＋ 计数路线 ＋ CPU/内存护栏（2026-09-25 20:2x）

### §11.1 `d=5` SDR 证书：**全量通过，零失败**

```
$$\text{A 片 } i_1\in[0,14]:\quad \text{tot}=94{,}017{,}378\ =\ \text{cert},\quad \text{fail}=0,\ \text{unk}=0\quad (680\ \text{s})$$
$$\text{B 片 } i_1\in[15,119]:\ \text{tot}=96{,}560{,}646\ =\ \text{cert},\quad \text{fail}=0,\ \text{unk}=0\quad (702\ \text{s})$$
$$\text{合计}=\mathbf{190{,}578{,}024}=\binom{120}{5}\ \text{（正好全量）};\quad \text{失败文件 0 行}\ \Longrightarrow\ \forall D,|D|=5:\ \text{SDR 存在}\ \Longrightarrow\ \alpha_2(U_D)\ge5\ ✓✓$$
$$\textbf{统一证书（d ≤ 5）}:\ \boxed{\forall D,\ |D|\le5:\ \alpha_2(U_D)\ge|D|}\ \Longrightarrow\ \rho(D)\ge|D|>|D|-1$$
$$\Longrightarrow\ \boxed{\text{deletion distance}\le5\ \text{内不存在 }119\text{-码}}\quad(\text{仍为局部证书})$$
$$

### §11.2 计数路线（**更简洁的证明靶**）

```
$$\text{定义 } M(D):=\max_{w\notin C_{120}}|B_1(w)\cap U_D|\ \ (\text{新字对缺口的最大重叠})$$
$$\text{则}\ \rho(D)\ \ge\ \left\lceil \frac{|U_D|}{M(D)}\right\rceil;\qquad \textbf{证明靶}:\ \boxed{\left\lceil \frac{|U_D|}{M(D)}\right\rceil\ >\ |D|-1}\iff |U_D|>M(D)\cdot(|D|-1)$$
$$
| d | `|U_D|` 范围（均值） | `M(D)` 分布 | `⌈|U|/M⌉` | 需 > d−1 |
|---|---|---|---|---|
| 3 | [12,30]（20.1） | {2:64,3:99,4:128,5:8,6:1} | [4,13] | >2 ✓ |
| 4 | [18,37]（26.8） | {2:13,3:78,4:180,5:27,6:2} | [5,16] | >3 ✓ |
| 5 | [25,44]（33.9） | {3:8,4:36,5:15,6:1} | [6,12] | >4 ✓ |

```
$$\text{抽样 }300/300/60\ \text{例\textbf{全部满足}} ✓✓\quad \textbf{裕度}\ge2\ (\text{如 }d=5:\ \ge6\ \text{vs 需}>4)$$
$$\textbf{注意}:\ M(D)\ \text{可达 }6\text{–}7\ \Longrightarrow\ \textbf{不存在固定统一上界}（\text{与唐先生 15:09 的判断一致}）\ \Longrightarrow\ \text{应证\textbf{联合不等式}}$$
$$

### §11.3 CPU/内存护栏（唐先生 20:24 令）

```
$$\text{事故}:\ \text{当日多次并发/大循环}\ \Longrightarrow\ \text{load 峰值 104}\ \Longrightarrow\ \text{容器重启};\ \text{另有 Killed(OOM)}$$
$$\textbf{规则（已入 }TOOLS.md\ \text{＋}\ AGENTS.md\ §11\text{，违反视为任务失败）}:\ \text{后台 Python}\le2;\ \text{一律经 }pyguard.sh;\ \text{断点续跑};\ \text{流式落盘};\ \text{禁 }|tail;$$
$$\qquad \text{内存目标}<500\text{MB};\ \text{启动前查 load/free};\ \text{结束核验}$$
$$\textbf{护栏 } \texttt{scripts/pyguard.sh}:\ \text{① }\mathtt{ulimit -v}\ \text{② 单线程(}{\rm OMP/OPENBLAS/MKL}{=}1)\ \text{③ }\mathtt{nice}\ \text{④ 并发闸}\le2\ \text{⑤ 槽位自动回收}$$
$$\text{三项自检通过}:\ \text{单线程 ✓}\mid \text{内存上限生效（800MB 申请 → MemoryError）✓}\mid \text{并发闸（第 3 个自动等待）✓}$$
$$\textbf{实战拦截}:\ pyguard\ \text{当场拦下我把 }1.9\times10^8\ \text{组合物化成 list 的 MemoryError} ✓✓$$
$$

### §11.4 下一步（照唐先生 17:0x）

```
$$\text{不再机械扩 }d=6;\ \text{转而攻\textbf{结构性证明}};\ \text{首推\textbf{计数路线}（§11.2 的联合不等式）}$$
$$\text{可用部件}:\ \text{① 对偶引理（0/7140 普适）}\mid \text{② }P_1(c)\ \text{恒含相邻对（120/120）}\mid \text{③ 私有性（新字重叠受限于"私有"结构）}$$
$$\textbf{边界}:\ \text{仍为相对 }C_{120}\ \text{的局部证书};\ \textbf{不得}写成 }K(10,1)>119$$
```

---

## §12 **d=3 全量 Γ-census（精确有限分类）**（2026-09-25 20:4x）

### §12.1 精确结果

```
$$\text{全量 } \binom{120}{3}=280{,}840\ \text{例};\qquad \Gamma(D):=|U_D|-(d-1)M(D)=|U_D|-2M(D)$$
$$\boxed{\Gamma_{\min}=\mathbf{3}}\ (\text{13 例});\quad \Gamma\ \text{分布}: 3{:}13,\ 4{:}84,\ 5{:}445,\ 6{:}1249,\ 7{:}2817,\ 8{:}5962,\ 9{:}11802,\ 10{:}19436,\ 11{:}24729,$$
$$\qquad 12{:}33791,\ 13{:}35136,\ 14{:}38780,\ 15{:}34093,\ 16{:}24690,\ 17{:}20075,\ 18{:}10962,\ 19{:}7886,\ 20{:}4178,\ 21{:}2411,\ 22{:}1365,\ 23{:}538,\ 24{:}386,\ 25{:}12$$
$$\Longrightarrow\ \Gamma(D)\ge3\ \text{（d=3 全量）}\ \Longleftrightarrow\ \boxed{|U_D|\ \ge\ 2M(D)+3}\quad(\text{比 }\Gamma>0\ \text{更强})$$
$$\textbf{抽样教训}:\ \text{660 抽样给 }\Gamma_{\min}=6;\ \text{全量给 }\mathbf{3}\ \Longrightarrow\ \text{抽样\textbf{系统性低估极值}} ✓\ (\text{已记})$$
```

### §12.2 **13 个极值构型（全部）**

```
$$(|U|,M)\in\{(7,2),(11,4),(15,6)\}\ \text{且恒满足}\ \boxed{|U|=2M+3}\ (\text{等号族});\quad M\ \text{恒为\textbf{偶数}}$$
$$\Delta=0\ \text{全部成立}\ \Longrightarrow\ \textbf{极值均为"纯私有"缺陷（无共享）} ✓\ (\text{猜想①成立})$$
$$P^\downarrow\ \text{仅 4 种形态}:\ (6,3,2)\times6\mid(3,2,2)\times4\mid(5,4,2)\times2\mid(6,6,3)\times1\ \Longrightarrow\ \text{极值族\textbf{小且可枚举}} ✓$$
$$\text{被删热字}:\ 83(9)\mid77(8)\mid58(7)\mid49(3)\mid89(3)\mid13,90(2)\mid\ldots$$
$$\text{修补热字}:\ 673(6)\mid475(4)\mid662(4)\mid645(3)\mid\ldots$$
$$

### §12.3 **否定结果：`P↓ → M` 无函数关系**

```
$$\text{统计}: 164\ \text{种 }P^\downarrow\ \text{形态};\ \text{其中 57 种都能达到 }M=6\ \Longrightarrow\ \boxed{\text{不存在 }P^\downarrow\Rightarrow M\ \text{的简单关系}} ✗$$
$$\qquad \Longrightarrow\ \text{联合不等式必须以\textbf{其它耦合量}表达（\text{不能靠 partition 决定 }M）}$$
$$

### §12.4 结论与下一步

```
$$\textbf{Lemma C（d=3）已从"抽样支持"升级为\textbf{精确有限分类}}:\ \text{极值 = 13 个可枚举构型} ✓$$
$$\text{等价目标}:\ \boxed{|U_D|\ge2M(D)+3}\ (\text{等号恰在 13 例})$$
$$\text{下一步（照唐先生 20:36 的预案）}:\ \text{① 用"热字集"(83,77,58,49,89,\ldots)\ 做 }d=4\ \text{\textbf{定向扫描}}\ (\text{廉价});$$
$$\qquad \text{② 若极值机制"抬升"成功}\ \Longrightarrow\ \text{再决定 }d=4\ \text{是否全量};\ \text{③ 不盲目跑 8.2M}$$
\text{产物}:\ \texttt{gamma\_d3\_full.py}\mid\texttt{gamma\_d3\_full.jsonl}(19.4\text{MB})\mid\texttt{gamma\_d3\_summary.json}
```

---

## §13 **d=3 包络曲线 ＋ 局部容量引理**（2026-09-25 20:5x）

### §13.1 包络表 `m_3(u)`（全量，u = |U_D|）

```
$$\textbf{Step A–C}:\ m_3(u):=\max\{M(D):|U_D|=u\},\quad g_3(u):=u-2m_3(u)$$
\begin{array}{c|c|c|c|c}
u&m_3(u)&g_3&\#D(u)&\#\text{达包络}\\ \hline
7&2&3&4&4\\
8&2&4&14&14\\
9&2&5&32&32\\
10&3&4&144&29\\
11&4&3&516&8\\
12&4&4&846&22\\
13&4&5&1988&119\\
14&5&4&5401&19\\
15&6&3&8838&1\\
16&5&6&12277&102\\
17&6&5&21784&1\\
18\!-\!29&6&6\!-\!17&\ldots&\ldots\\
30&5&20&300&42\\
31&6&19&180&18\\
33&6&21&20&20
\end{array}$$
$$\boxed{g_3\ge3};\qquad g_3=3\ \text{恰在}\ \boxed{u\in\{7,11,15\}}\ (m_3=2,4,6)\ \Longleftrightarrow\ \text{13 个极值构型} ✓$$
$$\textbf{注意}:\ m_3(u)\ \textbf{非单调}（m_3(15)=6>m_3(16)=5）\ \Longrightarrow\ \text{增量式单调律路线\textbf{不可用}} ✗$$
$$

### §13.2 ⭐ **局部容量引理（穷举验证，最干净的可证候选）**

```
$$\forall w\notin C_{120},\ \forall x\in C_{120}:\quad \boxed{|B_1(w)\cap\{v:x\in S(v)\}|\ \le\ 2}$$
$$\text{穷举 }664\times120=79{,}680\ \text{对，取值分布 }\boxed{\{0:\ 102{,}278\ \mid\ 2:\ 6{,}202\}}\ \Longrightarrow\ \textbf{只有 0 或 2，绝无 1}$$
$$\textbf{同一性}:\ |B_1(w)\cap P_1(x)|\le2\ \text{同样成立} ✓$$
$$\textbf{推论（已证）}:\ M(D)=\max_w|B_1(w)\cap U_D|\ \le\ \sum_{x\in D}|B_1(w)\cap\{v:x\in S(v)\}|\ \le\ \boxed{2|D|}$$
$$\qquad \Longrightarrow\ \textbf{对 }d=3:\ M\le6\ \text{（与实测 max }M=6\ \text{吻合）} ✓$$
$$\textbf{结构母题}:\ \text{捕获值}\in\{0,2\}\ \Longrightarrow\ \boxed{\text{被捕获的点成对出现}}\ \text{—— 与唐先生从 LMOV 提炼的"坏项配对"同构} ✓$$
$$

### §13.3 Step D：witness 贡献谱

```
$$\text{随机 4000 例：} \max_x m_x(w)\ \text{分布}=\{1{:}5,\ 2{:}3995\}\ \Longrightarrow\ \text{恒}\le2\ ✓$$
$$\text{达包络者的贡献向量}:\ (2,2,2)\times24\mid(2,2,0)\times3\mid(2,2,1)\times2\ \Longrightarrow\ \textbf{(2,2,2) 主导} ✓\ (\text{与唐先生猜测一致})$$
$$

### §13.4 d=3 的证明靶（已锁定）

```
$$\boxed{\text{靶 1（局部容量引理）}:\ m_x(w)\le2\ \text{且取值}\in\{0,2\}\ \Longleftarrow\ \text{穷举已验，待证}}$$
$$\boxed{\text{靶 2（耦合）}:\ |U_D|\ \ge\ 2M(D)+3\ \Longleftrightarrow\ \Gamma\ge3\ (\text{等号在 }u\in\{7,11,15\})}$$
$$\text{机制线索}:\ M=2k\ (k=\text{参与贡献的字数})\ \text{时}\ u\ge4k+3;\ \text{即"每个字的 2 点被捕获，迫使缺口额外增长"}$$
$$\textbf{注}:\ \text{粗合并（}M\le2d\ \text{＋ }|U|\ \text{下界）\textbf{不足以}推出靶 2（d=3 时 }u_{\min}=7<2\cdot2\cdot3+3)\ \Longrightarrow\ \text{必须用\textbf{耦合}} ✓$$
```

---

## §14 ⭐ **定理骨架：容量引理（已证）＋ 有限残量**（2026-09-25 21:0x）

### §14.1 **Lemma（容量上界）——两行纯度量证明**

```
$$\textbf{Claim}:\quad \forall w\notin C_{120},\ \forall x\in C_{120}:\quad |B_1(w)\cap\{v:x\in S(v)\}|\ \le\ 2$$
$$\textbf{Proof}:\quad w\ne x\ \Longrightarrow\ \{v:x\in S(v)\}\subseteq B_1(x)\ \Longrightarrow\ |B_1(w)\cap\{v:x\in S(v)\}|\le|B_1(w)\cap B_1(x)|$$
$$\qquad \text{而 Hamming 球交（10 维，半径 1）}:\quad |B_1(w)\cap B_1(x)|=\begin{cases}2,&d(w,x)\in\{1,2\}\\0,&d(w,x)\ge3\end{cases}$$
$$\qquad \text{（}d=1,2\ \text{时两球交于"交换对"两点；}d\ge3\ \text{时不相交）}\ \Longrightarrow\ \le2\ \square$$
$$\text{穷举核验}:\ 664\times120=79{,}680\ \text{对，公式\textbf{无反例}；取值分布}\{0{:}102{,}278\mid2{:}6{,}202\}\ \text{（\textbf{只有 0 或 2}）} ✓$$
$$\textbf{Corollary}:\quad M(D)=\max_w|B_1(w)\cap U_D|\ \le\ \sum_{x\in D}2\ =\ \boxed{2|D|}\quad(\text{完全严格，与码结构无关})$$
$$

### §14.2 **定理骨架（d ≤ 5 局部证书的结构化证明）**

```
$$\text{设 }|D|=d.\quad \text{Case A}:\ |U_D|>2d(d-1)\ \Longrightarrow\ \rho(D)\ge\left\lceil\frac{|U_D|}{M(D)}\right\rceil\ge\left\lceil\frac{2d(d-1)+1}{2d}\right\rceil=d>d-1\ ✓$$
$$\qquad (\text{只需 Lemma};\ \textbf{无需任何穷举})\ ✓✓$$
$$\text{Case B}:\ |U_D|\le2d(d-1)\ \Longrightarrow\ \textbf{有限残量}\ (\text{可逐个验证})$$
$$\textbf{d=3}:\ \text{A 覆盖 }|U|\ge13;\quad \text{B 残量}=\{|U|\le12\}\ \text{共}\ \mathbf{1{,}556}\ \text{个构型}\ (0.55\%)\ \text{（}u{=}7{:}4,\ 8{:}14,\ 9{:}32,\ 10{:}144,\ 11{:}516,\ 12{:}846\text{）}$$
$$\qquad \text{逐例}\ \max M\ \text{由 census 已知}:\ m_3(7..12)=2,2,2,3,4,4\ \Longrightarrow\ \Gamma\ge3\ ✓$$
$$\textbf{d=4}:\ \text{A 覆盖 }|U|\ge25;\ \text{B 残量}=\{|U|\le24\}\ (\text{由 d=4 census 给出，进行中})$$
$$\textbf{d=5}:\ \text{A 覆盖 }|U|\ge41;\ \text{B 残量}=\{|U|\le40\}$$
$$

### §14.3 意义（对照 LMOV 方法论）

```
$$\textbf{原形式}:\ \text{"28 万例全部通过"} \Longrightarrow \textbf{现形式}:\ \boxed{\text{一条两行度量引理}\ +\ \text{有限残量}}$$
$$\textbf{结构母题}:\ \text{捕获值}\in\{0,2\}\ \text{（成对）}\ \Longleftrightarrow\ \text{LMOV 的"坏项成对配对"} ✓$$
$$\textbf{容器思想}:\ \text{Lemma 与码的具体结构\textbf{无关}}（\text{纯 Hamming 度量}）\ \Longrightarrow\ \text{对所有半径-1 覆盖码成立，可直接复用} ✓$$
$$\textbf{仍缺（靶 2 剩余部分）}:\ \text{有限残量内}\ \Gamma>0\ \text{的\textbf{统一论证}}（\text{当前靠 census/穷举}）$$
$$

---

## §15 **极值几何解剖 ＋ 精化靶（4k+3）**（2026-09-25 21:1x）

### §15.1 球交公式（唐先生逐项验证，已穷举核验）

```
$$|B_1(x)\cap B_1(w)|=\begin{cases}n+1=11,&d(x,w)=0\\ 2,&d(x,w)=1\\ 2,&d(x,w)=2\\ 0,&d(x,w)\ge3\end{cases}\quad(\text{穷举 }1024^2\ \text{对，无反例}) ✓$$
$$\Longrightarrow\ S_x=\{v:x\in S(v)\}=B_1(x)\ \Longrightarrow\ |B_1(w)\cap S_x|\le2\ (w\ne x)\ \Longrightarrow\ M(D)\le2d\ ✓$$
$$

### §15.2 **13 个极值构型的球交几何**（全部算出）

```
$$\textbf{样板（唯一 }M=6\text{ 的极值）}:\ D=[49,77,89],\ |U_D|=15,\ P^\downarrow=(6,6,3),\ w=673$$
$$\qquad d(w,x_i)=[2,2,2];\quad B(w)\cap B(x_i)=\text{"交换对"两点，且\textbf{两点皆为该字私有点}}$$
$$\qquad B(w)\cap B(417)=\{161,929\}\ (\text{owner }49);\quad B(w)\cap B(643)=\{641,675\}\ (\text{owner }77);\quad B(w)\cap B(745)=\{681,737\}\ (\text{owner }89)$$
$$\textbf{三条规律}:\ (i)\ \text{贡献字皆在距离 2};\quad (ii)\ \text{捕获点\textbf{全为私有点}}（\Delta=0\ \text{一致}）;\quad (iii)\ \text{捕获对互不相交}\ \Longrightarrow\ M=2k$$
$$

### §15.3 ⭐ **精化靶：`M=2k ⟹ |U_D| ≥ 4k+3`**

```
$$\text{由 census 包络（偶数行）}: \quad k=1:\ |U|\ge7;\quad k=2:\ |U|\ge11;\quad k=3:\ |U|\ge15\ \Longleftrightarrow\ \boxed{|U_D|\ge2M(D)+3}\ \Longleftrightarrow\ \Gamma\ge3\ ✓$$
$$\textbf{与度量的关系}:\ \text{Hamming 度量只给 }|U|\ge2k\ (=\text{每字贡献 2 点的下界});\ \text{而 }4k+3\ \textbf{超出度量} \Longrightarrow$$
$$\qquad \boxed{\text{该耦合\textbf{依赖 }C_{120}\ \text{的具体结构}}\ (\text{"码的有限局部引理"})}\ \Longleftrightarrow\ \text{LMOV 中"特殊 ring／容器"那一招的位置} ✓$$
$$

### §15.4 证明架构（当前最优形态）

```
$$\boxed{\text{Case A（已证）}:\ |U_D|>2d(d-1)\ \Longrightarrow\ \rho\ge d\ \text{（仅用容量引理）}}$$
$$\boxed{\text{Case B（有限残量）}:\ |U_D|\le2d(d-1)}$$
$$\qquad \text{d=3}:\ \text{残量 }|U|\le12;\ \text{只需 6 个值}\ m_3(7..12)=(2,2,2,3,4,4)\ \Longrightarrow\ \Gamma\ge3\ ✓$$
$$\qquad \text{若要\textbf{消掉}残量} \Longrightarrow \text{证明 §15.3 的 }4k+3\ \text{（码结构引理）}$$
$$\textbf{边界}:\ \text{仍为相对 }C_{120}\ \text{的局部证书};\ \textbf{不得}写成 }K(10,1)>119$$
```

---

## §16 **M=6 全分类 ＋ 并集引理**（2026-09-25 21:2x）

### §16.1 M=6 的类型分类（全量 1,484 例）

```
$$\text{类型 }t=(d(w,x_1),d(w,x_2),d(w,x_3)):\quad (1,1,1)\ \textbf{与}\ (1,1,2)\ \textbf{完全不出现}\ ✓$$
\begin{array}{c|c|c|c}
t&\text{例数}&\min|U_D|&|U_D|\ \text{分布（前几项）}\\ \hline
(1,2,2)&310&18&18{:}1,\ 19{:}7,\ 20{:}14,\ 21{:}26,\ldots\\
(2,1,2)&386&18&18{:}1,\ 19{:}4,\ 20{:}24,\ldots\\
(2,2,1)&215&19&19{:}5,\ 20{:}10,\ 21{:}24,\ldots\\
(2,2,2)&573&\mathbf{15}&15{:}\mathbf{1},\ 17{:}1,\ 18{:}45,\ 19{:}28,\ldots
\end{array}$$
$$\boxed{M=6\ \Longrightarrow\ |U_D|\ge15};\quad \text{唯一等号}=\boxed{D=[49,77,89],\ w=673}\ (\text{即 §15 解剖的那一例}) ✓✓$$
$$

### §16.2 ⭐ **并集引理（纯 Hamming 几何，已证）**

```
$$\boxed{M(D)\ \le\ \left|\bigcup_{x\in D}\bigl(B_1(w)\cap B_1(x)\bigr)\right|}\quad(\text{对达到 }M\ \text{的 }w)$$
$$\text{球交的\textbf{两种形态}}:\quad d(w,x)=1\Rightarrow B_1(w)\cap B_1(x)=\{x,w\}\ (\textbf{都含 }w);\quad d(w,x)=2\Rightarrow\{\text{两中点}\}\ (\text{不含 }w,x)$$
$$\Longrightarrow\ \text{并集大小}:\ t=(1,1,1)\to\mathbf{4};\quad (1,1,2)\to\mathbf{5};\quad (1,2,2)/(2,2,2)\to\mathbf{6}\quad(\text{已逐例验证} ✓)$$
$$\Longrightarrow\ \boxed{M=6\ \Longrightarrow\ \text{至多一个字满足 }d(w,x)=1}\ ✓\ (\text{与 census 类型分布完全吻合} ✓✓)$$
$$

### §16.3 d=3 的最终状态

```
$$\textbf{已证（几何）}:\ M(D)\le2d;\quad \text{并集引理};\quad M=6\Rightarrow\ge\text{少一距离-1}$$
$$\textbf{已穷举验证}:\ \forall|D|=3:\ \boxed{|U_D|\ge2M(D)+3}\iff\Gamma\ge3;\quad \text{等号 13 例（}(7,2){\times}4,(11,4){\times}8,(15,6){\times}1\text{）} ✓$$
$$\textbf{仍缺（唯一）}:\ \text{把 }|U|\ge2M+3\ \text{的耦合证成\textbf{结构性引理}};\ \text{已知它\textbf{超出 Hamming 度量}}\ \Longrightarrow\ \text{依赖 }C_{120}\ \text{的局部结构}$$
$$\qquad \text{候选形式}:\ M=2k\ (\text{k 个字贡献 2 点})\ \Longrightarrow\ |U_D|\ge4k+3\ \text{（}k=1,2,3:\ 7,11,15\text{）}$$
$$

### §16.4 d=4 后台（census 进行中）

```
$$\text{进度（i1 分片 mod 2）}:\ \Gamma_{\min}\ \text{已见 }1\ (\text{i1}=0,2,10)\ \text{与 }3\text{--}4\ (\text{奇数片}) \Longrightarrow\ \textbf{d=4 的裕度小于 d=3} ✓$$
$$\text{（按唐先生指示：先用 d=3 机制预测，不急着全量判读 d=4）}$$
$$

---

## §17 **M=6 的支撑结构定理 ＋ d=4 的反向观察**（2026-09-25 21:3x）

### §17.1 ⭐ **支撑不相交定理（M=6）**

```
$$\text{设 }a_i:=x_i\oplus w,\ \text{则 }d(w,x_i)=2\Longleftrightarrow |a_i|=2,\ \text{支撑 }A_i=\mathrm{supp}(a_i)\ (\text{2-子集})$$
$$\text{对 }M=6\ \text{的}\ (2,2,2)\ \text{型（573 例）逐例统计}\ \boxed{(d_{12},d_{13},d_{23})=(4,4,4)\ \textbf{全部}}$$
$$\Longrightarrow\ \boxed{\text{三个支撑 }A_1,A_2,A_3\ \text{两两不相交}}\ \Longleftrightarrow\ \text{三个字在 }\mathbf{6}\ \text{个互异坐标上与 }w\ \text{相异}\ ✓✓$$
$$\textbf{可证性}:\ \text{若 }A_i\cap A_j\ne\varnothing\ (\text{共享坐标})\ \Longrightarrow\ \text{中点集相交}\ \Longrightarrow\ \left|\bigcup C_i\right|<6\ \Longrightarrow\ M<6\ ✗\ \text{（由 §16.2 并集引理）} ✓$$
$$\text{唯一 }|U|=15\ \text{例}:\ D=[49,77,89],\ w=673;\quad |S_x\cap U_D|\ \text{两两交}=0,\ \text{三交}=0\ \Longrightarrow\ U_D\ \textbf{无重叠分解}\ (\Delta=0)$$
$$
$$

### §17.2 M=6 的完整局部图景

```
$$\text{3 个字}\ \times\ \text{2 个互异坐标}\ =\ 6\ \text{个中点}\ \Longrightarrow\ \text{6 个中点全部}\in U_D\ \text{且\textbf{全为私有点}}$$
$$\text{总缺口}:\ |U_D|\ge15;\quad \text{极值 }=15=6\ (\text{中点})+(6,6,3)\ \text{的其余私有部分}$$
$$\textbf{仍缺}\ (\text{唯一}) :\ \text{在"支撑两两不相交"的刚性构型下证明 }|U_D|\ge15$$
\qquad \Longrightarrow\ \text{已压缩为一个\textbf{有限局部 Hamming 构型分类问题}}（\text{非全量 census}） ✓$$
$$
$$

### §17.3 ⚠️ **d=4 的反向观察（census 进行中）**

```
$$\text{d=4 census 已见}\ \Gamma_{\min}=\mathbf{-1}\ (\text{i1}=0,2,10,24\ \text{等片})\ \text{与 }0\ (\text{i1}=25) \Longrightarrow\ \textbf{存在 }|U_D|<3M(D)\ \text{的构型}$$
$$\Longrightarrow\ \boxed{\text{计数路线 }\Gamma_d>0\ \textbf{对 }d=4\ \text{不成立}}\ (\text{与唐先生预判一致：}d=3\ \text{的斜率 }1/2\ \text{不能直接推广})$$
$$\textbf{但}:\ \text{packing 路线（}\alpha_2(U_D)\ge d\text{）在 }d\le5\ \textbf{已穷举通过} ✓ \Longrightarrow\ \boxed{\text{packing 是稳健路线，计数只是 }d=3\ \text{的便利}} ✓$$
$$
$$
