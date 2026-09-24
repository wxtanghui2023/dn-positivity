已查地图：命中（`M03-P2ii-first-order-attempt-and-three-corrections`）⟹ 一阶线性化与封口证书，不开新案
D0: 本档对象 = ⭐**一阶封口证书**：`9` 参数线性化（`J` 秩 `5`、切空间维数 `4`）＋ **通解** ＋ **`u_a+u_f=-1`（与 `\beta,t` 无关）** ＋ **一阶锥不可行** ＋ **结构解释（迹亏空 vs 零对角）** ＋ 适用范围声明
D1: 1（首次给出 `P2` 侧的一阶封口与 Farkas 型证书）
[RESEARCH]

# **`P2(ii)`：一阶刚性证书（切锥不可行）**

## §1 基点与精确化（一般 `\beta`、`t`）

```
$$\text{族}:\ 9\ \text{参数 }(a,b,c,d,e,f,g,h,i)\ge0;\quad B_{\rm odd}=\begin{pmatrix}a-b&c-d\\ c-d&f-g\end{pmatrix},\quad Q_{\rm even}=\begin{pmatrix}a+b&c+d&\sqrt2e\\ c+d&f+g&\sqrt2h\\ \sqrt2e&\sqrt2h&i\end{pmatrix}$$ ✓
$$\textbf{5 条谱约束（Case II: }\sigma(B)=\{t,-s\},\ \sigma(Q)=\{1,t,-s\}\text{）}:$$
$$\quad F_1=(a-b)+(f-g)-(t-s);\quad F_2=(a-b)(f-g)-(c-d)^2+ts;\quad F_3=(a+b)+(f+g)+i-(1+t-s);$$
$$\quad F_4=e_2(Q)-(t-s-ts);\quad F_5=\det Q+ts$$ ✓✓
$$\qquad \text{（}\operatorname{tr}A=2a+2f+i=1+2t-2s\ \text{与}\ F_1+F_3\ \text{自动相容，}\textbf{不构成独立方程}）$$ ✓
$$\text{基点（}b=\beta\ \text{的一般形式）}:\ a=f=e=h=0,\ g=\tfrac{1-t}2-\beta,\ i=t,\ c=\tfrac{W+V}2,\ d=\tfrac{W-V}2,$$
$$\qquad W=\sqrt{\beta g+s_0},\quad V=\sqrt{\beta g+ts_0};\qquad s_0=\tfrac{1+t}2\ (\delta=0)$$ ✓✓
$$\text{（}t=\tfrac9{20},\ \beta=\tfrac{1-t}4=\tfrac{11}{80}\ \text{时精确值}: (a,b,c,d,e,f,g,h,i)=(0,\tfrac{11}{80},\tfrac{29}{40},\tfrac{11}{80},0,0,\tfrac{11}{80},0,\tfrac9{20}),\ W=\tfrac{69}{80},\ V=\tfrac{47}{80}\ \checkmark\text{）}$$ ✓✓
```

## §2 ⭐ 线性化与一阶封口

