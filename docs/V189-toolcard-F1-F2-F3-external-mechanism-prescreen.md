# V189 · 🧰 **工具卡：外部机制三筛（F1 信息饱和／F2 涨落层级／F3 通道分类）＋ 外部机制普查正式收束**

> 委托 ✓ 唐先生 2026-09-15 13:01：**"V188 的'饱和定理'应当升级为工具箱级元判据"**；**措辞收紧**：**"线性统计量不能直接分辨支撑性质"** 成立且有价值，但**不要**写成"任何有限/无限线性统计量都绝对不能恢复支撑"（若有**全部测试函数的完整无界精度数据**，测度本身原则上可被恢复，进而恢复支撑 —— 即我在 V188 指出的"无界精度"边界）；并**拍板 V189 ＝ ① → ③**（先固化三筛，再停止外部机制普查；**不要再立即攻第四类**）
> 背景档 ✓ `V188`（饱和定理；四通道穷尽）｜`V187`（离轴对三面性；三分分类）｜`V186`（inertia 终点退化；转移原理）｜`V183`（$S(T)$；源-基数障碍）｜`V182`（正性 ⟹ 无计数界）
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V189**

---

## §0 用法（30 秒预筛，顺序固定）

$$\boxed{\text{F3 通道分类}\ \longrightarrow\ \text{F1 信息饱和}\ \longrightarrow\ \text{F2 涨落层级}}$$
$$\text{任一步判定为"回归旧墙"，}\textbf{立即停止}，\text{不进入推导（}\textbf{禁止先写数十页}\bigr）✓$$

---

## §1 🧰 F1 · 信息饱和判据

**陈述（✓ 唐先生收紧后的版本）**：

$$\text{若候选}\ \textbf{只}\ \text{增加}\ L_f(\mu)=\sum_\rho m_\rho f(\gamma_\rho)\ \text{及其有限／可控组合}，\ \text{而这些量}\ \textbf{已被显式公式与算术侧确定}，\ \text{则它}\ \textbf{未产生新的独立信息};\ \text{必须}\ \textbf{进一步}\ \text{证明它能从统计量进入}\ \textbf{支撑性质}，\ \text{否则}\ \textbf{关闭} ✓$$

**严格形式（本档的精确表述）**：

$$\text{设}\ \mathcal L:=\overline{\operatorname{span}}\{L_f\ :\ f\in\mathcal S\}\ \text{为线性泛函族};\ \text{显式公式给出}\ L_f(\mu)=A(f)\（\text{算术可算}\bigr)\ \text{对全部}\ f ✓$$
$$\qquad\Longrightarrow\ \mathcal L\ \textbf{已饱和}⟹\ \text{额外线性关系}\in\mathcal L\ \text{的代数推论} ⟹ \Delta I=0 ✓$$
$$\qquad\boxed{\text{线性统计量}\ \textbf{不能直接分辨}\ \text{支撑性质}} ✓✓\（\text{注意}\ \textbf{"直接"}\ \text{二字不可省}\bigr）$$

**⚠️ 边界（必须与陈述同时引用）**：

$$\text{若拥有}\ \textbf{全部测试函数}\ \text{的}\ \textbf{完整无界精度}\ \text{数据}，\text{则}\ \mu\ \textbf{原则上可被恢复} ⟹ \text{支撑可被恢复} ✓$$
$$\qquad\Longrightarrow\ \text{但那是}\ \textbf{反演}\（\text{inversion}\bigr）,\ \textbf{不是}\ \text{判别（discrimination）};\ \text{而}\ \textbf{反演所需的无界精度}\ \text{正是}\ S(T)\ \text{问题本身} ✓$$
$$\qquad\Longrightarrow\ \text{故 F1 的正确用法是}\ \textbf{问"是否携带新的独立信息"}，\ \textbf{不是}\ \text{宣判"绝对不可能"} ✓✓$$

**用法三步**：① 列出候选增加了哪些量；② 检查是否 ∈ $\mathcal L$ 或其推论（若否，记录其为**潜在新信息**）；③ 若 ∈ $\mathcal L$，要求给出**统计量 → 支撑性质**的过渡证明；无则该候选**关闭** ✓

---

## §2 🧰 F2 · 涨落层级判据

**三层阶梯（经典；候选必须自报它控制哪一层）**：

$$\begin{array}{c|c|c}
\text{层} & \text{陈述} & \text{状态}\\
\hline
\text{L1 典型} & S(T)\asymp\sqrt{\log\log T} & \textbf{无条件}（\text{Selberg CLT}）\\
\text{L2 无条件最坏} & S(T)=O(\log T) & \textbf{无条件}（\text{Littlewood 1924}）\\
\text{L3 目标最坏} & S(T)=O\!\left(\frac{\log T}{\log\log T}\right) & \textbf{RH}\ \Longleftrightarrow\（\text{von Koch}）\\
\end{array}$$

**判据**：$$\boxed{\text{只达到 L1 或 L2 者，}\textbf{不能冒充}\ \text{RH 级控制}} ✓✓$$
$$\qquad ⚠️\ \text{注意阶梯是}\ \log T\ \text{与}\ \log\log T\ \text{同时出现}：\text{由 }\sqrt{\log\log T}\ \text{到}\ \log T/\log\log T\ \text{的差距}\ \textbf{不是常数因子}，\ \text{是}\ \textbf{典型的"最坏情形"}$\unicode{x0020}\text{鸿沟} ✓$$

