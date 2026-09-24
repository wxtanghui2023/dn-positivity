已查地图：命中（`Mt07-WP0-cell-pool-and-coverage-screening`）⟹ `Mt07-G0` 双格竞争，不开新案
D0: 本档对象 = **`DS1.18` 原文抽取（`R(C_4,K_{1,n})` 与 `R(3,10)`）** ＋ **双格竞争 Gate 0 十一项表** ＋ **两格同灭风险判定** ＋ 新判据（"开放≠值得做"）的结论 ＋ 下一步
D1: 0（审计型，无数学推导）
[REVIEW]

# **`Mt07-G0`：双格竞争**

## §0 `DS1.18` 原文抽取（来自 tavily 抽取，**非逐字核验**）

```
$$\textbf{DS1 定位}:\ \text{Radziszowski, \textit{Small Ramsey Numbers}, EJC Dynamic Survey } \texttt{DS1.18}\ (\textbf{2026-04-24}),\ 149\ \text{页};\ \text{PDF}:\ \texttt{cs.rit.edu/\textasciitilde spr/ElJC/ejcram18.pdf}$$ ✓（引用级）
$$\textbf{关键条目（逐字抽取）}:$$
$$\qquad \text{(c)}\ R(C_4,K_{1,n})=R(C_4,W_{n+1})\ (n\ge6)\ [\texttt{ZhaBC1}];\qquad \text{(e)}\ \text{同（}n\ge7\text{）};\quad \text{(f)}\ \text{紧界 }R(C_4,W_n)\ (46\le n\le93)\ [\texttt{NoBa}]$$
$$\qquad \boxed{\text{(d)}\ \text{对一切奇素数幂 }q:\ q^2+1\le R(C_4,K_{1,q^2-q+1})\le q^2+2\le R(C_4,K_{1,q^2-q+2})\le q^2+3}$$ ✓✓✓
$$\qquad \textbf{2025 综述}:\ \text{“an extensive summary of results involving }C_4\text{, and in particular on }R(C_4,K_{1,n})\text{, was published in }[\texttt{ChenZZ7}]\text{”}$$ ✓✓
$$\textbf{关于 }R(3,k):\ \text{#544 报告引 DS1.18 §2.3(e)}:\ \text{仅有“easy pointwise bounds”};\ R(3,3)\dots R(3,9)=6,9,14,18,23,28,36;\ \boxed{40\le R(3,10)\le41}$$ ✓✓
```

## §1 ⭐ 双格竞争 Gate 0（先生指定十一项）

```
$$\begin{array}{c|l|l}
\text{项} & G_A=R(C_4,K_{1,n})\ (\text{取 }n=39,51;\ \text{族 (d)}) & G_B=R(3,10)\\\hline
\text{① DS1.18 状态} & \textbf{BOUND}:\ \text{(d) 给出一族 1-单位缺口};\ 46\le n\le93\ \text{为紧界} & \textbf{BOUND}:\ 40\le R(3,10)\le41\\
\text{② 最新原始论文} & \text{Boza }\texttt{arXiv:2409.12770v2}\ (2026);\ \text{Wu–Sun–Zhang–Radziszowski (2015)} & \text{Goedgebeur–Radziszowski }\texttt{arXiv:1210.5826};\ \text{Zhu–Xu–Radziszowski (2016)}\\
\text{③ 2026 preprint} & \boxed{\text{有，且正解两格}}:\ \texttt{github/zach7036/c4-star-ramsey}\ (\textbf{AI 生成},\ \textbf{未同行评审},\ \text{人类审阅尚未发生}) & \text{OpenAI/其它 2026 比值论文（}R(k,\ell+1)/R(k,\ell)\ \text{相对界}）；\ \text{未直接定 }R(3,10)\\
\text{④ 当前上界} & R(C_4,K_{1,q^2-q+1})\le q^2+2;\ R(C_4,K_{1,q^2-q+2})\le q^2+3 & R(3,10)\le41\\
\text{⑤ 当前下界} & q^2+1\ (\text{同族}) & R(3,10)\ge40\\
\text{⑥ 是否 1-unit gap} & \boxed{\text{是}}（(d) 两族皆 1 单位） & \boxed{\text{是}}\\
\text{⑦ 等价问题} & \boxed{\text{存在 }C_4\text{-free 图／正则 }C_4\text{-free 图（}f(n)\text{ 型）}} & \text{存在 40 顶点无三角且 }\alpha\le9\ \text{的图}\\
\text{⑧ 已知构造} & \text{极性图 }\mathrm{PG}(2,q)\ (\text{下界主力});\ \text{仓库给出 }45\ \text{顶点 }\delta=6、58\ \text{顶点 }\delta=7\ \text{证书} & R(3,9)\ \text{临界图唯一}:\ \mathbb Z/35\ \text{上 }\ 8\text{-正则循环图，距离集 }\{1,7,11,16\}\\
\text{⑨ 已有非存在证明} & \text{SAT/ILP};\ \textbf{仓库称"第五矩为决定性约束"（}\text{Theorem 1}\text{）} & \text{长期 SAT/穷举};\ \text{点态下界 }3\le\Delta_s\le s\\
\text{⑩ 我们可攻击缺口} & \textbf{矩/谱约束路线}（第五矩型）—— \textbf{须先查其是否已在文献} & \text{同一 40 顶点存在性（规模巨大）}\\
\text{⑪ 重复投资风险} & \boxed{\textbf{HIGH}}（2025 综述＋2026 Boza＋2026 AI 仓库正解） & \boxed{\textbf{HIGH}}（经典最密集战场）\\
\end{array}$$ ✓✓✓
```

