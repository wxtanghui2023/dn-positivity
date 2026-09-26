已查地图：已跑 scripts/prework_map_check.sh H 高重叠缺陷 T₃ 分层 b_max 极值 ⟹ 执行自 T3SPLIT-2026-09-26 档；本档为**代数纠正＋精确恒等式＋H=0 否证＋极值特异观测**（唐先生 2026-09-26 14:49 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 高重叠缺陷 H 的精确分层、T₃=Q₂+H/3 恒等式、"高k被强制"的否证、b_max≤3 极值观测
D1: 1（新增：**T₃=Q₂+H/3 恒等式** ✓✓；**H=0∧E>0 否证** ✗；**极值 b_max≤3 观测（候选猜想）** ✓）

# HLAYER-2026-09-26

## §1 ⚠️ 代数纠正（唐先生式有误 ✗，我方核验 ✓）

```
$$\text{唐先生写}: \binom{k}{3}=\frac{k-2}{3}\binom{k-1}{2}\ ✗$$
$$\textbf{逐值核验}: k=3:\ 1\ \text{vs}\ 0.333\ ✗;\ k=4:\ 4\ \text{vs}\ 2\ ✗;\ k=5:\ 10\ \text{vs}\ 6\ ✗;\ k=6:\ 20\ \text{vs}\ 13.33\ ✗\ \Longrightarrow\ \textbf{该式错}\ ✗✓$$
$$\textbf{正确式}: \boxed{\binom{k}{3}=\frac{k}{3}\binom{k-1}{2}}\ ✓✓\ (\text{逐值全过}\ ✓)$$
$$\text{由来}: \binom{k}{3}=\frac{k(k-1)(k-2)}{6}=\frac{k}{3}\cdot\frac{(k-1)(k-2)}{2}\ ✓$$
$$

## §2 ✅ **修正后的精确恒等式**（数值全过 ✓✓）

```
$$\text{由 }k=3+(k-3): \binom{k}{3}=\binom{k-1}{2}+\frac{k-3}{3}\binom{k-1}{2}\ ✓$$
$$\textbf{定义 }H:=\sum_{k\ge4}(k-3)\binom{k-1}{2}N_k\ \ge0\ ✓\ \Longrightarrow\ \boxed{T_3=Q_2+\frac{H}{3}}\ ✓✓$$
$$\textbf{核验}: (4,4):\ 0=0+0\ ✓;\ (4,5):\ 4=3+3/3\ ✓;\ (5,7):\ 2=2+0\ ✓;\ (9,64):\ 64=64+0\ ✓✓\ (\text{全样本}\ ✓)$$
$$\textbf{二级分层（唐先生 ✓）}: H=3N_4+\sum_{k\ge5}(k-3)\binom{k-1}{2}N_k=:H_4+H_{\ge5}\ ✓\ (\text{核验 }\ ✓)$$
$$\Longrightarrow\ T_3-Q_2=N_4+\frac13\sum_{k\ge5}(k-3)\binom{k-1}{2}N_k\ ✓\ (k=4\ \text{线性}\ ✓;\ k\ge5\ \text{带 }C(k-1,2)\ \text{放大}\ ✓)$$
$$

## §3 ⛔ **"高 k 层被强制"被否证** ✗✓

