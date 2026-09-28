# WITEFF-2026-09-28 — **有效容量闸门**：$L_A\le9a+s-512$（精化 ✓✓）＋ 双侧合并式修正（$2s+47$）＋ 边界刚性

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:45 令 ✓）**：保留一般参数、推进"有效容量"（$9|A|\to9|A|-2e(A)-T_A$）；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-440／C-439／C-438，非新案 ✓）**
`docs/WITGATE-2026-09-28-…`（**交界点 $393/8$／$\mathrm{min\_excess}_9$／$s\le61$ 为空 ✓✓**）｜`docs/WITCAP-2026-09-28-…`（**$9a+s\ge512$／去特化 ✓✓**）｜`docs/ERRATUM-2026-09-28-WITSAT-…`（**$X_L$ 定义／不可完成性 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** 容量／$A$-内部结构对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出有效容量恒等式（$L_A=2e(A)+T_A$）＋ 精化闸门 $L_A\le9a+s-512$ ＋ 双侧合并式之算术修正（$2s+47$）＋ 边界刚性（$a{=}44,s{=}116\Rightarrow e(A)=T_A=0$）** ✓）
**[RESEARCH]**

---

## §0 结论（**精化成立 ✓✓｜两处必改 ✗✓｜边界刚性 ✓✓｜ρ_A 已核 ✓**）

$$\text{记号 ✓}:\ a=|C_0|,\ b=|C_1|,\ a+b=119✓;\ s=|U|,\ |H|=119-s✓;\ |A|=a+s-119,\ |B|=b+s-119,\ |A|+|B|=2s-119✓$$
$$\qquad X_L:=U^c\cap\{x:N(x)\cap H=\varnothing\}✓\ \big(\text{C-438 §0 的正确对象}\ ✓\big);\quad r_A(x):=|N(x)\cap A|✓;\quad T_A:=\sum_{x\in X_L}\big(r_A(x)-1\big)\ge0✓$$
$$\boxed{\textbf{(1) ✗必改一（重复陷阱，第 3 次 ✓）}:\ \text{前提\ \textbf{不是} }U^c\subseteq N[A]\ ✗;\ \text{而是}\ X_L\subseteq N(A)\ ✓✓}$$
$$\qquad\textbf{理由 ✓}:\ U^c\subseteq N(C_0)=N(H\cup A)\ ✗\ \text{不是 }N(A)\ ✓;\ \text{仅当 }x\ \text{无 }H\text{-邻（即 }x\in X_L\text{）时才有 }N(x)\cap C_0\subseteq A✓✓$$
$$\qquad\Longrightarrow\ \textbf{（规则化 ✓）}:\ \text{本线凡"每个外部点"型断言，}\textbf{一律先问是否仅对 }X_L\ \text{成立}\ ✓✓\ \big(\text{C-437 §0(3)／C-438 §1 同源 ✗}\big)$$
$$\boxed{\textbf{(2) ✓精化成立（本档核验 ✓✓）}:\ \sum_{x\in X_L}r_A(x)=|X_L|+T_A\ \le\ \sum_{x\notin A}r_A(x)=9|A|-2e(A)\ \Longrightarrow\ \boxed{|X_L|\ \le\ 9|A|-2e(A)-T_A}\ ✓✓}$$
$$\qquad\textbf{（理由 ✓）}:\ \text{① }X_L\cap A=\varnothing\ \big(X_L\subseteq U^c✓\big);\ \text{② }x\in X_L\Longrightarrow r_A(x)\ge1✓;\ \text{③ }\sum_{x\in V}r_A(x)=9|A|✓,\ \sum_{x\in A}r_A(x)=2e(A)✓✓$$
$$\boxed{\textbf{(3) ★★精化闸门（本档核心 ✓✓）}:\ \text{记 }L_A:=2e(A)+T_A\ \big(\text{＝"有效容量损失"✓}\big);\ \text{配合 }|X_L|\ge8s-559\ \big(\text{重容量 ✓}\big) \Longrightarrow}$$
$$\qquad\boxed{L_A\ \le\ 9|A|+8s-559-|X_L|\ \le\ 9a+s-512}\ ✓✓\qquad \big(\text{用 }|A|=a+s-119✓\big)$$
$$\qquad\textbf{等价读法 ✓}:\ \boxed{9a+s\ \ge\ 512+L_A}\ ✓\ \big(\text{＝C-439 闸门 ＋ 层 }A\ \text{的内部结构项 }\ L_A✓✓\big)$$
$$\boxed{\textbf{(4) ✗必改二（双侧合并式的算术）}:\ \text{唐先生写 }16s+L_A+L_B\le2189\ \textbf{不成立}\ ✗\ \big(\text{用了 }a+b=119\ \text{代入，而界施于 }|A|,|B|✓\big)}$$
$$\qquad\textbf{正确 ✓}:\ |A|+|B|=2s-119\ \ge\ \frac{(8s-559+L_A)+(8s-559+L_B)}{9} \Longrightarrow \boxed{L_A+L_B\ \le\ 2s+47}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{取 }L=2e+T\ge2e:\quad \boxed{e(A)+e(B)\ \le\ s+23}\ ✓✓\ \big(\text{新且更紧（唐先生版给 }s\le136.8\ \text{空转 ✗；本式在 }s\ \text{大时可变紧 ✓）}\big)$$
$$\textbf{(5) ★★边界刚性（新 ✓✓）}:\ L_A\le9a+s-512\ \text{在 }a{=}44,\ s_{\min}{=}116\ \text{处给}\ L_A\le\mathbf 0 \Longrightarrow \textbf{强制}\ e(A)=0\ \wedge\ T_A=0\ ✓✓$$
$$\qquad\textbf{读法 ✓}:\ \text{若 }(|C_0|,s)=(44,116)\ \text{则该层 }A\ \text{必须}\ \textbf{完全无内部边且每个 }X_L\text{-点恰有唯一 }A\text{-邻}\ ✓✓\ \big(|A|=41✓\big)$$
$$\qquad\Longrightarrow\ \textbf{首次出现对\ \textbf{层内部几何} 的必要条件}✓✓\ \text{—— 比"纯容量"多一层结构 ✓（但尚非矛盾 ✗：独立集可达 256 ✓）}$$
$$\textbf{(6) ✓ρ_A 已核（唐先生 §7–§9）}:\ |X_L|\ \le\ \sum_{a\in A}\rho_A(a),\qquad \rho_A(a):=\#\{i:\exists j\ne i,\ a\oplus e_i\oplus e_j\in B\}\le9\ ✓\ \big(\text{选择函数给单射 ✓}\big)$$
$$\qquad\Longleftrightarrow\ \rho_A\ \text{是 }9|A|\ \text{的\ \textbf{方向级分解}：}\ |X_L|\le9|A|-\#\{\text{未激活方向}\}\ ✓\ \big(\text{与 (2) 的 }L_A\ \text{同族 ✓}\big)$$

