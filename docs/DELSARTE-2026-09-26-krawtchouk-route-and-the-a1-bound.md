已查地图：已跑 scripts/prework_map_check.sh K(10,1) Delsarte Krawtchouk A_1 triple-overlap ⟹ 执行自 `docs/GAPTHEOREM-2026-09-26-K101-119-independent-input-gap.md`（缺口＝支撑型 ✓）＋ `docs/L2AUDIT-...md`（SDP 格值 ✓）；本档为**唐先生 2026-09-26 21:20 指定的一刀**（三阶唯一性 ＆ Krawtchouk 耦合 ✓）；**含 LP 计算**（3 法 ＋ 直测 ＋ 对照 ✓）。
D0: 本档对象 = $Q=1$ 下的三阶量 $\sum_x\binom{b(x)}3$ 与距离分布 Krawtchouk 矩（既有对象）
D1: 1（**新增一条独立参数界 $A_1\le49$** —— 本日首个二阶来源的新界 ✓）

# DELSARTE-2026-09-26 · Krawtchouk 路线审计与 $A_1$ 新界

## §0 结论（先给）

```
$$\boxed{\textbf{(S-1 确认＋加严)}\ \sum_x\binom{b(x)}3=1\ ✓;\ \text{且}\ \big|\bigcap_{c\in T}B_1(c)\big|\le1\ \Longrightarrow\ \sum_x\binom{b(x)}3=|\mathcal T|\ \textbf{精确相等}}\ ✓✓$$
$$\boxed{\textbf{(S-2 退化)}\ \sum_x\binom{b(x)}3=1\ \Longleftrightarrow\ \text{profile}\ (740,283,1)\ \Longrightarrow\ \textbf{不含超出 }Q=1\text{ 假设的新信息}}\ ✗$$
$$\boxed{\textbf{(S-3 正面)}\ \text{二阶路线\textbf{非空转}}:\ \text{Delsarte＋本项目}\ Q=1\ \text{恒等式}\ \Longrightarrow\ \mathbf{A_1\le49}\ ✓✓\ （\text{强于匹配定理的 59}\ ✓）}$$
$$\boxed{\textbf{(S-4 判定)}\ \text{但\textbf{未闭合}缺口}\ ✗:\ \text{无矛盾};\ \text{十族仍窗口不敏感}\ ⚠️\ \Longrightarrow\ \text{产出＝收紧参数窗，非 P1}}$$
$$
$$
```

---

## §1 (S-1) 三阶量的精确形式（本档加严 ✓）

```
$$\text{"同一点被 }k\text{ 个球覆盖"}\ b(x)=|C\cap B_1(x)|\ ✓;\quad \sum_x\binom{b(x)}3=\#\{(x,T):|T|=3,\ T\subseteq B_1(x)\}\ ✓$$
$$\textbf{关键引理}:\ \text{若}\ x\ne y\ \text{且}\ d(x,y)\in\{1,2\}:\ |B_1(x)\cap B_1(y)|=\mathbf 2\ ✓;\ d\ge3:\ 0\ ✓$$
$$\qquad\Longrightarrow\ \text{三点}\ T\ \text{若有两个共同点}\ x\ne y\ \Longrightarrow\ T\subseteq B_1(x)\cap B_1(y)\（\textbf{2 元集}）\ ✗\ \text{矛盾}\ \Longrightarrow\ \boxed{\big|\bigcap_{c\in T}B_1(c)\big|\le1}\ ✓✓$$
$$\qquad\Longrightarrow\ \sum_x\binom{b(x)}3=|\mathcal T|:=\#\{T\subset C,\ |T|=3:\ \exists x,\ T\subseteq B_1(x)\}\ \textbf{（精确，无多重度）}\ ✓✓$$
$$\textbf{数值核验（本档 ✓）}:\ n=10\ \text{随机}\ 10{,}647\ \text{个}\ d\in\{1,2\}\ \text{的点对}\ \Longrightarrow\ |B_1\cap B_1|>2\ \text{次数}\ \mathbf 0\ ✓✓$$
$$
$$
```

---

## §2 (S-2) 与 profile 等价（故非独立输入 ✗）

```
$$\text{设}\ n_k=\#\{x:b(x)=k\}\ ✓;\quad \sum_x b(x)=|C|\cdot11=1309\ ✓,\ \sum_x1=1024\ \Longrightarrow\ \sum_k(k-1)n_k=\mathbf{285}\ ✓$$
$$\sum_x\binom{b(x)}3=1\ \Longrightarrow\ \text{至多一个点}\ b\ge3\ \text{且}\ b=3\（b\ge4\Rightarrow\binom43=4>1\ ✗）\ \Longrightarrow\ n_3=1\ ✓$$
$$\qquad\Longrightarrow\ n_2+2n_3=285\Rightarrow n_2=283,\ n_1=740\ \text{（profile ✓）};\qquad \text{反向：profile}\Rightarrow\sum\binom b3=\binom33=1\ ✓$$
$$\Longrightarrow\ \boxed{\text{二者\textbf{等价}}}\ \Longrightarrow\ Q=1\ \text{假设的\textbf{改写}} \Longrightarrow\ \textbf{不构成新攻击面}\ ✗✓$$
$$
$$
```

---

