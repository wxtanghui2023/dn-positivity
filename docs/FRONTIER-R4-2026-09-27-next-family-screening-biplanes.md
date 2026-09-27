已查地图：已跑 scripts/prework_map_check.sh biplane quasi-symmetric 自正交 λ=2 large set ⟹ 执行自 `PHASE2-2026-09-27`（BLOCKED ✓）＋ 唐先生 10:03 ✓；本档为**机制优先筛选（下一族候选）**，**未动算** ✓。
D0: 本档对象 = 下一族候选 cell 与"能约束存在性"的未饱和机制
D1: 1（新增：**λ=1→λ=2 自正交引擎复活的结构反差** ✓；**biplane 家族通过机制门** ✓）

# FRONTIER-R4-2026-09-27 · 下一族筛选（biplane 线）

## §A 前置：Steiner p-rank lane 正式存档（唐先生 10:03 ✓）

```
$$\boxed{\text{Steiner p-rank lane = }\textbf{BLOCKED}}\ ✗\ \text{—— 表述为"已检查的 rank 引擎未形成 extension-specific 的 P1 障碍"}\ ✓$$
$$\qquad\textbf{不是}\ \text{"}S(3,5,41)\ \text{尚未算出来"}\ ✗;\ \text{故 }\texttt{5f6ada6}\ \text{作为}\textbf{机制否证资产}\ \text{保存}\ ✓\ \text{（不再用 }S(3,5,17)\ \text{救该线}\ ✗）$$
$$\qquad\text{rank 分布实验}\ \textbf{暂缓}\ ✗\ \text{（它回答机制存在性，而非当前 cell 的 P1 ⟹ 易退回"先算再找解释"✓）}$$
$$
$$
```

---

## §B 核心发现：自正交引擎在 λ=1 死、在 λ=2 活（结构反差 ✓✓）

```
$$\text{两块交点数（Steiner vs biplane）}:\quad \lambda=1:\ |A\cap B|\in\{0,1\}\ ✓;\quad \lambda=2\ (\text{biplane}):\ |A\cap B|\in\{0,2\}\ ✓$$
$$\Longrightarrow\ \langle 1_A,1_B\rangle\ \text{mod}\ 2:\quad \lambda=1:\ 1\not\equiv0\ ✗\ \text{（引擎死 ✓）};\quad \lambda=2:\ 2\equiv0\ ✓\ \text{（引擎\textbf{活} ✓✓）}$$
$$\text{再加权偶性 }k\ \text{偶（biplane 阶 }n\ \text{偶}\ ✓\text{）}\ \Longrightarrow\ \textbf{块码自正交}\ (\text{over }\mathbb F_2)\ \Longrightarrow\ \dim C\le v/2\ \text{成立}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{对 biplane，"rank}\Rightarrow\text{上界"引擎\textbf{可用}}\ ✓\ \text{——恰是我们刚对 Steiner 否证的那一条}\ ✓✓}$$
$$
$$
```

---

## §C 候选 family 筛选表（唐先生四列 ✓）

```
$$\begin{array}{c|l|l|l}
\text{对象} & \text{OPEN 命题} & \textbf{USED} & \text{未用／可组合机制}\\
\hline
\textbf{biplane }2\text{-}(v,k,2) & \text{未决阶的存在性} & \text{BRC}\ ✓;\ \text{码/rank 非存在性}\ (\texttt{arXiv:2003.04453}\ \text{三元码，已用于 quasi-symmetric／biplane}\ ✓);\ \text{自同构群}\ ✓ & \text{① 层式 derived／残差一致性};\ \text{② 交数整可实现性};\ \text{③ trade／switching 不变量};\ \text{④ 无自同构情形轨道计数};\ \text{⑤ 三元码在\textbf{未决阶}上的覆盖缺口}\ ⚠️\\
\text{LSTS}(v) & \text{已解决} ✗ & \text{Lu／Teirlinck}\ ✓ & —\ \text{（跳过}\ ✗\text{）}\\
\text{GLS}／\text{large sets of SQS} & \text{部分开放}\ ⚠️ & \text{Lu 型构造}\ ✓ & \text{待查（本轮未定}\ ⚠️\text{）}\\
\text{trade／switching} & — & \text{检索命中噪音}\ ✗ & \text{需换源再查}\ ⚠️
\end{array}$$
$$
$$
```

---

## §D 门判定（唐先生硬门 ✓）

```
$$\textbf{biplane 线}:\ \text{机制}\ \text{②自正交／rank}\ \text{确实}\textbf{约束存在性}\ ✓\ (\dim C\le v/2\ \text{与设计参数相撞即非存在}\ ✓)\ \Longrightarrow\ \textbf{过门（机制层）}\ ✓$$
$$\qquad\textbf{但必须诚实}:\ \text{该机制}\textbf{已被使用}（2003.04453\ ✓\text{）}\ \Longrightarrow\ \text{按唐先生规则：}\textbf{不自动算新机制}\ ✗$$
$$\qquad\Longrightarrow\ \textbf{P1 待定}:\ \text{唯一可能的新性}＝\text{该机制在\textbf{尚未覆盖的未决阶}上是否留缺口}\ ⚠️\ \text{（须先读原文，仍不动算}\ ✓\text{）}$$
$$\text{其余族}:\ \text{LSTS 已解决}\ ✗;\ \text{GLS／LS(SQS) 与 trade 线}\ \textbf{本轮不足以下判}\ ⚠️$$
$$
$$
```

---

## §E 下一步（source-first，仍不动算 ✓）

```
$$\text{① 读 }\texttt{arXiv:2003.04453}\ \text{与其引文，钉死：三元码机制\textbf{覆盖了哪些阶}、\textbf{用什么判据}（}\dim C\ \text{与 }v/2\ \text{的具体碰撞式}\ ✓\text{）}$$
$$\text{② 取得 biplane \textbf{已知阶表}（来源：Key 的 biplane 计算论文 ✓），确定\textbf{真未决阶}集合}\ ✓$$
$$\text{③ 若存在"未决阶 ∧ 码机制留缺口" ⟹ 写可检验 }P1\ \text{不等式}\ ✓\ \Longrightarrow\ \text{才进入第二阶段}\ ✓$$
$$\textbf{禁止}:\ \text{未确认缺口就开算／枚举}\ ✗$$
$$
$$
```

---

## §F 边界（诚实标注）

- §B 为**结构性观察** ✓（mod 2 内积 ✓，初等 ✓）；§C–§D 为**筛选与门判定** ✓
- **不主张** biplane 线必含新 P1 ✗（仅主张：过机制门 ✓，且需查缺口 ✓）
- **未**排除任何未决阶的存在／不存在 ✗；本档**未动算** ✓
- GLS／LS(SQS)／trade 线**未下判** ⚠️（本轮证据不足 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 自正交反差  命中文件数=1    :: ./FRONTIER-R4-2026-09-27-next-family-screening-biplanes.md 
技术词 biplane 机制门 命中文件数=1    :: ./FRONTIER-R4-2026-09-27-next-family-screening-biplanes.md
```
- **本档新增**：λ=1→λ=2 自正交反差、biplane 机制门判定（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：BRC、Kramer–Mesner、DHV、quasi-symmetric、Key biplane 计算
