# V190 · ⭐⭐⭐⭐⭐ **受约束外部搜索（按 F3／F1／F2 预筛）—— 找到 F3 分类之外的**首个具名通道**：稳定性／全正性（LP-class／hyperbolicity／TP-PF），且**通过 F1（支撑级信息）与 F2（不同轴）** ⟹ 判定 **ALIVE（不封）** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 13:04：**"有了这些前提条件和约束后，再搜索一次所有的物理和数学模型，看看有没有适配我们研究的"**
> 方法 ✓ **不再凭"像不像"，而是用 `V189` 的三筛做预筛**：F3 先归类 → F1 判"是否携带新的独立信息" → F2 判"控制到哪一层"；凡回归线性／二次／逐点者即停
> 检索 ✓ 多轮（web／tavily）：稳定性保持算子／全正性与 Pólya 频率／Pólya 判据与实零点傅里叶变换／Jensen 多项式与 Turán 不等式
> 执行 ✓ 小灵（**§1 通道 S 的判定 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓（仅作等价性引用）；未跑 Lean ✓｜编号 ✓ **V190**

---

## §0 判定（一 ALIVE ＋ 四回归／工具）

**① 找到 1 个 ALIVE 候选：通道 S ＝「稳定性／全正性」（hyperbolicity／LP-class／TP-PF）✓✓✓**

$$\text{F3 归类}：\textbf{other}\（\text{既非 linear，亦非 quadratic／signature，亦非 pointwise}\bigr)\ ——\ \text{它是}\ \textbf{F3 "other" 的首个具名占位者} ✓✓$$
$$\text{F1 判定}：\textbf{通过} —— \text{它携带}\ \textbf{支撑级信息}（\text{§1.2}）,\ \text{而 F1 恰指出"线性统计量}\textbf{不能直接分辨}\ \text{支撑性质"} ✓✓✓$$
$$\text{F2 判定}：\textbf{不适用／新轴} —— \text{其缺口按}\ \textbf{(d,n)}\ \text{指标化}，\ \textbf{不是}\ T\ \text{的涨落尺度} ✓✓$$

**② 另有 4 项：1 项回归（二次型通道）、3 项为工具／地图 ✓**

**③ 这是本晚外部搜索中**第一个未被我们四通道表覆盖、且未被封**的具体候选 ✓✓✓**

---

## §1 通道 S：稳定性／全正性（LP-class／hyperbolicity／TP-PF）

### 1.1 位置

$$\text{核心对象}：\text{一族}\ \textbf{算术定义的多项式}\ \text{的}\ \textbf{实根性／双曲性}（hyperbolicity）,\ \text{以及保持它的算子类}$$
$$\qquad ⚠️\ \text{与}\ \text{`V187`／`V188`}\ \text{的四通道对照}：\text{linear}\（\text{盲}\bigr）|\ \text{quadratic}\（\text{Weil／Li}\bigr）|\ \text{signature／inertia}\（\text{终点退回正性}\bigr）|\ \text{pointwise}\（S(T)\bigr）\ ——\ \textbf{均不覆盖本通道} ✓✓$$

### 1.2 ⭐ F1：独立信息 ＝ 支撑级（本档核心正面判断）

$$\textbf{Bochner（二次型通道）}：f\ \text{正定}\ \Longleftrightarrow\ f\ \text{是}\ \mathbb R\ \text{上}\ \textbf{正测度的傅里叶变换}\ ——\ \textbf{对测度支撑无限制} ✓$$
$$\textbf{Schoenberg（本通道）}：f\ \text{是全正／Pólya 频率函数}\ \Longleftrightarrow\ f\ \text{是}\ \mathbb R_{\ge0}\（\textbf{半直线}\bigr）\ \text{上正测度的拉普拉斯变换}\ ——\ \textbf{支撑被限制在一侧} ✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{该通道比二次型通道}\ \textbf{严格更强}：\text{它把}\ \textbf{支撑信息}\ \text{编码进去}};\ \text{而}\ \textbf{支撑信息}\ \text{正是 F1 说"线性统计量不能直接分辨"的那一类} ✓✓✓$$
$$\qquad ⚠️\ \text{等价形式（现代）}：\text{全正性／}\textbf{变差缩减}\（\text{variation diminishing}\bigr）/\ \textbf{全子式非负}（\text{all minors}\bigr）\ ——\ \textbf{不是}\ \text{有限阶、}\textbf{不是}\ \text{二次型} ✓$$

