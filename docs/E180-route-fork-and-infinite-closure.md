# E180 · ⭐⭐⭐⭐⭐ **路线分叉校正（U/G）＋ 无限双集合闭包新模式 ＋ E178 归约确认**
> 依唐先生 2026-09-14 15:28 裁定 ✓（**分叉点在 2 而非 29 ✓；"1∉B"仅属路线 U ✓；不追 29 ✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；零新数值 ✓；未跑 Lean ✓

---

## §0 采纳校正（✓ 我的 E179 审计混淆了两条路线 ✗）

$$\textbf{路线 U（唯一铺砌 ✓）}：S=A\oplus B\ ✓\ \Longrightarrow\ \boxed{1\notin B}\ \text{【成立 ✓】}\quad\text{（本档此前的链【只】属此路线 ✓）}$$
$$\textbf{路线 G（一般覆盖 ✓）}：\boxed{S=A+B}\ ✓\ \text{仅要求每个平方自由数【至少一个】表示 ✓} \Longrightarrow\ \boxed{1\in A\cap B\ \text{允许 ✓}}\ \text{、重复表示允许 ✓}$$
$$\qquad\Longrightarrow\ ⚠️\ \textbf{我 E179 中"分支 (ii)（}4\in B\text{）"的分析【混用了两路线 ✗】}：\text{它用了 }1\notin B\ \text{（U 专属 ✓）却又允许 }B\ \text{含非平方自由元（G 特征 ✗）}$$
$$\textbf{精确状态（依您 ✓）}：\ \boxed{\text{E179：有限唯一链【未闭合 ✗】；一般覆盖问题【仍 OPEN ✓】}}$$

## §1 ⭐ 您 §1 的核（✓ 我验为【正确且更锋利 ✓】）