```
$$\textbf{线性化}:\ x=x^{(0)}+\delta u,\ s=s_0+\delta \Longrightarrow \boxed{Ju=r},\quad J=\partial_xF|_{0}\ (5\times9),\quad r=-\partial_sF|_{0}$$ ✓✓
$$\boxed{\operatorname{rank}J=5}\ (\textbf{满行秩};\ \text{对一切 }\beta,t\ \text{成立}) \Longrightarrow \textbf{切空间维数}=9-5=\boxed{4}$$ ✓✓✓
$$\qquad \textbf{（校正计数}:\ \text{独立谱约束是 }5\ \text{条而非 }4\ \text{条};\ \text{维数 }4\ \text{而非 }5\text{）}$$ ✓✓
$$\textbf{通解}:\ (u_a,u_b,u_c,u_d,u_e,u_f,u_g,u_h,u_i)=(-\tau_1-1,\ -\tau_2,\ \cdots,\ \tau_0,\ \tau_1,\ \tau_2,\ \tau_3,\ 0)$$ ✓✓
$$\Longrightarrow\ \boxed{u_a=-\tau_1-1,\qquad u_f=\tau_1,\qquad u_e=\tau_0,\qquad u_h=\tau_3,\qquad u_i=0}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\,u_a+u_f=-1\quad(\textbf{与 }\beta,t,\tau\ \textbf{全部无关})\,}$$ ✓✓✓
$$\textbf{一阶锥（非负性）}:\ a,e,f,h\ \text{在基点恰为 }0 \Longrightarrow \text{一阶必须}\ \boxed{u_a\ge0,\ u_e\ge0,\ u_f\ge0,\ u_h\ge0}$$ ✓✓
$$\qquad \text{但 }u_a+u_f=-1\ \text{而}\ u_a,u_f\ge0\Rightarrow u_a+u_f\ge0\ \Longrightarrow \boxed{\textbf{矛盾}}$$ ✓✓✓
$$\boxed{\textbf{结论（一阶封口）}:\ \text{在 }Z_2\text{-Case II 边界族上},\ \textbf{不存在}\ \delta>0\ \text{的一阶可行方向}}$$ ✓✓✓
$$\textbf{Farkas 形式}:\ \text{取 }y=(y_1,\dots,y_5)\ \text{使 }y^TJ=\mathbf e_a+\mathbf e_f\ (\text{即 }u_a+u_f)\ \Longrightarrow\ y^Tr=-1<0\ \text{而锥侧要求 }\ge0$$ ✓✓✓
```

## §3 结构解释（为什么边界刚性）

```
$$\text{迹恒等式}:\ 2a+2f+i=1+2t-2s\ \Longrightarrow\ \text{一阶}:\ 2u_a+2u_f+u_i=-2$$ ✓
$$\qquad \text{而切空间强制}\ \boxed{u_i=0}\ (\text{第 5 对角在切空间内\textbf{冻结}}) \Longrightarrow u_a+u_f=-1$$ ✓✓
$$\text{读法}:\ \delta>0\ \text{要求总对角 }2a+2f+i\ \textbf{下降}\ 2\delta;\ \text{但 }i\ \text{一阶冻结},\ \text{故必须由 }a,f\ \text{承担};$$
$$\qquad \text{而 }a,f\ \text{在基点恰为 }0\ \text{且须}\ge0 \Longrightarrow \textbf{无路可走}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\text{“迹亏空必须由恰好为零的对角元承担”}=\textbf{结构性障碍}}$$ ✓✓（**先生预告的 }(3d)\text{ 型结构障碍** ✓）
```

## §4 适用范围与纪律（不得夸大）

```
$$\text{本档证明的是}:\ \boxed{Z_2\text{-Case II 边界族的\textbf{一阶}（线性尺度）封口}}$$ ✓✓
$$\textbf{不证明}:\ \text{(i) 二阶/}\sqrt\delta\ \text{尺度穿透不存在};\ (\text{ii) 整个 }Z_2\ \text{族封口};\ (\text{iii) }S\ \text{不可实现}$$ ✗✗
$$\text{（若取 }u=\varepsilon v,\ \delta=\varepsilon^2\ \text{即 }\sqrt\delta\ \text{尺度} \Longrightarrow \text{线性系统退化为 }Jv=0\ \text{型},\ \text{需二阶分析，见下一步）}$$ ✓
$$\text{已知相关结果}:\ \delta\le t/2\ (\text{零阶迹预算})\ \text{在 }S\ \text{上自动满足} \Longrightarrow \text{零阶有余量，一阶被堵}$$ ✓✓
【⛔ 纪律】 本轮为**符号线性代数**（sympy 精确）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §2 的秩与通解为 sympy 精确（一般 `\beta,t`）；结论限于一阶切锥；**本档不含任何"可实现"结论** ✓

## §附 【技术词回查】（补录）
```
技术词 tangent cone     命中文件数=0    :: 
技术词 Farkas           命中文件数=12   :: ./C3880-standalone-paper-packaging-of-the-cone-separation-assets.md ./C3870-primal-attainment-six-active-system-and-c-star-equals-1-over-L.md ./C3868-kkt-to-farkas-proportionality-isomorphism.md 
```
