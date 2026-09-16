# V2-35-B — **$L^5$ 逐幂生成树审计**（账本框架锁死版）

> 唐先生 2026-09-16 22:43 拍板：$\boxed{\mathrm{V2\text{-}35\text{-}B}：\ L^5\ \textbf{逐幂生成树审计}}$（**不是**"$PQ$ 分划优化"）✓
> 目标：$\boxed{\text{从 (4.26) 到 (4.29)，证明每一个}\ L^\alpha\ \text{究竟在哪一步第一次出现}}$✓

---

## 1. ⚠️ 三处修正（唐先生指定，必须遵守）

### 修正 1：$P,Q$ 是**离散结构坐标**，但"对 $P,Q$ 求和"完全正常
$$\textbf{不可写}：\ P,Q\ \text{被唯一决定} \Longrightarrow P,Q\ \textbf{不应} \text{出现在求和中}✓✓$$
$$\textbf{正确}：\ (n_1,n_2,\ell_1,\ell_2)\ \longleftrightarrow\ (n_1',n_2',\mathfrak p_1,\mathfrak p_2,\mathfrak q_1,\mathfrak q_2)\ \text{是}\ \textbf{带 gcd 分解的重新参数化}✓✓$$
$$\qquad\text{给定原始变量，}\ \mathfrak p_1=(\ell_1,n_1)、\mathfrak p_2=(\ell_2,n_1)\ \textbf{唯一确定}；\ \text{反之若把}\ \mathfrak p_i\ \textbf{当求和变量}，\ \text{须同时施加整除／互素条件，}\ \text{并允许不同原始}\ (n,\ell)\ \text{产生不同 gcd 数据}✓✓$$
$$\qquad\Longrightarrow\ \boxed{P,Q\ \text{是}\ \textbf{离散结构坐标}，\ \textbf{而不是自由优化参数}}✓✓$$

### 修正 2：$L^5$ 至少有**三个不同来源**（不可合并归因）
$$\textbf{来源 I（最外层}\ L\text{）}：\ \text{该}\ L\ \text{在进入四-}\ell\ \text{结构}\ \textbf{之前} \text{已存在} \Longrightarrow \boxed{\textbf{绝不能} \text{归因于"四个}\ \ell\text{"}}✓✓$$
$$\textbf{来源 II（四个}\ \ell\ \text{的求和）}：\ \text{形式上}\ \boxed{L^4}，\ \text{但经整除／}u／\text{同余／}\mathfrak p,\mathfrak q\ \text{参数化后}\ \textbf{并非简单保留裸}\ L^4 \Longrightarrow \text{须问}\ \boxed{L^4\ \xrightarrow{(4.26)\text{--}(4.29)}\ \text{什么精确幂次？}}✓✓$$
$$\textbf{来源 III（联合计数产生的}\ DL\text{）}：\ \boxed{\frac{DL}{\mathfrak q_1\mathfrak p_2}}\ \text{——目前}\ \textbf{最可疑的一层}✓✓$$
$$\qquad\text{因它来自}\ u\bigl(\tfrac Lu+1\bigr)\bigl(\tfrac{D}{u\mathfrak q_1\mathfrak p_2}+1\bigr)，\ \textbf{而不来自} \text{某个可自由选择的}\ P,Q✓✓$$

### 修正 3：**不能把 $D$ 和 $L$ 混为一谈**
$$D=\frac{3NL}{M}\ \Longrightarrow \text{最终看到的很多}\ L \Longrightarrow \textbf{须区分}\ \boxed{\text{显式}\ L}\ \text{与}\ \boxed{D\ \text{内含的}\ L}✓✓$$
$$D^2L^5=\Bigl(\frac{3NL}{M}\Bigr)^2L^5=9\frac{N^2}{M^2}L^7；\qquad \text{开方}\ DL^{5/2}=\frac{NL}{M}L^{5/2}=\frac{NL^{7/2}}{M}✓$$
$$\textbf{但 (4.31) 最终出现}\ \frac{L^{5/2}N}{M} \Longrightarrow \boxed{\text{从 (4.29) 到 (4.30)/(4.31)}\ \textbf{并非} \text{简单代入}\ D^2L^5}✓✓$$
$$\qquad\Longrightarrow\ \textbf{绝对不能} \text{仅凭 (4.29) 说"}\ L^5\ \text{有五个独立}\ L\text{"}✓✓\quad(\text{这正是第二刀须逐行的原因})✓$$