### 1.3 关键事实链（经典）＋ 近期真进展

$$\textbf{Pólya (1927)}：\text{记}\ (-1+4z^2)\Lambda\!\left(\tfrac12+z\right)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n},\ \text{及}\ J_\gamma^{d,n}(x)=\sum_{j=0}^{d}\binom dj\gamma(n+j)x^j$$
$$\qquad\Longrightarrow\ \boxed{\text{RH}\ \Longleftrightarrow\ \textbf{全部}\ J_\gamma^{d,n}\ \text{双曲（全实根）}\（\text{对所有 }d\ge0,\ n\ge0\bigr）} ✓✓$$
$$\textbf{近期进展（Griffin–Ono–Rolen–Zagier, PNAS 2019, arXiv:1902.07321；被引 180+）} ✓✓✓：$$
$$\qquad\text{(i)}\ \text{对}\ \textbf{每个}\ d\ge1\ \text{存在}\ N(d)\ \text{使}\ n\ge N(d)\ \text{时}\ J^{d,n}\ \textbf{双曲} ✓\（\text{"高 }n\ \text{全部成立"}\bigr）$$
$$\qquad\text{(ii)}\ \text{对}\ 1\le d\le8\，\ \textbf{全部}\ n\ge0\ \text{双曲} ✓\（\text{此前最好}\ d\le3\bigr）$$
$$\qquad\text{(iii)}\ \text{方法}：\text{重正化 Jensen 多项式}\ \to\ \textbf{Hermite 多项式}\ H_d\（\text{实根}\bigr）\ \Longrightarrow\ \text{大 }n\ \text{双曲} ✓$$
$$\qquad\text{(iv)}\ \text{数值}：\text{"Analysis + Computer}\Longrightarrow d\le10^{20}\ \text{双曲"} ✓$$
$$\qquad\text{(v)}\ \text{作者自述}：\textbf{未发明新技术／新对象};\ \text{只是}\textbf{复活了 Jensen–Pólya 这条被认为已死的路线} ✓$$
$$\textbf{同通道的经典支撑}：\text{Csordas–Norfolk–Varga}\ \text{（Turán 不等式；解 Pólya 58 年问题）}\（\text{对应}\ d=2\ \text{情形}\bigr）;\ \text{Newman／Cardon"Fourier transforms with only real zeros"} ✓$$

### 1.4 ⭐⭐ 缺口结构（**与 $S(T)$ 不同轴**）

$$\text{RH}\ \Longleftrightarrow\ \text{所有}\ (d,n)\ \text{无例外};\ \text{已知}：\text{高 }n\ ✓\（\text{所有 }d\bigr）、\text{小 }d\ ✓\（d\le8，\text{全部 }n\bigr）$$
$$\Longrightarrow\ \text{缺口}\ =\ \text{中等／大}\ d\ \text{且}\ \textbf{小}\ n\ \text{的}\ \textbf{例外集} ✓$$
$$\qquad ⚠️\ ⭐\ \text{注意形状}：\text{对}\ \textbf{每个}\ d\ \text{只有}\ \textbf{有限多}\ n\ \text{例外} ⟹ \text{缺口是"}\textbf{每度有限的例外集族}"， \textbf{不是渐近墙} ✓✓$$
$$\qquad\Longrightarrow\ \text{故 F2 的三层阶梯（}\sqrt{\log\log T}/O(\log T)/O(\log T/\log\log T)\bigr)\ \textbf{不适用};\ \text{本通道有}\ \textbf{自己的缺口几何}（d\ \text{vs}\ n）✓✓$$

