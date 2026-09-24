已查地图：命中（`M03-LS-ES-specialization-and-region-subtraction`）⟹ 线性层闭合之独立核验 ＋ 边界族核验，不开新案
D0: 本档对象 = **`①②③` 的\textbf{独立逐条核验}**（`K_PM/K_Kellogg/K_Borobia` 在整个 `R` 上失效；边界族 `\Lambda(t)`；Johnson 墙的三次式与根；`\Lambda_*`）＋ **我方自身勘误一处** ＋ **`④` Ciarlet ⇒ Laffey–Šmigoc 锁定** ＋ **下一刀 `E` 型审计设计（含公式已存档）**
D1: 1（首次以逐字原文复核线性层失效；产出更干净的 Kellogg 排除证明与一条更强中间结论）
[RESEARCH]

# **线性层闭合与边界族：独立核验**

## §1 `①` 三项失效（逐条核验）

```
$$\textbf{PM}:\ \boxed{K_{\rm PM}\cap R=\varnothing}\ \textbf{核验通过};\ \text{链}: S<b\Rightarrow\boxed{c+d>1+a}\ (A1);\ 30d+10c=10(c+d)+20d\ge 20(c+d)\ (\text{用 }d\ge c)\ (A2)$$
$$\qquad \Rightarrow 30d+10c>20(1+a)>20\ge 12+3a+5b\ (\text{用 }b\le a\le1)\ (A3)\ \Longrightarrow\ \text{与 PM 要求矛盾}$$ ✓✓（逐字形式 $\lambda_1/5+\lambda_2/20+\lambda_3/12+\lambda_4/6+\lambda_5/2\ge0$ 已从原文核对）
$$\textbf{Kellogg}:\ \boxed{K_{\rm Kellogg}\cap R=\varnothing}\ \textbf{核验通过（本轮取到逐字完整式）};\ \text{原文 }(6)/(7):$$
$$\qquad (6)\ \lambda_0+\sum_{i\in K,\ i<k}(\lambda_i+\lambda_{n+1-i})+\lambda_{n+1-k}\ge0\ \forall k\in K;\qquad (7)\ \lambda_0+\sum_{i\in K}(\lambda_i+\lambda_{n+1-i})+\sum_{j=M+1}^{n-M}\lambda_j\ge0$$ ✓✓
$$\qquad \text{本例}:\ (\lambda_0..\lambda_4)=(1,a,b,-c,-d)\Rightarrow n=4,\ M=2,\ \lfloor n/2\rfloor=2;\ K=\{i:\lambda_i+\lambda_{5-i}<0\}=\{i: a-d<0\ \text{或}\ b-c<0\}$$ ✓
$$\qquad \text{情形分析（\textbf{四种全部排除}，每步仅用 }R\ \text{与 }(A1)\text{）}:$$
$$\qquad\qquad K=\varnothing\ (d\le a,\ c\le b)\Rightarrow c+d\le a+b\Rightarrow S\ge1>b>S\ \text{矛盾}$$ ✓
$$\qquad\qquad K=\{1\}\ (d>a,\ c\le b)\Rightarrow c+d>1+a\Rightarrow d>1+a-c\ge1+a-b\ge1 \Longrightarrow \boxed{d>1}\ \text{与 }d\le1\ \text{矛盾}$$ ✓✓（**比原推导更强的中间结论**）
$$\qquad\qquad K=\{2\}\ (c>b,\ d\le a)\Rightarrow c>1+a-d\ge1 \Longrightarrow \boxed{c>1}\ \text{矛盾}$$ ✓✓（同样更干净）
$$\qquad\qquad K=\{1,2\}:\ (6)|_{k=2}\ \text{给 }1+a-d-c\ge0\Rightarrow S-b\ge0\Rightarrow S\ge b\ \text{矛盾}$$ ✓
$$\Longrightarrow\ \text{故四种皆不可能};\ \boxed{K_{\rm Kellogg}\cap R=\varnothing}\ \textbf{确实成立}$$ ✓✓✓
$$\textbf{Borobia}:\ \boxed{K_{\rm Borobia}\cap R=\varnothing}\ \textbf{核验通过（结构层面）};\ \text{两划分}:$$
$$\qquad \text{划分 I}\ \{-c,-d\}\Rightarrow\ \text{压成 }(1,a,b,-(c+d));\ \text{因 }c+d>1+a>1,\ K\ \text{含 }i{=}1\ \text{且要求 }1-(c+d)\ge0\ \text{矛盾};$$
$$\qquad \text{划分 II}\ \{-c\}\cup\{-d\}\Rightarrow\ \text{退化为 Kellogg} \Longrightarrow \text{已排除}$$ ✓✓
$$\Longrightarrow\ \boxed{(R\setminus W)\setminus(K_{\rm PM}\cup K_{\rm Kellogg}\cup K_{\rm Borobia})=R\setminus W}\ \textbf{确认}$$ ✓✓✓
```

## §2 `②` 边界族核验

