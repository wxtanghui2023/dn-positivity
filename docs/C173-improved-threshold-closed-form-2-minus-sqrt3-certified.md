已查地图（**先查后写**）：`C-172`（近似周期单调性引理；阈值 `\sqrt{2/(9M)}`）、`C-159`（鸽笼定理）、`C-158`（`\kappa_N`）、`papers/rpM-window-cosines/OUTLINE.md`。关键词回查：`一维极小极大`=0、`闭式阈值`=0、`双约束相切`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 17:43「继续」）**：**放宽 `C-172` 的阈值。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{阈值从}\ \sqrt{2/(9M)}\ \text{改进到}\ \mathbf{0.732/\sqrt M}\（\textbf{改善}\ 1.553\times）✓✓$$
$$\qquad （\text{严格可认证的形式}：\varepsilon\le\sqrt{2\cdot0.2679/M}=\mathbf{0.73198/\sqrt M}✓）$$
$$\textbf{(二)}\ ⭐\ \textbf{精确阈值有闭式}：\lambda_{\max}:=2-\sqrt3=0.267949\ldots✓✓$$
$$\qquad \text{推导}：\text{两个约束同时相切（}m=1\ \text{与}\ m=2\text{）}：\cos\theta-\lambda=\cos2\theta-4\lambda=-1✓$$
$$\qquad\qquad \Longrightarrow 2(\lambda-1)^2=4\lambda\ \Longrightarrow\ \lambda^2-4\lambda+1=0\ \Longrightarrow\ \lambda=2-\sqrt3✓✓$$
$$\qquad \text{极值角}：\cos\theta=1-\sqrt3\approx-0.732 \Longrightarrow \theta\approx137.06^\circ✓$$
$$\textbf{(三)}\ \text{证书}：\text{1-D 自适应（区间＋保守）}\ \Longrightarrow\ \kappa_3(0.2679)\ge-1\ \text{（}\mathbf{59}\ \text{区间、}\mathbf 0\ \text{未决、余量}\ 5.2\times10^{-5}）✓✓$$
$$\textbf{(四)}\ ⚠️\ \text{仍不覆盖最硬点，但}\ \textbf{只差}\ 0.8\%：M=3\ \text{极小点的}\ \delta=0.426\ \text{rad}\ \text{vs 阈值}\ 0.4226\ \text{rad}✓$$

FREEZE-ACK: 本档即冻结期内的推导与认证（依 `§8.1`；不产候选结论）

D0: 本档对象 = **一维极小极大 `\kappa_N(\lambda)` ＋ 闭式 `\lambda_{\max}=2-\sqrt3` ＋ 1-D 证书 ＋ 改进引理** —— 关系 = 新引理与认证，非新机制
D1: 0

# C-173 · ⭐⭐ **改进阈值：闭式 `2-\sqrt3` 与 1-D 证书**

> **唐先生 2026-09-19 17:43**：继续（放宽阈值）✓

---

## §1 改进机制（本档核心）

$$\text{`C-172` 的粗界}：\text{取覆盖引理给出的}\ m\in\{1,2,3\}（\text{满足}\ \cos(m\theta)\ge0\text{）} \Longrightarrow \text{惩罚}\ \le\tfrac92M\varepsilon^2✓$$
$$\qquad \text{但它}\ \textbf{丢弃了} \text{“哪个}\ m\ \text{被选中”的信息}✗$$
$$\textbf{改进}：\text{对}\ m=1,2,3\ \textbf{逐个} \text{记账（每个}\ k=Pm\ \text{都可用！）}✓$$
$$\qquad \text{在}\ k=Pm：\text{旧点和}\ \ge M-\tfrac{M}2m^2\varepsilon^2；\ \text{新点项}=\cos(m\cdot P\psi)✓$$
$$\qquad \Longrightarrow \text{总和}\ \ge\ M+\Big[\cos(m\theta)-\lambda m^2\Big]，\ \lambda:=\tfrac{M\varepsilon^2}2，\ \theta:=P\psi✓$$
$$\qquad \Longrightarrow \max_{m\in\{1,2,3\}}\ \ge\ M+\kappa_3(\lambda),\qquad \kappa_N(\lambda):=\inf_{\theta}\max_{m\le N}\big[\cos(m\theta)-\lambda m^2\big]✓✓$$
$$\qquad （\text{引理}\ \text{`C-172`}\ \text{相当于用}\ \kappa_3(\lambda)\ge-9\lambda；\ \text{本档算}\ \textbf{精确值}）✓$$

## §2 ⭐ 一维极小极大与闭式阈值

$$\text{数值}：\kappa_3(0)=-1\ \text{hmm 无}；\ \kappa_3(0.25)=-0.968；\ \kappa_3(0.30)=-1.056 \Longrightarrow \lambda_{\max}\in(0.25,0.30)✓$$
$$\text{扫描＋二分}：\lambda_{\max}=0.26794952\ldots \Longrightarrow \textbf{恰好}\ 2-\sqrt3=0.26794919\ldots✓✓$$
$$\textbf{闭式推导（本档）}：\text{极值处两个约束同时相切（}m=1\ \text{与}\ m=2\text{）}：$$
$$\qquad \cos\theta-\lambda=\cos2\theta-4\lambda=-1\quad\Longrightarrow\quad \cos\theta=\lambda-1,\ \ \cos2\theta=4\lambda-1✓$$
$$\qquad \text{用}\ \cos2\theta=2\cos^2\theta-1：\ 2(\lambda-1)^2-1=4\lambda-1\ \Longrightarrow\ (\lambda-1)^2=2\lambda\ \Longrightarrow\ \lambda^2-4\lambda+1=0✓$$
$$\qquad \Longrightarrow\ \boxed{\lambda_{\max}=2-\sqrt3}\qquad(\text{另根}\ 2+\sqrt3\ \text{不合})✓✓$$
$$\qquad \text{极值角}：\cos\theta=1-\sqrt3\approx-0.73205 \Longrightarrow \theta=137.06^\circ✓$$

