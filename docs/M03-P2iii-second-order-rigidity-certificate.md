已查地图：命中（`M03-P2ii-first-order-rigidity-certificate`）⟹ 二阶（`\sqrt\delta` 尺度）封口证书，不开新案
D0: 本档对象 = **Gate 1（`\ker J` 精确结构）** ＋ **Gate 2（`R(v)`、`Jw=-R(v)`、锥判据单标量化）** ＋ ⭐**Gate 3（二阶封口：`W(\tau)=-1-\frac{250\tau_0^2+1380\tau_0\tau_3+250\tau_3^2}{517}\le-1<0`）** ＋ 适用范围
D1: 1（首次给出二阶（`\delta=\varepsilon^2`）尺度的封口与显式证书）
[RESEARCH]

# **`P2(iii)`：二阶刚性证书（`\delta=\varepsilon^2` 尺度封口）**

## §1 Gate 1：`\ker J` 精确结构

```
$$\text{基点 }t=\tfrac9{20},\ \beta=\tfrac{1-t}4=\tfrac{11}{80}\ (\text{专门点}:\ 4\beta+t-1=0):$$
$$\quad (a,b,c,d,e,f,g,h,i)=(0,\tfrac{11}{80},\tfrac{29}{40},\tfrac{11}{80},0,0,\tfrac{11}{80},0,\tfrac9{20})$$ ✓
$$\boxed{\operatorname{rank}J=5,\quad \dim\ker J=4};\qquad \textbf{基向量（该点处非常干净）}:\ \boxed{\ker J=\operatorname{span}\{e_a-e_f,\ e_b-e_g,\ e_e,\ e_h\}}$$ ✓✓✓
$$\quad \text{（}\beta=\tfrac{1-t}4\ \text{时核向量 }v_c=v_d=0\ \textbf{恒成立}:\ c,d\ \text{在 }\varepsilon\ \text{阶不可动）$$ ✓✓
$$\Longrightarrow\ \textbf{核的强制关系}:\ \boxed{v_a+v_f=0},\quad \boxed{v_i=0},\quad \boxed{v_b+v_g=0}$$ ✓✓✓
$$\textbf{锥条件推论}:\ v_a\ge0,\ v_f\ge0\ \Longrightarrow\ \boxed{v_a=v_f=0}\ \Longrightarrow\ \boxed{a,f=O(\varepsilon^2)}\ \textbf{（先生预测的降维）}$$ ✓✓✓
$$\qquad \text{可动的 }\varepsilon\ \text{阶方向}:\ \boxed{v=\tau_0e_e+\tau_3e_h+\tau_2(e_g-e_b)},\quad \tau_0,\tau_3\ge0,\ \tau_2\ \text{自由}$$ ✓✓
```

## §2 Gate 2：二阶方程与单标量判据

```
$$\text{展开}:\ x=x^{(0)}+\varepsilon v+\varepsilon^2w+\cdots,\quad s=s_0+\varepsilon^2;\qquad F(x,s)=0$$
$$\quad \Longrightarrow\ \varepsilon\ \text{阶}:\ Jv=0;\qquad \varepsilon^2\ \text{阶}:\ \boxed{Jw=-R(v)},\quad R(v)=\tfrac12D^2F[v,v]+F_s$$ ✓✓
$$\text{（}J\ \text{满行秩}\Longrightarrow Jw=-R(v)\ \text{恒有解};\ \text{信息全在}\textbf{锥约束})$$ ✓
$$\textbf{锥约束的单标量化}:\ \text{可加核方向 }e_a-e_f\ \text{任意倍数 }\lambda\Longrightarrow (w_a,w_f)\mapsto(w_a-\lambda,\ w_f+\lambda);$$
$$\quad \exists\lambda\ \text{使 }w_a,w_f\ge0\iff \boxed{W(v):=w_a+w_f\ge0}\quad(\textbf{不变量，与代表元选取无关})$$ ✓✓✓
$$\quad w_e,w_h\ \text{可经 }e_e,e_h\ \text{自由增大}\Longrightarrow\ \text{其非负恒可满足};\ \text{故二阶可行性}\iff W(v)\ge0$$ ✓✓
```

