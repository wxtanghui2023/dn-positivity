已查地图：已跑 scripts/prework_map_check.sh Boolean fiber 逐点平方 三阶不变量 distance-2 pair ⟹ 执行自 `GAPGLOBAL-2026-09-26`（格≠Boolean ✓）＋ `PREIMAGE2`（局部已闭 ✓）＋ `WHYPER／T3SPLIT`（T₃ 分析已做 ✓）；本档为**Boolean fiber 第一刀**（唐先生 2026-09-26 22:52 令 ✓）；含全枚举核验 ✓。
D0: 本档对象 = Boolean fiber 的逐点结构、$P(x)$ 与三阶不变量
D1: 1（新增：**逐点平方恒等式的公开化解剖（含一处修正）** ✓；**三阶不变量 $\sum_xP(x)^2$ 不被二阶数据决定（带证人）** ✓✓）

# FIBER-2026-09-26 · Boolean fiber 与三阶不变量

## §0 结论（先给）

```
$$\boxed{\textbf{(Z-1 核验)}\ \text{唐先生全部计数恒等式}\ \text{✓}\ \text{（}\Sigma_x\binom{b(x)}2=2(N_1+N_2)\ ⟹\ N_1+N_2=143\ ✓;\ \Sigma_{x\notin C}b(x)=1190-2N_1\ ✓;\ d_2+2d_3=285-2N_1\ ✓;\ \text{Case A/B}\ ✓\text{）}}$$
$$\boxed{\textbf{(Z-2 修正)}\ \text{逐点平方恒等式}\ b(x)^2=f(x)+3S(x)+2P(x)\ \textbf{仅对 }x\in C\ \text{成立}\ ✓;\ x\notin C\ \text{时为 }f+1\cdot S+2P\ ✓\ \text{（}\because 2f(x)+1\ ✓\text{）}}$$
$$\boxed{\textbf{(Z-3 剖析)}\ P(x)=\tbinom{S(x)}2\ \text{为\textbf{定义性}};\ \text{其求和恰回到 }2N_2\ \text{与 }N_1+N_2=143\ ✗\ \text{（＝唐先生警告的"二阶重复"）}}$$
$$\boxed{\textbf{(Z-4 新对象)}\ \sum_xP(x)^2\ \textbf{不被 }(\text{profile},N_1,N_2)\ \text{决定}\ ✓✓\ \text{（n=4 全枚举证人：同组内 }10\ \text{vs}\ 22\ ✓\text{）}}$$
$$
$$
```

---

## §1 (Z-1) 唐先生恒等式：全部核验通过 ✓（n=4 全枚举 5140 个合法 f ✓）

```
$$\checkmark\ \sum_x\binom{b(x)}2=2N_1+2N_2\ \Longrightarrow\ \boxed{N_1+N_2=143}\ ✓\ (\text{与既有 }A_1+A_2=143\ \text{一致 ✓})$$
$$\checkmark\ \sum_{x\notin C}b(x)=1190-2N_1\ ✓;\qquad \checkmark\ d_2+2d_3=285-2N_1\ ✓\ \text{（Case A: }d_2=285-2N_1;\ \text{Case B: }283-2N_1\ ✓\text{）}$$
$$\checkmark\ \deg_C(c)\le2\ \forall c\in C\ ✓;\quad \#\{c:\deg_C=2\}\le1\ ✓\ \text{（＝"匹配＋至多一条 2-边"结构 ✓，与既有匹配定理一致 ✓）}$$
$$
$$
```

---

## §2 (Z-2) 一处修正（逐点平方恒等式 ✓）

```
$$\text{唐稿}:\ b(x)^2=f(x)+3S(x)+2P(x)\quad\✗\ \text{（隐含 }2f(x)+1=3\text{ ⟺ }f(x)=1\ ✗）$$
$$\textbf{正确（对一切 }x\ ✓\text{）}:\quad \boxed{b(x)^2=f(x)+\bigl(2f(x)+1\bigr)S(x)+2P(x)}\ ✓\quad\Bigl(S(x):=\sum_{y\sim x}f(y),\ P(x):=\sum_{y<z\sim x}f(y)f(z)\Bigr)$$
$$\qquad\text{即}:\ x\in C\ \text{时 }b^2=f+3S+2P\ ✓;\quad x\notin C\ \text{时 }b^2=S+2P\ ✓$$
$$
$$
```

---

## §3 (Z-3) 剖析：为何该恒等式本身**不含新信息** ✗

