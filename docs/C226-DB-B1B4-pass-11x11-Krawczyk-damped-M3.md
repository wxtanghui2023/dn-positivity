已查地图（**先查后写**）：查 `C-225`（D-A′ 六分支解析）、`C-222`（无阻尼 7×7 Krawczyk 模板）、`C-190`（阻尼 M=3 执行清单）。回查见 §7 ✓

D0: 本档对象 = **甲 D-B：11×11 Krawczyk 严格认证（B1–B4 四门分列）** —— 关系 = 阻尼 M=3 closure 第二阶段
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 结论（先行）

$$\boxed{\text{D-B：B1–B4 四门【全部 PASS】✓✓✓}\quad（\text{B5 局部增长另算}✓，\text{属下一步}✓）}$$
$$\qquad \text{对象}：z=(r_2,r_3,\varphi_1,\varphi_2,\varphi_3,\lambda_1,\lambda_2,\lambda_3,\lambda_4,\lambda_5,\lambda_{15})\in\mathbb R^{11}✓,\ A=\{1,2,3,4,5,15\}✓$$
$$\qquad H(z)=\Big(\underbrace{\textstyle\sum_{k\in A}\lambda_k\nabla_zS_k}_{5},\ \underbrace{S_i-S_{15}\ (i=1..5)}_{5},\ \underbrace{\textstyle\sum\lambda_k-1}_{1}\Big)=0✓（11\ \text{方程／11 未知量}✓）$$

## §1 四门分列（**不合并成一个 PASS**✓，唐先生指定）

| Gate | 内容 | 判据 | 结果 |
|---|---|---|---|
| **B1** | Krawczyk existence | $K(X_0)\subset\mathrm{int}\,X_0$ | **True** ✓（$r_0\in\{10^{-4},\ldots,10^{-12}\}$ 五档全过 ✓） |
| **B2** | uniqueness | $\|I-YJ(X_0)\|_\infty<1$ | **0.019658**（$r_0{=}10^{-4}$）→ **$1.97\times10^{-10}$**（$r_0{=}10^{-12}$）✓✓ |
| **B3** | $\lambda$-positivity | $\min_{k\in A}\inf\lambda_k(X_0)>0$ | **0.11185924** ✓✓（六者全正 ✓） |
| **B4** | six-way tie | 唯一根满足 5 个 tie 方程 | **区间含 0** ✓✓（五条全含 ✓） |

$$\textbf{B4 的正确表述}✓✓（沿用 T13-A 纪律）\ \textbf{不得}写成"X_0\ \text{内六值恒等}"✗；\text{正确}：\text{Krawczyk 认证}\ X_0\ \text{内唯一根}\ z_0✓，\textbf{且该根满足六路 tie 方程}✓$$

## §2 采纳的严格盒（$r_0=10^{-4}$，最宽通过档）

$$\text{最大坐标宽}=3.93\times10^{-6}✓$$

| 变量 | 区间 | 宽 |
|---|---|---|
| $r_2$ | $[0.79051286581601794606,\ 0.79051360208471453086]$ | $7.36\times10^{-7}$ |
| $r_3$ | $[0.83020687425353775941,\ 0.83020771537560810112]$ | $8.41\times10^{-7}$ |
| $\varphi_1$ | $[0.34277956127726486534,\ 0.34277982323788260943]$ | $2.62\times10^{-7}$ |
| $\varphi_2$ | $[2.5781907738197263300,\ 2.5781913879731323768]$ | $6.14\times10^{-7}$ |
| $\varphi_3$ | $[1.4505338517301991052,\ 1.4505345162941329502]$ | $6.65\times10^{-7}$ |
| $\lambda_1$ | $[0.20005168968088671617,\ 0.20005562128030260806]$ | $3.93\times10^{-6}$ |
| $\lambda_2$ | $[0.17848638297740338887,\ 0.17848881919101464918]$ | $2.44\times10^{-6}$ |
| $\lambda_3$ | $[0.16550896682852119236,\ 0.16551106734873277347]$ | $2.10\times10^{-6}$ |
| $\lambda_4$ | $[0.19481755729550744787,\ 0.19481968515249192375]$ | $2.13\times10^{-6}$ |
| $\lambda_5$ | $[0.11185923586296582631,\ 0.11186100865610736203]$ | $1.77\times10^{-6}$ |
| $\lambda_{15}$ | $[0.14926898773262694292,\ 0.14927097799343916901]$ | $1.99\times10^{-6}$ |

## §3 B4 明细（盒上 tie 差的区间）

$$\boxed{\ S_1-S_2:\ [-7.563\times10^{-4},\ 7.563\times10^{-4}]✓;\quad S_1-S_3:\ [-9.148\times10^{-4},9.148\times10^{-4}]✓}$$
$$\qquad S_1-S_4:\ [-1.184\times10^{-3},\ 1.184\times10^{-3}]✓;\quad S_1-S_5:\ [-1.281\times10^{-3},1.281\times10^{-3}]✓$$
$$\qquad S_1-S_{15}:\ [-1.815\times10^{-3},\ 1.816\times10^{-3}]✓\ \Big（\text{全部含 0}✓；\text{宽度}\sim10^{-3}\ \text{与盒宽}\ 10^{-4}\ \text{相容}✓\Big)$$

## §4 实现要点（严格性来源）

