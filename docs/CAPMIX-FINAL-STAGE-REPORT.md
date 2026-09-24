已查地图：命中（`CAPMIX1B-B12-B11-closed-as-instance-of-known-theory`）⟹ 本档为**终期审计报告**（非研究论文），不开新案
D0: 本档对象 = **`CAP-MIX` 终期封存审计**：自证资产／已知理论实例／被反例杀死／孤立现象／停止理由 + **新性误判复盘**
D1: 0 （审计档，不产生新自由度）
[REVIEW]

# **`CAP-MIX` 终期审计报告（FINAL STAGE REPORT）**

## §0 Executive Status

```
$$\boxed{\texttt{CAP-MIX} = \textbf{CLOSED / ARCHIVED}};\qquad \texttt{U}_{2,3}=\textbf{PAUSED};\qquad \textbf{No RH re-entry}$$ ✓
$$\text{档案位置}:\ \texttt{docs/CAPMIX1B-B1..B12-*.md};\qquad \text{数据}:\ \texttt{out/capmix1B*.txt};\qquad \text{脚本}:\ \texttt{scripts/capmix1B*.py}$$ ✓
```

## §1 Problem Definition（`1A` / `1B`）

```
$$\lambda(G)=\#\{x\in G:\ 1+x\in G\}\ (p=2);\qquad \lambda(G)=\#\{x\in G:\ -1-x\in G\}\ (p\ \text{奇})$$ ✓
$$\text{CAP}:\ \text{无三/四元加法关系};\quad \text{Valid}:\ \text{非退化构型};\quad \text{blind}:\ J_{\rm info}=\varnothing;\quad \text{nonblind}:\ J_{\rm info}\ne\varnothing$$ ✓
$$1A:\ \text{奇特征（}R_\ast\ \text{压缩}+\lambda_{\rm valid}\text{）};\qquad 1B:\ \text{char 2（}V_\ast\ \text{二维压缩）}$$ ✓
```

## §2 `B1`–`B3` Initial Reduction

```
$$1A:\ \text{三项条件归一为 }x+y=-1\ (\textbf{一维})\ \Longrightarrow\ \lambda_{\rm valid}=0\iff\text{CAP}\ (\text{实测 }204/204)$$ ✓
$$1B:\ \text{四项条件归一为 }x+y+z+1=0\ (\textbf{二维})\ \Longrightarrow\ \text{对应量是 }|\text{Valid}|,\ \text{非 }\lambda$$ ✓✓（**维度差是本支线第一关键**）
$$B3\ \text{合并}:\ P_\ast=\{(x,1+x):x\in I_2(G)\};\quad V_\ast=\text{Valid}\sqcup\text{直线 }z=0;\quad \text{CAP}\iff V_\ast\subseteq\{z=0\}$$ ✓
```

## §3 `B4`（`T` 作用与 Frobenius–inversion 判据）

```
$$T(x)=1+x^{-1},\quad T^3=\mathrm{id};\qquad I(G)\ \text{严格 }T\text{-不变}\ (39/39);\qquad \lambda\equiv2\!\!\pmod3\iff3\mid d$$ ✓✓
$$\text{充分判据（初稿）}:\ 2^k\equiv-1\ (\mathrm{mod}\ d)\ \wedge\ 3\nmid d\ \Longrightarrow\ \lambda=0$$ ✓
$$\text{边界}:\ \textbf{充分 ≠ 必要};\quad (23,89)\ \text{在判据之外（}\mathrm{ord}\ \text{奇）}$$ ✓
```

## §4 `B5`（`\Gamma=\langle F,T\rangle`）

```
$$F(x)=x^2,\quad FT=TF,\quad \Gamma\cong C_n\times C_3\ (\text{或商});\qquad \text{轨道长度}\mid3n$$ ✓✓
$$\text{混合稳定元审计}:\ \textbf{全部 }9\ \text{个 }\lambda=0\ \text{案例中 }G\ \text{内均有混合稳定元}$$ ✓
$$\Longrightarrow\ \textbf{CLOSED 理由}:\ \text{混合稳定元\textbf{不能}解释 }\lambda=0\ (\text{按预设 EXIT})$$ ✓
```

## §5 `B6`（互补对偶扫描）

```
$$\text{22 对互补对}:\ I=1,\ II=0,\ \boxed{III=7},\ IV=14;\qquad B4\ \text{分类}:\ A=0,B=4,C=3,D=15$$ ✓
$$\boxed{III\ \text{类 7 例单侧零}\ \Longrightarrow\ \text{互补零性被击穿}};\qquad \text{且 7/7 零侧恰为满足 }B4\ \text{的一侧}$$ ✓✓
$$\Longrightarrow\ \textbf{CLOSED 理由}:\ \text{零性层面 }d\leftrightarrow m\ \text{对偶不成立}$$ ✓
```

