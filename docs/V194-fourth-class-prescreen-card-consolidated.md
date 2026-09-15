# V194 · 🧰 **第四类机制预筛卡（总卡）** —— 合并六件工具为**单页可执行卡**；含**二分封闭 Lemma**、**第四类严格定义**、**定义级核对纪律**、以及**回 A1／A3 的唯一问题**

> 委托 ✓ 唐先生 2026-09-15 13:19：同意 **② → ①**，**V194 不再扩展候选**；**"先把这轮得到的筛选器压缩成一张真正可执行的总卡，然后再回 A1／A3"**；关键理由：**"现在最有价值的不是再找一个名字，而是证明以后任何'第四类'候选都无法通过偷换信息类型逃过我们已经建立的封闭条件"**
> 并入 ✓ `V189`（三筛）＋ `V191`（F1 两问）＋ `V192`（F4；纵坐标退化封印）＋ `V193`（二分封闭；**information blindness $\neq$ effective extractability**）＋ `V188`（饱和判据）＋ **定义级核对纪律（Planat 事故）**
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V194**（**本卡取代 `V189`**）

---

## §0 用法（三步，$<2$ 分钟；任一步失败即**停**，禁止先写推导）

$$\textbf{步 1}\ \text{定性}：\text{F1 两问}\（\text{§1}\bigr）\ \longrightarrow\ \textbf{步 2}\ \text{结构}：\text{F4 六条}\（\text{§2}\bigr）\ \longrightarrow\ \textbf{步 3}\ \text{量化}：\text{三层涨落}\（\text{§4}\bigr）$$
$$\qquad ⚠️\ \text{同时对}\ \textbf{四通道穷尽表}\（\text{§5}\bigr）\ \text{归类};\ \text{凡落入已封通道者，}\textbf{立即记录并停止} ✓$$
$$\qquad ⚠️\ \text{凡引用外部结果者，先过}\ \textbf{定义级核对}\（\text{§7，六项}\bigr） ✓✓$$

---

## §1 I. F1：独立信息的**两问**（本卡第一关）

$$\boxed{\ \mathrm{F1a}:\ M\ \text{是否携带现有显式公式／Weil 型信息}\ \textbf{之外}\ \text{的新信息}？\qquad \mathrm{F1b}:\ M\ \text{能否以}\ \textbf{严格弱于 RH}\ \text{的输入}\ \textbf{无条件}\text{证明}？\ }$$

$$\begin{array}{c|c|l}
\mathrm{F1a} & \mathrm{F1b} & \text{判定}\\
\hline
\text{否} & \text{任意} & \textbf{REPACKAGED}（\text{换包装}）\\
\text{是} & \text{否} & \textbf{RH-EQUIVALENT / TOO STRONG}\\
\text{否} & \text{是} & \textbf{USEFUL BUT IRRELEVANT}\\
\textbf{是} & \textbf{是} & \boxed{\textbf{真正候选}}\\
\end{array}$$
$$\qquad ⭐\ \text{价值}：\text{把"看起来新"与"真能成为桥"}\ \textbf{彻底分开};\ \text{两问缺一不可} ✓✓$$

---

## §2 II. F4：Representation-change test（六条）

$$\boxed{\begin{array}{ll}
\mathrm{F4.1} & \text{非线性或非平凡结构变换}\\
\mathrm{F4.2} & \text{不能只是显式公式后的坐标变换}\\
\mathrm{F4.3} & \text{可直接由算术数据构造}\\
\mathrm{F4.4} & \textbf{对}\ \beta-\tfrac12\ \textbf{有实质敏感性}\\
\mathrm{F4.5} & \text{不能等价于}\ Q\succeq0\\
\mathrm{F4.6} & \text{最终产生}\ \textbf{定量定位}，\text{而非仅统计描述}\\
\end{array}}$$
$$\qquad ⭐\ \textbf{F4.4 是本轮最重要的升级} ✓✓：\text{因}\ \gamma_\rho=\dfrac{\rho-\frac12}{i}=\gamma-i\!\left(\beta-\tfrac12\right)，\ \text{故}\ \textbf{不能说"线性统计量看不到}\ \beta\text{"} ✓$$
$$\boxed{\text{information blindness}\ \neq\ \text{effective extractability}} ✓✓✓$$
$$\qquad\Longrightarrow\ \text{正确障碍}：\text{线性信息}\ \textbf{包含}\ \beta;\ \text{但从}\ \textbf{有限／可控输入}\ \text{中}\ \textbf{稳定提取}\ \beta\ \text{是困难的} ✓$$
$$\qquad ⚠️\ \textbf{纪律}：\text{此后一切报告}\ \textbf{一律使用后者}（\text{可提取性}）,\ \textbf{不再使用}"\text{盲}" ✓✓$$

