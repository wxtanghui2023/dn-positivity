# 论文骨架 · 短窗口余弦和的极小极大问题

已查地图（**先查后写**）：`C-144`（Case A）、`C-152`–`C-155`（`M=2` 完整；`M=3` 证书）、`C-158`/`C-159`（`\kappa_N`；鸽笼定理；周期单调性）、`C-160`（多点两障碍）、`C-161`–`C-169`（证书；附录）、`C-170`/`C-171`（`(c)` 诊断；靶子否证）、`E4-ENGINE-2`（引理 C）、`papers/palojarvi-constant/note.md`（`m\ge2` 缺口）。关键词回查：`窗口余弦和`=0、`极小极大常数`=0（**本档新增**）、`论文骨架`=1（`C-152`，**复用**）。
**本档任务（唐先生 2026-09-19 15:32 决定）**：**停止攻联合靶子；把已确定的结果整理成论文骨架。**
**本档定位**：**收束与产出**（不产新数学结论）✓

D0: 本档对象 = **论文骨架（`M\le5` 严格结果 ＋ 一般情形困难分析 ＋ 严格定位）** —— 关系 = 整理与登记，非新机制
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产新数学结论）

---

## §0 定位（一句话）

$$\text{本论文}\ \textbf{不} \text{证明一般}\ M\ \text{的}\ (\text{RP}_M)；\ \text{它对}\ \textbf{若干具体子情形} \text{给出}\ \textbf{严格、可独立复核} \text{的答案}，$$
$$\qquad \text{并把一般情形的困难}\ \textbf{具体化、定量化、诚实登记} \text{为开放问题。}$$

---

## §1 标题与摘要（草案）

$$\textbf{标题}：\text{短窗口余弦和的极小极大问题}：M\le5\ \text{的严格结果与一般情形的困难分析}$$
$$\textbf{English}：\text{Minimax of short-window cosine sums: rigorous results for}\ M\le5\ \text{and an analysis of the general case}$$
$$\textbf{摘要（草案）}：$$
$$\qquad \text{记}\ m_M:=\min_{\varphi\in[0,\pi]^M}\max_{1\le k\le5M}\sum_{j=1}^{M}\cos(k\varphi_j)✓$$
$$\qquad \text{本论文证明}\ m_M\ge\tfrac12\ \text{对}\ 1\le M\le5（M=1,2\ \text{取等}；M=3,4,5\ \text{有余量}）；$$
$$\qquad \text{等价地}：\forall z_1,\dots,z_M\in\mathbb C,\ |z_j|=1,\ M\le5：\exists k\le5M,\ \Re\sum_j z_j^k\ge\tfrac12✓$$
$$\qquad \text{方法}：M=1\ \text{为初等引理（}60^\circ\ \text{取等）；}M=2\ \text{为显式局部分析＋认证远场；}$$
$$\qquad M=3,4,5\ \text{为自适应分支定界证书（每箱精确下界 ＋ 保守浮点 ＋ 可复现 manifest）✓}$$
$$\qquad \text{另证}：\text{（i）单点锐定理}\ \max_{k\le N}\cos(k\theta)\ge\cos\tfrac{2\pi}{N+1}（三行鸽笼，最优）；$$
$$\qquad \text{（ii）对一切}\ M\ \text{成立的"Case A"；\ （iii）小公共周期配置的部分单调性引理；}$$
$$\qquad \text{（iv）}m_M\le\sqrt{2M\ln(10M)}\le M-1\ (M\ge12)✓$$
$$\qquad \text{并}\ \textbf{定量登记} \text{通向一般}\ M\ \text{的若干自然路线的障碍（计数、联立丢番图逼近、证书的}\ N^M\ \text{代价）✓}$$

---

## §2 贡献清单（含**严格状态**）

$$\begin{array}{c|l|l}
\# & \text{结果} & \text{状态}\\\hline
1 & \text{引理 C：}|z|=1\Rightarrow\max_{k\le5}\Re z^k\ge\tfrac12\ （60^\circ\ \text{取等}） & \textbf{已证}（初等）\\
2 & \text{鸽笼定理：}\max_{k\le N}\cos(k\theta)\ge\cos\tfrac{2\pi}{N+1}（最优） & \textbf{已证}（三行）\\
3 & \text{定理 1（}M=2\text{）：}\max_{k\le10}\ge\tfrac12 & \textbf{已证}（三段拼装）\\
4 & \text{定理 2--4（}M=3,4,5\text{）：}\max_{k\le5M}\ge\tfrac12 & \textbf{证书}（\text{`M=3`}\ \text{已有区间算术版（}\text{`C-177`}\text{）；其余为双实现＋误差模型}）\\
5 & \text{Case A（任意}\ M\text{）：}\ge\tfrac{2M}3+\tfrac13\ \text{点在}\ \pi\mathbb Z\ \text{附近}\Rightarrow f(2)\ge\tfrac12 & \textbf{已证}（三行）\\
6 & \text{周期单调性引理（}\mathrm{lcm}\le5(M+1)\ \text{类）} & \textbf{已证}（用\ \#2）\\
7 & m_M\le\sqrt{2M\ln10M}\ (M\ge12\ \Rightarrow\ \le M-1) & \textbf{已证}（概率方法）\\
8 & \text{一般}\ M\ \text{的困难分析 ＋ 开放问题} & \text{登记（本论文的诚实部分）}\\
9 & \text{近似周期单调性引理 ＋ 其推论（}\text{`C-172`}\text{；}\text{`C-176`}\ \text{关闭数值输入；}\text{`C-174`}\ \text{加强）} & \textbf{已证}（\text{引理三行；推论现无条件}）\\
10 & \text{一维极小极大}\ \kappa_N(\lambda)\ \text{与闭式}\ \lambda_{\max}=2-\sqrt3 & \textbf{已证}（\text{解析}）＋\ \text{1-D 证书}\\
11 & m_M\le M-1\ \text{对一切}\ M\ge2 & \textbf{已证}（\text{区间算术证书}\ \text{`C-176`}；\text{概率方法}\ \text{`C-159`}）\\
\end{array}✓$$

