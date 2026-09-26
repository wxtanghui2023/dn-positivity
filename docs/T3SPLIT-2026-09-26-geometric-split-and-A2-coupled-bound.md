已查地图：已跑 scripts/prework_map_check.sh T₃ 几何拆分 κ 三重球交 A≤2 ⟹ 执行自 WHYPER-2026-09-26 档；本档为**T₃ 几何拆分 ＋ A≤2 首次进入上界 ＋ κ≤1**（唐先生 2026-09-26 14:47 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = T₃ 的几何类型拆分（I/II/III）、各项的 A≤2 界、κ≤1 的验证、诚实定级
D1: 1（新增：**几何拆分 T₃=I+II+III** ✓✓；**I≤2A₂ 验证 + II,III≤2A₂/3 ⟹ T₃≤(10/3)A₂** ✓；**κ≤1 验证** ✓；

# T3SPLIT-2026-09-26

## §1 ✅ **几何拆分**（唐先生 (1) ✓，数值全过 ✓）

```
$$\text{对 }x\ \text{分两类}:$$
$$\quad x\in C:\ b(x)=1+d_C(x)\ \Longrightarrow\ \binom{b}{3}=\binom{d}{2}+\binom{d}{3}\ ✓\ (\text{（中心＋两邻）与（三邻）两型}\ ✓)$$
$$\quad x\notin C:\ b(x)=|\{c:\ d(c,x)=1\}|\ \Longrightarrow\ \binom{b}{3}\ \text{全为（三个邻点）型}\ ✓\ (\text{两两距离}=2\ ✓)$$
$$\boxed{T_3=\underbrace{\sum_{x\in C}\binom{d_C(x)}2}_{I}+\underbrace{\sum_{x\in C}\binom{d_C(x)}3}_{II}+\underbrace{\sum_{x\notin C}\binom{b(x)}3}_{III}}\ ✓✓$$
$$\textbf{数值}: (4,4),(4,5),(5,7)\ \text{全样本}\ T_3=I+II+III\ \text{全过}\ ✓$$
$$

## §2 ✅ **三项的 A≤2 界**（我方推导 ✓，A≤2 首次真正进入 ✓✓）

```
$$\textbf{(i) }I\le 2A_2\ ✓✓: \text{每个楔形}\ (x\text{＋两个码字邻点})\ \text{给出距离-2 对}\ \{c_i,c_j\}\ ✓;\ \text{该对恰有 2 个中点}\ ✓\ \Longrightarrow\ \text{重数}\le2\ ✓$$
$$\qquad\textbf{数值核验}: (4,4),(4,5),(5,7)\ \text{全样本}\ I\le2A_2\ \textbf{全过}\ ✓✓;\quad (9,64):\ I=64=2A_2\ \textbf{取等}\ ✓✓$$
$$\textbf{(ii) }II\le \tfrac{2A_2}{3}\ ✓: \text{三角形（三码字两两距离 2）每对在}\le2\ \text{个三角形中}\ ⟹\ 3\cdot\#\triangle\le2A_2\ ✓;\ \text{且由 }\kappa\le1\ \text{每三角形}\le1\ \text{个顶点}\ ✓$$
$$\textbf{(iii) }III\le \tfrac{2A_2}{3}\ ✓: \text{同理，非码字中心是三元组的公共点}\ ✓;\ \kappa\le1\ ⟹\ \text{每三元组}\le1\ \text{个中心}\ ✓$$
$$\Longrightarrow\ \boxed{T_3\ \le\ 2A_2+\tfrac{2A_2}{3}+\tfrac{2A_2}{3}\ =\ \tfrac{10}{3}A_2}\ ✓✓\ (\textbf{A≤2 真正出现在右端}\ ✓)$$
$$

## §3 ✅ κ ≤ 1（三重球交）验证 ✓

