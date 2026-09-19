已查地图（**先查后写**）：`C-151`（M=2 极小点唯一／远场 0.5278／局部机制）、`C-150`（覆盖计数撤回；有限维联合不等式靶子）、`C-146`（网格＋Lipschitz 法）、`C-144`（Case A）、`E4-ENGINE-2`（引理 C＝M=1）。关键词回查：`梯度正张成`=0、`覆盖常数`=0、`局部引理闭合`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:51「继续」续刀）**：**把 `M=2` 证完**。
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{局部引理（严格，显式常数）}：\text{设}\ \varphi_1=\tfrac\pi3+\delta_1,\ \varphi_2=\tfrac\pi2+\delta_2,\ |\delta|\le\varepsilon：$$
$$\qquad \max_{k\in\{1,4,5,7,8\}}\Big[\cos k\varphi_1+\cos k\varphi_2\Big]\ \ge\ \tfrac12+c|\delta|-32|\delta|^2,\qquad c=2.0512✓✓$$
$$\qquad \Longrightarrow\ |\delta|\le\tfrac c{32}=3.6727^\circ\ \text{时}\ \ge\tfrac12✓✓$$
$$\textbf{(二)}\ ⭐\ \text{机制（极简）}：\text{五个}\ k\ \text{在}\ (60^\circ,90^\circ)\ \text{处}\ \textbf{都恰给}\ 0.5，\ \text{梯度}\ g_k\ \textbf{共同正张成}\ \mathbb R^2✓✓$$
$$\qquad 7g_5+5g_7=0\quad(\text{精确}：7(4.3301,-5)+5(-6.0622,7)=(0,0))✓✓$$
$$\qquad 0\in\mathrm{conv}\{g_1,g_4,g_5,g_7,g_8\}\ \text{（权重}\ \lambda=(0,0,\tfrac7{12},\tfrac5{12},0))✓✓$$
$$\textbf{(三)}\ ⭐\ \text{远场}（\text{`C-151`}）：|\delta|>1^\circ\ \text{时认证}\ g\ge0.5278>\tfrac12✓✓$$
$$\textbf{(四)}\ \boxed{1^\circ<3.6727^\circ\ \text{两区重叠} \Longrightarrow \textbf{`M=2` 证明闭合}✓✓✓}$$
$$\qquad \text{状态}：\textbf{计算机辅助}（\text{局部＝精确三角展开}；\text{远场＝网格＋Lipschitz}）✓✓$$

