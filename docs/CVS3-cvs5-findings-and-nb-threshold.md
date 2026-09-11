# **C–vS §5 读毕**（自由对角元 + 三条正性条件）+ **发现 P50/P51 就是 NB 阈值线**

**依据**：唐先生 2026-09-11 20:46（"1，2"）
**原文**：C–vS（arXiv:2511.23257 / CMP 406(312) 2026）§4.2、§5、目录 ✓
**标注**：【外部·原文】｜【⭐发现】｜【核验】

---

## §1 【原文】**C–vS 的结构（目录级，极有价值）**
```
1 Introduction：**以 Carathéodory–Fejér 定理（1911）为**【起点】—— 它刻画 **Hermitian PSD Toeplitz 矩阵** ✓✓
2 **Toeplitz case**｜3 The Continuous Kernel Case｜4 Quadratic Form Q Associated to a Distribution
   （4.1 Matrix of the quadratic form｜**4.2 The diagonal values**｜4.3 Relation to the spectral action）
5 **Finite Dimensional Even Case**（5.1 General finite dimensional operator D）
6 **Infinite Dimensional Case**｜7 **Spectral Action and Divided Differences**
**Appendix A. An instance of TRUNCATION MATRICES** ✓✓｜Appendix B. Explicit checks for N = 1, 2 ✓
⟹ ⭐ 一切建立在 **Carathéodory–Fejér**（= Schur/单位圆结构 ✓）之上 ⟹ **"实零点 ↔ 单位圆"的经典机制** ✓✓
   （与我们 CVS1c 的核验完全一致 ✓）
```

## §2 【原文】**§5 的三条正性条件（全在少数参数上）**
```
"§5: We are given a **real symmetric positive matrix Q = (q_ij), i,j ∈ {−N,…,N} of the form (11)**" ✓
   其中 (11) 即：**q_ij = (b_i − b_j)/(λ_i − λ_j)（i≠j）+ 对角元 a_i**（**自由** ✓）
【三条"正性条件"（CMP 页 33–34 ✓）】参数 (a, y, β)：
 (1) **−a₃ ≥ 0** 且 (1/8)(4a sinβ + cosβ(3sin²β − 2a))(4sin³β − 4y sinβ + cosβ(8y − 11sin²β)) ≥ 0
 (2) **a₂ ≥ 0** 且 −(13/4)a sin2β − (2a+1/2)cos2β − 4ay + 5a + (3/4)sin2β − (3/8)sin4β
                + (33/64)cos4β − (3/4)y sin2β − y − 1/64 ≥ 0
 (3) **−a₁ ≥ 0** 且 5a + 2sin²β + cos²β + (3/2)sinβcosβ − y ≥ 0
⟹ ⭐ **有限情形的正性 = 少数参数（a₁,a₂,a₃,y,β）上的有限条不等式** ✓✓
   —— 这正是"**有限维正性 ⟺ 有限多个条件**（Sylvester 型）"结构 ✓，与本项目 A′/material-A 的
      "**有限可判定性**"主题一致 ✓✓
   —— 也确认 §0 的 ERR：**对角元 a_i 是【自由参数】**（其值由这些不等式约束 ✓），
      故"取 a_i = f″(λ_i) 就自动正定"是错的 ✗
```

## §3 ⭐⭐ **发现：P50/P51 脚本就是【Nyman–Beurling 阈值线】**（对门⑤的直接对账）
```
`escape_range_scan.py` 头部注释（原文 ✓）：
   "逃逸零点 (σ₀=½+δ, γ₀) 的 **d_N² 签名 ~ N^{2δ}·A(γ₀)/log²N，A ~ 1/γ₀²**"
   "检测需要 N^{2δ}/γ₀² ≳ 在线基线 C/log N → **N* ~ (γ₀²·C/log N*)^{1/(2δ)}**"
   "**C_burnol = 2 + 0.5772 − log(4π) ≈ 0.0462（Burnol 常数）**" ✓✓✓
⟹ 即：**本项目 P50/P51 线计算的是"离轴零点 (δ,γ₀) 在 NB 距离 d_N 中的检测阈值 N*(δ,γ₀)"** ✓✓
   —— **这正是门⑤的"转换形状"的直接测量** ✓✓✓
   —— 且它**用的是 Burnol 常数** ✓（与 Burnol 下界 D² ≳ C/log N 同源 ✓）
⟹ **预测检验**：若 N*(δ,γ₀) ~ (γ₀²)^{1/(2δ)}·…，则当 δ 固定时 N* **随 γ₀ 按多项式增长**
   ⟹ 与"log 型（弱）"或"T²（强）"哪一种相符？⟹ **跑脚本即得** ✓
【其他脚本】`p51_t3_*.py`：用 `zeros_odlyzko_100k.npy` 做 **ψ 的零点贡献差**（在线 vs 逃逸配置 ✓）
   —— 是"显式公式差分"路线 ✓（非 Toeplitz 路线 ✗⟹ 秩亏检查需另设对象 ✓）
```

## §4 边界
```
【外部·原文】§1 目录 ✓、§2 三条条件与 §5 开头 ✓、§3 脚本注释（**我方文件** ✓）
【ERR 确认】§2 末：对角元自由 ⟹ 上一轮的设定错误确认 ✓
【未做】未跑 `escape_range_scan.py`（本轮并发执行 ✓）；未读 C–vS §5 正文细节 ✗、Appendix A ✗
【未做】未输入 1/2；未构造模型；未改 L2；未声称任何证明
```
## §5 提交链
```
CVS2（a067f4c Loewner + ERR）→ 本篇（C–vS §5 条件 + 发现 P50/P51 = NB 阈值线）
```
