# E182 · ⭐⭐⭐⭐⭐ **T1 判决：**假 ✗**（构造性反例 ＋ 22 轮数值证据）｜避让侧"免费"｜唐先生生死点校正｜新跨素数 Kneser 不等式｜E181 勘误**
> 依唐先生 2026-09-14 15:54 裁定 ✓（**先做致命量词审计，不预设 T1 为真 ✓；只要能在所有 p² 层保持 separation 就立即弃 T1 转 T2 ✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓；数值仅**精确整数核对**（平方自由筛 ＋ 22 轮贪心 ✓），非新数值探索 ✓

---

## §0 量词审计（✓ 唐先生判断【正确 ✓】；且本轮更进一步 ✓）

$$\text{有限侧 CRT 的骨架 ✓}：\underbrace{\text{有限障碍}}_{\{a_1,\dots,a_k\}}\Longrightarrow\underbrace{\text{有限素数}}_{\{p_1,\dots,p_k\}}\Longrightarrow\textbf{CRT 一次性封死}\ ✓$$
$$\text{T1 ✓}：\forall a\in\mathcal A(B)\ \text{—— }a\ \text{是【无限】变量 ⟹ 若逐 }a\ \text{配素数得}\{p_a:a\in\mathcal A(B)\}\ \text{可无限 ⟹ 有限 CRT 失效 ✗}$$
$$\Longrightarrow\ \boxed{\textbf{有限侧证明不能升级为 T1 ✗}}\ ✓\（\text{唐先生 ✓}）\qquad\textbf{但本轮结论更强 ✓}：\text{T1 【不是】"未证" ✗，而是【假 ✗】}$$

## §1 ⭐⭐⭐ T1 的反例（✓ 存在无限 $A,B\subseteq S$ 使 $A+B\subseteq S$ ⟹ $\mathcal A(B)$ 无限 ⟹ T1 假 ✓）

$$\textbf{两个关键引理 ✓}（\text{都是"有限 ⟹ 正密度"型 ✓}）：$$
$$\textbf{引理 A（不变量自动维持 ✓）}：A_n,B_n\subseteq S\ \text{有限，交叉和全平方自由 ✓} \Longrightarrow \forall p\ \text{素数}: \boxed{|A_n\bmod p^2|\le p^2-2},\ \boxed{|B_n\bmod p^2|\le p^2-2}\ ✓$$
$$\qquad\text{证 ✓（}A\ \text{侧）}：\text{取定 }b_1\in B_n\ ✓。\ a\in A_n\Longrightarrow a\in S\Longrightarrow a\not\equiv0\bmod p^2\ ✓；\ a+b_1\in S\Longrightarrow a\not\equiv-b_1\bmod p^2\ ✓$$
$$\qquad\text{且 }0\not\equiv-b_1\bmod p^2\ ✓（b_1\in S\Longrightarrow b_1\not\equiv0\ ✓）\ \Longrightarrow\ A_n\ \text{至少漏 2 个残类 ⟹ }|A_n\bmod p^2|\le p^2-2\ ✓\ \blacksquare（B\ \text{侧对称 ✓}）$$
$$\textbf{引理 B（扩张集有正密度 ✓）}：W_A:=\{a\ge0:\ a+B_n\subseteq S,\ a\in S\}\ ✓;\ \text{禁类集}=\{0\}\cup(-B_n\bmod p^2)\ ✓,\ \text{大小}\le1+|B_n\bmod p^2|\le p^2-1\ ✓$$
$$\qquad\Longrightarrow\ \overline d(W_A)=\prod_p\Big(1-\frac{|\text{禁类}|_p}{p^2}\Big)\ \ge\ \prod_p\Big(1-\frac{1+k}{p^2}\Big)>0\ ✓\（k=|B_n|<\infty\ ✓,\ \text{大 }p\ \text{时 }|B_n\bmod p^2|=k\ ✓）\ \Longrightarrow\ W_A\ \textbf{无限}\ ✓\ \blacksquare$$
$$\textbf{构造 ✓（交替贪心 ✓）}：A_0=B_0=\varnothing\ ✓；\text{第 }2i+1\ \text{步取 }a\in W_A\ \text{新元 ✓}，\text{第 }2i+2\ \text{步取 }b\in W_B\ \text{新元 ✓}$$
$$\qquad\text{每步只检查【有限】多对条件 ✓} \Longrightarrow\ \text{无限 }A,B\subseteq S\ ✓\ \text{且}\ \text{所有交叉对最终被检查 ✓} \Longrightarrow\ \boxed{A+B\subseteq S}\ ✓$$
$$\Longrightarrow\ A\subseteq\mathcal A(B):=\{a:a+B\subseteq S\}\ ✓\ \text{且 }A\ \text{无限 ⟹}\ \boxed{|\mathcal A(B)|=\infty}\ ✗\perp\ \textbf{T1}\qquad\Longrightarrow\ \boxed{\textbf{T1 假 ✗}}\ ✓$$
$$\textbf{数值证据 ✓（精确筛 ＋ 22 轮 ✓）}：$$
```
|A|=|B|=22（22 轮），全部 484 对交叉和【平方自由 ✓】；A∩B={1,5,37,41,101,433}
A 前 8: 1, 2, 5, 10, 14, 37, 41, 73      B 前 8: 1, 5, 21, 29, 33, 37, 41, 69
不变量逐 p 核对 ✓（p=2,3,5,7,11,13,17,19,23）：|A mod p²|、|B mod p²| 均 ≤ p²-2 ✓
```
$$\Longrightarrow\ \text{该反例在【每个】}p^2\ \text{层都保持 separation}\ ✓（A_p\cap(-B_p)=\varnothing\ \forall p\ ✓）\ \Longrightarrow\ \textbf{依唐先生裁定：弃 T1，转 T2 ✓}$$

