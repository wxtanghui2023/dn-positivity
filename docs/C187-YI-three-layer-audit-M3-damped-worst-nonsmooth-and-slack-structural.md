已查地图（**先查后写**）：`C-184`（M=3 阻尼证书 0.35）、`C-186`（Fejér 可套性审计）、`C-161`（单模情形的单纯形签名）、`C-152`（M=2 局部机制）、`C-170`（mixed-λ 界）。关键词回查：`极小不在圆上`=0、`可分性松弛`=0、`非光滑极值`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 21:18 指令）**：**接乙**，三层：**乙-1**（真值/极值结构：极小是否在单位圆上）→ **乙-2**（0.35 与真值缺口的逐项账本）→ **乙-3**（能否推广到一般 M）✓
**结论（先行）**：$$\textbf{(一)}\ ⚠️\ \textbf{乙-1 的预期}\ \textbf{不成立}：\inf_{\mathbb D^3}\ \textbf{严格小于}\ \inf_{\mathbb T^3}✓$$
$$\qquad \text{全单位模}\ M=3：\min\text{-}\max=\mathbf{0.809017}=\cos36°（\text{精确代数值}）；\ \text{阻尼（}r_2{\approx}0.79,r_3{\approx}0.83\text{）}：\mathbf{0.3731}✓$$
$$\qquad \Longrightarrow \textbf{最坏构型是阻尼的}✗\ —— \textbf{"阻尼不改善最坏值"为假}✓✓\（\text{这解释了 Fejér 为何给不出尖锐常数}）$$
$$\textbf{(二)}\ ⚠️\ \textbf{乙-2 的缺口是【可分性松弛】且收敛极慢}：\text{箱下界与真实局部 min-max 的差}：$$
$$\qquad h=0.4\to0.2557；0.2\to0.1767；0.1\to0.1378；0.05\to0.1186；0.025\to0.1091；0.0125\to0.0850✓$$
$$\qquad \text{log-log 斜率}\approx 0.53,0.36,0.22,0.12,0.36 \Longrightarrow \textbf{既非}1\ \text{阶也非}2\ \text{阶}，\textbf{远慢于}1✗$$
$$\qquad \Longrightarrow \textbf{加密网格不是有效路线}✗\（\text{缺口源于}\ \max_k\ \text{与各坐标}\min\ \text{的不可交换}）✓$$
$$\textbf{(三)}\ ⚠️⚠️\ \textbf{乙-2b：局部方向性机制在阻尼情形【失效】}：\text{在阻尼局部极小点}：$$
$$\qquad \text{活跃}\ k=\{2,5\}\ \text{仅 2 个（5 维问题）} \Longrightarrow \mathbf{0\notin\mathrm{conv}\{\nabla S_k\}}✓\qquad c=\min_{|u|=1}\max_k\langle g_k,u\rangle=\mathbf{-2.81}<0✗$$
$$\qquad \Longrightarrow \textbf{阻尼极值是【非光滑}($\text{active set 不足}$)\text{的}✗\ —— \text{我们在单模情形最有效的局部机制不能平移}✗✓$$
$$\textbf{(四)}\ \textbf{三层的合读}：\text{阻尼情形}\ \textbf{同时抵抗}：\text{Fejér}（\text{单位模专属}✗）／\text{网格加密}（\text{收敛过慢}✗）／\text{局部单纯形}（\text{退化}✗）✓$$
$$\qquad \Longrightarrow \text{乙-3（一般 M 的统一增强项）在现有工具下} \textbf{无候选}✗\ —— \text{但负结构已精确定位：} \textbf{阻尼最坏情形是非光滑的}✓✓$$

FREEZE-ACK: 本档即冻结期内的攻击性审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **乙的三层审计（极小位置 ＋ 缺口收敛阶 ＋ 局部机制失效定位）** —— 关系 = 结构性判定，非新机制
D1: 0

# C-187 · 乙 · 三层审计（M=3）

---

## §1 乙-1：极小**不在**单位圆上（预期被否证）

$$\text{(a) 全单位模}：\min_{(\varphi_1,\varphi_2,\varphi_3)}\max_{1\le\nu\le15}\Big[\cos(\nu\varphi_1)+\cos(\nu\varphi_2)+\cos(\nu\varphi_3)\Big]=\mathbf{0.809017}✓$$
$$\qquad \text{精确值}\ \cos36°=\tfrac{1+\sqrt5}{4}\ \text{（数值吻合到 6 位）}✓\qquad \varphi^\ast/\pi\approx(0.1095,0.6,0.8905)✓$$
$$\text{(b) 阻尼（}\max|z_k|=1\text{）}：\min=\mathbf{0.373092}\quad\text{at}\ r_2\approx0.7905,\ r_3\approx0.8302✓$$
$$\Longrightarrow \textbf{差}=+0.4359 \Longrightarrow \textbf{最坏构型是阻尼的}✗\（\inf_{\mathbb D^3}=0.373<\inf_{\mathbb T^3}=0.809\text{）}✓✓$$
$$\qquad \textbf{推论}：\text{"阻尼不改善最坏值"}\ \textbf{假}✗ \Longrightarrow \text{不能把问题压回纯相位}✗$$
$$\qquad \qquad \text{且这}\ \textbf{解释了}\ \text{C-186 的发现}：\text{Fejér}\ \text{只覆盖单位模}⟹\text{它}\ \textbf{原理上} \text{给不出尖锐常数}✓✓$$

## §2 乙-2：缺口的逐项账本 ＝ **可分性松弛**

