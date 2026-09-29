# DERIVE-107-d（2026-09-29）—— **$\mu{=}2$ 之"正方形补全"是真强制；但 $\rho_{\max}{=}10$，③ 关闭；并得\textbf{局部载体复用上限}之元结论**

> **性质**：**纯推导 ＋ 全量实测**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 13:2x ✓
> **唐先生令**：③ 第一刀只做 $N_2$ ＋ 两个 owner 之距离/交集结构；定义不动 ✓

**已查地图**：`DERIVE-107-c`（② 关闭）／`DERIVE-107-b`（恒等式）✓

D0: 本档对象 ＝ **档案已有**（$\mu,N_2$／owner／对角点——无新数学对象 ✓）
D1: 0（产出＝**一处真强制 ＋ 两处判门失败 ＋ 一处元结论** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ }N_2=\mathbf{136}\ (\ne0)\Longrightarrow\ \text{③ 不因缺对象而关闭};\ d(c_1,c_2)\equiv\mathbf{2}}$$
$$\boxed{\text{② ✓✓ P-a\ \textbf{真强制}}:\ N_{11}(y)\equiv\mathbf{1}\ (136/136)\Longrightarrow\ \text{每个 }\mu{=}2\ \text{点有唯一\ \textbf{对角点} }z,\ \textbf{且 }\mu(z)\ge2}✓$$
$$\boxed{\text{③ ✗ P-b\ \textbf{失败}}:\ \rho_{\max}=\mathbf{10}\ (>5)\ \text{门槛（}\rho\ \text{分布 }\{1{:}44,2{:}13,6{:}1,7{:}1,8{:}2,9{:}3,10{:}1\})}$$
$$\boxed{\text{④ ✗✗ P-c\ \textbf{相消}}:\ \text{净账 }\Delta=\text{负}\ (N_2\le\rho_{\max}Q=1580\ \text{vs 实测 }136)\Longrightarrow\ \textbf{③ 关闭}}✓$$

## §1 ① $N_2$ 与 owner 距离（**✓**）

$$\text{非码字之 }\mu\ \text{分布}:\ \{1{:}746,\ \mathbf{2{:}136},\ 3{:}13,\ 4{:}2,\ 5{:}7\}\Longrightarrow\ \boxed{N_2=136}✓$$
$$\text{owner 数}\ne2\ \text{者}:\ 0;\qquad d(c_1,c_2)\ \text{分布}:\ \{\mathbf{2{:}136}\}$$
$$\therefore\ \boxed{d(c_1,c_2)\equiv2}\ ——\ \text{定理（}y\notin C\Rightarrow c_1,c_2\in N(y)\text{；无三角形）✓}$$
$$\text{（你预设之 }\{2,4,\dots\}\ \text{中只有 }2\ \text{会出现}✓）$$

## §2 ② P-a：正方形补全（**✓✓ 真强制**）

$$N_{11}(y)=\#\{z:d(z,c_1){=}d(z,c_2){=}1,\ d(z,y){=}2\}\ \equiv\ \mathbf{1}\qquad(136/136)✓$$
$$\text{几何}:\ y\ \text{与 }c_1{=}y\oplus e_a,\ c_2{=}y\oplus e_b\ \text{构成正方形之三角};\ \text{第四点 }z{=}y\oplus e_a\oplus e_b\ \text{唯一}✓$$
$$\text{关键}:\ d(z,c_1){=}d(z,c_2){=}1\Longrightarrow z\in B_1(c_1)\cap B_1(c_2)\Longrightarrow \boxed{\mu(z)\ge2}✓$$
$$\text{实测 }z\ \text{之 }\mu\ \text{分布}:\ \{2{:}26,\ 3{:}31,\ 4{:}19,\ 5{:}60\}\ ——\ \textbf{全部 }\ge2✓✓$$
$$\therefore\ \boxed{\text{每个 }\mu{=}2\ \text{点}\ \textbf{强制}出一个对角点 }z\ (d(y,z){=}2)\ \text{且}\ \mu(z)\ge2}\ ——\ \textbf{真强制}✓$$

## §3 ③ P-b：复用次数（**✗ 超门槛**）

$$\rho(z):=\#\{y\in N_2:\ z\ \text{为 }y\ \text{之对角点}\};\qquad \rho\ \text{分布}:\ \{1{:}44,\ 2{:}13,\ 6{:}1,\ 7{:}1,\ 8{:}2,\ 9{:}3,\ 10{:}1\}$$
$$\boxed{\rho_{\max}=\mathbf{10}\ \gg\ 5}\ \Longrightarrow\ \text{载体\ \textbf{不稀缺}}\ ✗$$
$$\text{（另有}:\ \text{被复用之 }z\ \text{个数 }65;\ \text{其中\ \textbf{码字} }24/136;\ \text{而 }\mu{=}2\ \text{点中 }26/136\ \text{自身亦为他人之对角点 ⟹ \textbf{自指结构}}✓）$$

## §4 ④ P-c：净账（**✗✗ 相消，与 ② 同型**）

$$\text{强制关系}:\ N_2\ \le\ \rho_{\max}\cdot Q\ =\ 10\cdot158\ =\ 1580\qquad\text{v.s.}\ \ \text{实测 }N_2=136$$
$$\therefore\ \Delta=\underbrace{1580}_{\text{"压掉"的上界}}-\underbrace{136}_{\text{实际}}=+\textbf{1444 冗余（无信息）}✗$$
$$\therefore\ \boxed{\text{与 ② 同型}:\ \text{载体存在、强制存在，但\ \textbf{计数相消}}（y\mapsto z\ \text{落入 }Q,\ \text{而 }Q\ \text{已含 }N_2）\Longrightarrow\ \textbf{③ 关闭}}✓$$

## §5 ★ 元结论（**本档最有价值者**）

$$\text{已试三种"局部位置"载体}:\ \text{①私有邻点位置（maxmult }9\text{）};\ \text{②}T\ \text{点（}p\le10-\mu\text{，代价自付）};\ \text{③对角点（}\rho_{\max}{=}10\text{）}$$
$$\therefore\ \boxed{\text{任何\ \textbf{局部位置}型载体，其复用上限}\ \approx\ \mathbf{10}\ (>5)\Longrightarrow\ \text{做不出}\ \le5\ \text{之系数}}✓✓$$
$$\text{根因}:\ \text{立方体局部结构过于\ \textbf{规则}（任意位置恒有 }10\ \text{个邻居可用）}\Longrightarrow\ \text{无稀缺性}$$
$$\therefore\ \boxed{\text{"局部充电"纲领\ \textbf{经验上关闭}};\ \text{欲}\ \le5\ \text{系数须一个\ \textbf{非局部}（全局/谱）载体}}✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "对角点强制" "rho_max10" "局部载体复用上限"
技术词 对角点强制      命中文件数=0    ::
技术词 rho_max10     命中文件数=0    ::
技术词 局部载体复用上限 命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code 全量实测（含 $N_2$、owner 距离、$N_{11}$、$\rho$ 分布、$\mu(z)$ 分布）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张** $107$ 不可达 ✗（V290）；③ 之关闭系**本载体**之结论 ✓
