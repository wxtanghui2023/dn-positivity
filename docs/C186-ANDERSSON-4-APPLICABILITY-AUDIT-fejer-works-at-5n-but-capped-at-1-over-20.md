已查地图（**先查后写**）：`external_refs/RP-M-LITERATURE-POSITIONING.md`（§7-§10）、`C-181`（阻尼引理 1/2、Fejér 权路线 §3(a)）、`C-183`/`C-184`（甲、M=3 阻尼证书）、`E4-ENGINE-1`（Montgomery Lemma 2.2 转引）。关键词回查：`可套性审计`=0、`对角项衰减`=0、`机制封顶`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 21:09 指令）**：**甲 —— 读 Andersson [4]（arXiv:0704.1879）并做「可套性审计」**，六项：Fejér 权 → 原始不等式 → m 的实际范围 → n 依赖 → 相位/实部信息 → **m=5n 是否可落地** ✓
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{Fejér 机制}\ \textbf{可以降到}\ m=5n：\text{论文中}\ \textbf{没有任何一步} \text{需要}\ m\gg n✓✓$$
$$\qquad （\text{其定理对}\ \textbf{任意} \ m\ge n\ \text{成立；}m\sim n^2\ \text{只出现在}\ \textbf{模长版的应用}，\text{不出现在机制}）✓$$
$$\textbf{(二)}\ ⚠️\ \textbf{但在我们的设定下它的常数恰被封顶在}\ \approx\tfrac1{20}：\text{单位模情形推出}\ \max_{\nu\le5M}\Re S(\nu)\ge\frac{M+1}{20M}\to\tfrac1{20}✓✓$$
$$\qquad \Longrightarrow \textbf{这解释了 Montgomery 的 1/20 与窗口 5M 的来源}（\text{同一机制}）✓\ —— \text{要向}\ \tfrac12\ \text{推进必须}\ \textbf{换机制}✓✓$$
$$\textbf{(三)}\ ⚠️\ \textbf{阻尼情形}（|z_j|<1）\ \textbf{Fejér 机制失效}：\text{对角项} K(r_k^2,0)=1+2\sum(1-\tfrac{\nu}{m+1})r_k^{2\nu}<m+1✓$$
$$\qquad \text{数值证实：阻尼时}\ \text{Lemma 1}\ \textbf{不成立}✗（\text{单位模时成立}✓）⟹ \text{阻尼情形必须用别的手段}✓$$
$$\textbf{(四)}\ ⭐\ 按唐先生决策树：\textbf{"Fejér 可降到}\ 5n\ \Longrightarrow\ \textbf{进入实部/方向性强化"}✓✓\ —— \text{故}\ \text{乙}\ \textbf{不是孤立数值优化}✓$$

FREEZE-ACK: 本档即冻结期内的文献可套性审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **Andersson [4] 六项可套性审计 ＋ 单位模情形的严格重证（$\max_{ν≤5M}\Re S≥(M+1)/(20M)$，全 $M$）＋ 阻尼失效定位** —— 关系 = 审计与新证明，非新机制
D1: 0

# C-186 · Andersson [4] 可套性审计（六项）

---

## §1 六项审计表

$$\begin{array}{c|l|l}
\text{项} & \text{内容（逐字/推导）} & \text{判定}\\\hline
\text{① Fejér 权} & F_{m+1}(x)=\sum_{|\nu|\le m}\big(1-\tfrac{|\nu|}{m+1}\big)e(\nu x)=\tfrac1{m+1}\big(\tfrac{\sin\pi(m+1)x}{\sin\pi x}\big)^2\ \ge0 & \text{非负}\ \checkmark\\
\text{② 原始不等式} & \text{Lemma 1}：\sum_{\nu\le m}(1-\tfrac\nu{m+1})|g(\nu)|^2\ge\tfrac{(m+1)B-A^2}2 & \text{对角提取}\ \checkmark\\
\text{③ m 的实际范围} & \text{定理对}\ \textbf{任意}\ m\ \text{成立}（\text{仅需窗口}\ \ge n）；m\sim n^2\ \text{只在应用} & ⭐\textbf{无需}\ m\gg n\ \checkmark\\
\text{④ n 依赖} & A=\sum b_k,\ B=\sum b_k^2 & \text{线性}\ \checkmark\\
\text{⑤ 相位/实部信息} & §2\ \text{即}\ \textbf{单侧（实部）理论}：g^+=\max(g,0)；\text{定理给}\ \max g^+ & ⭐\textbf{有实部信息}\ \checkmark\\
\text{⑥ m=5n 可落地？} & \textbf{可以}（单位模情形，\text{见 §2}）——\text{但常数}\approx1/20 & ⚠️\text{可落地而封顶}\\
\end{array}✓$$

## §2 ⭐ 我方推导：单位模情形在窗口 5M 的严格下界（全 M）

