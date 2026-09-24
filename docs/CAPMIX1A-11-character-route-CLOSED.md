已查地图：命中（`CAPMIX1A-10-char-expansion-verified-and-reencoding-verdict`）⟹ 执行其 §6 之 (1)，并**封档角色路线**，不开新案
D0: 本档对象 = **`+2A_H` 重算验证**（`J_{\rm match}=204/204`）＋ **`N^\ast=\lambda_{\rm raw}` 恒等式验证**（`204/204`）＋ **角色路线 CLOSED（三个锁定结论）** ＋ 一处**精度更正**（`T` 是 **3 阶**非对合）
D1: 1 （延续新自由度；本档给出双向恒等式并**正式关闭**角色算法路线）
[RESEARCH]

# **`CAP-MIX-1A(11)`：角色路线 CLOSED**

## §1 ⭐ 边界项算净（照您的 `S_\eta=mA_\eta+2`）

```
**【修正】** 常数项由 `A_H\Rightarrow2A_H` ✓；`z=0` 处补 **`\mathbf1_{\{z=0\}}`**（因 `\chi(0)=0` 而右式给 `-1`）✓✓
**【实测（修正后）】** $$\texttt{STATS}:\ \text{case}=204,\quad \boxed{J_{\rm match}=204},\quad \boxed{J_{\rm mismatch}=0}$$ ✓✓✓（修正前为 `14/190`）
$$\Longrightarrow\ \boxed{\mathcal J_H=m^2N^\ast-m\,|G\setminus\{-1\}|+2A_H}$$ ✓✓（**逐例成立**）
```

## §2 ⭐⭐ `N^\ast=\lambda_{\rm raw}`：**恒等式**（独立核验 204/204）

```
**【您的证明（本档复核）】** $$-\frac1{1+z}\in G\iff-(1+z)\in G\iff-1-z\in G$$ ✓（`G` 为乘法子群，取逆封闭）✓✓
$$\text{且 }-1-z\in G\Rightarrow-1-z\ne0\Rightarrow z\ne-1\ \Longrightarrow\ \textbf{排除条件冗余}$$ ✓✓
$$\boxed{N^\ast=\#\{z\in G:-1-z\in G\}=\lambda_{\rm raw}}$$ ✓✓
**【独立数值核验】** $$\texttt{N*=$\lambda$raw}:204\ \text{例一致},\ \text{mismatch}:0$$ ✓✓
```

## §3 ⭐ 双向恒等式（两分支，精确）

```
$$\boxed{\mathcal J_H=m^2\lambda_{\rm raw}-m\,|G\setminus\{-1\}|+2A_H}$$ ✓✓
$$\begin{cases}d\ \text{偶}\ (-1\in G):\ |G\setminus\{-1\}|=d-1,\ A_H=m-1\ \Longrightarrow\ \boxed{\mathcal J_H=m^2\lambda_{\rm raw}-q+3m-1}\\ d\ \text{奇}\ (-1\notin G):\ |G\setminus\{-1\}|=d,\ A_H=-1\ \Longrightarrow\ \boxed{\mathcal J_H=m^2\lambda_{\rm raw}-q-1}\end{cases}$$ ✓✓
$$\Longrightarrow\ \text{与 }\lambda_{\rm raw}=\dfrac{q-3m+1+\mathcal J_H}{m^2}\ (\text{偶}),\ \dfrac{q+1+\mathcal J_H}{m^2}\ (\text{奇})\ \textbf{完全回代闭合}$$ ✓✓
```

## §4 ⛔ 一处精度更正（`T` 不是对合）

```
**【您称 `T` 为 Möbius 对合】** 复核：
$$T(x)=-\frac1{1+x},\qquad M=\begin{pmatrix}0&-1\\1&1\end{pmatrix},\qquad M^2=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},\qquad \boxed{M^3=-I}$$ ✓
$$\Longrightarrow\ T\ \text{在 }\mathrm{PGL}_2\ \text{中阶为}\ \mathbf3\ (\textbf{非}2)$$ ⚠️
**【但恒等式不受影响】** `N^\ast=\lambda_{\rm raw}` 靠的是**子群取逆封闭**（§2），与 `T` 的阶无关 ✓✓
```

## §5 ⭐⭐⭐ 角色路线 CLOSED（三个锁定结论）

```
$$\boxed{(1)\ \text{边界项 CLOSED}:\ S_\eta=mA_\eta+2}$$ ✓
$$\boxed{(2)\ \text{恒等式 CLOSED}:\ N^\ast=\lambda_{\rm raw}}$$ ✓
$$\boxed{(3)\ \text{角色算法路线 CLOSED / RE-ENCODING}:\ \mathcal J_H=m^2\lambda_{\rm raw}-m|G\setminus\{-1\}|+2A_H}$$ ✓✓
$$\Longrightarrow\ \text{尽管形式上 }O(m^2)<O(d)\ (q^2<d^3),\ \text{但 }O(m^2)\ \text{个 Jacobi 和精确收缩回 }\lambda_{\rm raw}\ \Longrightarrow\ \textbf{无算法增益}$$ ✓✓✓
**【⟹ 纪律】** **不再在 Jacobi 路线上投入** ✓✓
```

## §6 封档状态与下一步

```
**【`CAP-MIX-1A` 全线状态】**
$$\text{非盲 }78:\ R_*\ \text{判定精确（}43\ \text{witness}+32\ \text{certificate};\ \text{另 }3\ \text{个体证书）};\qquad \text{盲 }126:\ \lambda_{\rm valid}\ \text{精确判定}$$ ✓✓
$$\text{退化点闭合};\qquad \text{角色路线关闭};\qquad \text{唯一未开分支}=\textbf{char 2 四项}$$ ✓
**【下一步（唯一）】** **`CAP-MIX-1B`：`p=2` 四项关系 `a+b+c+d=0`（论文 `Definition 1` 的 char 2 分支）** —— 归一化 `x+y+z+1=0`，Frobenius 展开 `(x+y+z+1)^{2^j}=x^{2^j}+y^{2^j}+z^{2^j}+1` ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停 ✓
【数据】 `out/capmix1N_charExpansion_fixed.txt`（204 行，`J_{\rm match}=204`）；脚本 `scripts/capmix1N_charExpansion.py`（已修正 `+2A_H`）✓
【边界】 §1/§2 为实测；§3/§5 的恒等式为**推导＋数值一致**；§4 更正已登记 ✓

## §附 【技术词回查】（补录）
```
技术词 involution       命中文件数=43   :: ./V106-L3-Q3-independent-sqrt-positivity-audit.md ./V175-level-theorem-local-factor-rigidity-bare-reflection.md ./CAPMIX1A-10-char-expansion-verified-and-reencoding-verdict.md 
技术词 re-encoding      命中文件数=11   :: ./E4-3-R-angle-I-shape-completeness-audit.md ./E5-1-region-to-line-strength-upgrade-boundary-audit.md ./RESEARCH-CONSTITUTION.md 
```
