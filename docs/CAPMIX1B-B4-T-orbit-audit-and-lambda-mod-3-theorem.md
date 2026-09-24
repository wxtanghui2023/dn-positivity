已查地图：命中（`CAPMIX1B-B3-bridge-1A-1B-same-translation-incidence`）⟹ 执行其 §5 之 (1) 的 `B4`，不开新案
D0: 本档对象 = **`B4`：`T(x)=1+x^{-1}` 的阶 3 群作用审计**：`T`-不变性（39/39）＋ ⭐**`\lambda\bmod3` 结构定理（39/39 验证）** ＋ `\lambda=0` 的 `d,n` 分类 ＋ **一条充分判据**与 **2 例未解释子案**
D1: 1 （新自由度：`I(G)` 上出现**阶 3 群作用**，并得到**只依赖 `d\bmod3` 的 `\lambda` 同余定理**）
[RESEARCH]

# **`CAP-MIX-1B · B4`：`T`-轨道与 `\lambda\bmod3` 定理**

## §1 ⭐ `T(x)=1+x^{-1}` 与 `T^3=\mathrm{id}`

```
$$T(x)=1+\frac1x=1+x^{-1};\qquad T^2(x)=1+\frac1{1+1/x}=\frac1{x+1};\qquad \boxed{T^3(x)=x}$$ ✓✓（char 2）
$$\textbf{实测}:\qquad \texttt{T\_inv\_bad}=0\ \Longrightarrow\ I(G)\ \textbf{严格 } T\text{-不变}\quad(\text{39/39})$$ ✓✓
$$\Longrightarrow\ \boxed{I(G)=\text{若干 } T\text{-轨道之并},\ \text{轨道长度}\in\{1,3\}}$$ ✓✓
**【新工具】** 此前未用过的**阶 3 群作用**，作用在与 `B2` 的 Frobenius 作用（`30/30` 完整轨道）**同一个** `I(G)` 上 ✓✓
```

## §2 ⭐⭐ `\lambda\bmod3` 结构定理（完全由 `d` 决定）

```
**【固定点】** $$T(x)=x\iff x=1+\frac1x\iff x^2+x+1=0\ (\mathrm{char}\,2)\iff x^3=1,\ x\ne1$$ ✓
$$\Longrightarrow\ \text{固定点}=\{\omega,\omega^2\}\ (\textbf{三阶根}),\qquad 1+\omega=\omega^2$$ ✓
$$\Longrightarrow\ \omega\in G\iff 3\mid d$$ ✓（**唯一阶 `d` 子群含三阶元 ⟺ `3\mid d`**）
**【定理形态】** $$\boxed{\lambda(G)\equiv\begin{cases}2\!\!\pmod 3,&3\mid d\\[2pt]0\!\!\pmod 3,&3\nmid d\end{cases}}$$ ✓✓
$$\text{更细}:\ 3\mid d\Rightarrow\lambda=2+3k\ (\text{恰 }2\ \text{个固定点});\qquad 3\nmid d\Rightarrow\lambda=3k\ (\text{无固定点})$$ ✓
**【实测（39 例）】** $$\texttt{lam\_mod3\_ok}=39,\quad \texttt{lam\_mod3\_bad}=0;\qquad \texttt{fix2\_when\_3d}=20/20,\qquad \texttt{fix0\_when\_not3d}=19/19$$ ✓✓✓
**【轨道结构直方图】** $$\{(\varnothing):9,\ (1):11,\ (3):10,\ (1,3):9\}\ \Longrightarrow\ \textbf{只出现长度 }1\ \text{与 }3\ \text{的轨道}$$ ✓✓
```

## §3 `\lambda=0` 的 `d,n` 分类（9 例）

```
$$\texttt{lam0\_cases}=9:\quad d\in\{5,5,17,11,23,89,5,13,65\}$$ ✓
$$\boxed{\lambda=0\ \Longrightarrow\ 3\nmid d}\quad(\texttt{lam0\_d3}=0)\ \checkmark$$ ✓✓（**必要条件成立**）
$$d\bmod3:\ 2\ \text{占 }8,\ 1\ \text{占 }1;\qquad n:\ \text{偶 }7,\ \text{奇 }2$$ ✓
```