## §2 ⚠️ 依先生新判据（"开放 ≠ 值得做"）的判定

```
$$\text{新判据}:\ \boxed{\text{开放}+\text{缺口结构简单}+\text{已有证明链存在可插入新环节}}$$
$$G_A:\ \text{缺口}=R\in\{N,N+1\}\Longrightarrow\textbf{已压缩为"C₄-free 图存在性"}\ \text{（}f(n)\ \text{型）}\Longrightarrow\ \text{剩余是}\textbf{有限存在性问题}$$ ⚠️
$$\qquad \text{若其唯一剩余手段是 SAT 穷举已知图类}\Longrightarrow\ \textbf{不适合我们}\ (\text{先生原话});\quad \text{但}\ \text{⑨ 提示}\ \textbf{矩/谱约束}\ \text{或为新环节}$$ ✓
$$G_B:\ \text{缺口}=\text{"40 顶点无三角 }\alpha\le9\ \text{存在性"}\Longrightarrow\ \textbf{纯有限搜索（规模巨大）}\Longrightarrow\ \text{不适合}$$ ✗
$$\textbf{共同结论}:\ \boxed{\text{两格均已压缩成"已知图类的有限存在性"}};\ \text{且重复风险}\ HIGH;\ \text{差异仅在于 }G_A\ \text{有"矩约束"这一潜在新环节}$$ ✓✓
```

## §3 逐条核验先生所给两来源

```
$$\textbf{(1) GitHub }\texttt{zach7036/c4-star-ramsey}:\ \text{标题“Candidate resolutions of }R(C_4,K_{1,39})\ \text{and}\ R(C_4,K_{1,51})\text{, with exact verification artifacts”};$$
$$\qquad \text{自述：由 AI（Claude；一步用 GPT-5.6）在仓库主人指导下完成，}\textbf{双重独立推导/机器检验};\ \textbf{人类数学审阅尚未发生};\ 0\ \text{星};\ \text{MIT};$$
$$\qquad \text{工件：}\texttt{lower\_bound\_45.json}\ (45\ \text{顶点},\ \delta=6,\ C_4\text{-free}\Rightarrow f(39)\ge46,\ \text{来自 }\mathrm{PG}(2,7)\ \text{极性图});\ \texttt{lower\_bound\_58.json}\ (\Rightarrow f(51)\ge59);$$
$$\qquad \text{参考文献}:\ \text{Boza }\texttt{arXiv:2409.12770v2}(2026);\ \text{DS1.18};\ \text{Parsons(1975)};\ \text{Wu–Sun–Zhang–Radziszowski(2015)};\ \text{Zhang–Broersma–Chen(2014)};\ \text{Zhang–Chen–Cheng(2017)};\ \text{Goryainov et al. }\texttt{arXiv:2103.00228}.$$
$$\qquad \Longrightarrow\ \textbf{判定}:\ \text{该仓库}\textbf{不构成已确立文献结果}，但证明}\ \boxed{\text{该格正被独立（AI）攻击}} \Longrightarrow\ \text{重复投资风险}\ HIGH$$ ✓✓
$$\textbf{(2) }\texttt{erdosproblemaday.com/report/544}:\ \text{#544 本体是}\ \textbf{Erdős–Sós 型渐近问题}\ (R(3,k+1)-R(3,k)\to\infty\ \text{及}\ =o(k)?),\ \text{状态 OPEN};$$
$$\qquad \text{该报告明确用于我方的关键数据}:\ \boxed{40\le R(3,10)\le41}\ (\text{引 DS1.18 §2.3(e)});\ R(3,9)\ \text{临界图唯一且为循环图};$$
$$\qquad \Longrightarrow\ \textbf{判定}:\ \text{#544 本身}\textbf{不是格}\（渐近问题）；其用作 }R(3,10)\ \text{当前界的数据源}$$ ✓
```

## §4 结论与下一步（单点）

```
$$\boxed{\textbf{本轮 Gate 0 判定}:\ G_A\ \text{与}\ G_B\ \textbf{均不冻结}}$$ ✓✓
$$\text{理由}:\ \text{① 两者都已压缩成“已知图类上的有限存在性问题”（先生新判据的排除型）；② 重复风险皆 HIGH；}$$
$$\qquad \text{③ }G_A\ \text{唯一潜在新环节}=\textbf{矩/谱约束}（仓库所称“第五矩”），}\textbf{但其文献归属未核}$$ ✓✓
$$\textbf{下一步（唯一）}:\ \boxed{\text{核查“矩/谱约束路线”是否已在文献}}:\ \text{查 Boza 2026（} \texttt{arXiv:2409.12770v2}\text{）、Zhang–Chen–Cheng 系列、Wu–Sun–Zhang–Radziszowski};\ $$
$$\qquad \text{若已覆盖}\Longrightarrow\ G_A\ \text{亦 KILL}\Longrightarrow\boxed{Mt07\ \text{整项登记为“无可用格”}};\quad \text{若未覆盖}\Longrightarrow\ \text{冻结的应是}\textbf{该机制}（而非格）\Longrightarrow\ \text{转入 }C3\ \text{（新不变量）}$$ ✓✓✓
【⛔ 纪律】 本轮**零数学计算**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §0/§3 的证据为**抽取级**（tavily 抽取 + 仓库自述），**未逐字核验原文**；§1 表格中"仓库称第五矩"为**未评审来源**，不得作为既定结论 ✓

## §附 【技术词回查】（补录）
```
技术词 moment constraint 命中文件数=0    :: 
技术词 finite existence 命中文件数=0    :: 
```
