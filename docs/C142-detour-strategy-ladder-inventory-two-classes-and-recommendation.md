已查地图（**先查后写**）：`E4-ENGINE-1`（引擎自足化：四条路线与确切堵点）、`E4-ENGINE-2`（初等覆盖引理；`M=1` 自足 ＋ 常数改善）、`E4-ENGINE-3`（衰减松弛移除可比性；残余＝Montgomery RP）、`E4-ENGINE-4`（`(RP_M)` 三工具 ＋ 数值 ＋ **诚实开放状态**）、`E4-ENGINE-5`（二阶矩族对 `M≳12` **可证不足**）、`E4-STATUS-AUDIT`、`C-124`（固定无零区域：**不与 RH 等价**）、`C-125`／`C-126`（尺度感知机制／尺度墙）、`C-111`（端点半阶分支）、`W6`（support>1）、`papers/brown-thm2-classical`（§7 honest gaps）、`papers/palojarvi-constant`（§3 `m\ge2` 可比性缺口）。关键词回查：`阶梯清单`=0、`路径外`=0、`迂回战略`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:12）**：**「RH 目前没有特别好的直接攻击办法，我们需要迂回攻击：先找相对难度没那么高的引理／猜想做证明，然后逼近 RH」**
**结论（先行）**：$$\textbf{(一)}\ \text{该战略}\ \textbf{档案已在跑}：\text{`E4-ENGINE-1`…`5`}\ \text{即完整样板}✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{阶梯分两类}：\textbf{甲类（路径上）}＝\text{RH 的弱推论（证明即朝 RH 推进）};\ \textbf{乙类（路径外）}＝\text{我方成果的技术补全}✓✓$$
$$\textbf{(三)}\ \text{读数}：\textbf{乙类可靠产定理};\ \textbf{甲类 9+ 次收敛到同一墙}（\text{support}>1／一致有限性界）✓✓$$
$$\textbf{(四)}\ ⭐\ \textbf{唯一例外}：\textbf{固定无零区域}\ \exists\delta>0\ ——\ \text{严格弱于 RH、有名字、}\textbf{不与 RH 等价}（\text{`C-124`}）✓✓$$
$$\textbf{(五)}\ \text{推荐双轨}：\text{乙类取最便宜真定理}\ \textbf{`(RP_M), M\le11` 完整证明};\ \text{甲类单点押}\ \textbf{固定无零区域}✓✓$$

FREEZE-ACK: 本档即冻结期内的战略清单与难度／价值评估（依 `§8.1`；不产候选结论）

D0: 本档对象 = **迂回战略的阶梯清单（甲／乙两类）＋ 难度／价值表 ＋ 双轨推荐** —— 关系 = 战略清单与评估，非新机制
D1: 0

# C-142 · **迂回战略：阶梯清单（两类 ＋ 难度／价值 ＋ 推荐）**

> **唐先生 2026-09-19 12:12**：先证相对低难度的引理／猜想，再逼近 RH ✓

---

## §1 档案样板：`E4-ENGINE` 线（**该战略已在跑**）