## §6 `B7`（盲类交叉检验与口径纠正）

```
$$\lambda_{\rm raw}=\lambda_{\rm valid}:\ \text{blind }17/17,\ \text{nonblind }22/22\ \Longrightarrow\ \texttt{PASS};\qquad \textbf{但为恒等（char 2 下 }D(G)=\varnothing\text{）}$$ ⚠️
$$\text{纠正}:\ N(G)\ (\text{有序计数}) \ne |\text{Valid}|\ (\text{三条退化族各贡献 }d\text{ 对});\qquad N(G)\ \textbf{恒}>0$$ ✓✓
$$\Longrightarrow\ \text{CAP 判定量是 }|\text{Valid}|;\quad \lambda=0\ \textbf{不}蕴含\ 1B\ \text{的 CAP}$$ ✓✓
```

## §7 `B8`（盲类结构）

```
$$\text{blind}\ \text{类全不变量只依赖 }d;\qquad d\in\{3,7,15,31,63\}=2^k-1\ \Longrightarrow\ G=\mathbb F_{2^k}^\times\ (\textbf{子域})$$ ✓✓
$$\text{盲类 CAP}:\ \text{四点须两两相异}\ \Longrightarrow\ \text{CAP}\iff d\le3\ (\textbf{基数判据})$$ ✓✓
$$\text{nonblind}:\ V_\ast\ \text{压缩}\le0.32,\ \text{可判定};\qquad \text{1A 侧}:\ \lambda_{\rm valid}\ \text{一维精确（盲区 }126/204\text{）}$$ ✓
```

## §8 `B9` ⭐ **唯一自证定理**

```
$$\boxed{\textbf{THEOREM}\ (\text{充分判据}):\quad \Big(\exists k:\ 2^k\equiv-1\ (\mathrm{mod}\ d)\Big)\ \wedge\ (3\nmid d)\ \Longrightarrow\ \lambda(G_{2^n,d})=0}$$ ✓✓✓
$$\text{证明}:\ x,1+x\in G\ \Longrightarrow\ x^{2^k}=x^{-1},\ (1+x)^{2^k}=1+x^{-1}=(1+x)^{-1}\ \Longrightarrow\ x^2+x+1=0\ \Longrightarrow\ \mathrm{ord}(x)=3\mid d\ \textbf{矛盾}$$ ✓
$$\text{机器核验}:\ \text{cases}=56,\ \texttt{hyp}=7,\ \texttt{hyp\_lam0}=7,\ \boxed{\texttt{hyp\_viol}=0}$$ ✓✓
$$\text{最小性}:\ \text{两条件皆必要（去 ② 有 }9\ \text{反例；去 ① 有 }16\ \text{反例）};\quad \text{且 }k\ \text{非最小仍成立}$$ ✓
$$\text{纠正}:\ \textbf{"}\mathrm{ord}_d(2)\ \text{偶" 不等价于条件①}\ (\text{5 反例}:d=35,85,91,341,455)$$ ✓✓
```

## §9 `B10`（同型族扫描 `(23,89)`）

```
$$\text{同型条件}:\ \mathrm{ord}_d(2)=\mathrm{ord}_m(2)=n\ \wedge\ -1\notin\langle2\rangle\ \text{两侧};\quad n\le14\ \text{命中 4 对}$$ ✓
$$\text{型分布}:\ 00=1\ (\text{仅 }(23,89)),\ ++=3\ \Longrightarrow\ \boxed{(23,89)\ \textbf{孤立算术例},\ \text{不构成族}}$$ ✓✓
```

## §10 `B11`（容量结构与三个否定）

```
$$\lambda\le d\ \textbf{为定义级（平凡）};\qquad \rho:=\lambda/d;\qquad \text{子域类}:\ d=p^k-1\Rightarrow\lambda=d-1\ (\textbf{已证})$$ ✓✓
$$\text{非子域极值}:\ \rho_{\max}=8/21=0.38095\ (\text{char 2 网格});\qquad \text{奇特征出现 }\rho>1/2\ (\text{指标 }2\ \text{子群})$$ ✓
$$\boxed{(1)\ E_{1/2}\ \textbf{否定}:\ 24\ \text{例跨特征非子域反例}}$$ ✓✓
$$\boxed{(2)\ 3/8\ \textbf{否定}:\ d=21,\ \lambda=8\Rightarrow\rho=8/21>3/8}$$ ✓✓
$$\boxed{(3)\ AA\setminus\{1\}\subseteq A\ \textbf{否定}:\ 50\ \text{例};\ \text{解析原因}:\ A=G\setminus\{-1\},\ AA=G\Rightarrow-1\in AA\setminus\{1\}\notin A}$$ ✓✓✓
```

