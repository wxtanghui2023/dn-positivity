已查地图（**先查后写**）：`acpc-minimal-test.md`（C＝逐点积 Hadamard 积 "无简单 ζ 表达——谱非显然"）、`acpc-loop-death.md`（链退化，只判链部分）、`viii-monodromy-derivation.md`（P(s) 奇点＝缩放轨道、延延必经 log ζ）、`CREATE-SPEC-4/5`（(iv′) 修正＋引理＋第四子类五成员）、`V188` §2（线性通道饱和）。关键词回查：`Hadamard 积`＝8 档（**皆指 Hadamard 分解**，与系数侧 Hadamard 积同名不同物）、`第四子类`＝1 档（本会话）、`素数限制系数`/`系数侧 Hadamard 积`＝0 档。结论：**M5 为第四子类唯一未判死成员 ⟹ 本档以三档对照实验判之** ✓

# CREATE-SPEC-6 · **(甲-1 终判 + 甲-2 文献核查)：M5 判死（带对照实验）＋ 引理的文献定位**

> **时间**：2026-09-18 21:40 唐先生：**「A，B」** ⟹ (A) 引理文献核查 ＋ (B) 测 M5 ✓

FREEZE-ACK: 本档即冻结期内的数值实验与文献核查（依 `§8.1`；不产候选结论）

D0: 本档对象 = M5 的**判死**（带对照实验）＋ 引理的**文献定位** —— 关系 = 实验判定与文献核查，非新机制
D1: 0

---

## §0 结论（先行）

$$\textbf{(B)}\ ⭐\ \textbf{M5 判死}：\text{C 级数}\ \textbf{对零点完全不可见}（\text{去趋势后}\ |D_C|\ \text{在}\ \gamma\ \text{处}\ \approx1.00,\ \text{局部极大}>1.05\ \textbf{共 0 个}）✓✓$$
$$\qquad \text{而}\ \textbf{同截断} \text{下的正对照}\ D_\Lambda\ \text{有}\ \textbf{50 个} \Longrightarrow \text{截断不是原因} \Longrightarrow \textbf{盲}✓✓$$
$$\Longrightarrow \textbf{第四子类五成员全死} \Longrightarrow \text{第四子类在已知成员上}\ \textbf{为空}✓✓$$
$$\textbf{(A)}\ \text{引理}\ Z(fg)=Z(f)\cup Z(g)\ \textbf{无具名来源} \Longrightarrow \textbf{folklore}（\text{如预期}）✓$$
$$\qquad ⭐\ \text{但所得}\ \textbf{方向有可引文献缺口}：\text{Tao（Polymath15）逐字承认}\ \textbf{"反向（}\Lambda\to\ \text{零-free 区域）虽可设想但未尝试"}✓✓$$

---

## §1 (B) M5 的判定实验（三档对照）

$$\text{对象}：C(n)=A(n)M(n),\quad D_C(T)=\Bigl|\sum_{n\le N}C(n)n^{-1/2-iT}\Bigr|,\quad N=4\times10^4✓$$
$$\text{对照一（正）}：D_\Lambda(T)=\Bigl|\sum_{n\le N}\Lambda(n)n^{-1/2-iT}\Bigr|\approx|\zeta'/\zeta(\tfrac12+iT)| \Longrightarrow \text{极点即在}\ \gamma✓$$
$$\text{对照二（负）}：\text{同支撑随机符号}\ C_{\mathrm{rand}}✓$$

### 第一次运行（未去趋势）⟹ 假信号警报

| | max/中位数 | 与 $D_\Lambda$ 相关 |
|:--|:--|:--|
| $D_\Lambda$ | **46.64** | 1.000 |
| $D_C$ | 18.72 | ⚠️ **0.926** |
| $D_{\mathrm{rand}}$ | 2.43 | 0.018 |

$$\Longrightarrow \text{乍看 }D_C\ \text{强相关}；\ \textbf{但} \text{在}\ \gamma\ \text{处}\ D_C/\text{中位}\approx1.000\text{–}1.035 \Longrightarrow \text{无}\ \textbf{局部} \text{信号}$$
$$\qquad \Longrightarrow \text{判定}：0.926\ \text{是}\ \textbf{"共同增长趋势"}\ \text{造的}\ \textbf{假相关} \Longrightarrow \textbf{必须去趋势复测}✓✓$$

### 第二次运行（去趋势，滑动窗 400）⟹ **决定性**

$$\text{去趋势后相关}：\operatorname{corr}(d_C,d_\Lambda)=\mathbf{0.273}\（\text{假相关消失}）;\ \operatorname{corr}(d_R,d_\Lambda)=-0.134✓$$

| $\gamma$ | $d_C(\gamma)$ | $d_\Lambda(\gamma)$ | $d_{\mathrm{rand}}(\gamma)$ |
|:--|:--|:--|:--|
| 14.135 | **0.998** | 1.434 | 0.245 |
| 21.022 | **0.997** | 1.136 | 1.220 |
| 25.011 | **1.010** | 0.562 | 0.918 |
| 30.425 | **1.008** | 0.781 | 1.534 |
| 32.935 | **0.992** | 1.595 | 0.465 |
| 37.586 | **0.988** | 1.135 | 1.451 |
| 40.919 | **1.005** | 1.532 | 1.100 |
| 43.327 | **1.012** | 1.222 | 0.959 |
| 48.005 | **1.007** | 1.799 | 0.808 |
| 49.774 | **1.004** | 2.066 | 1.318 |

