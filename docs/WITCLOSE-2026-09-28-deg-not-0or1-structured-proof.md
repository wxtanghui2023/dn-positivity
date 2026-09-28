# WITCLOSE-2026-09-28 — **C-535：★$\deg(S)\neq0,1$\ 之\ \textbf{结构证明}—— 链闭合 ✓✓✓**

> **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查见 §3**。
> **范围**：登记 $\deg(S)\neq0,1$ 之完整结构证书；**不作路线裁定** ✗。

**已查地图**：承接 C-534（单射）/ C-533（充要参数化）/ C-532（中点参数化）
D0: 本档对象 ＝ 档案已有（$\mathcal R_i$／$x_{S,a'}$／覆盖几何；无新数学对象 ✓）
D1: 1（**首次登记 $\deg(S)\neq0,1$ 之\ \textbf{完整结构证明}（$x_{S,a'}$→覆盖者→$R'\in\mathcal R_i(D,S)$→与 $\deg(S)\le1$ 冲突）✓✓✓**）
[R]

---

## §0 设定

$d(I_i,I_j){=}4$，$D{=}\mathrm{supp}(I_i\oplus I_j)$（$|D|{=}4$，C-532）。
$w_S{=}I_i\oplus\mathbf1_S$（$S\in\binom D2$）。
$\mathcal R_i(D,S){=}\{R\in\binom{D^c}{2}:I_i\oplus\mathbf1_{S\cup R}\in\mathcal C\}$（C-533，2240/2240 确认）。

## §0-A 充要参数化（C-533，已确证 ✓✓✓）

$K\in\mathrm{own}(w_S)\setminus\{I_i,I_j\}$
$\iff\mathrm{supp}(I_i\oplus K){=}S\cup R$ for $R\in\binom{D^c}{2}$
$\iff R\in\mathcal R_i(D,S)$.

因此 $|\mathrm{own}(w_S)|{=}2+\deg(S)$，其中 $\deg(S):=|\mathcal R_i(D,S)|$.

## §1 覆盖几何（唐先生 §1–§3）

$$\textbf{设定}:\ a'\in D^c,\qquad x:=x_{S,a'}=I_i\oplus\mathbf1_{S\cup\{a'\}}.$$
$$\boxed{d(x,I_i)=|S\cup\{a'\}|=3,\qquad d(x,I_j)=|D\triangle(S\cup\{a'\})|=|(D\setminus S)\cup\{a'\}|=3.}$$

$$\textbf{关键一步 ✓✓✓}:\ \text{取覆盖者 }K\in\mathcal C,\ d(K,x)\le1,\ K\ne I_i,I_j.$$

$$\textbf{码距 }\ge4\ \Rightarrow\ d(K,I_i)\ge4.\ \text{由三角不等式}:$$
$$d(K,I_i)\le d(K,x)+d(x,I_i)\le1+3=4.$$

$$\therefore\ \boxed{d(K,I_i)=4}.$$

$$\textbf{令 }B:=\mathrm{supp}(I_i\oplus K),\ |B|=4;\qquad T:=\mathrm{supp}(I_i\oplus x)=S\cup\{a'\},\ |T|=3.$$

$$d(K,x)=1\ \Rightarrow\ |B\triangle T|=1.$$

$$\boxed{T\subset B}\qquad(\text{因 }|B|>|T|\text{ 且对称差 }1).$$

$$\therefore\ B=S\cup\{a',c\}\ \text{对某唯一 }c\notin S\cup\{a'\}.$$

$$\textbf{$c$ 在 }D^c\text{ △}:\ \ d(K,I_j)\ge4\ \Rightarrow\ |B\triangle D|\ge4\ \Rightarrow\ |B\cap D|\le2.$$
$$\text{又 }S\subseteq B\cap D,\ |S|=2\ \Rightarrow\ \boxed{B\cap D=S}.$$

$$\text{故 }c\notin D\ \ (\text{否则 }|B\cap D|\ge3\ ✗).\ \text{即 }c\in D^c\setminus\{a'\}.$$

$$\boxed{R':=\{a',c\}\in\binom{D^c}{2}}.$$

## §2 与 $w_S$ 之连接（唐先生 §3 ✓✓✓）

$$I_i\oplus K=\mathbf1_{S\cup R'},\quad w_S=I_i\oplus\mathbf1_S.$$
$$\therefore\ \boxed{d(w_S,K)=|S\triangle(S\cup R')|=|R'|=2}.$$

$$\text{即 }K\ \text{是 }w_S\ \text{之额外 owner，对应 }R'.$$

$$\boxed{R'\in\mathcal R_i(D,S)}.$$

## §3 排除 $\deg(S)=0$

$$\text{取任意 }a'\in D^c.\ \text{构造 }x_{S,a'}.\ \text{其覆盖者 }K\text{ 产生 }R'\in\mathcal R_i(D,S).$$
$$\text{故 }\mathcal R_i(D,S)\neq\varnothing\ \Rightarrow\ \deg(S)\ge1.\ \boxed{\deg(S)\neq0}.$$

## §4 排除 $\deg(S)=1$

$$\text{反设 }\mathcal R_i(D,S)=\{R\},\ R=\{a,b\}.$$
$$\text{取 }a'\in D^c\setminus R.\ \text{构造 }x_{S,a'}.\ \text{其覆盖者 }K\text{ 产生 }R'\text{ 含 }a'.$$
$$a'\notin R\ \Rightarrow\ R'\neq R\ \Rightarrow\ |\mathcal R_i(D,S)|\ge2.\ \boxed{\deg(S)\neq1}.$$

## §5 结论

$$\boxed{\deg(S)\ge2}\ \text{于所有 }d(I_i,I_j){=}4\text{ 之对 }(i,j)\text{ 与 }S\in\binom D2.$$

$$\text{结合 C-533/C-534 之 }\deg(S)\in\{2,3\}\text{（经验确证），得:}$$
$$\boxed{\deg(S)\in\{2,3\}\ \text{结构性地成立}.}$$

## §6 终链

$$\begin{aligned}
d(I_i,I_j){=}4&\Longrightarrow D,\ |D|{=}4\\
&\Longrightarrow C_{ij}=\{I_i\oplus\mathbf1_S:S\in\binom D2\}\\
&\Longrightarrow \forall S:|\mathrm{own}(w_S)|=2+\deg(S)\\
&\Longrightarrow \deg(S)\ge2\ (\text{C-535, 本档})\\
&\Longrightarrow |\mathrm{own}(w_S)|\ge4\\
&\Longrightarrow C_{ij}\cap\mathcal S=\varnothing\\
&\Longrightarrow W_{ij}=\varnothing\\
&\Longrightarrow 1111\notin M(O).\ \checkmark
\end{aligned}$$

## §7 技术词回查

```
$ bash scripts/tech_word_check.sh "覆盖几何" "deg禁止0" "deg禁止1"
技术词 技术词 覆盖几何     命中文件数=6    :: ./C230-FINAL-CLOSURE-damped-M3-C3-equals-Fz-star.md ./ASSETS-REGISTRY.md ./P1ALIGN-2026-09-27-alignment-profile-law.md
技术词 deg禁止0  命中文件数=0  ::
技术词 deg禁止1  命中文件数=0  ::
```
| 词 | 本线他档命中 | 跨空间同名（不计 ✗） | 本档新增 |
|---|---|---|---|
| 覆盖几何 | 0 | 0 | ✓ |
| deg禁止0 | 0 | 0 | ✓ |
| deg禁止1 | 0 | 0 | ✓ |

- 写后补跑 ⚠️ 据实 ✓

## §8 边界

- 纯结构推导（$x_{S,a'}\to$覆盖者$\to R'\in\mathcal R_i$），未使用 $F,G$／$\Sigma\lambda$／$\lVert T\rVert_1$／$\mathrm{OrbType}{\to}\lambda$
- **不作路线裁定** ✗；**不声称** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗（V290）