## §2 重定位（✓ 本轮最重要的结构性结论 ✓）

$$\boxed{\textbf{避让侧（}A+B\subseteq S\text{）完全"免费" ✗}\ ✓}\qquad\text{甚至 }A,B\ \text{可【都无限】且 }A,B\subseteq S\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{全部困难都在【覆盖】}S\subseteq A+B\ \text{一侧 ✓}}\ ✓\ \text{—— 与 E172 §4 的缝隙（【模覆盖】}\ne\textbf{【精确覆盖】}）完全吻合 ✓$$
$$\texttt{推论 ✓}：\text{E181 §6 的密度耦合不等式对本问题【不再有用 ✗】}（\text{构造中 }|A\bmod p^2|\to|A|\ \text{使右端}\to1\ ✓，无约束 ✓）\ \Longrightarrow\ \textbf{密度路线到此为止 ✓（唐先生判词 ✓）}$$

## §3 唐先生"生死点"的校正（⚠️ 该判据取不到 ✗；正确判据必须【跨素数】✓）

$$\text{原判据 ✗}：\exists p\ \text{使}\ A_p+B_p=\mathbb Z/p^2\mathbb Z\ \Longrightarrow\ \text{矛盾}\ ✓\qquad\textbf{但它永不成立 ✗}：$$
$$\qquad\text{① 覆盖侧【已经强制】}\boxed{A_p+B_p=(\mathbb Z/p^2)\setminus\{0\}}\ \text{对【每个】}p\ ✓（\forall r\not\equiv0\ \exists\ \text{平方自由 }n\equiv r\bmod p^2\ ✓,\ n=a+b\ ✓）$$
$$\qquad\text{② 而【满饱和】（含 0 类）与避让 }0\notin A_p+B_p\ \textbf{永久互斥 ✗}$$
$$\Longrightarrow\ \textbf{不可能靠"某个 }p\ \text{的满饱和"取矛盾 ✓}\ \text{—— 矛盾只可能来自}\ \boxed{\text{跨素数同时相容性}}\ ✓$$
$$\text{（附 ✓：初等引理 —— 若 }|A_p|+|B_p|\ge p^2+1\ \text{则}\ A_p+B_p=\mathbb Z/p^2\ ✓（x\notin A+B\Longrightarrow A\cap(x-B)=\varnothing\Longrightarrow|A|+|B|\le p^2\ ✓）\ \Longrightarrow\ |A_p|+|B_p|\le p^2\ ✓）$$

