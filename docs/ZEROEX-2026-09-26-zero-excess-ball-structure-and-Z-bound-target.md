已查地图：已跑 scripts/prework_map_check.sh t_x=0 零过量球 结构引理 Z 上界 ⟹ 执行自 OCBRIDGE-2026-09-26 档；未跑 solver ✓。
D0: 本档对象 = 零过量球的局部结构引理（修正版）、偶 n 的推论、Z 上界目标的建立与一次失败尝试
D1: 1（新增：**零过量球结构引理（修正）** ✓；**偶 n ⟹ Z=0** ✓；目标 **Z ≤ 44** ✓；一次失败尝试 ✗）

# ZEROEX-2026-09-26

## §1 ⚠️ 我方上一推的错误（自捕 ✓）

```
$$\text{我原写"恰好 }5\text{ 个码字在 dist}\le2"\ \text{—— 那是 }n=9\ \text{的数值}\ (n+1=10\ ✓),\ \textbf{错当成通式}\ ✗$$
$$\text{正确通式}: \text{球 }B_1(x)\ \text{有 }n+1\ \text{点}\ ✓,\ \text{每个距 }x\ \text{为 1-2 的码字恰覆盖其中 2 点}\ ✓\ \Longrightarrow\ \text{码字数}=(n+1)/2\ ✓$$
$$\textbf{数值证实（n=5，我原预期 4，实为 2）}: \text{观测 }(a,b_2,\text{tot})=(1,2,3)\ ✓✓\ \text{—— 总数为 }(n+1)/2=3\ ✓✓$$
$$

## §2 ✅ **零过量球结构引理（修正版）**（数值核验 ✓）

```
$$\textbf{引理}. \text{设 }x\notin C\ \text{且 }t_x:=\mathrm{OC}(B_1(x))=0\ ✓.\ \text{则}:$$
$$\quad\text{① } B_1(x)\ \text{的 }n+1\ \text{点\textbf{全部 }b=1}\ ✓\ (\text{数值}: n=5\ \textbf{270/270}\ ✓✓)$$
$$\quad\text{② }x\ \text{恰被 1 个码字覆盖}\ ⟹\ \text{恰\textbf{一个}距离-1 码字}\ ✓\ (\text{数值}: n=5\ \textbf{270/270}\ ✓✓)$$
$$\quad\text{③ 其余 }n-1\ \text{个邻点被 }(n-1)/2\ \text{个距离-2 码字两两配对}\ ✓;\ \text{每个对应一个\textbf{坐标对}\ ⟹\ \text{除 }\ell\ \text{外 }n-1\ \text{个坐标的\textbf{完美匹配}}\ ✓✓$$
$$\text{（}n=9:\ 4\ \text{个距离-2 码字}\ ✓;\ n=5:\ 2\ \text{个}\ ✓\ \text{—— 通式 }(n-1)/2\ ✓)$$
$$

## §3 ⭐ **新推论：偶 n ⟹ Z = 0** ✓

```
$$n\ \text{偶}\ \Longrightarrow\ n+1\ \text{奇}\ \Longrightarrow\ (n+1)/2\notin\mathbb Z\ \Longrightarrow\ \text{配对不可能}\ \Longrightarrow\ t_x\ne0\ \forall x\notin C\ \Longrightarrow\ \boxed{Z=0}\ ✓✓$$
$$\text{（与奇偶引理一致}: \text{偶 }n\Rightarrow \mathrm{OC}\ \text{奇}\Rightarrow \mathrm{OC}\ge1\ ✓;\ \text{本档给出\textbf{几何解释}}: \text{球点数为奇数 ⟹ 无法两两配对}\ ✓✓)$$
$$\textbf{数值}: (4,4)\ (n\ \text{偶}): Z=0\ ✓✓;\quad (9,64)\ (n\ \text{奇},\ \text{但 hot 点稠密}): Z=0\ ✓;\quad (5,7): Z=9/\text{码}\ ✓$$
$$

## §4 ⭐ 目标的**上界化**（唐先生 §1 ✗ 我方接续 ✓）

```
$$Q_2=\frac{(n-1)E-\Sigma\mathrm{OC}}2\ \Longrightarrow\ (\text{M=62},n=9,E=108):\ Q_2=432-\tfrac12\Sigma\mathrm{OC}\ ✓$$
$$\text{奇 }n:\ \mathrm{OC}\ \text{偶}\ ⟹\ \mathrm{OC}>0\Rightarrow\mathrm{OC}\ge2\ ⟹\ \Sigma\mathrm{OC}\ \ge\ 2\,(N_{\text{nonC}}-Z)\ ✓,\ N_{\text{nonC}}=450\ ✓$$
$$\boxed{Q_2\le26\iff\Sigma\mathrm{OC}\ge812\iff \mathbf{Z\le44}}\ ✓✓\ (\text{2}(450-Z)\ge812\ ⟹\ Z\le44\ ✓)$$
$$\Longrightarrow\ \textbf{主攻目标 = 上界化 }Z=\#\{x\notin C:\ \mathrm{OC}(B_1(x))=0\}\ ✓\ ——\ \text{正是 Struik 逐球界失效的那些点}\ ✓✓$$
$$

