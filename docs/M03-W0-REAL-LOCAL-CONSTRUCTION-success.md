已查地图：命中（`M03-W0-four-point-minimal-scan`）⟹ `W=0` 点真实局部构造，不开新案
D0: 本档对象 = ⭐**真实局部构造成功**（`\delta=10^{-4}`、`F=0` 残差 `10^{-52}`、`x\ge0`）＋ **`5\times5` 块退化结构（`a,f` 不能同时自由：`0/126`）** ＋ **`R\setminus W` 定位核验** ＋ 严谨性与新性边界
D1: 1（首次把三阶形式穿透升级为真实非负局部解）
[RESEARCH]

# **`W=0` 点：真实局部构造成功**

## §1 IFT 结构（含一处关键退化）

```
$$\operatorname{rank}J=5;\quad 5\times5\ \text{非退化子块}=13/126\ (\text{含 }i\text{ 的块最大 }|\det|=3.49219)$$ ✓
$$\boxed{\text{“}a,f\text{ 同时自由”的非退化块数}=0/126}\ \Longrightarrow\ \textbf{不存在以 }(a,f)\ \text{为自由坐标的 IFT 图卡}$$ ✓✓✓
$$\quad \text{（先生预告的情形 B：非标准 IFT；但存在以 }a\ \text{自由（或 }f\ \text{自由）的图卡）}$$ ✓
$$\text{采用}: \operatorname{dep}=(c,d,f,g,i)\ (|\det|=3.49219),\quad \operatorname{free}=(a,b,e,h)$$ ✓
```

## §2 ⭐ 真实局部解（`\delta=\varepsilon^2=10^{-4}`）

```
$$\text{取 }a=h=0,\ e=\varepsilon\tau_0=\varepsilon\tfrac{\sqrt{35}}2,\ b=\beta=\tfrac1{20};\quad \text{Newton 解 }(c,d,f,g,i)$$ ✓
$$\begin{array}{c|ccccccccc}
\text{变量} & a & b & c & d & e & f & g & h & i\\\hline
\text{值} & 0 & 0.05 & 0.607552358 & 0.192185050 & 0.029580399 & 3.86754\times10^{-7} & 0.325100387 & 0 & 0.249799226
\end{array}$$ ✓✓✓
$$\boxed{\max|F|=1.095\times10^{-52}}\quad(\textbf{五条谱约束精确达成})\Longrightarrow \textbf{谱精确}=\{1,\tfrac14,\tfrac14,-s,-s\},\ s=\tfrac58+10^{-4}$$ ✓✓✓
$$\boxed{\text{全部 }9\ \text{坐标}\ge0}\ \checkmark\ (\min=0\ \text{于 }a,h)$$ ✓✓✓
$$\text{（}\varepsilon=0.005\ \text{亦成功};\ f=+2.408\times10^{-8}>0\ \checkmark\text{）}$$ ✓
```

## §3 定位核验：位于 2026 论文的**未覆盖区** `R\setminus W`

```
$$S=\operatorname{tr}=0.2498=1+2t-2s\ \checkmark;\quad \lambda_3=t=\tfrac14=0.25;\quad \lambda_1=1$$ ✓
$$\text{R 条件}:\ S>0\ \checkmark;\quad S<\min\{\lambda_3,\lambda_1/2\}=\tfrac14\ \checkmark\ (0.2498<0.25)$$ ✓
$$W\ \text{条件}:\ 4\lambda_1\le 9\lambda_3-S\ \text{即}\ 4\le2.0002\ \textbf{为假}\Longrightarrow \boxed{\text{落在 }R\setminus W\ (\text{2026 方法未覆盖})}$$ ✓✓✓
$$\Longrightarrow\ \textbf{本档给出一族（}\delta>0\text{）}\ R\setminus W\ \text{内的\textbf{非负实对称实现}}$$ ✓✓✓
```

## §4 严谨性与新性边界（不夸大）

```
$$\textbf{已建立}:\ \text{在 }(t,\beta)=(1/4,1/20)\ \text{处},\ \delta=10^{-4}>0,\ \exists x\ge0\ \text{使 }F(x,s_0+\delta)=0\ (\text{残差 }10^{-52},\ 50\ \text{位精度})$$ ✓✓
$$\textbf{严谨性补强（待做）}:\ \text{① Krawczyk/区间验证以给严格包含证书};\ \text{② 或用有理数微扰 + 精确消元};\ \text{③ 或直接给显式精确构造}$$ ⚠️
$$\textbf{新性（待核）}:\ \text{文献是否已记录 }R\setminus W\ \text{内的可实现点};\ \textbf{须先查再声称新性}$$ ⚠️
$$\textbf{不证明}:\ \text{真实解在 }\delta\ \text{上的}区间长度;\ \text{整族};\ E_+\ \text{侧};\ \text{其它 }t;\ \text{SNIEP n=5 的整体分类}$$ ✗
$$【⛔ 纪律】 本轮为**数值构造（50 位）+ 精确定位核验**；`U_{2,3}` 暂停；**不回 RH** ✓

## §附 【技术词回查】（补录）
```
技术词 explicit construction 命中文件数=1    :: ./E5-lagarias-gn-explicit.md 
技术词 interval certificate 命中文件数=0    :: 
```
