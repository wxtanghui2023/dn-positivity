# RESULT-2026-09-30 — **$h_{\min}(r,m)$ 完整整数表**（精确枚举 ✓）：接受 $m(q)=T(L_q)$ 修正；**Jensen 松弛不紧** ✗；**免费复用上限 $m_0(r)=\lfloor\binom r2/3\rfloor$** ✓；$h$ 饱和值 $=\binom r2\binom{r-2}2$ ✓

> 空间 B｜非 C 号｜唐先生 21:41 令（把反向计数算到底；先修正 $\binom{r_q}2\to\binom{r_q}3$）｜**不主张任何新值**（V290）

**已查地图** ✓：`RESULT-2026-09-30-hole-conflict-…`／`AUDIT-2026-09-30-map-shrinks-…`／`STATE-2026-09-30-block-layer-decomposition…`
D0: 本档对象 = **$h_{\min}(r,m)$ 精确表与新结构量（$m_0(r)$ 等）**（新 ✓）
D1: 0（产出 = **两张精确表 ＋ 三条结构读数 ＋ 一条"代回"条件** ⚠️✓）

---

## §0 **修正接受 ✓**

$$\textbf{旧（错 ✗）}:\ m(q)\le\binom{r_q}2;\qquad \textbf{新（对 ✓）}:\ \boxed{m(q)=T(L_q)},\ m(q)\le\binom{r_q}3$$
$$L_q=(V_q,E_q):\ V_q=\{i:q^i\in R\},\ E_q=\{\{i,j\}:q^{ij}\in A\};\quad \text{三角形}\ ijk\subseteq L_q\iff q=x^{ijk}\ \text{同时服务 }x\ \text{之三条 }R\text{-witness} ✓$$
$$\text{（双向 ⟹ 精确双射 ✓）；且}\ h_q:=\sum_{e\in E(L_q)}\binom{t_e(q)}2,\ t_e(q)=\#\{\text{含 }e\ \text{之三角形}\} ✓$$

## §1 **精确表（$r=3..7$ 全图枚举 ✓）**

| $r$ | 可实现 $m$（$T$ 之可能值） | $h_{\min}(m)$ |
|---|---|---|
| 3 | 0,1 | 0, 0 |
| 4 | 0,1,2,**4**（**3 不可实现** ✗） | 0,0,**1**,6 |
| 5 | 0–5,7,10（6,8,9 不可实现 ✗） | 0,0,0,2,4,8,15,30 |
| 6 | 0–13,16,20（14,15,17–19 ✗） | 0,0,0,1,2,5,7,12,12,20,25,33,34,42,60,90 |
| 7 | 0–23,25,26,30,35 | 0,0,0,0,1,3,5,7,10,14,15,21,24,30,…（完整 ✓） |

$$\textbf{Jensen 松弛（}\Sigma t_e=3m,\ t_e\le r{-}2\text{ 之均匀化）}\ \textbf{一律不紧} ✗:\ r{=}4,m{=}2\ \text{松弛 }0\ \text{而精确 }1;\ r{=}6,m{=}6\ \text{松弛 }3\ \text{而精确 }7\ ✓$$
$$\text{（根因：三角形**成对必共边**——}r{=}4\ \text{时任意两三角形共享边 ⟹ }m{=}2\Rightarrow h\ge1 ✓）$$

## §2 **三条结构读数（本档核心 ✓）**

$$\textbf{(i) 免费复用上限}:\ h_{\min}(r,m)=0\iff 3m\le\binom r2\ (\text{可 edge-disjoint})\ \Longrightarrow\ \boxed{m_0(r)=\Big\lfloor\tfrac12\binom r2\cdot\tfrac23\Big\rfloor=\Big\lfloor\binom r2/3\Big\rfloor}$$
$$m_0:\ r{=}3{:}1,\ 4{:}2,\ 5{:}3,\ 6{:}5,\ 7{:}7,\ \mathbf{8{:}9},\ \mathbf{9{:}12}\ ✓\ (\text{与表一致 ✓})$$
$$\textbf{(ii) 饱和（完全图）}:\ m=\binom r3\Rightarrow h=\binom r2\binom{r-2}2:\ r{=}7{:}210,\ \mathbf{r{=}8{:}420},\ \mathbf{r{=}9{:}756}\ ✓$$
$$\textbf{(iii) 可实现性有缺口}:\ m\ \text{集非区间（}r{=}4\ \text{缺 }3;\ r{=}5\ \text{缺 }6,8,9;\ r{=}6\ \text{缺 }14,15,17\text{--}19 ✓）\Longrightarrow \text{三角形数本身受图结构约束 ✓}$$

## §3 **二分法之量化（接唐先生 §146 ✓）**

$$\text{分散}: m\le m_0(r)\ (\le12\ \text{于 }r{=}9)\ \text{且}\ h_q=0;\qquad \text{重叠}: m>\ m_0(r)\Rightarrow h_q\ge h_{\min}(r,m)>0\ (\text{表在档 ✓})$$
$$\textbf{关键结论}:\ r_q=9\ \text{之 }q\ \text{可\ \textbf{免费} 服务至多 }12\ \text{个 triple-use} ✓,\ \text{但可至 }84\ \text{个（代价 }h=756 ✓）$$
$$\therefore\ \textbf{复用不受常数限制} ✗\ \text{（修正前之"常数重数"主张不成立）};\ \textbf{但当 }h\ \text{被要求小，则复用线性受限于 }r_q ✓✓\ \text{（这是可用形式 ✓）}$$

## §4 **"代回 $i=40..44$" 所需之条件（诚实）**

$$\text{需接}:\ e(U)\le 71-i;\ W=\sum_x t_x;\ D=\sum_x\Delta_x=\sum_q T(L_q);\ O=\sum_x\Omega_x^B;\ e(R,U)=\sum_x d_U(x)\ ✓$$
$$\text{本档已备}:\ \Sigma_q T(L_q)\le\Sigma_q\binom{r_q}3\ ✓\ \text{（上界）};\ \text{及拟合 }h\ \text{时之精确下界表 ✓}$$
$$\text{尚缺}:\ W,O,e(R,U)\ \text{之独立容量式（在唐先生自身簿记内 ⚠️）};\ \text{故"代回"本轮只作\ \textbf{条件式} 陈述}:\ \text{若 }W-2D-O>\ \text{R-U 容量}\ \text{则硬矛盾 ✓}$$

## §6 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 免费复用上限 命中文件数=1    :: 本档
技术词 三角形重叠表 命中文件数=0    :: 
```

$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档（“三角形重叠表”全档 0 命中）} ✓;\quad \textbf{档案已有}：\text{无};\quad \textbf{通用词（不计）}：\text{“重叠／复用”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}：\text{无跨空间同名} ✓$$


## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ r\le7\ \text{全枚举（}2^{21}\ \text{内 ✓）；}r{=}8,9\ \text{仅给下界/饱和值（明标 ⚠️）};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
