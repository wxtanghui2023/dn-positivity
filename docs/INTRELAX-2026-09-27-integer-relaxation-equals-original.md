已查地图：已跑 scripts/prework_map_check.sh 整数松弛 supp 覆盖码 ⟹ 执行唐先生 15:49 裁示（走甲 ✓）；本档 = **定理级判定：整数松弛 ≡ 原问题 ✓ ＋ 小 n 数值验证 ✓ ＋ n=10 ILP 已启动 ✓**。
D0: 本档对象 = $K_{\mathbb Z}(10,1)\le119$ 之判定（整数/多重覆盖松弛）
D1: 3（**等价定理 ✓✓（非松弛）**；**小 n 验证 n=4,5,6 ✓✓**；**n=10 ILP 启动 ⏳**）

# 整数松弛：等价定理与验证（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(PA-1 ⭐⭐等价定理（三行证明 ✓✓）)}\ \text{设 }f\in\mathbb Z_{\ge0}^{1024},\ Tf\ge1\ ✓.\ \text{对任意点 }y:\ (Tf)(y)=\sum_{x:d(x,y)\le1}f(x)\ge1 \Longrightarrow \exists x\in\mathrm{supp}(f),\ d(x,y)\le1\ ✓}$$
$$\qquad\Longrightarrow \boxed{\mathrm{supp}(f)\ \text{本身就是一个 0-1 覆盖码 ✓}}\ \text{且}\ \boxed{|\mathrm{supp}(f)|\le\sum_x f(x)}\ ✓ \Longrightarrow \boxed{\min\{\sum f:\ f\in\mathbb Z_{\ge0},\ Tf\ge1\}\ =\ K(n,1)}\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{整数松弛不是松弛 ✗}:\ "K_{\mathbb Z}(10,1)\le119"\iff"K(10,1)\le119"\iff\text{存在 119-覆盖码}\ ✓✓}$$
$$\qquad\textbf{但\textbf{性质改变} ✓}:\ \text{它给出一个\textbf{更宽的可搜索形式}（允许权重 ⟹ 约束更松 ✓）};\ \text{而任一 }\sum f=119\ \text{的整数解，其 }\mathrm{supp}\ \text{直接给一个 119-覆盖码 ✓✓}$$
$$\boxed{\textbf{(PB-1 ⭐小 n 数值验证 ✓✓（HIGHS ✓）)}\ \text{ILP}: \min\sum f\ \text{s.t.}\ Tf\ge1,\ f\in\mathbb Z_{\ge0},\ f\le2:}$$
$$\qquad\begin{array}{c|c|c|c}
n & \text{ILP 最优 }\sum f & K(n,1)\ (\text{已知}) & \text{最优解是否 0-1 值}\\
\hline
4 & \mathbf 4 & 4 & ✓（全部 ≤1）\\
5 & \mathbf 7 & 7 & ✓\\
6 & \mathbf{12} & 12 & ✓\\
\end{array} \Longrightarrow \textbf{三例皆与 }K(n,1)\ \text{相等 ✗（无松弛益）且最优解恒为 0-1 ✓（定理的实证 ✓✓）}$$
$$\qquad\textbf{定向反证 ✓}:\ n{=}5\ \text{穷举全部 6-子集（}C(32,6){=}906192\ ✓）\ \textbf{无一覆盖} ⟹ \sum f=6\ \text{不可行 ✓（与 }K{=}7\ \text{一致 ✓）}$$
$$
$$
```

## §1 n=10 现状（**⏳ 已启动**）

```
$$\text{ILP}:\ 1024\ \text{整数变量},\ 1024\ \text{覆盖约束（每 11 项 ✓）},\ f\le2\ ✓;\ \text{solver}=\text{HIGHS}\ ✓;\ \text{后台 }\texttt{setsid}\ +\ \text{pyguard}(2500\text{MB})\ ✓$$
$$\textbf{三种可能结局（皆有信息 ✓）}:\ \text{(i) 最优 }<120\ \text{或 }=119\Longrightarrow \text{直接取 }\mathrm{supp}\ \text{得 119-覆盖码 ⟹ }K(10,1)\le119\ \textbf{（正向突破 ✓✓）};\ \text{(ii) 证不可行 ⟹ }K\ge120\ \textbf{（负向突破 ✓✓）};\ \text{(iii) UNKNOWN ⟹ 与档案 CP-SAT 同境 ⚠️}$$
$$
$$
```

## §2 状态（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{整数路由\textbf{等价定理}定位（非松弛 ✗，但为更宽搜索形式 ✓）};\ \text{小 n 验证 ✓};\ \text{不写禁止表述 ✓}}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：等价定理（$\min\sum f=K(n,1)$）、小 $n$ 验证（$n{=}4,5,6$）、$n{=}5$ 六子集穷举反证、$n{=}10$ ILP 启动记录
- **档案已有（引用，不列为提出）**：$K$ 表值（$4/7/12$）、M-2A（LP $1024/11$）、CP-SAT UNKNOWN 记录


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 等价定理     命中文件数=6    :: ./LEVELS-2026-09-27-four-tier-separation-and-3B-pending.md ./R-A8-prime-pair-carrier-audit.md ./ZF-MECH-1-finite-index-mechanism-audit-and-convergence.md 
技术词 整数松弛     命中文件数=3    :: ./ASSETS-REGISTRY.md ./INTRELAX-2026-09-27-integer-relaxation-equals-original.md ./P1-REAUDIT-2026-09-27-E-correction-and-the-mod-11-theorem.md
```
- **本档新增**：等价定理（$\min\sum f=K(n,1)$）、小 $n$ 验证（$n{=}4,5,6$）、$n{=}5$ 六子集穷举反证、$n{=}10$ ILP 启动记录（见上方命中数；0 命中者为自造语／内部标签 ✓）
