已查地图：命中（`M03-R3-critical-line-beta-equals-t`）⟹ `E_\pm` 外角有限见证构造，不开新案
D0: 本档对象 = **两外角有限二阶可行方向的存在性见证**（含尺度审计）＋ **显式 `x(\varepsilon)` 逐条非负核验** ＋ **二阶相图定稿** ＋ 复核结论
D1: 1（首次把形式方向落成有限真实局部方向并给出显式见证）
[RESEARCH]

# **`R1/R2`：两外角 `E_\pm` 的有限见证**

## §1 检验协议（按先生要求）

```
$$\text{① 取固定有限 }\tau;\quad\text{② 核验 }v\ \text{满足一切一阶锥条件};\quad\text{③ 求 }w;\quad\text{④ 核验\textbf{全部原始非负约束}};\quad\text{⑤ 存在有限参数 ⟹ 正式记为"二阶确实可穿透"}$$ ✓✓
$$\textbf{锥约束的完整清单（本问题共 9 条 }x_j\ge0\text{，等价于支配条件）}:\ \text{基点处 }a=f=e=h=0\ \text{紧};\ b,g,c,d,i>0\ \text{松}$$
$$\quad \varepsilon\ \text{阶}:\ v_a,v_f,v_e,v_h\ge0;\qquad \varepsilon^2\ \text{阶}:\ \text{对 }v_j=0\ \text{者需 }w_j\ge0$$
$$\quad \text{可加核方向}: e_a-e_f\ (\text{同时改 }w_a,w_f,\text{反向})\Longrightarrow \textbf{唯一的不可自由量是 }W=w_a+w_f;$$
$$\qquad w_e,w_h\ \text{可分别经 }e_e,e_h\ \text{单向增大}\Longrightarrow \text{其}\ge0\ \textbf{恒可满足};\quad \text{故完整判据}=\boxed{W\ge0}$$ ✓✓✓
```

## §2 `E_-`：`\beta<\tfrac{1-3t}2`（`A<0,\ B>0`）

```
$$\text{取 }\tau_3=0,\ \tau_0=T\ (\text{有限}),\ \tau_1=\tau_2=0\Longrightarrow v=T\,e_e;\quad \mathcal Q=AT^2<0\Longrightarrow W=-1+\tfrac{|A|T^2}D$$
$$\textbf{见证点}:\ t=\tfrac14,\ \beta=\tfrac1{20}\ (A=-\tfrac{3}{20},\ B=\tfrac25,\ D=\tfrac{21}{16}),\quad T=4,\ \varepsilon=\tfrac1{100}$$
$$\quad \Longrightarrow \boxed{W_p=\tfrac{29}{35}>0}\ \textbf{（二阶锥可行）}$$ ✓✓✓
$$\quad x(\varepsilon)=(\,a,b,c,d,e,f,g,h,i\,)\ \text{（数值）}:$$
$$\quad (4.1429\!\times\!10^{-5},\ 0.0501691,\ 0.6071285,\ 0.1917474,\ 0.04,\ 4.1429\!\times\!10^{-5},\ 0.3250138,\ 0,\ 0.2496343)$$
$$\quad \textbf{全部 9 条非负}:\ \checkmark\ (\min=0);\qquad \text{谱约束残差}\ \max|F|=2.73\!\times\!10^{-5}\ \text{与 }O(\varepsilon^3)\ \text{级相符}$$ ✓✓
```

## §3 `E_+`：`\beta>t`（`B<0,\ A>0`）

