# AUDIT-2026-09-28ah — **$Z^{(i)}$ 表\ \textbf{独立复算全对} ✓，但 pair 层\ \textbf{闭合于 }103$（含三处修正）**

> **性质**：**审计（独立复算）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 23:20 ✓
> **唐先生令**：正确 $Z^{(i)}$ 已算完；下一步只剩 rounding cone 消元；含止损判据 ✓

**已查地图**：接续 `AUDIT-ag`（Zhang $r{=}1$ 核验）／`AUDIT-af`（Haas 2008）✓

D0: 本档对象 ＝ **档案已有**（$A_j$／association scheme 交数——无新数学对象 ✓）
D1: 0（产出＝**全表独立复算 ＋ 三处修正 ＋ 一处闭合判定** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 唐先生 }Z^{(i)}\ (i{=}0..10)\ \text{全表\ \textbf{独立复算逐项一致}（暴力算交数}\ p^k_{ij}\text{）}}$$
$$\boxed{\text{② ✗ sanity 常数差 10 倍}:\ \text{应为}\ \mathbf{220}\binom{10}i\ \text{（非 }22\binom{10}i\text{）};\ \text{修正后结论\ \textbf{更强}}}$$
$$\boxed{\text{③ ★★ 全部 }11\ \text{条 induced 皆给同一界 }\mathbf{102.4\Rightarrow103} \Longrightarrow \textbf{pair 层闭合于 }103}$$
$$\boxed{\text{④ ✗ 无 rounding 空间（LHS mod }11\ \text{取遍全部余数）};\ ✗\ \S4\ \text{之}A_0{=}1{\Rightarrow}A_1{=}A_2{=}A_3{=}0\ \text{为假}}$$

## §1 ① $Z^{(i)}$ 表之独立复算（**✓✓ 全对**）

$$\text{方法}:\ \text{暴力枚举}\ p^k_{ij}=\#\{x:d(0,x){=}i,\ d(v,x){=}j\}\ (v\ \text{取重量 }k)\ \text{于}\ Q_{10};\ \text{再}\ Z^{(i)}_k=\sum_{j=0}^3\lambda_jp^k_{ij}$$
$$\textbf{结果}:\ \text{11 行\ \textbf{逐项与唐先生表一致}}（\text{例 }Z^{(1)}=(50,14,18,3,4,0,\ldots),\ Z^{(5)}=(0,0,56,21,90,30,90,21,56,0,0)\text{）}\ ✓✓$$

## §2 ② sanity 常数之修正（**✗✓，且修正后更强**）

$$\text{唐先生写}:\ \sum_kZ^{(i)}_k\binom{10}k=22\binom{10}i\quad\text{（数值例 }2200\ \text{与 }22\binom{10}1{=}220\ \textbf{自相矛盾}）\ ✗$$
$$\textbf{实测}:\ \sum_kZ^{(i)}_k\binom{10}k=\mathbf{220}\binom{10}i=\Bigl(\sum_j\lambda_j\binom{10}j\Bigr)\binom{10}i\qquad(\text{比例 }220\ \text{对\ \textbf{一切} }i\ \text{恒定})\ ✓✓$$
$$\therefore\ \text{任一 induced 之界}:\ M\ \ge\ \frac{22\binom{10}i\cdot2^{10}}{220\binom{10}i}=\frac{22\cdot1024}{220}=\mathbf{102.4}\ \Longrightarrow\ \boxed{103}\quad(\text{对\ \textbf{每个} }i\ \text{相同})\ ✓✓$$

## §3 ★★ ③ pair 层闭合判定（**本档核心 ✓✓**）

$$\textbf{实测（}i{=}0,\ldots,10\text{ 逐条）}:\quad M\ \ge\ 1024\cdot\tfrac{22\binom{10}i}{220\binom{10}i}=102.4000\ \Longrightarrow\ 103\quad\text{全部}\ \mathbf{11/11}\ ✓$$
$$\therefore\ \boxed{\text{induced ＋ 非负线性组合\ \textbf{不可能}把 }103\ \text{提到 }107}\qquad(\text{因比例恒为 }220\ \text{——\ 齐次缩放})✓✓$$
$$\text{此即唐先生 §2 之判断，现\ \textbf{已数值证实}};\ \text{故增益只可能来自\ \textbf{rounding（破坏齐次比例）}}$$

## §4 ④ rounding 空间之实测（**✗ 无空间**）

$$\text{检验}:\ L\ :=5A_0+5A_1+A_2+A_3\ \text{之}\ \mathrm{mod}\ 11\ \text{分布（120-code 全量}）$$
$$\qquad \{0{:}22,\ 1{:}167,\ 2{:}65,\ 3{:}202,\ 4{:}261,\ 5{:}141,\ 6{:}88,\ 7{:}48,\ 8{:}17,\ 9{:}9,\ 10{:}4\}$$
$$\therefore\ \boxed{\text{各余数皆出现} \Longrightarrow \textbf{无同余型 rounding 增益}} ✗$$
$$\text{另}:\ \text{唐先生 §4 断言}\ A_0{=}1\Rightarrow A_1{=}A_2{=}A_3{=}0:\ \textbf{实测违反 }\mathbf{120/120}\ ✗✗$$
$$\qquad(\text{样本 }u\in C:\ (A_0,A_1,A_2,A_3)=(1,0,5,18)\ ——\ u\in C\ \text{时 }A_2,A_3\ \text{可正}）$$

## §5 ★ 止损判定（**照唐先生 §7 判据 ✓✓**）

$$\text{唐先生判据逐字}:\ "\text{若在整数格＋非负组合锥中，所有候选 rounding 都满足全局比值 }\le106\text{，则此路线到不了 }107"$$
$$\textbf{本轮实测}:\ \text{① }11/11\ \text{条 induced 皆给 }103;\ \text{② 无同余 rounding 空间} \Longrightarrow \boxed{\textbf{PAIR 层路线闭合于 }103}\ ✓✓$$
$$\therefore\ \text{据判据，下一步应进入}\ \textbf{triple-covering}\ \text{／}\ \textbf{二阶局部约束}（\text{与文献走向一致}:\ \text{Zhang 1991 pair}\to\text{Zhang--Lo 1992 triple}）✓$$
$$\text{（与 }\texttt{AUDIT-af}\ \text{一致}:\ \text{excess 族止于 }103;\ \text{pair 族亦止于 }103;\ \text{故 }105/107\ \text{须更高阶或混合码机制）}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "induced表核验" "同余无增益" "pair层闭合"
技术词 induced表核验  命中文件数=0    ::
技术词 同余无增益     命中文件数=0    ::
技术词 pair层闭合     命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **独立暴力复算**（交数＋11 行＋余数分布＋$A_0$ 断言）＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** 公式 ✗；**不主张** $106$ 已排除 ✗（V290）