### 1.5 同通道的现代工具与一刀

$$\text{(a)}\ \textbf{Borcea–Brändén}\ \text{稳定性保持算子分类}：\text{用算子}\ \textbf{symbol}\ \text{判定是否保稳定／保实根} ✓\（\text{可用于}\ \textbf{构造／否定}\ \text{保持算子}\bigr）$$
$$\qquad\text{(b)}\ ⚠️\ \textbf{Belton–Guillot–Khare–Putinar（2021/22）}\ \text{的}\ \textbf{TP-保持算子分类}：\text{在无限全序集上（存在 TP}_2\ \text{核时）}\ \textbf{TP 保持算子只有正齐次}（\text{positive homothety}\bigr）$$
$$\qquad\qquad\Longrightarrow\ \textbf{一刀}：\text{若坚持}\ \textbf{无限阶全正}\ \text{的保持算子，则保持类过窄（只有缩放）} ⟹ \text{该子通道}\ \textbf{不可用} ✓✓$$
$$\qquad\qquad ⟹\ \text{故要用的应是}\ \textbf{稳定性（Hyperbolicity）保持算子}\（\text{Borcea–Brändén；类很丰富}\bigr）,\ \textbf{而非}\ \text{无限阶 TP 保持算子} ✓✓$$

### 1.6 诚实风险（三条，必须随本档携带）

$$\textbf{(R-a)}\ \text{Pólya 1927 是}\ \textbf{RH 等价改写} ⟹ \text{按}\ \text{`V149`}\ \text{的教训：}\textbf{等价改写不自动带来新输入} ✓$$
$$\textbf{(R-b)}\ \text{本档的正面判断（"独立信息＝支撑级"）}\ \textbf{尚未证明}\ \text{能提供}\ \textbf{新的可证输入};\ \text{"携带独立信息"}\neq\text{"能被无条件确立"} ✓$$
$$\textbf{(R-c)}\ \text{缺口（中等 }d\ \text{、小 }n\text{）与}\ \textbf{低零点／小高度}\ \text{可能}\ \textbf{同源} ⟹ \text{可能隐藏同一核心难点} ✓$$

---

## §2 其余候选判定（✓ 预筛结果）