```
$$\text{由 }b=f+S\ ⇒\ b^2=f+2fS+S^2=f+2fS+S+2P\ ✓\ \text{——与 §2 相同 ⟹ \textbf{恒等式} ✓}$$
$$\qquad\text{进一步}:S^2=S+2P\ \Longleftrightarrow\ P=\tbinom S2\ ✓\ \text{（\textbf{定义性} ✓，无独立内容 ✗）}$$
$$\text{求和}:\ \sum_xP(x)=2N_2\ ✓\ (\text{每个距离-2 码对被其 2 个中点各计一次 ✓});\quad \sum_x\tbinom{S(x)}2=d_2+a_3+3d_3\ ✓$$
$$\qquad\Longrightarrow\ d_2+a_3+3d_3=2N_2\ \Longrightarrow\ (\text{代入 §1})\ N_1+N_2=143\ ✓\ \text{——\textbf{正是唐先生警告的"二阶重复"}}\ ✗✓$$
$$
$$
```

---

## §4 (Z-4) ⭐ 新对象：三阶量 $\sum_xP(x)^2$ 不被二阶数据决定 ✓✓

```
$$\textbf{测试（n=4 全枚举 ✓）}:\ \text{按 }(\text{profile},N_1,N_2)\ \text{分组，检查 }\sum_xP(x)^2\ \text{是否为组内常量}$$
$$\qquad\text{结果：25 组，其中 \textbf{1 组取多值} ✓：}\quad (\text{profile},N_1,N_2)=\bigl((6,6,4),\ 4,\ 5\bigr)\ \Longrightarrow\ \sum_xP^2\in\{\mathbf{10},\ \mathbf{22}\}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{存在\textbf{真正新的三阶 Boolean 不变量}（= 逐点"共同邻居码对"计数的二阶矩}\ ✓\text{）}}$$
$$\qquad\text{即}:\ \text{二阶数据 }(\text{profile},N_1,N_2)\ \text{**不能**固定 }\sum_xP(x)^2\ ✓\ \text{——\textbf{独立于既有不变量组}}\ ✓$$
$$
$$
```

---

## §5 四门判定与下一步（诚实 ✓）

```
$$\textbf{四门}:\\ N\ \text{（新颖）}\ ✓\ (\text{§4 证人});\quad I\ \text{（独立）}\ ✓\ (\text{非 }(\text{profile},N_1,N_2)\ \text{的函数});\quad \text{敏感}\ ✓;\quad \textbf{方向}\ \textbf{待定}\ ⚠️$$
$$\qquad\text{当前 }\sum_xP^2\ \text{在组内\textbf{自由变化}} ⟹ \text{尚\textbf{未}构成约束} ✗\ \text{（独立}\ne\text{有用，此教训已立 ✓）}$$
$$\textbf{下一步（本刀正经出口 ✓）}:\ \text{找 }\sum_xP(x)^2\ \text{的\textbf{约束源} —— 候选：}\ |\mathcal T|=1\ (\Sigma\binom b3=1\ ✓)\ \text{／ }T_3\ \text{窗口}\ [38,\tfrac{10}3A_2]\ ✓\ \text{／ }P(x)\in\{0,1,3\}\ \text{的量子化}\ ✓$$
$$\qquad\text{若找到"约束 }\sum P^2\ \text{且与 }(N_1,N_2)\ \text{耦合"的命题 ⟹ 首次真正三阶耦合 ✓✓};\ \text{若仍自由 ⟹ 记为第 }\textbf{三阶自由量} ✗$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1 为 **n=4 全枚举核验** ✓（5140 个合法 f ✓，恒等式全部成立 ✓）
- §3 的"定义性"判定为**本档推导** ✓（$P=\binom S2$ 恒等 ✓）
- §4 的证人在 **n=4** 上；**n=10 情形未测** ⚠️（不得外推 ✗）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张 $\sum P^2$ 有用 ✗（只主张其独立 ✓）
- 本轮未跑 SAT/CP-SAT ✓（仅全枚举小立方 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 三阶不变量  命中文件数=1    :: ./FIBER-2026-09-26-boolean-fiber-and-the-third-order-invariant.md 
技术词 共同邻居码对计数 命中文件数=0    ::
```
- **本档新增**：逐点平方恒等式的修正形式、三阶不变量 $\sum_xP(x)^2$（见上方命中数；0 命中者为自造语 ✓）
- **档案已有（引用，不列为提出）**：匹配定理、$\Sigma\binom b2$ 恒等式、$N_1+N_2=143$、$|\mathcal T|=1$、$T_3$ 窗口、Boolean fiber 接口

> ⚠️ **本档 (Z-4) 已被撤回**：见 `docs/TRIP-2026-09-27-unique-triple-point-and-the-withdrawal-of-z4.md` ✓（唯一 triple 类中 $\sum P^2$ 被 $(|C|,N_1,d_3)$ 完全钉死 ⟹ 非独立量 ✗）
