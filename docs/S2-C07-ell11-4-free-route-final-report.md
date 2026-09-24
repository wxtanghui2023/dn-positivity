已查地图：命中（`S2-C07-ell11-4-source-hunt-exhausted-free-routes`）⟹ `\ell_2(11,4)` 免费路线终报，不开新案
D0: 本档对象 = **`\ell_2(11,4)` 追源终报**：`P14`（1990 IEEE TIT）与 Davydov 2001 两份**已入档原文**的表体核对结果（**均不含 `(11,4)`**）＋ **文献状态判定** ＋ **剩余唯一入口** ＋ **两攻击入口的合法性**
D1: 1（首次把该节点核到两份原文表体；产出"文献中该节点两侧皆未闭合"的判定）
[RESEARCH]

# **`\ell_2(11,4)` 免费路线终报**

## §1 本轮入档两份原文（`sources/`）

```
$$\boxed{P14}\ \text{1990 IEEE TIT（7 页）}\ \Longrightarrow\ \texttt{sources/P14-1990-IEEE-TIT-covering-radius.pdf}$$ ✓
$$\qquad \text{表体核对}:\ \text{给 }t[40,18]\ge7,\ t[46,12]\ge12,\ t[46,36]=3,\ t[62,33]\ge8;\ \boxed{\ell(22,6)\ge41,\ \ell(10,2)\ge47}$$ ✓✓
$$\qquad \text{引用确认}:\ [1]=\text{BP 1990}\ (\text{“}l(m,R)\ \text{表},\ R\le m\le24\text{”});\ [S]=\ t[n,k]\ \text{表}\ (n\le64)\ \Longrightarrow\ \textbf{BP 表确实覆盖 }(11,4)$$ ✓✓
$$\qquad \textbf{但不含 }(11,4)\ \text{本身};\ \text{且给出}\ \textbf{下界方法学}（\text{van Wee／线性不等式}）$$ ✓✓
$$\boxed{\text{Davydov 2001}}\ \Longrightarrow\ \texttt{sources/Davydov-2001-new-constructions-covering-codes.pdf}\ (\text{12 页})$$ ✓
$$\qquad \textbf{Table 1}=\text{“Upper bounds on the length function }\ell(r,R;2)\text{”}\ \text{逐项对比书内 Table 7.3};\ \textbf{含 }R=4\ \text{项}:r=19\ (84{\to}82),\ 20\ (93{\to}90),\ 21\ (125{\to}122),\ 26,\ 40,\ 44,\ 48,\ 52,\ 56,\ 60,\ 64$$ ✓✓
$$\qquad \Longrightarrow\ \textbf{该表只在"作者有改进"的格上列值};\ \boxed{(r,R)=(11,4)\ \textbf{不在其中}}$$ ✓✓
$$\text{程序化复核}:\ \text{两 PDF 全文正则扫 }\ell(m,r)\ \text{型参数对} \Longrightarrow\ \textbf{零命中}$$ ✓
```

## §2 文献状态判定（**关键**）

