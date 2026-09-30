# LEMMA-2026-09-30 — **四步人工引理**：不存在 8 顶点 21 边图使每条边恰属 3 个三角形 ⟹ $D{=}0$ 被杀 ⟹ $h_{\min}(8,21)=66$

结论: 已查地图：未覆盖（关键词: 全偶度|全奇补图度|端点方程）—— 可开档，首行须照抄本行
D0: 本档对象 = 纯极值层整数结构引理（无档案同型；非已知 RH 对象重命名）
D1: 0

## §0 引理（唐先生 2026-09-30 定稿 ✓）

$$\boxed{\text{若 }G\ \text{是 8 顶点、21 边之简单图，则不可能所有 }e\in E(G)\ \text{皆恰属 3 个三角形}}\ ✓✓$$

## §1 四步证明（人工可读 ✓✓）

$$\textbf{(1)}\ \text{设 }t_e{=}3\ \forall e;\ \text{对顶点 }v:\ 3d_G(v)=\sum_{e\ni v}t_e=2\tau_v \Longrightarrow \gcd(3,2){=}1 \Longrightarrow \boxed{d_G(v)\ \text{全偶}}\ ✓$$
$$\textbf{(2)}\ H=\bar G:\ d_H(v)=7-d_G(v) \Longrightarrow \textbf{\text{全奇}};\ \sum_vd_H=2|E(H)|=14 \Longrightarrow \text{8 点全奇度和 14} \Longrightarrow \boxed{\#\{a_v{=}1\}\ \ge\ 5}\ ✓$$
$$\textbf{(3)}\ t_{uv}{=}3\Rightarrow c_{uv}=a_u+a_v-3;\ \text{若 }a_u{=}a_v{=}1\ \text{且 }uv\in E(G) \Longrightarrow c_{uv}=-1\ \text{不可能} \Longrightarrow \boxed{\text{度 1 点须两两相邻}}\ ✓$$
$$\textbf{(4)}\ \text{但度 1 点各只有一个邻点} \Longrightarrow \text{此类点\ \textbf{至多 2 个}};\ \text{与 (2) 之 }\ge5\ \textbf{\text{矛盾}}\ ✓✓$$

## §2 数值校验（本档 ✓✓）

| 校验 | 结果 |
|---|---|
| 8 点全奇度和 14 之 $\#\{a{=}1\}$ 最小值 | **5** ✓（例 $(3,3,3,1,1,1,1,1)$） |
| $e{=}21,T{=}21$ 之 198,600 图中全 $t_e{=}3$ 者 | **0** ✓✓ |

## §3 组装后的完整证明（$h_{\min}(8,21)=66$ ✓✓）

$$\underbrace{e_{\max}(8,21)=21}_{\text{判定式严格}}\ \Longrightarrow\ h\ge\underbrace{H(21,21)=63}_{\text{载荷凸性}}\ ;\quad h{=}63\iff t_e{=}3\ \forall e\ \Longrightarrow\ \textbf{\text{引理}\ \S1\ \textbf{排除}}\ ✓$$
$$\Longrightarrow\ h\ge64;\quad h{=}64,65\ (D{=}2,4)\ \text{由\ \textbf{极值层穷尽枚举} 排除}\ ✓\ \Longrightarrow\ \boxed{h_{\min}(8,21)\ge66};\ \text{而 }h{=}66\ \text{有 10,080 个 extremizer}\ ✓✓$$
$$\therefore\ \boxed{h_{\min}(8,21)=\mathbf{66}}\ ✓✓\ (\text{混合证明}:\ \textbf{\text{人工引理}} + \textbf{\text{有限穷尽}} + \textbf{\text{构造}} ✓)$$

## §4 对 $T{=}20$ 与 $T{=}21$ 现象之解释（唐先生 §6/§7 ✓）

$$\text{在 }D{=}0\ \text{之假设下},\ t_e{=}3\ \forall e\Rightarrow \sum t_e=63\Rightarrow T=21\ \textbf{\text{自动}}\ \Longrightarrow\ \text{故 }(e,21)\ \text{才触发"全偶度 }\to\text{ 全奇补图度 }\to\ \ge5\ \text{叶子}\ \to\ \text{叶子对 }c{=}-1"\ \text{之链}\ ✓✓$$
$$\therefore\ T{=}20\ \text{处 }h{=}63\ \text{可存在（载荷型非全 3）},\ \text{而 }T{=}21\ \text{处被引理杀掉}\ ✓\ \text{——\textbf{交互}而非边数}\ ✓✓$$

## §5 组织方式（唐先生 §7 定稿 ✓）

$$D{=}0:\ \textbf{\text{人工引理}}\ \S1;\qquad D{=}2,4:\ \textbf{\text{极值层穷尽性证据}};\qquad h{=}66:\ \textbf{\text{构造（}}10{,}080\ \text{个）}\ ✓$$

## §6 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{引理四步逐条核验＋两处数值校验} ✓;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §7 【技术词回查】

```
技术词 全偶度   命中文件数=1
技术词 端点方程  命中文件数=0
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档} ✓;\ \textbf{通用词（不计）}：\text{"引理／载荷"裸词} ✓$$
