已查地图：命中（`M03-3b-D2-exact-inclusion-test-verdict`）⟹ `(3b)` 最终登记 ＋ 精确集合差，不开新案
D0: 本档对象 = **(3b) 四点最终登记**（机制 PASS／区域 FAIL／参数化资产 PASS／真残余靶区）＋ ⭐**精确集合差**：`S=\{4/9<t<15/31,\ 4t-2<\varepsilon<\varepsilon_2(t)\}` **非空且 `u>0,\ v>0`（无既有墙触碰）** ＋ 措辞修正（2026 表述）
D1: 1（首次把条带拆为"旧墙覆盖区／真未决区"，并证明真未决区非空且宽度有下界）
[RESEARCH]

# **`(3b)` 最终登记 ＆ 真残余靶区**

## §1 `(3b)` 最终登记（先生指定格式）

```
$$\boxed{(3b)=\text{MECHANISM EXTENSION}\ /\ \text{NO REGION EXTENSION}}$$
$$\textbf{1. 机制层}:\ \boxed{\textbf{PASS}}\ ——\ \text{power-sum necessary condition 与 }(3a)\ \text{的 high-trace 机制\textbf{独立}};\ \text{确实在条带中产生新的"攻击接口"}$$ ✓✓
$$\textbf{2. 区域层}:\ \boxed{\textbf{FAIL（无新区域）}}\ ——\ W_{\rm PS}\subseteq\{\text{JMP-已排除}\}\cup\{\text{Loewy-已排除}\};\ \text{不得登记为 2026 新不可行区域}$$ ✓✓
$$\textbf{3. 参数化资产}:\ \boxed{\textbf{PASS}}\ ——\ \varepsilon_2(t)=3t-2+\tfrac12\sqrt{5t^2-2t+1}\ \text{给出既有幂和墙与本参数化的\textbf{显式解析边界}};$$
$$\qquad\boxed{\tfrac{15}{31}}\ \text{是它首次进入 }\varepsilon<0\ \text{条带的精确阈值}$$ ✓✓
$$\textbf{4. 真正剩余靶区}:\ \text{把 }W_{\rm PS}\ \text{从 residual target 剔除};\ \text{残余}=\Bigl\{\tfrac49<t<\tfrac{15}{31},\ 4t-2<\varepsilon<\varepsilon_2(t)\Bigr\}$$ ✓✓
$$\textbf{措辞修正（先生）}:\ \text{不得说 2026 论文"过度声称"};\ \text{正确表述}:\ \boxed{\text{"}R\setminus W\ \text{是 2026 方法留下的\textbf{候选残区}，但不等同于截至 2026 的\textbf{完整未知区}；}W_{\rm PS}\ \text{给出其中一个已由既有条件排除的具体子区"}}$$ ✓✓
```

## §2 ⭐ 精确集合差：`S` 非空且未被任何既有墙触碰

