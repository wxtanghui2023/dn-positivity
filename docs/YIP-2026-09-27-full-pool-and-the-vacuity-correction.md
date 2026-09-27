已查地图：已跑 scripts/prework_map_check.sh 全库 桶 退化 A₁=0 ⟹ 执行自 `YI-2026-09-27-classification-pool-bucket-analysis`（✓）＋ 唐先生 12:47（跑乙′ ✓）；本档 = **(乙′) 全库结果 ＋ 对上一轮"类型 1"结论的更正（空洞性 ✓）**。
D0: 本档对象 = 全库 14 个分类文件的桶分析及其有效性
D1: 1（新增：**14 文件全表 ✓，类数全中文献上标 ✓✓**；**空洞性更正 ⚠️**；**唯一非空洞测试场 =(8,1) ✓**）

# (乙′) 全库扩池 ＋ 空洞性更正（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BH-1 全库 14 文件 ✓✓)}\ \text{类数\textbf{逐一等于文献上标}}:\ 2,3,2,2,4,3,2,4,2,3,6,2,4,8\ \checkmark\ \Longrightarrow\ \text{流水线在 }\textbf{14 个 }(n,R)\ \text{上全部验证} ✓✓}$$
$$\boxed{\textbf{(BH-2 ⚠️ 空洞性更正)}\ \text{8 个非平凡桶的 }(A_1,A_2)\ \textbf{全部形如 }(0,\cdot)\ \Longrightarrow\ A_1=0\ \Longrightarrow\ d_1\equiv0\ \Longrightarrow\ m\equiv0\ \Longrightarrow\ J=(0,0,0,0,0,0,\cdot)\ \textbf{恒等被迫} ✗}$$
$$\qquad\Longrightarrow\ \text{这些桶的"J 全同"\textbf{不含任何 P1-2 信息} ✗ —— \textbf{更正上一轮 }YI\ \text{档的"类型 1"判定} ⚠️\ \text{（那是不成立的 ✓）}$$
$$\boxed{\textbf{(BH-3 唯一非空洞测试场 =(8,1) ✓✓)}\ \text{需同时满足}:\ A_1>0\ \text{（support 层非空 ✓）}\ \wedge\ \text{类数}\ge2\ \text{（桶内可比 ✓）}}$$
$$\qquad\text{全库扫查}:\ (8,1)\ \text{（10 类 ✓，}A_1\in\{8,16\}\ ✓\text{）}\ \textbf{是唯一候选};\ (9,1)\ \text{（2 类但 }(A_1,A_2)\ \text{各异 ✗）};\ \text{其余格 }A_1=0\ ✗$$
$$\qquad\Longrightarrow\ \textbf{(甲) 2018 supplementary 成为唯一路径} ✓✓\ \text{（不是"可选"，而是"唯一" ✓）}$$
$$
$$
```

---

## §1 全库表（**14 文件 ✓**）

```
$$\begin{array}{c|c|c|c|c|c|c|c}
\text{文件} & n,R & \text{类数} & \text{文献上标} & \text{桶数} & \text{最大桶} & \text{非平凡桶} & J\ \text{分叉}\\
\hline
K\_2\_1 & 2,1 & 2 & 2\ ✓ & 2 & 1 & 0 & 0\\
K\_3\_2 & 3,2 & 3 & 3\ ✓ & 3 & 1 & 0 & 0\\
K\_4\_1 & 4,1 & 2 & 2\ ✓ & 2 & 1 & 0 & 0\\
K\_4\_2 & 4,2 & 2 & 2\ ✓ & 1 & 2 & 1 & 0\\
K\_4\_3 & 4,3 & 4 & 4\ ✓ & 3 & 2 & 1 & 0\\
K\_5\_3 & 5,3 & 3 & 3\ ✓ & 1 & 3 & 1 & 0\\
K\_6\_1 & 6,1 & 2 & 2\ ✓ & 2 & 1 & 0 & 0\\
K\_6\_2 & 6,2 & 4 & 4\ ✓ & 3 & 2 & 1 & 0\\
K\_6\_3 & 6,3 & 2 & 2\ ✓ & 1 & 2 & 1 & 0\\
K\_7\_2 & 7,2 & 3 & 3\ ✓ & 3 & 1 & 0 & 0\\
K\_8\_3 & 8,3 & 6 & 6\ ✓ & 3 & 4 & 1 & 0\\
K\_9\_1 & 9,1 & 2 & 2\ ✓ & 2 & 1 & 0 & 0\\
K\_9\_2 & 9,2 & 4 & 4\ ✓ & 1 & 4 & 1 & 0\\
K\_9\_3 & 9,3 & 8 & 8\ ✓ & 7 & 2 & 1 & 0\\
\end{array}$$
$$\textbf{类数 }14/14\ \text{命中文献上标} ✓✓\ \text{（含本档新解析的 }K\_2\_1{:}2,\ K\_3\_2{:}3,\ K\_4\_2{:}2,\ K\_4\_3{:}4,\ K\_5\_3{:}3,\ K\_6\_2{:}4,\ K\_6\_3{:}2\ ✓）}$$
$$
$$
```

---

## §2 非平凡桶明细（**全部退化 ⚠️**）

```
$$\begin{array}{c|c|c|c|c|c}
\text{文件} & n & (A_1,A_2) & \text{类数} & J & \text{有效性}\\
\hline
K\_4\_2 & 4 & (0,0) & 2 & (0,\ldots,0) & \textbf{空洞} ✗\\
K\_4\_3 & 4 & (0,0) & 2 & (0,\ldots,0) & \textbf{空洞} ✗\\
K\_5\_3 & 5 & (0,0) & 3 & (0,\ldots,0) & \textbf{空洞} ✗\\
K\_6\_2 & 6 & (0,0) & 2 & (0,\ldots,0) & \textbf{空洞} ✗\\
K\_6\_3 & 6 & (0,0) & 2 & (0,\ldots,0) & \textbf{空洞} ✗\\
K\_8\_3 & 8 & (0,0) & 4 & (0,\ldots,0) & \textbf{空洞} ✗\\
K\_9\_2 & 9 & (0,0) & 4 & (0,\ldots,0) & \textbf{空洞} ✗\\
K\_9\_3 & 9 & (0,3) & 2 & (0,0,0,0,0,3,0) & \textbf{空洞} ✗\\
\end{array}$$
$$\text{空洞性证明（一行 ✓）}:\ A_1=0\Longrightarrow\ \text{无距离 1 对}\ \Longrightarrow\ S(c)=\varnothing\ \forall c\ \Longrightarrow\ m\equiv0,\ \sum_c d_1(c)^2=0,\ \sum_ia_i^2=0\ \Longrightarrow\ J\ \textbf{恒为} (0,\ldots,0)\ \text{（除 }J_7=\sum q_{ij}^2\ \text{随 }A_2\ ✓）$$
$$\qquad\Longrightarrow\ \text{桶内"J 全同"\textbf{是 }A_1=0\ \text{的必然后果} ✗，与 P1-2 无关} ✗$$
$$
$$
```

---

## §3 唯一非空洞测试场 ＋ 下一步（**✓**）

```
$$\boxed{\text{非空洞条件 ✓}:\ A_1>0\ \wedge\ \text{桶内类数}\ge2}$$
$$\qquad\text{全库满足者}:\ \textbf{仅 }(8,1)\ \text{—— 10 类 ✓，且已得代表 }A_1\in\{8,16\}\ >0\ ✓;\ \text{其余格或 }A_1=0\ ✗\ \text{或类数}<2\ ✗$$
$$\Longrightarrow\ \textbf{(甲) 2018 supplementary 是唯一路径} ✓✓\ \text{（唐先生 12:47 的判断得到全库扫描的独立佐证 ✓）}$$
$$\text{按唐先生纪律 ✓}:\ \text{若 (甲) 仍无分叉} \Longrightarrow \text{转 }J\ \text{的\textbf{代数推导}} ✓\ \text{（不再无限扩池 ✓）}$$
$$\qquad\text{已有代数线索 ✓}:\ \text{Kéri }(8,32)_1\ \text{码 }J_3=0\Longrightarrow m\equiv0\Longrightarrow \textbf{d}_1(c)\le1\ \forall c\ \text{（即 }\textbf{distance-1 图是匹配} ✓\text{）}$$
$$\qquad\qquad\text{—— 与档案在 }Q=1\ \text{情形证过的 matching 定理同型 ✓✓，可作为推导靶点 ✓}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1–§2 为本机全库计算 ✓（14 文件 ✓，类数全中 ✓✓）；§3 为**非空洞性判定 ＋ 路线** ✓
- ⚠️ **本档更正上一轮**（`2b5fafe`）的"类型 1"判定 ✗ —— 依据是 §2 的一行空洞性证明 ✓
- **未**声称 $J$ 由 $(A_1,A_2)$ 决定 ✗（唯一非空洞格未测 ⚠️）；**未**碰 $n=10/119$ ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：全库 14 文件桶表、空洞性更正、唯一非空洞测试场判定
- **档案已有（引用，不列为提出）**：$(A_1,A_2)$、$J$ fingerprint、matching 定理、$K(n,R)$ 上标、P1-2


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 空洞性更正  命中文件数=1    :: ./YIP-2026-09-27-full-pool-and-the-vacuity-correction.md 
技术词 唯一非空洞测试场 命中文件数=1    :: ./YIP-2026-09-27-full-pool-and-the-vacuity-correction.md
```
- **本档新增**：全库 14 文件桶表、空洞性更正、唯一非空洞测试场判定（见上方命中数；0 命中者为自造语／内部标签 ✓）
