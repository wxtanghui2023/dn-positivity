# AUDIT-2026-09-28ad — **$T{=}\triangle(G_2)$ 确认 ✓，但 $(E)$／$(F)$ \textbf{实测失效}（49/120）＋ 一处 $d_1$ 口径冲突**

> **性质**：**审计（实测）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:17 ✓
> **唐先生令**：把高阶路线推成可检验之局部不变量系统 ✓

**已查地图**：接续 `AUDIT-ac`（三矩恒等式）／`EXCESS-2026-09-25`（三球交表）✓

D0: 本档对象 ＝ **档案已有**（$G_2$／$q$／三矩恒等式——`EXCESS-2026-09-25` 与 `AUDIT-ac` 已载核心 ✓）
D1: 0（产出＝**一条新接口确认 ＋ 两处失效实测 ＋ 一处口径纠正** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 唐先生 (B) 成立}:\ \mathbf T=\Sigma_x\binom{a(x)}3=\triangle(G_2(C))\ \text{（实测 }138{=}138\text{）}}✓✓$$
$$\boxed{\text{② ✗ 口径纠正}:\ \Sigma_{c\in C}d_1(c)=2N_1\ \textbf{≠}\ \Sigma_x\delta(x);\ \text{故}"E{=}142\Rightarrow N_1{=}71"\ \textbf{不成立}}$$
$$\boxed{\text{③ ✗✗ 唐先生 (E)／(F) \textbf{实测失效}（120 码中 49 个违反）};\ (I)\ \text{成立}}$$

## §1 ✓ (B) 三角形接口确认（**本档最有价值之正面结果 ✓✓**）

$$T:=\sum_x\binom{a(x)}3;\qquad \triangle(G_2(C)):=\#\{\{c_1,c_2,c_3\}\subseteq C:\ \text{两两距离}\le2\}$$
$$\textbf{实测}:\ T=138,\ \triangle(G_2)=138\ \Longrightarrow\ \boxed{T=\triangle(G_2(C))}\ ✓✓$$
$$\text{几何理由（也已核）}:\ \text{三球交表仅 }(1,1,2)\text{-型}\Rightarrow1\ \text{与}\ (2,2,2)\Rightarrow1\ \text{非零};\ (1,2,2)\ \textbf{不可能}\ (\text{二进}: c_1{=}0,c_2{=}e_a,c_3\ \text{使 }d{=}(2,2)\ \text{无解})$$
$$\therefore\ \boxed{\Sigma_x\delta(x)^3\ =\ E\ +\ 6\,\triangle(G_2(C))}\quad(\text{三阶矩}\ \textbf{恰为 }G_2\ \text{之三角形数})$$

## §2 ✗ 口径冲突（**必须修正 ✓**）

$$\text{唐先生 §2／§10 用}\ \delta(c)=d_1(c)\ \text{并令}\ 2N_1=\sum_{c\in C}\delta(c)=\sum_x\delta(x)$$
$$\textbf{实测}:\ \sum_{c\in C}d_1(c)=2N_1=\mathbf{100}\qquad\text{vs}\qquad \sum_x\delta(x)=E=\mathbf{296}\ \Longrightarrow\ \textbf{不相等}\ ✗✗$$
$$\text{根源}:\ \delta(c)=d_1(c)\ \text{仅对\ \textbf{码字} }c\ \text{成立}\ (\text{因 }a(c)=1+d_1(c));\ \text{但}\ \sum_x\delta(x)\ \text{系对\ \textbf{全部 }1024\ \text{点求和}}$$
$$\therefore\ \boxed{E=142\ \text{只给}\ \sum_x\delta=142;\ \textbf{不}给\ N_1\Longrightarrow\ \text{唐先生之 }N_1{=}71\ \text{及由此得之 (G)(H) 皆不成立}}\ ✗$$

## §3 ✗✗ (E)／(F) 实测失效（**49/120 违反**）

$$\text{唐先生 §8 步骤}:\ A:=C\cap S_1(c),\ m(y):=|A\cap N(y)|,\ \text{并断言}\ d_2(c)=|\{y:m(y)\ge1\}|$$
$$\textbf{实测}:\ \text{(E)}\ d_2\le\min(9d_1,45)\ \text{违反 }\mathbf{49};\qquad\text{(F)}\ d_2+q\le9d_1\ \text{违反 }\mathbf{49};\qquad\text{(I)}\ q\le\binom{d_1}2\ \text{违反 }\mathbf{0}\ ✓$$
$$\text{诊断（错在何处）}:\ \sum_{y\in S_2(c)}m(y)=9s\ \text{确实成立} ⟹ \#\{y:m(y)\ge1\}\le9s\ ✓;\ \text{但\ \textbf{此非 }d_2(c)}$$
$$\qquad \#\{y\in S_2(c):m(y)\ge1\}=|N(A)\cap S_2(c)|\ \text{（被 }A\ \text{碰到之 }S_2\ \text{点）},\qquad d_2(c)=|C\cap S_2(c)|\ \text{（距离 2 之\ \textbf{码字}）}$$
$$\qquad \text{二者无包含关系}:\ y\in C\cap S_2(c)\ \text{不保证 }m(y)\ge1;\ m(y)\ge1\ \text{不保证 }y\in C\ ✗$$

## §4 可存活之资产（**重新清点 ✓**）

$$\checkmark\ \textbf{(B)}\ T=\triangle(G_2)\ \text{（新接口，实测）};\qquad \checkmark\ \textbf{(I)}\ 0\le q(c)\le\binom{d_1(c)}2\ \text{（实测 0 违反）}$$
$$\checkmark\ \Sigma_x\delta^3=E+6\,\triangle(G_2)\ \text{（恒等，源自 (B)）};\qquad \checkmark\ \text{三阶矩不能排除 }106\ (\text{唐先生 §6，}\textbf{正确} ✓:\ T{=}0\ \text{与 }E{=}142\ \text{相容})$$
$$\text{本轮实测数据}:\ \sum_c d_1(c)=100;\ \sum_c d_2(c)=298;\ \sum_c q(c)=4;\ \sum_c\binom{d_1(c)}2=41;\ \sum\delta^2=500$$

## §5 正确的下一步（**据实测诊断 ✓**）

$$\boxed{\text{需重建一个\ \textbf{正确}之局部不等式}:\ \text{形如}\ |C\cap S_2(c)|\ \le\ F(d_1(c),\text{局部构型})}$$
$$\text{且必须来自\ \textbf{覆盖要求}（非仅计数）};\ \text{唐先生原意（距离1结构与距离2结构耦合）方向正确} ✓\ \text{但需换械}$$
$$\therefore\ \text{仍归结到}\ \textbf{Zhang 1991 pair-covering inequality}\ \text{之类型}:\ \text{独立、非线性、且由覆盖逼出} ✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "口径冲突" "三角形接口" "局部界失效"
技术词 口径冲突   命中文件数=0    ::
技术词 三角形接口  命中文件数=0    ::
技术词 局部界失效  命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **本地实测**（120-code 全量）＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** Zhang／BÖW 公式 ✗；**不主张** $E\ge153$ 可得 ✗（V290）