---

## §3 III. 饱和判据（`V188` 的核心，措辞已修正）

$$\text{设}\ \mu_\zeta=\sum_\rho m_\rho\delta_\rho。\ \text{若候选最终只产生}\ L_f(\mu_\zeta)=\sum_\rho m_\rho f(\rho)\ \text{这类}\ \textbf{线性泛函}，\ \text{而}\ L_f\ \text{已被显式公式完全确定}：$$
$$\boxed{\ \text{它没有增加新的信息通道}\ }\qquad ⚠️\ \textbf{不得}\text{写成}\ \text{"linear}\Rightarrow\beta\text{-blind"}\ \textbf{（错）};\ \text{正确：}\ \boxed{\text{linear}\Rightarrow\text{information-saturated}}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{唯一出路}：\text{它须进一步给出}\ \boxed{\text{稳定、有限复杂度、定量可逆的}\ \textbf{support localization}}\ \text{才可能成为新机制} ✓✓$$

---

## §4 IV. 三层涨落判据

$$\boxed{\begin{array}{ccl}
\text{typical} & S(T)\sim\sqrt{\log\log T} & \textbf{无条件}（\text{Selberg CLT}）\\
\text{unconditional worst} & S(T)=O(\log T) & \textbf{无条件}（\text{Littlewood}）\\
\textbf{RH-level} & S(T)=O\!\left(\dfrac{\log T}{\log\log T}\right) & \textbf{RH}\ \Longleftrightarrow\（\text{von Koch}）\\
\end{array}}$$
$$\qquad\Longrightarrow\ \text{改善平均／典型涨落}\ \textbf{不蕴含}\ RH;\ \text{尤其}\ \text{RMT rigidity／pair correlation／variance／CLT}\ \text{若只控制 typical} ⟹ \text{降级为}\ \boxed{\text{statistical improvement}}\ \text{，}\textbf{非}\ \text{RH mechanism} ✓✓$$

---

## §5 V. 四通道穷尽表（本卡核心总表）＋ **第四类的严格定义**

$$\begin{array}{c|c|c}
\text{通道} & \text{能处理什么} & \text{当前状态}\\
\hline
\textbf{Linear／trace} & \text{全部显式公式线性信息} & \textbf{SATURATED}\\
\textbf{Quadratic／positivity} & \text{Weil 型二次型；部分零点比例} & \textbf{A1／A3 主线}\\
\textbf{Signature／inertia} & \text{正负惯性；部分在线比例} & \textbf{67.2\% ceiling（0.6818287）}\\
\textbf{Pointwise／dynamic} & \text{单点定位；最强局部信息} & \textbf{唯一真正未关闭类别}\\
\end{array}$$
$$\qquad ⚠️\ \text{以前我们把"第四类"说}\textbf{太宽};\ \text{现严格缩成}：$$
$$\boxed{\textbf{第四类}\ =\ \text{非二次型、非惯性、非纯线性，}\ \textbf{且能逐点／局部定位}\ \beta} ✓✓$$
$$\qquad ⚠️\ ⚠️\ \text{并按纪律携带}\ \text{`V189`}\ \text{的警告}：\boxed{\text{“第四类存在”目前只是}\ \textbf{逻辑剩余类}，\ \textbf{绝不是}\ \text{候选机制}} ✓$$

---

