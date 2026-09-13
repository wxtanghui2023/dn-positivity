# Karatsuba 1996 「On the function S(t)」 —— 页面图像（供逐字审计）

**来源** ✓
- A. A. Karatsuba, *On the function S(t)*, Izvestiya: Mathematics **60**:5 (1996), 901–931
  （俄文原版：Izv. RAN Ser. Mat. 60:5, 27–56）；DOI 10.1070/IM1996v060n05ABEH000086
- 英文 PDF（31 页，844,921 字节）：<https://www.mathnet.ru/eng/im86> → getFT 英文全文
- 本地抽取文本（PyMuPDF）：PDF 内有真实文本层，但**公式为 OCR 产物**，含符号误差

**本目录文件** ✓
| 文件 | 内容 | 印页 |
|:--|:--|:--|
| `KAR_page27.png` | **Theorem 4** ＋ Theorem 3 证明起点（(43) 式分离 $R_1,R_2,R_3,R_5,R_6,R_7$） | 927 |
| `KAR_page28.png` | $R_j$ 化为统一形式；引入 $R_4$；(44) 式 $\int_T^{T+H}\lvert\sum_{p<x^3}\frac{\sin(t\log p)}{\sqrt p}\rvert^{2k}dt=\sum_jK_j$ | 928 |
| `KAR_page30.png` | **§5 Proof of Theorems B, C, D**：(48) 显式余项 $R_1,R_2$ →(49) Selberg 渐近 →(50) $\int R_1=O(H)$ →(51) Hölder $O(H(\log\log T)^{k-0.5})$ | 930 |
| `thm4_statement_crop.png` | Theorem 4 陈述区的放大裁切（430 dpi） | 927 |

**E94／E95 审计要核对的两点** ✓
1. **Theorem 4 的对象**：求和号内 OCR 为 $\cos(t\log n)/(\sqrt n\,\log^{2}n)$ ✓ —— $\log^2n$ 是 $S_1$ 的签名 ⟹ **须确认是 $S$ 还是 $S_1$** ✗
2. **§5 (48)–(51) 对【余项】的确切速率** ✓ —— 决定 E93 的 LIVE／DEAD（阈值见 `scripts/E95_rate_thresholds.txt` ✓）

**版权** ⚠️：本目录为已发表论文的页面扫描，仅作本项目研究审计用（fair use），请勿再分发。
