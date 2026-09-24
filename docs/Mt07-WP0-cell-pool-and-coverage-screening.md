已查地图：命中（`CANDIDATE-CENSUS-v1` §8 ＋ `M03-P2-SNIEP-FINAL-STAGE-REPORT`）⟹ `Mt07` WP0（格池＋覆盖筛查），不开新案
D0: 本档对象 = **`Mt07` 身份澄清（无外部 spec，源于本仓 census F11 行）** ＋ **候选格池（10 项）** ＋ **三列覆盖表** ＋ **族字面检索记录** ＋ 证明链 `L0`–`L5` ＋ 挑战项/失败机制 ＋ 工作计划 `WP0`–`WP7`
D1: 0（选格＋审计型，无数学推导）
[REVIEW]

# **`Mt07` WP0：候选格池与覆盖筛查**

## §0 身份澄清（重要）

```
$$\boxed{\text{`Mt07` 不存在"外部原始 spec"可贴}}$$ ✓
$$\quad \text{其唯一来源} = \text{本仓 } \texttt{docs/CANDIDATE-CENSUS-v1.md} \text{ 第 145 行（F11 族，AMEND-15 候选工厂产出）}:$$
$$\qquad \texttt{Mt07 **Ramsey 型小参数**未收割格 — U};\quad \text{（Batch-4 中记为 }P_4\text{，形态 } \texttt{EV}\text{）}$$
$$\quad \Longrightarrow\ \textbf{其身份本就是"选格任务"（cell-hunting），不是已冻结对象} \Longrightarrow \text{WP0 必须由我方构造格池}$$ ✓✓
$$\text{（若先生另有外部来源的 }Mt07\ \text{原文，请贴出，我会立即并入本档）}$$ ✓
```

## §1 候选格池（`10` 项；`t`=目标量，`rec`=当前记录）

```
$$\begin{array}{c|l|l|l}
\#& (\mathcal C,\ s,t) & \text{目标量} & \text{当前记录（档级）}\\\hline
K1& \text{三色小图 Ramsey}\ R_3(G),\ G\ \text{含 6 边} & \text{恰值} & \text{DS1.18：}\textbf{尚余 10 个未定格}\ \texttt{[YY]}\\
K2& R(3,3,k) & \text{恰值} & 60<R(3,3,6)?;\ R(3,3,5)=42;\ \text{（}R(3,3,3)=17,R(3,3,4)=30\text{）}\\
K3& R(3,3,3,3) & \text{恰值} & 51\le a(4)\le62\ (\textbf{著名})\\
K4& R(3,k),\ k\ge10 & \text{恰值/界} & R(3,10)\le42,\ R(3,11)\le50,\ R(3,13)\le68,\ R(3,14)\le77\ \text{（活跃改进）}\\
K5& \text{induced-regular：}N_{\ge k} & \text{恰值} & N_{\ge5}=17;\ \textbf{仅下界 }N_{\ge6}\ge21,\ N_{\ge7}\ge30\\
K6& \text{induced-regular（恰 }k\text{）：}N_k & \text{恰值} & N_5=21;\ \textbf{仅下界 }N_6\ge28,\ N_7\ge71\\
K7& \text{size-Ramsey 小图} & \text{恰值} & \text{小阶图有零散恰值；大参数为主}\\
K8& R(C_4,K_n) & \text{恰值} & R(C_4,K_9)=30,\ R(C_4,K_{10})=36\ (\text{已被收割})\\
K9& R(B_m,B_n)\ \text{（书图）} & \text{恰值} & \text{DS1 Table IXb 已由 srg 给出大量恰值}\\
K10& R(W_m,W_n)\ \text{（轮图）} & \text{恰值} & R(W_3,W_n)=2n-1\ \text{已知；下界族已知}
\end{array}$$ ✓✓
```

## §2 ⭐ 三列覆盖表（对 `K1/K2/K5/K6` 四强候选）

