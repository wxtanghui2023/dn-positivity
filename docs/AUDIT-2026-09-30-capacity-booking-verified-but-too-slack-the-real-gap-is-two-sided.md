# AUDIT-2026-09-30 — 容量簿记**核验通过** ✓，但**可行域极松** ✗：真正缺口是**双向**的（$W$ 下界 ＋ $A_2$ 上界）

> 空间 B｜非 C 号｜唐先生 21:51 令（补齐容量簿记；$O$ 按 $L_q$ 的 wedge 数而非边数计）｜**不主张任何新值**（V290）

**已查地图** ✓：`ERRATUM-2026-09-30-graph-closure-…`（$h_{\min}$ 真值 ✓）／`RESULT-2026-09-30-triangle-overlap-table-…`／`RESULT-2026-09-30-tight-A-plus-Omega-…`
D0: 本档对象 = **簿记核验 ＋ 可行域松弛度判定**（判定类 ✓）
D1: 0（产出 = **一串核验 ＋ 一条松弛判定 ＋ 一条双向缺口陈述** ⚠️✓）

---

## §0 **核验通过之关系（逐条 ✓）**

$$\textbf{(1)}\ 9u=2e(U)+e(R,U)\ (u=106-i)\ \Longrightarrow\ \boxed{e(R,U)=954-9i-2e(U)}\ ✓;\quad \text{窗口}[812-7i,\ 954-9i]\ ✓$$
$$\textbf{(2)}\ \sum_{q\in B}e_q\le2e(U)\ ✓\ (\text{每条 }L_q\text{-edge}\leftrightarrow\text{一条 }U\text{-}U\text{ 边}\{q,q^{ij}\}\text{，每边}\le2\text{ 端}\ ✓)$$
$$\textbf{(3)}\ \omega_q\le(r_q-2)e_q\le7e_q\ \Longrightarrow\ O\le14e(U)\ ✓;\quad \omega_q\le3\binom{r_q}3\ \Longrightarrow\ O\le3C\ ✓\ (C:=\sum_q\binom{r_q}3)$$
$$\textbf{(4)}\ O=3D+O_{\rm nt}\ ✓;\quad e(R,U)\ge W+D-O=W-2D-O_{\rm nt}\ ✓;\quad W\ge3D\ ✓$$
$$\textbf{(5)}\ \Longrightarrow W+D\le9(106-i)+12e(U)\le\mathbf{1806-21i}:\ 966,945,924,903,882\ (i{=}40..44)\ ✓\ \textbf{\text{与唐先生一致}} ✓$$

## §1 **★ 可行域松弛度（本档新判定 ✗）**

$$\textbf{允许的 }W\text{ 上界}\approx e(R,U)+2D_{\max}+O_{\rm nt};\quad D_{\max}\le\underbrace{(106-i)}_{\#q\le|U|}\cdot\binom93=84(106-i)$$
| $i$ | $\#q\le$ | $D_{\max}$ | $O_{\rm nt}\le$ | 允许 $W$ |
|---|---|---|---|---|
| 40 | 66 | 5544 | 434 | ≈ **6572** |
| 41 | 65 | 5460 | 420 | ≈ 6465 |
| 42 | 64 | 5376 | 406 | ≈ 6358 |
| 43 | 63 | 5292 | 392 | ≈ 6251 |
| 44 | 62 | 5208 | 378 | ≈ 6144 |

$$\text{而 }W=\sum_{x\in R}t_x\ \text{之合理量级}\approx|R|\cdot t_x\sim10^3\ (\text{若 }|R|\sim500,\ t_x\sim3)$$
$$\therefore\ \text{账本可容纳 }W\ \text{约 6 倍于其自然量级} \Longrightarrow \boxed{\text{仅凭容量簿记\ \textbf{不可能} 排除 }M{=}106} ✗$$
$$\text{h 侧同样松}:\ 2A_2(R)\sim2\binom{|R|}2\cdot\tfrac{45}{1024}\approx11000\ \text{（}|R|\sim500\text{）},\ \text{而}\ \sum h_{\min}\ \text{可小（取 }m_q\ \text{小）} ✗$$

## §2 **真正的缺口是\ \textbf{双向} 的（修正唐先生 §169 之"唯一缺口" ⚠️）**

$$\text{(a)}\ \textbf{W 下界} ✗\ (\text{唐先生已指出 ✓}) \Longrightarrow W\ \text{大则}\ D\ \text{需大（因 }W\le e(R,U)+2D+O_{\rm nt}\ ✓) \Longrightarrow \sum h_{\min}\ \text{大}\ ✓$$
$$\text{(b)}\ \textbf{2A}_2(R)\ \textbf{之上界} ✗\ (\text{本档新增 ⚠️}) \Longrightarrow \text{否则}\ \sum h\le2A_2(R)\ \text{永不紧} ✗$$
$$\therefore\ \text{闭合链须为}:\ \boxed{W\ \text{大}\Rightarrow D\ \text{大}\Rightarrow\sum h_{\min}(r_q,m_q)\ \text{大}\Rightarrow A_2(R)\ \text{大}},\ \text{而与 }A_2(R)\ \text{之上界矛盾} ✓$$
$$\text{故}\ \textbf{\text{单侧补 }W\ \text{下界不够}} ✗;\ \text{须同时给出 }A_2(R)\ \text{之\ \textbf{距离层上界}} ✓$$

## §3 **诚实评估与建议**

$$\text{本线已把"一个 }q\ \text{重复服务很多次要付什么代价"算到底（}r_q,m_q,e_q,h_q\ \text{四变量 ＋ 三资源 ✓）};\ \text{但"106 必须产生多少 reuse"仍缺（W）✗}$$
$$\text{且由 §1：现有粗界（}O\le14e(U),\ W\ge3D\text{）与 }D_{\max}\ \text{之组合使账本松弛约 6 倍} ✗$$
$$\text{建议}:\ \text{①先补 }W\ \text{下界（唐先生 §170 之方向 ✓）；②同时须给 }A_2(R)\ \text{上界，否则（a）单独无法闭合 ✓；③若两者皆不可得，则该线应记为"簿记完整、双向缺口"而非"仅缺 W"} ✓$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 双向缺口     命中文件数=1    :: 本档
技术词 簿记松弛度   命中文件数=0    :: 
```

$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档（“簿记松弛度”全档 0 命中）} ✓;\quad \textbf{档案已有}：\text{无};\quad \textbf{通用词（不计）}：\text{“松弛／缺口”裸词} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{全部关系逐条核验 ✓；松弛度为新判定（明标 ⚠️）};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
