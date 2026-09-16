# V292 · **Track I：预算墙的隐含假设审计** ＋ **步骤 3：候选对表 E1–E4** —— ⭐⭐⭐ **结论：预算墙不是定理，而是"机制×输入"的联合属性**；**唯一可移项 ＝ "窗口型机制且 $h(n)$ 亚线性"**（＝`E30-2` 自己写下的具体目标）；**候选对表：未找到不落 E1–E4 者** ⭐⭐⭐⭐

$$\boxed{\textbf{Track I 结论}：\text{T}^2\ \text{律}\ \textbf{不是关于 RH 的定理}，\text{而是}\ \textbf{"机制×输入"的联合属性}（`E30`-2 §3）} ✓✓$$
$$\boxed{\text{机制 A（窗口型）}：h(n)=\tfrac{n}{2\pi}\ \textbf{线性};\ \text{输入}\ \textbf{无条件} ✓;\qquad \text{机制 B（尾部预算）}：h(n)\approx10\sqrt{\delta n}\ \textbf{亚线性};\ \text{输入}\ \textbf{条件性} ✗}$$
$$\boxed{\text{故唯一可移项}\ ＝\ \boxed{\text{"窗口型"机制且}\ h(n)\ \textbf{亚线性}}（`E30`-2 原文目标）} ✓✓✓$$
$$\boxed{\text{步骤 3 结果}：\text{存量候选}\ \textbf{全部落入 E1–E4 或属 UNINSTANTIATED} ⟹ \textbf{已审计范围内无逃逸者}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 12:16「**可以，继续**」（＝执行 `STRATEGY-2026-09-16` §7 的第 1 步与第 3 步）✓
> 依据（本档现场读取）✓ `E30-2-mechanism-and-refined-criterion.md`（61 行，全文读）｜`E30-2-T2-mechanism.md`｜`A3-1-moving-edge-necessity.md` §5｜`A3-third-moment-barrier.md`（文献侦察，标 `[原]`/`[引]`）｜`E217b`｜`V102`／`V162`／`V217b`｜`AOB4`／`G10`／`V250`／`V240`／`V248`／`ESC2` ✓
> 执行 ✓ 小灵｜**纸面 ✓（零数值推导；引用外部结论处标级别）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ `V292`（`id_claim.sh` ✓）

---

## §1 ⭐⭐⭐ Track I：预算墙的隐含假设——**已被 `E30-2` 写明，本档定位其"可移项"**

$$\textbf{机制 A（窗口／逐项正性）}：\text{在线零点第}\ n\ \text{项}\ ＝1-\cos(n\theta_\gamma),\ \theta_\gamma\approx\tfrac1\gamma ⟹ n^*(\gamma)\approx2\pi\gamma ⟹ \boxed{h(n)=\tfrac{n}{2\pi}\ \textbf{线性}} ✓$$
$$\qquad \text{输入}\ \textbf{无条件} ✓（\text{只用}\ 1-\cos\ge0）⟹ \text{这正是论文 A 的线性范围}\ 2T\ \text{的来源} ✓✓$$
$$\textbf{机制 B（尾部预算）}：|1-\tfrac1\rho|^2=1+\tfrac{1-2\beta}{\beta^2+\gamma^2} ⟹ q\approx1-\tfrac{\delta}{\beta^2+\gamma^2} ⟹ n^*\approx0.01005\,\tfrac{\gamma^2}{\delta} ⟹ n^*/\gamma^2=1.005（\text{常数}）✓$$
$$\qquad ⟹ \text{反解}\ \boxed{h(n)\approx10\sqrt{\delta n}}\ ⟹ \text{"T}^2\ \text{律"};\qquad \text{输入}\ \textbf{条件性} ✗（\text{需计数假设 ＋ 未证引理修复}）✓✓$$

$$\boxed{\textbf{精化判据（`E30-2` §2，两轴）}：\text{① } h(n)\（\text{可达范围}）\ ＋\ \text{② 输入的}\textbf{无条件性}\（\text{结论强度}）} ✓✓$$
$$\qquad \textbf{突破} ＝ \text{改善}\ h(n)\ \textbf{而不牺牲无条件性};\qquad \text{"为更大范围而放弃无条件性"}\ \textbf{不是进步} ✓✓✓$$
$$\Longrightarrow \boxed{\textbf{可移项（唯一）}：\exists\ \textbf{"窗口型"机制且}\ h(n)\ \textbf{亚线性}} ✓✓✓$$
$$\qquad \text{（现存窗口机制}\ h=\tfrac{n}{2\pi}\ \text{线性} ✓;\ \text{尾部机制}\ h\sim\sqrt{\delta n}\ \text{但条件性} ✗）✓$$

$$\textbf{补：}0.682\ \text{的真实身份}（`A3-1` §5）：\text{它}\ \textbf{是外部引用} —— \text{前沿论文}\ \mathrm{arXiv}{:}2608.13637\ \text{§7.2 "bandwidth-one 证书类天花板}\approx0.682" ✓$$
$$\qquad ⟹ \text{故}\ 0.682\ \textbf{不是本项目自推的律}，\text{而是}\ \textbf{证书类的外在限制};\ \text{本档}\ \textbf{不} \text{把它当作墙（N3：须带假设清单）} ✓✓$$

---

## §2 ⭐⭐ 与前沿的**独立互证**（`A3-third-moment-barrier`，文献已核验）

$$\text{前沿}：\mathrm{arXiv}{:}2608.13637\ \text{（"More than two thirds of the zeta zeros are simple and on the critical line"）§7.2(e)}：$$
$$\qquad \text{"}\textbf{X}\asymp\textbf{T}\ \text{时无条件更高矩一无所获"}\ ✓;\ \text{k=3 的对角法只覆盖}\ X\le T^{2/3-\varepsilon} ⟹ \text{推到}\ X\asymp T\ \textbf{还差}\ T^{1/3}\（\text{[原]}）✓✓$$
$$\qquad \text{k=2 是特例}（\text{Montgomery 无条件素数侧二阶矩；Aryan 2022；BGSTB24}）✓;\ \text{k=3 已知结果}\ \textbf{全部依赖 RH}（\text{Hej94／RS96，[引]}）✓$$
$$\Longrightarrow \boxed{\text{两条独立语言互证}：\text{前沿的"差}\ T^{1/3}\text{"} \longleftrightarrow \text{我方的"窗口机制}\ h\ \text{亚线性缺失"}} ✓✓✓$$
$$\qquad \text{共同形态}：\textbf{无条件技术不足一档，且缺口被精确定位}（\text{不是"原理性不可能"}）✓✓$$

---

## §3 ⭐ 步骤 3：存量候选**对表 E1–E4**

| 候选桥 | 形态 | 落点 | 依据 |
|:--|:--|:--:|:--|
| **Arakelov／Néron–Tate 高度配对** | 实值配对（正定） | **E2**（archimedean：$\infty$-位参与）＋**E4** | `AOB4`／`ESC2`／`V215` ✓ |
| **$\delta$-几何（Buium，char-0 Frobenius 替身）** | 代数提升结构 | **E4**（上同调／提升，无作用于所论谱） | `G10` 已封 ✓ |
| **MZV／周期（periods）** | 可计算周期不变量 | **E1**（可计算 ⟹ cylinder）＋**E4** | `AOB4`（无全局 similitude）✓ |
| **$\mathbf F_1$／Connes–Consani scaled site** | 几何／RR 型 | **E1**（几何不变量可计算）＋**E4** | `V250`／`V240`／`V267` ✓ |
| **第三型正性（锥分离）** | 非自对偶正性锥 | **E4**（判别锥须自对偶 ⟹ 回角 I；唯一幸存形态无实例） | `V248`（含撤回）／`V247` ✓ |
| **Selberg 型自伴正性** | 自伴算子的正性 | **E2**（archimedean 谱）＋**E4**；且其 $\beta$-刚性**来自自伴性而非闭合** | `V284` §4／`POS` 系列 ✓ |
| **窗口机制（$h=n/2\pi$）** | 检测型（非桥） | ⚠️ **E1**（可计算 ⟹ 不分离）；但**检测≠排除** | `E30-2`／"检测≠排除"线 ✓ |

$$\Longrightarrow \boxed{\text{已审计范围内：}\textbf{未找到不落 E1–E4 的候选}} ⟹ \text{无逃逸者} ✓✓$$
$$\qquad ⚠️\ \text{逐行落点为}\ \textbf{[判断]}（\text{本档现场判定，未逐篇重算}）；\ \text{E1–E4 为}\ \textbf{四条封锁线}，\text{非穷尽划分}（N1 纪律）✓$$

---

## §4 结论与下一步（按 `STRATEGY` §7 第 5 步）

$$\textbf{① Track I 的收获}：\text{墙的可移性被}\ \textbf{精确命名} \text{—— 不是"预算不够"，而是}\ \boxed{\exists\ \text{窗口型机制且}\ h(n)\ \text{亚线性}} ✓✓$$
$$\qquad ⟹ \text{Track I 留下}\ \textbf{一个可攻的定量靶} \text{（无条件 ＋ 亚线性）};\ \text{与前沿"差}\ T^{1/3}\text{"}\ \textbf{同址} ✓✓$$
$$\textbf{② 步骤 3 的收获}：\text{无逃逸者} ⟹ \text{按第 5 步 ⟹ }\textbf{开 Track II}（\text{桥公理}\ \mathrm{B1}\text{–}\mathrm{B5}\ ＋\ \text{完备性／逃逸者二择一}）✓✓$$
$$\textbf{③ 两轨关系}：\text{Track I}\ \text{给}\ \textbf{定量靶};\ \text{Track II}\ \text{给}\ \textbf{结构判据};\ \text{二者}\ \textbf{共享 E1–E4} \text{作排除工具} ✓$$

---

## §5 边界

```
① ⚠️ §1 全部取自 `E30-2`（现场读全文）；0.682 的身份取自 `A3-1` §5（该档自标为**引用** arXiv:2608.13637 §7.2）⚠️
② ⚠️ §2 为 `A3-third-moment-barrier` 的**文献侦察结果**（该档已标 `[原]`/`[引]`）；本档**未再核原文** ⚠️
③ ⚠️ §3 的落点为 **[判断]**；E1–E4 是**封锁线**，不是穷尽划分 ⟹ 不得升成"所有候选都已封"（N1）✗✓
④ ⚠️ Track II 尚未开；本档**不**声称完备性可证 ✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值推导 ✓
```

---

## §6 ✅ 净产出

```
① ⭐⭐⭐ **Track I 结果**：预算墙 **不是定理**，而是"**机制×输入**"联合属性（`E30-2` §3）；
   机制 A 无条件但 h 线性；机制 B 亚线性但条件性 ⟹ **唯一可移项 ＝ "窗口型且 h 亚线性"** ✓✓✓
② ⭐⭐ **0.682 的身份更正**：它是**外部引用**（bandwidth-one 证书类天花板，arXiv:2608.13637 §7.2），**不是本项目自推的律** ✓✓
③ ⭐⭐ **独立互证**：前沿"X≍T 差 T^{1/3}"（对角法上限 X ≤ T^{2/3−ε}）⟷ 我方"窗口机制 h 亚线性缺失" ⟹ **同址、且都非原理性不可能** ✓✓
④ ⭐ **步骤 3 完成**：7 类候选逐条对表 E1–E4 ⟹ **无逃逸者** ⟹ 按策略第 5 步转 **Track II** ✓✓
⑤ ⭐ **纪律**：0.682 不再当"墙"引用（N3）；E1–E4 非穷尽（N1）；落点标 [判断] ✓
【下一步】开 Track II：把 E1–E4 写成"桥公理"B1–B5，然后二择一（完备性证明／寻找逃逸者）✓
```
