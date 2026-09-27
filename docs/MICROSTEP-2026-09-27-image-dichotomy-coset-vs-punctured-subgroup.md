已查地图：已跑 scripts/prework_map_check.sh Φ 像 陪集 穿孔子群 微步 ⟹ 执行自 `YI-2026-09-27-...`（✓）＋ 唐先生 14:12（选 (i)，gate 固定 ✓）；本档 = **(i) 同语言分解：机制 SUPPORTED ✓，两因素拆开 ✓**。
D0: 本档对象 = n=8 三见证码与 n=16 对照的 Φ-像结构
D1: 3（**(i) 判定：机制支持 ✓（像的形态二分 ✓）**；**两因素拆开 ✓**；**(甲) 靶点再精确化 ✓**）

# (i) 同语言分解：Φ-像二分（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CI-1 ⭐机制 SUPPORTED ✓)}\ \Phi:=\sigma_{n-1}\ \text{限于第二半码};\ \text{标签群 }G=\mathbb F_2^{m}\ (n{=}8{:}G{=}\mathbb F_2^3,\ n{=}16{:}G{=}\mathbb F_2^4\ ✓) \Longrightarrow \textbf{像的形态二分 ✓✓}:}$$
$$\qquad\begin{array}{c|c|c|c|c}
\text{对象} & |G| & |\mathrm{im}\,\Phi| & \mathrm{im}\,\Phi\cup\{0\}\ \text{是子群?} & \text{纤维谱}\\
\hline
n{=}8,\ J_7{=}64 & 8 & 4 & \textbf{否} ✗（\text{陪集}） & \{4{:}4\}\\
n{=}8,\ J_7{=}128 & 8 & 2 & \textbf{否} ✗（\text{陪集}） & \{8{:}2\}\\
n{=}8,\ J_7{=}256 & 8 & 1 & \text{是（平凡 2 元）} & \{16{:}1\}\\
n{=}16,\ \lambda{=}\mathbf 1\ (s{=}9) & 16 & 8 & \textbf{是 ✓}（8 元 $=V$） & \{288{:}4,\ 224{:}4\}\\
n{=}16,\ \lambda{=}r\ (s{=}16) & 16 & 4 & \textbf{是 ✓}（4 元） & \{512{:}4\}\\
\end{array}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{n=16：像 = \textbf{穿孔子群 }H\setminus\{0\}}\ (H{=}V,\ 8\ \text{元}\ ✓);\qquad \textbf{n=8：像 = \textbf{陪集}（}0\notin\mathrm{im}\ ✓\text{，大小 }1/2/4\ \text{自由}）}$$
$$\boxed{\textbf{(CI-2 ⭐两因素拆开 ✓)}\ \text{因素①\textbf{集中形态}}:\ \text{像是否闭成子群（"穿孔子群"形 ✓）};\quad \text{因素②\textbf{纤维均匀}}:\ \text{纤维是否在稳定子陪集上恒定}}$$
$$\qquad n{=}16:\ \text{① 成立 ✓（像 }=\text{穿孔子群 }V\setminus\{0\}\ ✓\text{）};\ \text{② 成立 ✓（}W\text{-陪集常值 ✓）} \Longrightarrow J\ \text{被 }(A_1,A_2)\ \text{钉住 ✓}$$
$$\qquad n{=}8:\ \text{① \textbf{失败} ✗（像是陪集，非穿孔子群；大小 }1{/}2{/}4\ \text{自由 ⟹ 支撑形状自由 ⟹ }J\ \text{分叉 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{第一处失去强制 = 因素①（像的封闭形态）} ✓\ \text{—— 与乙-2 的"陪集常值"定位一致且更精确 ✓✓}$$
$$\boxed{\textbf{(CI-3 ⭐(甲) 靶点再精确化 ✓)}\ \text{ENP1CC puncturing 的目标}:\ \boxed{\text{刻意破坏"像 }=\text{穿孔子群"形态（或破坏纤维在稳定子陪集上的均匀性），同时保留两个完美半码与 }(A_1,A_2)\ \text{桶}}\ ✓}$$
$$\qquad\textbf{可测前置 ✓}:\ \text{对候选先算 }(\mathrm{im}\,\Phi,\ \text{纤维谱})\ \text{并与 }V\setminus\{0\}\ \text{形态对照};\ \text{不入形者优先 ✓}$$
$$
$$
```

---

## §1 原始记录（**✓ 本机生成与计算**）

```
$$\text{n=8 见证（新生成，桶 }(A_1,A_2)=(0,16)\ ✓\text{）}:\ q\ \text{形状}=(4{\times}4)/(2{\times}8)/(1{\times}16)\ ✓\ \text{（与 P12-PASS 记录一致 ✓）}$$
$$\qquad J_7{=}64:\ q=[4,4,0,0,4,4,0]\ ✓;\quad J_7{=}128:\ q=[0,0,0,0,0,8,8]\ ✓;\quad J_7{=}256:\ q=[0,\dots,0,16]\ ✓$$
$$\text{n=16 对照}:\ \lambda{=}\mathbf 1\ \Longrightarrow\ \mathrm{im}\,\Phi\cup\{0\}=V\ (\text{8 元子群 }\mathrm{span}\{2,4,9\}\ ✓);\ \text{纤维 }\{288{\times}4,\ 224{\times}4\}\ ✓$$
$$
$$
```

---

## §2 判定与下一步（**✓**）

```
$$\textbf{(i) 判定 ✓}:\ \boxed{\text{机制 SUPPORTED（不是"确认定理" ⚠️）}} \Longrightarrow \textbf{PASS → 转 (甲)} ✓\ \text{（按唐先生 gate ✓）}$$
$$\textbf{诚实边界 ⚠️}:\ \text{"为何 }n{=}16\ \text{必然给穿孔子群形态"尚未证明（现为观测二分 ✓）};\ \text{但靶点已被实证支持 ✓}$$
$$\textbf{下一步}:\ \text{(甲) ENP1CC puncturing（前置指标 }=\mathrm{im}\,\Phi\ \text{形态 ＋ 纤维谱 ✓）};\ \text{(乙) 不再继续猜 ✓（按唐先生 ✓）};\ \text{119：完全不碰 ✓}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\Phi$-像的形态二分（陪集 vs 穿孔子群）、两因素拆开（集中形态 ＋ 纤维均匀）、(甲) 靶点再精确化
- **档案已有（引用，不列为提出）**：A-YI-1、P12-PASS、A-SUBSPACE-1、A-CLOSEDFORM-1、内蕴 $\nu$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 形态二分     命中文件数=2    :: ./MICROSTEP-2026-09-27-image-dichotomy-coset-vs-punctured-subgroup.md ./M4-C6-REFINAL-gate-pass-order-TESTABLE1-then-F1-F8-then-endpoint.md 
技术词 穿孔子群     命中文件数=1    :: ./MICROSTEP-2026-09-27-image-dichotomy-coset-vs-punctured-subgroup.md
```
- **本档新增**：$\Phi$-像的形态二分（陪集 vs 穿孔子群）、两因素拆开（集中形态 ＋ 纤维均匀）、(甲) 靶点再精确化（见上方命中数；0 命中者为自造语／内部标签 ✓）
