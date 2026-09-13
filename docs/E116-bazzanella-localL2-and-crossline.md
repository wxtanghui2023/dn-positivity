# E116 · ⭐⭐⭐ **接受修正（local $L^2$ anti-concentration）＋ 重大跨线交叉：L3 的墙 ＝ 项目 T1 的残差** ✓

> 委托 ✓ 唐先生 22:42（修正"一个 log" ✗；给出 Bazzanella 的**局部二阶矩**结构 ✓；要求直接推导
> "RH 能否推出 Bazzanella 型局部 $L^2$ anti-concentration" ✓）
> 执行 ✓ 小灵｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**无计算 ✓**；⚠️ 全文标【推导】✗ 非定理 ✓

---

## 0. 结论（✓ 五条）

```
✅ **① 接受修正 ✓**：**"一个 $\log$"的表述不成立** ✗
   $$\text{真正的墙}\ =\ \textbf{pointwise}\ \longrightarrow\ \textbf{local }L^2\ \textbf{anti-concentration}\ \checkmark$$
   Bazzanella 的对象 ✓：$J(N,h)=\int_1^N(\vartheta(x+h)-\vartheta(x)-h)^2dx$ ✓，条件 $J(N+Y,h)-J(N,h)=o(hN)$ ✓（$Y\le N^{1/2}$ ✓）
   **反例转换 ✓**：$x_j=n^2,\ Y\asymp\sqrt{x_j},\ h\asymp2\sqrt{x_j}$ ⟹ 单点异常 ⟹ 长度 $Y$ 区间内 $|\Delta|\gg h$ ⟹
   $J(x_j+Y,h)-J(x_j,h)\gg Yh^2\asymp x_j^{3/2}$ ✓ **而 $hN\asymp x_j^{3/2}$** ⟹ **恰被 $o(hN)$ 压死** ✓✓
⭐⭐⭐ **② 重大跨线交叉（本轮核心 ✓）**：**这个对象【就是】项目 E83 已归约的 T1 残差** ✓✓
   $$\text{E83 逐字 ✓：}\textbf{"T1 已严格归约为【局部短区间 Selberg 二阶矩上界】，常数余量约 9\%"}\ ✓$$
   $$\Longrightarrow\ \textbf{素数间隙线（L3：Legendre／Brocard）与 Li 范围线（T1）归约为【同一对象】}\ \checkmark\checkmark$$
   —— **两条此前完全独立的线**（一条在 $\theta$-指数侧 ✓，一条在 Li 系数侧 ✓）**撞上同一个二阶矩** ✓✓
⭐⭐ **③ 于是"攻一次多问题收益"的真实范围被定位 ✓**：**局部短区间 Selberg 二阶矩** ✓
   $$\text{若该局部界成立}\ \Longrightarrow\ \textbf{T1 ✓ ＋ L3（Legendre ＋ Brocard）✓ 同时}\ \checkmark\checkmark$$
⭐ **④ 我的部分推导 ✓（含一处待解差异 ⚠️）**：
   · **点态路线 ✗**：RH 给 $\Delta\ll\sqrt N\log^2N$ ⟹ 窗口积分 $\le Y\cdot N\log^4N=N^{3/2}\log^4N$ ✗ **超 $hN$ 一个 $\log^4$** ✗
   · **全局二阶矩路线 ✓**：RH 给 $J(X,h)\ll Xh$（Selberg ✓ 在档 ✓）⟹ **若二阶矩密度局部均匀**，则增量 $\approx Yh=N=o(N^{3/2})$ ✓✓
   ⟹ **故关键 ⟺ 【全局 Selberg 界能否局部化】** ✓ —— **而"局部化 $L^2$ 界"比点态弱 ✓ ⟹ 这是可行的中间地带** ✓✓
⭐ **⑤ 更正 arXiv 号 ✓**：**arXiv:2308.04458**（非 2308.04558 ✗）✓ —— 属**指数路线** ✓，**不可与局部二阶矩路线混谈** ✓
```

## 1. Bazzanella 机制的逐字录取（✓ 唐先生提供 ＋ 文献 ✓）

$$J(N,h)=\int_1^N\bigl(\vartheta(x+h)-\vartheta(x)-h\bigr)^2dx\ ✓\qquad\text{条件 ✓}\ J(N+Y,h)-J(N,h)=o(hN)\quad(Y\le N^{1/2})\ \checkmark$$
$$\text{反例（$x_j=n^2$ ✓）}\ \Longrightarrow\ |\Delta(x,h)|\gg h\ \text{在长}\ Y\asymp\sqrt{x_j}\ \text{的区间 ✓}\ \Longrightarrow\ J(x_j{+}Y,h)-J(x_j,h)\gg Yh^2\asymp x_j^{3/2}\ ✓$$
$$\text{而}\ hN\asymp\sqrt{x_j}\cdot x_j=x_j^{3/2}\ \Longrightarrow\ \boxed{o(hN)\ \textbf{恰好压死反例}}\ \checkmark$$
$$\textbf{外部要点 ✓}：\text{Bazzanella 的 Conjecture 3 \textbf{弱于} Montgomery 强 pair-correlation 假设 ✓，却足以推出}\ \psi((n{+}1)^2)-\psi(n^2)\sim2n\ ✓$$
$$\textbf{故真正需要的量级 ✓}：\mathcal E:=\Delta J=o(hN)\ \text{—— \textbf{不是}"省一个 $\log$" ✗，而是\textbf{反例必须【无法局部集中】}} ✓✓$$

