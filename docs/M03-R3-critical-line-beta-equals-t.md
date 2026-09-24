已查地图：命中（`M03-BOUNDARY-RIGIDITY-STAGE-REPORT`）⟹ `R3` 临界线 `\beta=t` 精确分析，不开新案
D0: 本档对象 = **临界线 `\beta=t` 的精确符号分析** ＋ **恒等式 `D=2W^2`** ＋ **`t=\tfrac15` 分叉确认** ＋ ⚠️**对区域表的一处补正（`A\ge0` 亦为必需）** ＋ **失效阈值与渐近边缘性**
D1: 1（首次给出临界线的完整符号相位图与失效阈值）
[RESEARCH]

# **`R3`：临界线 `\beta=t`**

## §1 临界线上的精确结构

```
$$\beta=t\ \text{（要求 }g=\tfrac{1-3t}2>0\iff t<\tfrac13\text{）}:\quad B=2(t-\beta)=0\ \Longrightarrow\ \boxed{\tau_3^2\ \text{项精确消失}}$$ ✓✓
$$\quad A=2\beta+3t-1=\boxed{5t-1}\ (\text{与先生一致}\ \checkmark)$$ ✓✓
$$\quad W^2\Big|_{\beta=t}=\tfrac{(1-t)(1+3t)}2 \Longrightarrow \boxed{D:=(1-t)(1+3t)=2W^2\Big|_{\beta=t}}$$ ✓✓✓（**临界线上分母与 `W^2` 精确锁定**）
$$\Longrightarrow\ \boxed{W_t=-1-\frac{(5t-1)\tau_0^2+4W\tau_0\tau_3}{2W^2}}$$ ✓✓✓
```

## §2 `t=\tfrac15` 分叉（确认）

```
$$\boxed{t\ge\tfrac15\Longrightarrow 5t-1\ge0\Longrightarrow W_t\le-1<0\ \text{于全锥}\ (\text{临界线仍封口})}$$ ✓✓✓
$$\boxed{t<\tfrac15\Longrightarrow 5t-1<0};\quad \text{取 }\tau_3=0:\ W_t=-1+\frac{(1-5t)\tau_0^2}{2W^2}>0\iff \tau_0^2>\frac{(1-t)(1+3t)}{1-5t}$$ ✓✓
$$\quad \text{数值抽检}:\ t=\tfrac16\Rightarrow \text{阈值}^2=7.50;\quad t=0.15\Rightarrow 4.93\ (\textbf{均为有界}\Longrightarrow \text{失效为真})$$ ✓✓
$$\quad \boxed{\text{渐近边缘性}:\ t\to\tfrac15^-\Rightarrow \text{阈值}\to\infty\Longrightarrow \text{需无界 }\tau_0\ (\varepsilon\text{-展开失效})\Longrightarrow \textbf{该失效在 }t=\tfrac15\ \text{邻域为"边缘"}}$$ ✓✓（诚实标注）
$$\quad \text{（}|\tau_0|=O(1)\ \text{是 }\varepsilon\text{-展开有效的前提；阈值有界处失效结论成立）}$$ ✓
```

## §3 ⚠️ 对区域表的一处补正：`A\ge0` 亦为必需

