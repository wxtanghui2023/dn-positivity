已查地图：已跑 scripts/prework_map_check.sh I 2A₂ 非码字 clique 饱和等价 d_C ⟹ 执行自 HLAYER-2026-09-26 档；本档为**新精确恒等式＋饱和等价＋b_max≤3 猜想的两半拆分**（唐先生 2026-09-26 14:51 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 2A₂ 的精确拆分恒等式、I=2A₂ 的结构等价、b_max≤3 猜想的码字/非码字两半
D1: 1（新增：**2A₂ = I + Σ_{x∉C}C(b,2) 恒等式** ✓✓；**I=2A₂ ⟺ ∀x∉C: b≤1** ✓✓；猜想拆两半＋数据 ✓）

# SPLIT2-2026-09-26

## §0 文献标注（唐先生 ✓）

```
$$\text{检索确认 }K(9,1)=62\ [L]\ ✓;\quad \text{"}M=K\Rightarrow b_{\max}\le3\text{"\ \textbf{无一般定理可引}}\ \Longrightarrow\ \textbf{仍标 [G]}\ ✓✓\ (\text{不得当文献事实}\ ✗)$$
$$

## §1 ✅ 唐先生局部论证成立（我方核验 ✓）

```
$$\text{非码字 }x\ \text{有 }b(x)=k\ \Longrightarrow\ W(x)=\{c_1..c_k\}\ \text{两两距离 2}\ ✓\ \Longrightarrow\ \binom{k}{2}\ \text{个距离-2 对}\ ✓$$
$$\text{每个这样的对的两中点之一是 }x\ (\text{非码字}\ ✓)\ \Longrightarrow\ \text{该对在 }I\ \text{中\textbf{损失}\ge1}\ ✓\ \Longrightarrow\ I\ \le\ 2A_2-\binom{k}{2}\ ✓✓$$
$$\text{码字中心 }x\ (b=4):\ W(x)\ \text{含 }0\ \text{与三个邻点}\ ✓\ \Longrightarrow\ \binom32=3\ \text{个 }A_2\text{-对}\ ✓\ (\text{不矛盾，仅消耗}\ ✓)$$
$$

## §2 ⭐⭐ **新精确恒等式**（我方 ✓，60+ 样本全过 ✓✓）

```
$$\textbf{定义}: I:=\sum_{x\in C}\binom{d_C(x)}2\ ✓;\quad S:=\sum_{x\notin C}\binom{b(x)}2\ ✓$$
$$\boxed{2A_2=I+S}\ ✓✓$$
$$\textbf{证明（两向）}: \text{每个距离-2 对恰有 2 个中点}\ ✓\ \Longrightarrow\ 2A_2=\sum_{\text{pairs}}\#\{\text{中点}\}\ ✓$$
$$\qquad\#\{\text{码字中点}\}\ \text{之和}=I\ ✓\ (\text{楔形计数}\ ✓);\quad \#\{\text{非码字中点}\}\ \text{之和}=S\ ✓\ (\text{非码字邻点对}\ ✓)$$
$$\textbf{核验}: (4,4):\ 0=0+0\ ✓;\ (4,5):\ 6=3+3\ ✓;\ (5,7):\ 8=1+7\ ✓;\ (9,64):\ 64=64+0\ ✓✓\ (\text{全样本}\ ✓)$$
$$

## §3 ⭐ **饱和等价（结构性 ✓✓，唐先生"等号分析"的强化 ✓）**

```
$$\boxed{I=2A_2\iff S=0\iff \forall x\notin C:\ b(x)\le1}\ ✓✓$$
$$\text{读法}: \text{每个距离-2 对的两中点\textbf{必须都是码字}}\ ⟺\ \textbf{无任何非码字是中点}\ ⟺\ \text{非码字至多 1 个码字邻居}\ ✓$$
$$\textbf{实例}: (9,64):\ I=2A_2\ \textbf{饱和}\ ✓,\ \text{非码字 }b_{\max}=1\ ✓✓;\quad (5,7)=K:\ I=1\ll8=2A_2\ \textbf{不饱和}\ ✗,\ S=7\ ✓$$
$$

