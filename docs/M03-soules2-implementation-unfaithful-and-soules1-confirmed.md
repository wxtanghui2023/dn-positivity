已查地图：命中（`M03-soules1-audit-residue-at-Lambda-star`）⟹ `Soules-2` 保真性排查与 `Soules-1` 双重确认，不开新案
D0: 本档对象 = ⭐**保真判别器制度**（以定理自带恒等式/断言作实现判别）＋ **`Soules-2` 实现不保真**（16 约定组合全败，结论=未定而非否定）＋ **`Soules-1` 双重确认（单调性 `300/300` ＋ `Σd=Σλ` `58/58`）** ＋ 下一步分叉
D1: 1（首次以"定理自带恒等式"为判据排查实现保真性；避免了一次假阳性）
[RESEARCH]

# **`Soules-2` 实现不保真；`Soules-1` 双重确认**

## §1 ⭐ 本轮最重要的事：**保真判别器挡下一次假阳性**

```
$$\text{审计 }Soules\text{-}2\ \text{时，我的实现先给出 }329\ \text{个"命中"（}\min_i d_i\ge0\text{）}$$ ⚠️
$$\text{但保真判据（原文 Remark 3}:\ \sum_i d_i=\sum_i\lambda_i\text{）}\ \textbf{失败 }157/157 \Longrightarrow \text{该实现不保真}$$ ✓✓✓
$$\Longrightarrow \boxed{\text{329 个"命中"全部作废};\ \textbf{若当时直接采信，就会错称 }\Lambda_*\in\mathcal S_5}$$ ⚠️⚠️
$$\textbf{制度}:\ \text{任何"公式实现"在用于判定前，}\textbf{必须先通过该定理自带的结构性恒等式／断言}$$ ✓✓✓
$$\qquad \text{（}Soules\text{-}1:\ \text{单调性断言};\ Sousles\text{-}2:\ \text{Remark 3};\ \text{同类可推广）}$$
```

## §2 `Soules-2` 结论：**未定**（非否定）

```
$$\text{约定扫描}:\ 16\ \text{组合（}k/l\ \text{表升／降序} \times \text{指标式 }t\ /\ m-t+1\ /\ nj-q+1\text{）}\ \textbf{全部失败 }40/40$$ ✓✓
$$\Longrightarrow\ \text{问题不在指标约定，而在\textbf{结构解析}}（(12)\ \text{式为扁平化文本，中项 Σ 的取和范围与 }\lambda\ \text{指派仍存歧义）$$ ⚠️
$$\Longrightarrow\ \boxed{Soules\text{-}2\ \text{审计结论}=\textbf{未定};\ \textbf{不得写成"Soules-2 失败"}}$$ ✓✓（纪律）
$$\text{出路}:\ \text{(a) 取更清晰的原始表述（}Soules\ 1983\ \text{原文／现代记号复述）};\ \text{(b) 暂搁 }Soules\text{-}2,\ \text{走解析路线（见 }\S4\text{）}$$ ✓
```

## §3 `Soules-1`：**双重确认，残迹有效**

```
$$\text{判别器 1（定理自带单调性断言）}:\ \text{变体 A }300/300;\ \text{变体 B }0/300 \Longrightarrow \text{A 为正确定式}$$ ✓✓
$$\text{判别器 2（Remark 3}:\ \sum d_i=\sum\lambda_i\text{）}:\ \text{变体 A }\boxed{58/58\ \textbf{通过}}$$ ✓✓✓
$$\Longrightarrow\ \boxed{Soules\text{-}1\ \text{实现保真}} \Longrightarrow \textbf{上一轮残迹有效}:\ \max d_1=-\tfrac{106}{375}<0\ (\text{在 }x=(1,1,1,1,1))$$ ✓✓
$$\qquad \text{结论仍为}:\ \textbf{Soules-1 在已搜索参数族中未找到证书}（\text{非"Soules-1 不可实现"}）$$ ✓
```

## §4 下一步分叉（建议顺序已按先生意图调整）

```
$$\boxed{\text{(iii) 解析不可能性}}:\ \text{证 }\max_{1\le x_2\le\dots\le x_5}d_1(x)<0\ (\text{4 变量、结构已明}) \Longrightarrow \textbf{把残迹升级为定理}$$ ✓✓✓
$$\qquad \text{工具齐全}:\ A=\tfrac1{\sum x^2}\le\tfrac15;\ B=\lambda_5\tfrac{x_2^2}{1+x_2^2}\le-\tfrac{41}{100};\ C<0;\ D,E=\lambda_3\ \text{小正项（受分母压制）}$$ ✓
$$\boxed{\text{(iv) 解析合并}}:\ \text{把 }(iii)\ \text{与 Johnson 的 }D(t)<0\ \text{合并},\ \text{寻找新解析不可实现区域}\ W_{\rm new}\supset W$$ ✓✓
$$\qquad \textbf{这才是真正的 }P1（\text{扩张 }W\text{）};\ \text{而非再换一个充分条件}$$ ✓✓
$$\boxed{\text{(a) 补取 }Soules\ 1983\ \text{原文}}:\ \text{仅当需要 }Soules\text{-}2\ \text{时才做};\ \text{(b) LS/ES}:\ \text{最后再考虑}$$ ✓
【⛔ 纪律】 本轮计算仅限**保真性排查**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 的 329 个命中**从未被采信**（先跑判据后判定）；§2 为**未定**；§3 为**双重确认** ✓

## §附 【技术词回查】（补录）
```
技术词 fidelity         命中文件数=1    :: ./ALIGN-A6-A8-A9-A10-A11-B5-B7-A13.md 
技术词 false positive   命中文件数=1    :: ./CAPMIX1A-1-adversarial-FP-search-and-gcd-structure.md 
```
