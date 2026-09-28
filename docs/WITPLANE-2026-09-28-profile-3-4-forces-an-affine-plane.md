# WITPLANE-2026-09-28 — **$3^4\Rightarrow P$ 是二维仿射平面（新 ✓✓）；但闭环不排除 $3^4$（显式局部模型 ✗）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 12:12 令 ✓）**：闭环条件的有限结构推演；**零程序计算**（仅整数与有限结构核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-449／C-448／C-447，非新案 ✓）**
`docs/WITPROF-2026-09-28-…`（**$r_{\max}{=}3$／$D_2\in\{5,6\}$ 两 profile ✓✓✓**）｜`docs/WITCODE-2026-09-28-…`（**$e(A){=}0$／$D_2\ge5$ ✓✓**）｜`docs/WITA0-2026-09-28-…`（**$d(A_0)\ge3$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（"方向集" 3 命中／"仿射平面" 1 命中 —— **均属线未定 ⟹ 不计** ✗；"坐标支撑混淆" 0 ✓）
D0: 本档对象 ＝ **档案已有** 闭环条件／$3^4$ 结构对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $3^4\Rightarrow P=x\oplus\{0,u,v,u\oplus v\}$（二维仿射平面）＋ 坐标支撑/方向集混淆之澄清＋$3^4$ 之显式局部模型（不排除）** ✓）
**[RESEARCH]**

---

## §0 结论（**混淆 ✗✗｜仿射平面 ✓✓（新）｜$3^4$ 未被排除 ✗**）