```
$$\begin{array}{c|l|l|l}
\text{格}&\text{① 现有论文（同格/同参数）}&\text{② 充要条件/既有定理覆盖？}&\text{③ 等价参数化是否已研究}\\\hline
K1& \textbf{是}:\ \text{Radziszowski DS1.18 (2026-04-24) 系统列表，明确列出"余 10 格"}&\text{部分}:\ \text{已有大量 }R_3(G)\ \text{恰值；余格无定理}&\text{是}:\ \text{三色 Ramsey＝超图/着色等价表述已被体系化}\\
K2& \textbf{是，且极热}:\ \text{2026 年 OpenAI AI 生成证明突破多重色三角 Ramsey 的超指数增长；"Lower Bounds for }R(3,\dots,3)\text{" 收入《Ten Advances in Math \& TCS》(2026-08)}&\text{渐近层面刚被突破；}\textbf{恰值层面仍开}&\text{是}:\ \text{Shannon capacity（独立数 2 图）等价联系已建立}\\
K5& \textbf{是，且有专文}:\ \text{arXiv:2604.08215（Dyson 2026）“Ramsey numbers for regular induced subgraphs”；McKay–Dyson 数据页}&\text{部分}:\ \text{已有恰值 }\le17\ \text{与下界}\ N_{\ge6}\ge21,N_{\ge7}\ge30&\text{是}:\ \text{与 induced size-Ramsey、nearly-regular induced subgraph 文献同域}\\
K6& \text{同上（同一专文覆盖恰 }k\ \text{版本）}&\text{部分}:\ N_5=21,\ N_6\ge28,\ N_7\ge71&\text{同上}\\
\end{array}$$ ✓✓
```

## §3 族字面检索记录（`AMEND-20` 要求）

```
$$\begin{array}{c|l|l}
\text{查询式}&\text{命中}&\text{覆盖判定}\\\hline
\texttt{size Ramsey number small graphs exact values open cases table survey 2025}&\text{DS1.18(2026)；Faudree–Sheehan 小阶图；R(C_4,K_9/K_10) 计算文}&\textbf{部分覆盖（K7/K8）}\\
\texttt{multicolor Ramsey R(3,3,k) exact values R(3,3,5) R(3,3,6) table Radziszowski}&\text{DS1.18；Codish et al.（R(3,3,4)=30）；Temple 论文（R(3,3,6)>60）；arXiv:2509.03784}&\textbf{覆盖（K2 活跃；恰值仍开）}\\
\texttt{smallest n every graph contains regular induced subgraph k vertices}&\text{McKay–Dyson 数据页；}\textbf{arXiv:2604.08215 (Dyson 2026)}&\textbf{覆盖（K5/K6 有专文）}\\
\texttt{R(3,3,6) bounds 2026 best known lower upper}&\text{MathWorld（2026 OpenAI 证明；《Ten Advances》Ch.9）；Conlon 2021}&\textbf{覆盖且热（K3/K2）}\\
\end{array}$$ ✓✓
```

## §4 筛查结论

```
$$\boxed{\textbf{KILL（已覆盖/过熟）}}:\ K8\ (R(C_4,K_n)\ \text{已收割});\ K9/K10\ (\text{DS1 表已大量恰值});\ K3\ (\text{著名});\ K2\ (\textbf{2026 AI 突破＋《Ten Advances》收录＝前沿热点})$$ ✓✓
$$\boxed{\textbf{HOLD（有专文，须读原文判"是否只剩已列格"）}}:\ K5,\ K6\ (\text{Dyson 2026 专文})$$ ⚠️
$$\boxed{\textbf{CANDIDATE（唯一"有限未定清单"结构）}}:\ \boxed{K1}=\ R_3(G)\ \text{对含 6 边图尚余 10 个未定格}\ (\texttt{[YY]},\ \text{DS1.18 列表})$$ ✓✓
$$\text{理由}:\ \text{① 它是}\textbf{有限、已列举}的未定格清单（非"未知区域"）；② 每格是}\textbf{恰值判定}（证书型：下界＝显式着色；上界＝穷举/SAT）；$$
$$\qquad \text{③ 非著名（不像 }R(5,5)\text{）；④ 与 }C07\ \text{线同型（"表缺口＋机器证书"），我方有成熟工具链。}$$ ✓✓
```

## §5 证明链分解（`L0`–`L5`，先生指定格式）

