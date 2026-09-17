# 严格化重做：反证链 $D=0\Longrightarrow\mathrm{RH}$（首版论文期）

> **任务**：唐先生 2026-09-17 19:22 指示 —— "把我们之前关于有限个离轴零点的证明（反证法，这是最初一版论文时的证明了）提取出来，重新做一下严格化"。
> **出处**：`docs/candidate-proof-v1.md`（2026-08-31，"Candidate Proof v1: $D=0\Longrightarrow$ RH（配对歧义可解——Hadamard 闭合链）"），与首版论文 `papers/rh-discriminator-v28.tex`（2026-08-30）同期。
> **已有相关档**：`rh-discriminator-lemmas.md`（8/30，三引理骨架）、`grh-criterion-proof.md`（8/31，$w_H$／$P_\gamma$ 代数深化）。
> **地图检查**：已查 `CLOSED-ROUTES-MAP`／`MASTER-STATUS`／`ASSETS-REGISTRY`／`WALLS-DIFFICULTIES-LEDGER`。`candidate-proof-v1` 仅被 `A13-2b-theorem-B-label-collision.md` 引用，记为"**失败的尝试**（Hadamard 闭式 ✗）"。本档**不新增路线**，只对该既有条目做提取与严格化。
> **证据等级**：`[出处]` 逐字取自原档；`[严格]` 本档给出完整证明；`[自己推]` 本档新推的闭式；`[数值]` 本档实际跑出。

已查地图：**未覆盖**（所查档：`CLOSED-ROUTES-MAP.md`、`MASTER-STATUS-AND-CLOSURES.md`、`MASTER-NOGO-AND-LIVE-PATHS.md`、`ASSETS-REGISTRY.md`、`WALLS-DIFFICULTIES-LEDGER.md`、`REVIEW-LEDGER-22-items-tracker.md`；关键词：`candidate-proof-v1`、`D=0`、`Hadamard 闭式`、`离轴零点`、`有限个离轴`、`S_gamma`、`C_1`/`7.38e-5`。命中：`candidate-proof-v1` 仅被 `A13-2b-theorem-B-label-collision.md` 引用（记为"失败的尝试"）；`E4-palojarvi-finitely-many.md` 为"至多 m 个离轴"的另一条已闭合线；其余为判据分散档（`rh-discriminator-lemmas.md`、`grh-criterion-proof.md`）。**结论：本档不新增路线，仅对既有条目做提取＋严格化**）

---

## §0 提取：原始反证链（逐字摘要）

原档 `[出处]` 的引理链如下（每一步都自称"无条件——对 $\zeta$ 的实际零点——无论在线与否"）：

$$\textbf{引理 A（轨道差正性）}：P_\gamma(\delta)\ge0，=0\iff\delta=0$$
$$\textbf{引理 B（}D\text{ 的表示与正性）}：D:=\sum_\rho[\tilde h(\rho)-\tilde h(\tfrac12+i\gamma_\rho)]=\sum_{\text{轨道}}P_\gamma(\delta)\ge0$$
$$\textbf{引理 C–E（无条件常数）}：\sum_\rho\frac{1}{[1-(\rho-\tfrac12)^2]^2}=C_1:=\tfrac14\big[L(\tfrac32)-L(-\tfrac12)-L'(\tfrac32)-L'(-\tfrac12)\big]$$
$$\textbf{引理 F}：\sum_\rho q(\gamma_\rho)=C_1\quad(\text{原档称"无条件"})\qquad
\textbf{引理 G}：D=C_1-C_1=0$$
$$\textbf{引理 H}：D\ge0\ \wedge\ D=0\ \Longrightarrow\ \sum_{\text{轨道}}P_\gamma(\delta)=0\ \Longrightarrow\ \text{每项 }P_\gamma(\delta)=0\ \Longrightarrow\ \delta\equiv0\ \Longrightarrow\ \textbf{RH}$$

其中（原档冻结）：$\tilde h(s)=-\dfrac{1}{[1-(s-\frac12)^2]^2}$，$q(t)=\dfrac{1}{(1+t^2)^2}$，$\tilde h(\tfrac12+it)=-q(t)$，$L=\xi'/\xi$，$\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$。

