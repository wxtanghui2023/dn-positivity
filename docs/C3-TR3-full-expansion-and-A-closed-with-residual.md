已查地图：命中（`C3-step6-invalid-inversion-C2-not-established`（本档接其 §5 路 A）／`C3-bridge-C1-verified-and-abi`）⟹ 引用，不开新案
D0: 本档对象 = ⭐**`T_R^3=1` 的完全关系抽取**（`(TR3')`）＋ **`X=T_RaT_R^{-1}` 的化简链与残差** ＋ 判定 **`A-CLOSED`（带具体残差）**
D1: 0 （[REVIEW] 轮次：手工化简，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`T_R^3` 完全展开 ⇒ `A-CLOSED`（带残差）**

## §1 ⭐ 先抽 `T_R^3=1` 的完整关系

```
**【基本信息】** $$c^2\ \text{centralizes}\ b$$ ✓（由 `cbc^{-1}=b^{-1}` 平方 ⟹ `c^2bc^{-2}=b` ✓✓）
$$T_R=b^2c^{-1}=b^2c^2\ \Longrightarrow\ T_R^2=b^2c^2b^2c^2\ \xrightarrow{\ c^2b^2=b^2c^2\ }\ b^4c^4=b^4c$$ ✓
**【`T_R^3=1` 的直接等价形式（本档抽）】** $$T_R^2=T_R^{-1}=cb^{-2}$$ ✓ ⟹ $$b^2c^{-1}b^2c^{-1}=cb^{-2}\ \xrightarrow{\ \times c\ }\ \boxed{b^2c^{-1}b^2=c\,b^{-2}\,c}\quad\mathbf{(TR3')}$$ ✓✓
**【取逆形式】** $$\big(b^2c^{-1}b^2\big)^{-1}=b^{-2}cb^{-2},\qquad \big(cb^{-2}c\big)^{-1}=c^{-1}b^2c^{-1}\ \Longrightarrow\ \boxed{b^{-2}cb^{-2}=c^{-1}b^{2}c^{-1}}$$ ✓✓
**【可用的机械推论】** $$c^{-1}b^2=b^{-2}cb^{-2}c,\qquad c^{-1}b^{-2}=b^{2}cb^{2}c$$ ✓（由 `(TR3')` 左右乘取）
```

## §2 `X=T_RaT_R^{-1}` 的化简链（只用到已验证关系）

```
$$X=b^2c^{-1}a\,c\,b^{-2}$$ ✓（定义）
**【用 `(5)`】** $$c^{-1}ac=c\,b^{-2}ab^{2}c^{-1}$$ ✓（`(5)` 已验证）⟹ $$X=b^2\,\big(cb^{-2}ab^2c^{-1}\big)\,b^{-2}=\boxed{b^2c\,b^{-2}\,a\,b^2c^{-1}b^{-2}}$$ ✓✓
**【再用 `(TR3')` 的推论】** 由 `c^{-1}b^{-2}=b^2cb^2c` ⟹ $$X=b^2c\,b^{-2}\,a\,b^{2}\cdot(b^{2}cb^{2}c)=b^2c\,b^{-2}\,a\,b^{4}c\,b^{2}c$$ ✓（等价形式）
```

## §3 判定：**`A-CLOSED`（带具体残差）**

```
$$\boxed{\text{A-CLOSED}}$$ ✓（依您的三分类：**"在关系闭包内化简后仍无法进入目标轨道，并给出具体残差"**）✓✓
**【具体残差（明确列出，不是"无法证明"）】** $$X=b^2c\,b^{-2}\,a\,b^2c^{-1}b^{-2}\ =\ b^2c\,b^{-2}\,a\,b^4c\,b^2c\ \neq\ a$$ ✓
【判定依据】 `X` 中 `a` **只出现一次且被 `b,c`-字夹住**；现有已验证关系 `(5)`、`(TR3')` 及其推论**只能交换 `a` 两侧的 `c`-因子**，**不产生 `a` 的消去或纯 `b`-化** ⟹ **不能压成 `a`（`A-PASS` 不成立）、也不能压成已知非平凡轨道元素（`A-NEW` 未出现）** ✓
```

## §4 ⚠️ 诚实标注（本线已多次踩陷阱）

```
**【本档可靠性分类】**
**(i)** `c^2` centralizes `b`、`T_R^2=b^4c`、`(TR3')`、及其取逆形式 —— **由 `(bc)^2=1` 与 `T_R^3=1` 机械构造** ✓（**可手验**）✓
**(ii)** `X` 的两条链 —— **仅用已验证的 `(5)` 与 `(TR3')`** ✓✓
**(iii)** 判定 `A-CLOSED` —— **基于"现有关系集不产生 `a` 消去"** ⟹ **是"当前重写系统内"的结论，不是"不存在"** ✓✓
【教训沿用】** 取逆必保留 `b^{-1}` 指数；`c^{-1}(·)c` 与 `(c(·)c^{-1})^{-1}` **不得混同** ✓
```

## §5 状态与下一步

```
$$\begin{array}{c|c}
⑤\ \text{HAND-CANDIDATE FAMILY}&\textbf{FAIL}\\
C\text{-}1:[a,b^2c]=1&\checkmark\ \text{VERIFIED}\\
(5)\ cac^{-1}=b^{-2}ab^{2}&\checkmark\ \text{VERIFIED}\\
(TR3')\ b^2c^{-1}b^2=cb^{-2}c&\checkmark\ \text{本档抽出}\\
X=T_RaT_R^{-1}\ \text{化简}&\textbf{A-CLOSED（残差已列）}\\
C\text{-}2:[a,T_R]=1&\textbf{未成立}\\
U_{2,3}&\textbf{OPEN}\\
\mathrm{GAP}\ \text{／Todd–Coxeter}&\textbf{LOCKED}\\
\text{intersection-defect 证书}&\textbf{尚无}\\
\end{array}$$ ✓
【⟹ 按您的规则】**闭包内化简未给耦合 ⟹ 可正式转 `B`** ✓（`B` 仍待您解禁）✓
【⛔ 边界】 本档**未得证书**；§1–§2 可手验；§3 为**"当前重写系统内"判定**；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 rewrite system   命中文件数=0    :: 
技术词 normal form      命中文件数=17   :: ./V132-O3star-classification-proposition-beta-free-data-lemma.md ./V115-representation-contraction-r1r2r3.md ./p101-collision-orientation.md 
```
