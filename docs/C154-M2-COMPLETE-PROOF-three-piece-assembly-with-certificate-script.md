已查地图（**先查后写**）：`C-152`（局部引理＋远场）、`C-153`（`c` 精确值 `28\sqrt{1677}/559`；局部半径 `c/32`）、`C-151`（极小点唯一性／远场）、`C-150`（覆盖计数撤回）、`C-147`（反射归约）。关键词回查：`三段拼装`=0、`覆盖包含`=0、`可复现证书`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:15「继续完成严格化证明」）**：**把 `M=2` 的证明严格化到完整（含远场证书脚本）**。
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \boxed{(\text{RP}_2)\ \text{成立}：\forall\varphi_1,\varphi_2\in[0,\pi],\ \max_{1\le k\le10}\big[\cos k\varphi_1+\cos k\varphi_2\big]\ \ge\ \tfrac12}✓✓$$
$$\textbf{(二)}\ \text{证明＝}\textbf{三段拼装}：\text{(a) 局部（纯符号）}\ \cup\ \text{(b) 远场（可复现证书）}\ \cup\ \text{(c) 覆盖包含}✓✓$$
$$\qquad \text{(c) 是关键逻辑环}：\text{被排除方形（对角}\ 2.9133^\circ）\subset\ \text{局部盘（半径}\ 3.6727^\circ） \Longrightarrow \text{两情形覆盖全域}✓✓$$
$$\textbf{(三)}\ ⭐\ \text{证书稳健}：N=400/800/1500/2500\ \text{全部给出认证下界}\ 0.5239/0.5484/0.5666/0.5720\ >\ \tfrac12✓✓$$
$$\textbf{(四)}\ ⚠️\ \text{过程中抓到自己的实现 bug}：\text{交换点}\ (90^\circ,60^\circ)\ \text{的排除判据写错}（应为\ D_1-30）✓$$
$$\qquad \text{表现＝认证下界}\ 0.4827<0.5\ \text{异常} \Longrightarrow \textbf{先怀疑自己的实现}（\text{本会话第}\ 12\ \text{次应验}）✓✓$$