```
$$\text{取 }\tau_0=0,\ \tau_3=T\Longrightarrow v=T\,e_h;\quad W=-1+\tfrac{|B|T^2}D$$
$$\textbf{见证点}:\ t=\tfrac14,\ \beta=\tfrac3{10}\ (A=\tfrac7{20},\ B=-\tfrac1{10},\ D=\tfrac{21}{16}),\quad T=4,\ \varepsilon=\tfrac1{100}$$
$$\quad \Longrightarrow \boxed{W_p=\tfrac{23}{105}>0}\ \textbf{（二阶锥可行）}$$ ✓✓✓
$$\quad x(\varepsilon)=\ (1.0952\!\times\!10^{-5},\ 0.2999975,\ 0.6128012,\ 0.1899629,\ 0,\ 1.0952\!\times\!10^{-5},\ 0.0751244,\ 0.04,\ 0.2497562)$$
$$\quad \textbf{全部 9 条非负}:\ \checkmark\ (\min=0);\qquad \max|F|=1.94\!\times\!10^{-5}\ \text{与 }O(\varepsilon^3)\ \text{级相符}$$ ✓✓
```

## §4 尺度审计（先生特别要求）

```
$$\text{展开有效性}:\ \text{需 }|\varepsilon^2w|\ll|\varepsilon v|\iff \varepsilon T\ll1;\quad \text{本例 }\varepsilon T=0.04\ll1\ \checkmark$$ ✓✓
$$\text{阈值条件}:\ W>0\iff T>\sqrt{D/|A|}\ \text{或}\ \sqrt{D/|B|};\quad \text{两点分别 }\sqrt{8.75}=2.96,\ \sqrt{13.125}=3.62\Longrightarrow T=4\ \text{足够}$$ ✓✓
$$\Longrightarrow\ \text{对 }|A|\ \text{或 }|B|\ \text{有界远离 }0\ \text{的 }(t,\beta),\ \text{总可取 }T=O(1)\ \text{与 }\varepsilon\ \text{小到 }\varepsilon T\ll1\Longrightarrow \textbf{失效为真（非形式）}$$ ✓✓✓
$$\text{边缘情形（复述）}:\ t\to\tfrac15^-,\ \beta=t\ \text{时阈值}\to\infty\Longrightarrow \text{需无界 }T\Longrightarrow \text{该处失效为"边缘"}$$ ✓✓
```

## §5 二阶相图（定稿）

```
$$\boxed{\text{二阶封口区}=\Big\{\max\big(0,\tfrac{1-3t}2\big)\le\beta\le t\Big\}\ \cap\ \Big\{0<\beta<\tfrac{1-t}2\Big\}}$$ ✓✓✓
$$\quad t\ge\tfrac13:\ \text{封口区}=\text{全部允许区}\ (0,\tfrac{1-t}2)\ \Longrightarrow\ \text{两外角之一为空、另一不可允许}$$ ✓✓
$$\quad t<\tfrac13:\ \text{封口区}=\big[\tfrac{1-3t}2,\ t\big];\quad \textbf{逃逸外角}=\underbrace{\{\beta>t\}}_{E_+}\cup\underbrace{\{\beta<\tfrac{1-3t}2\}}_{E_-}$$ ✓✓✓
$$\text{两条临界线}:\ \boxed{A=0\iff\beta=\tfrac{1-3t}2},\qquad \boxed{B=0\iff\beta=t}\ \text{—— 恰为二次型在两个锥轴方向失去正性的边界}$$ ✓✓✓
$$\textbf{结论}:\ \text{“二阶证明失败”}\ne\ \text{事实};\ \text{真实图景}=\textbf{完整的二阶相图（封闭区｜双临界线｜双逃逸外角）}$$ ✓✓✓
【⛔ 纪律】 本轮为**精确符号 + 显式数值见证**；`U_{2,3}` 暂停；**不回 RH**；**未升 }\varepsilon^3$$** ✓
【边界】 `E_\pm` 的见证证明的是**二阶机制不封**（存在锥可行二阶方向 + 显式非负 `x(\varepsilon)`，谱残差 `O(\varepsilon^3)`）；**不构成**任何 `S` 内点可实现性的证明 ✓

## §附 【技术词回查】（补录）
```
技术词 witness          命中文件数=63   :: ./KERNEL-HUNT-1-two-minimization-problems.md ./V2-28B-L52-mechanism-identified-verdict-OPEN.md ./E4-2-falsifiable-conditions-spec-for-line-enforcing-localization.md 
技术词 escape corner    命中文件数=0    :: 
```