---

## §3 章节结构（7 节 ＋ 3 附录）

**§1 引言**：(RP_M) 的来源（Montgomery–Palojärvi 引理 2.2）；阻尼 vs 无阻尼；本论文的覆盖范围 ✓
$$\text{§2 初等结果}：\text{引理 C；鸽笼定理及其最优性（}\kappa_N=\cos\tfrac{2\pi}{N+1}）✓$$
$$\text{§3}\ M=2\ \text{的完整证明}：\text{局部符号（}c=\tfrac{28\sqrt{1677}}{559}）＋\text{远场认证}＋\text{覆盖包含}✓$$
**§4 证书方法（M=3,4,5）**：每箱精确下界；三行正确性；保守化；双实现交叉核验；误差模型核验 ✓
$$\text{§5 对一切}\ M\ \text{成立的结果}：\text{Case A；周期单调性引理；}m_M\le M-1✓$$
**§6 一般 M 的困难分析**：单调性归约；新鲜窗口现象；被否的充分条件；联合靶子 ✓
$$\text{§7 开放问题}：\text{逐条列出（见 §5）✓}$$
$$\text{附录 A 证书复现}；\text{附录 B 数值表}；\text{附录 C 与文献的关系（含撤回记录）}✓$$

**§2 表尾**：第 9、10 行 —— 近似周期单调性引理（C-172/C-174）；一维极小极大 κ_N(λ) 与闭式 2−√3（C-173）✓
---

## §4 各节要点与**证据位置**

$$\text{§1}：\text{Palojärvi 2019 Lemma 2.2 逐字（本地 PDF p.6）}：\max_j|z_j|=1\Rightarrow\max_{1\le n\le5M}\Re\sum_jz_j^n\ge\tfrac1{20}✓$$
$$\qquad ⚠️\ \textbf{作用域差异必须写清}：\text{引理 2.2 允许}\ |z_j|<1（\textbf{阻尼}）；\text{本论文结果针对}\ \textbf{所有}\ |z_j|=1✓$$
　　⚠️ **不得** 写成"把引理 2.2 的常数改进 10 倍"（该表述已在 C-157 撤回）✓
**§2**：引理 C（E4-ENGINE-2）；鸽笼定理三行证明（C-159）；κ_N 表（C-158）✓
$$\text{§3}：\text{局部引理（单纯形权重、}\lambda=(0,0,7/12,5/12,0)、c=\tfrac{28\sqrt{1677}}{559}\approx2.05122\text{）}✓$$
$$\qquad \text{远场：}L=10\sqrt2\ \text{、格点}\ N=1500\ \text{、认证下界}\ 0.56662>\tfrac12\ \text{、覆盖包含}\ 2.9133^\circ<3.6727^\circ✓$$
$$\qquad \text{源}：\text{`C-152`}\text{、`C-153`}\text{、`C-154`}✓$$
$$\text{§4}：\mathrm{LB}(B)=\max_k\sum_j\min_{[a_j,b_j]}\cos(k\varphi_j)\ \text{的三行正确性；}\mathrm{SLACK}=10^{-12}、\mathrm{TEST\_EPS}=10^{-9}✓$$
$$\qquad \text{三情形：}M=3\ (17{,}440\ \text{箱；余量}\ 0.002005)；M=4\ (1{,}036{,}096；0.000210)；M=5\ (72{,}440{,}000；3.957\times10^{-6})✓$$
$$\qquad \text{双实现逐位一致（}M=3,4\text{）；误差模型：}M=3\ \text{逐参数}\ 1{,}569{,}600\ \text{个；范围抽样三档，均}\ 9007\times\ \text{裕度✓}$$
$$\qquad \text{源}：\text{`C-161`}\text{–`C-169`}＋\texttt{cert\_appendix/manifest.json}\ (\text{哈希}\ \mathtt{7404cb37e7258940})✓$$
**§5**：Case A（C-144）；周期单调性引理（C-159）；m_M ≤ √(2M ln 10M)（C-159）✓
**§5′-新节**：近似周期单调性引理（C-172）＋ 簿记更正后阈值 ε ≤ ~51°（C-174）＋ 一维极小极大 κ_N(λ) 与闭式 λ_max = 2−√3（C-173）✓
**§6**：单调性归约（C-156）；新鲜窗口（C-157、C-170）✓
　　**周期门槛（C-174）**：在引理自身准入条件 3P ≤ 5(M+1) 内，M=3 最硬点的 ε(P) ≥ 93°（全部 P ≤ 6）≫ 阈值 51° ⟹ 近似周期类【原理上】覆盖不到最硬点 —— 这是路线的定性限制，如实登记于 §6 ✓
　　**被否的充分条件**（C-171：m'_M < m_M+1，含 m'_1 = κ_10 = cos(2π/11)）；**联合靶子（保留）** ✓
$$\qquad \text{两障碍：联立逼近需}\ K\sim K^2；\text{宽松计数在}\ M\ge8\ \text{失效（}\text{`C-160`}）；\ N^M\ \text{代价（}\text{`C-166`}\text{、`C-168`}）✓$$

