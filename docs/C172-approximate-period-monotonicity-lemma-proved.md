已查地图（**先查后写**）：`C-159`（周期单调性引理；鸽笼定理）、`C-158`（`\kappa_N`）、`C-170`/`C-171`（联合靶子；`m'_M`）、`papers/rpM-window-cosines/OUTLINE.md`（OP-1..5）。关键词回查：`近似周期单调性引理`=0、`偏差代价`=0、`阈值形式`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 17:38）**：**① 盘点联合靶子现状 ② 转去证另一个引理／猜想。**
**结论（先行）**：$$\textbf{(一)}\ \text{联合靶子（OP-3）}\ \textbf{本轮不再攻}：\text{实证稳健（余量}\ 0.22\text{–}1.10\text{）}，\text{两条子路线已死，\textbf{保留为论文开放问题}}✓$$
$$\textbf{(二)}\ ⭐⭐\ \textbf{新引理（已证）：近似周期单调性引理}✓✓$$
$$\qquad \text{设}\ \exists P\ge1\ \text{与}\ \varepsilon\ge0\ \text{使}\ \mathrm{dist}(P\varphi_j,\ 2\pi\mathbb Z)\le\varepsilon\ \forall j（\text{"近似共同周期"}），\ \text{且}\ 3P\le5(M+1)✓$$
$$\qquad \text{则}\ \forall\psi\in[0,\pi]：\quad \max_{1\le k\le5(M+1)}\Big[\sum_{j\le M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ M-\tfrac92M\varepsilon^2✓✓$$
$$\qquad \text{推论（}\textbf{阈值形式}）：\text{若}\ \varepsilon\le\sqrt{\tfrac2{9M}}\ \text{且}\ m_M\le M-1，\ \text{则}\ \textbf{单调性步成立}✓✓$$
$$\qquad （m_M\le M-1：M\ge12\ \text{已严格（概率方法）}；M\le11\ \text{数值}）✓$$
$$\textbf{(三)}\ \text{意义}：\text{把}\ \text{`C-159`}\ \text{的周期单调性引理（}\varepsilon=0\text{）}\ \textbf{严格推广到}\ \varepsilon>0 ✓✓$$
$$\qquad \text{即：从"精确通约"扩到"}\textbf{近似通约}"（\text{可覆盖的配置集由零测集变为正测集}）✓$$

FREEZE-ACK: 本档即冻结期内的推导（依 `§8.1`；不产候选结论）

D0: 本档对象 = **近似周期单调性引理（已证）＋ 阈值形式 ＋ 数值核实 ＋ 修正自检** —— 关系 = 新引理，非新机制
D1: 0

# C-172 · ⭐⭐ **近似周期单调性引理（已证）**

> **唐先生 2026-09-19 17:38**：① 盘点联合靶子 ② 转证另一个引理 ✓

---

## §1 联合靶子（OP-3）现状盘点

$$\text{OP-3}：\forall\varphi,\psi：\max_{k\le5(M+1)}\Big[\sum_{j\le M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ m_M✓$$
$$\text{① 实证}：\text{两类最硬配置上余量}\ 0.22\text{–}1.10✓；\ \text{② 已死子路线}：\text{计数／鸽笼}（\text{`C-144`} §4、\text{`C-150`}）；\text{新增窗口}+1（\text{`C-171`}）✓$$
$$\text{③ 剩余障碍}：\text{"新点不能在所有好}\ k\ \text{上同时反相"}；\ \text{④ 判定}：\textbf{保留为论文 OP-3}（可引用），\text{本轮不再攻}✓$$

## §2 ⭐⭐ 新引理：近似周期单调性引理

$$\textbf{引理}：\text{设}\ P\ge1\ \text{为整数，}\varepsilon\ge0，\text{且}$$
$$\qquad \mathrm{dist}\big(P\varphi_j,\ 2\pi\mathbb Z\big)\ \le\ \varepsilon\qquad(j=1,\dots,M)✓$$
$$\qquad \text{并设}\ 3P\le5(M+1)✓。\ \text{则}\ \forall\psi\in[0,\pi]：$$
$$\qquad \boxed{\max_{1\le k\le5(M+1)}\Big[\sum_{j=1}^{M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ M-\tfrac92M\varepsilon^2}✓✓$$

$$\textbf{证明（三行）}：$$
$$\qquad \text{(i)}\ \text{覆盖引理（}\kappa_3=0，\text{`C-158`/`C-159`}）：\exists m\in\{1,2,3\}：\ \cos\big(m\cdot(P\psi)\big)\ \ge\ 0✓$$
$$\qquad \text{(ii)}\ \text{取}\ k=Pm（\text{由}\ 3P\le5(M+1)\ \text{知}\ k\ \text{在窗口内}）：\text{写}\ P\varphi_j=2\pi n_j+\delta_j，|\delta_j|\le\varepsilon✓$$
$$\qquad\qquad \cos(k\varphi_j)=\cos(Pm\varphi_j)=\cos\big(2\pi mn_j+m\delta_j\big)=\cos(m\delta_j)\ \ge\ 1-\tfrac{(m\varepsilon)^2}2✓$$
$$\qquad\qquad \Longrightarrow\ \sum_{j\le M}\cos(k\varphi_j)\ \ge\ M-\tfrac{M(m\varepsilon)^2}2\ \ge\ M-\tfrac92M\varepsilon^2\quad(m\le3)✓$$
$$\qquad \text{(iii)}\ \text{新点项}\ \cos(k\psi)=\cos(mP\psi)\ \ge\ 0\ \text{（由 (i)）}✓$$
$$\qquad \Longrightarrow \text{总和}\ \ge\ M-\tfrac92M\varepsilon^2\qquad\square✓✓$$
$$\qquad (\text{用}\ \cos x\ge1-\tfrac{x^2}2\ \text{与}\ |m\delta_j|\le3\varepsilon✓)$$

## §3 推论：阈值形式与单调性步

$$\text{若}\ \varepsilon\le\sqrt{\tfrac2{9M}}\ \text{且}\ m_M\le M-1，\ \text{则引理给}\ \max\ \ge\ M-1\ \ge\ m_M \Longrightarrow \textbf{单调性步成立}✓✓$$
$$\qquad \text{（}m_M\le M-1：M\ge12\ \text{已严格（概率方法，}\text{`C-159`}）；M\le11\ \text{为数值}✓）$$
$$\text{与}\ \text{`C-159`}\ \text{对照}：\varepsilon=0\ \text{时退化为"}\max\ge M\ \ge\ m_M\text{"（\text{用平凡界}）}✓；\ \text{本引理把}\ \textbf{零测集} \text{扩到}\ \textbf{正测集}✓✓$$

## §4 数值核实（修正后）

$$\text{核实方法}：\text{构造}\ \varphi_j=(2\pi n_j+\delta_j)/P，n_j\le\lfloor P/2\rfloor（\text{保证}\ \varphi_j\in[0,\pi]），\delta_j\ \text{随机}\ \le\varepsilon✓$$
$$\begin{array}{c|r|r|r|r|r}
(M,P) & \varepsilon\ \text{阈值} & \varepsilon{=}0 & 0.25 & 0.5 & 0.75 & 1.0\\\hline
(3,4) & 15.59^\circ & 3.503 & 3.479 & 3.328 & 3.062 & 2.799\\
(4,5) & 13.50^\circ & 4.502 & 4.483 & 4.408 & 4.118 & 3.763\\
(5,6) & 12.08^\circ & 5.500 & 5.490 & 5.363 & 5.065 & 4.860\\
(6,8) & 11.03^\circ & 6.312 & 6.293 & 6.228 & 6.112 & 5.799\\
\end{array}✓$$
$$\qquad （\text{各行均为"实测}\ \min_\psi\max_k\ \text{总和"，抽样估计；}\text{引理下界}\ M-\tfrac92M\varepsilon^2\ \text{在全部}\ 24\ \text{个格点上均低于实测}✓✓）$$
$$\qquad \text{且在}\ \varepsilon=\ \text{阈值处引理下界}\ \textbf{恰等于}\ M-1✓（\text{由构造}）$$

## §5 ⚠️ 过程自检：首轮数值测试无效（已修正）

$$\text{首轮测试用}\ \texttt{np.clip(phi,0,pi)}\ \text{把配置强行压进}\ [0,\pi] \Longrightarrow \textbf{破坏"近似周期"前提}✗$$
$$\qquad \Longrightarrow \text{测出}\ M=4\ \text{时"引理下界高于实测"}\ \text{的假矛盾}✗；\ \text{修正构造（}n_j\le\lfloor P/2\rfloor\ \text{不做 clip）后全部通过}✓✓$$
$$\qquad \text{与既有教训一致}：\textbf{结果异常先怀疑自己的实现}✓$$

## §6 边界与回查

- ⚠️ §2 的证明为**严格**（三行：覆盖引理 ＋ `\cos x\ge1-x^2/2` ＋ 窗口条件）✓
- ⚠️ §3 的推论**依赖** `m_M\le M-1` 这一外部输入（`M\ge12` 严格；`M\le11` 数值）✓ —— 已在档中标明
- ⚠️ §4 的数值为**抽样估计**（每格 300 配置 × 6 个 `\psi`）✓
- ⚠️ 本引理**不覆盖**最硬点（数值极小点的偏差 `\delta\approx0.07`–`0.32\ \text{rad}` 超出阈值）✓
- ⚠️ **不声称** `(RP_M)` 一般成立；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 17:4x）`[纪律]`（先跑后写）

```
技术词 近似周期单调性引理  命中文件数=0 ::  ⟹ 本档新增
技术词 偏差代价          命中文件数=0 ::  ⟹ 本档新增
技术词 阈值形式          命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓

---

## §8 【状态更新·C-176】`m_M\le M-1` 已严格化（本引理的推论现无条件）

$$⚠️\ §3\ \text{原写"}\ M\le11\ \text{为数值}"✗ \Longrightarrow \textbf{现已补证}（\text{`C-176`}）✓✓$$
$$\qquad \text{对}\ 2\le M\le11：\text{显式配置 ＋ 区间算术证书} \Longrightarrow m_M\le M-1\ \textbf{严格}（\text{余量}\ 0.5\text{–}7.8）✓$$
$$\qquad \text{配}\ M\ge12\ \text{的概率方法（本档同引用）} \Longrightarrow m_M\le M-1\ \textbf{对一切}\ M\ge2\ \textbf{严格}✓✓$$
$$\Longrightarrow \textbf{本引理的推论（单调性步）不再依赖数值输入}✓✓$$
$$\qquad （\text{唯一例外}\ M=1：m_1=\tfrac12>0=M-1，\text{与}\ \text{`C-171`}\ \text{一致}）✓$$