$$\text{对称化}：\text{把}\ M\ \text{个点}\ \{z_k\}\ \text{扩为}\ 2M\ \text{个点}\ \{z_k,\bar z_k\}，\text{权}\ b=\tfrac12 \Longrightarrow g(\nu)=\Re S(\nu)✓$$
$$\qquad （\text{实值}\ ✓、\text{偶}\ ✓：g(-\nu)=\tfrac12\sum(z_k^{-\nu}+\bar z_k^{-\nu})=\tfrac12\sum(\bar z_k^{\nu}+z_k^{\nu})=g(\nu)✓）$$
$$\qquad A=g(0)=M,\qquad B=\sum b_k^2=\tfrac M2,\qquad |g(\nu)|\le\sum_k|z_k|^\nu\le M$$
$$\text{代入}\ [4]\ \text{Theorem 1}（|g(\nu)|\le M\Rightarrow\max_{\nu\le m}g^+\ge\tfrac{B(m+1)-AM-A^2}{2Mm}）\text{取}\ m=5M：$$
$$\qquad \max_{1\le\nu\le5M}\Re S(\nu)\ \ge\ \frac{\tfrac M2(5M+1)-\tfrac{M^2}{2}\cdot 2}{2\cdot M\cdot5M}\Big|_{\text{代入}A=M,B=M/2}=\frac{\tfrac M2(5M+1)-M^2-M^2}{10M^2}=\frac{M^2+M}{20M^2}=\boxed{\frac{M+1}{20M}}✓✓$$
$$\Longrightarrow \forall M\ge1,\ \forall|z_k|=1：\ \max_{1\le\nu\le5M}\Re\sum_k z_k^\nu\ \ge\ \frac{M+1}{20M}\ >\ \frac1{20}✓✓$$
$$\qquad \textbf{意义}：①\ \textbf{全 M 的严格下界}（\text{不再只靠转引}）✓；②\ \textbf{解释了 1/20 与窗口 5M 的来源}✓✓$$
$$\qquad \qquad ③\ \text{该路线}\ \textbf{给出 Montgomery Lemma 2.2 的单位模情形的自足重证}（\text{常数同 1/20，余量}\ \tfrac1{20M}）✓$$

## §3 ⚠️ 阻尼情形：Fejér 机制失效（对角项衰减）

$$\text{阻尼时配对核}：K(r,\varphi)=1+2\sum_{\nu\ge1}\big(1-\tfrac\nu{m+1}\big)r^\nu\cos(\nu\varphi)\ \ge0\ \text{仍成立}✓（\text{数值：}r\le1\ \text{全为正}✓）$$
$$\qquad \text{但}\ \textbf{对角项}：K(r_k^2,0)=1+2\sum\big(1-\tfrac\nu{m+1}\big)r_k^{2\nu}\ \color{red}{<}\ m+1\ \text{当}\ r_k<1✓$$
$$\qquad \Longrightarrow \sum_\nu\big(1-\tfrac\nu{m+1}\big)|g(\nu)|^2\ \ge\ \sum_k b_k^2K(r_k^2,0)\ \color{red}{<}\ B(m+1)✗$$
$$\text{数值证实}（\text{本次实算}）：
\begin{array}{c|c|c}
M & \text{单位模}\ \text{Lemma 1} & \text{阻尼}\ \text{Lemma 1}\\\hline
2,3,5,8,12,30,60 & \textbf{全部成立}✓ & \textbf{全部不成立}✗\\
\end{array}✓$$
$$\qquad \Longrightarrow \textbf{Fejér 机制本质上是"单位模专属"}✗\ —— \text{阻尼情形必须换手段}（\text{我方证书路线}✓）$$

## §4 数值对照（合规阻尼：max|z_j| = 1）

$$\text{随机}\ 3000\ \text{组/每 M}，\text{实测}\ \min\max_{\nu\le5M}\Re S(\nu)：$$
$$\begin{array}{c|r|r|r}
M & \text{实测最小值} & \tfrac1{20} & \text{我方定理（单位模}\ge\text{）}\\\hline
2 & 0.5214 & 0.05 & 0.075\\
3 & 0.6657 & 0.05 & 0.0667\\
5 & 0.7539 & 0.05 & 0.06\\
10 & 0.9594 & 0.05 & 0.055\\
20 & 0.9950 & 0.05 & 0.0525\\
\end{array}✓$$
$$\Longrightarrow \text{真值}\ \textbf{远高于}\ \tfrac1{20}（\text{且}\ M=2\ \text{处}\ 0.52\ge\tfrac12✓\ \text{与定理 1 一致}）✓$$

## §5 结论（按唐先生决策树）

$$\boxed{\text{Fejér 机制}\ \textbf{可降到}\ 5n（\text{项③⑤⑥}\ ✓）\ \text{但其常数封顶}\ \approx\tfrac1{20}\ \Longrightarrow\ \textbf{进入"实部/方向性强化"分支}✓✓}$$
$$\qquad \Longrightarrow \text{乙}（M=3\ \text{阻尼精确常数优化}）\ \textbf{不是孤立数值优化}✗\ —— \text{它是审计所指方向的自然延续}✓$$
$$\qquad \Longrightarrow \text{要把常数从}\ \tfrac1{20}\ \text{推到}\ \tfrac12\ \text{必须引入}\ \textbf{Fejér 之外} \text{的东西}（\text{= 我方证书/局部机制}）✓✓$$

## §6 边界

- ⚠️ §2 的推导**依赖** [4] §2 的 Lemma 1/Lemma 2/Theorem 1（外部逐字 ✓）——本档**未独立重证**该三件套 ✗（但已数值验证其在单位模情形成立 ✓）
- ⚠️ §3 的"失效"结论为**数值证实 ＋ 对角项结构分析**（非定理 ✗）
- ⚠️ §4 数值为随机抽样最小值（非全局极小 ✗）
- ⚠️ 本档**不声称**改进 [4] 或 Montgomery 的常数 ✓；**不声称** (RP_M) 对一般 M 成立 ✓
- **未用** RH；**未改**他档 ✓；**纪律**：**先跑后写** ✓（数值先于结论）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`）

```
技术词 可套性审计   命中文件数=0 ::  ⟹ 本档新增
技术词 对角项衰减   命中文件数=0 ::  ⟹ 本档新增
技术词 机制封顶    命中文件数=0 ::  ⟹ 本档新增
```