$$\boxed{\text{一般规则 ✓}：x\in A\cap B\ \Longrightarrow\ 2x\in A+B\subseteq S\ \Longrightarrow\ \boxed{2x\ \text{平方自由}}\ ✓}$$
$$\qquad\Longrightarrow\ \textbf{特别 ✓}：2\in A\cap B\ \Longrightarrow\ 2\cdot2=4\notin S\ ✗\ \Longrightarrow\ \boxed{2\in A\cap B\ \text{不可能 ✓}}\ \text{（您的 §1 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{推论 ✓}：\boxed{x\equiv2\bmod4\ \Longrightarrow\ x\notin A\cap B}\ ✓（2x=4\cdot\text{odd}\ ✗）$$
$$\textbf{故路线 U ✓}：2\in S\ \text{的唯一表示必为 }(2,0)\ \text{或}\ (1,1)\ ✓ \Longrightarrow\ \boxed{2\in A}\ \text{或}\ \boxed{1\in B}\ \text{（恰一 ✓）}$$
$$\qquad\text{若 }2\in A\ ✓：\text{则 }2\in A\cap B\ ✓（b=2\ \text{时 ✓）} \Longrightarrow \textbf{与 §1 矛盾 ✗} \Longrightarrow \boxed{2\notin A}\ \Longrightarrow\ \boxed{1\in B}\ ✓$$
$$\qquad\Longrightarrow\ \textbf{于是 }b=\min(B\setminus\{0\})=1\ ✓\ \text{（非 2 ✗）}—— \textbf{我 E179 的 }b=2\ \text{结论【在路线 U 下存疑 ✗】}$$

## §2 ⭐⭐ 新模式（您的 §3–§6 ✓）：双集合互定义的加法禁配闭包

$$A+B\subseteq S\ \Longleftrightarrow\ \boxed{\forall a\in A:\ a+B\subseteq S}\ \wedge\ \boxed{\forall b\in B:\ A+b\subseteq S}$$
$$\text{定义 ✓}：\boxed{\mathcal A(B):=\{a\ge0:\ a+B\subseteq S\}}\ ✓,\qquad \boxed{\mathcal B(A):=\{b\ge0:\ A+b\subseteq S\}}\ ✓$$
$$\text{任何解须满足 ✓}：\boxed{A\subseteq\mathcal A(B)}\ ✓,\qquad \boxed{B\subseteq\mathcal B(A)}\ ✓,\qquad\text{同时}\ \boxed{S\subseteq A+B}\ ✓$$
$$\Longrightarrow\ \textbf{问题 ＝ 求映射 }(A,B)\mapsto(\mathcal A(B),\mathcal B(A))\ \text{的【闭点 ✓】且满足覆盖 ✓}$$
$$\text{（}\textbf{与九条 NO-GO 的差别 ✓}：\mu^2(n)=\prod_p\mu_p^2(n)\ \text{只描述【单整数合法性 ✗】；}\text{此处是}\ \boxed{\text{同一个 }a\ \text{须同时通过【整个 }B\ \text{的平移测试 ✗】}}\ \text{—— }\textbf{第一次出现集合—集合级非局部耦合 ✓}）$$

## §3 ⭐ 阶段判定：**有限 }B$ ⟹ 回落 E178（✓ 我验为正确 ✓）**

$$\text{若 }|B|=k<\infty\ ✓：\ a+B\subseteq S\ \text{＝ }k\ \text{个平方自由平移的交 ✓} \Longrightarrow \text{每 }p\ \text{至多排除 }k\ \text{个 }p^2\text{-残类 ✓}$$
$$\qquad\xRightarrow{E177\ \text{一般原理}}\ p^2>k\ \text{时【不可能】完整禁阻 ✗} \Longrightarrow \text{仅 }p\le\sqrt k\ \text{参与 ✓} \Longrightarrow \textbf{有限局部条件 ⟹ CRT 可拼接（}E170\ ✓）\ \Longrightarrow \ \textbf{回落 E178 ✗}$$
$$\Longrightarrow\ \boxed{\textbf{有限 }B\ \text{（或有限构型／有限模／有限相关）}\ \Longrightarrow\ \text{全部回到局部筛框架 ✗}}\ ✓\ \text{（与 }E178\ \text{统一根因一致 ✓）}$$
$$\text{（}\textbf{故唯一活路 ✓}：\ \boxed{\textbf{无限 }A,B\ \text{的加法闭包 ✗}\ +\ \text{全覆盖 ✗}}\ —— \text{而非把 }29\ \text{换成 }31,37,\ldots\ ✗）$$

## §4 ⭐⭐ 新靶（您的 §7 ✓）：坏边计数

$$\boxed{E(X):=\#\{(a,b)\in A\times B:\ a+b\le X,\ a+b\notin S\}}\ ✓\qquad\text{要求}\ \boxed{E(X)=0}\ \forall X\ ✓\ \text{（【零个坏边 ✗】而非"坏边比例小 ✗"）}$$
$$\qquad\text{（}\textbf{您的 §8 警告照录 ✓}：\text{不可写 }E(X)\sim(1-6/\pi^2)A(X)B(X)\ ✗ —— \textbf{因 }A,B\ \text{【非随机 ✗】且正会主动避开非平方自由和 ✓}）$$
$$\text{（}\textbf{我加一条 ✓}：\text{由 }E(X)=0\ \text{＋ }A\subseteq\mathcal A(B)\ ✓，}\text{坏边【结构性】不存在 ✓ —— }\textbf{要求的量不是 }S\ \text{的密度 ✗，而是 }\boxed{\text{闭包算子的不动点存在性 ✗}}）$$

## §5 边界（✓）

```
✅ **§0 采纳校正（我的 E179 混用两路线 ✗）；§1 验您的 §1 为正确 ✓ 并加了"x≡2 mod 4 ⟹ x∉A∩B"推论 ✓**
✅ **§3 的有限 B ⟹ E178 归约【我独立验为正确 ✓】；§4 照录您的 E(X) ✓**
✅ **零新数值 ✓；未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓**
⚠️ **① §1 的推论导出了 }b=1$（非 }b=2$）—— **这使 E179 在路线 U 下的 }b=2$ 结论【存疑 ✗】**，需重核 ✓
⚠️ **② 本档【不判断】无限闭包是否存在 ✗（这才是 OPEN 的对象 ✓）**
⚠️ **③ 不声称原命题不可证 ✗**
⭐ **净产出 ✓**：① **两路线分叉的精确化 ✓**；② ⭐ **A∩B ⊆ {2x∈S} 规则 ✓（含您的 2+2=4 核 ✓）**；
   ③ ⭐ **闭包算子形式 }\mathcal A(B),\mathcal B(A)$ ✓**；④ **有限 }B$⟹E178 归约确认 ✓**；⑤ **新靶 }E(X)=0$ ✓**
```

## §6 一句话（✓）

$$\boxed{\text{分叉校正采纳 ✓（}1\notin B\ \text{仅属 U ✓）；}\textbf{新模式 ＝ 无限双集合加法闭包 }\mathcal A(B)/\mathcal B(A)\ \text{＋ 全覆盖 ✗；}\text{有限 }B\ \text{已回落 E178 ✓；不追 29 ✓}}$$
