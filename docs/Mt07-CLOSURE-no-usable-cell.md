已查地图：命中（`Mt07-G0-dual-cell-competition`）⟹ `Mt07` 收口，不开新案
D0: 本档对象 = **`Mt07` 正式收口（"无可用格"）** ＋ **`G_A`/`G_B` 分层判定表** ＋ **措辞纪律（第五矩不做过度归属）** ＋ **Gate 0 阻断重复投资的确认** ＋ 指针更新
D1: 0（收口型，无数学推导）
[REVIEW]

# **`Mt07` 收口：无可用格**

## §0 判定（严格照先生口径）

```
$$\boxed{\text{Mt07-G0}\ \text{收口为}:\ \textbf{无可用格}}$$ ✓✓
$$\textbf{不是}:\ \text{“Ramsey 方向没有开放问题”}\ \times;\quad \textbf{而是}:\ \boxed{\text{DS1.18 筛出的两个最有希望有限缺口，均不提供符合 \textsc{amend-21} 的新机制入口}}$$ ✓✓
$$\textbf{本轮未进入任何大规模计算} \Longrightarrow \boxed{\textbf{Gate 0 成功阻断重复投资}}$$ ✓✓
```

## §1 `G_A=R(C_4,K_{1,n})`：KILL（分层理由）

```
$$\begin{array}{c|l|l}
\text{Gate} & \text{判定} & \text{证据（抽取级）}\\\hline
\text{对象是否已有系统研究} & \boxed{\text{YES}\Rightarrow\text{FAIL}} & \text{2025 综述 }[\texttt{ChenZZ7}]\ \text{是 }R(C_4,K_{1,n})\ \text{的 extensive summary};\ \text{Boza 2026（}\texttt{arXiv:2409.12770v2}\text{）研究 }f(n)=R(C_4,K_{1,n})\ \text{并解决此前 }n\le38\ \text{的八个未知值，且建立跨 }n\ \text{的函数不等式}\\
\text{等价正则 }C_4\text{-free 图问题} & \boxed{\text{YES}\Rightarrow\text{FAIL}} & \text{该族已压缩为“}C_4\text{-free 图／正则 }C_4\text{-free 图存在性”（}f(n)\ \text{型）}\\
\text{极性图／极值图路线} & \boxed{\text{YES}\Rightarrow\text{FAIL}} & \text{Wu–Sun–Zhang–Radziszowski 已把极性图、}C_4\text{-free extremal graph 与 Ramsey 上界联系；Erdős \#552 现状沿 }n=q^2\pm t\ \text{参数族系统延伸（Parsons、WSZR15、ZCC17/17b）}\\
\text{五阶矩作为具体新证书是否逐篇归属} & \boxed{\text{未完全核清}} & \textbf{不得}写成“第五矩公式已被旧论文证明”\\
\text{当前具体 }f(39),f(51) & \boxed{\text{正被独立解决}} & \text{2026 候选解仓库（AI 生成、}\textbf{未同行评审}）声称 }R(C_4,K_{1,39})=46,\ R(C_4,K_{1,51})=59\ \text{并附机器验证材料}\\
\text{是否值得投入我方新机制计算} & \boxed{\text{NO}} & \text{追的是已被另一组工作做到最后一步的具体问题}
\end{array}$$ ✓✓
$$\textbf{措辞纪律（照先生）}:\ \boxed{\text{不是说“第五矩公式已被旧论文证明”，而是说“即使该具体公式的历史归属尚未逐条核清，整个对象族及其等价图论机制已被系统研究，因此不满足我方 Gate 0 新课题条件”}}$$ ✓✓
```

## §2 `G_B=R(3,10)`：KILL

```
$$\text{对象已被压缩为}\ \boxed{R(3,10)=40\ \text{or}\ 41}\iff\text{存在 40 顶点 triangle-free 且 }\alpha\le9\ \text{的图};\ \text{即经典 Ramsey 临界图搜索}$$ ✓
$$\boxed{G_B=\text{KILL}}\ \text{—— 不是没有数学价值，而是不符合本轮“新机制优先”标准}$$ ✓✓
```

## §3 指针更新（写入 census）

```
$$\textbf{Mt07 状态}:\ \boxed{\text{CLOSED — 无可用格}};\ \text{证据档}:\ \texttt{docs/Mt07-WP0-cell-pool-and-coverage-screening.md},\ \texttt{docs/Mt07-G0-dual-cell-competition.md},\ \text{本档}$$
$$\textbf{不再}:\ \text{在 }Mt07\ \text{内找第三个 Ramsey 格（照先生令）};\quad \textbf{下一步}:\ \text{回清单}\Rightarrow\boxed{\text{C06-G0}}$$
$$\textbf{止损逻辑（照先生）}:\ \text{若 }C06\ \text{两轮内亦被覆盖}\Longrightarrow\ \textbf{不再从 Zone-A/B 随意续挑}，\text{而是回完整候选表重做“独立问题 × 新量 × 可证明性”筛选}$$ ✓✓
【⛔ 纪律】 本轮**零数学计算**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 全部证据为**抽取级**（tavily 抽取 + 仓库自述），**未逐字核验原文** ✓