---

## §1 精化闸门的核验（**✓✓ 逐位**）

$$\textbf{①}:\ \sum_{x\in V}r_A(x)=\sum_{x\in V}|N(x)\cap A|=\sum_{a\in A}|N(a)|=9|A|✓\ \big(\text{每个 }a\in A\ \text{在 }Q_9\ \text{中恰 9 邻点 ✓}\big)$$
$$\textbf{②}:\ \sum_{x\in A}r_A(x)=\sum_{x\in A}|N(x)\cap A|=2e(A)✓\ \big(\text{无向图内部边被数两次 ✓}\big) \Longrightarrow \sum_{x\notin A}r_A(x)=9|A|-2e(A)✓$$
$$\textbf{③}:\ X_L\subseteq U^c\subseteq V\setminus A✓ \Longrightarrow \sum_{x\in X_L}r_A(x)\le\sum_{x\notin A}r_A(x)=9|A|-2e(A)✓$$
$$\textbf{④}:\ x\in X_L\Longrightarrow N(x)\cap C_0\subseteq A\ \wedge\ \ne\varnothing \Longrightarrow r_A(x)\ge1✓ \Longrightarrow \sum_{x\in X_L}r_A(x)=|X_L|+T_A✓\ \big(T_A\ge0✓\big)$$
$$\Longrightarrow\ \textbf{(2)(3) 得证}✓✓;\quad \text{逐位核对}:\ a{=}44\Rightarrow L_A\le s-116;\ a{=}50\Rightarrow L_A\le s-62;\ a{=}59\Rightarrow L_A\le s+19✓$$

## §2 边界与两侧核对（**✓**）

