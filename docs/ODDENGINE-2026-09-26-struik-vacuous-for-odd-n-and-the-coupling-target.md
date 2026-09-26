已查地图：已跑 scripts/prework_map_check.sh Struik 空不等式 奇 n 耦合 ⟹ 执行自 PROPAGATION-2026-09-26 档；本档为**"奇 n 为何先天难"的结构性解释 ＋ 耦合目标的正名**（唐先生 2026-09-26 13:19 指令）；未跑 solver ✓。
D0: 本档对象 = Struik/van Wee 一阶局部不等式在奇 n 的空性，及其对"耦合不变量"方向的定位
D1: 1（新增：**局部过量覆盖奇偶引理**（OC ≡ n+1 mod 2）✓；**一阶机器仅对偶 n 有内容**的结构性结论 ✓）

# ODDENGINE-2026-09-26

## §1 本轮收口（唐先生定 ✓）

```
$$\textbf{新增资产}: \text{传播引理}\ ✓;\quad \textbf{确认资产}: \text{中点引理}\ ✓;\quad \textbf{淘汰}: \text{ladder/}\sigma\ ✗;\quad \textbf{无新全局障碍}\ ✗;\quad \textbf{119 UNKNOWN}\ ✓$$
$$\text{定位}: \textbf{局部 rigidity 已出现，global coupling 尚未出现}\ ✓$$
$$

## §2 ⭐ **核验结果：Struik 一阶不等式在奇 n 处为空** ✓✓

```
$$\text{Struik/van Wee 局部不等式}（R=1）:\ \mathrm{OC}(B_1(x))\ \ge\ 2\Bigl(\bigl\lceil\tfrac{n+1}{2}\bigr\rceil-\tfrac{n+1}{2}\Bigr)\ ✓$$
$$\qquad n\ \text{偶}:\ \lceil(n+1)/2\rceil=n/2+1\ \Longrightarrow\ \text{下界}=1\ ✓;\qquad n\ \text{奇}:\ \lceil(n+1)/2\rceil=(n+1)/2\ \Longrightarrow\ \textbf{下界}=0\ ✗$$
$$\textbf{数值核验（我方 ✓）}:$$
$$\quad n=4\ (\text{偶},\ K):\ \text{下界 }1\ ✓;\ \mathrm{OC}\ \text{分布}=\{1{:}480\}\ \Longrightarrow\ \textbf{取等、有内容}\ ✓✓$$
$$\quad n=6\ (\text{偶},\ K):\ \text{下界 }1\ ✓;\ \mathrm{OC}\ \text{分布}=\{1{:}2520,\ 3{:}840,\ 5{:}280\}\ \Longrightarrow\ \textbf{紧、有内容}\ ✓✓$$
$$\quad n=5\ (\text{奇},\ K):\ \text{下界 }0\ ✗;\ \mathrm{OC}\ \text{分布}=\{0{:}2880,\ 2{:}4800,\ 6{:}320\}\ \Longrightarrow\ \textbf{36\% 取 0 ⟹ 不等式空}\ ✗✓$$
$$

## §3 ⭐⭐ **结构根因：局部过量覆盖奇偶引理**（我方推导 ✓，与数据完全吻合 ✓✓）

```
$$\text{双计数}: \sum_{y\in B_1(x)}b(y)=\sum_c|B_1(x)\cap B_1(c)|=(n+1)[x\in C]+2\,d_1(x)+2\,d_2(x)\ ✓$$
$$\qquad\Longrightarrow\ \sum_{y\in B_1(x)}b(y)\equiv(n+1)[x\in C]\ (\mathrm{mod}\ 2)\ ✓$$
$$\Longrightarrow\ \mathrm{OC}(B_1(x))=\sum_{y\in B_1(x)}(b(y)-1)\equiv(n+1)([x\in C]-1)\ (\mathrm{mod}\ 2)\ ✓$$
$$\boxed{\text{对 }x\notin C:\quad \mathrm{OC}(B_1(x))\equiv n+1\ (\mathrm{mod}\ 2)}\ ✓✓$$
$$\qquad n\ \text{奇}\Longrightarrow n+1\ \text{偶}\Longrightarrow \mathrm{OC}\ \textbf{必为偶数}\ ✓\ (\text{故取值 }\in\{0,2,4,\dots\}\ ✓\ \text{—— 与实算 }\{0,2,6\}\ \textbf{完全一致}\ ✓✓)$$
$$\qquad n\ \text{偶}\Longrightarrow n+1\ \text{奇}\Longrightarrow \mathrm{OC}\ \textbf{必为奇数}\ ✓\ (\text{与实算 }\{1\}\ /\ \{1,3,5\}\ \textbf{完全一致}\ ✓✓)$$
$$\Longrightarrow\ \boxed{\text{对奇 }n,\ \text{下界 }0\ \text{在\textbf{奇偶上就是可达的}\ ✗\ ⟹\ \textbf{一阶不等式\textbf{原理上不可能}有内容}}\ ✓✓\ (\text{不是紧不紧的问题}\ ✓)$$
$$

## §4 结论：**标准 excess 机器只对偶 n 有内容** ✓✓

```
$$\textbf{van Wee 界}: \text{奇 }n\ \text{时修正项}=0\ \Longrightarrow\ \text{退化为\textbf{球覆盖平凡界}}\ ✓\ (\text{无改进}\ ✗)$$
$$\textbf{Struik 局部不等式}: \text{奇 }n\ \text{时为空}\ ✗\ (\text{§2--§3}\ ✓)$$
$$\textbf{Habsieger 同余}: \text{适用条件 }6\mid n\ ⟹ n\ \text{偶}\ ✓$$
$$\boxed{\Longrightarrow\ \textbf{已知下界机器（van Wee / Struik / Habsieger）在奇 }n\ \text{上\textbf{整体无内容}}\ ✓✓}$$
$$\text{这解释了}: \text{① 文献改进界为何都限定偶 }n\ \text{或 }6\mid n\ ✓;\ \text{② 我方偶 }n\ \text{侧为何一攻即通（NP1CC 定理}\ ✓);\ \text{③ 奇 }n\ \text{侧为何屡攻不下}\ ✓$$
$$