## §6 VI. **二分封闭 Lemma**（`V193` 的升级；本卡最硬的一件）

$$\textbf{设定}：\text{算术构造}\ \mathcal A_{\mathbb P}\xrightarrow{\mathcal R}H\ \text{且声称}\ \operatorname{Spec}(H)\subset\mathbb R。\ \text{若}\ \operatorname{Spec}(H)\ \text{足以推出全部}\ \zeta\ \text{零点实}：$$
$$\textbf{支 A（}H\ \textbf{自伴）}：\operatorname{Spec}(H)\subset\mathbb R\ \textbf{自动成立}（\text{无信息}）⟹ \beta\ \text{只能经}\ \textbf{实谱无法区分}\ \text{的方式进入，即}\ (\gamma,\ \text{multiplicity})\ \text{数据}$$
$$\qquad\Longrightarrow\ \text{重新落入}\ \textbf{零点比例／重数通道}\（N_0^s／N_d\bigr）⟹ \text{撞已证上限}\ \textbf{0.6818287} ✓✓$$
$$\textbf{支 B（}H\ \textbf{非自伴但声称谱全实）}：\operatorname{Spec}(H)\subset\mathbb R\ \text{本身即}\ \textbf{极强的谱定位命题};\ \text{若它足以推出全部零点实}：\ \text{real spectrum}\Rightarrow RH$$
$$\qquad\Longrightarrow\ \textbf{没有"免费实谱"} ✓✓$$
$$\boxed{\text{自伴支}\ \cup\ \text{非自伴实谱支}\ =\ \textbf{全部封闭}} ✓✓✓$$
$$\qquad\Longrightarrow\ \text{真正剩下的只能是}：\ \boxed{\mathcal A_{\mathbb P}\xrightarrow{\mathcal R}\mathcal X}\ \text{其中}\ \mathcal X\ \textbf{不是先验实谱对象}，\ \text{却能从算术内部产生对}\ \beta-\tfrac12\ \text{的}\ \textbf{非退化敏感性} ✓✓$$

---

## §7 VII. ⚠️ 纪律：**Definition-level audit before theorem-level use**

$$\text{任何}\ \textbf{外部结果}\ \text{进入主线前，必须先核}\ \textbf{六项}（\text{逐项记录}）✓✓：$$
$$\boxed{\begin{array}{ll}
1. & \text{对象定义完全一致}\\
2. & \text{归一化一致}\\
3. & \text{指标依赖因子一致}\\
4. & \text{权重是否随指标变化}\\
5. & \text{结论适用域一致}\\
6. & \text{之后才谈定理结论}\\
\end{array}}$$
$$\qquad ⭐\ \text{Planat 事故}\ \textbf{非常典型}：\textbf{定理方向看起来漂亮，但对象已经不是 GORZ 的 Jensen polynomial} ✓$$
$$\qquad ⭐\ \text{本条为}\ \textbf{实质性成果}（\text{不是行政整理}）: \text{它把"}\textbf{引用风险}\text{"从}\ \text{判断力问题}\ \text{变成}\ \textbf{可执行清单} ✓✓$$

---

## §8 回 A1／A3 的**唯一问题**（V195 立项）

$$\text{主线压成}\ \boxed{\text{Weil positivity}\ \longleftrightarrow\ \text{Li positivity}}\ \text{，但}\ \textbf{不再问}\ \text{"能否找到另一个正性判据"}\（\text{已无价值}\bigr）✓$$
$$\textbf{新问题}：\boxed{\ \textbf{能否把 Weil／Li 正性从"全局无限族"降成一个可证明的}\textbf{局部结构条件}？\ }$$
$$\qquad\text{即寻找严格的}\ P_{\rm local}\ \text{使}\quad P_{\rm local}\Longrightarrow P_{\rm Weil}\iff\text{RH}\qquad \text{且}\ P_{\rm local}\ \text{本身可由}\ \textbf{严格弱于 RH 的算术事实}\ \text{推出} ✓✓✓$$
$$\qquad ⚠️\ \text{与过去的区别}：\text{过去一直在找}\ \text{new invariant}\to\text{RH};\ \textbf{现在攻的是}：$$
$$\boxed{\text{local arithmetic constraint}\ \longrightarrow\ \text{global positivity}}$$
$$\qquad ⚠️\ \text{附加约束}：P_{\rm local}\ \textbf{不能只是}\ \text{Weil 二次型的一个坐标表达}（\text{否则}\ \mathrm{F1a}=\text{否}\Rightarrow\textbf{REPACKAGED}）✓✓$$

