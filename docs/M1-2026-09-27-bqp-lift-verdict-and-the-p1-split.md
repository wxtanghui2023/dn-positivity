已查地图：已跑 scripts/prework_map_check.sh BQP 提升 support 可见性 ⟹ 执行自 `FRONTIER-R2-2026-09-27`（M-1 线索 ✓）＋ 唐先生 2026-09-27 09:35 ✓；本档为**核验 ＋ 循环判定 ＋ P1 拆分**。
D0: 本档对象 = BQP 提升机制与 119 的 P1-A／P1-B 拆分
D1: 1（新增：**M-1 循环判定** ✓；**P1-A／P1-B 拆分** ✓✓）

# M1-2026-09-27 · BQP 提升的核验与循环判定

## §0 核验结果（结论成立 ✓，但证明有一处错 ✗）

```
$$\text{唐稿论证}:\ f\ \text{非 Boolean}\Rightarrow\exists u: f(u)\ge2;\ \text{再取 }v\ne u\ \text{with}\ f(v)\ge1\ \Longrightarrow\ y_{uv}=f(u)f(v)>f(v)=x_v\ \Longrightarrow\ \text{违反 }y_{uv}\le x_v\ ✓$$
$$\textbf{核验}:\ \text{结论\textbf{成立}}\ ✓\ \text{（前提须修正 ✓）}$$
$$\qquad⚠️\ \textbf{证明步骤有错}:\ \text{"}\Sigma f\ge2\Longrightarrow\exists v\ne u:f(v)\ge1\text{"}\ \textbf{为假}\ ✗\ \text{（反例 }f=2e_u,\Sigma f=2,\text{其余全 }0\ ✓\text{）}$$
$$\qquad\textbf{正确前提}:\ \textbf{覆盖条件 }b\ge1\ ✓\ \text{才能给出 }\exists v\ ✓\ \text{（证: 若 }f(v)=0\ \forall v\ne u\ \Longrightarrow\ f=f(u)e_u\ \Longrightarrow\ b(x)=f(u)\mathbf 1[d(x,u)\le1]\ \Longrightarrow\ d(x,u)\ge2\ \text{处 }b=0\ \text{✗ 矛盾 ✓）}$$
$$
$$
```

---

## §1 ⚠️ 但该机制是**循环**的（AMEND-35 要害 ✓）

```
$$\text{精确提升下 }y_{uv}=x_ux_v\ \Longrightarrow\ y_{uv}\le x_v\ \Longleftrightarrow\ x_v(x_u-1)\le0\ \Longleftrightarrow\ \boxed{x_u\le1}\ (\text{当 }x_v\ge1\ ✓)$$
$$\Longrightarrow\ \text{该"机制"\textbf{等价于直接加约束 }x_u\le1}\ \Longrightarrow\ \text{即 Booleanity 的\textbf{同义改写}}\ ✗$$
$$\qquad\textbf{与本档上轮预警同型}\ ✓:\ \text{"其分离性 cut 可能只是 }f_i\le1\ \text{的改写}\ \Longrightarrow\ \textbf{循环}\ ✗\text{"（已被证实 ✓✓）}$$
$$\Longrightarrow\ \text{按 AMEND-35 \textbf{意图}（要求\textbf{非循环}的 support 可见性 ✓），M-1 \textbf{不构成新机制}}\ ✗$$
$$\qquad\textbf{注}:\ \text{唐稿已自行标注"针对\textbf{精确} integer lifted point"}\ ✓;\ \text{BQP \textbf{松弛}中 }y\ne x\otimes x\ \Longrightarrow\ \text{松弛\textbf{不}捕获 Booleanity}\ ✗\ \text{——该边界正确}\ ✓$$
$$
$$
```

---

## §2 ✅ 但 P1-A／P1-B 拆分是**真收获**（保留 ✓✓）

