已查地图：命中（`CAPMIX1A-I-vs-truth-sound-but-incomplete`）⟹ 执行其 §5 之 (1)，不开新案
D0: 本档对象 = **对抗式假阳性搜索**（逻辑反转：先代数 `PASS`，再独立找 AP witness）＋ **`g_j=\gcd(Q_j,X^d-1)` 度数与根结构审计**
D1: 1 （延续 `CAP-MIX-1` 新自由度；本档给出**严格代数版判据**与**其覆盖区极窄**的定量边界）
[RESEARCH]

# **CAP-MIX-1A(1)：假阳性搜索 ＋ gcd 结构**

## §1 执行方式（照您的三区设计，且**逻辑反转**）

```
$$\boxed{I\ \text{先 PASS}\ \Longrightarrow\ \text{独立寻找 AP witness}}$$ ✓✓（非"先枚举 cap 再看 `I`"）
**【严格代数版 `I_{\rm alg}`】** $$I_{\rm alg}=\text{PASS}\iff\exists\ \text{信息型}\ j:\ \gcd\!\big(Q_j(X),\,X^d-1\big)=X-1$$ ✓✓
$$\Longrightarrow\ \textbf{证明级证书}:\ \text{唯一公共根 }x=1\ \text{只能给平凡三元组}\ (1,-2,1)\ \Longrightarrow\ \text{cap}$$ ✓✓
**【同时记录】** 每个信息型 `j` 的 `\deg g_j` 与是否含 `X-1`；并记录 `r_j=p^j\bmod d` **轨道** ✓
**【实现】** 无表元组实现（内存安全，避免 `q^2` 表；前版因 `q=6561` 表格有 OOM 风险已废弃）✓
```

## §2 ⭐ 定量结果（`p\in\{3,5,7,11,13,17,19\}`，`q\le4000`，`d\le1200`）

```
$$\textbf{STATS}:\quad N_{\rm case}=204,\quad N_{\rm cap}=54,\quad \boxed{N_{\rm PASS}=3},\quad \boxed{N_{\rm FP}=0},\quad N_{\rm cert\cdot cap}=3$$ ✓✓
$$\qquad N_{\rm all\text{-}degen}=126,\qquad N_{\rm nontriv\ gcd}=75$$
**【结论一（可靠性）】** $$\boxed{\text{零假阳性}\ (N_{\rm FP}=0)}$$ ✓✓ —— **`I_{\rm alg}` 在 204 例中\textbf{从未误报}**；且 `N_{\rm PASS}=N_{\rm cert\cdot cap}=3` ⟹ **凡 PASS 者皆 cap** ✓✓
**【结论二（覆盖极窄）】** $$\boxed{\text{仅有 }3/54\ \text{个 cap 被 }I_{\rm alg}\ \text{认证}}$$ ✓ —— **严格代数版远不足以覆盖 cap** ⚠️
**【结论三（失败谱系）】** $$N_{\rm all\text{-}degen}=126:\ \text{无信息型 }j\ \text{存在（}\{p^j\bmod d\}\ \text{全为 }p\text{-幂）}\ \textbf{占 62\%}$$ ✓✓
$$\qquad N_{\rm nontriv\ gcd}=75:\ \text{有信息型 }j\ \text{但 }\deg g_j>1$$ ✓
```

## §3 诊断（本档核心判断）

```
**【关键对比】** 表列式弱判据（上一档）`13/83` ⟹ **严格代数判据 `3/204`** ⟹ $$\text{差距} = \big(\text{元素级"其他根不给 AP"}\big)\ \text{vs}\ \big(\text{代数级"唯一公共根是 }1\big)"$$ ✓✓
　**⟹ 两者都可靠，但都不完备；严格版更"漂亮"却更窄** ✓
**【占 62% 的 `all-degen` 才是主障碍】** 当 `\{p^j\bmod d\}` 全落在 `p`-幂轨道内时，**单步 Frobenius 完全无信息** ✓✓
　⟹ **这正好呼应您的第二阶机制假设**：$$\textbf{单步无信息}\ \Longrightarrow\ \textbf{联合投影可能产生信息}$$ ✓✓
```

## §4 下一步（锁死顺序，照您的裁定）

```
**(1)** $$\boxed{\gcd\!\big(Q_{j_1},\dots,Q_{j_m},\,X^d-1\big)}$$ **联合 gcd 机制**（第二阶）：在 `N_{\rm all\text{-}degen}=126` 与 `N_{\rm nontriv\ gcd}=75` 两类上测；若某对 `(j,k)` 的联合 gcd 降到 `X-1` ⟹ **`FAIL_cap` 转化为第二阶机制** ✓✓
**(2)** 若联合版仍不完备 ⟹ 记录**机制边界**（哪些 `(p,n,d)` 类确实需要第三种机制）✓
**(3)** 之后才做 `CAP-MIX-1B`（char 2 四项）✓
【⛔ 纪律】 计算仅本实验（`D` 层）；`U_{2,3}` 暂停；`T-1` 仍为 calibration ✓
【数据】 `out/capmix1E_FP.txt`；脚本 `scripts/capmix1e_FP_notables.py` ✓
【边界】 `I_{\rm alg}` 的可靠性仅**本批 204 例经验**，**未证明**；`N_{\rm FP}=0` ≠ 定理 ✓

## §附 【技术词回查】（补录）
```
技术词 joint gcd        命中文件数=0    :: 
技术词 false positive   命中文件数=0    :: 
```