---

## §5 开放问题（**逐条、可引用**）

$$\textbf{OP-1}\ （\text{主问题}）：(\text{RP}_M)\ \text{对一切}\ M\ \text{是否成立}？\ \text{等价}：m_M\ge\tfrac12\ \forall M✓$$
$$\textbf{OP-2}：\text{单调性}\ m_{M+1}\ge m_M\ \text{是否成立}？\ （\text{一旦成立} \Longrightarrow \text{OP-1}，\text{配}\ m_1=m_2=\tfrac12）✓$$
$$\textbf{OP-3}\ （\text{联合靶子}）：\forall\varphi,\psi：\max_{k\le5(M+1)}[\sum_{j\le M}\cos(k\varphi_j)+\cos(k\psi)]\ \ge m_M✓$$
$$\qquad \text{证据}：\text{两类最硬配置上余量}\ 0.22\text{–}1.10\ （\text{`C-170`}\text{、`C-171`}）✓$$
**OP-4**：m_M 的精确值（已知 M ≤ 5 的下界 1/2；数值上界：0.5, 0.5, ≤0.7641, ≤0.8109, ≤1.0270）✓
$$\textbf{OP-5}：\textbf{阻尼版}（\max_j|z_j|=1，\text{即引理 2.2 原形}）\ \text{的最优常数}：\text{数值}\ d_M\approx0.36\text{–}0.40\ \text{vs}\ \tfrac1{20}✓$$
**OP-6**：一维极小极大 κ_N(λ) = inf_θ max_{m≤N}[cos(mθ) − λm²] 的一般 N 与精确形式（已得：N=3 时 λ_max = 2−√3，闭式；N=3 的 1-D 证书 59 区间）✓

---

## §6 附录清单

$$\text{附录 A}：\text{证书复现——三条命令＋manifest＋哈希＋误差模型记录（}\text{`C-169`}）✓$$
**附录 B**：数值表 —— m_M（M ≤ 11）、m'_M、d_M、对偶间隙 c_M、κ_N（N ≤ 20）✓
**附录 B**：数值表 —— 已有各项，＋【κ_3(λ) 全圆表】（C-174 §2，λ ≤ 0.8）✓
$$\text{附录 C}：\text{与文献关系——引理 2.2 逐字；}\textbf{撤回记录} \text{（"10 倍"表述）}；\text{阻尼／无阻尼之辨✓}$$

---

## §7 投稿前待办（**简短清单**）

$$\text{①}\ \text{把}\ M=5\ \text{的误差模型做一次}\ \textbf{更细的核验}（\text{范围抽样}\to\text{分层抽样或等价论证}）✓$$
$$\text{②}\ \text{区间算术版本（形式化闭合浮点缺口）；可选：Lean 形式化}\ \mathrm{LB}\ \text{不等式✓}$$
③ m_M 的上界（OP-4）做更稳的全局优化，并标注"数值上界"✓
$$\text{④}\ \text{文献核查：鸽笼定理／}\kappa_N\ \text{的逐字出处（Fejér 族常数）✓}$$
$$\text{⑤}\ \text{语言与体例：正文用英文；证书脚本与 manifest 作为补充材料✓}$$

---

## §8 边界声明（必须写入论文）

- ⚠️ \textbf{不声称}一般 `M` 的 `(\text{RP}_M)`；**不声称**任何与 RH 的关系（本项目另有线索，本文不涉及）✓
- ⚠️ 证书为**计算机辅助**；严格性依赖三行不等式 ＋ 保守化 ＋ 误差模型核验（已做，残留为形式化）✓
- ⚠️ `m_M` 的上界为**启发式优化**所得，须标"数值上界"✓
- ⚠️ 引用引理 2.2 时必须写**作用域差异**（阻尼 vs 无阻尼）✓
