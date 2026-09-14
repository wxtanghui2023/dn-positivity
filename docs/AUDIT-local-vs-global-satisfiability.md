# 🔒 **结构性审计：局部可满足性为何无法产生全局 NO-GO**
## —— 一个**可复用的排除框架**（含四层排除 ＋ 失败链 ＋ 判据清单）

> 依唐先生 2026-09-14 14:11 裁定 ✓（**(ii) 但不是工作总结 ✗，而是可复用结构审计 ✓**）
> 执行 ✓ 小灵｜**纸面 ＋ 既有数值证据 ✓｜零新计算 ✓**｜纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓
> 适用范围 ✓：**任何「S 由局部（模）条件定义、问 S = A⊕B 是否可能」的加法分解问题 ✓**

---

# §0 核心命题（本审计的一句话）

$$\boxed{\textbf{局部有限模结构}\ \not\Rightarrow\ \textbf{全局加法分解障碍}}$$
$$\boxed{\text{local feasibility}\ +\ \text{multiplicative CRT compatibility}\ +\ \text{sieve density}\ \not\Rightarrow\ \text{global additive-decomposition obstruction}}$$

$$\textbf{精确定性 ✓}：\text{我们排除的【不是原命题 ✗】，而是}\ \boxed{\textbf{"有限局部奇点"作为 NO-GO 来源 ✗}}$$
$$\textbf{最终落点 ✓}：\boxed{\textbf{NO-GO 不是"还没找到" ✗，而是这些工具【原则上】看不到整体性障碍 ✗}}$$

---

# §1 一般框架（把具体问题抽象掉）

$$\text{设 }S\subseteq\mathbb N_0\ \text{由【局部（模）条件】定义 ✓}：\ S=\{n:\forall p,\ n\bmod p^2\in S_p\}\ ✓\ \text{（平方自由是特例 ✓：}S_p=G_p\setminus\{0\}\ ✓）$$
$$\text{问 ✓}：\ \exists\,A,B\subseteq\mathbb N_0\ \text{（非退化 ✓）}\ \text{使}\ \boxed{S=A\oplus B}\ \text{（唯一加法分解 ✓）}$$
$$\textbf{自然的四类攻击 ✓（本审计逐一排除 ✓）}：$$
$$\qquad\text{L1 有限模层 ✓：固定 }p\ \text{上 }A_p+B_p=S_p\ \text{是否可解 ✗？}$$
$$\qquad\text{L2 乘积／CRT 层 ✓：有限多个 }p\ \text{之间是否自动 incompatibility ✗？}$$
$$\qquad\text{L3 筛法／密度层 ✓：密度上界能否给出严格反常 ✗？}$$
$$\qquad\text{L4 提升层 ✓：相容局部族能否"提升"为单一 }(A,B)\ ✗？$$

---

# §2 四层排除（✓ 逐层给判定与证据 ✓）

## L1 有限模层 —— **可满足 ✓（因此无 NO-GO ✗）**

$$\textbf{事实 ✓}：\text{固定 }p\ \text{时，(A) }A_p+B_p=S_p\ \text{＋ (C) 唯一性 的解【存在且大量 ✓】}$$
$$\qquad\text{证据 ✓}：p=3\ (G=9)\ \text{穷举：非空子集 }511\ \text{个 ⟹ }\textbf{解数 3726 ✓}；\text{含【均衡解】}(|X|,|Y|)=(3,3)\ \text{共 108 个 ✓}$$
$$\qquad\text{（}\text{注 ✓}：\text{我曾提出的"跨所有 }p\ \text{的显式族"}\textbf{【是错的 ✗】}\ —— \text{错在把"奇剩余"当成【奇数集的模像】✗；}\text{实际模像是【全部剩余 ✗】}（p^2\ \text{奇 ⟹ }p^2\equiv0\text{ ✓）⟹ 已勘误 ✓}$$
$$\Longrightarrow\ \boxed{\text{单 }p\ \text{不可作 NO-GO ✗（即使 }p=2\ \text{也见下 ✓）}}$$

## L2 乘积／CRT 层 —— **乘积解自动提升 ✓ ⟹ 有限 CRT 永不 obstruction ✗**

$$\textbf{引理（乘积集恒等式 ✓ 自证 ✓）}：\ \boxed{(A_1\times A_2)+(B_1\times B_2)=(A_1+B_1)\times(A_2+B_2)}$$
$$\qquad\text{证 ✓}：\text{坐标逐一相加 ✓（}(a_1,a_2)+(b_1,b_2)=(a_1+b_1,a_2+b_2)\ ✓）$$
$$\textbf{推论 ✓}：\text{若 }A_M:=\prod_pA_p\ ✓,\ B_M:=\prod_pB_p\ ✓\ \text{且各 }p\ \text{满足 }A_p+B_p=S_p\ ✓，\text{则 }A_M+B_M=\prod_pS_p=S_M\ ✓$$
$$\qquad\Longrightarrow\ \textbf{乘积型局部解【永远】能拼成每个有限模数的解 ✗} \Longrightarrow \textbf{有限 CRT 层【没有】自动 incompatibility ✓}$$
$$\textbf{附注（密度侧 ✓）}：|S_M|=M\prod_{p\mid M}(1-p^{-2})\ \textbf{是完全乘性对象 ✓} \Longrightarrow \textbf{乘起来不会产生密度亏损 ✗}$$