**原档自列的 4 处待查漏洞**（逐字）：①引理 C 的"函数方程配对 = 绝对收敛"需严格证明；②引理 D 的 $\sum\frac{1}{3/2-\rho}+\sum\frac{1}{\rho+1/2}=L(3/2)-L(-1/2)$ 需严格写；③"实际 vs 人造"的区别需严格论证；④$\gamma$ 集合的确定性需严格陈述。

---

## §1 记号（冻结，全部为 $\zeta$ 的实际零点所定义，无 RH 输入）

设 $\rho=\tfrac12+\delta_\rho+i\gamma_\rho$ 遍历 $\xi$ 的非平凡零点（含重数），$\delta_\rho\in(-\tfrac12,\tfrac12)$。令

$$L(s):=\frac{\xi'(s)}{\xi(s)},\qquad
\tilde h(s):=-\frac{1}{[1-(s-\tfrac12)^2]^2},\qquad
q(t):=\frac{1}{(1+t^2)^2}=-\tilde h(\tfrac12+it)$$

$$\textbf{轨道}：\text{把 }\{\rho,\,1-\bar\rho\}=\{\tfrac12+\delta+i\gamma,\ \tfrac12-\delta+i\gamma\}\ \text{视为一个轨道（}\delta\ge0\text{）}；\qquad
P_\gamma(\delta):=\tilde h(\tfrac12+\delta+i\gamma)+\tilde h(\tfrac12-\delta+i\gamma)-2\tilde h(\tfrac12+i\gamma)$$

$$D:=\sum_\rho\big[\tilde h(\rho)-\tilde h(\tfrac12+i\gamma_\rho)\big],
\qquad
S_\gamma:=\sum_\rho\frac{1}{(1+\gamma_\rho^2)^2},\qquad
C_1:=\tfrac14\big[L(\tfrac32)-L(-\tfrac12)-L'(\tfrac32)-L'(-\tfrac12)\big]$$

**注 1.1（记账约定，本档改正）**：$\sum_\rho$ 按 $\xi$ 的全部非平凡零点计数；零点成对出现 $\rho,\bar\rho$，故**每个正纵标 $\gamma_k$ 被计两次**，即
$$S_\gamma=2\sum_{k\ge1}\frac{1}{(1+\gamma_k^2)^2}\quad(\gamma_k>0\ \text{递增})$$
原档数值核对若只取正 $\gamma$，须乘 2 —— 这是原链一处记账含糊，本档统一。

---

## §2 引理 A 严格版（轨道正性）

**定理 A** `[严格]`。设 $\gamma\ge1$，$0\le\delta<\tfrac12$。则
$$P_\gamma(\delta)=\frac{2N(\gamma,\delta)}{(1+\gamma^2)^2\,W(\gamma,\delta)^2}\ \ge\ 0,\qquad P_\gamma(\delta)=0\iff\delta=0$$
其中
$$W:=(1+\gamma^2-\delta^2)^2+4\delta^2\gamma^2,\qquad
N:=\delta^2\Big[10\gamma^6+18\gamma^4+6\gamma^2-2+\delta^2(5\gamma^4-6\gamma^2+5)+4\delta^4(\gamma^2-1)+\delta^6\Big]$$

**证明** `[自己推]`。记 $u:=\delta+i\gamma$。由 $(\tfrac12+\delta+i\gamma)-\tfrac12=u$、$(\tfrac12-\delta+i\gamma)-\tfrac12=-\bar u$：
$$P_\gamma(\delta)=-2\,\mathrm{Re}\frac{1}{(1-u^2)^2}+\frac{2}{(1+\gamma^2)^2}
=2\Big[\frac{1}{(1+\gamma^2)^2}-\frac{A^2-B^2}{W^2}\Big]$$
其中 $1-u^2=A+iB$，$A=1+\gamma^2-\delta^2$，$B=-2\delta\gamma$，$W=A^2+B^2=|1-u^2|^2$。通分得
$$P_\gamma(\delta)=\frac{2N}{(1+\gamma^2)^2W^2},\qquad N:=W^2-(A^2-B^2)(1+\gamma^2)^2$$
把 $N$ 展开并因式分解（本档对 $\delta,\gamma$ 作精确符号展开）恰得上式 $N$。**正性**：$\gamma\ge1$ 时 $5\gamma^4-6\gamma^2+5>0$、$\gamma^2-1\ge0$、$\delta^6\ge0$，故
$$N\ \ge\ \delta^2\big[10\gamma^6+18\gamma^4+6\gamma^2-2\big]\ >\ 0\quad(0<|\delta|,\ \gamma\ge1)$$
且 $N=0\iff\delta=0$。$\square$

**推论 A.1（衰减率）** `[自己推]`。$\gamma\to\infty$ 时 $A\sim\gamma^2$，$W\sim\gamma^4$，$N\sim10\delta^2\gamma^6$，故
$$P_\gamma(\delta)\ =\ \frac{20\delta^2}{\gamma^6}\big(1+O(\gamma^{-2})\big)$$
**数值** `[数值]`：$\gamma=10^3,\ \delta=0.1$ 时 $P=1.9999915\times10^{-19}$，而 $20\delta^2\gamma^{-6}=2.0\times10^{-19}$ ✓。

---

## §3 引理 B 严格版（轨道分解与绝对收敛）

**定理 B** `[严格]`。级数 $D:=\sum_\rho[\tilde h(\rho)-\tilde h(\tfrac12+i\gamma_\rho)]$ **绝对收敛**，且按轨道配对后
$$D=\sum_{\text{离轴轨道}}P_\gamma(\delta)\ \ge\ 0$$
（在轴轨道贡献**恰为** $0$；求和只对离轴轨道非平凡。）

**证明**。由函数方程 $\xi(s)=\xi(1-s)$，$\rho$ 与 $1-\bar\rho$ 同时为零点且纵标相同 ✓（**这关闭原档漏洞 ④的实质内容**：纵标多重集 $\{\gamma_\rho\}$ 只由 $\zeta$ 决定，与 RH 真假无关）。把 $\sum_\rho$ 按轨道 $\{\rho,1-\bar\rho\}$ 分组：若 $\delta=0$（在轴），两项各等于 $\tilde h(\tfrac12+i\gamma)$，贡献 $0$；若 $\delta>0$，贡献恰为 $P_\gamma(\delta)$ ✓。由推论 A.1，$P_\gamma(\delta)\ll\delta^2\gamma^{-6}$，而 $\sum_\rho\gamma_\rho^{-6}<\infty$（因 $N(T)\ll T\log T$）⟹ 按轨道求和绝对收敛 ⟹ 可以任意重排 ✓。由定理 A，$D\ge0$。$\square$

---

## §4 引理 C–E 严格版（无条件常数 $C_1$）

**定理 C** `[严格]`。$\displaystyle\sum_\rho\frac{1}{[1-(\rho-\tfrac12)^2]^2}=C_1=\frac14\big[L(\tfrac32)-L(-\tfrac12)-L'(\tfrac32)-L'(-\tfrac12)\big]$，无条件。

**证明**。（i）**偏分式**（本档精确核验，见 §8）：以 $u=\rho-\tfrac12$ 记，
$$\frac{1}{[1-(\rho-\frac12)^2]^2}=\frac{1}{(1-u)^2(1+u)^2}
=\frac14\Big[\frac{1}{(1-u)^2}+\frac{1}{(1+u)^2}\Big]+\frac14\Big[\frac{1}{1-u}+\frac{1}{1+u}\Big]$$
而 $1-u=\tfrac32-\rho$，$1+u=\rho+\tfrac12$ ✓。
（ii）**Hadamard**：$\xi$ 整、$\xi(0)=\tfrac12\ne0$，其 Hadamard 分解给出
$$L(s)=\frac{\xi'(s)}{\xi(s)}=B+\sum_\rho\Big[\frac{1}{s-\rho}+\frac{1}{\rho}\Big],\qquad B=L(0)$$
（$s=0$ 代入即得 $B=L(0)$：$\sum_\rho[-\frac1\rho+\frac1\rho]=0$ ✓）。逐项求导（在 $s\ne\rho$ 处一致收敛）：
$$L'(s)=-\sum_\rho\frac{1}{(s-\rho)^2}\ \Longrightarrow\
\begin{cases}\sum_\rho \frac{1}{(3/2-\rho)^2}=-L'(3/2)\\[2mm] \sum_\rho \frac{1}{(\rho+1/2)^2}=-L'(-1/2)\end{cases}$$
（注意 $\frac{1}{(-1/2-\rho)^2}=\frac{1}{(\rho+1/2)^2}$ ✓。）
（iii）**常数项抵消**：作差
$$L(\tfrac32)-L(-\tfrac12)=\sum_\rho\Big[\frac{1}{3/2-\rho}-\frac{1}{-1/2-\rho}\Big]=\sum_\rho\Big[\frac{1}{3/2-\rho}+\frac{1}{\rho+1/2}\Big]=\sum_\rho\frac{2}{(3/2-\rho)(\rho+\frac12)}$$
$B$ 相消 ✓；且末式**绝对收敛**（$|(3/2-\rho)(\rho+\frac12)|\asymp\gamma_\rho^2$）⟹ 无需任何配对/条件收敛论证 ✓。
（iv）合起来：$\sum_\rho\frac{1}{[1-(\rho-\frac12)^2]^2}=\frac14\big[-L'(\tfrac32)-L'(-\tfrac12)+L(\tfrac32)-L(-\tfrac12)\big]=C_1$ ✓ $\square$

**注 4.1（原始 4 漏洞中 ①②在此关闭）**：原档担心的"函数方程配对的合法性"其实**不需要**——所有出现的级数都是绝对收敛的（i–iii 步各自注明）✓。

---

## §5 严格重做版定理（本档主产出）

**定理 D** `[严格]`。$\displaystyle D=S_\gamma-C_1$，其中 $S_\gamma:=\sum_\rho\frac{1}{(1+\gamma_\rho^2)^2}$。

**证明**。$\tilde h(\rho)=-\frac{1}{[1-(\rho-\frac12)^2]^2}$，$\tilde h(\tfrac12+i\gamma_\rho)=-\frac{1}{(1+\gamma_\rho^2)^2}$。故
$$D=\sum_\rho\tilde h(\rho)-\sum_\rho\tilde h(\tfrac12+i\gamma_\rho)
=-\sum_\rho\frac{1}{[1-(\rho-\frac12)^2]^2}+\sum_\rho\frac{1}{(1+\gamma_\rho^2)^2}\ \overset{\S4}{=}\ -C_1+S_\gamma\ \ \square$$

**定理 E（无条件单向不等式）** `[严格]`。
$$S_\gamma=\sum_\rho\frac{1}{(1+\gamma_\rho^2)^2}\ \ge\ C_1=\frac14\big[L(\tfrac32)-L(-\tfrac12)-L'(\tfrac32)-L'(-\tfrac12)\big]$$
**证明**。$D=S_\gamma-C_1$（定理 D）；$D\ge0$（定理 B）✓ $\square$

**定理 F（判据，双向）** `[严格]`。
$$\boxed{\ \mathrm{RH}\iff S_\gamma=C_1\iff D=0\ }$$
**证明**。（$\Longleftarrow$）$D=0$ 且 $D=\sum_{\text{离轴轨道}}P_\gamma(\delta)$（定理 B）为**非负项级数** ⟹ 每项 $P_\gamma(\delta)=0$ ⟹ 由定理 A，$\delta=0$ ⟹ 无离轴零点 ⟹ RH ✓。
（$\Longrightarrow$）RH ⟹ 每个 $\rho=\tfrac12+i\gamma_\rho$ ⟹ $\tilde h(\rho)=\tilde h(\tfrac12+i\gamma_\rho)$ **逐项** ⟹ $D=0$ ✓ ⟹ $S_\gamma=C_1$（定理 D）✓ $\square$

**数值** `[数值]`（见 §8）：$C_1=7.3772455\times10^{-5}$；前 300 个零点 $2\sum_{k\le300}(1+\gamma_k^2)^{-2}=7.376929\times10^{-5}$，差 $3.3\times10^{-9}\approx$ 尾部积分估计 $2\times10^{-9}$ ✓ —— 与 RH 为真一致 ✓（**注意：这既不能证也不能否**）。

---

## §6 缺口定位：原链第 F 步 $\iff$ RH（故原链循环）

原档 §5 引理 F 断言"$\sum_\rho q(\gamma_\rho)=C_1$ **无条件**"，其理由只有一句"在线时：$\sum q(\gamma)=\sum\frac{1}{[1-(\rho-\frac12)^2]^2}$（逐项相等）$=C_1$"。

**命题 G** `[严格]`。"$S_\gamma=C_1$ 无条件" $\iff$ RH。
**证明**。即定理 F：$S_\gamma=C_1\iff$ RH ✓（两个方向都不需要额外假设）。$\square$

**结论**：原链的"反证"在第 F 步把**待证命题**当作已知（逐项相等只在 RH 下成立）⟹ 整条链得到的是**判据（重述）**而非证明 ✓。这与 `A13-2b` 把 `candidate-proof-v1` 记为"失败的尝试（Hadamard 闭式 ✗）"一致，但此处给出了**严格的失败理由**：失败点唯一且可定位（F $\iff$ RH），其余各步（A、B、C、D）**全部严格成立** ✓。

---

## §7 ⭐ 有限个离轴零点版本（唐先生所询的形态）

前面 $D$ 的求和对全部零点；当离轴轨道**有限**时，$D$ 退化为**有限的显式正项和**：

**定理 H$_m$** `[严格]`。设 $\xi$ 的离轴轨道（即 $\delta\ne0$ 的 $\{\rho,1-\bar\rho\}$）**至多 $m$ 个**，记为 $(\gamma_j,\delta_j)_{j\le m}$（$\delta_j\in(0,\frac12)$）。则
$$D=\sum_{j=1}^{m}P_{\gamma_j}(\delta_j)\qquad(\textbf{有限和，无尾部})$$
并且
$$\mathrm{RH}\iff\sum_{j=1}^{m}P_{\gamma_j}(\delta_j)=0\iff \delta_j=0\ \ \forall j\le m$$
**证明**。定理 B 的轨道分解中，在轴轨道贡献恰为 $0$；离轴轨道恰 $m$ 个 ⟹ 求和只有 $m$ 项 ✓；再由定理 A（$P_{\gamma_j}(\delta_j)=0\iff\delta_j=0$）✓ $\square$

**推论 H$_m'$（定量检测）** `[严格]`。设在轴外存在一个轨道满足 $|\delta|\ge\delta_0>0$ 且 $\gamma\le\Gamma$。则
$$D\ \ge\ \min_{\gamma_1\le\gamma\le\Gamma}\frac{2\big[10\gamma^6+18\gamma^4+6\gamma^2-2\big]}{(1+\gamma^2)^2\,W(\gamma,\delta_0)^2}\cdot\delta_0^2\ =:\ \kappa(\delta_0,\Gamma)\ >\ 0$$
即**离轴质量被一个显式正下界探测**（$P_\gamma(\delta)\ge\kappa$ 型），且无任何 RH 输入 ✓。

**注 7.1（与档案的联系）**：该"有限个 ⟹ 有限检测"的形态与 `docs/E4-palojarvi-finitely-many.md`（把 Palojärvi 定理 4.1 的"至多一个离轴零点"推广到"至多 $m$ 个"，2026-09-12 闭合）同型：都是把"离轴"编码为**有限可判决**的算术/解析事件。差别：E4 的检测量是 $\lambda_F(n,\tau)$ 的大 $n$ 行为（检出依赖"大 $n$"），本档的检测量是 $D=S_\gamma-C_1$（一个**常数级**量，但需要"$S_\gamma$ 可无条件算出"这一条，即定理 F ⟹ RH 的那一步）✗。

---

## §8 数值核验（全部本档实际跑出；`mpmath` 1.3.0，dps=25–30）

| 核验项 | 结果 | 结论 |
|:--|:--|:--|
| $C_1=\frac14[L(\frac32)-L(-\frac12)-L'(\frac32)-L'(-\frac12)]$ | $7.3772455\times10^{-5}$ | 与原档 $7.38\times10^{-5}$ 相符 ✓ |
| 分项 $L(\frac32),L(-\frac12)$ | $+0.04613592806,\ -0.04613592806$ | 反号（函数方程）✓ |
| 分项 $L'(\frac32),L'(-\frac12)$ | $0.04598838315,\ 0.04598838315$ | 相等 ✓ |
| 偏分式恒等式 | $u\in\{0,0.5,0.37\}$：LHS$-$RHS $=0,\ 0,\ 2\times10^{-31}$ | **精确成立** ✓ |
| $2\sum_{k\le300}(1+\gamma_k^2)^{-2}$ | $7.376929\times10^{-5}$ | 与 $C_1$ 差 $3.3\times10^{-9}$（= 尾部估计）✓ |
| $P_\gamma(\delta)\ge0$ | $\gamma\in\{14.13,50,100,10^3,5\times10^3\}$，$\delta\in\{0.001,\dots,0.49\}$ | 全为正 ✓ |
| 渐近 $P_\gamma(\delta)\sim20\delta^2\gamma^{-6}$ | $\gamma=10^3,\delta=0.1$：$1.9999915\times10^{-19}$ vs $2.0\times10^{-19}$ | 吻合 ✓ |
| $\delta\to0$ 行为 | $\delta=0.1,0.01,0.001$：$P/\delta^2\to3.0924\times10^{-7}$（$\gamma=20$） | 二次小量 ✓ |

**数值纪律**：以上仅作**核对**，不作证明输入；$\gamma_k$ 取自 `mpmath.zetazero`（已知零点表）；全部有限计算，未用 RH 假设推导任何一步 ✓。

---

## §9 边界、处置与不声称

**原档 4 处漏洞的逐条处置** `[严格]`：
1. "函数方程配对 = 绝对收敛，需严格证明" → **关闭** ✓：§4(iii) 显示该级数本身绝对收敛，配对论证不必要（§4 注 4.1）。
2. "$\sum\frac{1}{3/2-\rho}+\sum\frac{1}{\rho+1/2}=L(3/2)-L(-1/2)$ 需严格写" → **完成** ✓：§4(ii)–(iii)，$B=L(0)$ 相消。
3. "实际 vs 人造的区别需严格论证" → **消解** ✓：$D$ 与 $S_\gamma$ 都是 $\xi$ 的**实际**零点集的无条件泛函；人造配置定义的是**另一个常数**，故"人造离轴 $\Sigma\ne C_1$"本就不是反例，无需区分（§5、§6）。
4. "$\gamma$ 集合的确定性需严格陈述" → **关闭** ✓：由 $\xi(s)=\xi(1-s)$，纵标多重集 $\{\gamma_\rho\}$ 由 $\zeta$ 唯一决定，与 RH 无关（§3）。
5. **新增（真正的缺口）**：第 F 步 $\iff$ RH ⟹ 循环（§6 命题 G）。

**不声称**：
- **不声称证明 RH**。本档产出 = ①**提取**（原档逐字结构）；②**严格化**（定理 A、B、C、D、E、F、H$_m$ 全部有完整证明）；③**缺口精确化**（唯一缺口 = F $\iff$ RH）；④**有限个离轴版本**（定理 H$_m$／推论 H$_m'$）。
- 判据 $S_\gamma=C_1\iff$ RH 与首版论文 v2.8 的 $Q=Q'_{\mathrm{RH}}\iff$ RH 是同一判据的不同写法（$D=Q-Q'_{\mathrm{RH}}$ 至符号/归一化），**不构成新判据** ✓。
- 该判据属"机械 × 输入"型（`E30-2`）：单向不等式给予"输入"分量，跨过等号仍需独立输入 ⟹ 与 `W6`／`SUPPORT-1` 同址，**不构成突破** ✓。
- 数值仅核对，未使用任何"RH 为真"的假设作推导输入 ✓。
