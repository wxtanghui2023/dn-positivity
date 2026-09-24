已查地图：命中（`M03-3a-proof-chain-alignment-and-sharpness`）⟹ `(3b)` 条带内"与 high-trace 无关"的判定，不开新案
D0: 本档对象 = ⭐**幂和型必要条件在条带内的表现**：`D_{\rm PS}(t,\varepsilon)` 精确式＋因式分解＋临界闭式 `\varepsilon_2(t)` ＋ **新不可行区 `W_{\rm PS}\subset R\setminus W`（即 `W\cup W_{\rm PS}\supsetneq W`）** ＋ 控制组（plain JLL 不咬）＋ 依赖待核（Loewy 2021 逐字）
D1: 1（首次在条带内找到**与 high-trace 机制无关**的新必要条件且它给出 `W` 的真扩张候选）
[RESEARCH]

# **`(3b)`：幂和必要条件在条带内咬掉一块（`W` 真扩张候选）**

## §1 检验对象与硬规则

```
$$\text{目标区域}:\ \varepsilon\in(4t-2,\ 0)\ (\text{本行条带}=\text{2026 }W\ \text{右侧});\quad \text{已知}:\ Soules\text{-}1\ \text{排除};\ \text{high-trace／Lemma 4.2 失效（余量 }\varepsilon/18<0\text{）}$$ ✓
$$\textbf{硬规则（先生）}:\ \text{只检验是否产生\textbf{与 high-trace 无关}的新必要条件};\ \text{若仍落在同一门槛}\Longrightarrow\textbf{标"同墙重复"并转向}$$ ✓✓
$$\text{检验对象（}\textbf{与 high-trace 机制无关}）:\ \textbf{幂和型必要条件}——y:=\lambda_3-s_1\ge0\ \text{时}\ \boxed{s_3\ \ge\ s_1^3+6\,(s_1^2y+s_1y^2)}\ (\text{Loewy 2021，先生引用})$$ ✓✓
```

## §2 精确计算

