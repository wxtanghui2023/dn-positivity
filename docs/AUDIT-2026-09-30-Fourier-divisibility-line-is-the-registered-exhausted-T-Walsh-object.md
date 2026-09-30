# AUDIT-2026-09-30 — Fourier 可除性线 ＝ **档案已登记且已穷尽之 $T=A+I$ Walsh 对象** ✗；两式核验：一真一假（假者被真码反驳）

> 空间 B｜非 C 号｜唐先生 16:13「先搜索以往的研究，不要重复掉坑」｜**不主张任何新值**（V290）
> 时间：2026-09-30 16:2x

**已查地图** ✓：`AUDIT-2026-09-29w`（坐标-cell Walsh，r≤7 无矛盾 ✗）／`ASSETS-REGISTRY` L1899–1905（**复现守卫** ✓）／L3198（Walsh 功率谱 ⟺ 距离分布 ✗）／L3574（Parseval ⟹ SDP-3 ✗）
D0: 本档对象 = **档案已有**（$T$ Walsh 对象 ＋ 用户两式）之**归属判定与真码核验**（新数学对象：无 ✗）
D1: 0（产出 = **一条归属判定 ＋ 一条真码反驳 ＋ 一条合法方向重述** ⚠️✓）

---

## §0 **归属判定：本轮之对象 ＝ 已穷尽之 OB-1 模 11 定理对象** ✗

$$\text{本轮核心式}:\ \widehat e(S)=(11-2|S|)\widehat{1_C}(S)\quad\Longleftrightarrow\quad T:=A+I=I+\sum_{i=1}^{10}\sigma_i,\ \textbf{Walsh 对角化，特征值 }11-2w\ ✓$$
$$\text{档案逐字}:\ \text{“这正是档案 }P1\text{-REAUDIT-2026-09-27 的 }\textbf{OB-1 模 11 定理对象}”\ ✓\ (\texttt{ASSETS-REGISTRY} L1900)$$
$$\text{该对象\ \textbf{已第 3 次独立回潮}（逐字）}:\ \text{R3 坐标标记 excess} \to \text{C-417 层坍缩} \to \text{C-428 开邻域+Walsh} ✓$$
$$\boxed{\text{登记守卫（档案逐字）}:\ \text{任何 119-攻击\ \textbf{不可表为算子 }T=A+I\ \text{之 Walsh／谱形式（已穷尽）}}} ✗$$
$$\therefore\ \text{本轮线\ \textbf{落在守卫之内}} ⟹ \textbf{不得作为新机制计入} ✗✓$$

## §1 **更强的两条存档结论（该路的天花板）**

$$\textbf{(i)}\ \text{Delsarte--MacWilliams}:\ \text{Walsh }\textbf{功率谱}\ \{P_j{=}\sum_{|S|=j}\hat f(S)^2\}\ \Longleftrightarrow\ \text{距离分布}\ \{D_i\}\ (\text{Krawtchouk 可逆})$$
$$\qquad\Longrightarrow\ \textbf{Fourier 之自然内容 ＝ 距离分布之重编码} ✗\ (\texttt{ASSETS-REGISTRY} L3198)$$
$$\textbf{(ii)}\ \text{Parseval（二次）以 SDP 松弛 ⟹ \textbf{SDP-3 ＝ }105.2223\Rightarrow106}\ ✗\ (\text{L3574 逐字}:\ \text{“坐标-cell 路最终仍落在同一天花板”})$$

## §2 **用户两式之真码核验（120-码，已验证 R=1 覆盖码 ✓）**

$$\textbf{式①}\ \widehat e(i)=9(M-2a_i)\ ——\ \textbf{成立 ✓}:\ \text{实测 }\hat e(i)=[0,0,-72,0,-18,0,0,0,18,0]\ ✓\ (M{=}120)$$
$$\qquad\text{且 }m_i=M+9a_i-512\ \text{亦\ \textbf{成立} ✓}（a_i=[60,60,64,60,61,60,60,60,59,60]）$$
$$\textbf{式②}\ \text{“可除性 ⟹ }a_i\ \text{偶 ⟹ }\bigoplus_{c\in C}c=0”\ ——\ \textbf{假} ✗✗$$
$$\qquad\text{根因}:\ 2(n-1)\mid\widehat e(i)\ \Longleftrightarrow\ M\ \text{偶}\ ——\ \textbf{对任何偶 }M\ \textbf{自动成立} ⟹ \textbf{零信息} ✗$$
$$\qquad\textbf{真码反驳（决定性 ✓）}:\ a_i\ \text{含 }\mathbf{61,59}\ (\textbf{奇})\ ✗;\quad \boxed{\bigoplus_{c\in C}c=\mathbf{272}\ne0}\ ✗$$
$$\qquad\Longrightarrow\ \text{“}\bigoplus c=0\text{”被一个\ \textbf{已验证的 }R{=}1\ \text{覆盖码\ 直接推翻} ✗✓$$
$$\textbf{式③}\ \text{二阶 }14\mid\widehat e(ij):\ \text{用户\ \textbf{已自撤} ✓（恒等，\textbf{无 mod 7 内容} ✓）}$$

## §3 **合法方向（档案自己给的，唯一一条）**

$$\boxed{\text{新不变量必须携带 }T\ \text{之 Walsh 谱\ \textbf{看不到} 的信息 ⟺ \textbf{Booleanity 之外的排列／交叠结构}}} ✓\ (\text{L1904 逐字})$$
$$\text{而 }a_i,a_{ij}\ (\text{即 }|S|\le2\ \text{之 Walsh 系数})\ \textbf{全在 }T\text{-谱内} ⟹ \text{“消去 }a_{ij}\text{”之计划亦落在已穷尽对象内} ✗✓$$

## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{真码反驳为决定性，且为\ \textbf{反向核验} 所得（本线铁律 ✓）};\ \textbf{(D3)}\ \text{未主张新值／未取文献原文／未碰 RH} ✓$$
$$\textbf{附}\ \text{技术小疵}:\ 62\text{-码文件格式与解析器不符（}|C|{=}0\ \text{），未影响结论（120-码已足够 ✓）} ⚠️$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