## §5 因此耦合目标被**正名** ✓（唐先生的判断得到结构性支持 ✓）

```
$$\text{唐先生提出}: \text{下一步应找\textbf{跨多个 midpoint / 多个 distance-2 对的耦合不变量}}\ ✓$$
$$\text{§4 给出理由}: \text{一阶（单球）信息在奇 }n\ \text{上原理性为空}\ ✗\ ⟹\ \textbf{必须用二阶（球对/点对）泛函}\ ✓✓\ —— \text{不是风格选择，是\textbf{原理必需}}\ ✓$$
$$\textbf{候选形式（待验 ✓）}: \text{① 球对泛函 }\sum_{x,y:\ d(x,y)=2}\mathrm{OC}(B_1(x))\,\mathrm{OC}(B_1(y))\ ✓;\ \text{② 二阶 Struik}: \text{对 }B_1(x)\cup B_1(y)\ \text{的过量覆盖}\ ✓$$
$$\qquad\text{③ 用中点结构（天然位于距离 2}\ ✓): \text{distance-2 对 ＋ 其中点 ＋ 传播引理}\ ✓\ \text{构成的局部计数}\ ✓$$
$$

## §6 生死测试的**精确化**（唐先生框架 ✓，我方补充 ✓）

```
$$\text{原问题}: \text{是否存在任意大的奇 }n\ \text{的 }Q=0\ \text{构造？}\ ✓$$
$$\text{精确化}: \text{已知奇 }n=2^m-1\ \text{的\textbf{完美码}确实满足 }Q=0\ \text{且 }M=K\ ✓✓\ (\text{无限族}\ ✓)\ ——\ \text{但此时 }E=0\ ✗\ (\text{无超额可分散}\ ✓)$$
$$\Longrightarrow\ \text{判据须写成}: \boxed{\text{是否存在无限多\textbf{奇 }n\ \text{且 }E>0}\ \text{的 }Q=0\ \text{构造？}}\ ✓$$
$$\qquad\text{已知小例}: n=5\ (E=10>0):\ \textbf{不存在}\ ✗\ (\text{320 个码全 }Q=2\ ✓);\ n\ge9:\ \textbf{未知}\ ✗$$
$$\qquad\text{且注意}: \text{偶 }n=2^m\ \text{有 }E=M>0\ \text{且 }Q=0\ ✓\ (\text{NP1CC}\ ✓)\ \Longrightarrow\ \textbf{"}E>0\Rightarrow Q\ge1\text{" 并非普遍成立}\ ✗\ ⟹\ \text{奇偶确实在做实质工作}\ ✓$$
$$

## §7 边界（诚实标注）

- §2 为**数值核验**（n=4,5 全枚举 ✓；n=6 采样 70 码 ✓）；§3 的奇偶引理为**我方推导** ✓（与数据完全吻合 ✓）
- §4 的"机器无内容"为**结构性结论** ✓（依据 van Wee 公式的修正项、Struik 下界、Habsieger 适用条件 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 局部过量覆盖奇偶引理 命中文件数=0    :: 
技术词 空不等式     命中文件数=2    :: ./ASSETS-REGISTRY.md ./E4-ENGINE-1-selfcontainment-attempt-four-routes-and-precise-jam.md 
技术词 偶数专用机器 命中文件数=0    :: 
技术词 二阶耦合候选 命中文件数=0    ::
```

- **本档新增**（命中数=0）：局部过量覆盖奇偶引理、偶数专用机器、二阶耦合候选
- **档案已有（引用，不列为提出）**：空不等式
