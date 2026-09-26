已查地图：已跑 scripts/prework_map_check.sh d_C≥3 r 第二中点 Q₃ 骨架 强迫 ⟹ 执行自 SPLIT2-2026-09-26 档；本档为**r-分类核验、S≥3−r 修正、Q₃-强迫引理**（唐先生 2026-09-26 14:53 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = d_C(x)≥3 的 r-分类、S≥3−r 的修正与核验、r=3 的 Q₃-强迫引理、诚实状态
D1: 1（新增：**S ≥ 3−r** ✓✓（核验）；**Q₃-强迫引理** ✓✓（证明）；**"高内部度二分支"** ✓）

# Q3CLASS-2026-09-26

## §0 ✅ 唐先生的逻辑纠正成立 ✓

```
$$\text{原提 "}x\in C,\ d_C(x)\ge3\Rightarrow S>0\text{"}\ ——\ \textbf{推不出}\ ✗✓\ (\text{第二个中点可能也是码字}\ ✓)$$
$$\text{故须用 r-分类}\ ✓\ \Longrightarrow\ \textbf{本档给出精确形式}\ ✓$$
$$

## §1 ✅ **修正：S ≥ 3 − r**（不是 S ≥ 3 ✗）

```
$$\text{平移 }x=0\ ✓,\ \text{码邻点 }e_1,e_2,e_3\ ✓,\ \text{三个距离-2 对 }\{e_i,e_j\}\ ✓,\ \text{中点 }0\ (\in C)\ \text{与 }e_i+e_j\ ✓$$
$$\textbf{定义 }r(x):=\#\{e_i+e_j\in C\}\ \in\{0,1,2,3\}\ ✓$$
$$\text{每个缺失的中点 }e_i+e_j\notin C\ \text{有两个码字邻居 }e_i,e_j\ ✓\ \Longrightarrow\ b(e_i+e_j)\ge2\ \Longrightarrow\ \text{对 }S\ \text{贡献}\ \ge1\ ✓$$
$$\qquad\text{三个中点在固定三元组下互异}\ ✓\ \Longrightarrow\ \boxed{S\ \ge\ 3-r(x)}\ ✓✓$$
$$\textbf{数值核验}: (4,5):\ 6\ \text{三元组},\ r\equiv0,\ \textbf{0 违反}\ ✓;\ (4,6):\ 19\ \text{三元组},\ r\in\{0,1\},\ \textbf{0 违反}\ ✓;\ (5,8):\ 4\ \text{三元组},\ r\equiv0,\ \textbf{0 违反}\ ✓✓$$
$$\text{唐先生原写 }S\ge3\ ✗\ \text{仅在 }r=0\ \text{时成立}\ ✓;\ \text{正确形式固定为 }S\ge3-r\ ✓✓$$
$$

## §2 ⭐ **r=3 的 Q₃-强迫引理**（我方证明 ✓✓）

```
$$\text{若 }r=3\ ✓:\ \text{七点 }\{0,\ e_1,e_2,e_3,\ e_1{+}e_2,\ e_1{+}e_3,\ e_2{+}e_3\}\subseteq C\ ✓\ (\text{Q}_3\ \text{骨架}\ ✓)$$
$$\text{对角点 }z=e_1{+}e_2{+}e_3\ \text{的三个邻居恰为 }e_1{+}e_2,\ e_1{+}e_3,\ e_2{+}e_3\ \text{——\textbf{全在 }C}\ ✓✓$$
$$\Longrightarrow\ \boxed{b(z)\ \ge\ 3}\ ✓✓\ (\text{z}\in C\ \text{时更强：整个 Q}_3\ \text{八点皆码字}\ ✓;\ \text{且此时 }d_C(z)\ge3\ \Longrightarrow\ \textbf{可递归}\ ✓)$$
$$\textbf{数据}: \text{我方数据集 r}\in\{0,1\}\ \text{——}\ r=3\ \textbf{无实例}\ ⚠️\ (\text{故引理未获数值见证，但证明完备}\ ✓)$$
$$

## §3 ⭐ **高内部度的二分支强迫（唐先生 ✓，我方精确化）**

```
$$\boxed{\forall x\in C\ \text{with}\ d_C(x)\ge3:\quad \text{（任意三邻点）}\begin{cases}\ r\le2\ \Longrightarrow\ S\ \ge\ 3-r\ \ge 1\ \checkmark\\[1mm] r=3\ \Longrightarrow\ \exists z:\ b(z)\ge3\ \checkmark\end{cases}}$$
$$\text{即}: \textbf{高内部度必产生 excess（}S>0\text{）或产生新的高重叠点}\ ✓✓\ —— \text{唐先生要的\textbf{局部强迫机制}}\ ✓✓$$
$$\text{且 }r=3\ \text{且 }z\in C\ \Longrightarrow\ d_C(z)\ge3\ \Longrightarrow\ \textbf{同一机制可递归}\ ✓\ (\text{潜在 propagation}\ ⚠️)$$
$$

