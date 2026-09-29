# AUDIT-2026-09-29u — **★ 恒等式差因子 $2$；$(1)$ \textbf{再次为假}（同 $\texttt{29j}$ 之 $(F)$）；但浮出一条\ \textbf{精确 supply 恒等式}**

> **性质**：**实测核验 ＋ 纠错 ＋ 新恒等式**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 12:2x ✓
> **唐先生令**：excess 一阶质量 × 二阶相遇数 之耦合（$T_2$）✓

**已查地图**：★**命中既有档** —— `AUDIT-29j/29k`（**同一条 $(1)$ 已被否证**：49/120 违例）✓

D0: 本档对象 ＝ **档案已有**（$\mu$／$\delta$／$T_2$／$m(y)$——无新数学对象 ✓）
D1: 0（产出＝**一处因子纠错 ＋ 一处重复否证 ＋ 一条精确恒等式** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ }\star\ \text{差因子 }2:\ \textbf{正解}\ E+T_2=M(A_1+A_2),\ \text{非 }2M(A_1+A_2)}$$
$$\boxed{\text{② ✗✗ }(1)\ d_2(c)+q(c)\le9d_1(c)\ \textbf{为假}:\ \textbf{49/120 违例};\ \text{典型}\ d_1{=}0\Rightarrow 0<d_2{+}q✗}$$
$$\boxed{\text{③ ⟹ 由此推出之 }A_2\le12\ \textbf{不成立}}✗$$
$$\boxed{\text{④ ✓✓ 但得一条\ \textbf{精确恒等式}}:\ \sum_{y\in S_2(c)}m(y)=9d_1(c)\ \text{且}\ \#\{m{=}2\}=\tbinom{d_1(c)}2\ (\textbf{与 }d_2\ \textbf{无关})}$$

## §1 ① $\star$ 之因子纠错（**✓✓ 实测完全吻合**）

$$\text{120-code}:\ E=296,\ T_2=\sum_x\tbinom{\delta(x)}2=102,\ \Sigma_x\tbinom{\mu(x)}2=398=E+T_2\ ✓$$
$$A_1=\tfrac{2E_1}M=0.8333,\ A_2=\tfrac{2E_2}M=2.4833\ (E_1{=}50,E_2{=}149,M{=}120)$$
$$\text{你的形式}\ 2M(A_1+A_2)=\mathbf{796}\ \ne\ 398\ ✗✗;\qquad \textbf{正确形式}\ M(A_1+A_2)=\mathbf{398}=E+T_2\ ✓✓$$
$$\therefore\ \boxed{\text{正确之 }\star:\quad T_2=106(A_1+A_2)-142\quad(\text{非 }212(\cdot)-142)}$$

## §2 ② $(1)$ 之否证（**✗✗ 实测 49/120**）

$$\text{结构原因}:\ d_1(c)=0\ \text{时右端}=0,\ \text{而 }d_2(c)\ \text{可为 }1..5\ \text{（实测样本）}\Longrightarrow 0<d_2+q\ ✗$$

| $d_1$ | $d_2$ | $q$ | $9d_1$ | $d_2+q$ | 判定 |
|---|---|---|---|---|---|
| $0$ | $5$ | $0$ | $0$ | $5$ | ✗ |
| $0$ | $2$ | $0$ | $0$ | $2$ | ✗ |
| $0$ | $4$ | $0$ | $0$ | $4$ | ✗ |

$$\therefore\ \text{由 }(1)\ \text{推得之}\ 106A_2+Q\le9D_C\ \text{及其下游 }A_2\le12\ \textbf{全部失效}✗$$
$$\text{（⚠️ 本条与 }\texttt{AUDIT-29j}\ \text{之 }(F)\ \text{为\ \textbf{同一断言};\ 当时已实测 }\textbf{49 违例}\ ✗\ ——\ \text{属重复})$$

## §3 ④ 精确 supply 恒等式（**✓✓ 新、精确成立**）

$$\textbf{定义}:\ y\in S_2(c)\ (\text{距 }c\ \text{为 }2\ \text{之 }45\ \text{点}),\ m(y):=\#\{i:\ c\oplus e_i\in C,\ d(y,c\oplus e_i)=1\}$$
$$\text{每个 }1\text{-neighbor }c\oplus e_i\ \text{恰"服务"}\ 9\ \text{个 }S_2\ \text{点}\quad(\text{即 }c\oplus e_i\oplus e_j,\ j\ne i)$$
$$\therefore\ \boxed{\sum_{y\in S_2(c)}m(y)=9\,d_1(c)}✓\qquad \boxed{\#\{y:m(y)=2\}=\binom{d_1(c)}2}✓$$
$$\therefore\ \#\{y:m(y)\ge1\}=\binom{d_1}{2}+d_1(10-d_1)=d_1(10-d_1)+\binom{d_1}{2}$$
$$\therefore\ \boxed{\text{供给端}\ \textbf{仅是 }d_1(c)\ \text{之函数，与 }d_2(c)\ \textbf{无任何直接联系}}✗$$
$$\text{（即}:\ \text{"}d_2\ \text{大}\Rightarrow \text{collision 大"}\ \text{之桥\ \textbf{不存在}}\ ——\ \text{这正是 }(1)\ \text{反号之根因}）$$

## §4 可保留者与结论（**✓ 收束**）

$$\textbf{✓ 保留}:\ \text{正确 }\star\ (T_2=106(A_1+A_2)-142)\ \text{为真；配合 }T_2\ge0\Rightarrow A_1+A_2\ge1.34\ (\text{弱})$$
$$\text{（注}:\ \delta\le10\Rightarrow T_2\le639\Rightarrow A_1+A_2\le7.37\ \text{—— 仍弱于既有 }N_1{+}N_2\le161\ \text{之等价形式}）$$
$$\textbf{✗ 失效}:\ (1)\ \text{及其全部下游}\ (A_2\le12\ \text{等})$$
$$\therefore\ \boxed{\text{本路（excess 二阶碰撞耦合）当前\ \textbf{无新约束}};\ \text{须先找一条\ \textbf{真}之 }d_2\text{-耦合不等式}}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "因子2纠错" "supply恒等式" "d2无耦合"
技术词 因子2纠错    命中文件数=0    ::
技术词 supply恒等式  命中文件数=0    ::
技术词 d2无耦合    命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **120-code 全量实测（恒等式／违例／supply）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 含**重复事故之标注**（同 `29j` 之 $(F)$）✓；**不主张** $107$ 不可达 ✗（V290）
