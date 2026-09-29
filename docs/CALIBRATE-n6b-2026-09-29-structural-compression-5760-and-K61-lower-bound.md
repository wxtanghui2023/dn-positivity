# CALIBRATE-n6-b（2026-09-29）—— **结构压缩：$1.1{\times}10^6\to\mathbf{5760}$；$K(6,1)\ge12$ 之\ \textbf{纯结构}复核**

> **性质**：**A-1 首刀之正面结果**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 16:3x ✓
> **唐先生令**：A-1；攻 $Q_5,k{=}5,\mathrm{Def}{=}2$ 之不可能，**不枚举 $A$** ✓

**已查地图**：`CALIBRATE-n5`／`CALIBRATE-n5-b`／`CALIBRATE-n6`（A-3）✓

D0: 本档对象 ＝ **档案已有**（defect／packing 数——皆经典 ✓）
D1: 0（产出＝**你的引理之数值印证 ＋ 刚性化 ＋ 零互补对 ＋ 压缩比 $190\times$** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 你的引理成立}:\ A(5,3)=\mathbf{4}\ (5\text{-packing}\ \mathbf{0}\ \text{个},\ 4\text{-packing}\ 120\ \text{个});\ \mathrm{Def}_{\min}(5,5)=\mathbf{4},\ \mathrm{Def}{=}2\ \text{者 }\mathbf{0}}$$
$$\boxed{\text{② ✓✓ 刚性化}:\ M{=}11\Longrightarrow a,b\in\{5,6\}\ \text{且\ \textbf{小侧须 }\mathrm{Def}{=}4}},\ \text{实测 }\mathrm{Def}{=}4\ \text{之 }5\text{-set\ \textbf{全部}}\ |D_A|{=}6}$$
$$\boxed{\text{③ ✓✓ 零互补对}:\ \text{满足 }B{=}D_A,\ D_B\subseteq A\ \text{者}=\mathbf{0}\ \big|\ 5760\Longrightarrow M{=}11\ \text{不存在}\Longrightarrow K(6,1)\ge12}$$
$$\boxed{\text{④ ✓ 压缩比}:\ \text{枚举量}\ 1{,}107{,}568\to\mathbf{5760}\ (\approx190\times);\ \text{且\ \textbf{不需}}2^{32}}$$

## §1 ① 你的引理（**✓✓ 数值印证**）

$$\textbf{引理}:\ C\subseteq Q_5,\ |C|{=}4,\ d_{\min}\ge3\Longrightarrow\forall x\notin C:\ |C\cap B_2(x)|\ge2$$
$$\textbf{实测}:\ 4\text{-packing}\ (\text{两两距离}\ge3)\ \text{之 }|A|{=}4\ \text{者}=\mathbf{120}\ \text{个};\ |A|{=}5\ \text{者}=\mathbf{0}\Longrightarrow A(5,3)=\mathbf{4}✓✓$$
$$\therefore\ \text{你的情形 }\mathrm{I}\ (\text{两个 }\mu{=}2)\ \text{与情形 }\mathrm{II}\ (\text{一个 }\mu{=}3)\ \text{之排除\ \textbf{成立}}✓$$
$$\therefore\ \boxed{|A|{=}5\Longrightarrow\mathrm{Def}(A)\ge4}\ (\text{结构证明，无需枚举})✓✓$$

## §2 ② 刚性化（**✓✓ 关键**）

$$\text{设 }M{=}11:\ \text{由 }|D_A|\ge32-6a+\mathrm{Def}(A)\ \text{与}\ |D_A|\le b:\ \mathrm{Def}(A)\le5a-21$$
$$a\le4\Rightarrow\text{右侧}<0\ ✗;\qquad b\le4\ \text{对称}\ ✗\qquad\Longrightarrow\ a,b\in\{5,6\}✓$$
$$\text{若 }a{=}5:\ \mathrm{Def}(A)\le4;\ \text{但引理给}\ \mathrm{Def}\ge4\Longrightarrow\boxed{\mathrm{Def}(A)=4},\ |D_A|{=}32-30+4=\mathbf{6}=b\Longrightarrow\boxed{B=D_A}✓$$
$$\textbf{实测（决定性）}:\ \mathrm{Def}{=}4\ \text{之 }5\text{-set\ \textbf{全部}}\ 5760\ \text{个皆有}\ |D_A|{=}6\ (=\{6{:}5760\})✓✓$$
$$\therefore\ B=D_A\ \text{且\ \textbf{无空位}加字}\Longrightarrow B\ \text{须\ \textbf{独自}覆盖 }Q_5\setminus A✓$$

## §3 ③ 零互补对（**✓✓ 结论**）

$$\text{检查}:\ \text{对全部 }\mathrm{Def}{=}4\ \text{之 }5\text{-set }A:\ B{=}D_A\ \text{是否满足}\ N_1(B)\supseteq Q_5\setminus A\ (\iff D_B\subseteq A)✓$$
$$\textbf{实测}:\ \text{枚举 }5760\ \text{个},\ \text{满足者}=\mathbf{0}✓✓$$
$$\therefore\ \boxed{M{=}11\ \text{不存在}\Longrightarrow K(6,1)\ge\mathbf{12}}✓✓\ (\text{纯结构复核，与 A-3 独立一致})$$
$$\text{附}:\ \text{纯计数筛亦全灭}\ (\text{因 }|D_A|{=}b{=}6\ \text{无空位};\ R\ \text{须为空})✓$$

## §4 ④ 递归模板（**你之抽象，本档确认**）

$$\boxed{\text{若每个 }k\text{-set }A\subseteq Q_m\ \text{满足}\ |D_A|\ge m+1,\ \text{且}\ A(m,3)<k+1,\ \text{则}\ K(m,1)\ge k+2}✓$$
$$\text{本档实证链}:\ \mathrm{Def}_{\min}(5,5){=}4\Rightarrow|D_A|\ge6{=}m{+}1\Rightarrow K(5,1)\ge7;\ \text{再经双边刚性}\Rightarrow K(6,1)\ge12✓$$
$$\therefore\ \boxed{\text{压缩链}:\ \text{min defect}\to\text{defect-set shape}\to\text{dual closure}\to\text{lower bound}}\ \text{已跑通一级}✓✓$$

## §5 下一步（**供唐先生定**）

$$\textbf{A-1'}:\ \text{分类 }Q_5\ \text{中 }\mathrm{Def}{=}4\ \text{之 }5760\ \text{个 }5\text{-set\ 之\ \textbf{defect-set 形状}}（\text{现已知 }|D_A|{=}6\ \text{恒成立}）\ \text{以\ \textbf{不用枚举}证明}\ D_{D_A}\nsubseteq A✓$$
$$\textbf{A-2}:\ \text{把引理（4-code 对 }B_2\ \text{二重支配）推广到 }Q_6\ (A(6,3){=}8?\ \text{待测})\ \text{以取 }K(7,1)\ge16✓$$
$$\textbf{C}:\ \text{归档：本链已给出\ \textbf{第一条可传递且可压缩}之递归下界机制}✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "Def4五点集分类" "互补对为零" "结构压缩"
技术词 Def4五点集分类  命中文件数=0    ::
技术词 互补对为零     命中文件数=0    ::
技术词 结构压缩       命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **全量实测（$\binom{32}{4}$、$\binom{32}{5}$ packing 计数；$5760$ 个 $\mathrm{Def}{=}4$ 之互补检查）** ✓；**不占 C 号** ✓；**未用 SAT/CP-SAT** ✓
- **不主张** $K(6,1)$ 之值有疑 ✗；本档为**结构压缩**之实证 ✓