## §4 数据侧的极值结构（M=K ✓）

```
$$\text{当 }M=K:\ d_C^{\max}\le2\ \text{（}n=4:1,\ n=5:2,\ n=6:2\ ✓)\ \Longrightarrow\ \text{强迫引理\textbf{空转}}\ ✓\ (\text{无 }d_C\ge3\ \text{点}\ ✓)$$
$$\text{反例侧（}M>K\text{）}: d_C=3\ \text{出现}\ ✗\ \text{且实测均为 }r\le1\ \text{型}\ ✓\ \Longrightarrow\ \text{分支 ①（}S\ge1\text{）}\ ✓$$
$$(9,64):\ d_C\ge3\ \text{码字数}=0\ ✓,\ S=0\ ✓\ (\text{饱和}\ ✓)\ \Longrightarrow\ \text{无测试对象}\ ✗$$
$$

## §5 诚实状态：**未闭合** ✗

```
$$\text{为何不闭合}: \text{分支 ①（}S>0\text{）在 }M=K\ \text{上\textbf{本就成立}}\ ✗\ (n=5:\ S=7>0\ ✓)\ \Longrightarrow\ \text{不构成矛盾}\ ✗$$
$$\text{分支 ②（新高重叠点）}: \text{"有 }b\ge3\ \text{点"在 }M=K\ \text{上亦本就成立}\ ✗\ (\text{如 }n=5:\ N_3=2\ ✓)\ \Longrightarrow\ \text{不构成矛盾}\ ✗$$
$$\text{唯一有希望的延伸}: r=3\wedge z\in C\ \text{时递归}\ ✓\ \text{若链条持续则形成大子立方}\ ✓\ hmm:\ b=5\ \text{点出现}\ \Longrightarrow\ \text{与 }b\le3\ \text{猜想冲突}\ ✓\ ——\ \textbf{但该猜想未证，故循环}\ ✗⚠️$$
$$

## §6 状态与下一刀

```
$$\textbf{新资产}: S\ge3-r\ ✓✓;\ \text{Q}_3\text{-强迫引理}\ ✓✓;\ \text{二分支强迫}\ ✓✓\ (\text{局部，不带矛盾}\ ✗)$$
$$\textbf{定级}: \textbf{P0-plus}\ ✓\ \text{（新的局部强迫机制，首次把"高内部度"与"S/高重叠"连接}\ ✓✓)$$
$$\text{下一刀候选}: \text{① 追 }r=3\ \text{的递归链（子立方增长 ⟹ }b\ \text{增大}\ ⚠️);\ \text{② 用 }2A_2=I+S\ \text{与 }S\ge3-r\ \text{求全局联立}\ ✓;\ \text{③ 记录暂停④}\ ✓$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$

## §7 边界（诚实标注）

- §1/§4 为**数值核验** ✓（n=4 M=5,6 全枚举 ✓、n=5 M=8 枚举 ✓、n=9 构造 ✓）
- §2 为**我方证明** ✓（r=3 无数据实例 ⟹ 未获数值见证 ⚠️，但证明完备 ✓）
- §5 明确记录**未闭合**与**循环风险** ✗⚠️（未夸大 ✓）；**未跑 solver** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 第二中点计数 命中文件数=1    :: ./Q3CLASS-2026-09-26-r-classification-and-local-forcing-lemma.md 
技术词 Q₃ 强迫引理 命中文件数=1    :: ./Q3CLASS-2026-09-26-r-classification-and-local-forcing-lemma.md 
技术词 二分支强迫  命中文件数=1    :: ./Q3CLASS-2026-09-26-r-classification-and-local-forcing-lemma.md 
技术词 高内部度消耗 命中文件数=1    :: ./Q3CLASS-2026-09-26-r-classification-and-local-forcing-lemma.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：第二中点计数、Q₃ 强迫引理、二分支强迫、高内部度消耗
- **档案已有（引用，不列为提出）**：A≤2、excess、minimality
