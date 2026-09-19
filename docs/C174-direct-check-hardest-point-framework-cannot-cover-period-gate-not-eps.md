已查地图（**先查后写**）：`C-173`（改进阈值；`2-\sqrt3`）、`C-172`（近似周期引理）、`C-171`（联合靶子；`m'_M`）、`C-161`（`M=3` 极小点）、`C-170`（诊断：`\delta=0.0678`）。关键词回查：`直接检验判据`=0、`周期门槛`=0、`阈值误诊`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 17:52）**：**① 开 ① 之前，先对 `M=3` 最硬点做不经过解析不等式的直接检验 ② 以此判定"磨常数"还是"换框架"。**
**结论（先行）**：$$\textbf{(一)}\ ⚠️\ \textbf{我上一档的"只差 0.8%"是误诊，撤回}：\text{它拿}\ P=19\ \text{处的偏差去比阈值，但}\ P=19\ \textbf{不可准入}（19>\tfrac{5(M+1)}3=6.67）✗✗$$
$$\textbf{(二)}\ ⭐\ \textbf{直接检验（不经解析不等式）}：M=3\ \text{最硬点上}\ V:=\min_\psi\max_{k\le20}[\text{总和}]=1.881277✓$$
$$\qquad \text{而}\ m_3\le0.7641 \Longrightarrow V>m_3 \Longrightarrow \textbf{单调性步在该点成立}✓✓（\text{即：命题为真，是路线够不到}）$$
$$\textbf{(三)}\ ⭐\ \textbf{簿记更正（实质加强引理）}：\text{真需求是}\ \ge m_M，\text{不是}\ \ge M-1 ✗$$
$$\qquad \Longrightarrow \lambda\ \text{的可允许范围从}\ 0.2679\ \text{放宽到}\ \sim1.2（M=3），\ \varepsilon\ \text{阈值从}\ 24^\circ\ \text{放宽到}\ \sim51^\circ✓✓$$
$$\textbf{(四)}\ ⚠️\ \textbf{但框架仍}\ \textbf{定性} \text{够不到最硬点（这是}\ \textbf{周期门槛}，不是\ \varepsilon\ \text{阈值）}：$$
$$\qquad \text{在}\ \textbf{允许的}\ P\le6\ \text{内}，\varepsilon(P)=113.3^\circ,152.9^\circ,130.7^\circ,93.3^\circ,153.3^\circ,121.4^\circ \Longrightarrow \textbf{全部}\ \gg51^\circ ✗✗$$
$$\textbf{(五)}\ \Longrightarrow \textbf{判定}：\text{不要磨}\ \varepsilon\ \text{常数}✗（\text{它已宽到}\ 51^\circ）；\ \text{限制项是}\ \textbf{"存在小周期"} \text{这个前提}✗$$
$$\qquad \Longrightarrow \text{近似周期类}\ \textbf{在原理上} \text{覆盖不到最硬点} \Longrightarrow \text{应换结构性思路}✓$$

FREEZE-ACK: 本档即冻结期内的直接检验与判定更正（依 `§8.1`；不产候选结论）

D0: 本档对象 = **最硬点直接检验 ＋ 簿记更正（实质加强）＋ 周期门槛判定 ＋ 误诊撤回** —— 关系 = 检验、更正与判定，非新机制
D1: 0

# C-174 · ⚠️ **直接检验 + 两处更正：限制项是"周期门槛"，不是 `\varepsilon` 阈值**

> **唐先生 2026-09-19 17:52**：先做直接检验再决定磨细节还是换路 ✓

---

## §1 ⭐ 直接检验（不经任何解析不等式）

$$M=3\ \text{最硬点}：\varphi=(76.4304^\circ,\ 20.2320^\circ,\ 113.3311^\circ)✓$$
$$V:=\min_{\psi}\ \max_{1\le k\le20}\Big[\sum_{j\le3}\cos(k\varphi_j)+\cos(k\psi)\Big]\ =\ \mathbf{1.881277}✓（\text{最坏}\ \psi=104.211^\circ）$$
$$\text{对照}\ m_3：\text{下界}\ 0.5（\text{证书}）,\ \text{数值上界}\ 0.7641✓$$
$$\Longrightarrow V=1.881277\ \textbf{远大于}\ 0.7641 \Longrightarrow \textbf{单调性步在该点成立}✓✓$$
$$\qquad \text{解析界（经}\ \cos x\ge1-\tfrac{x^2}2\text{）}：M+\kappa_3(\lambda)=1.992484 \Longrightarrow \text{解析损失仅}\ 1.9925-1.8813=0.111✓$$

## §2 ⚠️ 更正一：簿记过强（实质加强引理）

