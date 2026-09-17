# T1-1 · **原文取证登记**（Kloosterman 分数指数路线）

> 依 `docs/TACTICAL-PLAN.md` T1-1｜**执行日**：2026-09-17 ✓｜**纪律**：只取证＋登记，不做数学判断 ✓

---

## 1. ⭐ 四篇的**精确身份**（用 BC 自己的参考文献逐字确认）

| 代号 | 完整引用 | DOI / arXiv | 取得状态 |
|:--|:--|:--|:--|
| **DFI97** | Duke, W.; Friedlander, J.B.; Iwaniec, H. **Bilinear forms with Kloosterman fractions**. Invent. Math. **128** (1997), no. 1, 23–43 | DOI **10.1007/s002220050135** | ✗ **闭源**（OpenAlex `is_oa: False`） |
| **BC18** | Bettin, S.; Chandee, V. **Trilinear forms with Kloosterman fractions**. Adv. Math. **328** (2018), 1234–1262 | **arXiv:1502.00769** | ✓ **全文**（PDF＋ar5iv HTML＋纯文本） |
| **BCR** | Bettin, S.; Chandee, V.; Radziwiłł, M. **The mean square of the product of the Riemann zeta function with Dirichlet polynomials** | **arXiv:1411.7764** | ✓ **全文**（PDF 346 KB＋ar5iv HTML 863 KB） |
| **DI83** | Deshouillers, J.-M.; Iwaniec, H. **Kloosterman sums and Fourier coefficients of cusp forms**. Invent. Math. **70** (1982/83), no. 2, 219–288 | DOI **10.1007/BF01390728** | ✗ **闭源**（OpenAlex `is_oa: False`） |

$$\textbf{注}：\text{BC 的参考文献中另有}\ \text{[DFI95]}\ \text{Representations by the determinant and mean values of}\ L\text{-functions（Cardiff 1995 会议录，1997 年出版，109--115）}✓$$
$$\qquad\Longrightarrow\ \text{与 DFI97 同族，}\ \text{若需可一并取}✓$$

---

## 2. ⭐ **已取得的原文**（存于 `refs/`，`.gitignore` 已排除 `*.pdf`）

| 文件 | 大小 | 来源 |
|:--|:--|:--|
| `refs/BC2018-kloosterman_fractions.pdf` | 476 KB | （唐先生昨日上传）✓ |
| `refs/bcr.pdf` | 346 KB | arXiv:1411.7764 ✓ |
| `refs/tril_2604.25177.pdf` | 319 KB | arXiv:2604.25177v2 ✓ |
| `refs/tril_2608.27732.pdf` | 317 KB | arXiv:2608.27732v1 ✓ |
| `docs/ref-bc-ar5iv-plaintext.txt` | 112 KB | BC 全文纯文本（本地 grep 用）✓ |
| `/tmp/BC_sec4_1_3_verbatim.txt` | 30 KB | BC §4.1.3 区段 ✓ |

---

## 3. ⭐ **2026 最新增量**（同一问题的最近进展）

| 论文 | arXiv | 状态 |
|:--|:--|:--|
| **Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions** | **2604.25177v2** | ✓ 已取 |
| **Trilinear Kloosterman fractions II: subdyadic intervals and nearly balanced convolutions** | **2608.27732v1** | ✓ 已取 |
| Bilinear forms with Kloosterman fractions and applications（Zeindler） | **2601.00292** | ✗ **已撤回** —— 核实逐字："**This paper has been withdrawn by Dirk Zeindler**"（v2, 2026-01-05）✓ |

$$\textbf{注意}：\text{I/II 的改进均为}\ \textbf{range-local}（\text{"in the case where}\dots\text{"}），\ \text{不能直接给出统一}\ (r,t)\ \text{点}✓\quad(\text{昨日 V2 系列已判：猎-6 判定 C})✓$$

---

## 4. ⚠️ **两篇闭源的替代路径**（合法）

$$\textbf{DFI97 的结构}：\text{BC §2 有}\ \textbf{完整 outline} \text{——逐字："Our proof has roughly the same structure of Duke, Friedlander and Iwaniec's proof of (1.1) and follows their clever application of the amplification method. However we introduce several refinements\dots among which is particularly important the fact that we keep a}\ \textbf{longer diagonal}\dots\text{"}✓✓$$
$$\qquad\Longrightarrow\ \text{DFI 的结果 (1.1) 在 BC 中}\ \textbf{逐字引用}：\mathcal B_a(M,N)\ll\|\alpha\|\|\beta\|(a+MN)^{3/8}(M+N)^{11/48+\varepsilon}✓$$
$$\textbf{DI83 的输入}：\text{被 BC／BCR 引用；其结果在后续文献中有}\ \textbf{精确陈述}；\ \text{替代：Iwaniec--Kowalski《Analytic Number Theory》Ch.16（Kuznetsov 公式＋大筛）等}✓✓$$
$$\qquad\textbf{合法获取途径}：\text{机构图书馆／馆际互借（ILL）／作者本人索取}✓\quad(\textbf{不用} \text{非授权镜像})✓$$

---

## 5. ⭐ 已从 BC 取到的**关键技术事实**（供 T1-2 起手）

$$\text{(1)}\ \textbf{C--S 作用集／保留集}：\text{BC 施于}\ \{n_1,n_2,a_2\}\ \text{而不施于}\ \{d,a_1,\ell_1,\ell_2\}；\ \text{DFI 则除}\ \{\ell_1,\ell_2\}\ \text{外全施}✓✓$$
$$\qquad\Longrightarrow\ \text{BC 相对 DFI 的}\ \textbf{增量}＝\text{额外保留}\ \{d,a_1\}✓$$
$$\text{(2)}\ \text{结果三式}：(1.1)\ \text{DFI}；\ (1.2)\ \text{BC Theorem 1（两项）}；\ \text{BCR Theorem 2 模板 (1.3)}✓$$
$$\text{(3)}\ \text{BC §2 outline：amplification ＋ longer diagonal ＋ }\delta\text{-symbol／互补除子}✓$$
$$\text{(4)}\ \text{BCR §3.4：}\ (1.3)\ \text{逐配置调用；}\ A=N_1N_2/d^2\cdot T^{1-\varepsilon}✓$$
$$\text{(5)}\ \text{互反恒等式 (4.17)（BC 自用）；}\ \Delta\ \text{定义与}\ \Delta=0/\ne0\ \text{分拆}✓$$

---

## 6. 状态与下一步

$$\boxed{\begin{array}{c|l}
\text{项}&\text{状态}\\ \hline
\text{BC18 全文} & ✓\ \text{已取}\\
\text{BCR 全文} & ✓\ \text{已取}\\
\text{2026 I/II} & ✓\ \text{已取（range-local）}\\
\text{2601.00292} & ✗\ \text{已撤回}\\
\text{DFI97} & ✗\ \text{闭源（结构经 BC §2 可得）}\\
\text{DI83} & ✗\ \text{闭源（结果可经二次文献精确获得）}\\
\end{array}}✓$$

$$\textbf{下一步 T1-2}：\ \text{抽出}\ \text{BCR Theorem 2 模板 (1.3) 的}\ (r,t)\ \text{如何被谱输入束缚}✓$$
$$\qquad\text{起手材料}：\ \texttt{refs/bcr.pdf}＋\texttt{refs/BC2018-*.pdf}\ \text{（§4 的}\ (4.26)\text{--}(4.33)\ \text{链已逐字在手）}✓$$
