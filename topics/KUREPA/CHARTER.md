已查地图：见 docs/TOPIC-INDEX.md（课题分档子档 · 本档为该课题总纲领）
D0: 本档对象 = 课题总纲领与行动方案（组织性）；非数学命题，不主张任何新值
D1: 0
ASSUMES: N/A (纲领档)

# CHARTER — **KUREPA（Kurepa 猜想／左阶乘，1971）** · 总纲领＋行动方案

## §1 目标
$$\text{主目标 }K\text{-A}：\textbf{\text{部分模结果}}——\text{证"若奇素数 }p\mid !p\ \text{则 }p\equiv r\pmod m"\ \text{型受限结论（加强/扩展已知约束）}$$
$$\text{副目标 }K\text{-B}：\text{新等价重构（承 Petojević 2023 路线）};\quad \text{副目标 }K\text{-D}：\text{广义 }!^kn\ \text{之 }k\text{-结构探索}$$

## §2 证明链（**全链条，逐环节**）

| 环 | 内容 | 现状 |
|---|---|---|
| **L0** | 规范：$!n=\sum_{k=0}^{n-1}k!$；等价：$\forall n>1\ \gcd(!n,n!)=2\iff$ 无奇素数 $p\mid !p$；广义 $!^kn$ | **已知** ✓ |
| **L1** | 基本恒等式：$!(n{+}1)=!n+n!$；$!n\equiv !p \pmod p\ (n\ge p)$；Wilson 型操作（$(p{-}1)!\equiv-1$）；**周期性**（若某 $p\mid !p$ 则无穷多 $n$ 亦然） | **已知** ✓ |
| **L2** | 已知等价族（Petojević 2023，Axioms：含**连分数**连接） | **已知** ✓（文献） |
| **L3** | **已知模约束**（"若 $p\mid !p$ 则 $p\equiv r\pmod m$"型） | **待核** ⚠️（须查 Ivić–Mijajlović 1995／Kellner 2004 原文；本轮检索未取到具体 $r,m$） |
| **L4** | 算法与验证：Andrejić 2021 余数算法改进；界 $p<2^{40}$（2021）／$p<2^{34}$（GPU 2023） | **已知** ✓（**记录竞赛**） |
| **L5** | 广义：$!^kn$，$1<k<100$ 皆存在奇素数 $p\mid !^kp$（Andrejić–Tatarević） | **已知** ✓ |
| **L6** | **主猜想本体**（无奇 $p\mid !p$） | **待完成** ⏳⏳（远超） |

## §3 环节分类（已知／可证／待完成）

$$\text{已知}=L0,L1,L2,L4,L5\ (L3\ \text{待核});\quad \text{可证（预期）}=\textbf{K-A（部分模结果，低成本）};\quad \text{待完成}=L6\ (\text{本体})$$


## §2.10 **命题级验证门**（唐先生 2026-10-02 10:03 令 ✓）

$$\boxed{\text{推导中用到的\ \textbf{每一个数学命题}，在\ \textbf{作为前提使用之前}，必须先附\ \textbf{机器检验}（脚本＋输出）；未验证者标 CONJECTURED，\textbf{不得作前提}}}$$
$$\text{三档状态}：\textbf{VERIFIED-SMALL}（\text{小规模穷举，反例}=0）｜\textbf{VERIFIED-EXACT}（\text{精确计算/证书}）｜\textbf{REFUTED}（\text{有反例}）；\quad \text{台账}＝\texttt{docs/PROPOSITIONS.tsv}$$
$$\text{硬要求}：\text{任何脚本\ \textbf{先写文件 → \texttt{python3 -m py_compile} → 最小样例自检 → 再跑}};\ \text{任何"保持某不变量"之构造，\textbf{先做反例搜索}}$$
$$\text{记教训}：\text{本日 }P\text{-001（"2-switch 保 }λ\text{"）为\ \textbf{100\% 错}（36/36），\text{十行穷举即可杀死}} \Longrightarrow \textbf{\text{"先理论推导"若不带反例检验，等于没推导}}$$

## §4 **逐环节：全部思路 × 可行性**（已过 §2.7 三问）

### 环节 **L3′ ＝ K-A（部分模结果）**（待完成 ⏳ · **本课题主攻**）
| # | 思路 | 做法 | 可行性 |
|---|---|---|---|
| a | **Wilson 型化归** | 把 $!p \bmod p$ 化为更简表达式（用 $(p{-}1)!\equiv-1$、$\binom{p-1}{k}\equiv(-1)^k$ 等），再由此逼出同余约束 | **中** ✓ |
| b | **二次剩余／虚二次域类数** | 类比 $\left(\frac{p-1}{2}\right)!\equiv\pm1$ 之经典结果（Mordell 1961；$h(-p)$ 表达），对 $!p$ 求同类刻画 | **中** ✓ |
| c | **分圆域／整值多项式** | Kellner 型（左阶乘与 $K(z)=\sum k!/z^{k+1}$ 之整值性） | **中** ✓ |
| d | **模 $p$ 有限差分／组合恒等式** | 用 $!p$ 的组合表达式找模结构 | **低-中** ⚠️ |
| e | **$p$-adic 展开** | $\lvert!p\rvert_p$／$p$-adic 估值 | **低-中** ⚠️ |
| **剔除** | ~~**推高验证界**~~ | 需 **GPU** 级算力（记录 $2^{34}$–$2^{40}$） | **剔除** ✗ |

### 环节 **L5′ ＝ K-D（广义 $!^kn$ 结构）**
| # | 思路 | 可行性 |
|---|---|---|
| a | 问：对哪些 $k$ 存在 $p\mid !^kp$（已知 $1<k<100$ 皆存在）⟹ 找**反例 $k$** 或**结构性刻画** | **中** ✓ |
| b | $k$ 的模/同余分类 | **低-中** ⚠️ |

### 环节 **L2′ ＝ K-B（新等价）**
| # | 思路 | 可行性 |
|---|---|---|
| a | 承 Petojević（连分数）再寻新等价 | **中低** ⚠️（须与已有等价查重，防 §2.8 违规） |

## §5 **价值裁定**（§2.9，溯 `docs/ASSESS-2026-10-01b`）

| V1 | V2 | V3 | V4 | V5 | V6 | V7 |
|---|---|---|---|---|---|---|
| 中低 | 中（MDPI/Axioms 级可发） | **高**（逐素数可复算） | **中高**（目标明确、可增量） | 中（**无 AI 团队**）✓ | 中 | 低-中（我方 0 档⟹全新；可借证书基础设施） |

$$\Longrightarrow\ \textbf{\text{值得作"低成本·小成果"课题}};\ \text{首选 }K\text{-A} ✓$$

## §6 制度引用
$$\text{§2.5 天花板前置}｜\text{§2.6 三重前置（理论→量级→前提/可行性）}｜\text{§2.7 逻辑可杀预筛}｜\text{§2.8 已试判定前置}｜\text{§2.9 价值评估前置} — \text{皆适用} ✓$$

## §7 文档存储
$$\text{本纲领}=\texttt{topics/KUREPA/CHARTER.md}\ \checkmark;\quad \text{评估}=\texttt{docs/ASSESS-2026-10-01b-second-assessment-Lehmer-Mahler-and-Kurepa.md};\quad \text{清单}=\texttt{docs/CONJECTURES-2026-10-01-…}$$
