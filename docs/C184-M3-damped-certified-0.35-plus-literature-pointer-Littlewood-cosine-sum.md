已查地图（**先查后写**）：`C-181`（阻尼引理 1/2）、`C-183`（甲：M=2 全区间 0.365）、`E4-ENGINE-1`（Montgomery Lemma 2.2 转引）、唐先生 2026-09-19 20:53 提供的 PDF（`docs/Montgomery-Ten-Lectures-CBMS84.pdf`）。关键词回查：`全阻尼三维`=0、`文献指针`=0、`余弦和问题`=0（**均本档新增**）。
**本档任务**：① 唐先生「看一下」→ 核实所给 PDF；② 继续推导 → **M=3 全阻尼证书** ✓
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{M=3 全阻尼定理（已证书）}：\forall(r_2,r_3)\in[0,1]^2,\ \forall(\varphi_1,\varphi_2,\varphi_3)\in[0,\pi]^3：$$
$$\qquad \boxed{\max_{1\le k\le15}\big[\cos(k\varphi_1)+r_2^k\cos(k\varphi_2)+r_3^k\cos(k\varphi_3)\big]\ \ge\ \mathbf{0.35}}✓✓\qquad（\mathbf{7\times}\ \text{Montgomery 的}\ \tfrac1{20}）✓$$
$$\textbf{(二)}\ ⚠️\ \textbf{所给 PDF}\ \textbf{不是} \text{CBMS 84 那本}：\text{实为}\ \textbf{Montgomery–Vaughan, \textit{Multiplicative Number Theory I: Classical Theory}}（\text{Cambridge CSAM 97, 2006}）✗$$
$$\qquad \text{全文搜}\ \texttt{5M}\ \text{仅命中丛书页／目录} \Longrightarrow \textbf{不含} \text{Palojärvi Lemma 2.2}（=\text{Ten Lectures Ch.5 Thm 11}）✗$$
$$\textbf{(三)}\ ⭐\ \textbf{但拿到两条有用指针}：\text{Littlewood (1937) 的}\ \textbf{"sum of cosines"}\ \text{问题 ＋ Turán 幂和方法}✓✓$$
$$\qquad （\text{p502 注记逐字}："\text{Littlewood (1937) was led to consider a question concerning a sum of cosines. Turán (1946) discovered that the theorem formulated by Littlewood is false …"}）✓$$
$$\qquad \text{出处}\ \text{逐字}：\text{Littlewood, \textit{An inequality for a sum of cosines}, J. London Math. Soc. \textbf{12} (1937), 217–221}✓✓$$

FREEZE-ACK: 本档即冻结期内的推导与文献核实（依 `§8.1`；不产候选结论）

D0: 本档对象 = **M=3 全阻尼证书（新定理）＋ 所给 PDF 的核实 ＋ Littlewood 余弦和文献指针** —— 关系 = 新定理与文献登记，非新机制
D1: 0

# C-184 · ⭐ M=3 全阻尼证书（0.35，7×）＋ 文献核实

---

## §1 M=3 全阻尼：定理与数据

$$\text{命题}：|z_1|=1,\ |z_2|=r_2\le1,\ |z_3|=r_3\le1 \Longrightarrow \max_{1\le k\le15}\ \Re\sum_{j=1}^3 z_j^k\ \ge\ 0.35✓$$
$$\text{方法}：\textbf{5 维（}r_2,r_3,\varphi_1,\varphi_2,\varphi_3\text{）自适应 B\&B}，箱下界【可分离 ＋ 四角最小】✓$$
$$\qquad \mathrm{LB}(B)=\max_{k\le15}\Big[\min_{I_1}\cos(k\varphi_1)+\min_{\text{corner}}(r_2^k\cos k\varphi_2)+\min_{\text{corner}}(r_3^k\cos k\varphi_3)\Big]✓$$
$$\begin{array}{c|r|r|r|r|r}
\text{靶值} & \text{箱数} & \text{未定} & \text{深度} & \text{最差余量} & \text{耗时}\\\hline
0.25 & 924\,160 & 0 & 20 & 1.16\times10^{-5} & 5.7\ \text{s}\\
\mathbf{0.35} & 1\,687\,984 & 0 & 30 & 3.41\times10^{-6} & \mathbf{10.7\ s}\\
0.38 & 33\,714\,000 & 11\,481\,808 & 49 & — & \text{预算耗尽}✗\\
\end{array}✓$$
$$\Longrightarrow \textbf{0.35 通过（定理）}✓；\textbf{0.38 未过}（\text{真值}0.4044，\text{余量仅}0.024⟹\text{本界收敛不足}）✗$$