FREEZE-ACK: 本档即冻结期内的证明闭合与证书固化（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=2` 的完整证明（三段拼装）＋ 可复现证书脚本 ＋ 覆盖包含逻辑** —— 关系 = 证明闭合，非新机制
D1: 0

# C-154 · ⭐⭐ **`M=2` 完整严格证明（三段拼装）**

> **唐先生 2026-09-19 13:15**：**「继续完成严格化证明」** ✓

---

## §1 定理（两种形式）

$$\textbf{定理 (RP}_2)：\quad \forall\varphi_1,\varphi_2\in[0,\pi]:\quad \max_{1\le k\le10}\Big[\cos k\varphi_1+\cos k\varphi_2\Big]\ \ge\ \frac12✓✓$$
$$\text{等价形式}：\forall z_1,z_2\in\{|z|=1\},\ \exists k\in\{1,\dots,10\}:\ \mathrm{Re}\big(z_1^k+z_2^k\big)\ \ge\ \frac12✓✓$$
$$\text{（反射归约}\ \text{`C-147`}\ \text{§1}：\ \varphi_j=\arccos(\cos\theta_j)\in[0,\pi]，\ \text{故}\ [0,\pi]^2\ \text{为完整参数域）}✓$$

## §2 三段的精确内容

$$\textbf{(a) 局部（纯符号，}\text{`C-152`}\text{＋}\text{`C-153`}\text{）}：\ \text{取}\ (\varphi_1^*,\varphi_2^*)=(\tfrac\pi3,\tfrac\pi2)\ \text{或其交换}✓$$
$$\qquad k\in\{1,4,5,7,8\}：F_k(\varphi^*)=\tfrac12\ \textbf{精确}；\ \text{梯度}\ g_k\in\mathbb Q(\sqrt3)^2；$$
$$\qquad \text{覆盖常数}\ c=\tfrac{28\sqrt{1677}}{559}；\ \text{二阶余项}\ \le32|d|^2 \Longrightarrow \max_kF_k\ge\tfrac12+c|d|-32|d|^2✓$$
$$\qquad ⟹\ |d|\le\varepsilon:=\tfrac c{32}=\tfrac{7\sqrt{1677}}{4472}\ \mathrm{rad}=3.6726996^\circ\ \text{时}\ \ge\tfrac12✓✓$$
$$\textbf{(b) 远场（可复现证书，本档脚本）}：\ \text{排除两方形（半宽}\ 2.0600^\circ）后：$$
$$\qquad \min_{\text{grid}}g=0.587564804\quad(N=1500)；\quad \text{Lipschitz}\ L=10\sqrt2=14.1421356；$$
$$\qquad \text{单元余项}=L\,h\sqrt2/2=0.020943951；\ \text{求值误差}\le10^{-12}✓$$
$$\qquad ⟹\ \boxed{g\ \ge\ 0.566620853\ >\ \tfrac12}\quad(\text{认证})✓✓$$
$$\textbf{(c) 覆盖包含（本档）}：\text{排除方形对角}=2.0600^\circ\times\sqrt2=2.9133^\circ\ <\ 3.6727^\circ=\varepsilon✓✓$$
$$\qquad ⟹\ \text{方形}\subset\ \text{局部盘} \Longrightarrow \varphi\notin\text{盘}\Rightarrow\varphi\notin\text{方形}\Rightarrow\text{远场适用}✓✓$$

## §3 证明（拼装逻辑）

$$\text{任取}\ (\varphi_1,\varphi_2)\in[0,\pi]^2：$$
$$\qquad \text{若}\ \mathrm{dist}\big(\varphi,\{\varphi^*,\varphi^{*\text{swap}}\}\big)_\infty\le2.0600^\circ \Longrightarrow \text{在方形内} \Longrightarrow \text{在对角}\ 2.9133^\circ\ \text{内}$$
$$\qquad\qquad \Longrightarrow |d|\le2.9133^\circ<3.6727^\circ \Longrightarrow \text{(a)}\Longrightarrow \ge\tfrac12✓$$
$$\qquad \text{否则} \Longrightarrow \text{不在两方形内} \Longrightarrow \text{(b)}\Longrightarrow \ge0.5666>\tfrac12✓$$
$$\Longrightarrow \textbf{两种情形覆盖全参数域} \Longrightarrow \text{定理成立}✓✓\qquad\square$$

## §4 常数表与稳健性（实测）

$$\begin{array}{c|r|r|r}
N & \min_{\text{grid}}g & \text{单元余项} & \text{认证下界}\\\hline
400 & 0.602425894 & 0.078539816 & 0.523886077\\
800 & 0.587671462 & 0.039269908 & 0.548401554\\
1500 & 0.587564804 & 0.020943951 & 0.566620853\\
2500 & 0.584550894 & 0.012566371 & 0.571984523\\
\end{array}✓✓$$
$$\text{行}\ N=400\ \text{的对角}=3.1466^\circ<3.6727^\circ\ \text{仍成立} \Longrightarrow \text{证书对角度的稳健性 OK}✓$$

## §5 可复现性

$$\text{脚本}：\ \texttt{scripts/rp2\_far\_field\_certificate.py}\qquad \text{调用}：\ \texttt{python3 scripts/rp2\_far\_field\_certificate.py 1500 2.0}✓$$
$$\qquad \text{输出（逐字）}：\texttt{★ 认证下界 = 0.566620853 > 1/2 ? True}；\ \texttt{方形 ⊂ 局部盘 ? True}✓$$
$$\text{严格性来源三条}：\text{(i) Lipschitz 常数显式}；\text{(ii) 求值误差显式}（\le10^{-12}）；$$
$$\qquad \text{(iii) 排除取"与方形相交的单元"} \Longrightarrow \text{被认证区域}\subset\text{方形之外}（\text{单向安全}）✓✓$$

## §6 尖锐性（数值，待给证明）

$$\text{等号成立点}：(\pi/3,\pi/2)\ \text{及其交换}（\text{该处五项}\ k\ \text{同时达}\ \tfrac12）✓$$
$$\qquad \text{数值：}g\le0.5001\ \text{的网格点}=0 \Longrightarrow \text{除该两点外}\ g>\tfrac12\ \text{（\textbf{数值}，非本档结论}）✓$$

## §7 状态与下一步

$$\begin{array}{c|l|l}
\text{条目} & \text{内容} & \text{状态}\\\hline
\text{引理 C} & M=1 & \text{初等已证}\\
\textbf{定理 1} & \textbf{M=2} & \textbf{本档完整严格}✓✓\\
\text{定理 2} & \text{Case A（任意}\ M） & \text{已证}\\
\text{数值} & M\le11 & \text{实算}\\
\text{下一步} & \text{把同一模板用于}\ M=3\ (\text{局部梯度正张成}\ \mathbb R^3＋\text{远场证书}) & \text{待开}\\
\text{开放} & \text{任意}\ M & \text{注册}\\
\end{array}✓$$

## §8 边界与回查

- ⚠️ §2(b) 为**计算机辅助**（双精度＋显式误差界＋Lipschitz）；§5 给出脚本与逐字输出 ✓
- ⚠️ §6 为**数值**，不构成本档证明的一部分 ✓
- ⚠️ **不声称** `M\ge3`；**不声称** 一般 `M` ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**结果异常先怀疑实现**（本档抓到交换点排除 bug）✓

## §9 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:2x）`[纪律]`（先跑后写）

```
技术词 三段拼装   命中文件数=0 ::  ⟹ 本档新增
技术词 覆盖包含   命中文件数=0 ::  ⟹ 本档新增
技术词 可复现证书  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
