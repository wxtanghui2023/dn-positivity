# WITC545-2026-09-28 — **C-545：★Haas-2013 congruence 路线 = DEAD（奇偶门）**

> **范围（照唐先生 2026-09-28 20:13 令 ✓）**：落槌封口；**不作路线裁定** ✗。空间 B ✓
> **证据级别**：唐先生提供之 **2013 正文级引文（逐字）** ✓

**已查地图**：承 C-544（$H_k$ DEAD）／C-542（$Z{=}\varnothing$）／C-541（文献判定）✓

D0: 本档对象 ＝ **档案已有**（$\delta_i$／congruence／$K(n,1)$ 阶梯——**无新数学对象** ✓）
D1: 1（**首次以\ \textbf{正文级引文}判定 Haas 2013 congruence 路线在 $n{=}10$ 于\ \textbf{奇偶门}处 DEAD ✓✓ ＋ 首次确认 Theorem 4 常数为 $(p{-}2)p{-}1$ ✓ ＋ 首次确认 Theorem 5 偶 $n$ 退化为 $2^n/n$ ⟹ $103$ ✓**）
[R]

---

## §0 判定

$$\boxed{\text{C-545}:\ \text{Haas-2013 congruence route}\ =\ \textbf{DEAD at parity gate}}\ ✗$$

$$\begin{array}{c}
n=10\\
\Downarrow\\
n\ \text{even}\\
\Downarrow\\
\text{Theorem 3 hypothesis fails}\\
\Downarrow\\
\text{Theorem 3 congruence machinery unavailable}\\
\Downarrow\\
\boxed{\text{Haas 2013 congruence route DEAD}}
\end{array}$$

## §1 门检证据（**正文级逐字引文 ✓**）

$$\textbf{(E1) Theorem 3 条件（逐字 ✓）}:\ \text{"}1\le q\le n\ \text{and }\textbf{odd }n\text{. Assume }q\ \text{and }n{+}1\ \text{do not have a common odd prime divisor."}$$
$$\Longrightarrow\ n{=}10\ \text{为}\ \textbf{偶}\ \Longrightarrow\ \text{Theorem 3\ \textbf{不适用}}\ ✓$$

$$\textbf{(E2) Theorem 4 证明中之再确认（逐字 ✓）}:\ \text{"Moreover }n\ \text{is odd, since (10) cannot be satisfied for even }n\ \text{when }p\ge5\ \text{holds."}$$
$$\Longrightarrow\ \textbf{原文自陈}:\ \text{偶 }n\ (p{\ge}5)\ \text{下 Theorem 4 假设\ \textbf{根本不成立}}\ ✓$$

$$\textbf{(E3) Theorem 5 证明开头（逐字 ✓）}:\ \text{"Without loss of generality we may assume that }n\ \text{is odd, since for even }n\ \text{Theorem 5 easily follows from the bound }K(n,1)\ge2^n/n\ \text{due to Johnson and van Wee."}$$
$$\Longrightarrow\ \textbf{偶 }n\ \text{无绕过 Theorem 3 之版本};\ \text{作者直接退回旧型界}\ ✓$$

$$\textbf{(E4) Theorem 4 常数（正文确认 ✓）}:\ \boxed{\delta_{p-1}(x)\ge(p-2)p-1}\quad\text{（\textbf{非} }(p{-}2)^{p-1}\ ✗\text{）}$$

## §2 三个判断之校正（正文级 ✓）

$$\textbf{(1) }p{=}11\ \text{形式匹配不够}:\ 10\equiv-1\pmod{11}\ ✓\ \text{但 Theorem 3 另有独立假设 }n\ \text{odd};\ \text{不能代入}\ ✗$$
$$\textbf{(2) Theorem 4 更不需审}:\ \text{原文自陈偶 }n\ \text{下 }\delta_0{=}\cdots{=}\delta_{p-2}{=}0\ \text{不可能}\ ✓\ \text{——比我们 C-542 之 }Z{=}\varnothing\ \text{更早的\ \textbf{参数级阻塞}}\ ✓✓$$
$$\textbf{(3) Theorem 5 对 }n{=}10\ \text{不恢复新界}:\ \text{偶 }n\Rightarrow K(n,1)\ge\frac{2^n}{n}\Rightarrow K(10,1)\ge\frac{1024}{10}=102.4\Rightarrow\mathbf{103}\ \text{（旧层级，非 }119\text{）}\ ✓$$

## §3 结论

$$\boxed{\text{无需再做 Theorem 3}\to4\to5\ \text{之 }n{=}10\ \text{翻译}}\ ✓$$
$$\text{常数}(p{-}2)p{-}1\ \text{若日后记该定理本身则为 }(p{-}2)p{-}1;\ \text{对本问题($n{=}10$)\ \textbf{无作用}}\ ✗$$

## §4 下一目标（**换机制**）

$$\boxed{\text{Haas 2002}\ \textbf{condition (15)}\ \text{之 P1 门检}}$$
$$\text{与 2013 之 parity obstruction\ \textbf{不同机制}}\ ✓;\ \text{须查其在 }n{=}10\text{、目标 }K{\ge}119\ \text{时能否产生\ \textbf{超出 }103\ \text{之量}}\ ⚠️$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "奇偶门" "congruence路线封口" "参数级阻塞"
技术词 奇偶门     命中文件数=0    ::
技术词 congruence路线封口 命中文件数=0    ::
技术词 参数级阻塞  命中文件数=0    ::
```

## §6 边界（硬 ✓）

- 文献审计（正文级引文）＋ 已有档案引证 ✓；未上 SDP/SAT ✗；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- 本档**不主张** Haas 2002 亦将 DEAD；其为独立机制，待单独门检 ✓
