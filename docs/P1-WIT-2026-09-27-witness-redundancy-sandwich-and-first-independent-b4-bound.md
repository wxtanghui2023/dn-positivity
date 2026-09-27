# P1-WIT-2026-09-27 — **见证系统冗余夹逼（新 ✓✓）＋ $b_4$ 的首个独立上界**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围**：沿 C-419 线**继续做 119 的数学** ✓（不开新筛 ✗、不切换 ✗、不替唐先生做路线决定 ✗）；零程序计算 ✓。

**已查地图：命中（接续 C-419／C-417／C-413，非新案 ✓）**
`docs/P1-NINT-2026-09-27-…`（**折衷关系 $b_3+4b_4\ge\binom s3$／独立性闸** ✓✓）｜`docs/P1-COV-2026-09-27-…`（**球面恒等式族／$E_k$ 度数决定** ✓✓）｜`docs/P1-D3b-…`（**$C(s,4,3)$ 方向纠正／混合块** ✓✓）｜`docs/P1-D3-…`（**被迫高层码字定理** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词，**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** 见证／$b_j$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出见证系统冗余夹逼 $\binom s3\le4b_4+b_3\le\binom s3+E_3(c)$ ＋ 见证星结构 ＋ $b_4$ 的首个独立上界** ✓）
**[RESEARCH]**

---

## §0 结论（**新引理 ✓✓｜见证星 ✓✓｜$b_4$ 上界 ✓｜诚实：与 C-419 联用不改善 ✗**）

$$\boxed{\textbf{(1) ★见证系统冗余夹逼（新 ✓✓）}:\ \text{令 }W(T):=\{x\notin T:\ c\oplus e_{T\cup\{x\}}\in C\}\ (T\subseteq S(c),|T|=3✓),\ m_T:=|W(T)|\ge1✓ \Longrightarrow}$$
$$\qquad\boxed{\binom{s(c)}3\ \le\ 4b_4+b_3\ =\ \sum_{T}m_T\ \le\ \binom{s(c)}3+E_3(c)}\ ✓✓\qquad\big(E_3(c)=8d_2(c)+d_3(c)+4d_4(c)-120✓\ \text{（C-417 $k=3$ ✓）}\big)$$
$$\boxed{\textbf{(2) ★见证星结构（新 ✓✓）}:\ \text{对固定 }T,\ \text{其 }m_T\ \text{个见证码字}\ c\oplus e_{T\cup\{x\}}\ (x\in W(T)✓)\ \textbf{全部落在同一球 }B_1(p_T)\ \textbf{内};\ p_T:=c\oplus e_T\ \textbf{非码字}✓✓}$$
$$\qquad\big(d(p_T,\ c\oplus e_{T\cup x})=1✓\ \forall x✓;\ \text{见证码字两两距离 }2✓;\ p_T\notin C\ \text{由 }(\alpha)✓\big) \Longrightarrow \textbf{（"见证星" ✓）}$$
$$\boxed{\textbf{(3) ★$b_4$ 的首个独立上界（新 ✓）}:\ \boxed{b_4\ \le\ \frac{\binom{s(c)}{3}+E_3(c)}{4}}\ ✓\qquad \text{（C-419 所缺"输入"的一半 ＝ 上界侧 ✓✓）}}$$
$$\boxed{\textbf{(4) ⚠️ 诚实：与 C-419 折衷式联用\ \textbf{不改善} 容量界 ✗}:\ E_3\ge0\Longrightarrow d_4\ge\binom s3-3b_4\ge\frac{\binom s3-3E_3}4\le\frac{\binom s3}4\ ✓ \Longrightarrow \textbf{仍只回到容量界}✗✓}$$

---

## §1 **定义**（**逐项 ✓**）

$$\textbf{（见证）}:\ T\subseteq S(c),\ |T|=3 \Longrightarrow x_T:=c\oplus e_{(T)}\notin C\ \big((\alpha)✓\big);\ \text{其覆盖须由 weight-4 见证 }y=c\oplus e_S\ (T\subset S,\ |S|=4✓)\ ✓\ \big(\text{C-419 ✓}\big)$$
$$\qquad\Longrightarrow\ S=T\cup\{x\},\ x\notin T \Longrightarrow W(T):=\{x\notin T:c\oplus e_{T\cup\{x\}}\in C\}✓;\quad m_T:=|W(T)|\ \ge\mathbf1\ ✓\ \big(\text{需求 ✓}\big)$$
$$\textbf{（分类对表）}:\ \text{对 weight-4 码字 }y=c\oplus e_S✓:\ \text{它计入的 }T\ \text{数}=\#\{T\subset S:T\subseteq S(c)\}=\binom{|S\cap S(c)|}3✓;\ \text{仅 }j=4,3\ \text{贡献 }(4,1)✓$$
$$\qquad\Longrightarrow\ \boxed{\sum_{T\subseteq S(c)}m_T=4b_4+b_3}\ ✓✓\ \big(\text{＝C-419 的 }\sum_j\binom j3b_j\ \text{的\ \textbf{恒等式形式}}✓\big)$$

## §2 **夹逼证明**（**三段 ✓✓**）

