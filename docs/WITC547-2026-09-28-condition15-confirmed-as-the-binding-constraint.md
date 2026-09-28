# WITC547-2026-09-28 — **C-547：condition (15) 确认 ＝ 封住 Haas-2002/Plagne 族之\ \textbf{binding 约束}**

> **范围（照唐先生 2026-09-28 20:15 令 ✓）**：核验 ＋ 落档确认；**不作路线裁定** ✗。空间 B ✓

**已查地图**：接续 C-546（WITC546）✓

D0: 本档对象 ＝ **档案已有**（condition (15)／$2^{n-k}{\ge}(n{+}1)r{+}s$——**无新数学对象** ✓）
D1: 1（**首次确认 condition (15) 形式 ＝ C-546 所用约束（逐字一致）✓ ＋ 首次确认 $n{=}10$ 之族天花板\ \textbf{恰在 condition (15) 边界取得}（binding）✓✓**）
[R]

---

## §0 结论

$$\boxed{\text{condition (15)}\iff 2^{\,n-k}\ \ge\ (n+1)r+s}\qquad\text{（与 C-546 所用约束\ \textbf{完全一致}\ ✓）}$$
$$\boxed{\text{且它正是封住该族天花板之\ \textbf{binding 约束}}\ ✓✓}$$

## §1 形式核验（**唐先生之独立确认 ＋ 本档复算 ✓**）

$$\text{Plagne 2009 重构（逐字）}:\quad s\ \le\ 2^{\,n-k}-(n+1)r\quad\Longleftrightarrow\quad \boxed{2^{\,n-k}-(n+1)r-s\ \ge\ 0}$$

**作用**：保证 Haas Thm 2 证明中**隐藏剩余项为正**；且会排除某些数值上更优的 $(k,s)$ ✓

**$n{=}27$ 经典例（唐先生给出，本档复算 ✓）**：

$$2^{27-13}=16384,\quad (n{+}1)r=28\cdot585=16380,\quad \text{差}=4=s\ \Longrightarrow\ \textbf{边界饱和}\ ✓$$

## §2 $n{=}10$：**天花板恰在 condition (15) 边界取得**（本档核心 ✓）

| $k$ | $r$ | $s$ | 主项 | condition (15) 余量 |
|---|---|---|---|---|
| $\mathbf 2$ | $\mathbf{23}$ | $\mathbf 3$ | $\mathbf{94.40}$ | $\mathbf 0$ ← 饱和 |
| $1$ | $46$ | $6$ | $93.71$ | $0$ ← 饱和 |
| $3$ | $11$ | $7$ | $93.60$ | $0$ ← 饱和 |
| $6$ | $1$ | $5$ | $93.09$ | $0$ ← 饱和 |

$$\therefore\ \boxed{\max=k{=}2,r{=}23,s{=}3\ \text{且恰在 }s=2^{n-k}-(n+1)r\text{ 处}}\ ⟹\ \text{condition (15)\ \textbf{即} 天花板之来源}$$

$$\text{（C-546 脚本已令 }s=2^{n-k}-(n+1)r\text{，故其 }\max=94.4\ \text{与之自洽 ✓）}$$

## §3 结论（**无修订**）

$$\boxed{\text{C-546 之重建\ \textbf{无需修订}}\ ✓}\qquad(\text{condition (15) 与其所用约束逐字一致})$$
$$\text{附注}:\ \text{Haas 经验最优 }k{=}\lfloor(n{-}1)/2\rfloor{=}4\ \text{在 }n{=}10\ \text{反而不最优（仅 }91.08）\ ⟹\ \text{启发式在偶 }n\ \text{小维不可靠}\ ⚠️$$
$$\text{且 }n{=}10\ \text{之最优参数（}k{=}2,r{=}23,s{=}3\text{）\ \textbf{合法}（不触发 Haas 在 }n{=}27\ \text{遇到之"最优参数被禁"问题）}\ ✓$$

## §4 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "binding约束" "边界饱和" "参数合法性"
技术词 binding约束  命中文件数=0    ::
技术词 边界饱和     命中文件数=1    :: ./C130-shape-test-step2-of-six-concrete-flows-S1-S2-S3-classification.md
技术词 参数合法性   命中文件数=1    :: ./ERRATUM-LJCR-B1-semantics-skew-vs-general.md
```


**口径（空间隔离 ✓）**：`边界饱和` 命中 `C130-…`、`参数合法性` 命中 `ERRATUM-LJCR-B1-…` —— 二者皆**空间 A（RH 线）** 同名 ⟹ 标「**空间 A 同名，不计**」✗（不作新性证据，亦不作"已有"依据）✓

## §5 边界（硬 ✓）

- 有限参数穷举（$k\le10$）＋ 逐字引文核验 ✓；未上 SDP/SAT ✗；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- C-546 之机制族穷尽结论**不变**（本档仅确认其 binding 约束）✓