## §3 1-D 保守证书

$$\text{算法}：\text{对}\ [0,2\pi)\ \text{自适应细分}；\text{每区间取保守下界}\ \max_{m\le3}\big[\min_{[a,b]}\cos(m\cdot)-\lambda m^2\big]-\mathrm{SLACK}✓$$
$$\text{结果}：$$
$$\begin{array}{c|r|r|r}
\lambda & \text{区间数} & \text{未决} & \text{最小余量}\\\hline
0.2500 & 27 & 0 & 0.009049\\
0.2600 & 31 & 0 & 0.009068\\
0.2650 & 35 & 0 & 0.002346\\
0.2670 & 35 & 0 & 0.000346\\
\mathbf{0.2679} & \mathbf{59} & \mathbf 0 & \mathbf{5.2\times10^{-5}}\\
\end{array}✓✓$$
$$\Longrightarrow \kappa_3(\lambda)\ge-1\ \text{对}\ \lambda\le0.2679\ \text{已}\ \textbf{严格认证}✓✓\ （\text{证书极小：}\ 59\ \text{个区间，可人工审计}）✓$$

## §4 改进后的引理

$$\textbf{引理}\ (\text{改进版})：\text{设}\ \mathrm{dist}(P\varphi_j,2\pi\mathbb Z)\le\varepsilon\ \forall j，\ 3P\le5(M+1)，\ \lambda:=\tfrac{M\varepsilon^2}2\le0.2679✓$$
$$\qquad \text{则}\ \forall\psi：\quad \max_{1\le k\le5(M+1)}\Big[\sum_{j\le M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ M+\kappa_3(\lambda)\ \ge\ M-1✓✓$$
$$\qquad \Longrightarrow \text{配}\ m_M\le M-1 \Longrightarrow \textbf{单调性步成立}✓✓$$
$$\textbf{阈值对照}：$$
$$\begin{array}{c|c|c}
\text{来源} & \varepsilon\ \text{上界} & \text{改善}\\\hline
\text{`C-172`（粗界）} & \sqrt{2/(9M)}=0.4714/\sqrt M & —\\
\text{本档（}\lambda_{\max}=2-\sqrt3\text{）} & \sqrt{2(2-\sqrt3)}/\sqrt M=(\sqrt3-1)/\sqrt M=0.7321/\sqrt M & \mathbf{1.553\times}\\
\text{本档（可认证值}\ \lambda=0.2679\text{）} & 0.73198/\sqrt M & \mathbf{1.553\times}\\
\end{array}✓✓$$

## §5 ⚠️ 仍不覆盖最硬点（但只差 0.8%）

$$M=3：\text{极小点的最优近似周期}\ q^*=19,\ \delta=0.0678\ \text{（turn）}=0.426\ \text{rad}✓$$
$$\qquad \text{新阈值}：0.7321/\sqrt3=0.4226\ \text{rad}✓ \Longrightarrow 0.426>0.4226 \Longrightarrow \textbf{刚好差}\ 0.8\%✓$$
$$\Longrightarrow \text{下一步若把阈值再推}\ \sim1\%\ \text{即可覆盖}\ M=3\ \text{的最硬点}✓✓\ （\text{具体可行的两条}）$$
$$\qquad \text{①}\ \text{换}\ \kappa_5\ \text{路线（窗口}\ P\le M+1\ \text{更窄，但新点项}\ \ge\tfrac12\ \text{可用）}✓$$
$$\qquad \text{②}\ \text{把}\ \cos x\ge1-\tfrac{x^2}2\ \text{换成更精细的逐坐标估计（含}\ m=1\ \text{的优先）}✓$$

## §6 边界与回查

- ⚠️ §2 的闭式为**解析推导**（两约束相切 ⟹ 二次方程）✓；数值与之吻合到 7 位 ✓
- ⚠️ §3 的认证为**计算机辅助**（1-D，59 区间，保守 `\mathrm{SLACK}=10^{-12}`）✓
- ⚠️ §4 的引理**依赖** `m_M\le M-1`（`M\ge12` 严格；`M\le11` 数值）✓ —— 与 `C-172` 同一外部输入 ✓
- ⚠️ **不声称** `(\text{RP}_M)` 一般成立；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 17:5x）`[纪律]`（先跑后写）

```
技术词 一维极小极大  命中文件数=0 ::  ⟹ 本档新增
技术词 闭式阈值     命中文件数=0 ::  ⟹ 本档新增
技术词 双约束相切   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓

---

## §8 【更正·C-174】指针（**必读**）

**① §5 的「只差 0.8%」—— 已撤回 ✗**

那个 δ 取自 q*=19，但引理自身的准入条件是 3P ≤ 5(M+1)，即 P ≤ 6 ⟹ 该比较在不可准入的 P 上做的，无意义 ✓

**② §4 的阈值是在「充分条件 M + κ_3 ≥ M − 1」下得到的 —— 该充分条件过强 ✗**

真需求是 M + κ_3(λ) ≥ m_M（而 m_M ≈ 0.2M ≪ M − 1）⟹ 阈值放宽：

   可允许 λ 到 ~1.2（M=3 时），即 ε ≤ ~51°（而非 24°）✓✓

（κ_3 表的全圆实算见 C-174 §2；本档 §2 的 2 − √3 闭式仍成立，作为「≥ M − 1」级的临界值 ✓）

**③ 真正的限制项是「周期门槛」（C-174 §5），不是 ε 阈值 ✓**
