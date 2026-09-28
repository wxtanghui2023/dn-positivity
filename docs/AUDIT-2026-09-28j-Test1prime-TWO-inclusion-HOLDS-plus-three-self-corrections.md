# AUDIT-2026-09-28j — **Test-1″：包含性测试**结果 **HOLDS** ⟹ 暂停 $\Phi_2$ ＋ **三处自纠**

> **性质**：**审计/实验**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:52 ✓
> **唐先生令**：跑 Test-1″＝**代数包含性测试**（$\operatorname{span}(\Phi_2\text{ stats})\subseteq\operatorname{span}(\text{SDP 3-point})$？）；**不含**：先做数值实验 ✗

**已查地图**：接续 `AUDIT-i`（$\Phi_2$）／C-474（SDP 之 3-point）✓

D0: 本档对象 ＝ **档案已有**（$\Phi_2$／三点数据——无新数学对象 ✓）
D1: 0（产出＝**Test-1″ 判定 HOLDS ＋ 三处自纠** ⚠️）

---

## §0 结论（先给）

$$\boxed{\textbf{Test-1″}:\ \operatorname{span}(\Phi_2\ \text{stats})\ \subseteq\ \operatorname{span}(\text{3-point distance data})\ \Longrightarrow\ \textbf{HOLDS}}\ ✓✓$$
$$\boxed{\Longrightarrow\ \text{按唐先生之情形 A ⟹ \textbf{暂停 }\Phi_2\ (\text{作为独立 }P_1\text{ 之资格很弱})}\ ✗}$$

## §1 ★ 决定性计算：$\nu(c_1,c_2,c_3)$ **由距离三元组决定**（**穷举 ✓✓**）

$$\nu(c_1,c_2,c_3):=\bigl|N(c_1)\cap N(c_2)\cap N(c_3)\bigr|,\qquad N(x)=\{y:d(x,y)=1\}$$

| $n$ | 遍历三点组 | 距离配置数 | $\nu$ **非单值**配置数 |
|---|---|---|---|
| $6$ | $41664$ | $16$ | $\mathbf 0$ |
| $7$ | $341376$ | $23$ | $\mathbf 0$ |

$$\boxed{\nu\ \textbf{完全由距离三元组决定}}\ \Longrightarrow\ \Sigma_y\binom{a_y}{3}=\sum_{\text{三点}} \nu(\text{三点})\ \text{为\ \textbf{三点距离分布之线性泛函}}\ ✓✓$$
$$\therefore\ \boxed{\Phi_2\ \text{之全部统计量}\ \subseteq\ \text{三点距离数据}}\ \Longrightarrow\ \text{与 C-474 之 SDP\textbf{同层}}\ ✓$$
（$\because$ SDP 之变量即 3-point configurations；该层已给 $105.2223<119$ ✓）

## §2 ⚠️ 三处自纠（**本档必录 ✓**）

### 自纠 ①：`AUDIT-i` 之"$M_3$ 结构定理"实为**恒等重写** ✗

$$\textbf{实测}:\ m_i(c)=a_{c\oplus e_i}\ ✓\ \Longrightarrow\ \sum_c\sum_i m_i(c)^2=\sum_c\sum_i a_{c\oplus e_i}^2=\sum_y a_y\cdot a_y^2=\sum_y a_y^3$$
$$\therefore\ \text{该"结构定理"＝\textbf{换标号重写}（tautology），\textbf{非}结构结果}\ ✗;\ \text{`AUDIT-i` D1 之"首次给出结构定理"应\textbf{降级}} ⚠️$$

### 自纠 ②：正确分解式

$$\boxed{M_3=10K+12N_2+6\sum_y\binom{a_y}{3}}$$
$$\text{（由 }M_3{=}10K{+}4N_2{+}2\sum_y a_y\binom{a_y}{2}\ \text{（实测 ✓）与 }a\binom a2{=}3\binom a3{+}2\binom a2\text{ 得）}$$
$$\Longrightarrow\ \text{真正新增者}＝\Sigma_y\binom{a_y}{3}\ \text{（三点共邻计数）}\ ✓$$

### 自纠 ③：唐先生式中之第一项

$$\text{唐先生写 }M_3=M_1+2\sum_{c,i}\binom{m_i(c)}2;\quad \textbf{但实测}\ \sum_c\sum_i m_i(c)=10K+4N_2\ \ne\ M_1=10K\ ✓$$
$$\therefore\ \text{第一项应为 }(10K+4N_2)\ \text{（含 }N_2\text{）},\ \textbf{非 }M_1\ ✗✓\ \text{（差 }4N_2\text{）}$$

**注**：三处均**不影响** §0 判定（因 $\nu$ 距离决定性直接给出包含）✓

## §3 判定与建议

$$\boxed{\text{情形 A 成立} \Longrightarrow \Phi_2\ \text{暂停};\ \text{不做"同距离分布异 }\Phi_2\text{"之构造实验}}\ ✗\ \text{（省计算 ✓）}$$
$$\textbf{准确表述（照唐先生 §"情形 A" ✓）}:\ \Phi_2\ \text{未引入超出该 SDP 三点信息空间之新变量层} \Longrightarrow \text{作为独立 }P_1\text{ 之资格\ \textbf{很弱}};$$
$$\qquad\text{结合 SDP 在 }n{=}10,r{=}1\ \text{之 }105.2223,\ \text{继续独立投入\ \textbf{无充分理由}}\ ✓$$

## §4 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "包含性测试" "恒等重写自纠" "三点距离决定"
技术词 包含性测试   命中文件数=0    ::
技术词 恒等重写自纠  命中文件数=0    ::
技术词 三点距离决定  命中文件数=0    ::
```

## §5 边界（硬 ✓）

- 穷举（$n{=}6,7$）＋ 恒等式推导 ＋ 既有档引证 ✓；**不占 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §1 之穷举证于 $n{=}6,7$；**未证** $n{=}10$（但 $\nu$ 为**局部**量，与 $n$ 无关之结构 ⟹ 强烈提示，已标注 ⚠️）