```
$$\lambda(t,\varepsilon)=\bigl(1,t,t,-(q+\varepsilon),-(q+\varepsilon)\bigr),\ q=\tfrac{5-7t}{2};\quad s_1=S=9t-4-2\varepsilon;\quad y=\lambda_3-s_1=4-8t+2\varepsilon$$ ✓
$$s_3=1+2t^3-2(q+\varepsilon)^3$$
$$\boxed{D_{\rm PS}(t,\varepsilon):=s_3-\bigl[s_1^3+6(s_1^2y+s_1y^2)\bigr]=-\frac34\bigl(-2\varepsilon+9t-3\bigr)\bigl(4\varepsilon^2-24t\varepsilon+16\varepsilon+31t^2-46t+15\bigr)}$$ ✓✓✓（sympy 精确因式分解）
$$\text{二次因子之较大根（闭式）}:\ \boxed{\varepsilon_2(t)=3t-2+\tfrac12\sqrt{5t^2-2t+1}}$$ ✓✓（判别式 }(16-24t)^2-16(31t^2-46t+15)=16(5t^2-2t+1)$$）
$$\text{在条带内 }y\ge0\ \text{恒成立}（\varepsilon=4t-2\ \text{时 }y=0,\ \varepsilon\to0^-\ \text{时 }y\to4-8t>0\text{）}\Longrightarrow \textbf{不等式前提满足}$$ ✓✓
$$

## §3 ⭐ 结论：`W` 的真扩张候选（且机制独立）

```
$$D_{\rm PS}<0\iff \varepsilon>\varepsilon_2(t)\ (\text{在本条带内}),\qquad \varepsilon_2(t)<0\iff t<\tfrac{15}{31}\approx0.48387$$ ✓✓
$$\boxed{W_{\rm PS}:=\Bigl\{\lambda(t,\varepsilon):\ \tfrac49<t<\tfrac{15}{31},\ \ \varepsilon_2(t)<\varepsilon<0\Bigr\}\ \subsetneq\ R\setminus W}$$ ✓✓✓
$$\text{（因 }\varepsilon<0\Rightarrow9b-S=4+2\varepsilon<4\Rightarrow\lambda\notin W;\ \text{而 }D_{\rm PS}<0\Rightarrow\textbf{不可实现}）$$
$$\Longrightarrow\ \boxed{W\ \cup\ W_{\rm PS}\ \supsetneq\ W\ \text{为不可行区域}}\quad(\textbf{条带右侧薄片},\ \text{宽}=2-3t-\tfrac12\sqrt{5t^2-2t+1}\approx0.09\text{–}0.14)$$ ✓✓✓
$$\text{机制独立性}:\ D_{\rm PS}\ \text{来自}\textbf{幂和}\ (\text{迹}) \text{结构},\ \text{与对角移位／高迹必要条件／五环约化\textbf{无关}};\ \text{亦与 Soules 构造无关}$$ ✓✓✓
$$\text{剩余未决夹缝}:\ \Bigl\{\varepsilon\in\bigl(4t-2,\ \varepsilon_2(t)\bigr),\ t\in(\tfrac49,\tfrac{15}{31})\Bigr\}\ \text{—— 此处}: \text{2026 机制失效}\wedge\text{Soules-1 排除}\wedge\text{幂和条件满足}$$ ✓✓
```

## §4 控制组（防止误判）

```
$$\text{plain JLL}（s_3\ge0）:\ \text{条带内}s_3=1+2t^3-2(q+\varepsilon)^3>0\ \text{恒成立}\ (\text{例 }t=0.45,\varepsilon=-0.2:\ s_3=0.42>0)\Longrightarrow \textbf{不咬}$$ ✓
$$\text{Perron／迹}\ (\lambda_1\ge|\lambda_i|,\ S\ge0):\ \text{条带内恒满足}\Longrightarrow \textbf{不咬}$$ ✓
$$\Longrightarrow\ \text{咬掉薄片的\textbf{是强化项 }6(s_1^2y+s_1y^2)=O(y)},\ \text{非普通幂和};\ \textbf{机制判定：非"同墙重复"}$$ ✓✓✓
```

## §5 ⚠️ 依赖与待核（不得跳过）

```
$$\textbf{(D1) 逐字核}:\ \text{Loewy 2021 的强化不等式（ELA，免费 PDF）必须逐字核实}（含前提：}y\ge0\ \text{是否还需其他条件；是否要求 }\in R\text{）$$ ⚠️⚠️
$$\qquad \text{本条一切不可行结论都依赖该不等式};\ \textbf{未核前只能写"若该式成立"}$$ ✓
$$\textbf{(D2) 新颖性}:\ \text{Loewy 2021 已证"此前未知区域中的非实现点"}\Longrightarrow W_{\rm PS}\ \text{是否已含于其例};$$
$$\qquad \text{2026 原文称 }R\setminus W\ \text{"potentially realizable"}——\ \text{若 }W_{\rm PS}\ \text{早已被 Loewy 覆盖},\ \text{则该表述需\textbf{细化为"减去幂和排除区"}}$$ ✓✓
$$\textbf{(D3) 几何自检}:\ \varepsilon_2(\tfrac{15}{31})=0\ \checkmark\ (\text{与 }D_{\rm PS}(\varepsilon=0)=0\ \text{相接});\ \ \varepsilon_2(\tfrac49)=-\tfrac23+\tfrac{\sqrt{89}}{18}\approx-0.1426\ \checkmark;\ \ \text{与条带下界 }4t-2\ \text{分离良好}$$ ✓
```

## §6 下一步

```
$$\boxed{\text{(i)}}\ \text{取 Loewy 2021 ELA 原文，逐字核实强化不等式与前提}（\text{这决定 }W_{\rm PS}\ \text{是否成立}）$$ ✓✓
$$\boxed{\text{(ii)}}\ \text{与原文区域比对新颖性};\ \text{若新颖}\Longrightarrow\ \textbf{登档为 }W\ \text{扩张资产};\ \text{若不新颖}\Longrightarrow\ \text{登记为"已知边界细化"}$$ ✓
$$\boxed{\text{(iii)}}\ \text{剩余夹缝 }(4t-2,\varepsilon_2(t))\ \text{内继续找与 high-trace 无关的机制}（\text{如更高阶幂和／}s_5\ \text{型／}S\ \text{型必要条件}）$$ ✓✓
【⛔ 纪律】 本轮为**解析计算**（sympy 精确因式分解，无搜索）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §2/§3 为**本行自证**；§5 的 (D1)(D2) **必须先做完**才能升级为公开结论 ✓

## §附 【技术词回查】（补录）
```
技术词 power sum        命中文件数=3    :: ./C3822-E0-multi-moment-feasibility-pivot.md ./C184-M3-damped-certified-0.35-plus-literature-pointer-Littlewood-cosine-sum.md ./M03-SPEC-CLOSURE-and-N5-first-assembly.md 
技术词 necessary condition 命中文件数=2    :: ./P8-CLASSIC-SOURCES-li1997-bombieriLagarias1999.md ./P8b-oesterle-rigor-status.md 
```
