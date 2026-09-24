已查地图：命中（`M03-L-star-illposed-and-marginal-locus`）⟹ `W=0` 轴点三阶计算，不开新案
D0: 本档对象 = **`W=0` 轴点三阶判定**：`w_a=w_f=0` 精确 ＋ **`Z_3=(4\sqrt{35}/35)\mu-(4\sqrt{3990}/35)\nu_h`** ＋ **`\nu_2` 系数为 `0`（再现结构正交性）** ＋ **`\partial Z_3/\partial\mu>0\Longrightarrow` 三阶不封** ＋ 关键前置澄清（`Z_3` 依赖 `w` 的核自由度）
D1: 1（首次把高阶判定推进到三阶并给出 `Z_3` 的精确形式与符号判定）
[RESEARCH]

# **`W=0` 轴点三阶计算**

## §0 ⚠️ 前置澄清（本档最重要的一步设计）

```
$$\textbf{陷阱}:\ Z_3=z_a+z_f\ \text{看似唯一，但 }S_3\ \text{线性依赖于 }w,\ \text{而 }w\ \text{在核方向上有剩余自由度}$$
$$\quad \ker J=\operatorname{span}\{e_a-e_f,\ e_b-e_g,\ e_e,\ e_h\};\quad (e_a-e_f)\ \text{被 }W=0\ \text{用掉（定 }w_a=w_f=0\text{）};$$
$$\qquad \text{剩余自由}:\ \mu\ (e_e),\ \nu_h\ (e_h),\ \nu_2\ (e_b-e_g);\quad \text{锥限制仅 }\nu_h\ge0\ (\text{因 }v_h=0\Rightarrow w_h\ge0),\ \mu,\nu_2\ \text{自由}$$
$$\Longrightarrow\ \textbf{必须把 }Z_3\ \text{算成 }(\mu,\nu_h,\nu_2)\ \text{的\textbf{仿射}函数再判符号},\ \text{不能取单一 }w$$ ✓✓✓
```

## §1 `W=0` 轴点与二阶层

```
$$\text{点}:\ t=\tfrac14,\ \beta=\tfrac1{20},\ \tau_0=\tfrac{\sqrt{35}}2,\ \tau_3=0;\quad v=\tfrac{\sqrt{35}}2e_e,\ \ R(v)=\tfrac12D^2F[v,v]+F_s$$ ✓
$$\Longrightarrow\ \boxed{W=w_a+w_f=0}\ \textbf{精确}\Longrightarrow \text{锥 }w_a,w_f\ge0\ \textbf{强迫}\ \boxed{w_a=w_f=0}$$ ✓✓✓（先生预测成立）
$$\qquad \text{（数值}:w_h=0,\ w_e=0,\ \text{故 }w_0\ \text{本身锥可行）$$ ✓
```

## §2 ⭐ 三阶结果（精确）

```
$$\textbf{三阶方程}:\ Jz=-S_3(v,w),\quad S_3=D^2F[v,w]+\tfrac16D^3F[v,v,v]+D^2_{xs}F[v,\mathbf1]$$ ✓
$$\boxed{Z_3=z_a+z_f=\frac{4\sqrt{35}}{35}\mu-\frac{4\sqrt{3990}}{35}\nu_h}$$ ✓✓✓
$$\quad \text{（}Z_3(0,0,0)=0\ \text{精确；（}\mu,\nu_h\text{）为 }w\ \text{的剩余核自由）}$$ ✓✓
$$\boxed{\frac{\partial Z_3}{\partial\mu}=+\frac{4\sqrt{35}}{35}\approx+0.6761>0},\qquad \frac{\partial Z_3}{\partial\nu_h}=-\frac{4\sqrt{3990}}{35}\approx-7.2190<0,\qquad \boxed{\frac{\partial Z_3}{\partial\nu_2}=0}$$ ✓✓✓
$$\textbf{关键}:\ \nu_2\ (e_b-e_g)\ \textbf{系数精确为零} \Longrightarrow \text{与 }W_\beta\ \text{中 }\tau_2\ \text{缺席\textbf{同一结构正交性}（再现）}$$ ✓✓✓
```

## §3 判定

```
$$\text{锥允许}:\ \nu_h\ge0,\ \mu\ \text{自由},\ \nu_2\ \text{自由};\quad \text{取 }\mu>0,\ \nu_h=0\Longrightarrow \boxed{Z_3>0}\ \textbf{可达}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\textbf{三阶不封（三阶穿透方向存在）}};\quad \text{无需进入四阶}$$ ✓✓✓
$$\textbf{读法}:\ W=0\ \text{恰是二阶的"临界层"};\ \text{在该层上，三阶可用自由核方向 }e_e\ \text{把 }z_a+z_f\ \text{推正}$$
$$\qquad \text{（即二阶临界并不自动意味着高阶封口；本点属于\textbf{三阶可穿透}}）$$ ✓✓
$$\textbf{对照（先生验收顺序）}:\ W=0\to w_a=w_f=0\ \checkmark\to Jz=-S_3\ \checkmark\to Z_3\ \checkmark\to \boxed{Z_3>0\Rightarrow\text{三阶穿}}$$ ✓✓✓
```

## §4 边界与未决

```
$$\textbf{本档证明}:\ \text{在 }(t,\beta,\tau_0,\tau_3)=(\tfrac14,\tfrac1{20},\tfrac{\sqrt{35}}2,0)\ \text{处，三阶系统存在锥可行解}$$ ✓✓
$$\textbf{不证明}:\ \text{(i) 四阶及以上不重新封口};\ (\text{ii) 真实 }\delta>0\ \text{解的存在（需全阶或构造）};\ (\text{iii) 整个 }W=0\ \text{曲线};\ (\text{iv) }E_+\ \text{侧对应点}$$ ✗✗
$$\qquad \text{注}:\ \nu_h>0\ \text{会使 }Z_3<0;\ \text{故符号\textbf{可控}，判定必须按"存在某组锥可行 }w";\ \text{本档取 }\mu>0,\nu_h=0$$ ✓
【⛔ 纪律】 本轮为**精确符号计算**（sympy，含 }\sqrt{35},\sqrt{3990}$$）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 三阶判定为**渐近展开的必要条件层**，非存在性证明 ✓

## §附 【技术词回查】（补录）
```
技术词 third order      命中文件数=0    :: 
技术词 kernel freedom   命中文件数=0    :: 
```
