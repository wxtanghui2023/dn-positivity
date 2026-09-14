# E190 · ⭐⭐⭐⭐⭐ **混合方案在窗口层面失败 ✗｜"bootstrap 失败"机制（首个看起来像真障碍的东西 ✓）｜界修正 ✗**
> 依唐先生 2026-09-14 16:39 裁定 ✓（**E189 死 ✓；E190 目标改为"消灭 persistent-dead 是否必然消耗无限多个低素数 residue class"✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ ✓；未跑 Lean ✓；数值＝精确整数枚举（P=3 累积 B 正确版 ✓）

---

## §0 ⚠️ 界修正（✗ 用户 §5 的 $\le p^2-2$ 应改为 $\le p^2-1$）

$$\text{禁类集 }R_p(A)=\{0\}\cup(-A\bmod p^2)\ ✓;\quad B\neq\varnothing\Longrightarrow R_p(A)\neq\mathbb Z/p^2\ ✓\Longrightarrow |A\bmod p^2|\le p^2-1\ ✓$$
$$\qquad\text{（}0\in A\Longrightarrow 0\in-A\bmod p^2\Longrightarrow R_p=-A\bmod p^2\ ✓\ \text{故并集不"多占"一类 ✓）}\qquad\text{且被漏的类可取 }-1\ ✓（A+1\subseteq S\ ✓）$$
$$\Longrightarrow\ \boxed{p=2:\ |A\bmod4|\le3}\ ✓\quad\text{—— 且【可达】✓（E181 §2 构型 (III)：}A\bmod4=\{0,1,2\}\ ✓）\ \Longrightarrow\ \textbf{用户的"}\le2\text{"【不成立 ✗】}$$
$$\qquad\text{（}p=3:\ \le8\ ✓;\ \text{一般 }p:\ \le p^2-1\ ✓\ \text{—— 仍足以支撑"residue 容量有限"这一论点 ✓）}$$

## §1 ⭐ residue 消耗机制：**不按原样触发 ✗**（两个干净事实 ✓）

$$\textbf{事实 A ✓}：\text{单元素可对【所有】}p\ \text{非-free ✓}：c=1\ \Longrightarrow\ 1\not\equiv0\bmod p^2\ \forall p\ ✓\ \Longrightarrow\ \text{"每素数都要非-free"} \text{ 由 }O(1)\ \text{个元素满足 ✓}$$
$$\textbf{事实 B ✓}：\text{对固定 }(a_0,p)\ \text{的 dead 类（}n\equiv-a_0\bmod p^2\ ✓\text{），穿透只需 }c\not\equiv0\bmod p^2\ ✓\ \text{且 }c\not\equiv n+a\bmod p^2\ \forall a\in A\ ✓$$
$$\qquad\text{而后者的禁集}=\{-a_0+a\bmod p^2:a\in A\}\ \text{大小}\le p^2-1\ ✓\ \Longrightarrow\ \text{可用类至少 1 个 ✓}\ \Longrightarrow\ \textbf{每素数新增 residue 消耗 }O(1)\ ✓$$
$$\Longrightarrow\ \boxed{\text{"无限 residue 消耗"机制本身【不】被迫发生 ✗}}\ ✓\ \text{—— 真正的代价仍是 sieve 伤害（E185/E186/E187 的老量 ✓）}$$

## §2 ⭐⭐⭐ 数值（$P=3$，累积 $B$ 正确版 ✓）：**非-free 元素造新 dead 的速度 > 杀 dead 的速度 ✗**

