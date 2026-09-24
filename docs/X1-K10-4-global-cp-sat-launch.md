已查地图：命中（`X1-K10-3-rigidity-certificate-1-1-2-1-3-2`）⟹ `X1` 第四轮：**全局精确 CP-SAT**（先生选乙），不开新案
D0: 本档对象 = **全局 `119` CP-SAT 模型规范** ＋ **对称破缺** ＋ **120-码 hint（软）** ＋ **incumbent 独立验证出口** ＋ **判定树（锁死）** ＋ 运行参数与监控命令
D1: 1（实际计算；全局搜索空间，非记录码邻域）
[RESEARCH]

# **`X1 / K(10,1) ≤ 119`：全局 CP-SAT（乙）**

## §1 模型（**精确式，非 min-cover 降**）

```
$$x_c\in\{0,1\},\quad c\in\{0,\ldots,1023\}\ (\text{全部 }\{0,1\}^{10}\ \text{词})$$
$$\boxed{\sum_c x_c = 119}\qquad(\text{精确规模};\ \text{solver 第一秒就在回答真问题})$$
$$\forall v\in\{0,1\}^{10}:\quad \boxed{\sum_{c:\ d_H(c,v)\le1} x_c\ \ge\ 1}\qquad(\text{每条约束恰涉及 }\mathbf{11}\ \text{个变量 —— 极稀疏集合覆盖})$$
```

## §2 对称破缺与 hint（照先生三条纪律）

```
$$\textbf{对称破缺}:\ \text{固定 }\boxed{x_{0000000000}=1}\ ——\ \text{由 }\operatorname{Aut}(Q_{10})\cong C_2^{10}\rtimes S_{10}\ \text{保一般性（任意码字可用坐标翻转送到零字）}$$
$$\qquad \text{第一版\textbf{只固定零字}};\ \text{不手工固定第二字的 Hamming 重量（避免为理论压缩增加模型复杂度）} ✓$$
$$\textbf{hint（\textbf{软}，非约束）}:\ \text{取已验证 120-码删去“私有覆盖最少”的字 }0111111001\ \Longrightarrow\ 119\ \text{字};\ \text{再做坐标翻转使其含零字（翻转是自同构，覆盖性不变）}$$
$$\qquad \text{实测}:\ \text{该 119-字集}\ \textbf{不是覆盖}（\text{剩 }2\ \text{点未覆盖}）\ \Longrightarrow\ \text{CP-SAT 自报}\ \boxed{\text{“complete, but it is infeasible! we will try to repair it”}}\ ——\ \text{正是“以近邻为起点、但不限于近邻”} ✓✓$$
$$\qquad \textbf{关键}:\ \text{hint \textbf{不}把搜索限制在记录码邻域};\ \text{solver 全局自由} ✓$$
```

## §3 incumbent 独立验证出口（硬纪律）

```
$$\text{回调对**每个** incumbent 立即执行}\ \boxed{\text{独立覆盖率验证（}1024/1024\text{）}};\ \text{仅当 }verify=True\ \text{才写出证书并 }\texttt{StopSearch}$$
$$\qquad \text{理由（已有实例）}:\ \text{此前 my own }(2,1)\ \text{首版实现 bug 产出假解，}\textbf{当场被 }verify\ \text{判死} \Longrightarrow\ \boxed{\text{solver 说“找到”不是交付；独立 verifier 的 }True\ \text{才是}} ✓$$
```

## §4 判定树（**锁死**）

```
$$\begin{array}{c|l}
\text{结果}&\text{允许的表述}\\\hline
\text{CP-SAT 返回已验证 119-cover}&\boxed{K(10,1)\le119\ \text{新上界记录（显式证书）}}\\
\text{预算内未找到}&\boxed{\text{“全局 CP-SAT 在给定模型/对称性/预算下未找到 119”}}\\
\text{（禁止）}&\boxed{\text{“119 不存在”}}\ ——\ \text{仅当获得}\ \textbf{UNSAT 证书／独立数学下界 120}\ \text{才可升级}
\end{array}$$
$$\textbf{与前三层的关系}:\ \text{局部刚性证书（}(1,1)/(2,1)/(3,2)\text{）与全局搜索是}\textbf{两个层级};\ \text{全局未找到}\ \textbf{不}\ \text{使局部证书作废；反之亦然}$$
```

## §5 运行与监控

```
$$\text{环境}:\ \texttt{ortools 9.15.6755};\quad \text{脚本}:\ \texttt{work/k10/cp119.py}\ (\text{预算／种子可传参});\quad \text{冒烟}:\ 30\ \text{s}\to\text{UNKNOWN},\ 325{,}702\ \text{conflicts}$$
$$\text{长跑}:\ \texttt{python3 -u cp119.py 3600 1 > cp119_run1.log}\ (\text{4 workers, hint 修复模式})$$
$$\text{监控}:\ \texttt{grep -E "incumbent|status|★" cp119_run1.log | tail};\quad \text{成功即出现 }\texttt{code119\_GLOBAL.json}$$
$$\textbf{明确不做}:\ (4,3)\ \text{定向剪枝（照先生令：先让全局 solver 说话，再决定是否回头）} ✓$$
【⛔ 纪律】 实际计算；\ \text{判定树锁死};\ \text{证书必须过独立 verifier} ✓
【边界】 记录 }[107,120]\ \text{取自 OEIS（抽取级）；本模型为精确编码，无松弛} ✓