```
$$\text{数据}: (4,4)=K:\ H=0\ ✓;\ (4,5):\ H\in\{0,3\}\ ✓;\ (4,6):\ H\in\{0,3,12\}\ ✓;\ (5,7)=K:\ H=0\ ✓;\ (9,64):\ H=0\ ✓$$
$$\qquad (9,64):\ E=128>0,\ H=0,\ b_{\max}=3,\ \text{分布}\ \{1{:}448,\ 3{:}64\}\ ✗✓$$
$$\Longrightarrow\ \boxed{\text{"高重叠层 }N_{\ge4}\ \text{被 minimality 强制"为假}}\ ✗✓\ (\text{极值壳 }M=K\ \text{上亦假}\ ✗)$$
$$\text{后果}: T_3\le\tfrac{10}3A_2\ \text{与 }T_3=Q_2+\tfrac H3\ \Longrightarrow\ Q_2\le\tfrac{10}3A_2-\tfrac H3\ ✓;\ \text{需 }H\ \text{的\textbf{下界}才有增益}\ ⚠️\ ——\ \text{而 }H=0\ \text{可达}\ ✗\ \Longrightarrow\ \textbf{无增益}\ ✗$$
$$

## §4 ⭐ **新的极值特异观测（候选猜想 ✓）**

```
$$\text{全部 }M=K\ \text{数据}: b_{\max}\ \text{取值}$$
$$\quad n=4\ (M=4):\ b_{\max}=2\ \Longrightarrow\ b\in\{1,2\}\ ✓; \qquad n=5\ (M=7):\ b_{\max}=3\ \Longrightarrow\ b\equiv\{1,2,3\}\ ✓$$
$$\quad n=6\ (M=12):\ b_{\max}=3\ \Longrightarrow\ \text{profile }(N_1,N_2,N_3)=(48,12,4)\ ✓$$
$$\quad \text{文献一致}: n=7\ (\text{perfect}):\ b\equiv1\ ✓;\quad n=8\ (\text{NP1CC}):\ b\in\{1,2\}\ ✓$$
$$\text{反例侧}: M>K\ \text{时 }b_{\max}\ \text{可达 }4,5\ ✗\ (\text{(4,5)}:\ 4\ ✓;\ \text{(4,6)}:\ 5\ ✓)\ \Longrightarrow\ \textbf{极值特异}\ ✓✓$$
$$\Longrightarrow\ \boxed{\textbf{候选猜想}: M=K(n,1)\ \Longrightarrow\ b(x)\le3\ \forall x\ (\iff H=0)}\ \⚠️\ (\text{数据全支持，未证}\ ✗)$$
$$\textbf{若真}: Q_2=N_3\ \text{且}\ E=N_2+2N_3\ \Longrightarrow\ Q_2=\frac{E-N_2}{2}\ \Longrightarrow\ \boxed{\text{"钉住 }Q_2\text{"}\iff\text{"钉住 }N_2\text{"}}\ ✓✓\ (\text{目标\textbf{换形}}\ ✓)$$
$$

## §5 状态与下一刀

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{入口 3/④}: \text{本轮完成}\ ✓;\quad \text{无 P1 进展}\ ✗\ (\text{诚实}\ ✓)$$
$$\textbf{新资产}: T_3=Q_2+H/3\ ✓✓;\ H=H_4+H_{\ge5}\ ✓;\ \text{猜想 }b_{\max}\le3\ (M=K)\ ⚠️;\ \text{目标换形 }Q_2\leftrightarrow N_2\ ✓$$
$$\text{下一刀候选}: \text{① 攻 }b_{\max}\le3\ \text{猜想（若成立 ⟹ 目标换成 }N_2\ \text{的钉住}\ ✓)$$
$$\qquad\text{② 用 }H=H_4+H_{\ge5}\ \text{对 }N_4\ \text{做局部禁形分析}\ ✓;\quad \text{③ 记录后暂停④}\ ✓$$
$$

## §6 边界（诚实标注）

- §1 为**代数纠正**（唐先生式错 ✗，我方逐值核验 ✓）；§2/§3/§4 为**数值核验** ✓（n=4 全枚举 ✓、n=5 全枚举 ✓、n=9 我方构造 ✓）
- §4 的猜想为**候选**（数据全支持 ✓，**未证** ✗，且 n=9 的 M=K 码不可得 ⟹ 无法直接验 ✓）
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 高重叠缺陷分层 命中文件数=1    :: ./HLAYER-2026-09-26-high-multiplicity-defect-and-extremal-bound-observation.md 
技术词 目标换形     命中文件数=1    :: ./HLAYER-2026-09-26-high-multiplicity-defect-and-extremal-bound-observation.md 
技术词 极值上界观测 命中文件数=1    :: ./HLAYER-2026-09-26-high-multiplicity-defect-and-extremal-bound-observation.md 
技术词 缺陷下界缺口 命中文件数=1    :: ./HLAYER-2026-09-26-high-multiplicity-defect-and-extremal-bound-observation.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：高重叠缺陷分层、目标换形、极值上界观测、缺陷下界缺口
- **档案已有（引用，不列为提出）**：excess、A≤2、minimality