---

## §9 判词与 V195 预登记

**V194 判词**：① **六件工具已合并为单页总卡**（F1 两问 ＋ F4 六条 ＋ 饱和判据 ＋ 三层涨落 ＋ 四通道表 ＋ 二分封闭 Lemma ＋ 定义级核对）✓✓✓；② **本卡取代 `V189`** ✓；③ **第四类严格定义**收窄为"非二次型、非惯性、非纯线性，且能逐点／局部定位 $\beta$" ✓✓；④ **二分封闭 Lemma** 成立（两支皆封；唯一剩余形态 $\mathcal A_{\mathbb P}\to\mathcal X$）✓✓✓；⑤ **两条纪律升级**：**information blindness $\neq$ effective extractability**（此后一律用后者）＋ **definition-level audit before theorem-level use**（六项清单）✓✓✓；⑥ 回主线的问题已写成**单一命题**（$P_{\rm local}\Longrightarrow P_{\rm Weil}\iff$RH，且 $P_{\rm local}$ 须严格弱于 RH）✓✓✓。

**净收获**：本卡把"第四类候选能否逃过封闭条件"**机械化**为三步判定；核心武器是 **F1 两问表** ＋ **二分封闭 Lemma** ＋ **定义级核对清单**。

**V195 预登记（唯一方向）**：
$$\text{立项}\：\textbf{Local Positivity Audit}\ ——\ \text{攻}\ \boxed{\text{local arithmetic constraint}\Longrightarrow\text{global Weil／Li positivity}}$$
$$\qquad\text{第一步（按 R1 与 F1）}：\text{先给出}\ P_{\rm local}\ \text{的}\ \textbf{严格定义}，\ \text{并自检两问}：\mathrm{F1a}\ \text{是否}\ \textbf{是}（\text{非换包装}）？\ \mathrm{F1b}\ \text{是否}\ \textbf{是}（\text{可由严格弱于 RH 的算术事实推出}）？$$
$$\qquad ⚠️\ \text{若两问任一为否} ⟹ \text{按本卡}\ \textbf{立即停}，\ \text{不进入推导} ✓✓$$

```
⚠️ §1 F1 两问与 2×2 表为唐先生逐字 ✓✓；§2 F4 六条为唐先生逐字 ✓✓（F4.4 为关键升级）
⚠️ §2 "information blindness ≠ effective extractability" 为唐先生逐字 ✓✓✓（本档据此正式废弃我此前的"盲"表述）
⚠️ §3 饱和判据（linear ⟹ information-saturated）为唐先生修正后的措辞 ✓✓
⚠️ §4 三层涨落为【经典 ✓】（Selberg CLT／Littlewood／von Koch⟺RH）；"统计改进不等于 RH mechanism"为唐先生 ✓✓
⚠️ §5 四通道表与第四类严格定义为唐先生 ✓✓；`V189` 的"逻辑剩余类"警告并行携带 ✓
⚠️ §6 二分封闭 Lemma 为唐先生逐字 ✓✓（支 A／支 B；唯一剩余形态）—— 证明骨架见 `V193` §3；【结构判定 ⚠️】非形式定理
⚠️ §7 定义级核对六项为唐先生逐字 ✓✓；Planat 事故为实例 ✓
⚠️ §8 回主线问题为唐先生逐字 ✓✓
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 单页总卡（取代 V189）✓✓✓；② 第四类严格定义 ✓✓；③ 二分封闭 Lemma ✓✓✓；
   ④ 两条纪律升级 ✓✓✓；⑤ 回主线的单一命题 ✓✓✓；⑥ V195 立项 ✓
```