## L3 筛法／密度层 —— **相容 ✗（误差吞主项 ✓）**

$$\text{CRT 筛 ✓}：\ A(X)\le X\prod_{p\le y}\frac{|A_p|}{p^2}+O(M)\ ✓,\qquad M=\prod_{p\le y}p^2=e^{2\theta(y)}$$
$$\qquad\text{取 }M\asymp X:\ \textbf{误差 }O(X)\ \text{吞掉主项 ✗（经典困境 ✓）}；\text{用筛法基本引理（}y=X^{1/u}\text{）：误差小 ✓ 但积只到 }p\le X^{1/u}\ ⟹\ \textbf{所得不等式【相容 ✗】}$$
$$\Longrightarrow\ \textbf{筛法路线不产生严格反常 ✓}；\text{且全局计数 }A(X)B(X)\asymp X\ \text{与之相容 ✓}$$

## L4 提升层 —— ⭐ **提升条件【等价于】全局条件 ⟹ 无新判据 ✗**

$$\textbf{关键引理（一字等价 ✓）}：\ \boxed{\text{"}B_p\cap\{0\}=\varnothing\ \ \forall p\text{"}\iff\text{"}B\ \text{不含任何 }p^2\ \text{的倍数"}\iff \boxed{B\subseteq S}}$$
$$\qquad\text{同理 ✓}：\ \boxed{\text{"}A_p\cap\{-1\}=\varnothing\ \forall p\text{"}\iff A+1\subseteq S}$$
$$\Longrightarrow\ ⭐\ \textbf{"相容局部族能否提升"这一问题【就是】全局条件本身 ✗}：\text{要求 }(A,B)\ \text{实现所有局部解 ✓}\ \textbf{⟺ 要求 }A+1\subseteq S,\ B\subseteq S\ ✓$$
$$\qquad\text{而 }A+1\subseteq S,\ B\subseteq S\ \text{＋覆盖性}\ \textbf{就是 }S=A\oplus B\ \text{的一部分 ✗} \Longrightarrow \boxed{\textbf{以"提升"为主线 ⟹ 重新证明原命题 ✗，不产生新判据 ✓}}$$

---

# §3 本轮最重要的**逻辑区分**（✓ 唐先生指明 ✓）

