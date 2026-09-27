已查地图：已跑 scripts/prework_map_check.sh 系统形式 完美码条件 Vasil'ev 失败 ⟹ 执行自 `P2-A-2026-09-27-...`（✓）＋ 唐先生 13:43（开甲 ✓）；本档 = **首次尝试失败（覆盖 ✗）＋ 导出并验证完美码的系统形式判定条件 ✓**。
D0: 本档对象 = 系统形式非线性完美码的构造条件与首次尝试结果
D1: 2（**失败记录（含纪律要点 ✓）**；**导出并验证判定条件 ✓✓**）

# P2-A 第一步：失败尝试与导出条件（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BY-1 ⚠️ 首次尝试失败)}\ \text{取 }C=\{(u,\psi(u))\},\ \psi=A\oplus\varphi\ (\varphi\ \text{非线性二次 ✓})\ \Longrightarrow\ \text{覆盖核验 }\mathfrak B_1(C_2)\ne\mathbb F_2^{15}\ ✗\ \text{且 }\mathfrak B_1(C)\ne\mathbb F_2^{16}\ ✗ \Longrightarrow \textbf{该对象不是 NP1CC} ✗}$$
$$\qquad\Longrightarrow\ \text{其 }(\nu\ \text{非星}\ ✓)\ \textbf{无效} ✗\ \text{——}\textbf{不得记为 P2 collision} ✓✓\ \text{（正是唐先生 13:43 警告的陷阱 ✓）}$$
$$\boxed{\textbf{(BY-2 ⭐导出条件 ✓✓)}\ \text{系统形式 }C=\{(u,\psi(u))\}\ (u\in\mathbb F_2^{11}\mapsto\psi(u)\in\mathbb F_2^4)\ \text{是完美 }[15,11,3]\ \text{码}}$$
$$\qquad\iff\ \boxed{\forall a\in\mathbb F_2^{11}:\quad\{\psi(a+e_j)\oplus\psi(a)\}_{j=1}^{11}=W_2:=\{v\in\mathbb F_2^4:\ \mathrm{wt}(v)\ge2\}\ (|W_2|=11)\ }\ ✓✓$$
$$\qquad\textbf{双向验证 ✓}:\ \text{线性 }\psi=A\ \text{（}11\ \text{列 }=W_2\ ✓\text{）违反 }0/2048 ✓;\ \text{我的 }\psi=A\oplus\varphi\ \text{违反 }1984/2048 ✗\ \Longrightarrow \text{条件\textbf{正确} ✓（含正控 ✓）}$$
$$\qquad\Longrightarrow\ \text{非线性的真正入口} =\ \textbf{解此条件} ✓\ \text{（Vasil'ev 型即其非线性解 ✓）};\ \text{条件为局部的（逐 }a\ \text{）且可即时检验 ✓✓}$$
$$
$$
```

---

## §1 尝试与失败数据（**✓ 诚实记录**）

```
$$\text{构造}:\ \psi(u)=A(u)\oplus\varphi(u),\quad \varphi(u)=(u_0u_1,\ u_0u_2,\ u_0u_3,\ u_0u_4)\ (\text{非线性二次 ✓},\ \varphi(0)=0\ ✓)$$
$$\begin{array}{c|c}
\text{项} & \text{结果}\\
\hline
|C_1|=|C_2| & 2048\ ✓\ (\text{尺寸对 ✓})\\
|C_1\cap C_2| & \mathbf{1088}\ \ (\text{部分 ⟹ "Type C" 形 ✓})\\
C_2\ \text{XOR 封闭?} & \textbf{否} ⟹ \text{非线性 ✓}\\
\mathfrak B_1(C_2)=\mathbb F_2^{15}? & \textbf{否} ✗\ \Longrightarrow C_2\ \text{非完美}\\
\mathfrak B_1(C)=\mathbb F_2^{16}? & \textbf{否} ✗\ \Longrightarrow C\ \text{非 1-覆盖}\\
|Z|, \text{伙伴对} & 6080,\ 3520\ \ (\ne M=4096,\ \ne M/2\ \text{——与覆盖失败一致 ✓})\\
\nu & \{1:1152,\ 2:2368\};\ \textbf{重量-2 差集 30 个、无公共坐标 ✗}\\
\end{array}$$
$$\textbf{判读 ✓}:\ \text{覆盖失败 ⟹ 对象非法 ⟹ }\nu\ \text{的"非星"结论\textbf{无数学意义} ✗\ \text{（已按纪律\textbf{不予采信} ✓）}$$
$$
$$
```

---

## §2 导出条件的证明骨架（**✓**）

```
$$\text{覆盖 }=\ \text{对任意 }(a,b)\in\mathbb F_2^{11}\times\mathbb F_2^4:\ \exists u\in\mathfrak B_1(a),\ d_H(\psi(u),b)\le1-|u-a|\ ✓\ \text{（}u=a\ \text{或 }u=a+e_j\ ✓\text{）}$$
$$\qquad\Longrightarrow\ \text{条件}:\ \mathfrak B_1(\psi(a))\ \cup\ \{\psi(a+e_j)\}_j=\mathbb F_2^4\ ✓;\ \text{而 }|\mathfrak B_1(\psi(a))|=5,\ |\{\psi(a+e_j)\}|=11,\ 5+11=16 ✓$$
$$\qquad\Longrightarrow\ \text{等价于}\ \{\psi(a+e_j)\}\cap\mathfrak B_1(\psi(a))=\varnothing\ \text{且内部互异} \iff \{\psi(a+e_j)\oplus\psi(a)\}=W_2\ ✓✓\ \text{（因为 }|\mathbb F_2^4\setminus\mathfrak B_1(0)|=11\ \text{且 }=W_2\ ✓\text{）}$$
$$\text{尺寸 }2048\cdot16=32768=|\mathbb F_2^{15}|\ \Longrightarrow\ \text{覆盖 +\ 计数 ⟹ 球恰好铺砌 ⟹ 最小距离 }\ge3\ ✓\ \text{（无需逐对 ✓）}$$
$$
$$
```

---

## §3 纪律要点（**✓ 本档最有价值的方法论产出**）

```
$$\boxed{\text{"非线性构造"}\ \textbf{不等于}\ \text{"valid NP1CC"};\ \text{必须先过覆盖检验，}\nu\ \text{的结论才被采信}} ✓✓$$
$$\qquad\text{本轮实证 ✓}:\ \text{一个"看起来 Type C + 非线性"的对象（}|C_1\cap C_2|=1088\ ✓\text{）竟然\textbf{不是覆盖码} ✗;\ \text{其 }\nu\ \text{呈现"非星"} ✗\ \text{——若草率采信会\textbf{伪造一个 P2 collision} ✗✗}$$
$$\qquad\text{这与唐先生设定的判停条件完全一致 ✓}:\ \text{先验证完美覆盖，再跑 }\nu\ ✓;\ \text{且必须"独立确认是 NP1CC" ✓}$$
$$
$$
```

---

## §4 下一步（**✓**）

```
$$\text{(甲) 解导出条件 }\forall a:\{\psi(a+e_j)\oplus\psi(a)\}=W_2\ ✓\ \text{（非线性解存在 ⟹ Vasil'ev 型 ✓）};\ \text{可行手法}:\ \text{(i) 用已知 Vasil'ev 递归（长 7 → 长 15 ✓）；\ (ii) 或按局部条件做定向搜索（每步只需维持 }W_2\ \text{置换 ✓）}$$
$$\qquad\Longrightarrow\ \text{一旦得到 \textbf{覆盖核验通过的非线性完美码}} \Longrightarrow \text{再组装 NP1CC} \Longrightarrow \text{跑已就绪的 }\nu\ \text{工具} \Longrightarrow \textbf{E3 才有效} ✓$$
$$\text{(乙) 或转向 ENP1CC puncturing（论文 open problem ✓，另一条族外入口 ✓）}$$
$$\text{119}:\ \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：系统形式完美码的导出判定条件（$W_2$ 置换条件 ✓）、首次尝试失败与纪律要点
- **档案已有（引用，不列为提出）**：A-P2A-1、内蕴 $\nu$ 工具、Theorem 13、$W_2$、覆盖检验


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 导出判定条件 命中文件数=1    :: ./P2-A-STEP1-2026-09-27-failed-attempt-and-the-derived-perfect-code-condition.md 
技术词 纪律要点     命中文件数=1    :: ./P2-A-STEP1-2026-09-27-failed-attempt-and-the-derived-perfect-code-condition.md
```
- **本档新增**：系统形式完美码的导出判定条件（$W_2$ 置换条件）、首次尝试失败与纪律要点（见上方命中数；0 命中者为自造语／内部标签 ✓）
