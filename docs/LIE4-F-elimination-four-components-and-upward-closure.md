# 猎-4（$\mathfrak F$ 消元）— **四分量展开 ＋ 一个已证结构结果（上闭性）**

> 唐先生 2026-09-16 20:03「继续」；按 REVIEW-20260916 登记的**下次第一刀**：$\mathfrak F$ 的完整消元，**而非**优化 $t$✓
> **防偷渡铁律**：$$\boxed{\mathfrak F\ne\{(r,t):r,t\ge0\}}$$
> 取证：BCR 原文 PDF（外部来源，仅作数据）—— 本档依其 (1.3)／Theorem 2／Conjecture 1 的**逐字陈述**展开。

---

## 1. 四分量逐项写出

### (i) $\mathfrak F_{\rm estimate}$
$$\text{(1.3)}：S_{A,M,N}\ll_\varepsilon\|\alpha\|\|\beta\|\|\nu\|(M+N)^{\frac12+r+\varepsilon}A^{t}+\|\nu\|A^{\frac12}\bigl(\|\alpha\|_\infty\|\beta\|N^{\frac12+\varepsilon}+\|\alpha\|\|\beta\|_\infty M^{\frac12+\varepsilon}\bigr)$$
$$\qquad M\le m<2M,\ N\le n<2N,\ A\le a<2A,\quad \boxed{A\ll(NM)^{\frac{0.5-r}{1+2t}+\varepsilon}}$$
$$\mathfrak F_{\rm estimate}:=\{(r,t):\text{(1.3) 成立}\}；\ \text{原文}：\text{"We conjecture that (1.3) holds true for}\ \textbf{all}\ r,t\ge0\text{"}$$
$$\qquad\Longrightarrow\ \mathfrak F_{\rm estimate}^{\rm conj}=\{r,t\ge0\}\ (\text{推测});\quad \mathfrak F_{\rm estimate}^{\rm uncond}\ \textbf{形状未知}，\ \text{已知含}\ (\tfrac{23}{48},\tfrac12)\ \text{与}\ (\tfrac9{20},\tfrac7{20})✓$$

### (ii) $\mathfrak F_A$
$$\text{要求}：\text{应用所需的}\ A\ \text{范围}\ \le\ \text{(1.3) 允许的}\ A\ \text{范围}\ (NM)^{\frac{0.5-r}{1+2t}+\varepsilon}$$
$$\qquad\text{注意}：\ \text{该指数}\ \textbf{随}\ r,t\ \text{减小而增大} \Longrightarrow \textbf{强输入}\leftrightarrow\textbf{长}\ A\ \text{范围}✓$$
$$\qquad\textbf{边界情形（本档核对）}：\ (r,t)=(0,0)\Longrightarrow \text{指数}=\tfrac12 \Longleftrightarrow \text{Conjecture 1 的}\ A\ll(NM)^{\frac12+\varepsilon}\ ✓✓\ (\text{两者一致})$$

### (iii) $\mathfrak F_{\rm error}$
$$\text{Theorem 2（原文）}：I=\sum_{d,e\le T^\theta}\frac{a_d\bar a_e}{[d,e]}\int_{\mathbb R}\Bigl(\log\frac{t(d,e)^2}{2\pi de}+2\gamma\Bigr)\varphi\Bigl(\frac tT\Bigr)dt+O\Bigl(T^{\frac12-t+\varepsilon}N^{\frac12+r+2t}+T^{\frac13+\varepsilon}\Bigr)$$
$$\qquad\text{for}\ \ \theta<\tfrac12+\frac{0.5-r}{1+2(r+2t)},\quad N:=T^{\theta}$$
$$\Longrightarrow\ \text{主误差}\ T^{\frac12-t+\varepsilon}N^{\frac12+r+2t}\ \text{次于主项}\ (\asymp T^{1+o(1)})\iff \theta<\frac{1+2t}{1+2r+4t}\ \textbf{（恒等，已验）}✓$$
$$\qquad\text{次误差}\ T^{\frac13+\varepsilon}\ \textbf{永不绑定}（\tfrac13<1）✓$$

### (iv) $\mathfrak F_{\rm application}$
$$\text{应用侧需求}：\text{mollifier 长度指数}\theta\ \text{目标}；\ \text{平衡条件}；\ \text{主项渐近式成立}✓$$

---