$$\text{`ENGINE-1`}：\text{目标引理（Palojärvi p.6 Lemma 2.2 ＝ Montgomery Ch.5 Thm 11）}：\max_{1\le n\le5M}\mathrm{Re}\sum_j z_j^n\ \ge\ \tfrac1{20}\ ✓$$
$$\qquad \text{四条路线}\ ＋\ \text{确切堵点}✓$$
$$\text{`ENGINE-2`}：\text{初等覆盖引理（}M=1\ \text{自足}＋\text{常数改善 10×}）\ \textbf{已成}✓✓$$
$$\text{`ENGINE-3`}：\text{衰减松弛移除可比性};\ \text{残余}＝\text{Montgomery RP}✓$$
$$\text{`ENGINE-4`}：\text{目标}\ (\text{RP}_M):\ |z_j|=1\Longrightarrow\exists k\le5M:\ \sum_j\mathrm{Re}\,z_j^k\ge\tfrac12;$$
$$\qquad \text{数值成立且}\ \tfrac12\ \text{饱和};\ \text{三工具（Fejér 恒等式＋非负权平均／尺度伸缩／鸽笼）};\ \textbf{未闭合}✓$$
$$\qquad ⚠️\ \text{逐字}：\text{"(RP}_M\text{) 的证明对 E4 结论}\ \textbf{并非必需}（\tfrac1{20}\ \text{已足够）}\Longrightarrow\ \textbf{数学上漂亮、工程上非必需}"✓✓$$
$$\text{`ENGINE-5`}：\text{二阶矩族对}\ M\gtrsim12\ \textbf{可证不足}（\text{损失}\ M^2\log K）;\ M\le11\ \text{数值成立＋二阶矩路线}\ \textbf{可证}（\text{未写出完整证明}）✓✓$$

## §2 ⭐ 两类阶梯（本档核心区分）

### 甲类（**路径上**：RH 的弱推论；证明即朝 RH 推进）

$$\begin{array}{c|c|c|c|c}
\text{靶子} & \text{性质} & \text{现状} & \text{难度} & \text{价值}\\\hline
\boxed{\text{固定无零区域}\ \exists\delta>0} & \textbf{严格弱于 RH};\ \textbf{不与 RH 等价}（\text{`C-124`}） & \text{未知};\ \text{机制皆尺度感知}（\text{`C-125`}） & \text{高} & \textbf{极大}\\
\Lambda\ \text{上界下降} & \text{极限}＝\text{RH};\ \text{端点半阶分支}（\text{`C-111`}） & 0.22\to0.1788\ (\text{外部}) & \text{中／级} & \text{每级可发}\\
\text{support}>1／\text{无条件三阶矩} & \text{`W6` 原子墙} & \text{仅 support}\le1 & \text{极高} & \text{越 0.6818 天花板}\\
\text{临界线占比／单零点} & \text{上限 0.6818} & 67.2\% & \text{高} & \text{每 % 一篇}\\
\end{array}$$

### 乙类（**路径外**：我方成果的技术补全）

$$\begin{array}{c|c|c|c}
\text{靶子} & \text{现状} & \text{难度} & \text{价值}\\\hline
\boxed{(\text{RP}_M),\ M\le11\ \text{完整证明}} & \text{二阶矩路线}\ \textbf{已"可证"}，\text{只差写全} & \textbf{低–中}\ ⭐ & \text{自足化论文}\\
(\text{RP}_M),\ \text{全体}\ M & M\gtrsim12\ \text{二阶矩族不足} & \text{高} & \text{完全免 Montgomery}\\
\text{Brown Lemma 5 两常数项} & \text{论文B §7 honest gaps} & \text{中} & \text{论文B 升级为完整}\\
\text{Conjecture 3.2.7 第二条} & \text{本次才在措辞中点明};\ \text{未涉及} & \text{中–高} & \text{Droll 修复的另一半}\\
\text{Palojärvi}\ m\ge2 & \text{需可比性假设}\ \sum_jD_j>M(M-1)/2 & \text{中} & \text{Thm 4.1 全}\ m\ \text{自足}\\
\text{论文A Li 范围扩展／}\tau\in[1,2) & \text{线性范围}\ 2T-O(1)\ \text{已证} & \text{中} & \text{范围推进可发表}\\
\end{array}$$

## §3 推荐（**双轨**）

$$\text{乙类首选}：\boxed{(\text{RP}_M),\ M\le11\ \text{的完整证明}} \—— \text{最便宜的}\ \textbf{真定理}：\text{路线已"可证"，只差写全}✓✓$$
$$\text{乙类次选}：\text{Palojärvi}\ m\ge2（\text{可比性假设}）／\text{Brown 两常数项}✓$$
$$\text{甲类单点}：\boxed{\text{固定无零区域}\ \exists\delta>0} \—— \text{唯一"}\textbf{严格弱于 RH 且不被天花板封}\text{"的靶子}✓✓$$
$$\qquad ⚠️\ \text{诚实预估}：\text{甲类过去 9+ 次收敛到同一墙};\ \text{固定无零区域是}\ \textbf{唯一} \text{`C-124` 已证"不与 RH 等价"的甲类靶子}✓$$

## §4 边界与回查

- ⚠️ §1 全为档案**逐字／近逐字**（`E4-ENGINE` 五档）✓
- ⚠️ §2／§3 的难度评级为**本档判断**（非定理）；"甲类 9+ 次收敛"为**经验归纳**（依 `C-116` 不得升级为否决）✓
- ⚠️ **不声称** 甲类不可解；**不声称** 乙类必成 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:1x）`[纪律]`（先跑后写）

```
技术词 阶梯清单   命中文件数=0 ::  ⟹ 本档新增
技术词 路径外    命中文件数=0 ::  ⟹ 本档新增
技术词 迂回战略   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