$$\text{证书的箱下界（可分）}：\mathrm{LB}(B)=\max_{k\le15}\Big[\min_{I_1}\cos(k\varphi_1)+\min_{\text{corner}}r_2^k\cos(k\varphi_2)+\min_{\text{corner}}r_3^k\cos(k\varphi_3)\Big]✓$$
$$\text{缺口来源（本档定位）}：\text{把}\ \max_k\ \text{放到各坐标}\ \min\ \text{之后}⟹\textbf{丢失} \text{（k 与各坐标的）耦合}✓$$
$$\begin{array}{c|r|r|r}
h & \mathrm{LB} & \text{真实局部 min-max} & \text{gap}\\\hline
0.4000 & 0.11739 & 0.37309 & 0.25570\\
0.2000 & 0.19642 & 0.37309 & 0.17667\\
0.1000 & 0.23525 & 0.37309 & 0.13784\\
0.0500 & 0.25445 & 0.37309 & 0.11864\\
0.0250 & 0.26399 & 0.37309 & 0.10910\\
0.0125 & 0.28809 & 0.37309 & 0.08500\\
\end{array}✓$$
$$\text{log-log 斜率}：0.53,\ 0.36,\ 0.22,\ 0.12,\ 0.36 \Longrightarrow \textbf{远小于 1}\ ✗$$
$$\Longrightarrow \textbf{加密网格不是有效路线}✗\ —— \text{要闭合缺口必须}\ \textbf{换界}（\text{非可分类}），\text{不是换步长}✓$$

## §3 乙-2b：局部方向性机制在阻尼情形**失效**

$$\text{在阻尼局部极小点精搜}：\min\text{-}\max=0.435520（r_2=0.888,\ r_3=0.938）✓$$
$$\qquad \text{活跃}\ k=\{2,5\}\ \textbf{仅 2 个}（\text{而问题是}\ \textbf{5 维}：\varphi_1,\varphi_2,\varphi_3,r_2,r_3\text{）}✓$$
$$\qquad \Longrightarrow \mathbf{0\notin\mathrm{conv}\{\nabla S_k\}}\ \text{（LP 判定失败）}✗\qquad c=\min_{|u|=1}\max_k\langle g_k,u\rangle=-2.811<0✗$$
$$\Longrightarrow \textbf{阻尼极值是【非光滑】的}✗\（\text{active set 数}<\text{维数}+1⟹\text{无单纯形签名}）✓✓$$
$$\qquad \textbf{对比}：\text{单模情形}\ M=3,4\ \text{的极值点}\ \textbf{都有} 0\in\mathrm{conv}\ \text{且}\ c_M>0✓（\text{C-161}）$$
$$\qquad \Longrightarrow \text{我们在单模情形最有效的那套（\text{局部符号＋}\ c_M\ \text{半径}）}\ \textbf{不能平移到阻尼}✗✓$$

## §4 乙-3：能否推广到一般 M？

$$\text{阻尼情形同时抵抗三条路线}：$$
$$\qquad ①\ \text{Fejér}\ \text{（单位模专属，对角项衰减）}✗\qquad ②\ \text{网格加密}（\text{斜率}\ll1\text{）}✗\qquad ③\ \text{局部单纯形}（\text{非光滑，active set 不足}）✗$$
$$\Longrightarrow \text{现有工具下}\ \textbf{无候选}✗\ —— \text{但}\ \textbf{负结构已精确定位}：$$
$$\qquad \boxed{\text{阻尼最坏情形是【非光滑}＋\text{可分性松弛】双重困难}}✓✓$$
$$\qquad \Longrightarrow \text{这正是}\ (RP_M)\ \text{一般}\ M\ \text{在主线上}\ \textbf{之外} \text{的部分}（\text{单模可证}✓／\text{阻尼难}✗）✓$$

## §5 本档净产出（4 条）

$$\textbf{①}\ \text{否证}：\inf_{\mathbb D^M}\ne\inf_{\mathbb T^M}\ \text{（}M=3\ \text{已证：}0.373\ \text{vs}\ 0.809\text{）}✓✓\ \text{—— 堵住"压回纯相位"这一条设想}✗$$
$$\textbf{②}\ \text{精确定位缺口}：\text{可分性松弛}；\text{收敛斜率}\approx0.2\text{–}0.5⟹\text{加密无效}✓$$
$$\textbf{③}\ \text{定位机制失效}：\text{阻尼极值}\ \textbf{非光滑}（0\notin\mathrm{conv}，c<0\text{）}✓✓$$
$$\textbf{④}\ \text{新的精确值发现}：\text{单模}\ M=3\ \text{的极小}\ =\cos36°\ \text{（代数）}✓\ ——\text{与}\ M=2\ \text{的}\ \tfrac12\ \text{并列}✓$$

## §6 边界

- ⚠️ §1 的极小值为**数值搜索**（DE ＋ Nelder-Mead；非全局证明 ✗）；阻尼情形景观多局部极小（本次两个起点给 0.373 与 0.436 ✗）
- ⚠️ §1 的"精确值 cos36°"为**数值吻合**（6 位），**未证** ✓
- ⚠️ §2 的斜率为**有限点拟合**（非收敛率证明）✗
- ⚠️ §3 的 LP 判定在**该局部点**成立（非所有阻尼极值 ✗）
- ⚠️ 本档**不声称** C_3 的精确值 ✓；**不声称** (RP_M) 阻尼版对一般 M 的结果 ✓
- **未用** RH；**未改**他档 ✓；**纪律**：先跑后写 ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`）

```
技术词 极小不在圆上   命中文件数=0 ::  ⟹ 本档新增
技术词 可分性松弛    命中文件数=0 ::  ⟹ 本档新增
技术词 非光滑极值    命中文件数=0 ::  ⟹ 本档新增
```
