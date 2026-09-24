已查地图：命中（`C3-nontriviality-resolved-by-dart-counting`（本档更正其 §4(iii)）／`C3-TL-verified-and-Zomega-structure`（更正其"折叠源"注））⟹ 引用，不开新案
D0: 本档对象 = **`54` 三项审计** ＋ **自纠**：此前记的"参数等价 `\{6,3\}_{(b,0)}\cong\{6,3\}_{2b}`"**降级（很可能不成立）** ＋ 结构注记（`T_LT_R\neq1` 不依赖 `54`）
D1: 0 （[REVIEW] 轮次：审计与自纠，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`54` 审计 ＋ 一处自纠**

## §1 项 1：`54` 的组合计数（无问题）

```
$$\{6,3\}_{(3,0)}:\quad V=2s^2=18,\quad E=3s^2=27,\quad F=s^2=9,\quad \text{Euler }18-27+9=0\ \checkmark$$ ✓
$$\#\text{darts}=2E=54$$ ✓
【⭐ 独立交叉核对】 我前档从 `RGPF-II` 抽到逐字 **"of order `108` for the toroidal polyhedron `\{3,6\}_{(3,0)}`"** ✓ ⟹ `\{3,6\}_{(3,0)}` 与 `\{6,3\}_{(3,0)}` 互为对偶（同 `V,E,F`）⟹ `|\mathrm{Aut}|=4E=108` ✓✓ ⟹ **`E=27` 获文献独立印证** ✓✓
```

## §2 项 2：`54=|\langle b,c\rangle|` 是否成立

```
【判据】 正则地图的 `\mathrm{Aut}` 在 **flags** 上 sharply transitive（`|\mathrm{Aut}|=\#flags=4E`）⟹ `|\mathrm{Rot}|=|\mathrm{Aut}|/2=2E`，且 **`\mathrm{Rot}` 在 darts 上 sharply transitive** ✓
【代入】 $$|\mathrm{Rot}(\{6,3\}_{(3,0)})|=2E=54$$ ✓✓（与 `|\mathrm{Aut}|=108` 交叉一致 ✓）
【parabolic 对应】 `\Gamma_{123}` 的旋转子群 ≅ `\{6,3\}_{(3,0)}` 的旋转群（**由 universal polytope 定义**：vertex-figure 即该 toroid）⟹ $$\boxed{|\langle b,c\rangle|=54}$$ ✓✓
【⟹ 项 2 通过】 ✓
```

## §3 ⚠️ 项 3：参数等价 —— **本档自纠**

```
**【自纠】** 我在 `C3-TL-verified-and-Zomega-structure` 记的"折叠源"$$"\{6,3\}_{(b,0)}\cong\{6,3\}_{2b}"$$（引 `Example 22`）**降级为"未核实、且很可能不成立"** ✓✓
【理由（本档核）】 $$\begin{array}{c|cc}&(b,0)&(2b,0)\\V&2b^2&8b^2\\E&3b^2&12b^2\\F&b^2&4b^2\end{array}$$ ⟹ **两者的 `V,E,F` 成比例但不同** ⟹ **不可能作为地图同构** ✓✓
【更正后的读法】 原句出现在 `Example 22`（关于 **Petrie dual** 与 `\{\{3,2b\}_6,\{2b,3\}_6\}` 的语境）⟹ 记号 `\{6,3\}_{2b}` 的含义 **未定**，**不能**读成"把 `(b,0)` 与 `(2b,0)` 折叠" ✓
【⟹ 对 `54` 的影响】**无**（`54` 由 `V,E,F` 与 Aut 阶直接给出）✓✓
【⟹ 对 `D` 计算的影响】**此前"必须商掉该参数等价"的要求\textbf{撤回}**；若日后确证存在其他参数等价，再另行登记 ✓
```

## §4 ⭐ 结构注记：`T_LT_R\neq1` **不依赖** `54`

```
$$T_LT_R=1\ \Longrightarrow\ T_L=T_R^{-1}=T_R^2\ \Longrightarrow\ T_L^2=T_R^4=1;\ \text{又}\ T_R^3=1\ \Longrightarrow\ T_R=1\ \Longrightarrow\ T_L=1$$ ✓
⟹ **只须 `T_L\neq1`（依赖 `24`）或 `T_R\neq1`（依赖 `54`）之一，即可得 `T_LT_R\neq1`** ✓✓
⟹ **`54` 的审计是 `T_R\neq1` 的前提，但不是 `T_LT_R\neq1` 的必要前提** ✓
```

## §5 审计结论与状态

```
$$\boxed{54\ \text{审计通过（独立印证）};\quad \text{参数等价折叠\textbf{撤回}};\quad ⑤\ \text{可进入}}$$ ✓✓
$$\begin{array}{c|c}
|\langle a,b\rangle|=24&\checkmark\ (\#\text{darts})\\
|\langle b,c\rangle|=54&\checkmark\ (\#\text{darts},\ \text{与 }|\mathrm{Aut}|=108\ \text{一致})\\
"\{6,3\}_{(b,0)}\cong\{6,3\}_{2b}"\ \text{折叠}&\textbf{撤回}\\
T_L,T_R,T_LT_R\neq1&\checkmark\\
U_{2,3}&\textbf{OPEN}\\
⑤\ \text{短字追踪}&\textbf{READY}\\
\mathrm{GAP}\ \text{／Todd–Coxeter}&\textbf{LOCKED}\\
\text{intersection-defect 证书}&\textbf{尚无}\\
\end{array}$$ ✓
【⛔ 边界】 本档**未得证书**；§1–§4 为**手工审计/自纠**（`V,E,F` 与 `108` 交叉核对可手验）；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 Petrie dual      命中文件数=1    :: ./C3-audit-of-54-and-correction-of-folding-note.md 
```
