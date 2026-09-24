已查地图：命中（`M03-R1R2-escape-corners-finite-witnesses`）⟹ 双临界线/点适定性核查与修正，不开新案
D0: 本档对象 = ⚠️**适定性核查（`L_1/L_2/L_\star` 三阶轴向计算不适定）** ＋ **"flat" 的解读澄清（`W=-1` 是基线而非无修正）** ＋ **临界线与双临界点的"margin 恰为 1 的一致封闭"** ＋ **正确的下一目标：逃逸角内的边缘轨迹 `W=0`**
D1: 1（首次给出临界族的一致 margin 与适定性判定，并定位真正适定的高阶目标）
[RESEARCH]

# **`L_\star` 适定性核查与修正**

## §1 ⚠️ 核查结果：三阶轴向系数在临界族上**不适定**

```
$$\textbf{锥约束的正确形式（本线已证）}:\ w_a,w_f\ge0\ \text{且 }e_a-e_f\ \text{是唯一可调配核方向}\Longrightarrow \text{完整判据}=\boxed{W=w_a+w_f\ge0}$$ ✓✓
$$\textbf{临界轴上}:\ W=-1\ (\text{精确})\ \Longrightarrow\ -1<0\ \textbf{已违反锥}\Longrightarrow \text{不存在锥可行的 }w\ \Longrightarrow\ \textbf{三阶方程 }Jz=\cdots\ \text{无可作基}$$ ✗✗
$$\textbf{故 }Z_3=z_a+z_f\ \text{在临界轴上\textbf{不可计算}（不是"算出来为正/为负"，而是\textbf{不适定）}}$$ ✓✓✓
```

## §2 "flat" 的解读澄清（关键）

```
$$\text{先生读法}:\ W=-1\ \text{"完全没有二阶修正"}\Longrightarrow \text{"二阶恰好失效、三阶决定"}$$
$$\text{实际含义}:\ W_\beta=\underbrace{-1}_{\textbf{基线（迹亏空）}}\ \underbrace{-\mathcal Q/D}_{\textbf{二次修正}};\quad \mathcal Q=0\ \text{只说明\textbf{修正项}为零},$$
$$\qquad \textbf{基线 }-1\ \text{本身已是锥障碍}（\text{锥要求 }W\ge0\text{）};\ \text{故"flat"}=\text{“障碍最小”而\not=“无障碍”}$$ ✓✓✓
$$\text{基线来源（精确、非渐近）}:\ 2a+2f+i=1+2t-2s\Longrightarrow 2(w_a+w_f)+w_i=-2;\ v=0\ \text{时 }w_i=0\Longrightarrow W=-1$$ ✓✓
$$\qquad \text{（与一阶证书 }u_a+u_f=-1\ \text{同源；}\tau=0\ \text{即纯 }\delta\ \text{方向）}$$ ✓✓
```

## §3 正面结果：临界族的一致封闭（margin 恰为 1）

```
$$\textbf{L1（}A=0\text{）}:\ \beta=\tfrac{1-3t}2,\ \tfrac15\le t<\tfrac13;\quad W=-1-\frac{B\tau_3^2+4W\tau_0\tau_3}D\le-1\ (\text{等号仅 }\tau_3=0)$$ ✓✓✓
$$\qquad \text{数值抽检 }t=\tfrac3{10},\beta=\tfrac1{20}:\ \text{锥上 }\max W=-1.000000\ \text{（}\tau=(0,0)\text{ 与 }\tau_3=0\ \text{射线）}$$ ✓✓
$$\textbf{L2（}B=0\text{）}:\ \beta=t,\ \tfrac15\le t<\tfrac13;\quad W=-1-\frac{(5t-1)\tau_0^2+4W\tau_0\tau_3}{2W^2}\le-1\ (\text{等号仅 }\tau_0=0)$$ ✓✓✓
$$\qquad \text{抽检 }t=\beta=\tfrac3{10}:\ \max W=-1.000000;\quad \text{沿 }\tau_0=0\ \text{射线 }W\equiv-1$$ ✓✓
$$\textbf{L}_\star\ (\text{双临界点 }t=\beta=\tfrac15,\ A=B=0):\ \boxed{W=-1-\frac{4W}{D}\tau_0\tau_3}\ (D=\tfrac{32}{25},\ 4W/D=2.5)$$ ✓✓✓
$$\qquad \Longrightarrow\ \text{两轴 }\tau_0\tau_3=0\ \text{上 }W=-1;\ \textbf{内部严格更负}\Longrightarrow \textbf{一致封闭（margin 恰 }1\text{）}$$ ✓✓✓
$$\textbf{意义}:\ \text{临界族的封闭\textbf{比一般封闭区更强}（margin 不高 }1\text{，且沿轴可达等号）};\ \text{而非"边缘/未定"}$$ ✓✓✓
```