| $a$ | $s_{\min}=\max(119-a,\ 512-9a,\ 62)$ | $L_A\le9a+s-512$（在 $s_{\min}$） | $\vert A\vert=a+s-119$ |
|---|---|---|---|
| 44 | 116 | **0** | 41 |
| 46 | 98 | **0** | 25 |
| 49 | 71 | **0** | 1 |
| 50 | 69 | 7 | 0 |
| 56 | 63 | 55 | 0 |
| 59 | 62 | 81 | 2 |

$$\Longrightarrow\ \textbf{最紧处 ＝ }a\in\{44,46,49\}\ \text{（}L_A\le0\ \text{型刚性 ✓）};\quad \textbf{最松处 ＝ }a=59\ (L_A\le81✓)$$
$$\textbf{两侧相加 ✓}:\ L_A+L_B\le(9a+s-512)+(9b+s-512)=9\cdot119+2s-1024=2s+47✓✓\ \big(\text{§0(4) ✓}\big)$$

## §3 为何精化仍不自动产生矛盾（**⚠️ 诚实**）

$$\textbf{① 一般情形下 }L_A\ \text{可为 }0\ ✗:\ \text{取 }A\ \text{为独立集且每个 }x\in X_L\ \text{恰一 }A\text{-邻} \Longrightarrow e(A)=T_A=0✓\ \big(\text{独立集在 }Q_9\ \text{可达 256（偶权层）✓}\big)$$
$$\textbf{② 唐先生 §3 的陷阱判定成立 ✓}:\ e(A)>0\ \text{不被现有条件强制}✗;\ A\ \text{甚至可很小}✓\ \big(a{=}59,s{=}62\Rightarrow|A|{=}2✓\big)$$
$$\textbf{③ 故精化的作用 ✓}:\ \text{不是"再给一个数"，而是把闸门}\textbf{参数化到层内部几何}:\ \text{损失 }L_A\ \text{必须落进滑动余量 }(9a+s-512)✓✓$$
$$\qquad\Longrightarrow\ \textbf{唯一活口 ⚠️}:\ \text{证明某个}(a,s)\ \text{区域强制 }L_A\ \text{超过余量}✗\ \big(\text{需 }e(A)\ \text{或 }T_A\ \text{的下界 —— 目前无 ✗}\big)$$

## §4 状态（**不作路线裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 有效容量恒等式（§1）};\ \text{② 精化闸门 }L_A\le9a+s-512✓;\ \text{③ 双侧正确式 }L_A+L_B\le2s+47\ \text{与 }e(A)+e(B)\le s+23✓;\ \text{④ 边界刚性（}a{=}44,46,49\Rightarrow L_A\le0✓）;\ \text{⑤ }\rho_A\ \text{单射界 ✓}$$
$$\textbf{已改正 ✗✓}:\ \text{① }U^c\to X_L\ \text{前提（第 3 次同型陷阱 ✓）};\ \text{② 双侧合并式之 }|A|+|B|=2s-119\ \text{代入 ✓}$$
$$\textbf{未确立 ⚠️}:\ e(A),T_A\ \text{的下界（即 }L_A\ \text{的强制增长）};\ \text{一般矛盾}✗;\ \mathrm{cov}_9\ \text{形状（C-440 遗留 ✓）}$$
$$\textbf{（与 C-440 的关系 ✓）}:\ \text{C-440 的 }\mathrm{min\_excess}_9\ \text{闸门与本文 }L_A\ \text{闸门\ \textbf{互补}:\ 前者管 }|U^c|\ \text{的可覆盖量（}a\le49\ \text{主导），后者管层内部几何 ✓}$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "有效容量" "激活方向" "精化闸门"
技术词 有效容量    命中文件数=0    ::
技术词 激活方向    命中文件数=0    ::
技术词 精化闸门    命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 有效容量 | 0 | 0 | 0（本档自造标签 ✓） |
| 激活方向 | 0 | 0 | 0（本档自造标签 ✓） |
| 精化闸门 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词**两空间皆 0** ⟹ 自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 恒等式核验 ＋ §0(3)(4)(5)(6) 四结论 ＋ §2 表 ＋ §3 诚实判定**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **两处必改**已在 §0(1)(4) 显式标注 ✓✓（防误用 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）
- **不声称** 119 已排除 ✗；**不声称** $L_A$ 有正下界 ✗；不声称 P1 成立 ✗（V290）
