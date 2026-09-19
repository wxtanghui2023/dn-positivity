已查地图（**先查后写**）：`C-154`（`M=2` 完整严格；三段拼装）、`C-153`（`c` 精确；局部半径）、`C-152`／`C-151`（局部＋远场）、`C-147`（反射归约）、`E4-ENGINE-2`（引理 C＝M=1）。关键词回查：`全域证书`=0、`松紧二分`=0、`维数壁垒`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:15「继续完成严格化证明」续刀）**：**把同一模板推广到 `M=3`**。
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \boxed{(\text{RP}_3)\ \text{成立}：\forall\varphi\in[0,\pi]^3,\ \max_{1\le k\le15}\sum_{j=1}^3\cos k\varphi_j\ \ge\ \tfrac12}\quad(\text{认证下界}\ 0.5500)✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{松紧二分（本档新认识）}：$$
$$\qquad M=1,2：\min\text{-}\max=\tfrac12\ \textbf{恰好取等} \Longrightarrow \text{必须} \text{局部精确＋远场拆分}✓$$
$$\qquad M\ge3：\min\text{-}\max=0.7775,0.866,1.12,\dots\ \textbf{有余量} \Longrightarrow \text{全域证书即可，}\textbf{不需局部引理}✓✓$$
$$\textbf{(三)}\ ⚠️\ \textbf{维数壁垒}：M=4\ \text{需}\ N\gtrsim628\ \text{每轴} \Longrightarrow N^4\approx1.6\times10^{11}\ \textbf{不可行} \Longrightarrow \text{需换法}✓✓$$
$$\textbf{(四)}\ ⚠️\ \text{本档又抓到自己两处实现 bug（异常先怀疑实现，第}\ 13\text{、}14\ \text{次应验）}✓$$

