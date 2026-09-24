已查地图：命中（`C3-bridge-C1-verified-and-abi`（本档更正其 §6 序号，未改其结论）／`C3-step5-candidates-and-its-structural-ceiling`）⟹ 引用，不开新案
D0: 本档对象 = ⑥ 逐项核：**⑥-1／⑥-3 通过**；**⚠️ 第 `(6)` 步取逆无效** ⟹ **`C-2:[a,T_R]=1` \textbf{未成立}** ＋ **自捉**（共轭 `b` 不翻转 `a`；`[a,b^2]=1` 不可用）
D1: 0 （[REVIEW] 轮次：核验与自纠，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **⑥ 核验：`C-2` 未成立**

## §1 通过的项

```
**【⑥-1】** 由 `[a,b^2c]=1`：$$ab^2c=b^2ca\ \xrightarrow{\ \times c^{-1}\ }\ ab^2=b^2cac^{-1}\quad(1)$$ ✓✓
$$\Rightarrow\ aT_Ra^{-1}=ab^2c^{-1}a^{-1}=b^2cac^{-2}a^{-1}\ \xrightarrow{c^{-2}=c}\ \boxed{b^2caca^{-1}}$$ ✓✓ —— **`(2)` 正确；且确实\textbf{无法}仅凭 `A`–`E`+`Bridge-C-1` 压入 `\Gamma_{123}`** ✓
**【⑥-3】** `T_R^3=1\Rightarrow T_R^2=T_R^{-1}=cb^{-2}` ✓（直接的）⟹ $$aT_R^2a^{-1}=acb^{-2}a^{-1}$$ ✓ 且 `Bridge-C-1` 给的是 `ab^2c`，**方向不对**，**不能互换** ✓✓
```

## §2 ⚠️ 第 `(6)` 步取逆无效（本档否决）

```
**【您的 (5)】** $$\boxed{cac^{-1}=b^{-2}ab^2}$$ ✓（本档复核：(5) 由 `dad^{-1}=a`（`d=b^2c`）展开得 `b^2cac^{-1}b^{-2}=a`，左乘 `b^{-2}` 右乘 `b^2` ✓ **成立**）✓
**【您的 (6)】** `"由 (5) 的逆形式：c^{-1}ac=b^{-2}ab^2"` —— **✗ 不成立** ✓✓
【为何】 **(i)** 对 `(5)` 取逆得的是 $$ca^{-1}c^{-1}=b^{-2}a^{-1}b^{2}$$（**不是** `c^{-1}ac`）✓；**(ii)** `c^{-1}ac` 是"用 `c^{-1}` 共轭"，与"(用 `c` 共轭)的逆"**不是同一件事**（除非 `c^2=1`，而 `c` 阶为 `3`）✓✓
【正确表达式（本档给）】 由 `(5)` 解出 `a=c^{-1}b^{-2}ab^2c` ⟹ $$c^{-1}ac=c^{-1}(c^{-1}b^{-2}ab^2c)c=c^{-2}b^{-2}ab^2c^{2}\ \xrightarrow{c^{-2}=c,\ c^2=c^{-1}}\ \boxed{c\,b^{-2}ab^2c^{-1}}$$ ✓✓
【⟹ 后果】 $$T_RaT_R^{-1}=b^2\cdot(c^{-1}ac)\cdot b^{-2}=b^2c\,b^{-2}ab^2c^{-1}b^{-2}\ \neq\ a$$ ⟹ **`[a,T_R]=1` \textbf{未成立}** ✓✓✓
```

## §3 ⚠️ 自捉：共轭 `b` **不**翻转 `a`（`b^{-1}\ne b`）

```
**【我一度想用】** $$b^2ab^{-2}=b(bab)b^{-1}=b a^{-1} b^{-1}=(bab)^{-1}=a$$ ⟹ `[a,b^2]=1` ✗✗
【错误处】 最后一步把 `b^{-1}` 当成 `b` —— **`b` 阶为 `6`，`b^{-1}=b^{5}\ne b`** ✓✓
【正确】** `(bab)^{-1}=b^{-1}a^{-1}b^{-1}=b^{5}a^{-1}b^{5}`，**与 `ba^{-1}b` 不同** ✓
【⟹ 结论】 $$\boxed{[a,b^2]=1\ \textbf{不可用}}$$ ✓✓（**该"桥"不存在**；从而 §2 的塌缩式推论也不适用）✓
【教训（与伪引理同族）】 `(x)^{-1}` 展开时**必须保留 `b^{-1}` 的指数**，**不得默认对合** ✓✓
```

## §4 状态（未变＋一项新增）

```
$$\begin{array}{c|c}
⑤\ \text{HAND-CANDIDATE FAMILY}&\textbf{FAIL}\\
C\text{-}1:[a,b^2c]=1&\checkmark\ \text{VERIFIED}\\
(5)\ cac^{-1}=b^{-2}ab^2&\checkmark\ \text{VERIFIED}\\
\boxed{C\text{-}2:[a,T_R]=1}&\textbf{未成立（第 (6) 步无效）}\\
T_R=b^2c^{-1},\ T_R^3=1&\checkmark\\
U_{2,3}&\textbf{OPEN}\\
\text{intersection-defect 证书}&\textbf{尚无}\\
\end{array}$$ ✓
```

## §5 下一步（两条，供裁）

```
**【路 A：在 `(5)` 下重新找耦合】** `(5)` 是**真关系**（把 `c`-共轭 `a` 转成 `b`-共轭 `a`）⟹ 可试 $$T_RaT_R^{-1}=b^2c\,b^{-2}a\,b^2c^{-1}b^{-2}\ \text{能否继续化简}$$（**须用 `b^6=1`、`c^3=1` 与 `(b^2c^{-1})^3=1`，不得再用 `b^{-1}=b`）✓
**【路 B】** 承认 `a`–`T_R` 耦合不成立，**回参数级审计**（`U_{2,3}` 仍 `OPEN`）✓
【⛔ 纪律】 **不解禁 `B`**；**未得证书只写"未产生证书"** ✓✓
【边界】 §1 为**复核您 ⑥-1/⑥-3 的成立**；§2 为**否决第 (6) 步**（附正确表达式）；§3 为**自捉**（`b^{-1}\ne b`）；**皆可手验**；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 inversion        命中文件数=15   :: ./C-first-cut-deformation-potential.md ./rh-discriminator-v11.md ./V189-toolcard-F1-F2-F3-external-mechanism-prescreen.md 
技术词 conjugation      命中文件数=9    :: ./C309-direction1-zero-spacing-anomaly-four-column-audit.md ./p47-g253-asf-audit.md ./gate9-C1star-replacement-audit.md 
```