$$\textbf{① 自建区间算术}：\texttt{Iv}\ \text{类，mpf 端点 ＋ 每步外扩}\ \mathrm{SLK}=10^{-45}✓（\mathrm{dps}=60✓）$$
$$\textbf{② 精确值域}：\cos/\sin\ \text{用临界点精确判定}✓（\text{奇/偶倍}\ \pi\ \text{枚举}＋\text{逐点}\ a\le t\le b✓）；\ r^k\ \text{用单调性}✓$$
$$\textbf{③ 11×11 Jacobian 解析装配}✓（\text{平稳行}=\sum\lambda_k\partial^2S_k✓；\text{tie 行}=g_0-g_i✓；\text{归一化行}=1✓）$$
$$\textbf{④ }Y\approx J(z_0)^{-1}（60\ \mathrm{dps}✓）；K(X)=m-YH(m)+(I-YJ(X))(X-m)✓$$

## §5 本档自我失误（第 41 次）

$$\textbf{41a ⭐ }\lambda\ \text{顺序错位}✗✗（\text{最有价值}）：\text{D-A′ 的}\ \lambda\ \text{按}\ A_6=[15,1,3,5,2,4]\ \text{给出}✓，\text{我按}\ [1,2,3,4,5,15]\ \text{装配}✗$$
$$\qquad \Longrightarrow \text{基点残差}\ \textbf{0.6065}✗（\text{应为}\ \sim10^{-12}✓），\text{且}\ \|YJ-I\|=10✗ \Longrightarrow \text{误判"结构有误"}✗ \Longrightarrow \text{重排后立即全过}✓✓$$
$$\qquad \textbf{教训}：\text{跨档传递}\ \lambda\ \text{这类"带索引的向量"必须【显式锁定索引顺序}】✓✓$$
$$\textbf{41b/41c 字典键名笔误两次}✗（\text{存}\ \texttt{nrm}/\texttt{lamlo}\ \text{而查}\ \texttt{B2}/\texttt{B3}✓） \Longrightarrow \text{已修}✓$$

## §6 状态表

| 项目 | 状态 |
|---|---|
| D-A′（六分支解析） | **PASS** ✓✓ |
| **D-B：B1 existence** | **PASS** ✓✓ |
| **D-B：B2 uniqueness** | **PASS** ✓✓（$1.97\times10^{-10}$） |
| **D-B：B3 $\lambda$-positivity** | **PASS** ✓✓（$0.11186$） |
| **D-B：B4 six-way tie** | **PASS** ✓✓ |
| **B5 local growth** | **未做** ✗（须【另算】$c_X,R,\rho_{\rm iso}$，5 维；**禁止移植** T13-A 的 $0.3193/169$✗） |
| D-C global exclusion | **仍封闭** ✗ |

## §7 边界

$$\textbf{① 本档为}60\ \mathrm{dps}\ \text{区间算术（自建}\ \texttt{Iv}＋\mathrm{SLK}=10^{-45}✓）\Longrightarrow \text{属【保守区间】级别}✓；\text{纯}\ \texttt{mpmath.iv}\ \text{版可后续加固}⚠️；$$
$$\textbf{② B1–B4 只证}：X_0\ \text{内}\ \exists!\ z_0\ \text{满足六路 nonsmooth KKT/tie 结构且}\ \lambda_k>0✓；\textbf{这不是局部极小性定理}✗（\text{须 B5}✓）；$$
$$\textbf{③ 不含}：\text{局部增长}✗、\text{全局排除}✗；\textbf{④ 不主张}：C_3\ \text{精确值}✗、\text{全局唯一极小}✗；\textbf{⑤ 未用 RH}✓；\text{未改他档}✓$$

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 四门分列     命中文件数=1    ::  ./C226-DB-B1B4-pass-11x11-Krawczyk-damped-M3.md
技术词 索引顺序锁定 命中文件数=1    ::  ./C226-DB-B1B4-pass-11x11-Krawczyk-damped-M3.md
技术词 六路并列     命中文件数=1    ::  ./C226-DB-B1B4-pass-11x11-Krawczyk-damped-M3.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §9 下一步

$$\textbf{B5（局部增长）}：\text{在 5 维变量}\ (r_2,r_3,\varphi_1,\varphi_2,\varphi_3)\ \text{上【重新计算】✓：}$$
$$\qquad \text{(i) active-set 隔离}\ \Delta_{\rm ref}✓（\text{六分支 vs 其余九支}✓，\text{外部 gap}\ 0.2796✓\ \text{极宽}✓）；\text{(ii) 一阶凸包}\ c_X✓（\text{facet 法＋containment}✓，5\ \text{维}✓）；$$
$$\qquad \text{(iii) 二阶余项}\ R=\max_{k\in A}\|\nabla^2S_k\|_2✓（\text{5×5 Hessian}✓）；\text{(iv) }\rho_{\rm iso}\ \text{与}\ \rho_{\rm up}\ \text{分离}✓；\text{(v) 边界裕量}\ c_X\rho-\tfrac R2\rho^2>0✓$$
$$\qquad \Longrightarrow \text{再由}\ \text{B4}\ \text{的"唯一根满足 tie"}\ \Longrightarrow\ \delta_A(z_0)=0✓ \Longrightarrow \text{局部严格极小}✓$$
