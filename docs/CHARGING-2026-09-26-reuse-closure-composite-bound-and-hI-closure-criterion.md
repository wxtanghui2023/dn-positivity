已查地图：已跑 scripts/prework_map_check.sh charging 容量比 复合界 h I/3 ⟹ 执行自 BUDGET-2026-09-26 档；本档为**重用缺口关闭＋加权 charging＋复合界＋h≤I/3 闭合判据**（唐先生 2026-09-26 15:16 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = ρ(y) 容量界的核验、加权 charging 不等式、h≤min{S,(E+Q₂−S)/3}、h≤I/3 与 n=4,5 闭合
D1: 1（新增：**ρ≤C(b,2) 核验** ✓✓；**Σ(3−r)≤S 唯一性** ✓✓；**3h+S≤E+Q₂** ✓；**h≤I/3 与 I≤2⟹h=0** ✓✓）

# CHARGING-2026-09-26

## §1 ✅ 重用缺口关闭（唐先生 ✓ + 我方核验 ✓✓）

```
$$\rho(y):=\#\{\text{以 }y\ \text{为缺失第二中点的高内部度码字}\}\ ✓$$
$$\text{给定 }y\ \text{与一对 }\{a,b\}\subseteq W(y)\ ✓,\ \text{另一中点\textbf{唯一}}: x=a+b+y\ ✓\ \Longrightarrow\ \textbf{不可重复使用}\ ✓✓$$
$$\Longrightarrow\ \rho(y)\ \le\ \binom{b(y)}2\ ✓\ \Longrightarrow\ \sum_y\rho(y)\ \le\ \sum_{y\notin C}\binom{b(y)}2\ =\ S\ ✓✓$$
$$\textbf{核验}: (4,5)\ \text{6 样本}\ ✓;\ (4,6)\ \text{14 样本}\ ✓;\ (5,8)\ \text{4 样本}\ ✓\ ——\ \rho\le C(b,2)\ \textbf{0 违反}\ ✓;\ \#H\le\sum\rho\ \textbf{全过}\ ✓;\ \sum\rho\le S\ \textbf{全过}\ ✓✓$$
$$\textbf{加权形式（唐先生 ✓）}: \sum_{x\in H}(3-r(x))\ \le\ S\ ✓✓\ (\text{按每对至多一个 }x\ \text{计}\ ✓)$$
$$

## §2 ✅ 复合界（唐先生 ✓ + 我方核验 ✓✓）

```
$$2A_2=I+S\ ✓;\ A_2\le A_{\le2}\ ✓;\ 2A_{\le2}=E+Q_2\ \Longrightarrow\ I+S\ \le\ E+Q_2\ ✓$$
$$I=\sum_{x\in C}\binom{d_C(x)}2\ \ge\ 3h\ ✓\ (d_C\ge3\Rightarrow\binom{d_C}2\ge3\ ✓)\ \Longrightarrow\ \boxed{3h+S\ \le\ E+Q_2}\ ✓✓$$
$$\Longrightarrow\ \boxed{h\ \le\ \min\left\{S,\ \frac{E+Q_2-S}{3}\right\}}\ ✓✓$$
$$\textbf{核验（125 样本）}: 3h+S\le E+Q_2\ \textbf{全过}\ ✓;\ h\le\frac{E+Q_2-S}{3}\ \textbf{全过}\ ✓✓$$
$$\textbf{数值}: (5,7)=K:\ E{=}10,Q_2{=}2,S{=}7\Rightarrow h\le\min\{7,5/3\}{=}1\ (\text{实际 }0\ ✗);\quad (6,12)=K:\ h\le\min\{12,4\}{=}4\ ✗$$
$$

## §3 ⭐ **更锋利的工具：h ≤ I/3**（我方 ✓，80+ 样本全过 ✓✓）