```
$$L0\ \text{对象身份}:\ (s,t,\mathcal C)=(\text{6 边图 }G,\ 3\ \text{色},\ G)\ \text{—— 待从 DS1 原文取具体 10 图};\ \textbf{状态: 待定义（须读 DS1.18 表）}$$
$$L1\ \text{已有结果层}:\ \textbf{已有成果}:\ R_3(G)\ \text{对 }\le4\ \text{边全定};\ 5\ \text{边全定（}R_3(K_4-e)=28\text{）};\ 6\ \text{边余 10 格};\ \text{相关下界构造法（群轨道）}$$
$$L2\ \text{可证项}:\ (a)\ \text{下界}:\ \text{显式三色着色（群轨道/循环着色）}\Rightarrow\ \text{可枚举＋可验证（我方 }D\ \text{资产）};\ $$
$$\qquad (b)\ \text{上界}:\ \text{穷举/SAT/ILP 排除（对称性约化＋图同构拒绝）};\ (c)\ \text{若某格恰值闭合}\Rightarrow\ \text{证书型结果}$$
$$L3\ \text{挑战项}:\ C1\ \text{上界搜索空间（}N\sim O(50\text{–}100)\text{，需对称性/局部引理约化）};\ C2\ \text{极值构造分类（达到下界的着色唯一性）};\ C3\ \textbf{新不变量}:\ \text{FORBID }K_3\ \text{的局部—全局约束是否产生新计数不变量（区别于三色 Ramsey 的既有群轨道不变量）}$$
$$L4\ \text{失败机制}:\ F1\ \text{局部量不足（两图同局部统计不同结果）};\ F2\ \text{边界非刚性（多构型）};\ F3\ \text{等价已知（}\Phi=\Phi_{\text{known}}\text{）}\Rightarrow\ \text{立即归档}$$
$$L5\ \text{推广性}:\ \text{6 边}\to7\ \text{边图};\ 3\ \text{色}\to4\ \text{色};\ \text{判"机制是否具推广自由度"}$$
```

## §6 工作计划（`WP0`–`WP7`，含硬停止点）

```
$$\begin{array}{c|l|l|c}
\text{WP}&\text{内容}&\text{进入条件}&\text{产出}\\\hline
WP0&\text{冻结 }(s,t,\mathcal C)&\text{现在（本档）}&\text{格池＋筛查表}\ \checkmark\\
WP1&\text{精确文献检索（读 DS1.18 原文，取 10 图清单）}&WP0&\text{三列 Coverage Table（原文级）}\\
WP2&\text{等价参数化检索}（超图/着色/覆盖/编码语言）&WP1&\text{等价对象族}\\
WP3&\text{已有 theorem 分解}&WP2&\text{Known / Provable / Open}\\
WP4&\text{小参数 census（下界着色枚举）}&Gate\ 0\ \text{PASS}&\text{极小解/反例}\\
WP5&\text{新不变量/边界机制}&WP4&\text{候选 lemma}\\
WP6&\text{证明链闭合}&WP5&\text{theorem / CLOSED}\\
WP7&\text{推广}&WP6&\text{新族/新资产}
\end{array}$$ ✓✓
$$\boxed{\text{硬停止点}:\ WP1/WP2\ \text{发现覆盖}\Rightarrow CLOSED;\quad WP4\ \text{发现已有分类}\Rightarrow ARCHIVE;\quad WP5\ \text{新量可由旧量表达}\Rightarrow CLOSED}$$ ✓✓
```

## §7 下一步（单点）

```
$$\boxed{\text{① 取 DS1.18（2026-04-24）原文}，从表/文本中抽出"6 边图 3 色 Ramsey 尚余 10 格"的}\textbf{具体 10 个图}$$ ✓
$$\boxed{\text{② 对每格做第二次 Gate 0（同格＋充要条件＋等价参数化）}};\ \text{仅存活者冻结}$$
$$\text{（若 10 格全部已在其它文献闭合或属"已列但正在被收割"}\Rightarrow\ K1\ \text{亦 KILL，则 }Mt07\ \text{整项回到"无可用格"并如实登记）}$$ ✓✓
【⛔ 纪律】 本轮**零数学计算**；`U_{2,3}` 暂停；**不回 RH**；**未读原文处标注为档级/摘要级** ✓
【边界】 `K1` 的"尚余 10 格"来自 DS1 摘要片段；**须原文确认**；`K5/K6` 的专文内容未读 ⟹ 仅标 HOLD ✓

## §附 【技术词回查】（补录）
```
技术词 cell pool        命中文件数=0    :: 
技术词 coverage table   命中文件数=0    :: 
```