## §3 ⭐ Gate 3：二阶封口（精确证书）

```
$$\textbf{精确结果（}t=\tfrac9{20},\ \beta=\tfrac{1-t}4\text{）}:$$
$$\boxed{W(\tau_0,\tau_2,\tau_3)=-\frac{250\tau_0^2+1380\tau_0\tau_3+250\tau_3^2}{517}-1}$$ ✓✓✓
$$\quad \text{（}\textbf{与 }\tau_2\ \text{无关};\ w_a=w_f\ \text{对称};\ w_e=w_h=0\ \text{（最小范数解））}$$ ✓✓
$$\text{锥 }\tau_0,\tau_3\ge0\ \text{上}: \quad 250\tau_0^2+1380\tau_0\tau_3+250\tau_3^2\ \ge0\ \text{（各项非负）} \Longrightarrow \boxed{W\le-1<0}$$ ✓✓✓
$$\qquad \text{（二次型矩阵特征值 }-\tfrac{20}{11},\ \tfrac{40}{47},\ 0:\ \text{正特征向量}=(1,-1)\ \textbf{在锥外} \Longrightarrow \text{锥上恒}\le0\text{）}$$ ✓✓
$$\Longrightarrow\ \boxed{\textbf{二阶封口}:\ \text{对一切锥可行核方向 }v,\ \text{不存在 }w\ \text{使 }Jw=-R(v)\ \text{且 }w_a,w_f\ge0}$$ ✓✓✓
$$\textbf{交叉核验}:\ v=0\ (\tau=0)\ \Longrightarrow\ W=-1,\ \text{与一阶证书 }u_a+u_f=-1\ \textbf{精确一致}$$ ✓✓✓
$$\textbf{迹恒等式在 }\varepsilon^2\ \text{阶（精确）}:\ 2w_a+2w_f+w_i=-2\Longrightarrow w_i=-2-2W\ge0\ (\text{与 }W\le-1\ \text{相容})$$ ✓✓
```

## §4 综合结论与适用范围

```
$$\boxed{\text{综合}:\ Z_2\text{-Case II 边界族在 }O(\delta)\ \text{与 }O(\sqrt\delta)\ \text{两个尺度上均被堵}}$$ ✓✓✓
$$\text{读法（结构）}:\ \text{迹亏空 }2\delta\ \text{必须由 }a,f\ \text{承担，而}\)a,f\ \text{的}\varepsilon\text{-阶被核强制为零、}\varepsilon^2\text{-阶被谱约束反号} \Longrightarrow \text{无路可走}$$ ✓✓
$$\textbf{不证明}:\ \text{(i) }\varepsilon^3\ \text{及更高阶};\ (\text{ii) 其它基点 }\beta\ne\tfrac{1-t}4;\ (\text{iii) 整个 }Z_2\ \text{族};\ (\text{iv) }S\ \text{不可实现}$$ ✗✗
$$\qquad \text{注}:\ \ker J\ \text{结构为一般 }(\beta,t)\ \text{符号结果};\ W\ \text{公式为 }t=\tfrac9{20}\ \text{数值点、}\beta\ \text{取自族内专门点}$$ ✓
【⛔ 纪律】 本轮为**符号/精确计算**（sympy，一元有理数）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 二阶封口限于 `Z_2`-`Case II` 边界族的 `\varepsilon^2` 尺度；**本档不含任何"可实现"结论** ✓

## §附 【技术词回查】（补录）
```
技术词 second order     命中文件数=0    :: 
技术词 rigidity         命中文件数=196  :: ./p36-3-gram-rigidity.md ./V172-rigidity-source-separation-FAS-trichotomy.md ./FINAL-LABEL-20260916-search-space-closed-proof-space-not-closed.md 
```