## §3 (S-3) 二阶路线的正面产出：$A_1\le49$ ✓✓

```
$$\textbf{二阶系统（\textbf{全部对假设的 119-覆盖有效} ✓）}:\ a_0=1,\ a_j:=\frac{\#\text{有序对}(d=j)}{|C|}\ ⟹ \sum_j a_j=|C|=119\ ✓$$
$$\qquad\text{Delsarte}:\ M_r:=\sum_{j=0}^{10}a_jK_r(j)\ \ge0\quad(r=0..10)\ ✓\ \text{（本档在 200 个随机 }n=6\ \text{码上复核全成立 ✓）}$$
$$\qquad\text{本项目 }Q=1\ \text{恒等式}:\ 2A_1+2A_2=\sum_x\binom{b(x)}2=283+3=286\ ⟹ \mathbf{a_1+a_2=\tfrac{286}{119}}\ ✓$$
$$\textbf{LP 结果（3 法一致 ✓）}:\ \max a_1=0.825236\ ⟹ \boxed{A_1\le\frac{119}{2}\times0.825236=49.102}\ ✓✓\quad(\text{最优解 Delsarte 取等}\ \min_rM_r=0\ ✓)$$
$$\textbf{独立直测}:\ a_1\ge0.8255\ \text{不可行}\ ✗;\ a_1\ge0.8252\ \text{可行}\ ✓\ \Longrightarrow\ \text{与 LP 一致}\ ✓✓$$
$$\textbf{对照（决定性 ✓）}:\ \text{去掉}\ a_1+a_2\ \text{约束后}\ \max a_1=7.2154\（A_1\le429\）\ ✗\ \Longrightarrow\ \text{该界＝\textbf{Delsarte × Q=1 恒等式}的联合产物}\ ✓✓$$
$$\textbf{推论}:\ A_2\ge94\ ✓\（\text{原 }83/84\ ✓）;\quad \#\{\text{孤立码字}\}=119-2A_1\ge\mathbf{21}\ ✓\（\text{原 }\ge1\ ✓）$$
$$\textbf{与已知构造无冲突（旁证 ✓）}:\ 120\ \text{码}\ A_1=50>49\ \text{不矛盾}\ ——\ \text{其 }M=120\ne119\ \text{且非 }Q=1\ \Longrightarrow\ \text{约束不适用}\ ✓$$
$$
$$
```

---

## §4 (S-4) 但未闭合缺口（诚实 ✓）

```
$$\textbf{十族重查}:\ A_1\le49\ \text{只移动窗口，不产生新约束类型};\ \text{已试支撑入口仍}\ O(1)\ \text{强制点}\ ✗$$
$$\qquad\text{例}:p:=\sum_c\binom{d_2(c)}2\ \le A_2\ ✓\ \text{且} p\ge\tfrac{(2A_2)^2}{2\cdot119}-\tfrac{119}2\ \text{(Kim–Vu)}\ ✓;\ A_2\ge94\Rightarrow p\ge32.5\ \le\ 94\ ✗\ \text{无矛盾}$$
$$\Longrightarrow\ \textbf{缺口形态不变}（\text{支撑型}）\ ✗;\ \text{但参数窗由}\ A_1\le59\ \text{收紧到}\ A_1\le49\ ✓$$
$$
$$
```

---

## §5 边界与建议

- §1 引理为**纯组合证明** ＋ 10,647 样本核验 ✓；§2 等价为**双向推导** ✓；§3 为 **LP 计算**（scipy highs 三法 ✓ ＋ 直测 ✓ ＋ 对照 ✓）
- ⚠️ **本档一处自查失误**：二分脚本用 `hi=mid` 加界检验（对一切 mid 均可行 ✗）⟹ 该支结果作废 ✗，已弃用；结论以**直测法**与三法 LP 为准 ✓
- ⚠️ **Delsarte 归一化**：$a_j$ 为**有序对**比例（$\sum_ja_j=|C|$ ✓）；若改用无序对须除以 2 ✓（本档已统一 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；段内**未**加 Van Wee／球覆盖不等式（见建议 ✓）
- **建议（下一步）**：① 把 **Van Wee / 球覆盖**不等式加入同一 LP（可能继续收紧 $A_1$ ✓）；② 以 $A_1\le49$（→ $A_2\ge94$、孤立码字 $\ge21$）**重跑十族**，看是否出现碰撞 ✓；③ 若仍为窗口效应，则与 GAPTHEOREM 合并封存 ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 三阶量精确形式 命中文件数=1    :: ./DELSARTE-2026-09-26-krawtchouk-route-and-the-a1-bound.md 
技术词 Krawtchouk 路线判定 命中文件数=1    :: ./DELSARTE-2026-09-26-krawtchouk-route-and-the-a1-bound.md 
技术词 A_1 <= 49        命中文件数=0    ::
```
- **本档新增**：三阶量精确形式、Krawtchouk 路线判定（各 1 档 ✓）；`A_1 <= 49` **命中 0** ⚠️（本档写作 $A_1\le49$ 形式 ⟹ 该检索词非档案术语，**不列为新命名** ✓）
- **档案已有（引用，不列为提出）**：匹配定理 $A_1\le59$、profile (740,283,1)、$A_1+A_2=143$、Delsarte 不等式族