$$\boxed{\text{"存在相容的局部族"}\ \ne\ \text{"存在满足全局平方自由条件的 }(A,B)"}$$
$$\boxed{\text{但反过来：要求后者【本身就是原命题的一部分 ✗】}}$$
$$\textbf{教训 ✓}：\text{任何"只依赖有限局部可满足性／局部密度／CRT／筛余类"的攻击，}\textbf{都【看不到】真正的障碍 ✗}$$
$$\qquad\text{因为障碍是【整体性】的 ✓：它只出现在 }A+B=S\ \text{这个整体约束里 ✓}（\text{即"哪些对落在哪里"✗），}\textbf{而不在任何一个模数上 ✗}$$

---

# §4 **失败链**（✓ 保留 ✓）

$$\begin{aligned}
\text{单 }p\ &\longrightarrow\ \textbf{可满足 ✓}（p=3:\ 3726\ \text{解 ✓}）\\
p=2\ &\longrightarrow\ \textbf{强刚性 ✓ 但不矛盾 ✗}（\text{解恰 }2\ \text{个 ✓} \Longrightarrow A\subseteq4\mathbb Z\ \text{或}\ B\subseteq4\mathbb Z+1\ ✓；\text{而 }A\subseteq4\mathbb Z\ \text{与}\ A(X)\asymp\sqrt X\ \textbf{相容 ✗}）\\
\text{有限 CRT}\ &\longrightarrow\ \textbf{乘积解自动提升 ✓}（\text{乘积恒等式 ✓）\\
\text{筛法}\ &\longrightarrow\ \textbf{密度不矛盾 ✗}（\text{误差吞主项 ✓）\\
\text{跨 }p\ \text{提升}\ &\longrightarrow\ \textbf{等价于原命题 ✗}
\end{aligned}$$
$$\textbf{一层比一层强 ✓，但}\ \boxed{\textbf{没有任何一层【原则上】能看到整体性障碍 ✗}}$$

---

# §5 ⭐ **可复用判据清单**（✓ 本审计的可迁移部分 ✓）

$$\text{给定任何"局部定义的 }S\ \text{＋ 问 }S=A\oplus B\text{"问题 ✓，先跑这四问 ✓：}$$
```
① **局部密度是否完全乘性 ✗？**  是 ⟹ L2 生效 ⟹ 【有限 CRT 永不 obstruction】✓ ⟹ 不要再堆模数
② **各模数局部解是否存在 ✗？**  是 ⟹ L1 生效 ⟹ 【单模数不可作 NO-GO】✓
③ **筛法误差能否被主项控制 ✗？** 不能 ⟹ L3 生效 ⟹ 【密度路线无严格反常】✓
④ **"提升"条件是否等价于全局条件 ✗？**  是 ⟹ L4 生效 ⟹ 【提升路线 = 循环 ✗】✓
⟹ 四问全"是" ⟹ **唯一出路 ＝ 引入【新的非局部机制 ✗】**（如全局加法结构 ✓），
   而不是再加一条模 p^2 条件 ✗
```

$$\textbf{注意 ✓}：\text{本清单【只】保证"不重复劳动"✗，不保证方向正确 ✓（同 }PROTOCOL-NOGO-GATE\ \text{的边界 ✓）}$$
$$\textbf{框架不适用的情形 ✓（须诚实标注 ✗）}：\text{① 若 }S\ \text{的局部结构【不是】完全乘性 ✓；② 若某模数局部解【不存在 ✓】；}\text{③ 若 }S\ \text{含有【非局部】定义成分 ✓（如由 }L\ \text{函数值定义 ✓）}$$

---

# §6 边界与纪律（✓）

```
✅ **纸面 ＋ 引用既有数值证据 ✓（p=3 穷举 ✓、p=2 穷举 ✓、奇数模像验证 ✓）；零新计算 ✓**
✅ **未用 RH ✓；未涉 ζ 解析 ✓（只用 |S∩[0,X]| 的经典计数 ✓）；未跑 Lean ✓**；**先查档 ✓**
⚠️ **① L1 的"单 }p$ 可满足"证据是【}p=3$ 穷举 ✓】** —— 更大 }p$ 未穷举 ✗；但 p=3 已足够否证"单模数必然矛盾"✓
⚠️ **② L4 的等价性是【一字级 ✓ 严格 ✓】**（"避开 0 模 }p^2$" ⟺ "不含 }p^2$ 倍数"✓）—— 无近似 ✗
⚠️ **③ 本审计【不声称】原命题不可证 ✗** —— 只声称四类工具看不到障碍 ✓
⚠️ **④ 本审计【不覆盖】非完全乘性／非局部定义的目标集合 ✗**（见 §5 末 ✓）
⭐ **净产出 ✓**：① **核心命题 ＋ 四层排除 ✓**；② ⭐ **L4 等价性（提升 ⟺ 全局 ✓）**；
   ③ **失败链 ✓**；④ ⭐ **可复用判据清单（四问 ✓）**；⑤ **框架适用边界 ✓**
```

## §7 一句话（✓）

$$\boxed{\text{四类局部工具（有限模／CRT 乘积／筛法密度／提升）【原则上】看不到障碍 ✗ —— 障碍是整体性的 ✓；下一阶段必须引入【新的非局部机制 ✓】}}$$


---

# §L5 ⭐ **框架外的"已排除"表**（2026-09-14 增补 ✓，防重复劳动 ✓）

与 L1–L4 不同，下表列的是**不属于**四层框架、但已试并失败的路线（全部落档 ✓）：

| 路线 ✓ | 结果 ✓ | 文档 ✓ |
|:--|:--|:--|
| (a) 差集支撑互斥计数 ✓ | **弱 ✗**（下界 ≍√X，之和 ≤ 2X+1 相容 ✓） | E172 §6 ✓ |
| (b) $p^2$-碰撞 ✓ | **不足 ✗**（Lemma A 只禁【共同】非零倍数 ✗） | E172 §6 ✓ |
| (c) $S-B+1\subseteq S$ ✓ | **我自误 ✗**（只对【配对】$(s,b)$ 成立 ⟹ 实为 $A+1\subseteq S$ 循环 ✓） | E172 §8 ✓ |
| (d) 互素积计数 ✓ | **相容 ✗**（$0.3696X\le0.6079X$ ✓） | E172 §8 ✓ |

**已得到的结构性定位 ✓**（`docs/E173-*.md` ✓）：缝隙 ＝ **代表元大小问题 ✗**；四层工具只对**存在性**敏感 ⟹ **结构上够不到缝隙 ✓**。

**下一步（未试 ✓）**：$N_M(c)$ 的估计 ✓；或"绕一圈解必存在"的证明 ✗。
