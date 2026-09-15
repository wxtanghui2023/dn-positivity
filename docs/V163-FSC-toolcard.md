# V163 · ⭐⭐⭐⭐ **FSC 工具卡（基础设施，非突破口）—— 最终判据 ＋ ⚠️ 措辞修正（**有限基本谱通道** 而非 "s-平面零点有限"）＋ 三步可执行流程 ＋ 适用边界纪律**
> 委托 ✓ 唐先生 2026-09-15 11:06（**"②值得做，但不要把它当成主线推进。它是基础设施，不是突破口。V162 已经把数学内容做完了；现在只需把 FSC 固化成严格、可执行的工具卡，并同时修掉一个细节"** ✓）
> 定位 ✓ **工具卡（基础设施）** —— 不再产生新结论；不占主线预算 ✓｜来源 ✓ `V162`（FSC ＋ C-i$^\star$ ＋ 三级结构）｜依据 ✓ Artin–Mazur／Ruelle（经典）＋ RvM 计数（经典）＋ `L1` NO-GO（档案）
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V163**

---

## §0 最终判据（✓）

$$\boxed{\dim\mathcal S<\infty\quad+\quad Z_{\mathcal S}(z)=\frac{1}{\det(I-zA)}\quad\Longrightarrow\quad Z_{\mathcal S}\ \text{rational}}$$
$$\text{若}\ A\in M_m(\mathbb C)\ ✓,\ \text{则}\ \det(I-zA)=\prod_{j=1}^{m}(1-\lambda_jz)\ ⟹ Z_{\mathcal S}(z)=\prod_{j=1}^{m}(1-\lambda_jz)^{-1} ⟹ \text{有限平面内的基本零／极点通道数}\le m ✓$$

---

## §1 ⚠️ 措辞修正（✓✓ 本档唯一实质修正 ✓）

$$\textbf{不得}\text{把}\ N_{Z_A}(R)\le m\ \text{写成所有"零点计数"的统一表述} ✗$$
$$\qquad\text{因若考虑}\ \textbf{周期覆盖}\ z\mapsto e^{s}\ ✓,\ \text{一个有限的 }z\text{-平面奇点可能对应 }s\text{-平面中的}\textbf{无限周期复制} ✓✓$$
$$\Longrightarrow\ \text{真正的不变量应叫}\ ✓：\boxed{\textbf{有限基本谱通道}}\ \text{而}\textbf{不是}\text{"}s\text{-平面零点有限"} ✓✓$$
$$\qquad\Longrightarrow\ \text{该措辞使 FSC 对后续审计}\textbf{更稳健} ✓\ \text{（周期／代数映射产生的无限复制仍只算有限基本通道）}$$

---

## §2 可执行三步流程（✓）

$$\textbf{FSC-1（状态有限性）✓}：\exists\ \text{有限集合}\ \mathcal S,\ |\mathcal S|=m<\infty\ ✓,\ \text{使整个动力学由}\ F:\mathcal S\to\mathcal S\ \text{或有限矩阵 }A\ \text{完整描述？}$$
$$\qquad\text{若 YES} ⟹ M\Rightarrow Z_M(z)\ \text{rational} ✓$$
$$\textbf{FSC-2（谱通道有限）✓}：\text{检查其独立谱参数是否只有}\ \lambda_1,\dots,\lambda_m\ ✓$$
$$\qquad\text{若只是有限参数经}\textbf{周期／代数映射}\text{产生无限复制} ⟹ \textbf{仍只是有限基本通道} ✓$$
$$\textbf{FSC-3（目标是否要求 ζ 完整谱）✓}：\text{若目标是}\ \Lambda_M\cong Z_\zeta-\tfrac12\ ✓,\ \text{则需}\ N_\zeta(T)\to\infty\ \text{且}\ \tfrac{N_\zeta(T)}{T}\sim\tfrac{1}{2\pi}\log T ✓$$
$$\qquad\Longrightarrow\ \text{有限基本通道}\textbf{不能}\text{承担这种完整谱识别} ⟹ \boxed{\text{FSC}=DEAD} ✓✓$$

---

## §3 适用边界（✓✓ 必须写进卡面 ✓）

$$\textbf{FSC 不能判死} ✗：|\mathcal S|=\infty\ ✓;\ Z_M(z)\ \text{非有理}\ ✓;\ N_M(T)\sim T\log T\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{FSC 只杀 finite-state，不杀 infinite-state}} ✓✓\ \text{（}V162\ \text{最重要的边界纪律）}$$

---

## §4 长期复用筛选器（✓）

$$\text{任何新提案}\ M\to\Lambda_M\to Z_\zeta-\tfrac12\ ✓,\ \text{先问}\ ✓：\boxed{\dim(\text{完整状态空间})<\infty\ ?}$$
$$\qquad\text{若是} ⟹ \boxed{\text{FSC-DEAD}}\ ✓\ \text{直接结束},\ \textbf{不再讨论} ✓：\text{Weyl law}／\text{谱统计}／\text{周期轨道}／\text{动力 ζ}／\text{"增加几个状态"}／\text{有限图}／\text{有限自动机}／\text{有限群作用}$$

---

## §5 声明表格式（✓ "可执行"的落地形式 ✓）

> ⚠️ FSC-1／FSC-2 属**建模判断**（判"状态空间是否有限"）⟹ 不可机器判定 ⟹ 故本卡为**流程卡 ＋ 声明表**，非脚本 ✓

```
提案名：________________
FSC-1  状态空间是否有限？  [ ] 有限(m=___)   [ ] 无限   [ ] 未声明
FSC-2  独立谱参数是否有限？[ ] 有限         [ ] 仅有限参数的周期/代数复制   [ ] 无限
FSC-3  目标是否 = ζ 完整谱？[ ] 是          [ ] 否
判定： [ ] FSC-DEAD（1 且 2 有限 且 3 是）   [ ] FSC 不适用（1 或 2 含无限）
备注：_________________________________________________________________
```

---

## §6 判词（✓）

$$\boxed{\textbf{V163 ✓}：① 最终判据固化 ✓;\ ② 措辞修正（有限基本谱通道）✓✓;\ ③ 三步流程可执行 ✓;\ ④ 边界纪律（只杀 finite-state）✓✓;\ ⑤ 复用筛选器 ＋ 声明表 ✓}$$
$$\qquad\textbf{纪律 ✓}：\text{本卡为}\textbf{基础设施}，\text{不作为主线推进};\ ③（T\log T\Rightarrow\text{连续化}）\ \textbf{不再做} ✓✓\ \text{（}N(T)\sim T\log T\ \text{本身几乎无承重能力；且}\lambda_n:=N^{-1}(n)\ \text{可人为制造完全离散序列}）$$
$$\qquad\textbf{下一步} ✓：\text{进入 }V164\ ——\ \text{攻"非算子化结构如何内生连续谱参数"（机制本体，非箭头本身）}$$

```
⚠️ §0–§2 依 V162 ✓ ＋ Artin–Mazur／Ruelle（经典）✓ ＋ RvM（经典）✓
⚠️ §1 措辞修正为【唐先生判定 ✓✓】—— 周期覆盖 z↦e^s 的无限复制仍需算作有限基本通道
⚠️ 本卡不产生新数学结论；不占主线预算 ✓
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓；零代码 ✓（判据为声明式）
✅ 净产出：① 判据固化 ✓；② 措辞修正 ✓✓；③ 三步流程 ＋ 边界纪律 ＋ 复用筛选器 ＋ 声明表 ✓
```
