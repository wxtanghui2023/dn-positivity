已查地图（**先查后写**）：查 `C-190`（阻尼 M=3 执行清单）、`C-195`（m_3 封口）、`C-184`（0.35 证书）、`C-207`（等号集属 M_cand 而非 m_3）。回查见 §8 ✓

D0: 本档对象 = **甲 D-A′（收敛审计）**：把"active-set 不稳"改判为精确表述，并以高精度 KKT Newton 判定六分支近簇的真伪 —— 关系 = 阻尼 M=3 closure 的第一阶段
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 结论（先行）

$$\boxed{\text{D-A′：PASS —— near-active structure resolved}✓✓}$$
$$\qquad \text{阻尼 }M=3\ \text{的候选是}\ \textbf{六分支 nonsmooth 结构}\✓：\ A_{\rm near}=\{1,2,3,4,5,15\}✓,\ \lambda_{\min}>0✓,\ \text{六值精确并列}✓,\ \text{外部 gap}=0.2796✓$$
$$\qquad \textbf{几何型与 T13-A 明确不同}✓✓（\text{后者}：3\ \text{变量中の 4 分支}\{1,5,11,13\}✓；\text{本者}：5\ \text{变量中の 6 分支}✓ = 5+1\ \text{单纯形签名}✓）$$

## §1 ⚠️ 概念更正（唐先生 2026-09-20 14:57，全部采纳）

$$A_{\rm exact}(x)=\arg\max_k S_k(x)\quad\neq\quad A_{\rm tol}(x)=\{k:S_{\max}-S_k\le{\rm tol}\}\ \text{（近最大集）}✓✓$$
$$\Longrightarrow \text{正确判词不是"active-set instability"}✗，\text{而是}\ \boxed{\text{active-set \textbf{unresolved at current numerical accuracy}}}✓$$
$$\qquad \text{未排除的解释}：x_*\ \text{未收敛到真 nonsmooth minimizer}✓（\text{本轮已被证实}✓✓）$$
$$\qquad \text{另一纪律}：\textbf{不得预先}\ \lambda\ \text{残差定性为"float artifact"}✗（\text{须由 Newton 区分}✓）$$

## §2 ① x* 处完整 gap spectrum（dps=60）

| k | $S_k(x_*)$ | $\Delta_k=S_{\max}-S_k$ |
|---|---|---|
| 15 | 0.3730920540028223241229029 | $0$（exact argmax） |
| 1 | 0.3730920527732274835939751 | $1.22959\times10^{-9}$ |
| 3 | 0.3730920526771632375285973 | $1.32566\times10^{-9}$ |
| 5 | 0.3730920517755615472983341 | $2.22726\times10^{-9}$ |
| 2 | 0.3730920215625671325909458 | $3.24403\times10^{-8}$ |
| 4 | 0.373091260432339073247646 | $7.9357\times10^{-7}$ |
| **14** | 0.09349002541888471010325665 | $\mathbf{0.279602}$ ← 巨大跳跃 |
| 13 | −0.1882429907425941702937476 | 0.561335 |
| 12 | −0.4973069027983616938554963 | 0.870399 |
| 其余 | ≤ −0.80 | ≥ 1.17 |

$$\Longrightarrow \textbf{六分支近-active 簇}✓（\Delta\le7.94\times10^{-7}）＋\textbf{一个巨大外部 gap}✓（0.2796✓）$$
$$\qquad \text{尺度分离}\ \frac{0.2796}{7.94\times10^{-7}}\approx3.5\times10^5✓✓ ⟹ \textbf{结构高度集中}✓，\text{非"乱掉"}✗✓$$

## §3 ② 真 KKT feasibility（真解，非零齐次解）

$$G_A^{\rm T}\lambda=0,\quad \mathbf 1^{\rm T}\lambda=1,\quad \lambda\ge0✓（\text{用约束最小二乘，}\textbf{不用无约束 LS}✗\text{——后者给}\ \lambda=0\ \text{无信息}✓）$$
$$\qquad \text{在}\ x_*\ \text{处（六分支假设）}：\lambda_{\min}=0.1119>0✓，\text{但残差}\ 2.54\times10^{-7}✗ \Longrightarrow \text{KKT 未闭合}✓（\text{由 }x_*\ \text{未收敛所致}✓，\text{下节证实}✓）$$

## §4 ③ ⭐⭐ 11×11 KKT Newton（**不预设 tie**；解后独立复核）

$$\textbf{维度说明}✓：\text{阻尼 }M=3\ \text{的构型变量为}\ \mathbf 5\ \text{个}\ (r_2,r_3,\varphi_1,\varphi_2,\varphi_3)✓（r_1=1\ \text{归一化固定}✓）；\text{候选}\ r_2,r_3\ \text{皆内点}✓$$
$$\qquad \Longrightarrow \text{方程}\ 5_{\rm stationarity}+1_{\rm norm}+5_{\rm tie}=11✓,\ \text{未知量}\ 5+6\lambda=11✓ \Longrightarrow \textbf{11×11}✓$$
$$\qquad（\text{对照}：\text{无阻尼 T13-A}\ \text{只有}\ \varphi_1,\varphi_2,\varphi_3 ⟹ 3+1+3=7✓）$$

