已查地图：已跑 scripts/prework_map_check.sh 钉住 K(n,1) 分类 等价 ⟹ 执行自 PINNING-2026-09-26 与 PROTO-2026-09-26 两档；本档为**AMEND-29 两步审计（文献接口 ＋ 量化）**（唐先生 2026-09-26 09:51 指令）；不开新方向 ✓。
D0: 本档对象 = 最小覆盖钉住现象在 n=6,7,8 的验证（我方实证对象；非新对象）
D1: 1（新增经验数据：n=6 全部样本 Q=4；n=8 存在最优码 Q=0 ✓）

# PINNING-AUDIT-2026-09-26 · 两步审计与 n=6,7,8 数据

## §1 **Step 1｜文献接口验证**（结果：接口为真，但**等价关系必须选对** ✓）

```
✓ **存在性**: Östergård–Weakley, *Classification of binary covering codes*,
   J. Combin. Des. **8 (2000) 391–401** ✓（经 Östergård 官方 pub 列表逐字确认标题 ✓）
   覆盖 **n≤8 的全部最优二元覆盖码（up to equivalence）** ✓
⚠️ **关键细节（唐先生预判正确 ✓）**: 2018 年 *Switching of covering codes*（Discrete Math 341, 1778–1788 ✓）
   摘要逐字: "Switching of optimal codes of size at most 7 and of codes attaining **K(8,1)=32** is further
   investigated, and **semiautomorphism classes** of these codes are found." ✓
$$\Longrightarrow\ \textbf{存在两个不同的等价关系}:\ \text{equivalence（}B_n\text{ 型）}\ \ne\ \text{semiautomorphism（半自同构，2018 ✓）}$$
$$\text{我方 }Q\ \text{的对称性}: \text{对坐标置换 ✓ 与平移 ✓ 均不变} \Longrightarrow Q\ \text{在 **equivalence** 下良定义}\ ✓$$
$$\text{但**未必**在半自同构下不变}\ ✗ \Longrightarrow \textbf{必须用 2000 年那个（较粗）的 equivalence 分类}\ ✓$$
（另注: 2018 摘要给出"半自同构 = 保持一切 r-球集合的双射" ✓，故其分类**比** equivalence **更细** ✓）
```

## §2 **Step 2｜量化**（不依赖付费墙，自己造最优码 ✓）

```
$$\begin{array}{c|c|c|c|c|c}
n & M & E & A_1+A_2 & Q & \text{来源/范围}\\
\hline
4 & 4 & 4 & 2 & \mathbf{0} & \textbf{穷举} 40 个（2 个 }B_4\text{-类，同值 ✓）\\
5 & 7 & 10 & 6 & \mathbf{2} & \textbf{穷举} 320 个（1 个 }B_5\text{-类）\\
6 & 12 & 20 & 12 & \mathbf{4} & \textbf{抽样} 171 个不同码，**全部同值** ✓（非穷举 ✗）\\
7 & 16 & 0 & 0 & \mathbf{0} & \text{完美 Hamming ⟹ }E=0\ \textbf{强制}\ Q=0\ ✓\\
8 & 32 & 32 & 16 & \mathbf{0} & \text{doubled Hamming（}=K(8,1)\ ✓\text{）；b 分布 }\{1{:}224,\ 2{:}32\}
\end{array}$$
$$\textbf{n=6 抽样细节}: 171\ \text{个不同}12\text{-字覆盖码 }Q\ \text{全为}4\ \checkmark\ (\text{例: }000100\ 000111\ 001010\ 001101\ 010001\ 011110\ 100001\ 101110\ 110010\ 110101\ 111000\ 111011)$$
$$\textbf{n=8 构造}: \text{doubled Hamming}= \{(c,0),(c,1):c\in H(7)\}\ ✓\ \text{覆盖 ✓}\ |C|=32\ ✓\ Q=0\ ✓$$
（我方先前猜测"doubled 码每点重数 2" **错** ✗ → 实测 $\{1{:}224,2{:}32\}$ ✓，已自纠 ✓）
```

