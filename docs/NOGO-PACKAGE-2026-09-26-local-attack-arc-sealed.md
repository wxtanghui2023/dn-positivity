已查地图：已跑 scripts/prework_map_check.sh local ledger gadget private point ball disjointness Z ⟹ 本档为**正式 NO-GO 包**（唐先生 2026-09-26 14:23 裁定 ✓）；未跑 solver ✓。
D0: 本档对象 = 局部攻击弧（midpoint/propagation/ladder/Ψ₂/Ψ_mid/gadget/私有点/Z）的正式封存与资产/淘汰清点
D1: 1（新增：**NO-GO 包**；**机制三要件判据** ✓✓；三项保留资产 ✓；区间 18 ≤ Z ≤ 44 ✓）

# NOGO-PACKAGE-2026-09-26 · 局部攻击弧封存

## §0 裁定（唐先生 ✓）

```
$$\boxed{\text{所有只看单个 }B_1(x)\text{、gadget、private point、球不交的机制都不够}}\ ✓✓$$
$$\text{理由}: Z\text{-gadget 局部可\textbf{完全模拟} perfect-code 的零 excess 结构}\ ✓\ \Longrightarrow\ \text{任何局部 lemma 无法区分 }E=0\ \text{与 }E>0\ ✗✓$$
$$\text{处置}: \text{本支\textbf{暂停}（非废弃 ✓）};\ \text{square／Z-gadget／private-point／ball-disjointness 全部保留为\textbf{未来机制的检测器}}\ ✓$$
```

## §1 保留资产（可复用 ✓）

```
$$\textbf{A1 零过量球结构引理}: t_x=0\ \Longrightarrow\ \text{① }B_1(x)\ \text{全 }b=1\ ✓;\ \text{② 恰一个距离-1 码字}\ ✓;\ \text{③ 其余 }n-1\ \text{坐标的\textbf{完美匹配}}\ ✓✓\ (\text{数值 }270/270\ ✓)$$
$$\textbf{A2 桥的重写}: Q_2=\frac{(n-1)E-\sum_{x\notin C}\mathrm{OC}(B_1(x))}{2}\ ✓✓\ (\text{全枚举精确验证}\ ✓)$$
$$\qquad\Longrightarrow\ \text{等价形式（}n=9,M=62\text{）}: Q_2=432-\tfrac12\Sigma\mathrm{OC}\ ✓;\ Q_2\le26\iff\Sigma\mathrm{OC}\ge812\iff Z\le44\ ✓$$
$$\textbf{A3 Z 的区间}: \boxed{18\le Z\le44}\ (n=9,M=62)\ ✓\ (\text{下界由 }I2+\text{奇 }n\ \text{的 }\mathrm{OC}\ge2+Q_2\ge0\ ✓)$$
$$\textbf{A4 gadget 刚性}: \text{Z-gadget 的 }(n+1)/2\ \text{个码字两两距离 }3/4\ \Longrightarrow\ \textbf{球两两不交}\ ✓✓\ (\text{数值全 0 违反}\ ✓)$$
$$\textbf{A5 gadget 局部完美}: \text{gadget 对 }E\ \text{贡献恒为 0}\ ✓✓\ (\text{每点恰 1 次 incidence};\ 9/9,\ 112/112\ ✓)$$
$$\textbf{A6 square 资产}: 4S\le Q_2\ ✓✓\ (＋(9,64)\ \text{取等饱和}\ ✓);\ \text{等号分类（面不交、}V=4S=N_{\ge3}\text{、每 hot 点恰 2 邻）}\ ✓$$
$$

## §2 ⭐⭐ **机制三要件判据**（本轮最重要的战略产出 ✓✓）

```
$$\boxed{\text{突破必须同时具备}: \text{① \textbf{global propagation}（跨 }B_1(x)\ \text{的耦合）};\ \text{② \textbf{minimality}};\ \text{③ \textbf{excess sensitivity}（内在用 }E>0\text{）}}\ ✓✓$$
$$\text{依据}: \text{完美码（}E=0,\ Z=112,\ \text{gadget 零 excess}\ ✓)\ \text{同时满足②③的表面形式却使结论平凡成立}\ ✓$$
$$\qquad\Longrightarrow\ \text{任何在 }E=0\ \text{处不退化的机制\textbf{必然错误}}\ ✗;\ \text{任何纯局部机制\textbf{必然被绕开}}\ ✗✓$$
$$\text{搜索空间后果}: \text{不再找"更强的局部不等式"}\ ✗,\ \text{改找"能把不同 }B_1(x)\ \text{耦合起来的全局对象"}\ ✓✓$$
$$

## §3 本支已淘汰清单（NO-GO 表 ✓）

```
$$\begin{array}{c|c|c}
\text{机制} & \text{形式} & \text{否证方式}\\
\hline
\text{local ledger} & \text{单球容量/账本推 }Q\le1 & \text{单位成本}\le33\ll\text{headroom }285\ ✗\\
\Psi_2/Z_2\ (\text{generic 二阶}) & \text{距离-2 点对 }o(x)o(y) & \text{Q=0 组内自变}\ \{24,26\}\ ✗\\
\Psi_{\mathrm{mid}}\ (\text{中点泛函}) & \sum o(m_1)o(m_2) & \text{极值壳被距离分布决定}\ ✗\\
\text{ladder}/\sigma & \text{binary ladder 结构} & \text{共享壳与 }u_\ell/v_\ell\ \text{断言数值证伪}\ ✗\\
\text{private-point 复用} & \text{不可复用私有点} & \text{完美码 reuse}=\mathbf{28}\ ✗✗\\
\text{ball-disjointness 计数} & \text{球不交推 }Z\ \text{上界} & \text{完美码 }Z=112\ \text{而结论平凡}\ ✗\\
\text{gadget 外溢强制 excess} & \text{外溢}\Rightarrow b\ge2 & \text{完美码外部 }b\ge2=0\ ✗✓\\
\end{array}$$
$$

## §4 保留下来的**检测器**用法（未来机制接入时 ✓）

```
$$\text{新机制候选 }M\ \text{进入时，先跑四条检测（全为必要条件，便宜 ✓）}:$$
$$\quad\text{① 在 perfect code 上是否退化到平凡？（不退化 ⟹ 立即毙}\ ✗)$$
$$\quad\text{② 是否只用单个 }B_1(x)\ \text{的信息？（是 ⟹ 毙}\ ✗)$$
$$\quad\text{③ 是否内在使用 }E>0?\ (\text{否 ⟹ 毙}\ ✗)$$
$$\quad\text{④ 在 }(5,7)\ \text{与 }(6,12)\ \text{上是否给出比真值更弱的界？}\ ✓$$
$$

## §5 状态

```
$$\textbf{桥}: \text{主桥（}M=K\Rightarrow A_{\le2}\text{）\textbf{仍未打通}}\ ✗;\ \text{本支\textbf{暂停}（非废弃 ✓）}$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓\ (\text{未被本支触及}\ ✗)$$
$$\textbf{下一入口}: \text{必须满足§2三要件；候选尚未出现}\ ⚠️$$
$$

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：机制三要件判据、检测器四问、局部攻击弧、NO-GO 包
- **档案已有（引用，不列为提出）**：local ledger、私有点、完美码、球不交、gadget