## 2. 我的部分推导（✓ 公开差异 ⚠️）

$$\text{两条可得界的【矛盾】✓}：$$
| 路线 | 得到的局部积分 | 与所需 $o(hN)=o(N^{3/2})$ 比 |
|:--|:--|:--|
| **点态（RH ✓）** $\Delta\ll\sqrt N\log^2N$ | $Y\cdot N\log^4N=N^{3/2}\log^4N$ | ✗ **大 $\log^4$** |
| **全局二阶矩（RH＋Selberg ✓）** $J\ll Xh$ | **若密度均匀**：$\approx Yh=N$ | ✓ **小 $\sqrt N$** |

$$\Longrightarrow\ \boxed{\textbf{关键问题 ✓}：\text{RH ＋ Selberg 全局界能否【局部化】为：对每个长 }Y\asymp\sqrt N\ \text{的窗口，}\ \int_{\text{window}}\Delta^2\ll Yh\ ?}$$
$$\Longrightarrow\ \text{若能 ✓}\ \Longrightarrow\ \mathcal E=Yh=o(hN)\ \Longrightarrow\ \textbf{Bazzanella 条件成立 ✓}\ \Longrightarrow\ \textbf{Legendre ＋ Brocard}\ ✓$$

⚠️ **待解差异 ✓**：两条界限相差 $\sqrt N/\log^4N$ ✗ —— **真相在两者之间** ✗；
   **我不声称已证任一端** ✗ —— 而这个差异**正是该问题的核心** ✓（＝二阶矩能否局部均匀 ✓）

## 3. ⭐⭐⭐ 跨线交叉（✓ 本轮最重要 ✓）

```
`E83-constant-audit.md` 逐字 ✓（本项目 2026-09-13 早先 ✓）：
   "**T1 已严格归约为局部短区间 Selberg 二阶矩上界，常数余量约 9.0%**" ✓
   ＋ E84b ✓："所有 band 都是 $[0,T]$ 的常数分数（0.052–0.699 ✓），**非短区间** ⟹ 可由 Selberg 全局二阶矩相减得到 ✓"
⟹ ⟹ **故两条线【归约为同一对象】✓✓**：
   $$\text{Li 范围线（T1 ✓）：需要}\ \int_I|E|^2\ \text{的局部界}\ ✓\qquad\text{素数间隙线（L3 ✓）：需要}\ J(N+Y,h)-J(N,h)=o(hN)\ ✓$$
   $$\textbf{两者都是【局部短区间 Selberg 二阶矩】} ✓✓$$
⭐ **结构意义 ✓**：这与唐先生指出的"**反例不能局部集中**"是**同一件事** ✓✓ ——
   而它与项目反复撞的 β 墙**不同** ✓（β 墙是**点态/符号**型 ✗；此处是**$L^2$/能量**型 ✓ ⟹ **逻辑出口不同** ✓✓）
```

## 4. 判据与下一步（✓）

$$\boxed{\text{攻一次 ⟹ T1 ＋ L3（Legendre ＋ Brocard）同时收益} \Longleftrightarrow \textbf{局部短区间 Selberg 二阶矩界}}$$

**下一步（唯一，按唐先生指定 ✓）**：**直接推导"RH ⟹ 局部 $L^2$ anti-concentration"** ✗
```
【第一刀 ✓】核 E83／E93 的**局部 Selberg 常数**与 Bazzanella 的 $o(hN)$ 是否**同一量级要求** ✓
   —— 若是 ⟹ **两条线的余量可以互借** ✓；若否 ⟹ 记下两套常数 ✓
【第二刀 ✓】核 Selberg 1943 的**局部版原文形态**（其证明是全局和 ✓，能否逐窗口 ✓）✗
【第三刀 ✓】若局部化不成立 ⟹ **精确算出 RH 允许的最小集中量** ✓（＝唐先生要求的"若不能，明确算出来"✓）
```

## 5. 边界与纪律（✓）

```
✅ **接受修正 ✓**（"一个 $\log$" ✗）；**更正 arXiv 号 ✓**（2308.04458 ✓）
⚠️ **§2 的推导为【部分】✗**：两条界限并存且相差 $\sqrt N/\log^4$ ⚠️ —— **未解差异，不声称已证** ✓
⚠️ **§3 的交叉是【对象识别】✓**：我核的是**两处文字描述**（E83 的"局部短区间 Selberg 二阶矩" ✓ 与 Bazzanella 的 $J$ ✓）
   —— **二者是否【严格同对象】须核 E83 原文的精确表述** ✗（下一步第一刀 ✓）
⚠️ **未用 RH** ✓（除引用在档的 RH 条件结果 ✓）；**未跑 Lean** ✓；**无计算** ✓
⭐ **纪律 ✓（本轮合规 ✓）**：开工前 grep（E83／E84b／Selberg ✓）＋ 外部走原文 ✓
```
