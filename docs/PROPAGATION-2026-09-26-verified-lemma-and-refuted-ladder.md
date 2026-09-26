已查地图：已跑 scripts/prework_map_check.sh midpoint 传播 ladder σ Q=0 ⟹ 执行自 CHANNELS-2026-09-26 档；本档为**传播引理：验证通过 ✓ ＋ ladder 论断：数值证伪 ✗**（唐先生 2026-09-26 13:13 指令）；未跑 solver ✓。
D0: 本档对象 = Q=0 时 midpoint 的二阶传播引理与其 ladder（σ 系统）论断的真伪判定
D1: 1（新增：**传播引理**（可证＋验证 ✓）；**ladder 两条论断被数值证伪** ✗）

# PROPAGATION-2026-09-26

## §1 ✅ **传播引理（Verified ✓）** —— 唐先生 §1–§3 正确 ✓

```
$$\text{设 }Q=0\ ✓,\ \{c,c'\}\ \text{为距离-2 对}\ ✓,\ m\ \text{为其中点}\ ✓\ (\text{中点引理给 }b(m)=2,\ C\cap B_1(m)=\{c,c'\}\ ✓)$$
$$\text{记 }B_1(m)\ \text{的其余 }n-2\ \text{个邻点 }x_l=m+e_l\ (l\notin\{\text{两差异坐标}\})\ ✓\ \text{—— 由 }b(m)=2\ \text{知 }x_l\notin C\ ✓$$
$$\text{每个 }x_l\ \text{须被某码字 }z\ne c,c'\ \text{覆盖}\ ✓\ \text{且 }a(z,m)\ge2\ (\text{否则 }b(m)\ge3\ ✗)\ ✓;\ \text{又 }d(z,m)\le d(z,x_l)+1=2\ ✓\ \Longrightarrow\ d(z,m)=2\ ✓$$
$$\Longrightarrow\ z\in S_2(m):=\{z\in C:\ d(z,m)=2\}\ ✓$$
$$\text{一个 }z\in S_2(m)\ \text{至多覆盖 2 个 }x_l\ ✓\ (\text{坐标论证: }z=m+e_a+e_b\ \text{覆盖 }x_a,x_b\ \text{恰两个}\ ✓)$$
$$\boxed{\textbf{传播引理}:\ |C\cap S_2(m)|\ \ge\ \Bigl\lceil\frac{n-2}{2}\Bigr\rceil}\ ✓✓\quad(\text{奇 }n=2r+1:\ \ge r\ ✓;\ \text{偶 }n=2r:\ \ge r-1\ ✓)$$
$$\textbf{数值核验}: n=4\ (bound=1):\ \textbf{40/40 全成立}\ ✓✓;\quad n=5\ (bound=2):\ \textbf{28/28 全成立}\ ✓✓$$
$$

## §2 ⛔ **ladder 论断：数值证伪** ✗（唐先生 §5 的两条）

```
$$\textbf{断言之①}: \bigl|C\cap S_2(m)\cap S_2(m')\bigr|\ \ge\ n-2\ ✗$$
$$\qquad\text{实测}: n=4:\ \text{范围 }[0,0]\ \text{vs 断言}\ge2\ ⟹ \textbf{不成立}\ ✗✓;\quad n=5:\ [0,2]\ \text{vs }\ge3\ ⟹ \textbf{不成立}\ ✗✓$$
$$\textbf{断言之②}: \text{"覆盖 }e_l\ \text{必占 }u_l=e_i+e_l\ \text{或 }v_l=e_j+e_l"\ ✗$$
$$\qquad\text{实测}: \textbf{存在 }e_l\ \text{被覆盖而 }u_l,v_l\notin C\ \text{的反例}\ ✗✓\ (n=4\ \text{与 }n=5\ \text{均有}\ ✓)$$
$$\textbf{根因（我方定位 ✓）}: \text{覆盖 }e_l\ \text{只要求某码字距 }e_l\ \text{为 1}\ ✓;\ u_l,v_l\ \text{只是其中两个候选}\ ✗\ ——\ B_1(e_l)\ \text{还含 }e_l\ \text{自身、}e_l+e_t\ (t\notin\{1,2,l\})\ \text{等大量候选}\ ✓$$
$$\Longrightarrow\ \text{"binary ladder }\sigma\in\{1,2\}^{n-2}\text{" 结构\textbf{不成立}}\ ✗\ \Longrightarrow\ \text{唐先生 §6--§9 的 Odd-Ladder Lemma 计划\textbf{建立在已被否掉的一步上}}\ ✗\ ——\ \textbf{建议不再投入}\ ✓$$
$$

## §3 Q=0 的局部结构（现已核实的两条 ✓）

```
$$\textbf{已核实}: \text{① 中点引理（距离-2 对的中点是非码字、}b=2\text{、孤立 ✓）};\quad \text{② 传播引理（}|C\cap S_2(m)|\ge\lceil (n-2)/2\rceil\ ✓)$$
$$\textbf{未核实/已否}: \text{③ ladder 共享壳下界 ✗};\quad \text{④ }\sigma\ \text{选择系统 ✗}$$
$$\text{注}: \text{②\textbf{不}给出奇偶障碍}\ ✗\ ——\ \text{它只给 }S_2(m)\ \text{的局部容量下界}\ ✓\ (\text{且不同中点可共享 }z\ ✓\ \text{故不受理全局计数}\ ✗)$$
$$

## §4 状态与台账

```
$$\textbf{桥仍未打通}\ ✗;\quad \textbf{119 保持 UNKNOWN}\ ✓$$
$$\textbf{资产（累计）}: \text{私有点引理};\ \text{奇偶引理＋P1};\ \Phi=A_1+A_2;\ \text{通道分解};\ \textbf{中点引理};\ \textbf{传播引理（本档新增 ✓）}$$
$$\textbf{已淘汰}: P\ (\text{换皮});\ P_2;\ \text{三进制同余};\ \Delta\to A_{\le2}\ \text{传递};\ \text{shadow 路线};\ \Phi\ \text{作路线};\ \textbf{ladder/}\sigma\ \text{系统（本档新增 ✗）}$$
$$

## §5 边界（诚实标注）

- §1 的证明为**我方推导** ✓ ＋ **数值验证** ✓（n=4 全枚举 ✓、n=5 M=8 采样 ✓）
- §2 的证伪为**数值反例** ✓ —— 唐先生 §5 的推断链有跳跃（覆盖候选远多于两个 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 传播引理     命中文件数=0    :: 
技术词 阶梯结构     命中文件数=2    :: ./dn-positivity-unconditional.md ./output-A-dn-theorem.md 
技术词 被证伪断言  命中文件数=0    :: 
技术词 共享壳容量  命中文件数=0    ::
```

- **本档新增**（命中数=0）：传播引理、被证伪断言、共享壳容量
- **档案已有（引用，不列为提出）**：阶梯结构
