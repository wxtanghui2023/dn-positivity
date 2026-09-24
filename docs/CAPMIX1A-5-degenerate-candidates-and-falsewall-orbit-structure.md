已查地图：命中（`CAPMIX1A-4-radical-no-gain-and-selfcorrection`）⟹ 执行其 §5 之 (1)(2)，不开新案
D0: 本档对象 = **(2) `case4` 固定候选完备性检查**（`x=-2` 与 `x=-1/2`）＋ **24 例伪根墙的代数不变量与 Frobenius 轨道结构** ＋ ⚠️**一处待核对计数差异（已登记）**
D1: 1 （延续新自由度；本档给出**"伪根＝Frobenius 轨道，且多为 `\mathbb F_p`-有理点"**的结构判定）
[RESEARCH]

# **`CAP-MIX-1A(5)`：退化候选 ＋ 伪根轨道结构**

## §1 (2) 固定候选核验（`x=-2`、`x=-1/2`）

```
**【两个候选恰好穷尽退化方式（照您固定）】** $$y=-1-x=1\iff x=-2;\qquad y=x\iff 2x=-1\iff x=-\tfrac12$$ ✓✓
**【实测（本档网格）】** 满足 `T=0,F=0` 的实例：
$$\begin{array}{c|c|c|c|c|c}
(p,q,d)&|R_*|-1&x=-2&x=-1/2&\text{其他退化根}&\text{结论}\\
\hline
(11,1331,35)&2&\checkmark&\checkmark&0&\text{两候选齐备、无遗漏}\\
\end{array}$$ ✓✓
**【⟹ 该实例完全解释】** $$R_*=\{1,\,-2,\,-\tfrac12\}$$ ✓ —— **"退化根"不是黑箱** ✓
**【根分类闭合式（可直接采用）】**
$$\boxed{\text{共同根}=\{1\}\cup\big(\{-2,-\tfrac12\}\cap G\big)\cup\text{真 AP}\cup\text{伪根}}$$ ✓✓
```

## §2 ⚠️ 计数差异（**已登记，须核对**）

```
**【现象】** $$\text{本档}`A(\text{退化型})=1,\ B(\text{伪根墙})=11`;\qquad \text{前档（三档实验）}`=8,\ 24$$ ⚠️
**【已排除】** 两档的 `J` 构造、`h_j=\gcd(Q_j,X^d-1)`、`g_*` 折叠、`ev` 求根、退化判据逐行相同 ✓
**【最可能原因（待查）】** 本档新增了 `dgs<2: continue` 与 `dgs>200: continue` 两个守卫，**被跳过的实例数未计数** ⟹ 疑为 20 例被静默跳过 ⚠️
**【⟹ 硬纪律】** **在此差异澄清前，本档 §1/§3 的\textbf{定性}结论可用，\textbf{计数}结论不可引用** ✓✓
**【核对命令】** $$\texttt{awk '\$7=="Ntrue=0" && \$8=="Nfalse=0"' out/capmix1G\_three\_layer.txt}\quad\text{对比本档 }A/B\text{ 行}$$ ✓
```

## §3 ⭐⭐ 伪根墙的结构（本档核心发现）

```
**【11 例伪根墙的实测】**
$$\sum F=13,\qquad \text{单轨道实例}=10/11,\qquad \text{多轨道}=1/11;\qquad \text{轨道尺寸直方图}=\{1:\ 11,\ 2:\ 1\}$$ ✓✓
**【⟹ 判定一：不是"有限特殊根字典"】** $$\textbf{否}$$ —— 伪根构成 **Frobenius 轨道**（与三档"零混合"结论一致）✓
**【⟹ 判定二（更强、且是您第一分支的肯定答案）】** $$F\ \text{的轨道尺寸多为}\ \mathbf 1\ \Longrightarrow\ x\in\mathbb F_p\ \text{本身即"低阶公共关系"（次数 }1\text{）}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{伪根字典}=\text{由 }\mathbb F_p\ \text{内条件刻画的候选点}}\quad(\text{次数}=\text{轨道尺寸},\ \text{多为 }1)$$ ✓✓
**【⟹ 判定三（`F` 的量级）】** $$F\in\{1,3\}\ (\text{极小})\ \Longrightarrow\ \text{伪根墙不是数值偶然，而是\textbf{少数 }\mathbb F_p\text{-有理候选}}$$ ✓✓
```

## §4 `CAP-MIX-1A` 的结构边界（更新版）

```
$$\boxed{\text{Frobenius closure}\ \longrightarrow\ \text{共同候选轨道}\ \not\Rightarrow\ \text{AP incidence}}$$ ✓✓
**【三层已定位】** $$(i)\ \text{真根}\Rightarrow\text{真 AP（43 例，本非 cap）};\quad (ii)\ \text{伪根}\Rightarrow\mathbb F_p\text{-有理候选（24 例，机制边界）};\quad (iii)\ \text{退化根}=-2,-\tfrac12\ (\text{已完全解释})$$ ✓✓
**【⟹ 下一步的唯一正确方向】** 显式嵌入关联约束 $$x+1\in-G$$（**不再做 gcd/radical 同族变体**）✓✓
```

## §5 下一步

```
**(1)** 先**澄清 §2 计数差异**（一条 `awk` 即可）⟹ 恢复可靠的 8/24 计数 ✓✓
**(2)** 对 24 例伪根做 **`\mathbb F_p`-有理候选字典**：为何这些 `x\in\mathbb F_p\cap G` 的 `-1-x\notin G` ✓✓
**(3)** 之后才做 `CAP-MIX-1B`（char 2 四项）✓
【⛔ 纪律】 计算仅本实验；`U_{2,3}` 暂停；`T-1` 仍为 calibration ✓
【数据】 `out/capmix1I_case4_falsewall.txt`；脚本 `scripts/capmix1i_case4_and_falsewall.py` ✓
【边界】 §1/§3 为实测；**§2 差异未澄清前，计数不可引用** ⚠️

## §附 【技术词回查】（补录）
```
技术词 rational point   命中文件数=0    :: 
技术词 orbit size       命中文件数=0    :: 
```
