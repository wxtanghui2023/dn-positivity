已查地图：命中（`X1-K10-5-global-cp-sat-run1-result`）⟹ `X1` 第六轮：**B1-a 搜索机制实验**（先生选 B1），不开新案
D0: 本档对象 = **B1-a 设计（同模型／同约束，只切 LP ＋ 多 seed，总预算仍 3600 s）** ＋ **冒烟对比基线** ＋ **判定表（锁死）** ＋ **API 修正** ＋ **cron 投递修复验证**
D1: 1（实际计算：搜索机制对照实验）
[RESEARCH]

# **B1-a：`no_lp` ＋ 多 seed（同模型）**

## §1 设计（**只动一个变量**）

```
$$\textbf{模型完全不变}:\quad \sum_{c=0}^{1023}x_c=119;\qquad \forall v:\sum_{d_H(c,v)\le1}x_c\ge1;\qquad x_{0000000000}=1$$
$$\textbf{唯一改动}:\ \text{子求解器集} = \boxed{\{\texttt{no\_lp}\}}\ (\text{切掉 }\texttt{default\_lp}/\texttt{max\_lp\_sym});\quad \textbf{多 seed}:\ 11,22,33,44$$
$$\textbf{总预算}:\ 4\times900\ \text{s}=3600\ \text{s}\ (\text{与首轮}\ \textbf{同总预算} \Longrightarrow \text{干净对照})$$
$$\text{记录}:\ status;\ incumbent;\ conflicts;\ branches;\ propagations;\ integer\_propagations;\ restarts;\ deterministic\_time;\ walltime;\ \boxed{cf/br,\ prop/br}$$
```

## §2 冒烟基线（已实测，15 s/seed）

```
$$\texttt{no\_lp}\ \text{生效确认}:\ \text{日志}\ \texttt{full problem subsolvers: [no\_lp(3)]};\quad \texttt{lp\_iterations} = \boxed{0}\ \checkmark$$
$$\text{seed }201:\ conflicts=278{,}098;\ branches=2{,}720{,}247;\ propagations=219{,}440{,}486;\ restarts=1{,}040;\ \boxed{cf/br=0.1022,\ prop/br=80.67}$$
$$\text{seed }202:\ conflicts=276{,}743;\ branches=2{,}716{,}084;\ propagations=218{,}393{,}932;\ restarts=1{,}037;\ \boxed{cf/br=0.1019,\ prop/br=80.41}$$
$$\Longrightarrow\ \text{速率}\approx18.5\text{k conflicts/s}\ \Longrightarrow\ 3600\ \text{s 预计}\approx\boxed{6.7\times10^7\ \text{conflicts}}\ (\approx 2.7\times\ \text{首轮}\ 2.45\times10^7)\ ——\ \text{对照有意义} ✓$$
```

## §3 判定表（**锁死**）

```
$$\begin{array}{c|l}
\text{B1-a 结果}&\text{含义}\\\hline
\text{找到 119 ＋ 独立验证 }1024/1024&\boxed{\text{成功}:\ K(10,1)\le119\ (\text{显式证书})}\\
\text{仍 0 incumbent}&\boxed{\text{no-LP 也无法进入可行域}}\\
\text{UNKNOWN ＋ 有 incumbent}&\text{必须独立验证};\ \text{验证通过才算成果}\\
\textbf{INFEASIBLE}&\boxed{\text{极重要}:\ 119\ \text{不可能}\Rightarrow K(10,1)=120};\ \textbf{必须保留 solver proof／response}
\end{array}$$
$$\textbf{禁止}:\ \text{“119 不存在”（除非上表第 4 行且证据留存）}$$
$$\textbf{实验要回答的问题}:\ \boxed{\text{119 的困难是}\textbf{LP/搜索器机制问题}\ \text{还是}\textbf{整个 CP-SAT 编码对组合结构不友好}?}$$
```

## §4 两处工程修正（本轮）

```
$$\textbf{(a) API}:\ \texttt{CpSolver.NumPropagations}\ \textbf{不存在}（AttributeError）\ \Longrightarrow\ \text{改从 }\boxed{\texttt{solver.ResponseProto()}}\ \text{读全部计数字段（}num\_conflicts/num\_branches/num\_binary\_propagations/num\_integer\_propagations/num\_restarts/deterministic\_time）$$
$$\qquad \text{另}:\ \texttt{parameters.subsolvers[:] = [...]}\ \text{抛 }TypeError\ \Longrightarrow\ \text{必须用}\ \boxed{\texttt{parameters.subsolvers.extend([...])}}$$
$$\textbf{(b) cron 投递}:\ \text{昨日失败根因}=\texttt{isolated}+\texttt{announce}\Rightarrow\texttt{last}\Rightarrow\text{Feishu 无 target};\ \text{本轮改为}\ \boxed{\texttt{sessionTarget="current"}}\ \text{（绑本会话）};\ \text{任务 id } \texttt{5495984f}✓$$
【⛔ 纪律】 同模型、同约束、同总预算；\ \text{不同时改模型};\ \text{不跑 }(4,3) ✓
【边界】 记录 }[107,120]\ \text{取自 OEIS（抽取级）};\ \text{数值均本地实测} ✓
