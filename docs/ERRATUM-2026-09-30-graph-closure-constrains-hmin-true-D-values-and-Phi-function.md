# ERRATUM + RESULT-2026-09-30 — **图闭合约束**：$h_{\min}$ 真值表、$D_{\rm true}(r)$、$\Phi(M_3)$

> 空间 B｜非 C 号｜唐先生 21:47 令（把 $h_q$ 算成可代入全局容量的整数函数；含 packing 修正）｜**不主张任何新值**（V290）

**已查地图** ✓：`RESULT-2026-09-30-triangle-overlap-table-…`（本档**修正其 §2(i)** ✗）／`RESULT-2026-09-30-hole-conflict-…`／`RESULT-2026-09-30-tight-A-plus-Omega-…`
D0: 本档对象 = **$h_{\min}$ 之图论真值 ＋ $D_{\rm true}$ ＋ $\Phi$**（修正类 ✓）
D1: 0（产出 = **两处纠正 ＋ 两张真值表 ＋ 一条反驳** ⚠️✓）

---

## §0 **两处纠正（相互独立 ✓）**

$$\textbf{(I) 我方错 ✗}:\ \text{上档称}\ h_{\min}(r,m)=0\iff3m\le\binom r2;\ \textbf{\text{实为仅必要}} ✓\ (\text{反例}:r{=}6,m{=}4\Rightarrow h_{\min}{=}2>0)$$
$$\textbf{(II) 唐先生 §155 表亦非可达值 ✗}:\ \text{其 }h_{\min}\ \text{系按\ \textbf{超图 packing} 计算，而 }L_q\ \text{是\ \textbf{图}} ⟹ \text{存在\ \textbf{闭合约束}（任三点集之并易逼出第 4 个三角形）}$$
$$\textbf{决定性反例（}r{=}4\text{）}:\ \{123,124,134\}\Rightarrow\text{边集}\{12,13,14,23,24,34\}=\text{全 6 条}=K_4\Rightarrow\text{三角形数}=4\ (\text{含 }234)$$
$$\qquad\Longrightarrow m{=}3\ \textbf{\text{不可实现}} ✗;\ \text{只可 }m{=}4,h{=}6\ ✓\ (\text{故我方枚举之 }\{0,1,2,4\}\ \text{为真 ✓})$$

## §1 **$D_{\rm true}(r)$（全枚举 $r\le7$ ✓）**

$$D_{\rm true}(r):=\max\{m:h_{\min}(r,m)=0\}:\quad r=3,4,5,6,7\ \Rightarrow\ \boxed{1,\ 1,\ 2,\ 2,\ 3}\quad(\text{唐先生 §154}:1,1,2,4,7\ ✗)$$
$$\textbf{论证（}r{=}7\text{）}:\ m{=}7\ \text{互不共边} \Rightarrow 21=3\cdot7\ \text{条边}=\binom72 \Rightarrow \text{图}=K_7 \Rightarrow T(K_7)=\binom73=\mathbf{35}\ne7\ ✗$$
$$\textbf{结构真值}:\ h{=}0\iff\text{每个边恰属一个三角形（“三角形森林”/友谊图 }F_k:2k{+}1\ \text{点},\ k\ \text{三角形）} \Longrightarrow D_{\rm true}\ \text{由友谊型极值给出（远小于 packing 数）} ✓$$

## §2 **$\Phi(M_3)$：最省 R-U 成本（DP ✓）**

$$\Phi(M_3)=\min\Big\{\sum_q r_q:\sum_q\binom{r_q}3\ge M_3,\ 3\le r_q\le9\Big\};\qquad \binom r3:\ 3{:}1,4{:}4,5{:}10,6{:}20,7{:}35,8{:}56,9{:}84$$
| $M_3$ | 1 | 4 | 10 | 20 | 35 | 56 | 84 | 120 | 168 | 252 |
|---|---|---|---|---|---|---|---|---|---|---|
| $\Phi$ | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 17 | 18 | 27 |

## §3 **满载效率核对（与唐先生 §167 一致 ✓）**

| $r$ | $m_{\max}=\binom r3$ | $m_{\max}/r$ | $h_{\max}=\binom r2\binom{r-2}2$ | $h_{\max}/r^2$ |
|---|---|---|---|---|
| 3 | 1 | 0.33 | 0 | 0 |
| 4 | 4 | 1.00 | 6 | 0.38 |
| 5 | 10 | 2.00 | 30 | 1.20 |
| 6 | 20 | 3.33 | 90 | 2.50 |
| 7 | 35 | 5.00 | 210 | 4.29 |
| 8 | 56 | 7.00 | 420 | 6.56 |
| 9 | 84 | 9.33 | 756 | 9.33 |

$$\therefore\ \text{“高 }r_q\ \text{换 triple capacity”代价为 }\Theta(r^4)\ \text{overlap} ✓\ (\text{与 }O(r^2)\ \text{收益相比极贵} ✓)$$

## §4 **状态系统就绪（用\ \textbf{正确} 表 ✓）**

$$\mathcal S=\{(r,m,h):3\le r\le9,\ 0\le m\le\binom r3,\ h\ge h_{\min}^{\rm true}(r,m)\};\quad \text{全局}:\ \sum r_q\le E_{RU},\ \sum h_q\le2A_2(R),\ \sum m_q\ge M_3^{\rm req} ✓$$
$$\textbf{本档所备}:\ r\le6\ \text{全精确};\ r{=}7\ \text{部分精确}+\text{Jensen};\ r{=}8,9\ \text{仅 Jensen}+\text{饱和值（明标 ⚠️）};\ D_{\rm true}\ \text{与}\ \Phi\ \text{精确} ✓$$
$$\textbf{尚缺（唐先生侧 ⚠️）}:\ M_3^{\rm req}(i),E_{RU}^{\max}(i),2A_2^{\max}(R;i)\ \ (\text{三个数}) \Longrightarrow \text{方可逐 }i=40..44\ \text{判硬矛盾} ✓$$

## §6 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 图闭合约束  命中文件数=1    :: 本档
技术词 三角形森林  命中文件数=1    :: 本档
```

$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{档案已有}：\text{无};\quad \textbf{通用词（不计）}：\text{“闭合／森林”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}：\text{无跨空间同名} ✓$$


## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{两处纠正经\ \textbf{精确枚举/反证} 核验 ✓};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