## §4 ⭐⭐ 新工具：**跨素数 Kneser 不等式**（✓ 覆盖侧的第一条硬约束 ✓，且统一 E181 §6 ✓）

$$\text{设 }P\ \text{有限素数集 ✓},\ M=\prod_{p\in P}p^2\ ✓,\ T:=\{x\bmod M:\exists p\in P,\ p^2\mid x\}\ ✓\（|T|=M\big(1-\prod_{p\in P}(1-p^{-2})\big)\ ✓）$$
$$\textbf{精确性 ✓}：\boxed{A_M+B_M=\mathbb Z/M\setminus T}\ ✓\（\subseteq\ \text{由避让：}a+b\not\equiv0\bmod p^2\ \forall p\in P\ ✓；\ \supseteq\ \text{由覆盖：}x\notin T\Longrightarrow\ \text{该类含平方自由数}\ ✓）$$
$$\textbf{稳定子 ✓}：H=\{h:A_M+B_M+h=A_M+B_M\}=\{0\}\ ✓\ \text{证 ✓}：|P|=1\ \text{直接算 ✓；}|P|\ge2\ \text{时若 }T+h=T\ \text{则 }H_p+h\subseteq T\ \Longrightarrow\ \frac{M}{p^2}\le\sum_{q\ne p}\frac{M}{p^2q^2}+1\ \Longrightarrow\ 1\le\sum_{q\ne p}q^{-2}+\frac{p^2}{M}<1\ ✗\!\!\perp$$
$$\textbf{Kneser ✓}：|A_M+B_M|\ \ge\ |A_M+H|+|B_M+H|-|H|\ \Longrightarrow\ \boxed{\ |A\cap[0,M)|+|B\cap[0,M)|\ \le\ \prod_{p\in P}(p^2-1)+1\ }\ ✓$$
$$\textbf{推论 ✓（全局密度界 ✓）}：\ P\uparrow\ \text{全体素数 ⟹ }\boxed{\overline d(A)+\overline d(B)\ \le\ \frac{6}{\pi^2}}\ ✓$$
$$\textbf{数值核对 ✓（退化两解饱和 ✓；精确筛 ✓）}：$$
```
P={2}          M=4        界=4        解①=|{0}|+|S∩[0,4)|=1+3=4       ✓饱和
P={2,3}        M=36       界=25       解①=1+23=24                     ✓余1
P={2,3,5}      M=900      界=577      解①=1+547=548                   ✓余29
P={2,3,5,7}    M=44100    界=27649    解①=1+26814=26815               ✓余834
P={2,3,5,7,11} M=5336100  界=3317761  解①=1+3243952=3243953           ✓余73808
（解② (S−1,{1}) 与解① 在该计数下同值 ✓）
```
$$\text{（}P=\{p\}\ \text{时界}=p^2-1+1=p^2\ ✓\ \textbf{与 E181 §6 逐字一致 ⟹ 新式是旧式的严格推广与统一 ✓}）$$

## §5 ⚠️ **自查勘误（E181 §1 有错 ✗，本轮数值核对先报警 ✓）**