## §4 ⭐ **猜想 b_max≤3 拆成两半（数据 ✓）**

```
$$\textbf{码字半}: x\in C:\ b=1+d_C(x)\le3\iff d_C(x)\le2\ ✓$$
$$\qquad\textbf{数据}: M=K:\ n=4:\ d_C^{\max}=1\ ✓;\ n=5:\ 2\ ✓;\ n=6:\ 2\ ✓\ (\text{因 }b_{\max}=3\ ✓)$$
$$\qquad\textbf{反例侧}: M>K\ (n=4,M=5):\ d_C^{\max}=\mathbf{3}\ ✗\ \Longrightarrow\ \textbf{极值特异}\ ✓✓$$
$$\textbf{非码字半}: x\notin C:\ b(x)\le3\ ✓$$
$$\qquad\textbf{数据}: M=K:\ n=5:\ 3\ ✓;\ n=6:\ 3\ ✓;\quad (9,64):\ 1\ ✓\ (\text{饱和}\ ✓)$$
$$\qquad\textbf{反例侧}: hmm\ \text{未观测到非码字 }b\ge4\ \text{于小样本}\ ⚠️\ (\text{样本有限}\ ✗)$$
$$

## §5 下一刀（唐先生 ✓：攻码字半）

```
$$\text{目标}: \boxed{M=K\ \wedge\ \exists x\in C:\ d_C(x)\ge3\ \Longrightarrow\ I<2A_2}\ \text{并看是否与其他恒等式冲突}\ ✓$$
$$\text{可用的新工具}: \text{恒等式 }2A_2=I+S\ ✓\ \text{把"饱和失败"精确量化为 }S\ ✓\ (S=\sum_{x\notin C}\binom{b}2\ ✓)$$
$$\qquad\Longrightarrow\ \text{若 }d_C\ge3\ \text{强迫非码字 }b\ge2\ (\text{即 }S>0)\ ✓\ \Longrightarrow\ I<2A_2\ \text{与某种"应饱和"矛盾}\ ⚠️$$
$$\text{注意}: \text{命题 }"I=2A_2\ \text{在 }M=K\ \text{成立}"\ \text{已被 }n=5\ \text{否证}\ ✗\ (I=1\ll8\ ✓)\ \Longrightarrow\ \text{不能走饱和路线}\ ✗✓$$
$$

## §6 状态

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{新资产}: 2A_2=I+S\ ✓✓;\ \text{饱和等价}\ ✓✓;\ \text{猜想拆两半}\ ✓$$
$$\textbf{已否}: \text{"}M=K\Rightarrow I=2A_2\text{"}\ ✗;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$

## §7 边界（诚实标注）

- §2/§3/§4 为**数值核验** ✓（n=4,5 全枚举 ✓、n=9 我方构造 ✓）；§5 的"已否"为**数据否证** ✓
- §0 的文献标注按唐先生要求：[L] 仅限 `K(9,1)=62` ✓；`b_max≤3` 标 **[G]** ✓
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 两向拆分恒等式 命中文件数=1    :: ./SPLIT2-2026-09-26-exact-split-identity-and-saturation-equivalence.md 
技术词 饱和等价     命中文件数=1    :: ./SPLIT2-2026-09-26-exact-split-identity-and-saturation-equivalence.md 
技术词 猜想两半拆分 命中文件数=1    :: ./SPLIT2-2026-09-26-exact-split-identity-and-saturation-equivalence.md 
技术词 饱和路线否证 命中文件数=1    :: ./SPLIT2-2026-09-26-exact-split-identity-and-saturation-equivalence.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：两向拆分恒等式、饱和等价、猜想两半拆分、饱和路线否证
- **档案已有（引用，不列为提出）**：A≤2、excess、minimality