## §2 数值真值（对照）

$$\min_{(r_2,r_3)}\min_\varphi\max_{k\le15}[\cdots]\ \approx\ \mathbf{0.4044}\ \text{at}\ (r_2,r_3)\approx(0.8,0.8)✓\qquad（8.1\times\ \tfrac1{20}）✓$$
$$\qquad \text{抽样}：(1,1)\to0.8142；\ (0.9,0.9)\to0.4496；\ (0.8,0.8)\to0.4044；\ (0.7,0.7)\to0.4629；\ (0,0)\to0.9239✓$$
$$\qquad \Longrightarrow \textbf{最坏仍在"中等阻尼"}\ \text{（与 M=2 的}\ r^\ast=0.70\ \text{同构）}✓$$

## §3 所给 PDF 核实（唐先生 20:53）

$$\text{文件}：\texttt{docs/Montgomery-Ten-Lectures-CBMS84.pdf}（571\ \text{页}，2.3\ \text{MB}）✓$$
$$\qquad \text{书名页实为}：\textbf{MULTIPLICATIVE NUMBER THEORY I: CLASSICAL THEORY}（\text{Cambridge CSAM 97}，\text{Montgomery \& Vaughan}，2006）✗$$
$$\qquad \Longrightarrow \textbf{不是} \text{Ten Lectures（CBMS 84, AMS 1994, xiii+220pp）✗；}\text{Ch.5 Thm 11 的原证明仍不可得}✗$$
$$\text{该书目录核对}：\text{无大筛法章、无幂和章；}\texttt{Turán}\ \text{出现在}\ p213（§6.4\ \text{注记}）／p502（§15.3\ \text{注记}）✓$$
$$\qquad \text{可用内容（若需）}：§11.2\ \text{Exceptional zeros；}§12.2\ \text{Weil 显式公式；}§14\ \text{Zeros；}§15\ \text{Oscillations}✓$$

## §4 ⭐ 文献指针（本档真正的副产品）

$$\text{p502 逐字}："\text{Littlewood (1937) was led to consider a question concerning a \textbf{sum of cosines}. Turán (1946) discovered that the theorem formulated by Littlewood is false — the argument provided establishes a weaker result than claimed. Turán undertook a detailed study of such power sums."✓$$
$$\qquad \text{出处}：\text{Littlewood, \textit{An inequality for a sum of cosines}, J. London Math. Soc. \textbf{12} (1937), 217–221}✓$$
$$\qquad \text{关联}：\text{Knapowski (1961) 用 Turán 幂和方法给出}\ c\ \text{的有效上界；Turán (1984) 专著}✓$$
$$\Longrightarrow ⭐\ \text{我方}\ (RP_M)\ \text{正是"余弦和"型极值问题} \Longrightarrow \textbf{这条谱系（Littlewood 1937 → Turán 幂和法）应纳入论文的文献位置}✓✓$$

## §5 边界

- ⚠️ 证书依赖 `SLACK=1e-12` / `TEST_EPS=1e-9`（同族假设）；区间算术版未做 ✓
- ⚠️ `0.35` 是**下界**（真值 ≈0.4044）✓；`0.38` **未证**（预算）✗
- ⚠️ 覆盖 `r_2,r_3 ∈ [0,1]²` 与 `φ ∈ [0,π]³`（后者由偶性＋周期性等价全空间）✓
- ⚠️ **未声称** `M ≥ 4` 的阻尼版 ✓
- ⚠️ §3 的核实**只基于该 PDF 自身**（书名页／目录／全文关键词）✓ —— 未做外部比对 ✓
- **未用** RH；PDF 已复制入 `docs/`（2.3 MB，本档一并提交）✓
- **纪律**：**先读后判** ✓（读目录与命中页后才下"不含该引理"的判断）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`）

```
技术词 全阻尼三维   命中文件数=0 ::  ⟹ 本档新增
技术词 文献指针    命中文件数=0 ::  ⟹ 本档新增
技术词 余弦和问题   命中文件数=0 ::  ⟹ 本档新增
```
