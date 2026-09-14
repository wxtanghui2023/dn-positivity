# E166 · ⭐⭐⭐⭐ **D1-B\* 重述：勘误 ＋ 归一化 $C=n^kF$ ＋ 一条已证不可能性（$C=\mu^2$）**
### 采纳您的核心重述 ✓；**并补上一条【已证】结论 ✓**：**多项式型 $A,B$ 不能产生 $C=\mu^2$ ✗**

> 委托 ✓ 唐先生 2026-09-14 13:40（**阻止 3 原子盲搜 ✓；先修正 §4 错误 ✓；重述核心命题 ✓；定向反例搜索 ✓**）
> 执行 ✓ 小灵｜**纸面审计 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**逐字核您的代数 ✓**

---

## §0 勘误（✓ 您逮到的错误 ✓）—— **但含一处对您推论的限定 ✗**

$$\text{我在 }E165\ \text{§4 写的 }\boxed{B_k=k^k-(k-1)^k\ \text{"多项式型／盲类可达"}}\ \textbf{【符号有误 ✗】}：\text{把【指数 }k\text{】与【求和下标】混同 ✗}$$
$$\textbf{您的两点批评 ✓ 皆对 ✓}：\text{(i) }k^k-(k-1)^k\ \text{【非】固定次数多项式 ✗（增长 }\sim k^k\log k\ ✓）\text{；(ii) 其"盲类可达"【未证 ✗】}$$
$$\textbf{但需限定一处 ⚠️}：\text{正确的陈述是【对固定 }k\ ✓\text{】}：\ \boxed{B_N=N^k-(N-1)^k\ \textbf{确是 }N\ \text{的 }k-1\ \text{次多项式 ✓}（N\ge1\ ✓,\ B_0=0\ ✓）}$$
$$\qquad\text{验证 ✓}：A=\text{const1}\ ✓,\ B_0=0\ ✓ \Longrightarrow C_N=\sum_{j=0}^{N}B_j=(N^k-0^k)=N^k\ ✓$$
$$\qquad\text{而 }N^{k-1}\ \text{在盲类中可达 ✓（}n^2\in\ \text{原子 ✓；}n^j\ \text{由 }\times\ \text{累乘 ✓；}\pm\ \text{由 }+\ \text{与缩放 ✓）} \Longrightarrow \textbf{该式在该意义下【成立 ✓】}$$
$$\Longrightarrow\ ⭐\ \textbf{结论 ✓}：\text{我改的是【符号 ✗】，不是【结论 ✓】；但您的批评【正确指出了】原写法的不可接受性 ✓ —— }\textbf{故照您要求，原句作废 ✓，改用上述限定版 ✓}$$
$$\text{（}\text{已给 }E165\ \text{§4 加勘误 ✓，原文保留不删 ✓（T10 ✓））}$$

## §1 采纳您的**归一化**（✓ 并独立核对 ✓）

$$\text{设 }C\ \text{乘性 ✓，写 }C_N=P(N)+R(N)\ ✓,\ P\ \text{自身乘性 ✓（}P=N^k\ ✓）；\text{对互素 }m,n\ ✓：$$
$$(mn)^k+R(mn)=\bigl(m^k+R(m)\bigr)\bigl(n^k+R(n)\bigr)\ \Longrightarrow\ R(mn)=m^kR(n)+n^kR(m)+R(m)R(n)\ ✓\ \textbf{（您 §7 ✓）}$$
$$\text{令 }F(n):=1+\frac{R(n)}{n^k}\ ✓ \Longrightarrow\ F(mn)=1+\frac{R(mn)}{(mn)^k}=1+\frac{R(m)}{m^k}+\frac{R(n)}{n^k}+\frac{R(m)}{m^k}\frac{R(n)}{n^k}=F(m)F(n)\ ✓✓$$
$$\Longrightarrow\ \boxed{\textbf{归一形 ✓}：C(n)=n^kF(n)\ ✓,\quad F\ \textbf{完全一般地乘性 ✗}}\ \ \textbf{（我逐式核对通过 ✓）}$$
$$\text{（}\textbf{忠实中肯 ✓}：\text{这把"非 }N^k\text{"从一个模糊搜索目标 ✓，压成【明确的乘性残差 }F\ ✗】—— 这是您本轮的关键贡献 ✓）}$$

