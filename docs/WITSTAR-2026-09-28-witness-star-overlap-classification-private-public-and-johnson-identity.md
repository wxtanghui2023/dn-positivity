# WITSTAR-2026-09-28 — **见证星交叠的精确分类 ＋ 私/公二分 ＋ Johnson 恒等式**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 00:0x 令 ✓）**：只做**一个极小而关键的理论动作** —— 精确分类 $|W(T)\cap W(T')|$ 作为 $|T\cap T'|$ 的函数 ✓；并检验 $\sum_T\binom{m_T}2$ 能否被 Johnson 边 incidence 精确控制 ✓。**零程序计算** ✓；**不碰 $E_3$** ✓（照唐先生 §7 刹车 ✓）；**不做路线裁定** ✗。

**已查地图：命中（接续 C-430／C-419／C-417／C-411，非新案 ✓）**
`docs/P1-WIT-2026-09-27-…`（**见证系统冗余夹逼 ＋ 见证星** ✓✓）｜`docs/P1-NINT-2026-09-27-…`（**折衷关系** ✓✓）｜`docs/P1-MICRO-…`（**$(\alpha)$ 内部子立方体排斥** ✓✓）｜`docs/P1-TWO-…`（**两点刚性／方向引理** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** 见证星／三元组交叠对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出交叠大小的精确分类（$\le1$，无条件）＋ 私/公二分 ＋ $\sum_T\binom{m_T}2$ 的 Johnson 恒等式** ✓）
**[RESEARCH]**

---

## §0 结论（**分类 ✓✓｜锐化 $\le2\to\le1$ ✓✓｜私公二分 ✓✓｜Johnson 恒等式 ✓✓｜下界为空 ✗**）