## §4 ⭐ 一条**充分判据**（本档导出）＋ **2 例未解释**

```
**【判据】** $$\boxed{\text{若}\ \exists k:\ 2^k\equiv-1\pmod d\ \text{且}\ 3\nmid d\ \Longrightarrow\ \lambda(G)=0}$$ ✓✓
**【推导】** 设 `x,1+x\in G`。则 `(1+x)^{2^k}=1+x^{2^k}=1+x^{-1}`（因 `x^{2^k}=x^{\pm1}`）；又 `1+x\in G\Rightarrow(1+x)^{2^k}=(1+x)^{-1}`：
$$(1+x)^{-1}=1+x^{-1}\ \Longrightarrow\ (1+x)\big(1+x^{-1}\big)=1\ \Longrightarrow\ \frac{(1+x)^2}{x}=1\ \Longrightarrow\ x^2+x+1=0\ \Longrightarrow\ 3\mid d$$ ✓✓
$$\text{与 }3\nmid d\ \text{矛盾}\ \Longrightarrow\ \lambda=0$$ ✓✓
**【覆盖面（手算）】** `d=5,5,17,11,13,65,5`（**7/9**）满足 `-1\in\langle2\rangle_d` ⟹ 判据适用 ✓（**含论文族 `d=2^k+1`**：`2^k\equiv-1` ✓）✓
**【剩余 2 例未解释】** $$d=23\ (n=11),\qquad d=89\ (n=11),\qquad \text{两者 }\mathrm{ord}_d(2)=11\ (\textbf{奇})\Rightarrow-1\notin\langle2\rangle_d$$ ⚠️
$$\Longrightarrow\ \textbf{需第二机制（登记为开放子案）};\quad \text{注}:\ n=11\ \text{时}\ q-1=2047=23\cdot89\ (\text{互补对偶})$$ ✓
```

## §5 ⛔ 边界（须记清，防误读）

```
$$\lambda=0\ \textbf{不蕴含 CAP}:\quad \text{CAP}\iff \text{Valid}=\varnothing\iff V_\ast\subseteq\{z=0\};\quad \lambda=0\Rightarrow\text{直线空}\Rightarrow\text{CAP}\iff V_\ast=\varnothing$$ ✓
$$\text{实测两型皆存在}:\ (4,16,5):\ V_\ast=0,\lambda_2=0\ \text{cap};\qquad (6,64,9):\ V_\ast=2,\lambda_2=2\ \text{cap}\ (\text{Valid}=0)$$ ✓✓
$$\Longrightarrow\ \lambda=0\ \text{既非 CAP 的充分、亦非必要条件}$$ ⚠️
```

## §6 下一步

```
**(1)** 解释剩余 2 例（`d=23,89`，`\mathrm{ord}_d(2)` 奇）—— 是否有**第二充分判据**（用 `m=(q-1)/d` 对偶？）✓
**(2)** `\lambda>0` 时**大容量**结构（`\lambda=\Theta(d)` 型）✓
**(3)** ⭐ **两群作用合并**：$$\langle\mathrm{Frob}_2,\ T\rangle\ \text{同时作用于}\ I(G)\ (\text{B2 的完整 Frobenius 轨道 }30/30\ +\ \text{本档阶 3})$$ ⟹ 试以该合并作用为透镜给出更细的分类 ✓✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；盲类仍暂放 ✓
【数据】 `out/capmix1B4_Torbit.txt`（39 行，含 `λ, λmod3, fix, orbits, dmod3`）；脚本 `scripts/capmix1B4_Torbit.py` ✓
【边界】 §1–§3 为实测（39 例）；§4 判据为**推导＋手算覆盖**（未逐一机器核验）；§5 边界为**实测反例支撑** ✓

## §附 【技术词回查】（补录）
```
技术词 orbit            命中文件数=95   :: ./grh-goldbach-paper-draft-v2.md ./p39-g1-finite-orbit-moduli.md ./iteration-double-counting-round7.md 
技术词 congruence       命中文件数=33   :: ./B-SERIES-INDEX.md ./E3-why-this-is-not-the-old-pit.md ./SEL1-selection-primitive-audit.md 
```
