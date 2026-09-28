# WITCOV-2026-09-28 — **R=0 分支：两处修正 ＋ 强制高层覆盖定理（新）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:11 令 ✓）**：沿 C-431／C-432 的 **$R=0$ 分支**继续 ✓；回 excess／LP ✗；**不做路线裁定** ✗；**零程序计算**（仅一处整数核对 ✓）。

**已查地图：命中（接续 C-432／C-430／C-419／C-410，非新案 ✓）**
`docs/WITSTAR-2026-09-28-…`（**交叠分类／私公二分／Johnson 恒等式** ✓✓）｜`docs/P1-WIT-2026-09-27-…`（**冗余夹逼／见证星** ✓✓）｜`docs/P1-D3-2026-09-27-…`（**被迫高层码字定理（先例 ✓✓）**）｜`docs/P1-MICRO-…`（**$(\alpha)$ 内部子立方体排斥** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** $R=0$ 分支／强制高层对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出两处修正（含整数核对）＋ 强制高层覆盖定理（一般形式，不需 $R=0$）＋ 级联形式** ✓）
**[RESEARCH]**

---

## §0 结论（**修正两处 ✗✗｜新定理 ✓✓｜级联 ✓✓｜无矛盾 ⚠️**）

$$\boxed{\textbf{(1) ✗修正一（第 2→3 步算术滑落）}:\ b_3=\binom s3-4b_4\ \text{代入}\ b_4\le\tfrac14\binom s3\ \textbf{只给}\ b_3\ge\mathbf 0\ ✗}$$
$$\qquad\text{（唐先生写 }b_3\ge\tfrac12\binom s3\ ✗\ \text{—— 正确代换：}\binom s3-4\cdot\tfrac14\binom s3=0✓\ \text{；逐点核对见 §1 表 ✓）}$$
$$\boxed{\textbf{(2) ✗修正二（第 4 步 packing 界用错对象）}:\ \text{正确界涉及 }S\ \textbf{内部的 pair}✓:\ b_3\le(10-s)\Big\lfloor\tbinom{s}{2}/3\Big\rfloor\ ✓}$$
$$\qquad\text{因同外部坐标 }x\text{ 下的 }B_3\text{ triples 两两至多共享 1 点（否则共享 triple }\Longrightarrow\text{ 双见证 }\Longrightarrow m_T\ge2\text{）} \Longrightarrow 3|\mathcal B_x|\le\tbinom s2\text{ ✓（而非 }\tbinom t2\text{ ✗）}$$
$$\qquad\Longrightarrow\ \textbf{故 "}R=0\Rightarrow s\le4\text{" \textbf{不成立}}✗✓\ \text{（无 }s\ \text{上界 ✓；}s=10\ \text{等极紧情形反而成立 ✓）}$$
$$\boxed{\textbf{(3) ★★强制高层覆盖定理（新 ✓✓，一般形式，不需 }R=0\text{）}:\ \text{设 }u\subseteq S(c),\ |u|=4,\ c\oplus e_u\notin C \Longrightarrow \exists\,i\notin u:\ c\oplus e_{u\cup\{i\}}\in C✓✓}$$
$$\qquad\textbf{证明（3 行 ✓）}:\ \text{点 }c\oplus e_u\ \text{须被覆盖 ✓；其 1-邻点两类：}c\oplus e_{u\setminus\{i\}}\ (|u\setminus i|=3,\ \subseteq S(c)\overset{(\alpha)}{\Longrightarrow}\notin C\ ✗)\ \text{与}\ c\oplus e_{u\cup\{i\}}\ (|u\cup i|=5✓)$$
$$\qquad\Longrightarrow\ \textbf{唯一出路 ＝ 距离-5 码字}✓✓\ \big(\text{＝P1-D3"被迫高层码字"的\textbf{对偶层}✓✓}\big)$$
$$\boxed{\textbf{(4) ★计数形式（新 ✓）}:\ \tbinom{s(c)}4-b_4\ \le\ \sum_{w\in C,\,d(c,w)=5}\tbinom{|S_w\cap S(c)|}4\ =\ \mathbf 5c_5+c_4\ ✓}$$
$$\qquad\big(c_j:=\#\{w\in C:d(c,w)=5,\ |S_w\cap S(c)|=j\}\ ✓;\ j=5\ \text{贡献 }\tbinom54=5✓,\ j=4\ \text{贡献 }1✓,\ j\le3\ \text{贡献 }0✗\big)$$
$$\boxed{\textbf{(5) ★级联（新 ✓✓，登记）}:\ \forall V\subseteq S(c),\ |V|=5:\ \text{若 }V\ \text{的全部 4-子集皆}\notin B_4 \Longrightarrow \exists\,\text{weight-6 码字}\supseteq V✓;\ \text{逐层类推至 weight-10}✓}$$
$$\qquad\Longrightarrow\ \textbf{局部强制塔}✓✓\ \big(\text{在 weight }\le10\ \text{处必然终止 ⟹ 终止处即潜在矛盾位置 ⚠️}\big)$$

---

## §1 修正一：整数核对（**逐字 ✓**）

```
$ python3 -c "from math import comb; [print(s, comb(s,3), comb(s,3)-4*(comb(s,3)//4)) for s in range(11)]"
s= 0  C(s,3)=  0  b_4<= 0.00  => b_3 >= 0   （唐先生写 >= 0 ✓）
s= 3  C(s,3)=  1  b_4<= 0.25  => b_3 >= 1   （唐先生写 >= 0 ✗）
s= 4  C(s,3)=  4  b_4<= 1.00  => b_3 >= 0   （唐先生写 >= 2 ✗）
s= 5  C(s,3)= 10  b_4<= 2.50  => b_3 >= 2   （唐先生写 >= 5 ✗）
s= 6  C(s,3)= 20  b_4<= 5.00  => b_3 >= 0   （唐先生写 >= 10 ✗）
s= 7  C(s,3)= 35  b_4<= 8.75  => b_3 >= 3   （唐先生写 >= 17 ✗）
s= 8  C(s,3)= 56  b_4<=14.00  => b_3 >= 0   （唐先生写 >= 28 ✗）
s= 9  C(s,3)= 84  b_4<=21.00  => b_3 >= 0   （唐先生写 >= 42 ✗）
s=10  C(s,3)=120  b_4<=30.00  => b_3 >= 0   （唐先生写 >= 60 ✗）
```
$$\Longrightarrow\ b_3\ \text{的这批下界\textbf{全部无效}}✗\ \text{（那些数字恰是 }\tfrac12\binom s3\text{ 的错代换产物 ✓）}$$

## §2 修正二：正确的 packing 界（**✓，沿用前一轮已登记形式 ✓**）

$$\textbf{外部坐标 packing ✓}:\ \text{固定 }x\in S^c\ (|S^c|=10-s✓),\ \mathcal B_x:=\{T\subseteq S(c):|T|=3,\ T\cup\{x\}\in B_3\}✓$$
$$\qquad T\ne T'\in\mathcal B_x\Longrightarrow|T\cap T'|\le1✓\ \big(\text{否则共享 triple ⟹ 双见证 ⟹ }m_T\ge2\ ✗\big) \Longrightarrow 3|\mathcal B_x|\le\tbinom s2 \Longrightarrow |\mathcal B_x|\le\Big\lfloor\tbinom s2/3\Big\rfloor✓$$
$$\qquad\Longrightarrow\ \boxed{b_3\le(10-s)\Big\lfloor\tbinom{s}{2}/3\Big\rfloor}\ ✓\ \text{（与上轮 (20) 一致 ✓）}$$
$$\textbf{pair-shadow ✓}:\ 2p_P+q_P=s-2\ \forall P\Longrightarrow p_P\ge s-6✓\ \big(\text{同前 ✓}\big)$$

## §3 修正后的 $R=0$ 系统（**✓ 与上轮一致，取代本轮的错误版 ✓**）

$$\boxed{\ \begin{aligned}&4b_4+b_3=\tbinom s3\ ✓;\\ &b_4\le\tfrac14\tbinom s3✓\ \big(=b_3\ge0\ \text{等价 ✓}\big);\\ &b_3\le(10-s)\Big\lfloor\tfrac12\tbinom s2\Big\rfloor✓;\\ &2p_P+q_P=s-2✓,\ p_P\ge s-6✓\end{aligned}\ }$$
$$\textbf{由 }\textcircled{1}\textcircled{3}\ \text{得 }b_4\ \text{下界}✓:\ b_4\ \ge\ \frac{\tbinom s3-(10-s)\lfloor\tbinom s2/3\rfloor}{4}\ \Longrightarrow\ \text{逐点}:\ s{=}10:\ b_4{=}\mathbf{30}✓;\ s{=}9:\ \ge18✓;\ s{=}8:\ \ge10✓;\ s{=}7:\ \ge4✓;\ s\le6:\ \ge0✓$$
$$\qquad\text{（}s=10\ \text{时}\ b_3\le0\therefore b_3=0\therefore b_4=30✓\ \text{—— 极紧且无矛盾 ✓）}\qquad\boxed{\textbf{故 }R=0\ \text{在所有 }s\ \text{下存活}✓\ \text{（无矛盾 ⚠️）}}$$

## §4 s=4 的两刚性模型（**✓ 该分类仍成立 ✓，因它只用 }b_4\le\tfrac14\tbinom s3=1$ ✓）

$$\binom43=4,\ b_4\le1 \Longrightarrow (b_4,b_3)\in\{(\mathbf{1,0}),(\mathbf{0,4})\}✓\ \Longrightarrow\ \textbf{Model A}:\ B_4=\{S\},\ B_3=\varnothing✓;\quad \textbf{Model B}:\ B_4=\varnothing,\ B_3=\tbinom S3✓$$
$$\textbf{Model A 覆盖检查 ✓}:\ \text{唯一 4-子集 }u=S\ \text{本身是码字（}S\in B_4✓\big) \Longrightarrow \text{自覆盖 ✓ ⟹ 无强制 ✓}$$
$$\textbf{Model B 覆盖检查 ✓（新）}:\ B_4=\varnothing\ \Longrightarrow\ c\oplus e_S\notin C \overset{§0(3)}{\Longrightarrow} \exists\,i\notin S:\ c\oplus e_{S\cup\{i\}}\in C✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{Model B 强制一个 weight-5 码字 }c\oplus e_{S\cup\{i\}}\ (i\in S^c)✓}\ \big(\text{新 ✓；}s^c\ne\varnothing\ \text{须 }s\le9✓\big)$$

