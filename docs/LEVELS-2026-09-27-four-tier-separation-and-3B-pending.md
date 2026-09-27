已查地图：已跑 scripts/prework_map_check.sh 复现 计算验证 数学证明 层级 ⟹ 执行自 `P2-2-...-LEVEL3-...` ✓＋ 唐先生 11:34（层级纠正 ✓）；本档 = **四层级彻底分离 ＋ Level 3 状态更正** ✓。
D0: 本档对象 = 已获成果的**性质分级**（复现／计算／证明／新结果）
D1: 0（产出为分级更正与状态重标 ✓）

# LEVELS-2026-09-27 · 四层级分离（唐先生 11:34 纠正 ✓）

## §0 更正（先给）

```
$$\boxed{\textbf{(OO-1 措辞更正)}\ \text{此前写"Level 3 等价性验证通过"\ \textbf{不当}}\ ✗\ \text{——应严格分为 \textbf{3A 计算等价（✓ 已做）} 与 \textbf{3B 数学等价（⏳ 未做）}}$$
$$\boxed{\textbf{(OO-2 四层级）}\ \text{① 文献复现}\ ✓\ |\ \text{② 计算验证}\ ✓\ |\ \text{③ 数学证明}\ ⏳\ \textbf{未完成}\ ✗\ |\ \text{④ 新数学结果}\ \textbf{未开始}\ ✗}$$
$$\boxed{\textbf{(OO-3 资产性质）}\ \text{当前 }A\text{-SDP-HARNESS-1 的性质 =}\textbf{ 复现／验证 harness}\ ✓\ \text{——\textbf{不是}已证的数学资产}\ ✗\ \text{（除非 3B 完成或结构被\textbf{使用}产生新结果 ✓）}}$$
$$
$$
```

---

## §1 四层级现状表（诚实 ✓）

```
$$\begin{array}{c|c|c|l}
\text{层级} & \text{状态} & \text{证据} & \text{性质}\\
\hline
\text{① 文献建模复现} & ✓ & \text{Thm 2.5／4.9 逐字转录；作者代码 }\texttt{numberOrbit}/\texttt{beta}/\lambda/\text{objective 逐项一致} & \text{reproduction}\\
\text{② 计算验证} & ✓ & n=6:\mathbf{11.5980553}\ \text{vs }11.5980;\ n=7:\mathbf{16.0000000}\ \text{vs }15.9999 & \text{numerical}\\
\text{③ 数学证明} & \boxed{⏳} & \textbf{缺}\ ✗ & \text{proof}\\
\text{④ 新数学结果} & \boxed{✗} & \textbf{未开始} & \text{new math}\\
\end{array}$$
$$\text{② 的支撑还包括 3A 特征值审计（}n=4,6,7\ \text{随机实例，偏差 }10^{-13}\sim10^{-15}\ ✓\text{）；}\ \text{③ 的缺口见 §3 ✓}$$
$$
$$
```

---

## §2 Level 3A（计算等价 ✓，已完成）＝ 做了什么

```
$$\text{① orbit basis 正确（}M^t_{i,j}\ \text{的轨道识别 }\mathrm{sort}(d,|u|,|v|)\ \text{与作者 }\texttt{numberOrbit}\ \text{一致 ✓）}$$
$$\text{② 重数 }m_k=\binom{n}{k}-\binom{n}{k-1}\ \text{正确 ✓（维度自检 }\sum_k m_k(n-2k+1)=2^n\ ✓\text{）}$$
$$\text{③ 归一同构因子 }\binom{n-2k}{i-k}^{-1/2}\binom{n-2k}{j-k}^{-1/2}\ \text{正确 ✓（PSD 不受对角正缩放影响，但\textbf{特征值}受影响 ✓）}$$
$$\text{④ }\beta^t_{i,j,k}\ \text{与论文公式／作者代码一致 ✓}\quad\text{⑤ }n=4,6,7\ \text{特征值并集吻合（}10^{-13}\sim10^{-15}\ ✓\text{）}$$
$$\Longrightarrow\ \text{这是\textbf{程序实现与预期块分解一致}的强证据 ✓ —— \textbf{不等于}对一切 }n\ \text{的 PSD 等价定理}\ ✗$$
$$
$$
```

---

## §3 Level 3B（数学等价 ⏳）＝ 需要补的证明链

```
$$\text{(1)}\ M^t_{i,j}\ \text{构成相应 invariant algebra（}\mathcal A_{2,n}\text{）的\textbf{基}}\ \text{——需证线性无关＋张成 ✓}$$
$$\text{(2)}\ \text{Terwilliger algebra 的分解（}\mathcal A_{2,n}\ \text{作为 }C^*\text{-代数 的不可约分解 ✓）}$$
$$\text{(3)}\ \text{每个 irreducible／isotypic component 的\textbf{重数 }m_k\ \text{及其来源}}\ ✓$$
$$\text{(4)}\ \widetilde B_k\ \text{的系数 }\beta^t_{i,j,k}\ \text{来自\textbf{相应表示}}\ \text{（而非数值拟合 ✓）}$$
$$\text{(5)}\ \text{归一化 }\binom{n-2k}{i-k}^{-\frac12}\binom{n-2k}{j-k}^{-\frac12}\ \text{的\textbf{来源}（显式基向量 }U_k\ \text{的范数 ✓）}$$
$$\text{(6)}\ \Longrightarrow\ M\succeq0\iff \widetilde B_k\succeq0\ \forall k\ \text{——\textbf{对一切 }n\ \text{成立}}$$
$$\text{现状}:\ \text{该链在论文中以 \cite{Sch05}（Schrijver）+ }\S3\ \text{给出 ✓ —— 我们要的是}\textbf{自足推导或逐环独立核对} ⚠️$$
$$
$$
```

---

## §4 路线（按唐先生 ✓）

```
$$\boxed{\text{Level 3A（复现）✓}\ \longrightarrow\ \text{Level 3B（独立证明）⏳}\ \longrightarrow\ \text{Level 4（}n=10\text{）}}$$
$$\text{并且强调}:\ \text{Level 3B 完成前，}\textbf{不得}把"reduced SDP 已验证"写成"已证明 formulation 等价" ✗$$
$$\text{研究贡献候选定位}:\ \text{不声称 Terwilliger 分解是新技术（已知工具 ✓）；贡献候选应来自\textbf{用它产生}新的 theorem／bound／construction／certificate ✓}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§2 的状态依本会话实际计算 ✓；§3 的六项为**待做证明链** ✓
- **未**主张任何数学等价定理已成立 ✗；§3 未完成 ⟹ ③⏳
- ⚠️ 附：R2（块式 SDP 数值比对）本轮**因 bmat 拼装错误失败** ✗（形状不符 ✓），修法已明 ✓ —— 属 ② 范畴 ✓，不改变 §1 分级 ✓
- **未**排除 119 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：四层级分离、3A/3B 拆分
- **档案已有（引用，不列为提出）**：Terwilliger、Schrijver Thm、$m_k$、归一因子、$\beta^t_{i,j,k}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 四层级分离  命中文件数=1    :: ./LEVELS-2026-09-27-four-tier-separation-and-3B-pending.md 
技术词 3B 待做        命中文件数=0    ::
```
- **本档新增**：四层级分离、3A/3B 拆分（见上方命中数；0 命中者为自造语／内部标签 ✓）