## §2 撤回我此前的**过强措辞** ✗（✓ 依法 ✓）

$$\text{我在 }E165\ \text{写"猜想有【强证据】✓"}\ \Longrightarrow \textbf{撤回 ✗}：\text{9612 对失败【只说明】"当前搜索空间无例 ✗"，}\textbf{不说明"一般结构大概率如此 ✗"}$$
$$\Longrightarrow\ ⭐\ \textbf{核心缺口精确化 ✓（＝您 §3 ✓）}：\ \boxed{\textbf{"盲语法产生的乘性输出，是否必然被迫进入【多项式世界】✗？"}}$$
$$\text{已证部分 ✓（}E165\ \text{§4 ✓，您的 §2 更硬的版本 ✓）}：\ P\ \text{多项式 ✓ ＋ }P(xy)\equiv P(x)P(y) \Longrightarrow a_ia_j=0\ (i\ne j) \Longrightarrow P=x^k\ ✓$$
$$\text{未证部分 ✗}：\ \mathfrak G\xrightarrow{\star_C}\{\text{乘性}\}\ \Longrightarrow\ \{\text{多项式}\}\ ✓\ \textbf{（这一步【没有证明 ✗】）}$$

## §3 定向反例搜索靶表（✓ 依您 §9 ✓，非盲目扩族 ✗）

$$\textbf{首靶 ✓}：\ \boxed{C(n)=\mu^2(n)\ ✓}\ \text{（＝ }k=0\ ✓,\ F=\mu^2\ne1\ \text{✓）}\ \text{或 }\ C(n)=n^k\mu^2(n)\ ✓$$
$$\qquad\text{核验其性质 ✓}：\text{① 盲 ✓（}\mu\ \text{在原子内 ✓）；② 非多项式 ✓；③ 严格乘性 ✓；④ 非退化 ✓；⑤ 不涉 RH ✓ ⟹ }\textbf{完美 kill 靶 ✓}$$
$$\textbf{其余优先靶 ✓}：F=1_{(n,q)=1}\ ✓\ \big|\ F=1_{p\nmid n}\ ✓\ \big|\ F=v_p(n)+1\ ✓\ \big|\ F=\tau(n)\ ✓$$
$$\textbf{判据 ✓}：\ \boxed{\text{若任一靶出现在 }\star_C\ \text{闭包内}\ \Longrightarrow\ \textbf{D1-B\* 立即死亡 ✗}}\ \big|\ \text{若可证皆不可达 ⟹ 接近"乘性 ⟹ 去奇异性 ⟹ }N^k\text{"✓}$$

## §4 ⭐ **一条【已证】结论**（✓ 本轮实质 ✓）：**多项式型 $A,B$ 不能产生 $C=\mu^2$** ✗

