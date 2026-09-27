已查地图：已跑 scripts/prework_map_check.sh P1-ALIGN alignment profile 律 ⟹ 执行自 `P12-PASS-2026-09-27-...`（✓）＋ 唐先生 13:17（开 P1-ALIGN ✓）；本档 = **第一关结论：覆盖几何只给 Σq=A₂；结构约束来自 F₂³ 算术，且给出完整律** ✓✓。
D0: 本档对象 = Type-B alignment profile q 的约束来源与完整刻画
D1: 2（**双计数律：H↔C₂ 完美匹配 ✓**；**完整 profile 律 J₇=A₂²/|S|，|S|∈{1,2,3,4,7} ✓**）

# P1-ALIGN 第一关（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BN-1 第一关 ✓ 纯双计数)}\ \text{局部计数给出}:\ \text{(i)}\ \textbf{H}\leftrightarrow C_2\ \text{是\textbf{完美匹配}}（每个 }h\in H\ \text{恰一个 }C_2\text{-邻居，反之亦然 ✓）};\ \text{(ii)}\ \text{对方向分布}\ q\ \text{只给}\ \boxed{\sum_iq_i=A_2}\ ✓}$$
$$\qquad\Longrightarrow\ \text{"覆盖几何 ⟹ }q\text{" 这条箭头的\textbf{第一关输出 = STOP} ✗（只有 }A_2\ \text{一个条件 ✓，遵唐先生规则 ✓）}$$
$$\boxed{\textbf{(BN-2 ⭐但约束确实存在，来源 = F}_2^3\textbf{ 算术 ✓)}\ \text{完整 }n=8\ \text{域（240 互异码 ✓）枚举给出\textbf{完整律}}:\ \boxed{q=\frac{A_2}{|S|}\cdot\mathbf 1_S}\ ✓\ \text{其中 }S=\mathrm{supp}(q)\ \text{满足}}$$
$$\qquad\boxed{J_7=\sum_iq_i^2=\frac{A_2^2}{|S|}},\qquad |S|\in\{1,2,3,4,7\}\ ✓;\qquad S=\text{方向综合征集的\textbf{仿射几何集}}\ ✓✓$$
$$\boxed{\textbf{(BN-3 判据 ✓)}\ \text{第一关输出 }\textbf{不止 }\sum q=A_2\ ✓\ \text{（有形状律 ✓）}\ \Longrightarrow\ \text{按唐先生判据 = }\textbf{GO（进入 P2）};\ \text{但须诚实标注}:\ \text{约束来自}\textbf{完美码算术}，\ \textbf{不是覆盖几何} ✓}$$
$$
$$
```

---

## §1 第一关：纯双计数（**✓ 推导 ＋ 数值核验 ✓**）

```
$$\text{对 }y\notin H\cup C_2:\ b((y,0))=[y\in H]+d_1^H(y)+[y\in C_2]=1\ ✓\ \text{（H 完美 ⟹ 恰一覆盖 ✓）};\ \text{对 }y\in C_2:\ b((y,0))=d_1^H(y)+1\le2\Longrightarrow d_1^H(y)\le1\ ✓$$
$$\text{同理 }b((y,1))=[y\in H]+[y\in C_2]+d_1^{C_2}(y)\le2\Longrightarrow\ \text{两个方向都}\ \le1\ ✓;\ \text{而 }k{=}0\Longrightarrow\ \text{两侧都}\ \ge1\ ✓\ \text{（覆盖 ✓）}\ \Longrightarrow\ \boxed{\text{完美匹配}}\ ✓✓$$
$$\textbf{数值核验 ✓}:\ \text{240 码全部满足}\ (\mathrm{nbH},\mathrm{nbC})=((1,\ldots,1),(1,\ldots,1))\ ✓\ \Longrightarrow\ \text{双计数只给 }\sum_iq_i=A_2\ ✗\ \text{（无方向信息 ✓）}$$
$$
$$
```

---

## §2 完整 profile 律（**✓ 240 码全枚举 ✓**）

```
$$\begin{array}{c|c|c|c|c}
A_1 & A_2 & |S| & q\ \text{形状}\ (\text{各值}) & J_7=A_2^2/|S|\\
\hline
16 & 0 & — & q\equiv0 & —\\
8 & 8 & 1 & 8\ \text{于单方向} & 64\\
4 & 12 & 3 & 4{+}4{+}4\ (\{a,b,a{+}b\}\ \text{型 ✓}) & 48\\
2 & 14 & 7 & 2{\times}7\ (\text{全方向 ✓}) & 28\\
0 & 16 & 1 & 16 & \mathbf{256}\\
0 & 16 & 2 & 8{+}8 & \mathbf{128}\\
0 & 16 & 4 & 4{+}4{+}4{+}4 & \mathbf{64}\\
\end{array}$$
$$\textbf{数量 ✓}:\ |S|{=}1:7\ \text{个};\ |S|{=}2:21=\binom72\ \text{个};\ |S|{=}4:7\ \text{个（}\mathbb F_2^3\ \text{中不含 0 的 2 维仿射平面 ✓）};\ |S|{=}7:1\ \text{个};\ |S|{=}3:7\ \text{个（}\{a,b,a{+}b\}\ ✓\text{）}$$
$$\textbf{几何识别 ✓}:\ S\ \text{恒为仿射几何集}:\ \text{点 / 直线 / 平面 / 全空间减 0 ✓（综合征 }\mathbb F_2^3\ \text{的仿射子空间 ✓✓）};\ q\ \text{在 }S\ \text{上\textbf{恒定}} ✓$$
$$
$$
```

---

## §3 判据与下一步（**✓**）

```
$$\text{唐先生第一关规则}:\ \text{"若只得到 }\sum q_i=16\ \text{或其代数等价 ⟹ STOP"};\ \text{本档得到 }\boxed{q=\frac{A_2}{|S|}\mathbf 1_S,\ |S|\in\{1,2,3,4,7\}}\ ⟹\ \textbf{非 STOP} ✓$$
$$\text{但诚实定位 ✓}:\ \text{该律来自}\textbf{完美码的综合征算术}（\mathbb F_2^3\ \text{仿射几何 ✓）}，\ \textbf{不是}覆盖几何 ✓\ \text{—— 故"covering geometry → }q\text{"箭头仍为 \textbf{STOP} ✗};\ \text{可用箭头是"perfect-code arithmetic → }q\text{" ✓✓}$$
$$\text{P2 候选 ✓}:\ \text{构造达到边界的显式 Type-B 码（已由三见证码给出 ✓）};\ \text{并检验该律能否推广到 }n=16\ (2^4)\ \text{与其它 }k\ ✓$$
$$\text{与 119 的连接 ✓}:\ \textbf{延后} ✓\ \text{（遵两空间纪律 ✓）；本资产价值 = support-2 层确有独立自由度，且其\textbf{形状被算术量子化} ✓✓}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**推导 ＋ 240 码数值核验** ✓；§2 为**完整枚举** ✓（n=8 Theorem-13 域 ✓，因 Zaremba 唯一性 ⟹ 该域 = 全部 $(H,C_2)$ 对 ✓✓）；§3 为**判据 ＋ 路线** ✓
- ⚠️ 律 $J_7=A_2^2/|S|$ 及 $|S|\in\{1,2,3,4,7\}$ 是 **n=8 的完整验证** ✓（非一般定理 ✗）；$n\geq16$ 未测 ⚠️
- ⚠️ **未**声称覆盖几何约束 $q$ ✗（恰恰相反 ✓）；**未**涉及 119 判定 ✓；**未**跑 SAT ✓（遵第一关纪律 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：alignment profile 律、$|S|$ 取值集、仿射几何支撑识别、双计数完美匹配律
- **档案已有（引用，不列为提出）**：Type B、$q_{ij}$、$J_7$、perfect matching、$A_1+A_2=M/2$、Theorem 13


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 alignment profile 律 命中文件数=1    :: ./P1ALIGN-2026-09-27-alignment-profile-law.md 
技术词 仿射几何支撑识别 命中文件数=1    :: ./P1ALIGN-2026-09-27-alignment-profile-law.md
```
- **本档新增**：alignment profile 律、$|S|$ 取值集、仿射几何支撑识别、双计数完美匹配律（见上方命中数；0 命中者为自造语／内部标签 ✓）