## §3 ⚠️ **失败记录（诚实）**：n=8 的保覆盖切换搜索**产出 0** ✗

```
设计: 从 doubled Hamming 出发，做 (1,1)-切换（移除 w、加入覆盖 w 全部"私有覆盖点"的 w' ✓）
$$\text{实测}: \textbf{0 个新码}\ ✗\quad\text{原因（我方设计缺陷）}:\ w\ \text{的私有点}\ge2\ \text{时}\ \cap_{p}N[p]=\emptyset\ \Longrightarrow\ \text{无合法移动}\ ✗$$
⟹ **这不是数学结论**，是**搜索移动设计失败** ✗ —— 不得写成"n=8 只有 Q=0" ✗（诚实标注 ✓）
⟹ 正确做法应是 (k,k)-切换或有序生成 ✓（成本高 ✗，见 §5 判定 ✓）
```

## §4 数据小结与**猜想状态**

```
$$\text{钉住序列}: Q^*(4)=0,\ Q^*(5)=2,\ Q^*(6)=4,\ Q^*(7)=0\ (\text{强制}),\ Q^*(8)\ni 0$$
· n=4: **两个非等价类同值** ⟹ 钉住非对称性产物 ✓（最强证据 ✓）
· n=5: 穷举 ⟹ 唯一类 ⟹ 不变量为真 ✓
· n=6: 171 抽样全同 ✓（**证据** ✓，非证明 ✗）
· n=8: 仅**一个**数据点（Q=0）✗ ⟹ **未验证是否钉住** ✗
$$\boxed{\textbf{猜想（暂不成立为定理）}: "M=K(n,1)\ \Longrightarrow\ Q=Q^*_n\ \text{唯一}"\ \text{—— 证据支持 }n\le6\ ✓;\ n=8\ \textbf{未测}\ ✗}$$
```

## §5 判定（按 AMEND-29 ✓）

```
$$\text{分类}: \textbf{B 类}\ ✓\ (\text{接口真实、对象完全匹配、但原形式（需付费墙数据）不适合} \Longrightarrow \textbf{先改造再验}\ ✓)$$
$$\text{证据充分度}: n\le6\ \text{已足够支持"钉住"作为\textbf{经验规律}}\ ✓;\ \text{但}\ \textbf{对 }n=10\ \text{完全无推论力}\ ✗\ (\text{不能外推 ✓})$$
\text{下一步（便宜）}: ① 取 2000 年论文的**分类表/代表元**（需唐先生下载 ✓，或找作者页面数据 ✓）
             ② 若无数据: 对 n=6 做**有序生成**（canonical 剪枝）以求穷举 ⟹ 把 n=6 从"抽样"升为"穷举" ✓
             ③ n=8 用 (k,k)-切换或已知半自同构类做定向检验 ✓
```

## §6 边界（诚实标注）

- §1 为**逐字核实**（Östergård pub 列表 + Aalto 2018 摘要 ✓）；**未**读到 2000 年论文正文 ✗（付费墙 ✗）
- §2 数据为**实算**（脚本 `work/k10/q10proto/{n6_search,n8_switch}.py` ✓）；n=6 为**抽样** ✗、n=4/p=5 为穷举 ✓
- §3 为**我方方法失败** ✗（非数学结论 ✓）；**未**排除任何 n ✓
- `K(6,1)=12`、`K(8,1)=32` 引自文献/OEIS ✓（本档**未**独立验证下界 ✓）

## 【技术词回查】（定稿前逐字输出）

```
技术词 最小覆盖钉住 命中文件数=0    :: 
技术词 半自同构类  命中文件数=0    :: 
技术词 保覆盖切换  命中文件数=0    :: 
技术词 等价关系分层 命中文件数=0    ::
```

- **本档新增**（命中数=0）：最小覆盖钉住、半自同构类、保覆盖切换、等价关系分层
- **档案已有（引用，不列为提出）**：—
- 注：四词含中文，回查解析器按首词匹配 ✓