**用法**：① 候选给出的是分布（典型）还是逐点（最坏）？② 若是典型/无条件最坏，则它**至多**覆盖 L1／L2；③ 若宣称 L3，须展示**逐点**论证（通常须穿越零自由区/显式公式的反演）✓

---

## §3 🧰 F3 · 通道分类器

$$\boxed{\text{linear}\ |\ \text{quadratic}\ |\ \text{signature/inertia}\ |\ \text{pointwise/dynamic}\ |\ \text{other}}$$
$$\text{立即检查}\：\boxed{\text{other}\ \stackrel{?}{\longrightarrow}\ \text{linear／quadratic／pointwise}}\ ✓$$
$$\qquad\text{已知归宿}：\text{linear}\to\text{盲（F1）};\quad \text{quadratic}\to\text{Weil／Li 正性};\quad \text{signature／inertia}\to\text{终点退回正性（`V186`）};\quad \text{pointwise／dynamic}\to S(T)\ \text{最坏（F2）};\quad \det\to\text{Deninger（缺 polarization）} ✓$$
$$\qquad\Longrightarrow\ \text{若发生回归，}\textbf{不再展开}（\text{见 §0）}\ ✓✓$$

---

## §4 组合用法（固定顺序）

$$\textbf{F3}\ \text{先判类型} \longrightarrow\ \textbf{F1}\ \text{判"是否只是已确定的线性信息"} \longrightarrow\ \textbf{F2}\ \text{判"控制到哪一层"} ✓$$
$$\qquad\Longrightarrow\ \text{三步全过}\ \text{才值得写推导};\ \text{任一步失败}\ \Longrightarrow\ \textbf{记录并停止} ✓$$

---

## §5 外部机制普查正式收束（✓ 唐先生 13:01 拍板）

$$\text{本轮（12:24–13:01）经}\ \textbf{两条独立入口}\ \text{扫描外部机制（不限 RH）}：$$
$$\qquad\text{入口 A（`V187`）机制族}：\text{index／inertia／RG／Lefschetz／sum rule／null relation};\qquad \text{入口 B（`V184`／`V188`）信息类型}：\text{linear／quadratic／符号／逐点／det} ✓$$
$$\text{两者}\ \textbf{收敛};\ \text{得到的不是"又关掉六条路"，而是一张}\ \textbf{结构性地图}：$$
$$\boxed{\ \text{线性统计}\ \to\ \text{信息饱和}\ }\qquad \boxed{\ \text{二次／符号}\ \to\ \text{Weil／Li 正性}\ }\qquad \boxed{\ \text{逐点／动态}\ \to\ S(T)\ \text{最坏}\ }$$
$$\qquad ⚠️\ \text{inertia 只是把第二列换成 signature 语言，}\textbf{最终仍回到正性} ✓$$
$$\Longrightarrow\ \text{当前真正留下的}\ \textbf{不是}\text{一个模糊的"第四类"}，\ \text{而是}：$$
$$\boxed{\textbf{必须找到一种既非线性统计、又非二次正性、又非逐点控制的独立信息载体}} ✓$$

**⚠️⚠️ 严格警告（唐先生逐字，必须随任何引用携带）**：

$$\boxed{\text{"第四类存在"目前}\ \textbf{只是逻辑剩余类}，\ \textbf{绝不是}\ \text{候选机制}} ✓✓$$
$$\qquad\Longrightarrow\ \text{否则易再陷循环}：\text{定义第四类}\to\text{加足够强结构}\to\text{结构隐含 Weil 正性}\to\text{重新得到 RH} ✓$$

---

## §6 重开门槛（✓ 三条硬规则）

$$\textbf{(R1)}\ \text{若新机制}\ \textbf{不能回答"它携带的独立信息究竟是什么"}，\ \textbf{则不进入推导} ✓✓$$
$$\textbf{(R2)}\ \text{禁止}\ \textbf{先写数十页再判类型};\ \text{必须}\ \textbf{先过 F3／F1／F2} ✓$$
$$\textbf{(R3)}\ \text{禁止}\ \textbf{把"第四类"当作目标对象};\ \text{它只能作为}\ \textbf{判定的剩余} ✓$$

---

## §7 判词

**V189 判词**：① 三筛固化完成（F1／F2／F3）✓✓；② F1 措辞已按唐先生收紧（"**不能直接分辨**"＋**无界精度反演边界**）✓✓；③ 固定预筛顺序 F3→F1→F2，任一步失败即停（禁止先写数十页）✓✓；④ 外部机制普查**正式收束**，产出**结构性地图**（三列）✓✓；⑤ 唯一开放入口精确表述为"**独立信息载体**"✓✓；⑥ ⚠️「第四类存在」标注为**逻辑剩余类，绝非候选机制** ✓✓；⑦ 重开门槛 R1–R3 登记 ✓。

```
⚠️ §1 F1 的严格措辞与边界为唐先生 13:01 收紧后的版本 ✓✓（"直接"二字不可省；无界精度反演 ≠ 判别）
⚠️ §2 三层阶梯为【经典 ✓】（Selberg CLT／Littlewood／von Koch⟺RH）；判据为【本档 ✓】
⚠️ §3 五类通道与归宿为【本档（承 V187／V188）✓】
⚠️ §5 "第四类是逻辑剩余类、非候选机制"为唐先生逐字 ✓✓；§6 R1–R3 为唐先生逐字 ✓✓
⚠️ 未用 RH ✓（仅作等价性引用）；未跑 Lean ✓；零数值 ✓
✅ 净产出：三筛（F1/F2/F3）固化 ✓✓；固定预筛流程 ✓；结构性地图 ✓✓；第四类警告与重开门槛 ✓✓
```
