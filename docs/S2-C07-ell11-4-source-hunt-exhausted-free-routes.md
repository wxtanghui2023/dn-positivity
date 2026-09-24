已查地图：命中（`S2-C07-chainA-closed-chainB-compressed`）⟹ `\ell_2(11,4)` 追源结果，不开新案
D0: 本档对象 = **`\ell_2(11,4)` 追源（免费路线）结果**：确认原始表出处（LNCS 781, 1994, pp. 51–55）与三点已锁事实；**免费网络路线穷尽、值未取得**；给出**唯一剩余入口**与三条合法分叉
D1: 1（首次把 C07 剩余节点压到单一外部资料；产出"需付费原文"的明确结论）
[RESEARCH]

# **`\ell_2(11,4)` 追源：免费路线已穷尽**

## §1 已锁事实（本轮新增，档级）

```
$$\textbf{① 原始表出处确认}:\ \text{Lobstein–Pless, “The Length Function: a Revised Table”, }\boxed{\text{LNCS 781, pp. 51–55, Springer 1994}}$$ ✓✓
$$\qquad \text{摘要逐字（LRI 页面）}:\ \text{"We give a table with the most current available information for the shortest length of a binary code with codimension }m\ \text{and covering radius }r\ \text{for}\ 1\!<\!m\!<\!25,\ 1\!<\!r\!<\!13\text{"}$$
$$\qquad \Longrightarrow\ \boxed{(m,r)=(11,4)\ \textbf{确在该表范围内}}$$ ✓✓✓
$$\textbf{② 现代综述确认其为直接来源}:\ \text{Cohen–Litsyn–Lobstein–Mattson 1997 综述把 length function 追溯至 BPW 1989，并列 Lobstein–Pless 1994 revised table 为直接资料}$$ ✓
$$\textbf{③ 1997 综述\textbf{未}收掉该节点}:\ \text{其 Table B 在 }(k,n)=(9,20)\ \text{仍记 }\boxed{4\text{-}5}\ \Longrightarrow \textbf{该综述不含 }exact$$ ✓✓
$$\textbf{④（先生补）链 A 加固}:\ \text{1997 综述亦给 }n=19,t=3\ \text{的独立下界推导} \Longrightarrow t[19,9]\ge4\ \text{再获一路支持}$$ ✓✓
```

## §2 免费路线穷尽（本轮实证）

```
$$\text{① Syracuse 技术报告 PDF（Covering Radius 1985–1994）}\ \Longrightarrow\ \textbf{5.8 KB stub（1 页 42 字符）};\ \text{无表}$$ ✗
$$\text{② }arXiv{:}2511.02542\ (2025)\ \text{全文}\ \Longrightarrow\ \textbf{(11,4) 命中 0}$$ ✗
$$\text{③ }lri.fr/{\sim}lobstein\ \text{三个页面（摘要页／书评页／主页）}\ \Longrightarrow\ \text{仅摘要与书目信息};\ \textbf{无表体}$$ ✗
$$\text{④ 主页 27 个链接中无表文件};\ \text{试 }\texttt{length.ps/.pdf},\ \texttt{table.ps},\ \texttt{lf.ps},\ \texttt{tables.html}\ \Longrightarrow\ \textbf{全 404}$$ ✗✗
$$\Longrightarrow\ \boxed{\text{免费网络路线\textbf{穷尽}};\ \ell_2(11,4)\ \text{值\textbf{未取得}}（诚实标注）}$$ ⚠️
```

## §3 唯一剩余入口（三条合法分叉）

```
$$\boxed{E1}\ \text{取 }\textbf{LNCS 781 (1994) pp. 51–55}\ \text{原文（Springer，付费）}\ ——\ \textbf{最直接}$$ ✓✓✓
$$\boxed{E2}\ \text{取 }\textbf{《Covering Codes》(1997)}\ \text{书内 }l(m,R)\ \text{表（Chapter 7 相关）}$$ ✓✓
$$\boxed{E3}\ \text{取 }\textbf{BPW 1989, IEEE TIT 35(1) 99–109}\ \text{（付费）};\ \text{或 Davydov 后续 length-function 表/改进}$$ ✓
$$\textbf{判定规则（不变）}:\ \text{表给 }exact\ \Longrightarrow\ \text{链 B 立即收口（}t=4\ \text{或 }5\ \text{二选一）};\ \text{若仍为 bound} \Longrightarrow \text{保留 frontier}$$ ✓✓
$$\textbf{禁止}:\ \text{不得从 1997 的 }t[n,k]\ \text{表反推（该表在 }(9,20)\ \text{处就是 }4\text{-}5\text{）};\ \text{不得用相邻参数替代};\ \textbf{不进入 }SAT$$ ✓✓
```

## §4 当前两链终态

```
$$\begin{array}{c|c|c}
\text{链}&\text{状态}&\text{节点}\\
\hline
A:\ t_2[19,9]&\boxed{\textbf{CLOSED}\ (=4,\ DROP)}&\ell_2(10,3)\ge21\ (\text{两路支持})\\
B:\ t_2[20,9]&\textbf{单一剩余整数节点}&\boxed{\ell_2(11,4)\ ?}\\
\end{array}$$ ✓✓✓
$$\Longrightarrow\ \textbf{压缩成果}:\ \text{整个}C07\ \text{只剩}\ \boxed{\text{一个外部整数量}};\ \text{且其原始表位置已确证（LNCS 781）}$$ ✓✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；不转 `Zone-B`；不进入 `SAT` ✓
【边界】 §1 的"确在表范围内"来自**摘要逐字**；表值**未取得** ⟹ 不得写 }exact$$ ⚠️

## §附 【技术词回查】（补录）
```
技术词 length function  命中文件数=4    :: ./S2-C07-chainA-closed-chainB-compressed.md ./S2-C07-modern-closure-check-19-9-20-9.md ./S2-C07-two-proof-chains-expanded.md 
技术词 table            命中文件数=101  :: ./C293-astra-liouville-source-verification-and-mangerel-grh-anchor.md ./p4-dilation-audit.md ./E20-E40-zero-density-2026-read.md 
```