```
$$\text{κ}:=\max_{\{c_1,c_2,c_3\}}|N[c_1]\cap N[c_2]\cap N[c_3]|\ ✓$$
$$\textbf{数值}: (4,4):\ \kappa_{\max}=0\ ✓;\ (4,5):\ 1\ ✓;\ (5,7):\ 1\ ✓;\ (9,64):\ 1\ ✓\ \Longrightarrow\ \kappa\le1\ ✓✓\ (\text{全部验证}\ ✓)$$
$$
$$

## §4 ⛔ **诚实定级：够到"部分 P1 判据"，但不足以闭合** ✗

```
$$\textbf{唐先生判据}: \text{若 }T_3\ \text{上界中\textbf{真正出现 minimality 或 }A_{\le2}}\ ⟹\ P1\ \text{有进展}\ ✓$$
$$\Longrightarrow\ \textbf{本次达标（A≤2 出现 ✓）};\ \textbf{但}:$$
$$\text{试闭合}: Q_2\le T_3\le\tfrac{10}3A_2\ \text{＋}\ 2A_{\le2}=E+Q_2\ \Longrightarrow\ Q_2\le\tfrac53(E+Q_2)\ \Longrightarrow\ -\tfrac23Q_2\le\tfrac53E\ \text{恒真}\ ✗✓\ \textbf{空转}\ ✗$$
$$\textbf{根因}: \text{常数 }10/3\ \text{太松}\ ✗\ \Longrightarrow\ \text{若要闭合需常数}<2\ ✓;\ \text{而 }I\le2A_2\ \text{已取等（}(9,64)\ ✓)\ ⟹\ \textbf{单靠这三项无法把常数压到 2 以下}\ ✗$$
$$\Longrightarrow\ \textbf{定级}: \textbf{P0-plus（A≤2 耦合不等式）}\ ✓,\ \textbf{非 P1}\ ✗;\ \text{但\textbf{保留了唯一带 }A_{\le2}\ \text{的三阶界}\ ✓$$
$$

## §5 观测（备用 ✓）

```
$$\textbf{O1}: (9,64):\ T_3=64=I,\ II=III=0\ ✓\ \Longrightarrow\ \text{全部三阶块是（中心＋两邻）型}\ ✓;\ I=2A_2\ \text{取等}\ ✓$$
$$\textbf{O2}: (5,7):\ T_3=2\ (I=1,\ II=0,\ III=1)\ ✓;\ (4,5):\ T_3=4\ (I=3,\ II=1,\ III=0)\ ✓$$
$$\textbf{O3}: \text{κ 的几何意义}: \text{三码字球至多一个公共点}\ ✓\ \Longrightarrow\ \text{三阶块的中心唯一}\ ✓\ (\text{每块的"中心"是其唯一公共点}\ ✓)$$
$$

## §6 下一刀候选（按判据筛选 ✓）

```
$$\text{① 用\textbf{minimality}压 II/III: 若 }\forall c\ \text{有私有点}\ ⟹\ \text{限制三角形/三邻点块}\ ⚠️\ (\text{未找到机制}\ ✗)$$
$$\text{② 改进 I 的常数: }I\le2A_2\ \text{已取等}\ ✗\ \Longrightarrow\ \text{不可能}\ ✗$$
$$\text{③ 反向用: 由 }Q_2\le T_3\le\tfrac{10}3A_2\ \text{得 }A_{\le2}\ \text{的\textbf{下界}}\ ✓\ (\text{方向不对}\ ✗)$$
$$\text{④ 混合: 对 }b(x)=k\ \text{按 }k\ \text{分层求上界（不用平均值）}\ ⚠️\ (\text{唯一未试}\ ✓)$$
$$

## §7 边界（诚实标注）

- §1–§3 全部**数值核验** ✓（n=4 全枚举 20 样本 ✓、n=5 全枚举 20 样本 ✓、n=9 我方构造 ✓）
- §2 的三条推导为**我方证明** ✓（II/III 的常数 2/3 依赖 κ≤1 ✓，已验 ✓）
- §4 明确记录**不足以闭合** ✗（未夸大 ✓）；**未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 T₃ 几何拆分 命中文件数=1    :: ./T3SPLIT-2026-09-26-geometric-split-and-A2-coupled-bound.md 
技术词 楔形数界     命中文件数=1    :: ./T3SPLIT-2026-09-26-geometric-split-and-A2-coupled-bound.md 
技术词 三阶块中心唯一 命中文件数=1    :: ./T3SPLIT-2026-09-26-geometric-split-and-A2-coupled-bound.md 
技术词 A≤2 耦合三阶界 命中文件数=1    :: ./T3SPLIT-2026-09-26-geometric-split-and-A2-coupled-bound.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：T₃ 几何拆分、楔形数界、三阶块中心唯一、A≤2 耦合三阶界
- **档案已有（引用，不列为提出）**：minimality、A≤2、excess
