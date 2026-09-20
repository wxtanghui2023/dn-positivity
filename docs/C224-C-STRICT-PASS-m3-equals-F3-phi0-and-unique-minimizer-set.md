已查地图（**先查后写**）：查 `C-223`（诊断＋两 bug）、`C-222`（B：X0）、`C-221`（A：局部刚性）、`C-220`（闭合审计）。回查见 §8 ✓

D0: 本档对象 = **C-strict 严格通过** ＋ **A+B+C 三件拼接**（$\Rightarrow m_3=F_3(\varphi_0)$、极小构型集 $=S_3\varphi_0$）—— 关系 = T13-A 主命题闭合
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 结论（一句话）

$$\boxed{\ \forall\varphi\in[0,\pi]^3:\quad F_3(\varphi)\ \ge\ F_3(\varphi_0)\✓；\ \text{等号}\iff \varphi\in S_3\!\cdot\!\varphi_0\✓✓\ }$$
$$\Longrightarrow\ \boxed{\ m_3=F_3(\varphi_0)=\text{唯一根处的值}\✓；\qquad \mathcal M_3=S_3\!\cdot\!\varphi_0\ \text{（唯一到置换）}\✓✓\ }$$

## §1 C1：Threshold 严格合法

$$T_C:=\sup F_3(X_0)+10^{-9}=\mathbf{0.7640811017461542}✓\qquad（F_3(X_0)\ \text{区间上界}=0.7640811007461542✓）$$
$$\text{逻辑}：\text{B 给出唯一根}\ z_0\in X_0✓ \Longrightarrow F_3(\varphi_0)\le\sup F_3(X_0)<T_C✓ \Longrightarrow \forall\varphi\in\mathcal C:\ F_3(\varphi)\ge T_C>F_3(\varphi_0)✓✓$$

## §2 C2：六球严格处理 ＋ 覆盖无 gap 无 overlap

$$R_B=\rho_{\rm up}-10^{-6}=1.4648\times10^{-3}✓（\text{保留}\ 10^{-6}\ \text{缓冲层}✓）；\ \text{球心}=\text{六条}\ S_3\ \text{轨道}\✓；\text{再各加}\ X_0\ \text{半对角}✓ \Longrightarrow B(\varphi_0,R_B)\subseteq B(c,R_{Bg})✓$$
$$\text{覆盖}：[0,\pi]^3=\Big(\bigcup_{\sigma\in S_3}B_\sigma(R_B)\Big)\cup\mathcal C✓\qquad（\mathcal C=\text{终端认证箱之并}✓）$$
$$\textbf{精确有理体积核验}✓✓：\underbrace{\tfrac{57982058467}{57982058496}}_{\mathcal C}+\underbrace{\tfrac{29}{57982058496}}_{\text{丢弃箱}}=1\ \text{精确成立}✓ \Longrightarrow \text{无 gap}✓、\text{无 overlap}✓$$
$$\qquad（\text{丢弃箱}=\text{整箱位于球内}✓ \Longrightarrow \text{由}\ \textbf{A}\ \text{覆盖而非 B\&B}✓，\text{已在证书内显式登记}✓）$$

## §3 C3：C-strict 运行结果（与 float 分区【逐项一致】✓✓）

| 量 | 值 |
|---|---|
| 评估箱 | 66,564 ✓（float diagnostic 亦 66,564 ✓✓ 同一套分区决策 ✓） |
| 认证（终端） | 40,156 ✓ |
| 丢弃（球内） | 38 ✓ |
| 分裂 | 26,370 ✓ |
| **未决** | **0** ✓✓ |
| 认证最小余量 | $3.487296432291842\times10^{-6}>0$ ✓ |
| 最小余量箱 | $x\approx(0.8919\!\sim\!0.8932,\ 0.5964\!\sim\!0.5990,\ 0.1094\!\sim\!0.1120)$ ✓ |

$$\textbf{严格性来源}✓：\text{箱坐标}=\textbf{dyadic 精确有理}（Fraction）✓；\text{临界点}=\textbf{精确整数判定}✓（\lceil kx_{\rm lo}\rceil..\lfloor kx_{\rm hi}\rfloor\ \text{含奇/偶整数}✓）；\text{端点}\ \cos=\text{float}＋\textbf{保守 slack}\ \mathrm{SLK}=10^{-13}✓$$
$$\qquad \text{③ 硬上限}\ 2\times10^6\ \text{未触发}✓；\text{min-width 箱}\to\texttt{unresolved}\ \text{绝不静默丢弃}✓（\text{本次}\ 0✓）$$

## §4 ⭐⭐ 三件拼接（最终证明链）