## §5 ⛔ 一次失败尝试（诚实记录 ✓）

```
$$\text{尝试}: \text{"每个零过量球含 }n+1\ \text{个 }b=1\ \text{点 ⟹ 它们都是私有点"}\ ⟹\ 10Z\le N_1\ ✓\ (\text{若无重数}\ ✓)$$
$$\Longrightarrow\ Z\le(512-Q)/10\le50\ ✓\ \text{—— \textbf{已接近目标 44}}\ ✓✓$$
$$\textbf{但推断有误 ✗}: \text{一个 }b{=}1\ \text{点可同时落在至多 }n+1\ \text{个球的 }B_1(\cdot)\ \text{中}\ ✗\ ⟹\ \text{球之间可共享私有点}\ ✗\ ⟹\ 10Z\le N_1\ \textbf{不成立}\ ✗✓$$
$$\text{（数值上 }n=5:\ Z=9,\ N_1=24:\ 10\cdot9=90\gg24\ ✗\ \text{确实不成立}\ ✓）$$
$$

## §6 台账与下一刀

```
$$\textbf{新增资产}: \text{零过量球结构引理}\ ✓;\ Z=0\ (\text{偶 }n)\ ✓;\ \text{目标 }Z\le44\ ✓$$
$$\textbf{桥}: \text{未打通}\ ✗\ (\text{但已缩到单一整数 }Z\ \text{的上界问题}\ ✓✓);\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$\text{下一刀候选}: \text{① 用匹配结构做坐标计数（每个零过量球给出一个 }(n-1)\ \text{点上的完美匹配}\ ✓);\ \text{② 用"距离-2 码字对 }\{x+e_i,x+e_j\}\ \text{的私有点"计数（避开共享陷阱}\ ✓);\ \text{③ 混合: 零过量球 ⟹ 相邻球的 }t\ \text{下界}\ ✓$$
$$

## §7 边界（诚实标注）

- §1–§3 的引理与推论为**我方推导 ＋ 数值核验** ✓（n=4/5 全枚举 ✓、n=9 我方构造 ✓）
- §3 的"偶 n ⟹ Z=0"是**奇偶引理的几何重述** ✓（非独立新信息 ✓，但给出了配对解释 ✓）
- §5 的失败尝试**明确记录** ✓（未掩盖 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 零过量球结构引理 命中文件数=1    :: ./ZEROEX-2026-09-26-zero-excess-ball-structure-and-Z-bound-target.md 
技术词 完美匹配结构 命中文件数=1    :: ./ZEROEX-2026-09-26-zero-excess-ball-structure-and-Z-bound-target.md 
技术词 目标上界化  命中文件数=1    :: ./ZEROEX-2026-09-26-zero-excess-ball-structure-and-Z-bound-target.md 
技术词 共享私有点陷阱 命中文件数=1    :: ./ZEROEX-2026-09-26-zero-excess-ball-structure-and-Z-bound-target.md 
```
- **本档新增**（命中数=1 但**仅本档自身 = self-hit** ⟹ 扣自引后 = 0 ✓）：零过量球结构引理、完美匹配结构、目标上界化 Z、共享私有点陷阱
- **档案已有（引用，不列为提出）**：over-covering、Struik