## 2. ⭐ 关键消元结果：**Theorem 2 的陈述方式吸收了 (ii)(iv)**
$$\text{原文陈述}：\ \text{"}\textbf{Suppose that (1.3) is true for some}\ r,t\ge0\text{.}\ \textbf{Then}\ I=\dots\ \text{for}\ \theta<\dots\text{"}$$
$$\Longrightarrow\ \text{该蕴含是}\ \textbf{对每个}\ (r,t)\ge0\ \textbf{一致断言} \text{的} \Longrightarrow \text{应用侧与}\ A\ \text{范围需求}\ \textbf{已由定理本身吸收}✓$$
$$\qquad(\text{原文}：\text{"The proof of Theorem 2}\dots\text{is the same as that of Theorem 1 except that we use (1.3) instead of Proposition 1. The modification will be discussed at the end of Section 3."})$$
$$\Longrightarrow\ \boxed{\mathfrak F_A\cap\mathfrak F_{\rm application}\ \text{不构成额外限制}；\ \text{故}\ \mathfrak F\ =\ \mathfrak F_{\rm estimate}}✓$$
$$\qquad\text{而}\ \mathfrak F_{\rm error}\ \textbf{不是}\ \mathfrak F\ \text{的成员条件}，\ \text{而是}\ \textbf{定义}\ \theta_{\max}(r,t)\ \text{的那个不等式}✓✓$$
$$\Longrightarrow\ \mathfrak F\ \text{的消元结论（干净形式）}：\ \boxed{\mathfrak F\ =\ \{(r,t):\text{(1.3) 成立}\}}\quad(\text{推测：全象限})✓$$

---

