已查地图：命中（`C3-bridge-C1-verified-and-abi`／`C3-TR3-full-expansion-and-A-closed-with-residual`／`C3-step6-invalid-inversion-C2-not-established`）⟹ **本档撤回其核心关系**，不开新案
D0: 本档对象 = ⛔**撤回**：**`c^2` \textbf{不}centralize `b`** ⟹ **`Bridge-C-1`、`(5)`、`(TR3')` 全部作废** ＋ **给出正确关系 `ab^2c=ca`**
D1: 0 （[REVIEW] 轮次：撤回与更正，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **撤回：`c^2` 不 centralize `b`**

## §1 ⛔ 被推翻的基座命题

```
$$\boxed{\textbf{我此前用的 }c^2bc^{-2}=b\ \text{（即 }c^2\ \text{centralizes}\ b\text{）\ \textbf{是错的}}}$$ ✓✓
**【我原先的"证明"】** `cbc^{-1}=b^{-1}` ⟹ 取平方 ⟹ `c^2bc^{-2}=b` —— **错在把"共轭的平方"当成"共轭 `c^2`"** ✓✓
【正确】 `c^2bc^{-2}=c\,(cbc^{-1})\,c^{-1}=c\,b^{-1}\,c^{-1}` ✓（**不是 `b`**）
**【数值反驳（`S_3`：`b=(12)`，`c=(123)`，《(bc)^2=1`、`b^2=1`、`c^3=1` 全满足）】**
$$c^2b=(23),\qquad bc^2=(13)\ \Longrightarrow\ c^2b\neq bc^2$$ ✓✓ **反例成立** ✓
```

## §2 ⛔ 连带作废（逐条）

```
**(i)** $$\boxed{(TR3')\ b^2c^{-1}b^2=cb^{-2}c\ \textbf{作废}}$$ ✓（其推导依赖 `T_R^2=b^2c^2b^2c^2=b^4c^4=b^4c`，**关键重排 `c^2b^2=b^2c^2` 用错**）✓
**(ii)** $$\boxed{Bridge-C-1\ [a,b^2c]=1\ \textbf{作废}}$$ ✓（其步 4 依赖 `(bc)^2` 与左右乘，最终形态应为**非交换式**，见 §3）✓
**(iii)** $$\boxed{(5)\ cac^{-1}=b^{-2}ab^2\ \textbf{作废（失去支撑）}}$$ ✓（`(5)` 由 `[a,b^2c]=1` 展开而来）✓
**(iv)** `X=T_RaT_R^{-1}` 的两条化简链（**用 `(5)` 与 `(TR3')`**）**作废** ⟹ **`A-CLOSED` 的残差式作废，需重算** ✓✓
```

## §3 ✅ 正确关系（本档重推，只用到 `(ab)^2=(bc)^2=(abc)^2=1`）

```
**(A)** `(ab)^2=1\ \xrightarrow{\ \times a^{-1}\ }` $$\boxed{bab=a^{-1}}$$ ✓
**(B)** `(abc)^2=1\ \xrightarrow{\ \times a^{-1}\ }` $$\boxed{b\,c\,a\,b\,c=a^{-1}}$$ ✓（即 `(bc)a(bc)=a^{-1}`，**但下面用左乘 `b^{-1}` 的展开式**）✓
**(A)=(B)** ⟹ `bab=bcabc` $$\xrightarrow{\ \times b^{-1}\ }\ \boxed{ab=cabc}$$ ✓ [E1]
**[E1] 右乘 `bc`（并用 `(bc)^2=1`）** ⟹ `ab\cdot bc=ca` $$\Longrightarrow\ \boxed{a\,b^2\,c=c\,a}$$ ✓✓✅
**【等价形式】** 右乘 `c^{-1}`：$$\boxed{c\,a\,c^{-1}=a\,b^2}$$ ✓（**共轭 `c` 把 `a` 送到 `a b^2`**）✓✅
【另附】 `b^2` centralizes `b` 显然；**`a` 侧的对应式（由 `(ab)^2`）**：`b a b=a^{-1}` ⟹ `a b a=b^{-1}` ✓
```

## §4 与既有判定的相容性自检

```
**【关键一致性检验】** 前面的链条曾推出 `b^2=c`、从而 `T_R=1` —— **与 `dart` 计数给出的 `T_R\neq1`（`|\langle b,c\rangle|=54`）\textbf{直接冲突}** ✓✓ ⟹ **这正是本档撤回的正确性验证**：**含错的链条必塌缩，而正经结构不塌缩** ✓✓
【⟹ 保留的（不受影响）】 `T_L=b^2a^{-1}`（逐字印证）／`T_R=b^2c^{-1}`（角抵消判据）／`T_R^3=1`／`T_L^2=1`／**非平凡性（`dart` 计数）**／`|\langle a,b\rangle|=24`、`|\langle b,c\rangle|=54` ✓✓
```

## §5 状态与下一步

```
$$\begin{array}{c|c}
Bridge-C-1&\textbf{作废}\\
(5)&\textbf{作废}\\
(TR3')&\textbf{作废}\\
A\text{-}CLOSED（残差式）&\textbf{作废，需重算}\\
\boxed{新关系\ ab^2c=ca\ (\iff cac^{-1}=ab^2)}&\checkmark\ \text{本档重推}\\
⑤\ \text{HAND-CANDIDATE FAMILY}&\text{FAIL（不依赖作废式）}\\
\text{非平凡性（}24/54\text{）}&\checkmark\\
U_{2,3}&\textbf{OPEN}\\
\text{intersection-defect 证书}&\textbf{尚无}\\
\end{array}$$ ✓
【⟹ 对 `B` 的影响】 `B1`（参数空间）与 `B3`（`d^2` 与 `T_R^3` 联立）**必须\textbf{在更正后的关系集上重做** ✓；**`d^2=1` 本身也需重新核**（其来源疑与作废式相关）✓⚠️
【⛔ 教训（本线第三次同类）】 **"共轭的平方"≠"平方元的共轭"**；**任何借"`x^2` 居中/翻转"的步骤必须单独写指数验证** ✓✓
【边界】 §1 含**数值反例**（`S_3`，可手验）；§3 重推**仅用三条 Coxeter 关系**（可手验）；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 centralizer      命中文件数=0    :: 
技术词 retraction       命中文件数=2    :: ./C66-A3-classical-short-interval-second-moment-check-and-target-inside-interval.md ./ID-CLAIMS.tsv 
```
