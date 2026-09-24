已查地图：命中（`M03-P2iii-second-order-rigidity-certificate`）⟹ 一般 `\beta` 的二阶封口定理（`(甲)`），不开新案
D0: 本档对象 = **一般 `\beta` 的 `J_\beta` 与 `\ker J_\beta`** ＋ **冻结结构审计（哪些是结构性的）** ＋ **`\tau_2` 恒缺席（结构性正交）** ＋ ⭐**显式 `W_\beta` 公式** ＋ **符号判据与 `\beta` 区间分档（EXIT A）** ＋ 一处自纠（符号 bug）
D1: 1（首次把二阶封口从单点升级为整条边界族的定理）
[RESEARCH]

# **`P2(iv)`：一般 `\beta` 的二阶封口定理**

## §1 `J_\beta`（一般 `\beta,t`，精确）

```
$$\textbf{行结构（9 列: }a,b,c,d,e,f,g,h,i\text{）}:$$
$$\quad \text{行0}:\ (1,-1,0,0,0,1,-1,0,0);\qquad \text{行2}:\ (1,1,0,0,0,1,1,0,1)$$ ✓✓
$$\quad \text{行1}:\ \big(-\kappa,\ \kappa,\ -2V,\ 2V,\ 0,\ -\beta,\ \beta,\ 0,\ 0\big),\quad \kappa:=\tfrac12-\beta-\tfrac t2$$ ✓
$$\quad \text{行3}:\ \big(\tfrac{1-t}2-\beta,\ \tfrac{1-t}2-\beta,\ -2W,\ -2W,\ 0,\ \beta+t,\ \beta+t,\ 0,\ \tfrac{1-t}2\big)$$ ✓
$$\quad \text{行4}:\ \big(\tfrac{t(1-2\beta-t)}2,\ \tfrac{t(1-2\beta-t)}2,\ -2Wt,\ -2Wt,\ 0,\ \beta t,\ \beta t,\ 0,\ -W^2-\beta^2-\tfrac{\beta t}2+\tfrac\beta2\big)$$ ✓
$$\boxed{\operatorname{rank}J_\beta=5\ \text{（一切 }\beta,t\text{）}\Longrightarrow\dim\ker J_\beta=4}$$ ✓✓✓
```

## §2 `\ker J_\beta` 与冻结结构审计（关键）

```
$$\ker J_\beta=\operatorname{span}\{\,N_1=e_e,\quad N_4=e_h,\quad N_2=(-1,0,\tfrac{\cdot}{\cdot},0,1,0,0,0),\quad N_3=(0,-1,\tfrac{\cdot}{\cdot},\tfrac{\cdot}{\cdot},0,0,1,0,0)\,\}$$
$$\quad N_{2,3}\ \text{的 }c,d\ \text{分量}: \tfrac{4V\beta+Vt-V\mp 4W\beta\mp Wt\pm W}{8VW}\ (\text{符号随列不同})$$ ✓
$$\textbf{审计结论（结构性 vs 特殊点）}:$$
$$\quad \boxed{v_a+v_f=0}\quad \textbf{对一切 }\beta,t\ \text{成立（结构性）}\ \checkmark$$ ✓✓✓
$$\quad \boxed{v_i=0}\quad \textbf{对一切 }\beta,t\ \text{成立（结构性）}\ \checkmark$$ ✓✓✓
$$\quad \boxed{v_b+v_g=0}\quad \text{对一切 }\beta,t\ \text{成立}\ \checkmark$$ ✓✓
$$\quad \boxed{v_c=v_d=0}\quad \textbf{仅当 }4\beta+t-1=0\ \text{即}\ \beta=\tfrac{1-t}4\ (\text{特殊点的额外消项，非结构性})\ \times$$ ✓✓
$$\Longrightarrow\ \text{锥 }v_a,v_f\ge0\ \text{仍强制}\ \boxed{v_a=v_f=0}\Longrightarrow a,f=O(\varepsilon^2)\ \textbf{整族成立}$$ ✓✓✓
```

## §3 ⭐ `\tau_2` 恒缺席与显式 `W_\beta`

