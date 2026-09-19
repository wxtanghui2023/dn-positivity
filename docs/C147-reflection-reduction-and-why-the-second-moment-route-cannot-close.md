已查地图（**先查后写**）：`C-143`（二阶矩余量≈M 倍；更正 `ENGINE-5`）、`C-145`（M=2 压力测试：Q=7.75，余量 3.1×）、`C-146`（认证下界 1.70×）、`E4-ENGINE-4`（"M≤11 数值成立＋二阶矩路线可证"）、`E4-ENGINE-5`（RMS 路线与失效点）、`C-144`（Case A 已证）。关键词回查：`反射归约`=0、`负部控制`=0、`路线缺口`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:35「继续推导证明」）**
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{反射归约（本档，已证）}：\text{因}\ \cos\ \text{为偶}，\text{WLOG}\ f(k)=\sum_l w_l\cos(k\varphi_l),\ \varphi_l\in[0,\pi],\ w_l\in\mathbb Z_{\ge1},\ \sum_lw_l=M✓✓$$
$$\qquad \text{作用}：\textbf{消去}\ \theta_j\pm\theta_l\approx0\ \text{型（}\text{共轭对）奇性}；\ \text{剩余奇性仅}\ \varphi_l\approx\varphi_{l'}\ \text{与边界}\ \varphi_l\approx0,\pi✓✓$$
$$\textbf{(二)}\ \text{精确恒等式}：D_K(\varphi)=\frac{\cos\varphi-\cos((K+1)\varphi)}{4\sin^2(\varphi/2)}-\frac12 \Longrightarrow \Big|D_K(\varphi)+\tfrac12\Big|\le\frac{1}{2\sin^2(\varphi/2)}✓✓$$
$$\textbf{(三)}\ ⭐\ \textbf{负部链（本档，已证）}：\text{设假设}\ \forall k:\ f(k)<\tfrac12，\ S:=\sum_kf(k)。\text{则}$$
$$\qquad 0\le f<\tfrac12\Rightarrow f^2\le\tfrac f2;\qquad f<0\Rightarrow f^2\le M|f|;\qquad \sum_{f<0}|f|=\sum_{f\ge0}f-S\le\tfrac K2-S$$
$$\qquad \Longrightarrow\ \boxed{Q\ \le\ \Big(M+\tfrac12\Big)\tfrac K2\ -\ M\,S}✓✓$$
$$\textbf{(四)}\ ⚠️\ ⚠️\ \textbf{决定性结论}：\text{二阶矩路线}\ \textbf{不可能闭合}（\text{不是"余量不足"，是}\ \textbf{结构性}）✓✓$$
$$\qquad \text{需}\ Q_{\text{可证}}\ >\ \Big(M+\tfrac12\Big)\tfrac K2+c_\delta M^2；\ \text{而}\ Q\ \text{实际量级}\ \approx KM/4 \Longrightarrow \textbf{差}\ \approx2\times\ \text{起，含}\ c_\delta\ \text{项后达}\ 10\times✓✓$$

FREEZE-ACK: 本档即冻结期内的推导推进与路线否决（依 `§8.1`；不产候选结论）

D0: 本档对象 = **反射归约（已证）＋ 负部链（已证）＋ 二阶矩路线不可闭合的决定性结论** —— 关系 = 推导推进与路线否决，非新机制
D1: 0

# C-147 · **反射归约（已证）＋ 为什么二阶矩路线不可能闭合**

> **唐先生 2026-09-19 12:35**：**「继续推导证明」** ✓

---

## §1 ⭐ 反射归约（**本档，已严格证明**）

$$\text{因}\ \cos(k(2\pi-\theta))=\cos(k\theta)\ (\cos\ \textbf{为偶}):\ \text{把}\ \{\theta_j\}\ \text{按}\ \theta\sim-\theta\ (\mathrm{mod}\ 2\pi)\ \text{配对}✓$$
$$\qquad \theta\ \text{与}\ 2\pi-\theta\ \text{的两点合计贡献}\ 2\cos(k\theta)；\ \theta\in\{0,\pi\}\ \text{的点单独计}\ \pm1✓$$
$$\Longrightarrow\ \textbf{WLOG}：\ \boxed{f(k)=\sum_{l}w_l\cos(k\varphi_l),\quad \varphi_l\in[0,\pi],\ w_l\in\mathbb Z_{\ge1},\ \sum_lw_l=M}✓✓$$
$$\textbf{作用（为何值得做）}：\text{归约后交叉项的}\ \pm\text{-型奇性}\ (\theta_j+\theta_l\approx0)\ \textbf{消失}；\ \text{剩余奇性只有两类}：$$
$$\qquad \text{①簇奇性}\ \varphi_l\approx\varphi_{l'}\ (\Longrightarrow\text{合并})；\qquad \text{②边界}\ \varphi_l\approx0\ \text{或}\ \pi\ (\Longrightarrow\text{Case A，已证})✓✓$$

## §2 精确恒等式（用于负部链）

$$D_K(\varphi)=\sum_{k=1}^{K}\cos k\varphi=\frac{\cos\varphi-\cos\big((K+1)\varphi\big)}{4\sin^2(\varphi/2)}-\frac12✓$$
$$\Longrightarrow\ \Big|D_K(\varphi)+\frac12\Big|\le\frac1{2\sin^2(\varphi/2)} \Longrightarrow \text{非边界区}\ (\varphi\ge\delta):\ \Big|D_K(\varphi)+\frac12\Big|\le\frac1{2\sin^2(\delta/2)}=:c_\delta✓✓$$

## §3 ⭐ 负部链（**本档，已严格证明**）

$$\textbf{假设}\ \forall k\le K:\ f(k)<\tfrac12\ (\text{即结论不成立}),\quad S:=\sum_{k\le K}f(k)✓$$
$$\text{①}\ 0\le f<\tfrac12\Rightarrow f^2\le\tfrac f2;\qquad \text{②}\ f<0\Rightarrow f^2\le M\,|f|\ (\text{因}\ |f|\le M)✓$$
$$\text{③}\ \text{质量守恒}：\ \sum_{f\ge0}f-S=\sum_{f<0}|f| \Longrightarrow \sum_{f<0}|f|\le\tfrac K2-S\quad(\text{用}\ \sum_{f\ge0}f<\tfrac K2)✓$$
$$\Longrightarrow\ Q=\sum f^2\le\tfrac12\sum_{f\ge0}f+M\sum_{f<0}|f|\le\tfrac12\Big(S+\tfrac K2-S\Big)+M\Big(\tfrac K2-S\Big)$$
$$\Longrightarrow\ \boxed{Q\ \le\ \Big(M+\tfrac12\Big)\frac K2\ -\ M\,S}✓✓$$
$$\text{配合}\ S\ge-c_\delta M\ (\text{非边界区，}§2) \Longrightarrow\ Q\ \le\ \Big(M+\tfrac12\Big)\frac K2\ +\ c_\delta M^2✓✓$$

## §4 ⚠️ 决定性结论：**二阶矩路线不可能闭合**

$$\text{闭合条件}：\ \exists\ \text{可证下界}\ Q_{\text{可证}}\ >\ \Big(M+\tfrac12\Big)\frac K2+c_\delta M^2✓$$
$$\text{对照实测（本档实算，}\textbf{最坏配置}\ \text{处）：}$$

$$\begin{array}{c|r|r|r|r|r|r}
M & \min\max_k f & Q & S=\sum_k f & \#\{f<0\} & \sum_{f<0}|f| & \text{路线所需上界}\ \big(M+\tfrac12\big)K/2-MS\\\hline
2 & 0.5000 & 7.75 & -2.50 & 4 & 5.00 & 17.50\\
3 & 0.7992 & 17.32 & -2.71 & 6 & 8.09 & 34.39\\
5 & 1.1209 & 45.50 & -5.87 & 11 & 15.22 & 98.08\\
8 & 1.5916 & 117.88 & -4.75 & 15 & 30.37 & 208.00\\
11 & 2.3489 & 258.54 & -12.68 & 28 & 53.89 & 455.70\\
\end{array}✓$$
$$\Longrightarrow\ \text{要闭合，需}\ Q\ \textbf{同时} \text{大于上表最后一列与}\ c_\delta M^2\ \text{项；}$$
$$\qquad \text{而二阶矩的真实量级}\ \approx KM/4\ (\text{认证：}M=2\ \text{为}\ 1.70\times K/4)✓✓$$
$$\qquad \textbf{差}：\text{纯}\ M\ \text{项差}\ \approx2\times；\ \text{加入}\ c_\delta M^2\ (\delta\approx0.4\ \text{时}\ c_\delta\approx13)\ \text{后达}\ 10\times✓✓$$
$$\Longrightarrow\ \boxed{\text{二阶矩路线}\ \textbf{DEAD}（\text{结构性：单侧假设不控负部，控制负部的代价超过余量}）}✓✓$$

## §5 结论落到证明策略

$$\text{①}\ \text{原路线（}\text{`E4-ENGINE-4`}\ \text{"}M\le11\ \text{二阶矩路线可证"}\text{）}\ \textbf{须撤回}✓✓$$
$$\text{②}\ \text{证明必须}\ \textbf{直接以}\ \max\ \text{为目标}（\text{非矩量}）：\ \text{候选＝}\textbf{簇合并归纳}：$$
$$\qquad \text{归约后}\ \varphi_l\in[0,\pi]\ \text{带整数权}\ w_l；\ \text{若某簇近边界}\ (0,\pi)\ \text{且权}\ \ge\tfrac{2M}3+\tfrac13 \Longrightarrow \text{Case A}\ ✓$$
$$\qquad \text{否则}\ \text{簇}\ \delta\text{-分离} \Longrightarrow \text{每簇独立可用引理 C} \Longrightarrow \text{权最大的簇}\ \ge\frac Mr \Longrightarrow \text{其贡献}\ \ge\frac{M}{2r}✓✓$$
$$\qquad \text{剩余任务}：\text{控制其余簇的负贡献}\ (-\frac{M(r-1)}r)\ \text{需用}\ \text{簇间的}\ \textbf{相位关系}（\text{非计数}）✓$$

## §6 边界与回查

- ⚠️ §1／§2／§3 为**本档严格证明**（可逐行核）✓
- ⚠️ §4 数值为**实际运行**（`/tmp` 脚本；最坏配置用 Nelder–Mead ×15 起点，含结构化起点 `60^\circ`／`60^\circ`-`90^\circ` 交替／均匀）✓
- ⚠️ §4 的"路线 DEAD"是**对该路线（二阶矩／RMS 族）**的否决，**不是**对 `(RP_M)` 的否决 ✓
- ⚠️ §5 为**策略草案**（未证明）✓
- **未用** RH；**未改**任何原档（仅追加撤回指针）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:4x）`[纪律]`（先跑后写）

```
技术词 反射归约   命中文件数=0 ::  ⟹ 本档新增
技术词 负部控制   命中文件数=0 ::  ⟹ 本档新增
技术词 路线缺口   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