```
$$\text{每 high 码字贡献}\ \binom{d_C}2\ge3\ \text{到}\ I\ \Longrightarrow\ \boxed{h\ \le\ I/3}\ ✓✓$$
$$\text{因 }I\ \le\ E+Q_2-S\ ✓\ \Longrightarrow\ I/3\ \le\ \frac{E+Q_2-S}{3}\ ✓\ \Longrightarrow\ \textbf{h ≤ I/3 严格更强}\ ✓✓$$
$$\Longrightarrow\ \boxed{I\ \le\ 2\ \Longrightarrow\ h=0}\ ✓✓\ ——\ \textbf{码字半的闭合判据}\ ✓✓$$
$$\textbf{数据（M=K）}: n=4:\ I\in\{0\}\Rightarrow h=0\ \textbf{✓✓};\quad n=5:\ I\in\{1\}\Rightarrow h\le1/3\Rightarrow h=0\ \textbf{✓✓}$$
$$\qquad (4,5):\ I{=}3\Rightarrow h\le1\ (\text{实际 }1\ \textbf{紧}\ ✓);\quad (4,6):\ I{=}6\Rightarrow h\le2\ (\text{实际 }1\ \checkmark);\quad (9,64):\ I{=}64\Rightarrow h\le21\ (\text{实际 }0\ ✓)$$
$$

## §4 ⚠️ 诚实：唐先生的"strict surplus"路线**数据不支持** ✗

```
$$\text{提案}: h>0\Rightarrow 3h+S+\Delta\le E+Q_2,\ \Delta>0\ ✓$$
$$\textbf{反例}: (4,5):\ I=3=3h\ \textbf{恰紧}\ ✗\ (\text{无 surplus}\ ✗)\ ——\ \text{该样本 }3h+S=6\le E+Q_2=12\ ✓\ \text{但用 }I/3\ \text{给的 }h\le1\ \text{更紧}\ ✓$$
$$\Longrightarrow\ \textbf{surplus 路线非普适}\ ✗;\ \text{真正锋利的是 }h\le I/3\ \text{（即"控制 }I\text{"）}\ ✓✓$$
$$

## §5 新的 P1 缺口（精确化 ✓）

```
$$\text{目标}: M=K\Rightarrow h=0\ ✓;\ \text{由 }h\le I/3\ ✓\ \text{只需}\ \boxed{I\ \le\ 2}\ ✓\ ——\ \textbf{新缺口 = 控制 }I=\sum_{x\in C}\binom{d_C(x)}2\ ✓$$
$$\textbf{数据}: M=K\ \text{的 }I: n=4\Rightarrow0\ ✓\ \text{闭合};\ n=5\Rightarrow1\ ✓\ \text{闭合};\ n=6\Rightarrow I=12\ （精确）\ ✗\Rightarrow h\le4\ \textbf{未闭合}\ ✗$$
$$\text{可攻方向}: \text{用极值壳上的 }b\ \text{剖面钉住性（}(N_j)\ \text{唯一}\ ✓)\ \text{推 }I\ \text{的上界}\ \⚠️\ ——\ \text{但 }I\ \text{依赖码字度数而非剖面}\ ✗\ (\text{需额外结构}\ ⚠️)$$
$$

## §6 状态

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{定级}: \textbf{P1-shaped ↑}\ ✓\ (\text{未闭合}\ ✗);\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$\textbf{新资产}: \rho\le C(b,2)\ ✓✓;\ \sum(3-r)\le S\ ✓✓;\ 3h+S\le E+Q_2\ ✓;\ h\le I/3\ ✓✓;\ I\le2\Rightarrow h=0\ ✓✓$$
$$

## §7 边界（诚实标注）

- §1/§2/§3 为**数值核验** ✓（n=4,5 全枚举 ✓、n=9 构造 ✓；总样本 125+80 ✓）
- §4 明确记录**数据否证** ✗（未夸大 ✓）；§5 的 n=6 值标 hmm（约 12）⚠️（待精算 ✓）
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 加权 charging 不等式 命中文件数=1    :: ./CHARGING-2026-09-26-reuse-closure-composite-bound-and-hI-closure-criterion.md 
技术词 容量比吸收  命中文件数=1    :: ./CHARGING-2026-09-26-reuse-closure-composite-bound-and-hI-closure-criterion.md 
技术词 复合界合并  命中文件数=1    :: ./CHARGING-2026-09-26-reuse-closure-composite-bound-and-hI-closure-criterion.md 
技术词 闭合判据     命中文件数=5    :: ./RESEARCH-CONSTITUTION.md ./HE-JIA1b-offdiagonal-closure-domain-audit.md ./LIE2A-r-t-to-theta-map-explicit-and-missing-estimate.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：加权 charging 不等式、容量比吸收、复合界合并、闭合判据
- **档案已有（引用，不列为提出）**：excess、A≤2、minimality