```
$$\text{迹恒等式（精确）}:\ 2w_a+2w_f+w_i=-2\Longrightarrow\boxed{W_\beta:=w_a+w_f=-1-\tfrac12w_i}$$ ✓✓
$$\quad \text{（因 }\ker J_\beta\ \text{无 }i\ \text{分量}\Longrightarrow w_i\ \text{是不变量，无需分别求 }w_a,w_f\text{）}$$ ✓✓
$$\boxed{W_\beta=-1-\frac{A\,\tau_0^2+B\,\tau_3^2+4W\,\tau_0\tau_3}{(1-t)(1+3t)}},\qquad A:=2\beta+3t-1,\quad B:=2(t-\beta)$$ ✓✓✓
$$\quad \text{其中 }(1-t)(1+3t)=1+2t-3t^2\ \textbf{与 }\beta\ \text{无关（分母 }\beta\text{-自由）}$$ ✓✓
$$\boxed{\tau_2\ \textbf{完全不出现在 }W_\beta\ \text{中（对一般 }\beta\text{）}}\Longrightarrow \text{（}b,g\text{）反对称核方向与“迹亏空承担量”}\textbf{结构性正交}$$ ✓✓✓
$$\quad \text{（先生指出的首要审计项，答案为：结构性，而非特殊点巧合）}$$ ✓✓
$$\textbf{交叉核验}:\ \beta=\tfrac{1-t}4\ \text{时退化为 }-\tfrac{250\tau_0^2+1380\tau_0\tau_3+250\tau_3^2}{517}-1\ \textbf{与上一档精确一致}$$ ✓✓✓
$$\textbf{独立数值核验}:\ \beta\in\{\tfrac1{40},\tfrac1{20},\tfrac{11}{80},\tfrac15,\tfrac14\}\ (\text{最小范数解}) \Longrightarrow \text{全部与公式一致}\ \checkmark\checkmark$$ ✓✓✓
```

## §4 符号判据与 `\beta` 区间分档

```
$$\text{允许区}:\ \beta\in(0,\tfrac{1-t}2)\ (\text{由 }b=\beta>0,\ g=\tfrac{1-t}2-\beta>0);\quad t\in(0,1)$$ ✓
$$\boxed{W_\beta\le-1<0\iff A\tau_0^2+B\tau_3^2+4W\tau_0\tau_3\ \ge0\quad\text{于锥 }\tau_0,\tau_3\ge0}$$ ✓✓
$$\quad A\ge0\iff\beta\ge\tfrac{1-3t}2;\qquad B\ge0\iff \beta\le t;\qquad 4W\tau_0\tau_3>0\ (\textbf{恒正，助刚性})$$ ✓✓
$$\textbf{情形 ①（}t\ge\tfrac13\text{，含我方 }t\in(\tfrac49,\tfrac{15}{31})\text{）}:\ (1-t)/2\le t\Longrightarrow \text{整条允许区 }\beta<t\Longrightarrow B>0;\ \text{且 }A\ge3t-1\ge0$$
$$\quad \Longrightarrow\ A,B\ge0\Longrightarrow \text{括号}\ \ge0\ (\text{外加正项})\Longrightarrow \boxed{W_\beta\le-1<0\ \text{于整条边界族}}$$ ✓✓✓
$$\qquad\Longrightarrow\ \boxed{\textbf{EXIT A（强成功）}:\ \text{一般 }\beta\ \text{二阶封口定理成立（}t\ge\tfrac13\text{）}}$$ ✓✓✓
$$\textbf{情形 ②（}t<\tfrac13\text{）}:\ \text{允许区延至 }\beta>(1-t)/2>t\Longrightarrow \beta>t\ \text{时 }B<0;\ \text{取 }\tau_0=0,\tau_3\ \text{大} \Longrightarrow W_\beta=-1+\tfrac{|B|\tau_3^2}{(1-t)(1+3t)}\ge0$$
$$\quad \Longrightarrow\ \boxed{\text{刚性仅在 }\beta\le t\ \text{成立（EXIT B：部分成功）};\ \beta\in(t,\tfrac{1-t}2)\ \text{存在二阶锥可行方向}}$$ ✓✓
```

## §5 自纠记录

```
$$\textbf{本次抓到自己的符号 bug}:\ w_i\ \text{应为}\ -u_i\!\cdot\! R\ (u_i:=e_i^\top J^+),\ \text{我首版漏负号}$$ ✗
$$\quad \text{修正前}:W=-1+\tfrac{A\tau_0^2+B\tau_3^2-2(t-\beta)\tau_3^2\cdots}{\cdots}\ \text{（与数值反向）};\quad \text{修正后与最小范数解核验 5/5 一致}$$ ✓✓✓
$$\quad \text{（教训：以“已知点退化值”作交叉核验（此处 }\beta=\tfrac{1-t}4\text{）能\n一步抓出全局符号错误）}$$ ✓
【⛔ 纪律】 本轮为**符号计算**（sympy 精确）＋ 数值交叉核验；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 定理限于 `Z_2`-`Case II` 边界族的 `\varepsilon^2` 尺度；端点 `\beta\to0`、`\beta\to\tfrac{1-t}2`（`b` 或 `g` 退化）**未覆盖**；`t<\tfrac13` 的 `\beta>t` 段**未封**；**本档不含"可实现"结论** ✓

## §附 【技术词回查】（补录）
```
技术词 parameter family 命中文件数=1    :: ./ix-final-archive.md 
技术词 structural orthogonality 命中文件数=0    :: 
```