$$\textbf{下界 ✓}:\ m_T\ge1\ \forall T \Longrightarrow \sum_Tm_T\ge\#\{T\}=\binom{s(c)}3✓\ \big(\text{＝C-419 的不等式 ✓}\big)$$
$$\textbf{上界（关键 ✓✓）}:\ \text{所有 }x\in W(T)\ \text{给出 }c\oplus e_{T\cup\{x\}}\in C✓;\ \text{且}\ d\big(p_T,\ c\oplus e_{T\cup\{x\}}\big)=|e_{(T\cup x)}\oplus e_{(T)}|=1✓\ \Longrightarrow\ \text{它们全在 }B_1(p_T)✓$$
$$\qquad\Longrightarrow\ b(p_T)\ \ge\ m_T✓;\qquad \text{（}p_T\big)_{T}\ \text{两两不同 ✓（}T\ \text{不同 ⟹ }e_{(T)}\ \text{不同 ✓）且皆在距离-3 球面 ✓）}$$
$$\qquad\Longrightarrow\ \sum_T\big(m_T-1\big)\ \le\ \sum_T\big(b(p_T)-1\big)\ \le\ \sum_{x\in S_3(c)}\big(b(x)-1\big)=E_3(c)✓✓\ \big(\text{各项 }\ge0✓\ \text{故部分和}\le\text{总和}\ ✓\big)$$
$$\qquad\Longrightarrow\ 4b_4+b_3-\binom s3=\sum_T(m_T-1)\le E_3(c)✓✓\ \Longrightarrow\ \textbf{§0 (1) 得证}✓$$
$$\textbf{（$p_T$ 非码字 ✓）}:\ p_T=c\oplus e_{(T)}✓,\ T\subseteq S(c),\ |T|=3 \overset{(\alpha)}{\Longrightarrow} p_T\notin C✓\ \big(\text{故它不是"被计数的码字"，而是}\ \textbf{纯球心}✓\big)$$

## §3 **推论与诚实评估**（**✓／✗**）

$$\textbf{推论 A（$b_4$ 上界 ✓）}:\ 4b_4\le4b_4+b_3\le\binom s3+E_3 \Longrightarrow b_4\le\big(\binom s3+E_3\big)/4✓✓$$
$$\textbf{推论 B（$b_3$ 上界 ✓）}:\ b_3\le\binom s3+E_3✓;\qquad \textbf{推论 C（冗余非负 ✓）}:\ 4b_4+b_3-\binom s3\in[0,E_3]✓$$
$$\textbf{⚠️ 与 C-419 联用的诚实评估 ✗}:\ \text{C-419}: d_4\ge\max\big(b_4,\ \binom s3-3b_4\big)✓;\ \text{用推论 A}: b_4\le\big(\binom s3+E_3\big)/4 \Longrightarrow \binom s3-3b_4\ge\frac{\binom s3-3E_3}4✓$$
$$\qquad\textbf{但}\ \frac{\binom s3-3E_3}4\le\frac{\binom s3}4\ \big(E_3\ge0✓\big) \Longrightarrow \textbf{该组合不超过容量界}✗✓\ \big(\text{故本引理\textbf{单独}不加强下界 ✓}\big)$$
$$\textbf{（本引理的正向价值 ✓）}:\ \text{① 把 C-419 的不等式\ \textbf{升级为夹逼}（含冗余 $=\sum_T(m_T-1)$ ✓）};\ \text{② 首次给出 }b_4,b_3\ \text{的独立上界 ✓};\ \text{③ 给出"见证星"这一\ \textbf{非 profile 结构} ✓✓}$$

## §4 **精确剩余缺口**（**C-419"缺输入"的锐化 ✓**）

$$\text{由 C-419}: d_4\ \ge\ \max\Big(b_4,\ \binom s3-3b_4\Big);\qquad \text{要超过容量界 }\binom s3/4,\ \text{只需其一}:$$
$$\qquad\textbf{(i)}\ b_4\ <\ \binom{s(c)}3/4\quad\big(\Longrightarrow d_4\ge\binom s3-3b_4>\binom s3/4✓\big);\qquad \textbf{(ii)}\ b_4\ >\ \binom{s(c)}3/4\quad\big(\Longrightarrow d_4\ge b_4>\binom s3/4✓\big)$$
$$\Longrightarrow\ \boxed{\text{真正缺的输入 ＝ 把 }b_4\ \text{相对 }\binom{s(c)}3/4\ \textbf{定位}（上界 }<\frac{\binom s3}4\ \text{或下界 }>\frac{\binom s3}4\ \text{二者之一 ✓✓）}$$
$$\textbf{（本档的贡献 ✓）}:\ \text{推论 A 给出 }b_4\le\big(\binom s3+E_3\big)/4\ ✓\ \text{——\ 与目标 }\binom s3/4\ \text{只差 }E_3/4✓\ \big(\text{即：}\textbf{若能把上界再压 }E_3/4\ \text{即成功 ✓}\big)$$
$$\qquad\textbf{（后续可攻点，登记未做 ✓）}:\ \text{① 用"见证星"共享同一球心 }p_T\ \text{的排除（两星不相交? ✓）收紧；② 用 }p_T\ \text{间的距离结构（}|T\cap T'|\ \text{决定 }d(p_T,p_{T'})✓\big)\ \text{建第二计数 ⚠️}$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "见证系统" "冗余夹逼" "见证星"
技术词 见证系统      命中文件数=0    ::
技术词 冗余夹逼      命中文件数=0    ::
技术词 见证星        命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 见证系统 | 0 | 0 | 0（本档自造标签 ✓） |
| 冗余夹逼 | 0 | 0 | 0（本档自造标签 ✓） |
| 见证星 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词**两空间皆 0** ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 定义 ＋ §2 夹逼 ＋ §3 推论 ＋ §4 锐化缺口**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **不做路线决定** ✓（照唐先生 2026-09-27 23:54 令 ✓：本档只给结果与缺口，STOP／切换由唐先生裁定 ✗）
- **不声称** P1 成立 ✗（V290）；**不声称** 与 C-419 联用已获增强 ✗（§3 已诚实标注 ✗）