$$\textbf{去趋势后局部极大数}（>1.05）：d_\Lambda=\mathbf{50},\quad d_C=\mathbf{0},\quad d_{\mathrm{rand}}=44✓✓$$
$$\Longrightarrow \boxed{D_C\ \textbf{在}\ \gamma\ \text{处毫无结构}（\text{连噪声都不如}）} \Longrightarrow \textbf{对零点盲}✓✓$$
$$\qquad ⚠️\ \text{关键}：\text{正对照}\ D_\Lambda\ \textbf{同截断}（N=4\times10^4）\ \text{却给出 50 个峰} \Longrightarrow \textbf{截断不是原因}✓✓$$

## §2 (B) 判定与载体

$$\textbf{结论}：M5\ \text{死在}\ \textbf{(iii) 极限恢复零结构} \Longrightarrow \textbf{第四子类五成员全死}（M1\text{–}M5）✓✓$$
$$\qquad \text{机制解释}：C=AM\ \text{是}\ \textbf{两个无零点信息的序列的逐点积} \Longrightarrow \text{振荡在乘性中被"抹平"}（\text{`acpc-minimal-test` 已记录"C 的主项平滑"}）✓$$
$$\qquad \text{与控制对照一致}：\text{正对照（}\Lambda\ \text{级数，}\textbf{直接来自}\ -\zeta'/\zeta\text{）有信号};\ \text{C 级数无}✓✓$$
$$\text{脚本}：\texttt{/tmp/m5\_test.py},\ \texttt{/tmp/m5\_detrend.py}（\text{临时；如需入仓请指示}）✓$$

## §3 (A) 引理的文献核查

$$\text{检索关键词}：\text{"operations moving zeros of zeta"},\ \text{"deformation分类"},\ \text{"completion factor zero-free"},\ \text{"de Bruijn–Newman 唯一典范变形"}✓$$
$$\text{结果一}：\textbf{引理}\ Z(fg)=Z(f)\cup Z(g)\ \textbf{无具名来源} \Longrightarrow \textbf{folklore}（\text{与"}\operatorname{ord}\ \text{等式直接改写"一致}）✓$$
$$\qquad \Longrightarrow \textbf{小注记的定位应为}\ \textbf{说明性}\（\text{除非其}\ \textbf{应用} \text{部分有新意}）✓✓$$
$$\text{结果二} ⭐\ \textbf{可引文献缺口（Tao, Polymath15 博客）逐字}：$$
$$\qquad \text{"The literature so far has }\textbf{almost exclusively focused on implications of the form 'information about zeroes of zeta'}\to\text{'information about the de Bruijn–Newman constant'}\text{, with the notable exception of course of the implication }\Lambda\le0\Rightarrow\mathrm{RH}\text{. It is conceivable that one could work on }\textbf{the converse}\text{ and eventually show, for instance, that }\textbf{smallness of }\Lambda\ \textbf{implies a zero free region for zeta}\text{... But ... I would imagine that this would be an }\textbf{extremely inefficient route}\text{"}✓✓$$
$$\Longrightarrow \text{三点可用}：$$
$$\qquad \text{(i)}\ \text{文献}\ \textbf{已研方向＝"零点}\to\Lambda\text{"};\quad \text{(ii)}\ ⭐\ \textbf{反向（}\Lambda\to\ \text{零-free 区域）"可设想但未尝试"} \Longrightarrow \textbf{我们 (iv$'$) 的攻向有具名缺口}✓✓$$
$$\qquad \text{(iii)}\ ⚠️\ \text{但 Tao 同段}\ \textbf{自评"极其低效"} \Longrightarrow \text{该方向}\ \textbf{有先验悲观} \text{，引用时须一并写出}✓✓$$
$$\text{结果三}：\text{Wikipedia 条目确认 FE 因子}\ \chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\ \text{的}\ \sin\ \text{零点被}\ \Gamma\ \text{的极点抵消} \Longrightarrow \text{（平凡零点）}\ \text{与本档 §1 的}\ (iv')\ \text{修正一致}✓$$

## §4 小注记的处置（依 (A) 结果）

$$\text{现状}：\texttt{papers/zero-free-factor-lemma/note.md}\ \text{已写（引理＋三推论）}✓$$
$$\qquad \textbf{定位调整} \text{（依 §3 结果一）}：\text{引理 folklore} \Longrightarrow \text{注记的}\ \textbf{可主张内容} \text{仅剩}：$$
$$\qquad \qquad \text{(a)}\ \text{把三类"不移动零点"变形}\ \textbf{归类};\quad \text{(b)}\ \text{指出}\ \textbf{第四类（非乘性＋系数侧）在本会话五成员全死（含 M5 数值判死）}✓$$
$$\qquad \Longrightarrow ⚠️\ \text{(b) 的"全死"是}\ \textbf{有界类内} \text{结论（非定理）} \Longrightarrow \text{注记须显式写此限定}✓✓$$
$$\qquad \text{建议}：\text{定位为}\ \textbf{内部说明性注记};\ \text{若未来有第四类的真实例，再考虑对外}✓$$

## §5 边界与回查

- ⚠️ (B) 为**数值判定**（$N=4\times10^4$、$T\in[2,60]$、步长 0.005）；**正负对照齐备** ⟹ 判死的**可信度高于**无对照者 ✓
- ⚠️ (B) 的**截断上限**：$N=4\times10^4$；正对照在同一截断下给出信号 ⟹ **截断被排除为原因**（此为本档的关键论证）✓
- ⚠️ (A) 的 Tao 引文为**检索片段级**（`[外搜·未读全文]`），引用前须核原文（Polymath15 博客）✓
- ⚠️ 本档**不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 21:4x）`[纪律]`（先跑后写）

```
技术词 去趋势复测        命中文件数=1  :: ./CREATE-SPEC-6-…（本档）
技术词 假相关           命中文件数=1  :: ./CREATE-SPEC-6-…（本档）
技术词 反向方向         命中文件数=1  :: ./CREATE-SPEC-6-…（本档）
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增** ✓
