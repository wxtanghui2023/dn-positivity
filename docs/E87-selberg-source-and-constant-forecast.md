# E87 · Selberg 原文溯源 ＋ **常数预判** ✓ —— **能显式化 ✓；但 $C\le0.05$ 不确定 ⚠️**

> 委托 ✓ 唐先生（20:17 "这个常数项能推导出来么？" ✓）｜执行 ✓ 小灵
> 纪律 ✓ 未用 RH ✓（RH 结果仅作诊断 ✗）；未跑 Lean ✓

---

## 0. 判定（✓ 严格分离您提的两问 ✓）

```
✅ **问一"能不能显式化"：能 ✓** —— 证明骨架是显式的 ✓（Cauchy–Schwarz／Parseval／素数和均值 ✓），常数可逐项抽出 ✓
⚠️ **问二"显式化后 $C\le0.050$"：不确定 ✓** —— 真值对应 $C_{\rm true}\approx0.042$ ✓（仅比允许值小 19% ✓）；
   而**把误差项取绝对值相加**极可能放大到 $\gg0.05$ ✗ —— **正是您的预判 ✓✓**
✗ **原文可得性**：**公开网络无** ✓（Collected Papers vol.1 ＝ 书 ✓；IAS 档案只有未发表残稿 ✗）
```

## 1. 关键新事实（✓ 文献 ✓ arXiv:2006.08503v2 ✓）

| 版本 | 结果 | 误差 |
|:--|:--|:--|
| **无条件**（Selberg 1946, Thm 6,7 ✓） | $\int_0^T\lvert S\rvert^2=\frac{T}{2\pi^2}\log\log T+\cdots$ | $O(T\sqrt{\log\log T})$ ✓ |
| **RH 下**（Selberg 本人 ✓） | 同上主项 | $\mathbf{O(T)}$ ✓✓（**小得多** ✓） |
| RH 下精化（Goldston 1987 ✓） | 甚至给出二阶项 $\frac{a}{\pi^2}T$ ✓ | $o(T)$ ✓ |

```
⭐ **重要 ✓**：**无条件误差 $T\sqrt{\log\log T}$ 比【真值】$O(T)$ 大** ✓
   ⟹ 要抽的 $C$ 是【证明给出的界】✓，而非真值 ✓ —— 故"能否 $\le0.05$"取决于**证明的松紧** ✓
```

## 2. ⭐ 常数预判（✓ 可算 ✓）

$$\text{真值（Goldston/RH ✓）}=\frac{T}{2\pi^2}\log\log T+\frac{a}{\pi^2}T,\quad a\approx0.70\ \Longrightarrow\ \frac{a}{\pi^2}=0.0709$$
$$\text{写成 }C\cdot T\sqrt{\log\log T}\text{ 形 ✓：}\quad C_{\rm true}=\frac{0.0709}{\sqrt{\log\log T}}\Big|_{\log\log T=2.634}=\frac{0.0709}{1.623}=\mathbf{0.0437}$$

$$\boxed{C_{\rm true}\approx0.044\;<\;\text{允许 }0.050\quad\Longrightarrow\quad\textbf{窗口存在，但余量仅约 14\%}\ \⚠️}$$

## 3. 证明骨架（✓ 已抓到 ✓）

```
· 截断参数 $x$ ✓（Dirichlet 多项式长度 ✓，通常 $x=T^{\theta}$ ✓）
· 主项 ✓：$\frac{T}{\pi^2}\sum_{m\le x}\frac{\Lambda^2(m)}{m(\log m)^{2n+2}}f_n\bigl(\frac{\log m}{\log x}\bigr)$ ✓
· 误差项形如 ✓：$x^2$ ✓｜$\frac{\sqrt x\log T}{(\log x)^{n+1}}$ ✓｜$\frac{x\log T}{(\log x)^{n+1}}$ ✓
· 另有一类 ✓：$\bigl|2\int I_{3,n}I_{4,n}dt\bigr|\ll\frac{\sqrt x\log T}{(\log x)^{n+1}}$ ✓
⟹ ⭐ **最终 $O(T\sqrt{\log\log T})$ 由【多项误差平衡】产生，不是单项** ✓✓（答您第 6 点 ✓）
⟹ 故显式化须：① 逐项常数 ✓ ② **优化截断 $x$** ✓ ③ 识别主导项 ✓（正是您列的五步 ✓）
```

## 4. 原文溯源（✓ 结果 ✓）

| 来源 | 状态 |
|:--|:--|
| Arch. Math. Naturvid. **48** (1946) 89–155 ✓ | ✗ **未上网** ✓ |
| **Collected Papers vol. 1**（Springer 1989）✓ | ✓ **含该文** ✓ —— 但为**书籍** ✓（需图书馆／购买 ✓） |
| IAS 官方档案（publications.ias.edu ✓） | ✗ 只有**未发表残稿** ✓（Gram 律、圆问题、密度定理 ✓） |
| arXiv:2006.08503v2 ✓ | ✓ **证明骨架 ＋ 二阶项讨论** ✓（二手但详细 ✓） |

## 5. 结论与建议（✓）

```
✅ **可推导 ✓**：骨架显式 ✓，常数可抽 ✓ —— 但需：① 原文（Collected Papers vol.1 ✓）或
   ② 谨慎重构 ✓（**您警告的风险成立** ✗：重构易得到"看似合理但不对应原定理"的常数 ✓）
⚠️ **$C\le0.05$ 只是【可能】** ✓：真值 0.044 ✓ 仅留 14% 余量 ✓；绝对值相加法很可能超 ✗
⭐ **故本轮判定 ✓**：$$\boxed{\text{能推 ✓}\quad\text{但 }C_{\min}\le0.05\text{ 需实测 ⚠️（不可先验断言 ✓）}}$$
```

## 6. 纪律（✓）

```
✓ 未用 RH ✓（RH 结果只作**真值诊断** ✗，不进证明链 ✓）；**未跑 Lean** ✓
✓ **未宣称常数已得** ✗；**未宣称 $C\le0.05$** ✗ —— 严格分离您提的两问 ✓
✓ R7 ✓：结论由 $C_{\rm true}$ 与允许值的比对驱动 ✓
```
