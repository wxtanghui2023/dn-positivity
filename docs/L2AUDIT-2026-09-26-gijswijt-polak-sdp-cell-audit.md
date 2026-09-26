已查地图：已跑 scripts/prework_map_check.sh K(10,1) SDP Gijswijt Polak 2504.01932 ⟹ 本档为 **L-2 文献 cell 级审计**（唐先生 2026-09-26 21:12 指定 ✓）；**含外部文献直读**（arXiv v2 HTML ✓）。
D0: 本档对象 = 2025–2026 covering-code SDP 新方法与 $K_2(10,1)$ 的具体格值（检索对象）
D1: 0（产出为一处格值钉死与一条 L-2 结论）

# L2AUDIT-2026-09-26 · 2504.01932 对 $K_2(10,1)$ 的 cell 级审计

## §0 结论（先给）

```
$$\boxed{\textbf{(R-1 钉死)}\ \text{arXiv:2504.01932v2 Table 5（}q=2,\ R\le6\text{）中 } n=10,\ R=1\ \text{格} = \mathbf{105.2223}\ \text{——\textbf{无粗体、无星号}}\ ✓✓}$$
$$\qquad\Longrightarrow\ K_2(10,1)\ \ge\ 106\ <\ \underbrace{107}_{\text{已知最好下界}}\ \ll\ 119\ \Longrightarrow\ \boxed{\textbf{新 SDP 未触及 119，亦未超过旧下界}}\ ✓✓$$
$$\boxed{\textbf{(R-2 L-2 结论)}\ \text{2025–2026 确有\textbf{方法升级}（SDP/Lasserre/Terwilliger 三点型），但\textbf{未形成 } K(10,1)\ \text{新界};\ \text{该方法\textbf{暂不能替代独立结构输入}}}}\ ✓$$
$$
$$
```

---

## §1 文献身份（逐字核对 ✓）

```
$$\text{题}:\ \text{Gijswijt \& Polak, "Semidefinite lower bounds for covering codes"}\ ✓$$
$$\text{arXiv:2504.01932v1（2025-04-02）→ v2（2026-06-19 修订，"added info on computation sizes (Table 4)"）}\ ✓$$
$$\text{期刊: IEEE Trans. Inform. Theory \textbf{72}(9),\ 6599–6614\ (2026)}\ ✓$$
$$\textbf{对象一致}:\ \text{论文明确定义 }K_q(n,r)=\text{一般（非线性）}q\text{ 元覆盖码最小规模}\ ✓\ \text{（与 119 线同对象 ✓，非仅线性码 ✓）}$$
$$\textbf{方法链}:\ \text{Gijswijt 2005 (matrix cuts / SDP)}\to\text{Lasserre 0-1 启发约束}\to\text{对称性约化＋更强目标}\to\text{Van Wee ＋球覆盖不等式}\ ✓$$
$$\qquad\text{参考文献含}\ [19]\ \text{Schrijver (Terwilliger)}\ ✓,\ [23][24]\ \text{Zhang 对覆盖不等式（pair/triple）}\ ✓,\ [22]\ \text{Wu–Chen 2024}\ ✓,\ [10]\ \text{Kéri 表}\ ✓$$
$$
$$
```

---

## §2 (R-1) Table 5 的 $n=10$ 行（逐字 ✓）

```
$$\text{表头}:\ \ |n|\ R{=}1\ |\ R{=}2\ |\ R{=}3\ |\ R{=}4\ |\ R{=}5\ |\ R{=}6\ |\ ✓$$
$$n=10\ \text{行}:\ \ |10|\ \mathbf{105.2223}\ |\ 22.4103\ |\ \mathrm X\ |\ \mathrm X\ |\ \mathrm X\ |\ \mathrm X\ |\ ✓✓$$
$$\text{论文自述}:\ \text{"Improvements over the values in Kéri's tables ... are in boldface and marked with an asterisk (}*\text{)"}\ ✓$$
$$\qquad\Longrightarrow\ n=10,\ R=1\ \text{格\textbf{无星号}} \Longrightarrow\ \textbf{论文自己也不主张在该格改进}\ ✓✓$$
$$\textbf{量级核对（内部一致 ✓）}:\ \text{球覆盖} = 2^{10}/11 = 93.09\ <\ 105.22\ (\text{本文 SDP})\ <\ 107\ (\text{已知最好下界})\ ✓$$
$$\qquad\text{旁证}:\ n=8,\ R=1\ \text{格}=31.9999\ \Longrightarrow\ K_2(8,1)\ge32\ \text{且已知}=32\ ⟹\ \text{界\textbf{紧}}\ ✓\ \text{（说明该 SDP 确实有效，非空转 ✓）}$$
$$
$$
```

---

## §3 (R-2) L-2 结论与旧基线核对（唐先生点 4 ✓）

```
$$\textbf{基线阶梯（本线档案 ＋ 本档核对 ✓）}:\quad 93.09\ (\text{球覆盖})\ <\ 103\ (\text{van Wee 1988/1991 球界})\ <\ \mathbf{107}\ (\text{Bertolo–Östergård–Weakley 2004 混合码})\ <\ \cdots\ \le\ 120\ (\text{已知最好上界})\ ✓$$
$$\textbf{注意}:\ \text{103 与 107 属\textbf{不同年代/不同方法}的下界} \Longrightarrow\ \textbf{不可混用}\ ✓\ \text{（唐先生点 4 ✓）；最好下界取 107}\ ✓$$
$$\qquad\text{上界 120 的归属（Östergård 构造 vs Wille）仍待 Kéri 图例钉死}\ ⚠️\ \text{（本档未闭合 ⟹ 标注）}$$
$$\textbf{旁证（论文脚注 ✓）}:\ K_2(18,1)\ge14665,\ K_2(30,1)\ge35874398\ \text{之改进\textbf{已被 Wu–Chen 2024 超过}}\ (14666;\ 35876816)\ ✓\ \text{（与本线档案一致 ✓）}$$
$$\textbf{最终记录（唐先生指定措辞 ✓）}:\ \boxed{\text{2025–2026 有方法升级，但没有形成 }K(10,1)\text{ 的新界；该方法暂不能替代独立结构输入}}\ ✓✓$$
$$
$$
```

---

## §4 边界（诚实标注）

- §2 的格值为**逐字直读 arXiv v2 HTML**（`Table 5` 的 `n=10` 行 ✓）；星号判定依论文自述规则 ✓
- §2 的"⟹ K_2(10,1) ≥ 106"为**整数取顶** ✓（SDP 给实数下界 105.2223 ✓）
- §3 的 103／107 归属依据本线既有档案 ＋ 本档文献 ✅；**120 的归属未闭合** ⚠️（已标）
- **未**主张"该 SDP 方法无价值" ✗ —— 只主张"在 (2,10,1) 格未形成新界" ✓（范围严格限定 ✓）
- **未跑**任何求解器 ✓（纯文献直读 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 SDP 格值钉死 命中文件数=1    :: ./L2AUDIT-2026-09-26-gijswijt-polak-sdp-cell-audit.md 
技术词 L-2 结论措辞 命中文件数=1    :: ./L2AUDIT-2026-09-26-gijswijt-polak-sdp-cell-audit.md
```
- **本档新增**：SDP 格值钉死、L-2 结论措辞（见上方命中数）
- **档案已有（引用，不列为提出）**：球覆盖/Van Wee/BÖW 阶梯、Wu–Chen 2024
