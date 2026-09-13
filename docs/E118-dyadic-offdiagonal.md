# E118 · ⭐⭐⭐ **撤回 ① ＋ 双滤波器结构 ＋ non-diagonal 的 dyadic 分解（含一处诚实簿记冲突 ⚠️）**

> 委托 ✓ 唐先生 22:47（撤回我的 ① ✗；给出双滤波器／区域 I–II／尺度巧合／Montgomery 缺口 ✓；
> 指定：**把非对角双和做完** $\mathcal N=\mathcal N_{\le T/\log T}+\sum_k\mathcal N_k$ ✓，逐层算量级 ✓）
> 执行 ✓ 小灵｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**无计算 ✓**；⚠️ 全文标【推导】✗ 非定理 ✓

---

## 0. 结论（✓ 五条 ＋ 一处撤回 ⚠️）

```
✅ **① 撤回 ✓**：**"RH $\nRightarrow$ 局部反集中"未被推出** ✗
   $$\textbf{已确立的只有 ✓}：\text{RH 的【点态信息】不足以【单独完成】该 }L^2\text{ 上界的证明}\ ✓\qquad\text{RH}\nRightarrow C_3\ \textbf{尚未证明}\ ✗$$
⭐⭐ **② 录取唐先生的结构 ✓（本轮基础 ✓）**：从显式公式
   $$\Delta(x,h)\simeq-\sum_\rho x^\rho\frac{(1+h/x)^\rho-1}{\rho}\qquad(h\ll x)\ ✓$$
   局部二阶矩的核心项出现【**两个独立滤波器**】✓：
   $$\boxed{W_h(\gamma-\gamma')}\ \text{（来自短区间 }h\text{ ✓）}\quad\text{与}\quad\boxed{K_Y(\gamma-\gamma')=\int_N^{N+Y}e^{i(\gamma-\gamma')\log x}dx}\ \text{（来自局部窗口 }Y\text{ ✓）}$$
   $$\textbf{且 ✓}：|K_Y(\delta)|\ll\min\!\Bigl(Y,\frac N{|\delta|}\Bigr)\ \Longrightarrow\ Y=\sqrt N\ \text{时}\ |\delta|\gg\sqrt N\ \text{已有}\ \frac N{|\delta|}\ \textbf{级衰减}\ ✓$$
   $$\Longrightarrow\ ⚠️\ \textbf{我此前"所有非对角项按绝对值相加得 }N^{3/2}\log^4N\text{"是【严重过估】}\ ✗$$
⭐⭐ **③ 危险区被精确定位 ✓**：**区域 I**（$|\delta|\lesssim N/Y=\sqrt N$ ✓，$K_Y\asymp Y$ ✓，无窗口相消 ⟹ **需零点相关结构** ✓）；
   **区域 II**（$|\delta|\gg\sqrt N$ ✓，$K_Y\ll N/|\delta|$ ✓ **确定性解析衰减** ✓）
   $$\Longrightarrow\ \textbf{真正需要 pair correlation 的范围}\ \approx|\gamma-\gamma'|\lesssim\sqrt N\ ✓\ \text{（而非"所有大 }\delta\text{" ✗）}$$
⭐⭐⭐ **④ 尺度巧合（本轮最漂亮的结构 ✓）**：$x\sim N$ ⟹ 相关零点自然高度 $T\sim N/h\sim\sqrt N$ ✓
   $$\boxed{T\sim\sqrt N\quad\text{且}\quad|\gamma-\gamma'|_{\text{relevant}}\lesssim\sqrt N}\ \Longrightarrow\ \textbf{局部窗口 }Y=\sqrt N\ \text{的 Fourier cutoff【正好落在零点高度同一量级】}\ \checkmark$$
⭐⭐⭐ **⑤ Montgomery 的【真正缺口】✓**：其经典可控区间 ＝ 归一化差值 $(\log T/2\pi)(\gamma-\gamma')$ 落在有限 support ⟹ 实际 $|\gamma-\gamma'|\lesssim T/\log T$ ✗；
   而**我们需要 $|\gamma-\gamma'|\lesssim T$** ✓ ⟹ $$\boxed{\text{需把 pair-correlation information 从 }T/\log T\ \textbf{推到}\ T}\ \checkmark$$
   —— ⭐ **这才是 \$\\log\$ 真正出现的位置** ✓（与"点态差一个 $\log$" ✗ 完全是两回事 ✓✓）
```