$$\boxed{\textbf{(1) ★精确分类（sharp，无条件 ✓✓）}:\ \text{对 }T,T'\subseteq S(c),\ |T|=|T'|=3:}$$
$$\qquad\qquad\boxed{\big|W(T)\cap W(T')\big|=\mathbf 1_{\{|T\cap T'|=2\}}\cdot\mathbf 1_{\{c\oplus e_{T\cup T'}\in C\}}}\qquad\big(\text{即 }0\ \text{或 }1✓\big)$$
$$\qquad\Longrightarrow\ \textbf{特别}:\ |T\cap T'|\le1\Longrightarrow W(T)\cap W(T')=\varnothing✓\ \big(\text{＝唐先生所写 ✓}\big);\quad |T\cap T'|=2\Longrightarrow \le1✓✓\ \big(\textbf{严于唐先生的 }\le2✓\big)$$
$$\boxed{\textbf{(2) ★锐化理由（无条件 ✓✓）}:\ \text{两个球心 }p_T,p_{T'}\ \text{在 }d=2\ \text{时确有 2 个公共邻点,但只有一个可达见证}}$$
$$\qquad p_T\oplus e_i\ \big(i\in T\triangle T'\big)\ \text{一侧给 }c\oplus e_{T\cap T'}\ (\text{距离 }\mathbf2\text{, 非见证}✗);\ \text{另一侧给 }c\oplus e_{T\cup T'}\ (\text{距离 }\mathbf4✓,\ \text{唯一候选})$$
$$\qquad\text{（因 }\textbf{见证必为距离-4 码字}✓:\ x\in W(T)\iff c\oplus e_{T\cup\{x\}}\in C,\ |T\cup\{x\}|=4✓\big)\ \Longrightarrow\ \textbf{故 }\le1✓✓\ \text{（无需 }A(c)=0✓\big)$$
$$\boxed{\textbf{(3) ★★私/公二分（新 ✓✓）}:\ \text{按 }|S_y\cap S(c)|\ \text{分类距离-4 见证 }y\ (S_y:=\mathrm{supp}(y\oplus c)✓)}$$
$$\qquad\text{① }\textbf{b_3 型}\ \big(|S_y\cap S(c)|=3✓\big):\ y\ \text{只属于}\ \textbf{一个}\ \text{星}\✓\ \big(\text{私有}✓\big);\qquad\text{② }\textbf{b_4 型（内部块）}\ \big(|S_y\cap S(c)|=4✓\big):\ y\ \text{恰属于}\ \binom43=\mathbf4\ \text{个星}\✓\ \big(\text{公有}✓\big)$$
$$\qquad\Longrightarrow\ \boxed{\sum_Tm_T=4b_4+b_3}\ \text{的系数}\ 4,1\ \textbf{由此而来}✓✓\ \big(\text{此前只是计数整理, 现为结构事实}✓\big)$$
$$\boxed{\textbf{(4) ★★精确 Johnson 恒等式（新 ✓✓）}:\ \boxed{\sum_{T}\binom{m_T}2\ =\ \sum_{y<y'\in D_4(c)}\binom{\big|S_y\cap S_{y'}\cap S(c)\big|}{3}}}$$
$$\qquad =\ \#\Big\{\{y,y'\}\subseteq D_4(c):\ d(y,y')=2,\ S_y\cap S_{y'}\subseteq S(c)\Big\}\ =\ E_J+E_{\rm cross}\ ✓$$
$$\qquad E_J:=\#\{\text{内部块对 }(u,u'):|u\cap u'|=3\}\ ✓;\qquad E_{\rm cross}:=\#\{\text{内部块 }u\ \text{与 b_3 型 }y:\ S_y\cap S(c)\subset u\}\ ✓$$

---

## §1 **分类的证明**（**两行 ✓✓**）

$$\text{设 }y\in W(T)\cap W(T') \Longrightarrow S_y=T\cup\{x\}=T'\cup\{x'\},\ |S_y|=4\ ✓\ \Longrightarrow\ S_y\supseteq T\cup T' \Longrightarrow |T\cup T'|\le4$$
$$\qquad|T\cup T'|=6-|T\cap T'|\le4 \Longrightarrow |T\cap T'|\ge2✓;\ \text{且当 }|T\cap T'|=2\ \text{时 }T\cup T'\ \text{本身是 4-集} \Longrightarrow S_y=T\cup T'\ \textbf{唯一}✓$$
$$\qquad\Longrightarrow\ y=c\oplus e_{T\cup T'}\ \text{是唯一候选} \Longrightarrow \textbf{§0 (1) 得证}✓\ \big(\text{充分性：}y\in C\ \text{时它同时属于两个星 ✓}\big)$$
$$\textbf{（$d(p_T,p_{T'})$ 对表 ✓）}:\ |T\cap T'|=2\Rightarrow d=2✓;\ =1\Rightarrow d=4✓;\ =0\Rightarrow d=6✓\ \big(|T\triangle T'|=2(3-|T\cap T'|)✓\big)$$
$$\qquad\text{故 }|T\cap T'|\le1\ \text{时两球心距离}\ge4 \Longrightarrow B_1(p_T)\cap B_1(p_{T'})=\varnothing \Longrightarrow \text{交为空}✓\ \big(\text{与 §1 一致 ✓}\big)$$

## §2 **私/公二分**（**★新 ✓✓**）

$$\textbf{（b_3 型私有 ✓）}:\ \text{设 }|S_y\cap S(c)|=3,\ S_y=T\cup\{x\}\ (T:=S_y\cap S(c)✓,\ x\notin S(c)✓);\ \text{若 }y\in W(T')\ \text{则 }T'\subset S_y,\ |T'|=3✓$$
$$\qquad\text{又 }T'\subseteq S(c)✓ \Longrightarrow T'\subseteq S_y\cap S(c)=T \Longrightarrow T'=T✓ \Longrightarrow \textbf{只属于一个星}✓✓$$
$$\textbf{（b_4 型公有 ✓）}:\ S_y\subset S(c),\ |S_y|=4 \Longrightarrow y\in W(T)\iff T\subset S_y \Longrightarrow \#\{T\}=\binom43=4✓✓$$
$$\qquad\Longrightarrow\ \sum_Tm_T=\sum_{y}\#\{T:T\subset S_y\cap S(c),\ |T|=3\}=\sum_y\binom{|S_y\cap S(c)|}3=4b_4+b_3✓✓$$

## §3 **Johnson 恒等式**（**✓✓ 含纪律标注**）

$$\sum_T\binom{m_T}2=\#\big\{(T,\{y,y'\}):\ y\ne y'\in W(T)\big\}=\sum_{y<y'}\#\big\{T:\ T\subseteq S_y\cap S_{y'},\ T\subseteq S(c),\ |T|=3\big\}=\sum_{y<y'}\binom{|S_y\cap S_{y'}\cap S(c)|}3✓✓$$
$$\textbf{（非零条件 ✓）}:\ \binom{\cdot}3\ne0 \iff |S_y\cap S_{y'}\cap S(c)|\ge3 \Longrightarrow |S_y\cap S_{y'}|\ge3 \iff d(y,y')\le2✓\ \big(\text{恰＝同星共球心 ✓}\big)$$
$$\qquad\text{且 }d(y,y')=2\iff|S_y\cap S_{y'}|=3\ \Longrightarrow\ \text{该 3-集} = S_y\cap S_{y'}✓ \Longrightarrow\ \text{贡献 }1\iff S_y\cap S_{y'}\subseteq S(c)✓$$
$$\textbf{★纪律（照唐先生 §3 ✓）}:\ \textbf{保持 }4b_4+b_3\ \textbf{口径}✓;\ \textbf{不得}偷换为 4d_4(c)✗\ \big(\because\ \binom{|S_y\cap S(c)|}3=0\ \text{当 }|S_y\cap S(c)|\le2✓,\ \text{故 }4d_4(c)\ \text{会高估}✗\big)$$

## §4 **评估（照唐先生判据 ✓，不做裁定 ✗）**

$$\textbf{① 过门 ✓✓}:\ \sum_T\binom{m_T}2\ \text{取决于 4-集的}\textbf{成对交叠}\ ✓,\ \textbf{非} profile 量 \big(d_j(c),\{N_j\}\ \text{不含此项}✓\big) \Longrightarrow \textbf{未落入 STOP}✓$$
$$\qquad\text{（对照 C-417／C-425 的 profile/方向两类塌缩：本量属}\textbf{第三种}✓\big)$$
$$\textbf{② ⚠️下界侧为空（唐先生 §5 ✓）}:\ \text{仅知 }\sum_Tm_T\ge\binom s3;\ \text{当 }\sum_Tm_T=\binom s3\ \text{时}\ \forall T:m_T=1 \Longrightarrow \sum_T\binom{m_T}2=0✓\ \big(\text{凸性不给正下界}✗\big)$$
$$\textbf{③ ⚠️上界侧＝唯一活口}:\ \text{由 §2 私有性 }+\ \text{§3 交叠规则, 上界须由 }b_4\ \text{与 }S(c)\ \text{内的 Johnson 结构给出}✓;\ \text{登记未做}✗$$
$$\qquad\textbf{（可用的局部界 ✓ 登记）}:\ E_J\le 2b_4(s-4)✓\ \big(\text{每内部块 }\#\{u':|u\cap u'|=3\}=4(s-4)✓,\ \text{对半}✓\big);\quad E_{\rm cross}\le b_3\,b_4✓$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "私公二分" "星共享图" "见证负载" "Johnson 边"
技术词 私公二分     命中文件数=0    ::
技术词 星共享图     命中文件数=0    ::
技术词 见证负载     命中文件数=0    ::
技术词 Johnson 边   命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 私公二分 | 0 | 0 | 0（本档自造标签 ✓） |
| 星共享图 | 0 | 0 | 0（本档自造标签 ✓） |
| 见证负载 | 0 | 0 | 0（本档自造标签 ✓） |
| Johnson 边 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（四词**两空间皆 0** ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 分类 ＋ §2 私公二分 ＋ §3 Johnson 恒等式 ＋ §4 评估**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓（纯推导 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **不碰 $E_3$** ✓（照唐先生 §7 ✓，避免回 profile 路 ✓）；**不作路线裁定** ✗（照 23:54 令 ✓）：本档只给分类／恒等式／评估，是否进入第二步由唐先生定 ✓
- **不声称** P1 成立 ✗（V290）；**不声称** 上界侧必有矛盾 ✗（§4 ③ 已标注 ✗）