$$Q=36,\ A_0=\{0,1,4,8\}\ ✓:\quad |B|=247\ ✓,\ \textbf{dead}=162\ ✓\qquad\text{（dead 在 mod 4 占 3 类：}1{:}16,2{:}6,3{:}140\ ✓；\text{mod 9 占 8 类 ✓）}$$
```
 步  加 c    吃掉 dead   剩余 dead    |A|   |B|      备注
 1    49      82         92           5    229      c=49=7² 便宜 ✓
 2    89      40         69           6    209      c=89 便宜 ✓
 3    18      19        248 ✗         7     96 ✗    c=18=2·3²：p=3 免费 ✓ 但 p=2 非-free ⟹ B 砍半 ✗✓
 4    46      63        209 ✗         8     86 ✗
 6    74      26        218 ✗        10     67 ✗
 9    13      24        205 ✗        13     53 ✗
12    20      29        305 ✗        16     32 ✗    B 从 247 崩到 32 ✗
```
$$\Longrightarrow\ \boxed{\textbf{hybrid 方案在窗口层面【失败 ✗】}}\ ✓：\text{第 3 步起 }|B|\ \text{崩塌 ⟹ 被 }B\ \text{覆盖的旧 }n\ \text{反而失去覆盖 ⟹ dead 总数【上升 ✗】}$$
$$\qquad\textbf{与 E189 定理合起来的清晰图景 ✓✓}：\underbrace{\text{free 元素【不能】碰 dead}}_{\text{E189 定理 ✓}}\quad+\quad\underbrace{\text{非-free 元素【能】碰 dead，但会造出新 dead}}_{\text{本步数值 ✓}}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{"bootstrap 失败"机制 ✓✓}}\ \text{—— 目前【唯一】看起来像真障碍的东西 ✓}$$

## §3 与 E187 的关系（✓ 不矛盾 ✓ 需说明 ✓）

$$\text{E187 的 }\rho_X^*>1\ ✓\ \text{说的是"【覆盖窗口】可行"（优化目标＝覆盖 }S\cap[1,X]\ ✓\text{，允许大 free 元素 ✓）}$$
$$\text{本轮说的是"【修补 dead】不可行"（优化目标＝消灭 dead 集 ✓，只许加非-free ✓）}$$
$$\Longrightarrow\ \text{两者优化目标不同 ⟹ 不矛盾 ✓；且合起来说明：}\boxed{\text{能覆盖窗口的元素【恰好】是碰不到 dead 的那些 ✗}}$$

## §4 判词与 (E191) 建议（✓）

$$\boxed{\text{residue 消耗机制：不触发 ✗（§1 ✓）；hybrid 方案：窗口层面失败 ✗（§2 ✓）；bootstrap 失败＝首个"真障碍候选" ✓}}$$
```
(E191) 把 bootstrap 失败【定量化】✓ —— 这是现在唯一值得打的方向 ✓
   定义单步净收益 ✓：加 c 后 Δ(dead) = (吃掉的 dead) − (因 |B| 收缩而新增的 dead) ✓
   第一目标（尖锐二分 ✓）：是否恒有 Δ(dead) ≥ 0 ✗（即"修补无净收益"✓）？
      若成立 ⟹ 得到真正的【层间障碍定理 ✓】（比 E186/E189 都强 ✓）
      若不成立 ⟹ 存在正净收益元素族 ⟹ 构造路线重新打开 ✓
   注意 ✓：P=3 数据里已有两个净收益为正的步骤（c=49: −70 ✓；c=89: −23 ✓）⟹
      "Δ≥0 恒成立"很可能【为假 ✗】⟹ 需改问"净收益能否持续/累积"✓
```

## §5 边界与一句话（✓）

```
✅ 界修正 ✓（p²−1；p=2 时 ≤3 ✓ 且构型 (III) 达到 ✓）；residue 机制不触发 ✓（事实 A/B ✓）
✅ 数值 ✓（P=3 累积 B 正确版 ✓）：hybrid 失败 ✗；bootstrap 失败机制 ✓（B 崩 ⟹ dead 升 ✓）
⚠️ 仅 P=3 单尺度 ✓；贪心非最优 ✗；未测 P=5 ✓
⚠️ 仍不声称构造存在 ✗、不声称不可能 ✗
⭐ 净产出 ✓：① 界修正 ✓；② residue 机制排除 ✓；③ ⭐ **bootstrap 失败机制（首个真障碍候选 ✓）**；④ E191 的尖锐二分 ✓
```
$$\boxed{\text{residue 消耗不触发 ✗ ⟹ 老量（sieve 伤害）仍是唯一货币 ✓；P=3 数值显示非-free 修补【净负】✗ ⟹ "bootstrap 失败"机制 ✓；下一枪 (E191)：Δ(dead) 的净收益能否持续为正 ✗}$$