## §11 `B12`（收口：已知理论实例）

```
$$\textbf{最小包含域引理（一行证明）}:\ Q=p^{\mathrm{ord}_d(p)}\ \Longrightarrow\ \boxed{\lambda(G,\mathbb F_{p^n})=\lambda(G,\mathbb F_Q)}$$ ✓✓
$$\text{字符展开}:\ 1_G=\frac1m\sum_{\chi^m=1}\chi\ \Longrightarrow\ \lambda=\frac1{m^2}\sum_{\chi,\psi}\sum_x\chi(x)\psi(1+x);\quad \text{主项}\ \frac{Q-2}{m^2}=\frac{d^2}{Q}(1+O(Q^{-1}))$$ ✓
$$\Longrightarrow\ \boxed{\lambda=\frac{d^2}{Q}+O(\sqrt Q)}\quad(\text{Weil/Jacobi 型，\textbf{已知机制}})$$ ✓✓
$$\text{439 例审计}:\ \texttt{dev}>\sqrt Q:\ \textbf{0 例};\qquad \max\frac{\texttt{dev}}{\sqrt Q}=\boxed{0.9648}$$ ✓✓（**偏差顶到上限 ⟹ 无可见加严空间**）
$$\boxed{\text{文献识别}:\ \text{乘法子群与加法平移的交集（Vyugin–Solodkova–Shkredov 2016 等）}\ \Longrightarrow\ \textbf{已知理论实例化}}$$ ✓✓
$$\textbf{收口写法}:\ \text{我们\textbf{不是}证明了一个新的"子域大容量定理"，而是发现并验证了一个结构现象，}$$
$$\qquad \text{随后识别出其控制量正是有限域乘法子群与加法平移交集这一已有理论对象，439 例实验与 }d^2/Q+O(\sqrt Q)\ \text{标准尺度一致}。$$ ✓✓
```

## §12 Asset Register（**本报告最重要部分**）

```
$$\textbf{A. 自证数学资产}\quad\begin{array}{c|c|c}
\text{资产}&\text{内容}&\text{新性}\\
\hline
A1&\textbf{B9 定理}:\ (2^k\equiv-1)\wedge(3\nmid d)\Rightarrow\lambda=0&\textbf{自证};\ \text{文献新性\textbf{未核}}\\
A2&\text{子域精确值}:\ d=p^k-1\Rightarrow\lambda=d-1&\text{自证（初等）}\\
A3&\text{最小包含域引理}:\ \lambda(\mathbb F_{p^n})=\lambda(\mathbb F_Q)&\text{自证（一行）；很可能属 folklore}\\
\end{array}$$ ✓
$$\textbf{B. 机器核验资产}\quad B1:\ B9\ \text{的 }7/7;\quad B2:\ B8\ \text{盲类 }d\text{-only};\quad B3:\ B12\ \text{的 }439\ \text{例偏差谱};\quad B4:\ B6\ \text{的 }22\ \text{对分类}$$ ✓
$$\textbf{C. 已知理论实例}\quad C1:\ \lambda\ \text{的尺度 }d^2/Q+O(\sqrt Q);\quad C2:\ \text{多平移交集（Stepanov 线）};\quad C3:\ \text{子域} / m=1\ \text{型（Garcia–Voloch 型）}$$ ✓
$$\textbf{D. 否定证书}\quad D1:\ E_{1/2}\ (24\ \text{例});\ D2:\ 3/8\ (d=21);\ D3:\ AA\setminus\{1\}\subseteq A\ (50\ \text{例});\ D4:\ \text{互补零性}\ (7\ \text{例});\ D5:\ \text{混合稳定元}\ (9/9\ \text{反})$$ ✓✓
$$\textbf{E. 孤立线索}\quad E1:\ (23,89)\ (\lambda=0,\ -1\notin\langle2\rangle);\quad E2:\ 8/21\ (\text{有限网格极值，非 sharp 常数})$$ ⚠️
$$\textbf{F. 数据工件}\quad \texttt{out/capmix1B*.txt};\quad \texttt{scripts/capmix1B*.py};\quad \texttt{docs/CAPMIX1B-B*.md}$$ ✓
```

## §13 Claim Discipline（**明令禁止的宣称**）

```
$$\textbf{禁止}:\ (1)\ \text{"大容量}\iff\text{子域"作为新定理};\ (2)\ 8/21\ \text{为 sharp 常数};\ (3)\ E_{1/2};\ (4)\ 3/8\ \text{界};$$
$$\qquad (5)\ (23,89)\ \text{作为族/机制};\ (6)\ B5/B6\ \text{作为正机制};\ (7)\ \text{把 }\lambda\ \text{的尺度写作本支线成果}$$ ✓✓
$$\textbf{允许}:\ B9\ \text{作为自证定理（标注新性未核）};\ \text{三个否定证书};\ \text{子域精确值};\ \text{最小包含域引理（标 folklore 风险）}$$ ✓
```

