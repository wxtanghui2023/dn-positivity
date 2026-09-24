已查地图：命中（`CAPMIX1A-6-ledger-reconciled-and-decision-procedure`）⟹ 执行其 §5 之 (1)，不开新案
D0: 本档对象 = **75 例非盲逐例判定表**（witness/certificate 区分 ＋ 实际 `R_*` 根保存 ＋ 退化/伪根分解）＋ 两处**记账伪影**登记
D1: 1 （延续新自由度；本档把"判定过程"钉成**逐例可核验表格**）
[RESEARCH]

# **`CAP-MIX-1A(7)`：75 例判定表**

## §1 ⭐⭐ 主结果（与预测精确一致）

```
$$\textbf{SUMMARY}:\quad \boxed{N_{\rm witness}=43},\qquad \boxed{N_{\rm certificate}=32},\qquad \boxed{FP=0},\qquad \boxed{FN=0},\qquad \text{rows}=75}$$ ✓✓✓
$$\Longrightarrow\ \textbf{75/75 与独立真值逐例一致（零误差）}$$ ✓✓
**【术语（照您要求）】** `witness certificate` = 给出实际 `x,y\in G` 的三元组；`cap certificate` = 给出 `R_*` 并证明其中无有效端点 ✓
```

## §2 ⭐ `R_*` 实测（cap certificate 类，32 例）

```
$$|R_*|\ \text{直方图}:\quad \{0:7,\ 1:13,\ 2:7,\ 3:1,\ 4:4\}\qquad\Longrightarrow\ \textbf{证书类压缩到 }|R_*|\le4\ (\text{常数级})$$ ✓✓
**【⭐ 您特别要求的检查 —— `R_*=\varnothing` 而非 `\{1\}`】** $$7\ \text{例}\ |R_*|=0\ (\text{即 }g_*=1)\ \Longrightarrow\ \boxed{R_*=\varnothing}\ \checkmark$$ ✓✓（**`x=1` 不是必然共同根**，已在证书定义中写清）
**【量化】** $$\#\{x=1\in R_*\}=12\ (\text{含 }1),\qquad \#\{1\notin R_*\}=20\ (\text{不含 }1)$$ ✓✓
$$\Longrightarrow\ \textbf{32 例中 20 例即使 }x=1\ \text{也不在 }R_*\ \text{中}$$ —— **彻底否证"1 是共同根"的旧默认** ✓✓
**【退化根出现】** $$\#\{-2\in R_*\}=9,\qquad \#\{-1/2\in R_*\}=9,\qquad \#\{\text{其他伪根}\}=26$$ ✓
```

## §3 ⚠️ 两处记账伪影（数学无错，标签须记清）

```
**(i) 标签歧义**：`cert_break` 的 `one/zero` 指 **"`1\in R_*` / `1\notin R_*`"**，**不是** "`R_*` 非空/空"；真正的空集见 §2 的 `|R_*|=0` 那 7 例 ✓
**(ii) p=3 的退化槽重合**：$$p=3\ \text{时}\ -2\equiv-\tfrac12\equiv1\ (\mathrm{mod}\ 3)\ \Longrightarrow\ \text{"退化候选"与平凡根 }1\ \textbf{重合}$$ ✓
　⟹ 解释了 `decomp_ok=27 / decomp_bad=5` 的 5 处不符（**全部为 p=3 实例的重复计数**，非数学冲突）✓
```

## §4 ⚠️ 一处须修正的措辞（压缩强度）

```
**【实测】** `|R_*|` 在 **certificate 类**为 `\le4`（常数级 ✓）；但在 **witness 类**可很大（表中见 `|R_*|=8,26,31,32,56`）✓
$$\Longrightarrow\ \textbf{压缩强度按类不同}:\ \text{证书类强压缩};\ \text{witness 类弱压缩（但仍给出显式 witness）}$$ ⚠️
**【⟹ 精确表述（替代"\|R_*\| 通常为常数级"）】**
$$\boxed{\text{判定完备（限非盲类）＋ 证书类常数级压缩};\ \text{witness 类靠显式构造}}$$ ✓✓
```

## §5 `CAP-MIX-1A` 非盲部分：可封档

```
**在 `J\ne\varnothing` 的 75 例上**：$$\text{Frobenius 族把 }G\ \text{压缩到 }R_*;\qquad \text{有效 AP 的存在性由 }R_*\ \textbf{完全决定}$$ ✓✓
$$\text{且}:N_{\rm witness}=43,\ N_{\rm certificate}=32,\ FP=FN=0\ (\text{逐例可查})$$ ✓✓
**【仍开放（唯一）】** $$J=\varnothing\ \Longrightarrow\ Q_j\equiv0\ \Longrightarrow\ R_*=G\ \Longrightarrow\ \text{压缩失效（126/204，62\%）}$$ ✓✓
$$\Longrightarrow\ \textbf{新问题（下一阶段）}:\ \boxed{\text{当 }J=\varnothing\ \text{时，如何从 }G\ \text{构造非 Frobenius 的压缩映射？}}$$ ✓
```

## §6 下一步

```
**(1)** 把 §1 的**证书可靠性**写成一行证明（推导已在档）✓
**(2)** **盲区压缩源**两候选：(a) `x^d=1\wedge(-1-x)^d\ne1` 的**联立**；(b) **子群加法像结构** ✓✓
【⛔ 纪律】 统一口径（`126+3+75`）；`8/24`、`1/11` 作废；计算仅本实验；`U_{2,3}` 暂停 ✓
【数据】 `out/capmix1K_decision_table.txt`（75 行逐例，含**全部实际 `R_*` 根**）；脚本 `scripts/capmix1k_decision_table.py` ✓
【边界】 §4 措辞已按实测修正（压缩强度分两类）⚠️

## §附 【技术词回查】（补录）
```
技术词 witness certificate 命中文件数=1    :: ./CAPMIX1A-7-decision-table-75-cases.md 
技术词 cap certificate  命中文件数=1    :: ./CAPMIX1A-7-decision-table-75-cases.md 
```
