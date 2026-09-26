已查地图：已跑 scripts/prework_map_check.sh pinning K(5,1) 等价 Kéri 表 ⟹ 执行自 PINNING-2026-09-26-data-hunt-negative-result 档；本档为**文献交叉验证 ✓ ＋ n≤8 全状态**（唐先生 2026-09-26 10:08 指令）；不开新方向 ✓。
D0: 本档对象 = 钉住猜想在 n≤8 的文献交叉验证与剩余缺口（非新对象）
D1: 1（新增独立验证：文献代表元 → 我方 Q 管道闭环 ✓；n=7 纯推理定案 ✓）

# PINNING-CROSSVAL-2026-09-26 · 文献交叉验证与 n≤8 全状态

## §1 **Step 1 收口**：等价定义 ✓（逐字）

```
$$\text{Kéri–Östergård 2006 逐字}: \textit{"Two binary codes are equivalent if one can be obtained from the other by a permutation of the coordinates followed by a transposition of the coordinate values in some of the coordinates."}$$
$$\text{坐标置换}\ +\ \text{逐坐标取反};\ \text{而在 } \mathbb F_2^n\ \text{中取反 = 平移} \Longrightarrow \boxed{\text{恰为 } B_n=2^n\rtimes S_n}\ ✓$$
$$\Longrightarrow\ \text{"1 inequivalent }(5,7)_1\text{"} \iff \text{"1 }B_5\text{-orbit"}\ ✓\ \text{—— 与我方计算所用完全一致 ✓（Step 1 通过 ✓）}$$
```

## §2 ⭐ **文献代表元 → 我方 Q 管道：闭环 ✓**（三重验证 ✓）

```
$$\text{文献 Theorem 2.1(a)}: \text{唯一 }(5,7)_1\ \text{码 } C=|C_1|C_2|C_3|C_4|C_5|\ \text{（逐列拼接 7 个长度 5 码字 ✓）}$$
$$\text{我方实算（该代表元）}: E=10,\ \min b=1,\ b\text{ 分布}=\{1{:}24,\ 2{:}6,\ 3{:}2\},\ A_1+A_2=6,\ \boxed{Q=2}\ ✓$$
$$\text{且 } |\mathrm{Aut}(C)|=\mathbf{12}\ \Longrightarrow\ 3840/12=320\ \checkmark\ \text{（与穷举 320 个码完美吻合 ✓）}$$
$$\boxed{\text{三重验证}: \text{文献分类（1 类）}＋\text{显式代表元（}Q=2\text{）}＋\text{我方穷举（320 个全 }Q=2\text{）}\ ✓✓}$$
```

## §3 **n=7 纯推理定案** ✓（无需文献 ✓）

```
$$\text{若 }|C|=16,\ n=7:\ E=16\cdot 8-2^7=128-128=\mathbf{0}\ \Longrightarrow\ \sum_x(b-1)=0\ \Longrightarrow\ b\equiv1\ \Longrightarrow\ \text{完美码}$$
$$\text{长 7 的 1-完美码唯一（Hamming）} \Longrightarrow\ \textbf{恰一} B_7\text{-类},\ \boxed{Q=0}\ ✓$$
```

## §4 n ≤ 8 全状态表

```
$$\begin{array}{c|c|c|c|c|c}
n & K(n,1) & E & Q & \text{验证强度}\\
\hline
4 & 4 & 4 & 0 & \textbf{穷举} 40 个（2 类，同值 ✓✓ 最强）\\
5 & 7 & 10 & 2 & \textbf{穷举 320} ＋ **文献三重复核** ✓✓✓\\
6 & 12 & 20 & 4 & **抽样 171 个全同** ✓（非穷举 ✗）\\
7 & 16 & 0 & 0 & \textbf{纯推理定案}（完美码唯一 ✓✓）\\
8 & 32 & 32 & 0 & 仅 **1 例**（doubled Hamming ✓）✗ 未判
\end{array}$$
$$K(n,1)\ \text{取值已由 Kéri 二元表独立确认}: 7,\ \mathbf{12},\ \mathbf{16},\ \mathbf{32}\ ✓\ （\text{表中 }n=10\ \text{行}: \textbf{107–120}\ ✓\ \text{即我方目标格 ✓}）$$
```

## §5 剩余缺口（精确）

```
$$\text{缺 }(6,12)_1\ \text{与}\ (8,32)_1\ \text{的\textbf{全部代表元}} ✗\ (\text{二者均属文献所称"six sporadic cases" ✓ 已分类 ✓})$$
$$\text{位置}: 2000\ \text{论文附录} ✗（付费墙）;\ \text{或 Kaski–Östergård 书 } \S7.2.6 ✗;\ \text{Bertolo 等 2004（Wiley ✗）}$$
$$\text{注}: \text{Kéri 二元素表}（2\_tables.pdf ✓）**只给界与引用标记 ✗**;\ \text{survey.pdf 仅 6 页、无分类表 ✗}$$
```

## §6 判定（AMEND-29 ✓）

```
$$\text{钉住猜想}: n=4,5,7\ \textbf{已定} ✓（n=4 非等同值同值 ✓; n=5 文献+穷举+代表元 ✓; n=7 纯推理 ✓）;\ n=6\ \text{强证据} ✓;\ n=8\ \text{未判} ✗$$
$$\text{状态}: \textbf{B / OPEN} ✓;\ \text{**不外推 }n=10 ✓$$;\quad \text{119 主线} = \textbf{UNKNOWN} ✓$$
\text{下一步}: ① 唐先生下载 2000 论文（附录 ✓）② 或 Kaski–Östergård 书 §7.2.6 ✓ ③ 拿到后: 代表元 → B_n 核验 → Q ✓
```

## §7 边界（诚实标注）

- §2 为**实算**（该代表元 → E/Q/Aut ✓，脚本内联；`|Aut|=12` 由 3840 个变换穷查 ✓）
- §3 为**纯推理** ✓（依赖：长 7 1-完美码唯一性 = 经典结果 ✓）
- Kéri 表数值为**逐字读取** ✓（`2_tables.pdf` ✓ 行 5/6/7/8/10 ✓）
- **未**排除任何 n ✗；**未**声称钉住为定理 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 文献交叉验证 命中文件数=0    :: 
技术词 代表元闭环  命中文件数=0    :: 
技术词 纯推理定案  命中文件数=0    :: 
技术词 限值表        命中文件数=0    ::
```

- **本档新增**（命中数=0）：文献交叉验证、代表元闭环、纯推理定案、限值表
- **档案已有（引用，不列为提出）**：—