```
$$\text{闭区判据（两项系数同时非负）}:\ A=2\beta+3t-1\ge0\ \textbf{且}\ B=2(t-\beta)\ge0$$
$$\qquad \Longrightarrow\ \boxed{\text{闭区}=[\max(0,\tfrac{1-3t}2),\ \min(t,\tfrac{1-t}2)]}$$ ✓✓✓
$$\text{① }t\ge\tfrac13:\ \tfrac{1-3t}2\le0\ \text{且}\ t\le\tfrac{1-t}2\Longrightarrow\text{闭区}=(0,t]\ \Longrightarrow\ \text{先生"}\beta<t\Rightarrow\text{封"}\ \checkmark$$ ✓
$$\text{② }t\in(\tfrac15,\tfrac13):\ \tfrac{1-3t}2>0\Longrightarrow \textbf{存在 }\beta<t\ \text{但 }A<0\Longrightarrow\textbf{机制失效}\ \boxed{\text{（先生表格此处过宽）}}$$ ✗✓
$$\qquad \text{实例 }t=\tfrac14:\ \text{闭区}=[0.125,\ 0.25];\quad \beta=0.05<t\ \text{但 }A=-0.15<0\Longrightarrow\text{失效（阈值 }\tau_0^2>8.75\text{）}$$ ✓✓
$$\text{③ 临界线 }\beta=t\ \text{仅当 }t<\tfrac13\ \text{可允许}\ (g>0)\Longrightarrow \textbf{表中" }t\ge\tfrac13,\ \beta=t\text{ "一行是空集}$$ ✓✓
```

## §4 补正后的完整相位图

```
$$\begin{array}{c|c|c}\text{区域} & \text{当前二阶结论} & \text{依据}\\\hline
\beta\in[\max(0,\tfrac{1-3t}2),\ \min(t,\tfrac{1-t}2)] & \textbf{封} & A,B\ge0\\\hline
\beta>t\ (\text{可允许}\iff t<\tfrac13) & \textbf{机制失效} & B<0,\ \tau_0=0,\ \tau_3\ \text{大}\\
\beta<\tfrac{1-3t}2\ (\iff t<\tfrac13) & \textbf{机制失效} & A<0,\ \tau_3=0,\ \tau_0\ \text{大}\\
\beta=t,\ t\ge\tfrac15 & \textbf{封} & A=5t-1\ge0\\
\beta=t,\ t<\tfrac15 & \textbf{机制失效} & A<0,\ \text{阈值有界}\\
\beta=t,\ t\ge\tfrac13 & \text{空集} & g\le0\\\end{array}$$ ✓✓✓
$$\textbf{结构读法}:\ \text{逃逸区是整个坐标方块的"两个外角"}\ \{\beta>t\}\cup\{\beta<\tfrac{1-3t}2\},\ \text{而非仅 }\beta>t$$ ✓✓
$$\qquad \text{（在 }t\ge\tfrac13\ \text{时第一外角独存，故先前只看到 }\beta>t\text{）}$$ ✓✓
```

## §5 结论（回答先生三问）

```
$$\text{① }\beta=t\ \text{是否仍二阶封口}:\ \boxed{\text{是，当 }t\ge\tfrac15};\ t<\tfrac15\ \text{时失效（阈值有界）}$$ ✓✓
$$\text{② }t<\tfrac15\ \text{是否真有二阶可行方向}:\ \boxed{\text{是}}（\tau_3=0,\ \tau_0^2>\tfrac{(1-t)(1+3t)}{1-5t}）;\ \text{但 }t\to\tfrac15^-\ \text{为边缘}$$ ✓✓
$$\text{③ 区域图精确化}:\ \text{见 §4};\quad \textbf{关键修正}：\text{“}\beta<t\Rightarrow\text{封”只在 }t\ge\tfrac13\ \text{成立}$$
$$\quad \text{（}t<\tfrac13\ \text{时闭区为有界区间 }[\tfrac{1-3t}2,t]，两侧皆失效）$$ ✓✓
【⛔ 纪律】 本轮为**精确符号分析 + 数值抽检**；`U_{2,3}` 暂停；**不回 RH**；**未升 }\varepsilon^3$$** ✓
【边界】 §1 恒等式为符号精确；§2 阈值为有界处失效为真、`t\to\tfrac15^-` 为边缘；§4 为"当前二阶机制"的相位图，**非**"可实现性相位图" ✓

## §附 【技术词回查】（补录）
```
技术词 critical line    命中文件数=44   :: ./grh-goldbach-paper-draft-v2.md ./E20-E40-zero-density-2026-read.md ./ALIGN-A4-A5-with-our-results.md 
技术词 phase diagram    命中文件数=0    :: 
```