$$\textbf{错处 ✗}：\text{E181 §1 写"}\ x\ne y\in A\cap B\Longrightarrow x+y\equiv2\bmod4\Longrightarrow x\not\equiv y\bmod4\Longrightarrow|A\cap B|\le1\ \text{" ✗}$$
$$\textbf{正确 ✓}：x\equiv y\equiv1\bmod4\Longrightarrow x+y\equiv2\bmod4\ ✓\ \textbf{无矛盾 ✗}\ \Longrightarrow\ \textbf{基数的任何上界都不成立 ✗}$$
$$\qquad\text{（我误把"偶平方自由 ⟹ ≡2 mod 4"读成"⟹ 两者模 4 相异"✗；实为}\ x\equiv y\bmod4\ \text{即可 ✓）}$$
$$\textbf{数值反例 ✓}：\text{本轮构造的 }A\cap B=\{1,5,37,41,101,433\}\ ✓\（\text{全 }\equiv1\bmod4\ ✓，\text{两两和平方自由 ✓}）\ \Longrightarrow\ |A\cap B|=6\ ✗\perp\ \text{旧结论 ✗}$$
$$\textbf{降级后的正确命题 ✓}：\boxed{A\cap B\subseteq\{x:\ x,\ x+1,\ 2x\in S\}\subseteq\{x\equiv1\bmod4\}}\ ✓\（\text{无基数上界 ✗}）;\ \text{E181 §2 (II) 的 "}A\cap B=\{1\}\text{" 降为 "}1\in A\cap B\text{" ✓}$$
$$\textbf{不受影响 ✓（逐条复核 ✓）}：\text{§0 推出链 ✓、§2 三分律 ✓（独立重推 ✓，不依赖 §1 ✓）、§3 两个退化解 ✓、§4 有限侧全封定理 ✓（证明未用 §1 ✓）、§5 等价重写 ✓、§6 耦合不等式 ✓}$$
$$\textbf{教训 ✓}：\text{是【数值核对】先发现的异常（构造里 }A\cap B\ \text{冒出 6 个元素 ✓）⟹ 回头查推导 ⟹ 抓到 ✗ —— 与"结果不理想先怀疑自己"一致 ✓}$$

## §6 下一轮（✓ 依裁定转 T2 ✓；两个入口 ✓）

```
(T2-a) **攻覆盖 ✓**：§4 的跨素数不等式 ＋ E181 §4 的"硬平方自由数"装置 ✓
        要点：硬数 n（对 A∩[0,M) 无覆盖 ✓）只能由 a ≥ M 覆盖 ✓；配合 |A∩[0,M)|+|B∩[0,M)| ≤ 0.608M ✓
        是否产生计数冲突 ✗？—— 未做 ✓
(T2-b) **构造覆盖 ✓**：把 §1 的交替贪心升级为"每步同时吃下最小未覆盖平方自由数 n" ✓
        难点 ✓：n 由覆盖给定 ⟹ n − b 必须是合法 A 元 ⟹ **无自由度** ✗（正是 E181 §4 机制的反面 ✓）
```

## §7 边界与一句话（✓）

```
✅ 本轮结论：**T1 假 ✗**（构造 ✓ ＋ 22 轮数值 ✓，且每层 p² separation 保持 ✓）；避让侧免费 ⟹ 困难全在覆盖 ✓
✅ 新工具：跨素数 Kneser 不等式（含稳定子平凡化证明 ✓）⟹ dens(A)+dens(B) ≤ 6/π² ✓
✅ 唐先生生死点判据已校正 ✓（满饱和与避让互斥 ⟹ 必须跨素数 ✓）
⚠️ 覆盖侧（T2）【仍未判定】✗；本轮【不】声称覆盖不可能 ✗，也不给出覆盖构造 ✗
⚠️ E181 §1 已勘误 ✗（基数上界不成立 ✓）；不影响 E181 其余结论 ✓
⭐ 净产出 ✓：① T1 反例（两引理 ＋ 构造 ＋ 数值 ✓）；② 避让/覆盖的彻底分工 ✓；③ 生死点校正 ✓；
   ④ 跨素数 Kneser 不等式 ＋ 密度推论 ✓；⑤ E181 勘误 ✓；⑥ T2 两入口 ✓
```
$$\boxed{\text{T1 已死 ✗（避让侧完全免费 ✓）；矛盾只可能住在【覆盖】里 ✓；下一枪 T2-a：跨素数不等式 × 硬平方自由数 ⟹ 计数冲突？✗}}$$