```
$$\text{1985 CKMS 表}:\ t_2[20,9]=\boxed{4\text{-}5};\quad \text{1997 综述 Table B}:\ \text{同样}\ \boxed{4\text{-}5}\ (\text{先生已核})$$ ✓✓
$$\Longrightarrow\ \text{“4-5”}\equiv\ \text{已知 }t\le5\ \text{（存在 }R{=}5\ \text{的 }[20,9]\ \text{码）},\ \text{且\textbf{未知 } }t\le4$$ ✓✓
$$\text{翻译成 }\ell:\ t_2[20,9]\le R\iff\ell_2(11,R)\le20 \Longrightarrow\ \boxed{\textbf{已知 }\ell_2(11,5)\le20;\ \ell_2(11,4)\le20\ \textbf{未知}}$$ ✓✓✓
$$\textbf{且逆侧亦未闭合}:\ \text{“4”为下界 }\Longrightarrow\ \text{已知 }\ell_2(11,3)\ge21\ (\text{无 }R{=}3\ \text{码});\ \text{但 }\ell_2(11,4)\ge21\ \textbf{未被证明}$$ ✓✓
$$\text{本轮核过的后续文献}:\ 1990\ (P14)\ \text{无};\ 2001\ (Davydov)\ \text{无};\ 2025\ (arXiv{:}2511.02542)\ \text{无} \Longrightarrow\ \textbf{未见该格被改进}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{该节点在可及文献中\textbf{两侧皆未闭合}}:\ \text{既无 }\ell_2(11,4)\le20\ \text{的构造，也无 }\ell_2(11,4)\ge21\ \text{的证明}}$$ ✓✓✓
$$\textbf{终态}:\ \boxed{C07\ \text{唯一剩余节点}=“\exists\ 11\times20\ \text{二元矩阵 }H\ \text{使 }\mathbb F_2^{11}\ \text{被}\le4\text{项列和覆盖？}}$$ ✓✓✓
```

## §3 两个攻击入口（按 `AMEND-19` 现在**均合法**）

```
$$\boxed{P2\ \text{构造侧}}:\ \text{找出 }[20,9]\ \text{码／}11\times20\ \text{矩阵，}R\le4 \Longrightarrow \boxed{t_2[20,9]=4}$$ ✓
$$\qquad \textbf{利好}: \text{计数松弛大}——\#\{\text{子集}\le4\}=6196\ \gg\ 2048\ \text{个 syndrome} \Longrightarrow \textbf{构造\textbf{不}受紧计数阻碍}$$ ✓✓✓
$$\boxed{P1\ \text{障碍侧}}:\ \text{证明不存在} \Longrightarrow \boxed{t_2[20,9]=5}$$ ✓
$$\qquad \text{工具（档级）}:\ \text{van Wee 型线性不等式};\ \text{线性结构约束};\ \text{对偶距离}$$ ✓
$$\Longrightarrow\ \text{与 }(19,9)\ \text{的关键差异}:\ \text{那里计数紧（}1160/1024\text{）}\to\ \text{实际被外部下界一击判死};\ \text{这里计数松}\to\ \textbf{构造侧更可能先通}$$ ✓✓✓
```

## §4 剩余唯一入口（若要一步定生死）

```
$$\boxed{E1}\ \text{《Covering Codes》(1997) \textbf{Table 7.3}}\ (=\ell(r,R)\ \text{总表};\ \text{Davydov 2001 引其为基准})$$ ✓✓✓
$$\boxed{E2}\ \text{BPW 1989, IEEE TIT 35(1) 99–109}\ ——\ \textbf{其表覆盖 }m\le12,r\le12\ \text{故\textbf{必含} }(11,4)$$ ✓✓✓
$$\boxed{E3}\ \text{BP 1990（Springer 会议卷 pp.\ 9–15）};\quad \boxed{E4}\ \text{LNCS 781 (1994) pp.\ 51–55}$$ ✓✓
$$\text{任一给出该格值} \Longrightarrow \text{链 B 立即收口};\ \text{四者皆取不到} \Longrightarrow \textbf{进入攻击（}P2\ \text{优先）}$$ ✓✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；不转 `Zone-B`；**未进入 }SAT$$ ✓
【边界】 §2 的 "4-5" 来自两份独立表；§3 的 6196/2048 为实算算术 ✓

## §附 【技术词回查】（补录）
```
技术词 length function  命中文件数=5    :: ./S2-C07-chainA-closed-chainB-compressed.md ./S2-C07-modern-closure-check-19-9-20-9.md ./S2-C07-two-proof-chains-expanded.md 
技术词 construction     命中文件数=58   :: ./B-SERIES-INDEX.md ./ARCHIVE-P34-FINAL-2026-09-02.md ./p36-4-arithmetic-operator.md 
```
