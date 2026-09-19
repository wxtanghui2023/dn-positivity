D0: 本档对象 = 论文 B 的两处**句级措辞修正建议**（依据 `C-67` 逐字核过的 Droll 原文归属）—— 关系 = 交付物（建议稿），非新机制
D1: 0
FREEZE-ACK: 本档即冻结期内的交付物整理（依 `§8.1`；不改原档、不改结论）

# 论文 B：两处措辞修正（**句级 diff · 建议稿，不改原档**）

> **依据**：`docs/C67-DROLL-Conjecture-327-verbatim-and-alignment-with-paperB-Theorem1.md`
> （Droll 原文已逐字核到：`Conjecture 3.2.7` @ PDF idx 99，行 30–58）
> **纪律**：本文件只是**建议**；`main.md` 与 `README.md` **未作任何改动**。

---

## 修正 ①：`k ≤ 2T²logT` 的**归属错位**

**逐字依据**：
```
k ≤ 2T²logT  —— 属 【Conjecture 1.7.10】（我们逐字核到）
Conjecture 3.2.7 本身为 k ≥ 2，【无上界】
```
⟹ 现文把"`k ≤ 2H²logH` 这一限制"写成 3.2.7 的限制而"我们去掉了它"，**归因错位**（张冠李戴）。

### diff 1.1 — `main.md`（第 33 行）

**现文**
> This is exactly inequality (3.2.7)-type of [Dr12] in the classical case, but with **no restriction k ≤ 2H²logH**: our range is all k ≥ 2.

**建议改为**
> This is exactly the **first** of the two inequalities in [Dr12, Conjecture 3.2.7], in the classical case (τ = 1), for all k ≥ 2. (The restriction k ≤ 2T²logT belongs to [Dr12, Conjecture 1.7.10]; it does not constrain Conjecture 3.2.7 itself.)

### diff 1.2 — `README.md`（第 4 行）

**现文**
> **Claims**: Theorem 1 (stronger than the statement in [Dr12] Conjecture 1.7.10, which restricts k ≤ 2T²logT).

**建议改为**
> **Claims**: Theorem 1 = the **first** of the two inequalities in [Dr12] Conjecture 3.2.7 (classical case τ = 1), for **all k ≥ 2**; in range it is stronger than [Dr12] Conjecture 1.7.10, which requires k ≤ 2T²logT.

---

## 修正 ②：`Conjecture 3.2.7` 含**两条**不等式，本论文只涉及**第一条**

**逐字依据**：
```
Droll 的第二条不等式：≤ (9/4)(·)[ aH log H + b⁺H + 2c log H + 2d ]  —— 本论文未涉及
```

### diff 2.1 — `main.md`（紧随 diff 1.1 之后**追加一句**）

**建议追加**
> Conjecture 3.2.7 contains a **second** inequality (with the factor 9/4 and the term b⁺H); the present paper addresses only the **first** one.

### diff 2.2 — `README.md`（在 Claims 行**末追加**）

**建议追加**
> Only the first inequality of Conjecture 3.2.7 is addressed; the second (factor 9/4, term b⁺H) is not.

---

## 小结

| # | 位置 | 性质 | 为何必须改 |
|:--|:--|:--|:--|
| ① | `main.md` §1 末／`README.md` Claims | **归因错位** | "强于 Droll"的确切所指会被审稿人质疑 |
| ② | 同上 | **范围外延不清** | 需明示只证**第一条**不等式 |

两处均为**句级**修正：不动证明、不动数值、不动结论 ✓

---

## ✅ 状态更新（2026-09-19 12:07）

**四处修正已应用**（不再只是建议稿）：

| # | 文件 | 状态 |
|:--|:--|:--|
| 1.1 | `main.md` 第 33 行 | ✅ 已改 |
| 1.2 | `README.md` 第 4 行 | ✅ 已改 |
| 2.1 | `main.md`（追加第二不等式说明） | ✅ 已改 |
| 2.2 | `README.md`（追加第二不等式说明） | ✅ 已改 |
| — | `main.tex` 第 80–82 行（同一修正，保持编译版一致） | ✅ 已改 |
| — | `main.pdf` | ✅ 已用 `pdflatex` 重编（5 页，0 错误；核验：新措辞已进、旧误述已无） |

**配套交付**：`papers/palojarvi-constant/note.pdf`（2 页，由 `scripts/md2pdf.py` ＋ weasyprint 生成；已剥离内部标记行 `D0`/`D1`/`FREEZE-ACK` 与生成戳记）。
