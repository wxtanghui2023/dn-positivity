已查地图：命中（`CAPMIX1B-B2-pseudo-survivors-are-the-zero-line`）⟹ 执行其 §6 之 (2)（对接四项硬检验），不开新案
D0: 本档对象 = **1A↔1B 对接四项硬检验**（A 集合恒等／B `Q_j` 自动消失／C 计数／D 退化集）＋ ⭐**"同一平移 incidence"正式确立**
D1: 1 （新自由度：两分支**共享同一平移核心** `I(G)`，且 `Q_j` 条件在直线上**冗余**）
[RESEARCH]

# **`CAP-MIX-1B · B3`：1A↔1B 对接（四项硬检验全 PASS）**

## §1 ⭐⭐⭐ 检验结果

```
$$\textbf{STATS}:\quad \text{case}=39,\qquad A_{\rm I\ne P}=0,\ \ A_{I\setminus P}=0,\ \ A_{P\setminus I}=0,\qquad \sum I=\sum P_x=\mathbf{388}$$ ✓✓✓
$$\qquad B_{\rm viol}=0,\qquad C_{\rm eq1}=39/39,\ \ C_{\rm eq2}=39/39,\qquad D_{\rm degen}=0,\qquad \lambda_2=0:9,\ \lambda_2>0:30$$
$$\begin{array}{c|c|c}
\text{项}&\text{内容}&\text{结果}\\
\hline
A&\{x:(x,1+x)\in P_\ast\}\ \overset{?}{=}\ I_2(G)&\boxed{\textbf{相等（双向，}0\ \text{差集）}}\ \checkmark\\
B&\forall x\in I,\forall j\in J_{\rm info}:\ x^{r_j}+(1+x)^{r_j}+1=0&\boxed{\textbf{零违例}}\ \checkmark\\
C&|P_\ast|=\lambda_2\ \text{且}\ |V_\ast|=|\text{Valid}|+\lambda_2&39/39、39/39\ \checkmark\\
D&\text{char 2 退化集空？}&x=1\Rightarrow y=0\notin G\ \Longrightarrow \boxed{\text{空}}\ \checkmark\\
\end{array}$$ ✓✓✓
```

## §2 ⭐⭐ 最强的一条：`Q_j` 条件**冗余**（B 项）

```
$$\boxed{\forall x\in G\cap(1+G),\ \forall r=r_j\in J_{\rm info}:\quad x^{r}+(1+x)^{r}+1=0\ \ \textbf{自动成立}}$$ ✓✓✓
$$\Longrightarrow\ \boxed{P_\ast=\{(x,1+x):\ x\in I_2(G)\}}\quad\textbf{不需要任何 } Q_j\ \text{条件}$$ ✓✓✓
**【⟹ 结构意义】** 直线 `z=0` 上，`r`-次幂的加法缺陷**恒消失**（与 `r` 是否为 `2`-幂无关）✓✓
$$\text{即}\quad x^r+y^r=(x+y)^r\quad\text{对 }(x,y)\in G^2,\ x+y=1\ \textbf{恒成立}$$ ✓✓
**【⟹ 本档的实质推进】** `B2` 的 `P_\ast=V_\ast\cap\text{直线}` **升级为** `P_\ast=\text{直线}\cap G^2`（与 `V_\ast` 无关）✓✓
```

## §3 ⭐ 与 `1A` 的同一性（正式表述）

```
$$\text{1A}:\ I_{\rm odd}(G)=\{x\in G:-1-x\in G\};\qquad \text{1B}:\ I_2(G)=\{x\in G:1+x\in G\}$$ ✓
$$\mathrm{char}\,2:\ -1=1\ \Longrightarrow\ -1-G=1+G\ \Longrightarrow\ \boxed{I_2(G)=I_{\rm odd}(G)}$$ ✓✓
$$\Longrightarrow\ \boxed{\textbf{两分支共享同一平移 incidence 核心}\ I(G)=G\cap(1+G)}$$ ✓✓✓（**不是"有关联"，是同一对象**）✓
**【char 2 的无退化性（D 项）】** $$x=1\Rightarrow y=0\notin G;\quad x=-2=0\notin G;\quad x=-\tfrac12=1\ (\text{与 }x=1\ \text{重合})\ \Longrightarrow\ \boxed{D(G)=\varnothing}$$ ✓✓
$$\Longrightarrow\ \lambda_{\rm raw}=\lambda_{\rm valid}=\lambda_2\quad(\textbf{char 2 无退化修正})$$ ✓
```

## §4 `B1` 判定机制的最终形态（精确）

```
$$\boxed{V_\ast=\text{Valid}\ \sqcup\ \{(x,1+x):x\in I_2(G)\}}$$ ✓✓
$$\boxed{|V_\ast|=|\text{Valid}|+\lambda_2},\qquad \boxed{\text{CAP}\iff V_\ast\subseteq\{z=0\}\iff\text{Valid}=\varnothing}$$ ✓✓✓
$$\text{且 }\lambda_2=0\ \text{时}\ V_\ast=\text{Valid}\ \text{（}9\ \text{例）};\quad \lambda_2>0\ \text{时按上式分离（}30\ \text{例）}$$ ✓
**【⟹ `B1` 已是精确判定机制（非"单侧证书"）】** ✓✓✓
```

## §5 状态与下一步（照您顺序）

```
$$\boxed{(2)\ \text{对接}=\textbf{PASS}（四项全过）}\ \Longrightarrow\ (1)\ \text{现变为\textbf{统一} } I(G)=G\cap(1+G)\ \text{的显式刻画问题}$$ ✓✓
**【(1) 的三个统一问题（照您 §末）】** $$(a)\ \lambda(G)=|I(G)|=0\ \text{何时？};\quad (b)\ \lambda(G)\ \text{何时大？};\quad (c)\ \text{能否由 }d,\ q=2^n\ \text{的结构直接判定？}$$ ✓✓
**【已有线索】** `(4,16,5)`：`|I|=0`（即论文族成员 `\lambda_2=0`）✓；`\lambda_2=0` 的 9 例在两类分支中分布可交叉核对 ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；盲类仍暂放 ✓
【数据】 `out/capmix1B3_bridge.txt`（39 行，含 `|I|,|Px|,差集,V*,valid,P*,λ2`）；脚本 `scripts/capmix1B3_bridge.py` ✓
【边界】 §1–§2 为实测（39 例）；§3 的同一性为**集合等式（char 2）**；§4 的组合式为**实测恒等＋推导** ✓

## §附 【技术词回查】（补录）
```
技术词 translation      命中文件数=20   :: ./p141-bridge-obstruction.md ./O3-mechanism-audit-and-ontology.md ./C3-TL-verified-and-Zomega-structure.md 
技术词 incidence        命中文件数=41   :: ./E3-why-this-is-not-the-old-pit.md ./TARGET-L9-q11-dir-probe.md ./TARGET-L9-source-fetch-report.md 
```