## §14 Final Closure Matrix

```
$$\begin{array}{c|c|c|c}
\text{档}&\text{STATUS}&\text{RESULT}&\text{WHY CLOSED / REOPEN}\\
\hline
B1\text{–}B3&CLOSED&\text{维度差}+\ V_\ast\ \text{分解}&—\\
B4&SPLIT&\text{充分判据（}\to B9\text{）}+\ \lambda\equiv2/0\bmod3&T\ \text{结构已用尽}\\
B5&CLOSED(负)&\Gamma\cong C_n\times C_3&\text{混合稳定元不能解释 }\lambda=0\\
B6&CLOSED(负)&\text{互补零性被击穿}&7\ \text{例单侧零}\\
B7&CLOSED&\text{口径纠正（}N(G)\ne|\text{Valid}|\text{）}&\text{恒等，非新信息}\\
B8&CLOSED&\text{盲类}=\text{子域类};\ \text{CAP}\iff d\le3&\text{基数为判据}\\
B9&\boxed{\textbf{SELF-PROVED}}&\text{定理（}7/7\text{）}&\text{新性未核（唯一保留定理）}\\
B10&CLOSED&(23,89)\ \text{孤立例}&\text{同型族 }++\ 3\ \text{例}\\
B11&CLOSED(负)&\text{三项否定（}E_{1/2},3/8,AA\text{）}&\text{反例批量}\\
B12&\boxed{\textbf{KNOWN-THEORY}}&\lambda=d^2/Q+O(\sqrt Q)&\text{已知理论实例化}\\
\end{array}$$ ✓✓
```

## §15 Reopening Conditions

```
$$\textbf{仅当新源提供}:\ (i)\ \text{真正新的算术对象};\ (ii)\ \text{标准平移子群理论之外的定理};\ (iii)\ \text{既有收口未覆盖的参数区};\ (iv)\ \text{可证伪的独立问题}$$ ✓✓
$$\text{不得以}:\ \text{"再拟合一次 }\rho"\ \text{／"换个 }p\ \text{再扫一遍"／"把 }B9\ \text{包装成一般判据"\ 方式重开}$$ ✓
```

## §16 Final Verdict

```
$$\boxed{\texttt{CAP-MIX}\ \textbf{ARCHIVED};\quad \textbf{No further mechanism generation};\quad \texttt{U}_{2,3}\ \textbf{PAUSED};\quad \textbf{No RH re-entry}}$$ ✓
```

## §17 ⛔ 新性误判复盘（本档**新增的流程结论**，与您 16:03 的质询直接对应）

```
$$\textbf{问}:\ \text{选课题时是否漏查"是不是已知定理"？}\qquad \textbf{答}:\ \text{漏查的不是\textbf{课题}，而是\textbf{问题的形状变化}。$$ ✓
$$\text{入档时（}2026\text{-}09\text{-}24\text{）已核}:\ \text{源论文（arXiv:2604.26989）明示一般分类与 }x_1^d+\dots+x_k^d=0\ \text{机制\textbf{开放}}\ \Longrightarrow\ \text{入口合法}$$ ✓
$$\text{但}:\ B11\ \text{把问题从"哪些 }G\ \text{是 cap"（} \lambda=0\ \text{的判定）\textbf{换成}"}\lambda\ \text{的尺度是多少"（}$$
$$\qquad \Longrightarrow\ \textbf{这一步恰好跨进了经典对象}（\text{乘法子群}\cap\text{加法平移的\textbf{大小}估计}），而\textbf{换形状时未重跑文献核}$$ ✗✗
$$\Longrightarrow\ \boxed{\textbf{流程修正}:\ \text{文献核查必须绑定\textbf{当前问题形状}，而非入档课题；对象一换形状，立即重跑}}$$ ✓✓（**本支线的最大教训，应与「先查地图」并列写入制度**）
$$\text{代价评估}:\ B11+B11.1+B11.3+B12\approx4\ \text{轮};\ \text{收益}:\ C1\ \text{定性};\ D1\text{–}D3\ \text{三个否定证书};\ A1\ \text{保留定理}$$ ✓

## §附 【技术词回查】（补录）
```
技术词 instantiation    命中文件数=5    :: ./C84-wall-breaking-phase-positivity-cone-source-enumeration-10-classes-classification-closed.md ./E23-lee-yang-dqpt-report.md ./INDEX-BY-DIRECTION.md 
技术词 shifted subgroup 命中文件数=0    :: 
```
