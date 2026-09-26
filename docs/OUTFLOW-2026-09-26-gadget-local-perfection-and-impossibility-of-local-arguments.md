已查地图：已跑 scripts/prework_map_check.sh gadget 外溢 强制 excess 完美码 ⟹ 执行自 GADGET-2026-09-26 档；未跑 solver ✓。
D0: 本档对象 = Z-gadget 外溢是否强制 excess 的判定，及 gadget 局部完美性的结构含义
D1: 1（新增：**gadget 局部完美（0 excess 贡献）✓**；**"外溢强制 excess" 为假 ✗**；**局部论证不可能性 ✓**；Z ≥ 18 ✓）

# OUTFLOW-2026-09-26

## §1 ✅ **gadget 局部完美：0 excess 贡献**（数值核验 ✓✓）

```
$$\text{gadget 的 }(n+1)/2\ \text{个球两两不交}\ \Longrightarrow\ \text{每个被覆盖点恰得 1 次 incidence}\ ✓$$
$$\textbf{数值}: (5,7):\ \text{9/9 gadget 全部 incidence}=1\ ✓✓;\quad (7,\text{完美码}):\ \text{112/112}\ ✓✓$$
$$\textbf{B}_1(x)\ \text{内}: (5,7):\ 54/54\ \text{恰 1}\ ✓✓\ \Longrightarrow\ \text{与 }t_x=0\ \text{一致}\ ✓$$
$$\Longrightarrow\ \boxed{\text{gadget 对 }E\ \text{的贡献\textbf{恒为 0}}}\ ✓✓\ \Longrightarrow\ \text{外溢记账退化为恒等式 }E=M(n+1)-2^n\ ✗\ (\text{无新界}\ ✗)$$
$$

## §2 ⛔ **断言"Z-gadget ⟹ 强制 excess" 为假** ✗✓

```
$$\textbf{完美码反例}: E=0,\ Z=112,\ \text{全部 gadget 的 incidence}=1\ ✗,\ \text{外部点 }b\ge2\ \text{数}=\mathbf{0}\ ✗✓$$
$$\qquad\Longrightarrow\ \text{112 个 gadget 产生\textbf{零} excess}\ \Longrightarrow\ \text{局部"外溢⟹excess"不成立}\ ✗✓$$
$$\textbf{(5,7) 半强制}: \text{外部点 108 个},\ b\ge2\ \text{的 54（50\%）}\ ✓,\ b=1\ \text{的 54}\ ✗\ \Longrightarrow\ \text{**仅一半**，非全部}\ ✗$$
$$\Longrightarrow\ \boxed{\text{外溢只是"允许"产生 excess，不"强制"}\ ✗}\ ——\ \text{唐先生路线 ① 的强形式被否}\ ✗✓$$
$$

## §3 ⭐⭐ **本轮真正的收获：局部论证不可能性**（结构性 ✓✓）

```
$$\text{gadget 是\textbf{局部完美片段}}: (n+1)/2\ \text{个两两不交的球、每点恰 1 次 incidence、0 excess}\ ✓$$
$$\qquad\Longrightarrow\ \text{它与完美码的局部图像\textbf{不可区分}}\ ✓\ \Longrightarrow\ \textbf{一切局部计数论证都会被完美码绕开}\ ✗✓$$
$$\Longrightarrow\ \boxed{\text{机制必须是\textbf{全局}的，且内在地用 }E>0}\ ✓✓\ (\text{强化前一轮"E-本质判据"}\ ✓)$$
$$\text{这解释了历史上的连续失败}: \text{local ledger}\ ✗,\ \text{私有点计数}\ ✗,\ \text{球不交计数}\ ✗,\ \text{外溢计数}\ ✗\ ——\ \text{全都撞在同一堵墙}\ ✓$$
$$

## §4 🆕 新推出的 Z **下界**（方向与目标相反，但记录 ✓）

```
$$\Sigma\mathrm{OC}=864-2Q_2\le864\ ✓;\quad \text{奇 }n:\ \mathrm{OC}>0\Rightarrow\mathrm{OC}\ge2\ \Longrightarrow\ \Sigma\mathrm{OC}\ge2(450-Z)\ ✓$$
$$\Longrightarrow\ 2(450-Z)\le864\ \Longrightarrow\ 450-Z\le432\ \Longrightarrow\ \boxed{Z\ge18}\ ✓\ (M=62,n=9)$$
$$\qquad\text{配合目标 }Z\le44\ \Longrightarrow\ \text{当前区间 }18\le Z\le44\ ✓\ (\text{下界新得}\ ✓,\ \text{上界仍缺}\ ✗)$$
$$

## §5 状态与下一刀

```
$$\textbf{资产（本轮）}: \text{gadget 0-excess 贡献}\ ✓;\ \text{局部论证不可能性}\ ✓✓;\ Z\ge18\ ✓$$
$$\textbf{已淘汰}: \text{① 外溢强制 excess}\ ✗\ (\text{加前：私有点复用}\ ✗,\ \text{球不交计数}\ ✗),\ \text{及其余承前条目}\ ✓$$
$$\textbf{桥}: \text{未打通}\ ✗;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$\text{下一刀候选}: \text{① 全局 }E\text{-传播（必须用 E>0 本质，且非局部}\ ✓);\ \text{② 转推 }Z\le44\ \text{的独立来源（如坐标/结构计数}\ ✓);\ \text{③ 记录后暂停主桥、转其它入口}\ ✓}$$
$$

## §6 边界（诚实标注）

- §1–§2 为**数值核验** ✓（n=5 全枚举 ✓、n=7 完美码精确构造 ✓）
- §3 的"局部论证不可能性"是**强结构性推论** ✓（依据：gadget 与完美码局部不可区分 ✓）—— 但**不等于**"桥不可能" ✗（全局论证仍可能 ✓）
- §4 的下界为**必要条件** ✓
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：局部完美片段、外溢强制 excess、局部论证不可能性、Z 下界
- **档案已有（引用，不列为提出）**：私有点、完美码、excess、球不交