$$\text{`C-172`/`C-173` 用的充分条件}：M+\kappa_3(\lambda)\ \ge\ M-1\quad✗\（\textbf{过强}）$$
$$\text{真需求}：M+\kappa_3(\lambda)\ \ge\ m_M✓\qquad(\text{而}\ m_M\approx0.2M\ \mathbf\ll\ M-1)✓$$
$$\Longrightarrow\ \text{可允许}\ \lambda：M=3\ \text{时到}\ \sim1.2（\text{而非}\ 0.2679），\ \text{即}\ \varepsilon\ \text{到}\ \sim51^\circ（\text{而非}\ 24^\circ）✓✓$$
$$\begin{array}{c|r|r|r}
\lambda & \kappa_3(\lambda) & M+\kappa_3 & \ge m_3(\le0.7641)?\\\hline
0.10 & -0.309148 & 2.6909 & ✓\\
0.20 & -0.878708 & 2.1213 & ✓\\
0.2679\ (2-\sqrt3) & -0.999913 & 2.0001 & ✓\\
0.50 & -1.395644 & 1.6044 & ✓\\
0.80 & -1.800000 & 1.2000 & ✓\\
1.00 & -2.000000 & 1.0000 & ✓\\
1.50 & -2.500000 & 0.5000 & ✗\\
\end{array}✓$$
$$\qquad （\kappa_3\ \text{表为全圆}\ 4\text{M}\ \text{点实算；}\kappa_3(\lambda)\ \text{单调下降}✓）$$

## §3 ⚠️ 更正二：一处计算 bug（已自捉）

$$\text{本档首轮曾用}\ \texttt{th[:1000001]}\ \text{取样} \Longrightarrow \text{只覆盖}\ [0,\pi/2] \Longrightarrow \text{得到假的"}\kappa_3(\lambda)=-\lambda\text{"}✗✗$$
$$\qquad \text{全圆重算后：}\kappa_3(0.3)=-1.0562（\text{非}\ -0.3）✓\ \text{已修正}✓$$
$$\qquad \text{与既有教训一致}：\textbf{结果异常先怀疑自己的实现}✓$$

## §4 ⚠️ 更正三：**"只差 0.8%"是误诊，撤回**

$$\text{`C-173`} §5\ \text{写}：M=3\ \text{最硬点}\ \delta=0.0678\ \text{（turn）}=0.426\ \text{rad}\ \text{vs 阈值}\ 0.4226\ \text{rad} \Longrightarrow "只差 0.8\%"✗$$
$$\qquad ⚠️\ \text{但那个}\ \delta\ \text{取自}\ q^*=19，\ \text{而准入条件要求}\ \textbf{3P}\le5(M+1)\ \Longrightarrow P\le6 ✗✗$$
$$\qquad \Longrightarrow \text{该比较}\ \textbf{在不可准入的}\ P\ \text{上做的} \Longrightarrow \textbf{无意义，撤回}✓$$

## §5 ⭐⭐ 真正的限制项：**周期门槛**

$$\text{在}\ \textbf{允许的}\ P\ \text{范围内（}P\le6\text{）重算}：$$
$$\begin{array}{c|r|r|r}
P & \varepsilon(P)=\max_j\mathrm{dist}(P\varphi_j,2\pi\mathbb Z) & M+\kappa_3 & \ge m_3?\\\hline
1 & 113.33^\circ & -6.0000 & ✗\\
2 & 152.86^\circ & -6.0000 & ✗\\
3 & 130.71^\circ & -6.0000 & ✗\\
4 & 93.32^\circ & -6.0000 & ✗\\
5 & 153.34^\circ & -6.0000 & ✗\\
6 & 121.39^\circ & -6.0000 & ✗\\
\end{array}✓$$
$$\Longrightarrow \text{全部}\ \varepsilon(P)\ge93^\circ \gg 51^\circ \Longrightarrow \textbf{近似周期框架在该点}\ \textbf{无一可用}\ P ✗✗$$
$$\qquad \Longrightarrow \text{限制项}\ \textbf{不是}\ \varepsilon\ \text{阈值（已宽到}\ 51^\circ\text{）}，\ \text{而是}\ \textbf{"存在小周期的近似通约配置"} \text{这一前提本身}✓$$

## §6 判定与后果

$$\textbf{① 不磨}\ \varepsilon\ \text{常数}✗：\text{它已从}\ 24^\circ\ \text{放宽到}\ \sim51^\circ，\ \text{再磨}\ 1\%\ \text{无意义}✓$$
$$\textbf{② 换路}✓：\text{近似周期类}\ \textbf{原理上} \text{覆盖不到最硬点（}\varepsilon(P)\ge93^\circ\ \text{在全部准入}\ P\ \text{上）}✗$$
$$\textbf{③ 但引理本身}\ \textbf{被加强}：\text{阈值}\ \varepsilon\le\sim51^\circ\ \text{（配置无关量级）}✓✓\ —— \text{可写入论文}✓$$
$$\textbf{④ 命题与路线的分离}：\text{直接检验证明}\ \textbf{命题在该点为真}（V=1.881>m_3）✓，\ \text{是}\ \textbf{路线} \text{够不到}✓✓$$

## §7 边界与回查

- ⚠️ §1 的 `V` 为**数值扫描**（`\psi` 网格 400001；`k\le20` 全枚举）✓ —— 比解析界紧，但仍是数值 ✓
- ⚠️ §2 的表为**实算**（全圆 4M 点）✓；`\kappa_3` 单调下降已核 ✓
- ⚠️ §4 的撤回依据是**准入条件 `3P\le5(M+1)`**（引理自身的假设）✓
- ⚠️ **不声称** `(\text{RP}_M)` 一般成立；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓；本档两次自捉计算/比较错误 ✓）

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 18:0x）`[纪律]`（先跑后写）

```
技术词 直接检验判据  命中文件数=0 ::  ⟹ 本档新增
技术词 周期门槛     命中文件数=0 ::  ⟹ 本档新增
技术词 阈值误诊     命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