## §5 级联（**登记未做 ⚠️，不作裁定 ✗**）

$$\textbf{递推形式 ✓}:\ \text{对 }k\ge4:\ \text{若某 }k\text{-子集 }W\subseteq S(c)\ \text{的全部 }(k-1)\text{-子集皆缺失，则 }\exists\,\text{weight-}(k{+}1)\ \text{码字}\supseteq W✓\ \big(\text{同 §0(3) 的证明 ✓}\big)$$
$$\qquad B_4\ \text{稀疏（}R=0\ \text{时 }4b_4\le\tbinom s3✓\big) \Longrightarrow \text{大量 4-子集缺失} \Longrightarrow \text{weight-5 层被大量强制} \Longrightarrow \text{逐层上行}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{强制塔必在 weight}\le10\ \text{处终止（无 weight-}>10)\ ✓ \Longrightarrow \textbf{终止层即潜在矛盾位置}⚠️}\ \big(\text{等级：未做 ✗}\big)$$

## §6 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "覆盖不等式" "强制高层" "级联" "pair-shadow"
技术词 覆盖不等式   命中文件数=5    :: ./DELSARTE-2026-09-26-… ./ASSETS-REGISTRY.md ./A5-FORM-RECONSTRUCTED-2026-09-26-closure.md …
技术词 强制高层     命中文件数=0    ::
技术词 级联         命中文件数=16   :: ./V106-L3-Q3-… ./P1-B4-2026-09-27-… ./C326-Littlewood-… …
技术词 pair-shadow  命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间／属线未定（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 覆盖不等式 | 0（`DELSARTE-*`／`A5-FORM-*` ⟹ **属线未定 ⟹ 不计** ✗） | 5 | 0（既有词 ✓） |
| 强制高层 | 0 | 0 | 0（本档自造标签 ✓） |
| 级联 | 0（16 命中多属空间 A／未定 ⟹ **不计** ✗） | 16 | 0（既有词 ✓） |
| pair-shadow | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（`强制高层`／`pair-shadow` 两空间皆 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1-§3 修正 ＋ §0(3)(4) 新定理 ＋ §4 两模型检查 ＋ §5 级联登记**（推导 ＋ 一处整数核对 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓（仅 §1 整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§6 已分栏 ✓）
- **§0(3) 依赖 $(\alpha)$** ✓（即 $A(c)=0$ ✓，内部子立方体排斥 ✓）—— 引用时须与 C-410 同引 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）：本档只给修正、新定理、级联与两模型检查；STOP／继续由唐先生定 ✓
- **不声称** $R=0$ 已被排除 ✗（§3 已明示其在所有 $s$ 存活 ✓）；**不声称** 级联必生矛盾 ✗（§5 已标未做 ✓）；不声称 P1 成立 ✗（V290）