## §4 相图的最终形式（无"未定区"）

```
$$\boxed{\text{封闭区}=\{(t,\beta):\ \mathcal Q\ge0\ \forall\tau\in\text{锥}\}\iff W\le-1\ \text{一致；}\qquad \text{逃逸区}=\{\exists\tau:\ W\ge0\}\iff W>0\ \text{可达}}$$ ✓✓
$$\quad \textbf{不存在"二阶未定/边缘"参数点}:\ \text{临界族亦是封闭（margin }1\text{）};\ \text{判据是 }W\ \text{的符号，完全二分}$$ ✓✓✓
$$\quad \text{（唯一边缘在 }\mathcal Q\ \text{的零点轨迹上，但那是在}\textbf{逃逸角内部}，见 §5\text{）}$$ ✓✓
```

## §5 正确的下一目标：逃逸角内的边缘轨迹 `W=0`

```
$$\textbf{仅当 }W\ \text{可取 }0\ \text{时二阶才真正"边缘"，三阶才有决定权};$$
$$\quad \text{在逃逸角内（如 }E_-:\ A<0\ \text{或 }E_+:\ B<0\text{）}:\ W=0\iff A\tau_0^2+B\tau_3^2+4W\tau_0\tau_3=-D\ (\text{双曲线分支})$$ ✓✓
$$\textbf{轴线阈值（已核验）}:\ E_-:\ \tau_0^2=\frac D{|A|}\ (\text{如 }t=\tfrac14,\beta=\tfrac1{20}:\ 8.75);\quad E_+:\ \tau_3^2=\frac D{|B|}\ (13.125)$$ ✓✓
$$\textbf{建议的适定三阶目标}:\ \text{取 }W=0\ \text{轨迹上的有限 }\tau^\star,\ \text{计算 }Z_3=z_a+z_f\ \text{的符号};\quad Z_3<0\Longrightarrow \text{该}\tau^\star\text{处三阶重新封死}$$
$$\qquad \text{（即在"二阶恰好平衡"的薄曲线上判定更高阶）；这比在已封死的临界族上算三阶\textbf{适定且有信息}$$ ✓✓✓
【⛔ 纪律】 本轮为**精确符号 + 数值抽检**；`U_{2,3}` 暂停；**不回 RH**；**未升 }\varepsilon^3$$** ✓
【边界】 §1 的"不适定"是**本线锥判据**（`W≥0`）的直接推论；§3 的"一致封闭"限于 `Z_2`-`Case II` 边界族的 `\varepsilon^2` 尺度；**不构成**"`S` 不可实现" ✓

## §附 【技术词回查】（补录）
```
技术词 ill-posed        命中文件数=2    :: ./FILTER-TESTABLE-1-testbed-range-three-classes-and-testability-precondition.md ./ATTACK-S2-pre-search-DBN-heatflow-ALREADY-CLOSED-and-my-proposal-illposed.md 
技术词 marginal locus   命中文件数=0    :: 
```
