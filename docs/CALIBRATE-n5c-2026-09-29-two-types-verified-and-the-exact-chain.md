# CALIBRATE-n5-c（2026-09-29）—— **两类型 $(e_1,e_2)$ 分类\ \textbf{核实}；球交公式纠正；链条闭合**

> **性质**：**结构核验（A-1 主链）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 15:1x ✓
> **唐先生令**：撤销 3-packing 假设，从 $\mathrm{Def}(A)=4$ 重建 ✓

**已查地图**：`CALIBRATE-n6-b`／`CALIBRATE-n5-b`✓

D0: 本档对象 ＝ **档案已有**（球交／multiplicity—皆经典 ✓）
D1: 0（产出＝**一处公式纠正 ＋ 两类型核实 ＋ 链之闭合** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ 你的球交公式要改}:\ |B_1(a)\cap B_1(b)|=\mathbf{2}\ (d\in\{1,2\}),\ \mathbf{0}\ (d\ge3);\ \textbf{非}\ (4,2,0)}$$
$$\boxed{\text{② ⟹ 正确: }P=2(e_1+e_2)\ (\textbf{非}\ 4e_1+2e_2)\ ——\ \text{实测 }0/5760\ \text{违例}✓}$$
$$\boxed{\text{③ ✓✓ 你的"两类型"成立}:\ (e_1,e_2)=(\mathbf{1,1}){:}\ 3840\ \text{个};\ (\mathbf{0,2}){:}\ 1920\ \text{个}\ ——\ \text{无第三类}}$$
$$\boxed{\text{④ ✓ multiplicity 谱\ 只有一种}:\ n_2=\mathbf{4}\ (\forall\ 5760)\ ——\ \text{无三重复盖}}$$
$$\boxed{\text{⑤ ✓✓ 你的两个 canonical form 精确证实};\ |N_1(D)|=22,\ |\Phi^2(A)|=10✓}$$
$$\boxed{\text{⑥ ✓ 全谱}:\ |\Phi^2(A)|\in\{10,11\}\Longrightarrow\mathrm{Def}(\Phi(A))\in\{14,15\}\ge14✓}$$

## §1 ① 球交公式（**✗ 纠正**）

$$\textbf{实测（}Q_5\text{，全部 }d\le3\ \text{之对）}:\ (d,|B\cap B|)\to\text{计数}=(1,2){:}80,\ (2,2){:}160,\ (3,0){:}160$$
$$\therefore\ \boxed{|B_1(a)\cap B_1(b)|=2\ \text{当}\ d\in\{1,2\};\ =0\ \text{当}\ d\ge3}\ ——\ \text{你写 }d{=}1\Rightarrow4\ ✗$$
$$\therefore\ P=\sum_x\tbinom{m(x)}2=\mathbf{2(e_1+e_2)}\quad(\text{实测 }0/5760\ \text{违例}✓✓)$$

## §2 ③ 两类型（**✓✓ 核实**）

| 类型 | $(e_1,e_2)$ | 个数 | 你之预测 |
|---|---|---|---|
| I | $(\mathbf{1,1})$ | $3840$ | ✓ |
| II | $(\mathbf{0,2})$ | $1920$ | ✓ |
| 第三类 | — | $\mathbf{0}$ | ✓ 无 |

$$\text{且 }P=2(e_1+e_2):\ \text{I}\Rightarrow4,\ \text{II}\Rightarrow4✓\ (\text{两者 }P\ \text{相同}=4)$$
$$\text{又 }P=\mathrm{Def}+\sum_x\tbinom{m(x)-1}{2}\Longrightarrow\sum_x\tbinom{m-1}2=0\Longrightarrow\boxed{\mu_A(x)\le2\ \forall x}✓$$
$$\therefore\ \textbf{multiplicity 谱唯一}:\ n_2=4,\ n_j=0\ (j\ge3)\ (\text{实测 }5760/5760)✓$$
$$\text{（你列的 5 种可能里，实际只有 }(4,0,0,0)\ \text{一种发生}✓）$$

## §3 ⑤ 两个 canonical form（**✓✓ 精确证实**）

$$\text{I}:\ A=\{0,1,6,26,29\}\ (\text{即 }00000,10000,00110,11010,11101)$$
$$\qquad D=\{11,12,15,19,20,23\}=\{01011,01100,01111,10011,10100,10111\}\ ✓;\quad |N_1(D)|=22,\ |\Phi^2|=10✓$$
$$\text{II}:\ A=\{0,3,12,21,26\}\ (\text{即 }00000,00011,01100,10101,11010)$$
$$\qquad D=\{6,9,15,22,25,31\}=\{00110,01001,01111,10110,11001,11111\}\ ✓;\quad |N_1(D)|=22,\ |\Phi^2|=10✓$$
$$\therefore\ \text{你给的 }D\ \text{集合\ \textbf{逐字正确}}✓✓$$

## §4 ⑥ 全谱与链条（**✓ 闭合**）

| $(e_1,e_2)$ | $\lvert\Phi^2\rvert=10$ | $=11$ |
|---|---|---|
| $(1,1)$ | $1920$ | $1920$ |
| $(0,2)$ | $960$ | $960$ |
| 合计 | $2880$ | $2880$ |

$$\therefore\ \boxed{|\Phi^2(A)|\in\{10,11\}\ \text{对全部 }5760}\Longrightarrow\mathrm{Def}(\Phi(A))=4+|\Phi^2(A)|\in\{14,15\}\ge\mathbf{14}✓✓$$
$$\textbf{主链（不含 3-packing 假设）}:\ \mathrm{Def}(A){=}4\Rightarrow(e_1,e_2)\in\{(1,1),(0,2)\}\Rightarrow|D|{=}6\Rightarrow|N_1(D)|{\le}22\Rightarrow|\Phi^2|{\ge}10\Rightarrow\mathrm{Def}(\Phi(A)){\ge}14✓$$

## §5 诚实之缺（**✗**）

$$10/11\ \text{之分\ \textbf{不}由}\ (e_1,e_2)\ \text{决定}（两类各半）\Longrightarrow\ \text{精确值需更细不变量}✗$$
$$\text{但对 }K(6,1)\ \text{只需下界 }10\ (=\mathrm{Def}\ge14>9)✓\ \text{—— 已足}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "两类短距离谱" "球交2-2-0" "10与11之分"
技术词 两类短距离谱    命中文件数=0    ::
技术词 球交2-2-0     命中文件数=0    ::
技术词 10与11之分     命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **全量实测（5760 个 $\mathrm{Def}{=}4$ 五集之 $(e_1,e_2)$／multiplicity 谱／$\Phi^2$；球交表；两 canonical form）** ✓；**不占 C 号** ✓
- **撤销** 3-packing 假设 ✓（唐先生纠正成立）；**不主张** $K$ 值有疑 ✗
