已查地图：已跑 scripts/prework_map_check.sh h(z) 影子质量 容量 p2 ⟹ 执行自 P14-2026-09-26 档；本档为**P1.5：影子质量容量不等式 ＋ 两项新事实 ＋ 容量路线否证**（唐先生 2026-09-26 16:43 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = p₂(z) 分叉验证、h(z)≤C(b,2)、max h 与 max h_iso、H_C/H_C̄ 分离、容量路线的松弛度
D1: 1（新增：**p₂ 分叉公式验证** ✓✓；**max h_iso=1（孤立影集不交）** ✓✓；**容量路线否证（松弛 5×）** ✗✓）

# P15-2026-09-26

## §1 ⭐ **唐先生 p₂(z) 分叉公式：完全验证** ✓✓

```
$$p_2(z)=\#\{\{u,v\}\subset C\cap B_1(z):\ d(u,v)=2\}=\begin{cases}q(z)=\binom{b(z)-1}2,&z\in C\\ \binom{b(z)}2,&z\notin C\end{cases}\ ✓✓$$
$$\text{实测 4 码: 违反 }\mathbf 0\ ✓✓\ (\text{唐先生此式正确}\ ✓)$$
$$

## §2 ⭐⭐ **h(z) 容量不等式与两项新事实**

```
$$h(z)\le\binom{b(z)}2\ \text{实测}: \textbf{违反 0}\ ✓✓;\quad \text{取等点数} = 34\ (\text{码#1})/29\ (\text{码#2})\ ✓\ (\text{容量被用满}\ ✓)$$
$$\textbf{新事实 ①}: \max_z h(z)=\mathbf 2\ (\text{全 b=4 中心})\ ✓\ ——\ \text{影子重数极小}\ ✓✓$$
$$\textbf{新事实 ②（更强）}: \max_z h_{\rm iso}(z)=\mathbf 1\ ✓✓\ \Longrightarrow\ \boxed{\text{孤立星的影集\textbf{两两不交}}\ ✓✓}$$
$$\qquad\text{即}: \Delta_x\cap\Delta_y=\varnothing\ \text{对所有孤立对}\ ✓\ (\text{码#1 分布 }\{1{:}30\}\ ✓;\ \text{码#2 }\{1{:}27\}\ ✓)$$
$$

## §3 ✗ **容量路线否证（诚实 ✓，松弛 5×）**

```
$$\begin{array}{c|c|c|c|c|c}
\text{码} & N_4 & \text{孤立数} & \Sigma|\Delta_x|_{\rm iso} & \Sigma\binom{b}2 & \text{松弛}\\
\hline
\text{码#1} & 10\ (A2/B8) & 6\ (A2/B4) & \mathbf{30} & 146 & \mathbf{\times4.9}\\
\text{码#2} & 10\ (A7/B3) & 6\ (A3/B3) & \mathbf{27} & 146 & \mathbf{\times5.4}\\
\end{array}$$
$$\text{全中心（含非孤立）}: \Sigma|\Delta_x| = 54\ (\text{码#1})/39\ (\text{码#2})\ \text{—— 仍远低于 146}\ ✗$$
$$\Longrightarrow\ \boxed{\text{影子质量远低于容量（松弛 }\gtrsim5\times\text{）}\ ✗\ \Longrightarrow\ \textbf{容量/平均不等式路线\textbf{无约束力}}\ ✗✓}$$
$$

## §4 H_C / H_C̄ 分离（唐先生所问 ✓）

```
$$\text{码#1}: H_C=0,\ H_{\bar C}=54\ (\text{孤立}: 0/30)\ ✗;\quad \text{码#2}: H_C=6,\ H_{\bar C}=33\ (\text{孤立}: 0/27)\ ✗$$
$$\Sigma_{z\in C}q(z)=6\ (\text{码#1})/27\ (\text{码#2})\ \mathbf{✗\ \text{分叉}}\ ✓;\quad \Sigma_{z\notin C}\binom{b}2=126/67\ \mathbf{✗\ \text{分叉}}\ ✓$$
$$\Longrightarrow\ \text{码#1 的屏障是 A 型极少（A2）}\ ✓;\ \text{码#2 是 A 型多（A7）}\ —\ \text{两者同为 }N_4=10\ ✗$$
$$

## §5 判决（诚实 ✓）

```
$$\boxed{\textbf{影子质量路线（P1.3--P1.5）\textbf{全部否证}}\ ✗\ ——\ \text{三条理由}}$$
$$\qquad\text{① 逐星 charging 不存在统一收费规则}\ ✗\ (\text{P1.4}\ ✓)$$
$$\qquad\text{② 碰撞非必然（可达 6，亦可为 0）}\ ✗\ (\text{P1.4}\ ✓)$$
$$\qquad\text{③ 影子质量}\ \ll\ \text{容量（松弛 5×）}\ ✗\ (\text{P1.5}\ ✓✓)$$
$$\text{保留资产}: p_2\ \text{分叉公式}\ ✓✓;\ h\le\binom b2\ ✓✓;\ \textbf{孤立影集两两不交}\ ✓✓;\ \max h=2\ ✓$$
$$\text{保留策略性事实}: \textbf{局部几何在 }M=K\ \text{上"太松"}\ ✗\ ——\ \text{影子结构承载不了 }N_4\ \text{的刚性}\ ⚠️$$
$$

## §6 状态与建议

```
$$\textbf{已证}: T_3=\#K_3(G_{\le2})\ \text{普适}\ ✓✓;\quad \text{剖面}\iff N_4=10\iff\#\triangle=48\ ✓✓$$
$$\textbf{未决}: N_4\le10\ ✗\ (\text{上界路线已连续否证 5 轮}\ ✗)\ ——\ \textbf{建议转攻下界}\ N_4\ge10\ ⚠️$$
$$\qquad\text{理由}: \text{上界需"局部几何}\Rightarrow\text{全局约束"，而实测各局部量在 }M=K\ \text{上都偏松}\ ✗$$
$$\qquad\text{下界}\ N_4\ge10\ \text{可能更易（覆盖性/奇偶性强制高重叠点存在）}\ ⚠️\ \text{待评估}$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §7 边界（诚实标注）

- §1–§4 为**实算**（4 码 ✓）；§5 明确登记**三条否证** ✗
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 影子质量容量 命中文件数=1    :: ./P15-2026-09-26-shadow-mass-capacity-and-its-failure.md 
技术词 孤立影集不交 命中文件数=1    :: ./P15-2026-09-26-shadow-mass-capacity-and-its-failure.md 
技术词 容量路线否证 命中文件数=1    :: ./P15-2026-09-26-shadow-mass-capacity-and-its-failure.md
```
- **本档新增**（扣自引后 = 0）：影子质量容量、孤立影集不交、容量路线否证
- **档案已有（引用，不列为提出）**：h(z)、p₂(z)、N₄
