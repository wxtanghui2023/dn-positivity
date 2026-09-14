# E181 · ⭐⭐⭐⭐⭐ **无限双集合问题首轮判定：有限侧【全封 ✗】＝ 新机制实例 ＋ mod 4 三分律 ＋ 两个退化解**
> 依唐先生 2026-09-14 15:28 裁定的下一轮对象 ✓（E180 §5 ⑥ 待重核项一并落实 ✓）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓；仅一处**精确整数核对**（平方自由判定，≤5000 ✓，非新数值探索 ✓）

---

## §0 口径与推出链（✓ 全部由【覆盖侧】强制 ✓；与 E179 §0 的"恰一个含 0"一致 ✓）

$$\text{口径 ✓}：S=\text{平方自由正整数}\ ✓\Longrightarrow\ \boxed{0\notin S}\ ✓（E179 §0 已立 ✓）\quad A,B\subseteq\mathbb N_0\ ✓,\quad \boxed{A+B=S}\ ✓$$
$$\textbf{第一步 ✓}：0\in S\ ✗\ \text{且}\ S\subseteq A+B\ \Longrightarrow\ \textbf{【恰一个】含 }0\ ✓（\text{两者皆含}\Longrightarrow 0=0+0\in A+B\ ✗）\quad\text{取}\ \boxed{0\in A,\ 0\notin B}\ ✓$$
$$\textbf{第二步 ✓}：1\in S\subseteq A+B\ \Longrightarrow\ 1=a+b\ \text{仅两种分解}\ (0,1)\ \text{或}\ (1,0)\ ✓；\text{又}\ 0\notin B\ \Longrightarrow\ \boxed{1\in B}\ ✓$$
$$\Longrightarrow\ \boxed{\text{(L1)}\ B\subseteq S}\ ✓\quad(\forall b\in B:\ b=0+b\in A+B\subseteq S\ ✓);\qquad \boxed{\text{(L2)}\ A+1\subseteq S}\ ✓\quad(\forall a\in A:\ a+1\in A+B\subseteq S\ ✓)$$
$$\textbf{对照 ✓}：\text{(L1)(L2) 正是 }AUDIT\ \S L4\ \text{的两条全局条件}\ ✓（B_p\cap\{0\}=\varnothing\ \forall p\ \text{与}\ A_p\cap\{-1\}=\varnothing\ \forall p\ ✓）\ \Longrightarrow\ \textbf{审计中"当作假设"的两条，在此【被覆盖侧推出 ✓】}$$
$$\qquad\text{（对偶方向 ✓}：\text{若取 }0\in B\ \text{（则 }1\in A\text{）}\ \Longrightarrow\ A\subseteq S,\ B+1\subseteq S\ ✓\ \text{—— E179 的"B\subseteq S-1"即此方向 ✓；下文固定 }0\in A\ ✓）$$

## §1 ⭐ 刚性：$A\cap B$ 至多一个元素，且必 $\equiv1\bmod4$（✓ 新 ✓）

