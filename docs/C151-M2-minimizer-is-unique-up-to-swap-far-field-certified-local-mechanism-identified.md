已查地图（**先查后写**）：`C-150`（覆盖计数撤回；`G_1\cap G_2=\varnothing`；M=2 有限覆盖路线）、`C-146`（网格＋Lipschitz 认证法）、`C-144`（Case A）、`C-147`（反射归约）。关键词回查：`远场认证`=0、`局部机制`=0、`极小点唯一性`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:51「继续」）**：**攻 `M=2` 的严格证明**。
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{极小点结构极干净}：\text{网格}\ 2000^2\ \text{上}\ g\le0.51\ \text{的点}\ \textbf{仅}\ 14\ \text{个}，\ \text{全部集中在}\ (60^\circ,90^\circ)\ \text{及其交换位置}✓✓$$
$$\qquad g\le0.55\ \text{的}\ 304\ \text{点}\ \textbf{仍全} \text{集中在同一点附近} \Longrightarrow \text{极小点集}\ \textbf{本质唯一}（\text{模交换}）✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{远场已认证（本档实算）}：\text{排除}\ 1^\circ\ \text{邻域后}\ \min g=0.5488，\ \text{网格误差}\le0.02094✓✓$$
$$\qquad \Longrightarrow \textbf{认证下界}\ =0.5278\ >\ \tfrac12✓✓（\text{半径}\ 2^\circ:0.566；4^\circ:0.627；6^\circ:0.630）✓✓$$
$$\textbf{(三)}\ ⭐\ \textbf{局部机制已定}：\text{在}\ (60^\circ,90^\circ)\ \text{处}\ k=4\ \text{与}\ k=8\ \text{都恰给}\ 0.5，\ \text{且}\ \partial_{\varphi_1}=\pm3.46,\mp6.93,\ \partial_{\varphi_2}=0✓✓$$
$$\qquad \Longrightarrow \textbf{局部证明模板}：\delta_1\ge0\ \text{用}\ k=4；\ \delta_1\le0\ \text{用}\ k=8 \Longrightarrow \text{两向覆盖}\ \varphi_1\ \text{方向}✓✓$$
$$\textbf{(四)}\ \text{状态}：M=2＝\textbf{远场已认证}（\text{严格，模浮点}）＋\textbf{局部有限覆盖}（\text{待做，机制已定}）✓$$

