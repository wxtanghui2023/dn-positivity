已查地图：命中 `CLOSED-ROUTES-MAP.md:731/739/741`（0.68185 与 0.6725 出处）｜`lmzouri-vs-p27-mapping.md`｜`V302`/`V303` → 本档＝**出处审计**

# 🔍 出处审计：哪些是文献、哪些是我们的自推、哪些是自造元语言

> 起因：唐先生 2026-09-17 17:53 的坦率批评 ——
> 「**精确到小数点后六位的常数…在标准 RH 文献里我找不到对应出处**」「**'承重墙'、'NO-GO 商空间'、'N1–N7'、'两轴结构'、'防伪门' 是自造的元语言**」
> 「**22 项台账里真正被验证／攻击的其实是'这个框架内部是否自洽'**」
> 本档＝对该批评的**逐条自查**。级别代码：**[L]**＝文献可查 ｜ **[O]**＝我方自推（可复核但需读我方档）｜ **[M]**＝自造元语言（外部无对应物）

---

## §1 常数与定量的出处（逐条）

| 断言 | 级别 | 真实出处 | 外部可否独立复核 |
|:--|:--:|:--|:--|
| $0.68185$（带宽≤1 证书类天花板）| **[L]** | arXiv:2608.13637 Remark 1.1（附 Lean 形式化）| ✓ 直接查论文即可；**我方早已自标为外部引用**（`CLOSED-ROUTES-MAP:2598` 逐字："0.682 身份更正：**外部引用**…**非本项目自推** ⟹ 不再当'墙'（N3）"）|
| $0.6725$（Montgomery–Taylor 极值／$c_{MT}^{-1}\approx1.3275$）| **[L]** | Carneiro 等 Cor 14；前沿 §7.1 | ✓ 查 CCLM17 Cor 14 |
| **"$\lambda\le1\ \Longrightarrow\ G\le0.672501$"** | ⚠️ **[O]** | **我方** `V316`→`V302`→`V303` 的**变分推导**（$\lambda\le1$ 是无条件证书的带宽参数）| ⚠️ 需读我方变分设定；**且 V301 版曾被我们自己撤回**（"$\Delta_\phi=O(1)$ 操作子分支"）⟹ 数字稳定性有自我更正史 |
| $\Lambda\ge0$（de Bruijn–Newman）| **[L]** | Rodgers–Tao, Forum Math. Pi 8 (2020) | ✓ |
| $\Lambda\le0.2$ | **[L]** | Polymath15 | ✓ |
| $\Lambda\le0.1787854$ | ⚠️ **[未核-第三方]** | 博客（Gomila, 2026-08-19，计算机辅助）| ✗ 未同行评议 |
| $|\delta_T|\asymp(\log T)^{1.0}$；分辨率地板 $\beta-\tfrac12\gtrsim0.15$ | ⚠️ **[O]** | 我方 `GAP-2` 数值（筛至 $10^7$）| ⚠️ 可复核**若**公布脚本与数据 |
| 素数侧 44 倍余量（$32.96$／$2.3982\times10^4$ vs $1.063\times10^6$）| ⚠️ **[O]** | 我方 `E92` | ⚠️ 同上 |
| Guth–Maynard 改进窗口 $N^{7/10}\lesssim V\lesssim N^{8/10}$ | **[L]** 定理 ＋ **[O]** 窗口推导 | GM Theorem 1.1；窗口为**我方**从两条交叉推出的 | ✓ 定理可查；窗口需重算 |

$$\Longrightarrow \textbf{结论}：\text{最高精度的几个常数中，}\ 0.68185／0.6725／\Lambda\ \text{相关}\ \textbf{有文献}✓；\ \text{而}\ \textbf{"}\lambda\le1\Rightarrow0.672501\text{" 这一条}\ \text{是}\ \textbf{我方自推}，\ \text{且带自我更正史}✓$$

## §2 自造元语言清单（**[M] 级**，外部无对应物）—— 唐先生批评属实
$$\textbf{[M]}\ \text{"承重墙"／"三面一墙"／"NO-GO 商空间"／"N1--N13 机制母类"／"两轴结构"／"防伪门"／"攻击·穿透·封口"／"墙体 W1--W12·难题 D1--D10"／"✓✓ 标记"}$$
$$\qquad ⚠️\ \text{且我方档案}\ \textbf{自己就记过}\ \text{这些是}\ \textbf{未证断言}：$$
$$\qquad\qquad \text{•}\ \text{"三面一墙"}\ \text{已由我方降级为}\ \textbf{待核}（\text{REVIEW-E4-FINAL §0；}\texttt{RESEARCH-CONSTITUTION:932}\ \text{"同一道墙"待核}）✓$$
$$\qquad\qquad \text{•}\ \text{"类表完整性"}\ \text{我方反复声明}\ \textbf{未证}（\text{"不证明类表完整，§E.4 仍开"}）✓$$
$$\qquad\qquad \text{•}\ \text{"唯一还活着的墙"}\ \text{一类措辞}\ \text{＝}\ [\textbf{M}]\ \text{级叙事，}\ \text{无数学内容}✓$$
$$\Longrightarrow \boxed{\text{唐先生的判断成立}：\ \text{这套元语言}\ \textbf{只在项目内部自洽}，\ \textbf{未被外部检验}✗✓}$$

## §3 "22 项台账验证了什么"—— 唐先生批评亦属实
$$\text{台账 22 项中，}\ \textbf{外部可判} \text{的仅有：}\ \text{文献条目（W1-lamzouri、W12-ceiling、W9-AKS）}\ \text{与}\ \text{少数可复算数值（E92、GAP-2）}✓$$
$$\qquad \text{其余大多数}\ \text{＝}\ \textbf{"该框架内该路已封闭"} \text{——}\ \text{与"RH 的某子命题成立／不成立"}\ \textbf{是两件事}✗✓$$
$$\qquad ⚠️\ \text{诚实补充}：\ \text{框架}\ \textbf{确有自我更正机制} \text{（V301 撤回、W9 撤回、FPCA 更正、今日"修正 B"撤回…）}\ \text{——这是优点，但}\ \textbf{自更正}\ \ne\ \textbf{外部验证}✓$$

## §4 建议的处置（依唐先生 17:53 两条建议）
$$\textbf{(E1)}\ \text{挑}\ \textbf{最具体、最可判定} \text{的一条断言，}\ \textbf{剥叙事} \text{写成标准数学陈述} \Longrightarrow \text{已做：}\ \texttt{docs/EXTERNAL-REVIEW-1-BC-reciprocity-claim-standalone.md}✓$$
$$\textbf{(E2)}\ \text{找}\ \textbf{完全未参与本项目、未见编号史} \text{的人复核} \text{——}\ \text{此项}\ \textbf{只能由唐先生执行}（\text{我无法联络外部专家}）✓$$
$$\qquad ⚠️\ \text{对 (E2) 的诚实提醒}：\ \text{应先给的}\ \textbf{不是} \text{22 项台账，而是 (E1) 那种}\ \textbf{单页、无编号、无叙事} \text{的陈述}✓$$

## §5 边界
$$\text{(i)}\ §1\ \text{全部依据档案逐字}（\texttt{N13} 已执行）✓✓；\ \text{级别判定为}\ [\textbf{结构}]\ \text{级自查}✓$$
$$\text{(ii)}\ \textbf{未用 RH}；\ \textbf{零数值}；\ \text{本档}\ \textbf{不新增数学}✓✓$$