$$\textbf{Newton}：\text{it}=0\ \text{残差}\ 7.94\times10^{-7} \to \textbf{it}=3\ \text{收敛}✓✓，\text{残差}\ 1.90\times10^{-50}✓✓$$
$$\text{解}：x=(0.790513233950366238,\ 0.830207294814572930,\ 0.109110164828623089\pi,\ 0.820663709520206675\pi,\ 0.461719371018610243\pi)✓$$
$$\qquad \lambda=(0.1492699829,\ 0.2000536555,\ 0.1655100171,\ 0.1118601223,\ 0.1784876011,\ 0.1948186212)✓,\quad \lambda_{\min}=\mathbf{0.11186012}>0✓✓$$
$$\textbf{解处独立复核}（\text{不预设 tie}）：\text{六分支}\ S_k\ \text{精确并列到}\ \mathbf{1\times10^{-51}}✓✓（\Delta_k=7.8\times10^{-52}\!\sim\!4.2\times10^{-51}✓）；\text{外部最小}\ \Delta=0.279602✓$$
$$\qquad F(\text{解})=0.3730918928958164248599364✓ \Longrightarrow \text{落在 bracket}\ [0.3730918,\ 0.373092075762]✓ \text{内，且比 census 候选}\ (0.3730920540)\ \textbf{低}\ 1.6\times10^{-7}✓✓$$
$$\qquad \Longrightarrow \textbf{"census 候选未收敛"被证实}✓✓；\text{真凹点更低}✓，\text{其几何为【六分支精确并列}】✓✓$$
$$\qquad ⚠️\ \text{输出中 exact argmax}=[15]\ \text{是用【精确相等】判定的假象}✗（\text{六值实际相等至}\ 10^{-51}✓） \Longrightarrow \text{确为六路 tie}✓✓$$

## §5 $h$ 三档稳定性检查（唐先生指定）

$$h\in\{10^{-20},10^{-25},10^{-30}\}\ \text{三档 Newton} \Longrightarrow \text{三档解最大偏差}\ \le4.4\times10^{-58}✓✓（\text{前 5 变量}\ \le7.8\times10^{-62}✓）；\text{首步}\ dz\ \text{三档跨度}\ \le1.5\times10^{-47}✓$$
$$\Longrightarrow \textbf{中心差分 Jacobian 稳健}✓（\text{但最终认证仍需解析／区间 Jacobian}✓，\text{属 D-B}✓）$$
$$\qquad ⚠️\ \text{不把}\ h=10^{-25}\ \text{的"误差}\ 10^{-35}\text{"当无条件定量}✗（\text{中心差分误差含高阶导数尺度／条件数／相消}✓）$$

## §6 状态表（更新）

| 项目 | 状态 |
|---|---|
| candidate | ✓ |
| 与 bracket 一致 | ✓（$F_{\rm sol}$ 亦在 bracket 内 ✓） |
| low-end isolation | ✓ 数值证据（六分支簇 ~0.3731 vs 其它局部极小 ≳0.7529 ✓；间隔 ≈0.38 ✓） |
| **near-active 结构** | **✓ 已解析**（六分支 ＋ 1e-51 并列 ＋ 外部 gap 0.2796 ✓✓） |
| KKT $\lambda>0$ | ✓ 数值（60 dps，$\lambda_{\min}=0.1119$ ✓） |
| 与 T13-A 几何型 | **明确不同** ✓（5 变量 6 分支 vs 3 变量 4 分支 ✓） |
| **D-B Krawczyk** | **现可开** ✓（已有 KKT 验证的精确 active set，$\lambda>0$ ＋ 六路 tie ✓；待唐先生授权 ✓） |
| D-C 全局排除 | 暂不开 ✗ |

## §7 边界

$$\textbf{① 本档为}60\ \mathrm{dps}\ \text{数值＋中心差分 Jacobian}✓，\textbf{非区间认证}✗ \Longrightarrow \text{结论是"结构已解析"✓，不是定理}✗；$$
$$\qquad \textbf{② 不含}：\text{rigorous enclosure}✗、\text{局部刚性重算}✗、\text{全局排除}✗；\textbf{③ 不主张}：C_3\ \text{的精确值}✗、\text{全局唯一极小}✗；\textbf{④ 未用 RH}✓；\text{未改他档}✓$$
$$\qquad \textbf{⑤ 保留原有纪律}：\text{不得把近-active 集称为 exact active set}✗（\text{除非 KKT 闭合}✓ —— \text{本轮已闭合至}\ 10^{-50}✓）$$

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 收敛审计       命中文件数=1    ::  ./C225-DAp-convergence-audit-six-branch-structure-resolved.md
技术词 六分支近簇     命中文件数=1    ::  ./C225-DAp-convergence-audit-six-branch-structure-resolved.md
技术词 尺度分离       命中文件数=1    ::  ./C225-DAp-convergence-audit-six-branch-structure-resolved.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §9 下一步（待授权）

$$\text{若授权}：\textbf{D-B}：\text{对}\ 11\ \text{元系统（}5\ \text{变量}+6\lambda\text{）建 Krawczyk 严格盒}\ X_0✓ \Longrightarrow \text{存在性／唯一性分列}✓ \Longrightarrow \text{再} D\text{-}C\ \text{全局排除}✓$$
$$\qquad \text{纪律}：\text{先确认}\ X_0\ \text{的区间包含}✓；\lambda_{\min}>0\ \text{区间复核}✓；\text{六路 tie 的区间宽度}✓$$