```
$$\textbf{P1-A（Booleanity）}:\ \textbf{不再是障碍}\ ✓\ \text{——它只是 0/1 条件，可由\textbf{平凡线性约束 }x\le1\ \text{表达}\ ✓}$$
$$\qquad\Longrightarrow\ \text{"Booleanity gap" 是\textbf{红鲱鱼}}\ ✗\ \text{（本项目此前围绕它转了多轮 ✓）};\ \text{正式关闭该子问题}\ ✓$$
$$\textbf{P1-B（实数内容）}:\ \boxed{f\in\{0,1\}^{1024},\ Af\ge1\ \Longrightarrow\ \Sigma f\ge120?}\ ✓\ \text{——即 }K(10,1)\ge120\ \text{的经典核心}\ ✓$$
$$\qquad\Longrightarrow\ \textbf{归位}:\ 119\ \text{的真障碍＝}\textbf{规模下界}\ ✓;\ \text{与 Booleanity／提升\textbf{无关}}\ ✓✓$$
$$
$$
```

---

## §3 后续（改判优先级 ✓）

```
$$\textbf{M-1b（仅 cube-edge 对变量是否足够？）}:\ \text{真问题}\ ✓;\ \textbf{本档判断}:\ \textbf{不足}\ ✗\ \text{（所需的 }v\ \text{未必与 }u\ \text{相邻}\ ✓;\ \text{且全对提升本身已循环}\ ✗\text{）——待实测 ✓}$$
$$\textbf{M-2（Klapper 型 refined weight／multicovering 不等式）}:\ \textbf{真正的下一刀}\ ✓✓\ \text{（唯一可能触及 }|C|=119\ \text{的地方}\ ✓）$$
$$\textbf{交叉线注记（\textbf{不混写}}\ ✓\text{）}:\ \text{RH 的 support ceiling}\ \text{vs 119 的 moment}\not\Rightarrow\text{support};\ \text{抽象共同问题＝}\ \boxed{\text{何时必须升级变量空间，才能使 support 成为可证明信息}}\ ✓$$
$$
$$
```

---

## §4 边界（诚实标注）

- §0–§1 为**核验 ＋ 判定** ✓（前提修正已写明 ✓）；§2 为**结构性拆分** ✓（本档主要收获 ✓）
- M-1 判定为**机制级** ✓（"不构成新机制"✓），**非**"提升无用" ✗
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张 M-1b 必负 ✗（待实测 ✓）
- 后台：修正版 $D_0$ 测试（`p2fix.py`）在跑 ✓（前次结果因标签含 $f$ 而**无效** ✗，已标注 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 M-1 循环判定 命中文件数=1    :: ./M1-2026-09-27-bqp-lift-verdict-and-the-p1-split.md 
技术词 P1-A/P1-B 拆分 命中文件数=1    :: ./M1-2026-09-27-bqp-lift-verdict-and-the-p1-split.md
```
- **本档新增**：M-1 循环判定、P1-A/P1-B 拆分（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：BQP 提升、$y_{uv}\le x_v$、SUPPORT-VISIBILITY GATE、RH support ceiling


---

## §5 ⚠️ 状态更正：M-1 = **KILL**（唐先生 09:38 裁定 ✓）＋ P1-A 永久关闭 ✓

```
$$\textbf{AMEND-35 记账更正}:\ \text{M-1 记为}\ \boxed{\textbf{KILL}}\ ✗\ \text{（此前记为 PASS ✗，更正 ✓）}——\text{理由：其"分离"等价于 }f_u\le1\ \text{的改写 ⟹ 循环 ✓}$$
$$\boxed{\textbf{P1-A 永久关闭}}\ ✓:\ \text{此后\textbf{禁止}再把 Booleanity 作为独立研究问题引入}\ ✗\ \text{（防再走 }f\to f^2\to f\otimes f\to f\le1\ \text{一轮 ✓）}$$
$$\text{故 119 的问题形态被\textbf{锁定}为}:\quad C\subseteq\mathbb F_2^{10},\ \forall x:\ |B_1(x)\cap C|\ge1,\ |C|\le119?\ \Longleftrightarrow\ \boxed{K(10,1)\ge120?}\ ✓$$
```