$$\textbf{命题 ✓}：\text{若 }A,B\ \text{皆【多项式型 ✓】（}A_n=\sum_{j\le d_A}c_jn^j\ ✓），\text{则 }(A\star_CB)(N)\ \textbf{≠}\ \mu^2(N)\ \text{（对无穷多 }N\ ✓）$$
$$\textbf{证明链 ✓（三步 ✓）}：$$
$$\qquad\textbf{步 1 ✓（自证 ✓）}：\text{【有界】线性递推序列 ⟹ 【终期周期 ✗】}$$
$$\qquad\qquad\text{证 ✓}：\text{状态向量 }v_N=(a_N,\dots,a_{N+d-1})\ \text{满足 }v_{N+1}=Mv_N\ ✓\ \text{且 }v_N\ \text{落在【有限集 ✗】（有界 ✓）；}\text{确定性递推 ⟹ }\textbf{最终进入循环 ✓}$$
$$\qquad\textbf{步 2 ✓}：\ \mu^2\ \textbf{【非】终期周期 ✗}$$
$$\qquad\qquad\text{证 ✓}：\text{设 } \mu^2(n+q)=\mu^2(n)\ (n\ge N_0)\ ✓；\text{取素数 }p>N_0,\ p\nmid q\ ✓；\text{则 }p^2\ \text{非平方自由 ✓ ⟹ 全 }p^2+tq\ \text{非平方自由 ✗；}$$
$$\qquad\qquad\text{但 }(p^2,q)=1\ ⟹ \text{该 AP 含【正密度】多平方自由数 ✓（}\textbf{Mirsky ✓，AP 中平方自由数定理 ✓ ⚠️ 须对象固定 ✗）} \Longrightarrow \textbf{矛盾 ✓}$$
$$\qquad\textbf{步 3 ✓}：\ \mu^2\ \text{非有界 LRS ✗（步 1 逆否 ✓）} \Longrightarrow \mu^2\ \text{的【常系数线性递推】不存在 ⟹ GF【非有理 ✗】}$$
$$\qquad\text{而多项式型 }A,B\ \text{的 GF 皆【有理 ✗】（极点仅在 }x=1\ ✓），\text{其积【有理 ✗】} \Longrightarrow \textbf{不可能等于 } \mu^2\ \text{的 GF ✗} \Longrightarrow \textbf{命题成立 ✓✓}$$
$$\Longrightarrow\ ⭐\ \textbf{意义 ✓}：\text{这【证死了一个子类】✓（多项式型 ✗），}\textbf{并把残余【精确隔离】到"含 }\mu,\Lambda,\Omega\ \text{等非多项式原子"的那一半 ✓✓}$$

## §5 剩余开放问题（✓ 下一轮的可判定动作 ✓）

$$\textbf{开放 ✓}：\text{含【非多项式原子】（}\mu\ ✓,\ \Lambda\ ✓,\ \Omega\ ✓,\ \omega\ ✓）的盲 }A,B\ \text{能否产生 }C=\mu^2\ \text{或 }n^k\mu^2\ ✗$$
$$\textbf{下一轮两个可判定动作 ✓}：$$
$$\qquad\textbf{(甲) 代数去卷积 ✓}：\text{问 }C(x)=A(x)B(x)\ \text{的【盲因式是否存在 ✗】—— 即：}\mu^2\ \text{的 GF }\prod_p(1+x^p+x^{p^2}+\cdots)\ ✓\ \text{能否分解为两个【盲】GF ✗}$$
$$\qquad\textbf{(乙) 定向枚举 ✓（非盲目扩族 ✓）}：\text{只测【靶型】组合 ✓（}F=\mu^2,\ 1_{(n,q)=1},\ v_p+1,\ \tau\ ✓\text{），}\text{且判定标准改为"是否出现 }C=n^kF\ (F\ne1)\ ✗"}$$

## §6 边界与纪律（✓）

```
✅ **纸面 ＋ 一条已证命题 ✓**；未用 RH ✓；未跑 Lean ✓；**逐字核您的代数 ✓**；**勘误已落 ✓（T10 ✓）**
⚠️ **① 步 2 依赖 Mirsky（AP 中平方自由数正密度 ✓）—— 须按【组件 2】做对象固定 ✗（本轮未逐字抄原文 ✓）**
⚠️ **② §4 只覆盖【多项式型 ✓】** —— 非多项式盲类【完全未触及 ✗】⟹ **不是"}\mu^2\ \text{不可达"的完整结论 ✓**
⚠️ **③ 我撤回 }E165\text{ 的"强证据"措辞 ✓**；本档不声称猜想为真 ✗
⭐ **净产出 ✓**：① **勘误（符号 ✗）＋ 对您推论的限定 ✓**；② **采纳并核对归一形 }C=n^kF\ ✓**；
   ③ **撤回过强措辞 ✓ ＋ 核心缺口精确化 ✓**；④ **定向靶表 ＋ kill 判据 ✓**；⑤ ⭐ **已证：多项式型 }A,B\ ⇒C\ne\mu^2\ ✗**；
   ⑥ **残余精确隔离到非多项式原子那一半 ✓**
```

## §7 一句话（✓）

$$\boxed{\text{勘误在【符号】✗；您的归一化【采纳并核对 ✓】；}\textbf{并已证死一个子类（多项式型 ⇒ }C\ne\mu^2\text{✗）——残余精确落在非多项式原子 ✗}}$$
