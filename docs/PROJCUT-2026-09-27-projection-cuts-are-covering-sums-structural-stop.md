已查地图：已跑 scripts/prework_map_check.sh 投影割 正系数和式 割平面 ⟹ 执行唐先生 16:05 裁定（归档 ✓）；本档 = **投影割 STOP（结构性 ✓）＋ 一般命题（正锥内割先验无力 ✓）**。
D0: 本档对象 = 子立方投影割之有效性与其"零杠杆"之结构性解释
D1: 3（**投影割 = covering 约束之和（证明 ✓）**；**一般命题：正系数和式割先验不可能产生新下界 ✓✓**；**A4/SA 族之解释 ✓**）

# 投影割 STOP 与正锥命题（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(RA-1 ⭐投影割的正确形式（有效 ✓，已修正）)}\ \text{对子立方 }S=\{x:\ x|_U=w\}\ (\ |U|{=}m,\ |V|{=}n{-}m\ ✓\text{）},\ \text{记 }F(v):=\sum_{c:\ c|_U=v}f_c\ ✓:}$$
$$\qquad\boxed{(1+|V|)\,F(w)+\sum_{i\in U}F(w\oplus e_i)\ \ge\ 2^{|V|}}\ ✓\ \text{（有效 ✓：小 }n\ \text{全部 }\le K(n,1)\ ✓\text{）}$$
$$\qquad\textbf{我第一版的错误 ✗（自查发现 ✓）}:\ \text{曾写 }\sum_{c:\ d(c|_U,w)\le1}f_c\ge2^{|V|}\ \Longrightarrow\ n{=}4\ \text{给 }8>K{=}4\ ✗\ \text{（界超过真值 ⟹ 割\textbf{无效} ✓ 已修 ✓）}$$
$$\boxed{\textbf{(RB-1 ⭐⭐投影割 = covering 约束之和（证明 ✓✓）)}\ \text{对 }\Sigma_{x\in S}\ \text{（原 covering 约束）}:\ \sum_{x\in S}\sum_{c\in B_1(x)}f_c\ \ge\ |S|=2^{|V|}\ ✓}$$
$$\qquad\text{而左侧 }=\sum_c f_c\cdot\#\{x\in S:\ d(x,c)\le1\}=\underbrace{(1+|V|)F(w)}_{\text{且 }c|_U=w}-\ \text{项}+\sum_{i\in U}F(w\oplus e_i)\ ✓ \Longrightarrow \textbf{恰等于 (RA-1) 之左端 ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{\text{投影割不是"新割"，而是 covering 系统在子立方上的\textbf{逐项相加}}\ ✗}$$
$$\boxed{\textbf{(RC-1 ⭐⭐一般命题：正锥内割先验无力（唐先生 ✓）)}\ \text{设 }\lambda\ge0\ \text{（有限支撑 ✓）},\ \text{则 }\ \sum_x\lambda_x\!\!\sum_{c\in B_1(x)}\!\!f_c\ \ge\ \sum_x\lambda_x\ \text{只是原约束的正组合 ⟹ \textbf{恒被蕴含 ✗}}}$$
$$\qquad\Longrightarrow\ \boxed{\text{任何"正系数和式型"割（含全部投影割／子立方割／局部和式）×\textbf{先验上不可能改进 LP}} ✗✓\ \text{（不是算得不够，而是\textbf{信息形态被覆盖系统包含} ✓）}$$
$$\qquad\textbf{对 A4/SA 的解释 ✓}:\ \text{局部一致性约束在整层求和后正是此类 ∧ 原约束（本档 ＋ A4 档双重解释 ✓）} \Longrightarrow \text{其无力是\textbf{结构性的}，非工程量 ✗}$$
$$\qquad\textbf{有用割必须来自锥外 ✓}:\ \text{即来自 }\{\text{Boolean/整数性（}f_c^2{=}f_c\text{）}\}\ \text{或 SOS/Lasserre 二次层 ✓ —— 与"irreducible core = Boolean feasibility"一致 ✓✓}$$
$$
$$
```

## §1 实验记录（**✓**）

```
$$\text{实测（修正版 ✓）}: n{=}4,5,6,7,8:\ \text{纯 LP }3.2000/5.3333/9.1429/16.0000/28.4444 \Longrightarrow \text{加割后\textbf{完全不变}}（+0.0000 ✓），且全部 }\le K(n,1)\ ✓\ \text{（有效性核对通过 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{零杠杆 ✗}，且 (RB-1) 给出其\textbf{必然性} ✓$$
$$
$$
```

## §2 状态（**✓**）

```
$$\boxed{\text{当前锁定状态（唐先生 16:05 ✓）}:\ \boxed{\textbf{ILP RUNNING}\ +\ \textbf{projection-cut STOP}}\ ;\ \textbf{不增加任何 119 计算} ✗}$$
$$\qquad\text{ILP 若终为 UNKNOWN ⟹ 下一步\textbf{赞成}启动专用随机搜索（届时为"有明确 P2 目的的 witness search"，非"再换一个 solver" ✓）；且须先做 source-first 算法核验（目标函数／接受规则／历史 }n{=}10,R{=}1\ \text{结果是否确为 120 ✓）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：投影割正确形式与有效性核对、投影割＝covering 约束之和之证明、正锥内割先验无力之一般命题、A4/SA 无力之结构性解释
- **档案已有（引用，不列为提出）**：A4-2026-09-27、INTRELAX 系列、M-2A、21 条封口表


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 正锥内割     命中文件数=1    :: ./PROJCUT-2026-09-27-projection-cuts-are-covering-sums-structural-stop.md 
技术词 投影割        命中文件数=1    :: ./PROJCUT-2026-09-27-projection-cuts-are-covering-sums-structural-stop.md
```
- **本档新增**：投影割正确形式与有效性核对、投影割＝covering 约束之和之证明、正锥内割先验无力之一般命题、A4/SA 无力之结构性解释（见上方命中数；0 命中者为自造语／内部标签 ✓）