---

## 2. **L-来源矩阵**（待核版）
| 来源 | 数学动作 | 当前状态 |
|:--|:--|:--|
| $L_0$ | (4.26) 前已有因子 | **待核** |
| $L_\ell$ | $\ell_1,\ell_2,\ell_1',\ell_2'$ 求和 | **已知存在**（疑 $L^4$，须核每步实际幂） |
| $L_u$ | $u$-分解／同余类计数 | **待核**（用户指出：来自 $u(L/u+1)(D/(u\mathfrak q_1\mathfrak p_2)+1)$） |
| $L_d$ | $d,d'$ 范围 | **待核** |
| $L_{\mathfrak p,\mathfrak q}$ | gcd 坐标求和 | **待核**（修正 1：可求和，但非自由旋钮） |
| $L_D$ | $D=3NL/M$ 内含 $L$ | **可区分**（须与显式 $L$ 分开记） |
| $L_{\rm CS}$ | C--S 平方根 | **已知**：不产生完整新 $L$，而**改变幂次** |

$$\text{最终须得}\ \textbf{严格恒等账本}：\ \boxed{5\ =\ e_0+e_\ell+e_u+e_d+e_{pq}}✓✓\quad(e_i\ \text{为}\ \textbf{证明步骤产生的实际幂次}，\text{不是猜的})✓$$

