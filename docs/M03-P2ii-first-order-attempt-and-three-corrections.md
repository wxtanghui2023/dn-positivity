已查地图：命中（`M03-P2i-nine-param-audit-case-decomposition-and-search-status`）⟹ `P2(ii)` 一阶尝试与三项更正，不开新案
D0: 本档对象 = **三项更正**（先生 `(\theta_0,\phi_0)` 未通过核验；我方首次扫描参数化错误；我方解方程漏 `\operatorname{tr}Q`）＋ **正确边界结构（`a=f=0` 迹零强制）** ＋ **对称子族的精确判定** ＋ 后续正确一阶设定
D1: 1（首次给出 `\delta=0` 边界的正确结构与参数量；纠正三处错误）
[RESEARCH]

# **`P2(ii)`：一阶尝试与三项更正**

## §1 ⚠️ 更正一：先生的 `(\theta_0,\phi_0)` 未通过核验

```
$$\text{取 }t=0.45,\ s_0=\tfrac{1+t}2=0.725;\ \text{先生给出 }\cos^2\theta_0=\tfrac2{t+3},\ \cos^2\phi_0=\tfrac{t+1}{3t+1}$$ ✓（记录）
$$\text{实算}:\ \theta_0=0.705346,\ \phi_0=0.667281 \Longrightarrow Q_{11}=0.275,\ Q_{22}=0,\ Q_{12}=0.8515;\quad B_{11}=0,\ B_{22}=-0.275,\ B_{12}=0.5712$$ ✓
$$\text{支配余量}:\ Q_{11}-|B_{11}|=+0.275\ \checkmark;\quad \boxed{Q_{22}-|B_{22}|=-0.275\ \textbf{不成立}}\ ✗;\quad Q_{12}-|B_{12}|=+0.280\ \checkmark$$ ✓✓✓
$$\Longrightarrow\ \textbf{先生的"两对角支配同时取等号"在该点不成立}（Q_{22}=0\ \text{而}|B_{22}|=0.275\text{）};\ \text{且 }Q_{11}\ne B_{11}\ (0.275\ne0)$$ ⚠️
$$\text{（另：按对称方程解 }(1)(2)\ \text{得 }\cos^2\theta=\tfrac{1+t}{3+t}\ \text{而非 }\tfrac2{3+t};\ \text{该解还给出 }Q_{11}=0\ \text{退化）}$$ ⚠️
```

## §2 ⚠️ 更正二：我方首次扫描的参数化错误

```
$$\text{我首次扫描令 }Q_2=R_\theta\operatorname{diag}(1,-s_0)R_\theta^T,\ B=R_\phi\operatorname{diag}(t,-s_0)R_\phi^T\ \text{并视 }(\theta,\phi)\ \text{独立}$$ ✗
$$\text{但真族中偶块 }[[a+b,\ c+d],[c+d,\ f+g]]\ \text{与奇块 }[[a-b,\ c-d],[c-d,\ f-g]]\ \textbf{共享 }a,b,f,g,c\pm d$$
$$\Longrightarrow\ \text{独立角度化\textbf{过度限制}了族} \Longrightarrow \text{该扫描的"无可行点"结论\textbf{作废}}$$ ✓✓
```

## §3 ⚠️ 更正三（最重要）：我方解方程漏 `\operatorname{tr}Q`

