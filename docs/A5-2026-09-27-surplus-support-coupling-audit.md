已查地图：已跑 scripts/prework_map_check.sh surplus 支撑耦合 R_xc Y=ff^T ⟹ 续 `INCIDENCE-FIX-2026-09-27-...`（Booleanity 等价 ✓）＋ 档案 M-1/M-2A/Fourier audit/AMEND-35；本档 = **A5 审计：两条干净恒等式 ✓ ＋ 边际退化 ✗ ＋ A2 朴素松弛为空 ✗**。
D0: 本档对象 = A5（surplus×支撑耦合）之非径向可达性
D1: 3（**两条新恒等式 ✓（$\sum_{x\in C}\delta=2A_1$、$\sum_x b\delta=4(A_1{+}A_2)$ ⇒ $\sum\delta^2$ 闭式 ✓）**；**边际退化 ⟹ A5 坍缩封口 ✓**；**A2 朴素松弛（仅去 rank-1）为空 ✗**）

# A5 审计：surplus × 支撑耦合（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(LA-1 边际（marginals）退化 ✗）}\ R_{xc}:=f(c)\delta(x)\ \Longrightarrow\ \boxed{\sum_c R_{xc}=M\,\delta(x)}\ ✓（\delta\text{-型 ✗}）;\quad \boxed{\sum_x R_{xc}=285\,f(c)}\ ✓（f\text{-型 ✗}）}$$
$$\qquad\Longrightarrow\ \textbf{两个边际各只带一个变量} \Longrightarrow \text{新信息只能藏在\textbf{联合结构}（相关性 ✓），而任何\textbf{平移不变权重}的和会自动把它抹掉 ⚠️}$$
$$\boxed{\textbf{(LB-1 ⭐两条干净恒等式（本档新 ✓，可留档 ✓）)}\ \text{设 }b=Tf,\ \delta=b-1\ (n=10,\ M=119\ ✓):}$$
$$\qquad\boxed{\sum_{x\in C}\delta(x)=2A_1}\ ✓✓\qquad\text{（推导：}\ \sum_{x\in C}b(x)=M+2A_1\ ✓\ \text{—— 每码字贡献 }1+d_1(c)\ ✓,\ \sum_c d_1(c)=2A_1\ ✓\text{）}$$
$$\qquad\boxed{\sum_x b(x)\,\delta(x)=4\left(A_1+A_2\right)}\ ✓✓\qquad\text{（因 }\sum_{x\in B_1(c)}\delta(x)=2\bigl(d_1(c)+d_2(c)\bigr)\ ✓\ \text{（对角线贡献 }n{+}1\ \text{与 }-11\ \text{相消 ✓）}\text{）}$$
$$\qquad\Longrightarrow\ \textbf{推论（新形 ✓）}:\ \boxed{\sum_x\delta(x)^2=4(A_1+A_2)-285}\ ✓\ \text{—— 把 surplus 的\textbf{二阶矩}钉死在 }(A_1,A_2)\ \text{上 ✗（恒等式，非约束 ✗）}$$
$$\boxed{\textbf{(LC-1 🔴A5 判定 = 坍缩 ⟹ 按唐先生规则封口 ✓)}\ \text{一切平移不变权重 }\sum_{x,c}w(d(x,c))R_{xc}\ \text{皆退化为 }(M,A_1,A_2)\ \text{的函数 ✗};\ \text{仅非平移不变权重可保留坐标信息 ⟹ 但此类和无先验约束 ✗（自由参数 ✓）}}$$
$$\qquad\Longrightarrow\ \text{未得独立不变量 ✗ ⟹ \textbf{A5 封口}（第 19 次同向收敛 ✓）}$$
$$\boxed{\textbf{(LD-1 ⚠️A2 预警（本档顺带发现 ✓，很重要 ✓）)}\ \text{若 }Y=ff^{\mathsf T}\ \text{只放松 rank-1 而保留 }\{Y\succeq0,\ Y_{xx}=f_x\}\ \Longrightarrow\ \textbf{该松弛\textbf{为空} ✗}:\ \text{对任意 }f\ge0,\ Y=ff^{\mathsf T}\ \text{即合法 ⟹ 不排除任何 }f\ ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{A2 要有内容，必须保留\textbf{坐标级条目约束}（如 }Y_{x,x+e_i+e_j}\in\{0,1\}\ \text{对\textbf{特定 }(i,j)\ ✓）—— \text{而那正是 Booleanity 回归 ✗} \Longrightarrow \text{A2 的朴素形不可行 ⚠️}$$
$$
$$
```

## §1 AMEND-35 四问自查（**✓ 按唐先生硬门**）

```
$$\text{(1) 保留哪个实际支撑变量?}\ \ \checkmark\ f(c)\ ✓\ (\text{与 }\delta(x)\ \text{相乘 ✓});\quad \text{(2) 保留哪个 profile 看不到的坐标关系?}\ \ \text{联合 }(x,c)\ \text{结构 ✓ —— 但\textbf{可加性权重一平均即失 ✗}}$$
$$\text{(3) 为何 }A_d/N_k/\text{Walsh/Delsarte 不能恢复它?}\ \ ✗\ \textbf{答不出}:\ \text{本档显示它们\textbf{能}恢复全部平移不变聚合（即我们试过的全部 ✓）} \Longrightarrow \textbf{直接 STOP ✓（按你的规则 ✓）}$$
$$\text{(4) 放松后能推出什么新必要条件?}\ \ ✗\ \text{只有恒等式（LB-1 ✓），无新必要条件 ✗}$$
$$
$$
```

## §2 状态与下一步（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{A5 封口（第 19 次）✓};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$\textbf{本档净收获 ✓}:\ \text{(i) }\sum_{x\in C}\delta=2A_1\ ✓;\ \text{(ii) }\sum_x b\delta=4(A_1{+}A_2)\ \Rightarrow\ \sum\delta^2\ \text{闭式 ✓};\ \text{(iii) A2 朴素松弛为空的预警 ✓}$$
$$\textbf{下一步（按 Gate 2 ✓）}:\ \text{A2 若开，必须\textbf{设计带坐标条目的 }Y\ \text{约束}（否则为空 ✗）;\ \text{或直接跳到 A4（局部一致性）—— 后者是\textbf{真松弛}（局部可实现 ⇏ 全局 ✓），且天然支撑可见 ✓}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\sum_{x\in C}\delta=2A_1$、$\sum_x b\delta=4(A_1+A_2)$ 与 $\sum\delta^2$ 闭式、A5 边际退化判定、A2 朴素松弛为空之预警
- **档案已有（引用，不列为提出）**：Booleanity 等价（A-INCIDENCE-FIX-1）、M-1/M-2A、Fourier audit、AMEND-35


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 边际退化     命中文件数=1    :: ./A5-2026-09-27-surplus-support-coupling-audit.md 
技术词 朴素松弛为空 命中文件数=1    :: ./A5-2026-09-27-surplus-support-coupling-audit.md
```
- **本档新增**：$\sum_{x\in C}\delta=2A_1$、$\sum_x b\delta=4(A_1+A_2)$ 与 $\sum\delta^2$ 闭式、A5 边际退化判定、A2 朴素松弛为空之预警（见上方命中数；0 命中者为自造语／内部标签 ✓）
