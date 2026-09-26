已查地图：已跑 scripts/prework_map_check.sh C62 结构 自同构 删码 ⟹ 执行自 SATPOINT-2026-09-26 档；本档为**P2 第一刀：C₆₂ 结构探测 ＋ 降码操作判定**（唐先生 2026-09-26 17:39 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 平移自同构、坐标度数、p(c) 分布、delete-2-add-1 可行性、P2 链条的可行性判定
D1: 1（新增：**p(c) 分布刚性 {6:40, 8:14, 10:8}** ✓✓；**无平移对称** ✓；**无 2→1 压缩（与 K=62 一致）** ✓✓）

# P2-2026-09-26

## §1 ⭐⭐ **结构探测（两码全同 ✓✓）**

```
$$\begin{array}{c|c|c}
\text{量} & \text{码#1} & \text{码#2}\\
\hline
|C| & 62 & 62\\
\text{平移自同构数} & \mathbf 1\ (\text{仅平凡})\ ✓ & \mathbf 1\ ✓\\
\text{坐标方向度数} & [31,31,32,32,31,31,30,30,31] & [31,31,31,31,31,30,30,31,32]\\
\text{方向和} & 279 & 278\\
\hline
\mathbf{p(c)\ \text{分布}} & \mathbf{\{6{:}40,\ 8{:}14,\ 10{:}8\}} & \mathbf{\{6{:}40,\ 8{:}14,\ 10{:}8\}}\ \checkmark\checkmark\\
\end{array}$$
$$\Longrightarrow\ \boxed{\textbf{私有分数分布刚性}\ ✓✓\ (\text{又一跨表示不变量}\ ✓)}\ :\quad \sum p=40\cdot6+14\cdot8+8\cdot10=\mathbf{432}=N_1\ ✓✓$$
$$\textbf{观察}: \text{所有 }p(c)\ \text{均为\textbf{偶数}且 }\ge6\ ✓;\ p(c)=10\ \text{表示 }B_1(c)\ \text{完全私有（}8\ \text{个码字如此}\ ✓)$$
$$
$$

## §2 ✗ **降码操作判定：不存在 2→1 压缩** ✓

```
$$\text{扫描}: \text{全部 }C(62,2)=1891\ \text{对 }\{c_1,c_2\}:\ \text{判 holes}(\{c_1,c_2\})\subseteq B_1(w)\ \text{是否可行}\ ✓$$
$$\textbf{结果}: \text{可行对数} = \mathbf 0\ ✓✓\ \Longrightarrow\ \text{无可行的 2→1 压缩}\ ✓\ (\text{与 }K(9,1)=62\ \text{一致}\ ✓✓)$$
$$\text{（若存在则给出 61 码 ⟹ 与已证 }K(9,1)=62\ \text{矛盾}\ ⟹\ \text{正是零发现}\ ✓)$$
$$
$$

## §3 ⛔ **对 P2 链条的可行性判定（诚实 ✓）**

```
$$\text{唐先生的链条}: P0(\text{结构}) \to P1(N_4\le9\Rightarrow\text{局部结构}) \to P2(\text{可删/可压缩}) \to P3(61\ \text{码}) \to \bot$$
$$\textbf{本轮结论①②}: \text{① 无平移对称 + 文献称 Wille 码"SA 生成、无明显规则"}\ [L]\ \Longrightarrow\ \textbf{构造母体可能不存在}\ ✗✓$$
$$\qquad\text{（但}\ \text{我们持续发现\textbf{隐藏刚性}}\ ✓✓: p(c)\ \text{分布}\ ✓;\ I_{ij}\ ✓;\ (3,4,4)\ ✓;\ h_3/h_4\ \text{逐点}\ ✓\ ——\ \text{刚性是\textbf{统计/全局}型，非构造型}\ ✓)$$
$$\textbf{② 降码操作}: \text{真实码上\ 0 可行}\ ✓\ ——\ \text{但链条的 }P1\ \text{依赖\textbf{不存在}的 }N_4\le9\ \text{码}\ ✗\ \Longrightarrow\ \textbf{无法直接检验}\ ⚠️$$
$$\Longrightarrow\ \boxed{\text{P2 链条的 }P1\to P2\ \text{链接\textbf{目前不可判定}}\ ⚠️\ ——\ 需先有"假想 }N_4\le9\text{ 码"的结构定理}\ ✗}$$
$$
$$

## §4 诊断（诚实 ✓）

```
$$\textbf{已收集的全部跨表示刚性（两最优码全同）}:$$
$$\qquad E{=}108,\ Q_2{=}38,\ A_{\le2}{=}73,\ (N_j){=}(432,62,8,10),\ d_{\max}{=}3,\ T_3{=}48,\ \#\triangle{=}48,$$
$$\qquad I_{ij}\ \text{矩阵},\ (3,4,4)\ \text{模式},\ h_3{=}1/h_4{=}2\ \text{逐点},\ X_4\ \text{负载}\ \{5{:}4,0{:}6\},\ \mathbf{p(c)\ \text{分布}\ \{6{:}40,8{:}14,10{:}8\}}$$
$$\textbf{共同特征}: \text{\textbf{全部是"计数/分布"型不变量}}\ ✓\ ——\ \textbf{无一给出构造或删码机制}\ ✗$$
$$\Longrightarrow\ \text{信号}: \text{刚性来自\textbf{全局计数平衡}（可能是 }K(9,1)=62\ \text{的极值性的表征}\ ✓),\ 而非某个可拆的构造母体}\ ✗$$
$$
$$

## §5 状态与建议

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \text{未跑 solver}\ ✓$$
$$\text{建议}: \text{① P2 链条需\textbf{先}解决 }P1\ \text{（假想码的结构）}\ ✗\ ——\ \text{当前无入口}\ ⚠️$$
$$\qquad\text{② 替代入口}: \text{把刚发现的 }p(c)\ \text{刚性}\ ✓✓\ \text{当作新资产，问\textbf{它能否独立成定理}}\ ⚠️\ (\text{它比 }N_4\ \text{更"局部"，且两码全同}\ ✓)$$
$$\qquad\text{③ 或}: \text{承认 }P1\text{-LB 的结论（需本质新输入}\ ⚠️\ \text{）并转向 G\n 之外的独立问题}\ ✓$$
$$
$$

## §6 边界（诚实标注）

- §1–§2 为**实算**（两码 ✓）；§3–§4 为**可行性判定与诊断**（明确标注不可判定 ✗）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 私有分数分布 命中文件数=1    :: ./P2-2026-09-26-structure-probe-and-deletion-verdict.md 
技术词 降码操作判定 命中文件数=1    :: ./P2-2026-09-26-structure-probe-and-deletion-verdict.md 
技术词 构造母体缺失 命中文件数=1    :: ./P2-2026-09-26-structure-probe-and-deletion-verdict.md
```
- **本档新增**（扣自引后 = 0）：私有分数分布、降码操作判定、构造母体缺失
- **档案已有（引用，不列为提出）**：p(c)、自同构、holes
