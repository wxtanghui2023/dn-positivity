已查地图：命中（`P5-YI-and-P7-round2-hits` §5）⟹ 本档执行其 §7 之 (2) 的 `P7-2`，按 `E-38`／`AMEND-9` 出卡并过闸，不开新案
D0: 本档对象 = **`P7-2` 的 `SOURCE CARD` ＋ 七问 ＋ `AMEND-9` 闸门（`S1`–`S5` ＋ `L1`–`L4`）** ⟹ 判定 **`REJECT`**（**`AMEND-9` 首次应用**）
D1: 0（闸门档，零计算，不产生新自由度）
[REVIEW]

# **`P7-2` SOURCE CARD 与 `AMEND-9` 闸门判定：`REJECT`**

## §1 SOURCE CARD（七字段）

```
$$P:\ \text{哪些 }k\times\ell\ \text{的 }(0,1)\text{-矩阵 }F\ \text{落在 }\Theta(m^{k-1})\ \text{与}\ \Theta(m^{k})\ \text{的边界上（}\mathrm{forb}(m,F)\text{）}$$ ✓
$$X:\ F\ (\text{禁配矩阵});\quad \mathrm{Avoid}(m,F);\quad \mathrm{forb}(m,F):=\max\{\text{列数}\}$$ ✓
$$K:\ \text{综述 }EJC\ \texttt{DS20v2}\ (\text{Anstee–Sali, 2025});\ \text{专门文 }arXiv{:}2507.19336\ (\to AJC\ v95\ p307,\ 2026);\ arXiv{:}2601.04084\ (2026)$$ ✓
$$G:\ \text{"边界分类仍不完备"（原判定）}$$ ⚠️
$$A:\ A\ (\text{有限/关联结构})\ +\ D\ (\text{小参数精确核验})$$ ✓
$$N:\ \text{边界判据的新不变量／具体 }F\ \text{的精确阶}$$ ✓
$$O:\ \text{极值组合/禁配理论},\ \text{或外溢到超图 Turán 密度}$$ ✓
```

## §2 七问（`E-37` 口径）

```
$$Q1:\ \text{独立数学问题？}\quad \text{是（极值函数 }\mathrm{forb}(m,F)\text{）}$$ ✓
$$Q2:\ \text{要算什么？}\quad \mathrm{forb}(m,F)\ \text{的渐近阶与其"边界"判定}$$ ✓
$$Q3:\ \text{异常强迫出什么 OBJECT？}\quad \text{边界矩阵族}\ F\ \text{的分类}$$ ⚠️（**非"新类型对象"，是既有分类**）
$$Q4:\ \text{OBJECT 是否改名？}\quad \boxed{\textbf{是 —— 它就是 }\mathrm{forb}(m,F)\ \text{的边界分类本身}}$$ ✗
$$Q5:\ \text{第二尺度是否仍强迫？}\quad \text{该领域本身在逐 }k\ \text{推进（见 §4）}$$ ✗
$$Q6:\ \text{实验域外是否有定义？}\quad \text{有（纯组合定义）}$$ ✓
$$Q7:\ \text{何时立即 STOP？}\quad \text{若"边界在某层已被完全判定"}\ \Longrightarrow\ \textbf{本档即触发}$$ ✓
$$\textbf{结论}:\ Q4\ \text{失效（改名型）};\ Q5\ \text{失效（领域自己在推进）}\ \Longrightarrow\ \text{七问未过}$$ ✗✗
```

## §3 `AMEND-9` §1 触发信号检查

```
$$\texttt{S1}:\ \text{得到平凡/无信息上界？}\quad \text{部分（}\mathrm{forb}\ \text{型上下界已知）}$$ ⚠️
$$\texttt{S2}:\ \text{主项形如密度随机交？}\quad \text{否（是极值函数而非交集计数）}$$ ✓
$$\texttt{S3}:\ \text{余项 }\sqrt{\cdot}\ \text{型？}\quad \text{否}$$ ✓
$$\texttt{S4}:\ \text{现象可写成"某代数结构}\cap\text{某平移"？}\quad \boxed{\textbf{是 —— 极值函数 + 禁配结构 = 标准对象}}$$ ✓✓
$$\texttt{S5}:\ \text{一个参数同时控制全部观测？}\quad \text{是（}k\ \text{逐层控制阶）}$$ ✓✓
$$\Longrightarrow\ \boxed{\texttt{S4}\ \text{与}\ \texttt{S5}\ \textbf{同时触发}\ \Longrightarrow\ \text{强制进入 }L1\text{–}L4}$$ ✓✓
```

## §4 ⭐ `L1`–`L4` 文献封锁（**逐层命中**）

