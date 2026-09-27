已查地图：已跑 scripts/prework_map_check.sh surfeit ζ 割有效性 反例 ⟹ 执行自 `PHASE2-AUDIT-...-excess-surfeit-independence`（✓）＋ 唐先生 12:15（选 (a) 三关 ✓）；本档 = **surfeit 割有效性：第 2 关失败（显式反例 ✓）**。
D0: 本档对象 = surfeit 候选割 $\zeta\ge0$ 的有效性
D1: 1（新增：**$\zeta$ 的代数展开 $\zeta=\sum_{v\notin C}(2b_2(v)-n-2)$ ✓**；**$\zeta\ge0$ 被反例否证 ✓**）

# surfeit 割有效性审计（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AH-1 第 1 关 代数 ✓)}\ \mathrm{ball}(v)=\sum_{u\in B_1(v)}\delta(u)=2b_2(v)-(n+1)\ \Longrightarrow\ \boxed{\zeta=\sum_{v\notin C}\big(2b_2(v)-n-2\big)}\ ✓\ \text{（}b_2(v)=\#\{c\in C:1\le d(v,c)\le2\}\ ✓\text{）}}$$
$$\qquad\text{核对（本机 ✓）}:\ n=5,6\ \text{各 3 次随机码，全部吻合 ✓✓}$$
$$\boxed{\textbf{(AH-2 第 2 关 有效性 ✗ 失败)}\ \text{候选割 }\zeta\ge0\ \textbf{被显式反例否证} ✗:\ \text{完美 Hamming 码 }(n=7,M=16)\ \Longrightarrow\ \zeta=-112<0\ ✓✓}$$
$$\qquad\text{（本机复算 ✓ }|C|=16\ ✓,\ \delta\equiv0\ ✓,\ \zeta=-112\ ✓\ \text{——与档案 ALIGN 预测逐字一致 ✓）}$$
$$\boxed{\textbf{(AH-3 唯一有效版本 ✓ 但超 LP ✗)}\ \text{由 }\delta\ge0\ \text{仅有平凡有效界}:\ \zeta\ge-\#\{v\notin C\}=-(2^n-M)\ ✓;\ \text{在均匀点 }-930.9091<-905\ \Longrightarrow\ \text{违反 ✓（有切割力 ✓）}}$$
$$\qquad\text{但 }\zeta\ \text{对 }z\ \text{是\textbf{双线性}} \Longrightarrow \textbf{pair-level（二次）} \Longrightarrow \textbf{超出 LP} ✗\ \text{（需 QCQP/SDP ✓）}$$
$$
$$
```

---

## §1 第 1 关：代数展开（**证明 ✓**）

```
$$\zeta:=\sum_{v\notin C}\Big(\underbrace{\sum_{u\in B_1(v)}\delta(u)}_{=:\mathrm{ball}(v)}-1\Big)\ ✓\ \text{（档案 ALIGN L20 ✓，}S=V\ \text{取 }D\ \text{外部分 ✓）}$$
$$\text{展开}:\ \sum_{u\in B_1(v)}\delta(u)=\sum_{u\in B_1(v)}\big(b(u)-1\big)=\Big(\sum_{u\in B_1(v)}b(u)\Big)-(n+1)\ ✓$$
$$\sum_{u\in B_1(v)}b(u)=\#\{(c,u):\ u\in B_1(v),\ u\in B_1(c)\}=\sum_{c\in C}\big|B_1(v)\cap B_1(c)\big|\ ✓;\qquad \big|B_1(\cdot)\cap B_1(\cdot)\big|=\begin{cases}2,&d\le2\\0,&d\ge3\end{cases}\ ✓$$
$$\qquad\text{（}v\notin C\Longrightarrow d(v,c)\ge1\ ✓\text{）}\ \Longrightarrow\ \sum_{u\in B_1(v)}b(u)=2b_2(v)\ \Longrightarrow\ \textbf{AH-1}\ ✓\qquad\square$$
$$\textbf{结论}:\ \zeta\ \text{只含}\ \textbf{pair/局部 incidence}\ \text{项（}b_2(v)\ \text{＝"距离 }\le2\ \text{的码字数" ✓）—— 与档案判断一致 ✓（"surfeit 天然属 pair-level" ✓）}$$
$$
$$
```

---

## §2 第 2 关：有效性失败（**反例 ✓**）

```
$$\text{反例（完美 Hamming ∈ 合法 radius-1 覆盖码类 ✓）}:\ n=7,\ M=K(7,1)=16\ ✓\ \text{（}2^7/8=16\ ✓\text{）};\ \delta\equiv0\ ✓\ \text{（完美覆盖 ⟹ }b\equiv1\ ✓）$$
$$\Longrightarrow\ \mathrm{ball}(v)=0\ \forall v\ \Longrightarrow\ \mathrm{ball}(v)-1=-1\ \Longrightarrow\ \zeta=-\#\{v\notin C\}=-(128-16)=-112<0\ ✗\ \text{（本机复算 ✓✓）}$$
$$\Longrightarrow\ \textbf{候选割 }\zeta\ge0\ \textbf{在合法覆盖码类上为假} ✗\ \Longrightarrow\ \text{不可加入 LP} ✗\ \Longrightarrow\ \text{按唐先生：}\textbf{维持 M-2A′ BLOCKED} ✓$$
$$\textbf{唯一有效版本}:\ \zeta\ge-\#\{v\notin C\}\ ✓\ \text{（由 }\delta\ge0\Longrightarrow\mathrm{ball}\ge0\ ✓\ \text{，两行 ✓）};\ \text{它无排除力于完美码（取等 ✓）}$$
$$
$$
```

---

## §3 第 3 关：是否值得做（**结论：不入 LP ✓**）

```
$$\text{唐先生判据 ✓}:\ \text{"第 2 关不过 ⟹ 直接维持 M-2A′ BLOCKED"}\ ✓ \Longrightarrow\ \textbf{第 3 关不做} ✓\ \text{（不堆 cut ✓）}$$
$$\text{附带精确读数（本档 ✓）}:\ \text{唯一有效版本在 }z\text{-均匀点}\ \zeta=-\tfrac{10}{11}1024=-930.9091\ \text{vs 有效界 }-(1024-119)=-905\ ✓$$
$$\qquad\Longrightarrow\ \text{均匀点\textbf{违反}有效界（} -930.91<-905\ ✓\text{）}\ \Longrightarrow\ \text{该界\textbf{有切割力} ✓ —— 但它是\textbf{二次}约束（dual 到 pair-level ✓）⟹ \textbf{LP 装不下} ✗}$$
$$
$$
```

---

## §4 结论与解封条件（**诚实 ＋ 精确 ✓**）

```
$$\boxed{\textbf{状态}:\ \textbf{M-2A′ 维持 BLOCKED} ✓;\ \text{但闭环\textbf{更锋利}：}\zeta\ge0\ \text{被判\textbf{显式反例否证} ✗（此前仅记"有效性未证" ⚠️）}}$$
$$\boxed{\textbf{解封条件（精确 ✓）}:\ \text{需要\textbf{非 LP 的 pair-level（二次/QCQP/SDP）工具}:\ \text{既对全部覆盖码有效 ✓、又在均匀点有切割力 ✓ 的 }\zeta\ \text{型约束}}$$
$$\qquad\text{注 ✓}:\ \text{平凡有效版 }(\zeta\ge-(2^n-M)\ ✓)\ \text{已具切割力 ✓ ⟹ 若能\textbf{二次化入解}，它就是一个真正的候选机制 ✓（价值高于 }\zeta\ge0\ ✗）$$
$$\text{已关闭（不再走 ✓）}:\ \zeta\ge0\ \text{作为线性/割平面} ✗;\ \text{excess 矩路线（换皮 ✓）} ✗$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§2 为**证明 ＋ 反例 ＋ 本机复算** ✓；§3–§4 为**判据执行 ＋ 精确解封条件** ✓
- **未**加入任何新 LP 约束 ✓（遵唐先生 ✓）；**未**登记"机制找到" ✗；**未**改动 119 UNKNOWN ✓
- 本档把档案 M-2A′ 的"有效性未证 ✗"**升级为"被反例否证 ✗"** ✓（更强 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\zeta$ 代数展开、$\zeta\ge0$ 的反例否证、二次解封条件
- **档案已有（引用，不列为提出）**：$\zeta$、$\delta$、球交叠常数、M-2A′、Haas、均匀点


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 反例否证     命中文件数=9    :: ./PHASE2-AUDIT-2026-09-27-surfeit-validity-refuted.md ./C3899j-M3alpha-paper-attack-G0-G1-G2-verdict-GGAP.md ./C380-S1-FREEZE.md 
技术词 二次解封条件 命中文件数=1    :: ./PHASE2-AUDIT-2026-09-27-surfeit-validity-refuted.md
```
- **本档新增**：$\zeta$ 代数展开、$\zeta\ge0$ 的反例否证、二次解封条件（见上方命中数；0 命中者为自造语／内部标签 ✓）