$$\textbf{(2.1)}\ \text{2026 综述}\ \text{《The Riemann Hypothesis: Past, Present and a Letter to Riemann》}（arXiv:2602.04022）：\text{其原创贡献是}\ \textbf{极值化 Weil 二次型}\ \text{以逼近零点} ⟹ \textbf{二次型通道} ⟹ \textbf{回归，关闭}（仅登记）✓$$
$$\textbf{(2.2)}\ \text{Newman／Cardon"Fourier transforms with only real zeros"} ⟹ \textbf{通道 S 的经典工具}（对测度 }p\ \text{的刻画给出实零点充分条件）✓$$
$$\textbf{(2.3)}\ \text{Pólya–Schur–Lax 问题（AIM 2007 工作坊）} ⟹ \textbf{领域地图}（双曲性／稳定性保持算子专线）✓$$
$$\textbf{(2.4)}\ \text{Csordas–Norfolk–Varga（Turán 不等式）} ⟹ \textbf{通道 S 的}\ d=2\ \text{情形} ✓$$

---

## §3 预筛结论表

$$\begin{array}{c|c|c|c|c}
\text{候选} & \text{F3 归类} & \text{F1（独立信息）} & \text{F2（哪一层）} & \text{判定}\\
\hline
\textbf{通道 S：稳定性／全正性} & \textbf{other} & \textbf{支撑级}（\text{严格强于 Bochner}） & \text{新轴 }(d,n) & \boxed{\textbf{ALIVE（不封）}}\\
\text{Weil 二次型极值（2026 综述）} & \text{quadratic} & — & — & \textbf{回归，关闭}\\
\text{index／inertia／sum rule／RG／}\ker K & \text{linear／signature} & \text{无（盲／退回正性）} & L1\text{／}L2 & \text{已封（`V186`–`V188`）}\\
\text{Borcea–Brändén} & \text{工具} & — & — & \text{工具箱}\\
\text{TP-保持算子分类} & \text{工具＋一刀} & \text{无限阶 TP 保持只有正齐次} & — & \text{该子通道不可用}\\
\end{array}$$

---

## §4 判词与下一步（✓ 按 R1 写清"它携带的独立信息"）

**V190 判词**：① **找到通道 S（稳定性／全正性）＝ F3 之外的首个具名通道** ✓✓✓；② F1 **通过**（支撑级信息，严格强于二次型通道）✓✓✓；③ F2 **不适用**（缺口按 $(d,n)$ 而非 $T$）✓✓；④ 有**近期真进展**（GORZ PNAS 2019：每 $d$ 高 $n$ 全成立；$d\le8$ 全 $n$ 成立）与**明确剩余缺口**（中等 $d$、小 $n$ 的例外集，每度有限）✓✓；⑤ 同通道工具有 Borcea–Brändén（symbol 判据）✓，而无限阶 TP 保持算子因刚性**不可用** ✓；⑥ 三条风险已登记（等价改写／未证可确立／可能与低零点同源）✓。

**⭐ 按 R1 的回答（这是本档必须给出的那一句）**：
$$\boxed{\text{它携带的独立信息}\ =\ \textbf{支撑级信息}：\text{根集落在实轴上}\ \Longleftrightarrow\ \text{表示测度的支撑}\ \text{被限制在一侧／实轴}\ ——\ \text{严格强于"正定"（后者对支撑无限制）}} ✓✓✓$$

**下一步（V191 预登记，二选 —— 均须先过 R1）**：
① **结构性**：证明"中等 $d$、小 $n$ 的例外集为空"需要**何量级的输入**？（是否等价于低零点／Weil 正性 ⟹ 若是则封；若否，则这是**第一个定位在 (d,n) 轴上的新缺口**）
② **构造性**：用 **Borcea–Brändén symbol 判据**，能否构造一个**算术可实现**的稳定性保持算子，把"已知实根"的起点推向 $\xi$？（⚠️ 若该算子把目标写进 symbol，即属走私 ⟹ 按 `V188` 的判据自检）

```
⚠️ §1.3 Pólya 1927／GORZ 2019／Csordas–Norfolk–Varga／Newman–Cardon 为【外部经典与文献 ✓】，本档未独立复核
⚠️ §1.2 Bochner↔Schoenberg 的"支撑限制"对照为【本档核心判断 ✓✓✓】—— 数学内容经典，此处用作 F1 判定
⚠️ §1.4 缺口形状（每度有限例外集）为【本档判断 ✓✓】
⚠️ §1.5(b) TP-保持算子刚性（只有正齐次）取自 Belton–Guillot–Khare–Putinar（2022）【外部 ✓】；"该子通道不可用"为【本档判定 ⚠️】
⚠️ §1.6 三条风险为本档自陈 ✓；R-b 尤其重要：携带独立信息 ≠ 能被无条件确立
⚠️ 未用 RH ✓（仅作等价性引用）；未跑 Lean ✓；零数值 ✓（GORZ 的数值为文献转述）
✅ 净产出：① 找到并判定通道 S（ALIVE，不封）✓✓✓；② F1/F2 预筛给出明确依据 ✓✓；③ 给出 R1 要求的"独立信息"回答 ✓✓✓；
   ④ 一刀（无限阶 TP 保持算子刚性）✓；⑤ 两项下一步（结构性／构造性）✓✓
```
