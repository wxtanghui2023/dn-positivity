已查地图：命中（`M03-P2iv-general-beta-second-order-rigidity-theorem`）⟹ 抽象引理（`丙`），不开新案
D0: 本档对象 = ⭐**可复用引理**：「迹亏空—冻结对角—二阶反号」（机制链抽象＋**适用条件三件套**＋**已知失效模式**）
D1: 1（首次把一档计算抽象为带明确适用域的引理）
[RESEARCH]

# **引理（`丙`）：「迹亏空—冻结对角—二阶反号」**

## §1 引理陈述

```
$$\textbf{设定}:\ \text{谱-锥系统 }F(x,s)=0,\ F:\mathbb R^9\times\mathbb R\to\mathbb R^5,\ \text{变量 }x\in\mathbb R^9\ \text{受非负锥 }x_j\ge0;\quad \delta:=s-s_0>0,\ \varepsilon:=\sqrt\delta.$$
$$\textbf{假设}:\ (\text{在边界点 }x^{(0)},\delta=0\ \text{处})$$
$$\quad\textbf{(H1) 零坐标锥}:\ \boxed{a^{(0)}=f^{(0)}=0}\ (\text{并对 }a,f\ \text{有非负锥约束});$$
$$\quad\textbf{(H2) 一阶冻结}:\ J:=\partial_xF|_{0}\ \text{满行秩},\ \text{且}\ \boxed{v_i=0,\quad v_a+v_f=0}\ \text{对一切 }v\in\ker J;$$
$$\quad\textbf{(H3) 精确迹恒等式}:\ \boxed{2a+2f+i=c_0-2s}\ (c_0\ \text{常数});$$
$$\quad\textbf{(H4) 二阶谱非负}:\ \text{锥可行切向 }\tau\in\mathcal C\ \text{上，二阶谱可解性}\Longrightarrow\ \boxed{W:=w_a+w_f=-1-\mathcal Q(\tau),\ \ \mathcal Q\ge0\ \text{于}\ \mathcal C}.$$
$$\textbf{结论}:\ \text{不存在 }O(\varepsilon^2)\ \text{尺度（即 }\delta=\varepsilon^2\text{）的锥可行穿透}.$$
```

## §2 证明链（三步，均为恒等式级）

```
$$\text{第1步（冻结 + 锥）}:\ \text{由 (H2) }v_a+v_f=0;\ \text{由 (H1) 锥要求 }v_a,v_f\ge0\Longrightarrow\boxed{v_a=v_f=0};$$
$$\qquad \text{故 }a=\varepsilon^2w_a+O(\varepsilon^3),\ f=\varepsilon^2w_f+O(\varepsilon^3)\ (\varepsilon\ \text{阶不可动}).$$
$$\text{第2步（迹亏空转移）}:\ \text{把上式与 }i=i^{(0)}+\varepsilon^2w_i\ \text{代入 (H3) 的 }\varepsilon^2\ \text{阶}:$$
$$\qquad 2w_a+2w_f+w_i=-2\ \Longrightarrow\ \boxed{W=w_a+w_f=-1-\tfrac12w_i}.$$
$$\text{第3步（二阶反号）}:\ \text{由 (H4) }W=-1-\mathcal Q(\tau)\le-1<0;\ \text{而二阶锥要求 }w_a,w_f\ge0\Longrightarrow W\ge0\ \Longrightarrow\ \textbf{矛盾}.$$
$$\qquad \Longrightarrow\ \boxed{\text{引理成立}};\ \text{证书形式}:\ \boxed{W<0\ \text{与}\ W\ge0\ \text{不相容}}.$$
```

## §3 ⚠️ 适用条件三件套（缺一即失效，**不得泛化**）

```
$$\boxed{\textbf{零坐标锥}\ (H1)\ +\ \textbf{一阶冻结}\ (H2)\ +\ \textbf{二阶谱非负}\ (H4)}$$
$$\quad \text{(H1) 缺} \Longrightarrow \text{一阶就可能已有严格下降方向（无需二阶）};$$
$$\quad \text{(H2) 缺} \Longrightarrow v_a,v_f\ \text{未必被逼零},\ a,f\ \text{可在 }\varepsilon\ \text{阶直接移动};$$
$$\quad \text{(H4) 缺} \Longrightarrow W\ \text{可正，二阶锥可行（本线已出现该情形，见 §4）}.$$
$$\text{另注}:\ \text{(H4) 中的 }\mathcal Q\ \text{只由“迹亏空承担量”决定};\ \text{与本族中被证明\textbf{结构性正交}的核方向（}\tau_2\text{）无关}.$$
```

## §4 已知失效模式（不是"待证"，而是**机制确实失效**）

```
$$\text{在本族（}Z_2\text{-Case II 边界族）中}:\ \mathcal Q=\frac{A\tau_0^2+B\tau_3^2+4W\tau_0\tau_3}{(1-t)(1+3t)},\ A=2\beta+3t-1,\ B=2(t-\beta)$$
$$\quad \boxed{t\ge\tfrac13\Longrightarrow A,B\ge0\ \text{于允许区}\Longrightarrow \mathcal Q\ge0\Longrightarrow \text{引理适用（整族封口）}}$$
$$\quad \boxed{t<\tfrac13,\ \beta>t\Longrightarrow B<0\Longrightarrow \text{取 }\tau_0=0,\tau_3\ \text{大得 }\mathcal Q<0\Longrightarrow W\ge0\Longrightarrow \textbf{引理不适用}}$$
$$\qquad \text{并已存在二阶可行方向证据} \Longrightarrow \text{应标为"}\textbf{当前二阶机制失效}\text{"，}\textbf{而非 OPEN/待证}.$$
```

## §5 可迁移性（预期，不夸大）

```
$$\text{可迁移的形式特征}:\ \text{非负锥上的谱-切问题};\ \text{某对对角元恰在锥顶点};\ \text{迹恒等式给出“亏空承担量”};\ \text{核冻结该对对角的一阶.}$$
$$\text{迁移时须\textbf{逐条}核验 (H1)-(H4)};\ \text{不得因"形式相似"直接套用};\ \text{(H4) 的符号是本引理的真正判据}.$$
【⛔ 纪律】 本档为**抽象与边界声明**（零新计算）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 引理为**充分条件型**；满足 (H1)-(H4) 处封口，不满足处**不推出任何结论** ✓

## §附 【技术词回查】（补录）
```
技术词 stage report     命中文件数=1    :: ./S2-C07-STAGE-REPORT-CLOSED.md 
技术词 applicability    命中文件数=1    :: ./C3882-noncanonical-escape-hatch-specification-and-closure.md 
```
