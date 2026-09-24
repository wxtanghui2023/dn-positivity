已查地图：命中（`M03-W0-third-order-axis-point`）⟹ `W=0` 四点最小结构扫描，不开新案
D0: 本档对象 = **四点扫描**（`E_-` 轴点/非轴点 + `E_+` 轴点/非轴点）＋ ⭐**`C_e` 在两侧变号（先生猜想不成立）** ＋ ⭐**"自由方向驱动"对偶律** ＋ **`\partial Z_3/\partial\nu_2\equiv0` 四点普适** ＋ 统一判据
D1: 1（首次给出跨两侧的四点结构对照与新判据）
[RESEARCH]

# **`W=0` 四点最小结构扫描**

## §1 四点结果（`t=\tfrac14` 固定）

```
$$\begin{array}{c|c|c|c|c|c}
\text{点} & \tau_0 & \tau_3 & \partial Z_3/\partial\mu & \partial Z_3/\partial\nu_h & \partial Z_3/\partial\nu_2\\\hline
E_-\ \text{轴点}(\beta=\tfrac1{20}) & \tfrac{\sqrt{35}}2 & 0 & \mathbf{+0.6761} & -7.2190 & \mathbf{0}\\
E_-\ \text{非轴}(\tau_3=1) & \sqrt{114}+\tfrac{\sqrt{4515}}6 & 1 & \mathbf{+2.5598} & -53.9974 & \mathbf{0}\\
E_+\ \text{轴点}(\beta=\tfrac3{10}) & 0 & \tfrac{\sqrt{210}}4 & \mathbf{-8.8844} & \mathbf{+0.5521} & \mathbf{0}\\
E_+\ \text{非轴}(\tau_0=1) & 1 & \sqrt{259}+\tfrac{21\sqrt{10}}4 & \mathbf{-80.7136} & \mathbf{+2.5298} & \mathbf{0}
\end{array}$$ ✓✓✓
$$\quad \text{四点 }W=0\ \text{精确成立（}w_a+w_f=0\text{）};\quad A,B,D\ \text{按侧取号}$$ ✓
```

## §2 ⚠️ 先生猜想不成立：`C_e` 在两侧**变号**

```
$$\text{先生期望}:\ \boxed{C_e=\partial_\mu Z_3>0\ \text{在 }W=0\ \text{曲线上恒正}}\ \Longrightarrow\ \textbf{不成立}$$ ✗
$$\quad E_-\ \text{侧}: C_e=+0.6761,\ +2.5598\ (>0\ \checkmark);\qquad E_+\ \text{侧}: C_e=-8.8844,\ -80.7136\ (<0\ \times)$$ ✓✓
$$\Longrightarrow\ \textbf{不存在统一的 }e_e\ \text{驱动机制};\ \text{但见 §3 的更强替代判据}$$ ✓
```

## §3 ⭐ 替代判据（各点均成立）：**"自由方向驱动"对偶律**

```
$$\text{锥对 }\varepsilon^2\text{ 阶核自由的限制}:\ v_e=0\Rightarrow\mu\ge0;\quad v_h=0\Rightarrow\nu_h\ge0;\quad v_e>0\Rightarrow\mu\ \text{自由};\quad v_h>0\Rightarrow\nu_h\ \text{自由}$$
$$\begin{array}{c|c|c|c|c}
\text{点} & v_e & v_h & \text{可用自由方向} & \text{该方向系数}\\\hline
E_-\ \text{轴} & >0 & 0 & \mu\ (\text{自由}) & +0.6761>0\ \checkmark\\
E_-\ \text{非轴} & >0 & >0 & \mu,\nu_h & +2.5598>0\ \checkmark\\
E_+\ \text{轴} & 0 & >0 & \nu_h\ (\text{自由}) & +0.5521>0\ \checkmark\\
E_+\ \text{非轴} & >0 & >0 & \mu,\nu_h & +2.5298>0\ \checkmark
\end{array}$$ ✓✓✓
$$\boxed{\textbf{对偶律}:\ \text{在每一点},\ \text{至少一条\textbf{不受锥符号限制}的 }e\text{-型核方向系数严格为正}}$$ ✓✓✓
$$\qquad \text{且被 }v\ \text{占用而受限的方向系数恰好为负（}E_-\ \text{轴}:\nu_h\ge0\ \text{但系数}<0;\ E_+\ \text{轴}:\mu\ge0\ \text{但系数}<0\text{）}$$
$$\qquad \Longrightarrow\ \text{取自由方向为正、受限方向为零} \Longrightarrow \boxed{Z_3>0\ \text{可达}\ \textbf{四点皆可}}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\textbf{四点均为三阶可穿透（无需四阶）}}$$ ✓✓✓
```

## §4 ⭐ `\nu_2` 系数**四点全部为零**（普适结构指纹）

```
$$\boxed{\partial Z_3/\partial\nu_2\equiv0\ \text{在全部四点}}$$ ✓✓✓
$$\quad \text{与 }W_\beta\ \text{中 }\tau_2\ \text{缺席、（}b,g\text{）反对称方向不参与二阶障碍\textbf{同一机制}}$$
$$\Longrightarrow\ \textbf{普适结构指纹}:\ (b,g)\ \text{反对称核方向与“不可自由调配量”}\ W\ \text{及 }Z_3\ \textbf{双双正交}$$
$$\qquad \text{（三处独立出现：}W_\beta\ \text{的 }\tau_2\ \text{缺席}；Z_3\ \text{的 }\nu_2=0\ \text{（轴点）}；Z_3\ \text{的 }\nu_2=0\ \text{（非轴点）}）$$ ✓✓✓
```

## §5 阶段结论与边界

```
$$\textbf{可记录的阶段结论}:$$
$$\quad \text{① }W=0\ \text{二阶边界在 }E_-/E_+\ \text{代表性分支上\textbf{均存在三阶穿透方向}};\ \text{驱动方向为\textbf{不被 }v\ \text{占用的自由 }e\text{-型方向}};$$
$$\quad \text{② }(b,g)\ \text{反对称核方向对二阶与三阶障碍\textbf{均不贡献}（普适正交，}4/4\text{）};$$
$$\quad \text{③ 先生的 }C_e>0\ \text{统一猜想\textbf{被否}，替代为"自由方向驱动"对偶律（4/4 成立）}.$$
$$\textbf{不证明}:\ \text{(i) 四阶及以上};\ (\text{ii) 实际有限 }\delta>0\ \text{构造};\ (\text{iii) 整条 }W=0\ \text{曲线（仅四点）};\ (\text{iv) 其它 }t\ \text{值}$$ ✗✗
$$\text{下一堵真墙（先生所指）}:\ \boxed{\text{能否把三阶穿透升级为实际有限 }\delta>0\ \text{构造？}}$$ ✓✓
【⛔ 纪律】 本轮为**精确符号计算**（含 }\sqrt{4515},\sqrt{57190},\sqrt{1110},\sqrt{2590}$$）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 三阶判定为渐近展开的必要条件层；"三阶可穿透" ≠ "存在真实解" ✓

## §附 【技术词回查】（补录）
```
技术词 duality          命中文件数=63   :: ./MASTER-NOGO-AND-LIVE-PATHS.md ./O3-mechanism-audit-and-ontology.md ./V145-archimedean-boundary-three-gate-audit-deninger-hit.md 
技术词 free direction   命中文件数=0    :: 
```