FREEZE-ACK: 本档即冻结期内的认证计算与局部机制定位（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=2` 极小点唯一性（模交换）＋ 远场认证下界 0.5278 ＋ 局部 `k=4`／`k=8` 机制** —— 关系 = 认证与定位，非新机制
D1: 0

# C-151 · **`M=2`：极小点唯一（模交换）、远场已认证、局部机制已定**

> **唐先生 2026-09-19 12:51**：**「继续」** ✓

---

## §1 ⭐ 极小点结构（决定证明结构）

$$\text{网格}\ 2000^2\ \text{上}：\min_{\text{grid}}g=0.5023（\text{网格间距效应}），\ \text{且}\ g<0.5\ \text{的点数}=0✓$$
$$\begin{array}{c|l}
\text{阈值} & \text{命中点}\\\hline
g\le0.5001 & 0\\
g\le0.5020 & 0\\
g\le0.5100 & 14\ \text{个，全部落在}\ (59.9^\circ\text{–}60.1^\circ,\ 89.9^\circ\text{–}90.2^\circ)\ \text{及其交换}\\
g\le0.5500 & 304\ \text{个，仍全部落在同一点附近}\\
\end{array}✓✓$$
$$\Longrightarrow \text{极小点集}\ \textbf{本质唯一}：\{(60^\circ,90^\circ),(90^\circ,60^\circ)\} \Longrightarrow \text{证明＝}\textbf{局部精确}＋\textbf{远场认证}✓✓$$

## §2 ⭐ 远场认证（本档实算）

$$\text{邻域}\ \mathcal N_r:=\{|x-60^\circ|\le r,\ |y-90^\circ|\le r\}\cup\{\text{交换}\};\quad \text{网格}\ 1500^2,\ \text{Lipschitz}\ L=\sqrt2 K=14.14✓$$
$$\text{误差}\le L\cdot h\sqrt2/2=\tfrac{14.14\times0.002094\times1.414}{2}=0.02094✓$$
$$\begin{array}{c|r|r|r}
r & \min_{\mathcal N_r^{\complement}}g & \text{认证下界} & >\tfrac12\\\hline
1^\circ & 0.548776 & 0.527832 & ✓\\
2^\circ & 0.586969 & 0.566025 & ✓\\
4^\circ & 0.648303 & 0.627359 & ✓\\
6^\circ & 0.651288 & 0.630344 & ✓\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{远场部分已完成}：\text{在}\ \mathcal N_{1^\circ}^{\complement}\ \text{上}\ g\ge0.5278>\tfrac12✓✓$$

## §3 ⭐ 局部机制（已定位）

$$\text{在}\ (\varphi_1,\varphi_2)=(\pi/3,\pi/2)：\text{五项}\ k=1,4,5,7,8\ \text{都恰给}\ 0.5✓$$
$$\begin{array}{c|r|r|r}
k & F_k(60^\circ,90^\circ) & \partial/\partial\varphi_1 & \partial/\partial\varphi_2\\\hline
4 & 0.500000 & +3.4641 & 0.0000\\
8 & 0.500000 & -6.9282 & 0.0000\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{局部模板}：\delta_1\ge0\ \text{用}\ k=4\ (\text{随}\ \varphi_1\ \text{增而增})；\ \delta_1\le0\ \text{用}\ k=8 \Longrightarrow \varphi_1\ \text{方向}\ \textbf{双向覆盖}✓✓$$
$$\qquad \delta_2\ \text{方向}：\text{一阶为零}\ (\partial_{\varphi_2}=0) \Longrightarrow \text{需二阶控制}：$$
$$\qquad\qquad \cos(4(\pi/2+\delta_2))=\cos(4\delta_2)\ge1-8\delta_2^2 \Longrightarrow F_4\ge0.5+0.866\sin(4\delta_1)-8\delta_2^2✓$$
$$\qquad ⟹ \text{还需}\ k=1,5,7\ \text{在"}\delta_2\ \text{主导"区域补上} \Longrightarrow \textbf{有限覆盖}（\text{待做}）✓$$

## §4 状态与下一步

$$\text{①}\ \textbf{远场}\ \mathcal N_{1^\circ}^{\complement}：\textbf{已认证}\ g\ge0.5278>\tfrac12✓✓$$
$$\text{②}\ \textbf{局部}\ \mathcal N_{1^\circ}：\text{机制已定}（k=4/k=8\ \text{控}\ \varphi_1；k=1,5,7\ \text{控}\ \delta_2），\ \text{需逐段写出}\ \Longrightarrow \text{有限覆盖，无新分析难点}✓$$
$$\text{③}\ \text{完成后}：M=2\ \text{成为}\ \textbf{第一个完整严格的小情形}（M=1\ \text{由引理 C}）✓✓$$
$$\text{④}\ \text{可复用模板}：\text{"局部精确＋远场认证"}\ \text{对每个固定}\ M\ \text{都可用} \Longrightarrow \text{论文可写}\ M=1,2\ \text{严格}＋M\le11\ \text{数值}✓✓$$

## §5 边界与回查

- ⚠️ §1／§2／§3 为**实际运行**（网格法；`L` 与误差公式显式；邻域显式）✓
- ⚠️ §2 的"已认证"为**计算机辅助**（网格＋Lipschitz），**模浮点求值误差**（可用定向舍入收紧）✓
- ⚠️ §3 的局部覆盖**未写完** ⟹ **不声称** `M=2` 已证 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:5x）`[纪律]`（先跑后写）

```
技术词 远场认证   命中文件数=0 ::  ⟹ 本档新增
技术词 局部机制   命中文件数=0 ::  ⟹ 本档新增
技术词 极小点唯一性 命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
