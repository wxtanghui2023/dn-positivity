已查地图（**先查后写**）：`C-296`（逐层审计 ✓；**本档＝唐先生编号的 C-296** ✓）、`C-295`（仓库枚举 ✓）、`C-294`（架构 ✓）。一手材料：`Coset.lean`／`Extension.lean`／`Descent.lean`／`Reduction.lean` raw 逐字（✓）。回查见 §6 ✓

D0: 本档对象 = **C-297：Coset descent 定向审计（唐先生四项清单）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 四项清单结论（✓✓）

$$\textbf{① } q\ \text{是否必为素数}：\textbf{在已审两层中，} q.Prime\ \text{是}\ \textbf{输入假设}✗，\textbf{不是}在此推导 ✓；\text{推导点应在}\ \texttt{Extension.lean}\ \text{主定理内（本次仅部分读到}⚠️）$$
$$\textbf{② } n < p/(2q)：\checkmark\checkmark\ \text{结论逐字就是}\ \texttt{2 * (q * n) < p}✓；\text{严格性由}\ \textbf{奇偶性} \text{保证（} p\ \text{奇、}2qn\ \text{偶 }\Longrightarrow 2qn\ne p✓）$$
$$\textbf{③ 两分支是否无漏项}：\checkmark\checkmark\ \text{无漏项} \text{——见 §3（}\texttt{by\_cases}\ +\ q\%3\in\{1,2\}\ \text{对素数} q\ge5\ \text{完备 }✓）$$
$$\textbf{④ } |p-an|/2\ \text{是否仍同 coset}：\checkmark\ \text{结构上成立}✓\ \text{——由 ①}j<q\ \text{乘子不变 ②}2,3\in H\ \text{ ③ 取负不变 三条共同保持 }✓\text{（细节见 §4}✓）$$

---

## §1 `short_representative_of_invariance` **完整语句**（逐字 ✓✓）

```
theorem short_representative_of_invariance
    (p q : ℕ) (hp : p.Prime) (hpgt : 3 < p)
    (hq : q.Prime) (hqge : 5 ≤ q) (hqp : 2 * q < p)
    (P : ZMod p → Prop)
    (hneg : ∀ x, P (-x) ↔ P x)
    (hsmall : ∀ j : ℕ, 0 < j → j < q → ∀ x,
      P ((j : ZMod p) * x) ↔ P x)
    (hex : ∃ x : ZMod p, x ≠ 0 ∧ P x) :
    ∃ n : ℕ, 0 < n ∧ 2 * (q * n) < p ∧ P (n : ZMod p)
```

- **docstring 逐字** ✓：Every nonempty set of nonzero residues invariant under negation and multipliers below `q` has a representative below `p / (2q)`. For a subgroup containing those multipliers, apply this to any multiplicative coset. ✓✓
- **⟹ 这是"纯组合／有限域"引理** ✓：**无**解析输入 ✓、**无** L-函数 ✓、**无** GRH ✓✓
- **假设清单** ✓：`p` 素 `> 3` ✓；`q` **素** 且 `>= 5` ✓；`2q < p` ✓；`P` 非空（含非零元 ✓）、对取负不变 ✓、对一切 `j < q` 的**乘子**不变 ✓

## §2 关于 ①：`q.Prime` 是**输入**（✓✓ 关键发现）

- `Coset.lean`：`hq : q.Prime` 在**假设行** ✓
- `Extension.lean` 调用侧：`(hq : q.Prime) (hqge : 5 ≤ q) (hqp : 2 * q < p)` 也**同为假设** ✓
- ⟹ **本引理不负责证明"最小坏乘子是素数"** ✗ —— 该步骤必在 **`Extension.lean` 主定理**（`half_interval_extension_via_invariance` 的证明体 ✓）或更上层 ✓
- **审计待办（唯一未闭合项）** ✓✓：定位 `hq : q.Prime` 的** discharger**（谁提供 q 为素、为何 `5 <= q`、为何 `2q < p` ✓）
- **注意同名陷阱** ✗✓：`Reduction.lean` 里也有一个 `q`（`Nat.exists_prime_and_dvd` 取出的**素因子** ✓），与 `H` 无关 ✗ —— **两个 q 不是同一个对象** ✓