```
$$S:=\Bigl\{(t,\varepsilon):\ \tfrac49<t<\tfrac{15}{31},\ 4t-2<\varepsilon<\varepsilon_2(t)\Bigr\}$$ ✓
$$\textbf{(a)}\ v>0\ \text{on}\ S:\ v<0\iff b<b_{LO}\iff \varepsilon>\varepsilon_2(t)\ \Longrightarrow\ \varepsilon<\varepsilon_2(t)\Rightarrow \boxed{v>0}\ (\text{在 }LO\ \text{之上})$$ ✓✓
$$\textbf{(b)}\ u>0\ \text{on}\ S:\ \text{关键两条}:\ (\text{i})\ \text{Loewy Cor.\ 3.1}:\ LO\ \text{严格位于 }JMP\ \text{之上（除 }W_4\text{）};\ (\text{ii})\ \frac{\partial u}{\partial b}=-6(a+b+1)(a+3b+1)>0\ \text{于本区};$$
$$\qquad \Longrightarrow\ u|_{LO}>0;\ \text{而 }\varepsilon<\varepsilon_2\Rightarrow b>b_{LO}\Rightarrow u>u|_{LO}>0\ \Longrightarrow\ \boxed{u>0}$$ ✓✓✓
$$\qquad \text{数值核验 }\ u(t,\varepsilon_2(t)):\ 0.0606\ (t=\tfrac49),\ 0.0617\ (\tfrac9{20}),\ 0.0634\ (\tfrac{23}{50}),\ 0.0661\ (\tfrac{12}{25}),\ 0.0664\ (\to\tfrac{15}{31})\ \textbf{全}>0$$ ✓✓
$$\textbf{(c)}\ \text{宽度}:\ \text{width}(t)=\varepsilon_2(t)-(4t-2)>0,\ \text{数值 }0.0797\ (\tfrac49)\to0.0645\ (\tfrac{15}{31})\ \Longrightarrow\ \textbf{有下界 }\tfrac{2}{31}\ \text{附近}$$ ✓✓
$$\textbf{(d)}\ S\subseteq \operatorname{int}D:\ \text{四条不等式逐条成立（样点 }t=0.45,\varepsilon=-0.15:\ 1+a+2b=-0.1\le0;\ 5+2b-7a=0.3\ge0;\ u=0.161\ge0;\ 4ab+1=-0.395\le0）$$ ✓✓
$$\Longrightarrow\ \boxed{S\ \text{未被 JMP、Loewy }v、MN、LM、LS\ \text{任一墙触碰};\ \text{且 2026 机制余量 }\varepsilon/18<0,\ \text{Soules-1 已排除}}$$ ✓✓✓
```

## §3 条带三分解（本档核心产物）

```
$$\text{条带}\ \{\tfrac49<t<\tfrac{15}{31},\ 4t-2<\varepsilon<0\}\ =\ \underbrace{W_{\rm PS}\ (\varepsilon_2<\varepsilon<0)}_{\textbf{旧墙已排除}}\ \cup\ \underbrace{S\ (4t-2<\varepsilon<\varepsilon_2)}_{\textbf{真未决}}$$ ✓✓✓
$$\begin{array}{c|c|c|c}
\text{区} & \text{位置} & \text{状态} & \text{来源}\\
\hline
W & \varepsilon\ge0 & \text{不可实现} & 2026\ (\text{机制锋利，}(3a))\\
W_{\rm PS} & \varepsilon_2<\varepsilon<0 & \text{不可实现（\textbf{旧}）} & \text{Loewy }v<0\ \text{或 JMP }u<0\\
S & 4t-2<\varepsilon<\varepsilon_2 & \boxed{\textbf{未决}} & \text{无墙触碰；Soules-1 排除；2026 机制失效}
\end{array}$$ ✓✓✓
$$\Longrightarrow\ \text{把 }(3a)\ \text{留下的条带进一步拆成"旧墙覆盖区"与"真正未决区"};\ \textbf{不再把整个 }R\setminus W\ \text{当作同质 residual region}$$ ✓✓✓
```

## §4 下一步（只打 `S`）

```
$$\boxed{\text{(3c)}}\ \text{在 }S\ \text{内找\textbf{与 high-trace 无关}的新机制}:\ s_5\ \text{型／更高阶幂和／}S\text{-型必要条件};\ \text{目标}:\ \text{再咬掉 }S\ \text{的一块}$$ ✓✓
$$\boxed{\text{(3d)}}\ \text{或 }P2:\ \text{在 }S\ \text{内换机制尝试构造（直接矩阵构造／LS／ES／Soules-2）};\ \text{成功} \Longrightarrow \Lambda\ \text{类谱的可实现新点}$$ ✓✓
$$\boxed{\text{(3e)}}\ \text{登记两项资产}:\ (\text{i})\ \text{三分解表};\ (\text{ii})\ \varepsilon_2(t)\ \text{的解析边界};\ \text{并注明 }S\ \text{是当前唯一靶区}$$ ✓
【⛔ 纪律】 本轮为**精确代数与原文引用**（无搜索）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 的措辞修正按先生原文；§2(b) 的 `u>0` 由 Loewy Cor.\ 3.1＋单调性给出（非数值推断），数值仅作旁证 ✓

## §附 【技术词回查】（补录）
```
技术词 residual target  命中文件数=1    :: ./M03-3b-final-registration-and-residual-target.md 
技术词 set difference   命中文件数=0    :: 
```