$$\textbf{设定 ✓}:\ r(p):=\big|\{i\in[9]:p\oplus e_i\in A_1\}\big|\ \ \text{（\textbf{方向集}，非坐标支撑 ✗）}✓;\quad \sum_{p\in P}r(p)=12✓;\ r(p)\le3✓;\ D_2\in\{5,6\}✓$$
$$\boxed{\textbf{(1) ✗✗系统性混淆（本档澄清）}:\ \text{唐先生 §1 设}\ S(p):=\operatorname{supp}(p)\ \text{且}\ k=|S(p)|=r(p)\ \textbf{不对}\ ✗✗}$$
$$\qquad \operatorname{supp}(p)=\{i:p_i=1\}\ \text{（\textbf{坐标支撑}）}\ \ne\ D(p):=\{i:p\oplus e_i\in A_1\}\ ✓\ \text{二者\ \textbf{一般无关} ✗}$$
$$\qquad\textbf{反例 ✓}:\ p=e_1{\oplus}\cdots{\oplus}e_5\ \big(\text{weight }5✓\big)\ \text{而}\ D(p)=\{7,8,9\}\ \text{完全可能 ✓};\ \text{故 }k=|S(p)|\ne r(p)✗$$
$$\qquad\Longrightarrow\ \text{§2 的"}|q|=k{-}2\text{"、§3–§5 的"weight-3 ⟹ 三个单位向量入 }P\text{"、§4 的"2-交 3-一致族"、§6 的 (6)(7) 全部\textbf{不成立}}\ ✗✗$$
$$\boxed{\textbf{(2) ✓✓但纠正后的闭环更强（新）}:\ \text{对 }p\in P\ \text{与}\ i\ne j\in D(p):\ p\oplus e_i,\ p\oplus e_j\in A_1\ \text{皆与 }p\ \text{距离 1}}$$
$$\qquad\Longrightarrow\ \text{共同邻点}=\{p,\ p\oplus e_i\oplus e_j\}✓ \Longrightarrow \boxed{q:=p\oplus e_i\oplus e_j\in P,\ r(q)\ge2}✓✓;\quad \text{且 }e_i\oplus e_j\ (i<j)\ \textbf{互异}\Longrightarrow\text{闭环点\textbf{互异}}✓✓$$
$$\qquad\textbf{(3) ★★profile }3^4\ \textbf{的精确结构（新 ✓✓）}:\ \text{对每个 }a:\ \binom32=3\ \text{个闭环点与 }p_a\ \text{合为 4 点}=P✓ \Longrightarrow$$
$$\qquad\qquad\boxed{P=\{x,\ x\oplus u,\ x\oplus v,\ x\oplus(u\oplus v)\}\quad\big(u=e_i\oplus e_j,\ v=e_i\oplus e_k,\ u\oplus v=e_j\oplus e_k✓\big)}✓✓$$
$$\qquad\qquad\Longrightarrow\ \{0,u,v,u\oplus v\}\ \text{对 XOR 封闭（}=\{0,\ e_i{\oplus}e_j,\ e_i{\oplus}e_k,\ e_j{\oplus}e_k\}\ \text{是子群 ✓）} \Longrightarrow \boxed{P\ \text{是 }Q_9\ \text{中的二维仿射平面}}✓✓$$
$$\qquad\qquad\text{（核对 ✓）}\ u\oplus v=e_i\oplus e_j\oplus e_i\oplus e_k=e_j\oplus e_k✓;\quad u\oplus v\oplus(u\oplus v)=0✓;\ \text{群结构成立 ✓✓}$$
$$\boxed{\textbf{(4) ⚠️但 }3^4\ \textbf{未被闭环排除（显式局部模型 ✓）}:\ }A_1=\{e_i,\ e_j,\ e_k,\ e_i{\oplus}e_j{\oplus}e_k\}\ \big(4\ \text{点},\ e(A_1){=}0✓\big)$$
$$\qquad P=\{0,\ e_i{\oplus}e_j,\ e_i{\oplus}e_k,\ e_j{\oplus}e_k\}\ \big(\text{＝二维仿射平面 ✓}\big) \Longrightarrow r(p)=\mathbf{(3,3,3,3)}✓,\ \sum r=12✓,\ 2D_2=12✓,\ D_2=6✓✓$$
$$\qquad\Longrightarrow\ \textbf{闭环条件不排除 }3^4\ ✗✓\ \big(\text{局部层面 }3^4\ \text{可实现 ✓}\big);\ \text{但其\ \textbf{全局}可完成性\ \textbf{未验}}✗\ \big(\text{须 }|A|=45,\ |U|=119,\ \text{其余 }N(A_1)\ \text{点落 }U^c\ \text{等 ✓}\big)$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✗}:\ S(p)=\operatorname{supp}(p)\ \text{与 }k=r(p)\ \text{之等同 ✗；"support 下降闭包"}\ \text{之表述\ \textbf{不适用}}✗;\ \textbf{但}q=p\oplus e_i\oplus e_j\in P\ \text{核心 ✓✓（=(2) ✓）}$$
$$\textbf{§2 ✗}:\ "k_a=2\Rightarrow\text{flip}=0\text{"}\ ✗\ \big(\text{系坐标支撑视角 ✓}\big);\ \textbf{正确}:\ r(p_a){=}2\Rightarrow\text{唯一闭环点}=p_a\oplus e_i\oplus e_j\ \text{（}\ne0✓\big)$$
$$\textbf{§3–§5 ✗}:\ \text{"weight-3 迫使三个单位向量入 }P\text{"}\ ✗\ \big(\text{方向集 }D(p)\ \text{与坐标无关 ✓}\big);\quad \text{故 (1)–(6) 诸结论不成立}\ ✗$$
$$\textbf{§6–§7 ✗}:\ \text{"}3^4\Rightarrow|S(p)|{=}1\ \forall p\text{（全为单位向量）}"\ ✗\ \text{—— 正确结论是\ \textbf{二维仿射平面} ✓✓（=§0(3) ✓）}$$
$$\textbf{§8–§9 ✗}:\ \text{型 A／型 B 之 }2\text{-交 3-一致族分析}\ ✗\ \text{（基于同一混淆 ✓）}$$
$$\textbf{§11 ✓（形式 ✓）}:\ 2D_2=\sum_P\binom{r_p}2=4\binom32=12\Rightarrow D_2=6✓✓;\ \text{"饱和等号结构"之提法 ✓（但须以 (3) 之平面结构为出发点 ✓）}$$
$$\textbf{§2 之数值重述 ✓}:\ r_{\max}\le3\Rightarrow D_2\le6✓;\ D_2\in\{5,6\}✓✓\ \big(\text{C-449 ✓}\big);\ \text{profile }3^32^11^1\ \text{仍待攻 ✓}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }D(p)\ \text{与 }\operatorname{supp}(p)\ \text{之区分 ✓✓};\ \text{② 闭环点互异且 }\in P✓✓;\ \text{③ }\boxed{3^4\Rightarrow P\ \text{是二维仿射平面}}✓✓;\ \text{④ }3^4\ \text{之显式局部模型 ✓};\ \text{⑤ }D_2=6\Rightarrow\sum_P\binom{r_p}2=12\ \text{饱和 ✓}$$
$$\textbf{已否证 ✗✓}:\ \text{"}k=|S(p)|=r(p)\text{"};\ \text{"weight-3}\Rightarrow\text{三个单位向量入 }P\text{"};\ \text{"}3^4\Rightarrow\text{全为单位向量}\text{"};\ \text{型 A／型 B 分类};\ \text{闭环排除 }3^4\ ✗$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ t{=}12\ \text{的关闭};\ 3^4\ \text{之全局可完成性};\ 3^32^11^1\ \text{的排除}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① }3^4:\ \text{由 }P\ \text{为二维仿射平面 ＋ }A_1\ \text{之四点结构，做全局计数}\ \big(|A|{=}45,\ |U|{=}119,\ N(A_1)\setminus P\subseteq U^c✓\big);\ \text{② }3^32^11^1:\ \text{待攻}\ ✓$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "方向集" "仿射平面" "坐标支撑混淆"
技术词 方向集       命中文件数=3    :: ./p28b1-blockmass.md ./p34b-multiplier-kernel.md ./P14-2026-09-26-second-layer-shadow-collision-table.md
技术词 仿射平面     命中文件数=1    :: ./P1ALIGN-2026-09-27-alignment-profile-law.md
技术词 坐标支撑混淆 命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 属线未定（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 方向集 | 0 | 3（`p28b1`／`p34b`／`P14-*` ⟹ 属线未定 ⟹ **不计** ✗） | 0（既有词 ✓） |
| 仿射平面 | 0 | 1（`P1ALIGN-*` ⟹ 属线未定 ⟹ **不计** ✗） | 0（既有词 ✓） |
| 坐标支撑混淆 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（自造标签仅作结构命名，不作新性主张 ✓）

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅整数与有限结构核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处混淆**（坐标支撑 vs 方向集）已在 §0(1) 显式标注 ✓✓；**新纪律**：用 $\operatorname{supp}$ 前须声明是坐标支撑还是方向集 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗；**不声称** $3^4$ 已被排除 ✗（V290）
