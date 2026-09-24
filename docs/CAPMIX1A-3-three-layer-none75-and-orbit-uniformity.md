已查地图：命中（`CAPMIX1A-2-joint-gcd-S0-verdict`）⟹ 执行其 §5 之第⑤步，不开新案
D0: 本档对象 = **`none=75` 三层分离**（共同真根／共同伪根／`(X-1)^k` 重根）＋ **Frobenius 轨道均匀性（零混合）** ＋ **`CAP-MIX-1A` 收口判词** ＋ 一条**廉价改进**（radical 版判据）
D1: 1 （延续新自由度；本档给出机制边界与一条**更强且仍可靠**的判据形式）
[RESEARCH]

# **`CAP-MIX-1A(3)`：`none=75` 三层分离**

## §1 ⭐⭐ 定量结果

```
$$\textbf{STATS（仅 }none=75\text{ 例）}:\quad \text{case1}(g_*=X-1)=0,\quad \boxed{\text{case2 真根}=43},\quad \boxed{\text{case3 伪根墙}=24},\quad \text{case4 重根}=8$$ ✓✓
$$\qquad\text{sum } N_{\rm true}=420,\qquad \text{sum } N_{\rm false}=82,\qquad \text{skipped}=0,\qquad \text{orbit\_all\_out}=95,\qquad \boxed{\text{orbit\_mixed}=\mathbf{0}}$$
**【一致性交叉核验（关键）】**
$$\boxed{\text{cap\_with\_true}=0}\quad\text{且}\quad\boxed{\text{noncap\_no\_true}=0}$$ ✓✓
$$\Longrightarrow\ N_{\rm true}>0\iff\text{实例\textbf{非} cap};\qquad N_{\rm true}=0\iff\text{实例是 cap}$$ ✓✓（**本批\textbf{双向一致}，无例外**）
```

## §2 三层分离（照您的四情形表，实测填数）

```
$$\begin{array}{c|c|c}
\text{情形}&\text{数学含义}&\text{本批}\\
\hline
g_*=X-1&\text{与 }none\ \text{标签矛盾（须查实现）}&0\ \checkmark\\
g_*\ne X-1,\ N_{\rm true}>0&\textbf{实例本身非 cap};\ \text{机制其实找到了真实障碍}&43\\
g_*\ne X-1,\ N_{\rm true}=0,\ N_{\rm false}>0&\boxed{\textbf{共同伪根墙}\ =\ \text{1A 的真正机制边界}}&24\\
g_*=(X-1)^{k}\ (k>1)&\text{仅重根、无伪根}\ \Longrightarrow\ \textbf{可由 radical 版修好}&8\\
\end{array}$$ ✓✓
**【⟹ 判词】** `CAP-MIX-1A` 的机制边界 = **24 例共同伪根墙**；而那 43 例**本非 cap**（`R_*` 里就有真 AP witness）✓✓
```

## §3 ⭐⭐ Frobenius 轨道均匀性（**零混合**）

```
**【实测】** $$\boxed{\text{orbit\_mixed}=0},\qquad \text{orbit\_all\_out}=95$$ ✓✓
$$\Longrightarrow\ \textbf{"是否给出 AP" 在整个 Frobenius 轨道上\textbf{恒定}}:\ \forall x\in\mathcal O(x_0),\ \big(-1-x\in G\big)\ \text{同真同假}$$ ✓✓
**【⟹ 这正是您预判的结构】** $$\boxed{\text{Frobenius-invariant algebraic candidate orbit}\ \not\subset\ \text{AP incidence locus}}$$ ✓✓
**【⟹ 解释力】** **所有 `Q_j` 在检测\textbf{同一个 Frobenius-不变的外部候选结构}**，**不是** AP 关联轨迹：
$$\text{这就是为什么继续增加 }j,k,\ell\ \text{没有用（二阶零收缩、三阶亦无）}$$ ✓✓
```

## §4 结论：`CAP-MIX-1A` 收口

```
$$\boxed{\text{Frobenius-polynomial closure 不能把 cap 条件与一个更大的代数候选轨迹区分开}}$$ ✓✓
$$\boxed{\text{missing datum}\ =\ \text{子群关联约束 }x+1\in-G\ (\text{即 }-1-x\in G)}$$ ✓✓
**【⟹ 明确入口（不再盲试高阶 gcd）】** 下一机制应显式处理**关联约束**：
$$(a)\ \text{把 }-1-x\in G\ \text{写成代数条件并嵌入方程系};\qquad (b)\ \text{或走子群内部二次结构};\qquad (c)\ \text{或用 radical/重数信息（见 §5）}$$ ✓
```

## §5 ⭐ 一条廉价改进（本档提出，可靠且更强）

```
$$I^\ast_{\rm alg}:\ \exists j\ \text{s.t.}\ \mathrm{rad}\big(\gcd(Q_j,X^d-1)\big)=X-1\qquad(\text{即唯一\textbf{相异}根为 }1)$$ ✓✓
**【可靠性】** 若 `Q_j` 在 `G` 上唯一根为 `1`，则任何 AP 都要求 `x\ne1` 且 `Q_j(x)=0` ⟹ 矛盾 ⟹ **cap** ✓✓ **（与 `I_{\rm alg}` 同理由，可靠）**
**【立即收益】** 本批 **8 例 `(X-1)^k`** 可被认证 ⟹ `\mu=1` 计数（同批）由 **3 ⟹ 11** ✓
**【下一步】** 在**全 204 例**上重跑 radical 版，测其覆盖率与是否仍零假阳性 ✓✓
```

## §6 下一步（三件）

```
**(1)** 全批重跑 **radical 版** `I^\ast_{\rm alg}`（零假阳性？覆盖率提升多少？）✓✓
**(2)** 对 24 例伪根墙做**结构刻画**：伪根是否总落在少数固定轨道型（如 `x=-2`、`x^2+x+1=0` 类）⟹ 形成"伪根字典"✓
**(3)** 之后才做 `CAP-MIX-1B`（char 2 四项）✓
【⛔ 纪律】 计算仅本实验；`U_{2,3}` 暂停；`T-1` 仍为 calibration ✓
【数据】 `out/capmix1G_three_layer.txt`；脚本 `scripts/capmix1g_three_layer.py` ✓
【边界】 §1–§3 为本批实测（`none=75`）；`I^\ast` 的可靠性为**同理由推理**，未全批验证 ✓

## §附 【技术词回查】（补录）
```
技术词 radical          命中文件数=14   :: ./B-SERIES-INDEX.md ./C3820B-R0-T-semantic-closure.md ./NOGO-registry-and-screens.md 
技术词 orbit            命中文件数=90   :: ./grh-goldbach-paper-draft-v2.md ./p39-g1-finite-orbit-moduli.md ./iteration-double-counting-round7.md 
```
