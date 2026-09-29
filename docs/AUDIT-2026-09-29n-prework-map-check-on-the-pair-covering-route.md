# AUDIT-2026-09-29n —— **开工前查地图：pair covering 路线"是否已试过"**（唐先生令：先查再算）

> **性质**：**查地图（PRE-WORK MAP CHECK）**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:45 ✓

**已查地图**：`docs/` 全目录 grep（`struik`／`pair covering`／`triple covering`／`f_C(`）✓
**触发**：唐先生令「首先看之前有没有试过，然后再算」✓

D0: 本档对象 ＝ **档案已有**（pair 层三次失败／Struik 一阶空性—皆已登记 ✓）
D1: 0（产出＝**一次查地图 ＋ 一处关键区别 ＋ 一次实现失败记录** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 试过}:\ \text{pair 层\ \textbf{三次独立攻击}（单条／组合／整数消元）$=103$}✗\ (\text{未达文献 }105)}$$
$$\boxed{\text{② ✓ 试过}:\ \text{Struik/van Wee \textbf{一阶局部不等式}已审计（}\texttt{ODDENGINE}\text{）:\ 奇 }n\ \text{处为空}✗}$$ 
$$\boxed{\text{③ ✗ 未试过}:\ \text{Struik §2.7 之\ \textbf{原式 (2.35)} 从未正确转录／实现}}$$
$$\boxed{\text{④ ✗ 我方刚做的实现失败}:\ \text{OCR 转录错 ⟹ 给荒谬数（}n{=}10\Rightarrow4\text{）;\ 已作废}}$$

## §1 查地图结果（✓ 逐条可核）

$$\textbf{（甲）pair 层三次独立失败（}\texttt{ASSETS-REGISTRY}\ \text{L3392 逐字）}:$$
$$\text{sphere }94\ /\ \text{excess}=103\ /\ \textbf{Zhang pair 单条}=103\ /\ \text{induced }Z^{(i)}+非负=103\ /\ \text{induced}+FM\ \text{无闭合}=103$$
$$\Longrightarrow\ \text{逐字}:\ \textbf{"自助路线在 pair 层三重独立失败（单条／组合／整数消元）"}✓$$

$$\textbf{（乙）Struik 一阶局部不等式（}\texttt{ODDENGINE-2026-09-26}\ \text{逐字）}:$$
$$\mathrm{OC}(B_1(x))\ \ge\ 2\bigl(\lceil\tfrac{n+1}2\rceil-\tfrac{n+1}2\bigr):\quad n\ \text{偶}\Rightarrow1\ ✓;\quad n\ \text{奇}\Rightarrow\mathbf0\ (\text{空})✗$$
$$\text{奇偶引理}:\ x\notin C\Rightarrow\mathrm{OC}(B_1(x))\equiv n+1\ (\mathrm{mod}\ 2)\ \Longrightarrow\ \text{奇 }n\ \text{处下界 }0\ \textbf{可达}⟹\text{原理性空}✗$$

$$\textbf{（丙）van Wee 原式已在档（}\texttt{AUDIT-2026-09-28q}\text{，源 }\texttt{arXiv:2608.12595}\text{ equ (5)）}:$$
$$M\Bigl(\sum_{i=0}^{R}\tbinom ni-\tfrac{\binom nR}{\lceil\frac{n-R}{R+1}\rceil}\bigl(\lceil\tfrac{n+1}{R+1}\rceil-\tfrac{n+1}{R+1}\bigr)\Bigr)\ge2^n\ \Longrightarrow\ n{=}10,R{=}1:\ \text{分母 }10\Rightarrow\mathbf{103}\ ✓✓$$

## §2 ★ 关键区别（本轮真正信息）

$$\text{已试的是\ \textbf{我方的重构版}（单条／组合／整数消元）, 皆止于 }103✗$$
$$\text{未试的是\ \textbf{文献原式} (2.35)（Struik §2.7 转录）}——\ \text{从未正确转录}✗$$
$$\therefore\ \boxed{\text{"未复现 }105\text{" 与 "未试 (2.35)" 是同一件事的两面}⟹\ \textbf{转录原式 ＝ 新动作}}✓$$
$$\text{且已定位}:\ \texttt{sources/TUe-covering-codes-chapter-IR425174.pdf}\ \text{pp.~41--43 含 (2.33)(2.35)(2.36)}✓$$

## §3 我方实现失败（✗ 如实记录）

$$\text{我据 OCR 文本臆测 (2.35) 并实现} ⟹ n{=}10\ \text{给 }4\ (\text{应 }\sim103)\ ✗\ \Longrightarrow\ \textbf{转录错误，数值全部作废}✗$$
$$\text{正路}:\ \text{渲染 pp.~41--43 为图、}\textbf{视觉读公式}\ ✓\ (\text{已渲染}\ \texttt{/tmp/struik\_p41..43.png},\ 200\ \text{dpi})$$

## §4 下一步（照唐先生顺序：先查后算 ✓ 已查完）

$$\boxed{\text{① 视觉转录 (2.35){+}(2.36) 与 }s\ \text{之确切定义};\quad②\ \text{实现并}\ \textbf{校准}={105}?;\quad③\ \text{若校准过 ⟹ 同框架升一阶试 }107}$$

## §5 边界（硬 ✓）

- **查地图结果全部可核（引档名/行号/逐字）** ✓；**我方实现失败已作废** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）

## §6 【技术词回查】（**提交前实跑，逐字粘贴**）

```
开工前查地图pair层 : 技术词 开工前查地图pair层 命中文件数=0    ::
源式未转录 : 技术词 源式未转录   命中文件数=0    ::
校准105 : 技术词 校准105    命中文件数=0    ::
```
