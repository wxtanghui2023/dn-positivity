已查地图：已跑 scripts/prework_map_check.sh K(10,1) Gram-lift 287 二阶矩 ⟹ 执行自 `docs/GRAM-LIFT-2026-09-25-...md` ＋ `memory/2026-09-25.md`（23:32–23:50 段）＋ `docs/SECOND-ORDER-2026-09-25-...md`；本档为**单一任务：逐行追 287 的出处**（唐先生 2026-09-26 19:36 指令 ✓）；**未跑程序** ✓，零新假设 ✓。
D0: 本档对象 = `G_00 ≤ 287` 的来源追溯（287 是已证下界还是未审计上界？）
D1: 0（本档为溯源/审计，不新增自由度；产出为出处定位与缺口判定）

# TRACE-287-2026-09-26 · `G_00 ≤ 287` 逐行追溯

## §0 结论（一句话）

$$\boxed{287\ \text{是\textbf{已严格证明的下界}}\ ✓;\ \ \text{其\textbf{匹配的上界无任何来源}\ ✗}\ ——\ \text{它是\textbf{缺口本身}，不是未审计跳步}\ ✓}$$

---

## §1 追到的原始出处（逐字引）

`memory/2026-09-25.md` 第 85 行（23:32–23:45「二阶计数链」段）：

> **加强①（我加）**：由已验证恒等式 `Σδ²+Σδ=4(A₁+A₂)` ⟹ **`Σδ² ≡ 3 (mod 4)`**（强于"Q 奇"）⟹ `Σδ²≥287`，Q=1 的 profile **唯一锁定**：283×{δ=1}+1×{δ=2}+740×{δ=0} ✓

同段：

> **明确 crux**：需要 **`A₁+A₂` 的上界**（⟺ Q 上界）✓ —— 若证 ≤143 且 Q≥3 即与 ≥144 矛盾

`docs/GRAM-LIFT-2026-09-25-...md` §11：

> `G_00 = 4(D_1+D_2) - 285 ≥ Σδ_0 = 285 ⟹ D_1+D_2 ≥ 143` ✓（机制=整数凸性 `δ²≥δ`）

⟹ **287 与 143 同源** ✓：一个是另一个的等价写法 ✓。

---

## §2 核心恒等式（本档独立重推，结论 ✓✓）

```
$$\textbf{记号}: C\subseteq\mathbb F_2^{10},\ |C|=M,\ b(x):=|C\cap B_1(x)|,\ \delta(x):=b(x)-1\ge0$$
$$\qquad A_r:=\#\{\{c,c'\}\subset C:\ d(c,c')=r\},\quad E:=11M-2^{10}=11M-1024\ (M=119\Rightarrow E=\mathbf{285})$$
$$\textbf{(I) 球交基数}: |B_1(c)\cap B_1(c')|=\begin{cases}11,&c=c'\\ 2,&d(c,c')=1\\ 2,&d(c,c')=2\\ 0,&d(c,c')\ge3\end{cases}$$
$$\textbf{(II) 二阶矩}: \sum_x b(x)^2=\sum_{c,c'}|B_1(c)\cap B_1(c')|=11M+4(A_1+A_2)$$
$$\textbf{(III) 恒等式}\ \boxed{\sum_x\delta(x)^2\ =\ 4(A_1+A_2)-E}\qquad(\text{由 (II) 减 }2\sum b+1024,\ \sum b=11M)$$
$$\textbf{(IV) 行和}: \sum_j G_{0j}=\sum_x\delta_0(x)\sum_j\delta_j(x)=E\sum_x\delta_0=E^2=81225$$
$$
$$
```

**核验（120-码，M=120 ⟹ E=296）**：`Σδ² = 4(50+149) − 296 = 500` ✓ 与 profile 直算 `Σδ²=500` **一致** ✓✓（archive 同）✓

---

## §3 287 的**严格来源**（两条独立路径，均已证 ✓）

```
$$\textbf{路径 A（整数凸性）}:\ \delta(x)\in\mathbb Z_{\ge0}\Longrightarrow\delta^2\ge\delta\Longrightarrow\sum\delta^2\ \ge\ \sum\delta=E=285$$
$$\qquad\Longrightarrow 4(A_1+A_2)-285\ \ge\ 285\ \Longrightarrow\ \boxed{A_1+A_2\ \ge\ 142.5\ \Longrightarrow\ \ge\mathbf{143}}\ ✓$$
$$\textbf{路径 B（同余，更强）}:\ E=285\equiv 1\!\!\pmod 4\Longrightarrow\sum\delta^2=4(A_1+A_2)-285\equiv -285\equiv \mathbf 3\!\!\pmod 4$$
$$\qquad\text{而}\ \sum\delta^2\ge 285\ \text{且}\ \equiv3\!\!\pmod 4\ \Longrightarrow\ \text{最小可行值} = \mathbf{287}\ \Longrightarrow\ \boxed{\sum\delta^2\ \ge\ \mathbf{287}}\ ✓✓$$
$$\qquad\Longrightarrow\ 4(A_1+A_2)\ \ge\ 572\ \Longrightarrow\ \boxed{A_1+A_2\ \ge\ 143}\ ✓\ (\text{同值，路径 B 更强})$$
$$
$$
```