```
$$\Lambda(t)=\Bigl(1,\ t,\ t,\ -\tfrac{5-7t}{2},\ -\tfrac{5-7t}{2}\Bigr),\quad t\in\mathbb Q\cap(\tfrac49,\tfrac12)$$ ✓
$$\text{核验}:\ 4=9b-S\iff S=9t-4;\ S=1+2t-(c+d)\Rightarrow c+d=5-7t;\ c=d=\tfrac{5-7t}{2}\Rightarrow \text{代回自洽}$$ ✓✓
$$\text{R 三条件}:\ S>0\iff t>\tfrac49;\quad S<\tfrac12\iff t<\tfrac12;\quad S<b=t\iff t<\tfrac12;\quad \text{Perron } c\le1\iff t\ge\tfrac37\ (\text{自动})$$ ✓✓
$$\Longrightarrow\ \Lambda(t)\subset\partial W\cap R\ (\text{严格})$$ ✓✓
```

## §3 `③` Johnson 墙核验（含我方一处勘误）

```
$$D(t):=2\Bigl(\tfrac{5-7t}{2}\Bigr)^3-1-t^3-(4-8t)^3\ \overset{\text{sympy 逐字}}{=}\ \boxed{\tfrac34\bigl(567t^3-779t^2+337t-45\bigr)}$$ ✓✓✓（与先生所报完全一致）
$$\text{根}:\ \{0.2616134317,\ \boxed{0.4791595247},\ 0.6331247508\};\ \textbf{唯一落在 }(\tfrac49,\tfrac12)\ \text{内者}=t_*=0.479159524723$$ ✓✓（与先生一致）
$$\text{符号}:\ D(\tfrac9{20})=+0.42778>0\Rightarrow\textbf{被排除};\quad D(\tfrac{12}{25})=-0.011952<0,\ D(\tfrac{49}{100})=-0.15069<0\Rightarrow\textbf{不排除}$$ ✓✓
$$\Lambda_*=\bigl(1,\tfrac{12}{25},\tfrac{12}{25},-\tfrac{41}{50},-\tfrac{41}{50}\bigr):\ S=\tfrac8{25}\checkmark,\ 9b-S=4\checkmark,\ c=\tfrac{41}{50}\checkmark,\ S<b,\ S<\tfrac12,\ \text{Perron }\tfrac{41}{50}<1\ \checkmark$$ ✓✓
$$\text{Johnson 判据在 }\Lambda_*:\ \text{LHS}=2(\tfrac{41}{50})^3=\tfrac{68921}{62500}\approx1.102736\ <\ \text{RHS}=1+(\tfrac{12}{25})^3+(\tfrac4{25})^3=\tfrac{17417}{15625}\approx1.114688 \Longrightarrow \textbf{未被排除}$$ ✓✓
$$\textbf{⚠️ 我方自身勘误}:\ \text{上一条核验脚本我误把 }(a+2d-1)^3\ \text{写成 }S^3=(\tfrac8{25})^3;\ \text{正确为 }(\tfrac4{25})^3=\tfrac{64}{15625}$$ ⚠️
$$\qquad \text{更正后结论不变}（\text{LHS}<\text{RHS}\text{）};\ \text{已记录以便后续不复犯}$$ ✓
```

## §4 `④` 关系锁定

```
$$\boxed{\text{Ciarlet}\Rightarrow\text{Perfect--Mirsky}\Rightarrow\text{Suleimanova}}\ (\text{原文 Thm 15，逐字})$$ ✓✓
$$\boxed{\text{Ciarlet}\Rightarrow\text{Laffey--Šmigoc}}\ (\text{原文 Thm 18，先生已核}) \Longrightarrow \textbf{正式锁死};\ \text{我方待取该文逐字复核}$$ ✓✓
```

## §5 状态与下一刀

```
$$\boxed{U_{\rm linear}=R\setminus W};\quad \boxed{M03\ \textbf{不得因线性充分条件而 }DROP}$$ ✓✓✓
$$\boxed{\text{目标收缩为\textbf{单点} }\Lambda_*\ \text{与\textbf{边界族} }\Lambda(t),\ t\in(t_*,\tfrac12)}$$ ✓✓
$$\boxed{\text{下一刀}=\textbf{只对 }\Lambda_*\ \text{做 }E\ \text{型证书审计}}:\ \text{先 Soules 1/2 的 }\exists x\ \text{；再 LS／ES 递归分裂}$$ ✓✓
$$\qquad \textbf{方法}:\ \text{Soules 1 的 }(11)\ \text{式已存 }\texttt{out/map2017\_Thm9\_Soules\_page.txt};\ \text{单调性注记}:\ 0<x_1\le\dots\le x_5\Rightarrow d_1\le\dots\le d_5 \Longrightarrow \textbf{只需验 }d_1\ge0$$ ✓✓
$$\qquad \text{成功}\Rightarrow \Lambda_*\ \text{可实现（}\textbf{新正结果}:\ W\ \text{边界非全域}）;\ \text{失败}\Rightarrow \text{记录具体失败不等式（}residue\text{）},\ \text{再转 LS/ES 或 }P1$$ ✓✓
【⛔ 纪律】 `U_{2,3}` 暂停；**不回 RH**；`C07` 已封口；下一刀若涉搜索须先报代价 ✓
【边界】 §1 的 Kellogg 逐字式本轮已取；§1 的三项失效结论为\textbf{本行独立核验}；§3 的勘误为\textbf{我方自我更正} ✓

## §附 【技术词回查】（补录）
```
技术词 symbolic elimination 命中文件数=0    :: 
技术词 witness          命中文件数=61   :: ./KERNEL-HUNT-1-two-minimization-problems.md ./V2-28B-L52-mechanism-identified-verdict-OPEN.md ./E4-2-falsifiable-conditions-spec-for-line-enforcing-localization.md 
```