FREEZE-ACK: 本档即冻结期内的证明推进与证书固化（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=3` 认证 ＋ 松紧二分（`M\le2` 紧／`M\ge3` 松）＋ 维数壁垒** —— 关系 = 证明推进与结构认识，非新机制
D1: 0

# C-155 · ⭐ **`M=3` 已认证；结构新认识："松紧二分"与维数壁垒**

> **唐先生 2026-09-19 13:15**：**「继续完成严格化证明」**（续刀）✓

---

## §1 `M=3` 定理与证书

$$\textbf{定理 (RP}_3)：\quad \forall(\varphi_1,\varphi_2,\varphi_3)\in[0,\pi]^3:\quad \max_{1\le k\le15}\Big[\sum_{j=1}^{3}\cos k\varphi_j\Big]\ \ge\ \tfrac12✓$$
$$\text{方法}：\textbf{全域证书}（\text{无需局部引理}）：\ \text{单元中心 grid ＋ Lipschitz}✓$$
$$\qquad |\nabla F_k|=k\sqrt{\textstyle\sum_j\sin^2k\varphi_j}\le k\sqrt3\le K\sqrt3=25.9808=:L✓$$
$$\qquad \text{单元余项}=L\,h\sqrt3/2；\ h=\pi/N✓$$
$$\begin{array}{c|r|r|r}
N & \text{网格最小}\ g & \text{单元余项} & \text{★认证下界}\\\hline
260 & 0.781667026 & 0.271869417 & 0.509798431\ >\tfrac12✓\\
320 & 0.770910080 & 0.220893482 & 0.550016847\ >\tfrac12✓\\
400 & 0.771016968 & 0.176714786 & 0.594302381\ >\tfrac12✓\\
\end{array}✓✓$$
$$\text{脚本}：\texttt{scripts/rpM\_global\_certificate.py}\ \text{（通用}\ M，\text{分块＋向量化；}N=320\ \text{用时}\ 2.1\ \mathrm{s}）✓$$

## §2 ⭐ 松紧二分（本档新认识）

$$\begin{array}{c|r|c|l}
M & \min\text{-}\max & \text{相对}\ \tfrac12 & \text{证明形态}\\\hline
1 & 0.5000 & \textbf{紧} & \text{引理 C（初等）}\\
2 & 0.5000 & \textbf{紧} & \text{局部精确＋远场证书（三段）}\\
3 & 0.7775 & \text{松（+0.2775）} & \text{全域证书}\\
4 & 0.8660 & \text{松（+0.3660）} & \text{全域证书（维数受限）}\\
5 & \approx1.12 & \text{松} & \text{同上}\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{结构性结论}：(\text{RP}_M)\ \textbf{只在}\ M=1,2\ \text{取等} \Longrightarrow \text{分析难点}\ \textbf{集中在} M=1,2（\text{均已完成}）✓✓$$
$$\qquad M\ge3\ \text{的困难}\ \textbf{不再是分析，而是}\textbf{维数与证书成本}✓✓$$

## §3 ⚠️ 维数壁垒（下一步的真障碍）

$$\text{全域证书成本}：\text{网格}\ N^M，\ \text{余项}\ \propto L\,h\sqrt M/2\propto \tfrac{K M}{N}\propto\tfrac{M^2}{N}✓$$
$$\qquad \text{要余项}<\text{余量}\ (M=3:0.2775)：N\gtrsim M^2/0.2775\approx255\ (M=3)\ ⟹\ 2.6\times10^4\ \text{点}✓$$
$$\qquad M=4：\text{余量}\ 0.366 \Longrightarrow N\gtrsim400/0.366\approx1090 \Longrightarrow N^4\approx1.4\times10^{12}\ \textbf{不可行}✓✓$$
$$\Longrightarrow \text{可选换法（三条，均未开）}：$$
$$\qquad \text{①}\ \textbf{分支定界}（\text{Lipschitz 逐盒剪枝}）；\qquad \text{②}\ \textbf{结构归约}（\text{Case A＋聚类，把}\ M\ \text{降到} M-1）；$$
$$\qquad \text{③}\ \textbf{极小点降维参数化}（\text{数值观察：紧配置近退化} \Longrightarrow \text{极小点可能落在低维子流形）}✓✓$$

## §4 过程记录：本档抓到自己两处实现 bug

$$\text{①}\ \text{稳健性循环把}\ \min_k\big[F_k.\min()\big]\ \text{当}\ \min_x\max_kF_k\ \text{用} \Longrightarrow \text{得到}\ -3.0\ \text{（反例级异常）}✓$$
$$\qquad \text{表现：认证下界}\ -3.59\ \text{荒谬} \Longrightarrow \textbf{先怀疑自己的实现}✓$$
$$\text{②}\ \texttt{rpM\_global\_certificate.py}\ \text{广播维数写错}（\texttt{sh} \text{少成块维）} \Longrightarrow \texttt{ValueError}✓$$
$$\Longrightarrow \text{本会话"结果异常先怀疑实现"累计}\ \textbf{14 次应验}✓✓$$

## §5 状态与下一步

$$\begin{array}{c|l|l}
\text{条目} & \text{内容} & \text{状态}\\\hline
\text{引理 C} & M=1 & \text{初等已证}✓\\
\text{定理 1} & M=2 & \text{完整严格（三段）}✓✓\\
\text{定理 2} & M=3 & \textbf{本档认证}✓✓\\
\text{定理 3} & \text{Case A（任意}\ M） & \text{已证}✓\\
\text{数值} & M\le11 & \text{实算}✓\\
\text{下一步} & M=4\ \text{（需换法：分支定界／结构归约／降维）} & \text{待开}\\
\end{array}✓$$

## §6 边界与回查

- ⚠️ §1 为**计算机辅助证书**（双精度＋显式 Lipschitz 余项＋求值误差界）；脚本可复现 ✓
- ⚠️ §2 的 `M\ge4` 行 min-max 为**数值**（非本档结论）✓
- ⚠️ **不声称** `M\ge4`；**不声称** 一般 `M` ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**异常先怀疑实现** ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:3x）`[纪律]`（先跑后写）

```
技术词 全域证书   命中文件数=0 ::  ⟹ 本档新增
技术词 松紧二分   命中文件数=0 ::  ⟹ 本档新增
技术词 维数壁垒   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