## 1. **三层墙**（✓ 逐字录取 ✓）

$$\boxed{\begin{array}{ccc}\text{RH}&\Longrightarrow&\text{零点在临界线上}\\[1mm]\downarrow&&\\\text{二阶矩}&&\text{需要 }\gamma-\gamma'\text{ 的相关}\\[1mm]&&\downarrow\\&&|\gamma-\gamma'|\lesssim T\\[1mm]&&\downarrow\\&&\text{Montgomery 已知：}\lesssim T/\log T\end{array}}$$

## 2. dyadic 分解的执行（✓ 按您指定 ✓）＋ ⚠️ **诚实簿记冲突**

$$\mathcal N=\sum_{\gamma,\gamma'}A_T(\gamma)A_T(\gamma')F_T(\gamma-\gamma')\ \xrightarrow{\ dyadic\ }\ \mathcal N=\mathcal N_{\le T/\log T}+\sum_{k\ge0}\mathcal N_k,\quad |\gamma-\gamma'|\sim2^k\frac T{\log T}$$

$$\textbf{逐层估计 ✓}：\text{pair count at }\delta\approx N(T)\cdot\frac{\log T}{2\pi}\delta\approx\frac{T\log T}{2\pi}\cdot\frac{\log T}{2\pi}\delta\ ;\qquad\text{weight}\ \frac1{|\rho||\rho'|}\approx\frac1{T^2}\ ;\qquad F_T\approx Y=T$$

$$\Longrightarrow\ \mathcal N_k\approx\frac{T\log^2T}{4\pi^2}\cdot 2^k\frac T{\log T}\cdot\frac1{T^2}\cdot T=\frac{T\log T}{4\pi^2}2^k\ \checkmark$$
$$\Longrightarrow\ \sum_k\mathcal N_k\ \text{（几何比 2，顶层 }2^k\sim\log T\text{ 主导）}\ \approx\frac{T\log^2T}{4\pi^2}=O(\sqrt N\log^2N)\ \ll\ hN=N^{3/2}\ ✗$$

$$\text{而【对角】✓}\approx(\sqrt N\log N)\cdot\frac{h^2Y}N=N\log N\ \checkmark\ \Longrightarrow\ \text{总计}\approx N\log N=o(N^{3/2})\ ✓$$

⚠️⚠️ **簿记冲突（必须公开 ✓）**：若上述成立 ⟹ **$C_3$ 无条件成立 ⟹ Legendre 可证** ✗✗
   —— **与"Legendre 已知开放"矛盾** ✗ ⟹ **我的簿记必缺一项** ✗
   ⭐ **最可疑处 ✓**：**相干性（coherence）因子** ✓ —— 我的逐层估计用了**"无相关"的 pair count**（均匀密度 ✓），
     而【点态 RH 界】$\Delta\ll\sqrt x\log^2x$ ⟹ $|\Delta|^2\ll x\log^4x$ ⟹ 窗口积分 $N^{3/2}\log^4N$ ✗
     ⟹ **两点之比 $=\sqrt N/\log^3N$ 正是"相干增益"** ✓
   $$\Longrightarrow\ \textbf{同一条 }L^2\ \text{量在【典型（随机相位）】与【全相干（对齐）】之间相差}\ \sqrt N/\log^3N\ ✗$$
   $$\Longrightarrow\ \text{我 §2 的两条界 ＝ 这两个极端 ✓ —— 而**决定实际值的是 pair correlation**（您 §4 的缺口 ✓）✓✓}$$

## 3. 三个结局与我当前的判断（✓ 按您指定 ✓）

$$\boxed{\text{①}\ \sum_k\mathcal N_k=o(hN)\ \text{（真的破墙 ✓）}\quad\text{②}\ \exists k:\ \mathcal N_k\simeq hN\ \text{（找到结构墙 ✓）}\quad\text{③}\ \text{绝对值达 }hN\ \text{但有 signed cancellation（继续做 ✓）}}$$
```
【我的判断 ✓】按【均匀 pair count】计算 ⟹ 结局 ①；但**这【假定】了无相关** ✗ ⟹ **相当于把您 §4 的缺口当成了已知** ✗
⟹ **故真实状态是：§2 的计算把缺口【藏进了假设】✗ —— 必须显式化** ✓
⭐ **因此正确的下一步（与您 §6 一致 ✓）**：不用均匀密度，而是**对每一层代入 pair correlation 的【已知部分】**
   （$k$ 小 ⟹ Montgomery 可控 ✓）与【未知部分】（$k$ 大 ⟹ 未知 ✗），看**未知层的实际上界**能到多大 ✓
```

## 4. 真正的"破墙点"（✓ 您 §6 的正规化 ✓）

```
【须检验 ✓】把非对角写成 $\mathcal N=\sum A_T(\gamma)A_T(\gamma')F_T(\gamma-\gamma')$ 后，
   按 $|\gamma-\gamma'|\sim2^k\frac T{\log T}$ 分层 ✓ —— **若第 $k$ 层获得额外衰减**（如 $F_T\ll T/\delta$ ✓）
   能抵消 pair-count 的增长 ✓ ⟹ **则【不需要】把 Montgomery support 扩到 $T$** ✓✓
   ⚠️ **但按本文 §2 ✓**：在 $|\delta|\le T$ 内 $F_T\approx Y=T$ **【不衰减】** ✗（$N/\delta\ge Y\iff\delta\le N/Y=T$ ✓）
   ⟹ **额外衰减只在 $|\delta|>T$ 出现** ✗ ⟹ **窗口本身【不提供】$|\delta|\le T$ 内的补偿** ✗
   ⟹ ⚠️ **故您 §6 的希望（$F_T\ll T/\delta$ 抵消增长）在相关区内【不成立】** ✗ —— **除非用 $W_h$ 或权重 $1/(|\rho||\rho'|)$** ✓
   $$\textbf{而权重的作用 ✓}：1/(|\rho||\rho'|)\approx1/(\gamma\gamma')\ \text{在【小 }\gamma\text{】处【增大】✗\ \text{（非减小 ✓）}$$
   ⟹ ⚠️ **故权重的净效应是【放大小}-\gamma\text{ 对】** ✗ ⟹ **它不能替代对相关** ✗ —— 须记入 ✓
```

## 5. 边界与纪律（✓）

```
✅ **① 撤回已执行 ✓**；② 录取您的双滤波器／区域／尺度巧合／Montgomery 缺口 ✓；③ **dyadic 分解已做 ✓**
⚠️ **§2 的簿记冲突【未解】✗** —— 我给出的是"按下均匀密度 ⟹ 结局 ①"，**而均匀密度正是您 §4 的缺口** ✗
   ⟹ **不声称任何结局成立** ✓ —— 只声称：**冲突的存在本身定位了缺口的所在（相干增益 $\sqrt N/\log^3N$ ✓）** ✓
⚠️ **§4 的"权重放大"是我的推导 ✗ 非定理** ✓（须核 $1/(|\rho||\rho'|)$ 在精确和中的实际作用 ✗）
⚠️ **未用 RH** ✓；**未跑 Lean** ✓；**无计算** ✓
⭐ **本轮净产出 ✓**：① 撤回 ✓；② **双滤波器与区域划分的机制** ✓；③ **尺度巧合 $T\sim\sqrt N$** ✓；
   ④ ⭐ **Montgomery 缺口的精确形式（$T/\log T\to T$）—— log 的真正位置** ✓✓；⑤ **dyadic 框架 ＋ 一处诚实冲突** ✓
```
