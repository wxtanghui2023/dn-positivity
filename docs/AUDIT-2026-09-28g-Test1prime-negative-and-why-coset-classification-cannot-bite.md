# AUDIT-2026-09-28g — **Test-1′ 结果：负（$\Delta_{\rm orbit}{=}0$）＋ 为何 coset 分类不可能咬**

> **性质**：**实验/审计**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:40 ✓
> **唐先生令**：跑 Test-1′（$|C|{=}118$ 固定；$m{=}1$ 先，$m{=}2$；输出 $N_{\rm raw},N_{\rm orbit},N_{\rm compatible},\Delta_{\rm orbit}$；＋线性闭包测试）✓

**已查地图**：接续 `AUDIT-f`（Test-1：LP 层零增益）／`SUBSPACELP`（等号定理）／`WITFIB`·`WITW2C`（$k{=}1$ fiber 化 ＝ 精确重述）✓

D0: 本档对象 ＝ **档案已有**（coset 分布／Aut-orbit／整性——**无新数学对象** ✓）
D1: 0（产出＝**Test-1′ 负结果 ＋ 结构性否决理由** ⚠️）

---

## §0 结论（先给）

$$\boxed{\textbf{(1) 结构性否决}:\ \text{level-}m\ \text{之\ \textbf{完整 local state} ⟺ }C\ \textbf{双射（无归约）}}\ ⚠️✓$$
$$\boxed{\textbf{(2) 唯一有损归约 ＝ 只保留 coset \textbf{尺寸} } y_\alpha\ \Longrightarrow\ \text{约束\ \textbf{全为线性}}\ ⟹\ \textbf{无 orbit 层 incompatibility}}\ ✓✓}$$
$$\boxed{\textbf{(3) Test-1′ 负}:\ \Delta_{\rm orbit}=0\ \Longrightarrow\ \text{按唐先生判据 ⟹ 该 classification 亦为\ \textbf{同层重编码} ⟹ \textbf{KILL}}\ ✗}$$

## §1 ★ 结构性否决（**本档核心 ✓✓，一行论证**）

$$\text{分区}:\ \text{固定 }m\ \text{坐标} \Longrightarrow 2^m\ \text{个 coset，每个 } \cong\mathbb F_2^{\,n-m}$$
$$\text{每个 coset 内，codeword 由其 }(n{-}m)\ \text{位投影\ \textbf{唯一确定}（注入 ✓）}$$
$$\Longrightarrow\ \text{完整 state}=(P_\alpha)_{\alpha\in\mathbb F_2^m},\ P_\alpha\subseteq\mathbb F_2^{\,n-m}\quad\Longleftrightarrow\quad C\ \textbf{双射}\ ✓$$
$$\therefore\ \boxed{\text{level-}m\ \text{之"完整局部状态"\ \textbf{就是 }C\ \text{本身}} ⟹ \text{该层面\ \textbf{无归约}（＝原问题）}}\ ⚠️$$

## §2 size-level 实测（$K{=}118$ ✓）

| $m$ | $N_{\rm raw}$（线性 coset 覆盖约束） |
|---|---|
| $1$ | $\mathbf{31}$（$(a,b)$：$10a{+}b{\ge}512$、$a{+}10b{\ge}512$、$a{+}b{=}118$ ⟹ $a{\in}[44,74]$） |
| $2$ | $\mathbf{6220}$（$9y_\alpha{+}y_{\alpha\oplus e_i}{+}y_{\alpha\oplus e_j}{\ge}256$，$\forall\alpha$） |

## §3 线性闭包测试（**照唐先生 §5 ✓**）

$$\text{额外\ \textbf{非线性} 必要条件（}\texttt{WITFIB}\text{C-435）}:\ P_0{\cup}P_1\ \text{须为 9-cover} \Longrightarrow |P_0{\cap}P_1|\le K-62=56$$
$$\text{但 size-level}:\ |P_0{\cap}P_1|\le\min(a,b),\ \text{而实测 }\min(a,b)_{\min}=44\le56\ \Longrightarrow\ \textbf{自动满足}\ ✓$$
$$\therefore\ \boxed{\mathcal F_{\rm refined}^{\mathbb Z}=\mathcal F_{\rm linear}^{\mathbb Z}\ (m{=}1,2)}\ \Longrightarrow\ \text{按唐先生 §5 判据 ⟹ \textbf{KILL}}\ ✗$$

$$\text{Aut-orbit}:\ \operatorname{Aut}(Q_{10})\ \text{传递于坐标} \Longrightarrow m{=}1\ \text{全部 }(a,b)\ \text{同 orbit} \Longrightarrow N_{\rm orbit}{=}1;\ \Delta_{\rm orbit}{=}0\ ✓$$

## §4 ★ 为何 coset 分类**不可能咬**（**本档诊断 ✓✓**）

$$\text{coset 尺寸归约把\ \textbf{覆盖} 变成\ \textbf{线性计数}}:\ \text{每 cell 之覆盖需求}\ \le\ \text{各 cell 之尺寸线性组合}$$
$$\text{（}\texttt{SUBSPACELP}\ \text{等号定理（一切 }m\text{）：}L(m){=}\frac{2^n}{n+1}\ \text{恰等号 ⟹ 无间隙 ✓）}$$
$$\therefore\ \boxed{\text{尺寸层面\ \textbf{不可能} 产生 }s_i{\not\leftrightarrow}s_j\ \text{型 incompatibility}}\ ⚠️✓$$

**★ 由此可信推论（诚实标注 ⚠️，未证）**：Östergård–Blåss 之真正力量**不来自某一层的约束**（尺寸层线性、完整层＝$C$），而来自**递归分支（branch-and-bound）＋ 不等价类剪枝**——即**计算力**，非**新不变量** ✗。
$$\text{（与本项目纪律一致：solver 之 UNKNOWN ＝ 证据，非证明 ✓；本法若成功，产出为\ \textbf{certificate}，非新数学层 ⚠️）}$$

## §5 判定与建议

$$\boxed{\text{Test-1′ ＝ 负};\ \text{按唐先生判据 ⟹ coset-classification 路线\ \textbf{KILL}}\ ✗}$$
$$\text{（与 Test-1（LP 层 KILL）合：}\texttt{SUBSPACELP}\ \text{系 ＋ Test-1/1′ ⟹ }\boxed{\text{coset 层之\ \textbf{全部} 归约皆已否决}}\ ✓)$$

$$\text{尚存之真活口（若唐先生仍欲推进）}:\ \text{仅剩\ \textbf{计算型 certificate 路线}（非新不变量）}\ ⚠️$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "coset尺寸归约" "继承人结构" "计算力而非不变量"
技术词 coset尺寸归约  命中文件数=0    ::
技术词 继承人结构     命中文件数=0    ::
技术词 计算力而非不变量 命中文件数=0    ::
```

## §7 边界（硬 ✓）

- 有限穷举（$m{=}1,2$；$K{=}118$）＋ 一行双射论证 ＋ 既有档引证 ✓；**无新数学** ✗；**不加 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §4 之"计算力而非不变量"为**可信推论（未证）**⚠️，已显式标注；**不主张** Östergård–Blåss 已死 ✗
- §5 之"全部归约已否决"限于**本档已检验之 coset 族**，非"不存在任何归约"（V290 ✓）
