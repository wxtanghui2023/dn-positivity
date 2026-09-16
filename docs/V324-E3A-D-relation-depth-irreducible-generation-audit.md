# V324 / E3-A-D — **不可约生成深度**类 $\mathfrak d$ 的审计

> 唐先生 2026-09-16 17:13 指定。纪律：**不搜索"新的数值不变量"，而搜索"动态结构本身产生的不可压缩量"**。
> 范围：**只审「关系深度／不可约生成深度」这一类**；**不扩大搜索**；**不提前判死**。

---

## 1. D3 精确化（D3.1–D3.8）
$$\begin{aligned}
D3.1&\quad \mathfrak d_T\ \text{由}\ O_T\ \textbf{的内部结构} \text{定义，而非外加计数器}\\
D3.2&\quad T<T'\Rightarrow\mathfrak d_T\le\mathfrak d_{T'}\\
D3.3&\quad \exists T<T':\mathfrak d_T<\mathfrak d_{T'}\\
D3.4&\quad \mathfrak d\ \text{不是}\ \text{support/cardinality/zero-count/correlation}\\
D3.5&\quad \mathfrak d\ \text{不是}\ \text{有限证书长度或计算复杂度}\\
D3.6&\quad \mathfrak d\ \text{不来自}\ \text{有限阶局部核}\\
D3.7&\quad \mathfrak d\ \text{的增长不能等价改写成}\ \text{bandwidth demand}\\
D3.8&\quad \mathfrak d_{T'}-\mathfrak d_T\ \text{必须是}\ \textbf{新的结构性 defect}，\text{而非"多加入了一些对象"}
\end{aligned}$$

## 2. 第一候选批：关系复杂度（交换 defect）—— **DEAD**
$$\Delta_T：＝\operatorname{Def}(A_T,M_T),\quad A_T=\text{加法闭包},\ M_T=\text{乘法闭包}$$
$$\textbf{吸引力}：\text{天然动态；}\text{非简单支持大小}。\quad\textbf{撞墙}：$$
$$\text{V241}：\text{所有 dilatation 生成元}\ T_p\ \text{彼此交换（}T_pT_q=T_qT_p\text{）} \Longrightarrow \Delta_T\ \text{为}\ \textbf{trivial coboundary}$$
$$\qquad\text{（并 V284 五族全败：}[D,U]\ \text{型算子退回熟悉算术量）} \Longrightarrow \boxed{\Delta_T=0\ \text{或本质等价于已有 coboundary}\ \Rightarrow\ \mathrm{DEAD}}$$

## 3. 第二候选批：关系空间的新自由度 —— **暂不 ALIVE（未证新颖）**
$$\mathcal R_T：＝\{\text{截至尺度}T\ \text{可由自然算术关系生成的关系空间}\},\quad \mathfrak d_T：＝\dim\frac{\mathcal R_{T'}}{\mathcal R_T}\ (\text{或最小关系阶数／生成元独立度})$$
$$\mathcal R_T\subsetneq\mathcal R_{T'}\ \text{确实可出现，但须立刻检查是否偷换名}：$$
$$\text{若独立度}\ =\ \text{新素数／新支撑／新关系数量}\ \Longrightarrow \text{cardinality/support}\ \to\ \text{旧类}\ \mathrm{DEAD}$$
$$\text{若只看}\ \text{有限阶关系}\ \Longrightarrow\ \text{V294-A}\ \mathrm{DEAD}\ (\text{有限阶局部核聚合增益}\le0)$$
$$\text{若最小关系长度增长}\ \Longrightarrow\ \text{certificate/complexity}\ \to\ \text{V259/V271}\ \mathrm{DEAD}$$
$$\text{若关系空间最终当谱空间用}\ \Longrightarrow\ \text{易变}\ \text{V317 feasible-domain}\ \mathrm{DEAD}$$
$$\Longrightarrow\ \boxed{\text{未证新颖，暂不 ALIVE}}$$

## 4. 第三候选批：**不可约关系深度**（本档主审对象）

### 4.1 定义（唐先生原式）
$$\mathcal R_T^{(0)}\subset\mathcal R_T^{(1)}\subset\cdots,\qquad \mathcal R_T^{(k+1)}=\operatorname{Cl}\bigl(\mathcal R_T^{(k)}\bigr)\quad(\operatorname{Cl}\ \text{由}\ \textbf{预先固定的自然算术操作}\ \text{给出})$$
$$\delta_T(r)：＝\min\{k:r\in\mathcal R_T^{(k)}\}\ (\text{不存在则}\ \infty)；\qquad \boxed{\mathfrak d_T：＝\sup\{\delta_T(r):r\ \text{是}\ T\ \text{新出现且此前不可推出}\}}$$
$$\textbf{关键}：\text{它}\ \textbf{暂时未被 V294-A 直接杀}（\text{非核矩、非局部相关、非 bandwidth}）✓$$

### 4.2 三种实现逐一审计（本档核心）
$$\textbf{(甲) 实现＝推导长度}：\delta_T(r)\ \text{是}\ \textbf{表示的词长度} \Longrightarrow \textbf{依赖生成元选取}（\text{换较短的表示即得较短的推导）$$
$$\qquad \Longrightarrow \text{展示依赖／}\textbf{非呈现无关} \Longrightarrow \text{落 complexity} \Longrightarrow \text{D3.5 违反}\ \to\ \textbf{V259/V271}\ \mathrm{DEAD}\ ✗$$
$$\textbf{(乙) 实现＝闭包格的链长型不变量}（\text{最长严格上升链}\Longrightarrow\text{Noether 维数}）；\text{结构性}\ ✓，\text{但}：$$
$$\qquad \text{此类量为}\ \textbf{指标型／上同调型}；\ \text{而 V211 §5 的排除表明确列出"}\textbf{非指标}\text{"}\Longrightarrow \textbf{指标型已属已分类} \to\ \text{旧类}\ \mathrm{DEAD}\ ✗$$
$$\textbf{(丙) 关键退化（本档给出）}：\text{对算术闭包操作}\ (+,\times,\text{局部化},\text{商化})，\text{由"素数}\le T_0\ \text{的关系"推出"涉及素数}\le T\ \text{的新关系"所需深度，}$$
$$\qquad \text{与}\ \textbf{从}\ T_0\ \text{传播到}\ T\ \text{的步数同阶} \Longrightarrow \delta_T\ \textbf{与传播／支撑扩散不可分离} \Longrightarrow \text{撞第 2 行}\ \to\ \textbf{V162/V295}\ \mathrm{DEAD}\ ✗$$
$$\text{理由（本档论证）}：\operatorname{Cl}\ \text{若由有限元算术操作生成，则}\ \delta_T(r)\ \text{被}\ r\ \text{的项结构深度控制，}$$
$$\qquad \text{而项结构深度在算术闭包下}\ \textbf{随支撑尺度单调增长} \Longrightarrow \text{不可与"传播"分离。}\qquad\textbf{[结构判定]}$$

### 4.3 唐先生锋利判定表（逐行落座）
$$\boxed{\begin{array}{ccl}
\text{只是关系数量}&\Rightarrow&\text{旧类}\ \mathrm{DEAD}\\
\text{只是传播步数}&\Rightarrow&V162/V295\ \mathrm{DEAD}\\
\text{有限阶关系深度}&\Rightarrow&V294\text{-A}\ \mathrm{DEAD}\\
\text{证书/算法复杂度}&\Rightarrow&V259/V271\ \mathrm{DEAD}\\
\text{真正不可约的动态关系深度}&\Rightarrow&\text{继续}\ D4
\end{array}}$$
$$\text{本档审计：}\text{(甲)}\to\text{第 4 行；}\text{(乙)}\to\text{旧类（指标型）；}\text{(丙)}\to\text{第 2 行；}\text{§2 交换 defect}\to\text{旧类；}\text{§3 关系空间维度}\to\text{第 1／3／4 行（分情形）}$$
$$\Longrightarrow\ \textbf{第五行（真正不可约）}\ \textbf{仍无实例}。$$

## 5. 关键检验（须显式通过才算活）
$$\text{对任何候选}\ \mathfrak d，\text{须找到}\ \mathfrak d_{T'}>\mathfrak d_T，\text{且}\ \boxed{\mathfrak d_{T'}-\mathfrak d_T\ \neq\ \text{finite propagation／bandwidth demand}}$$
$$\text{若做不到}\ \Longrightarrow\ \mathrm{DEAD}；\ \text{若做到}\ \Longrightarrow\ \text{第一次出现}\ \textbf{动态增长}\neq\text{局部核聚合}\neq\text{带宽需求}\ \text{的东西} \Longrightarrow\ \text{才轮到}\ D4$$

## 6. 本轮判定（**不提前判死**）
$$\textbf{本档不宣布 E3-A DEAD}：\text{审计为}\ \textbf{逐情形诊断}，\text{非"必然退化"的证明}；$$
$$\qquad \text{四类已识别实现（§2／§3／§4.2 甲乙丙）}\ \textbf{全数坍缩}；\ \text{第五行仍无实例}\ \Longrightarrow\ \text{记作}\ \textbf{未找到，而非不存在（N1/N2）}；$$
$$\textbf{若须收口，所需的是}\ \textbf{退化性证明}：\text{证明任何由有限元算术闭包操作生成的}\ \delta_T\ \text{必与传播／复杂度／指标型之一同阶}；$$
$$\qquad \text{该证明}\ \textbf{本档未给出}（\text{仅给出 §4.2(丙) 的论证骨架}）\Longrightarrow\ \textbf{E3-A 保持 ALIVE 但无实例}。$$

## 7. 边界（N1/N2 严守）
$$\text{① 本档}\ \textbf{只审一类}（\text{关系深度／不可约生成深度}），\text{不扩大搜索}；$$
$$\text{② §4.2(丙) 为}\ \textbf{[结构判定]}，\text{非定理}；\quad\text{③ V241／V284／V294-A／V295／V259／V271／V211 为档案既有结论，}\textbf{未逐行重验}；$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 8. 净产出
$$\text{(i) D3.1–D3.8 精确化；}\quad\text{(ii) 三批候选（交换 defect／关系空间维度／不可约深度）逐一批审；}$$
$$\text{(iii) §4.2 给出不可约深度的}\ \textbf{三种实现}：\text{(甲) 推导长度}\to\text{复杂度；(乙) 链长型}\to\text{指标型旧类；(丙) 与传播同阶（论证骨架）}；$$
$$\text{(iv) }\textbf{第五行无实例} \Longrightarrow \text{E3-A 保持 ALIVE 但无实例；判死需退化性证明（未给出）}。$$
