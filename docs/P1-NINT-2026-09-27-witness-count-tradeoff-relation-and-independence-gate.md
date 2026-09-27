# P1-NINT-2026-09-27 — **$N_{\rm int}$ 的 P1 micro-check**：折衷关系（新 ✓✓）＋ 独立性闸 PASS（但使用仍缺输入 ⚠️）

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 23:19 令 ✓）**：① 定义 $N_{\rm int}$ 类量；② 检验 covering 能否给它**独立新约束**；③ 过**独立性闸**；零程序计算 ✓；**不升级任何短名单项** ✓。

**已查地图：命中（接续 C-418／P1-G2／P1-D4b，非新案 ✓）**
`docs/P1-SCREEN-2026-09-27-…`（**C-418 预筛门** ✓✓）｜`docs/P1-G2-2026-09-27-…`（**见证者分解（情形 A／B）** ✓✓）｜`docs/P1-D4b-2026-09-27-…`（**内部 weight-4 逃逸合法** ✓✓）｜`docs/P1-D3-2026-09-27-…`（**被迫高层码字定理** ✓✓）｜`docs/P1-AVOID-…`／`docs/R7-LOCK-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，**已分线**，见 §6）
D0: 本档对象 ＝ **档案已有** $N_{\rm int}$／见证对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $d_4$ 与内部块数的\*\*折衷关系\*\* ＋ 其隐含容量界的一致性核验 ＋ 独立性闸判定** ✓）
**[RESEARCH]**

---

## §0 结论（**折衷关系新 ✓✓｜独立性闸 PASS ✓｜使用仍缺输入 ⚠️**）

$$\boxed{\textbf{(2) ★折衷关系（新 ✓✓）}:\ \text{设 }b_j:=\#\{y\in C:d(c,y)=4,\ |S_y\cap S(c)|=j\}\ (j=0..4)\ \text{（块级分类 ✓）} \Longrightarrow \boxed{b_3+4b_4\ \ge\ \binom{s(c)}3}}$$
$$\qquad\Longrightarrow\ \boxed{d_4(c)\ \ge\ \max\Big(b_4,\ \binom{s(c)}3-3b_4\Big)}\ ✓✓\ \big(\text{＝本线的\textbf{第一条排列级}下界 ✓}\big)$$
$$\qquad\textbf{（一致性核验 ✓）}:\ \text{该式\textbf{蕴含}容量界}\ \lceil\binom{s}3/4\rceil✓\ \big(\text{若 }b_4\le\binom s3/4:\ \text{RHS}\ge\binom s3-3\binom s3/4=\binom s3/4✓;\ \text{否则 RHS}=b_4>\binom s3/4✓\big)$$
$$\boxed{\textbf{(3) 独立性闸 PASS ✓}:\ b_4,b_3\ \text{属\textbf{排列级}（度数只见 }d_4(c)\ \textbf{总数}、不见其分裂 ✓）} \Longrightarrow \textbf{非 profile 决定}✓;\ \text{且该关系与\textbf{覆盖条件直接绑定}（见证需求 ✓）}}$$
$$\boxed{\textbf{(4) ⚠️ 诚实（关键）}:\ 使用该关系\textbf{仍需 }b_4\ \text{的输入}✗;\ \text{而 avoidance（逃逸 ✗ P1-D4b）与容量（profile ✗ C-409）\textbf{都不提供} ⟹ \textbf{门 PASS ＋ 关系成立，但"对 119 的新约束"仍未得}⚠️}$$

---

## §1 **定义**（**两级 ✓**）

$$\textbf{块级 ✓}:\ \text{对 }c\in C,\ \text{记其 weight-4 邻居 }y=c\oplus S_y\ (|S_y|=4✓);\ \textbf{分类} b_j:=\#\{y:\ |S_y\cap S(c)|=j\}\ (j=0,\dots,4)✓;\ \sum_jb_j=d_4(c)✓$$
$$\qquad\text{每块覆盖的 forced 三元数 }=\binom{|S_y\cap S(c)|}3\ \big(=0,0,0,1,4\ \text{对 }j=0,\dots,4✓\big)\ \Longrightarrow\ \text{仅 }b_3\ \text{贡献 1／块 ✓、}b_4\ \text{贡献 4／块 ✓}$$
$$\textbf{三元级 ✓}:\ N_{\rm int}(c):=\#\{T\subseteq S(c),|T|=3:\ T\ \text{有}\textbf{内部见证}（S\subseteq S(c)✓）\}\ \le\ 4b_4✓;\qquad \text{总 forced 三元数}=\binom{s(c)}3✓$$

## §2 **折衷关系的推导**（**＋ 一致性核验 ✓✓**）

$$\text{forced 情形（P1-D3／P1-G2 ✓）}:\ T\subseteq S(c),\ |T|=3\ \Longrightarrow\ x_T=c\oplus e_{(T)}\notin C\ \big((\alpha)✓\big),\ \text{其 3 个 weight-2 邻居}\notin C\ \big(A(c)=0✓\big)$$
$$\qquad\Longrightarrow\ x_T\ \text{须由 weight-4 见证 }y=c\oplus S_y\ (T\subset S_y✓)\ \text{覆盖}✓;\ \text{而 }y\ \text{覆盖的 forced 三元}\ T\ \text{满足}\ T\subseteq S_y\cap S(c),\ |T|=3\ \Longrightarrow\ \binom{|S_y\cap S(c)|}3\ \text{个}✓$$
$$\qquad\Longrightarrow\ \sum_y\binom{|S_y\cap S(c)|}3=b_3+4b_4\ \ge\ \binom{s(c)}3\ ✓✓\ \big(\text{每个 forced 三元至少被覆盖一次 ✓}\big)$$
$$\qquad\Longrightarrow\ b_3\ge\binom s3-4b_4\ \text{且}\ d_4=b_0+b_1+b_2+b_3+b_4\ge b_3+b_4\ \Longrightarrow\ \boxed{d_4(c)\ \ge\ \max\Big(b_4,\ \binom{s(c)}3-3b_4\Big)}\ ✓✓$$
$$\textbf{（为何 max ✓）}:\ \text{两支}\ b_4\ \text{与}\ \binom s3-3b_4\ \text{分别来自"每块至少覆盖自身"与"覆盖需求"}\ ✓;\ \text{取大者 ✓}$$

## §3 **独立性闸**（**PASS ✓✓**）

$$\textbf{排列级论证 ✓}:\ \text{度数信息 }\{(d_j(c))\}_j\ \text{只含 }d_4(c)=\sum_jb_j\ \big(\textbf{总数}✓\big)\ \textbf{不含分裂}\ (b_0,\dots,b_4)✓$$
$$\qquad\text{而分裂由"\textbf{哪些} 4-集恰是码字"决定 ⟹ \textbf{排列级}✓⟹ 非 degree-profile 函数 ⟹ \textbf{过 C-418 门 ＋ 过独立性闸}✓✓}$$
$$\textbf{（示例 ✓）}:\ \text{取 }s(c)<10\ \text{（则 }S(c)\subsetneq[10]✓\big);\ \text{同样 }d_4(c)=D\ \text{下，块可全部落在 }S(c)\ \text{内}\ (b_4=D✓)\ \text{或全部跨出}\ (b_3=D✓)\ \text{—— 覆盖需求随之不同 ✓✓}$$
$$\qquad\text{（注 ✓）}:\ s(c)=10\ \text{时分裂\textbf{退化}（一切 weight-4 块皆 }b_4✓\big)\ \Longrightarrow\ \text{门的咬合只在 }s<10\ \text{时生效 ✓}$$

## §4 **诚实边界**（**⚠️ 必须写 ✓**）

$$\textbf{关系本身 ✓}:\ \S2\ \text{的折衷式\textbf{不是}度数的函数 ✓（排列级 ✓）⟹ \textbf{不是} profile 恒等式的重述 ✓✓\ \text{—— 这是本档的实质进展 ✓}$$
$$\textbf{但它不能被"独立使用" ✗}:\ \text{要用它约束 119-cover，须有 }b_4\（\text{或 }b_3\text{）\textbf{的输入}⚠️;\ \text{现有两条来源皆不提供}:$$
$$\qquad\text{① avoidance 侧}:\ \text{内部块\textbf{合法}（P1-D4b 显式反例 ✓）} \Longrightarrow \text{不能用 avoidance 界 }b_4\ ✗✓$$
$$\qquad\text{② 容量／度数侧}:\ \text{与 }\{n_j\}\ \text{同源（C-409 ✓）} \Longrightarrow \text{不给排列级信息} ✗✓$$
$$\Longrightarrow\ \boxed{\text{门 PASS ＋ 关系成立，但"119-cover 的新数学约束"\textbf{仍未获得}}⚠️\ \big(\text{照唐先生 23:19 的判据：若最终只得到可由总覆盖／度数账本恢复的式子 ⟹ 闸 STOP ✓}\big)}$$
$$\textbf{（当前判定 ✓）}:\ \text{折衷式\textbf{不}是"可由账本恢复"的式子 ✓（故未触发 STOP ✓）};\ \text{但它\textbf{悬空}——缺 }b_4\ \text{的独立估计 ⚠️} \Longrightarrow\ \textbf{C-418 门保持 PASS、后续仍 HOLD}✓$$

## §5 状态锁（**照唐先生 23:19 ✓**）

$$\boxed{\textbf{现状}:\ \text{C-418 ＝ 筛选器已成立 ✓};\ N_{\rm int}\ \text{＝第一候选 ✓};\ \textbf{尚无新数学约束}✗;\ \textbf{119 主问题仍完全 LIVE}✓}$$
$$\textbf{未升级 ✓}:\ \textbf{不}把任何短名单项提前升级成 closure／NO-GO ✗（照令 ✓）；**未改** closure gate／nogo gate ✗$$
$$\textbf{优先级（照令 ✓）}:\ N_{\rm int}(c)\ \longrightarrow\ G_2(C)\ \text{的谱接口}\ \longrightarrow\ \text{见证超图}✓;\ \text{每项须先过 C-418 门 ＋ 独立性闸 ✓}$$

## §6 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "见证计数" "块分类" "折衷关系" "独立性闸"
技术词 见证计数      命中文件数=3    :: ./ASSETS-REGISTRY.md ./WILLE-4-ITEMS-2026-09-26-extremal-conjecture-EXT-L.md ./P1-SCREEN-2026-09-27-C418-pre-screen-gate-and-first-pass.md
技术词 块分类        命中文件数=0    ::
技术词 折衷关系      命中文件数=0    ::
技术词 独立性闸      命中文件数=11   :: ./V271-non-cylinder-carrier-five-conditions-and-certificate-impossibility.md ./V272-certificate-barrier-hypothesis-minimization-and-branch-II-verdict-type.md ./V274-cell-existence-nontrivial-cylinder-nonzeta-local-and-V270-erratum.md
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 见证计数 | 2（`ASSETS-REGISTRY.md`／`P1-SCREEN-…` ✓） | 1（`WILLE-4-ITEMS-…` **未定 ⟹ 不计** ✗） | 0（既有词 ✓） |
| 块分类 | 0 | 0 | 0（本档自造标签 ✓） |
| 折衷关系 | 0 | 0 | 0（本档自造标签 ✓） |
| 独立性闸 | 0（共享档 `CLOSED-ROUTES-MAP`／`MASTER-STATUS` 不计 ✗） | 11（`V271`／`V272`／`V274`／`REVIEW-2026-09-16`／`STRATEGY-2026-09-16` 等 **空间 A** ✗） | 0（既有词 ✓） |

- **本档新增**：**0** 个术语 ✓（`块分类`／`折衷关系` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`见证计数`／`独立性闸` 的**本线命中**皆既有 ✓）
- **注 ✓**：本档实质＝**§1 定义 ＋ §2 折衷关系 ＋ §3 独立性闸 ＋ §4 诚实边界**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§6 已分栏 ✓）
- **本档未产生对 119 的新数学约束** ✗（诚实 ✓）；**不声称** P1 成立 ✗（V290）；**不升级**短名单项 ✗（照令 ✓）
- §4 的"折衷式悬空（缺 $b_4$ 输入）"**必须保留** ✓（防把关系误读为已可用的约束 ✗）