## §3 关于 ③：分支**无漏项**（✓✓）

- **外层**（`Extension.lean`／`Descent.lean` 可见 ✓）：`by_cases hstrip : (2 * q - 1) * n < p` ✓
  - 分支 A：`(2q-1)n < p` ✓
  - 分支 B：`¬((2q-1)n < p)` ⟹ `p <= (2q-1)n` ✓；再与 `hshort' : p < 2*q*n` 合并 ⟹ **`(2q-1)n <= p < 2qn`** ✓✓
  ⟹ **A ∪ B 覆盖全部情形，无第三情形** ✓✓
- **内层**（q mod 3 ✓）：`hqmod : q % 3 = 1 ∨ q % 3 = 2` ✓ —— 对**素数** `q >= 5` **完备** ✓✓（`q % 3 ≠ 0` ✓，推导可见 ✓）
- ⟹ **两分支 × 两子分支 = 4 格，无漏项** ✓✓
- **与 `a` 的对应**（✓✓，可手验）：`a = 2q - 1`（`q ≡ 2 mod 3` 时 `3 | a` ✓）；`a = 2q + 1`（`q ≡ 1 mod 3` 时 `3 | a` ✓）✓
- **`j = a/3` 满足 `0 < j < q`** ✓（代码内 `omega` 闭合 ✓）

## §4 关于 ④：同 coset 保持的三条机制（✓✓）

- **第 1 条（乘子）** ✓：`hsmall j hjpos hjlt` ⟹ 乘 `j < q` 保持 `P` ✓
- **第 2 条（2、3 已 good）** ✓：`htwo`／`hthree`（`IsGood F 2`／`IsGood F 3` ✓）⟹ 乘 2 或 3 保持"坏集" ✓
- **第 3 条（取负）** ✓：`hneg` ✓（在 `Coset.lean` 末尾由 `exact_mul_iff ... hminus ...` ＋ `not_congr` **导出** ✓✓ —— 即 `P` 是"**乘法性失效**"集合 ✓，用 `not_congr` 把 good 的不变性转成 bad 的不变性 ✓）
- **结合** ✓：`ha : a = 3*j`（或 `2*j` 型 ✓）＋ `j < q` ＋ `2,3 in H` ⟹ `P (a * n)` ✓✓
- **v 的选取** ✓：分支 A 用 `v := a*n - p`（`n < v < 2n` ✓）；分支 B 用 `v := p - a*n`（`0 < v < 2n` ✓）；并由**奇偶性**使 `v` 为偶 ✓ ⟹ 取 `v/2 < n` ✓✓
- **⟹ 得到更小的同余坏参数** ✓✓ —— 与"最小坏参数"矛盾 ✓ ⟹ **`H = F_p^×`** ✓

## §5 provenance 与状态（**维持分离**✗✓）

- 媒体（如 Lookonchain ✓）把该仓库归因于 GPT-6 Astra ✓ —— 这是 **provenance claim** ✓，**不得**与 Lean 定理的逻辑正确性混为一谈 ✗✓
- 仓库自身**未**证明其与 Astra／OpenAI 的关联 ✗ ⟹ 证据链仍只到 **公开 GitHub artifact** ✓
- **状态维持** ✓：语句级 ✓／公理级 ✓／Coset descent **结构上无漏项** ✓／**`hq.Prime` 的 discharger 待定位** ⚠️／独立复现待做 ⚠️

## §6 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **纪律**：不接 M-TOWER ✗；不建判据 ✗；不与 L／F／B／R 排序 ✗；不问 RH ✓
- **不得**写成：该引用已完全闭合 ✗（`hq.Prime` 未定位 ✓）；该结果已独立复现 ✗；该结果是 Astra 官方成果 ✗
- **本档新增词**：`定向审计`／`同 coset 保持`（0 命中 ✓）