⟹ **287 是 `Σδ²` 的下界** ✓；把它写成 `G_00 = Σδ² = 4(D₁+D₂) − E`（因 `D_r ≡ A_r` ✓）即得 **`D₁+D₂ ≥ 143`** ✓。

---

## §4 ⚠️ **匹配的上界（`G_00 ≤ 287`）在档案中无任何来源** ✗

```
$$\textbf{逐处搜索（本档实跑）}:\ \texttt{grep -rn "287" docs/*.md work/k10/**/*.py}\ \text{与 memory}:\ \text{命中仅上述下界用法}\ ✗\ (\text{无上界出处})$$
$$\texttt{grep -rn "1881"}:\ \text{命中仅}\ \texttt{C189/C190}\ \text{的不相关数值}\ 0.3730721881\ ✗\ (\text{与本题无关})$$
$$
\textbf{唯一相关的档案原话（诚实结论，逐字）}:
```
> **诚实结论**：census 全域可行 ⟹ **Q=1 未被排除** ✗；且"只需排除 Q=1 即证 119 不可能"**不成立** ✗
> （Q≥3 仅给 `A₁+A₂≥144`，仍需**独立上界 ≤143** ✓）
> —— `memory/2026-09-25.md`（23:36–23:50 段）

⟹ **判定**：`G_00 ≤ 287`（⟺ `A₁+A₂ ≤ 143` ⟺ `Q ≤ 1`）**既不是已证命题、也不是隐含假设、也不是链条跳步**；
它是 `119` 主线的**开放 crux 本身** ✓✓。

---

## §5 ⚠️ 额外的结构警告（档案已记，须一并保留）

```
$$\textbf{警告①}:\ \text{即使证到}\ Q\le1\ (\Longleftrightarrow A_1+A_2\le143),\ \text{也\textbf{不立即}矛盾}\ ✗\ ——\ \text{它只把解空间逼到}$$
$$\qquad\boxed{A_1+A_2=143\ \wedge\ Q=1}\ \text{（即}\ \sum\delta^2=287\ \text{恰饱和，profile 唯一}:\ 283\times\{\delta{=}1\}+1\times\{\delta{=}2\}+740\times\{\delta{=}0\}\ ✓)$$
$$\qquad\Longrightarrow\ \text{还须在该分支内再给出\textbf{第二处矛盾}}\ ✓\ (\text{即档案所说 "profile}\leftrightarrow\text{indicator 耦合"}\ ✓)$$
$$\textbf{警告②}:\ \text{层 }i\ge1\ \textbf{不进入 pair 层}\ \Longrightarrow\ \text{pair 链\textbf{无法自闭合}}\ ✗\ (\text{需补耦合}\ ✓)$$
$$\textbf{警告③}:\ \text{本链}\ \equiv\ \textbf{van Wee excess counting}\ ✓\ \Longrightarrow\ \text{单独强度}\ \approx 2^n/n=103\ \Longrightarrow\ \textbf{不足以排除 119}\ ✗$$
$$
$$
```

---

## §6 档案给出的**下一步优先级**（逐字登记，未执行 ✓）

```
$$\textbf{①}\ F_1\to F_4\ \text{去重传播表}\ (\text{A/B 两分支};\ \text{严格推出集合};\ \text{逐层}|F_i|;\ \text{全部交叉重叠};\ \text{真并集};\ \text{每点原因标签}\ \{b{=}2\,|\,d_1\,|\,d_2\,|\,\text{传播}\})$$
$$\qquad\textbf{禁忌（档案明文）}:\ \text{各层 forced 数\textbf{不得直接相加}}\ ✗\ (\text{层间重叠 ⟹ 会造假突破});\ \text{A/B \textbf{不得混算}}\ ✗$$
$$\textbf{②}\ \text{小 }n\ (4\!\sim\!7)\ \text{真实最优码上的 "}Q{=}1\ \text{型" 探测（结构性证据）}$$
$$\textbf{③}\ \text{van Wee 1988 原文核对（二阶矩是否已被覆盖 ⟹ 决定本层是否属已知机制）}$$
$$
$$
```

---

## §7 边界（诚实标注）

- §2 恒等式 (III) 为**本档独立重推**（与 archive §11 一致 ✓，并用 120-码数值核验 ✓）
- §3 两条路径均为**已证命题**（路径 B 更强 ✓）；**287 与 143 同源** ✓
- §4 的"无上界来源"为**实跑 grep 结论**（docs / work / memory 三处 ✓）；**未主张**该上界不存在于更广文献 ✗
- **未跑程序** ✓；**未提出新假设** ✗；**未排 119** ✗
