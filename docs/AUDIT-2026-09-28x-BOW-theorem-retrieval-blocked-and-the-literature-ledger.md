# AUDIT-2026-09-28x — **BÖW 一般定理取法受阻（工具额度全灭）＋ 文献账定格**

> **已查地图**：★**命中既有档** —— `AUDIT-v`（H–P 2000 ＋ $106$ 已排除）／`AUDIT-w`（$103$ 系 1991 年值）／`AUDIT-q`（van Wee 原式）／`AUDIT-r`（Kamenetsky $120$ 词）✓

**性质**：**审计/受阻记录**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:58 ✓
> **唐先生令**：**聚焦 BÖW 2004 之 general $R{=}1$ theorem 本身**，不泛搜 ✓

D0: 本档对象 ＝ **档案已有**（文献账／取法——无新数学对象 ✓）
D1: 0（产出＝**受阻记录 ＋ 文献账定格 ＋ 可执行取法** ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{① 本轮\ \textbf{未能取到 BÖW 一般定理};\ \text{② 工具受阻:\ Tavily 432、Firecrawl 402\ （额度耗尽）;\ \text{③ Kéri PDF 下载成功但抽文失败}}}$$
$$\boxed{\text{④ 文献账\ \textbf{定格}（见 §2）};\ \text{⑤ 可执行取法\ \textbf{四条}（见 §3）}}$$

## §1 受阻详情（**诚实 ✓**）

| 工具 | 结果 |
|---|---|
| `tavily_search` / `tavily_extract` | **HTTP 432**（plan 额度耗尽） |
| `firecrawl_search` / `firecrawl_scrape` | **HTTP 402**（Insifficient credits） |
| `web_search` | 走 Firecrawl ⟹ **402** |
| `web_fetch`（Kéri PDF） | **200**，但返回**原始 PDF 二进制**（压缩流） |
| `pdftotext` | **未安装** ✗ |
| 朴素 `zlib` 抽流 | **抽出 0 字节**（子集字体内码，非简单 `(...)Tj`）✗ |

$$\therefore\ \boxed{\text{本轮无法取到 BÖW 2004 之一般定理式}}\ ✗\ \text{（**非**"不存在"——**工具额度所致**} ⚠️）$$

## §2 文献账（**本会话定格 ✓**）

$$\boxed{107\ \le\ K_2(10,1)\ \le\ 120}\qquad\text{（当前；两独立权威一致）}$$

| 年 | 下界 | 源 |
|---|---|---|
| $1988$ | $2^n/n\Rightarrow102.4\to103$ | van Wee, IEEE TIT 34, 237--245（**原式已取且代入已核 ✓**） |
| $1991$ | $\mathbf{103}$ | van Wee **博士论文**（TU/e，1991-06-04 答辩；本会话已定分 ✓） |
| $1997$ | $105$ | CLLM 综述 Table A（标 "j"） |
| $2004$ | $\mathbf{107}$ | **BÖW 2004**（OEIS `%H` 逐字 `[a(10)>=107]`；Kéri 表 2026-08 一致） |
| 上界 | $\mathbf{120}$ | Östergård 1991（mixed）→ Kamenetsky 显式 $120$ 词（2020-07-27，**已取并核 ✓**） |

$$\text{演进（唐先生所引 Kéri 档）}:\ 94\to96\to97\to103\to105\to107$$

**旁证账（本会话已核）**：
- H--P 2000 ＝ **linear inequality of a code** 族（摘要逐字 ✓）
- Habsieger/Honkala 直接 congruence 界在 $n{=}10$ **仅 94** ✓（唐先生算，本档复算一致）
- Blass--Litsyn 1998 主攻 $A'(9,1)>57$、$K(II,1)>180$（**非** $K_2(10,1){=}107$ 此项）✓
- Haas 2000（DM 219, 97--106）与 Haas 2002（DM 256, 161--178）**两篇须区分** ✓

## §3 ★ 可执行取法（**四条，按优先级 ✓**）

$$\text{① }\textbf{装 PDF 抽文器}（\texttt{pip install pypdf}\ \text{或 }apt\ pdftotext）\Longrightarrow \text{重抽已下载之 } \texttt{/tmp/keri.pdf}\ (798{,}720\ \text{B})\ \text{之表} ⚠️$$
$$\text{② }\textbf{作者主页}:\ Östergård（Aalto, \texttt{users.aalto.fi/\textasciitilde pat/}）\ \text{常自挂 PDF};\ \text{Weakley（IPFW）同} \Longrightarrow \text{最可能之免费源} ✓✓$$
$$\text{③ }\textbf{书}:\ \text{Cohen--Honkala--Litsyn--Lobstein,}\ \textit{Covering Codes}\ (1997)\ \text{相关章（excess/线性不等式）}\ \text{含 general }R{=}1\ \text{界之标准形式} ✓$$
$$\text{④ }\textbf{引文反查}:\ \text{Haas 2002（DM 256）、Plagne 2009（DM 309）—— 二者多半逐字引 BÖW 之定理}} ⚠️$$

## §4 边界（硬 ✓）

- 受阻**如实记录** ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- **不主张** BÖW 定理不存在 ✗（V290）；**不编造**其公式 ✗（遵前令 ✓）
- $\S2$ 之 $107$ 依赖 OEIS ＋ Kéri 表（**两独立权威**）✓；**BÖW 正文未核** ⚠️
