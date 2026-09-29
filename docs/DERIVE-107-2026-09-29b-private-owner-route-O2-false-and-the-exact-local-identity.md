# DERIVE-107-b（2026-09-29）—— **private-owner 链：$(O1)$ 成立，但 $(O2)(O6)$ \textbf{为假}；纠正后得\ \textbf{精确恒等式}；系数 $10$ 太弱**

> **性质**：**纯推导 ＋ 全量实测**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 13:0x ✓
> **唐先生令**：「先把能严格推出的东西完整压出来」✓

**已查地图**：`DERIVE-107`（校准与充电形式）／`29x`（私有点层）✓

D0: 本档对象 ＝ **档案已有**（$P,Q,\mu,r_x,s_x$——无新数学对象 ✓）
D1: 0（产出＝**一处证成立 ＋ 两处否证 ＋ 一条精确恒等式 ＋ 系数定位** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ }(O1)\ \textbf{成立}:\ r_x=|C\cap S_2(x)|\ge5\ ——\ \text{实测 }746/746\ \text{零违例};\ \text{分布 }\{5{:}338,6{:}319,7{:}63,8{:}25,9{:}1\}}$$
$$\boxed{\text{② ✗✗ }(O2)\ \textbf{为假}:\ d(c,d)\in\{1,3\}\ \text{皆发生};\ \text{显式反例}\ x{=}0000001101,c{=}0010001101,d{=}0010001100\Rightarrow d(c,d){=}1✗}$$
$$\boxed{\text{③ ✗✗ }(O6)\ \textbf{为假}:\ \text{违例 }393/746\ (\text{与 }s_x{>}0\ \text{之 }393\ \text{例一一对应})}$$
$$\boxed{\text{④ ✓✓ 纠正后\ \textbf{精确恒等式}}:\ \sum_{y\in N(x)\setminus\{c\}}\bigl(\mu(y)-1\bigr)=2r_x-\mathbf{s_x}-9\ (\text{余量恒 }0)}$$
$$\boxed{\text{⑤ ✗ 系数}:\ \text{实测 }\text{maxmult}=9\Longrightarrow P+Q\le10E\Longrightarrow M\ge\mathbf{102}\ (\textbf{弱于}\ \text{van Wee }103)}$$

## §1 ① $(O1)$ 成立（**✓✓ 零违例**）

$$\text{每个 }d\in C\cap S_2(x)\ \text{恰覆盖 }N(x)\ \text{之两点}\ (\text{差两坐标}\{i,j\}\Rightarrow y{=}x\oplus e_i,x\oplus e_j)\Longrightarrow\ \text{需}\ \lceil9/2\rceil=5✓$$

## §2 ② $(O2)$ 之显式反例（**✗✗**）

$$\textbf{实测反例}:\ x=0000001101,\ \text{owner }c=0010001101,\ d=0010001100$$
$$d(x,c)=1,\quad d(x,d)=2,\quad \boxed{d(c,d)=1}\ ✗\ (\text{你称必为 }3)$$
$$d\ \text{覆盖}\ N(x)\ \text{之两点}=\{0000001100,\ 0010001101\}\ \ni c\ \Longrightarrow\ \text{对 }N(x)\setminus\{c\}\ \text{之有用覆盖仅 }1\ \text{点（非 }2)$$
$$\text{你的理由「否则 }d\ \text{会覆盖 }x\text{」\ \textbf{不成立}}:\ d(d,x)=2>1\ \text{与 }d(c,d)\ \text{无关✓}$$

## §3 ③ $(O6)$ 为假 ＋ ④ 精确恒等式（**✗✗ ＋ ✓✓**）

$$\text{记}\ s_x:=\#\{d\in C\cap S_2(x):d(c,d)=1\};\quad \text{实测 }s_x\ \text{分布}:\ \{0{:}353,1{:}224,2{:}132,3{:}37\}$$
$$\text{几何事实（可证）}:\ N(x)\setminus\{c\}\ \text{之 }9\ \text{点\ \textbf{只能}由 }C\cap S_2(x)\ \text{覆盖}$$
$$\text{（}d(w,x)\in\{0,1\}\ \text{不可能};\ d(w,x)=3\Rightarrow d(w,y)\in\{2,4\}\ \text{不可覆盖}✓）$$
$$\therefore\ \sum_{y\in N(x)\setminus\{c\}}\mu(y)=\sum_{d\in C\cap S_2(x)}\bigl(2-[d(c,d){=}1]\bigr)=2r_x-s_x$$
$$\therefore\ \boxed{\sum_{y\in N(x)\setminus\{c\}}\bigl(\mu(y)-1\bigr)=2r_x-s_x-9}\qquad\textbf{实测 746/746，余量恒为 }0✓✓$$
$$\text{即此式是\ \textbf{恒等式}（非约束）；你的 }(O6)\ \text{相当于令 }s_x{=}0,\ \text{故 }393/746\ \text{处失效}✗$$

## §4 ⑤ 系数与最终界（**✗ 太弱**）

$$\text{容量论证（用户之 }p_c\le\tfrac35a_3\text{）以 }(O2)\ \text{为前提}\Longrightarrow\ \textbf{不成立}✗$$
$$\text{正确的求和链}:\ P\le\sum_x(2r_x-s_x-9)\le\text{maxmult}\cdot E$$
$$s_x\ \text{分布}+r_x\ \text{分布}\Longrightarrow\ \sum_x(2r_x-9-s_x)=\sum_x\sum_{N(x)\setminus\{c\}}(\mu-1)=1536$$
$$\text{实测 }\text{maxmult}=\mathbf{9}\ (\text{mult 分布 }\{0{:}120,3{:}6,4{:}10,5{:}42,6{:}103,7{:}181,8{:}497,9{:}65\})$$
$$\therefore\ P+Q\le(\text{maxmult}+1)E=10E\Longrightarrow M\ge\frac{1024\cdot11}{111}=101.48\Longrightarrow\mathbf{102}\ ✗$$
$$\boxed{\text{须 maxmult}\le5\ \text{方能给 }107;\ \text{实测 }9\Longrightarrow\ \text{此路\ \textbf{不足以闭合}}}✗$$

## §5 保留与结论（**✓ 诚实**）

$$\textbf{保留}:\ (O1)\ (r_x\ge5)\ ✓;\ \text{恒等式}\ \sum_{N(x)\setminus\{c\}}(\mu-1)=2r_x-s_x-9\ ✓;\ N(x)\setminus\{c\}\ \text{仅由 }S_2(x)\ \text{覆盖}\ ✓$$
$$\textbf{失效}:\ (O2)\ (d(c,d)\equiv3)\ ✗;\ (O6)\ ✗;\ p_c\le\tfrac35a_3(c)\ ✗;\ \text{系数 }10\Rightarrow102 ✗$$
$$\therefore\ \boxed{\text{private-owner 链\ \textbf{当前产出 }102，低于 van Wee 之 }103\Longrightarrow\ \text{无净进步}}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "(O2)反例" "精确局部恒等式" "系数10"
技术词 (O2)反例      命中文件数=0    ::
技术词 精确局部恒等式   命中文件数=0    ::
技术词 系数10       命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code 全量实测（含显式反例、恒等式余量、mult 分布）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 含**我上一批测试之 bug 之更正**（切片/断言残缺）✓；**不主张** $107$ 不可达 ✗（V290）
