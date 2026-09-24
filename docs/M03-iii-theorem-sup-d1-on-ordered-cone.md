已查地图：命中（`M03-soules2-implementation-unfaithful-and-soules1-confirmed`）⟹ `(iii)` 解析不可能性，不开新案
D0: 本档对象 = ⭐**定理（本行自证）**：`\sup` 在有序锥上 `d_1\le-\tfrac{106}{375}<0`；**`Gate A` 精确式** ＋ **四方向导数定号（`Gate B` 打通）** ＋ 下降链证明 ＋ **结论的严格措辞（`x` 序前提）** ＋ 无序 `x` 的数值旁证
D1: 1（首次把 `Soules-1` 在 `\Lambda_*` 上的失败由数值残迹升级为**解析定理**）
[RESEARCH]

# **`(iii)` 定理：有序锥上 `d_1\le-\tfrac{106}{375}<0`**

## §1 `Gate A`：精确式（`x_1=1`，变体 A，双重保真已验证）

```
$$d_1(x)=\frac{1}{T_5}-\frac{41}{50}\frac{x_2^2}{T_2}-\frac{41}{50}\frac{x_3^2}{T_2T_3}+\frac{12}{25}\frac{x_4^2}{T_3T_4}+\frac{12}{25}\frac{x_5^2}{T_4T_5},\qquad T_2=1+x_2^2,\ T_3=T_2+x_3^2,\ T_4=T_3+x_4^2,\ T_5=T_4+x_5^2$$ ✓✓
$$\text{sympy 通分形式（用于定号）}:\ d_1=\frac{-41x_2^4-82x_2^2x_3^2-41x_2^2x_4^2-41x_2^2x_5^2+9x_2^2-\cdots+24x_4^2+24x_5^2+50}{50\,(x_2^4+2x_2^2x_3^2+\cdots+x_5^2+1)}$$ ✓
$$\text{核验}:\ d_1(1,1,1,1,1)=-\tfrac{106}{375}\ \checkmark$$ ✓✓
```

## §2 `Gate B`：四方向导数定号（**打通**）

```
$$\boxed{\frac{\partial d_1}{\partial x_5}=-\frac{26x_5}{25\,T_4^{\prime 2}}\le0}\ \text{其中 }T_4=x_2^2+x_3^2+x_4^2+x_5^2+1$$ ✓✓✓（sympy \textbf{精确}核实）
$$\text{代入 }x_5=x_4:\ \boxed{\frac{\partial}{\partial x_4}=-\frac{52x_4}{25\,(x_2^2+x_3^2+2x_4^2+1)^2}<0}$$ ✓✓✓
$$\text{再代 }x_5=x_4=x_3:\ \boxed{\frac{\partial}{\partial x_3}=-\frac{13x_3\,P_3}{25\,(x_2^2+x_3^2+1)^2(x_2^2+3x_3^2+1)^2}<0},$$
$$\qquad \qquad P_3=11x_2^4+42x_2^2x_3^2+22x_2^2+51x_3^4+42x_3^2+11\ \textbf{（全部系数为正 ⟹ }P_3>0\text{）}$$ ✓✓✓
$$\text{再代 }x_5=x_4=x_3=x_2:\ \boxed{\frac{\partial}{\partial x_2}=-\frac{26x_2\,(96x_2^4+56x_2^2+9)}{25\,(2x_2^2+1)^2(4x_2^2+1)^2}<0}$$ ✓✓✓（系数全正）
```

## §3 下降链 ⟹ 定理

```
$$\text{对任意 }1\le x_2\le x_3\le x_4\le x_5:$$
$$\quad d_1(x)\ \le\ d_1(1,x_2,x_3,x_4,x_4)\ \le\ d_1(1,x_2,x_3,x_3,x_3)\ \le\ d_1(1,x_2,x_2,x_2,x_2)\ \le\ d_1(1,1,1,1,1)$$ ✓✓✓
$$\qquad \text{（每步：该方向偏导严格为负 ⟹ 把该变量压到其下界 ⟹ 值\textbf{不降}）}$$
$$\Longrightarrow\ \boxed{\sup_{1\le x_2\le x_3\le x_4\le x_5}d_1(1,x_2,x_3,x_4,x_5)=d_1(1,1,1,1,1)=-\frac{106}{375}<0}$$ ✓✓✓
$$\Longrightarrow\ \textbf{对一切递增 }x\textbf{（}0<x_1\le\dots\le x_5\textbf{）},\ d_1(x)<0 \Longrightarrow \text{Soules-1 的判据在该锥上\textbf{恒失败}}$$ ✓✓✓
$$\text{（本轮取代原数值残迹；}x=(1,1,1,1,1)\ \text{确为全局最大点，先生预判正确）}$$ ✓
```

## §4 结论的严格措辞（状态纪律）

```
$$\boxed{\Lambda_*\notin\text{Soules-1 可实现族}\ (\text{递增 }x\ \text{分支})}$$ ✓✓
$$\textbf{不得写}:\ \Lambda_*\notin\mathcal S_5\ \text{或 }\Lambda_*\ \text{不可实现}$$ ✗
$$\textbf{残余前提（须显式标注）}:\ (\text{i})\ \text{本轮只封\textbf{递增 }x\ \text{分支}（因定理单调性注记只在 }0<x_1\le\dots\le x_n\ \text{下把全条件化归 }d_1\ge0\text{）};$$
$$\qquad (\text{ii})\ \text{一般（无序）}x\ \text{须逐项要求 }d_i\ge0\ \text{五条件},\ \text{本轮\textbf{未封}};\quad (\text{iii})\ Soules\text{-}2/LS/ES\ \text{均未封}$$ ✓✓
$$\textbf{无序 }x\ \text{数值旁证（}4000\ \text{样本},\ \text{递增与任意序各半},\ \text{尺度任意）}:\ \min_i d_i<0\ \text{占比}\ \mathbf{\frac{4000}{4000}}$$ ✓✓（旁证非证明）
```

## §5 下一步

```
$$\boxed{\text{(a)}}\ \text{封\textbf{无序 }x\ \text{分支}（困难）};\ \text{或把定理改写为"Soules-1 的\textbf{递增分支}在 }\Lambda_*\ \text{上恒失败"（已足够用作接口）}$$ ✓
$$\boxed{\text{(b)}}\ \text{与 Johnson 的 }D(t)<0\ \text{合并} \Longrightarrow \text{寻找 }W_{\rm new}\supset W\ (\textbf{真正的 }P1)$$ ✓✓
$$\boxed{\text{(c)}}\ \text{补取 Soules 1983 原文（若仍需 }Soules\text{-}2\text{）};\ \text{LS/ES 最后}$$ ✓
【⛔ 纪律】 本轮为**解析证明**（无搜索）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §2/§3 为**本行自证**（sympy 逐式核实偏导）；§4 的三条残余前提**必须随定理一起引用** ✓

## §附 【技术词回查】（补录）
```
技术词 descent chain    命中文件数=1    :: ./TLDC-1-reverse-isomorphism-audit-old-bridges-vs-descent-chain.md 
技术词 ordered cone     命中文件数=0    :: 
```
