已查地图：命中（`C3-pdf-full-scan-what-it-does-and-does-not-contain`／`C3-problem16-17-verbatim-parameter-space`）⟹ 引用，不开新案
D0: 本档对象 = `Monson–Schulte 2008`（`arXiv:0805.3479`）取证：**modular 构造精确覆盖范围** ＋ 四类语义**重要更正**（modular 覆盖**不移除** `D`）＋ 免费下一站
D1: 0 （[REVIEW] 轮次：取证与更正，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **Modular 覆盖范围 ＋ 四类语义更正**

## §1 来源（已归档）

```
`B. Monson` ＆ `E. Schulte`，**"Locally Toroidal Polytopes and Modular Linear Groups"**（`arXiv:0805.3479v1`，`2008-05`，`21` 页；`2010` 发表于 `Discrete Math.`）✓
存：`sources/monson-schulte-2008-arXiv0805.3479.pdf` ✓
```

## §2 ⭐⭐ 逐字证据

```
**【现状（`2008`）】** "The `n`-polytopes of this kind **have not yet been fully classified**, although quite a lot is known（see `[6, Chs. 10-12]`）." ✓✓
**【`[3,6,3]` 具体算例】** "When `s=4` we find that `G_4` **has order `7680`** and is the automorphism group of a locally toroidal 4-polytope in the class `\langle\{3,6\}_{(4,0)},\{6,3\}_{(4,0)}\rangle`." ✓✓
**【⭐⭐ modular 构造的精确参数覆盖】** "`G^d` is a string C-group **whenever the modulus `d` is divisible by either `4` or an odd prime, that is, whenever `d\ge3`**. The polytope `P(G^d)` is in the class `\langle\{3,6\}_q,\{6,3\}_r\rangle`，where **always `q=(d,0)`**，but **`r=(d,0)` when `3\nmid d`** and **`r=(d/3,d/3)` when `3\mid d`**." ✓✓✓
```

## §3 ⚠️ 四类语义**更正**（重要）

```
**【更正】** modular 构造给出的是**"该类中存在有限 polytope"（有限商/有限成员）**，**不是**"universal polytope 有限" ⟹ $$\boxed{\text{modular 覆盖}\ \textbf{不移除}\ D}$$ ✓✓（与您"**参数出现过 ≠ universal classification 已解决**"一致）✓
【⟹ 框架修正】**排除项只剩两类**：**(A)** `\{11E\}` 已决｜**(B)** `11H` 关系归约；**原 `C`（modular）不是排除项**，仅作**"该类非空"的证据** ✓✓
【⟹ 后果】 `D`（universal finite/infinite 未决）**可能很大** ⟹ **"最小未决"更值得问**（取最小参数组合即可）✓
```

## §4 ⭐ 免费下一站（重大线索）

```
**【引用 [9]】** "In `[9]` we discussed **all locally toroidal 4-polytopes `P(G_p)`** which arise from our construction with prime modulus `p`." ✓
　`[9]` ＝ `B. Monson` ＆ `E. Schulte`，**"Reflection groups and polytopes over finite fields, II"**，*Adv. in Appl. Math.* **38** (2007), 327–356 ✓
　（同系：`[8]` Part I，*Adv. Appl. Math.* **33** (2004) 290–317；`[10]` Part III，**41** (2008) 76–94）✓
**【⟹ 关键】** 该文**系统处理 rank-4 locally toroidal 的 modular 构造** ⟹ **极可能含我们缺的"哪些参数已定"清单** ✓✓
　**且早前检索显示其有 `arXiv` 版**：`arXiv:math/0601502`（"Reflection Groups and Polytopes over Finite Fields, II"，`2006`）⟹ **免费、且 `arXiv` 通常可直接抓取** ✓✓
```

## §5 拼图更新

```
$$\begin{array}{c|c|c}
\text{项目}&\text{状态}&\text{来源}\\
\hline
\text{参数空间}\ s\ge2,t=0\ \text{或}\ s=t;\ u\ge2,v=0\ \text{或}\ u=v&\checkmark&\text{PDF p11}\\
\text{存在性}\ne\text{群}\ne\text{有限性}&\checkmark&\text{PDF p10}\\
\{3,6,3\}\ \text{未完全分类}\ (2008)&\checkmark&\text{MS2008\ \S7}\\
\text{modular 覆盖范围}\ q=(d,0),\ r\in\{(d,0),(d/3,d/3)\},\ d\ge3&\checkmark&\text{MS2008\ \S7}\\
\text{modular}\ \ne\ \text{universal 判定（∴ 不移除 }D)&\checkmark\ (\text{更正})&\text{本档}\\
\text{sparse 清单（`\{11E,H\}`）}&\textbf{OPEN}&\text{书}\ [42]\\
\text{最小未决 }(s_*,t_*,u_*,v_*)&\textbf{OPEN}&—\\
H\ \text{固定维？}\ H>0\iff\text{finite？}&\textbf{OPEN}&—\\
\end{array}$$ ✓
```

## §6 下一步（不计算）

```
**【第一优先】** 抓 **`arXiv:math/0601502`**（`Part II`，**免费**）⟹ 取 rank-4 locally toroidal 的**modular 参数清单** ⟹ 再与 `\{11E,H\}` sparse 清单交叉 ✓
【备选】 `1992 CMH`（`e-periodica`，浏览器）｜书 `[42] §11E/H`（`Cambridge` 挡）✓
【⛔ 纪律】 **不计算、不实现**；`C2` 暂停 ✓
【边界】 §1–§4 为**本地 `pymupdf` 逐字提取**（原文已归档）；§3 更正是**本档推理**；§5 为**拼图更新**；`arXiv:math/0601502` 的可抓性**未实测**；未制造候选／未启动搜索／未碰 RH。

## §7 【技术词回查】（补录）
```
技术词 modular linear groups 命中文件数=3    :: ./C3-problem16-17-verbatim-parameter-space.md ./C3-concretized-36s-63t-family.md ./C3-premise-confirmed-by-handbook.md 
```
