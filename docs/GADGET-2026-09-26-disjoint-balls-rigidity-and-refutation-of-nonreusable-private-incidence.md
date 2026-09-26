已查地图：已跑 scripts/prework_map_check.sh gadget 球不交 私有点复用 Z ⟹ 执行自 ZEROEX-2026-09-26 档；未跑 solver ✓。
D0: 本档对象 = gadget 刚性（球两两不交）的验证，及"不可复用私有点"lemma 的否证
D1: 1（新增：**gadget 球两两不交 ✓✓**；**"不可复用私有点"被完美码否证 ✗**；机制必须 E-相对 ✓）

# GADGET-2026-09-26

## §1 ✅ **断言 A（我方）：gadget 的球两两不交** ✓✓

```
$$\text{设 }x\notin C,\ t_x=0\ ✓,\ \text{唯一距离-1 码字 }c=x+e_\ell\ ✓,\ \text{匹配对 }\{i,j\}\mapsto c_{ij}=x+e_i+e_j\ ✓$$
$$\textbf{两两距离}: d(c,c_{ij})=|\{\ell\}\triangle\{i,j\}|=3\ ✓✓;\qquad d(c_{ij},c_{i'j'})=|\{i,j\}\triangle\{i',j'\}|=4\ ✓✓\ (\text{对不交}\ ✓)$$
$$\Longrightarrow\ \text{全部距离}\ \ge3\ \Longrightarrow\ \boxed{\text{gadget 的 }(n+1)/2\ \text{个闭合球\textbf{两两不交}}}\ ✓✓$$
$$\textbf{数值核验}: (5,7):\ \text{距离违反}=0,\ \text{球相交对}=0\ ✓;\qquad (7,\text{Hamming 16}):\ \text{距离违反}=0,\ \text{球相交对}=0\ ✓✓$$
$$\text{推论}: \text{一个 }Z\text{-球携 }(n+1)/2\ \text{个码字、其球共覆盖 }\frac{n+1}{2}(n+1)\ \text{点}\ ✓\ (\text{n=9}: 50\ ✓);\ \text{其中 }2m=4(n-1)\ \text{点在 }B_1(x)\ \text{外}\ ✓$$
$$

## §2 ⛔ **断言 B（唐先生）："不可复用私有点" —— 被否证** ✗✓

```
$$\text{数据}: (5,7):\ \text{私有点数}=24,\ \text{复用 max}=9,\ \textbf{avg}=4.5\ ✗;\qquad (7,\text{完美码}):\ \text{私有点}=128,\ \text{复用 max}=\textbf{avg}=28\ ✗✗$$
$$\text{完美码是最强反例}: E=0\Rightarrow b\equiv1\Rightarrow \text{全部 }112\ \text{个非码字都是 }Z\text{-球}\ ✓,\ \text{全部 }128\ \text{点都是私有点}\ ✓,\ \text{每个点被 }28\ \text{个 gadget 覆盖}\ ✗$$
$$\Longrightarrow\ \boxed{\text{私有点计数\textbf{无法}给 }Z\ \text{任何有效上界}}\ ✗✓\ (\text{任何 }cZ\le N_1\ \text{型论证都被完美码杀死}\ ✗)$$
$$

## §3 ⭐ 由此得到一条**对候选机制的硬约束**（本轮真正收获 ✓）

```
$$\text{完美码}: Z=112\ (\text{极大}\ ✓)\ \text{但 }E=0\Rightarrow Q_2=0\ ✓\ \Longrightarrow\ \text{结论\textbf{平凡成立}}\ ✓$$
$$\Longrightarrow\ \text{任何成功的机制必须}: \text{① 用 minimality}\ ✓;\ \text{② 用 }n\ \text{奇}\ ✓;\ \text{③ \textbf{内在地}用 }E>0\ ✓✓\ (\text{在 }E=0\ \text{处可退化}\ ✓)$$
$$\text{这排除的机制类}: \text{纯组合计数/私有点计数/球不交计数}\ ✗\ (\text{它们在完美码上全部失效}\ ✓)$$
$$\text{保留的机制类}: \text{以 }E\ \text{（即 excess）为\emph{本质}变量的传播机制}\ ✓\ ——\ \text{与我们已知的 "}Q_2\ \text{由 }E\ \text{定价"}\ ✓\ \text{一致}\ ✓$$
$$

## §4 状态与下一刀

```
$$\textbf{资产 ── 本轮}: \text{gadget 球不交刚性}\ ✓✓;\ \text{机制必须 }E\text{-本质的判据}\ ✓✓$$
$$\textbf{已淘汰}: \text{② 不可复用私有点}\ ✗;\ \text{（承前）}P,P_2,\text{三进制同余},\Delta\to A_{\le2},\text{shadow},\Phi\ \text{作路线},\text{ladder}/\sigma,\Psi_2/Z_2,\Psi_{\mathrm{mid}}(A)\ ✗$$
$$\textbf{桥}: \text{未打通}\ ✗\ (\text{仍需 }Z\le44\ \text{或等价的 }\Sigma\mathrm{OC}\ \text{下界}\ ✓);\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$\text{下一刀候选}: \text{① 以 }E\ \text{为本质变量的 gadget 外溢计数（每 }Z\text{-球的外部 }4(n-1)\ \text{点是否强制 excess}\ ✓);\ \text{② 用球不交 ⟹ 局部点密度上界 ⟹ 与 }E\ \text{挂钩}\ ✓;\ \text{③ 记录后暂停，转其它主桥入口}\ ✓$$
$$

## §5 边界（诚实标注）

- §1–§2 全部为**数值核验** ✓（n=5 全枚举 ✓、n=7 完美码精确构造 ✓）
- §2 的否证依赖**完美码反例** ✓ —— 该反例不含矛盾（其结论平凡成立 ✓），故否定的是**计数机制**而非桥本身 ✓
- §3 的"3 条硬约束"为**我方推论** ✓（非定理 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：gadget 球不交刚性、不可复用私有点、机制 E 本质判据、外溢计数
- **档案已有（引用，不列为提出）**：私有点、完美码、excess