$$x\in A\cap B\ \Longrightarrow\ \underbrace{x\in S}_{(0\in A)},\ \underbrace{x+1\in S}_{(1\in B)},\ \underbrace{2x\in S}_{x\in A,\ x\in B}\ ✓\ \Longrightarrow\ x+1\ \text{偶且平方自由}\ \Longrightarrow\ x+1\equiv2\bmod4\ \Longrightarrow\ \boxed{x\equiv1\bmod4}\ ✓$$
$$x\ne y\in A\cap B\ \Longrightarrow\ x+y\in A+B\subseteq S\ ✓\ \text{且偶}\ \Longrightarrow\ x+y\equiv2\bmod4\ \Longrightarrow\ x\not\equiv y\bmod4\ ✗\!\!\perp$$
$$\Longrightarrow\ \boxed{\big|A\cap B\big|\le1}\ ✓,\qquad \boxed{A\cap B\subseteq\{x\equiv1\!\!\pmod 4\}}\ ✓$$
$$\text{（对 E180 §1 的加强 ✓}：\text{E180 得 }A\cap B\subseteq\{x:2x\in S\}\ ✓；\text{此处再叠 }x,\ x+1\in S\ \text{两个强制条件 ⟹ 模 4 类锁定 ✓）$$

## §2 ⭐ mod 4 三分律（✓ 穷举 ✓，恰三种，无第四种 ✓）

$$\textbf{可用条件 ✓}：(a)\ \alpha:=A\bmod4\subseteq\{0,1,2\}\ \text{且}\ 0\in\alpha\ ✓\ [\text{由 (L2)}:\ a+1\ \text{平方自由}\Longrightarrow a\not\equiv3\bmod4\ ✓]$$
$$\qquad(b)\ \beta:=B\bmod4\subseteq\{1,2,3\}\ \text{且}\ 1\in\beta\ ✓\ [\text{由 (L1)}:\ b\ \text{平方自由}\Longrightarrow b\not\equiv0\bmod4\ ✓]$$
$$\qquad(c)\ \text{避让 ✓}：\alpha\cap(-\beta)=\varnothing\ ✓\qquad (d)\ \text{覆盖 ✓}：1,2,3\in S\ \text{的分解}\ \Longrightarrow\ \alpha+\beta\supseteq\{1,2,3\}\ ✓$$
$$\textbf{穷举 ✓}：\alpha\in\{\{0\},\{0,1\},\{0,2\},\{0,1,2\}\}\ \text{（四种，全部验过 ✓）}$$

| $\alpha=A\bmod4$ | 可行 $\beta$ | 判定 |
|:--|:--|:--|
| $\{0\}$ | $\beta=\{1,2,3\}$ ✓（$\alpha\cap(-\beta)=\{0\}\cap\{3,2,1\}=\varnothing$ ✓） | ✅ **构型 (I)** |
| $\{0,1\}$ | $3\notin\beta$ ⟹ $\beta\subseteq\{1,2\}$；$\beta=\{1\}$ 给 $\{1,2\}\not\ni3$ ✗ ⟹ $\beta=\{1,2\}$ ✓ | ✅ **构型 (II)** |
| $\{0,2\}$ | $-\alpha=\{0,2\}$ ⟹ $\beta\subseteq\{1,3\}$；$\beta=\{1\}$ 给 $\{1,3\}$ ✗、$\{1,3\}$ 给 $\{1,3\}$ ✗ | ❌ 排除 |
| $\{0,1,2\}$ | $-\alpha=\{0,3,2\}$ ⟹ $\beta\subseteq\{1\}$ ⟹ $\beta=\{1\}$，$\alpha+\beta=\{1,2,3\}$ ✓ | ✅ **构型 (III)** |

$$\Longrightarrow\ \boxed{\textbf{恰三种构型}}\ ✓\qquad\textbf{强制小元 ✓}：$$
$$\text{(I)}\ A\subseteq4\mathbb Z\ ✓,\ 1,2,3\notin A\ ✓,\ \{2,3\}\subseteq B\ ✓\ [2=a+b,\ a\in A,\ a\le2\Longrightarrow a=0\ ✓]\ \Longrightarrow\ \boxed{A\cap B=\varnothing}\ ✓$$
$$\text{(II)}\ 1\in A\cap B=\boxed{\{1\}}\ ✓,\ 2\in B\ ✓,\ 2\notin A\ ✓\ [\alpha\not\ni2\ ✓]\quad\text{（由 }3=2+1\ \text{或}\ 1+2\ \text{且}\ 2\notin A\ ✓）$$
$$\text{(III)}\ B\subseteq\{b\equiv1\!\!\pmod4\}\ ✓,\ \boxed{2\in A}\ ✓\ [3=a+b,\ b\in B,\ b\le3,\ b\equiv1\!\!\pmod4\Longrightarrow b=1\ ✓],\ 1\notin A\ \text{不强制 ✓}$$

## §3 ⭐⭐ 两个**退化解**（✓ 恰落在 (I) 与 (III) ✓；数值核对 ✓ $n\le200$ 全通过 ✓）

$$\textbf{解①（落 (I) ✓，}|A|=1\text{）}：\boxed{A=\{0\},\ B=S}\ ✓\qquad A+B=S\subseteq S\ ✓;\ \ S\subseteq 0+S=S\ ✓;\ \ \alpha=\{0\},\ \beta=S\bmod4=\{1,2,3\}\ ✓$$
$$\textbf{解②（落 (III) ✓，}|B|=1\text{）}：\boxed{A=S-1:=\{s-1:s\in S\},\ B=\{1\}}\ ✓\qquad A+B=(S-1)+1=S\ ✓\ \text{两个包含方向均成立 ✓}$$
$$\qquad\qquad A\bmod4=\{0,1,2\}\ ✓\（0=1-1,\ 1=2-1,\ 2=3-1\ ✓）,\quad B\bmod4=\{1\}\ ✓\ \Longrightarrow\ \textbf{与构型 (III) 逐条吻合 ✓}$$
$$\Longrightarrow\ \textbf{存在性 ✓}：\text{【非退化】只需一侧单点即已给出两个显式解 ✓}\ \Longrightarrow\ \textbf{构型 (I)(III) 都真实被实现 ✓；构型 (II) 【无】单点见证 ✓}$$

## §4 ⭐⭐⭐⭐ **新定理：有限侧全封 ✗**（→ E180 §5 ⑥ 与 §3 的升级 ✓）

$$\boxed{\textbf{定理 ✓}：\text{若}\ 2\le|A|<\infty\ \text{或}\ 2\le|B|<\infty\ ✓，\text{则}\ \textbf{无解}\ ✗（\text{即}\ A+B=S\ \text{不可能}）}\ ✓$$
$$\textbf{证明（}A\ \text{侧 ✓）}：\text{记}\ A=\{a_0=0,a_1,\dots,a_k\}\ (k\ge1)\ ✓,\quad X:=\bigcap_{a\in A}(S-a)\ ✓$$
$$\qquad(1)\ \text{避让 ✓}：b\in B\Longrightarrow b+a\in S\ \forall a\in A\Longrightarrow \boxed{B\subseteq X}\ ✓$$
$$\qquad(2)\ \text{覆盖 ✓}：n\in S\Longrightarrow n=a_i+b\ (b\in B\subseteq X)\ \Longrightarrow\ \boxed{n-a_i\in X}\ ✓\ \text{对某个 }i\ ✓$$
$$\qquad(3)\ \text{硬数构造 ✓}：\text{每 }i\ \text{取 }j(i)\ne i\ ✓,\ e_i:=a_{j(i)}-a_i\ne0\ ✓；\text{取互异素数 }p_i\nmid e_i\ ✓；\text{CRT}：n\equiv-e_i\bmod p_i^2\ (\forall i)\ ✓$$
$$\qquad\qquad\Longrightarrow\ n+e_i\equiv0\bmod p_i^2\ \Longrightarrow\ (n-a_i)+a_{j(i)}\notin S\ \Longrightarrow\ \boxed{n-a_i\notin X\supseteq B}\ ✓\ \Longrightarrow\ n-a_i\notin B\ \ \forall i\ ✓$$
$$\qquad(4)\ n\ \text{可取为【平方自由】✓}：\text{模 }P^2=\prod_ip_i^2\ \text{的该类中平方自由数有正密度 ✓（}#\ \prod_{q\nmid P}(1-q^{-2})\ \text{校正}\ ✓\text{，且}p_i^2\nmid n\ \text{由 }p_i\nmid e_i\ \text{保证 ✓）}$$
$$\qquad(5)\ \text{于是 }n\in S\ \text{但 }n\notin A+B\ ✓（\text{任何表示 }n=a_i+(n-a_i)\ \text{都要求 }n-a_i\in B\ ✗）\ \Longrightarrow\ \text{与 }S\subseteq A+B\ ✗\!\!\perp\ \blacksquare$$
$$\text{（}B\ \text{侧对称 ✓，只需交换 }A\leftrightarrow B\ \text{并把基点换成 }b_0=1\ ✓）\quad\textbf{例外 ✓}：|A|=1\Longrightarrow A=\{0\}\ ✓\ \text{即解① ✓；}|B|=1\Longrightarrow B=\{1\}\ ✓\ \text{即解② ✓}$$
$$\textbf{精确数值见证 ✓（CRT 机制的显式最小反例，}A=\{0,d\}\text{ 型 ✓）}：$$
```
d=1→17 (16,18 非自由) ｜ d=2→6 (4,8) ｜ d=3→15 (12,18) ｜ d=4→94 (90,98) ｜ d=5→13 (8,18) ｜ d=6→10 (4,16)
d=7→11 (4,18) ｜ d=8→17 (9,25) ｜ d=9→41 (32,50) ｜ d=10→14 (4,24) ｜ d=11→29 (18,40) ｜ d=12→37 (25,49)
```
$$\qquad\Longrightarrow\ \text{与 E179 手算的 }n=17\ (d=1)\ \textbf{逐字吻合 ✓}；\text{每个 }d\ \text{都给出反例 ⟹ 有限侧无逃生口 ✓}$$

## §5 三种等价重写（✓ 供下一轮选用 ✓）

$$\textbf{(甲) 闭点 ✓}：A\subseteq\mathcal A(B),\ B\subseteq\mathcal B(A)\ ✓\ \text{且可【无损放大】到}\ \boxed{A=\mathcal A(B),\ B=\mathcal B(A)}\ ✓（\text{单调性：放大只增强覆盖 ✓）$$
$$\textbf{(乙) 平移覆盖 ✓}：\boxed{S=\bigcup_{a\in A}(B+a)}\ ✓\qquad\textbf{(丙) }X\text{-形式 ✓}：X:=\bigcap_{a\in A}(S-a)\supseteq B\ ✓,\qquad \boxed{S\subseteq X\cup(X+A')}\ ✓,\ A'=A\setminus\{0\}\ ✓$$
$$\qquad\text{（乙）把问题变成"用 }B\ \text{的平移铺满 }S\ \text{"；（丙）把覆盖拆成"已在 }X\ \text{内"与"由 }A\ \text{平移补齐"两段 ✓}$$

## §6 耦合不等式（✓ 新 ✓；且说明**为何不闭合** ✓，与 E171/E172 一致 ✓）

$$\forall p\ \text{素数}\ ✓:\quad \boxed{\overline d(B)\le1-\frac{|A\bmod p^2|}{p^2}}\ ✓\quad(\text{因 }b\in B\Longrightarrow b\not\equiv-a\bmod p^2\ \forall a\in A\ ✓,\ \text{禁 }|A\bmod p^2|\ \text{个类}\ ✓)$$
$$\qquad\text{对偶 ✓}：\overline d(A)\le1-|B\bmod p^2|/p^2\ ✓；\quad\text{另 ✓}：\big|A\cap[0,p^2)\big|+\big|B\cap[0,p^2)\big|\le p^2\ ✓\（\text{同余类互异 ＋ 互补 ✓}）$$
$$\textbf{为何不足 ✗}：\text{当 }A\ \text{在 }p^2\ \text{尺度上稀疏（}|A\bmod p^2|=o(p^2)|）\ \text{时右端}\to1\ \Longrightarrow\ \text{无约束 ✗}；\text{反之 }A\ \text{局部富 ⟹ }B\ \text{稀疏，但覆盖只需 }A(X)B(X)\gtrsim X\ ✓\ \text{仍相容 ✗}$$
$$\Longrightarrow\ \textbf{与 E171/E172 结论一致 ✓}：\text{局部／密度工具【原则上】看不到障碍 ✗ ⟹ 障碍仍住在【精确覆盖】这一侧 ✓}$$

## §7 判词与下一轮子目标（✓ 诚实边界 ✓）

```
✅ **已闭合 ✓**：① 推出链（恰一个含 0 → 1∈B → B⊆S、A+1⊆S ✓）；② |A∩B|≤1 且 ≡1 mod 4 ✓；
   ③ mod 4 三分律（恰三种 ✓，穷举 ✓）；④ 两个退化解显式给出 ✓（落 (I)(III) ✓）；⑤ ⭐ **有限侧全封 ✗**
   （2≤|A|<∞ 或 2≤|B|<∞ ⟹ 无解 ✓，CRT 硬数机制 ＋ 12 个 d 的显式最小反例 ✓）
⚠️ **仍 OPEN ✗**：**两侧都无限**的情形 —— 这【正是】E180 的目标问题 ✓，本轮【未】判定 ✓
⭐ **本轮的机制性收获 ✓**：有限侧是被【非局部机制】关闭的（CRT 造"硬平方自由数" n，n-a_i∉B ∀i ✓），
   **而非**四层局部工具 ⟹ 这是 E180 §5 ① 形态（"不可能 ⟹ 新机制"）的**第一个实例** ✓✓
🎯 **下一轮两个子目标 ✓（择一 ✓）**：
   (T1) 证明：B\subseteq S 无限 ⟹ \mathcal A(B)=\{a:a+B\subseteq S\} **有限** ✓
        （因 A\subseteq\mathcal A(B) ✓；若 (T1) 成立，则"A 无限"与"A 有限"同时为假 ⟹ **问题判为不可能 ✓**）
   (T2) 直接构造：两侧无限 —— 需同时满足 (甲) 闭点 ＋ (乙) 平移覆盖 ✓（构型 (II) 无单点见证 ✓，或为其唯一活口 ✓）
```

## §8 边界（✓）

```
✅ 新定理证明只用：恰一个含 0、避让（A+B⊆S）、覆盖（S⊆A+B）✓；未用 RH ✓、未涉 ζ ✓、未跑 Lean ✓
✅ 数值仅一处：平方自由判定枚举（≤5000，整数精确 ✓）用于 CRT 机制的显式见证 ✓
⚠️ 不声称无限侧不可能 ✗；不声称无限侧可能 ✗ —— **本轮对无限侧保持 OPEN ✓**
⚠️ 构型 (II) 与"无限解"的关系【未判定】✗（仅知它无单点见证 ✓）
⭐ 净产出 ✓：① 推出链 ＋ 刚性 ✓；② mod 4 三分律 ✓；③ 两个退化解 ✓；④ ⭐ 有限侧全封定理 ✓；
   ⑤ 三种等价重写 ✓；⑥ 耦合不等式及其失效说明 ✓；⑦ 下一轮 (T1)/(T2) ✓
```

## §9 一句话（✓）

$$\boxed{\text{有限侧【全封 ✗】（新 CRT 机制 ✓）；退化侧【两个显式解 ✓】；两侧无限 ⟹ 唯一活口，仍 OPEN ✓ —— 下一枪打 (T1)：无限 }B\Longrightarrow\mathcal A(B)\ \text{有限}\ ✗}$$