## 3. 现有三行结构的 $L$-幂（初步读数，待逐行核）
$$\text{第 1 式}：\ \frac{\|\nu\|^2A^2\,\boxed{L^1}\,N^{3/2}M^\varepsilon}{\mathfrak p_1\mathfrak p_2}\operatorname*{\sum\sum\sum\sum}_{\ell_1,\ell_2,\ell_1',\ell_2'}\dots \Longrightarrow \text{显式}\ L^1\ +\ \text{四个}\ \ell\text{-求和}✓$$
$$\text{第 2 式}：\ \frac{\|\nu\|^2A^2\,\boxed{D L^2}\,N^{3/2}M^\varepsilon}{(\mathfrak p_1+\mathfrak q_1)\mathfrak p_1\mathfrak q_1\mathfrak p_2^2}\operatorname*{\sum\sum}_{\ell_2,\ell_2'}\frac{\boxed{DL}}{\mathfrak q_1\mathfrak p_2}\dots \Longrightarrow \text{两个}\ \ell\text{-求和已执行}＋\text{新因子}\ \tfrac{DL}{\mathfrak q_1\mathfrak p_2}✓$$
$$\text{第 3 式}：\ \frac{\|\nu\|^2A^2\,\boxed{D^2L^5}\,N^{3/2}}{\dots\mathfrak p_1\mathfrak q_1^2\mathfrak p_2^3\mathfrak q_2}\dots \Longrightarrow \text{四个}\ \ell\text{-求和全部执行}＋\text{分母}\ \mathfrak p_2\mathfrak q_2\ \text{因子}✓$$
$$\Longrightarrow\ \textbf{初步}：\ L^5=L^1_{(\text{显式，来源 I})}\times L^4_{(\text{四个}\ \ell\text{，来源 II})}\ \text{——}\ \textbf{但}\ \text{(4.29)}\to\text{(4.31)}\ \text{的幂次处理}\ \textbf{未核}✓✓$$

## 4. 判定（只允许三种结果，唐先生指定）
$$\boxed{\textbf{A}\ \text{真正存在可优化幂次}：\ \text{某步}\ L^\alpha\ \text{来自非必要上界且可严格换成}\ L^{\alpha-\delta} \Longrightarrow \boxed{\text{F5 出现新的实质攻击入口}}}✓✓$$
$$\boxed{\textbf{B}\ \text{每个幂次都有独立结构来源}：\ \text{如}\ L^5=L^4_\ell+L^1_{\rm unavoidable}\ \text{且}\ L^1\ \text{来自不可避免的同余／参数空间尺寸} \Longrightarrow \boxed{\text{F5 局部生成机制锁定}}}✓✓$$
$$\qquad(\textbf{但仍不能} \text{升级为 17/33 普适硬墙})✓$$
$$\boxed{\textbf{C}\ \text{幂次来源耦合，当前无法拆分} \Longrightarrow \mathrm{OPEN}}，\ \text{但至少知道下一步攻击哪个耦合}✓✓$$

## 5. ⚠️ 第三种危险形态（唐先生警告）
$$L^5=L^4\times L\ \text{若那个额外}\ L\ \textbf{不是一次粗计数}，\ \text{而}\ \textbf{是几个结构因素相乘} \text{恰好得到}\ L^{a_1}L^{a_2}\cdots=L✓✓$$
$$\qquad\Longrightarrow\ \text{攻击其中任一局部因子，}\ \textbf{可能被另一因子的变化抵消} \Longrightarrow \boxed{\textbf{"看见一个}\ L\ \textbf{就优化它"是错误的}}✓✓$$
$$\qquad\Longrightarrow\ \text{必须做}\ \textbf{净幂次账} \text{（与 V2-33 的纪律一致）}：\ \text{新自由度收益}-\text{C--S 成本}+\text{后续算术稀疏收益}✓✓$$

## 6. 残余（不得省略）
$$\text{残余 1（关键）：}\ (4.26)\text{--}(4.29)\ \textbf{原文未逐行核}（\text{本档为框架；已导出原文区段待核}）✓✓$$
$$\text{残余 2：每个}\ \ell\ \text{受整除／互素／同余条件影响的实际幂次未逐项算}✓$$
$$\text{残余 3：}u\ \text{-分解与}\ d\ \text{-范围的}\ L\ \text{贡献未单独归因}✓\quad\text{残余 4：}\ L_D\ \text{内含}\ L\ \text{与显式}\ L\ \text{的分离记账未完成}✓\quad\text{残余 5：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只做}\ L^5\ \text{逐幂溯源；}\quad\text{② }\textbf{不碰} \ F_5\ \text{envelope、}\textbf{不碰} \ P,Q\ \text{优化}；\quad\text{③ }\textbf{不} \text{宣布 A/B/C}；\quad\text{④ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) ⚠️ 三处修正已采纳（}P,Q\ \text{=离散结构坐标可求和；}L^5\ \text{三来源；}D\ \text{vs 显式}\ L\text{）}✓✓$$
$$\text{(ii) ⭐⭐ L-来源矩阵框架锁死（}L_0,L_\ell,L_u,L_d,L_{\mathfrak p,\mathfrak q},L_D,L_{\rm CS}\text{）＋恒等账本}\ 5=e_0+e_\ell+e_u+e_d+e_{pq}✓✓$$
$$\text{(iii) ⭐ 初步读数：}L^5=L^1_{(\text{来源 I})}\times L^4_{(\text{来源 II})}；\ (4.29)\to(4.31)\ \text{幂次处理未核}✓$$
$$\text{(iv) ⭐⭐ 三种判定 A/B/C＋第三种危险形态（净幂次账纪律）}✓✓$$
$$\text{(v) 原文区段已导出：}\ \texttt{BC\_sec4\_1\_3\_verbatim.txt}（30 KB）＋全文}\ \texttt{docs/ref-bc-ar5iv-plaintext.txt}✓✓$$
