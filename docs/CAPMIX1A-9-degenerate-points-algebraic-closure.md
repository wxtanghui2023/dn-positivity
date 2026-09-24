已查地图：命中（`CAPMIX1B-lambda-additive-image-exact-on-blind`）⟹ 执行其 §5 之 (2)，不开新案
D0: 本档对象 = **退化点算术闭合**：`\lambda_{\rm raw}-\lambda_{\rm valid}=|D(G)|` **204/204 验证** ＋ ⛔**一次公式误用自纠** ＋ 第二端点条件代数化 ＋ 步骤②的可行性预判
D1: 1 （延续新自由度；本档把 `\lambda_{\rm valid}` 的"程序扣除规则"**化为纯代数指标**）
[RESEARCH]

# **`CAP-MIX-1A(9)`：退化点闭合**

## §1 ⛔ 自纠（第一次实现用错公式）

```
**【错误实现】** 用"候选集交 `G`"计数：$$|D|=\#\{1,-2,-\tfrac12\}\cap G\ \Longrightarrow\ \textbf{match}=110,\ \textbf{mismatch}=94$$ ✗
**【诊断（差异恰好符合代数预测）】** $$\text{mismatch}=94=204-110=\#\{(-2)\notin G\}$$ ✓✓
**【错误本质】** 漏掉了 `D(G)` 的**联合条件 `-1-x\in G`**：$$x=1\ \text{与}\ x=-2\ \textbf{各自}贡献一个退化 `x`\ (\text{当 }-2\in G)\ \Longrightarrow\ \text{不是集合交，而是两条独立贡献}$$ ✓✓
```

## §2 ⭐⭐ 修正后：`|D(G)|` 定义 ＋ **204/204 命中**

```
$$\boxed{D(G)=\{x\in G:\ -1-x\in G,\ x\in\{1,-2,-\tfrac12\}\}}\qquad(\textbf{集合计数，故 }p=3\ \text{碰撞自动只计一次})$$ ✓✓
$$\textbf{STATS}:\quad \boxed{\text{case}=204,\ \text{match}=204,\ \text{mismatch}=0},\qquad \sum(\lambda_{\rm raw}-\lambda_{\rm valid})=268$$ ✓✓✓
$$\Longrightarrow\ \boxed{\lambda_{\rm raw}-\lambda_{\rm valid}=|D(G)|\quad\textbf{逐例成立}}$$ ✓✓
**【三条贡献的分解（照您推导）】**
$$x=1:\ \text{条件}\ -2\in G;\qquad x=-2:\ \text{条件}\ -2\in G;\qquad x=-\tfrac12:\ \text{条件}\ -\tfrac12\in G$$ ✓
$$\Longrightarrow\ \text{（}p\ne3\text{）}|D(G)|=2\cdot[\![-2\in G]\!]+[\![-\tfrac12\in G]\!]$$ ✓（**这正是 `mismatch=94` 的来源**）
```

## §3 ⭐ 第二端点条件的纯代数形式

```
$$\boxed{-2\in G\iff(-2)^d=1};\qquad\boxed{-\tfrac12\in G\iff 2^{\,d}=(-1)^d}$$ ✓
【注】照您提醒：**这是关于具体 `G` 的条件，不得简化为 `d` 的奇偶性**（`-2` 不必落在 `\mathbb F_p` 的小子群结构里）✓
```

## §4 ⭐ 结果：`\lambda_{\rm valid}` 的**无规则代数指标**

```
$$\boxed{\lambda_{\rm valid}=\Big|\big\{x\in G:\ -1-x\in G\big\}\setminus\{1,-2,-\tfrac12\}\Big|}$$ ✓✓
$$\Longrightarrow\ \textbf{程序层面的"特殊扣除规则"可全部删除};\ \text{退化修正理论上限}=3\ (\text{实际更小})$$ ✓✓
```

## §5 步骤②的可行性预判（**先做诚实判断，不急着上 Jacobi**）

```
$$\lambda_{\rm raw}=\#\{x\in G:\ x+1\in G\}=\sum_{x}1_G(x)\,1_G(x+1)$$ ✓（即您说的**平移自相关**，Frobenius 正交）
**【随机模型主项】** $$\mathbb E\,\lambda_{\rm raw}\approx\frac{d^2}{q}=\frac{d}{m},\qquad m=\frac{q-1}{d}$$ ✓
**【角色展开后的误差上界（Weil 型）】** 非平凡 `\chi` 对的 Jacobi 和满足 `|J|\le\sqrt q` ⟹ 粗界
$$\lambda_{\rm raw}\ \le\ \frac{d^2}{q}+\sqrt q$$ ⚠️
$$\Longrightarrow\ \boxed{\text{粗 Weil 界\textbf{不能}推出 }\lambda_{\rm valid}=0\ (\text{因 }\sqrt q\ge1\ \text{恒})}$$ ✗
**【⟹ 步骤②的正确目标（收紧后）】** 不是"用粗误差界强迫零"，而是：
$$(i)\ \text{求出 }\lambda_{\rm raw}\ \text{的\textbf{精确写法}}:\ \lambda_{\rm raw}=\frac1{m^2}\sum_{r,s}\chi^r(-1)\,J(\text{型})\ \text{的闭式};\quad (ii)\ \text{算其代价 }O(m^2)\ \text{vs 枚举 }O(d)$$ ✓✓
$$\text{交叉点}:\ m^2<d\iff\Big(\frac{q}{d}\Big)^2<d\iff q^2<d^3\ \Longrightarrow\ \text{此时\textbf{廉价}}$$ ✓✓
**【因此步骤②判据】** 只有先得到 `\lambda_{\rm raw}` 的**精确闭式**，才谈得上"廉价 cap 证书"；**粗界路线已判不可行** ✓
```

## §6 状态与下一步

```
**【1A 已完成】** 非盲 75/78 判定表（`43 witness + 32 certificate`，零误差）；`R_*` 与 `\lambda` 同一关联集 ✓ —— **不再回头碰 1A** ✓
**【本档新闭合】** `\lambda_{\rm valid}=\lambda_{\rm raw}-|D(G)|`，且 `|D(G)|` 由 `(-2)^d=1`、`2^d=(-1)^d` 两条件给出 ✓✓
**【下一步（步骤②）】** 求 `\lambda_{\rm raw}` 的**精确角色展开闭式**（含 `r=0`/`s=0` 退化的分类处理），并给出 `O(m^2)` 算法与 `O(d)` 枚举的**交叉判据** ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**暂不碰 char 2** ✓
【数据】 `out/capmix1M_degenerate_fixed.txt`（204 行真值表）；脚本 `scripts/capmix1M_degenerate_closure.py`（已修正）✓
【边界】 §2 的 `204/204` 为实测；`|D(G)|` 的代数分解为推导 ✓

## §附 【技术词回查】（补录）
```
技术词 degenerate       命中文件数=30   :: ./E20-E40-zero-density-2026-read.md ./GT-0-and-GT-STRATEGY-audit.md ./CAPMIX1A-6-ledger-reconciled-and-decision-procedure.md 
技术词 Jacobi sum       命中文件数=1    :: ./CROSS-0-additive-multiplicative-cross-invariant-MAP-CHECK.md 
```
