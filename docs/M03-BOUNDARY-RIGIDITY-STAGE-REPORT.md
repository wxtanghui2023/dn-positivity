已查地图：命中（`M03-LEMMA-trace-deficit-frozen-diagonal-second-order-sign`）⟹ 阶段收口报告（`丁`），不开新案
D0: 本档对象 = **阶段收口**：已封区／未封区隔离 ＋ **临界线 `\beta=t`** 登记 ＋ 资产登记 ＋ 重开条件 ＋ 纪律与边界
D1: 0（收口型文档，无新自由度）
[REVIEW]

# **`Z_2`-`Case II` 边界刚性：阶段收口报告**

## §1 已封（`t\ge\tfrac13`，`0<\beta<\tfrac{1-t}2`）

```
$$\text{对象}:\ Z_2\text{-Case II 边界族（}b+g=\tfrac{1-t}2,\ a=f=e=h=0,\ i=t\ \text{的边界构型};\ \text{谱}\ \sigma(B)=\{t,-s\},\ \sigma(Q)=\{1,t,-s\}).$$
$$\quad\boxed{O(\delta)\ \textbf{封}}:\ Ju=r\ \text{无锥可行解，证书 }u_a+u_f=-1<0\ (\text{与 }\beta,t\ \text{无关}).$$
$$\quad\boxed{O(\sqrt\delta)\ \textbf{封}}:\ \varepsilon=\sqrt\delta\ \text{尺度下 }W_\beta=-1-\mathcal Q(\tau)\le-1<0\ \text{于整锥}.$$
$$\quad\boxed{\textbf{一阶冻结结构性}}:\ v_a+v_f=0\ \text{与}\ v_i=0\ \text{对一切 }(\beta,t)\ \text{成立}.$$
$$\quad\boxed{\textbf{二阶反号（整族）}}:\ W_\beta=-1-\frac{2\beta+3t-1\ \tau_0^2+2(t-\beta)\ \tau_3^2+4W\tau_0\tau_3}{(1-t)(1+3t)}\le-1<0.$$
$$\quad\boxed{\tau_2\ \textbf{缺席结构性}}:\ (b,g)\ \text{反对称核方向与迹亏空承担量正交（对一般 }\beta).$$
```

## §2 未封（须严格隔离）

```
$$\boxed{t<\tfrac13,\ \beta>t}:\ \text{已有 }W_\beta\ge0\ \text{的二阶可行方向证据} \Longrightarrow \textbf{当前二阶机制确实失效}\ (\text{非"待证"}).$$
$$\boxed{\beta=0,\ \beta=\tfrac{1-t}2}:\ \text{端点退化（}b\ \text{或 }g\ \text{到边界），}\textbf{未覆盖}.$$
$$\boxed{\text{非边界内部点}}:\ \text{边界构型之外的 }Z_2\ \text{族内部点},\ \textbf{未覆盖}.$$
$$\boxed{\text{其它情形}}:\ \text{Case I（未 CLOSED）、Case III（已 CLOSED）};\ \text{更高阶尺度 }\varepsilon^3,\varepsilon^4\ (\textbf{未做},\ \text{且已判定边际价值低}).$$
$$\text{注}:\ \text{上述"未封"}\ne\text{"不存在封口"};\ \text{亦}\ne\text{"}Z_2\ \text{族整体可实现"}.$$
```

## §3 临界线（最值得关注的新对象）

```
$$\boxed{\beta=t}\ \text{是 }B=2(t-\beta)\ \text{的符号分界，也是本题中出现的\textbf{唯一干净临界线}}.$$
$$\quad\text{几何含义}:\ b=\beta=t=\lambda_1\ \text{（即 }b\ \text{与 Perron 根同值）；}\ B=0\ \text{时 }\tau_3\ \text{方向不再贡献负项}.$$
$$\quad\text{地位}:\ \text{作为}\textbf{候选相变线}\ \text{登记};\ \text{未证明其有物理/结构相变含义};\ \textbf{不得升级为已证结论}.$$
```

## §4 资产登记

```
$$\textbf{A1 引理（可复用）}:\ \text{迹亏空—冻结对角—二阶反号（含 (H1)-(H4) 适用域与失效模式）}.$$
$$\textbf{A2 一阶证书}:\ u_a+u_f=-1\ (\text{参数无关}).\qquad\textbf{A3 二阶公式}:\ W_\beta\ \text{显式二次型（分母 }\beta\text{-自由）}.$$
$$\textbf{A4 方法资产}:\ \text{“已知点退化值”交叉核验（本次抓出全局符号错误）};\ \text{锥约束单标量化（不变量 }W).$$
$$\textbf{A5 负资产}:\ \text{Case III CLOSED（迹符号）};\ \text{线性层 }K_{PM}=K_{Kellogg}=K_{Borobia}=\varnothing\ \text{于 }R;\ \text{对称子族不可行}.$$
$$\textbf{A6 数据}:\ \text{ker }J_\beta\ \text{显式结构};\ J_\beta\ \text{行结构};\ \text{基点参数化 }(W,V).$$
```

## §5 重开条件

```
$$\text{(R1) 出现新工具可处理 }t<\tfrac13,\beta>t\ \text{段的二阶可行方向};\quad\text{(R2) 端点退化 }(\beta\to0\ \text{或}\ \tfrac{1-t}2)\ \text{的特殊分析};$$
$$\text{(R3) 临界线 }\beta=t\ \text{的结构/相变判据};\quad\text{(R4) 非边界内部点的独立论证};\quad\text{(R5) 新对象/新机制出现（本引理之外）}.$$
【⛔ 纪律】 本档为**收口**（零新计算）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 的"已封"限于 `Z_2`-`Case II` 边界族与 `\varepsilon^2` 尺度；**不得**表述为"`S` 不可实现"或"`Case II` 已封" ✓

## §附 【技术词回查】（补录）
```
技术词 stage report     命中文件数=2    :: ./S2-C07-STAGE-REPORT-CLOSED.md ./M03-LEMMA-trace-deficit-frozen-diagonal-second-order-sign.md 
技术词 applicability    命中文件数=2    :: ./C3882-noncanonical-escape-hatch-specification-and-closure.md ./M03-LEMMA-trace-deficit-frozen-diagonal-second-order-sign.md 
```