```
$$\textbf{L1 对象}:\ \boxed{\textbf{标准}} —— \text{禁配矩阵/极值函数是成熟领域};\ \text{综述 }EJC\ \texttt{DS20v2}\ (\text{2013 初版 }\to\ \text{2025 更新})$$ ✓✓
$$\textbf{L2 计数}:\ \text{综述逐字}:\ \boxed{\text{"This completely determines the boundary between }\Theta(m^k)\ \text{and }\Theta(m^{k-1})\text{"}}$$ ✓✓✓
$$\qquad \text{（Theorem 1.13/1.14：}k{=}3\ \text{先证[AS05][AGS97]，一般 }k\ \text{由[AF11][AFFS05]证）}\ \Longrightarrow\ \boxed{\text{该层边界\textbf{已完全判定}}}$$ ✓✓
$$\qquad \text{下一层（}\Theta(m^{k-1})\leftrightarrow\Theta(m^{k-2})\text{）由 }\textbf{Conjecture 3.2}\ (\text{Anstee–Sali})\ \text{支配（预测矩阵见 Theorem 9.3）—— \textbf{该领域自己正在做}}$$ ✓
$$\textbf{L3 方法}:\ \text{极值集合论/矩阵法};\quad \boxed{\text{硬事实}:\ \text{"Finding the number predicted by the Anstee–Sali conjecture is }\textbf{NP-hard}"\ (arXiv{:}1210.8189)}$$ ✓✓✓
$$\qquad \Longrightarrow\ \textbf{我方 }D\ (\text{精确小参数核验})\ \text{在一般情形被\textbf{结构性阻塞}}$$ ✗✗
$$\textbf{L4 特殊化}:\ \text{小 }k\ \text{精确界正是 }arXiv{:}2507.19336\ (\text{"four extremal configurations"})\ \text{与 }arXiv{:}2601.04084\ \text{正在收割的区}$$ ✓✓
$$\qquad \text{（另有 "Conjecture predicts nine 5-rowed simple matrices }F\ \text{which are boundary cases"）}$$ ✓
$$\Longrightarrow\ \boxed{\text{L1 标准};\ L2\ \text{本层已完全判定};\ L3\ \textbf{NP-hard 阻塞我方 }D;\ L4\ \text{活跃收割}}$$ ✓✓✓
```

## §5 判定

```
$$\boxed{\texttt{P7-2} = \textbf{REJECT}}$$ ✓✓✓
$$\text{理由（三条，皆独立充分）}:\ (1)\ \textbf{对象标准且本层边界已完全判定};\ (2)\ \textbf{本领域自己在逐 }k\ \text{收割（2025–2026 专文）};\ (3)\ \boxed{\textbf{Anstee–Sali 预测数计算 NP-hard} \Longrightarrow \text{我方 }D\ \text{资产失效}}$$ ✓✓✓
$$\text{与 }Gate\ 2\ \text{的关系}:\ \textbf{Gate 2（资产天然适配）失败} —— D\ \text{被 NP-hard 阻塞};\ A\ \text{是该领域自身工具，非差异优势}$$ ✓✓
$$\text{不得宣称}:\ \text{"边界分类整体已解决"}\ (\text{仅本层已判定，下一层仍属 Conjecture 3.2});\quad \text{不得重开为"换 }F\ \text{再试"}$$ ⚠️
```

## §6 指针更新（照运行规则 6）

```
$$\textbf{本条状态}:\ \texttt{P7-2}\ \to\ \textbf{REJECT}（附三条理由与不得重开形态）$$ ✓
$$\textbf{清单剩余合法条目}:\ \texttt{P8}\ (\text{暂缓，等待条件已解除});\quad \texttt{P5-乙-2}\ (\text{coset 余维数});\quad \texttt{P5-乙-3}\ (\text{能量失配});\quad \texttt{P6}\ (\text{仅 failure-mechanism})$$ ✓
$$\boxed{\textbf{下一动作}:\ \text{由唐先生指定唯一活跃条目（三选一）}\ \Longrightarrow\ \text{再出 }SOURCE\ CARD\ +\ \text{七问}\ +\ \texttt{AMEND-9}\ \text{闸门（零计算）}}$$ ✓（**方向选择权保留给唐先生**）
$$\text{注}:\ \text{规则 1（同时仅一条活跃）仍生效};\ \text{本档未指定活跃条目 ⟹ 指针待填（已标明）}$$ ✓
```

## §7 `AMEND-9` 首次应用记录（制度验证）

```
$$\textbf{成本}:\ 2\ \text{轮检索（零计算）};\qquad \textbf{节省}:\ \text{若照旧流程，本项将进入 }L\text{-级机制开发}（\text{参考 }CAP\text{-MIX}\approx\text{十余档}）$$ ✓✓
$$\Longrightarrow\ \boxed{\text{制度有效}:\ \texttt{S4}+\texttt{S5}\ \text{触发}\to L1\text{–}L4\ \text{三步内即判 REJECT}}$$ ✓✓
$$\text{关键杀伤点}:\ L3\ \text{的 NP-hard 事实（}arXiv{:}1210.8189\text{）—— \textbf{这是 }Gate\ 2\ \text{的硬证据，而非"看起来有用"}}$$ ✓✓
【⛔ 纪律】 本轮**零计算、零实现**；`U_{2,3}` 暂停；**不回 RH**；`T-1` 仅作 calibration ✓
【数据】 无（纯文献闸门）；引文来源为外部检索（**档级，未逐字核原文 PDF**）⚠️
【边界】 §1/§2 为出卡；§3/§4 为**外部检索证据（文档级）**；§5 为**闸门判定**；§6 指针待唐先生指定 ✓

## §附 【技术词回查】（补录）
```
技术词 forbidden configuration 命中文件数=4    :: ./CAPMIX1A-I-vs-truth-sound-but-incomplete.md ./WHERE-CAN-NEW-MECHANISM-APPEAR-survey.md ./P5-YI-and-P7-round2-hits.md 
技术词 boundary         命中文件数=168  :: ./C3880-standalone-paper-packaging-of-the-cone-separation-assets.md ./grh-goldbach-paper-draft-v2.md ./p47-g2-gluing-defect.md 
```