## 3. ⭐⭐ 已证结构结果：$\mathfrak F$ 是**上闭集**（coordinatewise）
$$\text{设}\ (r,t)\in\mathfrak F。\ \text{取}\ r'=r+\epsilon\ (\epsilon>0)：$$
$$\qquad\text{(a) 界：}\ (M+N)^{\frac12+r'+\epsilon'}\ \ge\ (M+N)^{\frac12+r+\epsilon} \Longrightarrow \text{界}\ \textbf{更弱}，\ \text{故仍成立}✓$$
$$\qquad\text{(b)}\ A\ \text{范围}：\ \frac{0.5-r'}{1+2t}=\frac{0.5-r-\epsilon}{1+2t}<\frac{0.5-r}{1+2t} \Longrightarrow \text{范围}\ \textbf{更短} \Longrightarrow \text{是原陈述的子范围}✓$$
$$\qquad\Longrightarrow\ (r',t)\in\mathfrak F✓$$
$$\text{同理}\ (r,t')\ (t'=t+\epsilon)：\ A^{t'}\ge A^{t}\ (\text{因}\ A\ge1\ \text{且}\ t'>t)\ \text{界更弱}✓；\ \frac{0.5-r}{1+2t'}<\frac{0.5-r}{1+2t}\ \text{范围更短}✓\Longrightarrow (r,t')\in\mathfrak F✓$$
$$\Longrightarrow\ \boxed{\mathfrak F\ \text{在坐标序下}\ \textbf{上闭}：\ (r,t)\in\mathfrak F,\ r'\ge r,\ t'\ge t\Longrightarrow(r',t')\in\mathfrak F}✓✓\ (\textbf{本档证明，据 (1.3) 的形式})$$
$$\textbf{推论 1}：\ \inf_{(r,t)\in\mathfrak F}(17r+t)\ \text{在其}\ \textbf{下边界}\ \partial\mathfrak F\ \text{上取到}✓$$
$$\textbf{推论 2}：\ r\ge\tfrac12\ \text{时}\ 0.5-r\le0 \Longrightarrow A\ \text{范围退化},\ \theta_{\max}\le\tfrac12 \Longrightarrow \textbf{相关区域落在半平面}\ r<\tfrac12✓$$

---

## 4. ⭐ 消元后的二分判据（唐先生版）——**其中一支被排除**
$$\boxed{\inf_{(r,t)\in\mathfrak F}\bigl(17r+t\bigr)\ \begin{cases}<8 &\Rightarrow \textbf{架构内已有突破空间}\\ =8 &\Rightarrow \textbf{17/33 是应用可达域边界}\\ >8 &\Rightarrow \textbf{17/33 点需重新解释}\end{cases}}$$
$$\textbf{本档排除第三支}：\ \text{BC 点}\ (\tfrac9{20},\tfrac7{20})\in\mathfrak F_{\rm estimate}^{\rm uncond}\ \text{且}\ 17r+t=\textbf{8}\ \text{恰在线上}$$
$$\qquad\Longrightarrow\ \inf_{\mathfrak F}(17r+t)\le8 \Longrightarrow \boxed{\text{"}>8\text{"}\ \textbf{不可能}}✓$$
$$\textbf{故}\ \text{二分支}：\ \inf=8\ (\text{边界卡住})\quad\text{或}\quad\inf<8\ (\text{存在严格突破点})✓$$
$$\text{且推测域}\ \mathfrak F^{\rm conj}=\{r,t\ge0\}\Longrightarrow \inf=0<8 \Longrightarrow \textbf{19/33 型改进在猜想型输入下}\ \textbf{无阻塞}✓（\text{即 N3-C}）$$

---

## 5. 由此得到的"墙 A 天花板"的**最干净形式**
$$\boxed{\text{天花板问题}\ \equiv\ \text{已证区域}\ \mathfrak F^{\rm uncond}\ \text{的}\ \textbf{下边界}\ \partial\mathfrak F^{\rm uncond}\ \text{是否穿过直线}\ 17r+t=8}$$
$$\qquad\textbf{现状}：\ \text{已知最低}\ \textbf{已证点} \text{恰落在线上}（\text{BC 点}）\Longrightarrow \text{当前}\ \inf=8 ✓$$
$$\qquad\textbf{攻击＝}\text{把}\ \partial\mathfrak F^{\rm uncond}\ \textbf{下移} \text{（\text{即证出一个}\ 17r+t<8\ \text{的点}）}✓$$
$$\qquad\textbf{且由 §3 上闭性}：\ \text{只需证出}\ \textbf{任意一点} \text{在带内} \Longrightarrow \text{整个上闭包}\ \text{进入带内}✓$$

## 6. 残余（不得省略）
$$\text{残余 1：§2 的"吸收"依据原文陈述方式（}+\ \text{§3 结尾的 modification 说明）；}\textbf{§3 实际修改未读} \Longrightarrow \text{若该修改对某些}\ (r,t)\ \text{另有要求，则}\ \mathfrak F\ne\mathfrak F_{\rm estimate}✓$$
$$\text{残余 2：}\ \mathfrak F^{\rm uncond}\ \text{的}\ \textbf{完整形状未知}（\text{仅知两点}）；\ \text{残余 3：}\ §3\ \text{上闭性证明基于}\ (1.3)\ \text{的}\ \textbf{形式}，}\textbf{未} \text{核对}\ (1.3)\ \text{在}\ A<1\ \text{等边界的退化情形}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 取证 BCR 原文（外部来源），关键公式与语句}\ \textbf{逐字引用}✓；\quad\text{② 已守住防偷渡（}\mathfrak F\ne\text{全象限：}\mathfrak F\ \text{是}\ \textbf{上闭集} \text{且有}\ A\ \text{范围约束}）✓；$$
$$\text{③ }\textbf{未用 RH}；零数值（\text{仅代数证明与恒等式）}；\ \text{未跑 Lean}✓$$

## 8. 净产出
$$\text{(i) 四分量逐项写出（依原文公式）；}$$
$$\text{(ii) ⭐ 消元：Theorem 2 的}\ \textbf{一致陈述} \text{吸收了}\ \mathfrak F_A\cap\mathfrak F_{\rm application} \Longrightarrow \boxed{\mathfrak F=\mathfrak F_{\rm estimate}}；\ \mathfrak F_{\rm error}\ \text{定义}\ \theta_{\max}\ \text{而非成员条件}；$$
$$\text{(iii) ⭐⭐ }\textbf{已证}：\mathfrak F\ \text{坐标序上闭} \Longrightarrow \inf(17r+t)\ \text{在}\ \partial\mathfrak F\ \text{取到}；\ \text{相关区域}\ r<\tfrac12；$$
$$\text{(iv) 三支判据中}\ \textbf{"}>8\text{"}\ \textbf{被排除}（\text{BC 点在线上}）\Longrightarrow \text{只剩二分}；$$
$$\text{(v) 天花板的最干净形式：}\partial\mathfrak F^{\rm uncond}\ \text{是否下穿}\ 17r+t=8；\ \text{攻击＝下移该边界（由上闭性只需一点）。}$$