$$\textbf{① }\mathcal C\ \text{上}：F_3\ge T_C>F_3(\varphi_0)✓（\S1\ +\ \S3✓）$$
$$\textbf{② 六个球内}：\text{A＋B 给出}\ 0<\|\delta\|\le\rho_{\rm up}\Longrightarrow F_3(\varphi_0+\delta)\ge F_3(\varphi_0)+c_X\|\delta\|-\tfrac{169}{2}\|\delta\|^2>F_3(\varphi_0)✓✓$$
$$\qquad（c_X=0.319306988✓，\rho_{\rm up}=1.4658\times10^{-3}✓，\text{边界裕量}\ 2.87\times10^{-4}>0✓）$$
$$\textbf{③ 覆盖}：[0,\pi]^3=(\cup_\sigma B_\sigma)\cup\mathcal C✓（\S2\ \text{精确体积}✓） \Longrightarrow \textbf{两处合并给出}\ \forall\varphi:\ F_3(\varphi)\ge F_3(\varphi_0)✓✓$$
$$\qquad \text{等号条件}：\text{球内仅}\ \delta=0✓；\mathcal C\ \text{上严格}>✓ \Longrightarrow \mathcal M_3=S_3\!\cdot\!\varphi_0✓✓$$

## §5 最终账本（T13-A）

| 阶段 | 状态 |
|---|---|
| A：局部增长证书（区间） | **PASS** ✓✓ |
| B：$7\times7$ Krawczyk（存在性＋唯一性分列） | **PASS** ✓✓ |
| C diagnostic（capped census） | **PASS** ✓✓ |
| **C strict interval certification** | **PASS** ✓✓✓ |
| $m_3=F_3(\varphi_0)$ | **已宣布** ✓✓ |
| 极小构型集 $=S_3\!\cdot\!\varphi_0$（唯一到置换） | **已宣布** ✓✓ |

$$\textbf{严格下界链}：0.76\le m_3\le0.76408110074585388514756267472105✓（\text{数值 bracket 由}\ C-219\ \text{与}\ C-212/213\ \text{给出}✓）$$
$$\qquad \text{而本档进一步【识别】了取到者}：\boxed{m_3=F_3(\varphi_0)}✓，\varphi_0=\text{Krawczyk 唯一根}✓✓$$

## §6 本档自我失误（第 40 次）

$$\textbf{40a 元组不可变}✗：箱行建为 tuple ⟹ \texttt{b1[j][1]=mid} 报 TypeError✗ \Longrightarrow \text{改 list}✓$$
$$\qquad（\text{提示}：\text{本档前的}\ C-223\ \text{两 bug（坐标维数、ceil/floor 奇偶判定）见}\ C-223\ \S2✓，\text{合计本轮实现错误}\ 3\ \text{个}✓）$$

## §7 边界（诚实标注）

$$\textbf{① 严格性层级}：\text{本题使用 float 端点}\cos＋\mathrm{SLK}=10^{-13}✓（\text{double 误差}\sim5\times10^{-15}✓，\text{保守}✓）；\text{临界点为精确整数判定}✓；$$
$$\qquad \text{体积核验为精确有理}✓✓ \Longrightarrow \text{属【保守浮点区间】级别}✓，\textbf{尚未做纯}\ \texttt{mpmath.iv}\ \text{版}⚠️（\text{可作后续加固}✓）$$
$$\textbf{② }T_C\ \text{依赖}\ F_3(X_0)\ \text{的浮点上界＋}10^{-9}✓，\text{其上界性由}\ \mathrm{SLK}\ \text{保守保证}✓$$
$$\textbf{③ 不主张}：m_3\ \text{的十进制精确值}✗（\text{仅给出严格 bracket}✓）；\text{未用 RH}✓；\text{未改他档}✓；\text{丙（其它全域工程）不开}✓$$

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 三件拼接     命中文件数=1    ::  ./C224-C-STRICT-PASS-m3-equals-F3-phi0-and-unique-minimizer-set.md
技术词 精确有理体积 命中文件数=1    ::  ./C224-C-STRICT-PASS-m3-equals-F3-phi0-and-unique-minimizer-set.md
技术词 极小构型集   命中文件数=1    ::  ./C224-C-STRICT-PASS-m3-equals-F3-phi0-and-unique-minimizer-set.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §9 下一步（可选加固，非阻塞）

$$\text{① 把 float+slack 端点升级为纯}\ \texttt{mpmath.iv}\ \text{端点}✓；\text{② }T_C\ \text{用纯区间上界}✓；\text{③ 合并入}\ \texttt{papers/rpM-window-cosines/main.md}✓（\text{本文档的}\ \S0\ \text{结论新增一章}✓）$$