FREEZE-ACK: 本档即冻结期内的证明闭合（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=2` 的完整证明（局部引理＋远场认证＋重叠）** —— 关系 = 证明闭合，非新机制
D1: 0

# C-152 · ⭐⭐ **`M=2` 证明闭合**：局部引理（梯度正张成）＋ 远场认证

> **唐先生 2026-09-19 12:51**：**「继续」** ✓

---

## §1 目标

$$(\text{RP}_2)：\quad \min_{\varphi_1,\varphi_2\in[0,\pi]}\ \max_{k\le10}\Big[\cos k\varphi_1+\cos k\varphi_2\Big]\ \ge\ \tfrac12✓$$

## §2 ⭐ 局部引理（**严格**，显式常数）

$$\text{记}\ \varphi_1=\tfrac\pi3+\delta_1,\ \varphi_2=\tfrac\pi2+\delta_2,\quad F_k(\delta):=\cos k\varphi_1+\cos k\varphi_2✓$$
$$\text{关键：}\ k\in\{1,4,5,7,8\}\ \text{五个}\ k\ \text{满足}\ F_k(0)=\tfrac12✓✓$$
$$(\text{核验}：\cos60^\circ+\cos90^\circ;\ \cos240^\circ+\cos360^\circ;\ \cos300^\circ+\cos450^\circ;\ \cos420^\circ+\cos630^\circ;\ \cos480^\circ+\cos720^\circ\ \text{全}=0.5)✓$$
$$\text{梯度}（\text{本档实算}）：g_k:=\nabla F_k(0)=(-k\sin k\varphi_1,\ -k\sin k\varphi_2)✓$$
$$\begin{array}{c|r|r}
k & g_{k,1} & g_{k,2}\\\hline
1 & -0.8660 & -1.0000\\
4 & +3.4641 & 0.0000\\
5 & +4.3301 & -5.0000\\
7 & -6.0622 & +7.0000\\
8 & -6.9282 & 0.0000\\
\end{array}✓$$
$$\text{二阶余项}：\Big|F_k(\delta)-F_k(0)-\langle g_k,\delta\rangle\Big|\le\tfrac{k^2}2|\delta|^2\le32|\delta|^2\quad(k\le8)✓✓$$
$$\text{覆盖常数}（\text{实算，20 万向扫描}）：c:=\min_{|u|=1}\max_k\langle g_k,u\rangle=2.0512\ (\text{在}\ 53.69^\circ)✓✓$$
$$\Longrightarrow\ \boxed{\max_{k}\ \ge\ \tfrac12+c|\delta|-32|\delta|^2\ \ge\ \tfrac12\quad\text{当}\ |\delta|\le\tfrac c{32}=0.06410\ \mathrm{rad}=3.6727^\circ}✓✓$$
$$\textbf{关键结构}：7g_5+5g_7=0\ \textbf{精确成立} \Longrightarrow \text{两个梯度反向共线}；$$
$$\qquad 0\in\mathrm{conv}\{g_k\}\ \text{由五个向量共同保证}（\lambda=(0,0,\tfrac7{12},\tfrac5{12},0)\ \text{是一组解})✓✓$$

## §3 远场（沿用 `C-151`，实算）

$$\mathcal N_{1^\circ}^{\complement}\ \text{上：}\ \min g=0.548776,\quad \text{网格}\ 1500^2,\ \text{误差}\le0.02094 \Longrightarrow g\ge0.5278>\tfrac12✓✓$$

## §4 ⭐ 闭合

$$\text{局部：}|\delta|\le3.6727^\circ \Longrightarrow g\ge\tfrac12✓$$
$$\text{远场：}|\delta|>1^\circ \Longrightarrow g\ge0.5278>\tfrac12✓$$
$$\boxed{1^\circ<3.6727^\circ \Longrightarrow \text{两区重叠且覆盖全平面} \Longrightarrow (\text{RP}_2)\ \textbf{成立}}✓✓✓$$
$$\qquad \text{（交换对称}\ \varphi_1\leftrightarrow\varphi_2\ \text{自动覆盖}\ (90^\circ,60^\circ)\ \text{邻域}）✓$$

## §5 论文骨架（现已可用）

$$\begin{array}{c|l|l}
\text{条目} & \text{内容} & \text{状态}\\\hline
\text{引理 C} & M=1：(|z|=1\Rightarrow\exists k\le5:\ \mathrm{Re}\,z^k\ge\tfrac12) & \text{初等已证}\\
\text{定理 1} & M=2\ (\text{RP}_2) & \textbf{本档闭合}（\text{局部}＋\text{远场}）\\
\text{定理 2} & \text{Case A（任意}\ M：\text{近}\ \pi\mathbb Z\ \text{权}\ \ge\tfrac{2M}3+\tfrac13） & \text{已证}\\
\text{数值} & M\le11\ \text{对抗优化（}\min\max f=0.50,0.80,\dots,2.35） & \text{实算}\\
\text{开放} & M\ge3\ \text{一般情形；}2M\ \text{vs}\ x^{1/(M+1)}\ \text{尺度冲突} & \text{注册}\\
\end{array}✓✓$$

## §6 边界与回查

- ⚠️ §2 局部引理**严格**（三角恒等式＋显式余项界）；`c=2.0512` 为**数值扫描**（`20` 万方向），
  ⚠️ **正式版需精确重算**（LP／有理算术）⟹ 标 `[数值·可精确化]` ✓
- ⚠️ §3 远场为**计算机辅助**（网格＋Lipschitz），模浮点求值误差（可用定向舍入收紧）✓
- ⚠️ 若 `c` 重算后 `c/32` 不再 `>1^\circ`，则需更细网格缩小远场半径（无损：网格可任意细）✓
- ⚠️ **不声称** `M\ge3` 已证；**不声称** `(\text{RP}_M)` 一般成立 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:5x）`[纪律]`（先跑后写）

```
技术词 梯度正张成  命中文件数=0 ::  ⟹ 本档新增
技术词 覆盖常数    命中文件数=0 ::  ⟹ 本档新增
技术词 局部引理闭合  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
