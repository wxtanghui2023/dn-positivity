已查地图：已跑 scripts/prework_map_check.sh d₁ 匹配性 n=2^m 猜想 ⟹ 执行自 `YIP-2026-09-27-full-pool-...`（✓）＋ 唐先生 12:49（(甲) 优先 ✓）；本档 = **(甲) 渠道穷尽 ＋ 代数路线首个清晰猜想** ✓。
D0: 本档对象 = $(8,32)_1$ 代表的可得性；以及 $d_1\le1$ 的结构性猜想
D1: 1（新增：**结构对照表 ✓**；**匹配性猜想（n=2^m 型）✓**）

# (甲) 渠道穷尽 ＋ 匹配性猜想（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BI-1 (甲) 公开渠道穷尽 ✗)}\ 10\ \text{个 }(8,32)_1\ \text{代表：\textbf{无公开来源}} ✗}$$
$$\qquad\text{已核}:\ \text{Kéri 库（仅 1 码 }\&\text{ 无 }\_classif ✗）};\ \text{Östergård 页（仅 }(8,2,12)\ \text{的 277 码 ✗）};\ \texttt{\textasciitilde pat/codes/}\ \text{（仅 rate-1/2 ✗）};\ \text{2000/2018 论文（付费 ✗，无免费 supplementary ✗）};\ \texttt{tcs.hut.fi/\textasciitilde pat/}\ \text{（已废 ✗）}$$
$$\qquad\Longrightarrow\ \text{唯一解}:\ \text{唐先生提供 2018 PDF（机构访问 ✓）或原代表表 ✓};\ \text{否则 (甲) 阻塞 ⚠️}$$
$$\boxed{\textbf{(BI-2 ⭐ 匹配性猜想（新 ✓）)}\ \text{对 }\textbf{最优 }(n,1)\ \text{覆盖码，若 }n=2^m,\ \text{则 distance-1 图是\textbf{匹配}（}d_1(c)\le1\ \forall c\ ✓\text{）}}$$
$$\qquad\textbf{支持} ✓:\ n=8\ \text{两码}\ d_1^{\max}=1\ \text{（}J_3=0\ ✓✓\text{）};\qquad \textbf{反例侧} ✓:\ n=6\ \text{的 }K\_6\_1\#1\ (d_1^{\max}=2,\ J_3=4)\ ✗;\ n=9\ \text{两码}\ (d_1^{\max}=3,\ J_3=6/117)\ ✗$$
$$\qquad\Longrightarrow\ \text{与档案在 }Q=1\ \text{情形已证的 matching 定理\textbf{同型}} ✓✓\ \text{—— 可作一般化靶点 ✓}$$
$$
$$
```

---

## §1 结构对照表（**✓ 本机，决定性 ✓**）

```
$$\begin{array}{c|c|c|c|c|c|c|c}
\text{码} & n & |C| & A_1 & A_2 & d_1^{\max} & d_1\ \text{分布} & J_3\\
\hline
\text{Kéri }K\_8\_1 & 8\ (=2^3) & 32 & 8 & 8 & \mathbf 1 & \{0{:}16,\ 1{:}16\} & \mathbf 0\\
H(7,4)\times\mathbb F_2 & 8\ (=2^3) & 32 & 16 & 0 & \mathbf 1 & \{1{:}32\} & \mathbf 0\\
K\_6\_1\ \#0 & 6 & 12 & 0 & 12 & 0 & \{0{:}12\} & 0\\
K\_6\_1\ \#1 & 6 & 12 & 4 & 8 & \mathbf 2 & \{0{:}6,1{:}4,2{:}2\} & \mathbf 4\\
K\_9\_1\ \#0 & 9 & 62 & 7 & 66 & \mathbf 3 & \{0{:}52,1{:}8,3{:}2\} & \mathbf 6\\
K\_9\_1\ \#1 & 9 & 62 & 26 & 47 & \mathbf 3 & \{0{:}30,1{:}19,2{:}6,3{:}7\} & \mathbf{117}\\
K\_7\_2\ \#0 & 7,\ R{=}2 & 7 & 2 & 2 & 2 & \{0{:}4,1{:}2,2{:}1\} & 1\\
K\_9\_2\ \#0/\#1 & 9 & 16 & 0 & 0 & 0 & \{0{:}16\} & 0\\
\end{array}$$
$$\textbf{判读 ✓}:\ \text{恰好 }n=2^m\ (\text{仅 }n=8\ ✓)\ \text{的两码满足 }d_1^{\max}=1\ ✓;\ \text{而 }n=6,9\ \text{均失效} ✗$$
$$\qquad\text{（}n=7\ \text{行是 }R{=}2\ \text{码，不可比 ⚠️，仅作对照 ✓）}$$
$$
$$
```

---

## §2 猜想的技术表述与已知边界（**✓**）

```
$$\boxed{\textbf{猜想 }(M_1):\ C\subseteq\mathbb F_2^n\ \text{最优}\ (n,1)\ \text{覆盖码},\ n=2^m\ \Longrightarrow\ \text{distance-1 图是匹配}\ ✓}$$
$$\text{已知支持} ✓:\ n=2\ (\text{平凡 ✓}),\ n=4\ (\text{待核 ⚠️}),\ n=8\ (\text{两码 ✓✓});\ \text{档案 }Q=1\ \text{情形（n=10）已证 matching} ✓$$
$$\text{已知反例/失效} ✗:\ n=6\ (d_1^{\max}=2),\ n=9\ (d_1^{\max}=3),\ n=10\ \text{非 }Q{=}1\ \text{情形（待核 ⚠️）}$$
$$\text{若 }(M_1)\ \text{成立} \Longrightarrow\ m\equiv0\ \Longrightarrow\ J_3=J_6=0,\ \sum_ic_i^2\ \text{由 }A_1\ \text{决定} \Longrightarrow \textbf{J 的 support-2 层在 }n=2^m\ \text{处\textbf{整体退化}} ✓✓$$
$$\qquad\text{—— 这将\textbf{解释}为何现有 }n=8\ \text{两码 J 相同 ✓，并\textbf{预测}其余 9 类亦同桶同 J ✓（若 }(M_1)\ \text{真 ✓）}$$
$$
$$
```

---

## §3 下一步（**两选项 ＋ 判据 ✓**）

```
$$\text{(甲) 唐先生提供 2018 PDF 或 }(8,32)_1\ \text{原代表表} \Longrightarrow \text{第一次真正的\textbf{非空洞} P1-2 判定} ✓✓$$
$$\qquad\text{判据}:\ \exists C\ne C':\ (A_1,A_2)\ \text{同}\ \wedge\ J\ne J'\ \Longrightarrow\ \textbf{P1-2 PASS} ✓;\ \text{否则转 }(M_1)\ \text{证明} ✓$$
$$\text{(M₁) 证明路线（无需新数据 ✓）}:\ \text{从 }n=2^m\ \text{的 van Wee 取等 ＋ nearly-perfect 结构出发};\ \text{核心引理候选}:\ d(c,c')=2\ \Longrightarrow\ \text{公共邻居数}\le1\ ✓$$
$$\qquad\text{（即：}n=2^m\ \text{时不存在"三点 V 形"}\ ✓\ \text{—— 与 }n=9\ \text{的失效对照 ✓）}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为本机计算 ✓（10 码对照 ✓）；§2–§3 为**猜想 ＋ 路线** ✓（未证 ⚠️）
- **未**声称 $(M_1)$ 成立 ✗（2 码支持 ＋ 2 处失效 ✓，非证明 ✗）；**未**改动 119 UNKNOWN ✓；**未**碰 $n=10$ 计算 ✓
- ⚠️ $(M_1)$ 若真 ⟹ 反面含义：**support-2 层在 }n=2^m\ \text{处是"伪自由度"** ✓（这本身是有价值的结构性结论 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$(8,32)_1$ 渠道穷尽清单、匹配性猜想 $(M_1)$、结构对照表
- **档案已有（引用，不列为提出）**：matching 定理、van Wee 取等、nearly-perfect、$d_1$、$J_3$、separation pair


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 匹配性猜想  命中文件数=1    :: ./ALG-2026-09-27-matching-conjecture-for-n-2m.md 
技术词 结构对照表  命中文件数=1    :: ./ALG-2026-09-27-matching-conjecture-for-n-2m.md
```
- **本档新增**：$(8,32)_1$ 渠道穷尽清单、匹配性猜想 $(M_1)$、结构对照表（见上方命中数；0 命中者为自造语／内部标签 ✓）
