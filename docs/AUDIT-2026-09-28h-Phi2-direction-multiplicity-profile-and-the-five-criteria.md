# AUDIT-2026-09-28h — **$\Phi_2$ 候选（方向重数剖面）＋ 五条标准逐条判定**

> **性质**：**审计/实验**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:43 ✓
> **唐先生令**：停 coset 层；找**二阶/三阶 interaction representation**；硬早停门＝"若 $\Phi$ 由距离分布决定 ⟹ KILL" ✓

**已查地图**：★**命中** `WITPLANE-2026-09-28`（**方向集 $r(p):=|\{i:p\oplus e_i\in A_1\}|$**，C-450）✓ —— 但那是 **$S$-$I$ 局部版**，与本档之**全局**剖面**不同对象** ✓；另接续 `AUDIT-f/g`／`SUBSPACELP` ✓

D0: 本档对象 ＝ **档案已有**（方向集）＋ **本档新造之全局版**（$\Phi_2$ 定义为本档首提 ✓）
D1: 1（**首次定义\ \textbf{全局}方向重数剖面 $\Phi_2$ ＋ 首次核验 $\sum_x\binom{|A(x)|}2{=}2N_2$ ＋ 首次逐条对照五标准 ✓**）

---

## §1 候选 $\Phi_2$ 之定义（**本档首提 ✓**）

$$A(x):=\{c\in C:\ d(c,x)=1\};\qquad \Phi_2(C):=\big\{|A(x)|\big\}_{x\in\mathbb F_2^{10}}\ \big(\text{multiset}\big)$$

**动机（为何是"三阶耦合载体"✓）**：

$$x\ \text{为距离-2 对 }(c,c')\ \text{之中点}\ \iff\ c,c'\in A(x)\ \text{相异}\ \iff\ c=x{\oplus}e_i,\ c'{=}x{\oplus}e_j\ (i{\ne}j)\ ✓$$
$$\Longrightarrow\ \text{"pair state}\to\text{forced third-order state" 之天然载体}\ ✓\ \text{（唐先生 §4 所求 ✓）}$$

## §2 恒等式核验（**实测 ✓✓**）

$$\boxed{\sum_x\binom{|A(x)|}{2}=2N_2}\qquad\text{（实测三例全部相等：}4572{=}4572,\ 3324{=}3324,\ 554{=}554\ ✓✓\text{）}$$
$$\text{（每距离-2 对有\ \textbf{恰好 2} 个中点 ⟹ 双重计数 ✓）};\qquad \sum_x|A(x)|=10K\ ✓$$

## §3 ⚠️ 距离分布决定性门（**唐先生硬早停门**）——**未决** ⚠️

$$\textbf{实测}:\ \text{8 个随机覆盖码（}K{=}143..498\text{）}\ \Longrightarrow\ \textbf{8 个互异距离分布} \Longrightarrow\ \text{无同分布对可比 ⟹ 门\ \textbf{未决}}\ ⚠️$$

$$\textbf{理论论证（★ 支持"不被决定"✓，但\ \textbf{未证}} ⚠️\textbf{）}:\ \Phi_2\ \text{之更高阶矩涉及\ \textbf{距离-2 三角} 计数：}$$
$$\sum_x\binom{|A(x)|}{3}\ \text{计入\ \textbf{三点两两距 2\ 且共中点}}\ T_{222}\ \text{型量};\quad \text{而距离分布仅给 }N_2\ \text{（对数），\textbf{不含}三角数} ✗$$
$$\therefore\ \Phi_2\ \text{应\ \textbf{严格细于} 距离分布（}\text{因 }T_{222}\ \text{一般不由 }\{N_i\}\ \text{决定）}\ ✓\ \text{——\textbf{待证}} ⚠️$$

## §4 ★ 五条标准逐条判定（**照唐先生 §"最低成功标准" ✓**）

| # | 标准 | 判定 |
|---|---|---|
| 1 | $\neq$ covering identity | ✓（$\Phi_2$ 非 $\delta/\sum\delta$ 之线性重写） |
| 2 | $\neq$ coset-size/full-state reencoding | ✓（不涉 coset 分区） |
| 3 | $\neq$ distance-distribution reencoding | **未决** ⚠️（§3：理论支持"细于"，但未证） |
| 4 | 存在 genuine compatibility/incompatibility | **未测** ✗ |
| 5 | 该 incompatibility 对 $\|C\|{=}118$ 有作用 | **未测** ✗ |

$$\boxed{\text{五条中：2 条 ✓；1 条未决 ⚠️；2 条未测 ✗}}\ \Longrightarrow\ \text{按唐先生"缺一不可" ⟹ \textbf{尚未达标}}\ ⚠️$$

## §5 结论与下一步（**待唐先生定**）

$$\text{本档仅完成}\ \Phi_2\ \text{之\ \textbf{定义 ＋ 一条恒等式 ＋ 门检框架}};\ \text{要件 3/4/5 尚未取得}\ ✗$$
$$\textbf{建议（若继续）}:\ \text{先攻标准 3（证 }\Phi_2\ \text{不被距离分布决定）—— 因它是最廉价且可\ \textbf{早期否决}之要件；}$$
$$\qquad\text{若 3 过，再攻 4（是否有 incompatibility）；\textbf{不可跳步} ✗（遵"缺一不可"✓）}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "方向重数剖面" "三阶耦合载体" "距离分布决定性门"
技术词 方向重数剖面   命中文件数=0    ::
技术词 三阶耦合载体   命中文件数=0    ::
技术词 距离分布决定性门 命中文件数=0    ::
```

**口径**：`方向集`（既有档 `WITPLANE`）与本档之 `方向重数剖面` 为**不同对象**（前者 $S$-$I$ 局部、后者全局）✓

## §7 边界（硬 ✓）

- 有限计算（8 码之恒等式核验）＋ 既有档引证 ✓；**无新数学定理** ✗；**不加 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §3 之"细于距离分布"为**理论论证（未证）**⚠️，已标注；**不主张** $\Phi_2$ 已达五标准 ✗