```
$$\text{我曾在对称子族 }(a=f=A,\ b=g=B,\ e=0)\ \text{中只解 }e_2(Q)\ \text{与}\ \det Q,\ \textbf{未加}\ \operatorname{tr}Q = 1+t-s$$ ✗✗
$$\text{结果得到"}\delta>0\ \text{可行点"}\Longrightarrow \textbf{谱检验立即否定}:\ \text{构造矩阵特征值与目标最大偏差达 }0.08\sim0.38\ ✗$$ ✓✓✓（**谱检验挡住一次错误正向结论**）
$$\textbf{根因}:\ \operatorname{tr}Q = 2C+i\ \text{在对称子族下为 }2C+i,\ \text{须 }=1+t-s;\ \text{而 }i=1+2t-2s\ (\text{矩阵迹强制}) \Longrightarrow \boxed{C:=a+b=\tfrac{s-t}2}$$ ✓✓
$$\qquad \text{结合 }A-B=\tfrac{t-s}2 \Longrightarrow \boxed{A=a=f=0,\ B=b=g=\tfrac{s-t}2}\ \text{被强制}$$ ✓✓
$$\Longrightarrow\ \text{对称子族只剩 }(w^2,h^2)\ \text{两未知、两方程}（e_2\ \text{与}\det\text{）};\ \text{数值求解得 }h^2<0\ \textbf{恒成立} \Longrightarrow \boxed{\text{对称子族在 }\delta>0\ \textbf{不可行}}$$ ✓✓
```

## §4 正确的边界结构（`\delta=0`，已核验）

```
$$\text{迹约束}:\ \operatorname{tr}A=2a+2f+i=1+2t-2s;\ \delta=0\Rightarrow \operatorname{tr}A=t;\ \text{4-块迹}=1+t-2s_0=0\Rightarrow\boxed{a=f=0},\ \boxed{i=t}$$ ✓✓✓
$$\text{偶块}:\ [[b,w],[w,g]],\ b+g=1-s_0=\tfrac{1-t}2;\quad \text{谱}\{1,-s_0\}\Rightarrow \boxed{w^2=bg+s_0}$$ ✓✓
$$\text{奇块}:\ [[-b,c-d],[c-d,-g]],\ \text{谱}\{t,-s_0\}\Rightarrow\boxed{(c-d)^2=bg+ts_0}$$ ✓✓
$$\textbf{对角支配自动取等}:\ Q_{11}=b=|\alpha|,\ Q_{22}=g=|\gamma|\ \checkmark;\quad \textbf{唯一实约束}:\ |c-d|\le w\iff ts_0\le s_0\iff\boxed{t\le1}\ \checkmark$$ ✓✓✓
$$\Longrightarrow\ \text{边界配置\textbf{存在}，且为 }1\ \text{参数族 }b\in[0,\tfrac{1-t}2]\ (\text{附离散符号选择})$$ ✓✓
$$\qquad \text{（对照：先生把杀点定位在"正性锥}\Rightarrow Q_{33}>t\text{"，但在正确结构下**对角支配是自动等号**，杀点需重新定位）}$$ ⚠️
```

## §5 下一步（正确的一阶设定）

```
$$\text{一般族（\delta>0）}:\ 9\ \text{个非负参数};\ \text{5 条谱约束}:\ \operatorname{tr}B_{odd}=t-s,\ \det B_{odd}=-ts,\ \operatorname{tr}Q=1+t-s,\ e_2(Q)=t-s-ts,\ \det Q=-ts$$ ✓
$$\text{其中 }\operatorname{tr}A\ \text{与}\ \operatorname{tr}B_{odd}+\operatorname{tr}Q\ \text{自动相容}\ (\text{都}=1+2t-2s) \Longrightarrow 4\ \text{独立约束} \Longrightarrow \text{解集维数 }9-4=5$$ ✓✓
$$\Longrightarrow\ \textbf{一阶问题}:\ \text{在 }5\ \text{维解空间内是否存在} a,b,c,d,e,f,g,h,i\ge0\ \text{的解}\ (\text{小 }\delta>0)$$
$$\qquad \text{方法}:\ \text{先用 }\delta=0\ \text{的显式边界点（如 }b=\tfrac{1-t}4\text{）作线性化},\ \text{解线性系统后用 }Farkas/正性锥判定可行性}$$ ✓✓✓
【⛔ 纪律】 本轮为**精确核验＋数值检验**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 的两处不通过为**独立复算**；§3 的谱检验为**决定性**；**本档不含任何"可实现"结论** ✓

## §附 【技术词回查】（补录）
```
技术词 first order      命中文件数=1    :: ./E18-NOGO-ALIGNMENT-2.md 
技术词 positivity cone  命中文件数=1    :: ./V317-feasible-domain-source-audit-C-T-operator.md 
```
