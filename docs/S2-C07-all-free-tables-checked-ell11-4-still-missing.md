已查地图：命中（`S2-C07-ell11-4-free-route-final-report`）⟹ 全部免费表体核对完毕，不开新案
D0: 本档对象 = **又入档两份原文（GS-1985 全表／TU/e 章节）** ＋ **四源表体核对总表** ＋ **`\ell_2(11,4)` 在所有免费表中\textbf{均不存在}的结论** ＋ **BPW 1989 的 OA 状态（API 判 CLOSED）**
D1: 1（免费表体普查完结；产出"该格不在任何免费表内"的确定结论）
[RESEARCH]

# **全部免费表体核对完毕：`\ell_2(11,4)` 仍缺**

## §1 本轮新增入档（`sources/`）

```
$$\boxed{\text{GS-1985 全表}}\ \Longrightarrow\ \texttt{sources/Graham-Sloane-1985-covering-radius-on-codes.pdf}\ (65\ 页,\ UCSD/Fan-Chung 镜像)$$ ✓✓
$$\qquad \text{表体页码}:\ 49\text{–}58\ (\text{5 个 SECTION});\ \textbf{坐标法读出 }k=9\ \text{行}:$$
$$\qquad\qquad N{=}12{:}1,\ 13{:}2,\ 14{:}2,\ 15{:}2,\ 16{:}2\text{-}3,\ 17{:}3,\ 18{:}3\text{-}4,\ \boxed{19{:}3\text{-}4},\ \boxed{20{:}4a},\ 21{:}4\text{-}5,\ 22{:}4\text{-}5$$ ✓✓
$$\qquad \textbf{OCR 说明}:\ \text{“}4a\text{”}=\text{“}4\text{-}5\text{”的扫描残迹（同页他处见 “}3s\text{”“}4P4\text{-}5\text{”等同类残迹）}\ \Longrightarrow\ \textbf{与 CKMS-1985 及 1997 综述的 }4\text{-}5\ \textbf{一致}$$ ✓
$$\boxed{\text{TU/e 章节}}\ \Longrightarrow\ \texttt{sources/TUe-covering-codes-chapter-IR425174.pdf}\ (\text{DOI }10.6100/IR425174)$$ ✓
$$\qquad \text{内容}:\ \text{用对偶码约束证明"稀疏线性覆盖码不存在"，并\textbf{证明 BPW 的一个猜想};\ \text{给 }\ell(7,2){=}19,\ \boxed{\ell(9,2)\ge33,\ \ell(11,2)\ge65,\ \ell(13,2)\ge129}$$ ✓✓
$$\qquad \Longrightarrow\ \textbf{全部为 }R{=}2\ \text{的结果};\ \textbf{不含 }(11,4)$$ ✓✓
```

## §2 四源表体核对总表

```
$$\begin{array}{c|c|c}
\text{来源}&\text{表体}&\ (11,4)\ ?\\
\hline
P14\ (1990)&\ t[n,k]\ \text{与 }\ell\ \text{片段（}\ell(22,6),\ \ell(10,2)\text{）}&\text{无}\\
\text{Davydov 2001 Table 1}&\ \ell\ \text{上界改进（}R{=}4\ \text{仅 }r\ge19\text{）}&\text{无}\\
\text{TU/e 章节}&\ \ell(m,2)\ \text{下界族}&\text{无}\\
\text{GS-1985 全表}&\ t[n,k]\ (n\le64)\ \text{完整}&\text{无（该表为 }t\ \text{非 }\ell\text{）}\\
\end{array}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\text{所有免费可及表体均无 }\ell_2(11,4)}$$ ✓✓
```

## §3 `BPW 1989` 的 OA 状态（本轮实证）

```
$$\text{Semantic Scholar API}:\ \texttt{isOpenAccess: false},\ \texttt{openAccessPdf.status: CLOSED}$$ ✓✓
$$\text{Unpaywall API}:\ \texttt{is\_oa: false},\ \text{无 }best\_oa\_location$$ ✓✓
$$\text{DBLP 记录页}:\ \textbf{被 Anubis 反爬挑战拦截} \Longrightarrow \text{我方\textbf{无法自行核实}“unpaywalled version”标记}$$ ⚠️
$$\Longrightarrow\ \text{结论}:\ \text{该文\textbf{无免费全文}（两 API 独立判 CLOSED）};\ \text{若 DBLP 确有 OA 标记},\ \textbf{需人工在浏览器打开} \Longrightarrow \text{建议先生取}IEEE\ \text{版（pp.\ 108–109 的表）}$$ ✓✓
```

## §4 终态与唯一动作

```
$$\boxed{C07=G1^\star};\quad \text{唯一节点}=\ell_2(11,4)\ (\text{两侧皆未闭合},\ \text{已核 }1990/2001/2025/GS/}TU\text{e}\ \text{等})$$ ✓✓
$$\boxed{\text{唯一动作}}:\ \text{取 }\textbf{BPW 1989 pp.\ 99–109（表在末尾，}\approx\text{pp.\ 108–109）}\ \text{或《Covering Codes》Table 7.3}$$
$$\qquad \text{该表覆盖 }m\le12,r\le12 \Longrightarrow \textbf{必含 }(11,4) \Longrightarrow \textbf{一步定生死}$$ ✓✓✓
$$\text{若仍不可得} \Longrightarrow \text{按 }AMEND\text{-}19\ \text{开 }\boxed{P2\ \text{构造侧}}\ (\text{计数松弛大}:6196\ \text{vs}\ 2048)$$ ✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；不转 `Zone-B` ✓
【边界】 §1 表值为**坐标法实读**（“4a”含 OCR 歧义，已标）✓

## §附 【技术词回查】（补录）
```
技术词 table            命中文件数=101  :: ./C293-astra-liouville-source-verification-and-mangerel-grh-anchor.md ./p4-dilation-audit.md ./E20-E40-zero-density-2026-read.md 
技术词 open access      命中文件数=1    :: ./E29-A5-4-burnol-li-isomorphism-check.md 
```
